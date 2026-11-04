---
id: ossandon-introduzione-conversion-report.en
anchors: "none, and none is wanted: this is apparatus about a work, not a work. The `id` exists so that it is addressable and so that the catalogue stops reporting it as an uncitable source, which it never was."
title: "Ossandón, *Introduzione generale alla Sacra Scrittura* — conversion report"
kind: provenance
about: "ossandon-introduzione.en"
language: en
status: current
note: "Apparatus, not a work: how the English text beside it was converted. It travels with the text (#74)."
characters: 16605
---
# Conversion & repair report

`Introduzione generale alla Sacra Scrittura en-GB.pdf` (321 pp.) converted with **docling 2.117.0**,
then repaired against the Italian first edition.

**Outputs**

| File | What it is |
|---|---|
| `Introduzione generale alla Sacra Scrittura en-GB.md` | The conversion (primary deliverable). |
| `Introduzione generale alla Sacra Scrittura en-GB (corrected).pdf` | The repaired text re-typeset as a PDF. Reflows to 221 pp. — it does **not** reproduce the original page layout. |
| `CONVERSION-REPORT.md` | This file. |

## Docling settings

| Setting | Value | Why |
|---|---|---|
| `do_ocr` | `False` | The PDF has a text layer, and the corruption below is in the **rendered glyphs**, so OCR would reproduce it faithfully while losing italics and footnote-zone separation. |
| `do_table_structure` | `True`, `TableFormerMode.ACCURATE` | Contents, abbreviations, book-list tables. |
| `generate_picture_images`, `generate_page_images` | `False` | No images requested. |
| pdf backend | `docling_parse` (default) | Best layout and footnote-zone separation. |

## Structure recovered

- **210** headings; levels derived from section numbering (`4.1.1.` → `####`).
- **0** footnotes as Markdown footnotes, renumbered globally (the book restarts at 1 on every page); **0** carry an in-text `[^n]` anchor.
- Footnote markers were located by **superscript font metrics** (a 6pt digit inside a 10pt line), not by pattern-matching stray digits.
- Block quotations detected by indentation (x≈113pt vs 72pt body).
- 0 images, 0 base64.

## The English PDF is itself corrupted

It was made by running the Italian through DeepL and re-generating with Aspose.Words. The Italian sets digits as **oldstyle figures** (`/one.oldstyle`) and Greek as `/uniXXXX`; that pipeline mis-mapped the glyphs, so the English PDF **renders wrong characters on the page**:

| Renders as | Should be |
|---|---|
| `199y–2oo2` | `1997–2002` |
| `!1` (page number) | `31` |
| `&ιà yáρτου uαì µέʎανο@` | `διὰ χάρτου καὶ μέλανος` |
| `4.z. Materials` | `4.1. Materials` |
| `15th`, `25th` (page numbers) | `150`, `250` — `0`→`º`, which DeepL then "translated" as an ordinal |

Substitution map derived from page-aligned comparison with the Italian: `y`→7, `!`→3, `o`→0, `z`→1, `$`→3, `s`→3, `ı`→1. Note `y` is genuinely ambiguous — it is 7 in most fonts but **5** in others, which is why heading numbers were taken from the Italian rather than from this map.

## Post-review repairs (four review agents audited the first pass)

| Defect found | Fix |
|---|---|
| 42 footnotes numbered **3** were silently merged into footnote 2 — a footnote 3 renders as `!`, and the splitter required a literal digit | number matching now accepts corrupted glyphs, and footnote starts are confirmed by hanging-indent geometry (first line x=72, continuations x=89.5) |
| Page-leading continuation fragments were minted as new footnotes, truncating their parent | they are now appended to the previous page's last note |
| Markers were paired to notes by ordinal position, so one bad match shifted every later anchor | markers are paired by their own **digit value** |
| Superscripts that are not footnote markers (`P52`, `NA27`, verse numbers, a 5pt letter `o`) were consumed as markers, in two cases deleting a character | 18 rejected by validating the value against the page's actual footnote numbers |
| `s`→3 corrupted correct English: "the 1960s" became "the 19603" | the numeric pass no longer maps `s` (headings still do) |
| A duplicate reference pair applied twice, yielding `Acts 1:133,21-26` | replacement is de-duplicated and refuses to match inside an already-corrected reference |
| **Page 29 produced no output at all** — docling classified the whole page as a picture | pages that emit nothing are recovered from the text layer (3 pages, incl. the Egypt/Israel/Mesopotamia chronology chart) |
| 222 bibliography entries lost their leading author initial (docling read `S.` as a list bullet) | 97 restored by re-matching against the PDF line |
| 3 headings dropped to level 1 because glyph residue (`8.1.3.!.`) defeated the level parser | residue stripped before parsing |
| ~17 sentence fragments, diagram labels and bibliography lines were emitted as level-1 headings | 12 demoted to paragraphs |
| `*Title *` is not valid CommonMark emphasis (117 occurrences) | space before the closing delimiter removed |
| docling repeats a spanned table cell across every column | duplicate cells collapsed, empty columns dropped |

## Repairs applied

Pagination is **1:1 across all 321 pages** between the editions, which made page-level alignment reliable.

| Repair | Count |
|---|---|
| Greek/Hebrew runs restored from the Italian | 75 |
| Heading numbers corrected | 76 |
| Scripture references with dropped digits recovered | 19 |
| Headings recovered from misclassification | 8 |
| Headings re-inserted from the table of contents | 2 |

Greek/Hebrew replacements were accepted only when the surviving real Greek letters agreed with the Italian (this rejected 11 same-length but wrong alignments). Scripture references were accepted only when the book abbreviations corresponded across languages (`Ex`/`Es`, `John`/`Gv`) — e.g. `Ex 1:18` → `Ex 31:18`, `Mt 5:1` → `Mt 5:17`.

## Known remaining problems

### 1. Digits dropped outside scripture references

Some digits vanished rather than being substituted, leaving a number that still looks valid — e.g. `pp. 1–100, especially pp. 1–8` should be `71–100` and `71–78`. Inside `Book ch:v` references these were recoverable because the book name anchors the alignment; **in free-running text they were not**, since a lone `1` could be `21`, `31`, `71` or `171`. These are left as-is rather than guessed at.

### 2. 35 Greek/Hebrew runs still garbled

Where alignment with the Italian was not confident enough to justify a replacement. Listed below.

### 3. 10 footnotes without an in-text anchor

The footnote text is preserved in full; only the `[^n]` marker position could not be located.

### 4. DeepL translation artefacts (not repaired — these are translation, not encoding, defects)

- Running headers alternate between "Part I: The Bible and **Revelation**" and "…and **Revival**".
- Some TOC titles disagree with the body: TOC "7. The Parable of the Lost Sheep" vs body "7. The Word of God in History" (the Italian reads *La parola di Dio nella storia*).
- "11. INTRODUCTION: THE FIRST BOOKS OF THE DECADE" mistranslates *i libri prima della stampa* ("books before printing").
- Occasional dropped words, e.g. "in apostolic pre tion" for "preaching".

## Appendix A — headings recovered

These exist in the PDF but docling had classified them as body text, caption or code:

| Page | Number | Heading |
|---|---|---|
| 90 | 9.1 | 9.1. The teaching of Jesus |
| 103 | 10 | 10. Revelation and Inspiration |
| 107 | 10.2 | 10.2. Inspiration within the framework of revelation and its |
| 113 | 11.1 | 11.1. The study of textual variants |
| 133 | 15.1 | 15.1. The main ancient versions |
| 164 | 17.2 | 17.2. The criteria of canonicity and the apostolicity of the |
| 255 | 24.2 | 24.2. Author - text - reader. God as author and the importan |
| 271 | 27.2.1 | 27.2.1. The Eleven sent by Jesus (Mt 28:16-20; |

These are **absent from the English PDF altogether** and were re-inserted from its table of contents:

| Page | Number | Title |
|---|---|---|
| 112 | 11 | INTRODUCTION: THE FIRST BOOKS OF THE DECADE |
| 119 | 12.1 | The text in Hebrew |

## Appendix B — scripture references corrected

| Page | Was | Now |
|---|---|---|
| 22 | `John 2:9` | `John 20:9` |
| 27 | `Ps 8:1` | `Ps 78:1` |
| 30 | `Ex 1:18` | `Ex 31:18` |
| 30 | `Ex 4:18` | `Ex 34:18` |
| 45 | `Luke 2:17` | `Luke 23:17` |
| 57 | `Tim 1:1` | `Tim 1:17` |
| 57 | `Mt 11:2` | `Mt 11:27` |
| 65 | `Heb 2:1` | `Heb 2:17` |
| 93 | `John 1:18` | `John 13:18` |
| 97 | `Mt 5:1` | `Mt 5:17` |
| 97 | `Lk 24:2` | `Lk 24:27` |
| 116 | `Sam 1:1` | `Sam 13:1` |
| 136 | `Sam 1:1` | `Sam 13:1` |
| 172 | `Acts 2:8` | `Acts 23:8` |
| 245 | `Josh 1:22` | `Josh 13:22` |
| 245 | `Neh 1:2` | `Neh 13:2` |
| 270 | `John 1:16` | `John 13:16` |
| 273 | `Acts 1:1` | `Acts 1:13` |
| 277 | `Acts 1:1` | `Acts 1:13` |

## Appendix C — Greek/Hebrew still unresolved

(Five of the garbled spans quoted below contained raw NUL bytes (U+0000), reproduced verbatim from the docling output. Recorded here as ␀ (U+2400) since 2026-08-28 (#90): a raw NUL makes the whole file binary to git and invisible to grep, and the byte's presence in the conversion is what matters, not the byte itself.)

| Page | Garbled text |
|---|---|
| 32 | `χάρτης).␀Qumran` |
| 51 | `&ιá` |
| 51 | `suτο@` |
| 51 | `pαuτí(m έν u&ατι` |
| 91 | `οúu` |
| 91 | `θον uατα` |
| 104 | `τ2ν τοũ uυρíου` |
| 104 | `íτσοũ xριστοũ &úναµιν uαì uαρουσíαν` |
| 105 | `uνsúµατο@ áγíου φsρóµsνοι έ` |
| 105 | `цσαν` |
| 105 | `θsοũ ắνθρmuοι` |
| 105 | `τà &υνáµsνá σs σοφíσαι` |
| 105 | `σmτцρíαν` |
| 106 | `uρò@ &ι&ασuα` |
| 106 | `íαν, uρò@ έ` |
| 106 | `sγµóν, uρò@ έuανóρθmσιν, uρò@ uαι&síαν τ2ν έν &ιuαιοσúνy` |
| 118 | `θsò@ έν τq Eµέρą τq έuτy τà έργα αúτοũ, ầ␀ἐποίησεν]␀The` |
| 154 | `έργáτц@ τοũ µισθoũ αúτοũ].'␀The` |
| 154 | `έργáτц@ τί@ τροφί@ αúτοũ` |
| 179 | `uατà τ2ν ἐπίπνοιαν τ2ν` |
| 189 | `usíµsνον έν τy Épραϊuy, τq &έ τοũ Tmp2τ` |
| 189 | `έγουσιν οí έu usριτοµί@` |
| 190 | `οµĩno@ Παροιµíαι` |
| 190 | `uαì zοφíα` |
| 190 | `uαρ' Épραíοι@` |
| 208 | `έu uíστsm@` |
| 211 | `Éρµί@` |
| 244 | `οi uατ' έuστασιν τĩν έν αúτοĩ@` |
| 244 | `uαì αú` |
| 244 | `цτ2@ αú` |
| 244 | `òν έµuνsúσαι` |
| 268 | `áuóστο` |
| 268 | `ο@` |
| 270 | `&έ áuóστο` |
| 270 | `πέμπω):␀Jesus` |

## Appendix D — number repairs not confirmed against the Italian

Applied via the substitution map, but the result was not found among that page's Italian numbers.

| Page | Was | Now |
|---|---|---|
| 17 | `2o12` | `2012` |
| 17 | `2o16` | `2016` |
| 17 | `2o16` | `2016` |
| 26 | `58y` | `587` |
| 44 | `196!` | `1963` |
| 45 | `194!` | `1943` |
| 56 | `11!` | `113` |
| 142 | `15y161` | `157161` |
| 163 | `16y` | `167` |
| 163 | `6y` | `67` |
| 163 | `19o` | `190` |
| 166 | `202!` | `2023` |
| 173 | `1!11!5` | `131135` |
| 178 | `1!2` | `132` |
| 178 | `1!5` | `135` |
| 180 | `1y` | `17` |
| 191 | `19!` | `193` |
| 191 | `19y` | `197` |
| 194 | `14y` | `147` |
| 195 | `zy22` | `1722` |
| 195 | `zy22` | `1722` |
| 198 | `zy46` | `1746` |
| 198 | `669!` | `6693` |
| 198 | `2yy299` | `277299` |
| 215 | `y688` | `7688` |
| 237 | `22!` | `223` |
| 249 | `19419y` | `194197` |
| 263 | `2y` | `27` |
| 265 | `2y` | `27` |
| 272 | `4!` | `43` |
| 272 | `!5` | `35` |
| 304 | `1y` | `17` |
| 306 | `2o1y` | `2017` |
| 313 | `2oo9` | `2009` |
| 315 | `2o1y` | `2017` |
| 316 | `196!` | `1963` |

## Appendix E — heading numbers changed

| Page | Was | Now | Source | Heading |
|---|---|---|---|---|
| 20 | `ı` | `1` | italian | ı. The Names of the Bible |
| 25 | `$` | `3` | italian | $.  Historical Background |
| 30 | `4.z` | `4.1` | italian | 4.z. Materials |
| 38 | `y.z` | `5.1` | italian | y.z. The Hebrew Bible |
| 41 | `y.2` | `5.2` | italian | y.2. The Old Testament |
| 43 | `y.s` | `5.3` | italian | y.s. The twenty-seven books of the New Testament |
| 44 | `y.4` | `5.4` | italian | y.4. Chapters and verses |
| 45 | `6.z` | `6.1` | italian | 6.z. Introduction |
| 48 | `6.2.1` | `6.2.3` | italian | 6.2.1.  Two special cases: Daniel and Esther |
| 50 | `6.s` | `6.3` | italian | 6.s.  New Testament |
| 55 | `y.z` | `7.1` | italian | y.z. Why study Dei Verbum ? |
| 56 | `y.2` | `7.2` | italian | y.2. Theme and structure of Dei Verbum |
| 57 | `y.s` | `7.3` | italian | y.s. Revelation and its economy (DV2) |
| 58 | `y.!.1` | `7.3.1` | italian | y.!.1. Deeds and words |
| 60 | `y.!.2` | `7.3.2` | italian | y.!.2.  Revelation and history |
| 62 | `y.4` | `7.4` | italian | y.4. Revelation in DVs |
| 63 | `y.y` | `7.5` | italian | y.y. Jesus Christ, Mediator and Fulness of all rev |
| 70 | `8.z` | `8.1` | map | 8.z. Orality and writing |
| 72 | `8.1` | `8.1.3` | italian | 8.1. !. Communicative effectiveness (advantages an |
| 86 | `8.2.1` | `8.2.3` | italian | 8.2.1. The Lutheran principle of sola Scriptura |
| 97 | `9.s` | `9.3` | italian | 9.s. The mutatio scripturarum : the Scriptures as |
| 103 | `zo.z` | `10.1` | map | zo.z. Biblical testimonies on inspiration |
| 104 | `1.1.1` | `10.1.1` | italian | 1.1.1. The Spirit and the Scriptures (1 Peter 1; 2 |
| 105 | `1.1.2` | `10.1.2` | italian | 1.1.2. Inspired Scripture (2 Timothy !) |
| 115 | `zz.2` | `11.2` | italian | zz.2. Some examples of textual variants |
| 126 | `12.2.1` | `12.2.3` | italian | 12.2.1. Critical editions |
| 127 | `ı$` | `13` | italian | ı$. The text of the New Testament |
| 128 | `zs.z` | `13.1` | italian | zs.z. Textual witnesses |
| 129 | `zs.2` | `13.2` | italian | zs.2. Variants |
| 130 | `zs.s` | `13.3` | italian | zs.s. Critical editions |
| 137 | `zy.2` | `15.2` | italian | zy.2. Modern versions |
| 141 | `15.2.1` | `15.2.3` | italian | 15.2.1. Some modern Bibles worth knowing |
| 144 | `6` | `16` | italian | 6.  An Introduction to the Problem of the Biblical |
| 144 | `16.z` | `16.1` | italian | 16.z. Some terminological clarifications |
| 148 | `16.s` | `16.3` | italian | 16.s. The Gospel of Thomas |
| 153 | `zy.z` | `17.1` | italian | zy.z. Key historical evidence regarding the format |
| 156 | `17.1.!` | `17.1.3` | italian | 17.1.!. St Justin |
| 161 | `17.1.y` | `17.1.7` | italian | 17.1.y. Debates in the third and fourth centuries: |
| 168 | `18.z` | `18.1` | italian | 18.z. The Scriptures of Israel before Jesus |
| 171 | `18.1.1` | `18.1.3` | italian | 18.1.1. The translation of the Torah and other boo |
| 178 | `18.s` | `18.3` | italian | 18.s. Among the Jews at the end of the first centu |
| 179 | `18.!.1` | `18.3.1` | italian | 18.!.1. The twenty-two books according to the test |
| 182 | `18.!.2` | `18.3.2` | italian | 18.!.2. The ninety-four books (24 + yo) according |
| 188 | `18.y` | `18.5` | italian | 18.y. The formation of the Old Testament canon in |
| 194 | `9` | `19` | italian | 9.  The modern debate surrounding the canon |
| 194 | `19.z` | `19.1` | italian | 19.z. Luther and the Canon |
| 198 | `19.s` | `19.3` | italian | 19.s. The Biblical Canon at the Council of Trent ( |
| 198 | `19.!.1` | `19.3.1` | italian | 19.!.1. The list |
| 199 | `19` | `19.3.2` | italian | 19. !.2.  The anathema |
| 205 | `2` | `20` | italian | 2.  The Interpretation of Texts in General |
| 205 | `20.z` | `20.1` | italian | 20.z. What does it mean to interpret? |
| 207 | `2.2` | `20.2` | italian | 2.2. Some examples of difficult texts |
| 208 | `20.s` | `20.3` | italian | 20.s. Philosophical hermeneutics |
| 211 | `2.4` | `20.4` | italian | 2.4. The distance between author and reader |
| 215 | `21.z` | `21.1` | italian | 21.z. The Church as the original locus of biblical |
| 215 | `2.2` | `21.2` | italian | 2.2. Principles for Interpretation (DV 2) |
| 221 | `21.2.!` | `21.2.3` | italian | 21.2.!. Analogy of Faith |
| 223 | `2.s` | `21.3` | italian | 2.s. The Role of the Magisterium in Interpretation |
| 227 | `22.z` | `22.1` | italian | 22.z. The truth for our salvation (DVzz) |
| 235 | `22.2.1` | `22.2.3` | italian | 22.2.1. At a philosophical level: knowledge of the |
| 239 | `22.s` | `22.3` | italian | 22.s. The 'obscure' passages of the Bible |
| 243 | `2s.z` | `23.1` | italian | 2s.z. Inadequate models due to insufficient consid |
| 243 | `2.1.1` | `23.1.1` | italian | 2.1.1. Inspiration as ecstasy |
| 246 | `2.1.2` | `23.1.2` | italian | 2.1.2. Mechanical Dictation and Fundamentalism |
| 247 | `2s.2` | `23.2` | italian | 2s.2. Inadequate models due to insufficient consid |
| 250 | `24.z` | `24.1` | italian | 24.z. The notion of the instrumental cause and hag |
| 263 | `27.z` | `25.1` | italian | 27.z. Scripture in Origen's *De principiis* |
| 265 | `27.2` | `25.2` | italian | 27.2. St Augustine's *De doctrina christiana* |
| 269 | `27.z` | `27.1` | italian | 27.z. Etymology of the word and its use in John an |
| 274 | `27.s` | `27.3` | map | 27.s. 'Apostle' in Paul's letters |
| 278 | `27.y` | `27.5` | italian | 27.y. Other characteristics of the apostles |
| 283 | `29.z` | `29.1` | italian | 29.z. References to the written Torah in the Penta |
| 286 | `29.1` | `29.1.3` | italian | 29.1. !.  The Book of the Torah and the Pentateuch |
| 290 | `29.2.1` | `29.2.3` | italian | 29.2.1.  Ezra and the Proclamation of the Torah |
| 293 | `$o` | `30` | italian | $o.  The word 'prophet' |
| 296 | `$ı` | `31` | italian | $ı. The value of the other books of the Old Testam |
