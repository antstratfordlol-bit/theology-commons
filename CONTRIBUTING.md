# Contributing to Theology Commons

We welcome contributions of new theological treatises, patristic texts, liturgical studies, and philosophical works from all members of the research circle.

---

## 1. Where to File New Works

Place new texts within the appropriate shelf under `Library/`, `Magisterium/`, or `Scripture/`:

| Target Shelf | Content & Scope | Example Works |
| :--- | :--- | :--- |
| `Library/theology/` | Systematic, dogmatic, historical, or moral theology monographs | Scheeben, De Lubac, Ratzinger, Congar, Garrigou-Lagrange |
| `Library/liturgy/` | Liturgical history, rites, theology, and commentary | Jungmann, Botte, Mohlberg, Gamber, Reid |
| `Library/fathers-schaff/` | Early Church Fathers in English (Schaff ANF/NPNF) and Spanish | Irenaeus, Athanasius, Basil, Gregory of Nazianzus |
| `Library/doctors/` | Writings of declared Doctors of the Church | Anselm, Bernard of Clairvaux, John of the Cross, Teresa of Ávila |
| `Library/philosophy/` | Classical, Aristotelian, Scholastic, and modern philosophy | Aristotle, Boethius, Gilson, Maritain, Pieper |
| `Library/spirituality/` | Spiritual classics, ascetical theology, and interior life treatises | Francis de Sales, Scupoli, Teresa of Jesus |

---

## 2. File Naming Conventions

* File names must use lowercase Latin characters, hyphens, and standard ISO language suffixes:
  `<title-or-slug>.<lang>.md`
* Examples:
  * Latin: `de-incarnatione-verbi.la.md`
  * Greek: `de-incarnatione-verbi.grc.md`
  * English: `on-the-incarnation.en.md`
  * Spanish: `sobre-la-encarnacion.es.md`
  * Italian: `sull-incarnazione.it.md`

---

## 3. Document Frontmatter

Open every new Markdown file with standardized YAML frontmatter:

```yaml
---
title: "De Spiritu Sancto"
creator: "Basil of Caesarea"
year: 375
language: grc
source: "SC 17 bis / NPNF series 2 vol. 8"
anchors: true
---
```

---

## 4. Universal Paragraph Anchors

Where possible, anchor major sections and numbered paragraphs using standard inline sigla:

```markdown
### Chapter 1 {#basil.dss.1}

[1]{#basil.dss.1.1} In your surprise at what seemed an unusual custom...
```

Anchoring ensures that when another language edition is added in the future, parallel passages align automatically for cross-lingual search and comparative reading.

---

## 5. Submission Workflow

1. Create a descriptive branch for your addition:
   ```bash
   git checkout -b add/ratzinger-theology-liturgy
   ```
2. Commit your new file(s) with a clear commit message:
   ```bash
   git add Library/liturgy/...
   git commit -m "Add Joseph Ratzinger: The Spirit of the Liturgy (en)"
   ```
3. Push your branch to GitHub and open a Pull Request:
   ```bash
   git push origin add/ratzinger-theology-liturgy
   ```
