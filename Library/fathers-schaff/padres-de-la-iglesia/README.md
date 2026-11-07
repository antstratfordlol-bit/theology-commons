# Padres de la Iglesia — the Spanish anthology

Promoted 2026-08-30 from the Biblioteca iSilo decode (#57) by
`99. Tools/promote/promote_padres.py`; witnessed by `verify_padres.py`.
Repaired and re-derived 2026-08-31 — see **Known defects** below.
**66 authors, one file each**, from Clement of Rome to Isidore of Seville,
8.7 M characters, **519 anchors** under the class sigla `padres` (67 author
sections and 452 pieces).

## Read this before citing anything here

**Nobody knows whose Spanish this is, and no file pretends otherwise.** The
anthology names no translator, edition, publisher or date for any author, in
8.7 MB. It is measurably **not one hand**: five of its author sections address
the reader with Latin-American *ustedes* — Justin 333 occurrences against 25
peninsular forms, Ammonas 89/0, Gregory of Nyssa 40/0, Polycarp 24/12,
Pachomius 7/0 — and the other 58 use peninsular *vosotros*, with pre-1999
accentuation (*éste*, *sólo*, *fué*) throughout. It names an edition in exactly
two places: **BAC 241** (*Obras de San Cipriano*), cited with page ranges inside
the Cyprian section, and PL / PLS / CCL / CSEL line references inside Caesarius
of Arles on the Apocalypse.

**So cite it as what it is** — *Padres de la Iglesia*, the Spanish anthology of
the Biblioteca, translator unknown — and never as a named translation. Where
`../critical/` holds the Greek or Latin, that is the citable text for
scholarship; where the Schaff series holds an English translation, that one at
least names its translator. This shelf is for reading and finding in Spanish.

**Its rights position is not established**, and every file says so in a
`rights:` field. The Greek and Latin is public domain by age; these
translations are not, and they are what is held. **The shelf is in kit-export
scope** — `99. Tools/share/publish.sh` excludes only `05. Working Docs/` and
`USER.md` — so publishing would redistribute it. Awaiting Alex's decision;
`04. Reference/source-index.md` carries the argument.

## Where it came from

Six decode corpora that are **one work**: `Padres` plus the five per-author
satellites its own contents page links to — `PAgustin`, `PCirilo`, `PCreta`,
`PCrisostomo`, `POrigenes`. The compiler is anonymous. The collection's own
colophon (Biblioteca record 0004, now at
`01. Sources/_originals/Biblioteca/_markdown/Biblioteca/`) calls it a private
compilation, *"versión 6"*, made for himself and his friends, contact
`recursos@almudi.org`; almudi.org distributes `.pdb` documents for iSilo, and a
stray HTML 4.01 DOCTYPE fragment surviving as the title of record `Padres/0048`
shows the book was built out of web pages. The decode is untouched and every
file records the records it came from.

## How it is anchored

**No number is minted, because the anthology prints none.** The second position
of an anchor is the title the anthology's **own contents apparatus** gives a
piece — the master index at `Padres/0001`, the per-author *índice* records, or
the contents block heading an author's first record — slugified and truncated
to 24 characters. A line is anchored **if and only if** that apparatus names
it — and only where it carries text of its own. Three things
are therefore left unanchored, and each is named in the file's `declared:`
rather than given an empty section:

- the **second level of captions** the anthology prints above many excerpts
  (*"Hágase tu voluntad, así en la tierra como en el cielo:"*) **where no
  apparatus lists them** — a set built on those would be ours rather than the
  work's. Where the per-author *índice* record does list them, they are
  anchored like any other entry;
- any piece the apparatus names **whose text the decode does not carry**;
- **24 work titles that enclose nothing** — the anthology puts a second-level
  caption immediately under them, so the title has no text between itself and
  that caption. They are printed as unanchored `##` headings above the `###`
  pieces they contain (*Tratado sobre el Padrenuestro*, *Stromata*,
  *Protréptico*, *Cristo redentor*, Irenaeus's seven divisions, Basil's seven
  homily titles). Cite the caption beneath. The proper repair is a two-level
  anchor space, `padres.<author>.<work>.<section>`, which `odsearch ref`
  already resolves through its container fallback; it would rename section ids
  that already exist, so it waits on Alex.

**The heading printed above an anchor is the body's own line, decoration and
all, and the slug comes from the contents list** — so the two can differ:
`### Carta 1. La salud y el cuerpo {#padres.ammonas.carta-1}`, because the
contents list says only *Carta 1*.

## What it adds

**31 of the 66 authors have no work in the Schaff series and none in
`../critical/`.** Caesarius of Arles (212 k characters, with a complete
commentary on the Apocalypse), Dorotheus of Gaza (267 k), Andrew of Crete's
Marian homilies (242 k), Pachomius (109 k), Ammonas (64 k), Peter Chrysologus,
Maximus of Turin, Maximus the Confessor, Isidore of Seville, Ildephonsus of
Toledo, Pacian of Barcelona, Zeno of Verona, Fulgentius of Ruspe, Germanus of
Constantinople, John Climacus, John Mandakuni, John the Solitary, Romanos the
Melodist, Salvian of Marseilles, Jacob of Serugh, Sophronius of Jerusalem,
Theodotus of Ancyra, Evagrius Ponticus, Chromatius of Aquileia, Anastasius of
Sinai, Zephyrinus, the Akáthistos, the *Regla de los Padres*, Antony's letters,
an ancient paschal homily, and the Qumran community rule, which came with the
*.pdb* and is not patristic at all.

**Cyril of Alexandria is the borderline case.** Schaff prints no work of his,
but five of his documents stand in `NPNF2-14` as acts of the Third Ecumenical
Council. For the remaining 34 authors the Spanish is a new language of a work
already held in English or in the original.

## The witness

Never read the output and find it plausible. Re-run `verify_padres.py`:

- **completeness** — 22,207 of the decode's 22,277 non-blank lines are present
  in the promoted text (**99.69%**); 1,827 of 8,748,207 characters are absent
  (**0.021%**), and every absent line is a running head, a nav bar or a
  contents-list title (measured after the 31 August repair; the 30 August run
  scored 99.68% on the same test);
- **containment** — 8-word shingles of each of the 178 source records against
  the promoted text: **median 0.9989, p05 0.9716**. The six records below 0.95
  are contents screens whose content *is* the list, and whose lines are
  therefore navigation. A shingle breaks wherever a navigation line was
  removed, which is why the line count above is the decisive measure and this
  one is the corroborating one;
- **anchors** — 519, none duplicated, none malformed, **and none with no body
  text under it**. That last measurement did not exist on 30 August, and its
  absence is what let 52 empty anchors through; `promote_padres.py --verify`
  makes it as well.

## Sidecar

`_citations.tsv` — the anthology's **16,256 outbound references**, of which
**11,003 point into the CEE Bible**. The promoted prose carries what was
printed (*"(Jn 2, 4)"*); the link target is printed nowhere and would otherwise
be lost, so it is kept in a fourth column, `decode_target`, which nothing reads.

Columns: `src_anchor`, `decode_target_work`, `label`, `decode_target`. The first
three are the shape `99. Tools/links/citation_links.py` reads by name across all
sixteen sidecars in the library; `99. Tools/guard/check_citation_sidecars.py`
checks it.

**Rewritten 2026-08-31, and not by renaming its columns.** The first version had
a header of its own invention, which stopped the citation graph rebuilding at
all; but the column that mattered was `from_anchor`, which held the author
FILE's own top anchor. All 3,021 Chrysostom references were hung on
`padres.san-juan-crisostomo`, which carries 72 characters of text, so renaming
it `src_anchor` would have recorded 16,432 citations that resolve to nothing and
point at a whole 2.2 MB file. The sidecar now names the **enclosing piece** —
291 distinct anchors instead of 44 — and every label in it can be found in the
text of the anchor it is attributed to. 176 rows were dropped: links standing on
the anthology's own contents lines, which are not printed in the promoted text
at all.

## Known defects

### Repaired 2026-08-31 — 52 anchors resolved to nothing

**Between 30 and 31 August 2026 this shelf carried 52 `##` anchors with no body
text at all**, and `odsearch ref padres.san-cipriano.tratado-sobre-el-padrenu`
— the anchor `04. Reference/anchors.md` gave as the worked example for the
sigla — returned *no chunk with anchor*. The check reported above as "534
anchors, none duplicated, none malformed" was true and useless: it measured
uniqueness and form, and never whether an anchor sat above any text.

Two causes, both in the tool, both now fixed there and the shelf re-derived
from the untouched decode at
`01. Sources/_originals/Biblioteca/_markdown/Padres/`:

1. **28 anchors were pinned to the contents list.** The tool matched a
   contents entry to its body heading *verbatim*, and the anthology decorates
   the heading — `Carta 1` in the list against `Carta 1. La salud y el cuerpo`
   in the body; `El Verbo y su generación` against `I. El Verbo y su
   generación`; `Carta 1` … `Carta 7` against `Primera` … `Séptima`. Nothing
   matched, every anchor stayed on the line that named it, and the whole of the
   text fell after the last one: `padres.ammonas.carta-11` held 64,375
   characters and the ten letters above it held none. Two lesser faults fed the
   same failure — a contents block of only two entries was rejected outright
   (Hilary, Hippolytus), and `Padres/0012 f.md`, whose decode title is a stray
   character, had that character read as the start of a piece, which put
   Basil's contents block out of the tool's reach (seven anchors).
2. **24 were work titles that enclose nothing**, described under *How it is
   anchored* above. Those are now printed but not anchored.

Ammonas gained three more: the body prints fourteen letters where the contents
list names eleven, so `pieces: 11` under-declared, and *Carta 12*, *13* and
*14* are now anchored on the body's own witness.

**No anchor that had text lost or changed its id.** 24 ids were withdrawn and
all 24 were among the empty ones; 9 were added. Two author-level anchors,
`padres.san-cipriano` and `padres.clemente-de-alejandria`, now index a one-line
stub — the unanchored work title that opens the file — instead of falling back
to their children; that is the price of printing the title rather than dropping
the line.

**This repair is not visible to search until `99. Tools/index/build_index.py`
runs.** It was being held for a single run while several sessions wrote, so
until then the repaired anchors stay unresolvable and the index still holds the
30 August chunking.

### Defects of the decode, not repaired

- The decode drops **all character styling**, so where the anthology set a
  quoted source in italic the boundary between the Father's words and the
  compiler's framing is lost.
- Three lines in the master index are **two lines joined with no break** —
  `Los frutos de la PasiónSantiago de Sarug` is the clearest. They are split on
  the author name where that is unambiguous and reported by the tool otherwise.
- Record `Padres/0048` is titled `4.01 Transitional//EN">` — the tail of an
  HTML DOCTYPE that leaked into the page table.
