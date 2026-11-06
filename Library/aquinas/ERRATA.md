# Errata and Textual Emendation Protocol

This document establishes the official scholarly protocol for identifying, documenting, verifying, and emending textual errors within the *Corpus Thomisticum* Markdown repository.

---

## 1. Governance Principles & Core Rules

1. **Separation of Research and Textual Emendation:**
   Researchers and AI assistants (including Claude Code, Gemini, and GPT instances) must **never** edit corpus text files during active research, reading, or philosophical analysis sessions. Any suspected corruptions, OCR artefacts, or transcription errors encountered must be logged into this document rather than modified immediately in the source text.

2. **Mandatory Critical Authority Requirement:**
   No correction may be proposed or applied based solely on an AI model's conjecture or intuitive sense of Latin syntax. Every emendation must be supported by an authoritative critical witness:
   * **Primary Authority:** The Leonine Commission critical edition (*Sancti Thomae de Aquino Opera Omnia iussu Leonis XIII P. M. edita*), citing volume, page, line, and apparatus variant.
   * **Secondary Authority:** Established historical critical editions: Marietti (Rome/Turin), Lethielleux (Paris), Vivès, or Enrique Alarcón's *Corpus Thomisticum* (Universidad de Navarra).
   * **Paleographical Authority:** For texts awaiting critical Leonine publication, citation of relevant manuscript witnesses (e.g. *codex autographus*, *exemplar Parisiense*).

3. **Strict Invariant Anchor Preservation:**
   Structural anchor tags (`{#sigla.ref}`) establish cross-lingual alignment between Latin, English, and Spanish parallel files. Textual corrections must **never** modify, delete, or renumber anchor tags. If an anchor is corrupted or displaced, its rectification must be applied synchronously across all parallel language editions.

4. **Dedicated Git Workflow (`corrections` branch):**
   Corrections must not be committed directly to `main`. They are processed in separate, dedicated emendation sessions:
   ```bash
   # Create and switch to the corrections branch
   git checkout -b corrections

   # Apply verified fixes, one work per commit
   git add <file>
   git commit -m "fix(Super-Romanos): emend lect. 1 typo against Leonine t. XIII"

   # Push and open a Pull Request
   git push origin corrections
   ```

---

## 2. Errata Log Schema

When logging an erratum, append a row to the table below using the following format:
* **ID:** Sequential identifier (`ERR-001`, `ERR-002`, etc.).
* **Date:** ISO-8601 date (`YYYY-MM-DD`).
* **Work & File:** Relative filename (e.g. `Summa.1a.la.md`).
* **Anchor / Location:** Structural anchor tag and/or section (e.g. `{#sth.1a.q2.a3}`).
* **Current Reading:** The corrupt or suspect text as currently printed.
* **Proposed Reading:** The emended text.
* **Critical Authority & Evidence:** Edition, volume, page, line, or manuscript reference.
* **Status:** `Pending Verification` | `Verified` | `Applied` | `Rejected`.
* **Reporter:** Name or GitHub handle of contributor.

---

## 3. Active Errata Registry

| ID | Date | Work & File | Anchor / Location | Current Reading | Proposed Reading | Critical Authority & Evidence | Status | Reporter |
|---|---|---|---|---|---|---|---|---|
| ERR-001 | 2026-11-03 | `README.md` | §3 Pauline Corpus | Listed Romans as present | Restored Romans to active tree | Discrepancy between README and repository tree | Applied | Anthony / Colleague |

---

## 4. Submission & Upstream Synchronisation

External contributors and collaborating scholars are encouraged to submit errata via GitHub:
1. Open an Issue with label `erratum` citing the exact anchor and Leonine witness.
2. Or submit a Pull Request from a dedicated feature branch adhering to the single-commit per work standard.
