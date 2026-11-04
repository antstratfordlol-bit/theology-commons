# Acta Sanctae Sedis and Acta Apostolicae Sedis

The official acts of the Holy See, 1865 to 2006, as scanned PDFs with a text layer. Fetched from **vatican.va itself** on 2026-08-21 by `99. Tools/fetch/fetch_acta.py`.

*Acta Apostolicae Sedis* is the official gazette of the Holy See, established by St Pius X in the constitution *Promulgandi Pontificias Constitutiones* of 29 September 1908 and published from 1909. **Promulgation in it is what gives a universal law its legal force** — `cic.8.1`: *"Las leyes eclesiásticas universales se promulgan mediante su publicación en el Boletín Oficial «Acta Apostolicae Sedis»"*, and they bind three months from the date of the issue. *Acta Sanctae Sedis* is its predecessor: a compilation begun privately in 1865 by Pietro Avanzini, later recognised as official, and superseded when AAS began. (The date and instrument of that recognition — commonly given as 1904 — has not been verified here against a source.)

**This is the primary text.** Where a document is in these volumes, this is the promulgated Latin, not a translation or a reproduction of one — the thing itself, with its volume and page. Cite by series, volume, year and page: *AAS* 58 (1966) 947.

---

## What is here

| Series | Volumes | Years | Files |
|---|---|---|---|
| **ASS** | 1–41, complete | 1865–1908 | `ASS-NN-YEARS-ocr.pdf` |
| **AAS** | 1–94, complete (9 and 75 in two volumes each) | 1909–2002 | `AAS-NN-YYYY-ocr.pdf` |
| **AAS** | 95, 96, 97, 98 | 2003–2006 | as above |

**From 2003 the Holy See publishes monthly fascicles, not annual OCR volumes.** The index page links twelve PDFs per year from 2003 onward. **Four** whole-year OCR volumes nevertheless sit on the server, linked from nowhere — 95 (2003), 96 (2004), 97 (2005) and 98 (2006). All four are here and all four are genuine: their title pages read *AN. ET VOL. XCV / XCVI / XCVII / XCVIII*, 990 to 1,143 pages each. Volumes 99 (2007) onward were not probed and appear to exist only as fascicles; if they are wanted, they are twelve files a year at the same politeness.

**A warning about this server, learned the hard way.** `AAS-97-2005-ocr.pdf` returned a clean **HTTP 404** on one pass and a genuine 4.6 MB PDF on the next. Under load or a flaky connection vatican.va returns 404s, truncated SSL sessions and closed connections for files that are plainly there. **A single failed request is not evidence that a volume is absent.** The fetcher therefore retries every request four times with backoff, 404 included, and reports nothing missing until it has failed all four.

Two ASS filenames are irregular because those volumes carry a supplement with its own pagination, and the Holy See put the page ranges in the filename:

```
ASS-10-1877-1-639+supplemento-321-448-ocr.pdf
ASS-16-1883-84-1-576+supplemento-17-96-ocr.pdf
```

A URL built by pattern misses both, which is why the list is read off the index page rather than generated. The two index pages are `https://www.vatican.va/archive/aas/index_sp.htm` and `https://www.vatican.va/archive/ass/index_sp.htm`; **the ASS page is not linked from the AAS page** and is easy to miss entirely.

## Rights — read this before quoting into anything published

Libreria Editrice Vaticana asserts rights over the Holy See's texts broadly and without distinguishing by date. Against that stands the age of the material, and the distinction that actually matters is between holding a copy and republishing it.

- **ASS, 1865–1908, is unambiguously in the public domain by age.** Every volume here is more than a century old.
- **AAS before 1930 is beyond any plausible copyright term**, on any jurisdiction's rules.
- **The mid-century volumes are a grey zone.** Roughly 1930 to the 1970s: old enough that the claim is doubtful, recent enough that it is not absurd. Nobody has litigated it.
- **For a private local study library the exposure is nil.** These are official public documents, published by their own author for consultation, and reading them here is exactly the use vatican.va offers.
- **The risk attaches to republication**, not to holding. Reproducing a substantial run of a post-1930 volume in something that leaves this machine — an artifact, a website, a printed booklet — is a different act from citing a page. Quoting a canon, a decree or a paragraph with its AAS reference is ordinary scholarly citation and is not what this warning is about.

The text itself is a legal-official text of the Holy See; in most jurisdictions official legislative texts carry a weaker copyright claim than ordinary works, but the Holy See is not most jurisdictions and does not say so.

## The text layer — what it is good for, and what it is not

Every volume carries a real text layer, produced by **ABBYY FineReader 9.0** in 2009. It is not a re-OCR of a bad scan; it is generally accurate on body text and worth grepping. But "clean" would overstate it, and the defects are systematic:

Measured on `AAS-01-1909-ocr.pdf` (908 pages, 2.08 M characters, 2,294 per page, 5 pages with no text) and `ASS-01-1865-66-ocr.pdf` (767 pages, 1.77 M characters, 2,310 per page, none empty):

1. **Hyphenation is preserved as a soft hyphen (U+00AD) plus a line break.** 5,259 of them in AAS 1, 9,058 in ASS 1. So `admi­nistratione` does not match a search for *administratione*. **De-hyphenation is mandatory before this corpus is searchable at all** — the same class of trap as the long ſ in Mansi, recorded in `04. Reference/external-corpora.md`.
2. **Accented text is correct.** Italian, French, Spanish and German documents come through with their accents intact — `é à è ì ù ò ñ ü ö ä` all present in the right places. The claim that the OCR handles accents well holds.
3. **Display type defeats the OCR.** Mastheads and ornamental headings are frequently mangled: `ACTA APOM¡G¡FSMS` for *ACTA APOSTOLICAE SEDIS*, `COMMENTAEIÜM` for *COMMENTARIUM*, `EX S. CONGBESATIOSE` for *EX S. CONGREGATIONE*, `ACT A` for *ACTA*. Body text is far better than the headings.
4. **Nineteenth-century quotation typography survives literally.** ASS repeats a `»` at the head of every line of a block quotation — 5,965 `»` against 1,469 `«` in ASS 1 — and closing guillemets are sometimes read as `))` or `<(`.
5. **Scattered single-character slips** in body text: `§ %` for `§ 2`, `iisdQm` for *iisdem*, `excelienti` for *excellenti*, `ab1` for *ab*.

**Practical consequence.** Good enough to find a passage and read it; **not good enough to quote from without checking the quotation against the page image.** Treat it as a finding aid over an authoritative scan, and quote from the scan.

## What has deliberately not been done

**No Markdown conversion.** 545 MB of scanned Latin is not worth converting in bulk before anyone knows which volumes matter, and a conversion that carried the hyphenation and the mangled headings through would be worse than none. The value now is having the volumes locally, complete, and catalogued. A later pass over selected volumes should: join soft-hyphenated words, normalise the guillemets, and keep the page number, because the page is the citation unit.

**No anchor grammar.** There is nothing to anchor on: these are page images, and AAS is cited by volume and page, not by a numbered unit. If a specific document from a volume is wanted as text, fetch that document from vatican.va in its own right — it will be there, in several languages, and anchored.

## Provenance

Fetched with a 2-second delay between requests and an identifying User-Agent, honouring `https://www.vatican.va/robots.txt` (`User-agent: * / Allow: * / Crawl-delay: 2`, checked on the day). The fetcher is resumable and verifies `%PDF` magic on every response, so a captured error page cannot pass as a volume; every file here was checked for PDF magic, a `%%EOF` trailer and a readable page tree.

This replaces **Documenta Catholica Omnia** as the source for both series. DCO forbids robot download and mirroring in its own terms; the Holy See does not, and publishes the same volumes itself. See `04. Reference/external-corpora.md`.
