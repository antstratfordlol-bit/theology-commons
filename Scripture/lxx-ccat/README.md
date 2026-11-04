# lxx-ccat — the Septuagint, Rahlfs (1935), CATSS text from CCAT

> **Terms of use — read before using or passing this on.** The text is held under CCAT's user declaration (the full text is in the originals store beside the source files): non-commercial study use, access controlled by the holder, and **anyone supplied with any portion of it is asked to register a signed agreement with CCAT**. It is committed to this library and ships in the shared copy on the owner's permission of 2026-09-14 (*"i give you permission to commit, both here and in the kit, the various bibles"*, `decisions.md`). That permission is his; it does not change what CCAT asks of each recipient.

**59 books, 1,188 chapters, 30,603 numbered verses**, one file per book. Taken 13–14 September 2026 under tracker #41, on Alex's answer 15a of 21 August: *"(a) Sign the declaration, take the complete tagged text"*, recorded as decided because signing a free academic declaration is not a purchase.

| | |
|---|---|
| **Source** | The CATSS morphologically analysed Septuagint (LXXM), distributed by the Center for Computer Analysis of Texts (CCAT), University of Pennsylvania: 64 `.mlxx` files from `https://ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/`, fetched 2026-09-13 |
| **Text** | *Septuaginta*, ed. A. Rahlfs (Stuttgart: Württembergische Bibelanstalt, 1935), in the computer form prepared by the TLG and verified by CATSS (the CCAT `0-readme.txt`) |
| **Originals** | `01. Sources/_originals/Scripture/lxx-ccat/`: the 64 files and CCAT's `0-user-declaration.txt`, `0-readme.txt`, `*ReadMe.Analysis`, `*Morph-Coding`, `0-betacode.txt`. CCAT publishes no checksum; each file matched the size its directory listing gives |
| **Terms** | CCAT User Agreement/Declaration, version 050215 — below, and `04. Reference/rights-register.md` row L15 |
| **Language** | `grc` |
| **Anchors** | `{#lxx.Gen.1.1}` — **a numbering space of its own**, never the bare OSIS anchors, because Rahlfs's numbering is a different system: the Greek psalm numbers (`lxx.Ps.22.1` is Hebrew Psalm 23:1), the Greek order of Jeremiah, Greek chapter order in Proverbs |
| **Converter** | `99. Tools/hebrew-greek/convert_lxx_ccat.py`; why not odtake: `99. Tools/hebrew-greek/README.md` |

## The terms, verbatim where it matters

From `0-user-declaration.txt`: *"In accepting materials distributed by or through CCAT, the recipient agrees to observe the following 'fair use' provisions: (1) Not to use or make available these materials for commercial purposes without first obtaining the written consent of the owners/encoders; (2) To observe any special restrictions that may govern the use of particular texts … (3) To control access to these materials and require any other party to whom the recipient supplies any portion of this material to observe these conditions and to register a signed USER AGREEMENT form with CCAT; (4) When making formal public reference to the materials, to acknowledge appropriately the holder of the copyright to any published text that has been encoded as well as to the encoder and the source … (5) To report promptly to CCAT any errors discovered …"* The form ends with lines for signature, name, address and the texts obtained.

From `0-readme.txt`: the files are *"for the use of students, teachers and scholars in study and education contexts … If copies are made and given to other persons for NON-COMMERCIAL use, those persons are also required to register with CCAT by completing the standard 'User Declaration' … This is for legal and collaborative purposes only; no fees are involved."*

**What this means here.** Private study in this repository is inside the terms. The private backup at `github.com/jordan-alex/OD` is access-controlled and Alex's own. **The kit supplies it to other people**, who have not registered; Alex gave permission on 2026-09-14 to commit the shelf and ship it in the kit (`decisions.md`), and each recipient reads CCAT's terms above. **The declaration itself has not been signed or sent**: that is Alex's act, and the text has been taken on his decision of 21 August to sign it.

## What the reading text is

The **word column** of the CATSS analysis, converted here from Beta Code to Unicode Greek (NFC):

- Rahlfs's word forms, accents and breathings. **CATSS removed punctuation, brackets and the capital at the start of a sentence** (`*ReadMe.Analysis` §C.1), so this text has none; proper nouns keep their capital. It is a text to search and to read a verse in, not a typeset edition.
- The conversion was checked by counting letters and marks on both sides: they agree exactly in every book (3,075,591 letters). Beta Code `#` (numeral sign) is `ʹ`, `'` (elision) is `’`.
- **The morphological analysis is not in the Markdown**: type, parse and lemma columns stay in the source files.

## What the numbering carries, all declared in each file

- **Two text forms of one book are two files**, since each has its own numbering: `JoshB` and `JoshA` (the A text only in the portions Rahlfs prints), `JudgB`/`JudgA`, `TobBA`/`TobS`, `DanOG`/`DanTh`, `SusOG`/`SusTh`, `BelOG`/`BelTh`.
- **Kingdoms** keep OSIS book codes with the Greek names in the title: `1Sam` = 1 Kingdoms, `1Kgs` = 3 Kingdoms. **2 Esdras** (`2Esdr`) is Ezra and Nehemiah under one numbering, 23 chapters, and is not split; **1 Esdras** is `1Esd`.
- **Lettered verses** as Rahlfs prints them (`lxx.Esth.1.1a`, `lxx.1Kgs.2.35a`): 267.
- **Joint verses** printed as one (`Sus 7/8`, `Jer 7:27/28`, `Bel 15-17`) are anchored as ranges, `lxx.SusOG.1.7-8`, and labelled as printed: 11.
- **One-chapter books** (Obadiah, Letter of Jeremiah, Susanna, Bel): the source numbers verses only; chapter 1 is supplied in the anchor on the OSIS convention and declared.
- **Unnumbered text** Rahlfs prints before a numbered verse — the titles of the Odes and of the Psalms of Solomon, the prologue of Lamentations, the preface to Daniel 5 (Old Greek), the superscription of Bel — is anchored `.pre` under its chapter (`lxx.Odes.9.pre`): 34.
- **The Odes are numbered by the verses of the book each comes from** (Ode 9 is `lxx.Odes.9.46`, Luke 1:46), so their "gaps" are the unprinted numbers before each ode's first verse, not losses.
- **Proverbs returns to chapters 24, 30 and 31** in Rahlfs's Greek order; the chapter anchor stands where the chapter first appears and the heading repeats unanchored.
- **Sirach's prologue** is `lxx.Sir.prolog.1` ….
- Verse numbers absent from a chapter are listed under `gaps` and none is invented.

## Canon

CCAT's list is Rahlfs's, which is wider than the Catholic canon and narrower than nothing: it carries **1 Esdras, 3 and 4 Maccabees, the Odes, the Psalms of Solomon and Psalm 151**, which are not in the Nova Vulgata's canon, beside the whole deuterocanon (Tobit, Judith, 1–2 Maccabees, Wisdom, Sirach, Baruch, the Letter of Jeremiah, and the Greek parts of Esther and Daniel). *Liturgiam authenticam* 37 makes the Nova Vulgata's book list the frame (`04. Reference/versification.md`), so a Catholic-canon question subtracts from this shelf.

## How it was checked

- **Shape.** 59 books from 64 files (Genesis, Psalms, Isaiah, Jeremiah and Ezekiel each come in two). Chapter counts are the source's own; Psalms has 151.
- **Parity.** Letters and marks, Beta Code against Unicode, exact in every book.
- **Emptiness.** `99. Tools/guard/check_anchor_bodies.py` on this folder: no anchor empty, no repeated body; the shortest bodies are genuine one-name verses of the genealogies (`lxx.1Chr.1.24` Σαλα).
- **Read**: Gen 1:1, Ps 22:1 (Hebrew 23), Isa 7:14, Sir 1:1, Wis 3:1, Tob 12:8 (BA), 2 Macc 12:45, Ps 151:1.

The index has not been rebuilt for this shelf, and its routing is an open question: see the tracker note for #41.
