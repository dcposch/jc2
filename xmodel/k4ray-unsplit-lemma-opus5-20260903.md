# The UNSPLIT-CONFIGURATION LEMMA on the k = 4 two-point ray — PARTIAL

Lane `k4ray-unsplit-lemma-opus5-20260903`; basis `e4e0d0eb`; adapter opus.
Drivers and logs: `box/k4ray-20260903/` (`artifacts.sha256`, 31 files).

## 0. Provenance and verdict up front

**Input verification.** The manifest was generated mechanically from
`xmodel/k4ray-unsplit-lemma-opus5-20260903.run.v2` with `awk` on the
`charged_input_<i>_sha256=` / `_basename=` lines and checked with
`sha256sum -c`: **11/11 OK**, no digit retyped. Moh p. 207–209 was read from
the PDF text layer directly (`pdftotext -f 68 -l 71`), so §1 is a primary read,
not a relay. Per the round's no-collision rule the three in-flight lane reports
(`k16-rank-criterion`, `h1-nonres-census`, `g9966-n2-closure`) were **not**
opened; their box directories were not read.

**VERDICT: PARTIAL.** Typed exactly:

| arm | status |
|---|---|
| (2) `B₂` constant ⇒ composite ⇒ dead | **PROVED, uniformly in `K`, unconditionally** (§3). Chart-free; needs only the shape Moh prints on p. 209. |
| bound `deg_y B₂ < K` | **PROVED** (§2.3): it is the defining property of the 2nd approximate root, not a normalisation. |
| new uniform constraint on the nonconstant arm | **PROVED, uniformly in `K`** — TOP-BAND LEMMA (§4): `β ∉ k ⇒ y^⌈(K−1)/2⌉(y−x) ∣ β_b`. |
| (3) `B₂` nonconstant ⇒ inconsistent | **PROVED at `K = 4, 5` on the stratum `deg β ≤ K−1` only** (§5), exact over **Q**, by a certificate strictly stronger than Rabinowitsch (`cst^N ∈ I`, `N = 1, 2`, `lift`-verified at `K = 4`). **OPEN** for `K ≥ 6` and **OPEN** on `K ≤ deg β ≤ 2K−1`. |
| (4) `K`-uniform certificate | **PROVED as a closed-form ladder** (§6), verified all rows at `K = 4, 5, 7, 9`; the killing *row* is identified in closed form, the killing *combination* is not. |
| (5) two-instrument agreement | **NOT ACHIEVED** — the second instrument (direct Moh-p.209 span port) was not reached inside budget (§8). |
| (6) case (A) / D = 108 / the `δ₁' = 0` rows | **NOT CLOSED.** `K = 4, 5` are *below* the census; the open rows are `K = 7, 8, 9`. Nothing in §5 touches them. |

**The one sentence a reader should carry away:** the composite half of the
dichotomy is now a theorem for every `K` and costs nothing, and the nonconstant
half has a proved uniform structural constraint plus two exact small-`K` kills —
but the ray is *not* dead, and the honest residual is two named strata, not a
conjecture.

**FALLACY-v2 posture.** No exit claim is made, so no `charge_basis` line is
emitted. Floor/attainment: `cst^N ∈ I` is an *attainment* statement (an exact
identity over **Q**), not a floor. Carrier/attainment: the `K = 4, 5` results
are `FULL_ACTUAL` **only** on the declared stratum `deg β ≤ K−1`; that stratum
bound is **not** proved, and every claim below is scoped by it. `sat()` was not
used. No modular-only result is promoted: the two timed-out runs are reported as
timeouts, not as kills.

---

## 1. The source, read (Moh p. 207–209)

Extracted from the text layer, verbatim (OCR artefacts preserved):

> "In the fourth case there are complications. First, there are two
> possibilities according to the distribution of the roots of `g(y)` in the
> minor disc … The polynomial `g_σ(π)` is either a power of a linear polynomial
> or the 9-th power of a cubic polynomial with precisely two roots. For the
> first possibility the data can be transformed to `n = 27, m = −M₁ = 18,
> M₂ = 21, V₂ = 8, δ₂ = −1, δ₁ = 0, Jacobian X⁴`. The above mentioned method
> can be used to reduce the number of coefficients to 10."

and, on p. 209, the reduction itself:

> "where `γ` and `δ` are defined by … with `deg_y γ* < deg h = 4`,
> `deg δ* < deg h² = 8`. Thus the total number of coefficients are reduced
> to 10."

Two things follow that matter for this lane.

1. **The "Jacobian" column is `X⁴`, not a constant.** The descended pair
   satisfies `J(f, g) = c·x⁴` with `c ≠ 0`, not `J = c`. The tuple's `k = 4` is
   exactly this exponent. (`(16,12)` carries `X`, i.e. `k = 1`; `(15,10)` carries
   `X²`.) Every chart below imposes `J = c·x⁴`, and the positive control §5.1
   imposes `J = c·x¹`.
2. **Moh's two displayed bounds are the approximate-root bounds of the tower**,
   with `deg h` playing the role of `K`. In our normalisation (§2) they read
   `deg_y B₂ < deg h = K` and `deg δ* < deg h² = 2K`. So the `γ*`-bound the
   prompt asks us to *prove* is a theorem (§2.3), not an assumption. What Moh
   does **not** print — and what the count "10" silently uses — is a *further*
   restriction of the surviving coefficients to a span; that restriction is the
   necessity obligation this lane could not discharge (§8, `OPEN[K4RAY-BETA-DEG]`).

---

## 2. Ray coordinates, fixed once

### 2.1 The data

```text
R_4 := { (n, m; M₂', V₂'; k) = (3K, 2K; 3K−6; K−1; 4) : K ≥ 4 },  (δ₂', δ₁') = (−1, 0),  u' = 1,
       descended pair (g, f) of π-degrees (3K, 2K),  J(f, g) = c·x⁴,  c ≠ 0.
K = 7 ← (147,98)   K = 8 ← (168,112) = the D = 108 no-split datum   K = 9 ← (189,126) = (99,66) case (A)
```

Write `(x, y) = (γ, π)`. Let `H := y^{K−1}(y−x)`, the two-point leading form:
one root of multiplicity `V₂' = K−1` (the centre, at `y = 0`) and one simple
root (at `y = x`). Normalising the centre to `y = 0` costs `y ↦ y + λx`
(unimodular, fixes `x`, fixes `J`), and moving the second root to `y = x` costs
`x ↦ μx` (rescales `c` only). The mirror normalisation `y(y−x)^{K−1}` is carried
onto this one by `(x, y) ↦ (−x, y−x)`, which has determinant `−1` and fixes
`x⁴`; so no generality is lost by the choice.

### 2.2 The tower

`h` := the **2nd approximate root of `f`**: the unique polynomial monic in `y`
of `y`-degree `K` with `deg_y(f − h²) < K`. Put

```
f = h² + B ,        B := f − h² ,        deg_y B < K            (definition of h)
g = h³ + a₂h² + a₁h + a₀ ,               deg_y a_i < K          (h-adic expansion; always valid)
```

The second line is division with remainder by the monic `h`, so it is
unconditional. Setting `β := B/2` and `α := quo_y(β², h)`, the **tower** is

```
f = h² + 2β ,     g = h³ + 3βh + (3/2)α ,   i.e.   a₂ = 0, a₁ = 3β, a₀ = (3/2)α .
```

Derivation (not assumption): with `β² = αh + ρ`, `deg_y ρ < K`,

```
g² − f³ = (2ε − 3α)h³ − 3ρh² + 9αβh + (9/4)α² − 8β³        for  g = h³ + 3βh + ε,
```

so `ε = (3/2)α` is precisely the choice that annihilates the `h³` band —
i.e. `g` is `f^{3/2}` truncated. Verified exactly:
`box/k4ray-20260903/identity_check.out` `MARK_ID3_GSQ 0`.

### 2.3 What is proved about the shape, and what is not

* **`lf(f) = H²`, `lf(g) = H³`.** For `K ≥ 2` the top Jacobian band
  `J(lf f, lf g)` sits in degree `5K−2 > 4` and must vanish; for binary forms
  `J(F,G) = 0` with `deg F = 2K`, `deg G = 3K` forces `F³ = λG²`, hence
  `F = H²`, `G = H³` for a common form `H` of degree `K`. Consequently
  `deg B ≤ 2K−1`, `deg a₂ ≤ K−1`, `deg a₁ ≤ 2K−1`, `deg a₀ ≤ 3K−1`.
* **`deg_y B < K` is PROVED**, being the defining property of the approximate
  root. This discharges the prompt's step-(3) obligation *in the `y` direction*.
* **`a₂ = 0`, `a₁ = 3β`, `a₀ = (3/2)α` is a normalisation with a residual
  obligation.** Its top band is proved here: matching band `3K−1` gives
  `g_{3K−1} = (3/2)H·f_{2K−1}`, and since the three `h`-adic pieces
  `a₂H², Ha₁, a₀` occupy the *disjoint* `y`-degree ranges `[2K, 3K−1]`,
  `[K, 2K−1]`, `[0, K−1]`, the band separates into
  `(a₂)_{K−1} = 0`, `(a₀)_{3K−1} = 0`, `(a₁)_{2K−1} = (3/2)B_{2K−1}`.
  The same `y`-degree separation is available at every band, so the induction is
  routine; I did not write it out band by band and do **not** claim it as proved.
  Everything in §3 is stated in the *general* shape (no tower) precisely so that
  the composite arm does not depend on it.
* **`deg β ≤ K−1` (total degree) is NOT proved.** Only `deg β ≤ 2K−1` is. This
  is the single scoping restriction on §5 and is raised as
  `OPEN[K4RAY-BETA-DEG]`.

---

## 3. The `B₂` dichotomy, arm (2): PROVED uniformly in `K`

### 3.1 The general-shape identity

For **any** `h, A₂, A₃, B₂` (no tower, no chart, no order basis), writing
`J(u,v) := u_xv_y − u_yv_x`:

> **IDENTITY (ID1).**
> `J(h² + B₂ , h³ + A₂h + A₃) = h²[2J(h,A₂) − 3J(h,B₂)] + h[2J(h,A₃) + J(B₂,A₂)]
>  − A₂J(h,B₂) + J(B₂,A₃)`

Verified: `identity_check.out` `MARK_ID1_GENERAL_SHAPE 0`.

### 3.2 The kill

> **LEMMA B2-CONST (uniform in `K`, unconditional).** Let `f = h² + B₂`,
> `g = h³ + A₂h + A₃` with `deg_y h = K ≥ 1`, `h` monic in `y`. If `B₂ ∈ k`
> then
> ```
> J(f, g) = 2h·[ h·J(h,A₂) + J(h,A₃) ] ,      so   h ∣ J(f,g).
> ```
> Hence `J(f,g)` is **not** of the form `c·x⁴` with `c ≠ 0`: `h` is monic in `y`
> of `y`-degree `K ≥ 1`, and no such polynomial divides `x⁴`. The same argument
> kills `J = c·x^k` for every `k ≥ 0`, in particular the Keller condition `J = c`.

Proof: `B₂ ∈ k` makes `J(h,B₂) = J(B₂,A₂) = J(B₂,A₃) = 0` in ID1. Verified:
`MARK_ID4_HDIVJ 0` (the reduction of `J` modulo `(h)` is `0`) and
`MARK_ID4_QUOT 0` (the displayed quotient identity). ∎

### 3.3 On the tower it is the composite locus, and `J ≡ 0`

If additionally `(A₂, A₃) = (3β, (3/2)α)` with `β = B₂/2 ∈ k`, then
`β²` is a constant, `deg_y β² = 0 < K`, hence `α = quo_y(β², h) = 0` and

```
f = h² + 2β ,   g = h³ + 3βh   →   f = φ(h),  g = ψ(h)  with φ(T) = T² + 2β,  ψ(T) = T³ + 3βT,
```

so the pair is **composite** — `J(φ(h), ψ(h)) = φ'ψ'·J(h,h) = 0` identically —
and a composite pair is not a Keller counterexample. Verified:
`MARK_ID5_ALPHA_ZERO 0`, `MARK_ID5_J 0`.

The kill is *not* the weaker condition `α = 0`: the control `β = x² − y` has
`α = 0` but `J ≠ 0`. It needs `β` constant, nothing less. This reproduces, and
now proves uniformly in `K`, the `K = 9` statement banked as
PROVED-HERE[BRANCH-A-JACOBIAN-IDENTITY].

---

## 4. The nonconstant arm: a sharpened identity and a uniform TOP-BAND LEMMA

### 4.1 Two sharpenings of the tower identity

> **IDENTITY (ID2).** `J(f,g) = 3h·J(h,α) − 6β·J(h,β) + 3J(β,α)`.
> **IDENTITY (ID6, sharper — new).** With `ρ := β² − αh` (so `deg_y ρ < K`),
> ```
>                J(f, g)  =  3·[ J(β, α) − J(h, ρ) ] .
> ```

ID6 follows from ID2 in one line: `2βJ(h,β) = J(h,β²) = hJ(h,α) + J(h,ρ)`, so
the `3hJ(h,α)` term cancels exactly. Verified at `K = 4, 5, 7`:
`identity2_check.out` `MARK_ID6_a/b/c` all `0`, with the attained `y`-degree
bounds `deg_y J(h,ρ) = 2K−2`, `deg_y J(β,α) = 2K−4` (`MARK_ID6_degy_bounds`
prints `12 12 10 10` at `K = 7`).

ID6 is the right object: the whole Jacobian is a difference of two Wronskians,
and the entire `α`-tower has been absorbed into the single remainder `ρ`.

### 4.2 The top band

Let `b := deg β ≥ 1` (total degree; `b ≤ 2K−1` by §2.3), `β_b` its leading form,
and `R₀ := rem_y(β_b², H)`, a form of degree `2b` with `deg_y R₀ ≤ K−1`.
Division of a form by the `y`-monic form `H` is degree-homogeneous, so `R₀` is
exactly the degree-`2b` part of `ρ`.

> **TOP-BAND IDENTITY.** `[J(f,g)]_{2b+K−2} = −3·J(H, R₀)`.

Verified at `(K,b) = (5,6)` and `(4,5)`, and in an `R₀ = 0` instance where the
predicted band collapse occurs (`deg J = 9 < 11 = 2b+K−2`):
`topband_check.out` `MARK_TB1_resid 0`, `MARK_TB2_resid 0`, `MARK_TB3_R0 0`.

> **TOP-BAND LEMMA (uniform in `K`).** For `K ≥ 4` and `β ∉ k`,
> ```
>            H ∣ β_b²   in k[x,y],  equivalently   y^{⌈(K−1)/2⌉}·(y−x)  ∣  β_b .
> ```
> In particular `b ≥ ⌈(K−1)/2⌉ + 1`, so `2b ≥ K+1`.

*Proof.* Since `b ≤ 2K−1 < 2K`, the term `3J(β,α)` of ID6 has degree
`≤ 3b−K−2 < 2b+K−2`, so the top band is the displayed one. If
`2b+K−2 > 4` the band must vanish, i.e. `J(H, R₀) = 0`. Euler's relation gives
`x·J(H,R) = K·H·R_y − 2b·H_y·R`, so `J(H,R₀) = 0` forces either `R₀ = 0` or
`R₀^K = λH^{2b}` with `λ ≠ 0`. In the second case `H = y^{K−1}(y−x)` is not a
proper power (the exponent gcd is `gcd(K−1,1) = 1`), so `R₀ = λ'H^{2b/K}` with
`K ∣ 2b`, whence `deg_y R₀ = 2b`; but `deg_y R₀ ≤ K−1`, so `2b ≤ K−1 < K`, and
with `K ∣ 2b` this forces `b = 0`, contradicting `β ∉ k`. Hence `R₀ = 0`, i.e.
`y^{K−1}(y−x) ∣ β_b²`, i.e. `y^{⌈(K−1)/2⌉}(y−x) ∣ β_b`.

The single excluded case is `2b+K−2 ≤ 4` with `b ≥ 1`, i.e. `(K,b) = (4,1)`.
There `[J]_4 = −3J(H, β_1²) = −6β_1J(H,β_1)` must equal `c·x⁴`, so `β_1 ∣ x⁴`
and `β_1 = μx`, `μ ≠ 0`; then `J(H, μx) = −μ(4y³ − 3xy²)` and
`−6β_1J(H,β_1) = 6μ²x(4y³ − 3xy²) ≠ c·x⁴`. So `(K,b) = (4,1)` is dead outright. ∎

This is a genuinely new, `K`-uniform constraint on the nonconstant arm: the
leading form of `β` must already carry `⌈(K−1)/2⌉` powers of the centre
direction **and** the second point. It is the structural half of what the
"`B₂` lies in a bounded space" step wants, and it holds with no chart at all.

---

## 5. The bounded chart, exact over Q

### 5.1 Instrument, grading, controls

Chart (`box/k4ray-20260903/gen_k4ray3.py`): unknowns are all `h_{ij}` with
`i+j ≤ K−1` and all `B_{ij}` with `j ≤ K−1`, `i+j ≤ Bdeg`; then `f = h² + B`,
`α = quo_y(B², h)` computed by an explicit `y`-division loop,
`g = h³ + (3/2)Bh + (3/8)α`, `J = f_xg_y − f_yg_x`; `I` := all coefficients of
`J` in `k[x,y]` **except** the `x⁴` one; `cst` := the `x⁴` coefficient.

**The grading (used, and machine-confirmed).** The solution set is invariant
under `(x,y) ↦ (tx,ty)` with `h_{ij} ↦ t^{i+j−K}h_{ij}`,
`B_{ij} ↦ t^{i+j−2K}B_{ij}`, `c ↦ t^{6−5K}c`. So with
`w(h_{ij}) = K−i−j ≥ 1`, `w(B_{ij}) = 2K−i−j ≥ 1` the ideal `I` is
weighted-homogeneous with **positive** weights and `cst` is `w`-homogeneous of
weight `5K−6`. Singular confirms both independently: `MARK_HOMOG_I 1`,
`MARK_HOMOG_CST 1`, and `MARK_CST_WT` = `14` at `K = 4` (`5·4−6`), `19` at
`K = 5` (`5·5−6`). Per the homogeneous-cone rule this is *not* tested by
`dim −1` on an inhomogeneous ideal; `V(I)` is a cone, so

```
chart empty  ⟺  V(I) ∩ {cst ≠ 0} = ∅  ⟺  cst ∈ √I  ⟸  cst^N ∈ I for some N.
```

`cst^N ∈ I` is **strictly stronger** than a Rabinowitsch `dim −1`: it is an
exact cofactor identity over **Q**, `lift`-verifiable, and it transfers to every
field. That is the test reported below.

**Controls, all four printed in every run.**
`CTRL_RAW_DIM = dim std(I) > 0` (the unlocalised chart is a positive-dimensional
cone — the rows are not vacuously everything); `CTRL_UNIT = dim std(1) = −1`;
`CTRL_ORIGIN = dim std(m) = 0`; and `LIFT_VERIFY`, the exact check
`cst − Σ q_i I_i = 0`.

**POSITIVE CONTROL (a survivor must survive).** Same code path, `K = 1`,
`Bdeg = 1`, target `x¹`. By hand: `h = y − x + h₀`, `B = B_{00} + B_{10}x`,
`α = 0`, and `J = (3/2)B_{10}(B_{00} + B_{10}x)`, so the single non-target row
is `B_{00} = 0` and `c = (3/2)B_{10}² ≠ 0` — a genuine survivor of
`J = c·x^k`. `PC_K1_B1_x1.out` reports exactly this:

```
MARK_NROWS 1     MARK_CST_IN_I 0     MARK_CTRL_RAW_DIM 2
MARK_DIM 2       MARK_GB1 B_0_0      MARK_RED1 1        (Rabinowitsch NOT a unit)
MARK_CTRL_UNIT -1   MARK_CTRL_ORIGIN 0
```

A second, independent survivor of the same `J = c·x^k` family, in the *tower*
shape, is exhibited in `identity_check.out` `MARK_PC_*`:
`f = y² + x`, `g = y³ + (3/2)xy`, `J = (3/2)x`. So the pipeline is not a
machine that returns "empty" on everything handed to it.

### 5.2 Results (char 0, `Q`, exact)

| K | Bdeg | rows | params | `std(I)` | `CTRL_RAW_DIM` | kill certificate | wall |
|---|---|---|---|---|---|---|---|
| 1 (PC) | 1 | 1 | 3 | 1 | 2 | **none — SURVIVES** (as required) | <1 s |
| **4** | **3 = K−1** | 39 | 20 | 75 | 11 | **`cst ∈ I`** (`N = 1`), `lift` verified, 13 nonzero cofactors | 4.76 s |
| **5** | **4 = K−1** | 68 | 30 | 303 | 16 | **`cst² ∈ I`** (`N = 2`) | ≈30 s + |
| 6 | 5 = K−1 | — | 42 | — | — | `std(I)` did not terminate in 9 min — **TIMEOUT, not a kill** | >540 s |
| 4 | 7 = 2K−1 | 95 | 36 | — | — | `std(I)` did not terminate in 555 s — **TIMEOUT, not a kill** | >555 s |

`CTRL_UNIT = −1` and `CTRL_ORIGIN = 0` in every completed run.

> **MEASURED[K4RAY-K4-EMPTY].** For `K = 4`, on the stratum `deg β ≤ 3`, the
> `x⁴` coefficient of `J` lies **in** the ideal generated by all the other
> coefficients of `J`, over **Q**. Hence `J = c·x⁴` forces `c = 0`: the chart is
> empty. The certificate is an explicit identity `cst = Σ_{i=1}^{13} q_i·I_i`
> returned by `lift` and verified to be exactly `0` (`MARK_LIFT_VERIFY 1`).

> **MEASURED[K4RAY-K5-EMPTY].** For `K = 5`, on the stratum `deg β ≤ 4`,
> `cst² ∈ I` over **Q** (`cst ∉ I`, so `N = 1` genuinely fails and `N = 2` is
> sharp). Chart empty.

Note the `N`-ladder `1, 2` at `K = 4, 5`: the certificate is *not* uniform in
degree, which is itself information — a single linear cofactor identity cannot
be the `K`-uniform certificate.

### 5.3 What these two rows do and do not establish

They are **calibration**, not census closure. `K = 4` and `K = 5` sit *below*
the ray's census members. The open rows are `K = 7, 8, 9`. Neither
`MEASURED[K4RAY-K4-EMPTY]` nor `MEASURED[K4RAY-K5-EMPTY]` touches
`(147,98)`, `(168,112) = D = 108`, or `(99,66)` case (A). Reading them as
partial closure of those rows would be a carrier/attainment error of exactly the
kind FALLACY-v2 names.

---

## 6. The `K`-uniform certificate: a closed-form ladder

Write, over `k[x]`, `h = Σ_{i=0}^{K} c_i y^i` (`c_K = 1`,
`c_{K−1} = h_{0,K−1} − x`), `ρ = Σ_{j<K} r_j y^j`, `β = Σ_{j<K} b_j y^j`,
`α = Σ_{i≤K−2} a_i y^i`, with `β² = αh + ρ`. Expanding ID6 by `y`-degree:

> **LADDER (closed form in `K`).** For every `l`,
> ```
>   J_l  =  3 · Σ_{i+j = l+1}  [ ( i·a_i·b_j′ − j·a_i′·b_j )  +  ( i·c_i·r_j′ − j·c_i′·r_j ) ]
> ```
> (`′ = d/dx`; in the first bracket `i ≤ K−2`, `j ≤ K−1`; in the second
> `i ≤ K`, `j ≤ K−1`). The Keller condition is `J_l = 0` for `l ≥ 1` and
> `J_0 = c·x⁴`.

Verified **row by row, all `2K−1` rows**, at `K = 4, 5, 7, 9`:
`ladder_check.out` `MARK_LADDER_K{4,5,7,9}_BADROWS` all `0`.

Both brackets are the same Wronskian pairing `Σ_{i+j=l+1}(i·u_i·v_j′ − j·u_i′·v_j)`,
applied to `(α, β)` and to `(h, ρ)`. Because `deg_y J(β,α) ≤ 2K−4`, the top two
rows involve only `(h, ρ)` and specialise to

```
  L1  :  J_{2K−2}  =  3K · r_{K−1}′                                    ⇒  r_{K−1} ∈ k
  L2  :  J_{2K−3}  =  3[ K·r_{K−2}′ + (K−1)c_{K−1}r_{K−1}′ − (K−1)c_{K−1}′ r_{K−1} ]
                    =  3[ K·r_{K−2}′ + (K−1) r_{K−1} ]      (using L1 and c_{K−1}′ = −1)
```

Verified at `K = 4, 6, 9`: `MARK_TOPROWS_K{4,6,9}` print `L1resid: 0
L2resid: 0`. So `r_{K−1} = R ∈ k` and `r_{K−2} = −((K−1)/K)·R·x + const`.

This is the ladder object the round asked for, in the shape of the K16 ladder
`9(99−3n−11i)` and the D = 108 residues: an explicit `K`-indexed row family with
`K`-dependent rational coefficients (`3K`, `(K−1)/K`), verified against the
expanded Jacobian at four values of `K`. What it is **not**: a proof. It
identifies the killing rows in closed form; it does not exhibit the `K`-uniform
*combination* of them that produces `c = 0`. That combination is the residual
(`OPEN[K4RAY-UNIFORM-COMBINATION]`).

Two structural consequences worth recording, both immediate from the ladder plus
§4: for `b ≤ K` every band of `ρ` of degree `> K−1` vanishes (iterate the
top-band argument, the `J(β,α)` term entering only at band `3b−2K`); and in the
extreme branch `ρ = 0` one gets `J·h² = 3β²·J(h,β)`, so `β² ∣ x⁴h²` up to
constants — a stratum small enough to be finished by hand.

---

## 7. Dependency chain, stated honestly

What a *complete* proof of the lemma would give, and what today gives:

```
UNSPLIT-CONFIGURATION LEMMA uniformly in K
   ⇒ (99,66) case (A) dead            [K = 9]        NOT OBTAINED
   ⇒ D = 108 no-split arm dead        [K = 8]        NOT OBTAINED
   ⇒ the three δ₁′ = 0 two-point rows dead  [K = 7,8,9]  NOT OBTAINED
```

Today's arms of it:

```
LEMMA B2-CONST (§3)          — PROVED ∀K, unconditional, chart-free.
    ⇒ on every member of R_4, the composite stratum β ∈ k is dead.
    ⇒ the K = 9 instance reproduces PROVED-HERE[BRANCH-A-JACOBIAN-IDENTITY]
      and is now independent of the (99,66) branch-A chart entirely.
TOP-BAND LEMMA (§4)          — PROVED ∀K ≥ 4 (plus the (K,b) = (4,1) case by hand).
    ⇒ β ∉ k ⇒ y^⌈(K−1)/2⌉(y−x) ∣ β_b and 2b ≥ K+1, for every member of R_4,
      including K = 7, 8, 9.  This DOES bite on the open rows — it is the only
      statement in this report that does.
CHART EMPTINESS (§5)         — K = 4, 5 only, and only for deg β ≤ K−1.
```

So the correct summary of the campaign position is: **the ray is not closed, one
of its two arms is closed for all `K`, and the other arm has gained a uniform
structural constraint plus two exact sub-census kills.** The `(99,66)` skeleton
verdict is *not* complete for all three configurations, `D = 108` is *not*
closed, and the `δ₁' = 0` rows remain open.

---

## 8. What was not done, and why

* **The second instrument (direct Moh-p.209 span port to `(3K,2K)`) was not
  built.** Budget went to the general-`β` chart and to the uniform structure.
  Consequently the prompt's step (5) — two independent instruments agreeing — is
  **not** satisfied, and no result here is cross-checked by a second chart. The
  template exists and is small (`box/minor-residue-20260903/charts/moh1612_kill.sing`,
  41 lines, `h = y³(y−x) + b₁y³ + b₂y² + b₃y + b₄`, tower coefficients in the
  span of the truncations `A, B, (y−x), 1`); porting it to `(3K,2K)` is a
  half-hour job for the next lane.
* **`K = 6..9` on the general chart is out of reach monolithically.** `K = 6`
  has 42 parameters and did not finish `std(I)` in 9 minutes; `K = 9` would have
  90. The band-wise route is the ladder of §6, and that is where the next lane
  should spend its time — not on a bigger Gröbner. (This confirms, on a fresh
  system, the standing "emit and eliminate band-wise" finding.)
* **No modular result was promoted.** Both timeouts are reported as timeouts.

---

## OPENS RAISED

**`OPEN[K4RAY-BETA-DEG]`** — prove or refute `deg β ≤ K−1` (total degree) for a
`k = 4` ray pair, given the proved bounds `deg_y β ≤ K−1` and `deg β ≤ 2K−1`.
This is the *only* thing standing between §5's two kills and an unconditional
statement for `K = 4, 5`.
QUANTITY: the total degree `b` of `β`, currently bounded `1 ≤ b ≤ 2K−1`, with
the §4 constraint `2b ≥ K+1`; decide whether `b ≤ K−1`.
CHEAPEST TEST: run `gen_k4ray3.py 4 Bdeg 0 4` for `Bdeg = 4, 5, 6, 7` and read
the first `Bdeg` at which `cst^N ∈ I` fails or `std(I)` diverges; each step adds
`≈ K` parameters. Singular, ≈ 60 lane-minutes for the four.

**`OPEN[K4RAY-UNIFORM-COMBINATION]`** — exhibit the `K`-uniform combination of
the §6 ladder rows that forces `c = 0`, i.e. the closed-form analogue of the K16
pivot law `9(99−3n−11i)`.
QUANTITY: the number `N(K)` of ladder rows needed, and the certificate exponent
`N` in `cst^N ∈ I`; measured `N = 1` at `K = 4` and `N = 2` at `K = 5`, so
`N` is **not** constant and any uniform certificate must be at least quadratic.
CHEAPEST TEST: solve `L1, L2, L3, L4` symbolically in `K` (they involve only
`r_{K−1..K−4}` and `c_{K−1..K−4}`) and check whether the `x⁴` row is already in
their span; no Gröbner needed. ≈ 45 lane-minutes.

**`OPEN[K4RAY-TOWER-INDUCTION]`** — complete the band-by-band induction of
§2.3 showing `a₂ = 0`, `a₁ = 3β`, `a₀ = (3/2)α` is forced (not normalised).
The top band is proved here; the inductive step is the same `y`-degree
separation `[2K,3K−1] ⊔ [K,2K−1] ⊔ [0,K−1]`.
QUANTITY: the residual `Δ := g − (h³+3βh+(3/2)α)`; show `deg Δ < 0`, i.e.
`Δ = 0`. Currently only `(a₂)_{K−1} = 0` and `(a₀)_{3K−1} = 0` are proved.
CHEAPEST TEST: run the `hadic` variant of `gen_k4ray.py` (already written,
`variant=hadic`, general `a₂, a₁, a₀`) at `K = 4` and check that the ideal
contains every `p_*` generator. ≈ 30 lane-minutes if it terminates.

**`OPEN[K4RAY-SECOND-INSTRUMENT]`** — port `moh1612_kill.sing` to `(3K,2K)`
and require agreement with §5 at `K = 4, 5` before any `K = 7,8,9` claim is
made on either.
QUANTITY: the two instruments' verdicts at `K = 4, 5`; agreement `=` required,
currently `1 of 2` instruments has reported.
CHEAPEST TEST: the 41-line template with `h = y^{K−1}(y−x) + Σ b_j y^j`,
`f = h² + be2`, `g = h³ + al2·h + al3`, coefficients in the truncation span.
≈ 30 lane-minutes.

**`OPEN[K4RAY-RHO-ZERO-STRATUM]`** — finish the branch `ρ = 0` (i.e. `h ∣ β²`)
by hand from `J·h² = 3β²·J(h,β)` and `β² ∣ x⁴h²`.
QUANTITY: the divisor of `β` relative to `x` and to the irreducible factors of
`h`; decide whether `deg β ≥ 1` is possible at all in this branch.
CHEAPEST TEST: pure factorisation argument, no CAS. ≈ 20 lane-minutes.

---

## Artifacts

`box/k4ray-20260903/` — 31 files, `artifacts.sha256`. Generators
`gen_k4ray{,2,3}.py`; identity verifications `identity_check.{sing,out}`,
`identity2_check.{sing,out}`, `topband_check.{sing,out}`,
`ladder_check.{sing,out}`; charts `PC_K1_B1_x1.*`, `K4_B3_Q.*`, `K5_B4_Q*.*`,
`K6_B5_Q.*`, `K4_B7_Q.*`, `k4ray_K4_tower_B7.*`. Every Singular `.out` was
grepped for `MARK_*` rather than trusted by exit status, per the lane-CAS rule;
the two timeouts are visible as a missing `MARK_STDI_DONE`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `26157`.
- Body SHA-256:
  `bcafc9a0e92fc94f5617092d221e55454404aa73ef12b5d19607f70832f115e3`.
- Frozen basis: `e4e0d0eb88d22c50fa3d90bd90936fd7726e1bb1`.
