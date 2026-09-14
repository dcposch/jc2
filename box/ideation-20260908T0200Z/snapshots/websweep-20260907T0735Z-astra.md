# Broad JC2 sweep: a new composition theorem, but no licensed JC2 attachment

2026-09-07. **PARTIAL external coverage; no JC2 proof, counterexample, source exclusion or guarded point found.** Window: September 6, 09:23 UTC through the actual final retrieval **September 7, 07:56:45 UTC**, plus broad undated discovery. Endpoint-specific retrieval times are retained; this is not continuous monitoring.

The strongest new lead is a plausible all-degree proof of Furter's one-variable composition-rigidity conjecture. It merits one narrow independent mathematical read. It does **not** presently supply our missing degeneration, polynomial-termination or source-to-receiver arrow. There are zero newly licensed faster JC2 paths, one actionable external-theorem candidate, and several useful scope corrections.

## 1. Actionable first: polynomial composition rigidity via critical values

The partially recovered `@octonion` profile linked **liqsweep / blueberryvertigo, Polynomial composition rigidity via critical values** on September 7 at 04:26:26 UTC. Current head is `b17b6b9f7440b12fd85df2c2db9c98209ecc174d`, committed 04:19:19 UTC; the current PDF has **eight pages**, although the social post describes a two-page proof. Whole current Typst source, README and references were read. PDF SHA256 `0e9662c12bba4204c12ce6e1a2140687d138d33a520f771320f87129879f445d`; source `8a6e152c797c227529e88572db140fcfb5b6c3ad61650c2a94fc6304cb334af6`. [Pinned primary paper](https://github.com/blueberryvertigo/polynomial-composition-rigidity/blob/b17b6b9f7440b12fd85df2c2db9c98209ecc174d/proof.pdf).

Exact main claim: for nonconstant complex polynomials `f_i`, if `F=f_s∘…∘f_1`, `F(0)=0`, `F'(0)=1`, and `F≠z`, then

    ord_0(F-z) ≤ 1 + Σ_i(deg f_i-1).

For two factors this gives `ord_0(a∘b-z)≤deg a+deg b−1`, hence Furter's `R(m,n)` for every m,n. This is a genuine all-degree claim, not another bounded computation.

The load-bearing proof is short enough for an explicit desk check. Write `F=z+c z^(k+1)+z^(k+2)r`, c≠0. For small positive δ, the polynomial `(1+δ^k)F` has k distinct nonzero fixed points `z_j=δ(α_j+O(δ))`, where `1+c α_j^k=0`. Their multipliers are `1−kδ^k+O(δ^(k+1))`, hence attracting. Each full attracting basin contains a critical point: otherwise inverse branches of all iterates over a small disk would be uniformly bounded by the polynomial escape radius, while their derivatives grow as the inverse multiplier powers, contradicting Cauchy's estimate. Distinct basins give distinct critical **values**, not merely critical points. Scalar multiplication preserves their number. Finally

    CV(a∘b) ⊆ CV(a) ∪ a(CV(b))

gives the bound. I found no gap in this core on the first full read. The nonzero multiplier case, properness of the one-variable polynomial, and the attracting sign are addressed explicitly. The characteristic-p control `a=z+z^p`, `b=z−z^p` gives contact p² and shows why characteristic zero matters. This is **provisional external mathematics**, not an independent formal verification, specialist review or campaign promotion.

The original Furter bridge was checked against the author-hosted October 10, 2013 manuscript: introduction, definition of the ambient ind-variety/group, Theorem B, and Lemma 11/proof. Theorem B conditionally describes closures of length-two polydegree strata **in `G=Aut(A²)`**. Its long proof remains an imported published dependency, not newly replayed here. The new producer's finite-flat composition-coefficient map and restricted Strong Factorial consequences likewise must not be inflated to arbitrary Keller maps. [Furter primary manuscript](https://www.math.u-bordeaux.fr/~jpfurter/polynomialCompositionRigidityAndPlanePolynomialAutomorphisms.pdf); [published version](https://doi.org/10.1112/jlms/jdu064).

**Exact missing client arrow.** Charged APPROACHES still needs a guarded-source component to reach k=0 with controlled coefficients, or a global obstruction to components avoiding that fiber/diverging at infinity. Our receiver `A(g,p),B(g,p)` with bracket `c g²` is not a one-variable composition. Its marked boundary polynomials `A(0,p),B(0,p)` have degrees15/25, but are not licensed as compositional inverses or as a composition agreeing with the identity to order40. Polynomiality of both physical lifts supplies no such statement. Nor has a hypothetical source point been placed in a degeneration of a fixed length-two automorphism stratum. Assuming that placement would assume substantive invertibility/degeneration information absent from the source contract.

Even the finite-flat coefficient map is a different morphism: at m=n=1 its first coefficients are `(a+b,2ab)`, with Jacobian `2(a−b)`, not a nonzero constant. Its properness cannot be transferred to our 81-coordinate source merely because both are coefficient schemes.

**Cheapest discriminator:** one independent desk gate on Lemmas2.1/3.1, the critical-value composition bound, and the exact Furter statement. If accepted, require a named source identity producing excessive one-variable contact, or an actual morphism into the specified automorphism degeneration, **before** any JC2 descendant. In the currently charged source neither exists. This may retire unrelated finite `R(3,n)` searches if validated; it does not justify diverting the direct complete-ideal or remaining global/pure-boundary task. No claimed consequence establishes all Strong Factorial cases, full HC4 or JC2.

## 2. Other changes and undated discoveries

**Collision geometry narrowed its claim.** One in-window commit moved `0f1f2c8c…` to `2e40066e722b601157885fd2a8264569be3ea2b8`, September 7, 00:29:16 UTC. Current Paper II is a generic-function-field-degree-two exclusion. The prior full-JC2 boundary/inertia manuscript is archived; those modules are outside the stable core. Whole current paper was read, with its main theorem and challenge declaration. A separable quadratic extension is Galois; the proof explicitly assumes classical Keller–Galois rigidity and obtains the contradiction through its collision ideal. Ambient dimension two and generic degree two are different hypotheses. Proposed Palomar submissions remain unsubmitted and require toolchain migration; a deliberate `sorry` in the challenge template is not evidence that its solution contains a missing proof. No Lean build was run. **Actor correction, not a new JC2 frontier.** [Pinned repository](https://github.com/what-social-construct/jacobian-collision-geometry/tree/2e40066e722b601157885fd2a8264569be3ea2b8).

**Atwell: one new consequence, one updated old record.** Date-filtered Zenodo returned new record22551146, created September6 19:57:55 UTC, version1.0.0, manuscript dated September2. Whole short note read: an existing quartic Hessian-nilpotent failure in some dimension is extended by two variables using `R=q(u+iv)`. Its square-zero Hessian and harmonic powers, together with Zhao's disjoint-sum identity, preserve the original nonvanishing obstruction while making the series nonpolynomial. Zhao's Corollary2.8/proof, Problem5.2, and Theorem7.2/proof were checked in the primary preprints. The argument is coherent conditional on the already imported higher-dimensional failure; **adding two variables is not plane descent**. [New deposit](https://doi.org/10.5281/zenodo.22551146), [Zhao 2008 v2](https://arxiv.org/abs/0704.1689v2), [Zhao equivalence v2](https://arxiv.org/abs/math/0409534v2).

Relative-rank record22168498 was updated September6 11:40:54 UTC; it still exposes v5.1 and the rank≤1 theorem. Whole current source read. Its generic rank-two vector-space quotient is expressly not a global polynomial plane quotient. The previous campaign's independent vacuity proof remains applicable on its stated unequal-degree/non-pure-top locus. Historical file bytes are unavailable, so the update is not represented as a newly proved theorem or an identified textual diff. [Current record](https://doi.org/10.5281/zenodo.22168498).

**HC4 discovery correction.** Evidence Press's current ipitchford release page explicitly cites Ni2608.14217 and clarifies that its unresolved ternary-quintic branch belongs to **full HC4**, not merely quartic HC4. The page labels the clarification September1; I cannot establish when those web bytes changed. This corrects the last sweep's overly broad inference from repository-README absence. The underlying package/head remains fixed; the page's Ni audit is producer-side, not independently checked here. Its finite structural certificates leave a secant target and full HC4 open. Ni's current abstract is byte-identical to the retained old hash; no revision was found. No renewed Ni or HC4 task is suggested. [Producer release page](https://www.evidencepress.org/releases/hc4-five-support-structural-reductions/).

**Van Dobben's boundary theorem is not our missing global arrow.** Whole2608.27341v1 read. Theorem3.1 treats a projective bundle over P¹ with two irreducible **relative hyperplane** boundary divisors. In surface dimension, affine-plane complement forces their intersection to be one reduced point; tangential intersection of multiplicity>1 is ruled out by topology at infinity. Remark3.3 suggests possible JC2 use. Our charged marked O(−4)-torsor completion instead deletes a section and a **vertical fiber**; the second divisor does not satisfy the theorem. Our chart is already A², so its topology alone supplies no contradiction. A contraction/alternate completion preserving the marked chart and forcing the required two-section intersection is missing. Neither this theorem nor abstract torsor classification removes the boundary of the finite normalization. No additional lane is recommended absent that exact predicate. [Primary v1](https://arxiv.org/abs/2608.27341v1).

Broader undated discovery also returned Truong's 2026 journal publication of the older properness program: bounded hypotheses and conjectural higher-rank criteria, not a new arbitrary-plane result. Real-Jacobian papers and an expository JC-for-n=2 page were not misread as constant-complex-Jacobian proofs. An August JTP Math sheaf/topology page exposes no accessible full theorem/proof; an old Preprints.org claim returned a placeholder. These are limitations, not accepted or refuted results.

## 3. Broad coverage, including Monday announcements

| Channel | Checked coverage and bounded result |
| --- | --- |
| arXiv Monday September7 | AG:13 new/4 cross/11 replacements; AC:4/5/5; CV:8/3/4. Lists really identify Monday, not the previous announcement. Keyword hits concerned commutators, reaction-network Jacobians or compactified Jacobians, not JC2. Category APIs were also queried. |
| arXiv discovery/revisions | JC phrase total219; newest submitted2608.27341v1; newest updated2608.19112v2 at September2 02:45:38. Keller/Hessian/plane-pair/Abhyankar–Moh/polynomial-automorphism queries and20 author queries found no indexed in-window relevant revision/submission. Announcement date is not manuscript timestamp; private/unannounced submissions remain invisible. |
| Watched authors | Orevkov, Guccione, Valqui, Horruitiner, Pissolato, Shaska, Migus, Jelonek, Xavier, Gao, Meng, Charbonnel, Kowalczyk, Alpöge, Ni, van Dobben, van den Essen, de Bondt, Zhao and Truong. Name queries have homonym noise; they are not identity-complete bibliographies. |
| GitHub broad/new actors | Repository query63 versus prior61. Two September6 vibemathing problem-admission repositories contain fixed harness/contract scaffolding, not proof artifacts; both issue lists empty. Full nonprotected trees/context contracts inspected. Furter's repository was discovered separately through the account feed, illustrating keyword-search incompleteness. |
| Watched repository heads | SuperMind, both Strinz mains and watched branches, ipitchford, AEjonanonymous, SNAPKITTYWEST and CAOS unchanged. Exact full heads in coverage-final.json. No new Strinz source adapter/artifact drop observed. |
| Roy | Head a293bd9… moved132 commits. GitHub compare capped at300 files, so no inference from that truncated list alone. Exact plane-jc/extended-geometry path histories were empty in-window. Full typed-status comparison1232→1368 entries:139 changed/new, **zero changed or removed among240 JC2/HC4-matching entries**. No mathematical promotion from status labels. |
| Zenodo | Date-scoped JC queries:1 new record,3 updated records; the third is unrelated CogOS. Plane/Keller updated query isolates the rank record. **Unfiltered newest/mostrecent omitted these hits**, despite total126; sorted-list absence alone would have been wrong. Direct records confirm dates/files. |
| Palomar/public discussion |197 recent entries;11 publications/revisions in-window, none JC2. MSC14R15 index6 entries and math.AG12, none in-window. PalomarArchive metadata checked. Registry presence is not independent human semantic verification. Tao's JC and Palomar comment feeds have no in-window entry; MO/MSE queries empty. |
| MO watched artifact | Thread513413 still4 answers and August19 last activity. ratto3423 still one post with no promised write-up; September5 last access is unchanged. Views/access activity are not theorem delivery. |
| Social | Mathstodon JC/Jacobian/Keller tags: no in-window post; lean tag4, none relevant; Tao account none in-window. X profile yielded9 actual posts, including2 in-window and the Furter lead. Global X, Bluesky and Zulip remain incomplete as detailed below. |

All actual request URLs, UTCs, statuses, sizes and hashes are in the final source index. Initial query failures were preserved, then corrected by exact public endpoints; they are not silently counted as negative results. No repository source under the protected campaign project was accessed, even where public indexes mentioned it.

## 4. Holes, stop conditions, and custody

**Do not reset the outstanding September3 10:17 UTC coverage clock.** Global X search returned a shell; `@octonion` is only partially recovered (nine visible posts, not all replies/deleted posts/search history). Bluesky's public and alternative search endpoints returned403. Zulip's documented web-public message API still returned401 even with the required public-channel narrow; the public archive has no Palomar channel. Registry JSON and Tao comments do not replace that missing discussion. GitHub code search/authenticated content and arbitrary unrelated repositories are not exhaustively covered. Restricted or inaccessible candidate text remains unverified.

Immediate recommendation: independently assess the pinned Furter core and **its absent client attachment**, then stop if no exact contact/degeneration arrow is produced. Everything else found is a consequence, scope correction, unchanged watch item or hypothesis-mismatched geometry. None licenses a coefficient cut, a new gauge, a third order-only run, properness, or a point. Finite boundary exclusions still do not prove that a guarded component approaches k=0; the currently accepted actual-source construction/replay is not superseded by this sweep.

Six charged campaign snapshots and their hashes are in `charged-pins.json`; APPROACHES was frozen at SHA40783391…, completed1435 synthesis fd465715…, prior sweep c98fe644…. Reading scopes and exact search limitations are in `search-scope.md`. The old sweep's raw source bodies were generally unavailable; only its retained index was charged, with fresh exact-commit snapshots where actual comparison was needed.

Evidence root: `box/websweep-20260907T0735Z/`.

- `coverage-final.json`: SHA256 `1b59aaeeadbabc5b92dae5c55a8dc5eccf19d67a4d3212e0768c6af12e48311e`.
- `source-index-final.tsv`: `3c502c121adaddb4d7518b91086f50c1be446c1e5005d761a74b22e318b88c09`.
- `custody.json`: `c0d46225197b1136474c5f989d46310acaf9e40c9c51a50c54c7f417f9e01454`, pinning194 files, including149 response snapshots and their receipts. HTTP200 does not mean useful content or mathematical verification.

All13 fetch batches and metadata children exited; no remote writes, accounts, fleet, CAS, solver or proof-assistant execution occurred. No canonical ledger or frozen campaign artifact was edited. This is external intelligence only. **All owned writers terminal; STOP/IDLE after transactional publication.** Next full-sweep backstop is September8 07:56:45 UTC, with earlier action on credible public deltas; the unresolved social-channel history retains its older start.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16457`.
- Body SHA-256:
  `b12abbe56311e7e47e06644a1fa2f61855efbfa379ac5e40ff3f9ed6c6979f35`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
