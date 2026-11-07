# Theology Commons

A collaborative, machine-readable digital library of Catholic theological, patristic, philosophical, scriptural, and magisterial literature in clean UTF-8 Markdown.

This repository is maintained as a shared research and study platform for colleagues and scholars, providing complete texts with invariant structural paragraph anchors (`{#...}`) across multiple languages for precise citation and academic retrieval.

```text
theology-commons/
├── README.md
├── CONTRIBUTING.md
├── .gitignore
├── Scripture/              # Sacred Scripture in original languages, Vulgate, and vernaculars with Navarra commentary
├── Magisterium/            # Ecumenical Councils, Papal Encyclicals, Vatican II, Curial Documents, Catechism, Canon Law
├── Patrologia-Migne/       # Complete Patrologia Graeca (PG), Patrologia Latina (PL), and Patrologia Orientalis (PO)
└── Library/                # Primary scholarly literature across theology, patristics, and philosophy
    ├── aquinas/            # St Thomas Aquinas Opera Omnia (Latin, English, Spanish)
    ├── fathers-schaff/     # Early Church Fathers in English (Schaff ANF/NPNF) and Spanish with critical selections
    ├── doctors/            # Doctors of the Church (Bonaventure, Bellarmine, Alphonsus, etc.)
    ├── latin-west/         # Medieval, Carolingian, and Scholastic Latin literature
    ├── liturgy/            # Historical rites, liturgical theology, and conciliar reform treatises
    ├── philosophy/         # Classical, medieval, and scholastic philosophical texts
    ├── spirituality/       # Spiritual classics, treatises, and interior life theology
    ├── theology/           # Systematic, dogmatic, moral, and historical theology monographs
    └── encyclopedia/       # Catholic reference works and historical encyclopedias
```

---

## 1. Core Principles

* **Original Languages Preserved**: Texts are preserved in their original tongues (Latin, Greek, Hebrew, Spanish, Italian, French, German) alongside reliable English and vernacular translations. Files follow the canonical convention `<work-title>.<lang>.md` (e.g. `de-trinitate.la.md`, `de-trinitate.en.md`).
* **Universal Paragraph Anchors**: Every significant locus carries an invariant citation anchor (e.g. `{#dv.11}` for *Dei Verbum* 11, `{#ST.1.Q2.A3}` for the *Summa*, `{#Gen.1.1}` for Genesis 1:1) that maps identical paragraphs across all language editions.
* **Plain Text Primacy**: Clean, standard GitHub Flavored Markdown readable on any platform, indexed by full-text search tools (`grep`, `ripgrep`, Obsidian, VS Code) without database lock-in.

---

## 2. Reading and Exploring the Library

You can explore and research this corpus in several ways:

### A. In-Browser Search & Navigation (github.dev)
You do not need to download the full repository locally to browse or search it.
1. Navigate to this repository page on GitHub: `https://github.com/antstratfordlol-bit/theology-commons`.
2. Press the **`.`** (period) key on your keyboard (or replace `.com` with `.dev` in the URL bar).
3. This opens **github.dev** (a full in-browser VS Code editor) with instant global search (`Ctrl + Shift + F`) across every markdown file without downloading anything to your machine.

### B. Local Clone for Deep Research
To clone the library locally for use with Obsidian, ripgrep, or personal LLM assistants (such as Claude Code or Antigravity):

```bash
git clone https://github.com/antstratfordlol-bit/theology-commons.git
```

*(Ensure Git has long paths enabled: `git config --global core.longpaths true`)*.

---

## 3. Contributing New Texts

All members of the collaboration circle are warmly invited to add new treatises, monographs, and critical editions to the library shelves. Please consult [CONTRIBUTING.md](CONTRIBUTING.md) for naming standards, frontmatter conventions, and anchor rules.
