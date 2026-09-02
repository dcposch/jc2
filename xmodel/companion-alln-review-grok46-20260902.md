# Hostile review: COMPANION-ALLN — THEOREM COLLAPSE-N and THEOREM COMPANION-EXISTS

**Reviewer.** grok-4.6 (different-model gate).
**Date.** 2026-09-02.
**Lane.** `COMPANION-ALLN-REVIEW`.
**Charge.** Default to refutation. Desk-scale exact reasoning plus sympy 1.14.0 over `Q`. A false COLLAPSE-N wrongly retires `(M')` as a gate; a false COMPANION-EXISTS wrongly keeps `(9,6,2)` alive. `FALLACY-v2` in force. No `charge_basis` line: this review asserts no new exit price.

**Headline.** All five charged items are **CONFIRMED**. The two UNREVIEWED theorems survive independent re-derivation and machine replay. The identity charged to constrain the companion is information-free once `(LOC)`, `(AGG)` and Lemma A are granted; the forced companion datum is realized by an explicit three-row family, including at `(9,6,2)`. This licenses the producer’s `CLOSED-NEGATIVE as an obstruction lane` at the exact scope of those two theorems. It does not license a Keller map, and it does not close `OPEN[REP-96-BM-FACTORISATION]` or `OPEN[REP-96-SOURCE-IS-C2]`.

## Verdict table

| # | Claim | Verdict |
|---|---|---|
| (1) | THEOREM COLLAPSE-N, including the §2.2 cancellation and the §2.5 controls | **CONFIRMED** |
| (2) | THEOREM COMPANION-EXISTS at three independent spots, plus Corollary MULT-2 | **CONFIRMED** |
| (3) | `(9,6,2)` witness `xi |-> (xi^3+xi+1, xi^2+3)` and the §5.4 `a_p` census | **CONFIRMED** |
| (4) | Lemma CONTACT, and the §5.5 item 3 `M <= K` resultant-degree bookkeeping | **CONFIRMED** |
| (5) | Chau Cor 1 / Cor 2 inversions against `xi |-> (2 xi^3, xi^2)` | **CONFIRMED** |
| — | Producer `COMPANION-CURVE-ALLN: CLOSED-NEGATIVE as an obstruction lane` | **CONFIRMED** at the two-theorem scope |

Three nonblocking observations, none of which moves a verdict, are recorded in §6.

---

## 0. Custody, method, scope

Frozen copies were hashed with `shasum -a 256` **before any reading**. Both match the charge exactly:

```text
bf6b82e91c9441fea1998fb157289f44becf7cf6603b61b3c21c229272f4b943  companion-curve-alln-opus5-20260902.md
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  rep-96-inner-opus5-20260901.md
```

Below: **CC** = the charged companion-curve report, **REP** = the charged inner report. Primary literature opened independently, hashed on this host before reading:

```text
8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f  refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf
```

This matches CC SS0 / SS9. Chau was rasterized and read as images (pages 1–3); `pdftotext` on this file is glyph salad and was not used as a source.

One non-charged campaign file was grepped, and is disclosed because a load-bearing sign was checked against it: `xmodel/reducible-all-n-r2-opus5-20260901.md` for the printed `(LOC)` and `(BUD)` displays. The theorem under review takes `(LOC)` as a hypothesis, so the grep is a campaign-sign audit, not a dependency. `round1033-sheet-gate-opus5-20260831.md` was **not** opened; the block-free `(M')` is taken as quoted in REP SS7 R4 and restated in CC SS2.1.

**Method.** Independent derivation of the COLLAPSE-N cancellation (not a line-check of CC SS2.2). Exact sympy over `Q`: resultants, gcds, squarefree decompositions, a lex Groebner basis for the `D_1` singular locus, integer Euler arithmetic, and a randomised identity harness. No floating point enters any PASS/FAIL. No `msolve`, no `qqideal`, no `jc2-lean`, no ledger edit.

This is not an exit-price assertion.

---

## 1. THEOREM COLLAPSE-N — CONFIRMED

### 1.1 Independent derivation of the cancellation

Objects, fixed as in CC SS2.1–2.2 and REP SS7 R4. `A_F = union_i D_i` is a reduced affine plane curve; `Sigma := Sing(A_F)`; `sigma := |Sigma|`; `eta_i : D~_i -> D_i` the normalisation of the `i`-th irreducible component, with `D~_i` smooth and irreducible; `chi~_i := chi_c(D~_i)`; `r_{i,p} := # eta_i^{-1}(p)` (zero off `D_i`); `sigma_i := |Sigma n D_i|`; `nu_i := sum_{p in Sigma n D_i}(r_{i,p}-1)`; `a^{(i)} = N - W_i`; and `(LOC)` at every `p in Sigma`,

```text
    a_p + sum_i r_{i,p} W_i + K_p  =  N .
```

Block-free `(M')` is the statement

```text
    LHS  :=  sum_i a^{(i)} chi_c(D_i \ Sigma) + sum_{p in Sigma} a_p
    RHS  :=  1 - N chi_c(V),     V := C^2 \ A_F ,
```

and `LHS = RHS`. Only Keller is used for `RHS`: `F` is unramified of geometric degree `N` and finite étale over `V`, so `chi_c(C^2 \ F^{-1}(A_F)) = N chi_c(V)`, and `chi_c(C^2) = 1` splits as `chi_c(F^{-1}(A_F)) + N chi_c(V)`. Compactly-supported Euler is additive on a closed subset and its complement, so `chi_c(V) = 1 - chi_c(A_F)` and

```text
    RHS  =  1 - N + N chi_c(A_F) .
```

**Stratum and normalisation.** The sets `D_i \ Sigma` are pairwise disjoint and disjoint from `Sigma`, so `chi_c(A_F) = sum_i chi_c(D_i \ Sigma) + sigma`. The map `eta_i` is an isomorphism over the regular locus of `D_i`; crossings regular on `D_i` have `r_{i,p}=1`; the only failure of injectivity is over multibranch points, which lie in `Sigma`. Thus `eta_i : D~_i \ eta_i^{-1}(Sigma) -> D_i \ Sigma` is a bijection and `chi_c(D_i \ Sigma) = chi~_i - sum_{p in Sigma} r_{i,p}`. Off-component `r_{i,p}` vanish, so that sum is `sigma_i + nu_i`. Finite-set Euler is cardinality: we subtract points of the normalisation, not branches of the image. Hence `chi_c(A_F) = sum_i (chi~_i - sigma_i - nu_i) + sigma`.

**Sum `(LOC)` and assemble.** Correction sites lie in `Sigma`, so `sum_p K_p = K_tot` and `sum_p a_p = N sigma - sum_i W_i(sigma_i+nu_i) - K_tot`. Then

```text
    LHS  =  sum_i (N - W_i)(chi~_i - sigma_i - nu_i)
            + N sigma - sum_i W_i (sigma_i + nu_i) - K_tot
         =  sum_i (N - W_i) chi~_i - N sum_i (sigma_i + nu_i) + N sigma - K_tot ,
```

the `W_i(sigma_i+nu_i)` sums cancelling in pairs. Insert `chi_c(A_F)` into `RHS`:

```text
    RHS  =  1 - N + N sum_i chi~_i - N sum_i (sigma_i + nu_i) + N sigma .
```

The two `-N sum_i (sigma_i+nu_i)` terms and the two `N sigma` terms cancel, and `sum_i (N-W_i) chi~_i - N sum_i chi~_i = - sum_i W_i chi~_i`, leaving

```text
    LHS - RHS  =  (N - 1) - K_tot - sum_i W_i chi~_i .
```

This is CC’s display, obtained without quoting it. Every singularity variable — `sigma_i`, `nu_i`, `sigma`, the split of `Sigma` into self-singularities and crossings, the `r_{i,p}` — has cancelled. The identity is an Euler tautology given `(LOC)` and the stratification, not a constraint on node counts or crossings.

A three-component symbolic expansion and the one-component degeneration both reduce to residual `0`. Under `m=1` and `chi~=1` the block-free form recovers verbatim the irreducible `(M')` of REP SS7 R4. That is the H2+H3 control CC SS2.1 claims, re-derived.

### 1.2 Sign hunt: `(LOC)`, `chi_c` additivity, Lemma A

**(LOC) sign.** Three independent locks, all the same sign.

- *Generic fibre.* On `D_i \ Sigma` one has `r_{i,p} = 1` for that `i` and `0` else, `K_p = 0`, so `(LOC)` reads `a^{(i)} + W_i = N`. This is the definition `a^{(i)} = N - W_i`. The opposite sign on the `W`-term would contradict the definition of `a^{(i)}`.
- *Witness census.* At `N = 4`, `W = (2,1)`, `K = 0`: a `D_1`-node with `r = (2,0)` gives `a_p = 0`; a transverse crossing `r = (1,1)` gives `a_p = 1`; the `D_2`-node `r = (0,2)` gives `a_p = 2`. All three lie in `{0,1,2}` and match the cluster reading of REP SS7 R4 (`2+2` letters over a `D_1`-node, `2+1` over a crossing, `1+1` over a `D_2`-node). The opposite sign produces `a_p > N`.
- *Campaign print.* The grepped CAGE display is `a_p + sum_i r_{i,p} W_i + K_p = N`. CC did not flip it.

**(LOC) as `a_p = # F^{-1}(p)`.** That is the object list of CC SS2.1. Then `sum r_{i,p} W_i + K_p` counts the sheets that have escaped to infinity over `p`. Subtracting them from `N` is the only convention compatible with a non-proper map of geometric degree `N`.

**`chi_c` additivity, and the node-as-point vs node-as-branches trap.** `chi_c(A_F) = sum_i chi_c(D_i \ Sigma) + sigma` adds **points** of `Sigma`, not branches. A node of `D_1` contributes `-r_{1,p} = -2` on the normalisation and `+1` as a point of `Sigma`: net the Euler of two points of `A^1` glued, which is the nodal curve. A crossing of two smooth branches is removed from both `D_i \ Sigma` and added once. Replacing `sigma` by `sum_{i,p} r_{i,p}` would double-count every node and fail the witness (`chi_c(A_F)` would be `-15 - 5 = -20`, not `-15`). CC uses the point count. The sign on `|eta_i^{-1}(Sigma)|` is a subtraction because those points are deleted from a smooth curve; compactly-supported Euler of a finite set is its cardinality, not its negative.

`Sing D` in the quoted `(M'-bf)` is the global singular locus of the union. Distinct irreducibles meet in `Sigma` (the union is singular at any intersection). Crossings are not omitted from the `a_p` sum, and they are not left inside `D_i \ Sing D`. No flag/place confusion between `Sing(D_i)` and `Sing(A_F)` is used in the cancellation.

**Does “given Lemma A” smuggle the conclusion?** No. The cancellation never uses `chi~_i = 1` and never uses `(AGG)`. It says `(M'-bf)` holds iff `sum_i W_i chi~_i + K_tot = N-1`. `(AGG)`/`(BUD)` is `sum_i W_i + K_tot = N-1`, a dicritical-budget identity that does not mention `chi~_i`. Subtracting gives `sum_i W_i(chi~_i-1)=0`. An irreducible smooth affine curve has `chi_c = 2-2g-n` with `n>=1`, so `chi~_i <= 1` with equality iff `D~_i \cong A^1`; every component of `A_F` owns a dicritical, so `W_i >= 1`. Those inequalities convert the weighted sum into Lemma A.

Given `(LOC)` and the stratification, any two of `(M'-bf)`, `(AGG)`, Lemma A imply the third. CC F1’s “granted Lemma A, the right side is `(AGG)`” is the dual of the theorem’s “granted `(AGG)`, equivalent to Lemma A”. Neither direction enters the cancellation. The corollary that `(M')` is not an independent RED-N gate consumes Lemma A as already promoted — the point of the corollary, not a hidden hypothesis of the identity. Pinning `D_2` cannot make cancelled variables reappear. `OPEN[REP-96-MPRIME-COMPANION]` is correctly closed NEGATIVE.

### 1.3 §2.5 controls, and the floating-`K_tot` trap

**Positive control, arithmetic.** The census `W=(2,1)`, `K_tot=0`, `chi~=(1,1)`, `sigma=17`, `(sigma_1,nu_1)=(16,4)`, `(sigma_2,nu_2)=(13,1)`, `sum a_p = 0*4 + 1*12 + 2*1 = 14` gives `chi_c(D_1\Sigma) = -19`, `chi_c(D_2\Sigma) = -13`, `LHS = 2(-19)+3(-13)+14 = -63`, `chi_c(A_F) = -15`, `chi_c(V) = 16`, `RHS = 1-4*16 = -63`. Predicted defect `(N-1)-K_tot-sum W_i chi~_i = 0`. Geometry of this census is §3; the arithmetic is exact.

**Negative controls.** Holding the census fixed and replacing `chi~_2 = 1` by `0, -1, -3` produces defects `1, 2, 4`, matching `1 - chi~_2`. The identity detects the one thing it can detect.

**Randomised control, and the reported harness failure.** Two independent samplers, exact integer arithmetic.

- *Rejection sampler* (CC’s filter: retain `sum_i W_i + sum_p K_p = N-1` and `a_p >= 0`): `4596` AGG configurations, `N in [4,12]`, `m in [2,4]`, up to 8 points. With `chi~ = 1`: **0/4596** failures of `LHS = RHS`. With `chi~_i` free in `[-3,1]`: **0/4596** mismatches against the predicted defect.
- *Constructed-AGG sampler* (partition `N-1` into weights and `K_p` from the inside): **0/5000** failures at `chi~=1`, **0/5000** free-`chi~` mismatches.
- *Unfiltered tautology* (`K_tot := sum_p K_p`, no AGG): **0/41123** mismatches. The identity does not need `(AGG)`. CC’s AGG filter is a subset, not a concealment.
- *Floating-`K_tot` trap* (draw `K_tot` independently of `sum_p K_p`, as CC says the first harness did): **35116/41123** mismatches. The trap is real. The repaired control — identifying `K_tot` with `sum_p K_p` — is actually repaired: once that identification is enforced, the identity is an algebraic tautology and the sampler cannot fail except by a coding error.

CC’s `33116` is a larger sample of the same tautology. I did not bit-reproduce that count; I reproduced the claim that a correct harness reports zero failures and that a floating-`K_tot` harness reports mass failures.

---

## 2. THEOREM COMPANION-EXISTS and Corollary MULT-2 — CONFIRMED

### 2.1 Three spot instances, chosen here

The three-row family of CC SS4.2, evaluated at three points that vary `(d,e)`, the Chau invariant `lambda = A^e/B^d`, and `m`, including one repaired `e=1` row.

| spot | `(d,e,m)` | `(A,B)` | `lambda` | row | immersive | double-point resultant |
|---|---|---|---|---|---|---|
| 1 | `(3,2,1)` | `(1,1)` | `1` | `d,e >= 2` | `gcd(a',b')=1` | degree `2` |
| 2 | `(5,3,2)` | `(2,1)` | `8` | `d,e >= 2` | `gcd(a',b')=1` | degree `36` |
| 3 | `(2,1,2)` | `(3,1)` | `3` | `e=1` repaired | `gcd(a',b')=1` | degree `2` |

Spot 1 is the family member `xi |-> (xi^3+xi, xi^2)` of which the §5.3 witness is an affine translate. Spot 2 is a non-monic, higher-multiplicity, swapped-scale instance: leading form `B^d u^e - A^e v^d = u^3 - 8 v^5` has invariant `8`, not `1`. Spot 3 is off the `(3,2)` row entirely. In all three: bidegree `(md, me)` on the nose; one place at infinity (polynomial parametrisation); immersive; double-point resultant of positive degree, hence not injective, hence singular, hence C1–C4 and C6–C7. C8 for a single curve is one point at infinity; for `deg >= 2` the intersection multiplicity with `L_inf` is the degree, so the “tangent to `L_inf`” clause is automatic. C5 constrains the profile weight `w`, not the curve. C9 is stated as generic relative to the rest of `A_F` and was not claimed as an intrinsic property of these three curves.

Birationality of the `d,e>=2` row: collisions are `xi_2 = zeta xi_1` with `zeta^{me}=1`, and `xi^{md-1}(1-zeta^{md})+(1-zeta)=0` is not identically zero for `zeta != 1` (`md >= 2`). Finite collisions imply birational onto the image. Immersivity is uniform: `b'` vanishes only at `0`, where `a'(0)=A != 0`. The same for both repaired rows.

### 2.2 MULT-2: the kill is sound, and it is silent at `(d,e)=(3,2)`

If `min(d,e)=1` and `m=1`, say `e=1`, then `deg b = 1`, so `xi |-> b(xi)` is an automorphism of `A^1` and the component is the graph of `a o b^{-1}`: a closed embedding `A^1 hookrightarrow C^2`. Gate EMB forbids a smoothly embedded `A^1` in `A_F`. No immersivity hypothesis is used (a polynomial graph is automatically immersive: the derivative is `(f',1)`). The kill applies to every component, branched or companion. Machine control: the naive `m=1`, `e=1` curve `xi |-> (xi^3+xi, xi)` is immersive with double-point resultant identically `0`.

It is silent at `(d,e)=(3,2)`: `min=2 != 1`, so `m=1` is allowed. Spot 1 and the §5.3 witness are nodal cubics, not embeddings.

The naive `e=1` row is injective at CC’s three points `(d,m)=(2,2),(3,2),(2,3)` (resultant identically zero; here `deg b | deg a`). That is why the repaired row adds `xi^{m+1}`. CC’s five repaired `e=1` pairs, three `d=1` transposes, and 21-shape `d,e>=2` grid are immersive with positive-degree resultant in every case (`8+21`).

Abhyankar–Moh was not re-proved. EMB-AUTO’s reduction to it is correct. For the exhibited family the resultant already supplies the nodes; AM is used only to extend the kill/non-embedding from these rows to every bidegree of the same shape. There is no `N_0`. The only exclusion is MULT-2’s constraint on multiplicity, not on degree.

---

## 3. The `(9,6,2)` witness — CONFIRMED

`D_1 : t |-> (t^9+12 t^5+24 t, t^6+8 t^2)` and `D_2 : xi |-> (xi^3+xi+1, xi^2+3)`, exact over `Q`.

### 3.1 `D_1` re-verified

Identity `p^2-q^3-64q-64t^2=0`. `f_1 := Res_t(p-u,q-v)` has total degree `9`, `deg_u=6`, `deg_v=9`, weighted-`(3,2)` degree `18`, weighted-leading form exactly `(u^2-v^3)^3`. CC SS3.3’s closed form equals the resultant exactly. Weighted levels: `18,14,10,6,2` only. `f_1(0,v)=-v(v^4+96v^2+1536)^2`. `gcd(p',q')=1`; `p=t(t^8+12t^4+24)`; `p'(0)=24 != 0`. Lex Groebner basis of `(f_1, partial_u f_1, partial_v f_1)` over `Q` is exactly `(u, v^4+96v^2+1536)` with the quartic squarefree: **exactly four** affine nodes, all on `u=0`, no others. `delta_aff=4` is exhausted. Chau data: `(d,e)=(3,2)`, `m_1=3`, `A=B=1`, invariant `1`.

### 3.2 `D_2`

Bidegree `(3,2)`, leading `(1,1)`, invariant `1`, matching `D_1`. `gcd(3xi^2+1, 2xi)=1`. Self-crossing: `b(eta)=b(xi)` forces `eta=-xi`; substituting into `a` yields `xi^2+1`. One pair `{i,-i}`, both mapping to `(1,2)`, both branches with `a' != 0`: ordinary node, `r=2`. Pullback `S := f_1(a(xi),b(xi))` has degree `12`, `lc=-343=-7^3`, is squarefree and irreducible over `Q`; `disc(S) != 0`, so twelve distinct complex parameters. `gcd(S,a)=1` (no crossing on `u=0`); `gcd(S, b^4+96b^2+1536)=1` (four `D_1`-nodes avoided); `xi^2+1` does not divide `S` (`D_2`-node not on `D_1`). The only non-injective pair of `eta_2` is `{i,-i}`, not among the twelve roots, so twelve distinct plane points. Each is smooth on both curves with simple pullback, so `(D_1.D_2)_p=1`: twelve transverse crossings, `r_{1,p}=r_{2,p}=1`. Bezout `27=12+15`. CONTACT bounds `12 <= 17` and `15 >= 10` hold.

### 3.3 §5.4 `a_p` census

From `(LOC)` at `N=4`, `W=(2,1)`, `K_p=0`:

```text
   4 nodes of D_1     : r = (2,0)  ->  a_p = 4 - 4     = 0
   1 node of D_2      : r = (0,2)  ->  a_p = 4 - 2     = 2
  12 crossings        : r = (1,1)  ->  a_p = 4 - 2 - 1 = 1
```

`sum a_p = 14`, `Sigma` has `17` points, `(sigma_1, nu_1)=(16,4)`, `(sigma_2, nu_2)=(13,1)`, and the Euler arithmetic of §1.3 gives `LHS = RHS = -63`. Fibre bounds `0 <= a_p <= a^{(i)}` hold (`2 <= a^{(2)}=3` at the `D_2`-node; `1 <= min(2,3)` at a crossing). `(M')` is satisfied exactly by a hand-chosen curve pair with no map in the construction.

The pair is a curve pair, not a Keller counterexample. CC SS5.5 states this and is not over-read here.

---

## 4. Lemma CONTACT and `M <= K` — CONFIRMED

### 4.1 CONTACT bookkeeping, replayed

Grade `C[u,v]` by `wt(u)=d`, `wt(v)=e`. A component of multiplicity `m_1` has weighted degree `m_1 d e` with weighted-leading form `(B^d u^e - A^e v^d)^{m_1}` (corrected Chau Cor 1, §5). The `D_2`-parametrisation is proper and birational, so `sum_{p affine}(D_1.D_2)_p = deg_xi f_1(a_2,b_2)`.

A monomial of weight `w` pulls back to `xi`-degree at most `m_2 w`, since `deg a_2 = m_2 d` and `deg b_2 = m_2 e`. The top level contributes at most `m_1(m_2 d e - 1)` because C7 cancels the leading coefficient of `B^d a_2^e - A^e b_2^d` (drop at least `1`; more drop only helps). Every strictly lower weighted level has weight `<= m_1 d e - 1`, hence pullback degree `<= m_2(m_1 d e - 1)`. Degree of a sum is at most the max of the degrees, not the sum, so

```text
    deg_xi f_1(a_2,b_2)  <=  max( m_1(m_2 de - 1), m_2(m_1 de - 1) )
                         =  m_1 m_2 d e - min(m_1, m_2) .
```

The equality `max(m_1(m_2 de-1), m_2(m_1 de-1)) = m_1 m_2 de - min(m_1,m_2)` was checked on all coprime `(d,e)` with `m_i in [1,5]`. The identity `max(d,e)^2 - de = max(d,e)|d-e|` was checked on `d,e in [1,11]`. Bezout then gives the infinity bound.

The lemma is one-sided and is used only so. Witness: affine `12 <= 17`, infinity `15 >= 10`. Two independent `m_2=2` samples against `D_1` (the family member `xi |-> (xi^6+xi, xi^4)` and a perturbation `xi |-> (xi^6+xi^3+xi, xi^4+3)`): affine degrees `21` and `27`, both `<= 34`; infinity `33` and `27`, both `>= 20`. CC’s “actual `33` twice” refers to two unspecified `m_2=2` companions; I did not recover those particular curves, and I do not need them. The bound is not an equality and is not read as one.

### 4.2 `M <= K`, `deg_u` / `deg_v` bookkeeping

Chau’s resultant `Res_y(P-u, Q-v) = R_0(u,v) x^N + ... + R_N(u,v)`, in the monic-in-`y` coordinates of Theorem 1, has `deg_y P = K d` and `deg_y Q = K e`. The Sylvester determinant is of degree `deg_y Q` in the coefficients of `P-u` and of degree `deg_y P` in the coefficients of `Q-v`. The variable `u` appears only in `P-u`, so `deg_u Res <= K e`; `v` appears only in `Q-v`, so `deg_v Res <= K d`. The leading `x`-coefficient `R_0` cannot raise those degrees.

Corrected Cor 1: the weighted-leading form of `R_0` is `C (B^d u^e - A^e v^d)^M`. Expanding, the unique highest-`u` term is `C B^{d M} u^{M e}` and the unique highest-`v` term is `C (-A^e)^M v^{M d}`. Lower-weight terms cannot cancel these (they have weight `< M d e`, while `u^{M e}` and `v^{M d}` have weight exactly `M d e`). Thus for `M >= 1` one has `deg_u R_0 = M e` and `deg_v R_0 = M d`. Combined with the Sylvester bounds,

```text
    M e  <=  K e ,     M d  <=  K d ,     hence  M <= K .
```

The printed (inverted) leading form `(A^e u^e - B^d v^d)^M` has the same `deg_u = M e` and `deg_v = M d`; the inversion does not affect this inequality.

Machine checks, not on a Keller map (there is no known Keller example with `M > 0`): (i) `(B^d u^e - A^e v^d)^M` at `(d,e,M)=(3,2,4)` has `deg_u=8=M e`, `deg_v=12=M d`; (ii) `Res_y(y^3+x y+x - u, y^2+x - v)` obeys `deg_u Res <= 2 = K e` and `deg_v Res <= 3 = K d`; (iii) a `K=2` example `Res_y(y^6+x y^2+1-u, y^4+x-v)` obeys `deg_u Res <= 4`, `deg_v Res <= 6`. In proper examples `R_0` can drop below the Sylvester ceiling (even to `deg_u R_0 = 0`, i.e. `M=0`), which is consistent with `M <= K` and is the empty-`A_F` case.

Then `sum_i deg D_i = sum_i m_i max(d,e) <= M max(d,e) <= K max(d,e) = max(deg P, deg Q)`, allowing extra scheme-multiplicities `k_i` in `M = sum k_i m_i`. This is a ceiling, not a `d_min` bound, and is gauge-dependent on the `(x,y)` side, as CC flags. It is the correct currency of `OPEN[COMPANION-R0-REALISATION]`.

---

## 5. Chau inversions — CONFIRMED

Chau, arXiv:math/0305088, Theorem 1 (p. 2, read from the page image): `P, Q` monic in `y` with leading coefficients `A, B`, `deg P = K d`, `deg Q = K e`, `gcd(d,e)=1`, and every component of `A_f` is parametrised by `xi |-> (A xi^{m d} + l.o.t., B xi^{m e} + l.o.t.)`.

Printed Cor 1: `R_0 = C(A^e u^e - B^d v^d)^M + lower`. Printed Cor 2: `c` is a `d`-radical of `B^d/A^e`. The paragraph immediately above Cor 1 prints the same two formulae for a single parametrised curve.

Charged instance `xi |-> (2 xi^3, xi^2)`: `A=2`, `B=1`, `d=3`, `e=2`, `m=1`. Directly `u^2 - 4 v^3 = 0` on the curve, and `Res_xi(u-2 xi^3, v-xi^2) = -(u^2-4 v^3)`.

| combination | value | on the instance |
|---|---|---|
| corrected `B^d u^e - A^e v^d` | `u^2 - 4 v^3` | vanishes |
| printed Cor 1 `A^e u^e - B^d v^d` | `4 u^2 - v^3` | does **not** vanish |
| corrected `c^e = A^e/B^d` with `c=2` | `4 = 4` | holds |
| printed Cor 2 `c^d = B^d/A^e` | `8` vs `1/4` | fails |

Leading-term cancellation: `u ~ A xi^{m d}`, `v ~ B xi^{m e}` gives `B^d u^e ~ B^d A^e xi^{m d e}` and `A^e v^d ~ A^e B^d xi^{m d e}`, which cancel identically. The printed combination cancels iff `A^{2 e} = B^{2 d}`, which fails on the instance (`16 != 1`). The Newton–Puiseux coefficient along `xi = v^{1/2}` is `c = A B^{-d/e} = 2`, so `c^e = A^e/B^d`. Both printed formulae are correct at `A=B=1`, which is the monic normalisation the campaign has used; nothing banked at `(9,6,2)` is disturbed.

The same inversion appears on Chau p. 3, not numbered as a corollary: the printed leading-form relation is `P_+^e = (B^d/A^e) Q_+^d`. For `P_+ = A y^{K d}`, `Q_+ = B y^{K e}` this requires `A^{2 e} = B^{2 d}` again. The identity that holds is `P_+^e = (A^e/B^d) Q_+^d`. CC SS3.3(i) uses the corrected ratio, consistently with AUDIT-CC-3, without listing p. 3 as a third inverted display. Harmless: the producer never consumes the printed p. 3 formula.

Sharpening (i) of CC SS3.3 is correct: Theorem 1 feeds the *same* `(A,B)` to every component, and `xi |-> lambda xi` fixes `A^e/B^d`. The component-independent scalar is that one number. Sharpening (ii) — `c` common only up to an `e`-th root — follows from `c^e = A^e/B^d`. CAGE clause 1’s “a common type `u = c v^{d/e}`” over-reads the source if `c` is taken literally common; CC does not use the strong form.

Positive control on the campaign curve: `f_1` of `D_1` has weighted-leading form `(u^2-v^3)^3`, which is the *corrected* Cor 1 shape at `(d,e)=(3,2)`, `m_1=3`, `A=B=1`, `M=3`. At `A=B=1` printed and corrected agree, so this is a shape check, not an inversion check. The inversion check is the charged instance above.

---

## 6. Nonblocking observations

None of these moves a CONFIRMED.

1. CC F1 says “granted Lemma A, `(M'-bf)` is the budget”; the theorem says “granted `(AGG)`, `(M'-bf)` iff Lemma A”. Both are the pairing of §1.2. The cancellation uses neither. No repair required.
2. CC SS3.4’s “actual `33` twice” for `m_2=2` CONTACT controls does not name the two companions. The bound was confirmed on the witness and on two named `m_2=2` curves of this review; sharpness on unspecified samples is not a lemma claim.
3. Chau p. 3 carries the same inverted ratio as Cor 1 / Cor 2. Recorded as a source observation. The producer’s corrected ratio in SS3.3(i) is the right one.

---

## 7. FALLACY-v2 self-check

*Flag/place/series.* `(LOC)`’s `a_p` is the finite-fibre count, not a branch count and not a dicritical index. `Sing D` in `(M'-bf)` is `Sing(A_F)`, not `Sing(D_i)`. The two `b` symbols of the charge (`b_dic` vs `b_br`) are not used in any identity replayed here. Prop 2.4’s ceiling (AUDIT-CC-1) was not consumed: COLLAPSE-N does not need it, and COMPANION-EXISTS does not apply it to companions.

*Per-ray / exit-set.* No exit is charged. No `charge_basis` line.

*Carrier/attainment.* The §5.3 pair is a curve pair satisfying a necessary cage. THEOREM COMPANION-EXISTS attains prescribed curve data by construction plus machine check, not by non-emptiness of a numerical cage. `REPRESENTATIVE` is not read as `FULL_ACTUAL_EXIT`.

*Floor/attainment.* Lemma CONTACT and `M <= K` are one-sided and are left one-sided. The witness numbers (`12` vs `17`, `15` vs `10`) are reported as such.

*Raw remainder degree / variable-ring map.* Every substitution `u |-> a(xi)`, `v |-> b(xi)` is in `Q[xi]`, with `f_1 in Q[u,v]` computed as `Res_t(p-u,q-v)`. Weighted degree is with the declared grading `wt(u)=d`, `wt(v)=e`. Leading coefficients are named, not inferred from variable names.

*`sat()` wrapping, pole/interior, prime-label, merge-free, target/arrival.* Not in play. The one Groebner basis (lex, `Q[u,v]`, generators `f_1, partial_u f_1, partial_v f_1`) is a singular-locus computation with a two-element basis `(u, nodepoly)`, not a saturation.

*Gaps.* None filled by cap or analogy. Where Chau and the campaign disagree, the instance decides. Where a first family failed (`e=1` naive row), the failure is the content of MULT-2, not a silent replacement.

---

## 8. Gate

THEOREM COLLAPSE-N is **CONFIRMED**. Independently derived, `(LOC)` sign locked three ways, `chi_c` additivity using points not branches, Lemma A not smuggled, §2.5 positive and negative controls exact, floating-`K_tot` trap real, repaired harness actually repaired. `(M')` is not an independent gate in RED-N.

THEOREM COMPANION-EXISTS is **CONFIRMED** at written scope, including MULT-2 (kill sound, silent at `(3,2)`). The `(9,6,2)` witness is **CONFIRMED** in every charged particular. Lemma CONTACT and `M <= K` are **CONFIRMED** as bookkeeping. The Chau inversions are **CONFIRMED** against the charged instance.

The producer’s obstruction-lane verdict `CLOSED-NEGATIVE` is licensed on these two theorems. The `(9,6,2)` row survives this attack on the merits and remains open at `OPEN[REP-96-BM-FACTORISATION]` and `OPEN[REP-96-SOURCE-IS-C2]`. No promotion of a Keller map is implied.

```text
computation
  sympy 1.14.0 over Q; scripts /tmp/companion-review/verify_all.py
  no AWS, no msolve/qqideal, no jc2-lean, no canonical ledger
consulted, disclosed
  8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f
      refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf   [L]
  xmodel/reducible-all-n-r2-opus5-20260901.md   (grep of (LOC)/(BUD) only)
```
