# Frozen public source index

## Coverage comparison and limitations

arXiv exact phrase feed:220total/30returned, unchanged query and count; newest returned exact-phrase item remains BGV. Related OR feed:46total/30returned versus45 previously, with new Zhang listing. These are search-index counts, not counts of new theorems. math.AG/math.AC/math.CV announcement pages were screened; Zhang appears in AC. No date-only discovery restriction.

GitHub query `jacobian-conjecture`, updated descending,100cap:79total/78retained after protected filtering, same query/count as prior. Ten exact watched commit endpoints,3commits each, additionally checked; only Roy and KellerMap heads are newer in that watched set. Eight unchanged heads predate cutoff. Ruellee repository push did not yield exact jacobian-path commits. Catalog comparisons are scoped metadata, not proof-code validation.

Zenodo recovered HTTP200:126total/25returned with whole returned record metadata retained; list ordering is not treated as an exhaustive chronological stream. Exact Atwell22551146/rank22168498 endpoints also recovered; both unchanged September6. DataCite25latest returned metadata, newest BGV creation September9 04:31:45, before prior cutoff. No full-pagination absence claim; old larger Zenodo coverage debt is not erased by three successful requests.

Palomar recent catalog:198retained after protected filtering; six entries created after previous cutoff, unrelated titles. Subject14R15 summary says6versions; year file6days/newestAugust29. Whole returned metadata, not six theorem bodies. Protected entries were removed before display; protected project never opened.

MO/MathSE:30returned records each; latest relevant-query activity timestamps August22/August4, before cutoff. Broad unquoted search includes noise; finite response is weak absence evidence only.

Mathstodon tags:10 `jacobian` and7 `jacobianconjecture` posts, latestAugust7/August16. Tao bounded account40posts:four after cutoff, about fluid mechanics and mathematical/AI exploration; none supplies a JC2 result. This is actual bounded actor coverage, not global Mastodon coverage. New BGV Reddit discussion was read only as the returned rendered page; no claim all comments were fetched.

Persistent holes: X HTTP200 shell, no actual search tweet data established; Bluesky403; Zulip authenticated API401 and proposed public archive404. GLOBAL X/Bluesky/Zulip debt remains September3 10:17 UTC. No login, account action, alternative protected route, or retry farm. JTPMath primary manuscript access is recovered, but unrelated membership content remains unread.

## Undated/concept search log

Four batches, four queries each, response_length=long. Batches2/4 displayed clipped results; only recovered primary sources support technical observations. No search-only absence claim.

1. "Jacobian conjecture" proof counterexample September 2026
2. "Keller maps" nonproperness Newton polynomial 2026
3. "Mathieu conjecture" moments counterexample 2026
4. "Poisson conjecture" "Jacobian" 2026 symplectic
5. "Jacobian conjecture" "September 10" 2026 -site:reddit.com -site:jc2-lean
6. "Keller maps" "holonomic"
7. "Jacobian conjecture" Guccione Valqui Furter Moskowicz 2026
8. "Jacobian conjecture" "proof" "2026" nonproperness compactification degree
9. "Jacobian conjecture" "September 2026" proof correction -site:reddit.com -site:jc2-lean
10. "Jacobian conjecture" "nonproper" 2026
11. "Mathieu conjecture" "2026" moments Long Zwart
12. "Jacobian conjecture" "September" "2026" Lamy Guccione Moskowicz Zhao
13. "Jacobian conjecture" "September 10, 2026" proof
14. "polynomial automorphism" "Keller" "2026" new
15. "Poisson conjecture" symplectic "2026" counterexample
16. "Jacobian conjecture" Atwell Burns Ni "2026" correction

Older Long Mathieu/Poisson, Prellberg/Hessian, graded/cyclic normal-form and real-Jacobian results resurfaced without verified new version. They were not re-proved or transferred to the complex plane. Discovery-only aggregator/mirror hits were not accepted as technical sources.


## Fetch URLs (part2)

- mathstodon-tag.json: https://mathstodon.xyz/api/v1/timelines/tag/jacobian?limit=40
- mathstodon-jctag.json: https://mathstodon.xyz/api/v1/timelines/tag/jacobianconjecture?limit=40
- mathstodon-tao.json: https://mathstodon.xyz/api/v1/accounts/109378244433513115/statuses?limit=40
- bluesky.json: https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts?q=Jacobian%20conjecture&limit=30&sort=latest
- x.html: https://x.com/search?q=%22Jacobian%20conjecture%22&src=typed_query&f=live
- zulip.json: https://leanprover.zulipchat.com/api/v1/messages?anchor=newest&num_before=20&num_after=0
- zulip-public.html: https://leanprover-community.github.io/archive/stream/113488-general/topic/Jacobian.20conjecture.html
- zenodo-atwell.json: https://zenodo.org/api/records/22551146
- zenodo-rank.json: https://zenodo.org/api/records/22168498
- palomar-recent-filtered.json: https://data.palomar-registry.org/recent.json
- palomar-subject.json: https://data.palomar-registry.org/subjects/msc/14R15.json
- palomar-year.json: https://data.palomar-registry.org/subjects/msc/14R15/2026.json
- github-discovery-filtered.json: https://api.github.com/search/repositories?q=jacobian-conjecture&sort=updated&order=desc&per_page=100
- roy-plane-current.json: https://api.github.com/repos/royvanrijn/jacobian-research/contents/research/plane-jc?ref=0d23a2e91143e73b5f67be491cb61a3ab9541875
- roy-plane-previous.json: https://api.github.com/repos/royvanrijn/jacobian-research/contents/research/plane-jc?ref=bcfe480d9101380451099d6f25f54d9bca71dc20
- reuellee-plane-commits.json: https://api.github.com/repos/reuellee/finite-certificates/commits?path=jacobian&since=2026-09-09T22:31:29Z&per_page=30
- jtpmath-contents.json: https://api.github.com/repos/jtpmath/jacobian-conjecture-sheaf-obstructions/contents/
- jtpmath-commits.json: https://api.github.com/repos/jtpmath/jacobian-conjecture-sheaf-obstructions/commits?per_page=3
- jtpmath-README.md: https://raw.githubusercontent.com/jtpmath/jacobian-conjecture-sheaf-obstructions/main/README.md
- jtpmath.pdf: https://raw.githubusercontent.com/jtpmath/jacobian-conjecture-sheaf-obstructions/52b813def0672581006ee292feaffc81c34ba311/paper/compiled/Manuscript.pdf

Browser-only discussion (returned rendered page read; no local raw body or all-comments completeness claim): https://www.reddit.com/r/math/comments/1wcstct/260905746_on_endomorphisms_of_affine_spaces_and/ . Primary corroboration is the byte-identical BGV PDF supplemental statement, not anonymous comments.


This index records documentary reads, not mathematical validation. Retrieval began September 10 at 21:54 UTC; last successful raw fetch completed 22:01:02.811468974 UTC. Four broad search batches finished before clock22:02:11 UTC. The previous successful broad cutoff was September9 22:31:29.498797611; unchanged inherited backstop September10 22:31:29.498797611. Global social coverage remains partial.

Each body has an adjacent .headers file. PINS.json records exact SHA256/bytes and body file-write UTC for each; the latter is capture metadata, NOT a source publication date. Curl calls had 15-second (final PDF20-second) timeouts and 1–2MiB byte caps. No response hit its declared byte cap. Palomar and GitHub discovery JSON was protected-entry-filtered before retention/display: these are generated filtered snapshots, not untouched server bodies. All other fetched bodies are retained raw. PDFs were only converted to documentary text.

## Fetch URLs (part1)

- arxiv-jc.xml: https://export.arxiv.org/api/query?search_query=all:%22jacobian%20conjecture%22&sortBy=lastUpdatedDate&sortOrder=descending&max_results=30
- arxiv-related.xml: https://export.arxiv.org/api/query?search_query=all:%22Keller%20maps%22%20OR%20all:%22Hessian%20conjecture%22%20OR%20all:%22Mathieu%20conjecture%22%20OR%20all:%22Poisson%20conjecture%22&sortBy=lastUpdatedDate&sortOrder=descending&max_results=30
- arxiv-AG.html: https://arxiv.org/list/math.AG/new
- arxiv-AC.html: https://arxiv.org/list/math.AC/new
- arxiv-CV.html: https://arxiv.org/list/math.CV/new
- datacite.json: https://api.datacite.org/dois?query=%22Jacobian%20conjecture%22&sort=-created&page%5Bsize%5D=25
- zenodo.json: https://zenodo.org/api/records?q=%22Jacobian%20conjecture%22&sort=mostrecent&size=25
- bgv-abs.html: https://arxiv.org/abs/2609.05746
- github-royvanrijn--jacobian-research.json: https://api.github.com/repos/royvanrijn/jacobian-research/commits?per_page=3
- github-wstrinz--plane-jacobian-72-108.json: https://api.github.com/repos/wstrinz/plane-jacobian-72-108/commits?per_page=3
- github-wstrinz--plane-jacobian-75-125.json: https://api.github.com/repos/wstrinz/plane-jacobian-75-125/commits?per_page=3
- github-blueberryvertigo--polynomial-composition-rigidity.json: https://api.github.com/repos/blueberryvertigo/polynomial-composition-rigidity/commits?per_page=3
- github-YucongDuan--Plane-Jacobian-Conjecture-DIKWP-MESH-8.0-Bilingual-Proof-Package.json: https://api.github.com/repos/YucongDuan/Plane-Jacobian-Conjecture-DIKWP-MESH-8.0-Bilingual-Proof-Package/commits?per_page=3
- github-Kakarottoooo--jacobian-2d-research.json: https://api.github.com/repos/Kakarottoooo/jacobian-2d-research/commits?per_page=3
- github-SuperMindAI--Jacobian-Conjecture.json: https://api.github.com/repos/SuperMindAI/Jacobian-Conjecture/commits?per_page=3
- github-alok--jacobian-two.json: https://api.github.com/repos/alok/jacobian-two/commits?per_page=3
- github-nasqret--jacobian-counterexample.json: https://api.github.com/repos/nasqret/jacobian-counterexample/commits?per_page=3
- github-rk-mlu--kellermap.json: https://api.github.com/repos/rk-mlu/kellermap/commits?per_page=3
- mo.json: https://api.stackexchange.com/2.3/search/advanced?site=mathoverflow&order=desc&sort=activity&q=jacobian%20conjecture&pagesize=30&filter=withbody
- mathse.json: https://api.stackexchange.com/2.3/search/advanced?site=math&order=desc&sort=activity&q=jacobian%20conjecture&pagesize=30&filter=withbody
- bgv-v1.pdf: https://arxiv.org/pdf/2609.05746v1
- zhang.pdf: https://arxiv.org/pdf/2609.10180v1
- roy-plane-commits.json: https://api.github.com/repos/royvanrijn/jacobian-research/commits?path=research/plane-jc&since=2026-09-09T22:31:29Z&per_page=30
- kellermap-references.md: https://raw.githubusercontent.com/rk-mlu/kellermap/44f4736cf6505c72aa72edb744bd1e118f93c761/docs/references.md
