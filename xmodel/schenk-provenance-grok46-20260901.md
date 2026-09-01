# SCHENK-PROVENANCE — Zenodo 18622130 (Schenk JC2 claim)

Lane: bounded provenance scout. Target: Zenodo record 18622130, posted
2026-02-12. Scope: author identity, discussion, version history, arXiv
status, professional engagement. Not a mathematical audit.

Charged inputs (SHA-256 verified 2026-09-01, match the launch hashes):

- `6ba4088386eb40affbb4abad54bb8e1574de09d00da9d1fbeac9f5c88d160f24` `inputs/schenk_jc2_zenodo18622130.pdf`
- `23fab48635178dd905d67be2b9d0eeb8574b641be0d097c82af4a55bf4fcc7d4` `inputs/web-sweep-20260901-grok46.md`
- `763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9` `inputs/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md`

Fetch hashes below are SHA-256 of the retrieved bytes at the stated URL
and fetch time, unless marked `OPEN`.

## 0. Registry and method

Lane scope is provenance only: who posted Zenodo 18622130, what else they have posted, whether the record was revised, whether it appears on arXiv, and whether any named mathematician or reviewing service has engaged the JC2 claim in the ~6.5 months since 2026-02-12. This is not a mathematical audit. Parallel hostile-text lanes own soundness.

Charged-input SHA-256 values were recomputed this session and match the launch hashes. The PDF is 53 pages, 569113 bytes, pdfTeX-1.40.27, CreationDate `Thu Feb 12 09:38:47 2026 PST`. Its MD5 is `6286a51fdd7768502208655de23a1f71`, matching the Zenodo file checksum.

Method, all desk-scale, no CAS, no `jc2-lean`, no canonical-ledger edits:

- Zenodo REST: record, versions, creator search, owner search (`owners:1484150`).
- arXiv API (`au:"Philipp Schenk"`, `au:Schenk_Philipp`, `all:"valuation-theoretic proof of the Jacobian"`, `all:PhilippSchenk6`, `all:18622130`) plus the HTML author search.
- MathOverflow and Math Stack Exchange 2.3 API; the `[jacobian-conjecture]` tag; question 513413 and its answers.
- zbMATH Open API (positive control: Keller 1939 is indexed; `au:schenk.philipp` is not).
- DataCite, OpenAlex, Crossref, ORCID public search, HAL.
- Wikipedia Jacobian conjecture and MathWorld Jacobian Conjecture snapshots.
- X keyword search (`"Philipp Schenk" Jacobian OR Zenodo OR Hodge OR "18622130"`); Semantic Scholar DOI lookup.
- PDF text via `pdftotext` for title-page identity, acknowledgements, and bibliography only.

Fetch hashes of retrieved bytes are in §8. Search snippets are not evidence. A negative API result is evidence of absence *from that index at fetch time*, not a proof that a private referee report does not exist. arXiv does not publish rejections; “not listed” is not “rejected.”

Window: 2026-02-12 through 2026-09-01. Status pages used as community thermometers (Wikipedia last-edited 2026-08-28, MathWorld snapshot 2026-08-28) still treat characteristic-zero JC2 as open. The charged web-sweep (`xmodel/web-sweep-20260901-grok46.md`) registered this record as F8, a scoop-claim of the whole plane problem, not a threat to THEOREM 7.B, and recorded that campaign greps of `Schenk` / `18622130` had been empty.

## 1. Record identity (Zenodo 18622130)

Canonical landing: `https://zenodo.org/records/18622130` (HTML SHA-256 `313564c5cf7705ce3855e4728bef44c52b39c2140b8ef99d648cd561975e873a`, fetched 2026-09-01). API: `https://zenodo.org/api/records/18622130` (JSON SHA-256 `3b0618737000589f378d5cd6eef773c013fefb267519aefdd8fa90d023038006`).

| field | value | source |
|---|---|---|
| title | A Valuation–Theoretic Proof of the Jacobian Conjecture in Dimension Two | API `metadata.title`; PDF title page |
| creator | Schenk, Philipp; affiliation `null` | API `metadata.creators` |
| contact on PDF | `PhilippSchenk6@web.de` | PDF p.1 (`pdftotext`) |
| version label | v1 (landing); API `version` is `None`; relations index 0, `is_last` true | landing HTML; API `relations.version` |
| DOI / concept DOI | `10.5281/zenodo.18622130` / `10.5281/zenodo.18622129` | API |
| created / published | 2026-02-12T14:11:39.800441+00:00 / 2026-02-12 | API |
| last modified | 2026-02-13T16:35:37.830816+00:00; `revision` 17 | API |
| file | `Jacobi in N=2.pdf`, 569113 bytes, `md5:6286a51fdd7768502208655de23a1f71` | API `files` |
| license | CC-BY-4.0 | API |
| related identifiers | none (no arXiv, no journal, no ORCID) | API `related_identifiers` |
| resource type | Publication / Text | API; DataCite `resourceTypeGeneral: Text` |
| owner | Zenodo user id `1484150` | API `owners` |
| stats at fetch | views 98 / unique 58; downloads 363 / unique 327 | API `stats` |

Theorem 1.1 on PDF p.1 claims: over an algebraically closed field of characteristic 0, every polynomial morphism \(F=(P,Q):\mathbb{A}^2\to\mathbb{A}^2\) with \(\det DF\in k^\times\) is an automorphism. The historical paragraph still says the conjecture “remains open in dimension \(\ge 2\)” (true on 2026-02-12; Alpöge’s \(n\ge 3\) counterexample is 2026-07-19). Strategy, as advertised: normalize the projective graph, Stein-factor, kill horizontal boundary (U-HIT), Rees-degenerate affine dicriticals, force positivity of the Jacobian two-form, contradict the Keller identity, then invoke triviality of finite étale covers of \(\mathbb{A}^2\) and Zariski’s Main Theorem.

Bibliography (PDF pp. 48–49) is 17 items: Keller 1939, Bass–Connell–Wright 1982, van den Essen 2000, plus textbooks (Hartshorne, Eisenbud, Matsumura, EGA/SGA, Milne, Shafarevich, Zariski–Samuel, Stacks 2024). Entries [11] and [12] are the same Matsumura 1989 title twice. There is no Moh, Abhyankar–Moh, Kaliman–Koras, Miyanishi, or post-2000 research article. No acknowledgements, no institutional address, no ORCID on the PDF or the record.

DataCite (`https://api.datacite.org/dois/10.5281/zenodo.18622130`, SHA-256 `c1202043821bf4220527804e5c9bae3696fac392e96ee4ff2cb5a7beac4d6659`): `citationCount` 0, `relatedIdentifiers` only `IsVersionOf` 10.5281/zenodo.18622129, creators have empty `affiliation` and empty `nameIdentifiers`. Crossref `GET /works/10.5281/zenodo.18622130` returned the literal body `Resource not found.` OpenAlex indexes the DOI as `W7128733671` with `cited_by_count` 0 and empty institutions (`https://api.openalex.org/works/https://doi.org/10.5281/zenodo.18622130`, SHA-256 `3c1d44a4b0a68908ec01a0f0e72edd0d44cf5cd7e2d18b2754b411571ee8dafc`). Semantic Scholar returned `Paper with id DOI:10.5281/zenodo.18622130 not found` (SHA-256 `d3429e832f360774941f2580042e14d4411670d6d458f297fa3b6e872a9f2071`).

## 2. Author identity and track record

**On-record identity.** The only identifiers attached to the JC2 claim are the name `Schenk, Philipp`, the consumer address `PhilippSchenk6@web.de` (WEB.DE Freemail, 1&1 Mail & Media, Germany), and Zenodo owner `1484150`. Affiliation is `null` on every record this owner published. No ORCID, no institutional email, no MathSciNet/zbMATH author code, no arXiv author identifier.

**Homonyms, not identified with this depositor.** ORCID public expanded-search for given-names Philipp AND family-name Schenk returned four people (XML SHA-256 `37ecd7fa624ac41d211d965f8bdfa358e206f8d3b0415a61070a2add21183f24`): `0000-0002-3610-2469` (no institution in the payload); `0000-0001-6044-1068` (BioNTech / TU Dresden / TUM / WEHI / iOmx — the ubiquitin-signalling PhD, not algebraic geometry); `0009-0002-6879-2211` Daniel Philipp Schenk, Universität der Bundeswehr München; `0009-0008-0882-7252` Lukas Philipp Schenk, University of Tübingen. Google Scholar’s first Philipp Schenk hit is a biomechanics employee at BG Klinikum Bergmannstrost Halle. None of these profiles lists the Zenodo JC2 paper, and the Zenodo record carries no ORCID that would bind it to them. They are listed so they are not silently merged.

**Same-owner corpus (identity lock).** Zenodo `q=creators.name:"Schenk, Philipp"` and `q=owners:1484150` both return the same 18 records, all owner `1484150`, all affiliation `null` (search JSON SHA-256 `1059d3a8b7cc8b65ed08e67964f9dbced4a6273c5200a537b49fa84869afdd44` and `a1ea25b6f1fce069531374bbea2bebc9bc39e56084779b1f1c4c5d661b197bc0`). Chronological:

| date | id | title (short) | claim type |
|---|---|---|---|
| 2025-12-07 | 17848952 (3 versions) | UDML — Universal Deterministic Machine Language | new machine model |
| 2025-12-07 | 17849844 | UDML / functional intentionality in non-Turing machines | same programme |
| 2025-12-07 | 17849988 | L-OPS | protocol language |
| 2025-12-08 | 17850374 | Die Nicht-Turing-Maschine | same programme |
| 2025-12-14 | 17931062 | Deterministic governance of probabilistic AI | framework |
| 2025-12-16 | 17957291 | Prägeometrisches Substrat-Framework, QFT and gravity | unification framework |
| 2025-12-17 | 17957750 | Formwahl und formaler Zwang in fundamentalen mathematischen Problemen | methodology; explicitly “erhebt keinen Anspruch auf eine Lösung” of P vs NP or RH |
| 2025-12-17–26 | 17968094, 17969993, 17991860, 18007613, 18007659, 18007688, 18027205, 18064315 | SAT / P vs NP structural programme | mostly “does not claim a proof”; 18064315 is “Routes to P ≠ NP”, conditional on a normalization hypothesis |
| 2025-12-27 | 18069657 | The Hodge Conjecture as an Operator Rigidity Problem | reformulation + no-go: “no purely formal operator framework can force universal extension vanishing” |
| **2026-02-12** | **18622130** | **JC2 valuation-theoretic proof** | **unconditional complete-proof claim (Thm 1.1)** |
| 2026-08-12 | 21909284 (3 versions) | Das Instrumental | philosophy/sociology book |

The JC2 record is this depositor’s only unconditional complete-proof claim of a classical conjecture. Hodge is framed as a rigidity/no-go analysis, not a proof of Hodge. The P vs NP series, in the collection abstracts, refuses an unconditional separation (18007613: “The collection does not claim a proof of P ≠ NP”). That is a different speech-act from Theorem 1.1.

**Track record in the professional literature.** zbMATH Open API `document/_search?search_string=au:schenk.philipp` returned 404 / “No results found” (SHA-256 `a83ad54f488cf3bc317981ec0cedc273c5b0cdb8f7fca4310d15f2fef724e4b0`). The same API finds Keller 1939 as a positive control (`search_string=keller ganze cremona`, SHA-256 `63fc0ba09e3c469d6ad8af44f199dee094c3de9231eb4861ee0be07c47c1ae55`). arXiv HTML: “Sorry, your query for author: Schenk, Philipp produced no results” (`https://arxiv.org/search/?searchtype=author&query=Schenk%2C+Philipp`, SHA-256 `7c3771e35e24bd777021e5561fb4e1932f6a43309718551f54905e08472b6339`). arXiv API author and title-phrase queries: `totalResults` 0. HAL: `numFound` 0. MathOverflow `inname=Philipp Schenk`: empty user list. No zbMATH/MathSciNet author page was located for this depositor as an algebraic geometer.

**Prior claims on major conjectures, typed.** The owner spent 20 December-days (2025-12-07 to 2025-12-27) depositing machine-model, QFT–gravity, SAT/P vs NP, and Hodge manuscripts, then deposited an unconditional JC2 proof 47 days later. That is a documented pattern of unaffiliated, rapid, multi-front writing on major open problems. It is not a published research record in affine algebraic geometry. It is not, by itself, a refutation of Theorem 1.1.

## 3. Version history on Zenodo

`GET https://zenodo.org/api/records/18622130/versions` returns `hits.total = 1` (JSON SHA-256 `5414a5f54ba7b4eb8369fcb12ef1bfd472da17af840e9c568fdd9bfcbc28536d`). The single hit is record 18622130 itself, file `Jacobi in N=2.pdf` with the same MD5 as the charged PDF. The landing page labels it “Version v1”. DataCite `version` is `null`; `relationships.versions.data` is empty; the only related DOI is the concept parent 18622129 via `IsVersionOf` / `versionOf`.

There is therefore no v2, no replacement PDF, and no erratum record. The charged SHA-256 is the published bytes.

What did change: `revision` 17 and `updated` 2026-02-13T16:35:37Z, about 26 hours after `created`. Zenodo increments `revision` on metadata edits without minting a new version. The file checksum did not change, so those revisions are metadata (keywords include MSC 14R15, 14E05, 13A18, 14B25 and a long keyword list). DataCite’s `updated` timestamp is earlier, 2026-02-12T17:39:17Z, consistent with metadata continuing to move after the DOI registration snapshot.

This owner *does* version other deposits when they rewrite: UDML 17848952 has three versions (17842600 on 2025-12-06, 17848612 on 2025-12-07, 17848952 on 2025-12-07; versions JSON SHA-256 `6be6264793658720fabe92f55c471d31afe9394d7738d25fe180e36b90784209`). `Das Instrumental` 21909284 is version index 2. The JC2 record’s lack of a new version is therefore a choice, not a platform limitation: no corrected text has been posted in 6.5 months.

## 4. arXiv status (submission, rejection, withdrawal)

**Public listing: none.**

| query | endpoint | `totalResults` | fetch SHA-256 |
|---|---|---|---|
| `au:"Philipp Schenk"` | arXiv API | 0 | `a4c16c092791034aa1bb795030f5d9c16834c0b96ac32dd1ac41bf92377e44a0` |
| `au:Schenk_Philipp` (normalized to `au:"Schenk Philipp"`) | arXiv API | 0 | `eed6b203539ae067d3d6305eaa82ff07af93b3430c3a708e2dd053ab134dfc1d` |
| `all:"valuation-theoretic proof of the Jacobian"` | arXiv API | 0 | `ca91c7b6f7d00c32162f6d4aa7a005e3aa0ee7232c2c3301b65c68e0712afc51` |
| `all:PhilippSchenk6` | arXiv API | 0 | `0e13da8392a0eccaf790d5852461863c092cc05c4c6fceb611d2bbc6a07555a4` |
| `all:18622130` | arXiv API | 0 | `d894a6c3078c6879494a1391bac2ac687c9785a9d09ab107484a033bb9058af6` |
| author HTML `Schenk, Philipp` | `arxiv.org/search/?searchtype=author&query=Schenk%2C+Philipp` | page text: “Sorry, your query for author: Schenk, Philipp produced no results.” | `7c3771e35e24bd777021e5561fb4e1932f6a43309718551f54905e08472b6339` |

The Zenodo record has empty `related_identifiers`, so it does not point at an arXiv id. No withdrawn (`withdrawn`) paper under this name was found because no paper under this name was found at all. Trackbacks cannot exist for a DOI that was never an arXiv listing.

**Rejection is not observable.** arXiv moderation does not publish a rejection ledger. The public facts are: no listing, no withdrawal stamp, no arXiv-id in DataCite/Zenodo. Those facts are compatible with never-submitted, with submitted-and-rejected, and with submitted-and-still-in-moderation-for-an-implausibly-long-time. Type the rejection question `OPEN`. Do not upgrade “not on arXiv” to “arXiv rejected it.”

A different, older “valuation-theoretic” JC programme exists on arXiv under Susumu Oda (e.g. `math/0706.1138`, `1203.1691`); that is a distinct author and is not this deposit.

## 5. Discussion sweep (MO, arXiv trackbacks, blogs, reviews, social)

Positive hits naming this preprint, outside Zenodo/OpenAlex’s automatic DOI ingest and this campaign’s own files: **none found**.

**MathOverflow.** Advanced search `Philipp Schenk Jacobian` and `18622130 OR zenodo Schenk`: `items: []` (SHA-256 `d71ca66bb2860128b1667d0e0911a4824162c630a2112d0fdf6ebac4e21108fa`). The `[jacobian-conjecture]` tag (20 most recently active questions, SHA-256 `0bad6899f4c4de937f48b1bd5c1a56ff8cc979eba2ff90cd14ae0ba5dbf447ac`) is dominated by post-Alpöge traffic from July 2026. None of those titles or the sampled bodies contain `Schenk` or `18622130`.

The highest-visibility plane-case thread after Alpöge is question 513413, “The simplest case of Jacobian conjecture” (asked 2026-07-21, score 49, 4 answers; question SHA-256 `70246a08e7afd748a52145ee874460d5a4820e463c60bc136ed3ede9d5c2fba0`; answers SHA-256 `4f064aba09c941f2769b6d7e08cb972f0fc2b54ca128be0ed7e4971d7988377c`). The question states that JC is false for \(n\ge 3\) and asks whether there are reasons the two-variable case could still be true. Answers: KConrad (score 56), Alexandre Eremenko (53), Claudio Procesi (20), ratto3423 (14). None of the four answer bodies contains `schenk` or `zenodo`. This is a named-professional conversation about JC2 remaining open, held five months after the Zenodo posting, that does not mention the posting.

**Math Stack Exchange.** Same query: `items: []` (SHA-256 `fb9e9b89b80d61ae519afc6a8ed2ec3ada7f97e0b3507dad9b5e87c96bfcd893`).

**Status pages.** Wikipedia *Jacobian conjecture*, last edited 2026-08-28T14:47:56Z (HTML SHA-256 `bb3141f765691d516124c10b6c3f031bc22fb98c713fd6dc273ca65aef5efee1`): “the only case that remains unresolved as of 2026” is \(n=2\); string counts `Schenk` = 0, `18622130` absent, `zenodo` absent. MathWorld *Jacobian Conjecture* (HTML SHA-256 `a10706c747b5c04c7eef43ff436cc7be4cfff3c0700ff16c3c731366c091f01e`): “the plane case remains open”; `Schenk` = 0. Both pages discuss Alpöge 2026 and do not discuss Schenk.

**Reviews.** zbMATH Open API: no document for `au:schenk.philipp` (§2). zbMATH HTML search was Cloudflare-intercepted (`Just a moment...`; SHA-256 `3f79b56540009746726b4677d97f932c77d337b53f97a1854777a1fd4e68627d`) — the API 404 is the usable negative. MathSciNet was not successfully fetched (paywall; typed OPEN in §9). DataCite `citationCount` 0; OpenAlex `cited_by_count` 0 and `filter=cites:W7128733671` returns `count: 0` (SHA-256 `e89b8b92dacafb30279cf6bcdc7a49d2e17a75850b536aaf72f17bfd01614cba`). Semantic Scholar: DOI not found.

**Blogs / social.** X keyword search for `"Philipp Schenk" Jacobian OR Zenodo OR Hodge OR "18622130"` and `"valuation-theoretic" Jacobian Schenk`: no results. Semantic X search for the preprint returned only Alpöge/Fable JC\(_{\ge 3}\) posts, not Schenk. Web search for the exact title and for `10.5281/zenodo.18622130` returns the Zenodo record and its PDF, not a third-party discussion. Targeted blog-domain search (`golem.ph.utexas.edu`, `gowers.wordpress.com`, `sbseminar.wordpress.com`, `math.columbia.edu/woit`) returned no Schenk hit. HAL `numFound` 0.

**Professional papers that treat JC2 as open after 2026-02-12**, without citing Schenk (non-engagement, not a review): Shaska arXiv:2607.20210 (2026-07-22/25) proves every *graded* plane Keller map is an automorphism and treats the ungraded plane case as remaining; Jelonek arXiv:2607.20597 (2026-07-22); Wikipedia/MathWorld as above; Bisi–et al. *Random planar trees and the Jacobian conjecture*, J. London Math. Soc. (first published 2026-01-22, DOI 10.1112/jlms.70416) still calls JC “one of the outstanding open problems” ten days after the Zenodo deposit — too early to count as a snub, recorded only as a date check.

**Download counts are not discussion.** 327 unique downloads against 58 unique views is compatible with harvesters, DOI resolvers, and this campaign’s own fetches. It is not a named engagement.

The charged web-sweep independently recorded the same absence: campaign greps empty, no prior discussion found, F8 registered as a scoop-claim to audit.

## 6. Professional engagement

**Named mathematicians engaging this preprint: none found.**

What was found instead is named mathematicians engaging the *plane Jacobian conjecture* after 2026-07-19 without this preprint entering the conversation:

- KConrad, Alexandre Eremenko, and Claudio Procesi, answering MathOverflow 513413 on 2026-07-21 and after, on whether JC2 could still be true. Bodies contain no Schenk/Zenodo string (§5).
- Levent Alpöge’s 2026-07-19 announcement of the \(n=3\) counterexample (X post 2079028340955197566 and the Wikipedia/MathWorld writeups) does not mention a February Zenodo JC2 proof.
- T. Shaska, arXiv:2607.20210v2, 2026-07-25, writes a graded-Keller paper whose dim-2 theorem would be implied by a true JC2 proof and does not cite Schenk.
- Wikipedia editors, through 2026-08-28, and MathWorld, through the 2026-08-28 snapshot, still mark JC2 open and do not list Schenk among attempted proofs (MathWorld does list “at least five published incorrect proofs”).

No zbMATH review, no MathSciNet review located, no MO question or answer, no arXiv trackback, no OpenAlex citation, no DataCite citation, no Semantic Scholar record, no ORCID-linked publication, no HAL record, no X post by a research mathematician naming the deposit.

Owner 1484150’s other 17 deposits likewise show no professional reviews in this sweep; they are context for identity, not additional JC2 engagement.

Type: **zero located professional engagement with Zenodo 18622130 as of 2026-09-01.** Private emails and unindexed seminar remarks are invisible; that invisibility is recorded as a coverage gap in §9, not as a hidden positive.

## 7. Bayesian typing (not a mathematical verdict)

Facts used, all sourced above:

1. Unaffiliated depositor, consumer email, no zbMATH/arXiv/ORCID research identity in algebraic geometry.
2. Same owner deposited, from 2025-12-07 through 2025-12-27, a burst of unaffiliated manuscripts on machine models, QFT–gravity, SAT/P vs NP, and Hodge; the JC2 proof followed on 2026-02-12; a philosophy book followed on 2026-08-12. JC2 is the only complete-proof claim of a classical conjecture in that corpus.
3. The JC2 text cites Keller, Bass–Connell–Wright, van den Essen 2000, and textbooks; it does not cite the specialist plane-JC literature. No acknowledgements. Duplicate bibliography entries. Single version, no correction in 6.5 months.
4. Not on arXiv; rejection unobservable.
5. Zero located citations, reviews, MO/MSE threads, blog posts, or X posts naming the preprint. Named professionals (KConrad, Eremenko, Procesi, Shaska, Wikipedia/MathWorld editors, Alpöge) discussed JC2 as open after the deposit without citing it.
6. Status pages on 2026-08-28 still mark characteristic-zero JC2 open.

**Typing.** A six-month-old complete-proof claim of a century-old conjecture, posted off-arXiv by an author with no algebraic-geometry publication record and a December 2025 burst of writing on other major open problems, that has attracted no located professional engagement, is **weak Bayesian evidence against soundness**. It is the same kind of prior one applies to the long list of unaffiliated JC2 manuscripts (MathWorld’s “at least five published incorrect proofs”; Oda’s valuation series; the 2026 Matysiak SSRN pair already audited unsound in this campaign). The prior is about *base rate and visibility*, not about a lemma.

**It is not a mathematical verdict.** Silence does not exhibit a gap in U-HIT, Rees degeneration, wedge strictness, or the étale-cover step. A correct proof can sit unread on Zenodo; an incorrect proof can be ignored for the same reason. The right action, already named by the charged web-sweep, is a hostile primary-text audit, not a provenance-based close. If that audit finds a break, provenance was only the routing signal. If it does not, the zero-engagement prior is overridden by the text.

## 8. Source table

All fetches 2026-09-01 unless noted. SHA-256 of retrieved bytes.

| id | URL | SHA-256 |
|---|---|---|
| charged PDF | frozen `inputs/schenk_jc2_zenodo18622130.pdf` | `6ba4088386eb40affbb4abad54bb8e1574de09d00da9d1fbeac9f5c88d160f24` (MD5 `6286a51fdd7768502208655de23a1f71`) |
| charged sweep | frozen `inputs/web-sweep-20260901-grok46.md` | `23fab48635178dd905d67be2b9d0eeb8574b641be0d097c82af4a55bf4fcc7d4` |
| charged integration | frozen `inputs/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md` | `763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9` |
| Zenodo API record | https://zenodo.org/api/records/18622130 | `3b0618737000589f378d5cd6eef773c013fefb267519aefdd8fa90d023038006` |
| Zenodo versions | https://zenodo.org/api/records/18622130/versions | `5414a5f54ba7b4eb8369fcb12ef1bfd472da17af840e9c568fdd9bfcbc28536d` |
| Zenodo landing | https://zenodo.org/records/18622130 | `313564c5cf7705ce3855e4728bef44c52b39c2140b8ef99d648cd561975e873a` |
| Zenodo creator search | `q=creators.name:"Schenk, Philipp"` size=25 | `1059d3a8b7cc8b65ed08e67964f9dbced4a6273c5200a537b49fa84869afdd44` |
| Zenodo owner search | `q=owners:1484150` size=25 | `a1ea25b6f1fce069531374bbea2bebc9bc39e56084779b1f1c4c5d661b197bc0` |
| DataCite DOI | https://api.datacite.org/dois/10.5281/zenodo.18622130 | `c1202043821bf4220527804e5c9bae3696fac392e96ee4ff2cb5a7beac4d6659` |
| OpenAlex work | https://api.openalex.org/works/https://doi.org/10.5281/zenodo.18622130 | `3c1d44a4b0a68908ec01a0f0e72edd0d44cf5cd7e2d18b2754b411571ee8dafc` |
| OpenAlex cites | `filter=cites:W7128733671` | `e89b8b92dacafb30279cf6bcdc7a49d2e17a75850b536aaf72f17bfd01614cba` |
| ORCID search | https://pub.orcid.org/v3.0/expanded-search/?q=given-names:Philipp AND family-name:Schenk | `37ecd7fa624ac41d211d965f8bdfa358e206f8d3b0415a61070a2add21183f24` |
| arXiv API / HTML | five API queries + author HTML (§4) | listed in §4 |
| zbMATH API author | `au:schenk.philipp` | `a83ad54f488cf3bc317981ec0cedc273c5b0cdb8f7fca4310d15f2fef724e4b0` |
| zbMATH API control | `keller ganze cremona` | `63fc0ba09e3c469d6ad8af44f199dee094c3de9231eb4861ee0be07c47c1ae55` |
| MO Schenk/18622130 | API advanced search | `d71ca66bb2860128b1667d0e0911a4824162c630a2112d0fdf6ebac4e21108fa` |
| MO tag jacobian-conjecture | API questions tagged | `0bad6899f4c4de937f48b1bd5c1a56ff8cc979eba2ff90cd14ae0ba5dbf447ac` |
| MO Q513413 | https://api.stackexchange.com/2.3/questions/513413 | `70246a08e7afd748a52145ee874460d5a4820e463c60bc136ed3ede9d5c2fba0` |
| MO Q513413 answers | API answers | `4f064aba09c941f2769b6d7e08cb972f0fc2b54ca128be0ed7e4971d7988377c` |
| MO user inname | `inname=Philipp Schenk` | `a18f977821bb65a5951759ce6ee9ca6f850dc3f24a2ffb9bc0d33e27e1f59e9b` |
| MSE search | Philipp Schenk Jacobian | `fb9e9b89b80d61ae519afc6a8ed2ec3ada7f97e0b3507dad9b5e87c96bfcd893` |
| Wikipedia JC | https://en.wikipedia.org/wiki/Jacobian_conjecture | `bb3141f765691d516124c10b6c3f031bc22fb98c713fd6dc273ca65aef5efee1` |
| MathWorld JC | https://mathworld.wolfram.com/JacobianConjecture.html | `a10706c747b5c04c7eef43ff436cc7be4cfff3c0700ff16c3c731366c091f01e` |
| HAL | `q="Philipp Schenk" AND Jacobian` | `316b596864c92e18c8f6688107ad49ecfc3fe632ebdc85efe82c65ed28ba8064` |
| Semantic Scholar DOI | DOI:10.5281/zenodo.18622130 | `d3429e832f360774941f2580042e14d4411670d6d458f297fa3b6e872a9f2071` |
| Crossref | https://api.crossref.org/works/10.5281/zenodo.18622130 | `ae8462e3af85ca7577aaa97ff22a194f9dfd7fada58cf4944b53d2fdfa7b1f92` (body: `Resource not found.`) |

Sibling Zenodo JSON for owner 1484150 is in `/tmp/jc2-schenk-prov-20260901/zenodo-*.json`; identities and dates in §2 are taken from those payloads. X searches returned no posts (tool-level empty, no byte hash).

## 9. OPEN items

- **arXiv rejection vs never-submitted.** Not observable from public indexes (§4). Typed OPEN.
- **MathSciNet review.** No successful fetch (subscriber wall). zbMATH Open API is the substitute negative.
- **zbMATH HTML.** Cloudflare interstitial; API 404 used instead. A human browser session could still differ; typed residual OPEN on HTML confirmation only.
- **SSRN HTML search.** Cloudflare interstitial. Web phrase-search did not surface an SSRN copy. Residual OPEN.
- **viXra.** Search URLs used here 404’d. No positive viXra hit from web search. Residual OPEN on interface, not a positive listing.
- **Semantic Scholar keyword search.** DOI lookup was a clean “not found”; the `/paper/search` route 429’d. Residual OPEN on the search route only.
- **Google Scholar.** No dedicated Scholar API fetch this session; web search did not return a Scholar card for the DOI. Residual OPEN.
- **Private correspondence, referee reports, seminar talks.** Invisible by construction.
- **Homonym lock.** Identity is locked to Zenodo owner `1484150` plus `PhilippSchenk6@web.de`. It is not locked to a passport or to any of the four ORCID Philipp Schenks. Do not merge with the WEHI/BioNTech or Bergmannstrost homonyms.
- **Download semantics.** 327 unique downloads unexplained; not promoted to “readers.”
- **Mathematical soundness.** Out of scope. Hostile primary-text audit remains the charged next action from the web-sweep coordinator note.

**Coordinator-facing summary.** Author: unaffiliated Philipp Schenk, owner 1484150, 18 Zenodo records Dec 2025–Aug 2026, JC2 the only unconditional complete-proof claim. Version: v1 only, PDF unchanged, metadata revision 17 on 2026-02-13. arXiv: not listed; rejection OPEN. Discussion: none located. Professional engagement: none located; KConrad/Eremenko/Procesi treated JC2 as open on 2026-07-21 without citing it. Bayesian type: weak evidence against soundness, not a verdict. Do not withdraw 7.B on this record. Route the text to the parallel audit lanes.

<!-- BODY-END -->

