# Corpus Thomisticum (S. Thomae de Aquino Opera Omnia in Markdown)

A curated, machine-readable digital corpus of the complete works (*Opera Omnia*) of Saint Thomas Aquinas, formatted in clean UTF-8 Markdown with cross-lingual structural anchors for scholarly research, semantic search, and AI-assisted theology.

```text
corpus-thomisticum/
├── README.md                    # Repository documentation and catalogue
├── _index.md                    # Complete inventory of works, editions, and sigla
├── ERRATA.md                    # Scholarly errata registry and emendation log
├── Summa.*.md                   # Summa Theologiae (1a, 1a2ae, 2a2ae, 3a, Supp) in la, en, es
├── Summa-contra-Gentiles.*.md   # Summa contra Gentiles (Books 1–4) in la, en, es
├── Compendium-theologiae.*.md   # Compendium of Theology in la, en, es
├── QD-*                         # Disputed Questions (De Veritate, De Potentia, De Anima, etc.)
├── Super-*                      # Scriptural and Patristic/Neoplatonic commentaries
├── Catena-aurea.*.md            # Catena Aurea on the four Gospels in la, en, es
├── De-*                         # Philosophical and theological opuscula
├── Cajetan.*.la.md              # Cardinal Cajetan's commentaries on the Summa Theologiae
└── *.leonine.tsv                # Structural Leonine concordance tables
```

---

## 1. Corpus Overview & Scope

* **Scale**: Over 184 language editions across 97 distinct works (218 files, ~177 MB).
* **Editions Incorporated**:
  * **Latin (`.la.md`)**: Texts from *Corpus Thomisticum* (Fundación Tomás de Aquino / Enrique Alarcón, Universidad de Navarra), the Leonine Commission (*Editio Leonina*), and SCTA (*Scholastic Commentaries and Texts Archive*).
  * **English (`.en.md`)**: Translations by the Fathers of the English Dominican Province (Benziger Brothers, 1947 / CCEL) and Joseph Kenny OP (Dominican House of Studies Priory).
  * **Spanish (`.es.md`)**: Critical translations from the *Biblioteca de Autores Cristianos* (BAC) and the Instituto del Verbo Encarnado (*tomasdeaquino.org*).

---

## 2. Invariant Cross-Lingual Structural Anchors

Every work in this repository is segmented with invariant anchor tags (in HTML anchor format: `{#sigla.reference}`). 

Because the anchors match across languages, a single locator resolves identically across Latin, English, and Spanish texts:
* **Summa Theologiae**: `{#sth.1a.q2.a3}` (Prima Pars, question 2, article 3)
* **Summa contra Gentiles**: `{#scg.1.c13}` (Book 1, chapter 13)
* **De Ente et Essentia**: `{#ente.c1}` (Chapter 1)

This allows instant bilingual or trilingual alignment, parallel reading, and direct citations that adhere to Roman and pontifical academic citation standards.

---

## 3. Contents by Category

### A. The Theological Summae
* **Summa Theologiae**: Complete text in Latin, English, and Spanish across all parts:
  * *Prima Pars* (`1a`)
  * *Prima Secundae* (`1a2ae`)
  * *Secunda Secundae* (`2a2ae`)
  * *Tertia Pars* (`3a`)
  * *Supplementum* (`supp`, currently in English; Latin in progress)
* **Summa contra Gentiles**: Books 1 through 4 in Latin, English, and Spanish.
* **Compendium Theologiae**: In Latin, English, and Spanish.
* **Scriptum super Sententiis**: Commentary on the Sentences of Peter Lombard. Complete in Latin across all four books (Liber 1: The Trinity; Liber 2: Creation and Fall; Liber 3: Incarnation and Virtues; Liber 4: Sacraments and Eschatology; plus the *Lectura Romana*) spanning all ~180 distinctiones, alongside the English outline.

### B. Disputed Questions (*Quaestiones Disputatae*)
* *Quaestiones Disputatae de Veritate* (Truth) in Latin, English, and Spanish.
* *Quaestiones Disputatae de Potentia Dei* (The Power of God) in Latin and English.
* *Quaestio Disputata de Anima* (The Soul) in Latin, English, and Spanish.
* *Quaestio Disputata de Spiritualibus Creaturis* in Latin, English, and Spanish.
* *Quaestiones Disputatae de Virtutibus* (Virtues in General, Charity, Cardinal Virtues) in Latin and English.
* *Quaestio Disputata de Unione Verbi Incarnati* in English.
* *Quaestio Disputata de Malo* (complete Latin text covering Questions 1 to 16, plus Question 1 in Spanish).
* *Quaestiones Quodlibetales* (complete Latin text of Quodlibets 1 to 12).

### C. Major Opuscula & Theological Commentaries
* *De Ente et Essentia* (On Being and Essence) in Latin, English, and Spanish.
* *De Principiis Naturae* (On the Principles of Nature) in Latin, English, and Spanish.
* *De Unitate Intellectus contra Averroistas* in Latin, English, and Spanish.
* *De Substantiis Separatis* (On Separate Substances) in Latin, English, and Spanish.
* *De Aeternitate Mundi* (On the Eternity of the World) in Latin, English, and Spanish.
* *De Regno, ad Regem Cypri* (On Kingship) in Latin, English, and Spanish.
* *De Articulis Fidei et Ecclesiae Sacramentis* in Latin, English, and Spanish.
* *De Rationibus Fidei contra Saracenos, Graecos et Armenos* in Latin and English.
* *Super Boetium De Trinitate* in Latin and English.
* *Super Boetium De hebdomadibus* (*Expositio libri Boetii De ebdomadibus*) in Latin.
* *Super Librum De causis* (*Expositio super librum De causis*) in Latin.
* *Super De divinis nominibus* (*In librum beati Dionysii De divinis nominibus*) in Latin.
* Shorter opuscula and polemical treatises:
  * Logical treatises: *De fallaciis*, *De propositionibus modalibus*.
  * Pastoral and disciplinary treatises: *De forma absolutionis*, *De secreto*, *De regimine Iudaeorum (Ad ducissam Brabantiae)*.
  * Canonical expositions: *Expositio super primam et secundam Decretalem*.
  * Canonical responses: *Responsiones ad diversos* (De 108, 43, 36, 30, et 6 articulis, including replies to John of Vercelli and the Venetian/Besançon lectors).
  * Natural philosophy and metaphysics: *De mixtione elementorum*, *De motu cordis*, *De operationibus occultis naturae*, *De iudiciis astrorum*, *De sortibus*, etc.

### D. Scripture Commentaries
* **Catena Aurea**: Complete commentaries on Matthew, Mark, Luke, and John in Latin, English, and Spanish.
* **Gospel Commentaries**: *Super Evangelium S. Ioannis* and *Super Evangelium S. Matthaei* in Latin and English.
* **Complete Pauline Corpus**: Full commentaries across all fourteen epistles:
  * *Super Epistolam ad Romanos* in Latin.
  * *Super I et II ad Corinthios* in Latin and English.
  * *Super ad Galatas* in Latin and English.
  * *Super ad Ephesios* in Latin and English.
  * *Super ad Philippenses* in Latin and English.
  * *Super ad Colossenses* in Latin and English.
  * *Super I et II ad Thessalonicenses* in Latin (1 Thess in English as well).
  * *Super I et II ad Timotheum* in Latin.
  * *Super ad Titum* in Latin.
  * *Super ad Philemonem* in Latin and English.
  * *Super ad Hebraeos* in Latin and English.
* **Old Testament**: Commentary on the Book of Job (*Expositio super Iob ad litteram*), Psalms (*In Psalmos*), Isaiah (*Super Isaiam*), Jeremiah (*Super Ieremiam*), and Lamentations (*Super Threnos*).

### E. Aristotle Commentaries
* *Sententia libri Ethicorum* (Nicomachean Ethics).
* *Sententia super Metaphysicam* (Metaphysics).
* *Sententia super Physicam* (Physics).
* *Sententia super librum De Anima* (On the Soul).
* *Sententia libri Politicorum* (Politics).
* *Expositio libri Posteriorum Analyticorum* and *Peri Hermeneias*.
* *De Caelo et Mundo*, *De Generatione et Corruptione*, *Meteora*, *De Sensu et Sensato*, *De Memoria et Reminiscentia*.

### F. Mendicant Controversies & Polemical Treatises
* *Contra Impugnantes Dei Cultum et Religionem* in Latin, English, and Spanish.
* *Contra Retrahentes Homines a Religionis Ingressu* in Latin, English, and Spanish.
* *De Perfectione Vitae Spiritualis* in Latin, English, and Spanish.
* *Contra Errores Graecorum* in Latin, English, and Spanish.

### G. Historical Commentaries
* **Cardinal Cajetan (*Tommaso de Vio*)**: Full Latin commentaries on the *Summa Theologiae* (*Prima Pars*, *Prima Secundae*, and *Secunda Secundae*).

---

## 4. Scholarly Errata, Textual Emendation & Contribution Protocol

To protect the integrity of the corpus and avoid corrupting machine-readable anchors, all researchers and collaborating AI agents must observe the formal governance protocol detailed in [ERRATA.md](file:///C:/Users/antst/Documents/corpus-thomisticum/ERRATA.md):

1. **Never edit during research sessions:**
   Do not apply immediate textual changes during active theological analysis or reading sessions. Log every suspect reading into `ERRATA.md`.

2. **Cite authoritative witnesses:**
   No conjectural corrections are permitted. Every change must cite a verified critical edition (Leonine volume, page, line, or variant) or an established printed text (Marietti, Alarcón).

3. **Preserve invariant anchors:**
   Never delete, modify, or renumber structural anchors (`{#sigla.ref}`). Corrections apply strictly to prose text.

4. **Dedicated git branch workflow:**
   All emendations are executed on the `corrections` git branch (`git checkout -b corrections`) with atomic commits citing the authority in the commit message, followed by a Pull Request.

---

## 5. How to Use with Agentic Tools & Editors

### Command-Line Search (`ripgrep`)
```bash
# Search for passive potency in the Latin Prima Pars
rg "potentia passiva" Summa.1a.la.md

# Search across all disputed questions
rg "ratio boni" QD-*.la.md
```

### In Claude Code, Antigravity, or Obsidian
* Open the directory directly as a workspace.
* Search across Markdown files using native fuzzy find or grep.
* Anchor locators allow direct cross-referencing between Latin originals and vernacular translations.
