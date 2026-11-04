# The Catholic Encyclopedia (1913)

*An International Work of Reference on the Constitution, Doctrine, Discipline
and History of the Catholic Church.* Charles G. Herbermann, Edward A. Pace,
Condé B. Pallen, Thomas J. Shahan and John J. Wynne, eds. New York: Robert
Appleton Company and The Encyclopedia Press, 1907–1913. Fifteen volumes, an
index volume, and a supplement of 1922.

**English. Public domain in the United States** — every article carries
`{{PD-US}}` on Wikisource, the work having been published before 1929.

## Where this came from, and why not New Advent

New Advent hosts the same encyclopedia and is the copy most people mean when
they cite it, but it asserts copyright over its own transcription and asks not
to be harvested. `04. Reference/external-corpora.md` records that. English
Wikisource carries an independent volunteer transcription under `{{PD-US}}`,
and that is what is here. **Do not cite New Advent's article numbers** (the
`cathen/15062a.htm` form); cite the printed work.

## How to cite

Author, article, volume — the three things an encyclopedia citation needs — are
in every file's frontmatter.

> Pohle, Joseph. "Grace." *The Catholic Encyclopedia*, vol. 6. New York: Robert
> Appleton Company, 1909. `cathen.grace`

`author` is the full name Wikisource records from the header template; `signed`
is the name printed at the foot of the article, which is usually the initials
(*J. POHLE*). Where they differ, both are right — quote the printed signature.

**Pages, not columns.** The 1913 encyclopedia is paginated by page. Only the
articles Wikisource built by transcluding proofread page scans carry a page
range; the rest were typed in as continuous wikitext and have no page anchors
at all, so their frontmatter reads `pages: unknown`. The counts are in
`99. Tools/encyclopedia/README.md`.

## Anchors

`{#cathen.article-slug}`, one per file, on the H1. An encyclopedia is cited by
article, so nothing below the article is anchored.

```bash
grep -rn '{#cathen\.grace}' "01. Sources/Library/encyclopedia/"
```

## Finding an article — read `_aliases.md` first

The work does not file everything under the word you would search for.
*Marriage* is **Sacrament of Marriage**, *Mass* is **Sacrifice of the Mass**,
*Incarnation* is **The Incarnation**, *Charity* is **Charity and Charities** for
the works and **Love (Theological Virtue)** for the virtue. `_aliases.md` maps
them, in four layers of decreasing authority — the work's own *see* references
first, then a curated list, then Wikisource's redirects, then mechanical
guesses which are marked as guesses.

**There is no article on Transubstantiation.** The printed work does not have
one: volume 15, page 20 reads *"Transubstantiation. See Eucharist."* The
doctrine is treated in *The Real Presence of Christ in the Eucharist* (Pohle,
vol. 5).

## Three kinds of file

Frontmatter `entry-type` distinguishes them.

- `article` — a real article.
- `see-reference — not an article` — an entry the encyclopedia prints only as a
  cross-reference (*Abbacy. See Abbot.*). These are a handful of words long by
  design. They are kept because they are entries in the work and because they
  are how it tells you where a subject is filed, but **a short file is not a
  failed conversion**, and `cross-reference` names the target.
- `container — the material is in the subarticles named in the body` — a
  headword under which Wikisource holds no text at all, because it has put the
  article in subarticles and its page says so. There are **five**: *St.
  Augustine of Hippo* (Life, Teaching, Works), *Jerusalem* (four period
  articles), *Jews and Judaism* (*History of the Jews*, *Judaism*), *Popes
  Benedict I-X* and *Popes Boniface III-VII* (one article per pope). Every
  subarticle is held, so **no text is missing**; the head page's own note is
  the body, and `_aliases.md` routes the headword to the subarticles first.
  Until 2 September 2026 these five were typed `article` with an empty body and
  nothing saying why (state review of 1 September, PUE-1 and B5).

## Five partial transcriptions

Wikisource marks five of these articles `{{incomplete}}` — its volunteers have
not finished transcribing them, and the printed article is longer than what is
here. Their frontmatter now says so, in `transcription: "incomplete on
Wikisource at retrieval"` with the notice itself in `transcription-notice`;
before 2 September 2026 the notice arrived as a row of prose in the article
body and no field declared the gap (PUE-2).

| Article | Volume |
|---|---|
| Austro-Hungarian Monarchy | 2 |
| Benedictine Order | 2 |
| Socialism | 14 |
| Tommaso Campanella | 3 |
| University of Fribourg (Switzerland) | 6 |

*Gaetano Sanseverino* is **not** one of them: the words "This work is
incomplete" in that file are the encyclopedia's own, about Sanseverino's
*Philosophia christiana*.

## The second witness

`validate_cathen.py` answers five questions out of each converted file alone —
including the character count, which it compares with that same file's body and
which therefore cannot ever disagree. `validate_cathen.py --against-cache` is
the check that can: it re-reads the cached Wikisource HTML by a different route
from the converter's own walker and asks whether every prose paragraph of the
source reached the Markdown.

**Run of 2 September 2026: 11,611 articles compared, 68,344 source paragraphs
probed, 0 not found.** No article prose is missing from this shelf.

One defect it turned up is not ours. ***Caracalla*** ends with the word
"block" where its bibliography should be: on Wikisource the `{{Smaller}}`
template was given its arguments the wrong way round, so the bibliography is in
the page's wikitext and **the page itself does not render it**. The converter
reproduced what the page shows. Nothing was invented to fill the hole.

## What this work is, and is not

It is the standard English Catholic reference work of its period, written by
about a thousand named contributors, and it is cited constantly in the older
literature — which is the reason to hold it. **It is 1913 scholarship.** Its
biblical criticism predates *Divino afflante Spiritu* and the Pontifical
Biblical Commission's later work; its history of the Church's relations with
other confessions and with the Jewish people is written in the register of its
day; its science and its ethnography are a century old; and it is written
before two world wars, two councils and the entire modern development of
Catholic social teaching. Use it for what the older literature meant when it
cited an article, for patristic and mediaeval reference, and for biography and
institutional history. **Do not use it as a statement of current teaching** —
that is what the Catechism, the conciliar documents and the magisterium in
`01. Sources/Magisterium/` are for.

The shelf and `_aliases.md` are generated by `99. Tools/encyclopedia/` and are
derived output: regenerate, do not hand-edit. **This page is written by hand**
(the footer said otherwise until 2 September 2026, and no tool has ever written
it).
