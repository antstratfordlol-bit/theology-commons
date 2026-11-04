---
id: ossandon-introduzione-repair-report.en
anchors: "none, and none is wanted: this is apparatus about a work, not a work. The `id` exists so that it is addressable and so that the catalogue stops reporting it as an uncitable source, which it never was."
title: "Ossandón, *Introduzione generale alla Sacra Scrittura* — second repair report"
kind: provenance
about: "ossandon-introduzione.en"
language: en
status: current
note: "Apparatus, not a work: the 1,323 verified fixes of the second repair pass. It travels with the text (#74)."
characters: 7588
---
# Repair report — *A General Introduction to Holy Scripture* (English study edition)

Second repair pass, 8 August 2026. Inputs: the English PDF (321 pp.), the Italian first
edition (321 pp., 1:1 pagination), and the previous conversion's markdown.

**Outputs**

| File | What it is |
|---|---|
| `Introduzione generale alla Sacra Scrittura en-GB (repaired).pdf` | 222 pp., re-typeset (XeLaTeX / TeX Gyre Pagella, polytonic Greek and pointed Hebrew in FreeSerif). |
| `Introduzione generale alla Sacra Scrittura en-GB (repaired).md` | The same text as markdown, with an anchor-linked contents list. |
| `Dei Verbum.pdf` | The constitution, vatican.va English, 41 footnotes, clickable TOC. |
| `Benedict XVI - Tradition (3 Audiences).pdf` | The audiences of 26 Apr, 3 May and 10 May 2006 in one file. |

The originals were left in place; nothing was overwritten.

## 1. The table of contents

The old front matter was the printed book's contents page, which docling had read as a
five-column table. It carried the 2021 edition's page numbers, which no longer matched
anything after the text reflowed, and it had no links. It also disagreed with the body in
several places, because DeepL had translated the same heading twice — the TOC said
"7. The Parable of the Lost Sheep" where the body said "7. The Word of God in History"
(Italian: *La parola di Dio nella storia*).

That table was deleted. The contents are now generated from the body's own headings, so
they cannot drift. **All 195 entries were verified to link to exactly the page they
print.** The PDF bookmark tree matches, and the running heads now carry the current
chapter and section instead of repeating a line of the old TOC.

## 2. Headings

Titles were checked against the Italian contents (pp. 5-10) and corrected: `7.4. Revelation
in DVs` → `in DV 3`; `8.2. … (DVy-zo)` → `(DV 7-10)`; `10.1.2. Inspired Scripture (2 Timothy!)`
→ `(2 Timothy 3)`; `19.3.2.!.2. The anathema` → `19.3.2.`; `22.1. … (DVzz)` → `(DV 11)`;
`30. The word 'prophet'` → `The prophetic word`; `PART I THE BIBLE AND REGENERATION` →
`REVELATION`. Truncated titles (24.2, 27.2.1) were completed, and the two mangled Excursus
titles restored. Five lines of body text that had been misread as chapter headings were
demoted, a duplicated heading for section 11 removed, and the bibliography front matter put
back into the Italian's order (*Indicazioni bibliografiche* → *Nota* → *Manuali* → …).

The abbreviations table and the list of biblical books had lost whole cells in conversion
(`NJBC The New Jerome` with no "Biblical Commentary", `1 Sam` with no name, and so on).
Both were rebuilt from Italian pp. 11-13.

## 3. Greek and Hebrew

All 80 lines carrying Greek or Hebrew were realigned to the Italian page and repaired —
**52 runs**, including the 35 the previous pass had left unresolved. `&ιà yáρτου uαì
µέʎανο@` is now διὰ χάρτου καὶ μέλανος; `uá ʎ in`/`mám` (the etymology of *palimpsest*)
is now πάλιν/ψάω. Hebrew that had been emitted in visual rather than logical order was
reversed. No garbled run remains: a scan for Latin letters and stray symbols adjacent to
Greek characters returns nothing.

## 4. Text repairs

**1,323 verified substitutions**, each one checked to match its line exactly once before
being applied.

| Class | n |
|---|---|
| Glyph and number corruption | ~500 |
| Broken words, lost text, misplaced footnote markers | ~330 |
| Scripture set to RSV Catholic Edition | ~105 |
| Magisterium set to the official English | ~85 |

**Numbers.** The Italian sets oldstyle figures, which the pipeline mapped to letters
(`y`=7, `o`=0, `z`=1, `!`/`$`=3). Every numeric change was confirmed against the Italian
page. Some samples: `199y- 2oo2` → 1997-2002; Luther `(14811546)` → (1483-1546); Jerome's
whole chronology, which was out by two centuries (born 145 → **347**, Vulgate begun 190 →
**390**); the Letter of Aristeas' *twenty* elders → **72**; the NT manuscript counts
`around 100 … only 14` → **300 … 34**; the Neovulgate promulgated 1989 → **1979**;
`Excursus!, pp. 281-!oo` → Excursus 3, pp. 281-300. Roughly 80 scripture references had
lost a digit — `Mt 5:1` → 5:17, `Acts 1:1` → 1:13, `Jer 21:29` → 23:29.

**Meaning errors** that the numbers exposed: "All of them received a truly apostolic
mission" was a negation dropped from *non tutti* — and the sentence turned out to be a
stray fragment of footnote 359, so it was deleted; "they are not part of **the Bible**"
should read "the **BH**", which is the whole point of the argument; "Heinrich
**Schleiermacher**, a disciple of Bultmann" is Heinrich **Schlier**.

**Scripture.** Quoted passages had been DeepL'd out of the Italian CEI. They now carry the
RSV-CE, with the author's bracketed Greek and his own ellipses kept in place. Passages
where he is deliberately quoting something else — the LXX, the Vulgate, the Neovulgate, a
manuscript variant, or the CEI itself as the object of discussion — were **not** touched;
they are listed in §5.

**Magisterium.** *Dei Verbum* (about forty quotations), *Verbum Domini*, the Catechism,
*Providentissimus Deus*, *Divino Afflante Spiritu*, *Donum veritatis*, *Aperuit illis*,
*Scripturae Sacrae affectus*, Trent's decree, and the PBC documents now read as their
official English. Latin quotations that DeepL had silently translated — thirteen footnotes
and Trent's canon of Scripture — were restored to Latin from the Italian.

**Characters.** No replacement characters, control characters, non-breaking spaces or soft
hyphens remain. Fixed: 160 phonetic-extension small-capital letters, 24 broken emphasis
delimiters (`*Title *`), doubled commas, spaces before punctuation, `DV12` → `DV 12`
throughout, empty quote pairs left by dropped italics, spaced-out words (`a n d`), and
words broken across the original page breaks (`in apostolic pre tion` → preaching).

**Footnotes.** All 381 definitions now have an anchor — ten had lost theirs and would have
been dropped silently. About twenty markers that sat on the wrong sentence were moved,
each confirmed by matching the note's content to the Italian page.

## 5. Known remaining problems

- **Deliberately not RSV-CE.** 2 Cor 8:23 ("delegates", the author's point), Rom 1:17
  ("from faith to faith", on which five interpretations hang), Rom 16:7 (Junia), Lk
  23:16-18 and Ps 2:9 (quoted as CEI), Mk 3:13-14 (quoted for a variant), and the whole
  textual-criticism chapter, where the witnesses are the subject.
- **Vocabulary now split between quotation and commentary.** Official DV 12 says "literary
  forms" and "the harmony which exists between elements of the faith"; the author's
  surrounding prose says "literary genres" and "analogy of faith". Same for DV 7's
  "by example, and by observances" against his "examples and institutions". Replacing his
  commentary too would have meant rewriting him — worth an editorial decision.
- **Not sourced.** John Paul II's address of 23 April 1993 (no English on vatican.va);
  *Fides et Ratio* 84; Vatican I's *Dei Filius* in English; a truncated Origen quotation in
  footnote 192, which breaks off mid-sentence in the English and needs re-translating from
  Italian p. 161.
- **Figures not reconstructible as text**: the written-communication diagram (Italian
  p. 71), the DV 7 transmission schema (p. 81), and the two-column Latin schema of DV 2b.
- **Probably wrong in the Italian itself**, so left alone: Sixtus V "elected in 1575"
  (1585); "pp. 72-72"; `Mt 11,22` where 11:27 is meant.
- Foreign-language book titles and French/Spanish quotations that DeepL rendered into
  English are left as English.
