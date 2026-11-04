# The Latin West — the register

The Latin Christian literature of the fifth to the twelfth century, converted
from the **openMGH** TEI editions of the Monumenta Germaniae Historica on
**31 August 2026**: 250 works from 37 volumes, 10,956 anchors, 22.4 M characters,
all in Latin, all original-language. The first pass took 132 works from 31
volumes; SS rer. Merov. 2–7, Krusch's *Passiones vitaeque sanctorum aevi
Merovingici* and the Fredegar volume, were added the same day and brought 118
more — the largest hagiographic dossier in Latin for the early West. The shelf
exists because this library was strong in patristics and magisterium and had
almost nothing of the early medieval West.

**How it was made and every decision behind it**: `99. Tools/mgh/README.md`.
That file carries the provenance, the licence and the anchoring argument; this
one is the register of what is here.

## Citing from this shelf

**Cite the work's own division in prose, and give the MGH page as the anchor.**

> Salvian, *De gubernatione Dei*, IV, 15 (MGH Auct. ant. 1,1, ed. Halm, Berlin
> 1877 — LA) · `salvian-de-gubernatione-dei.p54`

The book and chapter are in the text, printed as running headings; they are
**not** in the markup, and none was invented. The anchor is therefore the MGH
printed page and nothing finer — `{#sigla.pN}`, one heading per page, the same
form as `aas`. The `p` prefix keeps the page space clear of a book-and-chapter
space, should one ever be built by hand.

**Each file opens with a derived table of its own divisions** — every `part` and
`section` in the TEI, the page it opens on, and its opening words. For Salvian
that reads *praefatio, LIBER I … LIBER VIII* with the page of each, which is how
to get from a citation like IV, 15 to the right page. The table is apparatus: it
carries no anchor and is not indexed.

## Naming

`<author-key>-<work-key>`, lowercase kebab, **English author name and Latin work
title**, `v` never `u`, per `04. Reference/citation-guide.md`. A byname
disambiguates where a bare name would not (`gregory-tours-historiae`, on the
`gregory-great-dialogi` precedent); a work with no named author takes the Latin
title alone; a work MGH prints as spurious or misattributed takes `pseudo-`.
All 132 checked with `99. Tools/anchors/check_sigla.py` before minting.

## Text quality

MGH's own critical text, **transcribed and not OCR'd**, and the openMGH files
carry the reading text only — there is **no apparatus criticus** in them, so
none was dropped. Printed lines are kept as MGH set them. Line-end hyphenation
is resolved from the TEI's own `@lemma` (44,857 groups, none unresolved); the
handful of line-end hyphens the TEI does not mark up at all are left broken and
named page by page in each file's `text_quality`. `|` (MGH's manuscript column
mark, which falls inside words) and `†` (the crux desperationis) are kept.

Character retention was verified at **100.00 % on all 132 files** by an
independent reader, and **131 of the 132 contain their author's name in the
text**; the exception is `pseudo-venantius-carmina-spuria`, where MGH's own
heading is *Carminum spuriorum appendix* and the attribution is its placement,
not the text's claim.

**Second tranche, 31 August 2026 — MGH SS rer. Merov. 2, 3 and 4** (Krusch, 1888, 1896,
1902): the Merovingian hagiographic dossier, **64 works, 1,269 anchors, 2.8 M characters**,
verified at **100.00 % character retention on all 64**, anchors equal to the `<pb>` count on
every file, no duplicate anchor and no duplicate `id:` anywhere on the shelf, and no empty
anchor. **Fifty-six of the 64 are anonymous or of more than one hand and carry no author
key** — a life is not by its subject, and the *Vita Genovefae* is not Genovefa's. Of the
eight that do name an author, **seven name him inside their own text** (a prologue
salutation or a colophon: *Lupus Waldoni suo salutem*, *Hincmarus nomine non merito
episcopus*, *Balthenus infimus servorum Dei servulus*, *Ado Viennensis episcopus*,
*Florentius presbyter*, *Albinus* and *pauperis Alcuini*, *Eucherius* to Salvius). The eighth,
`gislemar-vita-droctovei`, does **not**: the name Gislemar occurs once in the whole volume,
in MGH's own `@n` for the work, and nowhere in the printed text. The attribution there is the
edition's and the file says so.

`century` in this tranche is filled **only** where a named, dated author or the file's own
words fix it. The composition dates of the anonymous Merovingian lives are a scholarly
question the edition does not settle, so the field is left empty rather than guessed.

## Licence and attribution — required in any reuse

CC BY 4.0. The licence covers the markup added by the **Monumenta Germaniae
Historica (MGH)** and the **Bavarian State Library, Munich (BSB)**; MGH claims
no rights in the medieval text itself. Attribution must name both, and the
source `www.mgh.de/mgh-digital/openmgh`. Every file carries this in its
frontmatter. The TEI originals are in the store at
`01. Sources/_originals/Library/latin-west/`.

---

## The works, by volume

### MGH Auct. ant. 1,1 — ed. Halm, Karl, 1877

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `salvian-de-gubernatione-dei` | *De gubernatione Dei* | Salvian of Marseilles | (1)–108 | 108 |
| `salvian-epistulae` | *Epistulae* | Salvian of Marseilles | 108–119 | 12 |
| `salvian-ad-ecclesiam` | *Ad ecclesiam* | Salvian of Marseilles | (120)–168 | 49 |

### MGH Auct. ant. 1,2 — ed. Sauppe, Hermann, 1877

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `hymnus-sancti-severini` | *Hymnus sancti Severini* | anonymous | (XIX)–XX | 2 |

### MGH Auct. ant. 12 — ed. Mommsen, Theodor, 1894

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `cassiodorus-variae` | *Variae* | Cassiodorus | (1)–385 | 384 |
| `epistulae-theodericianae-variae` | *Epistulae Theodericianae variae* | various | (387)–392 | 5 |
| `acta-synhodorum-romae` | *Acta synhodorum habitarum Romae* | various | (393)–455 | 55 |
| `cassiodorus-orationes` | *Orationum reliquiae* | Cassiodorus | (457)–484 | 21 |

### MGH Auct. ant. 14 — ed. Vollmer, Friedrich, 1905

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `dracontius-carmina` | *Carmina* | Dracontius | (23)–228 | 206 |
| `eugenius-toledo-carmina` | *Carmina et epistulae* | Eugenius of Toledo | (231)–(291) | 61 |

### MGH Auct. ant. 15 — ed. Ehwald, Rudolf, 1919

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `aldhelm-carmina-ecclesiastica` | *Carmina ecclesiastica* | Aldhelm | 11–32 | 22 |
| `aldhelm-de-metris` | *Epistula ad Acircium* | Aldhelm | 59–204 | 146 |
| `aldhelm-de-virginitate-prosa` | *De virginitate (prosa)* | Aldhelm | 226–323 | 98 |
| `aldhelm-de-virginitate-carmen` | *De virginitate (carmen)* | Aldhelm | 350–471 | 122 |
| `aldhelm-epistulae` | *Epistulae* | Aldhelm | (475)–503 | 28 |
| `aldhelm-carmina-rhythmica` | *Carmina rhythmica* | Aldhelm | 524–537 | 14 |

### MGH Auct. ant. 3,1 — ed. Halm, Karl, 1879

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `victor-vita-historia-persecutionis` | *Historia persecutionis Africanae provinciae* | Victor of Vita | (1)–58 | 58 |
| `passio-martyrum-carthaginiensium` | *Passio beatissimorum martyrum* | anonymous | (59)–62 | 4 |

### MGH Auct. ant. 4,1 — ed. Leo, Friedrich, 1881

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `venantius-carmina` | *Carmina* | Venantius Fortunatus | (1)–270 | 267 |
| `venantius-carmina-appendix` | *Appendix carminum* | Venantius Fortunatus | (271)–292 | 22 |
| `venantius-vita-martini` | *Vita sancti Martini* | Venantius Fortunatus | (293)–370 | 78 |
| `pseudo-venantius-carmina-spuria` | *Carminum spuriorum appendix* | Pseudo-Venantius Fortunatus | (371)–386 | 16 |

### MGH Auct. ant. 4,2 — ed. Krusch, Bruno, 1885

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `venantius-vitae-sanctorum` | *Vitae sanctorum* | Venantius Fortunatus | (1)–54 | 54 |
| `pseudo-venantius-opuscula` | *Opuscula male attributa* | Pseudo-Venantius Fortunatus | (55)–110 | 56 |

### MGH Auct. ant. 6,2 — ed. Peiper, Rudolf, 1883

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `avitus-epistulae-homiliae` | *Epistulae et homiliae* | Avitus of Vienne | (1)–157 | 157 |
| `avitus-appendix` | *Appendix* | various | (159)–(199) | 40 |
| `avitus-carmina` | *Carmina* | Avitus of Vienne | (201)–294 | 93 |

### MGH Auct. ant. 7 — ed. Vogel, Friedrich, 1885

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `ennodius-opera` | *Opera* | Ennodius of Pavia | (LXIII)–326 | 327 |
| `florianus-epistulae` | *Epistulae* | Florianus of Romenum | (LIX)–LXI | 3 |

### MGH Auct. ant. 8 — ed. Lütjohann, Christian, 1887

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `sidonius-epistulae` | *Epistulae* | Sidonius Apollinaris | (1)–172 | 172 |
| `sidonius-carmina` | *Carmina* | Sidonius Apollinaris | (173)–264 | 92 |
| `faustus-riez-epistulae` | *Epistulae* | Faustus of Riez | (265)–298 | 34 |
| `ruricius-epistulae` | *Epistulae* | Ruricius of Limoges | (299)–350 | 52 |

### MGH SS rer. Merov. 1,1 — ed. Krusch, Bruno, 1951

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `gregory-tours-historiae` | *Libri historiarum X* | Gregory of Tours | (1)–537 | 536 |

### MGH SS rer. Merov. 1,2 — ed. Krusch, Bruno, 1969

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `gregory-tours-miracula` | *Miracula* | Gregory of Tours | (1)–370 | 338 |
| `gregory-tours-miracula-andreae` | *Liber de miraculis beati Andreae* | Gregory of Tours | (371)–396 | 22 |
| `gregory-tours-passio-septem-dormientium` | *Passio septem dormientium* | Gregory of Tours | (397)–403 | 7 |
| `gregory-tours-de-cursu-stellarum` | *De cursu stellarum* | Gregory of Tours | (404)–422 | 17 |
| `gregory-tours-in-psalterium` | *In psalterii tractatum commentarius* | Gregory of Tours | (423)–427 | 5 |
| `passio-iuliani-martyris` | *Passio sancti Iuliani martyris* | anonymous | 429–431 | 3 |

### MGH SS rer. Merov. 2 — ed. Krusch, Bruno, 1888

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `chronica-fredegarii` | *Chronica* | anonymous | 18–193 | 176 |
| `passio-sigismundi-et-vita-chrothildis` | *Passio sancti Sigismundi regis; Vita sanctae Chrothildis* | anonymous | 333–348 | 15 |
| `vita-chlodovaldi` | *Vita Chlodovaldi* | anonymous | 350–357 | 8 |
| `de-vita-radegundis-libri-duo` | *De vita sanctae Radegundis libri duo* | various | 364–395 | 32 |
| `gesta-dagoberti` | *Gesta Dagoberti I regis Francorum* | anonymous | 399–425 | 27 |
| `vita-arnulfi` | *Vita Arnulfi* | anonymous | 432–446 | 15 |
| `vita-geretrudis` | *Vita Geretrudis* | anonymous | 453–474 | 22 |
| `vita-balthildis` | *Vita Balthildis* | anonymous | 482–508 | 27 |
| `vita-dagoberti-iii` | *Vita Dagoberti III* | anonymous | 511–524 | 14 |

### MGH SS rer. Merov. 3 — ed. Krusch, Bruno, 1896

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `vita-lucii-curiensis` | *Vita Lucii* | anonymous | 2–7 | 6 |
| `passio-quirini` | *Passio Quirini* | anonymous | 11–20 | 10 |
| `eucherius-passio-acaunensium` | *Passio Acaunensium martyrum* | Eucherius of Lyon | 32–41 | 10 |
| `conversio-et-passio-afrae` | *Conversio et passio Afrae* | anonymous | 55–64 | 10 |
| `passio-floriani` | *Passio Floriani* | anonymous | 68–71 | 4 |
| `lupus-ferrieres-vita-maximini` | *Vita Maximini* | Lupus of Ferrieres | 74–82 | 9 |
| `vita-servatii` | *Vita Servatii* | anonymous | 87–91 | 5 |
| `vita-bibiani` | *Vita Bibiani* | anonymous | 94–100 | 7 |
| `vita-memorii` | *Vita Memorii* | anonymous | 102–104 | 3 |
| `vita-aniani` | *Vita Aniani* | anonymous | 108–117 | 10 |
| `vita-lupi-trecensis` | *Vita Lupi Trecensis* | anonymous | 120–124 | 5 |
| `vita-patrum-iurensium` | *Vita patrum Iurensium* | anonymous | 131–166 | 36 |
| `vita-severini-acaunensis` | *Vita Severini Acaunensis* | anonymous | 168–170 | 3 |
| `vita-abbatum-acaunensium` | *Vita abbatum Acaunensium* | anonymous | 174–183 | 10 |
| `vita-eptadii` | *Vita Eptadii* | anonymous | 186–194 | 9 |
| `vita-apollinaris-valentinensis` | *Vita Apollinaris* | anonymous | 197–203 | 7 |
| `vita-genovefae` | *Vita Genovefae* | anonymous | 215–238 | 24 |
| `hincmar-vita-remigii` | *Vita Remigii* | Hincmar of Reims | 250–349 | 100 |
| `balther-vita-fridolini` | *Vita Fridolini* | Balther | 354–369 | 16 |
| `vita-melanii` | *Vita Melanii* | anonymous | 372–376 | 5 |
| `vita-iuniani` | *Vita Iuniani* | anonymous | 377–379 | 3 |
| `vita-aviti-aurelianensis` | *Vita Aviti Aurelianensis* | anonymous | 383–385 | 3 |
| `vita-carileffi` | *Vita Carileffi* | anonymous | 389–394 | 6 |
| `vita-leonardi` | *Vita Leonardi* | anonymous | 396–399 | 4 |
| `vita-vedastis-duplex` | *Vita Vedastis duplex* | various | 406–427 | 22 |
| `vita-fidoli` | *Vita Fidoli* | anonymous | 428–432 | 5 |
| `vitae-caesarii-arelatensis` | *Vitae Caesarii libri duo* | various | 457–501 | 45 |
| `vita-nicetii-lugdunensis` | *Vita Nicetii* | anonymous | 521–524 | 4 |
| `ado-vienne-vita-theudarii` | *Vita Theudarii* | Ado of Vienne | 526–530 | 5 |
| `vita-tigridis` | *Vita Tigridis* | anonymous | 533–534 | 2 |
| `gislemar-vita-droctovei` | *Vita Droctovei* | Gislemar | 537–543 | 7 |
| `vita-dalmatii` | *Vita Dalmatii* | anonymous | 545–549 | 5 |
| `vita-eparchii` | *Vita Eparchii* | anonymous | 553–564 | 12 |
| `miracula-martini-vertavensis` | *Miracula Martini Vertavensis* | anonymous | 567–575 | 9 |
| `vita-aridii` | *Vita Aridii* | anonymous | 581–612 | 32 |
| `vita-betharii` | *Vita Betharii* | anonymous | 613–619 | 7 |
| `vitae-desiderii-viennensis` | *Vitae Desiderii Viennensis* | various | 630–648 | 19 |
| `vita-gaugerici` | *Vita Gaugerici* | anonymous | 652–658 | 7 |

### MGH SS rer. Merov. 4 — ed. Krusch, Bruno, 1902

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `vita-walarici` | *Vita Walarici* | anonymous | 160–175 | 16 |
| `vita-lupi-senonensis` | *Vita Lupi Senonensis* | anonymous | 179–187 | 9 |
| `vita-austrigisili` | *Vita Austrigisili* | anonymous | 191–208 | 18 |
| `vitae-amati-romarici-adelphii` | *Vitae Amati, Romarici, Adelphii* | anonymous | 215–228 | 14 |
| `vita-galli-triplex` | *Vita Galli triplex* | various | 251–337 | 87 |
| `florentius-vita-rusticulae` | *Vita Rusticulae* | Florentius | 339–351 | 13 |
| `passio-thrudperti` | *Passio Thrudperti* | anonymous | 357–363 | 7 |
| `vita-sulpicii-bituricensis` | *Vita Sulpicii* | anonymous | 371–380 | 10 |
| `alcuin-vita-richarii` | *Vita Richarii* | Alcuin | 389–401 | 13 |
| `vita-goaris` | *Vita Goaris* | anonymous | 411–423 | 13 |
| `vita-fursei-et-passio-haimhrammi` | *Vita Fursei; Vita vel passio Haimhrammi* | anonymous | 434–524 | 71 |
| `antiphonae-haimhrammi` | *Antiphonae de sancto Haimhrammo* | anonymous | 525–526 | 2 |
| `vita-bavonis` | *Vita Bavonis* | anonymous | 534–546 | 13 |
| `vita-desiderii-cadurcensis` | *Vita Desiderii Cadurcensis* | anonymous | 563–602 | 40 |
| `vita-sigiramni` | *Vita Sigiramni* | anonymous | 606–625 | 20 |
| `vita-geremari` | *Vita Geremari* | anonymous | 628–633 | 6 |
| `vita-eligii` | *Vita Eligii* | various | 663–761 | 95 |

### MGH SS rer. Merov. 5 — ed. Krusch, Bruno, 1910

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `vita-wandregiseli` | *Vita Wandregiseli* | anonymous | 13–24 | 12 |
| `bobolenus-vita-germani-grandivallensis` | *Vita Germani abbatis Grandivallensis* | Bobolenus | 33–40 | 8 |
| `vita-sadalbergae` | *Vita Sadalbergae* | anonymous | 49–66 | 18 |
| `vita-frodoberti` | *Vita Frodoberti* | anonymous | 72–88 | 17 |
| `vita-remacli` | *Vita Remacli* | anonymous | 104–111 | 8 |
| `ermenbert-vita-vincentiani` | *Vita Vincentiani* | Ermenbertus | 116–128 | 13 |
| `vita-menelei` | *Vita Menelei* | anonymous | 135–157 | 23 |
| `vita-nivardi` | *Vita Nivardi* | anonymous | 160–171 | 12 |
| `vita-faronis` | *Vita Faronis* | various | 184–206 | 23 |
| `passio-ragneberti` | *Passio Ragneberti* | anonymous | 209–211 | 3 |
| `passio-praeiecti` | *Passio Praeiecti* | anonymous | 225–248 | 24 |
| `passiones-leudegarii` | *Passiones Leudegarii* | various | 282–362 | 81 |
| `vita-memmii` | *Vita Memmii* | anonymous | 365–367 | 3 |
| `visio-baronti` | *Visio Baronti* | anonymous | 377–394 | 18 |
| `vita-amandi` | *Vita Amandi* | various | 428–485 | 58 |
| `julian-toledo-historia-wambae` | *Historia Wambae regis* | Julian of Toledo | 500–535 | 36 |
| `vita-audoini` | *Vita Audoini* | anonymous | 553–567 | 15 |
| `vita-filiberti` | *Vita Filiberti* | various | 583–606 | 24 |
| `vita-lantberti-fontanellensis` | *Vita Lantberti* | anonymous | 608–612 | 5 |
| `aigradus-vita-ansberti` | *Vita Ansberti* | Aigradus | 618–643 | 26 |
| `vita-condedi` | *Vita Condedi* | anonymous | 646–651 | 6 |
| `vita-eremberti` | *Vita Eremberti* | anonymous | 653–656 | 4 |
| `vita-vulframni` | *Vita Vulframni* | Ionas | 661–673 | 13 |
| `vita-ermenlandi` | *Vita Ermenlandi* | anonymous | 682–710 | 29 |
| `passio-kiliani` | *Passio Kiliani* | anonymous | 722–753 | 8 |
| `vitae-audomari-bertini-winnoci` | *Vitae Audomari, Bertini et Winnoci* | various | 753–786 | 34 |

### MGH SS rer. Merov. 6 — ed. Krusch, Bruno, 1913

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `vita-erhardi` | *Vita Erhardi* | Paulus | 8–23 | 16 |
| `vita-odiliae` | *Vita Odiliae* | anonymous | 37–50 | 14 |
| `passio-desiderii-et-reginfridi` | *Passio Desiderii et Reginfridi* | anonymous | 55–63 | 9 |
| `vita-anstrudis` | *Vita Anstrudis* | anonymous | 66–78 | 13 |
| `vita-aldegundis` | *Vita Aldegundis* | various | 85–109 | 17 |
| `vita-boniti` | *Vita Boniti* | anonymous | 119–139 | 21 |
| `vita-hrodberti` | *Vita Hrodberti* | anonymous | 157–162 | 6 |
| `stephen-vita-wilfridi` | *Vita Wilfridi* | Stephanus presbyter | 193–263 | 71 |
| `donatus-vita-trudonis` | *Vita Trudonis* | Donatus | 273–298 | 26 |
| `vitae-landiberti-traiectensis` | *Vitae Landiberti* | various | 353–429 | 77 |
| `vita-landelini` | *Vita Landelini* | anonymous | 438–444 | 7 |
| `vitae-ursmari-et-erminonis` | *Vitae Ursmari et Erminonis* | various | 453–470 | 18 |
| `vita-hugberti` | *Vita Hugberti* | anonymous | 482–496 | 15 |
| `vitae-corbiniani` | *Vitae Corbiniani* | various | 560–635 | 76 |

### MGH SS rer. Merov. 7 — ed. Krusch, Bruno, 1920

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `vita-et-miracula-leutfredi` | *Vita et miracula Leutfredi* | anonymous | 7–18 | 12 |
| `vita-pardulfi` | *Vita Pardulfi* | anonymous | 24–40 | 17 |
| `vita-eucherii` | *Vita Eucherii* | anonymous | 46–80 | 31 |
| `alcuin-vita-willibrordi` | *Vita Willibrordi* | Alcuin | 113–141 | 29 |
| `vita-gangulfi` | *Vita Gangulfi* | anonymous | 155–174 | 20 |
| `vita-bertuini` | *Vita Bertuini* | anonymous | 177–182 | 6 |
| `vita-gamalberti` | *Vita Gamalberti* | anonymous | 185–191 | 7 |
| `passio-afrae-supplementum` | *Passio Afrae (supplementum)* | anonymous | 200–224 | 11 |
| `constantius-vita-germani` | *Vita Germani* | Constantius | 247–283 | 37 |
| `vita-sollemnis` | *Vita Sollemnis* | anonymous | 311–321 | 11 |
| `venantius-vita-germani-parisiaci` | *Vita Germani episcopi Parisiaci* | Venantius Fortunatus | 372–428 | 57 |
| `vita-lonoghylii` | *Vita Lonoghylii* | various | 432–437 | 6 |
| `vita-richarii` | *Vita Richarii* | anonymous | 444–453 | 10 |
| `libellus-de-ecclesiis-claromontanis` | *Libellus de ecclesiis Claromontanis* | anonymous | 456–467 | 12 |

**A note on the author column in SS rer. Merov. 5–7.** These are 130-odd saints'
lives and most of them are anonymous, so `anonymous` here means *the file names
no writer*, and the sigla is the Latin title alone. Nine works carry an author
key, and every one of the nine was read off the file itself — MGH's own printed
rubric (*auctore Venantio Fortunato*, *Stephani presbiteri*, *a domino Iuliano
Toletanae sedis episcopo edita est*) or the work's own dedication or colophon
(Bobolenus, Aigradus, Donatus, Alcuin, Constantius, Ermenbertus). `various`
means MGH prints several pieces by different hands as one work-group; the hands
it names are in each file's `note:`. Two files name a writer in `author:` but
carry no author key in the sigla, because a bare `jonas-` or `paul-` key would
file them beside a different man: `vita-vulframni`, whose preface is signed
Ionas — not Jonas of Bobbio, whose *Vitae Columbani* are in SS rer. Merov. 4 —
and `vita-erhardi`, whose prologue is signed Paulus.

### MGH SS rer. Germ. 26 — ed. Mommsen, Theodor, 1898

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `eugippius-vita-severini` | *Vita Severini* | Eugippius | (1)–58 | 58 |

### MGH SS rer. Germ. 34 — ed. Winterfeld, Paul von, 1902

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `hrotsvitha-opera` | *Opera* | Hrotsvitha of Gandersheim | 2–246 | 245 |

### MGH SS rer. Germ. 37 — ed. Krusch, Bruno, 1905

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `jonas-vita-columbani` | *Vita Columbani* | Jonas of Bobbio | 144–294 | 151 |
| `jonas-vita-vedastis` | *Vita Vedastis* | Jonas of Bobbio | 309–319 | 11 |
| `jonas-vita-iohannis` | *Vita Iohannis abbatis Reomaensis* | Jonas of Bobbio | 326–344 | 19 |

### MGH SS rer. Germ. 45 — ed. Hofmeister, Adolf, 1912

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `otto-freising-chronica` | *Chronica sive Historia de duabus civitatibus* | Otto of Freising | (1)–457 | 457 |

### MGH SS rer. Germ. 55 — ed. Waitz, Georg, 1884

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `rimbert-vita-anskarii` | *Vita Anskarii* | Rimbert | (13)–100 | 87 |

### MGH SS rer. Germ. 57 — ed. Levison, Wilhelm, 1905

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `willibald-vita-bonifatii` | *Vita Bonifatii* | Willibald | (1)–57 | 57 |
| `martyrologium-fuldense` | *Martyrologium Fuldense* | anonymous | (59)–61 | 3 |
| `vita-bonifatii-radbodi` | *Vita altera Bonifatii* | Radbod of Utrecht | (62)–78 | 17 |
| `vita-bonifatii-tertia` | *Vita tertia Bonifatii* | anonymous | (79)–89 | 11 |
| `vita-bonifatii-quarta` | *Vita quarta Bonifatii* | anonymous | (90)–106 | 17 |
| `vita-bonifatii-quinta` | *Vita quinta Bonifatii* | anonymous | (107)–110 | 4 |
| `otloh-vita-bonifatii` | *Vita Bonifatii* | Otloh of St Emmeram | (111)–216 | 106 |

### MGH SS rer. Germ. 68 — ed. Staub, Johannes, 1999

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `iotsald-vita-odilonis` | *Vita Odilonis* | Iotsald of Saint-Claude | (141)–281 | 141 |
| `epistola-monachorum-silvaenigrae` | *Epistola monachorum Silvae Nigrae* | anonymous | (285)–290 | 6 |
| `epistola-burchardi` | *Epistola Burchardi* | Burchard | (293)–294 | 2 |
| `notitia-de-elevatione-odilonis` | *Notitia de elevatione Odilonis* | anonymous | (297)–(297) | 1 |

### MGH SS rer. Germ. N. S. 10 — ed. Ott, Irene, 1951

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `ruotger-vita-brunonis` | *Vita Brunonis* | Ruotger | (XXXI)–55 | 56 |

### MGH Ldl 1 — ed. Dümmler, Ernst, 1891

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `wido-epistula-ad-heribertum` | *Epistula ad Heribertum* | Wido, a monk | 5–7 | 3 |
| `de-ordinando-pontifice` | *De ordinando pontifice* | anonymous | (8)–14 | 7 |
| `peter-damian-liber-gratissimus` | *Liber gratissimus* | Peter Damian | 17–75 | 59 |
| `peter-damian-disceptatio-synodalis` | *Disceptatio synodalis* | Peter Damian | 77–94 | 18 |
| `humbert-adversus-simoniacos` | *Adversus simoniacos* | Humbert of Silva Candida | 100–253 | 154 |
| `pseudo-udalric-de-continentia-clericorum` | *Epistula de continentia clericorum* | Pseudo-Udalric | 255–260 | 6 |
| `gebhard-salzburg-epistula` | *Epistula ad Herimannum* | Gebhard of Salzburg | 263–279 | 17 |
| `wenric-trier-epistula` | *Epistula ad Gregorium VII* | Wenric of Trier | 284–299 | 16 |
| `manegold-liber-ad-gebehardum` | *Liber ad Gebehardum* | Manegold of Lautenbach | 303–431 | 129 |
| `peter-crassus-defensio-heinrici` | *Defensio Heinrici IV regis* | Peter Crassus | 434–453 | 20 |
| `dicta-de-discordia-papae-et-regis` | *Dicta cuiusdam de discordia papae et regis* | anonymous | (454)–460 | 7 |
| `wido-osnabruck-de-controversia` | *De controversia inter Hildebrandum et Heinricum* | Wido of Osnabrück | 462–470 | 9 |
| `liber-canonum-contra-heinricum` | *Liber canonum contra Heinricum IV* | anonymous | 472–516 | 45 |
| `anselm-lucca-liber-contra-wibertum` | *Liber contra Wibertum* | Anselm of Lucca | 519–528 | 10 |
| `wido-ferrara-de-scismate-hildebrandi` | *De scismate Hildebrandi* | Wido of Ferrara | 532–567 | 36 |
| `bonizo-liber-ad-amicum` | *Liber ad amicum* | Bonizo of Sutri | 571–620 | 50 |
| `decretum-wiberti` | *Decretum Wiberti vel Clementis papae* | Wibert of Ravenna | 622–626 | 5 |

### MGH Ldl 2 — ed. Dümmler, Ernst, 1892

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `bernold-libelli` | *Libelli* | Bernold of Constance | 7–168 | 161 |
| `altercatio-inter-urbanum-et-clementem` | *Altercatio inter Urbanum et Clementem* | anonymous | 170–172 | 3 |
| `liber-de-unitate-ecclesiae-conservanda` | *Liber de unitate ecclesiae conservanda* | anonymous | 184–284 | 101 |
| `walram-et-herrand-epistulae` | *Epistulae de causa Heinrici regis* | Walram of Naumburg and Herrand of Halberstadt | 286–291 | 6 |
| `deusdedit-libellus-contra-invasores` | *Libellus contra invasores et symoniacos* | Deusdedit | 300–365 | 66 |
| `beno-gesta-romanae-ecclesiae` | *Gesta Romanae ecclesiae contra Hildebrandum* | Beno and other cardinals | 369–425 | 55 |
| `garsias-tractatus` | *Tractatus de reliquiis* | Garsias of Toledo | 425–435 | 11 |
| `sigebert-gembloux-apologia` | *Apologia contra eos qui calumniantur missas coniugatorum sacerdotum* | Sigebert of Gembloux | 437–448 | 12 |
| `epistola-leodicensium-adversus-paschalem` | *Epistola Leodicensium adversus Paschalem papam* | clergy of Liège | 451–464 | 14 |
| `hugh-fleury-de-regia-potestate` | *Tractatus de regia potestate et sacerdotali dignitate* | Hugh of Fleury | 466–494 | 29 |
| `de-investitura-episcoporum` | *Tractatus de investitura episcoporum* | anonymous | 498–504 | 7 |
| `ranger-lucca-de-anulo-et-baculo` | *Liber de anulo et baculo* | Ranger of Lucca | 508–533 | 26 |
| `gregory-catino-orthodoxa-defensio` | *Orthodoxa defensio imperialis* | Gregory of Catino | 535–542 | 8 |
| `bruno-segni-de-simoniacis` | *Libellus de symoniacis* | Bruno of Segni | 546–562 | 17 |
| `bruno-segni-epistulae` | *Epistulae quattuor* | Bruno of Segni | (563)–565 | 3 |
| `placidus-de-honore-ecclesiae` | *Liber de honore ecclesiae* | Placidus of Nonantola | 568–639 | 72 |
| `ivo-chartres-epistulae` | *Epistulae* | Ivo of Chartres | (640)–657 | 16 |
| `disputatio-pro-paschali-papa` | *Disputatio vel defensio Paschalis papae* | anonymous | 659–666 | 8 |
| `hildebert-epistulae` | *Epistulae* | Hildebert of Lavardin | 668–675 | 8 |
| `geoffrey-vendome-libelli` | *Libelli* | Geoffrey of Vendôme | 680–700 | 21 |

### MGH Ldl 3 — ed. Dümmler, Ernst, 1897

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `epistula-de-vitanda-missa-uxoratorum` | *Epistula de vitanda missa uxoratorum sacerdotum* | anonymous | 2–11 | 10 |
| `epistula-de-sacramentis-haereticorum` | *Epistula de sacramentis haereticorum* | anonymous | (12)–20 | 9 |
| `hesso-relatio-de-concilio-remensi` | *Relatio de concilio Remensi* | Hesso Scholasticus | 22–28 | 7 |
| `honorius-augustodunensis-libelli` | *Libelli* | Honorius Augustodunensis | 38–80 | 43 |
| `arnulf-sees-invectiva` | *Invectiva in Girardum Engolismensem episcopum* | Arnulf of Sées | 85–108 | 24 |
| `tractatus-de-scismate` | *Tractatus de scismate* | anonymous | 110–130 | 21 |
| `gerhoh-libelli-selecti` | *Libelli selecti* | Gerhoh of Reichersberg | 136–525 | 389 |
| `dialogus-de-pontificatu` | *Dialogus de pontificatu sanctae Romanae ecclesiae* | anonymous | (526)–546 | 20 |
| `carmina-de-schismate-alexandrino` | *Carmina ad schisma Alexandrinum pertinentia* | various | (547)–554 | 7 |
| `walter-insulis-carmina` | *Carmina* | Walter of Châtillon | (555)–560 | 6 |
| `de-fine-schismatis-vaticinium` | *De fine schismatis vaticinium* | anonymous | (561)–570 | 6 |
| `epistula-cameracensium-et-noviomensium` | *Epistula Cameracensium et Noviomensium clericorum* | clergy of Cambrai and Noyon | (573)–578 | 6 |
| `defensio-pro-filiis-presbyterorum` | *Defensio pro filiis presbyterorum* | anonymous | (579)–583 | 5 |
| `fragmentum-merseburgense-de-caelibatu` | *Fragmentum Merseburgense de caelibatu cleri* | anonymous | (584)–587 | 3 |
| `tractatus-pro-clericorum-conubio` | *Tractatus pro clericorum conubio* | anonymous | (588)–596 | 9 |
| `bernold-de-vitanda-excommunicatorum` | *Libellus de vitanda excommunicatorum communione* | Bernold of Constance | (597)–602 | 6 |
| `theobald-etampes-epistula` | *Epistula ad Roscelinum* | Theobald of Étampes | (603)–607 | 5 |
| `de-paenitentia-regum` | *De paenitentia regum et de investitura regali* | anonymous | (608)–614 | 7 |
| `carmen-de-simoniaca-haeresi` | *De simoniaca haeresi carmen* | anonymous | (615)–617 | 3 |
| `satira-in-mettenses` | *Satira in Mettenses* | anonymous | (618)–621 | 4 |
| `monachi-exulis-opusculum` | *Opusculum monachi cuiusdam exulis* | anonymous | (622)–641 | 19 |
| `tractatus-eboracenses` | *Tractatus Eboracenses* | anonymous | (642)–687 | 44 |
| `de-sepultura-falso-excommunicatorum` | *De sepultura eorum qui falso excommunicati dicuntur* | anonymous | (688)–690 | 3 |
| `marbod-opuscula` | *Opuscula* | Marbod of Rennes | (691)–696 | 6 |
| `carmina-in-simoniam` | *Carmina in simoniam et Romanorum avaritiam* | anonymous | (697)–710 | 14 |
| `hugh-metel-opuscula` | *Opuscula* | Hugh Metel | (711)–719 | 8 |
| `hunald-carmen-de-anulo-et-baculo` | *Carmen de anulo et baculo* | Hunald | (720)–722 | 3 |
| `versus-de-anulo-baculo-gladio` | *Versus de anulo baculo gladio et diademate* | anonymous | (723)–725 | 3 |
| `versus-de-anulo-et-baculo` | *Versus de anulo et baculo* | anonymous | 726–728 | 3 |

### MGH QQ zur Geistesgesch. 1 — ed. Wachtel, Alois, 1955

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `alexander-minorita-expositio-in-apocalypsim` | *Expositio in Apocalypsim* | Alexander Minorita | (1)–510 | 510 |

### MGH QQ zur Geistesgesch. 13 — ed. Schmidt, Paul Gerhardt, 1989

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `otloh-liber-visionum` | *Liber visionum* | Otloh of St Emmeram | (33)–113 | 81 |

### MGH QQ zur Geistesgesch. 16 — ed. Nachtmann, Doris, 1998

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `hincmar-de-cavendis-vitiis` | *De cavendis vitiis et virtutibus exercendis* | Hincmar of Reims | (101)–268 | 168 |

### MGH QQ zur Geistesgesch. 4 — ed. Niemeyer, Gerlinde, 1963

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `hermann-de-conversione-sua` | *Opusculum de conversione sua* | Hermannus quondam Iudaeus | (69)–127 | 59 |

### MGH QQ zur Geistesgesch. 5 — ed. Haacke, Rhaban, 1970

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `rupert-deutz-de-victoria-verbi-dei` | *De victoria verbi Dei* | Rupert of Deutz | (1)–426 | 426 |

### MGH QQ zur Geistesgesch. 8 — ed. Hartmann, Wilfried, 1972

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `manegold-liber-contra-wolfelmum` | *Liber contra Wolfelmum* | Manegold of Lautenbach | (39)–108 | 70 |

### MGH Dt. MA 3 — ed. Menzel, Ottokar, 1937

| sigla | work | author | pp. | anchors |
|---|---|---|---|---|
| `vita-liutbirgae` | *Vita Liutbirgae* | anonymous | (10)–46 | 37 |
