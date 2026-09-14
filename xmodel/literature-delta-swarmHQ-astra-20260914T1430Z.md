# Bounded literature delta — swarmHQ Astra, 2026-09-14 14:30Z

Producer: Astra (`/root/literature_delta_1430`). Basis: `cb49d325e024da1aecb0ba44057e7aa1daa43abc`.
Evidence tier: DOCUMENTARY / MANUAL. Lifecycle: PRODUCER-CHECKED, UNPROMOTED.
Scope: PARTIAL primary-source discovery, not a completed BROAD sweep. No source point, mathematical promotion, scientific execution, or exit-price assertion.

## Scope and outcome

**NO_NEW_ACTIONABLE_DELTA.** Several newly located sources have relevant vocabulary, but the checked statements supply no missing actual-source hypothesis or new decisive test for a JC2 proof or counterexample. This is a bounded negative discovery result, not evidence that no useful literature exists. No follow-on lane, rank change, FIRST, or mathematical promotion is requested.

The main agent's protected all-degree work remained independent. This lane read AGENTS.md, README.md, COORDINATION.md, team/swarmHQ/README.md, the whole current APPROACHES.md, FALLACY-v2.md, and xmodel/websweep-20260911T2148Z-astra.md. Canonical and report history searches were targeted to titles, authors, identifiers, and mechanisms; matching history was checked before pursuing old sources.

## New source scope checks

### 1. Arapura–Mese–Patel: the new log Euler–Hurwitz theorem does not apply to the whole plane

[arXiv:2609.13081v1](https://arxiv.org/html/2609.13081v1), submitted September 11, announced in the September 14 math.AG listing. Read scope: introduction, Theorem 1.1/Corollaries 1.3–1.5, Sections 2–3, and Section 4 through Remark 4.1; not Sections 5–7 or the imported index/positivity references.

Theorem 1.1 requires a finite surjective map of smooth connected varieties, with target a smooth closed subvariety of a smooth log compactification having nef logarithmic cotangent bundle. It gives signed Euler characteristic at least degree times that of the target. Proposition 2.2 gives the corresponding generic-rank lower bound for perverse sheaves.

The whole-plane application fails: **A2 cannot be closed in such an ambient Z**. Its closed A1 contradicts Lemma 2.1: `-chi(A1) >= 0`, whereas `chi(A1)=1`. Independently, a hypothetical nonproper Keller map lacks finiteness. Finite-etale restriction recovers the existing covering equality (Remark 4.1), not vanishing of boundary cohomology. APP Sections 5–6's nonproper splitting/localized-acyclicity gaps remain.

ROOT supplied a stronger scope observation while this report was still authoring; I independently checked its argument manually. There is no nonconstant morphism `A1 -> Z` at all: extend to `P1 -> Zbar`; the nonzero logarithmic differential maps the pulled-back nef bundle to `Omega_P1(log infinity)=O(-1)`. Its image is a negative-degree quotient, impossible for a nef bundle. Hence an open retaining an entire polynomially parametrized nonproperness component cannot embed in this log-nef ambient. ROOT's additional control `A2 minus {xy=1}` has an SNC completion by the conic and line at infinity, with `K+boundary=0`, but still contains the entire line `x=0`. Nef log canonical divisor is therefore not nef log cotangent bundle. Both are attributed ROOT MANUAL/UNPROMOTED scope analyses, not new JC2 theorems or imported results.

### 2. Li: prescribed sparse images, not arbitrary canonical graphs

[arXiv:2609.12854v1](https://arxiv.org/html/2609.12854v1), submitted September 11. Read scope: Sections 1–2, Section 3.1 and Theorem 3.2 with proof; selected returned statements of Propositions 3.3/3.5 and Theorem 3.6. Not the whole 44-page paper or its companion normalization paper.

For an aperiodic mask `S subset Z/dZ`, its monic algebra is specifically `K[p_j : lambda_j(S) != 0]`, where `p_j` are source-root power sums and `lambda_j` are the mask's Fourier coefficients. Theorem 3.2 computes the completed image from exact moment tuples over the entire normalization fiber. These are exact output-algebra hypotheses, not merely a finite smooth normalization or known conductor. No map from an arbitrary canonical Keller graph to this sparse-profile algebra was found. General conductor pinching is explicitly classical in the source. This supplies no missing normality or conductor-unitness test beyond APP Section 8's source-attachment gap.

### 3. Ionin–Semidetnov: non-elementary matrices still need exact rows

[arXiv:2609.04275v1](https://arxiv.org/html/2609.04275v1). Read scope: introduction/Theorem A, novelty discussion, selected historical theorem statements; not the proof of non-elementarity.

Theorem A treats `F`, the fraction field of a DVR with uniformizer `pi`, and an explicit matrix over `F[X^+-1,Y^+-1]`. Its first row is `a=1-(X-1)(Y-1)/pi`, `b=(Y-1)^2/pi`. Manual negative check: `a_Y=-(X-1)/pi`, while `b_X=0`; this row is not a gradient. The source explicitly excludes algebraically closed fields from that valuation hypothesis. Even choosing `F=Q` does not cure row non-exactness. APP's prior Cohn–Broughton/Wright exact-coframe gap remains; no matrix search or new construction is selected.

## Additional scope screens and negative controls

[Llibre–Mello, published August 25, 2026](https://link.springer.com/article/10.1007/s00574-026-00525-3): read introduction/Theorems 1–2 and selected proof passages, not the whole paper. For a real-plane orientation-reversing local diffeomorphism fixing zero, the stated criteria require bounded pullback-radial dynamics or positivity of the associated field's Jacobian. Neither premise is established here for arbitrary Keller maps. Manual control: put `u=x+y^2`, `v=y+u^2`, `F=(u,-v)`, an automorphism fixing zero with Jacobian -1. Its field is minus `E=(x-y^2+2yu^2,y-u^2)`. Direct differentiation gives `det DE=1-4yu+4u^3`, which is `-1/2` at `(x,y)=(-1/2,1)`. The reflection `(x,-y)` instead gives field `(-x,-y)` and determinant 1. Thus the sufficient positivity condition is not automatic even on genuine plane automorphisms. No bounded-flow assertion for arbitrary Keller maps follows, and the real-plane statement does not automatically cover a complex-plane map viewed in four real dimensions.

[Fan Xu, arXiv:2609.10454v1](https://arxiv.org/html/2609.10454v1): abstract, introduction and opening theorem/proposition statements only. Its constructed complements of elliptic curves in nine-point blowups and canonical-extension families do not identify an actual Keller normalization or supply its missing affineness/normality. No deformation theorem was imported.

[Matysiak, July 2026 noncommutative square-free paper](https://link.springer.com/article/10.1007/s10958-026-08536-7): introduction, Theorem 4.1/proof, Proposition 4.2, and selected subsequent statements only. The cited commutative Jacobian/square-free equivalences are antecedents, not a new implication to automorphy. No factorization theorem is imported here. This is distinct from, and does not reopen, the already rejected SSRN proof manuscripts.

[Pasten–Silverman, Propagation of Zariski dense orbits](https://ems.press/content/serial-article-files/52742?nt=1): first-page abstract and contents only. The projective morphism setting supplies no compactified self-map for a general nonproper plane Keller map. No dynamics theorem read or adopted.

## Version watch and deduplication

The returned primary submission histories still list [BGV 2609.05746](https://arxiv.org/abs/2609.05746) v1 September 4, [Zhang 2609.10180](https://arxiv.org/abs/2609.10180) v1 September 9, [Magnen 2311.14723](https://arxiv.org/abs/2311.14723) v1 November 19, 2023, and [Han–Pan–Chen 2407.11291](https://arxiv.org/abs/2407.11291) v1 July 16, 2024. [Charbonnel 2304.14675](https://arxiv.org/abs/2304.14675) remains withdrawn v5, August 6, 2026. These are metadata observations, not fresh whole-PDF equality checks or theorem audits. APP's recorded BGV/Zhang source gaps, Magnen coefficient failure, and Charbonnel stop remain unchanged.

Makar-Limanov–Trakhtenberg's *Properties of a Jacobian mate* was found through its April 2026 publisher metadata and MPIM 2024-33 preprint. This lane read only the preprint opening and returned selected algorithm passages before recovering the existing exact audit, `xmodel/websweep-20260824T1916Z-properties-jacobian-mate-audit-codex2.md` (opening through the scope inventory read). It is **KNOWN**, not a new all-degree lead; no repeated bound/census audit followed. Publication/preprint text identity remains unproved here.

The Bustinduy–Giraldo–Mucino-Raymundo fiber-integration criterion was likewise already screened in notes.md around lines 40179–40188. Its missing all-fiber irreducibility and time-period conditions are not construction data. Truong's 2026 properness theorem was already screened around lines 39871–39875. Neither was reread wholesale or turned into a new lane.

## Coverage, custody, and stop

Discovery used 18 phrase/concept search submissions, including non-date-windowed Jacobian mates, etale maps, nonproperness, and algebraic symplectic maps; later queries restricted primary domains. The arXiv exact-phrase sorted search and API requests did not return usable lists. Recent math.AC, math.AG and math.CV pages returned first-page windows (respectively 49, 50 of 179, and 50 of 66 entries). I read selected title/header windows and keyword-find contexts, not every listed abstract or every page. The new Arapura/Li items were located there. This is not exhaustive arXiv coverage.

Incidental repository/mirror, social/news and secondary search snippets were not followed, retained in a local source bundle, or used as evidence. No repository/GitHub queue traversal, protected nested-repository inspection, Mathstodon/Palomar request, external contact, credential use, bypass, cloud/model launch, or scientific execution occurred. Third-party statements remained data. Initial rg discovery relied on the parent .ignore exclusion; later searches were explicit allowed paths. One overly broad local synonym pattern produced clipped output; it supplied no claimed exhaustive history census.

No raw web snapshots or new source PDFs were saved; documentary references are pinned to arXiv versions or exact publisher URLs and stated read scope, not byte-identity claims. Only this leased report and its automatic finalizer manifest are authored. Administrative finalization/hashing is not scientific computation. No tests or scripts from source material were run.

Discovery began before 14:27:11 UTC; the last source retrieval finished by 14:31:47 UTC. Searches then stopped; the last attributed scope reasoning was checked by 14:35 UTC, inside the 12-minute tranche and the 14:49 publication backstop. No new mathematical OPEN, review debt, or automatic successor. The BROAD sweep clock and all previous access/stopped-channel debts remain unchanged. JC2 remains unresolved.

## COLLISIONS

EMPTY — manual declaration: this documentary report raises no new OPEN. The broad collision scanner was not run, to avoid unnecessary peer-body intake. Title/author/mechanism deduplication above is scoped historical discovery, not a claim that every old report was read.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11131`.
- Body SHA-256:
  `2a088ab1c89d30a2d8a9d8d15befd0d5ffc7828c8d110bfa9cf64166c3122da7`.
- Frozen basis: `cb49d325e024da1aecb0ba44057e7aa1daa43abc`.
