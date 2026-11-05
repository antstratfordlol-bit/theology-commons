# pdf2md: PDF to Markdown for Scholarly Books

`pdf2md.py` converts a PDF of a scholarly book into clean Markdown that keeps:

- the **book’s own page numbers**, marked `**[p. 47]**` (not the PDF’s page numbers);
- **real Markdown footnotes**: `[^c01-49]` in the text and `[^c01-49]: …` under the page that cites it;
- tidy **headings** (Title Case for English, sentence case for Italian, Spanish and other languages);
- repaired text: running heads and folios removed, split words rejoined, ligatures normalised, small-caps headings fixed;
- file names, YAML frontmatter and (optionally) paragraph anchors following the project conventions below.

It works with page-foot footnotes, with chapter-end “Notes” lists, and with e-book style endnotes at the back of the volume. All of these are turned into footnotes placed under the page that cites them.

## Setup (Once)

```bash
cd ~/Documents/Research/pdf-convert        # any folder you like
python3 -m venv .venv
.venv/bin/pip install pymupdf pymupdf4llm
```

Put `pdf2md.py` and the PDF in that folder.

## Basic Use

```bash
cd ~/Documents/Research/pdf-convert
.venv/bin/python pdf2md.py book.pdf
```

If the page numbers come out wrong (see the next section), add `--offset`:

```bash
.venv/bin/python pdf2md.py book.pdf --offset 15
```

Always test a few pages first; it takes seconds:

```bash
.venv/bin/python pdf2md.py book.pdf --offset 15 --pages 60-65
```

## What `--offset` Means

A PDF counts its pages from 1 at the very first page (cover, title page, roman-numeral front matter, and so on). A book counts from the page where its main text starts. **The offset is the PDF page on which printed page 1 falls.**

Example: you open the PDF, scroll to the first page that is printed “1”, and your viewer says it is PDF page 15. Then:

```bash
.venv/bin/python pdf2md.py book.pdf --offset 15
```

The script then labels PDF page 15 as `[p. 1]`, PDF page 16 as `[p. 2]`, and so on. Pages before it are labelled as front matter.

How to find it: open the PDF, go to the first page whose printed number is 1, and read the PDF page number in the viewer’s page box (not the printed one).

You often do not need it. The script first reads the PDF’s embedded page labels, then looks for printed folios at the top or bottom of the pages and works out the offset itself. Use `--offset` when the labels are missing or wrong, or when the first run shows page numbers that do not match the printed ones. Add `--roman` to label the pages before the offset i, ii, iii…

## Options

| Option | Purpose |
|---|---|
| `--offset N` | PDF page on which printed page 1 falls |
| `--roman` | with `--offset`: label earlier pages i, ii, iii… |
| `--pages 60-65` | convert only these PDF pages (for testing) |
| `-o FILE` | output path (default: next to the PDF) |
| `--slug`, `--lang` | set the file-name slug or the language code by hand |
| `--title`, `--author`, `--year`, `--source` | values for the frontmatter |
| `--name-authors N` | how many authors go into the file name (default: all if 1–2, first only if 3 or more) |
| `--sigla STEM` | turn on alignment anchors with this stem, e.g. `basil.dss` |
| `--anchors` | turn on anchors with an automatic stem |
| `--para-anchors` | also number body paragraphs |
| `--no-frontmatter` | omit the YAML block |

## Output Conventions

**File name.** `<author-surnames>-<title-slug>.<lang>.md`: lowercase Latin letters, hyphens, ISO language code (`la`, `grc`, `en`, `es`, `it`…). One or two authors are both named; three or more, the first only. Apostrophes are dropped (O’Callaghan becomes `ocallaghan`). Example: `ocallaghan-children-of-god-in-the-world.en.md`. Separate several authors with a semicolon: `--author "Matthew Lamb; Matthew Levering"`.

**Frontmatter.**

```yaml
---
title: "The Reception of Vatican II"
creator: "Matthew L. Lamb; Matthew Levering"
year: 2017
language: en
source: "Oxford University Press (2017)"
anchors: false
---
```

Title and creator come from the PDF’s metadata unless you pass `--title` and `--author`; the language is detected.

**Anchors (optional).** With `--sigla basil.dss`, every heading gets a stable id, e.g. `### Chapter 1 {#basil.dss.1}`; with `--para-anchors`, paragraphs are numbered `[1]{#basil.dss.1.1} Text…`. The same stem across editions or translations lets the texts be aligned.

**Full example.**

```bash
.venv/bin/python pdf2md.py book.pdf --offset 15 \
  --title "The Reception of Vatican II" \
  --author "Matthew Lamb; Matthew Levering" \
  --year 2017 --source "Oxford University Press (2017)"
```

## When the First Run Is Not Good Enough

PDFs differ a great deal, so the first run is often good but not perfect. Check these things in the output:

1. Page numbers match the printed ones (otherwise correct `--offset`).
2. Footnote markers `[^…]` sit in the text, and there are no stray `<sup>` tags or numbers glued to words.
3. Headings are right and in the right case.
4. No running heads or page numbers left inside the text.

Count what remains:

```bash
grep -c '<sup>' file.md              # unconverted note markers
grep -o '\[\^[^]]*\]:' file.md | wc -l   # footnote definitions
```

Some markers are simply absent from a PDF’s text layer (typically a handful per book); they cannot be attached automatically.

### Second Pass: A Prompt for Claude Code

If problems remain, open Claude Code in the same folder and paste this, replacing the file name:

```text
I converted a PDF to Markdown with pdf2md.py. Read file.md and check it against file.pdf.
Do not rewrite the text. Find and fix only conversion errors:

1. Page markers: check that **[p. N]** matches the printed page numbers in the PDF
   at five or six places (front matter, middle, end).
2. Footnotes: list any <sup> tags or bare numbers that should be markers, any
   [^id] without a definition, and any definition without a marker. Attach them
   where the PDF shows them.
3. Headings: fix levels and capitalisation (Title Case for English only; sentence
   case for other languages) and remove running heads that became headings.
4. Residue: remove running heads, folios, licence stamps and repeated lines left
   in the text; rejoin words split across lines or pages.
5. Do not change wording, spelling or punctuation of the author’s text. Use curly
   quotation marks.

Make the changes in a copy named file.clean.md. Then report briefly: what you
changed, how many items, and what you could not resolve.
```

If the same kind of error appears in many places, it is a pattern the script itself should learn. Ask Claude Code to fix `pdf2md.py` rather than the output, then re-run, so every later book benefits (“Why does this happen? Please fix it in pdf2md.py and show me that earlier books still convert identically”).

## Known Limits

- Scanned books need OCR first; the script reads the PDF’s text layer.
- A few note markers missing from the text layer stay unattached (reported as leftover `<sup>`).
- Anchors follow the heading tree of the converted book; they are not tied to any external edition’s numbering.
- `source` is never auto-detected: pass `--source`.
- EPUB files do not go through this script; use Pandoc for them.
