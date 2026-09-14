# Scheduled broad external sweep — September 11, 2026

Status: PARTIAL / BOUNDARY INCIDENT. External documentary findings only; no theorem, source-point, counterexample or execution promotion. JC2 remains unresolved. Owner: /root/nonemptiness_certificate.

First action 21:48:32 UTC. Sixteen broad query submissions completed by 21:53:20.326987046. Last successful raw retrieval completed 21:53:56.454480381; final generated filtered capture completed 21:53:56.520844211. All network calls were terminal at 21:53:56.598798932, before the unchanged 22:01:02.811468974 backstop. Publication reserve 22:09; hard stop 22:12. Prior comparison cutoff September 10, 22:01:02.811468974. These are retrieval clocks, not publication dates.

## Actionable findings

1. Two new same-author plane-proof claims are BLOCKED_CLAIM, not mathematical progress. Cláudio Vicente da Silva's [4D Transductive Proof](https://zenodo.org/records/22709821) was created September 11 at 13:40:18.528783 UTC. Its full 313-line extracted text was read. Section 3 infers eventual zero coefficients from finite exponentially weighted square energy. That implication is false: for positive mu, c_k=epsilon exp(-mu k) gives finite such energy and infinitely many nonzero coefficients; epsilon can make the sum arbitrarily small. Independently, its added dynamics/metric hypotheses are not derived for arbitrary Keller maps. Cheapest action: retain this explicit failed implication; no verifier launch or proof promotion. PDF SHA256: `3d7236b9040d548887a97e46f886628ae15b99a4db4ce482e17d034182980ca8`.

   The earlier [Transductive Solution](https://zenodo.org/records/22708234), created the same day at 12:14:05.931880 UTC, explicitly identifies the missing passage from the Jacobian condition to its global closure condition. Selected sections 25–26 and 42–45 were read, not the whole 976-line extraction. The final theorem adds that closure assumption; this does not establish it for every Keller pair. Cheapest action: record the precise missing global hypothesis. PDF SHA256: `c24b83aee034dcdb9cb7bfa60df0779b840f46792a13ba9688daa616a8392cb0`.

2. KellerMap has a genuine ACTOR_CORRECTNESS_UPDATE. The September 11 [pruning correction](https://github.com/rk-mlu/kellermap/commit/d09d2fe9c5b825c9cf808305655c343793c10f79) says the old peel search could incorrectly report exhaustion: it used an acyclic-carrier predicate where the factor search needed the derivative-based carrier condition. The returned patch adds the latter and routes untargeted pruning through it. The author also documents a remaining targeted-search deduplication limitation; this is not a claim that all search modes are complete. I read the commit message and all returned patches, but ran no tests and did not audit whole source files. Cheapest action: qualify historical negative search claims by exact version, and keep targeted completeness unresolved. No campaign theorem depended on this search. Commit-response SHA256: `3069a9e2fddd9759989ac454929b8a70e6372f75ea07a1768fdb62dce56bc94d`.

   Its current [references](https://raw.githubusercontent.com/rk-mlu/kellermap/1ee87113617985d82ffa9e48ff45dff17f9de5b2/docs/references.md) also correct the symmetric-lift attribution to de Bondt/van Essen and retract an apparent degree-record comparison. This is an attribution/status update, not an independently reproduced construction.

3. No new BGV/Zhang mathematical delta was found in the returned versions. Fresh [BGV v1](https://arxiv.org/pdf/2609.05746v1) and [Zhang v1](https://arxiv.org/pdf/2609.10180v1) PDFs are byte-identical to the previous sweep: respectively `814c3f2572f660a47778663384077d6357e9947f1585c1e16372f6cdbe138425` and `210dd708c651358ccd5765332ab708d8581fb990a7596b4ec34587b449b46148`. This round read abstract/feed metadata and hashed the PDFs, not their full bodies. The prior weak-type-1 source-divisor and positive-characteristic/characteristic-zero limitations remain unchanged.

4. A [GGV institutional catalog entry](https://cris.pucp.edu.pe/es/publications/the-lower-side-of-the-newton-polygon-of-hypothetical-counterexamp/) now provides DOI `10.2989/16073606.2026.2701437` and accepted/in-press 2026 status for the lower Newton-polygon paper. Publisher access returned 403. This is a bibliographic pointer only: neither a new September theorem nor equality with an older preprint was established. Cheapest next check, when publicly accessible: compare the literal published hypotheses before changing an imported interface. HTML SHA256: `23dbe5adad78da8d5dc8ad7c18f824ff81f371ffac5c942fac8c4f4ed2aaaa79`.

## Breadth and remaining holes

Comparable endpoints covered arXiv exact phrase and Keller/Hessian/Mathieu/Poisson concepts, math.AG/AC/CV announcement titles, GitHub discovery and eleven watched heads, scoped plane paths, Zenodo/DataCite, MathOverflow/MathSE, public catalog metadata and actual actor/social feeds. Sixteen supplementary concept/name/date searches included nonproperness, Newton/Puiseux, compactification, automorphisms, moments, symplectic/Poisson and Eulerian/D-module routes. Search snippets were discovery only; some aggregate tool output clipped. No exhaustive result-body claim is made.

- arXiv returned 30 of 220 exact-phrase records and 30 of 46 related records. No later BGV/Zhang version appeared in those returned windows. Registry pagination remains open.
- Zenodo returned 25 of 130 hits, versus 126 previously. Its returned ordering was not reliably chronological; four newly noticed records do not exhaust possible changes. DataCite returned 25 records, including concept/version duplicates. Existing Atwell and rank-obstruction records were metadata checks only.
- GitHub discovery retained 78 allowed entries after filtering. Eleven three-commit head windows were checked. Roy's latest head concerned Curve302; both named plane-path queries returned empty windows, as did the scoped reuellee query. This does not prove whole-tree equality. The other watched heads except KellerMap had no post-cutoff head date. A newly noticed actor's three commits concerned unrelated Bell/POVM work, so no further traversal followed.
- MathOverflow/MathSE returned 30 records each; selected title/activity metadata showed no newer relevant activity. No answer-body audit occurred.
- Mathstodon returned 10 and 7 tag posts and 40 Tao posts. Tao's [September 11 announcement](https://mathstodon.xyz/@tao/117253629967855195) links a joint mathematics-and-AI declaration; that actual post was read, but the declaration itself returned 403. Its content/signatories were not independently verified. No post-cutoff JC tag item appeared in the returned windows.
- X supplied HTTP200 shells, not authenticated post text. Bluesky returned 403, Zulip API 401/public archive 404, Reddit JSON 403, and the GGV publisher/declaration endpoints 403. Search-rendered allegations about authorship were not adopted. Global X/Bluesky/Zulip coverage debt remains the prior September 3, 10:17 UTC anchor; this sweep does not reset it.

## Boundary incident and custody limitations

The Palomar subject request was mistakenly retained and displayed before protected-entry filtering. It contained prohibited catalog summaries. No protected entry was followed and no protected repository/tree/code was accessed. ROOT was immediately informed and ordered the affected subject channel stopped. No protected titles, identifiers or content are reproduced here or used as evidence.

The exact owned unfiltered file `/home/ubuntu/jc2/box/websweep-20260911T2148Z-astra/palomar-subject.json` (HTTP200, 7108 bytes; retrieval completed 21:50:13.499411376) was removed after generating a filtered snapshot. Its body hash was not recorded before removal; it is not recoverable from a retained local raw copy, and it was not re-fetched. Headers and the generated filtered snapshot remain hash-bound. The affected subject/year channel is excluded from scientific evidence. This is PARTIAL/BOUNDARY INCIDENT, not clean coverage.

Two initial watched-head downloads accidentally shared `github-wstrinz.json`. That ambiguous file and combined headers are retained but NOT USED. One fresh request per endpoint under distinct filenames supplied the actual metadata comparison. This was filename recovery, not a scientific retry.

All documentary downloads had a 15-second request limit and 2 MiB response cap; none reached that cap. Browser result limits and access failures remain separate. READ-SCOPE distinguishes raw retention, generated filtering, selected reads and hash-only PDFs; PINS and custody bind all retained bytes, including unusable/access-failure artifacts. No downloaded code was executed. No route re-ranking, source claim, new mathematical OPEN, follow-on computation or authority results from this sweep.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8813`.
- Body SHA-256:
  `c003248866387d6fe987bb7a83f18e22ee0975eda9974e5452a23bb6c11de532`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
