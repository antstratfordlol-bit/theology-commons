# Migne Patrologia Cursus Completus (Digital TEI Edition)

A complete, machine-readable, column-anchored digital edition of Jacques-Paul Migne's *Patrologia Cursus Completus* in clean UTF-8 Markdown, based on verified TEI XML transcriptions (Open Greek and Latin / Perseus / Corpus Corporum / The Faith Received).

This edition replaces raw historical OCR with curated polytonic Greek, Latin, and Oriental source texts, providing universal column milestone anchors (`{#pg.VOL.COL}` and `{#pl.VOL.COL}`) for precise academic citation and computational retrieval.

```text
migne-patrologia/
├── README.md
├── migne_manifest.json          # Complete JSON catalogue of all 12,298 treatises and column spans
├── Patrologia_Graeca/           # 161 volumes (PG 1–161) — Curated Polytonic Greek (3,146 treatises)
├── Patrologia_Latina/           # 221 volumes (PL 1–221) — Clean Ecclesiastical Latin (8,966 treatises)
│   └── (Volumes 32–47 contain the complete 283-work Corpus Augustinianum)
└── Patrologia_Orientalis/      # 60 volumes (PO 1–60) — Syriac, Arabic, Coptic, Armenian (400 treatises)
```

---

## 1. Key Editorial Enhancements Over Raw OCR

| Feature | Raw Archival OCR | Digital TEI Edition (This Release) |
| :--- | :--- | :--- |
| **Greek Orthography** | Garbled Latin-1 characters / corrupted OCR | **Clean Polytonic Greek** (Perseus / Open Greek and Latin TEI) |
| **Granularity** | Monolithic 20–50 MB volume files | **Treatise-by-treatise** files with YAML metadata |
| **Citation Milestones** | None / unanchored text blocks | **Universal column anchors** (`{#pg.44.125}`, `{#pl.87.1089a}`) |
| **Oriental Corpus** | Absent | **Patrologia Orientalis added** (60 volumes, Syriac/Eastern) |
| **English Machine Noise**| Unfiltered machine translations | **Stripped to pure original languages** (`grc`, `la`, `syc`) |

---

## 2. Directory Structure & File Metadata

Treatises are partitioned by volume directories. Every Markdown document opens with structured YAML frontmatter:

```yaml
---
id: pg.044.578
title: "On the Making of Man (De Hominis Opificio)"
creator: "Gregory of Nyssa"
language: grc
volume: "PG 44"
columns: "123–197"
anchors: "sigla.reference — {#pg.44.colN}"
---
```

### Universal Column Milestones
The traditional Migne column numbers are marked throughout the body:

```markdown
[123] {#pg.44.123}

### ΤΟΥ ΕΝ ΑΓΙΟΙΣ ΓΡΗΓΟΡΙΟΥ ΝΥΣΣΗΣ ΠΕΡΙ ΚΑΤΑΣΚΕΥΗΣ ΑΝΘΡΩΠΟΥ.
Εἰ ταῖς διὰ τῶν χρημάτων τιμαῖς ἔδει γεραίρειν τοὺς κατʼ ἀρετὴν διαφέροντας...
```

---

## 3. Computational Search & LLM Retrieval

Because every volume is partitioned into UTF-8 Markdown treatises with exact column milestones, the corpus can be indexed directly into Obsidian, SQLite FTS5, or queried using `ripgrep`:

```bash
# Search for polytonic Greek terms across the Greek Fathers
rg -i "ἐπέκτασις" Patrologia_Graeca/

# Search for Latin dogmatic terms across the Latin Fathers
rg -i "Trinitatis" Patrologia_Latina/

# Jump directly to a Migne column anchor
rg "\{#pg\.44\.125\}" Patrologia_Graeca/
```

### Python Manifest Querying
The catalog in `migne_manifest.json` provides programmatic mapping for every treatise:

```python
import json

with open("migne_manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

# Inspect treatises in PG 44 (St Gregory of Nyssa)
for treatise in manifest["PG"]["44"]["treatises"]:
    print(f"[{treatise['columns']}] {treatise['title']} -> {treatise['file']}")
```

---

## 4. Provenance & Acknowledgements
- **Migne Patrologia Cursus Completus**: Originally published by Abbé Jacques-Paul Migne (Paris, 1844–1866); public domain worldwide.
- **TEI Transcriptions**: Open Greek and Latin Project (University of Leipzig), Perseus Digital Library (Tufts University), Corpus Corporum (Universität Zürich), and The Faith Received (Mere Orthodoxy).
- **Curated & Anchored Edition**: Processed, anchored, and catalogue-indexed by Tobias Hoonhout and Anthony Stratford.
