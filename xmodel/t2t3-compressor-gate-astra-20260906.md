**Hostile promotion gate: attained T₂/T₃ compressor and direct presentation**

**A — CONFIRMED-WITH-FIX. B — CONFIRMED-WITH-FIX. The frozen report is not promotable verbatim.** The mathematical compressor, quotient isomorphism, counts, and literal-subset implication survive. The frozen full builder has a completion bug. The report also misstates what properness of the complete ideal would imply. The charged harvest establishes two timeouts; the chart remains **OPEN**.

| Audited assertion | Verdict | Promotion scope |
|---|---|---|
| T₂ bounds 20/25; T₃ scalar conclusion | CONFIRMED-WITH-FIX | Total degree and recursive support explicit |
| Theorem B; isomorphism; counts; subset | CONFIRMED | Hash-bound maps and generator lists |
| Frozen full-builder completion | REFUTED | Contradictory raw/emitted counts |
| Proper complete ideal “not a Keller pair” | REFUTED | Withdraw the incorrect negative |

The corrected mathematics and subset implication are promotable; the unchanged full executable is not. No production unit is declared.

**Custody.** Before writing, `df -h /` reported 96G/85G/12G. I built the nine-entry manifest with `awk` from the indexed basename/SHA fields of the `.run.v2` receipt and ran `sha256sum -c`: all nine files under `/tmp/jc2-lane.BkloGL/inputs` returned `OK`. See [mechanical output](/home/ubuntu/jc2/box/t2t3-compressor-gate-20260906/charged-check.txt). Frozen basis: `36db4240df0b96565569a65780af015292051537`.

Charged basenames below mean the frozen copies. Supplementary source maps match the embedded `build_direct.py:35–83` hashes; the graph producer matches custody SHA `bc83ab1560f418038c7cc26cca003c45fb51ac8745ef2ae4cb5d257438ba6ca4`. No `ideation-*`, `jc2-lean`, charged-input mutation, or ledger edit was used.

**The compressor.** Moh’s target order is `(f,g)=(G,F)`, with `deg F=deg_y F=n`, `deg G=deg_y G=m`. Put `Q=T₂^ψ(G,F)`, `W=T₃^ψ(G,F)`, `B_i=(∂T_i^ψ/∂f)(G,F)`. Then

\[
J(F,Q)=B_2J(F,G),\qquad J(F,W)=B_3J(F,G).
\]

Differentiate the formal first argument before composition. Moh p.150’s definitions give the arithmetic independently recomputed in `arithmetic-check.json`:

| `(n,m)` | `M` | `d` | `Λ` | characteristic degrees `D` |
|---|---|---|---|---|
| `(99,66)` | `−66,77,97` | `99,33,11,1` | `−6534,−1815,−1595` | `66,55,145` |
| `(108,72)` | `−72,81,106` | `108,36,9,1` | `−7776,−2268,−2043` | `72,63,227` |

Lemma 2.1, p.151, uses Keller to obtain `e=n−1` and constant earlier series coefficients. Proposition 2.1, p.152, commutes approximate-root formation with coefficient specialization `ψ:x→0`, acting on target coefficients. Proposition 2.2, pp.152–154, gives **exact y-degree** `D_i` and nonzero scalar leader for `M_i<e`. Here `97<98`, `106<107`; the exceptional terminal case does not apply. On p.154, monic means unit leader, not normalization to one.

The requested pp.150–157 are insufficient. Proposition 3.1 is on p.157, specialization p.159; Proposition 3.2 is on pp.159–161. Proposition 2.2 alone does not give total degree. That necessity uses Proposition 4.5’s proof, p.172, under `M₃=n−2` and Keller. Its minimum over roots of `g∏_{i≤3}T_i^ψ`, including T₃, excludes order below −1. Scalar leader and these root orders give `deg_x[y^{D−j}]T_i≤j`, hence total degree `D_i`. This justifies necessity for Keller realizations; it must not be used backwards to assume Keller at arbitrary chart points. See frozen `char-degree-instrument…:28–40,53–79` and Moh pp.169–172.

Proposition 3.1 enumerates exactly

\[
Q=G^3-F^2+aG^2+bFG+cF+dG+e_0,
\quad B_2=3G^2+2aG+bF+d.
\]

`F²` is the unique equality-weight cancellation against `G³`, forcing coefficient −1; all five lower coefficients remain. Since `2m>n,m`, `deg B₂=2m`. For `j=J(F,G)≠0`, total-degree attainment and domain degree additivity give

\[
2m+\deg j=\deg J(F,Q)\le n+D_2-2,
\]

which is `99+55−2−132=20` and `108+63−2−144=25`. T₂ alone does not force constancy.

Proposition 3.2 gives the *exact* derivative y-degree `deg_y B₃=D₃+M₃=242/333`; its specialization remark on p.161 applies here. Consequently

\[
242\ (333)\le\deg B_3\le\deg B_3+\deg j
=\deg J(F,W)\le n+D_3-2=242\ (333).
\]

Thus `deg j=0`; only `deg B₃≥deg_y B₃` was needed.

The retained recurrence gives a noncircular check. At 99, `W=Q³−λ₂³FG+uFQ` has derivative term `3Q²B₂` of degree 242, versus at most 231 for other active derivatives; seven passive monomials have degree at most 132<145. At 108, `W=Q⁴−λ₂⁴FG²+uFGQ+vFQ²` gives 333 versus at most 324; thirteen passive monomials have degree at most 216<227. Enumerate `nj+ma+D₂b≤n₂D₂`, `a<3`, `b<n₂`. Actual total-degree attainment and this recursive support suffice for the derivative assertion, even without independently certifying canonicality.

**Theorem B and zero.** The relevant theorem is frozen `char-degree-instrument…:120–132`, a campaign source-face theorem, not a Moh-labelled theorem. A source-support closeout assuming a nonzero monomial Jacobian cannot establish `j≠0`.

Suppose `j=0`. In characteristic zero, the common-polynomial theorem gives `F=f(H),G=g(H)`; I checked [Arzhantsev–Petravchuk, Lemmas 4–5, p.5](https://arxiv.org/pdf/math/0608157). Set `r=deg_y H`. Composition degrees and `deg F=deg_y F` imply `deg H=r`; attained positive `deg_y Q` implies `r|gcd(n,m,D₂)`, namely 11 or 9. Since the highest forms of F are `y²⁷(y−x)⁷²` and `y²⁴(y−x)⁸⁴`, unique factorization forces `(r,deg f)=(11,9)` and `(9,12)` respectively.

On the actual major covers `(t,z)=(s³,πs⁴)` and `(s⁴,πs⁵)`, F has valuation −9/−12 and faces `(π³−1)²⁴`/`(π⁴−1)²¹`. The negative valuation forces H to have negative valuation. The highest power in `f(H)` then strictly dominates, so the F face must be a ninth/twelfth power up to a scalar. Its root multiplicities 24/21 contradict this. Zero is excluded without any Jacobian equation.

Fresh [symbolic source-map checks](/home/ubuntu/jc2/box/t2t3-compressor-gate-20260906/major_face_audit.json) verify the **actual major faces in all three charts**. For either 99 branch, minimum weights `3r+4z` for `h₃,C₂,C₃,D,C` are `32,64,96,192,291`, and

\[
(h_{3,\mathrm{face}})^3+C_{2,\mathrm{face}}h_{3,\mathrm{face}}
+C_{3,\mathrm{face}}=(\pi^3-1)^8
\]

including cancellation of the free inner parameters. Thus h has weight 96; F/G corrections exceed weights 288/192 by at least three. In free-mean D108, h has weight 140 and face `(π⁴−1)⁷`, D/C have weights 280/424, and corrections exceed F/G’s 420/280 by at least four. This verifies powers 24/16 and 21/14. The report’s later minor split faces alone would not give this contradiction.

Hence `j∈k×`, with no `j=1` gauge or explicit j coordinate/localizer needed. This is a field-point statement; degree additivity is not applied in a possibly nonreduced universal quotient. No scheme isomorphism to a Jacobian-equation presentation is claimed.

**The circuit quotient and counts.** Let `A=Q[s₁,…,s₄₄₉]` in the precise semantic order, and `B=A[X₁,…,X₇₁₃₆]`. Each circuit definition is `d_i=X_i−f_i(s,X_{<i})`. Recursive evaluation defines `φ:B→A`; successive monic elimination proves `ker φ=(d_i)` and

\[
B/(d_i,c_1,\ldots,c_r)\cong A/(\phi(c_1),\ldots,\phi(c_r)).
\]

There is no division by a parameter and no vanished-leader branch. Primitive integral normalization multiplies each nonzero image by a nonzero rational unit, so it preserves this ideal over Q.

Fresh replay parsed 11,606 rows: 7,136 definitions and 4,470 constraints. Every pivot occurs alone linearly with coefficient +1; dependencies precede it; all 7,136 exact local round trips vanish. The independent type check identifies pivots *exactly* with graph variables, disjoint from semantic coordinates. No constraint is consumed. `graph-replay.json` retains the matching ledger SHA and driver custody.

“No constraint pivot” applies to this conversion; earlier source parametrization already incorporated rational constraint-derived eliminations. `build_direct.py:153–166` declares semantic order, solver permutation and alias bijection; `425–500` filters zero images and emits Q/aliased integer terms together.

An independent support computation bounds every possible nonzero site. A deterministic specialization modulo the checked prime 1,000,000,007 makes **every candidate generator nonzero**, with invertible denominators. This proves an exact lower bound matching the support upper bound. No identity is inferred from a zero specialization. `support-counts.jsonl` retains assignments and value hashes; these are not ideal solutions or Gröbner evidence.

| case | semantic variables | old circuit constraint slots | zero images | nonzero direct rows |
|---|---:|---:|---:|---:|
| 99 δ=2 | 449 | 4,470 | 1,716 | 2,754 |
| 99 δ=5/2 | 447 | 4,470 | 1,716 | 2,754 |
| 108 free mean | 507 | 7,022 | 3,826 | 3,196 |

**Executable defect:** `add`/`mul` delete zero coefficients (`build_direct.py:221–250`), and the strict T₃ loop visits only `T3.items()` (`634–636`). Its raw/emitted counts must agree: 962/962 or 1,514/1,514. But `EXPECTED` demands 2,539/962 or 5,123/1,514; `finish:655–661` asserts both. The frozen full builder cannot close normally. Actual visited raw totals are 2,893/2,893/3,413; the differences are old graph slots with identically zero images. Fix by visiting missing zero slots or separating old-circuit statistics from direct traversal counts. No nonzero polynomial changes. Frozen drivers remain untouched.

**Literal subset.** δ=2 has no residual source rows. `build_t2_certificate.py:35–88` selects 462 `T2_Rhigh` rows, `T2_face_55`, and three inverse equations. Its H/v/U/R construction matches `build_direct.py:528–560`, its six face summands match `575–584`, and its target/inverse rows match `591–596,645–647`. Full-builder support guards skip only zero coefficients. Both use the same ring and primitive emitter; the omitted Q constant lies beyond the cap.

Semantic order SHA: `ee778e93b4293b9399761911d80dd71dd63b5fa95d21055cf50cd0db51428a4b`. Move `Z55,Zrho,Z3` to the final `dp(3)` block and map solver coordinate i to `v_i`. The preceding matrix block is global: its first row is strictly positive and its identity completion omits a minor of determinant 63. Thus a Singular unit means a polynomial-ideal unit, not merely a local-order unit.

Independent recursive evaluation of original graph constraints `T2_Rhigh_62_50`, `_75_48`, `_97_33` gives 16, 1,467, 2,803 terms. Their primitive hashes and all three inverse hashes match fresh certificate labels; see `graph-generator-samples.json`.

The fresh frozen-driver rebuild completed rc0 in 1,192.235 s, peak RSS 89,536,168 KiB: **449 variables, 466 generators, 6,448,959 terms** (4,607,718 in the face row). Stream SHA `a78c6a46e4b50dec6df51712c9c4b8d3c717b52490488d6819563cb5e18044fe`; exact-Q file SHA `a604ed314ced1a33ff46e43081c2222430f24bde96a10405a3a8562ec6dccbbc`; alias file SHA `7f593b87e40f02dbdb91f9b22aace6989f4a4d2092d9903276675b3265c7b572`. All match the charged artifacts. `subset-rebuild-check.json` independently binds fresh file hashes, labels and six graph samples, closing the historical metadata’s different driver-hash labels.

`make_sound_prefix.py:55–108` preserves ring/alias map, requires a later completion-witness row, checks paired rows and appends production inverse polynomials. Fresh synthetic worker controls passed ring/map/literal-polynomial checks and rejected an alias perturbation and missing later row (`prefix_control_result.json`). Reordered localizer factors are equal polynomials.

**Exact-Q unit scope.** In the declared ring let `J₅₅` be the subset and `I₂` the full δ=2 ideal. Literal membership gives `J₅₅⊆I₂`. A completed, validated exact-Q proof of `1∈J₅₅` proves `I₂=(1)`, also after characteristic-zero field extension, and kills the isomorphic circuit chart. A completed full stream is unnecessary for this implication.

The algebraic kill is the normalized **(99,66), δ=2, stage-8 source parametrization**, with upper-R equations, top T₂ coefficient equal to nonzero `leader55`, and `rho≠0`. `J₅₅` contains no T₃ recurrence/strict/face rows: `t3eq,t3_fq` are free and `Z3*lambda3−1` is a Laurent factor. The contradiction therefore needs neither T₃ attainment nor the compressor. Conversely, subset points lack the full T₂ strict equations, so leader inversion alone does not license Theorem B there.

This excludes compatible canonical attained-T₂+T₃ data mapping here. For Keller pairs/minimal counterexamples, the source classification and allowed normalization/translation must supply that route. Minimality is not needed for ideal containment. Gauges remain `beta=1` and the transported 99 translation slice, with free nonzero separation/leaders and no `j=1` normalization.

This would not kill δ=5/2, D108, other configurations, or the Jacobian conjecture globally; it proves no census completeness or missing route into this chart. Modular unit alone does not prove characteristic-zero unit; subset nonunit does not prove full-ideal properness; timeout proves neither emptiness nor existence. Acceptance must bind input/ring, reject CAS/parser errors even at rc0, and supply a complete exact result or checked rational cofactor identity.

**Further correction.** Frozen direct lines 33–40 wrongly deny that a proper complete ideal could supply a Keller pair. Denormalize h/D/C tables with degrees `k,2k−1,3k−1` via `P_phys=x^N K_P(1/x,y/x−1)`. Their checked supports `r+z≤N` make these actual polynomials. Using physical h/D/C,

\[
F=h^3+(3D+a)h/2+C,\qquad G=h^2-bh/3+D.
\]

In extraction coordinates, the normalized Q differs from the six-summand `Q_*` by `q*t^(6k−2)+(Rraw−Rlow)*(3H²/4+t*v)` (frozen instrument:164–170). Upper-R rows kill the latter term. The scalar term has depth 196/214>qcap 161/176; F/G corrections begin at 32/35>defects 20/25. Full strict/face rows therefore give actual degrees 55/63 and 145/227, choosing passive coefficients zero. The preceding proofs force Keller at every field-valued full-ideal point. Properness would imply existence over Qbar, without exhibited coordinates, a canonical resultant lift, or verification of omitted source conditions. No properness is asserted.

**Final custody.** The charged harvest resolves the placeholders: both production jobs reached 9,000-second caps. Singular stops at `ALL_ROWS_PARSED`, `BEGIN_STD`, `halt 1`; the modular basis is empty. Neither has algebraic force. δ=2 remains **OPEN**; other charts are undecided.

This audit launched only `i-05c263805fb29259f`, `r7i.8xlarge`, private IP `172.30.0.240`, Owner `t2t3-compressor-gate-astra-20260906`, at 2026-09-06 08:30:09 UTC. All polynomial expansion and generator-stream scratch stayed on that worker. AWS confirmed **terminated**; the recorded termination request was 08:54:20 UTC. Only compact evidence was retained: notes plus this sealed report are below 0.5 MB, within the 2 MB host-write cap. `evidence.sha256` binds the retained files.

FALLACY-v2: attainment is not inferred from floors; major/minor faces and source/target variables remain separate; zero Jacobian, ring maps and containment are explicit. No `sat()` wrapper, vanished-leader division, raw-remainder heuristic or canonical-lift inference is used. No new exit price is asserted, so no charge-basis declaration applies.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15577`.
- Body SHA-256:
  `22f264a75cd24c757b3884437359f16908aa31b8dacc28f7626f967f6aa57d83`.
- Frozen basis: `36db4240df0b96565569a65780af015292051537`.
