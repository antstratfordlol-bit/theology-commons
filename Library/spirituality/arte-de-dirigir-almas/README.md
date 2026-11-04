# *El arte de dirigir almas*

*Una selección de textos para un posible itinerario* — **José Manuel Martín (ed.), Roma 2012.**
Eight signed chapters on the practice of spiritual direction, held here **in Spanish and
English**, sixteen files, 1.0 M characters. Sigla `arte-dirigir-almas`.

Fetched 2026-08-31 from **collationes.org**, not from opusdei.org, by
`99. Tools/collationes/convert_arte.py`. The PDFs are in the store at
`01. Sources/_originals/Library/spirituality/arte-de-dirigir-almas/`.

## Why this work is here and not retired

The Biblioteca decode's `DEspiritual` corpus carried a standing instruction: *fetch the
official text from opusdei.org, then retire*. **This work is 48 % of that corpus and is not
on opusdei.org at all.** It is published on collationes.org — which the decode's own colophon
names five times against a single mention of opusdei.org — and the library's own *Discernir,
acompañar y orientar* course sets one of its chapters as reading. Carrying out the
instruction as written would have destroyed the largest single work in either decode corpus.
Alex ruled on 31 August 2026: **fetch, compare, then promote**. The investigation behind it is
`05. Working Docs/research/2026-08-31-resumenes-despiritual.md`; the corrected rows are
`04. Reference/biblioteca-disposition.md` and `04. Reference/biblioteca-final-review.md` §13.

## The chapters, and how to cite them

The anchor is **the work's own part-and-chapter numbering**, as the collationes.org resource
page prints it, written arabic: `arte-dirigir-almas.<part>.<chapter>`.

| Anchor | Part | Chapter | Author |
|---|---|---|---|
| `arte-dirigir-almas.1.1` | I. Perspectiva histórica | Breve panorámica histórica de la dirección espiritual hasta el siglo XIX | Manuel Belda |
| `arte-dirigir-almas.2.1` | II. La dirección espiritual: aspectos generales | Práctica de la dirección espiritual | José Luis Gutiérrez |
| `arte-dirigir-almas.2.2` | II | La dirección espiritual personal: una aproximación teológico-espiritual desde el espíritu y la experiencia del Opus Dei | Guillaume Derville |
| `arte-dirigir-almas.3.1` | III. Factores y circunstancias relacionados con la formación espiritual | Factores culturales de especial incidencia en la formación espiritual | Ángel Rodríguez Luño |
| `arte-dirigir-almas.4.1` | IV. Algunas situaciones particulares en la dirección espiritual | Aspectos de la dirección espiritual especialmente relacionados con la vida social | Martin Schlag |
| `arte-dirigir-almas.4.2` | IV | Acompañamiento espiritual en las diversas circunstancias de la vida | José Luis Gutiérrez |
| `arte-dirigir-almas.4.3` | IV | Noviazgo y matrimonio | Michele Díaz |
| `arte-dirigir-almas.4.4` | IV | La dirección espiritual de personas que padecen alguna enfermedad | Wenceslao Vial Mena |

**Sections are rendered as headings and are deliberately not anchored.** Their numbering is
not language-invariant: 2.1, 4.2 and 4.3 number their sections in Spanish and leave them
unnumbered in English, and 4.4 numbers its conclusion in Spanish (`5. CONCLUSIÓN`) and not in
English. An anchor set built on them would resolve in one language and not the other. That is
the `ocariz-vivir-hijos-dios` rule, and it is also why every anchor here stands over a real
body.

## What the fetch was measured against

Two witnesses, neither of them the output read back.

1. **The PDFs the files came from**: 95.4–99.8 % of each PDF's word tokens are in its file.
   The shortfall is the contents list, which is read but not written.
2. **The Biblioteca decode of the same chapters**, extracted from a `.pdb` by a different tool
   at the same 2012 vintage. Per chapter, in Spanish:

| Chapter | decode words | written words | decode ⊂ written | written ⊂ decode | 8-word shingles |
|---|---:|---:|---:|---:|---:|
| 1.1 | 3,554 | 3,441 | 96.3 % | 99.5 % | 88.8 % |
| 2.1 | 9,926 | 9,724 | 97.3 % | 99.3 % | 86.2 % |
| 2.2 | 13,797 | 13,564 | 97.3 % | 99.0 % | 82.5 % |
| 3.1 | 8,221 | 8,108 | 98.4 % | 99.8 % | 93.7 % |
| 4.1 | 4,534 | 4,462 | 98.1 % | 99.7 % | 88.1 % |
| 4.2 | 9,407 | 9,298 | 98.7 % | 99.8 % | 93.4 % |
| 4.3 | 10,251 | 10,042 | 97.8 % | 99.8 % | 87.8 % |
| 4.4 | 21,706 | 21,510 | 99.0 % | 99.9 % | 94.3 % |

Every run the decode holds and this text does not is a **decode artefact** — its own record
headers (`document despiritual page 22 characters 16569 …`), its contents blocks, and its
run-together note apparatus. **Nothing substantive is held by the decode and not here**, which
is what licensed the retirement of `DEspiritual` to the store the same day.
`99. Tools/guard/check_anchor_bodies.py` reports no empty anchor in these sixteen files.

## What the source itself is missing, declared and never smoothed

Each file's `declared:` names its own. The pattern worth knowing: several chapters print a
footnote for which no marker appears anywhere in the text — nine of them in 4.4 — and 4.3
prints a marker 38 in Spanish for which no note is given. **The same numbers are unmarked in
both languages**, which is what shows these to be the source's own state and not the
conversion's. No marker and no note is invented.

## Two things that differ between the languages, and are the publisher's

The two languages are **separate revisions published on different dates**, not one text in two
forms, and each file says so in `language-differences:`. 4.2 is dated October 2011 in Spanish
and October 2010 in English; 4.3 October 2011 and October 2010. Footnote counts differ by one
or two in five chapters. The English of 4.4 carries `© CRIS, 2010` where every other file
carries `© ISSRA, <year>`.

## Rights

Every chapter closes with a **dual copyright line** — `© ISSRA, <year>` and `© <author>,
<year>` — beside free publication of the whole text in four languages, with no licence
statement and no permission notice anywhere on collationes.org. That exact wording is in each
file's `rights:` field. It is **not** the `NOT ESTABLISHED` case: authorship is complete and
the rightsholders are named.
