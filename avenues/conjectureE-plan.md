# Conjecture E ("remainder vanishing") — statement, smallest instances, and a laptop-scale test plan

Source: arXiv:2205.12792v2, *On the two-dimensional Jacobian conjecture: Magnus' formula
revisited, II*, Glidewell–Hurst–Lee–Li (source file `Jac_conj2appd.tex`, 2022-06-21; fetched
2026-07-29 from `arxiv.org/e-print/2205.12792`). Lettered conjectures share one `\Alph` counter,
so in order of appearance: `\label{Jac_conj}`=**A**, `Jac_conj2`=**B**, `Jac_conj3`=**C**,
`Jac_conj4`=**D**, `Jac_conj5`=**E** (§4, "The remainder vanishing conjecture").
Macro dictionary: `\lowerF`=u_F, `\upperF`=v_F, `\lowerE`=u_E, `\upperE`=v_E, `\epell`=ε,
`\frmm`=𝔪, `\frj`=𝔧, `\g`=α. Proved chain: **E ⇒ D** (§5 lemma) **⇒ C** (Lemma `DtoC`)
**⇒ B** (Lemma `CtoB`) **⇒ A** (Lemma `BtoA`), and **A ⇔ JC2** (Abhyankar's degree-divisibility
equivalence, [vdEssen Thm 10.2.23], restated as A in §1). No converse implication is claimed for
E, D, or C.

---

## 1. Precise statement of Conjecture E, with all objects defined

Ambient ring `R = C[x,y]`; `[f,g] = f_x g_y − f_y g_x`. For a direction `w=(u,1)`,
`f = Σ_j f_j^w` is the w-homogeneous decomposition (`f_j^w` = span of `x^i y^k` with `ui+k=j`);
`w-deg` = top such `j`. `N^0(f)` = convex hull of `supp(f) ∪ {(0,0)}`.
`T_{m,n} = {(x,y): 0 ≤ y ≤ n, 0 ≤ x ≤ m+n−y}` (trapezoid).
`𝕋` = Tschirnhausen polynomials `α(z) = z^k + e_{k−2}z^{k−2} + ... + e_0` (monic, no `z^{k−1}`).
`ℰ(f) = {E : f = α(E), α ∈ 𝕋}`; `f` is **principal** iff `ℰ(f) = {f}`.
`[r]_+ = max(0,r)`.

### Discrete parameters (eq. `uLetc1`/`uLetc2` ≈ (4.1)/(4.2))

- `(a,b,m,n) ∈ 𝒬 = {m<n, a|m, a|n, gcd(a,b)=1, 2 ≤ a < b}` (positive integers).
- `δ ∈ Δ` = positive common divisors of `m/a` and `n/a`.
- `ε = 1/(m(n−m))`; `i ∈ ℐ = {i ∈ [0, m(n−m)] : m|i or (n−m)|(i+1)}` (exclusive by Lemma `not_both`).
- Case split:
  - if `m | i` (so `u=0`, `w=(0,1)`): `L = x+1`, `u_E = (n−m)/(δa)`, `u_F = ⌊i(n−m)ε⌋`,
    `R_2 = C[x^{±1}, y^{±1/m}]`, `S(τ) = (x+1)y^{n/m}`;
  - if `(n−m) | (i+1)` (so `u=1`, `w=(1,1)`): `L = x+y`, `u_E = m/(δa)`, `u_F = ⌊(i+1)mε⌋`,
    `R_2 = C[x^{±1/n}, y^{±1}]`, `S(τ) = x^{m/n}(x+y)`.
- `d = um+n`, `e = bd/a`, `𝔪 = d+e−u−2`, `v_E = d/(δa)`, `r = gcd(m,n)`,
  `a_i = ⌊(i+1)mε⌋`, `b_i = a_i + ⌊i(n−m)ε⌋`.
- `v_F` (three cases):
  - `u_F + (un−um+m)(a−1)/a − 1` if `i > m(n−m)(a−1)/a`;
  - `u·a_i + b_i − 1` if `i ≤ m(n−m)(a−1)/a` and `aδ⌊i(n−m)ε⌋/(n−m) = aδ⌊(i+1)mε⌋/m ∈ Z`;
  - `u·a_i + b_i` otherwise.

### Formal (tilde) layer

`R_1 = C[Γ̃_0..Γ̃_{v_E−1}, x̃_0..x̃_{v_F}, c̃_1, c̃_2, ...]`, and in `R_1[τ]`:

    F̃° = Σ_{j=u_F}^{v_F} τ^{j−u_F} x̃_j  +  Σ_{j=0}^{u_F−1} x̃_j
    Ẽ° = τ^{v_E−u_E} + Σ_{j=u_E}^{v_E−1} τ^{j−u_E} Γ̃_j + Σ_{j=0}^{u_E−1} Γ̃_j

Grading: `deg τ = n/m` (u=0) or `m/n+1` (u=1); `deg Γ̃_j = j − [j−u_E]_+ deg τ`,
`deg x̃_j = j − [j−u_F]_+ deg τ`, so `deg(τ^{[j−u_E]_+}Γ̃_j) = deg(τ^{[j−u_F]_+}x̃_j) = j`.
Homogenization `h(f) = Σ_{j≤deg f} f_j t^{deg f − j}`; set

    H = h( α°(Ẽ°) + F̃° )  ∈ R_1[τ, t]      (top term τ^{δa(v_E−u_E)}, t-degree d).

Fractional powers `H^A` (`A = (e−β)/d`) are defined by the generalized binomial series
(eq. `eq:xA` ≈ (4.4)) with `y_0` = leading τ-power; `[·]_{t^μ}` and `[·]_{τ^{−j}}` extract
coefficients. When `rA ∈ Z·(r/d)`… concretely: `[H^{(e−β)/d}]_{t^μ} ∈ R_1[τ^{±1}]` has integer
τ-exponents exactly when `r(e−β)/d ∈ Z`, which defines the admissible index set

    B_max = {β ∈ [1,𝔪] : r(e−β)/d ∈ Z}.

For `B ⊆ B_max` and `μ ∈ [0,𝔪]` (eq. `mathfrakversion2` ≈ (4.5)):

    G̃_{B,e−μ} = [H^{e/d}]_{t^μ} + Σ_{β ∈ B∩[1,μ]} c̃_β [H^{(e−β)/d}]_{t^{μ−β}}  ∈ R_1[τ^{±1}],

`𝔧(μ) = min{𝔧 ≥ 0 : [G̃_{B,e−μ}]_{τ^{−j}} = 0 for all j > 𝔧}` (identically in `R_1`), and for
`k ∈ [1, 𝔧(μ)]` the "k lowest τ-tail, re-homogenized":

    G̃_{B,e−μ,k} = Σ_{j=𝔧(μ)+1−k}^{𝔧(μ)} τ^{𝔧(μ)−j} [G̃_{B,e−μ}]_{τ^{−j}}  ∈ R_1[τ].

### Concrete layer and "supported"

Fix `E°, F° ∈ C[x,y]`, `α° ∈ 𝕋`, and a ring hom `S ∈ 𝒮^w ⊂ Hom(R_1[τ], R_2)` with `S(τ)` as
above, subject to (eq. `mathfrakversion` ≈ (4.3)):

    S(c̃_β) ∈ C for β ∈ [1,𝔪];
    F° = S(F̃°),  w-deg F° ≤ v_F,  (F°)_j^w = S(τ^{[j−u_F]_+} x̃_j)  for j ∈ [0,v_F];
    E° = S(Ẽ°),  w-deg E° ≤ v_E,  (E°)_j^w = S(τ^{[j−u_E]_+} Γ̃_j)  for j ∈ [0,v_E−1];
    deg α° = δa.

(Since `L^{-1} ∉ R_2`, membership `S(x̃_j) ∈ R_2` silently forces `L^{j−u_F} | (F°)_j^w` for
`j ≥ u_F`, and likewise `L^{j−u_E} | (E°)_j^w`: these are the w-divisibility conditions.)
Write `x_j = S(x̃_j)`, `Γ_j = S(Γ̃_j)`, and let `P_k : R_2 → R_2/L^k` be the projection
(`R_2/L` is a domain). **Definition (`supported`, eq. `soeq1` ≈ (4.6)).** `B ⊆ B_max` is
*supported w.r.t. `(S,E°,F°,α°)`* iff

    P_k( S(G̃_{B,e−μ,k}) ) = 0   for μ ∈ [0,𝔪], k ∈ [1,𝔧(μ)],   and
    S(G̃_{B,e−μ}) = 0            for μ ∈ [e+1, 𝔪].

> **Conjecture E (`Jac_conj5`).** Assume the hypotheses of Definition `supported`.
> Fix `ℓ ∈ [u_F, v_F]`. Suppose `B` is supported w.r.t. `(S,E°,F°,α°)` and `P_1(x_j) = 0`
> for `j ∈ [ℓ+1, v_F]` (vacuous when `ℓ = v_F`). If `E°` is a principal polynomial, then
> either `P_1(x_ℓ) = 0` or there exists a **proper subset** of `B` which is supported
> w.r.t. `(S,E°,F°,α°)`.

Iterated downward over `ℓ`, this yields `P_1(x_ℓ)=0` for all `ℓ ∈ [u_F,v_F]`, i.e. one more
factor of `L` in every `(F°)_j^w` — exactly the step `i → i−1` of Conjecture D's induction.

**Relation to the generalized Magnus expansion** (Theorem `prop:Magnus_formula_equivalence`,
from paper I = arXiv:2201.06613): if `[F,G] ∈ C`, `d = w-deg F`, `e = w-deg G`, `r` maximal with
`F_d^{1/r} ∈ C[x,y]`, then there are unique constants `c_0 ≠ 0, c_1, …, c_{d+e−u−1−1}` with

    G_{e−μ} = Σ_{β=0}^{μ} c_β [h(F)^{(e−β)/d}]_{t^{μ−β}}   for μ ∈ [0, d+e−u−2],

and `c_β = 0` unless `r(e−β)/d ∈ Z` (the paper's `c_γ`/`γ` there is a typo for `c_β`/`β`).
So `G ≈ Σ_β c_β F^{(e−β)/d}` order-by-order in the w-filtration. The "supported" system is the
*shadow* of this expansion when `F = α°(E°) + F°`: the `P_k`-conditions say the fractional-power
tails (negative τ-powers) cancel mod `L^k`, and the `μ ∈ [e+1,𝔪]` conditions say the expansion
truncates — i.e. "a polynomial `G` could exist". Crucially, **no actual `G` and no Jacobian pair
appear in E's hypotheses**: `(S, E°, F°, α°, B)` is abstract data.

---

## 2. Smallest nontrivial instances

`𝒬`-minimal quadruple: `(a,b,m,n) = (2,3,2,4)` (forced: `a≥2`, `a|m ⇒ m≥2`, `a|n, n>m ⇒ n≥4`,
`b≥3`). Then `Δ = {1}` so `δ = 1`, `ε = 1/4`, `m(n−m) = 4`, `ℐ = {0,1,2,3,4}`,
threshold `m(n−m)(a−1)/a = 2`. Verified table (script-checked against the formulas, and the
formulas cross-checked against the paper's own Example: `(2,3,4,8), δ=1, i=15 ⇒ u=1, d=12, e=18,
u_E=2, v_E=6, u_F=4, v_F=7` — exact match):

| i | w | L | d | e | 𝔪 | B_max | u_E | v_E | u_F | v_F | ℓ range |
|---|------|-----|---|---|----|-------------|-----|-----|-----|-----|---------|
| 0 | (0,1)| x+1 | 4 | 6 | 8  | {2,4,6,8}   | 1   | 2   | 0   | −1  | ∅ (vacuous) |
| 1 | (1,1)| x+y | 6 | 9 | 12 | {3,6,9,12}  | 1   | 3   | 1   | 2   | {1,2} |
| 2 | (0,1)| x+1 | 4 | 6 | 8  | {2,4,6,8}   | 1   | 2   | 1   | 1   | {1} |
| 3 | (1,1)| x+y | 6 | 9 | 12 | {3,6,9,12}  | 1   | 3   | 2   | 3   | {2,3} |
| 4 | (0,1)| x+1 | 4 | 6 | 8  | {2,4,6,8}   | 1   | 2   | 2   | 2   | {2} |

**Primary instance `P1`:** `(2,3,2,4), δ=1, i=4, w=(0,1), ℓ = u_F = v_F = 2` (hypothesis
`P_1(x_j)=0, j∈[3,2]` vacuous — the "top of the induction" case the paper itself flags).
Concrete shape (`e/d = 3/2`, `τ ↦ (x+1)y²`):

- `Ẽ° = τ + Γ̃_1 + Γ̃_0`, so `E° = (x+1)y² + g₁(x)·y + g₀(x)`, unknown `g₁, g₀ ∈ C[x]`.
- `α° = z² + e₀` (Tschirnhausen of degree `δa = 2`), unknown `e₀`.
- `F̃° = x̃_2 + x̃_1 + x̃_0` (no τ powers since `u_F = 2`); `F° = q₂(x)y² + q₁(x)y + q₀(x)`,
  and `x_j = (F°)_j`, so the conclusion `P_1(x_2)=0` is literally `(x+1) | q₂`.
- `H = τ² + 2Γ̃₁τ·t + (2Γ̃₀τ + Γ̃₁² + x̃₂)t² + (2Γ̃₀Γ̃₁ + x̃₁)t³ + (Γ̃₀² + e₀ + x̃₀)t⁴`.
- Exponents needed: `(e−β)/d = 3/2, 1, 1/2, 0, −1/2` for `β = 0,2,4,6,8` (all with integer
  τ-powers, since `r=2`); series truncated at `t^8`; `𝔧(μ) ≤ 5`, so `P_k` for `k ≤ 5`.
- **Principality of `E°` is automatic here**: `E° = α(E)` with `deg α ≥ 2` would force
  `w-deg E = 1` and `(top of E)² = (x+1)y²`, impossible since `x+1` is not a square in `C[x]`.
  (Same for the u=1 instances: `x(x+y)²` is not a perfect power.) So the principality side
  condition drops out of the smallest instances entirely.

**Even smaller sibling `P2`:** same tuple, `i = 2`, `ℓ = u_F = v_F = 1`: `F̃° = x̃_1 + x̃_0`,
`F° = q₁(x)y + q₀(x)`, conclusion `(x+1) | q₁`. Fewest unknowns of any nonvacuous instance.

Plain-language content of `P1`: *if the fractional-power tails of
`(α°(E°) + F°)^{3/2}` can be cancelled modulo powers of `(x+1)` by corrections
`Σ_{β∈B} c_β (…)^{(6−β)/4}` (B supported), then `(x+1)` must divide the top remainder piece
`q₂` — unless some proper sub-collection of the corrections already achieves the cancellation.*

Secondary targets, in order: `i=2` and `i=4` (u=0, tiny), then `i=1, 3` (u=1, needs `x^{1/2}`
bookkeeping), then `(2,3,4,8), δ∈{1,2}, i=15` to cross-check against the worked examples in
paper III ([GHLL3], see the authors' site) before trusting any surprising verdict.

---

## 3. Computational test plan (exact arithmetic over Q)

**Claim shape.** For fixed `(a,b,m,n,δ,i,ℓ)` and fixed `B ⊆ B_max`, "B is supported" is a finite
system of polynomial equations over Q in finitely many scalar unknowns; Conjecture E's instance
asserts emptiness of {supported} ∩ {P_1(x_ℓ) ≠ 0} ∩ {no proper supported subset} (principality
being automatic here). Refutation = one explicit solution; verification = emptiness certificate.

**Unknowns (instance `P1`, with x-degree caps from the intended application — see honesty note):**
`supp(E°) ⊆ T_{1,2}` ⇒ `deg g₁ ≤ 2, deg g₀ ≤ 3` (7 coeffs); `e₀` (1);
`supp(F°) ⊆ T_{2,4}` ⇒ `deg q₂ ≤ 4, deg q₁ ≤ 5, deg q₀ ≤ 6` (18); `c_β, β ∈ B` (≤4);
plus one saturation variable `s`. Total ≤ 30 unknowns (`P2`: ≈ 17).

**Algorithm.**
1. *Layer 1 (formal).* Work in `Q[Γ̃_j, x̃_j, c̃_β, e₀][τ^{±1}, t]/(t^{𝔪+1})`, encoded as a
   jc.py-style dict `{(τexp, texp): Coef}` with `Coef` = sparse monomial dict in the symbol
   indices (exactly `lib/jc.py`'s `BiPoly`/`Coef`; `padd`/`pmul`/`cadd`/`cmul` are
   exponent-sign-agnostic and reusable as-is). Build `H`; compute
   `H^A = τ^{2A·…}·Σ_k C(A,k) u^k` with `u = H/τ^{lead} − 1` (t-adically nilpotent), using
   `fractions.Fraction` scalars (the dict code paths accept them) or pre-clearing `2^K`
   denominators to stay in Z. Assemble `G̃_{B,e−μ}`, read off `[τ^{−j}]` coefficients,
   compute `𝔧(μ)`, form `G̃_{B,e−μ,k}`.
2. *Layer 2 (substitution S).* Change chart `z = x+1` (u=0), so `S(τ) = z·η^n` with `η = y^{1/m}`
   is a Laurent *monomial* (u=1 analog: `w = x+y`, `ξ = x^{1/n}`, `S(τ) = ξ^m w`; cf.
   `lib/chartelim.py` for the chart-shift pattern). Map each `R_1`-monomial to a product of the
   capped symbolic polynomials `Γ_j, x_j` (unknown coefficients as `Coef` variables) via `pmul`;
   `τ^{pos} ↦ z^{pos}η^{n·pos}`. `P_k` = *drop every monomial with z-exponent ≥ k* — trivial on
   the dict representation. Each condition is w-homogeneous ⇒ a single fixed η-power times a
   polynomial in `z`; harvest one scalar equation per z-coefficient. Yield: ≈ 60–100 equations
   of degree ≤ ~9 (sparse) for `P1`.
3. *Nonvanishing.* Add `s · q₂(−1) − 1 = 0` (i.e. `P_1(x_ℓ) ≠ 0`), the same saturation trick as
   `SystemA` in `lib/jc.py`.
4. *Emit and solve.* Reuse `SystemA`'s emitters verbatim (`_poly_str`, `write_msolve`,
   `write_singular`) into `systems/`, run msolve GB mod 65521 first (evidence lane), then char 0
   (certificate lane) — the repo's standard two-lane runbook. Optionally shrink first with the
   `lib/reduce.py` unit-linear elimination cascade.
5. *Decision.* For each of the ≤ 2^4 = 16 subsets `B ⊆ B_max` (start with `B = ∅`, which has no
   proper subset — there E claims `P_1(x_ℓ)=0` outright — then `B_max`):
   - GB = [1] for all B ⇒ instance verified (in the strong form: the proper-subset escape was
     never needed).
   - GB ≠ [1] for some B ⇒ extract witness points (msolve rational parametrization if 0-dim;
     else slice), and for each witness *evaluate* (via `SystemA.substitute`-style exact
     plugging) whether any proper `B' ⊂ B` is supported. Only a witness failing **all** proper
     subsets refutes E.
6. *Validation fixture (run first).* `E° = (x+1)y² + xy + x³` (say), `α° = z² + e₀` with
   `e₀ ≠ 0`, `F° = 0`, honest `G = E°³ + λE°` (`[F,G] = 0 ∈ C`, `N⁰(G) = T_{3,6}`): the Magnus
   theorem guarantees `B_max` is supported with the induced `c_β`; the pipeline must confirm
   this identically. Unit-test the binomial series against `(1+t)^{±1/2}` truncations.

**Expected sizes.** Layer-1 series: ≤ a few hundred `R_1[τ]`-monomials per `t^μ` slot
(products of ≤ 8 symbols). Layer-2 expansion: bounded by z-truncation (`k ≤ 5`) — well under
10^5 dict terms; seconds-to-minutes in stdlib Python. GB: 17–30 variables, comparable to or
smaller than the campaign's solved `reg_9_24_c3` (57 vars); mod-p in minutes, char-0 plausibly
hours on a laptop for `P2`/`P1`. New code: ~300 lines (t-series wrapper, binomial power,
S-substitution, harvest), everything else reused.

**Honesty note on degree caps.** As literally stated, E quantifies over *all* `E°, F° ∈ C[x,y]`
with the given w-structure — no x-degree bound. The caps above define a stratum. A
counterexample found under caps refutes E as stated, unconditionally. A capped verification is
stratum-relative — but the caps `N⁰(E°) = (1/δa)T_{m,n}`, `supp(F°) ⊆ N⁰(F)∖𝒩''` are exactly
what the E⇒D proof instantiates (Definitions `def:Ecirc`, `def:VF`), so a capped verification
covers everything the implication chain uses at this parameter node; raise caps to extend.

---

## 4. What a counterexample to E would and would not imply

Verified reading of the paper: E ⇒ D ⇒ C ⇒ B ⇒ A, and A ⇔ JC2; the paper says only "we will
show that the following conjecture implies the Jacobian conjecture" (§4, before `Jac_conj5`) —
**E is sufficient for JC2, never claimed necessary.**

A small-instance counterexample (concrete `(S, E°, F°, α°, B)` supported, `E°` principal,
`P_1` tail vanishing, `P_1(x_ℓ) ≠ 0`, no proper supported subset) **would**:
- disprove Conjecture E and void the program's route E ⇒ D, i.e. the announced plan of papers
  III/IV ([GHLL3], [GHLL4] "in preparation") to prove JC2 via E — the induction engine dies;
- say nothing further: it would **not** disprove JC2, and not even disprove D, C, or B, because
  E's data is abstract — there is no polynomial `G` and no Jacobian pair in it; the supported
  system only mimics what Magnus' formula would produce *if* a mate `G` existed. The specific
  `(E°, F°)` need not extend to any `F` satisfying B(1)–(5).

Contrast (levels where a counterexample *would* hit JC2): a counterexample to **A** or **B** is
a genuine Jacobian pair with degree ratio `a:b`, `gcd(a,b)=1`, `2≤a<b`, contradicting JC2 via
Abhyankar's equivalence; a counterexample to **C**/**D** kills JC2 only if its `[F,G] ≠ 0`
(with `[F,G] = 0` it kills only the program). Conversely, verifying E in small instances proves
nothing about JC2 (E must hold for *all* parameters) — it is program evidence only.

Caveats before announcing a kill: (i) the TeX source contains commented-out sharper case-split
refinements of E (after `Jac_conj5`) — check any counterexample against paper III/IV's final
formulation; (ii) confirm the witness respects the exact normalizations (`c̃`-constancy, the
`1·x^{m/aδ}y^{n/aδ}` term in `E°`, Tschirnhausen `α°`); (iii) char-0 certificate, not just mod-p.
