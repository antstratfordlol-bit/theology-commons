# greek-sblgnt — the SBL Greek New Testament

**27 books, 260 chapters, 7,939 verses**, one file per book under its OSIS name. Taken 13–14 September 2026 under tracker #41, on Alex's answer 15 of 21 August. The SBLGNT is the readable running text of the Greek New Testament; STEPBible's TAGNT, which marks word by word what each major edition prints, was its witness.

| | |
|---|---|
| **Source** | *The SBL Greek New Testament* (SBLGNT), Society of Biblical Literature and Logos Bible Software, 2010; **v1.2 of 2023-07-10**, which added John 7:53–8:11. `data/sblgnt/text/*.txt` from `github.com/Faithlife/SBLGNT`, commit `c4d241a9c1c479a55b989ba35a4976c1d0b8052c` (2025-01-19), fetched 2026-09-13 |
| **Originals** | `01. Sources/_originals/Scripture/greek-sblgnt/`: the 27 text files, each matching its git blob SHA-1 at the pinned commit. TAGNT is not copied into the store (below) |
| **Licence** | **CC BY 4.0**; "Copyright 2010 by the Society of Biblical Literature and Logos Bible Software" (the repository README). `04. Reference/rights-register.md` row L14 |
| **Language** | `grc` |
| **Anchors** | Bare OSIS, `{#John.1.1}`, on the SBLGNT's own numbering, the standard critical-text numbering (`04. Reference/versification-hebrew-greek.md` §3) |
| **Converter** | `99. Tools/hebrew-greek/convert_sblgnt.py`; why not odtake: `99. Tools/hebrew-greek/README.md` |

## The text as distributed

Nothing is normalised. Each file keeps:

- the book's Greek title as the source prints it (`ΚΑΤΑ ΙΩΑΝΝΗΝ`);
- **the SBLGNT's variation-unit signs ⸀ ⸁ ⸂ ⸃ ⸄ ⸅** — 8,705 in all, counted per file in `text-form`. They point into its critical apparatus, and **the apparatus is not held in this library**: the signs mark where editions differ without saying how. TAGNT's edition columns say how;
- **⟦ ⟧** where the edition prints them: Mark 16:8 (the shorter ending), Mark 16:9–20, John 7:53–8:11;
- **no verse number this edition does not print. 18 verses are absent**, checked against every verse TAGNT lists in any edition: Matt 17:21, 18:11, 23:14; Mark 7:16, 9:44, 9:46, 11:26, 15:28; Luke 17:36, 23:17; John 5:4; Acts 8:37, 15:34, 24:7, 28:29; **Rom 16:25–27**. Each file's `gaps` lists its own. The doxology of Romans is absent from the SBLGNT text and XML files alike, and TAGNT does not mark it SBL (`versification-hebrew-greek.md` §3).

## TAGNT, the witness

STEPBible's *Translators Amalgamated Greek NT* (TAGNT; CC BY 4.0; commit `ae39711d78`) lists every word of NA27/28, the Textus Receptus, the Byzantine text, SBLGNT, Tregelles, Westcott–Hort and the Tyndale House GNT, each marked with the editions that print it. The check took the words it marks `SBL`, in order and in SBL's spelling, and compared them with this text verse by verse after folding (Greek letters only, no accents, lower case): **7,564 of 7,939 verses identical (95.3 %)**. The 375 that differ are explained by the data, not by the conversion:

- TAGNT spells words as NA28 does, and the commonest difference is **movable nu**;
- TAGNT does not mark the twelve verses of **John 7:53–8:11** as SBL; SBLGNT added them in v1.2;
- the rest are words SBLGNT prints that TAGNT does not tag `SBL` (Mark 8:34 ἐλθεῖν, Gal 1:3 ἡμῶν, Luke 23:42 ἐν τῇ βασιλείᾳ).

No verse TAGNT marks `SBL` is missing here. **TAGNT is not in the tree or the store**: it stays in the cache as fetched (`$OD_CACHE/stepbible`, verified by `fetch.py`). Whether its tagging — Strong's numbers, morphology, glosses, the edition columns — should come in as a sidecar is an open question for Alex.

## How else it was checked

- **Shape.** 27 books, 260 chapters. Chapter ends agree with the Nova Vulgata on 259 of 260, the RSV-2CE on 256, the Bible Hub interlinear on 255. The differences are numbering, not loss (`versification-hebrew-greek.md` §3).
- **Character parity**, source → Markdown, is exact in every book.
- **Emptiness.** `99. Tools/guard/check_anchor_bodies.py` on this folder finds no empty anchor and no repeated body.
- **Read**: Matt 1:1, John 1:1, John 8:11, Rom 3:23, Rev 22:21.

The index has not been rebuilt for this shelf.
