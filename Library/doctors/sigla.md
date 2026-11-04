# Sigla — Doctors of the Church corpus

Minted by the extractors in `99. Tools/doctors/` and registered here as a class, like `fathers/sigla.md`, rather than one by one in `anchors.md`.

Pattern: `author-shorttitle.REF`, **language-invariant** — one sigla covers every language a work is held in, so `beda-historia.2.13` is the same chapter of Bede in Latin and English and `juan-subida.2.14` the same chapter of the Subida in the Spanish original and the English translation. The **document id** carries the language (`juan-subida.es`, `juan-subida.en`) because `build_index.py` keys documents by id and would otherwise drop the second language as a duplicate. All sigla checked with `check_sigla.py`.

Where a work is held in both languages, the anchors meet at the level each edition prints: the chapter. Below it the Spanish adds the numbered paragraph (`juan-noche.1.9.2`), which the English editions do not number.

The 47 rows marked `la` from **Migne's Patrologia Latina** (Corpus Corporum, mlat.uzh.ch) entered on 2026-08-30 by `99. Tools/doctors/extract_corpuscorporum.py` — the Latin works of Peter Chrysologus, Hildegard of Bingen, Leo the Great and Gregory the Great. Their anchors are **the work's own division as Migne prints it**, written arabic whatever the source sets (Roman numeral, Latin ordinal word or arabic), dot-joined where the work divides more than once: `chrysologus-sermones.176`, `hildegard-scivias.3.13`. **Migne's column is preserved in the text as an inline `[PL 52, 184A]` marker and is never anchored** — the column is a fact about the printing, not a division of the work. Every one of these files is citable **as Migne and never as a critical text**; each carries the project's two caveats (OCR mistakes; 16th–18th-century, non-critical editions) in its frontmatter.

Three of them take a sigla they would not otherwise need. `gregory-great-dialogi-pl` and `gregory-great-moralia-pl` are the **Migne witnesses** of works already held in English under `gregory-great-dialogi` and `gregory-great-moralia`: Migne divides them differently, and two numbering systems are never merged into one anchor space, so the Latin keeps its own. `gregory-great-moralia-ii` is Migne's second half of the *Moralia* (PL 76), which the site serves as a separate work.

*De vocatione omnium gentium* stands in the site's list under Leo but **is not held**: its TEI carries no column of the printed work at all, only Migne's editors' note referring the reader to another tome, so no file was written.

The 177 works marked `la` for **Peter Damian, Bernard of Clairvaux and Anselm of Canterbury** entered on 2026-09-14 (tracker #70, T4-2), from the same Patrologia Latina site by the same tool, which gained the rules these volumes forced (its docstring, *T4-2*): 175 new rows. Two works join an English already held **on its sigla**, because their chapters were checked to correspond by content as well as number: `bernard-diligendo` (*De diligendo Deo*, 15 chapters; the Latin adds Mabillon's paragraphs) and `anselm-monologion` (Migne's *Monologium*, preface and 79 chapters; one printed numeral repaired and declared, XLII printed for XLIII). Four take `-pl` beside a held English that divides the work differently: `bernard-epistolae-pl`, `bernard-malachia-pl`, `anselm-orationes-pl`, and `anselm-cur-deus-homo-pl`, whose English prints II.18 twice, so that its II.19-22 are Migne's II.20-23. `peter-damian-` is latin-west's prefix; Damian's *Liber gratissimus* and *Disceptatio synodalis* are **not** taken again, being held there in MGH's critical text, and *De translatione S. Hilarii* (PL 9) is not taken, being Sermo II of his *Sermones*. Six Bernard works (*Opuscula duo*, *Super hymnum*, *Tonale*, *De corpore Domini*, *De cantu*, *In verba Evangelii*) and Anselm's *Quaedam dicta utilia* carry an `attribution-doubt` quoting Migne's editors or the witness's own heads. Anselm's letters here are PL 158 only: those Migne prints in PL 159 are not served by the site and are not held.

The 87 `alfonso-*` rows marked *Grimm* entered on 2026-09-14 (#70 T4-3), written by `99. Tools/doctors/convert_grimm.py` from the Internet Archive's OCR of Grimm's Centenary Edition, *The Ascetical Works* (vols. I–VI, IX–XXII; VII–VIII not held). **One file per work, anchored at the work's own printed numbering** — chapter, section, consideration, meditation, visit, letter (`alfonso-lettere.1.373` is Part I letter 373; Part II restarts at 1, so the part is in the anchor; the supplementary runs are `.1.supp.N` and `.2.supp.N`), the psalm by its Vulgate number as Grimm prints it (`alfonso-salmi.118`). Unnumbered units of the author's own carry a slug (`.preface`, `.dedication`); a work that prints no numbering has one anchor on its H1. Grimm's pages are unanchored inline markers `[Grimm VOL, PAGE]`. Every repair of a heading numeral is declared in the file's `repairs:`. Italian titles are given only where certain; otherwise the row says Grimm's English title stands. `alfonso-uniformita-grimm` is Grimm's translation of a work already held (`alfonso-uniformita`, CCEL): its numbering differs, so it has its own anchor space and `status: witness`.

The 269 files marked `la` for **Ambrose, Hilary of Poitiers, Isidore of Seville, Bede, Jerome and Augustine** entered on 2026-09-14 (tracker #70, T4-6), from Corpus Corporum's Patrologia Latina by the same tool, with the rules these volumes forced (its docstring): 264 new sigla. **These sigla keep the Latin title's leading particle**, as `04. Reference/citation-guide.md` prescribes for the Fathers and `fathers/sigla.md` already writes them (`augustine-de-doctrina-christiana`), so that a Migne witness meets a work already registered there; none collided. Three works the site serves as several files are one sigla each, the part in the document id: `ambrose-epistolae-pl` (letters 1-91, `.la.1`-`.la.2`), `augustine-sermones-pl` (the Maurist sermons 1-363 in four classes, `.la.1`-`.la.4`) and `augustine-enarrationes-in-psalmos-pl` (psalms 1-150, `.la.1`-`.la.2`). Works whose Latin is already held in the CSEL texts of `fathers/critical/Latin/`, or in the doctors shelf, were excluded at fetch; a Migne witness beside an English held under an English-titled NPNF sigla (`augustine-holy-trinity`, `hilary-de-trinitate-or-trinity`) takes its own Latin-titled sigla, and the two are not merged. Isidore's Regula is held twice, from PL 83 and from the Codex regularum in PL 103, on separate sigla. Not converted, each with its evidence in the tool's SKIP table: Bede's Excerpta de S. Aldhelmo, Jerome's Vita Sancti Hilarii, Excerpta de aliquot Palaestinae locis and the PL 165 Prologus, Augustine's Additamentum and the Contra Faustum extract Quo genere cultus SS. Martyres; De Psalmorum auctore and Notitia were refused as containing no page of Migne. Every file is citable as Migne, never as a critical text.

The 5 `sales-*` rows marked *Mackey* entered on 2026-09-14 (#70 T4-4), written by `99. Tools/doctors/convert_grimm.py --series mackey` from the Internet Archive's OCR of Mackey's *Library of St. Francis de Sales* (vols. I, III–VI). Vol. II, the *Treatise on the Love of God*, is not taken: it is the translation already held as `sales-amour-de-dieu`. **Anchored at the printed numbering**: `sales-lettres-monde.BOOK.LETTER` and `sales-letters-religion.BOOK.N` (Book V's instructions are numbered the same way); `sales-controverses.PART.CHAPTER` for Part I and `.PART.ARTICLE.CHAPTER` for Parts II–III; `sales-entretiens.N`, with `.4.1` and `.4.2`; `sales-cantique.N`, with `.preface` and `.argument`. Mackey's pages are unanchored `[Mackey VOL, PAGE]` markers. V and VI are the series order: those title pages print no volume number. Every numeral repair and inserted heading is declared in the file's `repairs:`. Two rows keep Mackey's English title because the volume prints no French one.

The 2 `bernard-*-eales` rows and the English of `bernard-sermones-cantica-canticorum` entered on 2026-09-14 (#70 T4-5), written by `99. Tools/doctors/convert_grimm.py --series eales` from the Internet Archive's OCR of Eales's *Life and Works of Saint Bernard* (vols. I–II the Burns & Oates second edition, n.d.; III–IV Hodges, 1896). **`bernard-epistolae-eales.N` is Eales's own numbering, I–CDXC**: I–CCCLXXX follow Mabillon's order, and CCCLXXXI–CDXC are Eales's renumbering of the later letters. It is not Migne's (`bernard-epistolae-pl`), and the two are not merged. About 66 of these letters are the same translation as CCEL's *Some Letters* (`bernard-epistolae`, the 1904 selection's own numbering); both are current, and the file's `relations:` maps each unit to its Eales number. **`bernard-sermones-de-tempore-eales.N`** is Eales's continuous numbering I–XIX across several Latin works (Advent, the Vigil of the Nativity, *Missus est*), so it has its own anchor space. **The *Sermons on the Song of Songs* take the Latin's sigla**: Eales's I–LXXXVI are Migne's 1–86, checked by content on six sermons, anchored at the sermon (Migne's paragraph anchors are not claimed). Eales's pages are unanchored `[Eales VOL, PAGE]` markers. Declared in the files: vol. II pp. 820–821 (the head of Letter CCCVII) are absent from the scan's OCR; CDLVI–CDLVIII are charters; footnotes the page model could not split stay in the body, counted.

| sigla | author | work | languages | anchors |
|---|---|---|---|---|
| `albertus-adhaerendo` | Albert the Great (attributed) | De adhaerendo Deo | en | 16 |
| `alfonso-admonitions-all-states` | Alphonsus de Liguori | Admonitions addressed to Persons of All States who desire to be Saved (Grimm's English title; Italian not established) — Grimm, vol. I | en | 1 |
| `alfonso-advice-young-person` | Alphonsus de Liguori | Advice to a Young Person in Doubt about the State of Life which she Ought to Embrace (Grimm's English title; Italian not established) — Grimm, vol. III | en | 1 |
| `alfonso-answer-young-man` | Alphonsus de Liguori | Answer to a Young Man who Asks Counsel on the Choice of a State of Life (Grimm's English title; Italian not established) — Grimm, vol. III | en | 1 |
| `alfonso-apparecchio` | Alphonsus de Liguori | Apparecchio alla morte — Grimm, vol. I | en | 149 |
| `alfonso-apparecchio-passione` | Alphonsus de Liguori | The Respect, the Preparation, and Thanksgiving that Priests should practise in order to derive Fruit from the Celebration of Mass — Grimm, vol. XIII | en | 56 |
| `alfonso-aspirations-love` | Alphonsus de Liguori | Aspirations of Love to Jesus Christ (Grimm's English title; Italian not established) — Grimm, vol. IV | en | 13 |
| `alfonso-atti-apparecchio` | Alphonsus de Liguori | Considerations and Affections for Preparation for Mass and Thanksgiving; Various Prayers — Grimm, vol. XIII | en | 26 |
| `alfonso-avvisi-vocazione` | Alphonsus de Liguori | Avvisi spettanti alla vocazione religiosa — Grimm, vol. III | en | 14 |
| `alfonso-canzoncine` | Alphonsus de Liguori | Canzoncine spirituali — Grimm, vol. IX | en | 5 |
| `alfonso-cerimonie-messa` | Alphonsus de Liguori | The Ceremonies of the Mass (Grimm's English title; Italian not established) — Grimm, vol. XIII | en | 107 |
| `alfonso-considerations-passion` | Alphonsus de Liguori | Considerations on the Passion of Jesus Christ (Grimm's English title; Italian not established) — Grimm, vol. V | en | 60 |
| `alfonso-considerazioni-stato-religioso` | Alphonsus de Liguori | Considerazioni per coloro che sono chiamati allo stato religioso — Grimm, vol. III | en | 15 |
| `alfonso-corpus-christi-octave` | Alphonsus de Liguori | Meditations for the Octave of Corpus Christi (Grimm's English title; Italian not established) — Grimm, vol. VI | en | 8 |
| `alfonso-daily-acts` | Alphonsus de Liguori | Acts that the Christian should Perform Every Day (Grimm's English title; Italian not established) — Grimm, vol. IV | en | 1 |
| `alfonso-discorsi-calamita` | Alphonsus de Liguori | Nine Discourses for Times of Calamities (Grimm's English title; Italian not established) — Grimm, vol. XVII | en | 9 |
| `alfonso-discourse-mental-prayer-priests` | Alphonsus de Liguori | Discourse on the Necessity of Mental Prayer for Priests (Grimm's English title; Italian not established) — Grimm, vol. XII | en | 2 |
| `alfonso-discourse-pious-maidens` | Alphonsus de Liguori | Discourse to Pious Maidens (Grimm's English title; Italian not established) — Grimm, vol. III | en | 1 |
| `alfonso-divine-love-means` | Alphonsus de Liguori | Divine Love (Grimm's English title; Italian not established) — Grimm, vol. II | en | 9 |
| `alfonso-ejaculatory-solemnities` | Alphonsus de Liguori | Ejaculatory Prayers for the Twelve Greatest Solemnities in the Year (Grimm's English title; Italian not established) — Grimm, vol. IV | en | 14 |
| `alfonso-esercizi-missioni` | Alphonsus de Liguori | The Exercises of the Missions (Grimm's English title; Italian not established) — Grimm, vol. XV | en | 81 |
| `alfonso-esortazione-novizi` | Alphonsus de Liguori | Exhortation to Novices to Persevere in their Vocation (Grimm's English title; Italian not established) — Grimm, vol. XVII | en | 10 |
| `alfonso-esortazione-religiosi` | Alphonsus de Liguori | Exhortation to Religious to Advance in the Perfection of their State (Grimm's English title; Italian not established) — Grimm, vol. XVII | en | 1 |
| `alfonso-exercises-passion` | Alphonsus de Liguori | Various Exercises for the Use of Persons devoted to the Passion of our Lord (Grimm's English title; Italian not established) — Grimm, vol. V | en | 22 |
| `alfonso-exhortation-students` | Alphonsus de Liguori | Exhortation to Young Men who Devote Themselves to the Study of the Ecclesiastical Sciences (Grimm's English title; Italian not established) — Grimm, vol. XII | en | 1 |
| `alfonso-fedelta-sudditi` | Alphonsus de Liguori | Fidelity of Subjects to God renders them faithful to the Prince, their Ruler (Grimm's English title; Italian not established) — Grimm, vol. XVII | en | 9 |
| `alfonso-gran-mezzo` | Alphonsus de Liguori | Del gran mezzo della preghiera — Grimm, vol. III | en | 59 |
| `alfonso-hymn-mary-our-hope` | Alphonsus de Liguori | Mary our Hope — Grimm, vol. I | en | 1 |
| `alfonso-hymns-infancy` | Alphonsus de Liguori | Hymns (Grimm's English title; Italian not established) — Grimm, vol. IV | en | 5 |
| `alfonso-interior-trials` | Alphonsus de Liguori | Interior Trials (Grimm's English title; Italian not established) — Grimm, vol. II | en | 6 |
| `alfonso-istruzione-popolo` | Alphonsus de Liguori | Instructions for the People — Grimm, vol. XV | en | 148 |
| `alfonso-lettera-missioni` | Alphonsus de Liguori | Letter to a Bishop recently appointed on the Advantages of Missions — Grimm, vol. XV | en | 1 |
| `alfonso-lettera-predicare` | Alphonsus de Liguori | Letter to a Religious on the Manner of Preaching with Apostolic Simplicity — Grimm, vol. XV | en | 1 |
| `alfonso-lettere` | Alphonsus de Liguori | Lettere — Grimm, vols. XVIII, XIX, XX, XXI, XXII | en | 1464 |
| `alfonso-manner-mental-prayer` | Alphonsus de Liguori | Manner of Making Mental Prayer (Grimm's English title; Italian not established) — Grimm, vol. IV | en | 3 |
| `alfonso-massime-eterne` | Alphonsus de Liguori | Massime eterne — Grimm, vol. I | en | 27 |
| `alfonso-maxims-love` | Alphonsus de Liguori | Maxims for the Direction of a Soul that Desires to Attain Perfection in the Love of Jesus Christ (Grimm's English title; Italian not established) — Grimm, vol. IV | en | 1 |
| `alfonso-meditations-all-times` | Alphonsus de Liguori | Meditations Suitable for All Times of the Year (Grimm's English title; Italian not established) — Grimm, vol. II | en | 97 |
| `alfonso-meditations-passion` | Alphonsus de Liguori | Meditations on the Passion of Jesus Christ (Grimm's English title; Italian not established) — Grimm, vol. V | en | 37 |
| `alfonso-mental-prayer` | Alphonsus de Liguori | Mental Prayer (Grimm's English title; Italian not established) — Grimm, vol. III | en | 7 |
| `alfonso-messa-strapazzata` | Alphonsus de Liguori | La Messa e l'Officio strapazzati — Grimm, vol. XIII | en | 17 |
| `alfonso-metodo-missioni` | Alphonsus de Liguori | Method of Giving Missions (Grimm's English title; Italian not established) — Grimm, vol. XV | en | 3 |
| `alfonso-miracolo-ostie` | Alphonsus de Liguori | Account of a Striking Miracle: Hosts discovered in 1772 in a Field near Naples — Grimm, vol. XIII | en | 1 |
| `alfonso-modo-conversare` | Alphonsus de Liguori | Modo di conversare continuamente ed alla familiare con Dio — Grimm, vol. II | en | 13 |
| `alfonso-novena-holy-ghost` | Alphonsus de Liguori | Novena to the Holy Ghost (Grimm's English title; Italian not established) — Grimm, vol. VI | en | 12 |
| `alfonso-novena-holy-name` | Alphonsus de Liguori | Novena to the Holy Name of Jesus (Grimm's English title; Italian not established) — Grimm, vol. IV | en | 9 |
| `alfonso-novena-natale` | Alphonsus de Liguori | Novena del Santo Natale — Grimm, vol. IV | en | 76 |
| `alfonso-novena-sacred-heart` | Alphonsus de Liguori | Novena to the Sacred Heart of Jesus (Grimm's English title; Italian not established) — Grimm, vol. VI | en | 12 |
| `alfonso-onorario-messe` | Alphonsus de Liguori | The Honorarium of Masses — Grimm, vol. XIII | en | 12 |
| `alfonso-other-meditations-advent` | Alphonsus de Liguori | Other Meditations for Advent and the Novena of Christmas — Grimm, vol. IV | en | 22 |
| `alfonso-passion-kindles-love` | Alphonsus de Liguori | The Passion of Jesus Christ (Grimm's English title; Italian not established) — Grimm, vol. II | en | 9 |
| `alfonso-pious-sentiments` | Alphonsus de Liguori | Pious Sentiments of a Soul that Desires to Belong Entirely to Jesus Christ (Grimm's English title; Italian not established) — Grimm, vol. IV | en | 7 |
| `alfonso-poverta-religiosa` | Alphonsus de Liguori | Religious Poverty (Grimm's English title; Italian not established) — Grimm, vol. XVII | en | 1 |
| `alfonso-pratica` | Alphonsus de Liguori | Pratica di amar Gesù Cristo — Grimm, vol. VI | en | 45 |
| `alfonso-predicazione-confutata` | Alphonsus de Liguori | Refutation of a French Work entitled 'On Preaching' — Grimm, vol. XV | en | 2 |
| `alfonso-prediche-missione` | Alphonsus de Liguori | Table of Mission Sermons — Grimm, vol. XV | en | 5 |
| `alfonso-protestation-happy-death` | Alphonsus de Liguori | Protestation for a Happy Death (Grimm's English title; Italian not established) — Grimm, vol. I | en | 1 |
| `alfonso-purita-intenzione` | Alphonsus de Liguori | Purity of Intention (Grimm's English title; Italian not established) — Grimm, vol. XVII | en | 1 |
| `alfonso-reflections-passion` | Alphonsus de Liguori | Reflections and Affections on the Passion of Jesus Christ (Grimm's English title; Italian not established) — Grimm, vol. V | en | 123 |
| `alfonso-regola` | Alphonsus de Liguori | Rules and Constitutions of the Congregation of the Most Holy Redeemer (Grimm's English title; Italian not established) — Grimm, vol. XVII | en | 25 |
| `alfonso-regolamento-seminari` | Alphonsus de Liguori | Rules for Seminaries (Grimm's English title; Italian not established) — Grimm, vol. XVII | en | 5 |
| `alfonso-regolamento-vita` | Alphonsus de Liguori | Regolamento di vita di un cristiano — Grimm, vol. I | en | 25 |
| `alfonso-retreat-exercises` | Alphonsus de Liguori | The Exercises of a Retreat (Grimm's English title; Italian not established) — Grimm, vol. III | en | 50 |
| `alfonso-riflessioni-divote` | Alphonsus de Liguori | Riflessioni divote sopra diversi punti di spirito — Grimm, vol. II | en | 45 |
| `alfonso-riflessioni-vescovi` | Alphonsus de Liguori | Riflessioni utili a' vescovi per la pratica di ben governare le loro chiese — Grimm, vol. XVII | en | 17 |
| `alfonso-rule-of-life-abridged` | Alphonsus de Liguori | Rule of Life (Abridged) (Grimm's English title; Italian not established) — Grimm, vol. II | en | 13 |
| `alfonso-sacrifice-jesus` | Alphonsus de Liguori | The Sacrifice of Jesus Christ (Grimm's English title; Italian not established) — Grimm, vol. VI | en | 60 |
| `alfonso-saette-fuoco` | Alphonsus de Liguori | Saette di fuoco — Grimm, vol. IV | en | 38 |
| `alfonso-salmi` | Alphonsus de Liguori | Traduzione de' Salmi e de' Cantici che si contengono nell'Officio divino — Grimm, vol. XIV | en | 169 |
| `alfonso-selva` | Alphonsus de Liguori | Selva di materie predicabili ed istruttive, per dare gli esercizj ai Preti, ed anche per uso di lezione privata a proprio profitto — Grimm, vol. XII | en | 153 |
| `alfonso-sermone-passione` | Alphonsus de Liguori | Sermon on the Passion of Jesus Christ (Grimm's English title; Italian not established) — Grimm, vol. XVII | en | 3 |
| `alfonso-sermone-rosario` | Alphonsus de Liguori | Sermon on the Rosary — Grimm, vol. XVII | en | 2 |
| `alfonso-sermoni` | Alphonsus de Liguori | Sermoni compendiati per tutte le domeniche dell'anno — Grimm, vol. XVI | en | 53 |
| `alfonso-short-treatise-prayer` | Alphonsus de Liguori | A Short Treatise on Prayer (Grimm's English title; Italian not established) — Grimm, vol. II | en | 11 |
| `alfonso-sighs-love` | Alphonsus de Liguori | Sighs of Love towards God (Grimm's English title; Italian not established) — Grimm, vol. IV | en | 21 |
| `alfonso-simple-exposition` | Alphonsus de Liguori | Simple Exposition of the Circumstances of the Passion of Jesus Christ (Grimm's English title; Italian not established) — Grimm, vol. V | en | 74 |
| `alfonso-sure-signs-love` | Alphonsus de Liguori | Sure Signs by which we may know whether we have the Divine Love in us (Grimm's English title; Italian not established) — Grimm, vol. II | en | 1 |
| `alfonso-testi-calamita` | Alphonsus de Liguori | Texts from Holy Scripture and from the Holy Fathers referring to some Particular Calamities (Grimm's English title; Italian not established) — Grimm, vol. XVII | en | 7 |
| `alfonso-uniformita` | Alphonsus de Liguori | Uniformità alla volontà di Dio | en, it | 8 |
| `alfonso-uniformita-grimm` | Alphonsus de Liguori | Uniformità alla volontà di Dio — Grimm, vol. II; witness of `alfonso-uniformita` | en | 14 |
| `alfonso-vera-sposa` | Alphonsus de Liguori | La vera sposa di Gesù Cristo — Grimm, vols. X, XI | en | 98 |
| `alfonso-visita-comune` | Alphonsus de Liguori | Pious Acts to be made in the Common Visit to the Blessed Sacrament and to the Blessed Virgin (Grimm's English title; Italian not established) — Grimm, vol. XV | en | 2 |
| `alfonso-visite` | Alphonsus de Liguori | Visite al SS. Sacramento e a Maria Santissima — Grimm, vol. VI | en | 41 |
| `alfonso-vita-cafaro` | Alphonsus de Liguori | Notes on the Life of the Rev. Father Paul Cafaro — Grimm, vol. XVII | en | 15 |
| `alfonso-vita-curzio` | Alphonsus de Liguori | Notes on the Life of Vitus Curzius — Grimm, vol. XVII | en | 6 |
| `alfonso-vita-sarnelli` | Alphonsus de Liguori | Notes on the Life of Father Januarius Maria Sarnelli — Grimm, vol. XVII | en | 13 |
| `alfonso-vittorie` | Alphonsus de Liguori | Vittorie de' martiri — Grimm, vol. IX | en | 116 |
| `alfonso-vocation-priesthood` | Alphonsus de Liguori | The Vocation to the Priesthood (Grimm's English title; Italian not established) — Grimm, vol. III | en | 6 |
| `alfonso-way-bethlehem` | Alphonsus de Liguori | The Way of Bethlehem — Grimm, vol. IV | en | 13 |
| `ambrose-anacephalaeosis-historiae-de-excidio` | Ambrose of Milan | Anacephalaeosis Historiae de excidio Hierosolymitanae urbis | la | 23 |
| `ambrose-apologia-altera-prophetae-david` | Ambrose of Milan | Apologia altera prophetae David | la | 87 |
| `ambrose-apologia-prophetae-david` | Ambrose of Milan | Apologia Prophetae David | la | 102 |
| `ambrose-de-abraham` | Ambrose of Milan | De Abraham | la | 209 |
| `ambrose-de-benedictionibus-patriarcharum` | Ambrose of Milan | De benedictionibus patriarcharum | la | 71 |
| `ambrose-de-bono-mortis` | Ambrose of Milan | De bono mortis | la | 69 |
| `ambrose-de-cain-et-abel` | Ambrose of Milan | De Cain et Abel | la | 107 |
| `ambrose-de-elia-et-jejunio` | Ambrose of Milan | De Elia et jejunio | la | 106 |
| `ambrose-de-excessu-fratris-sui-satyrus` | Ambrose of Milan | De excessu fratris sui Satyrus | la | 219 |
| `ambrose-de-excidio-urbis-hierosolymitanae` | Ambrose of Milan | De excidio urbis Hierosolymitanae | la | 181 |
| `ambrose-de-fide` | Ambrose of Milan | De fide | la | 918 |
| `ambrose-de-fuga-saeculi` | Ambrose of Milan | De fuga saeculi | la | 67 |
| `ambrose-de-incarnationis-dominicae-sacramento` | Ambrose of Milan | De incarnationis Dominicae sacramento | la | 124 |
| `ambrose-de-institutione-virginis` | Ambrose of Milan | De institutione virginis | la | 131 |
| `ambrose-de-interpellatione-job-et-david` | Ambrose of Milan | De interpellatione Job et David | la | 160 |
| `ambrose-de-isaac-et-anima` | Ambrose of Milan | De Isaac et Anima | la | 87 |
| `ambrose-de-jacob-et-vita-beata` | Ambrose of Milan | De Jacob et vita beata | la | 118 |
| `ambrose-de-joseph-patriarcha` | Ambrose of Milan | De Joseph Patriarcha | la | 99 |
| `ambrose-de-lapsu-virginis-consecratae` | Ambrose of Milan | De lapsu virginis consecratae | la | 62 |
| `ambrose-de-mysteriis` | Ambrose of Milan | De mysteriis | la | 1 |
| `ambrose-de-nabuthe-jezraelita` | Ambrose of Milan | De Nabuthe Jezraelita | la | 90 |
| `ambrose-de-noe-et-arca` | Ambrose of Milan | De Noe et Arca | la | 162 |
| `ambrose-de-obitu-theodosii-oratio` | Ambrose of Milan | De obitu Theodosii oratio | la | 57 |
| `ambrose-de-obitu-valentiniani-consolatio` | Ambrose of Milan | De obitu Valentiniani consolatio | la | 82 |
| `ambrose-de-officiis-ministrorum` | Ambrose of Milan | De officiis ministrorum | la | 658 |
| `ambrose-de-paradiso` | Ambrose of Milan | De paradiso | la | 92 |
| `ambrose-de-poenitentia` | Ambrose of Milan | De poenitentia | la | 232 |
| `ambrose-de-sacramentis` | Ambrose of Milan | De sacramentis | la | 181 |
| `ambrose-de-spiritu-sancto` | Ambrose of Milan | De Spiritu Sancto | la | 539 |
| `ambrose-de-tobia` | Ambrose of Milan | De Tobia | la | 117 |
| `ambrose-de-viduis` | Ambrose of Milan | De viduis | la | 105 |
| `ambrose-de-virginibus` | Ambrose of Milan | De virginibus | la | 175 |
| `ambrose-de-virginitate` | Ambrose of Milan | De virginitate | la | 155 |
| `ambrose-enarrationes-in-xii-psalmos-davidicos` | Ambrose of Milan | Enarrationes in XII psalmos Davidicos | la | 560 |
| `ambrose-epistolae-pl` | Ambrose of Milan | Epistolae (classis I-II) | la | 1476 |
| `ambrose-epistulae` | Ambrose of Milan | Epistulae (selection) | la | 1 |
| `ambrose-exhortatio-virginitatis` | Ambrose of Milan | Exhortatio virginitatis | la | 107 |
| `ambrose-fragmentum` | Ambrose of Milan | Fragmentum | la | 1 |
| `ambrose-fragmentum-ex-theodoreto-desumptum` | Ambrose of Milan | Fragmentum ex Theodoreto desumptum | la | 2 |
| `ambrose-hymni` | Ambrose of Milan | Hymni | la | 1 |
| `ambrose-sermones` | Ambrose of Milan | Sermones | la | 23 |
| `anselm-admonitio-morienti` | Anselm of Canterbury | Admonitio morienti | la | 1 |
| `anselm-aliud-carmen-contemptu` | Anselm of Canterbury | Aliud carmen de contemptu mundi | la | 1 |
| `anselm-apologeticus` | Anselm of Canterbury | Liber apologeticus contra Gaunilonem | la | 11 |
| `anselm-azymo-et-fermentato` | Anselm of Canterbury | De azymo et fermentato | la | 8 |
| `anselm-carmen-contemptu-mundi` | Anselm of Canterbury | Carmen de contemptu mundi | la | 1 |
| `anselm-conceptu-virginali` | Anselm of Canterbury | De conceptu virginali et originali peccato | la | 30 |
| `anselm-concordia-praescientiae` | Anselm of Canterbury | De concordia praescientiae et praedestinationis | la | 28 |
| `anselm-cur-deus-homo` | Anselm of Canterbury | Cur Deus homo | en | 51 |
| `anselm-cur-deus-homo-pl` | Anselm of Canterbury | Cur Deus homo | la | 51 |
| `anselm-dialogus-casu-diaboli` | Anselm of Canterbury | Dialogus de casu Diaboli | la | 28 |
| `anselm-dialogus-grammatico` | Anselm of Canterbury | Dialogus de grammatico | la | 21 |
| `anselm-dialogus-libero-arbitrio` | Anselm of Canterbury | Dialogus de libero arbitrio | la | 14 |
| `anselm-dialogus-veritate` | Anselm of Canterbury | Dialogus de veritate | la | 14 |
| `anselm-epistola-ad-wilhelmum` | Anselm of Canterbury | Epistola ad Wilhelmum Hirausgiensem | la | 1 |
| `anselm-epistolae` | Anselm of Canterbury | Epistolae | la | 132 |
| `anselm-exhortatio-ad-contemptum` | Anselm of Canterbury | Exhortatio ad contemptum temporalium et desiderium aeternorum | la | 1 |
| `anselm-fide-trinitatis` | Anselm of Canterbury | De fide trinitatis | la | 10 |
| `anselm-homiliae-et-exhortationes` | Anselm of Canterbury | Homiliae et exhortationes | la | 16 |
| `anselm-hymni-et-psalterium` | Anselm of Canterbury | Hymni et psalterium de S. Maria | la | 15 |
| `anselm-meditatio-super-miserere` | Anselm of Canterbury | Meditatio super Miserere | la | 44 |
| `anselm-meditationes-et-orationes` | Anselm of Canterbury | Meditationes et orationes | la | 54 |
| `anselm-monologion` | Anselm of Canterbury | Monologion | en, la | 81 |
| `anselm-nuptiis-consanguineorum` | Anselm of Canterbury | De nuptiis consanguineorum | la | 7 |
| `anselm-offendiculum-sacerdotum` | Anselm of Canterbury | Offendiculum sacerdotum | la | 1 |
| `anselm-oratio-ante-perceptionem` | Anselm of Canterbury | Oratio | la | 1 |
| `anselm-orationes` | Anselm of Canterbury | Orationes sive meditationes (The Devotions) | en | 60 |
| `anselm-orationes-pl` | Anselm of Canterbury | Orationes | la | 77 |
| `anselm-pace-et-concordia` | Anselm of Canterbury | De pace et concordia | la | 3 |
| `anselm-pro-insipiente` | Anselm of Canterbury | Pro insipiente (Gaunilo) et Responsio | en | 12 |
| `anselm-processione-spiritus-sancti` | Anselm of Canterbury | De processione Spiritus sancti contra Graecos | la | 31 |
| `anselm-proslogion` | Anselm of Canterbury | Proslogion | en, la | 27 |
| `anselm-quaedam-dicta-utilia` | Anselm of Canterbury | Quaedam dicta utilia | la | 3 |
| `anselm-responsio-waleranni` | Anselm of Canterbury | Responsio | la | 4 |
| `anselm-salutatio-ad-jesum` | Anselm of Canterbury | Salutatio ad Jesum Christum | la | 1 |
| `anselm-sermo-passione-domini` | Anselm of Canterbury | Sermo de passione Domini | la | 1 |
| `anselm-tractatus-asceticus` | Anselm of Canterbury | Tractatus asceticus | la | 5 |
| `anselm-versus-lanfranco` | Anselm of Canterbury | Versus de Lanfranco | la | 1 |
| `anselm-voluntate` | Anselm of Canterbury | De voluntate | la | 1 |
| `anselm-voluntate-dei` | Anselm of Canterbury | De voluntate Dei | la | 5 |
| `augustine-adversus-judaeos` | Augustine of Hippo | Adversus Judaeos | la | 25 |
| `augustine-annotationes-in-job` | Augustine of Hippo | Annotationes in Job | la | 1 |
| `augustine-breviculus-collationis-cum-donatistis` | Augustine of Hippo | Breviculus collationis cum Donatistis | la | 22 |
| `augustine-collatio-cum-maximino-episcopo-arianorum` | Augustine of Hippo | Collatio cum Maximino episcopo Arianorum | la | 41 |
| `augustine-contra-academicos` | Augustine of Hippo | Contra Academicos | la | 147 |
| `augustine-contra-adimantum` | Augustine of Hippo | Contra Adimantum | la | 77 |
| `augustine-contra-adversarium-legis-et-prophetarum` | Augustine of Hippo | Contra adversarium legis et prophetarum | la | 133 |
| `augustine-contra-cresconium-grammaticum-donatistam` | Augustine of Hippo | Contra Cresconium grammaticum Donatistam | la | 58 |
| `augustine-contra-duas-epistolas-pelagianorum` | Augustine of Hippo | Contra duas epistolas Pelagianorum | la | 183 |
| `augustine-contra-epistolam-manichaei` | Augustine of Hippo | Contra epistolam Manichaei | la | 93 |
| `augustine-contra-epistolam-parmeniani` | Augustine of Hippo | Contra epistolam Parmeniani | la | 53 |
| `augustine-contra-faustum-manichaeum` | Augustine of Hippo | Contra Faustum Manichaeum | la | 465 |
| `augustine-contra-fortunatum-manichaeum` | Augustine of Hippo | Contra Fortunatum Manichaeum | la | 40 |
| `augustine-contra-gaudentium` | Augustine of Hippo | Contra Gaudentium | la | 19 |
| `augustine-contra-julianum` | Augustine of Hippo | Contra Julianum | la | 490 |
| `augustine-contra-litteras-petiliani` | Augustine of Hippo | Contra Litteras Petiliani | la | 160 |
| `augustine-contra-maximinum-episcopum-arianorum` | Augustine of Hippo | Contra Maximinum episcopum Arianorum | la | 118 |
| `augustine-contra-mendacium` | Augustine of Hippo | Contra mendacium | la | 63 |
| `augustine-contra-priscillianistas-et-origenistas` | Augustine of Hippo | Contra Priscillianistas et Origenistas | la | 25 |
| `augustine-contra-secundinum-manichaeum` | Augustine of Hippo | Contra Secundinum Manichaeum | la | 27 |
| `augustine-contra-sermonem-arianorum` | Augustine of Hippo | Contra Sermonem Arianorum | la | 73 |
| `augustine-de-actis-cum-felice-manichaeo` | Augustine of Hippo | De actis cum Felice Manichaeo | la | 45 |
| `augustine-de-altercatione-ecclesiae-et-synagogae` | Augustine of Hippo | De altercatione Ecclesiae et Synagogae | la | 1 |
| `augustine-de-anima-et-ejus-origine` | Augustine of Hippo | De anima et ejus origine | la | 200 |
| `augustine-de-baptismo-contra-donatistas` | Augustine of Hippo | De baptismo contra Donatistas | la | 144 |
| `augustine-de-beata-vita` | Augustine of Hippo | De beata vita | la | 42 |
| `augustine-de-cantico-novo` | Augustine of Hippo | De cantico novo | la | 20 |
| `augustine-de-catechizandis-rudibus` | Augustine of Hippo | De catechizandis rudibus | la | 83 |
| `augustine-de-conjugiis-adulterinis` | Augustine of Hippo | De conjugiis adulterinis | la | 107 |
| `augustine-de-correptione-et-gratia-pl` | Augustine of Hippo | De correptione et gratia | la | 66 |
| `augustine-de-disciplina-christiana` | Augustine of Hippo | De disciplina Christiana | la | 30 |
| `augustine-de-diversis-quaestionibus` | Augustine of Hippo | De diversis quaestionibus | la | 188 |
| `augustine-de-diversis-quaestionibus-ad-simplicianum` | Augustine of Hippo | De diversis quaestionibus ad Simplicianum | la | 69 |
| `augustine-de-divinatione-daemonum` | Augustine of Hippo | De divinatione daemonum | la | 25 |
| `augustine-de-doctrina-christiana-pl` | Augustine of Hippo | De doctrina Christiana | la | 389 |
| `augustine-de-dono-perseverantiae` | Augustine of Hippo | De dono perseverantiae | la | 94 |
| `augustine-de-duabus-animabus` | Augustine of Hippo | De duabus animabus | la | 40 |
| `augustine-de-excidio-urbis` | Augustine of Hippo | De excidio urbis | la | 17 |
| `augustine-de-fide-et-symbolo` | Augustine of Hippo | De fide et symbolo | la | 36 |
| `augustine-de-fide-rerum-quae-non` | Augustine of Hippo | De fide rerum quae non videntur | la | 20 |
| `augustine-de-fide-spe-et-charitate` | Augustine of Hippo | De fide spe et charitate | la | 155 |
| `augustine-de-genesi-contra-manichaeos` | Augustine of Hippo | De Genesi contra Manichaeos | la | 142 |
| `augustine-de-gestis-cum-emerito` | Augustine of Hippo | De gestis cum Emerito | la | 12 |
| `augustine-de-gestis-pelagii-pl` | Augustine of Hippo | De gestis Pelagii | la | 101 |
| `augustine-de-gratia-christi` | Augustine of Hippo | De gratia Christi et de peccato originali | la | 196 |
| `augustine-de-gratia-et-libero-arbitrio` | Augustine of Hippo | De gratia et libero arbitrio | la | 71 |
| `augustine-de-haeresibus` | Augustine of Hippo | De haeresibus | la | 89 |
| `augustine-de-immortalitate-animae` | Augustine of Hippo | De immortalitate animae | la | 42 |
| `augustine-de-libero-arbitrio` | Augustine of Hippo | De libero arbitrio | la | 231 |
| `augustine-de-magistro` | Augustine of Hippo | De magistro | la | 62 |
| `augustine-de-moribus-ecclesiae` | Augustine of Hippo | De moribus Ecclesiae | la | 213 |
| `augustine-de-musica` | Augustine of Hippo | De musica | la | 289 |
| `augustine-de-natura-boni` | Augustine of Hippo | De natura boni | la | 48 |
| `augustine-de-nuptiis-et-concupiscentia-pl` | Augustine of Hippo | De nuptiis et concupiscentia | la | 173 |
| `augustine-de-oratione` | Augustine of Hippo | De oratione | la | 1 |
| `augustine-de-ordine` | Augustine of Hippo | De ordine | la | 122 |
| `augustine-de-peccatorum-meritis-et-remissione-pl` | Augustine of Hippo | De peccatorum meritis et remissione | la | 243 |
| `augustine-de-perfectione-justitiae-hominis` | Augustine of Hippo | De perfectione justitiae hominis | la | 50 |
| `augustine-de-praedestinatione-sanctorum` | Augustine of Hippo | De praedestinatione sanctorum | la | 65 |
| `augustine-de-quaestionibus-dulcitii` | Augustine of Hippo | De quaestionibus Dulcitii | la | 52 |
| `augustine-de-quantitate-animae` | Augustine of Hippo | De quantitate animae | la | 119 |
| `augustine-de-quatuor-virtutibus-charitatis` | Augustine of Hippo | De quatuor virtutibus charitatis | la | 1 |
| `augustine-de-sermone-domini-in-monte-pl` | Augustine of Hippo | De sermone Domini in monte | la | 121 |
| `augustine-de-trinitate` | Augustine of Hippo | De Trinitate | la | 601 |
| `augustine-de-unico-baptismo-contra-petilianum` | Augustine of Hippo | De unico baptismo contra Petilianum | la | 16 |
| `augustine-de-utilitate-credendi` | Augustine of Hippo | De utilitate credendi | la | 55 |
| `augustine-de-utilitate-jejunii` | Augustine of Hippo | De utilitate jejunii | la | 24 |
| `augustine-de-vera-religione` | Augustine of Hippo | De vera religione | la | 169 |
| `augustine-enarrationes-in-psalmos-pl` | Augustine of Hippo | Enarrationes in Psalmos (PL 36-37) | la | 3498 |
| `augustine-epistola-ad-catholicos` | Augustine of Hippo | Epistola ad Catholicos sive De unitate ecclesiae | la | 53 |
| `augustine-excerptum-de-manichaeis` | Augustine of Hippo | Excerptum de Manichaeis | la | 10 |
| `augustine-expositio-epistolae-ad-galatas` | Augustine of Hippo | Expositio Epistolae ad Galatas | la | 64 |
| `augustine-expositio-inchoata-epistolae-ad-romanos` | Augustine of Hippo | Expositio inchoata Epistolae ad Romanos | la | 24 |
| `augustine-expositio-propositionum-ex-epistola` | Augustine of Hippo | Expositio propositionum ex Epistola ad Romanos | la | 75 |
| `augustine-fragmenta-sermonum` | Augustine of Hippo | Fragmenta sermonum | la | 32 |
| `augustine-homilia-in-dominica-ii-adventus` | Augustine of Hippo | Homilia in Dominica II Adventus | la | 1 |
| `augustine-in-epistolam-joannis-ad-parthos` | Augustine of Hippo | In Epistolam Joannis ad Parthos tractatus X | la | 136 |
| `augustine-in-joannis-evangelium-tractatus-cxxiv` | Augustine of Hippo | In Joannis evangelium tractatus CXXIV | la | 1246 |
| `augustine-liber-imperfectus-de-genesi` | Augustine of Hippo | Liber imperfectus de Genesi ad litteram | la | 79 |
| `augustine-liber-sententiarum` | Augustine of Hippo | Liber sententiarum | la | 21 |
| `augustine-locutiones-in-heptateuchum` | Augustine of Hippo | Locutiones in Heptateuchum | la | 7 |
| `augustine-opus-imperfectum-contra-secundam` | Augustine of Hippo | Opus imperfectum contra secundam responsionem Juliani | la | 841 |
| `augustine-post-collationem-ad-donatistas` | Augustine of Hippo | Post collationem ad Donatistas | la | 26 |
| `augustine-principia-dialecticae` | Augustine of Hippo | Principia dialecticae | la | 10 |
| `augustine-psalmus-contra-partem-donati` | Augustine of Hippo | Psalmus contra partem Donati | la | 1 |
| `augustine-quaestiones-evangeliorum` | Augustine of Hippo | Quaestiones Evangeliorum | la | 104 |
| `augustine-quaestiones-in-heptateuchum` | Augustine of Hippo | Quaestiones in Heptateuchum | la | 677 |
| `augustine-quaestiones-xvii-in-matthaeum` | Augustine of Hippo | Quaestiones XVII in Matthaeum | la | 35 |
| `augustine-regula` | Augustine of Hippo | Regula | la | 25 |
| `augustine-sermo-ad-plebem-ecclesiae-caesareensis` | Augustine of Hippo | Sermo ad plebem ecclesiae Caesareensis | la | 9 |
| `augustine-sermo-i-de-symbolo` | Augustine of Hippo | Sermo I de symbolo | la | 26 |
| `augustine-sermo-ii-de-symbolo` | Augustine of Hippo | Sermo II de symbolo | la | 37 |
| `augustine-sermo-iii-de-symbolo` | Augustine of Hippo | Sermo III de symbolo | la | 25 |
| `augustine-sermo-in-circumcisione-domini` | Augustine of Hippo | Sermo in circumcisione Domini | la | 1 |
| `augustine-sermo-iv-de-symbolo` | Augustine of Hippo | Sermo IV de symbolo | la | 26 |
| `augustine-sermones-1` | Augustine of Hippo | Sermones 1 | la | 38 |
| `augustine-sermones-2` | Augustine of Hippo | Sermones 2 | la | 5 |
| `augustine-sermones-inediti` | Augustine of Hippo | Sermones inediti | la | 184 |
| `augustine-sermones-pl` | Augustine of Hippo | Sermones ad populum (classes I-IV) | la | 4990 |
| `augustine-soliloquia-pl` | Augustine of Hippo | Soliloquia | la | 104 |
| `augustine-speculum-de-scriptura-sacra` | Augustine of Hippo | Speculum de Scriptura sacra | la | 52 |
| `avila-audi-filia` | Juan de Ávila | Audi, filia (Libro espiritual) | es | 112 |
| `beda-allegorica-expositio-in-cantica-canticorum` | Bede the Venerable | Allegorica expositio in Cantica canticorum | la | 58 |
| `beda-allegorica-expositio-in-canticum-habacuc` | Bede the Venerable | Allegorica expositio in Canticum Habacuc | la | 1 |
| `beda-allegorica-expositio-in-esdram` | Bede the Venerable | Allegorica expositio in Esdram et Nehemiam | la | 41 |
| `beda-allegorica-expositio-in-parabolas-salomonis` | Bede the Venerable | Allegorica expositio in Parabolas Salomonis | la | 34 |
| `beda-allegorica-expositio-in-samuelem` | Bede the Venerable | Allegorica expositio in Samuelem | la | 51 |
| `beda-allegorica-interpretatio-in-tobiam` | Bede the Venerable | Allegorica interpretatio in Tobiam | la | 1 |
| `beda-commentarii-in-pentateuchum` | Bede the Venerable | Commentarii in Pentateuchum | la | 138 |
| `beda-de-arte-metrica` | Bede the Venerable | De arte metrica | la | 25 |
| `beda-de-celebratione-paschae` | Bede the Venerable | De celebratione Paschae | la | 1 |
| `beda-de-die-judicii` | Bede the Venerable | De die judicii | la | 1 |
| `beda-de-muliere-forti` | Bede the Venerable | De muliere forti | la | 22 |
| `beda-de-natura-rerum` | Bede the Venerable | De natura rerum | la | 52 |
| `beda-de-nominibus-locorum` | Bede the Venerable | De nominibus locorum | la | 17 |
| `beda-de-ordinatione-feriarum-paschalium` | Bede the Venerable | De ordinatione feriarum Paschalium | la | 1 |
| `beda-de-orthographia` | Bede the Venerable | De orthographia | la | 1 |
| `beda-de-ratione-computi` | Bede the Venerable | De ratione computi | la | 18 |
| `beda-de-ratione-temporum` | Bede the Venerable | De ratione temporum | la | 72 |
| `beda-de-schematibus-et-tropis-sacrae` | Bede the Venerable | De schematibus et tropis sacrae Scripturae | la | 15 |
| `beda-de-tabernaculo-et-vestibus-sacerdotum` | Bede the Venerable | De tabernaculo et vestibus sacerdotum | la | 39 |
| `beda-de-templo-salomonis` | Bede the Venerable | De templo Salomonis | la | 26 |
| `beda-de-temporibus` | Bede the Venerable | De temporibus | la | 23 |
| `beda-de-tonitruis` | Bede the Venerable | De tonitruis | la | 4 |
| `beda-epistolae` | Bede the Venerable | Epistolae | la | 17 |
| `beda-explanatio-apocalypsis` | Bede the Venerable | Explanatio Apocalypsis | la | 27 |
| `beda-expositio-super-acta-apostolorum` | Bede the Venerable | Expositio super Acta Apostolorum | la | 29 |
| `beda-fragmenta-in-proverbia-salomonis` | Bede the Venerable | Fragmenta in Proverbia Salomonis | la | 11 |
| `beda-fragmentum-de-divisione-horae` | Bede the Venerable | Fragmentum de divisione horae | la | 1 |
| `beda-hexaemeron` | Bede the Venerable | Hexaemeron | la | 5 |
| `beda-historia` | Bede the Venerable | Historia ecclesiastica gentis Anglorum | en, la | 148 |
| `beda-homiliae` | Bede the Venerable | Homiliae | la | 161 |
| `beda-hymni-xiii` | Bede the Venerable | Hymni XIII | la | 13 |
| `beda-in-evangelium-s-joannis` | Bede the Venerable | In Evangelium S. Joannis | la | 37 |
| `beda-in-evangelium-s-lucae` | Bede the Venerable | In Evangelium S. Lucae | la | 35 |
| `beda-in-evangelium-s-marci` | Bede the Venerable | In Evangelium S. Marci | la | 22 |
| `beda-in-evangelium-s-matthaei` | Bede the Venerable | In Evangelium S. Matthaei | la | 32 |
| `beda-interpretatio-artis-cantilenae-psalterii` | Bede the Venerable | Interpretatio artis cantilenae psalterii | la | 1 |
| `beda-kalendarium-anglicanum` | Bede the Venerable | Kalendarium Anglicanum | la | 14 |
| `beda-libellus-precum` | Bede the Venerable | Libellus precum | la | 8 |
| `beda-martyrologium` | Bede the Venerable | Martyrologium | la | 740 |
| `beda-martyrologium-poeticum` | Bede the Venerable | Martyrologium poeticum | la | 13 |
| `beda-passio-justini-martyris` | Bede the Venerable | Passio Justini martyris | la | 1 |
| `beda-praefatio-de-cyclo-paschali` | Bede the Venerable | Praefatio de cyclo Paschali | la | 2 |
| `beda-quaestiones-in-acta-apostolorum` | Bede the Venerable | Quaestiones in Acta Apostolorum | la | 5 |
| `beda-quaestiones-in-libros-regum` | Bede the Venerable | Quaestiones in libros Regum | la | 32 |
| `beda-retractatio-in-acta-apostolorum` | Bede the Venerable | Retractatio in Acta Apostolorum | la | 29 |
| `beda-super-epistolas-catholicas` | Bede the Venerable | Super epistolas Catholicas | la | 26 |
| `beda-vita-felicis-confessoris` | Bede the Venerable | Vita Felicis confessoris | la | 1 |
| `beda-vita-metrica-s-cuthberti` | Bede the Venerable | Vita metrica S. Cuthberti | la | 49 |
| `beda-vita-prosaica-s-cuthberti` | Bede the Venerable | Vita prosaica S. Cuthberti | la | 47 |
| `beda-vita-v-sanctorum-abbatum` | Bede the Venerable | Vita V sanctorum abbatum | la | 2 |
| `bellarmine-aeterna-felicitate` | Robert Bellarmine | De aeterna felicitate sanctorum (Vivès, *Opera omnia* VIII, 1873; archive.org OCR, two columns) | la | 63 |
| `bellarmine-arte-bene-moriendi` | Robert Bellarmine | De arte bene moriendi — Dalton, *The Art of Dying Well* (London: Richardson and Son, n.d. [1847]; archive.org OCR); Preface and chapters I–XVI, no book number printed | en | 17 |
| `bellarmine-ascensione-mentis` | Robert Bellarmine | De ascensione mentis in Deum per scalas rerum creatarum (Vivès VIII) | la | 16 |
| `bellarmine-cognitione-dei` | Robert Bellarmine | Tractatus de cognitione Dei (Vivès VIII) | la | 13 |
| `bellarmine-gemitu-columbae` | Robert Bellarmine | De gemitu columbae, sive de bono lacrymarum (Vivès VIII; pp. 458–459 absent from the scan) | la | 39 |
| `bellarmine-officio-principis` | Robert Bellarmine | De officio principis christiani — Liber I by chapter, the lives of Libri II–III by slug from the printed name (Vivès VIII) | la | 45 |
| `bellarmine-risposta-gersone` | Robert Bellarmine | Risposta ad un libretto intitolato Trattato e risoluzione … di Gio. Gersone (Vivès VIII) — `.1`–`.6`, `.considerazione.1`–`.12`, `.risposta`, two numberings kept apart | it | 20 |
| `bellarmine-risposta-lettera-senza-nome` | Robert Bellarmine | Risposta ad una lettera senza nome di autore (Vivès VIII) | it | 8 |
| `bellarmine-risposta-marsilio` | Robert Bellarmine | Risposta alla difesa delle otto proposizioni di Giovanni Marsilio (Vivès VIII) | it | 3 |
| `bellarmine-risposta-sette-teologi` | Robert Bellarmine | Risposta al trattato dei sette teologi di Venezia (Vivès VIII) | it | 19 |
| `bellarmine-septem-verbis` | Robert Bellarmine | De septem verbis a Christo in cruce prolatis (Vivès VIII) | la | 39 |
| `bernard-adventu-domini` | Bernard of Clairvaux | De adventu Domini | la | 48 |
| `bernard-annuntiatione-bvm` | Bernard of Clairvaux | In annuntiatione B. V. Mariae | la | 32 |
| `bernard-apologia-ad-guillelmum` | Bernard of Clairvaux | Apologia ad Guillelmum | la | 54 |
| `bernard-ascensione-domini` | Bernard of Clairvaux | In ascensione Domini | la | 52 |
| `bernard-assumptione-bvm` | Bernard of Clairvaux | In assumptione B. V. Mariae | la | 33 |
| `bernard-baptismo` | Bernard of Clairvaux | De baptismo | la | 32 |
| `bernard-cantu` | Bernard of Clairvaux | De cantu | la | 16 |
| `bernard-capite-jejunii` | Bernard of Clairvaux | In capite jejunii | la | 14 |
| `bernard-chartae` | Bernard of Clairvaux | Chartae | la | 15 |
| `bernard-circumcisione-domini` | Bernard of Clairvaux | In circumcisione Domini | la | 24 |
| `bernard-coena-domini` | Bernard of Clairvaux | In Coena Domini | la | 6 |
| `bernard-consideratione` | Bernard of Clairvaux | De consideratione | la | 167 |
| `bernard-contra-quaedam-capitula` | Bernard of Clairvaux | Contra quaedam Capitula errorum Abaelardi | la | 36 |
| `bernard-conversione` | Bernard of Clairvaux | De conversione | la | 62 |
| `bernard-conversione-s-pauli` | Bernard of Clairvaux | In conversione S. Pauli | la | 12 |
| `bernard-corpore-domini` | Bernard of Clairvaux | De corpore Domini | la | 2 |
| `bernard-dedicatione-ecclesiae` | Bernard of Clairvaux | In dedicatione ecclesiae | la | 39 |
| `bernard-die-sancto-paschae` | Bernard of Clairvaux | In die sancto Paschae | la | 19 |
| `bernard-diligendo` | Bernard of Clairvaux | De diligendo Deo | en, la | 62 |
| `bernard-dominica-1-novembris` | Bernard of Clairvaux | Pro Dominica I Novembris | la | 34 |
| `bernard-dominica-1-post-octavam-epiphaniae` | Bernard of Clairvaux | Dominica I post octavam Epiphaniae | la | 16 |
| `bernard-dominica-4-post-pentecosten` | Bernard of Clairvaux | Dominica IV post Pentecosten | la | 7 |
| `bernard-dominica-6-post-pentecosten` | Bernard of Clairvaux | Dominica VI post Pentecosten | la | 18 |
| `bernard-dominica-infra-octavam-assumptionis` | Bernard of Clairvaux | Dominica infra octavam assumptionis B. V. Mariae | la | 16 |
| `bernard-dominica-palmarum` | Bernard of Clairvaux | In Dominica Palmarum | la | 19 |
| `bernard-epiphania-domini` | Bernard of Clairvaux | In Epiphania Domini | la | 23 |
| `bernard-epistolae` | Bernard of Clairvaux | Epistolae (Some Letters of Saint Bernard) | en | 77 |
| `bernard-epistolae-eales` | Bernard of Clairvaux | Epistolae — Eales, *Life and Works*, vols. I–III; Letters I–CDXC on Eales's numbering (about 66 also in `bernard-epistolae`, same translation) | en | 490 |
| `bernard-epistolae-pl` | Bernard of Clairvaux | Epistolae | la | 1088 |
| `bernard-feria-iv-hebdomadae` | Bernard of Clairvaux | In feria IV Hebdomadae Sacrae | la | 15 |
| `bernard-festo-omnium-sanctorum` | Bernard of Clairvaux | In festo omnium sanctorum | la | 49 |
| `bernard-festo-pentecostes` | Bernard of Clairvaux | In festo Pentecostes | la | 25 |
| `bernard-festo-petri-pauli` | Bernard of Clairvaux | In festo SS. Petri et Pauli | la | 22 |
| `bernard-festo-s-andreae` | Bernard of Clairvaux | In festo S. Andreae apostoli | la | 20 |
| `bernard-festo-s-martini` | Bernard of Clairvaux | In festo S. Martini | la | 19 |
| `bernard-festo-s-michaelis` | Bernard of Clairvaux | In festo S. Michaelis | la | 12 |
| `bernard-formula-confessionis` | Bernard of Clairvaux | Formula confessionis privatae | la | 5 |
| `bernard-gradibus-humilitatis` | Bernard of Clairvaux | De gradibus humilitatis et superbiae | la | 83 |
| `bernard-gratia-et-libero` | Bernard of Clairvaux | De gratia et libero arbitrio | la | 67 |
| `bernard-laude-militiae` | Bernard of Clairvaux | Liber ad milites Templi de laude novae militiae | la | 1 |
| `bernard-laudibus-virginis-matris` | Bernard of Clairvaux | De laudibus Virginis Matris | la | 57 |
| `bernard-malachia` | Bernard of Clairvaux | Vita Sancti Malachiae | en | 18 |
| `bernard-malachia-pl` | Bernard of Clairvaux | Vita S. Malachiae | la | 108 |
| `bernard-moribus-et-officio` | Bernard of Clairvaux | De moribus et officio episcoporum | la | 53 |
| `bernard-natali-s-benedicti` | Bernard of Clairvaux | In natali S. Benedicti | la | 13 |
| `bernard-natali-s-victoris` | Bernard of Clairvaux | In natali S. Victoris confessoris | la | 12 |
| `bernard-nativitate-bvm` | Bernard of Clairvaux | In navitate B. V. Mariae | la | 19 |
| `bernard-nativitate-domini` | Bernard of Clairvaux | In nativitate Domini. | la | 33 |
| `bernard-nativitate-s-joannis` | Bernard of Clairvaux | In nativitate S. Joannis Baptistae | la | 12 |
| `bernard-nativitate-ss-innocentium` | Bernard of Clairvaux | In nativitate SS. Innocentium | la | 4 |
| `bernard-obitu-d-humberti` | Bernard of Clairvaux | In obitu D. Humberti | la | 8 |
| `bernard-octava-epiphaniae` | Bernard of Clairvaux | In octava Epiphaniae | la | 6 |
| `bernard-octava-paschae` | Bernard of Clairvaux | In octava Paschae | la | 15 |
| `bernard-officium-s-victore` | Bernard of Clairvaux | Officium de S. Victore | la | 5 |
| `bernard-opuscula-duo` | Bernard of Clairvaux | Opuscula duo | la | 3 |
| `bernard-parabolae` | Bernard of Clairvaux | Parabolae | la | 36 |
| `bernard-praecepto-et-dispensatione` | Bernard of Clairvaux | De praecepto et dispensatione | la | 94 |
| `bernard-psalmum-qui-habitat` | Bernard of Clairvaux | In psalmum Qui habitat | la | 143 |
| `bernard-purificatione-bvm` | Bernard of Clairvaux | In Purificatione B. Mariae | la | 13 |
| `bernard-quadragesima` | Bernard of Clairvaux | In Quadragesima | la | 31 |
| `bernard-rogationibus` | Bernard of Clairvaux | In rogationibus | la | 3 |
| `bernard-s-clemente` | Bernard of Clairvaux | De S. Clemente | la | 7 |
| `bernard-sententiae` | Bernard of Clairvaux | Sententiae | la | 45 |
| `bernard-septuagesima` | Bernard of Clairvaux | In Septuagesima | la | 10 |
| `bernard-sermones-cantica-canticorum` | Bernard of Clairvaux | Sermones in Cantica canticorum (en: Eales, vol. IV, anchored at the sermon, 86) | en, la | 875 |
| `bernard-sermones-de-tempore-eales` | Bernard of Clairvaux | Sermones de tempore — Eales, vol. III, Sermons I–XIX on his own numbering (Advent to the Nativity, with *Missus est*) | en | 19 |
| `bernard-sermones-diversis` | Bernard of Clairvaux | Sermones de diversis | la | 504 |
| `bernard-super-hymnum-jesu` | Bernard of Clairvaux | Super hymnum Jesu nostra redemptio | la | 2 |
| `bernard-tempore-resurrectionis` | Bernard of Clairvaux | In tempore resurrectionis | la | 20 |
| `bernard-tonale` | Bernard of Clairvaux | Tonale | la | 2 |
| `bernard-tractatus-cantandi-graduale` | Bernard of Clairvaux | Tractatus cantandi graduale | la | 1 |
| `bernard-transitu-s-malachiae` | Bernard of Clairvaux | In transitu S. Malachiae | la | 18 |
| `bernard-verba-evangelii` | Bernard of Clairvaux | In verba Evangelii | la | 8 |
| `bernard-vigilia-nativitatis-domini` | Bernard of Clairvaux | In vigilia nativitatis Domini | la | 57 |
| `bernard-vigilia-petri-pauli` | Bernard of Clairvaux | In vigilia SS. Petri et Pauli | la | 5 |
| `bernard-vigilia-s-andreae` | Bernard of Clairvaux | In vigilia S. Andreae apostoli | la | 5 |
| `bonaventura-itinerarium` | Bonaventure | Itinerarium mentis in Deum | en | 8 |
| `caterina-dialogo` | Catherine of Siena | Il Dialogo della Divina Provvidenza | en | 98 |
| `chrysologus-sermones` | Peter Chrysologus | Sermones | la | 176 |
| `cyril-alex-diodorum` | Cyril of Alexandria | Contra Diodorum (fragments) | en | 29 |
| `cyril-alex-ioannem` | Cyril of Alexandria | Commentarii in Ioannem (Commentary on the Gospel of John) | en | 66 |
| `cyril-alex-iulianum` | Cyril of Alexandria | Contra Iulianum (prefatory address and Book II) | en | 1 |
| `cyril-alex-lucam` | Cyril of Alexandria | Commentarii in Lucam (Commentary on the Gospel of Luke) | en | 134 |
| `cyril-alex-nestorium` | Cyril of Alexandria | Adversus Nestorium (Five Tomes against Nestorius) | en | 9 |
| `cyril-alex-quod-unus` | Cyril of Alexandria | Quod unus sit Christus (That Christ is One) | en | 1 |
| `cyril-alex-scholia` | Cyril of Alexandria | Scholia de incarnatione Unigeniti | en | 37 |
| `cyril-alex-synousiastas` | Cyril of Alexandria | Contra Synousiastas (fragments) | en | 18 |
| `cyril-alex-theodorum` | Cyril of Alexandria | Contra Theodorum Mopsuestenum (fragments) | en | 20 |
| `gregory-great-aliae-benedictiones` | Gregory the Great | Aliae benedictiones | la | 126 |
| `gregory-great-appendix-1` | Gregory the Great | Appendix 1 | la | 36 |
| `gregory-great-appendix-2` | Gregory the Great | Appendix 2 | la | 1 |
| `gregory-great-appendix-sacramentorum` | Gregory the Great | Appendix ad Librum sacramentorum | la | 7 |
| `gregory-great-benedictionale` | Gregory the Great | Benedictionale | la | 61 |
| `gregory-great-benedictiones` | Gregory the Great | Benedictiones | la | 1 |
| `gregory-great-cantica` | Gregory the Great | Expositio super Cantica canticorum | la | 181 |
| `gregory-great-concordia` | Gregory the Great | Concordia testimoniorum S. Scripturae | la | 34 |
| `gregory-great-constitutiones-lateranenses` | Gregory the Great | Constitutiones Lateranenses | la | 30 |
| `gregory-great-dialogi` | Gregory the Great | Dialogi (The Dialogues) | en | 152 |
| `gregory-great-dialogi-pl` | Gregory the Great | Dialogi | la | 226 |
| `gregory-great-ep-constantinam` | Gregory the Great | Epistula ad Constantinam Augustam (Reg. IV,30) | la | 1 |
| `gregory-great-epistolae` | Gregory the Great | Epistolae | la | 859 |
| `gregory-great-homiliae-evangelia` | Gregory the Great | Homiliae in Evangelia | la | 361 |
| `gregory-great-homiliae-ezechielem` | Gregory the Great | Homiliae in Ezechielem | la | 535 |
| `gregory-great-hymni` | Gregory the Great | Hymni | la | 8 |
| `gregory-great-in-regum` | Gregory the Great | Commentarii in librum I Regum | la | 768 |
| `gregory-great-liber-antiphonarius` | Gregory the Great | Liber antiphonarius | la | 234 |
| `gregory-great-liber-responsalis` | Gregory the Great | Liber responsalis | la | 578 |
| `gregory-great-liber-sacramentorum` | Gregory the Great | Liber sacramentorum | la | 255 |
| `gregory-great-moralia` | Gregory the Great | Moralia in Iob (Morals on the Book of Job) | en | 2468 |
| `gregory-great-moralia-ii` | Gregory the Great | Moralia II | la | 620 |
| `gregory-great-moralia-pl` | Gregory the Great | Moralia | la | 1853 |
| `gregory-great-mortalitate` | Gregory the Great | De mortalitate | la | 1 |
| `gregory-great-prolegomena` | Gregory the Great | Prolegomena | la | 115 |
| `gregory-great-psalmi-poenitentiales` | Gregory the Great | Expositio in psalmos poenitentiales | la | 165 |
| `gregory-great-regula-pastoralis` | Gregory the Great | Regula pastoralis | la | 66 |
| `gregory-great-tabulae-donariorum` | Gregory the Great | Tabulae donariorum marmoreae | la | 3 |
| `gregory-great-vita-benedicti` | Gregory the Great | Vita Sancti Benedicti (Dialogi, liber II) | en | 39 |
| `hilary-apologetica-responsa-ad-reprehensores-libri` | Hilary of Poitiers | Apologetica responsa ad reprehensores libri de synodis | la | 12 |
| `hilary-commentarius-in-matthaeum` | Hilary of Poitiers | Commentarius in Matthaeum | la | 396 |
| `hilary-commentarius-in-psalmos-xv-xxxi` | Hilary of Poitiers | Commentarius in psalmos XV XXXI XLI | la | 37 |
| `hilary-de-trinitate` | Hilary of Poitiers | De Trinitate | la | 589 |
| `hilary-epistola-ad-abram` | Hilary of Poitiers | Epistola ad Abram | la | 8 |
| `hilary-epistola-seu-libellus` | Hilary of Poitiers | Epistola seu libellus | la | 22 |
| `hilary-fragmenta-ex-aliis-operibus` | Hilary of Poitiers | Fragmenta ex aliis operibus | la | 9 |
| `hilary-fragmenta-ex-opere-historico` | Hilary of Poitiers | Fragmenta ex opere historico | la | 134 |
| `hilary-hymnus-abrae-missus` | Hilary of Poitiers | Hymnus Abrae missus | la | 1 |
| `hilary-liber-contra-arianos-vel-auxentium` | Hilary of Poitiers | Liber contra Arianos vel Auxentium | la | 16 |
| `hilary-liber-contra-constantium` | Hilary of Poitiers | Liber contra Constantium | la | 33 |
| `hilary-liber-de-synodis-seu-fide` | Hilary of Poitiers | Liber de synodis seu fide orientalium | la | 159 |
| `hilary-liber-primus-ad-constantium-augustum` | Hilary of Poitiers | Liber primus ad Constantium Augustum | la | 9 |
| `hilary-liber-secundus-ad-constantium` | Hilary of Poitiers | Liber secundus ad Constantium | la | 12 |
| `hilary-sermo-de-dedicatione-ecclesiae` | Hilary of Poitiers | Sermo de dedicatione ecclesiae | la | 1 |
| `hildegard-divinorum-operum` | Hildegard of Bingen | Liber divinorum operum simplicis hominis | la | 330 |
| `hildegard-epistolae` | Hildegard of Bingen | Epistolae | la | 281 |
| `hildegard-regula-benedicti` | Hildegard of Bingen | Explanatio regulae S. Benedicti | la | 2 |
| `hildegard-scivias` | Hildegard of Bingen | Scivias Hildegardis sive libri visionum ac revelationum | la | 30 |
| `hildegard-solutiones` | Hildegard of Bingen | Solutiones quaestionum XXXVIII | la | 78 |
| `hildegard-subtilitates` | Hildegard of Bingen | Subtilitates diversarum naturarum creaturum | la | 538 |
| `hildegard-symbolum-athanasii` | Hildegard of Bingen | Explanatio symboli S. Athanasii | la | 1 |
| `hildegard-vita-s-disibodi` | Hildegard of Bingen | Vita S. Disibodi | la | 59 |
| `hildegard-vita-s-ruperti` | Hildegard of Bingen | Vita S. Ruperti | la | 21 |
| `isidore-allegoriae-sacrae-scripturae` | Isidore of Seville | Allegoriae sacrae Scripturae | la | 235 |
| `isidore-chronicon` | Isidore of Seville | Chronicon | la | 47 |
| `isidore-de-ecclesiasticis-officiis` | Isidore of Seville | De ecclesiasticis officiis | la | 253 |
| `isidore-de-fide-catholica` | Isidore of Seville | De fide Catholica | la | 328 |
| `isidore-de-natura-rerum` | Isidore of Seville | De natura rerum | la | 125 |
| `isidore-de-ordine-creaturarum` | Isidore of Seville | De ordine creaturarum | la | 79 |
| `isidore-de-ortu-et-obitu-patrum` | Isidore of Seville | De ortu et obitu Patrum | la | 179 |
| `isidore-de-viris-illustribus` | Isidore of Seville | De viris illustribus | la | 54 |
| `isidore-differentiae` | Isidore of Seville | Differentiae | la | 733 |
| `isidore-epistolae` | Isidore of Seville | Epistolae | la | 88 |
| `isidore-etymologiae` | Isidore of Seville | Etymologiae sive Origines | la | 5778 |
| `isidore-historia` | Isidore of Seville | Historia de regibus Gothorum, Wandalorum et Sueborum | la | 1 |
| `isidore-liber-numerorum-qui-in-sanctis` | Isidore of Seville | Liber numerorum qui in sanctis Scripturis occurrunt | la | 88 |
| `isidore-prooemia-in-libros-veteris` | Isidore of Seville | Prooemia in libros Veteris ac Novi Testamenti | la | 99 |
| `isidore-quaestiones-de-veteri-et-novo` | Isidore of Seville | Quaestiones de Veteri et Novo Testamento | la | 69 |
| `isidore-quaestiones-in-veterum-testamentum` | Isidore of Seville | Quaestiones in Veterum Testamentum | la | 260 |
| `isidore-regula-monachorum` | Isidore of Seville | Regula monachorum 1 | la | 71 |
| `isidore-regula-monachorum-codex-regularum` | Isidore of Seville | Regula monachorum 2 | la | 24 |
| `isidore-sententiae` | Isidore of Seville | Sententiarum libri tres | la | 990 |
| `isidore-synonyma-de-lamentatione-animae-peccatricis` | Isidore of Seville | Synonyma de lamentatione animae peccatricis | la | 162 |
| `jerome-adversus-jovinianum` | Jerome | Adversus Jovinianum | la | 93 |
| `jerome-apologia-adversus-libros-rufini` | Jerome | Apologia adversus libros Rufini | la | 117 |
| `jerome-chronicon-s-hieronymi` | Jerome | Chronicon S. Hieronymi | la | 18 |
| `jerome-commentaria-in-abacuc` | Jerome | Commentaria in Abacuc | la | 33 |
| `jerome-commentaria-in-abdiam` | Jerome | Commentaria in Abdiam | la | 13 |
| `jerome-commentaria-in-aggaeum` | Jerome | Commentaria in Aggaeum | la | 17 |
| `jerome-commentaria-in-amos` | Jerome | Commentaria in Amos | la | 72 |
| `jerome-commentaria-in-danielem` | Jerome | Commentaria in Danielem | la | 231 |
| `jerome-commentaria-in-epistolam-ad-ephesios` | Jerome | Commentaria in Epistolam ad Ephesios | la | 10 |
| `jerome-commentaria-in-epistolam-ad-galatas` | Jerome | Commentaria in Epistolam ad Galatas | la | 4 |
| `jerome-commentaria-in-epistolam-ad-philemonem` | Jerome | Commentaria in Epistolam ad Philemonem | la | 2 |
| `jerome-commentaria-in-epistolam-ad-titum` | Jerome | Commentaria in Epistolam ad Titum | la | 2 |
| `jerome-commentaria-in-ezechielem` | Jerome | Commentaria in Ezechielem | la | 399 |
| `jerome-commentaria-in-isaiam` | Jerome | Commentaria in Isaiam | la | 93 |
| `jerome-commentaria-in-jeremiam` | Jerome | Commentaria in Jeremiam | la | 7 |
| `jerome-commentaria-in-job` | Jerome | Commentaria in Job | la | 44 |
| `jerome-commentaria-in-joelem` | Jerome | Commentaria in Joelem | la | 32 |
| `jerome-commentaria-in-jonam` | Jerome | Commentaria in Jonam | la | 41 |
| `jerome-commentaria-in-malachiam` | Jerome | Commentaria in Malachiam | la | 29 |
| `jerome-commentaria-in-matthaeum` | Jerome | Commentaria in Matthaeum | la | 5 |
| `jerome-commentaria-in-michaeam` | Jerome | Commentaria in Michaeam | la | 41 |
| `jerome-commentaria-in-naum` | Jerome | Commentaria in Naum | la | 31 |
| `jerome-commentaria-in-osee` | Jerome | Commentaria in Osee | la | 132 |
| `jerome-commentaria-in-sophoniam` | Jerome | Commentaria in Sophoniam | la | 25 |
| `jerome-commentaria-in-zachariam` | Jerome | Commentaria in Zachariam | la | 108 |
| `jerome-commentarius-in-ecclesiasten` | Jerome | Commentarius in Ecclesiasten | la | 2 |
| `jerome-contra-joannem-hierosolymitanum` | Jerome | Contra Joannem Hierosolymitanum | la | 48 |
| `jerome-contra-vigilantium` | Jerome | Contra Vigilantium | la | 21 |
| `jerome-de-formis-hebraicarum-litterarum` | Jerome | De formis Hebraicarum litterarum | la | 1 |
| `jerome-de-nominibus-hebraicis` | Jerome | De nominibus Hebraicis | la | 61 |
| `jerome-de-situ-et-nominibus-locorum` | Jerome | De situ et nominibus locorum Hebraicorum | la | 99 |
| `jerome-de-virginitate-b-mariae` | Jerome | De virginitate B. Mariae | la | 26 |
| `jerome-de-viris-illustribus` | Jerome | De viris illustribus | la | 143 |
| `jerome-de-x-nominibus-dei` | Jerome | De X nominibus Dei | la | 4 |
| `jerome-dialogus-contra-luciferianos` | Jerome | Dialogus contra Luciferianos | la | 29 |
| `jerome-dialogus-contra-pelagianos` | Jerome | Dialogus contra Pelagianos | la | 100 |
| `jerome-praefatio-in-evangelia` | Jerome | Praefatio in Evangelia | la | 1 |
| `jerome-praefatio-in-libros-salomonis` | Jerome | Praefatio in libros Salomonis | la | 1 |
| `jerome-praefatio-in-pentateuchum` | Jerome | Praefatio in Pentateuchum | la | 1 |
| `jerome-praefationes-aliae` | Jerome | Praefationes aliae | la | 3 |
| `jerome-quaestiones-hebraicae-in-genesim` | Jerome | Quaestiones Hebraicae in Genesim | la | 123 |
| `jerome-vita-malchi-monachi-captivi` | Jerome | Vita Malchi monachi captivi | la | 10 |
| `jerome-vita-s-hilarionis` | Jerome | Vita S. Hilarionis | la | 49 |
| `jerome-vita-s-pauli-primi-eremitae` | Jerome | Vita S. Pauli primi eremitae | la | 21 |
| `juan-avisos` | Juan de la Cruz | Avisos (las cinco colecciones) | es | 76 |
| `juan-cantico` | Juan de la Cruz | Cántico espiritual (redacción B) | en, es | 439 |
| `juan-cantico-a` | Juan de la Cruz | Cántico espiritual (redacción A) | es | 380 |
| `juan-cantico-ca` | Juan de la Cruz | Cántico espiritual (canciones solas) | es | 39 |
| `juan-cautelas` | Juan de la Cruz | Cautelas | es | 17 |
| `juan-dichos` | Juan de la Cruz | Dichos de luz y amor | es | 78 |
| `juan-epistolario` | Juan de la Cruz | Epistolario | es | 38 |
| `juan-grados` | Juan de la Cruz | Grados de perfección | es | 17 |
| `juan-llama` | Juan de la Cruz | Llama de amor viva (redacción B) | es | 182 |
| `juan-llama-a` | Juan de la Cruz | Llama de amor viva (redacción A) | es | 162 |
| `juan-noche` | John of the Cross | Noche oscura | en, es | 304 |
| `juan-poesias` | Juan de la Cruz | Poesías | es | 66 |
| `juan-subida` | John of the Cross | Subida del Monte Carmelo | en, es | 701 |
| `leo-great-appendix-prima` | Leo the Great | Appendix prima | la | 31 |
| `leo-great-appendix-secunda` | Leo the Great | Appendix secunda | la | 5 |
| `leo-great-epistola-ad-flavianum` | Leo the Great | Epistola ad Flavianum | la | 1 |
| `leo-great-epistola-lxxxviii` | Leo the Great | Epistola LXXXVIII | la | 1 |
| `leo-great-epistolae` | Leo the Great | Epistolae | la | 953 |
| `leo-great-eutychiana` | Leo the Great | De haeresi et historia Eutychiana | la | 309 |
| `leo-great-manichaeorum` | Leo the Great | De haeresi et historia Manichaeorum | la | 242 |
| `leo-great-pelagiana` | Leo the Great | De haeresi Pelagiana | la | 67 |
| `leo-great-priscillianistarum` | Leo the Great | De haeresi et historia Priscillianistarum | la | 145 |
| `leo-great-quadragesima` | Leo the Great | Sermones de Quadragesima I-II | la | 13 |
| `leo-great-sacramenta` | Leo the Great | Sacramenta Romanae Ecclesiae | la | 302 |
| `leo-great-sermones` | Leo the Great | Sermones | la | 575 |
| `leo-great-sermones-inediti` | Leo the Great | Sermones inediti | la | 43 |
| `newman-addresses` | John Henry Newman | Addresses to Cardinal Newman with His Replies | en | 6 |
| `newman-anglicans-1` | John Henry Newman | Certain Difficulties Felt by Anglicans in Catholic Teaching, Volume 1 | en | 12 |
| `newman-apologia` | John Henry Newman | Apologia pro vita sua | en | 15 |
| `newman-arguments` | John Henry Newman | Discussions and Arguments on Various Subjects | en | 29 |
| `newman-arians` | John Henry Newman | The Arians of the Fourth Century | en | 13 |
| `newman-british-critic` | John Henry Newman | Essays from the British Critic | en | 15 |
| `newman-callista` | John Henry Newman | Callista: A Tale of the Third Century | en | 38 |
| `newman-development` | John Henry Newman | An Essay on the Development of Christian Doctrine | en | 15 |
| `newman-discourses` | John Henry Newman | Discourses Addressed to Mixed Congregations | en | 18 |
| `newman-england` | John Henry Newman | Lectures on the Present Position of Catholics in England | en | 10 |
| `newman-error` | John Henry Newman | The Development of Religious Error | en | 5 |
| `newman-essays-1` | John Henry Newman | Essays Critical and Historical, Volume 1 | en | 15 |
| `newman-essays-2` | John Henry Newman | Essays Critical and Historical, Volume 2 | en | 14 |
| `newman-gain` | John Henry Newman | Loss and Gain: The Story of a Convert | en | 50 |
| `newman-gerontius` | John Henry Newman | The Dream of Gerontius | en | 7 |
| `newman-grammar` | John Henry Newman | An Essay in Aid of a Grammar of Assent | en | 13 |
| `newman-historical-1` | John Henry Newman | Historical Sketches, Volume 1 | en | 20 |
| `newman-historical-2` | John Henry Newman | Historical Sketches, Volume 2 | en | 15 |
| `newman-historical-3` | John Henry Newman | Historical Sketches, Volume 3 | en | 29 |
| `newman-idea` | John Henry Newman | The Idea of a University | en | 20 |
| `newman-justification` | John Henry Newman | Lectures on the Doctrine of Justification | en | 16 |
| `newman-meditations` | John Henry Newman | Meditations and Devotions | en | 12 |
| `newman-miracles` | John Henry Newman | Two Essays on Biblical and on Ecclesiastical Miracles | en | 11 |
| `newman-ninesermons` | John Henry Newman | Faith and Prejudice and Other Unpublished Sermons | en | 9 |
| `newman-norfolk` | John Henry Newman | A Letter Addressed to the Duke of Norfolk | en | 11 |
| `newman-occasions` | John Henry Newman | Sermons Preached on Various Occasions | en | 18 |
| `newman-oxford` | John Henry Newman | Fifteen Sermons Preached before the University of Oxford | en | 15 |
| `newman-parochial` | John Henry Newman | Parochial and Plain Sermons | en | 191 |
| `newman-prophetical-office` | John Henry Newman | The Via Media, Volume 1: Lectures on the Prophetical Office of the Church | en | 16 |
| `newman-pusey` | John Henry Newman | A Letter to the Rev. E. B. Pusey on his Recent Eirenicon | en | 6 |
| `newman-saints` | John Henry Newman | Lives of the English Saints (Newman's contributions) | en | 3 |
| `newman-sayings` | John Henry Newman | Sayings of Cardinal Newman | en | 2 |
| `newman-sermonnotes` | John Henry Newman | Sermon Notes of John Henry Cardinal Newman | en | 11 |
| `newman-subjects` | John Henry Newman | Sermons Bearing on Subjects of the Day | en | 26 |
| `newman-tracts-theological` | John Henry Newman | Tracts Theological and Ecclesiastical | en | 6 |
| `newman-tracts-times` | John Henry Newman | Tracts for the Times (Newman's own) | en | 46 |
| `newman-verses` | John Henry Newman | Verses on Various Occasions | en | 184 |
| `newman-via-media-2` | John Henry Newman | The Via Media, Volume 2 | en | 11 |
| `peter-damian-abdicatione-episcopatus` | Peter Damian | De abdicatione episcopatus | la | 13 |
| `peter-damian-acta` | Peter Damian | Acta | la | 1 |
| `peter-damian-actus-mediolani-privilegio` | Peter Damian | Actus Mediolani de privilegio Romanae ecclesiae | la | 11 |
| `peter-damian-antilogus-contra-judaeos` | Peter Damian | Antilogus contra Judaeos ad Honestum | la | 5 |
| `peter-damian-apologeticum-contemptu` | Peter Damian | Apologeticum de contemptu saeculi | la | 35 |
| `peter-damian-apologeticus-monachorum` | Peter Damian | Apologeticus monachorum adversus canonicos | la | 4 |
| `peter-damian-apologeticus-ob-dimissum` | Peter Damian | Apologeticus ob dimissum episcopatum | la | 9 |
| `peter-damian-bono-status-religiosi` | Peter Damian | De bono status religiosi et tropologia variarum animantium | la | 32 |
| `peter-damian-bono-suffragiorum` | Peter Damian | De bono suffragiorum et variis miraculis | la | 9 |
| `peter-damian-brevitate-vitae-pontificum` | Peter Damian | De brevitate vitae pontificum Romanorum et divina providentia | la | 7 |
| `peter-damian-caelibatu-sacerdotum` | Peter Damian | De caelibatu sacerdotum | la | 5 |
| `peter-damian-carmina-sacra` | Peter Damian | Carmina sacra et preces | la | 225 |
| `peter-damian-castitate-et-mediis` | Peter Damian | De castitate et mediis eam tuendi | la | 7 |
| `peter-damian-celebrandis-vigiliis` | Peter Damian | De celebrandis vigiliis | la | 8 |
| `peter-damian-collectanea-vetus` | Peter Damian | Collectanea in Vetus Testamentum | la | 301 |
| `peter-damian-communi-vita-canonicorum` | Peter Damian | De communi vita canonicorum | la | 6 |
| `peter-damian-contra-clericos-aulicos` | Peter Damian | Contra clericos aulicos | la | 5 |
| `peter-damian-contra-clericos-regulares` | Peter Damian | Contra clericos regulares proprietarios | la | 7 |
| `peter-damian-contra-errorem-graecorum` | Peter Damian | Contra errorem Graecorum de processione Spiritus Sancti | la | 8 |
| `peter-damian-contra-inscitiam` | Peter Damian | Contra inscitiam et incuriam clericorum | la | 5 |
| `peter-damian-contra-intemperantes` | Peter Damian | Contra intemperantes clericos | la | 27 |
| `peter-damian-contra-philargyriam` | Peter Damian | Contra philargyriam et cupiditatem munerum | la | 10 |
| `peter-damian-contra-sedentes-tempore` | Peter Damian | Contra sedentes tempore divini officii | la | 5 |
| `peter-damian-dialogus-inter-judaeum` | Peter Damian | Dialogus inter Judaeum et Christianum ad Honestum | la | 1 |
| `peter-damian-dignitate-sacerdotii` | Peter Damian | De dignitate sacerdotii | la | 4 |
| `peter-damian-dissertatiuncula` | Peter Damian | Dissertatiuncula | la | 4 |
| `peter-damian-divina-omnipotentia` | Peter Damian | De divina omnipotentia in reparatione corruptae et factis infectis reddendis | la | 18 |
| `peter-damian-eleemosyna-ad-mainardum` | Peter Damian | De eleemosyna ad Mainardum | la | 9 |
| `peter-damian-epistolae` | Peter Damian | Epistolae | la | 166 |
| `peter-damian-expositio-mystica` | Peter Damian | Expositio mystica historiarum Libri Geneseos | la | 30 |
| `peter-damian-expositio-visionum` | Peter Damian | Expositio visionum SS. Mariani et Jacobi | la | 1 |
| `peter-damian-ferenda-aequanimiter` | Peter Damian | De ferenda aequanimiter correptione | la | 7 |
| `peter-damian-fide-catholica` | Peter Damian | De fide catholica ad Ambrosium | la | 13 |
| `peter-damian-fide-deo-obstricta` | Peter Damian | De fide Deo obstricta | la | 15 |
| `peter-damian-fluxa-gloria-mundi` | Peter Damian | De fluxa gloria mundi et despectione saeculi | la | 11 |
| `peter-damian-frenanda-ira` | Peter Damian | De frenanda ira et simultatibus extirpandis | la | 10 |
| `peter-damian-fuga-dignitatum` | Peter Damian | De fuga dignitatum ecclesiasticarum | la | 4 |
| `peter-damian-gradibus-parentelae` | Peter Damian | De gradibus parentelae | la | 13 |
| `peter-damian-horis-canonicis` | Peter Damian | De horis canonicis | la | 12 |
| `peter-damian-hymnus-gloria-paradisi` | Peter Damian | Hymnus de gloria Paradisi | la | 1 |
| `peter-damian-institutio-monialis` | Peter Damian | Institutio monialis | la | 16 |
| `peter-damian-institutis-suae` | Peter Damian | De institutis suae congregationis | la | 33 |
| `peter-damian-invectio-episcopum-monachos` | Peter Damian | Invectio in episcopum monachos ad saeculum revocantem | la | 11 |
| `peter-damian-jejunio-sabbati` | Peter Damian | De jejunio Sabbati | la | 6 |
| `peter-damian-laude-flagellorum` | Peter Damian | De laude flagellorum et disciplinae | la | 7 |
| `peter-damian-liber-dominus-vobiscum` | Peter Damian | Liber Dominus vobiscum ad Leonem | la | 21 |
| `peter-damian-liber-gomorrhianus` | Peter Damian | Liber Gomorrhianus ad Leonem IX | la | 30 |
| `peter-damian-novissimis-et-antichristo` | Peter Damian | De novissimis et Antichristo | la | 5 |
| `peter-damian-officio-principis` | Peter Damian | De officio principis in coercitione improborum | la | 15 |
| `peter-damian-ordine-eremitarum` | Peter Damian | De ordine eremitarum et facultatibus eremi Fontis Avellani | la | 1 |
| `peter-damian-passio-ss-florae` | Peter Damian | Passio SS. Florae et Lucillae | la | 4 |
| `peter-damian-patientia-insectatione` | Peter Damian | De patientia in insectatione improborum | la | 5 |
| `peter-damian-perfecta-informatione` | Peter Damian | De perfecta informatione monachi | la | 12 |
| `peter-damian-perfectione-monachorum` | Peter Damian | De perfectione monachorum | la | 26 |
| `peter-damian-picturis-principum` | Peter Damian | De picturis principum apostolorum | la | 6 |
| `peter-damian-quadragesima-et-quadraginta` | Peter Damian | De quadragesima et quadraginta duabus mansionibus Hebraeorum | la | 10 |
| `peter-damian-sacramentis-per-improbos` | Peter Damian | De sacramentis per improbos administratis | la | 5 |
| `peter-damian-sancta-simplicitate` | Peter Damian | De sancta simplicitate scientiae inflanti anteponenda | la | 9 |
| `peter-damian-sermones` | Peter Damian | Sermones | la | 91 |
| `peter-damian-spiritualibus-deliciis` | Peter Damian | De spiritualibus deliciis | la | 5 |
| `peter-damian-tempore-celebrandi-nuptias` | Peter Damian | De tempore celebrandi nuptias | la | 6 |
| `peter-damian-variis-miraculosis` | Peter Damian | De variis miraculosis narrationibus | la | 18 |
| `peter-damian-variis-sacris-quaestionibus` | Peter Damian | De variis sacris quaestionibus | la | 15 |
| `peter-damian-vera-felicitate` | Peter Damian | De vera felicitate ac sapientia | la | 7 |
| `peter-damian-vili-vestitu` | Peter Damian | De vili vestitu ecclesiasticorum | la | 4 |
| `peter-damian-vita-eremitica` | Peter Damian | De vita eremitica et probatis eremitis | la | 15 |
| `peter-damian-vita-s-mauri` | Peter Damian | Vita S. Mauri | la | 4 |
| `peter-damian-vita-s-odilonis` | Peter Damian | Vita S. Odilonis | la | 1 |
| `peter-damian-vita-s-romualdi` | Peter Damian | Vita S. Romualdi | la | 73 |
| `peter-damian-vita-ss-rodulphi` | Peter Damian | Vita SS. Rodulphi et Dominici Loricati | la | 15 |
| `peter-damian-x-aegypti-plagis` | Peter Damian | De X Aegypti plagis atque decalogo | la | 14 |
| `sales-amour-de-dieu` | Francis de Sales | Traité de l'amour de Dieu | en | 201 |
| `sales-cantique` | Francis de Sales | The Mystical Explanation of the Canticle of Canticles (Mackey's English title; French not printed) — Mackey, vol. VI | en | 8 |
| `sales-controverses` | Francis de Sales | Les Controverses — Mackey, vol. III | en | 96 |
| `sales-entretiens` | Francis de Sales | Les Vrais Entretiens spirituels — Mackey, vol. V | en | 23 |
| `sales-letters-religion` | Francis de Sales | Letters to Persons in Religion (Mackey's English title; French not printed) — Mackey, vol. IV | en | 187 |
| `sales-lettres-monde` | Francis de Sales | Lettres à des gens du monde — Mackey, vol. I | en | 193 |
| `sales-vie-devote` | Francis de Sales | Introduction à la vie dévote | en | 126 |
| `teresa-camino` | Teresa of Jesus (of Ávila) | Camino de perfección | en, es | 397 |
| `teresa-fundaciones` | Teresa de Jesús | Libro de las fundaciones | es | 476 |
| `teresa-moradas` | Teresa of Jesus (of Ávila) | Castillo interior (Las moradas) | en, es | 412 |
| `teresa-relaciones` | Teresa of Jesus (of Ávila) | Relaciones espirituales | en | 11 |
| `teresa-vida` | Teresa de Jesús | Libro de la vida | en, es | 670 |
| `therese-conseils` | Thérèse of Lisieux | Conseils et souvenirs | en | 0 |
| `therese-histoire` | Thérèse of Lisieux | Histoire d'une âme | en | 13 |
| `therese-lettres` | Thérèse of Lisieux | Lettres (selection) | en | 57 |
| `therese-poesies` | Thérèse of Lisieux | Poésies | en | 50 |
| `therese-prieres` | Thérèse of Lisieux | Prières | en | 11 |
