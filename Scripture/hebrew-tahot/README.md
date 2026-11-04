# hebrew-tahot — the Hebrew Bible, Leningrad Codex (STEPBible TAHOT)

**39 books, 929 chapters, 23,213 verses**, one file per book under its OSIS name (`Gen.md` … `Mal.md`), in the Hebrew canon's 39 books and no deuterocanon, because the Hebrew has none (`04. Reference/versification.md`). Taken 13–14 September 2026 under tracker #41, on Alex's answer 15 of 21 August.

| | |
|---|---|
| **Source** | *Translators Amalgamated Hebrew OT* (TAHOT), STEPBible.org, data created by Tyndale House, Cambridge: four tab-separated files from `github.com/STEPBible/STEPBible-Data`, commit `ae39711d7843b2902d54993e432de9c12d6a4b9a` (2026-09-08), fetched 2026-09-13 |
| **Text** | The Leningrad Codex as in the Westminster Leningrad Codex 4.20 (via OpenScriptures), checked by Tyndale House against the Stuttgartensia electronic text and corrected towards the codex: "essentially, a corrected version of BHS" (the file's own description). Pointing, cantillation, maqqef, paseq, sof pasuq and the petuhah/setumah markers פ and ס as transmitted |
| **Originals** | `01. Sources/_originals/Scripture/hebrew-tahot/`, the four files byte for byte, each matching its git blob SHA-1 at the pinned commit |
| **Licence** | **CC BY 4.0**. Attribution: STEPBible.org, from data created by Tyndale House, Cambridge. Each file's header adds *"Refer others to github.com/STEPBible as the source of the data. Please do not redistribute it yourself."* — a request beside the licence, recorded verbatim in `04. Reference/rights-register.md` row L13; whether the kit carries this shelf is an open question for Alex |
| **Language** | `hbo` (Ancient Hebrew). Aramaic where the Bible is in Aramaic: Gen 31:47 (two words), Jer 10:11, Ezra 4:8–6:18 and 7:12–26, Dan 2:4b–7:28; each of those files says so |
| **Anchors** | Bare OSIS, `{#Gen.1.1}`, **on the Hebrew verse numbers**: psalm titles are verse 1, Malachi has three chapters, Joel four. This is the library's canonical numbering, the one the Navarra, CEE and Nova Vulgata already carry (`04. Reference/versification.md`) |
| **Converter** | `99. Tools/hebrew-greek/convert_tahot.py`; why not odtake: `99. Tools/hebrew-greek/README.md` |

## What the reading text is, and what it leaves out

TAHOT is a word table, not a running text: one row per word, marked with a text type. The reading text here is assembled from the rows, in order, under each word's Hebrew verse number:

- **L** (Leningrad) and **Q** (the Qere) rows are the text. Where Qere and Ketiv differ, the Qere is read, as TAHOT and translators do; the Ketiv stays in the source file's variant column. **14 positions, in 10 books, have a Ketiv and no Qere**, so they have no reading and no text here; each book's `gaps` lists them.
- **R** rows restore what Leningrad lacks from a parallel passage (Josh 21:36–37 from 1 Chr 6; Neh 7:67 from Ezra 2:66). They are printed inside ⟦ ⟧ and declared under `repairs`.
- **X** rows are words preserved only in the Greek, put back into Hebrew from the BHS/BHK apparatus. **They are not the Masoretic text and are left out** — 152 words over 14 books (Gen, Num, Deut, Judg, 1–2 Sam, 2 Kgs, 1–2 Chr, Ezra, Esth, Ps, Eccl, Dan; 59 of them in 1 Samuel), every one listed with its reference under that book's `gaps`.
- **TAHOT's tagging is not in the Markdown**: English glosses, Strong's numbers, morphology, meaning and spelling variants, proper-name identities. It is in the source files in the store, unchanged. Whether a tagging sidecar is wanted in the tree is an open question for Alex.

## Sidecars

- `_verse-counts.tsv` — verses per chapter, on the Hebrew numbering.
- `_english-versification.tsv` — **2,094 Hebrew verses whose words TAHOT numbers differently in English Bibles**, `book · hebrew · english` (`Gen 32:1 → 31:55`; a verse may list two English references where the English divides it). It is TAHOT's own crosswalk, read off the rows, not a table made here.

## How it was checked

- **Two witnesses from the source.** Character parity against the rows is exact in every book. The independent one is TAHOT's per-verse header line (`# Psa.3.0 (Heb: 3.1)`), which prints each verse's words separately from the rows: in **all 39 books** its characters equal the text's exactly, apart from the X words, which the headers print and the text leaves out.
- **Shape.** 39 books, 929 chapters; every chapter's verses run 1..n with no gap.
- **Against the four Bibles already held**, chapter by chapter (the last verse of each): Navarra 922/929 (99.2 %), CEE 923/929 (99.4 %), Nova Vulgata 911/929 (98.1 %), RSV-2CE 790/928 (85.1 %). Detail in `04. Reference/versification-hebrew-greek.md`.
- **Emptiness.** `99. Tools/guard/check_anchor_bodies.py` on this folder: no anchor empty, no repeated body.
- **Read**: Gen 1:1, Ps 23:1, Ps 51:1 (the title as verse 1), Isa 7:14, Mal 3:19.

The index has not been rebuilt for this shelf; its registration rows are proposed in the tracker note for #41.
