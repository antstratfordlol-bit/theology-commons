#!/usr/bin/env python3
"""pdf2md.py: convert a PDF to clean Markdown with the book's own page numbers
and real Markdown footnotes.

Page numbers
    Taken from the PDF's embedded page labels (i, ii, ... 1, 2, ...) when present.
    Otherwise the script reads the printed page numbers (folios) at the top or
    bottom of the pages and works out the offset itself. You can always force it
    with --offset N, where N is the PDF page on which printed page 1 falls.

Footnotes
    The footnote area of each page is found by type size and position, removed
    from the body, and rebuilt as Markdown footnotes:

        ... as Lord.[^c01-49]                 (in the text)
        [^c01-49]: The idea is thematic ...   (under the page it starts on)

    Ids are "c<sequence>-<note number>"; the sequence goes up each time the
    book's note numbering restarts at 1. A note that runs over onto the next
    page is completed on the page where it begins.

Cleaning
    Running heads and page numbers at the top of pages are removed. Words split
    across a line or page break are rejoined. Small-caps headings that come out
    with scrambled capitals (introduCtion) are repaired and set in title case.

Usage
    python pdf2md.py book.pdf
    python pdf2md.py book.pdf --pages 60-65      # test a few pages first
    python pdf2md.py book.pdf --offset 15        # force the page offset
"""
import argparse
import re
import statistics
import unicodedata
from collections import Counter
from pathlib import Path

import pymupdf
import pymupdf4llm

# ----------------------------------------------------------------- page labels


LIGATURES = str.maketrans({"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi", "\ufb04": "ffl",
                           "\ufb05": "st", "\ufb06": "st"})


def roman(n: int) -> str:
    out = ""
    for v, s in [(10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]:
        while n >= v:
            out += s
            n -= v
    return out


def detect_offset(doc):
    """Work out the PDF page on which printed page 1 falls, from the page
    numbers printed at the top or bottom of the pages."""
    deltas = Counter()
    for i in range(len(doc)):
        pg = doc[i]
        H = pg.rect.height
        for l in read_lines(pg):
            y = l["bbox"][1]
            if not (y < 0.1 * H or y > 0.8 * H):
                continue
            t = l["text"].replace(" ", " ").strip()
            m = (re.fullmatch(r"(\d{1,4})", t) or re.match(r"(\d{1,4})\s+\D", t)
                 or re.search(r"\D\s+(\d{1,4})$", t))
            if m:
                deltas[(i + 1) - int(m.group(1))] += 1
    if not deltas:
        return None
    delta, count = deltas.most_common(1)[0]
    return delta + 1 if count >= max(8, len(doc) // 25) else None


def page_labels(doc, offset, roman_front):
    n = len(doc)
    labels = [doc[i].get_label() for i in range(n)]
    if offset is None:
        if any(labels):
            return [l or f"PDF {i + 1}" for i, l in enumerate(labels)], None
        offset = detect_offset(doc)
        if offset is None:
            raise SystemExit("This PDF has no embedded page labels and the printed page numbers "
                             "could not be read; rerun with --offset N.")
        note = f"Detected page offset {offset} (printed page 1 = PDF page {offset}); override with --offset N."
    else:
        note = None
    out = []
    for i in range(n):
        printed = i + 1 - offset + 1
        if printed >= 1:
            out.append(str(printed))
        elif roman_front:
            out.append(roman(i + 1))
        else:
            out.append(f"PDF {i + 1}")
    return out, note


def front_roman_labels(doc, labels):
    """Front-matter pages carry roman numerals in their running heads or feet
    (v, vi, vii ...). Use them as the page labels where they can be read."""
    out = list(labels)
    for i, lab in enumerate(labels):
        if not lab.startswith("PDF "):
            continue
        pg = doc[i]
        H = pg.rect.height
        for l in read_lines(pg):
            y = l["bbox"][1]
            if not (y < 0.1 * H or y > 0.8 * H):
                continue
            t = l["text"].replace("\u2003", " ").strip()
            m = re.fullmatch(r"([ivxlc]{1,7})", t) or re.match(r"([ivxlc]{1,7})\s+\S", t) \
                or re.search(r"\S\s+([ivxlc]{1,7})$", t)
            if m:
                out[i] = m.group(1)
                break
    def rv(r):
        vals = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100}
        tot = 0
        for a, b in zip(r, r[1:] + " "):
            tot += -vals[a] if b != " " and vals[a] < vals[b] else vals[a]
        return tot

    nxt = None                                  # (value, index) of the next numbered page
    for i in range(len(out) - 1, -1, -1):
        if re.fullmatch(r"[ivxlc]+", out[i]):
            nxt = (rv(out[i]), i)
        elif out[i].startswith("PDF ") and nxt:
            v = nxt[0] - (nxt[1] - i)
            if 1 <= v < 40:
                out[i] = roman(v)
        elif not out[i].startswith("PDF "):
            nxt = None
    return out


# ------------------------------------------------------- page reading

NOTE_START = re.compile(r"^\s*(\d{1,3})(?:\.\s*|\s+(?=[^\d\s]))")
SMALL = 9.2  # footnote type is smaller than this; set from the book itself in main()


def detect_small_threshold(doc, idx):
    """Footnote type is clearly smaller than the body type; body type is the
    commonest size in the book."""
    c = Counter()
    step = max(1, len(idx) // 60)
    for pno in idx[::step]:
        for b in doc[pno].get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    c[round(s["size"], 1)] += len(s["text"].strip())
    body = c.most_common(1)[0][0] if c else 11.0
    return body * 0.9, body


def _dominant_size(spans):
    c = Counter()
    for s in spans:
        c[round(s["size"], 1)] += len(s["text"].strip()) or 1
    return c.most_common(1)[0][0]


def _style(span):
    f = span["font"].lower()
    return ("italic" in f or "oblique" in f or span["flags"] & 2 != 0, "bold" in f or span["flags"] & 16 != 0)


def read_lines(page):
    out = []
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            spans = [s for s in l["spans"] if s["text"] != ""]
            if not spans:
                continue
            out.append({
                "bbox": l["bbox"], "spans": spans, "dom": _dominant_size(spans),
                "text": "".join(s["text"] for s in spans),
            })
    out.sort(key=lambda l: l["bbox"][1])
    rows, cur = [], []
    for l in out:
        if cur and l["bbox"][1] - cur[0]["bbox"][1] > 3:
            rows.append(cur)
            cur = []
        cur.append(l)
    if cur:
        rows.append(cur)
    return [l for r in rows for l in sorted(r, key=lambda l: l["bbox"][0])]


def letters_key(text):
    return re.sub(r"[^a-zà-ɏ]+", "", text.lower())


def find_header_rects(doc, idx):
    """Running heads and page numbers at the top of the pages: lines in the top
    tenth of the page that are a bare page number, or whose text (ignoring the
    changing page number) repeats on several pages."""
    per, keys = {}, Counter()
    for pno in idx:
        pg = doc[pno]
        H = pg.rect.height
        ls = [l for l in read_lines(pg) if l["bbox"][1] < 0.1 * H and len(l["text"].strip()) < 100]
        per[pno] = ls
        for k in {letters_key(l["text"]) for l in ls if letters_key(l["text"])}:
            keys[k] += 1
    rects = {}
    for pno, ls in per.items():
        rs = []
        for l in ls:
            t = l["text"].replace(" ", " ").strip()
            k = letters_key(t)
            folio = re.fullmatch(r"\d{1,4}|[ivxlc]{1,7}|[IVXLC]{1,7}", t)
            in_margin = l["bbox"][1] < 0.07 * doc[pno].rect.height
            numbered = in_margin and len(t.split()) <= 9 and (
                re.match(r"(\d{1,4}|[ivxlc]{1,7})\s+\D", t) or re.search(r"\D\s+(\d{1,4}|[ivxlc]{1,7})$", t))
            if folio or numbered or (k and keys[k] >= 4):
                x0, y0, x1, y1 = l["bbox"]
                rs.append(pymupdf.Rect(x0 - 1, y0 - 1, x1 + 1, y1 + 1))
        for l in read_lines(doc[pno]):                     # stray one-letter marks at the page edges
            t = l["text"].strip()
            if len(t) == 1 and t.isalpha() and (l["bbox"][1] < 0.1 * doc[pno].rect.height
                                                or l["bbox"][1] > 0.85 * doc[pno].rect.height):
                x0, y0, x1, y1 = l["bbox"]
                rs.append(pymupdf.Rect(x0 - 1, y0 - 1, x1 + 1, y1 + 1))
        rects[pno] = rs
    return rects


def footnote_region(page, lines):
    """Index of the first footnote line, or None. The footnote area is a run of
    small-type lines at the bottom of the page (a bare folio may follow it)."""
    H = page.rect.height

    def ignorable(l):
        # a bare folio, or a short running head / footer in the top or bottom
        # margin (these sit below the footnotes on some books and get stripped anyway)
        t = l["text"].strip()
        y = l["bbox"][1]
        if re.fullmatch(r"(\d+|[A-Za-z])", t) and y > 0.8 * H:
            return True
        return (y > 0.87 * H or y < 0.12 * H) and len(t) < 60

    for s, l in enumerate(lines):
        if l["bbox"][1] < 0.12 * H or l["dom"] > SMALL:
            continue
        if all(m["dom"] <= SMALL or ignorable(m) for m in lines[s:]):
            return s
    return None


def render_pieces(pieces):
    """pieces: [(text, italic, bold)] -> Markdown with _italic_ and **bold**."""
    pieces = list(pieces)
    for i in range(1, len(pieces) - 1):
        t, it, bd = pieces[i]
        if t.strip() == "" and pieces[i - 1][1:] == pieces[i + 1][1:] and (pieces[i - 1][1] or pieces[i - 1][2]):
            pieces[i] = (t, pieces[i - 1][1], pieces[i - 1][2])
    merged = []
    for t, it, bd in pieces:
        if t == "":
            continue
        if merged and tuple(merged[-1][1:]) == (it, bd):
            merged[-1][0] += t
        else:
            merged.append([t, it, bd])
    out = ""
    for t, it, bd in merged:
        core = t.strip()
        if not core:
            out += t
            continue
        lead, trail = t[: len(t) - len(t.lstrip())], t[len(t.rstrip()):]
        if bd:
            core = f"**{core}**"
        if it:
            core = f"_{core}_"
        out += lead + core + trail
    out = out.replace("\xad", "")
    out = re.sub(r"[ \t]+", " ", out)
    out = re.sub(r"(?<=[_*]) (?=[.,;:!?)”’])", "", out)
    return out.strip()


# ------------------------------------------------------ footnote analysis


class NoteState:
    def __init__(self):
        self.prev = 0
        self.chapter = 1
        self.notes = {}      # id -> list of pieces
        self.last_id = None
        self.last_pno = None
        self.warnings = []


def char_markers(page, y_min, y_end, head_rects):
    """Markers that are digits *inside* a text line, set a little off the
    baseline (the way some publishers typeset note numbers)."""
    rows = []
    for b in page.get_text("rawdict")["blocks"]:
        for l in b.get("lines", []):
            chars = [c for s in l["spans"] for c in s["chars"]]
            if chars:
                rows.append((l["bbox"], chars))
    rows.sort(key=lambda r: r[0][1])
    grouped, cur = [], []
    for r in rows:
        if cur and r[0][1] - cur[0][0][1] > 3:
            grouped.append(cur)
            cur = []
        cur.append(r)
    if cur:
        grouped.append(cur)
    rows = [r for g in grouped for r in sorted(g, key=lambda r: r[0][0])]
    out = []
    for ri, (bbox, chars) in enumerate(rows):
        if bbox[1] < y_min or bbox[1] >= y_end:
            continue
        if any(r.intersects(pymupdf.Rect(bbox)) for r in head_rects):
            continue
        letters = [c["origin"][1] for c in chars if c["c"].isalpha()]
        if len(letters) >= 2:
            base = statistics.median(letters)
        else:   # e.g. a line that only holds the end of a citation: use the commonest height
            allc = [c["origin"][1] for c in chars if not c["c"].isspace()]
            if len(allc) < 4:
                continue
            base = statistics.median(allc)
        i = 0
        while i < len(chars):
            if not chars[i]["c"].isdigit():
                i += 1
                continue
            j = i
            while j < len(chars) and chars[j]["c"].isdigit():
                j += 1
            run = chars[i:j]
            if len(run) <= 3 and all(abs(c["origin"][1] - base) >= 0.4 for c in run):
                ctx = "".join(c["c"] for c in chars[:i])
                if len(re.sub(r"\s", "", ctx)) < 6 and ri > 0:
                    prev = "".join(c["c"] for c in rows[ri - 1][1]).rstrip()
                    ctx = re.sub(r"[-\xad]$", "", prev) + ctx
                out.append({"n": int("".join(c["c"] for c in run)), "ctx": ctx,
                            "pos": (round(bbox[1]), round(run[0]["origin"][0]))})
            i = j
    return out


def slice_line(l, a, b):
    """The part of a line between character offsets a and b, as a line."""
    spans, pos = [], 0
    for sp in l["spans"]:
        t = sp["text"]
        lo, hi = max(a, pos), min(b if b is not None else 10**9, pos + len(t))
        if lo < hi:
            spans.append({**sp, "text": t[lo - pos:hi - pos]})
        pos += len(t)
    return {**l, "spans": spans, "text": "".join(x["text"] for x in spans)}


def analyze_page(pno, page, st: NoteState, head_rects):
    """Return (fn_rect or None, [(note_id, number)], markers) for one page.
    Footnote pieces are accumulated in st.notes."""
    lines = read_lines(page)
    s = footnote_region(page, lines)
    if s is None:
        return None, [], []
    H = page.rect.height
    head_y = 0.07 * H
    fn_lines = [l for l in lines[s:] if l["dom"] <= SMALL]
    body_lines = [l for l in lines[:s]
                  if l["bbox"][1] >= head_y and not any(r.intersects(pymupdf.Rect(l["bbox"])) for r in head_rects)]

    # ---- find the in-text markers
    cands = []
    for li, l in enumerate(body_lines):
        sp = l["spans"]
        for j, s_ in enumerate(sp):
            t = s_["text"].strip()
            if not re.fullmatch(r"\d{1,3}", t):
                continue
            if j > 0:
                if s_["size"] > sp[j - 1]["size"] + 0.05:
                    continue
            elif s_["size"] > 10.2:
                continue
            ctx = "".join(x["text"] for x in sp[:j])
            if len(re.sub(r"\s", "", ctx)) < 6 and li > 0:
                prev = "".join(x["text"] for x in body_lines[li - 1]["spans"]).rstrip()
                ctx = re.sub(r"[-\xad]$", "", prev) + ctx
            cands.append({"n": int(t), "ctx": ctx, "pos": (round(l["bbox"][1]), round(s_["origin"][0]))})
    y_end = fn_lines[0]["bbox"][1] if fn_lines else H
    for c in char_markers(page, head_y, y_end, head_rects):
        if not any(c["n"] == o["n"] and abs(c["pos"][0] - o["pos"][0]) <= 2 for o in cands):
            cands.append(c)
    starts0 = [int(m_.group(1)) for m_ in (NOTE_START.match(l["text"]) for l in fn_lines) if m_]

    # ---- inline markers at body size, glued to the text ("...work.29 If one...").
    # Some books set the reference number in ordinary type rather than as a
    # superscript, so it is neither a small span nor off the baseline. When the
    # footnote numbers at the foot of the page are not otherwise accounted for,
    # look for each of them inline, in order, right after a letter or closing
    # punctuation and before a space or line end (never inside a year, page
    # range or scripture reference).
    have = {c["n"] for c in cands}
    want = [n for n in starts0 if n not in have]
    if want:
        search_from = 0
        for li, l in enumerate(body_lines):
            txt = "".join(x["text"] for x in l["spans"])
            for mm in re.finditer(r"(?<=[A-Za-z.,;:!?)\]”’\"'])(\d{1,3})(?=[ \t]|$|[)\]”’\"'.,;])", txt):
                n = int(mm.group(1))
                if n not in want:
                    continue
                # keep markers in increasing order
                if cands and n <= max(c["n"] for c in cands):
                    continue
                ctx = txt[:mm.start(1)]
                if len(re.sub(r"\s", "", ctx)) < 6 and li > 0:
                    prev = "".join(x["text"] for x in body_lines[li - 1]["spans"]).rstrip()
                    ctx = re.sub(r"[-\xad]$", "", prev) + ctx
                cands.append({"n": n, "ctx": ctx,
                              "pos": (round(l["bbox"][1]), round(l["spans"][0]["origin"][0]))})
                want.remove(n)

    cands.sort(key=lambda c: c["pos"])
    avail = Counter(c_["n"] for c_ in cands)

    starts = starts0
    continues = st.last_id is not None and st.last_pno == pno - 1
    real_body = [l for l in body_lines if l["dom"] > SMALL]
    follows = st.prev > 0 and (st.prev + 1) in starts and len(real_body) >= 3
    if not (any(avail[n_] for n_ in starts) or continues or follows):
        st.warnings.append(f"PDF p. {pno + 1}: small type at the bottom has no matching in-text marker; kept as body text")
        return None, [], []
    st.last_pno = pno

    # ---- build the notes
    page_notes = []   # (id, number) of notes that START on this page
    cur = None
    queue = list(fn_lines)
    while queue:
        l = queue.pop(0)
        # two notes can share one text line ("...12, 38.62. Ibid."): split before the next number
        m0 = NOTE_START.match(l["text"])
        own = int(m0.group(1)) if (m0 and (avail[int(m0.group(1))] > 0 or int(m0.group(1)) == st.prev + 1)) else st.prev
        for mm in re.finditer(r"(?<=[.?!)\]”’])\s*(\d{1,3})\.\s+(?=\S)", l["text"]):
            if mm.start(1) > 0 and int(mm.group(1)) == own + 1 and avail[own + 1] > 0:
                queue.insert(0, slice_line(l, mm.start(1), None))
                l = slice_line(l, 0, mm.start(1))
                break
        spans = l["spans"]
        m = NOTE_START.match(l["text"])
        is_new = False
        if m:
            n = int(m.group(1))
            # a numbered line starts a new note if the page has a matching marker
            # for it, or if it simply follows on from the previous note number
            # (this keeps numbered lists *inside* a note from being split off)
            if avail[n] > 0:
                is_new = True
                avail[n] -= 1
            elif n == st.prev + 1 or (st.prev == 0 and not page_notes):
                is_new = True
        if is_new:
            if n == 1 and st.prev >= 1:
                st.chapter += 1
            st.prev = n
            nid = f"c{st.chapter:02d}-{n}"
            if nid in st.notes:
                st.warnings.append(f"PDF p. {pno + 1}: duplicate note id {nid}; renamed")
                k_ = 2
                while f"{nid}x{k_}" in st.notes:
                    k_ += 1
                nid = f"{nid}x{k_}"
            cur = nid
            st.last_id = nid
            st.notes[nid] = []
            page_notes.append((nid, n))
            pieces, skip = [], m.end()
            for sp in spans:
                t = sp["text"]
                if skip >= len(t):
                    skip -= len(t)
                    continue
                pieces.append((t[skip:], *_style(sp)))
                skip = 0
        else:
            pieces = [(sp["text"], *_style(sp)) for sp in spans]
            if cur is None:           # continuation of the previous page's last note
                cur = st.last_id
                if cur is None:
                    st.warnings.append(f"PDF p. {pno + 1}: continuation text with no note to attach to")
                    continue
        buf = st.notes[cur]
        if buf:
            tail = "".join(p_[0] for p_ in buf[-3:])
            first_t = pieces[0][0] if pieces else ""
            if re.search(r"[A-Za-zÀ-ɏ]-$", tail) and re.match(r"[a-zß-ÿ]", first_t):
                t0, i0, b0 = buf[-1]
                if t0[:-1]:
                    buf[-1] = (t0[:-1], i0, b0)
                else:
                    buf.pop()
            elif not tail.endswith(" ") and not first_t.startswith(" "):
                buf.append((" ", False, False))
        buf.extend(pieces)

    markers, k = [], 0
    for nid, n in page_notes:
        found = None
        for ci in range(k, len(cands)):
            if cands[ci]["n"] == n:
                found, k = cands[ci], ci + 1
                break
        if found is None:
            for c in cands:
                if c["n"] == n and c not in [x[1] for x in markers]:
                    found = c
                    break
        if found is None:
            st.warnings.append(f"PDF p. {pno + 1}: no in-text marker found for note {n}")
        else:
            markers.append((nid, found))

    x0 = min(l["bbox"][0] for l in fn_lines) - 2
    x1 = max(l["bbox"][2] for l in fn_lines) + 2
    y0 = min(l["bbox"][1] for l in fn_lines) - 0.5
    y1 = max(l["bbox"][3] for l in fn_lines) + 0.5
    return pymupdf.Rect(x0, y0, x1, y1), page_notes, markers


# ---------------------------------------------------------- body cleanup


def blocks(text):
    return [b for b in re.split(r"\n\s*\n", text.replace("\xad", "").strip()) if b.strip()]


def norm(b):
    return re.sub(r"\s+", " ", b).strip()


def is_folio(b, label):
    return norm(b).strip("*# ").lower() == label.lower()


def find_running_heads(all_blocks):
    """Backup for running heads the geometric pass missed: short blocks at the
    top of the page that repeat once the changing page number is ignored."""
    c = Counter()
    for bl in all_blocks:
        for b in bl[:2]:
            n = norm(b)
            if len(n) < 90 and not n.startswith(("#", ">")):
                k = letters_key(n)
                if k:
                    c[k] += 1
    return {k for k, v in c.items() if v >= 4}


def strip_edges(bl, label, heads):
    for _ in range(2):
        if bl and (is_folio(bl[0], label) or (len(norm(bl[0])) < 90 and not bl[0].startswith(("#", ">"))
                                               and letters_key(bl[0]) in heads)):
            bl = bl[1:]
    if bl and is_folio(bl[-1], label):
        bl = bl[:-1]
    return bl


def tidy(text):
    text = re.sub(r"(?<=\S)[ ]{2,}(?=\S)", " ", text)           # double spaces
    text = re.sub(r"(?<=[_*]) (?=[.,;:!?)”’])", "", text)         # "_Title_ ."
    text = re.sub(r"_<br>_", "<br>", text)                         # "_a_<br>_b_"
    text = re.sub(r"(?<=[^\s_])_ _(?=[^\s_])", " ", text)           # "_a_ _b_" -> "_a b_"
    text = re.sub(r"\b(anti|semi|mid|post|pre|pro|neo|non|quasi|self|ex|inter|intra|ultra|sub|super|pan|proto|"
                  r"pseudo|half|first|second|third|well|ill|old|new|co)([A-Z][a-z]{2,})", r"\1-\2", text)   # antiChristian
    text = re.sub(r"([“‘(]) +", r"\1", text)                       # "“ word"
    text = re.sub(r" +([”’)])", r"\1", text)                       # "word ”"
    return text


def place_markers(text, markers, warnings, pno):
    """Replace the bare marker digits in the body Markdown with [^id]."""
    pos = 0
    for nid, c in sorted(markers, key=lambda x: x[1]["pos"]):
        full = re.sub(r"[\s_*\xad]", "", c["ctx"].translate(LIGATURES))
        n = str(c["n"])
        ref = f"[^{nid}]"
        m = None
        for take in (8, 5, 3):
            ctx = full[-take:]
            if not ctx:
                continue
            pat = r"[\s_*\xad]*".join(re.escape(ch) for ch in ctx) + r"[\s_*\xad]*(?:<sup>\s*)?(" + n + r")(?!\d)"
            m = re.compile(pat).search(text, pos) or (re.compile(pat).search(text, 0) if pos else None)
            if m:
                break
        if not m:  # last resort: digits glued to the preceding character, not inside a citation
            m = re.compile(r"(?<=[^\s\d\[>])(?<!\d:)(?<!\d–)(?<!\d-)(" + n + r")(?![\d\]:–])").search(text, pos)
            if m:
                warnings.append(f"PDF p. {pno + 1}: marker for note {n} placed by fallback; please check")
        if not m:
            warnings.append(f"PDF p. {pno + 1}: could not place marker for note {n} in the text")
            continue
        text = text[: m.start(1)] + ref + text[m.end(1):]
        pos = m.start(1) + len(ref)
    return re.sub(r"<sup>\s*(\[\^[^\]]+\])\s*</sup>(?:[ \t]+(?=[.,;:!?)”’]))?", r"\1", text)


# ------------------------------------------- small-caps heading repair

MINOR = set("a an the and but or nor for so yet as at by in of off on per to up via with among between "
            "according against from into over under upon onto than vs".split())
SEP = re.compile(r"(\s+|<br>|\|)")


def _core(tok):
    return re.sub(r"[^A-Za-z]", "", tok)


def _irregular(tok):
    c = _core(tok)
    return len(c) >= 3 and re.search(r"[a-z][A-Z]", c) is not None and not re.match(r"(Mc|Mac)[A-Z]", c)


def build_vocab(pages):
    c = Counter()
    for bl in pages:
        for b in bl:
            if b.startswith(("[^", "#", "|")):
                continue
            for w in re.findall(r"[A-Za-z]{2,}", b):
                if w.islower() or (w[0].isupper() and w[1:].islower()):
                    c[w.lower()] += 1
    return {w for w, k in c.items() if k >= 2}


def repair_line(line, vocab):
    """Small-caps text is stored in the PDF in a way that scrambles capitals and
    letter-spaces words ('introduCt ion'). Repair such lines and set them in
    title case. Ordinary lines are left alone."""
    s = line.lstrip()
    if not s or s.startswith(("[^", ">", "<!--", "**[p.")):
        return line
    parts = SEP.split(line)                    # even = tokens, odd = separators
    toks = [t for t in parts[::2] if _core(t)]
    if not toks:
        return line
    is_head = s.startswith(("#", "|"))
    irr = [t for t in toks if _irregular(t)]
    garbled = [t for t in irr if _core(t).lower() in vocab]
    if not (garbled or (is_head and len(irr) >= 2)):
        return line
    if not (is_head or (len(toks) <= 14 and len(line) < 110)):
        return line

    # 1. rejoin letter-spaced fragments ("introduct ion", "s ituating")
    k = 0
    while k + 2 < len(parts):
        a, sep, b = parts[k], parts[k + 1], parts[k + 2]
        mb = re.fullmatch(r"([A-Za-z]+)([,;:.!?]*)", b or "-")
        if sep == " " and re.fullmatch(r"[A-Za-z]+", a or "-") and mb:
            la, lb = a.lower(), mb.group(1).lower()
            if ((la + lb) in vocab and (la not in vocab or lb not in vocab)) or \
               (len(la) == 1 and la not in "ai" and len(lb) >= 3):
                parts[k:k + 3] = [a + b]
                continue
        k += 2

    # 2. repair capitals and set in title case
    start = True
    for k in range(0, len(parts), 2):
        t = parts[k]
        core = _core(t)
        if not core:
            if t.rstrip().endswith((":", ".")):
                start = True
            continue
        if _irregular(t):
            t = t.lower()
        if re.search(r"\d", t) or (len(core) >= 2 and core.isupper()):
            pass
        elif core.lower() in MINOR and not start:
            t = t.lower()
        else:
            i = next(i for i, ch in enumerate(t) if ch.isalpha())
            t = t[:i] + t[i].upper() + t[i + 1:]
        parts[k] = t
        start = t.rstrip().endswith((":", "."))
    return "".join(parts)


# ------------------------------------------- headings, contents, front matter

HEAD = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
PART = re.compile(r"^Part\s+(\d+|[IVX]+)[.:]?\s+(\S.{0,85})$")


def _plain(t):
    t = re.sub(r"\*\*|__|(?<!\w)_|_(?!\w)", "", t)
    return re.sub(r"\s+", " ", t).strip()


def _wants_merge(a, b):
    """Is heading b the second line of a title that began in heading a?"""
    if re.search(r"[.?!]$", a):
        return False
    last = re.sub(r"[^A-Za-z’']", "", a.split()[-1]).lower() if a.split() else ""
    return (len(a) >= 30 or a.endswith((",", ":", "-")) or last in MINOR or a.endswith(("’s", "'s"))
            or b[:1].islower() or b.split()[0].lower() in MINOR)


def _toc_or_list(block):
    """Turn a (header-less) Markdown table into a list: contents pages become
    'Title (p. N)', two-column glossaries become '**Term**: meaning'."""
    rows = []
    for ln in block.split("\n"):
        inner = ln.strip()
        inner = inner[1:] if inner.startswith("|") else inner
        inner = inner[:-1] if inner.endswith("|") else inner
        cells = [c.strip() for c in inner.split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue
        rows.append([c.replace("<br>", " ") for c in cells])
    if not rows or any(len(r) != 2 for r in rows):
        return block
    pagey = sum(1 for r in rows if re.fullmatch(r"[\divxlc]*", r[1]))
    out = []
    if pagey == len(rows):                                  # contents
        for a, b in rows:
            a = _plain(a)
            if not b and PART.match(a):
                out.append(f"\n**{a}**\n")
            else:
                a = re.sub(r"^(\d{1,2})\.\s", r"\1\\. ", a)      # "1\. Title": not a nested list
                out.append(f"- {a} (p. {b})" if b else f"- {a}")
    else:                                                   # glossary of abbreviations
        for a, b in rows:
            out.append(f"- **{_plain(a)}**: {b}")
    return "\n".join(out).strip("\n")



NUMWORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7}


def _toks(t):
    return re.findall(r"\w+", _plain(re.sub(r"^#+\s*", "", t)).lower())


def contents_titles(pages):
    """Read chapter and part titles from the book's own contents list."""
    chapters, parts = {}, {}
    for bl in pages[:40]:
        for b in bl:
            if b.strip().startswith("|"):
                b = _toc_or_list(b.strip())
            for ln in b.split("\n"):
                m = re.match(r"^- (\d{1,2})\\?\.\s+(.+?)(?:\s+\(p\.[^)]*\)?)?\s*$", ln.strip())
                if m and int(m.group(1)) not in chapters:
                    chapters[int(m.group(1))] = m.group(2).strip()
                m = re.match(r"^\*\*Part\s+(\d+)\.\s+(.+?)\*\*$", ln.strip())
                if m:
                    parts[int(m.group(1))] = m.group(2).strip()
    return chapters, parts


def find_chapter_titles(pages, front, chapters):
    """Locate each chapter's opening title (which may be split over several
    blocks of different heading levels) and return {page_k: (n, title, nblocks, levels)}."""
    found, k0 = {}, 0
    for n in sorted(chapters):
        target = _toks(f"{n} {chapters[n]}")
        for k in range(k0, len(pages)):
            if front[k]:
                continue
            pos, used, levs = 0, 0, []
            for b in pages[k][:6]:
                if "\n" in b.strip() or b.strip().startswith(("[^", "<!--", "|")):
                    break
                t = _toks(b)
                if not t or target[pos:pos + len(t)] != t:
                    break
                m = HEAD.match(b.strip())
                if m:
                    levs.append(len(m.group(1)))
                pos += len(t)
                used += 1
                if pos == len(target):
                    break
            main_len = len(_toks(f"{n} {chapters[n].split(':')[0]}"))
            if used and pos >= main_len and pos >= 3:
                found[k] = (n, f"{n}. {chapters[n]}", used, levs)
                k0 = k + 1
                break
    return found


CHAPWORD = r"(CAPITOLO|CAP[IÍ]TULO|CHAPITRE|CHAPTER|KAPITEL)"
PARTWORD = r"(PARTE|PARTIE|PART|TEIL)"
ORDINALS = ("PRIMA PRIMO SECONDA SECONDO TERZA TERZO QUARTA QUARTO QUINTA QUINTO SESTA SETTIMA "
            "PRIMERA PRIMERO SEGUNDA SEGUNDO TERCERA TERCERO CUARTA CUARTO QUINTA "
            "FIRST SECOND THIRD FOURTH FIFTH SIXTH ONE TWO THREE FOUR FIVE UNO DUE TRE QUATTRO "
            "PREMIÈRE DEUXIÈME TROISIÈME QUATRIÈME ERSTER ZWEITER DRITTER").split()
CHAP_RE = re.compile(rf"^{CHAPWORD}\s+([IVXLCDM]+|\d+)\.?$")
PART_RE = re.compile(rf"^{PARTWORD}\s+({'|'.join(ORDINALS)}|[IVXLCDM]+|\d+)\.?$")
MINOR_ALL = set("di a da in con su per tra fra e ed o il lo la i gli le l un una del dello della dei degli "
                "delle dell al allo alla ai agli alle all dal dalla dai dalle dall nel nella nei nelle nell "
                "sul sulla sui sulle col che de del los las el y en por para al du des et au aux à d "
                "les un une von der die das und zu im am".split())


def _title_case_caps(t):
    """GLI ATTRIBUTI DELL’ALLEANZA -> Gli Attributi dell’Alleanza (only for all-capital text)."""
    words, out, first = t.split(), [], True
    for w in words:
        m = re.match(r"^([A-Za-zÀ-ÿ]+[’'])(.*)$", w)             # elision: DELL’ALLEANZA, L’ETERNITÀ
        if m and len(m.group(2)) > 0:
            head, rest = m.group(1).lower(), m.group(2)
            head = head.capitalize() if first or head[:-1] not in MINOR_ALL else head
            if rest.lower() in MINOR_ALL and False:
                pass
            out.append(head + rest[:1].upper() + rest[1:].lower())
        elif re.fullmatch(r"[IVX]{2,}[.,;:)]?", w):
            out.append(w)
        else:
            core = re.sub(r"[^A-Za-zÀ-ÿ]", "", w).lower()
            if not first and core in MINOR_ALL:
                out.append(w.lower())
            else:
                out.append(w[:1].upper() + w[1:].lower())
        first = first or False
        first = False
    return " ".join(out)


def _is_caps_line(t):
    letters = re.sub(r"[^A-Za-zÀ-ÿ]", "", t)
    return len(letters) >= 4 and letters == letters.upper() and 2 <= len(t.split()) + (len(t) > 12) <= 40 \
        and len(t) <= 130 and not re.search(r"\d\s*$", t) and not t.startswith(("[^", "|", "<", ">", "-", "*"))


def title_case_en(t):
    """PERSONS AND PROPOSITIONS -> Persons and Propositions (English headings)."""
    words, out = t.split(), []
    for i, w in enumerate(words):
        bare = re.sub(r"[^A-Za-z]", "", w)
        if bare and bare == bare.upper() and re.fullmatch(r"[IVXLCDM]+", bare):
            out.append(w)                                        # roman numerals: II, XIV
        elif i and i < len(words) - 1 and bare.lower() in MINOR:
            out.append(w.lower())
        elif w[:1].isalpha():
            out.append(w[:1].upper() + w[1:].lower())
        else:
            out.append(w)
    return " ".join(out)


def normalize_headings(md, nonenglish):
    """A final sweep over every heading: drop ornament-only headings (a stray
    brace or dingbat that came through as large type), and recase all-capital
    headings — title case for English books, sentence case for others."""
    out = []
    for ln in md.split("\n"):
        m = re.match(r"^(#{1,6}) (.*)$", ln)
        if not m:
            out.append(ln)
            continue
        txt = re.sub(r"\s+", " ", m.group(2)).strip()
        plain = re.sub(r"[*_`]", "", txt)
        letters = re.sub(r"[^A-Za-zÀ-ÿ]", "", plain)
        if len(letters) < 2:
            continue                                             # ornament, e.g. "# }"
        if letters == letters.upper():
            txt = sentence_case(plain) if nonenglish else title_case_en(plain)
        out.append(m.group(1) + " " + txt)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


NONENGLISH = False          # set per book by detect_language()
PROPER = set()              # words that are capitalised in running text (Dio, Gesù, Antico Testamento ...)
SENTENCE_LOOKUP = {}        # letters-only key -> heading as written in the book's own contents list


def detect_language(pages):
    """True if the body text is not English (so headings use sentence case)."""
    text = " ".join(b for bl in pages[:400] for b in bl if not b.startswith(("[^", "#", "<!--", "|")))[:400000].lower()
    words = re.findall(r"[a-zà-ÿ]+", text)
    c = Counter(words)
    en = sum(c[w] for w in ("the", "of", "and", "that", "which", "with"))
    other = sum(c[w] for w in ("di", "del", "della", "che", "il", "la", "e", "de", "los", "las", "el", "y", "que",
                               "en", "du", "des", "et", "le", "les", "und", "der", "die", "das"))
    return other > en


def build_proper(pages):
    cap, low = Counter(), Counter()
    for bl in pages:
        for b in bl:
            if b.startswith(("[^", "#", "<!--", "|", "**")):
                continue
            for seg in re.split(r"[.?!:;»«“”\n]\s*", b):
                toks = re.findall(r"[A-Za-zÀ-ÿ]+", seg)
                for w in toks[1:]:
                    if w[:1].isupper() and not w.isupper() and len(w) > 2:
                        cap[w.lower()] += 1
                    elif w.islower():
                        low[w] += 1
    return {w for w, n in cap.items() if n >= 3 and n > low[w]}


def sentence_case(text):
    """Capital only at the start and on proper names; Italian, Spanish, French and German practice."""
    key = letters_key(text)
    if key in SENTENCE_LOOKUP:
        return SENTENCE_LOOKUP[key]
    out, first = [], True
    for tok in re.split(r"(\s+)", text):
        if not tok.strip():
            out.append(tok)
            continue
        def fix(m):
            w = m.group(0)
            if re.fullmatch(r"[IVXLCDM]{2,}", w) and w.isupper() and w not in ("DI", "IL", "LI", "MI", "CI", "DC"):
                return w
            return w.lower() if w.lower() not in PROPER else w[:1].upper() + w[1:].lower()
        t = re.sub(r"[A-Za-zÀ-ÿ]+", fix, tok)
        if first:
            t = re.sub(r"[A-Za-zÀ-ÿ]+(?![’'][A-Za-zÀ-ÿ])", lambda m: m.group(0)[:1].upper() + m.group(0)[1:], t, count=1)
            if re.match(r"^[A-Za-zÀ-ÿ]+[’']", t):          # L’eternità -> L’eternità (capital on the article only)
                t = t[:1].upper() + t[1:]
            first = False
        out.append(t)
    return "".join(out)


def _fix_minor(text):
    """Small words left in capitals by the small-caps repair (IL, DI) go back to lower case."""
    out = []
    for i, w in enumerate(text.split()):
        core = re.sub(r"[^A-Za-zÀ-ÿ]", "", w)
        low = core.lower()
        if core and core.isupper() and low in MINOR_ALL and not re.fullmatch(r"[IVX]{2,}", core):
            out.append(w.capitalize() if i == 0 else w.lower())
        else:
            out.append(w)
    return " ".join(out)


def _contents_blocks(text):
    """One flowing Italian contents paragraph -> nested list of chapters and sections."""
    if not re.search(r"CAP\. [IVXLC]+\. ", text):
        return None
    lines = []
    first, *chunks = re.split(r"(?=CAP\. [IVXLC]+\. )", text)
    first = first.strip()
    if first:
        for part in re.split(r"(?<=\d)\s+(?=[IVX]+\s+[A-ZÀ-Ý])", first):
            m = re.match(r"^([IVX]+)\s+([A-ZÀ-Ý’' ,.\-]+)\s*$", part.strip())
            if m:
                pt = _title_case_caps(m.group(2).strip())
                lines.append(f"\n**Parte {m.group(1)}. {sentence_case(pt) if NONENGLISH else pt}**\n")
            elif part.strip():
                m2 = re.match(r"^(.*?)(\d{1,3})$", part.strip())
                lines.append(f"- {m2.group(1).strip()} (p. {m2.group(2)})" if m2 else part.strip())
    for ch in chunks:
        m = re.match(r"CAP\. ([IVXLC]+)\. (.+?)\s?(\d{1,3})\s*(.*)$", ch.strip(), re.S)
        if not m:
            lines.append(ch.strip())
            continue
        num, title, page, rest = m.groups()
        ttl = _title_case_caps(title.strip())
        lines.append(f"- **Capitolo {num}.** {sentence_case(ttl) if NONENGLISH else ttl} (p. {page})")
        # trailing "Parte" line belonging to the next part, e.g. "III IL MISTERO ..."
        for e in re.finditer(r"(.+?),\s*(\d{1,3})(?:\s+|$)", rest.replace("\n", " ")):
            lines.append(f"  - {e.group(1).strip()} (p. {e.group(2)})")
    return "\n".join(lines)


def keyword_structure(parsed, front):
    """For books laid out as PARTE / CAPITOLO / capitalised section titles:
    build Part (#), Chapter (##) and section headings, drop repeated running
    heads, and turn broken-off sentence fragments back into text.
    Returns the rendered pages, or None if the book has no chapter keywords."""
    def kind_of(it):
        if it[0] in ("H", "P") and "\n" not in it[2]:
            t = _plain(it[2]).upper() if it[0] == "H" or _is_caps_line(it[2]) else ""
            if t and CHAP_RE.match(t):
                return "CHAP", t
            if t and PART_RE.match(t):
                return "PARTW", t
        return None, None

    global NONENGLISH, PROPER, SENTENCE_LOOKUP
    plain_pages = [[it[2] for it in items if it[0] == "P"] for items in parsed]
    NONENGLISH = detect_language(plain_pages)
    PROPER = build_proper(plain_pages) if NONENGLISH else set()
    SENTENCE_LOOKUP = {}
    first_struct = next((k for k, items in enumerate(parsed) if any(kind_of(it)[0] for it in items)), None)
    nchap = sum(1 for items in parsed for it in items if kind_of(it)[0] == "CHAP")
    if nchap < 3 or first_struct is None:
        return None
    front = [k < first_struct for k in range(len(parsed))]       # everything before the first PARTE / CAPITOLO

    lev_count0 = Counter(it[1] for k, items in enumerate(parsed) if not front[k]
                         for it in items if it[0] == "H" and not kind_of(it)[0])
    sec_orig = lev_count0.most_common(1)[0][0] if lev_count0 else 3
    has_parts = any(kind_of(it)[0] == "PARTW" for items in parsed for it in items)
    chap_lev = 2 if has_parts else 1

    seen, cur_chap, cur_part, finals = set(), None, None, []
    for k, items in enumerate(parsed):
        norm_items = []
        for it in items:
            kd, t = kind_of(it)
            if kd:
                norm_items.append([kd, 0, t])
            elif it[0] == "P" and not front[k] and "\n" not in it[2] and _is_caps_line(_plain(it[2])):
                norm_items.append(["H", sec_orig, _plain(it[2])])
            elif it[0] == "PART":
                norm_items.append(["PARTW", 0, it[2].upper()])
            else:
                norm_items.append(list(it))
        # a repeated "CAPITOLO V" / "PARTE PRIMA" at the top of a page is a running head
        norm2 = []
        for idx, it in enumerate(norm_items):
            if it[0] == "CHAP" and idx < 2 and it[2] == cur_chap:
                continue
            if it[0] == "PARTW" and idx < 2 and it[2] == cur_part:
                continue
            if it[0] == "CHAP":
                cur_chap = it[2]
            if it[0] == "PARTW":
                cur_part = it[2]
            norm2.append(it)
        joined, i = [], 0
        while i < len(norm2):
            it = norm2[i]
            if it[0] in ("CHAP", "PARTW") and i + 1 < len(norm2) and norm2[i + 1][0] == "H":
                title = norm2[i + 1][2]
                j = i + 2
                while j < len(norm2) and norm2[j][0] == "H" and norm2[j][1] == norm2[i + 1][1] \
                        and _wants_merge(title, norm2[j][2]):
                    title += " " + norm2[j][2]
                    j += 1
                m = (CHAP_RE if it[0] == "CHAP" else PART_RE).match(it[2])
                num = m.group(2) if (m.group(2).isdigit() or re.fullmatch(r"[IVXLCDM]+", m.group(2))) else m.group(2).capitalize()
                label = m.group(1).capitalize() + " " + num
                title = _fix_minor(title)
                joined.append(["CH" if it[0] == "CHAP" else "PT", 0,
                               f"{label}. {_title_case_caps(title) if title == title.upper() else title}"])
                i = j
            else:
                joined.append(it)
                i += 1
        kept = []
        for idx, it in enumerate(joined):
            key = letters_key(it[2]) if it[0] in ("H", "CH", "PT") else \
                (letters_key(it[2]) if it[0] == "P" and "\n" not in it[2] and len(it[2]) < 110 and _is_caps_line(_plain(it[2])) else "")
            if key and idx < 2 and key in seen and not front[k]:
                continue
            kept.append(it)
        for it in kept:
            if it[0] in ("H", "CH", "PT") and letters_key(it[2]):
                seen.add(letters_key(it[2]))
                if it[0] in ("CH", "PT"):
                    seen.add(letters_key(re.sub(r"^[^.]*\.\s*", "", it[2])))
        final = []
        for it in kept:
            if it[0] == "H" and not front[k] and (re.search(r"[.)]$", it[2]) or re.search(r"\[\^[^\]]+\]", it[2])
                                                    or it[2][:1].islower()):
                frag = it[2]
                prev = finals[-1] if finals else None
                if (frag[:1].islower() or frag[:1].isdigit()) and not final and prev is not None:
                    tgt = next((b for b in range(len(prev) - 1, -1, -1)
                                if prev[b][0] == "P" and not prev[b][2].startswith(("[^", "<!--", "**[", "---", ">", "- ", "|"))), None)
                    if tgt is not None:
                        prev[tgt][2] = prev[tgt][2].rstrip() + " " + frag
                        continue
                final.append(["P", 0, frag])
            else:
                final.append(it)
        finals.append(final)

    # contents pages: glue a block that runs on from the previous page, then make it a list
    for k in range(len(finals)):
        if not front[k]:
            continue
        for it in finals[k]:
            if it[0] == "P":
                mp = re.match(r"^([IVX]+)\s+([A-ZÀ-Ý’' ,.\-]{6,})$", it[2].strip())
                if mp:                                         # a Part line in the contents, e.g. "II IL MISTERO DI DIO ..."
                    pt = _title_case_caps(mp.group(2).strip())
                    it[2] = f"**Parte {mp.group(1)}. {sentence_case(pt) if NONENGLISH else pt}**"
                    continue
                lst = _contents_blocks(it[2])
                if lst:
                    it[2] = lst
    if NONENGLISH:                                              # the book's own contents list is the authority
        for k in range(len(finals)):
            if front[k]:
                for it in finals[k]:
                    for ln in it[2].split("\n"):
                        mm = re.match(r"^\s+- (.+?) \(p\. \d+\)$", ln)
                        if mm:
                            SENTENCE_LOOKUP.setdefault(letters_key(mm.group(1)), mm.group(1).strip())

    # one hierarchy for the sections: a chapter that has group headings gets one level more
    chap_id, has_group = [], {}
    cid = 0
    for k, final in enumerate(finals):
        for it in final:
            if it[0] == "CH":
                cid += 1
        chap_id.append(cid)
        if not front[k] and any(it[0] == "H" and it[1] < sec_orig for it in final):
            has_group[cid] = True

    def sec_level(orig, k):
        extra = 1 if has_group.get(chap_id[k]) else 0
        if orig < sec_orig:
            return min(chap_lev + 1, 6)
        return min(chap_lev + 1 + extra + (1 if orig > sec_orig else 0), 6)

    def tidy_title(text):
        if NONENGLISH:
            return sentence_case(text)
        if any(len(w) >= 2 and w.isalpha() and w.isupper() and not re.fullmatch(r"[IVX]+", w) for w in text.split()):
            text = _title_case_caps(text.upper())
        return _fix_minor(text)

    out = []
    for k, final in enumerate(finals):
        bl = []
        for kind, lev, text in final:
            if kind == "PT":
                lab, _, ttl = text.partition(". ")
                bl.append("# " + lab + ". " + tidy_title(ttl))
            elif kind == "CH":
                lab, _, ttl = text.partition(". ")
                bl.append(("#" * chap_lev) + " " + lab + ". " + tidy_title(ttl))
            elif kind in ("CHAP", "PARTW"):
                bl.append(f"**{text.title()}**")
            elif kind == "H":
                text = tidy_title(text)
                if front[k]:
                    m = re.match(r"^([IVX]+)\s+(.+)$", text)
                    bl.append(f"**Parte {m.group(1)}. {m.group(2)}**" if m else f"**{text}**")
                    continue
                bl.append("#" * sec_level(lev, k) + " " + text)
            else:
                bl.append(text)
        out.append(bl)
    return out


def polish(pages, labels_k, vocab):
    """Tidy the structure: one coherent heading hierarchy, titles split over two
    lines joined, lead-in sentences no longer headings, contents as lists, and
    scan noise removed from the front matter."""
    front, seen_body = [], False
    for lab in labels_k:
        seen_body = seen_body or lab.isdigit()
        front.append(not seen_body)

    chapters, parts = contents_titles(pages)
    chap_at = find_chapter_titles(pages, front, chapters) if chapters else {}
    chap_lev = Counter(l for v in chap_at.values() for l in v[3])
    ch_level = chap_lev.most_common(1)[0][0] if chap_lev else 2

    # pass 1: classify blocks, merge split titles
    parsed = []
    for k, bl in enumerate(pages):
        items = []
        skip = 0
        if k in chap_at:
            items.append(["H", ch_level, chap_at[k][1]])
            skip = chap_at[k][2]
        for b in bl[skip:]:
            b = b.strip()
            pm = re.match(r"^(?:#+\s*)?Part\s+(\w+)\b", b) if "\n" not in b and len(b) < 130 and not front[k] else None
            if pm:
                pn = int(pm.group(1)) if pm.group(1).isdigit() else NUMWORDS.get(pm.group(1).lower())
                pt = parts.get(pn) if pn else None
                if pt and _toks(b)[2:5] == _toks(pt)[:3]:
                    items.append(["PART", 0, f"Part {pn}. {pt}"])
                    continue
            m = HEAD.match(b) if "\n" not in b else None
            if m:
                items.append(["H", len(m.group(1)), _plain(m.group(2))])
            elif "\n" not in b and PART.match(b) and len(b) < 90 and not b.startswith(("[^", "|")):
                items.append(["PART", 0, _plain(b)])
            elif b.startswith("|"):
                items.append(["P", 0, _toc_or_list(b)])
            else:
                if front[k] and not b.startswith(("[^", "<!--", "*")):
                    toks = re.findall(r"[A-Za-z]+", b)
                    longw = [w for w in toks if len(w) >= 4]
                    if len(toks) >= 3 and len(b) < 160 and (
                            sum(1 for w in toks if w.lower() in vocab) / len(toks) < 0.3
                            or (len(b) < 80 and len(toks) >= 4 and not any(w.lower() in vocab for w in longw))):
                        continue                                  # scan noise on the cover
                items.append(["P", 0, b])
        merged = []
        for it in items:
            if merged and it[0] == "H" and merged[-1][0] == "H" and it[1] == merged[-1][1] \
               and _wants_merge(merged[-1][2], it[2]):
                first = it[2].split()[0]
                rest = it[2]
                if first.lower() in MINOR and not merged[-1][2].endswith(":"):
                    rest = first.lower() + it[2][len(first):]
                merged[-1][2] += " " + rest
            else:
                merged.append(it)
        for it in merged:                                         # a lead-in sentence is not a heading
            if it[0] == "H" and re.search(r"[:.]$", it[2]) and len(it[2].split()) >= 8:
                it[0] = "P"
        parsed.append(merged)

    if not chapters:
        alt = keyword_structure(parsed, front)
        if alt is not None:
            return alt

    # pass 2: one hierarchy for the whole book
    counts = Counter(it[1] for items in parsed for it in items if it[0] == "H")
    struct = sorted(l for l, n in counts.items() if n >= 5)
    has_parts = any(it[0] == "PART" for items in parsed for it in items)
    base = 2 if has_parts else 1

    def newlevel(orig):
        if not struct:
            return min(orig, 6)
        below = [l for l in struct if l <= orig]
        s = below[-1] if below else struct[0]
        return min(base + struct.index(s), 6)

    out = []
    for k, items in enumerate(parsed):
        bl = []
        for kind, lev, text in items:
            if kind == "PART":
                bl.append("# " + re.sub(r"^(Part\s+\w+)\s", r"\1. ", text) if not re.match(r"^Part\s+\w+[.:]", text)
                          else "# " + text)
            elif kind == "H":
                if lev not in struct and front[k]:
                    bl.append(f"**{text}**")                       # cover and title-page lines
                    continue
                if text == text.lower() and len(text) > 3:           # "general index" -> "General Index"
                    text = " ".join(w if (i and w in MINOR) else w.capitalize() for i, w in enumerate(text.split()))
                nl = newlevel(lev)
                if struct and nl == base:                          # chapter titles: "1 Title" -> "1. Title"
                    text = re.sub(r"^(\d{1,2})\s+(?=\S)", r"\1. ", text)
                bl.append("#" * nl + " " + text)
            else:
                bl.append(text)
        out.append(bl)
    return out


# ------------------------------------------------ e-books: endnotes, stamps, headings

TH_FIXES = {w: "Th" + w[1:] for w in (
    "Te Tey Tis Tat Tese Tose Tere Tus Ten Tem Teir Tings Ting Teology Teological Teologian Teologians "
    "Teologically Teories Teory Teoretical Tomas Tomist Tomists Tomistic Tought Toughts Tird Tirty Tousand "
    "Tessalonians Teodore Teophilus Tesis Teism Teistic Tan Tou Terefore Tereby Terein Teretofore "
    "Tough Tree Treats Treat Trough Troughout Tickness Tinking Tink Tinks Tinkers Tinker Tirst Tis's").split()}
for _bad in ("Tough", "Tree", "Treats", "Treat", "Trough", "Troughout", "Tinker", "Tinkers", "Tink", "Tinks", "Tickness", "Tirst", "Tis's"):
    TH_FIXES.pop(_bad, None)                      # real words as well: leave them alone
TH_FIXES_AMBIGUOUS = {"Tree": "Three", "Trough": "Through", "Troughout": "Throughout", "Tough": "Though",
                      "Tink": "Think", "Tinks": "Thinks", "Tinking": "Thinking", "Tinkers": "Thinkers"}


def repair_th(md):
    """Some e-books lose the 'Th' ligature when copied ('Te' for 'The', 'Tings' for 'Things')."""
    lost = len(re.findall(r"\bTe\b(?! Deum)", md))
    intact = len(re.findall(r"\bThe\b", md))
    if lost < 30 or lost < 5 * max(intact, 1):
        return md, 0
    count = 0
    TH_FIXES.update(TH_FIXES_AMBIGUOUS)               # safe once we know the ligature is systematically lost

    def fix(m):
        nonlocal count
        w = m.group(0)
        if w in TH_FIXES:
            if w == "Te" and md[m.end():m.end() + 6] == " Deum":
                return w
            count += 1
            return TH_FIXES[w]
        return w
    return re.sub(r"\bT[a-z]+\b", fix, md), count


def drop_repeated_lines(pages, share=0.25):
    """Delete a one-line block (e.g. 'This ebook belongs to …') that repeats on a quarter of the pages."""
    cnt = Counter()
    for p in pages:
        for b in {b.strip() for b in p.split("\n\n") if "\n" not in b.strip()}:
            if len(b) > 20 and not b.startswith(("<!--", "---")) and not re.match(r"^\*\*\[", b):
                cnt[b] += 1
    bad = {b for b, n in cnt.items() if n >= max(8, share * len(pages))}
    if not bad:
        return pages, 0
    out = []
    for p in pages:
        out.append("\n\n".join(b for b in p.split("\n\n") if b.strip() not in bad))
    return out, len(bad)


def page_label(p):
    m = re.search(r"^\*\*\[(?:PDF )?p\. ([^\]]+)\]\*\*", p, re.M)
    return m.group(1) if m else ""


def ebook_headings(pages):
    """Chapter titles from the contents list; bold one-line paragraphs become section headings."""
    toc = []                                         # (label, number, title)
    for p in pages[:20]:
        for ln in p.split("\n"):
            m = re.match(r"^- (?:(\d{1,2})\s+)?(.+?) \(p\. (\d+)\)$", ln.strip())
            if m:
                toc.append((m.group(3), m.group(1), m.group(2)))
    if len(toc) < 3:
        return pages, toc
    by_label = {}
    for lab, num, title in toc:
        by_label.setdefault(lab, (num, title))
    out = []
    for p in pages:
        lab = page_label(p)
        blocks = p.split("\n\n")
        if lab in by_label and not p.startswith("<!-- PDF page 7 "):
            num, title = by_label[lab]
            key = letters_key(title)
            for i, b in enumerate(blocks):
                bb = re.sub(r"^\*\*(.*)\*\*$", r"\1", b.strip())
                if i < 6 and bb and (letters_key(bb) == key or (len(key) > 8 and letters_key(bb)[:len(key)] == key)
                                     or (len(letters_key(bb)) > 8 and key.startswith(letters_key(bb)))):
                    blocks[i] = ("## " + (f"{num}. " if num else "") + title)
                    if i > 0 and re.fullmatch(r"\d{1,2}", blocks[i - 1].strip()):
                        blocks[i - 1] = ""
                    break
        front = "**[PDF p." in p
        for i, b in enumerate(blocks):                 # **Bold line** on its own = section heading
            m = re.fullmatch(r"\*\*([^*\n]{3,110})\*\*", b.strip())
            if m and not m.group(1).startswith(("This ebook", "[")) and lab and not lab.isalpha():
                blocks[i] = ("## " if front else "### ") + m.group(1)
        last2 = None
        for i in range(len(blocks)):                  # a section heading that only repeats the chapter title
            m1 = re.match(r"^## (?:\d+\. )?(.+)$", blocks[i].strip())
            if m1:
                last2 = letters_key(m1.group(1))
                continue
            m2 = re.match(r"^### (.+)$", blocks[i].strip())
            if last2 and m2 and len(letters_key(m2.group(1))) > 8 and letters_key(m2.group(1)) in last2:
                blocks[i] = ""
        out.append("\n\n".join(b for b in blocks if b != ""))
    return out, toc


def endnotes_to_footnotes(pages, toc):
    """Turn a closing 'Notes' section into real footnotes placed under the page that cites each one.
    Returns (pages, report string or None)."""
    ni = next((k for k, p in enumerate(pages) if re.search(r"^## Notes\s*$", p, re.M)), None)
    if ni is None:
        return pages, None
    ei = next((k for k in range(ni + 1, len(pages)) if re.search(r"^## (?!Notes)", pages[k], re.M)), len(pages))
    # chapters in the order of the contents list, up to "Notes"
    starts = []
    for lab, num, title in toc:
        if title == "Notes":
            break
        if lab.isdigit():
            starts.append((int(lab), (num and f"c{num}") or ("concl" if title.lower().startswith("conclusion")
                                                              else "intro" if title.lower().startswith("intro") else letters_key(title)[:6])))
    # the notes themselves, in groups
    items, groups, cur = {}, [], None
    for k in range(ni, ei):
        for b in pages[k].split("\n\n"):
            b = b.strip()
            if not b or b.startswith(("<!--", "---", "**[")) or re.match(r"^## Notes", b):
                continue
            if re.fullmatch(r"\*\*Chapter \d+\*\*|### [A-Z].{0,60}", b):
                groups.append({})
                cur = None
                continue
            if not groups:
                groups.append({})
            for part in re.split(r"\n(?=- \d+ )", b):
                m = re.match(r"^- (\d+) (.*)$", part, re.S)
                if m:
                    cur = (len(groups) - 1, int(m.group(1)))
                    groups[-1][cur[1]] = m.group(2).strip()
                elif cur is not None and not b.startswith("#"):
                    groups[cur[0]][cur[1]] += " " + part.strip()
    if len(groups) != len(starts):
        return pages, f"endnotes not converted: {len(groups)} note groups but {len(starts)} chapters in the contents"
    used, missing, n_conv = set(), 0, 0
    out = list(pages)
    for k in range(0, ni):
        p = pages[k]
        lab = page_label(p)
        if not lab.isdigit():
            continue
        gi = max((i for i, (st, _) in enumerate(starts) if st <= int(lab)), default=None)
        if gi is None:
            continue
        cid = starts[gi][1]
        defs = []

        def rep(m):
            nonlocal n_conv, missing
            n = int(m.group(1))
            if n in groups[gi] and (gi, n) not in used:
                used.add((gi, n))
                defs.append(f"[^{cid}-{n}]: {groups[gi][n]}")
                n_conv += 1
                return f"[^{cid}-{n}]"
            missing += 1
            return m.group(0)
        p = re.sub(r"<sup>_?(\d{1,3})_?</sup>", rep, p)
        if defs:
            p = p.rstrip() + "\n\n" + "\n\n".join(defs)
        out[k] = p
    orphan = sum(len(g) for g in groups) - len(used)
    for k in range(ni, ei):
        lab = page_label(pages[k])
        head = pages[k].split("\n\n")[:2]
        keep = "\n\n".join(head[:2]) if k == ni else "\n\n".join(head[:2])
        body = ("## Notes\n\n*The endnotes have been moved: each now appears as a footnote on the page where it is cited.*"
                if k == ni else "*(endnotes: see the footnotes on the pages where they are cited)*")
        out[k] = "\n\n".join(x for x in pages[k].split("\n\n")[:2] if x.startswith(("<!--", "**["))) + "\n\n" + body
    rep_txt = f"{n_conv} endnotes converted to footnotes; {missing} in-text numbers without a note; {orphan} notes without an in-text number"
    return out, rep_txt


NOTE_HEAD = re.compile(r"^#{0,6}\s*(?:\*\*)?NOTES?(?:\*\*)?\s*$", re.I)
SUP_MARK = re.compile(r"<sup>\s*_?(\d{1,3})_?\s*</sup>")
_ABBR = {"no", "nos", "p", "pp", "vol", "vols", "n", "nn", "fol", "col", "art", "q", "qq",
         "c", "cap", "ch", "chap", "v", "vv", "sec", "par", "fig", "pt", "bk"}
# a reference number that begins a note: at the start, or after sentence-ending
# punctuation, followed by note text (a capital letter, quotation mark or italics),
# never a page/volume citation like "no. 16." or a bare year
_NOTE_AT = re.compile(r'(?:^|(?<=[.)\]”’"]))\s+(\d{1,3})\.\s+(?=[A-Z“"\'_(])')


def split_notes(parts):
    """A chapter's notes, given as a list of text blocks. Each block usually
    starts a new note ('75. They could also…'), and several notes may also run
    together on one line ('56. … 57. … 59. …'). Return {n: text}, taking numbers
    in increasing order (small gaps allowed for a note missing from the text
    layer) and ignoring numbers that are really page or volume references."""
    # one string, remembering where each block began (a reliable note boundary)
    region, starts = "", set()
    for p in parts:
        starts.add(len(region))
        region += " " + p.strip()
    cands = []
    for m in re.finditer(r"(\d{1,3})\.\s+(?=[\"“'(_]|[A-Za-z])", region):
        s = m.start(1)
        at_block = (s - 1) in starts or (s >= 1 and region[s - 1] == " " and (s - 1) in starts)
        if not at_block:
            # mid-line: require a sentence boundary and reject "no. 16." etc.
            if s == 0 or region[s - 1] not in " ":
                continue
            prev = region[:s].rstrip()
            if prev and prev[-1] not in ".)]”’\"":
                continue
            tok = re.split(r"[\s(]", prev)[-1].rstrip(".").lower() if prev else ""
            if tok in _ABBR:
                continue
        cands.append((s, int(m.group(1)), m.end()))
    chosen, last = [], 0
    for st, n, en in cands:
        if n > last and n <= last + 10:
            chosen.append((st, n, en))
            last = n
    notes = {}
    for idx, (st, n, en) in enumerate(chosen):
        end = chosen[idx + 1][0] if idx + 1 < len(chosen) else len(region)
        notes[n] = region[en:end].strip()
    return notes


def convert_chapter_endnotes(pages):
    """Books that gather each chapter's notes in a 'Notes' list at the chapter
    end, with superscript reference numbers in the body. Turn every <sup>n</sup>
    into a real footnote [^cNN-n] placed under the page where it is cited, and
    remove the Notes lists. Returns (pages, report) or (pages, None) if the book
    is not laid out this way."""
    note_heads = sum(1 for p in pages if any(NOTE_HEAD.match(ln) for ln in p.split("\n")))
    sup_total = sum(len(SUP_MARK.findall(p)) for p in pages)
    if note_heads < 1 or sup_total < 20:
        return pages, None

    # flatten to items, keeping each block's (page, block-index)
    blocks = [p.split("\n\n") for p in pages]
    items = [(k, bi) for k, bl in enumerate(blocks) for bi in range(1, len(bl))]

    def text(it):
        return blocks[it[0]][it[1]]

    # locate each Notes group: its heading item, its note dict, and the items it owns
    groups = []
    i = 0
    while i < len(items):
        bl_text = text(items[i]).strip()
        if NOTE_HEAD.match(bl_text.split("\n")[0]):
            owned, region_parts = [items[i]], []
            j = i + 1
            while j < len(items):
                t = text(items[j]).strip()
                if re.match(r"^#{1,6}\s", t) and not NOTE_HEAD.match(t.split("\n")[0]):
                    break                                     # next chapter heading ends the list
                if re.match(r"^\d{1,3}\.\s", t) or (region_parts and not t.startswith("#")):
                    owned.append(items[j])
                    if not t.startswith(("<!--", "**[", "---")):
                        region_parts.append(t)
                elif t.startswith(("<!--", "**[", "---")):
                    owned.append(items[j])                    # keep page markers inside the list
                else:
                    break
                j += 1
            notes = split_notes(region_parts)
            if notes:
                groups.append({"notes": notes, "owned": set(owned), "hpos": i})
            i = j
        else:
            i += 1
    if not groups:
        return pages, None

    owned_all = set().union(*(g["owned"] for g in groups))
    add_defs = {}                                             # page index -> [def lines]
    n_conv = missing = 0

    for idx, it in enumerate(items):
        if it in owned_all:
            continue
        # notes follow their markers, so a marker belongs to the next Notes list
        g = next((gg for gg in groups if gg["hpos"] > idx), None)
        if g is None:
            continue
        cid = f"c{groups.index(g) + 1:02d}"
        k, bi = it
        defs = []

        def rep(mm):
            nonlocal n_conv, missing
            n = int(mm.group(1))
            if n in g["notes"]:
                n_conv += 1
                defs.append(f"[^{cid}-{n}]: {g['notes'][n]}")
                return f"[^{cid}-{n}]"
            missing += 1
            return mm.group(0)
        new = SUP_MARK.sub(rep, blocks[k][bi])
        blocks[k][bi] = new
        if defs:
            add_defs.setdefault(k, []).extend(defs)

    # blank out the Notes lists (keep page markers / separators) and append defs
    for g in groups:
        for (k, bi) in g["owned"]:
            t = blocks[k][bi]
            keep = "\n".join(ln for ln in t.split("\n") if ln.startswith(("<!--", "**[", "---")))
            blocks[k][bi] = keep                              # drop the note text, keep any page marker
    for k, defs in add_defs.items():
        seen, uniq = set(), []
        for d in defs:
            if d not in seen:
                seen.add(d)
                uniq.append(d)
        blocks[k].append("\n\n".join(uniq))

    out = []
    for bl in blocks:
        out.append("\n\n".join(b for b in bl if b.strip()))
    rep_txt = (f"{n_conv} chapter endnotes converted to footnotes under the cited pages"
               + (f"; {missing} superscript marks had no matching note" if missing else ""))
    return out, rep_txt


def ebook_cleanup(md):
    """Post-processing for e-books with endnotes; returns (markdown, [messages])."""
    pages = md.split("\n\n---\n\n")
    msgs = []
    pages, nrep = drop_repeated_lines(pages)
    if nrep:
        msgs.append(f"removed {nrep} line(s) repeated on many pages (licence stamps and the like)")
    text, nth = repair_th("\n\n---\n\n".join(pages))
    if nth:
        msgs.append(f"repaired {nth} words where the “Th” ligature had been lost (“Te” → “The”)")
    pages = text.split("\n\n---\n\n")
    if sum(1 for p in pages for _ in re.finditer(r"^#{1,6} ", p, re.M)) < 12:
        pages, toc = ebook_headings(pages)
        pages, rep = endnotes_to_footnotes(pages, toc)
        if rep:
            msgs.append(rep)
    return "\n\n---\n\n".join(pages), msgs


# ------------------------------------------- file naming, frontmatter, anchors

LANG_WORDS = {
    "en": "the of and to in that is was for as with his this which it not are be by",
    "it": "di che il la del e in per con una non si gli le dei della al dal nel è",
    "es": "de la que el en y los las por con una del no se para su lo al es",
    "fr": "de la le et les des que en un une dans pour qui est au aux par ne",
    "de": "und der die das in zu den von mit nicht ist auf dem des sich im für",
    "la": "et in est non ad cum qui quod sed per hoc autem nec esse enim ex quae",
}
GREEK = re.compile(r"[Ͱ-Ͽἀ-῿]")


def detect_lang_code(pages):
    """Best-guess ISO code (en, it, es, fr, de, la, grc) from the body text."""
    text = " ".join(b for bl in pages[:400] for b in bl
                     if not b.startswith(("[^", "#", "<!--", "|", "**[")))
    greek = len(GREEK.findall(text))
    latin = len(re.findall(r"[A-Za-zÀ-ÿ]", text))
    if greek > 200 and greek > latin:                        # a Greek text, not a Latin one that quotes Greek
        return "grc"
    c = Counter(re.findall(r"[a-zà-ÿ]+", text.lower()))
    best, score = "en", -1
    for code, ws in LANG_WORDS.items():
        s = sum(c[w] for w in ws.split())
        if s > score:
            best, score = code, s
    return best


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return re.sub(r"-{2,}", "-", s) or "document"


def output_name(pdf, args, lang):
    """<slug>.<lang>.md next to the PDF (Anthony's convention), unless -o given."""
    if args.output:
        return Path(args.output)
    slug = args.slug or slugify(pdf.stem)
    if args.author and not args.slug:
        people = [a.strip() for a in re.split(r"\s*(?:;|&|\band\b)\s*", args.author) if a.strip()]
        # default: one or two authors/editors are all named; three or more -> first only
        n = args.name_authors if args.name_authors else (len(people) if len(people) <= 2 else 1)
        names = []
        for a in people[:n]:
            sur = a.split(",")[0].split()[-1] if "," in a else a.split()[-1]
            sur = slugify(re.sub(r"['’‘`]", "", sur))
            if sur and sur not in slug.split("-") and sur not in names:
                names.append(sur)
        if names:
            slug = "-".join(names) + "-" + slug
    return pdf.with_name(f"{slug}.{lang}.md")


def frontmatter(title, creator, year, lang, source, anchors):
    def esc(x):
        return '"' + str(x).replace('"', '\\"') + '"'
    lines = ["---", f"title: {esc(title)}"]
    if creator:
        lines.append(f"creator: {esc(creator)}")
    if year:
        lines.append(f"year: {year}")
    lines.append(f"language: {lang}")
    if source:
        lines.append(f"source: {esc(source)}")
    lines.append(f"anchors: {'true' if anchors else 'false'}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def add_anchors(md, sigla, para=False):
    """Give every heading a stable id {#sigla.1.2…} by its place in the heading
    tree, so parallel passages in other-language editions can be aligned. With
    para=True, also number the body paragraphs within each top-level section as
    [k]{#sigla.<chapter>.<k>}."""
    cnt, out, chap, pnum = {}, [], 0, 0
    top = None
    for ln in md.split("\n"):
        m = re.match(r"^(#{1,6}) (.+?)\s*$", ln)
        if m and not re.search(r"\{#[^}]+\}\s*$", ln):
            lev = len(m.group(1))
            top = lev if top is None else min(top, lev)
            cnt[lev] = cnt.get(lev, 0) + 1
            for d in [d for d in cnt if d > lev]:
                del cnt[d]
            path = ".".join(str(cnt[d]) for d in sorted(cnt))
            out.append(f"{ln} {{#{sigla}.{path}}}")
            if lev == top:
                chap += 1
                pnum = 0
            continue
        if para and ln.strip() and not ln.startswith(("#", "[^", "<!--", "**[", "---", ">", "|", "- ", "*", "~")) \
                and not re.match(r"^\s*\[\d+\]\{#", ln) and chap:
            pnum += 1
            out.append(re.sub(r"^(\s*)(\S)", rf"\1[{pnum}]{{#{sigla}.{chap}.{pnum}}} \2", ln, count=1))
            continue
        out.append(ln)
    return "\n".join(out)


# --------------------------------------------------------------------- main


def parse_pages(spec, n):
    if not spec:
        return list(range(n))
    a, _, b = spec.partition("-")
    a, b = int(a), int(b or a)
    return list(range(max(a, 1) - 1, min(b, n)))


def main():
    global SMALL
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--offset", type=int, help="PDF page on which printed page 1 falls (only needed if it cannot be detected)")
    ap.add_argument("--roman", action="store_true", help="with an offset: label earlier pages i, ii, iii...")
    ap.add_argument("--pages", help="only convert these PDF pages, e.g. 60-65 (for testing)")
    ap.add_argument("-o", "--output", help="output .md path (default: <slug>.<lang>.md next to the PDF)")
    ap.add_argument("--slug", help="file-name slug (default: from the PDF's name)")
    ap.add_argument("--lang", help="ISO language code for the name and frontmatter (default: detected)")
    ap.add_argument("--title", help="title for the frontmatter (default: PDF metadata or the file name)")
    ap.add_argument("--name-authors", type=int, default=0, metavar="N",
                    help="how many authors/editors go into the file name (default: all if 1-2, first only if 3+)")
    ap.add_argument("--author", help="author for the frontmatter and, in the file name, the author slug")
    ap.add_argument("--year", help="year for the frontmatter")
    ap.add_argument("--source", help="source/edition note for the frontmatter")
    ap.add_argument("--sigla", help="turn on alignment anchors with this stem, e.g. basil.dss")
    ap.add_argument("--anchors", action="store_true", help="turn on alignment anchors with an automatic stem")
    ap.add_argument("--para-anchors", dest="para_anchors", action="store_true",
                    help="also number body paragraphs for cross-lingual alignment (needs --sigla/--anchors)")
    ap.add_argument("--no-frontmatter", dest="frontmatter", action="store_false",
                    help="do not add YAML frontmatter")
    args = ap.parse_args()

    pdf = Path(args.pdf)
    doc = pymupdf.open(str(pdf))
    labels, offset_note = page_labels(doc, args.offset, args.roman)
    labels = front_roman_labels(doc, labels)
    if offset_note:
        print(offset_note)
    idx = parse_pages(args.pages, len(doc))
    SMALL, body_size = detect_small_threshold(doc, idx)
    print(f"Body type {body_size} pt; footnote type is anything below {SMALL:.1f} pt.")

    # 1. find running heads, then analyse footnotes, on the original pages
    heads_geo = find_header_rects(doc, idx)
    st = NoteState()
    info = {}
    for pno in idx:
        info[pno] = analyze_page(pno, doc[pno], st, heads_geo[pno])

    # 2. take the footnote areas and running heads out of the body text
    n_heads = 0
    for pno in idx:
        pg = doc[pno]
        rects = ([info[pno][0]] if info[pno][0] is not None else []) + heads_geo[pno]
        n_heads += len(heads_geo[pno])
        for r in rects:
            pg.add_redact_annot(r)
        if rects:
            try:
                pg.apply_redactions(images=0, graphics=0)
            except TypeError:
                pg.apply_redactions(images=0)

    chunks = pymupdf4llm.to_markdown(doc, pages=idx, page_chunks=True)

    # 3. place markers, tidy, strip any remaining running heads/folios
    texts = []
    for k, pno in enumerate(idx):
        _, _, markers = info[pno]
        t = place_markers(chunks[k]["text"], markers, st.warnings, pno)
        texts.append(blocks(tidy(t)))
    heads = find_running_heads(texts)
    pages = [strip_edges(bl, labels[pno], heads) for bl, pno in zip(texts, idx)]

    # 4. finish words split across a page break
    joined = 0
    for i in range(len(pages) - 1):
        if not pages[i] or not pages[i + 1]:
            continue
        last, first = pages[i][-1], pages[i + 1][0]
        m = re.search(r"[A-Za-zÀ-ɏ]-\s*$", last)
        f = re.match(r"\s*([a-zß-ÿ]+)[ \t]*", first)
        if m and f and not first.startswith(("#", ">", "[^")):
            pages[i][-1] = re.sub(r"-\s*$", "", last) + f.group(1)
            rest = first[f.end():]
            if rest.strip():
                pages[i + 1][0] = rest
            else:
                pages[i + 1].pop(0)
            joined += 1

    # 5. repair small-caps headings
    vocab = build_vocab(pages)
    repaired = 0
    for bl in pages:
        for bi, b in enumerate(bl):
            new = "\n".join(repair_line(ln, vocab) for ln in b.split("\n"))
            if new != b:
                repaired += 1
                bl[bi] = new

    # 6. headings, contents, front matter
    pages = polish(pages, [labels[pno] for pno in idx], vocab)

    # 7. assemble
    out, n_notes = [], 0
    for k, pno in enumerate(idx):
        body = "\n\n".join(b.strip() for b in pages[k])
        body = re.sub(r"[ \t]+\n", "\n", body)
        body = re.sub(r"\n{3,}", "\n\n", body)
        if not body.strip():
            body = "*(no text on this page)*"
        defs = []
        for nid, _n in info[pno][1]:
            defs.append(f"[^{nid}]: {render_pieces(st.notes[nid])}")
            n_notes += 1
        if defs:
            body += "\n\n" + "\n\n".join(defs)
        mark = f"[PDF p. {pno + 1}]" if labels[pno].startswith("PDF ") else f"[p. {labels[pno]}]"
        out.append(f"<!-- PDF page {pno + 1} -->\n**{mark}**\n\n{body}")

    final_md = "\n\n---\n\n".join(out) + "\n"
    extra = []
    if n_notes == 0:                                   # e-books with endnotes, licence stamps, lost ligatures
        final_md, extra = ebook_cleanup(final_md)
    # books that print each chapter's notes as an end-of-chapter "Notes" list
    pages2, crep = convert_chapter_endnotes(final_md.split("\n\n---\n\n"))
    if crep:
        final_md = "\n\n---\n\n".join(pages2)
        extra.append(crep)
    nonenglish = detect_language(pages)
    if nonenglish and not PROPER:
        globals()["PROPER"] = build_proper(pages)
    final_md = normalize_headings(final_md, nonenglish)

    # Anthony's conventions: ISO-suffixed name, YAML frontmatter, alignment anchors
    lang = args.lang or detect_lang_code(pages)
    meta = doc.metadata or {}
    sigla = args.sigla or (slugify((args.author or "").split()[-1] if args.author else pdf.stem) if args.anchors else None)
    if sigla:
        final_md = add_anchors(final_md, sigla, para=args.para_anchors)
        extra.append(f"added alignment anchors with stem “{sigla}”" + (" (with paragraph numbers)" if args.para_anchors else ""))
    if args.frontmatter:
        title = args.title or (meta.get("title") or "").strip() or pdf.stem.replace("-", " ").replace("_", " ").title()
        creator = args.author or (meta.get("author") or "").strip()
        final_md = frontmatter(title, creator, args.year, lang, args.source, bool(sigla)) + final_md

    dest = output_name(pdf, args, lang)
    dest.write_text(final_md.translate(LIGATURES), encoding="utf-8")
    print(f"Wrote {dest}: {len(idx)} pages, {n_notes} footnotes, {n_heads} running heads/page numbers removed, "
          f"{joined} page-break words rejoined, {repaired} small-caps heading block(s) repaired")
    for w in extra:
        print("  note:", w)
    for w in st.warnings:
        print("  warning:", w)
    print(f"{len(st.warnings)} warning(s)")


if __name__ == "__main__":
    main()
