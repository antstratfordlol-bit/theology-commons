# philosophy — the shelf

What is here, where it came from, and what is still missing. The sigla are in `sigla.md`; the catalogue row for every file is generated into `../_index.md`.

Built 2026-08-30 (od-e4) on Alex's ask, after a survey found the library held **two** philosophy files against 32,497 Magisterium and 14,955 Library files. The survey's other finding matters more and is not fixed here: **the philosophy that already existed was shelved under Aquinas**, not under philosophy — 26 of the 86 Aquinas works are philosophical, including twelve Aristotle commentaries, and nothing pointed at them.

## What the shelf holds

| | works | languages | anchored by |
|---|---|---|---|
| `plato/` | 36 — the whole canon, dubia and *Letters* included | Greek and English, all 36 | Stephanus |
| `aristotle/` | 28 | Greek all 28; English 7 | the edition's book/chapter/section — **not Bekker**, see below |

107 files, 22 MB. Every file records its edition, its editor or translator, its CTS URN where it has one, and its licence in frontmatter.

## The Spanish came and went on 31 August, and that is a decision, not a gap

**Azcárate's Spanish Plato and Aristotle were fetched, anchored and committed on
2026-08-31, and withdrawn from the tree the same evening.** Alex ruled, having
been shown the shape of the shelf first: *"let's ignore them for now, and stick
with english. do not add them to the kb"*. Fifty-seven files, 532 anchors, and
twenty-five sigla went with them; `sigla.md` names every one and says where the
fetched text still is. **Do not re-fetch it believing it was never tried.**

Two things settled it, and both are worth keeping on the record because they
will be true of the next Spanish Plato somebody proposes:

- **It would have cost a permanent exception to the language-invariant anchor
  rule.** Plato is cited by Stephanus and Aristotle by Bekker, and no lawfully
  usable Spanish edition of either prints those numbers — every edition that
  does is in copyright. So the Spanish could not share `plato-gorgias`, and a
  parallel `-es` space would have had to stand for good, in a language Alex does
  not need these two authors in.
- **What it bought was findable, not citable.** Twelve of the seventeen
  dialogues carried a single whole-document anchor, because neither witness
  prints any division inside them: a search could reach the dialogue and never a
  passage in it. The *Protágoras* was a stub — 17 of its 83 pages transcribed.

The Greek and English are untouched and are what this shelf is.

## Why this shelf, in this library

The library already held **twelve of Aquinas's Aristotle commentaries** in Latin, English and Spanish — `In-Metaphysicam`, `In-Physicam`, `In-De-anima`, `In-Ethicorum`, `In-Politicorum`, `In-Perihermeneias`, `In-Posteriora-Analytica` and the rest — and not one of the texts they comment on. That is the case for the shelf: it puts the commented text beside the commentary. `aristotle-metaphysica.1.980a` and Aquinas's `In-Metaphysicam` on the same passage are now both here.

## Where it came from

Two corpora, because **neither has Aristotle whole**.

- **canonical-greekLit** (Perseus Digital Library, `PerseusDL/canonical-greekLit`, CC BY-SA 4.0), cloned 2026-08-30 as a sparse checkout of Plato and Aristotle only. Greek **and** English. Greek is Burnet's *Platonis Opera* (Clarendon 1900-07) for Plato and the Loeb/Perseus editions for Aristotle; the English is the 19th and early-20th-century translations Perseus carries, each named in the file.
- **First1KGreek** (`OpenGreekAndLatin/First1KGreek`), already held since 2026-08-21. **Greek only** — it is where the *Organon*, the *Physics*, *De anima*, the *Parva naturalia* and the *Magna Moralia* come from, none of which Perseus carries in English.

Provenance, commit and tree hashes, and the manifest digest: `01. Sources/_originals/corpora/PROVENANCE.md`.

The underlying texts are ancient and long out of copyright. What CC BY-SA covers is Perseus's TEI encoding and the modern editions; the attribution is in every file's `edition`, `edition_editor` and `licence` fields.

## Anchors

Read off each file's CTS `<refsDecl>`, never invented — the corpora declare their own citation scheme and that scheme *is* the work's native reference. So `plato-respublica.1.327` is Stephanus 327 of Republic I, and it resolves in the Greek and the English alike, because the sigla is language-invariant and the language lives in the document id.

### Aristotle is not anchored by Bekker, and this needs a decision

**Plato came out right and Aristotle did not.** Perseus's section numbers for Plato *are* Stephanus numbers, so `plato-respublica.1.327` is a citation any reader of Plato recognises. Perseus's sections for Aristotle are **its own sequential divisions**: `aristotle-metaphysica.1.1.1` is book 1, chapter 1, section 1 — not *Metaphysics* 980a. Aristotle's own reference is Bekker, and citing him by anything else is the same error as citing *Camino* by page.

**The Bekker numbers are held, just not as anchors.** They survive in the text as page markers — `‹page 980a›`, 238 of them in the *Metaphysics* — so they are greppable and visible to a reader, and nothing has been lost or invented. What is missing is the ability to write `odsearch ref aristotle-metaphysica.980a` and land on the passage.

Two ways to close it, and it is Alex's call which: re-anchor Aristotle on the `‹page›` markers, minting `aristotle-metaphysica.980a` (correct, and it discards Perseus's own scheme); or keep both, anchoring on Bekker and carrying the book/chapter as a second reference. Neither was done on a guess. Recorded in the tracker.

Verified against canonical structure rather than by reading the output: Republic 10 books, Laws 12, *Metaphysics* 14, *Nicomachean Ethics* 10, *Politics* 8, *Physics* 8, *De anima* 3, *Topics* 8, *Rhetoric* 3, *De caelo* 4 — ten checks, all matching.

## What is missing, and it is worth knowing

1. **The *Analytica posteriora* is in neither corpus.** Aquinas's commentary on it is held; the text is not. This is the one gap in Aristotle's philosophical corpus and it cannot be closed from these two sources.
2. **No Spanish**, and that is now a ruling rather than a gap. Azcárate's Spanish Plato and Aristotle were taken in on 31 August and withdrawn the same day on Alex's word; see the section above. The shelf is Greek and English.
3. **English for only 7 of 28 Aristotle works.** The *Organon*, *Physics*, *De anima* and the *Parva naturalia* are Greek-only, because First1KGreek is Greek-only. Less of a problem here than it would be elsewhere — Alex holds a King's College London Graduate Diploma in Classical Studies (2018, convalidated as *Lingua græca* in 2021, summa cum laude) — but a facing translation is still faster than reading Aristotle's Greek cold, and for these works the Latin of Aquinas's commentary is the nearest thing held.
4. **Deliberately not converted**: the biology (*Historia animalium*, *De partibus animalium*, *De generatione animalium*, *De animalium incessu*/*motione*, *De plantis*), the *Problemata*, and the spuria and fragments. They stay as TEI in `_originals/corpora/` and convert on demand. The reason is `convert_selection.sh`'s reason — an unread mass of text drowns the index.
5. **Nothing after Aristotle.** No Plotinus, no Augustine *as philosophy*, no Boethius, no modern philosophy at all. The Catholic Encyclopedia's articles (*Plato and Platonism*, *Philosophy of Kant*, *Nominalism, Realism, Conceptualism*, *Epistemology*, *Logic*) are the only coverage of any of it.

## Two files that predate the shelf

- `Ethica-Nicomachea-VIII-IX.en.md` — Books VIII and IX only, English only, promoted 2026-08-27 for the *Commentary on Friendship* course. **Now redundant**: `aristotle/Ethica-Nicomachea.en.md` holds all ten books, with the Greek beside it. Left in place rather than deleted, because the course folder may reference it and deleting another session's promotion is not this session's call. Worth retiring — see the tracker.
- `History-of-Mediaeval-Philosophy.en.pdf` — never converted. A binary in the tree, so it is #42/#94's business, not this shelf's.

## Regenerating

Derived output. Do not hand-edit:

```bash
sh "99. Tools/patristics-open/convert_philosophy.sh"          # Greek and English
```
