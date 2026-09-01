# Scout report: DOMRINA-FULLTEXT — genuine Izvestiya II bytes

**Lane.** Bounded acquisition; page-verify every PDF candidate.
**Target.** A. V. Domrina, “On four-sheeted polynomial mappings of \(\mathbf{C}^2\). II. The general case”, *Izvestiya: Mathematics* **64**:1 (2000) 1–33, DOI `10.1070/IM2000v064n01ABEH000273`. Russian original: *Izv. RAN Ser. Mat.* **64**:1 (2000).
**Date.** 2026-09-01.
**Author.** grok-4.6 scout lane.
**Non-targets.** Do not re-fetch the two shadow-library copies already known to carry identical 2008 Ni3Al / JPCM bytes. Do not edit canonical ledgers or charged files. Do not inspect `jc2-lean`. No CAS. No `charge_basis`.

## 0. Method and reject rule

Reject rule (as charged): a candidate PDF is genuine only if the first *content* page shows the Domrina four-sheeted title. A first page that is JPCM / Ni3Al (or any other paper) is a reject, even if the filename, DOI string, or landing-page metadata look correct. Shadow-library copies of DOI `10.1070/IM2000v064n01ABEH000273` were not re-fetched.

Acquisition order: (1) mathnet.ru free full text (Russian original required; English translation also hosted there); (2) IOP/Turpion legacy ISSN `1064-5632` vol. 64 issue 1; (3) citing repositories. Every URL tried is in §5. No CAS. No `jc2-lean`. No ledger or charged-file edits. The already-pinned 1999 English scan `refs/domrina1999_mathnotes65_four_sheeted_general_case.pdf` was not opened for content and was not overwritten.

Page verification for a typeset PDF: `pdfinfo` + `pdftotext -f 1 -l 2` + `pdftoppm` of page 1 + a whole-file `rg` for `Ni3Al`/`JPCM`/`Domrina`/`four-sheeted`. For a scan, the same plus a rendered first-page image.

## 1. Mathnet.ru: author search, paperid, Russian original PDF

Author search `https://www.mathnet.ru/php/search.phtml?option_lang=eng&AuthorLastName=Domrina` landed on the Terms-of-Use interstitial, not a hit list. The paper page `https://www.mathnet.ru/eng/im273` (Mi `im273`) names the author and links `personid=8915`. That is the correct paperid: *Izv. RAN Ser. Mat.* **64**:1 (2000) 3–36; English *Izv. Math.* **64**:1 (2000) 1–33. Abstract on the landing page: there are no four-sheeted polynomial mappings \(\mathbf C^2\to\mathbf C^2\) whose Jacobian is a non-zero constant. Received 05.03.1998. MR 1752579, zbMATH 0962.14038.

Mathnet hosts **both** full texts for free (download counters: Russian 320, English 143):

- Russian scan, advertised 2804 kB: `getFT.phtml?jrnid=im&paperid=273&what=fullt` → `/links/<token>/im273.pdf`.
- English typeset, advertised 399 kB: `getFT.phtml?…&what=fullteng` → `/links/<token>/im273_eng.pdf`.

Unchunked `curl` of the English object stalled at exactly 20480 bytes (first TCP window). HTTP/1.1 `Range: bytes=` of 16 KiB succeeded. Assembled sizes match `Content-Range` totals and the ETag object-size field (`63cee` = 408814; `2bd0a8` = 2871464). Tokens in `/links/<hex>/` change per session; they are not content hashes.

**Russian original — ACCEPT (language: Russian, as charged).** Path `refs/domrina2000_im273_russian.pdf`. 2 871 464 bytes, 34 pages (journal 3–36), PDF 1.2, producer ABBYY Hot Folder (2007-06-21), Last-Modified 2009-05-15. First content page (rendered and `pdftotext`): running head «СЕРИЯ МАТЕМАТИЧЕСКАЯ / Том 64, № 1, 2000», УДК 517.55, author «А. В. Домрина», title «О четырехлистных полиномиальных отображениях \(\mathbf C^2\). II. Общий случай», theorem that topological degree four forbids a non-zero constant Jacobian, continuation of [4] (one-dicritical case). Last page: bibliography of four items (Vitushkin; Bass–Connell–Wright; Orevkov 1986; Domrina–Orevkov I) and «Поступило в редакцию 5.III.1998». No Ni3Al / JPCM string anywhere.

**English translation on the same host — ACCEPT.** This is the Turpion/LMS typesetting, not a third-party re-OCR. Path `refs/domrina2000_izv64_four_sheeted_general_case.pdf`. 408 814 bytes, 33 pages (journal 1–33), PDF 1.3, Acrobat Distiller 3.0 for Windows, CreationDate 2000-05-30, ModDate 2000-07-27. First content page (rendered PNG + `pdftotext -layout`):

- running heads `Izvestiya: Mathematics 64:1 1-33` and `Izvestiya RAN: Ser. Mat. 64:1 3-36`, `©2000 RAS(DoM) and LMS`, UDC 517.55, DOI `10.1070/IM2000v064n01ABEH000273`;
- title **On four-sheeted polynomial mappings of \(\mathbf C^2\). II. The general case**, A. V. Domrina;
- Abstract: no four-sheeted polynomial mappings of \(\mathbf C^2\) into itself whose Jacobian is a non-zero constant;
- Theorem (p. 1): topological degree four \(\Rightarrow\) Jacobian cannot be a non-zero constant; continuation of [4]; RFBR 96-01-01218; MSC 13B10, 14E05.

Page 2, Proposition 1.2: two dicritical components, ramification orders 1 and 2, \(m(\tilde g_1)=n(\tilde g_1)=1\), \(m(\tilde g_2)=1\), \(n(\tilde g_2)=2\). Last page 33: bibliography [1]–[4], «Received 5/MAR/98», «Translated by THE AUTHOR», «Typeset by AMS-TeX». Whole-file search: many `Domrina` / `four-sheeted` / `Jacobian`; zero `Ni3Al` / `JPCM` / condensed-matter. `qpdf --check` reports no stream errors.

Unchunked GET of the same English URL is a **transport dead end** (stall at 20 KiB); the assembled Range file is complete.

## 2. IOP / Turpion English translation

ISSN `1064-5632` vol. 64 issue 1 is live. The TOC `https://iopscience.iop.org/issue/1064-5632/64/1` lists Domrina as the first article (pages 1–33) with the correct abstract and DOI. The article HTML `https://iopscience.iop.org/article/10.1070/IM2000v064n01ABEH000273` shows the same title, citation `A V Domrina 2000 Izv. Math. 64 1`, and a paywall: “The computer you are using is not registered by an institution with a subscription.” Direct PDF `…/ABEH000273/pdf` returned HTTP 302 to Radware `validate.perfdrive.com` (bot manager). No PDF bytes were obtained from IOP. No first-page check was possible; this is a **paywall / bot-challenge dead end**, not a Ni3Al reject.

Turpion: `https://www.turpion.org/php/paper.phtml?journal_id=im&paper_id=273` failed at fetch; `http://www.turpion.org/php/paper.phtml?journal_id=im&paper_id=273` timed out (20 s). Dead end.

Crossref for the English DOI names Steklov as publisher and sets the primary resource URL to `https://www.mathnet.ru/eng/im273`. The mathnet English PDF of §1 is therefore the official translation, obtained without IOP.

## 3. Citing repositories hosting the translation

No independent host of the *translation* was found.

- Orevkov’s page `https://www.math.univ-toulouse.fr/~orevkov/` hosts paper I (`do.pdf`) and Orevkov 1986 (`jc86.pdf`), not II.
- OpenAlex `W2071669920`: `is_oa=false`, `oa_url=null`, `any_repository_has_fulltext=false`.
- Semantic Scholar `6c9a868303476821282f345288a567b3fcf0a171`: `isOpenAccess=false`, empty `openAccessPdf.url`.
- Unpaywall API: 422 (example.com email rejected); not retried with a personal address.
- CyberLeninka guessed slug `…/o-chetyrehlistnyh-polinomialnyh-otobrazheniyah-c-2-ii-obschiy-sluchay`: 404. Search page returned no usable hit.
- Wayback CDX queries: HTTP 429.
- zbMATH `an:0962.14038`: Cloudflare interstitial, no PDF.
- ISTINA author list `https://istina.msu.ru/workers/2701793/all/` confirms the 2000 *Izv. RAN* citation (pp. 3–36); a guessed publication URL 404’d.
- `fizmathim.com/o-chetyrehlistnyh-polinomialnyh-otobrazheniyah-s2`: 1998 MSU dissertation (Vitushkin advisor), HTML OCR of the thesis, not the Izvestiya typesetting. Chapter II = one dicritical; Chapter III = two dicriticals. Related, not the target bytes. No journal PDF there.

Shadow-library copies of the DOI were **not** re-fetched.

## 4. Domrina mathnet author page: complete paper list

Fetched: `https://www.mathnet.ru/php/person.phtml?option_lang=eng&personid=8915` and the Russian twin. Aleksandra Vladimirovna Domrina; MathSciNet 633292; eLibrary 15807; MSU CMC. Math-Net.Ru counts **11 scientific articles**. Listed newest-first as on the page (mathnet handle → landing URL `https://www.mathnet.ru/eng/<handle>` or `/rus/<handle>`).

| # | Year | Handle | Paper |
|---|------|--------|--------|
| 1 | 2022 | `mmo672` | On properties of limits of solutions in the noncommutative sigma model. *Tr. Mosk. Mat. Obs.* 83:2, 241–256. |
| 2 | 2019 | `tmf9700` | Description of solutions with uniton number 3 … Counterexample to the dimension conjecture. *TMF* 201:1, 3–16. |
| 3 | 2017 | `tm3807` | (with A. V. Domrin) On the dimension of solution spaces of a noncommutative sigma model, uniton number 2. *Trudy MIAN* 298, 112–126. |
| 4 | 2014 | `tmf8595` | Integer-valued characteristics of solutions of the noncommutative sigma model. *TMF* 178:3, 307–321. |
| 5 | 2012 | `tm3433` | Extended solutions in a noncommutative sigma model. *Trudy MIAN* 279, 72–80. |
| 6 | 2008 | `rm9219` | (with A. V. Domrin) On the divergence of the Kontsevich–Witten series. *Uspekhi Mat. Nauk* 63:4, 185–186. |
| 7 | 2006 | `tm83` | A restriction on the combinatorial structure of counterexamples to the Jacobian conjecture at infinity. *Trudy MIAN* 253, 61–66. |
| 8 | 2000 | **`im273`** | **Target.** On four-sheeted polynomial mappings of \(\mathbf C^2\). II. The general case. *Izv. RAN Ser. Mat.* 64:1, 3–36 / *Izv. Math.* 64:1, 1–33. |
| 9 | 1999 | `mzm1070` | Four-sheeted polynomial mappings in \(\mathbf C^2\). The general case. *Mat. Zametki* 65:3, 464–467 / *Math. Notes* 65:3, 386–389. |
| 10 | 1998 | `mzm1464` | (with S. Yu. Orevkov) On four-sheeted polynomial mappings of \(\mathbf C^2\). I. The case of an irreducible ramification curve. *Mat. Zametki* 64:6, 847–862. |
| 11 | 1996 | `mzm1910` | An example of a strictly pseudoconvex domain homeomorphic to the ball with a complex disk attached from the outside. *Mat. Zametki* 60:6, 919–924. |

Five talks are listed on the same page (`present34575`, `present19231`, `present12508`, `present5787`, `present3874`); they are not papers.

**1999 Mat. Zametki original, also fetched.** `getFT` for `mzm1070` → 193 837 bytes, 4 pages (journal 464–467). Saved as `refs/domrina1999_mzm1070_russian.pdf` (does **not** overwrite the charged English scan). First page (rendered): journal masthead «Математические заметки / том 65 выпуск 3 март 1999», «КРАТКИЕ СООБЩЕНИЯ», title «О ЧЕТЫРЕХЛИСТНЫХ ПОЛИНОМИАЛЬНЫХ ОТОБРАЖЕНИЯХ \(\mathbf C^2\). ОБЩИЙ СЛУЧАЙ», A. V. Domrina, the same N=4 theorem, and Proposition 1 (exactly two dicriticals, ramification orders 1 and 2, each meeting \(L_\infty\) once). Ghostscript 5.10, 2006-03-22. The charged English 1999 file `refs/domrina1999_mathnotes65_four_sheeted_general_case.pdf` (316 609 bytes) was left untouched.

## 5. URL log (every URL tried)

Mathnet: `/php/search.phtml?…AuthorLastName=Domrina` (ToU interstitial); `/eng/im273`; `/rus/im273`; `/php/getjrn.phtml?jrnid=im&paperid=273&option_lang=eng`; `/php/archive.phtml?wshow=paper&jrnid=im&paperid=273&option_lang=eng`; `/php/person.phtml?personid=8915` (eng+rus); `/eng/person8915`; `/rus/person8915`; `/php/agreement.phtml?option_lang=eng`; `/php/getFT.phtml?jrnid=im&paperid=273&what=fullteng&option_lang=eng`; `/php/getFT.phtml?jrnid=im&paperid=273&what=fullt&option_lang=rus`; `/links/b922de90ce37fddd3006ce99aa090fe7/im273_eng.pdf` (assembled); `/links/74bb10397ee10cca756024612b0ce068/im273_eng.pdf` (HEAD token); `/links/66ff62d24ff50e434e64e0adde1eef5e/im273.pdf` (HEAD token); `/links/f6eeff53f09c98c03fb54b4c9ec61a56/im273.pdf` (assembled Russian); `http://www.mathnet.ru/links/…/im273_eng.pdf` (connection reset); `http://mi.mathnet.ru/im273` (redirect); `/eng/mzm1070`; `/php/getFT.phtml?jrnid=mzm&paperid=1070&what=fullt&option_lang=rus`; `/links/83719d40a09d3c6f9273be77270463ae/mzm1070.pdf`.

DOI/Crossref: `https://doi.org/10.1070/IM2000v064n01ABEH000273`; `https://doi.org/10.4213/im273`; `https://api.crossref.org/works/10.1070/IM2000v064n01ABEH000273`.

IOP/Turpion: `https://iopscience.iop.org/article/10.1070/IM2000v064n01ABEH000273`; same `/pdf` (Radware 302); `https://iopscience.iop.org/issue/1064-5632/64/1`; `https://www.turpion.org/php/paper.phtml?journal_id=im&paper_id=273` (fail); `http://www.turpion.org/php/paper.phtml?journal_id=im&paper_id=273` (timeout).

Indexes/repos: OpenAlex `https://api.openalex.org/works/https://doi.org/10.1070/IM2000v064n01ABEH000273`; Semantic Scholar graph DOI query; Unpaywall v2 (422); zbMATH `an:0962.14038`; Wayback CDX for mathnet `*im273*` and the IOP article (429); CyberLeninka search and guessed article slug (404); ISTINA worker `2701793/all` and guessed publication 404; Orevkov homepage; fizmathim dissertation page.

Shadow-library URLs for this DOI were not requested.

## 6. Files, hashes, and first-page verification

```text
0be24c5c6a9cc9423c3049c3402f2c98e44bac5f1c6018b3999989e0f32e5018  refs/domrina2000_izv64_four_sheeted_general_case.pdf
     408814 bytes, 33 pp, PDF 1.3, Distiller 3.0 (2000-05-30). English Turpion.
     First page: Domrina title + DOI 10.1070/IM2000v064n01ABEH000273. ACCEPT.
     qpdf: no syntax/stream errors.

a78e61decc1b4b005a63471bff9b954cad83ff7520ed7e295f8e022dd6d55029  refs/domrina2000_im273_russian.pdf
     2871464 bytes, 34 pp, PDF 1.2, ABBYY (2007). Russian original.
     First page: «О четырехлистных полиномиальных отображениях C^2. II. Общий случай». ACCEPT.
     qpdf: linearized-hint warnings only (page 33 shared-object list).

98b9414294980cc174101776f703073a30d82deeed2669ee339698a1bb808975  refs/domrina1999_mzm1070_russian.pdf
     193837 bytes, 4 pp. 1999 Mat. Zametki original (author-page obligation, not the 2000 target).
     First page: «О ЧЕТЫРЕХЛИСТНЫХ … ОБЩИЙ СЛУЧАЙ», Prop. 1 two-dicritical. ACCEPT.
     Did not touch refs/domrina1999_mathnotes65_four_sheeted_general_case.pdf.
```

SHA-256 via `shasum -a 256` after assembly. Range tokens are session cookies, not hashes.

## 7. Verdict

**CLOSED.** Genuine Izvestiya II bytes are in hand from mathnet.ru, page-verified against the Ni3Al reject rule.

- Primary Russian original: `refs/domrina2000_im273_russian.pdf` (`a78e61de…`).
- Official English translation (Turpion typesetting, same mathnet paperid `im273`): `refs/domrina2000_izv64_four_sheeted_general_case.pdf` (`0be24c5c…`).

IOP/Turpion PDFs were not obtained (paywall + bot challenge / timeout). No citing repository hosted a second copy of the translation. The 1999 short note’s Russian original was fetched as part of the author-page obligation. No `charge_basis` line: this lane delivers custody, not an exit price.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14743`.
- Body SHA-256:
  `82358e7c38e59a6d8a018745d417ef31954c5b1d4b60f6d0bd2b58ec3485cceb`.
- Frozen basis: `33d570703724abe1bb1f7fba4ca87e5b83cfbc1d`.
