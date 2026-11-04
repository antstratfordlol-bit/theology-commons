# Sigla — philosophy shelf

Minted by `99. Tools/patristics-open/convert_philosophy.sh` on 2026-08-30 and registered here as a class, like `../doctors/sigla.md` and `../fathers/sigla.md`, rather than one by one in `anchors.md`. All 64 checked free with `check_sigla.py`.

Pattern: `author-shorttitle.REF`, **language-invariant** — one sigla covers every language a work is held in, so `plato-respublica.1.327` is the same passage in Burnet's Greek and in the English beside it. The **document id** carries the language (`plato-respublica.grc`, `plato-respublica.en`), because `build_index.py` keys documents by id and would drop the second language as a duplicate otherwise.

**The sigla carries the author because the titles collide.** Both Plato and Aristotle have a *Politicus*/*Politica*, an *Epistulae* and a *Topica*-adjacent work, and the library already holds four other authors with a *De anima*. This is the `surname-shorttitle` form `anchors.md` registers.

**The reference is the edition's own, not one counted here** — read off each file's CTS `<refsDecl>` rather than invented, which is why the `reference form` column differs work by work: a dialogue long enough to be divided into books gives `book.section`, a short one gives `section` alone.

**For Plato that reference is Stephanus**, so `plato-respublica.1.327` is a citation any reader recognises. **For Aristotle it is not Bekker** — Perseus divides him by its own book/chapter/section, so `aristotle-metaphysica.1.1.1` is book 1 chapter 1 section 1, and not *Metaphysics* 980a. The Bekker numbers are held in the text as `‹page 980a›` markers (238 in the *Metaphysics*) and are greppable, but they are not anchors. Closing that is a decision for Alex, not a default: see `README.md` and the tracker.

**A note on the anchor count.** It is the count in the fullest witness held, normally the Greek. Where a work is held in two languages the two counts are within a few of each other; they are not asserted equal.

| sigla | author | work | languages | reference form | anchors |
|---|---|---|---|---|---|
| `aristotle-analytica-priora` | Aristotle | Analytica priora | grc | section | 133 |
| `aristotle-athenaion-politeia` | Aristotle | Ἀθηναίων πολιτεία | grc | section.subsection.section | 381 |
| `aristotle-categoriae` | Aristotle | Categoriae | grc | chapter | 16 |
| `aristotle-de-anima` | Aristotle | De anima | grc | section | 34 |
| `aristotle-de-caelo` | Aristotle | De caelo | grc | section | 44 |
| `aristotle-de-divinatione` | Aristotle | De divinatione per somnum | grc | section | 3 |
| `aristotle-de-generatione` | Aristotle | De generatione et corruptione | grc | section | 24 |
| `aristotle-de-insomniis` | Aristotle | De insomniis | grc | section | 4 |
| `aristotle-de-interpretatione` | Aristotle | De interpretatione | grc | chapter | 15 |
| `aristotle-de-iuventute` | Aristotle | De iuventute et senectute, De vita et morte | grc | section | 7 |
| `aristotle-de-longitudine` | Aristotle | De longitudine et brevitate vitae | grc | section | 7 |
| `aristotle-de-memoria` | Aristotle | De memoria et reminiscentia | grc | section | 3 |
| `aristotle-de-respiratione` | Aristotle | De respiratione | grc | section | 22 |
| `aristotle-de-sensu` | Aristotle | De sensu et sensibilibus | grc | section | 170 |
| `aristotle-de-somno` | Aristotle | De somno et vigilia | grc | section | 4 |
| `aristotle-de-virtutibus` | Aristotle | περὶ Ἀρετῶν καὶ Κακιῶν | grc | section | 2 |
| `aristotle-ethica-eudemia` | Aristotle | Ἠθικὰ Εὐδήμεια | en, grc | book.section.subsection | 629 |
| `aristotle-ethica-nicomachea` | Aristotle | Ἠθικὰ Νικομάχεια | en, grc | book.section.subsection | 1331 |
| `aristotle-magna-moralia` | Aristotle | Magna Moralia | grc | book.chapter.section | 488 |
| `aristotle-metaphysica` | Aristotle | τὰ Μετὰ τὰ Φυσικά | en, grc | book.section.subsection | 1712 |
| `aristotle-meteorologica` | Aristotle | Meteorologica | grc | section | 46 |
| `aristotle-oeconomica` | Aristotle | Οἰκονομικά | en, grc | book.section.subsection | 86 |
| `aristotle-physica` | Aristotle | Physica | grc | section | 80 |
| `aristotle-poetica` | Aristotle | Περὶ ποιητικῆς | en, grc | chapter.subchapter.section | 408 |
| `aristotle-politica` | Aristotle | Πολιτικά | en, grc | book.bekker_page.section | 198 |
| `aristotle-rhetorica` | Aristotle | Ῥητορική | en, grc | book.chapter.section | 946 |
| `aristotle-sophistici-elenchi` | Aristotle | De sophisticis elenchis | grc | chapter | 34 |
| `aristotle-topica` | Aristotle | Topica | grc | section | 92 |
| `plato-alcibiades-i` | Plato | Ἀλκιβιάδης αʹ | en, grc | section | 34 |
| `plato-alcibiades-ii` | Plato | Ἀλκιβιάδης βʹ | en, grc | section | 15 |
| `plato-amatores` | Plato | Ἐρασταί | en, grc | section | 9 |
| `plato-apologia` | Plato | Ἀπολογία Σωκράτους | en, grc | section | 27 |
| `plato-charmides` | Plato | Χαρμίδης | en, grc | section | 25 |
| `plato-clitopho` | Plato | Κλειτοφῶν | en, grc | section | 6 |
| `plato-cratylus` | Plato | Κρατύλος | en, grc | section | 59 |
| `plato-critias` | Plato | Κριτίας | en, grc | section | 17 |
| `plato-crito` | Plato | Κρίτων | en, grc | section | 13 |
| `plato-epinomis` | Plato | Ἐπινομίς | en, grc | section | 21 |
| `plato-epistulae` | Plato | Ἐπιστολαί | en, grc | letter.section | 79 |
| `plato-euthydemus` | Plato | Εὐθύδημος | en, grc | section | 38 |
| `plato-euthyphro` | Plato | Εὐθύφρων | en, grc | section | 16 |
| `plato-gorgias` | Plato | Γοργίας | en, grc | section | 82 |
| `plato-hipparchus` | Plato | Ἵππαρχος | en, grc | section | 9 |
| `plato-hippias-maior` | Plato | Ἱππίας μείζων | en, grc | section | 25 |
| `plato-hippias-minor` | Plato | Ἱππίας ἐλάττων | en, grc | section | 15 |
| `plato-ion` | Plato | Ἴων | en, grc | section | 14 |
| `plato-laches` | Plato | Λάχης | en, grc | section | 25 |
| `plato-leges` | Plato | Νόμοι | en, grc | book.section | 340 |
| `plato-lysis` | Plato | Λύσις | en, grc | section | 22 |
| `plato-menexenus` | Plato | Μενέξενος | en, grc | section | 17 |
| `plato-meno` | Plato | Μένων | en, grc | section | 32 |
| `plato-minos` | Plato | Μίνως | en, grc | section | 10 |
| `plato-parmenides` | Plato | Παρμενίδης | en, grc | section | 42 |
| `plato-phaedo` | Plato | Φαίδων | en, grc | section | 63 |
| `plato-phaedrus` | Plato | Φαῖδρος | en, grc | section | 54 |
| `plato-philebus` | Plato | Φίληβος | en, grc | section | 58 |
| `plato-politicus` | Plato | Πολιτικός | en, grc | section | 56 |
| `plato-protagoras` | Plato | Πρωταγόρας | en, grc | section | 55 |
| `plato-respublica` | Plato | Πολιτεία | en, grc | book.section | 289 |
| `plato-sophista` | Plato | Σοφιστής | en, grc | section | 54 |
| `plato-symposium` | Plato | Συμπόσιον | en, grc | section | 53 |
| `plato-theaetetus` | Plato | Θεαίτητος | en, grc | section | 70 |
| `plato-theages` | Plato | Θεάγης | en, grc | section | 12 |
| `plato-timaeus` | Plato | Τίμαιος | en, grc | section | 77 |

---

# The Spanish was minted here on 31 August and withdrawn the same day

**Twenty `-es` sigla and two class sigla were registered in this file on
2026-08-31 and are registered here no longer.** Alex ruled that evening, having
been given the shape of the shelf first: *"let's ignore them for now, and stick
with english. do not add them to the kb"*. **This is a deliberate removal, not a
gap**, and none of the withdrawn sigla is in use anywhere in the library.

What went: `plato-alcibiades-i-es`, `plato-alcibiades-ii-es`,
`plato-apologia-es`, `plato-banquete-es`, `plato-carmides-es`,
`plato-clitofon-es`, `plato-criton-es`, `plato-eutidemo-es`,
`plato-eutifron-es`, `plato-fedon-es`, `plato-fedro-es`, `plato-filebo-es`,
`plato-ion-es`, `plato-laques-es`, `plato-lisis-es`, `plato-protagoras-es`,
`plato-sofista-es`, `plato-timeo-de-locres-es`, `aristotle-metafisica-es`,
`aristotle-etica-nicomaco-es`, and the two class sigla `azcarate-platon` and
`azcarate-aristoteles` for Azcárate's own prefatory essays and *argumentos*.
Fifty-seven files, 532 anchors, withdrawn together. Three further Aristotle
sigla had been reserved and never minted — `aristotle-politica-es`,
`aristotle-moral-a-nicomaco-es`, `aristotle-gran-moral-es` — and the reservation
lapses with them. **All twenty-five are free again**, and `check_sigla.py` will
say so, because it reads `04. Reference/anchors.md` and the live index, not this
file.

**Why, in the terms this file argued in.** The `-es` space was minted because
Plato is cited by Stephanus and Aristotle by Bekker and no lawfully usable
Spanish edition of either prints those numbers — every edition that does is in
copyright — so the Spanish could not share the language-invariant sigla the
Greek and English use, and reusing them would have minted citations that look
right and resolve to the wrong passage. That reasoning was sound and it is what
settled the matter: keeping the shelf meant a permanent exception to the
language-invariant anchor rule, in a language Alex does not need these two
authors in. And the shelf it bought was findable rather than citable —
**twelve of the seventeen dialogues carried one whole-document anchor**, because
neither witness prints any division inside them, so a search could reach the
dialogue and never a passage in it; the *Protágoras* was a stub of 17 of its 83
pages. The `-es` suffix does not appear anywhere in the library now, and it
should not be reintroduced without Alex saying so.

**Where the text is, so nobody re-fetches it believing it was never tried.**
Both intakes are still in the fetch cache, outside the repository and outside
the originals store, which is itself part of the library Alex said not to add
them to:

- `~/Library/Caches/od-knowledgebase/doctors/eswikisource/` — 97 files, 5.3 MB,
  the es.wikisource.org wikitext and rendered HTML for the 17 dialogues, the
  *Metafísica* and the *Ética a Nicómaco*.
- `~/Library/Caches/od-knowledgebase/doctors/filosofia/` — 186 files, 4.1 MB,
  the filosofia.org pages for 16 dialogues and Azcárate's apparatus. The
  Aristotle was never complete there: 381 pages were needed and 37 fetched, and
  the detached fetch that was still working through the remainder at the site's
  60-second crawl delay was stopped when the ruling came.

Both converters still work: `99. Tools/eswikisource/` for the
Wikisource side, `99. Tools/doctors/extract_filosofia.py` for filosofia.org.
Each now carries a banner saying it must not be re-run without Alex's word.
