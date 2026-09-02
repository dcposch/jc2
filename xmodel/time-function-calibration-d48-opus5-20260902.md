# TIME-FUNCTION CALIBRATION at `D = 48` — the bottom-disc expansion of the Keller condition, order by order: Moh's leading order is an ODE that NEVER kills, the kill at `D = 48` is the Galois symmetry of the star, and Moh's own search conditions (8)–(11) are MISSING from the campaign census

## 0. Custody, method, scope

Lane `time-function-calibration-d48`, Opus 5, 2026-09-02. Charged inputs verified by
SHA-256 before use, all eight matching:

```text
26479b06  d1-subtree-opus5-20260902.md              66c3e82f  d1-subtree-review-grok46-20260902.md
126d9c84  integration17-coordinator-fable51-...md   450e4610  time-function-endgame-...prompt.md
30220204  moh_skeleton_N.py                         cf0780cc  d1floor.py
574f2f45  jacfibre.py                               e7d7d2e6  general.py
```

The parallel flagship's **report** (`time-function-endgame-opus5-20260902.md`, running at
`D = 105`) was **not** read; only its charged prompt, as instructed. Firsthand source read
in this lane: `box/depth-drivers-20260902/moh.txt` (the `pdftotext` extraction of Moh,
*J. reine angew. Math.* **340** (1983) 140–212), specifically **Definition 4.1** of the
symbol `D` (moh.txt:1325–1326), **Proposition 4.6** (moh.txt:1609–1645), **Appendix I
Propositions A.1–A.4** (moh.txt:3361–3560) and — the item that turned this lane —
**the search conditions (1)–(13) and the published `n ≤ 100` table** (moh.txt:3258–3350).

Drivers, fail-closed, in `box/tfcal-drivers-20260902/`: `tfcal.py` (37 checks, 0 failures),
`mohcond.py`, `d48{groups,detail,uni,pick,final}.py`, `sweep.py`, `sweep1.py`,
`survivors.py`, `star_explicit.py`, `kernel_L.py`, plus frozen copies of the four charged
drivers. Wall `< 20` min per run, memory `< 1` GB. Scope: Keller, noninvertible,
degree-minimal, Moh's gauge (GEN, NU-TWO). No canonical ledger edited; `jc2-lean` not
inspected.

---

## 1. Verdict, up front

1. **The exact bottom-disc expansion of `[f,g] = c` is an order-graded linear recursion**
   (§3.1). Its **order 0** is, verbatim, Moh's Prop 4.6 clause at `r = 1`; its **order `ν > 0`**
   is a one-parameter family of linear operators `L_ν` on the pair of correction
   polynomials. PROVED-HERE, machine-checked on genuine Keller pairs.
2. **Moh's `r = 1` clause is an ODE that never kills.** `d Q P' − e Q' P = γ ≠ 0` forces `P`
   and `Q` to have **simple roots and no common root**; `Q^e/P^d` is then a genus-0 Belyi
   map with a completely determined ramification profile, and the corresponding dessin
   exists for **every** `(d,e,V)` — a cubic plane map whose core is a tree with `V+1` leaves,
   one loop per leaf. Explicit solutions printed at `V = 1, 2`. **`OPEN[STAR-REALISABILITY]`
   is therefore answered NEGATIVE at the ODE level: no skeleton dies from a forced repeated
   root of `p(π)`.**
3. **What does kill at order 0 is the GALOIS symmetry of the star, not the ODE.** The
   order-`Δ_1` automorphism that Moh's search condition (8) introduces multiplies `π` by a
   primitive `Δ_1`-th root of unity and permutes the `a_1 = eV_2` roots of `P`. Since those
   roots are **simple** (item 2 = D1-STAR(d)), at most one of them is `0`, so
   ```text
      (10)_1     a_1 = e V_2  ≡  0  or  1   (mod Δ_1),
      Δ_1 = reduced denominator of L_1·δ_1,  L_1 = lcm{den δ_s, …, den δ_2}.
   ```
   PROVED-HERE (both branches). All six of Moh's published survivor rows pass it.
4. **The `D = 48` skeleton selected by the charge's own criteria dies at order 0, by (10)₁.**
   The criteria (smallest budget `u·e`, fewest tame coefficients) select
   `(n,m) = (48,32)`, `M = (−32,−12,46)`, `V = (V_2,V_3) = (1,3)`, `s = 3`,
   `δ = (−1, 7/22, 3/8)`, `a_1 = 3`, `b_1 = 2`, `q = 3/4`, `N ∈ {6, 9}`. There
   `L_1 = 22`, `Δ_1 = 4`, `a_1 = 3 ≡ 3 (mod 4)`: **DEAD**, before any correction order.
5. **The whole of `D = 48` is empty** once (10)₁ is combined with a reconstruction of Moh's
   (10) at levels `j ≥ 2` (§4.3): 1301 `V`-assignments → 33 → **0**. Likewise `D = 66` and
   `D = 78`. Consistent with — and far weaker than — Moh's `D ≤ 100` theorem.
6. **The campaign census omits Moh's search conditions (8)–(11).** `moh_skeleton_N.py`
   implements (1)–(7) and Def 5.1(2) only. Over `48 ≤ D ≤ 120` the reconstructed (10)+(10)₁
   cut the reviewed census from **902 893 `V`-assignments to 329** and from **10 637
   `(n,m,M,V_s)` groups to 287**, of which **233 survive the pinned-`N` knapsack** at
   `N ∈ [6,16]`. At `D = 105`: **264 groups → 3**. The integration-#17 filter numbers were
   computed on a strict superset of Moh's admissible skeletons.
7. **Beyond order 0** (§3.4–3.6): `L_ν` has a 3-dimensional kernel generically (`V = 1`), so
   the first correction order alone does **not** kill. On the **NO-TAME** subspace it is
   injective for every `ν ≠ 1 − δ_1`, and then the geometry forces `h'(C) = 0` with
   `h = p_2/(π−C)^{V_2}`; if the bottom-major discs **exhaust** their `D_2` this gives
   `Σ_{i<j} V_iV_j = 0`, so there can be **at most one** bottom-major disc whenever the
   ceiling `N = U` is attained. Order `2ε` is set up but **not** imposed: typed OPEN.

**Correction to a charged input.** The D1-SUBTREE review's "intra-`f` clustering below `δ_1`
is free" is **REFUTED**: `Q = p_f` has simple roots by Moh's own `r = 1` clause, so no two
`f`-roots of `D_1` may share a leading `π`-coefficient. (The review's "invisible to `N`"
stands; "free" does not.)

---

## 2. Part (1): the `D = 48` census, the knapsack, and the selected skeleton

### 2.1 `D = 48` is rigid before anything is imposed

`K = gcd(m,n) ≥ 16` (GGV Cor 6.6) and `K ≤ n/3` force `K = 16`, `e = 3`, and
`2 ≤ d < e` with `gcd(d,e)=1` forces `d = 2`. So

```text
   n = 48,  m = 32,  K = 16,  (d,e) = (2,3),  d_2 = 16,  d_{s+1} = gcd(d_s, 46) = 2,
   divisor chains below K:  d_3 ∈ {8,4} (s=3)  or  (d_3,d_4) = (8,4) (s=4).
```

`census(48)` yields **1301 `V`-assignments in 50 groups** `(m, M_2..M_s, V_s)` — matching
the D1-SUBTREE framework exactly. The hypothesis-free knapsack
`N = Σ_B V_2(B) q(B), Σ_B V_2(B) ≤ u`, run at `N ∈ [6,16]` with `CAP = 2·10^5`:

```text
   D = 48 :  ALIVE 39   KILLED 11   CAPPED 0            (driver d48groups.py)
```

*Correction to the charge.* The charge says "the general knapsack … killed 9 of them at
`N ≥ 6`". `box/d1sub-drivers-20260902/general.log` was run at `N ∈ [4,16]` with
`CAP = 6·10^4`, giving `9 killed / 3 capped`. At `N ∈ [6,16]` with a larger cap the honest
figures are **11 killed, 0 capped, 39 alive**.

### 2.2 The selection

Every surviving group has `u ∈ {12, 14}`, i.e. total root budget `u·e ∈ {36, 42}`; all five
`u = 10` groups (`V_3 = 5`) are killed by integrality. The charge's keys are
(i) smallest `u·e` → `u = 12`, `u·e = 36`; (ii) fewest tame coefficients → smallest star
`a_1 = eV_2` and shortest tower `s`. Under (UNI) (`N = k V_2 q`, `k V_2 ≤ u`) exactly one
row has `u = 12`, `a_1 = 3` and `s = 3`:

```text
   SELECTED SKELETON  (48,32) M = (−32, −12, 46),  V_4 = 2, V_3 = 3, V_2 = 1,  s = 3
     d-chain      d_1..d_4 = 48, 16, 4, 2
     radii        δ_3 = −1,  δ_2 = 7/22,  δ_1 = 3/8
     bottom disc  a_1 = e V_2 = 3 roots of g,  b_1 = d V_2 = 2 roots of f
     level 2      a_2 = 36 = u e,  b_2 = 24;   v_2 = V_3 d_2/d_3 = 12 = u
     top form     u = 12, v = 4  (l(g) = L_1^{36} L_2^{12})
     q = (1−δ_1) d e/(d+e) = 3/4      N = k·q  with k = Σ_B V_2(B) ≤ 12
     N = 6 (k = 8 bottom discs)  or  N = 9 (k = 12, the ceiling N = U attained)
     tame budget  3 + 2 = 5 star tails + the two outer series per correction order
```

Runner-up (kept as a cross-check): `M = (−32, 4, 46)`, `V = (2,3)`, same `u·e = 36`,
`δ = (−1, 5/16, 3/8)`, `a_1 = 6`, `b_1 = 4`, `q = 3/4`, `N ∈ {6, 9}`.

---

## 3. Part (2): the bottom-disc expansion of the Keller condition

### 3.1 The chart, and the exact order decomposition

Put `t = x^{-1}`, `ord = ord_t`, and let `σ_1` be the truncation at radius `δ_1` of a
`g`-root of a bottom-major disc `D_1`. In the chart

```text
        y = σ_1(x) + π x^{-δ_1},        (x,y) → (x,π) has Jacobian  ∂π/∂y = x^{δ_1},
```

write `f = x^A Φ(x,π)`, `g = x^B Γ(x,π)` with

```text
   A := −λ_f(δ_1) = m(1−δ_1)/(n+m) = d κ,   B := −λ_g(δ_1) = n(1−δ_1)/(n+m) = e κ,
   κ := (1−δ_1)/(d+e),        A + B − 1 + δ_1 = 0.
```

The last identity is **exactly D1-PIN**: `A + B = 1 − δ_1` is `floor = ceiling` at `r = 1`.
Because the `σ'`-terms cancel in the 2×2 determinant,

```text
   (♦)   [f,g] = A Φ Γ_π − B Φ_π Γ + x(Φ_x Γ_π − Φ_π Γ_x)  =  c .
```

Expanding `Φ = Σ_ν Φ_ν x^{-ν}`, `Γ = Σ_ν Γ_ν x^{-ν}` (`ν ≥ 0` in the value group of the
branch; `x∂_x` acts as `−ν`), the coefficient of `x^{-ν}` in (♦) is

```text
   Σ_{α+β=ν} [ (A−α) Φ_α Γ_β' − (B−β) Φ_α' Γ_β ]  =  c·[ν = 0].
```

Write `P := Γ_0 = p_g` (degree `a_1 = eV_2`) and `Q := Φ_0 = p_f` (degree `b_1 = dV_2`).
Then

```text
   ORDER 0    A Q P' − B Q' P = c                                            (BOTTOM)
   ORDER ν>0  L_ν(Φ_ν, Γ_ν) = −R_ν,
              L_ν(F,G) := (A−ν) F P' − B F' P + A Q G' − (B−ν) Q' G,
              R_ν := Σ_{α+β=ν, α,β>0} [ (A−α)Φ_αΓ_β' − (B−β)Φ_α'Γ_β ].
```

Dividing by `κ` and setting `ν̃ := ν/κ`, `L_ν` becomes a **skeleton-free** operator:

```text
      L̃_ν̃(F,G) = (d − ν̃) F P' − e F' P + d Q G' − (e − ν̃) Q' G .
```

*Where the time function enters.* JAC-FIBRE in fibre form is
`d/dx f(x,τ_i(x)) = c/g_y(x,τ_i(x))`, and `f/(g−c_2) = Σ_i F_i/(g_y(τ_i)(y−τ_i))` turns the
charge's condition (i) into `Σ_i F_i F_i' τ_i^r = 0` for `r = 0,…,n−m−2` and `= c` at
`r = n−m−1`; at `r = 0` that reads `d/dx[Σ_i F_i(x)²] = 0` — the trace of `f²` over the
generic fibre is constant in `x`, a conservation law for the Keller time function. These
are *automatic* for a polynomial `f`; the content is the **converse**, that the `F_i`
produced by integrating `g` alone assemble into a polynomial. That converse localises to
(♦): (♦) at every order **is** the full Jacobian condition read at the bottom disc.

### 3.2 Order 0 is Moh Prop 4.6 at `r = 1`, and it never kills

Moh's Definition 4.1 (moh.txt:1326) is `D(a,b,p,q) = a p q' − b q p'`, and Prop 4.6's last
clause (moh.txt:1637) reads, verbatim,

> Moreover if `r = 1` then `g_σ(π)` and `T^ψ_{1,σ}(π)` satisfy the following differential
> equation `D(n, −M_1, g_σ(π), T^ψ_{1,σ}(π)) = nonzero constant.`

With `−M_1 = m` and `A : B = m : n = d : e`, `(BOTTOM)` **is** that clause up to sign:

```text
      (BOTTOM)     d Q P' − e Q' P  =  γ ≠ 0 ,     deg P = eV_2,  deg Q = dV_2 .
```

> **PROPOSITION TF-0 (PROVED-HERE).** `(BOTTOM)` with `γ ≠ 0` forces `P` and `Q` to have
> **simple roots** and to be **coprime**.
>
> *Proof.* At a double root `π_0` of `P`, `P(π_0)=P'(π_0)=0` so `γ = 0`; likewise for `Q`;
> at a common root both terms vanish. ∎ (machine-checked, `tfcal.py`.)

This is a second, one-line proof of **D1-STAR (d)** — and it also settles the `f`-family:
the review's "intra-`f` clustering below `δ_1` is free" is **refuted**, `Q` has simple roots.

> **PROPOSITION TF-DESSIN (PROVED-HERE).** Put `φ := Q^e/P^d` (well defined, `deg φ = deV`,
> `φ(∞) = 1`). Then `φ'/φ = −γ/(PQ)`, so `φ` is ramified only over `{0,1,∞}` with profile
> ```text
>    over ∞ :  eV points of index d            over 0 :  dV points of index e
>    over 1 :  ONE point (π = ∞) of index (d+e)V − 1, all others simple;
>              deg(Q^e − P^d) = deV − (d+e)V + 1 .
> ```
> Equivalently: a genus-0 bipartite map with `dV` black vertices of degree `e`, `eV` white
> of degree `d`, one face of degree `(d+e)V−1` and `V(de−d−e)+1` faces of degree 1.

For `(d,e) = (2,3)` the white vertices have degree 2 and contract, leaving a **cubic plane
map** with `2V` vertices, `3V` edges, `V+1` monogonal faces and one face of degree `5V−1`.
Deleting the `V+1` loops leaves a tree with `2V` vertices, `V+1` leaves and `V−1` trivalent
vertices — which exists for every `V ≥ 1` and is planar; re-attaching one loop at each leaf
reconstructs the map. By Riemann existence, `(BOTTOM)` is **solvable for every `V`**.
Machine witnesses (`star_explicit.py`, all clauses verified: constant, nonzero, simple
roots both sides, coprime, `deg(Q^e−P^d)` as predicted):

```text
   V = 1 :  P = π³ + 3π,                 Q = π² + 2,      γ = 12
   V = 2 :  P = π⁶ + 3π³ + 3/2,          Q = π⁴ + 2π,     γ = −9
```

(The `V = 2` solution is the `ζ_3`-equivariant one the `K_{1,3}` dessin predicts.)
Unknown/equation count `((d+e)V+2` vs `(d+e)V−2)` matches the 4-dimensional symmetry group
`{π ↦ απ+β} × {P ↦ λP} × {Q ↦ μQ}`, so the solution is rigid modulo symmetry — the `V = 1`
solution above is the unique one.

**Consequence.** `OPEN[STAR-REALISABILITY]` — "a skeleton whose bottom polynomial `p(π)` is
forced to have a repeated root dies" — has the answer **no such skeleton exists**: the
repeated root is never forced, at any `(d,e,V)`. The bottom leading form is not a census
filter.

### 3.3 The order-0 GALOIS layer: the star congruence

Moh's search condition **(8)** (moh.txt:3299 ff.) introduces exactly the object that does
kill:

> (8) … let the l.c.m. of the reduced denominators of `δ_s,…,δ_r` be `L`. Then `Δ_{r−1}` is
> defined to be the reduced denominator of `L δ_{r−1}`. … Due to the existence of the
> following automorphism … `t ↦ ω t` where `ω` is a `Δ_{r−1}`-th root of unity, the value of
> `V_{r−1}` is further restricted by (10) … if the corresponding factor of `p(π)` is of the
> form `π − α` with `α ≠ 0` or … (11) … if the corresponding factor of `p(π)` is of the
> form `π`.

> **THEOREM (10)₁ (PROVED-HERE; = Moh (8)–(11) at `r = 1`, sharpened by D1-STAR(d)).**
> Let `L_1 := lcm{den δ_s, …, den δ_2}` and `Δ_1 :=` reduced denominator of `L_1 δ_1`. Then
> ```text
>          a_1 = e V_2  ≡  0  or  1   (mod Δ_1).
> ```
>
> *Proof.* By Moh's search condition (4) the `δ_i` are the characteristic exponents of the
> branch, so every exponent of `σ_1` has denominator dividing `L_1`, i.e.
> `σ_1 ∈ K_1 := C((x^{-1/L_1}))`. Write `δ_1 = p/q` in lowest terms; then
> `lcm(L_1,q) = L_1Δ_1` and `Gal(C((x^{-1/L_1Δ_1}))/K_1)` is cyclic of order `Δ_1`,
> generated by `τ : T ↦ ζT` with `T = x^{-1/(L_1Δ_1)}` and `ζ` primitive. `τ` fixes `σ_1`
> and sends `x^{-δ_1} ↦ ζ^{L_1Δ_1δ_1} x^{-δ_1}` with `gcd(L_1Δ_1δ_1, Δ_1) = 1`, so `τ`
> multiplies the leading coefficient `ξ` of `ρ − σ_1` by a **primitive** `Δ_1`-th root of
> unity. `τ` permutes the roots of `g` and preserves `D_1`, so the set `{ξ_1,…,ξ_{a_1}}`
> — which by TF-0 has `a_1` **distinct** elements — is stable under that multiplication.
> Its orbits have size `Δ_1` except the orbit `{0}`, which occurs at most once. ∎

**Calibration (fail-closed, `d48final.py`).** All six of Moh's published survivor rows pass
(10)₁ — five with `a_1 ≡ 0`, one (`(75,50), V_2 = 3`) with `a_1 ≡ 1`, i.e. through Moh's
`α = 0` branch (11):

```text
   row                   δ_1     L_1  Δ_1  a_1  a_1 mod Δ_1
   (64,48)               9/16     4    4    12      0
   (84,56) M2=64,V2=2   16/21     7    3     6      0
   (84,56) M2=72,V2=5    7/12     4    3    15      0
   (75,50) V2=3           1/2     5    2     9      1     <- the α = 0 branch
   (75,50) V2=2           2/3     5    3     6      0
   (99,66)                4/9     3    3    24      0
```

### 3.4 Order `ν > 0`: the operator, in closed form

Substituting `Φ_ν = Qφ`, `Γ_ν = Pψ` and setting `X := dψ − eφ`, `Y := φ + ψ`,
`ν̂ := ν/(1−δ_1)`, one gets the compact form

```text
      L_ν(Qφ, Pψ)  =  γ (1 − ν̂) Y  +  κ [ ν̂ (PQ)' X  +  PQ X' ] .
```

For the `V = 1` bottom form (`P = π³+3π`, `Q = π²+2`, `d,e = 2,3`) the matrix of `L̃_ν̃` on
`{deg F ≤ 3} × {deg G ≤ 4}` is `6 × 9` of generic rank 6 (`kernel_L.py`, `tfcal.py`):

```text
   ν̃        1/7  1/3   1    2    3    4    5   11/2   7
   nullity    3    3    4    4    3    3    3    3    3
```

The three generic kernel vectors are identified: `(F,G) = (−Q', −P')` is the shift
`y ↦ y + a x^{-δ_1-ν}` of the whole chart (a gauge move, not geometry); the rank drop at
`ν̃ = d = 2` is `f ↦ f + const`, at `ν̃ = e = 3` it is `g ↦ g + const`. So the first
correction order is **positive-dimensional** and does not kill by itself.

**Which `Φ_ν, Γ_ν` are geometrically realisable?** From the product structure
`Γ = Π_g(x)·∏_{k}(π − ξ_k − u_k(x))·∏_{j∉D_1}(1 + π w_j)`,

```text
   Γ_ν = P(π)·(c_0 + c_1 π + c_2 π² + …) − Σ_k u_{k,ν} P/(π−ξ_k),
   Φ_ν = Q(π)·(b_0 + b_1 π + …)        − Σ_j v_{j,ν} Q/(π−η_j),
```

and since `{P/(π−ξ_k)}` is a Lagrange basis of `C[π]_{≤a_1−1}`, the realisable space at the
first order is **all** of `C[π]_{≤b_1+1} × C[π]_{≤a_1+1}`. Hence the 3-dimensional kernel is
the honest answer at order `ε`: **positive-dimensional, dimension 3**.

### 3.5 The NO-TAME theorem, and `h'(C) = 0`

The picture changes if the star's own tails are silent at that order.

> **THEOREM TF-NOTAME (PROVED-HERE; machine-checked at `V = 1`).** Suppose at order `ν` the
> tame tails contribute nothing, i.e. `Γ_ν = P(g_0 + g_1π)` and `Φ_ν = Q(f_0 + f_1π)`. Then
> `L_ν = 0` forces `f_0 = f_1 = g_0 = g_1 = 0`, for every `ν ≠ 1 − δ_1`.
>
> *Proof.* The `π^{(d+e)V}` coefficient gives `dg_1 = ef_1`; the `π^{(d+e)V−1}` one gives
> `dg_0 = ef_0`; substituting, `L_ν = πγ s[(d+e) − ν/κ] + γσ[(d+e) − ν/κ]` with
> `f_1 = ds, g_1 = es, f_0 = dσ, g_0 = eσ`, and `(d+e) − ν/κ = 0` exactly at `ν = 1−δ_1`. ∎
> At `ν = 1−δ_1` (`ν̃ = d+e = 5`) the driver returns the residual family `g_i = (e/d) f_i`.

The geometric meaning of `g_1` and `f_1` is explicit. At level 2, Moh Prop 4.6(1) gives
`g_σ = p_2^{n/d_2} = p_2^{e}` and `T^ψ_{1,σ} = p_2^{m/d_2} = p_2^{d}`, and the bottom disc is
a root `C` of `p_2` of multiplicity `V_2`. Writing `h := p_2/(π−C)^{V_2}`, the outer roots
nearest `D_1` sit at contact `δ_2`, so at `ν = ε := δ_1 − δ_2`

```text
      g_1 = e·h'(C)/h(C),      f_1 = d·h'(C)/h(C)     (ratio d : e automatic).
```

So under the NO-TAME hypothesis at `ν = ε`,

```text
      (TF-1)      h'(C) = 0,   i.e.   Σ_{j ≠ i} V_j/(C_i − C_j)  +  w'(C_i)/w(C_i) = 0
```

for every bottom-major disc `C_i`, where `p_2 = ∏_i (π−C_i)^{V_i} · w(π)`.

### 3.6 The exhausting corollary

> **COROLLARY TF-EXH (PROVED-HERE; identity machine-checked, `k = 2..6`).** If the
> bottom-major discs exhaust their `D_2` (`w` constant; for `s = 3` this is
> `Σ_B V_2(B) = u = deg p_2`, i.e. the ceiling `N = U` attained), then under the NO-TAME
> hypothesis there is **at most one** bottom-major disc.
>
> *Proof.* Multiply (TF-1)`_i` by `V_i C_i` and sum; pairing `(i,j)` with `(j,i)`,
> `Σ_{i≠j} V_iV_jC_i/(C_i−C_j) = Σ_{i<j} V_iV_j > 0`, contradicting `0`. ∎

For equal weights this is `W''(C_i) = 0` for all roots of `W = ∏(π−C_i)`, i.e. `W | W''`,
i.e. `deg W ≤ 1`. The automorphism control `(y, x+y^k)` sits exactly at `k = 1` disc.

Applied to the selected skeleton at `N = 9` (`k = 12` discs, `Σ_B V_2 = u = 12`,
exhausting): **dead** under NO-TAME. At `N = 6` (`k = 8`, `deg w = 4`) TF-1 is 8 equations
that are individually satisfiable, and one must go to order `2ε`.

### 3.7 Orders `2ε` and beyond — what is NOT done

At `ν = 2ε` the operator is the same `L̃` at `ν̃ = 2ε/κ`, but `R_{2ε}` is the quadratic form
in the order-`ε` data and needs the second symmetric functions `Σ_{i<j}w_iw_j` of the outer
series plus the star-tail cross terms — mechanical, a different size of computation.
**This lane did not impose order `2ε`**; it is `OPEN[TF-ORDER2]` (§8), and it is why item 7
of §1 says "positive-dimensional", not "determined".

---

## 4. Part (3): at which order does the `D = 48` skeleton die?

### 4.1 The answer for the selected skeleton

```text
   SELECTED  (48,32) M = (−32,−12,46), V = (1,3):  L_1 = lcm(1,22) = 22,
             Δ_1 = den(22·3/8) = den(33/4) = 4,   a_1 = 3,   3 mod 4 = 3 ∉ {0,1}
   =>  DEAD at ORDER 0, by the star congruence (10)_1.
```

It never reaches a correction order. Note *how* it dies: not through the ODE `(BOTTOM)`
(which is solvable at `V_2 = 1`, §3.2, with `P = π³+3π`, `Q = π²+2`), but through the
`Δ_1 = 4` automorphism, which cannot act on a 3-element set of distinct `ξ`'s with at most
one fixed point. The runner-up `M = (−32,4,46)`, `V = (2,3)` has `Δ_1 = 1` and passes
(10)₁; it fails Moh (10) at level 2 instead (`Δ_2 = 16`, `Δ_2V_2 = 32 > v_2 = 12`).

### 4.2 Is the killing condition a SKELETON condition?

**Yes, entirely.** `(10)₁` depends only on `(n, m, M_*, V_*)` through `δ_1, …, δ_s` and
`a_1 = eV_2` — it is a candidate **Moh condition (16)** in the charge's sense, except that
it is not new: it is Moh's own (8)–(11) at `r = 1`, which the campaign census does not
implement. What *is* new here is (a) the proof at `r = 1` with the **simple-root** input
(TF-0 / D1-STAR(d)), which sharpens Moh's multiplicity-`V_{r−1}` version to the congruence
`a_1 ≡ 0,1 (mod Δ_1)`, and (b) the measurement of its cost on the campaign census.

The conditions of §3.5–3.6 (`h'(C) = 0`, "exhausting ⟹ one disc") are **not** skeleton
conditions: they constrain the level-2 configuration `p_2`, i.e. the realisation. The
`N = U` corollary is however *nearly* skeletal — it says the ceiling row of the knapsack is
attainable only with a single bottom disc.

### 4.3 Moh's (10) at `j ≥ 2`, reconstructed

The OCR of (9)–(11) is unrecoverable. The structure is not: at level `j` the `Δ_j`-automorphism
permutes the roots of `p_j` in orbits of size `Δ_j` (for `α ≠ 0`), multiplicities constant
along orbits, so the chosen factor of multiplicity `V_j` needs

```text
   (10)      Δ_j · V_j  ≤  v_j = V_{j+1} d_j/d_{j+1}       (j = 2,…,s−1;  α ≠ 0 branch)
```

**Typed `RECONSTRUCTED / UNREVIEWED`.** Calibration: all six of Moh's published rows pass,
two of them at equality (`(64,48)`: `4·3 = 12 = v_2`; `(99,66)`: `3·8 = 24 = v_2`). The
`α = 0` alternative (11) is **not** reconstructed, so **(10) at `j ≥ 2` may over-kill**: the
numbers below that use it are a *kill ceiling*, not a measurement. The level-1 statement
(10)₁ has both branches and is not subject to this caveat.

---

## 5. The census at `D ≤ 120`

### 5.1 With (10) + (10)₁ (the `j ≥ 2` clause is the reconstruction; kill CEILING)

`sweep.py`, 26 degrees with a nonempty census in `[48,120]`:

```text
     D   V-skel    groups  g:(10)  g:+(10)_1  g:+knapsack        D   V-skel  groups (10) (10)_1 knap
    48     1301        50      12          0           0        96   130186    1113  109     25     23
    54      514        40       5          2           2        99     1180      50   11      6      4
    60     3623       110      20          7           6       100    26873     732   66     14     13
    63      438        30       6          2           1       102      984      40    7      3      3
    64     2417        84      12          4           4       104      786      42    5      3      3
    66      390        25       3          0           0       105     5037     264   38      8      3
    72    15694       316      47         11          10       108    85205     824   84     39     30
    75      682        40       6          3           3       110     1890     120   12      1      1
    78      558        30       5          0           0       112    47655    1163   93     20     17
    80    16074       496      56         10           9       114     1242      45    8      3      3
    81      764        40       4          1           1       117     1686      60   11      4      3
    84    10748       207      36         16          13       120   516309    4104  301     86     62
    88      550        35       4          1           1
    90    30107       577      51         18          18
   TOTAL  V-assignments 902 893 → (10) 3 760 → (10)_1 329
          groups 10 637 → (10) 1 012 → (10)_1 287 → knapsack-alive (N ∈ [6,16]) 233
          degrees EMPTIED:  D = 48, 66, 78
```

The base column reproduces the reviewed integration-#17 numbers exactly
(`902 893` `V`-assignments; per-degree groups `105: 264, 108: 824, 112: 1163, 117: 60,
120: 4104`), which calibrates this lane's census against the charged inputs.
**No degree above 100 is claimed emptied** — none is.

The three surviving `D = 105` groups (all `(d,e) = (2,3)`, `s = 3`, `a_1 = 3`):

```text
   m=70  M = (28,103)  V_s = 5  u = 25   N ∈ {6,…,12}
   m=70  M = (28,103)  V_s = 6  u = 30   N = 9
   m=70  M = (40,103)  V_s = 4  u = 28   N = 9
```

### 5.2 With (10)₁ alone (fully proved, both branches)

`sweep1.py`, `D ∈ [48,90]` complete at the time of sealing (`D ≥ 96` still running; §5.1
covers those degrees under the reconstruction):

```text
     D   V-skel  V:(10)_1   groups  g:(10)_1  g:+knapsack
    48     1301       207       50        42          23
    54      514        42       40        31          10
    60     3623       608      110       101          45
    63      438        25       30        20           5
    64     2417       408       84        71          48
    66      390        21       25        17           2
    72    15694      2165      316       287         205
    75      682        68       40        36          13
    78      558        24       30        18           2
    80    16074      2429      496       435         179
    81      764        49       40        31          12
    84    10748      1366      207       185         106
    88      550        39       35        22           5
    90    30107      3699      577       496         261
   TOTAL 48..90: V-assignments 83 860 → 11 150 (86.7% killed);
                 groups 2 080 → 1 792 → knapsack-alive 916.
```

**Honest reading.** (10)₁ alone is a very strong filter on `V`-assignments (86%) but a weak
one on *groups* (14%): a group dies only when **every** admissible `V_2` fails the
congruence. It does **not** empty `D = 48` on its own; it kills the charge-selected
skeleton and 1094 of the 1301 `D = 48` assignments, and the group-level emptying of
`D = 48, 66, 78` needs the `j ≥ 2` clause as well.

---

## 6. Part (4): controls

All fail-closed; `tfcal.py` reports **37 checks, 0 failures**; the charged `jacfibre.py`
reruns **101 checks, 0 failures**.

```text
  CONTROL A  (y, x + y^k), k = 2..8.  δ_1 = −1/k, A = 1/k, B = 1, P = π^k + 1, Q = π.
             A + B − 1 + δ_1 = 0 verified;  (BOTTOM) A Q P' − B Q' P = −1 = [f,g] EXACTLY,
             on every k.  One bottom disc (k = 1), consistent with TF-EXH.
  CONTROL B  (y + x², x + (y+x²)²).  Keller verified;  JAC-FIBRE d/dx f(τ) = J/g_y verified
             on BOTH branches τ = −x² ± √(c₂−x);  the LAGRANGE INTERPOLANT of the two time
             functions returns f = y + x² EXACTLY (conditions (i)+(ii) satisfied, f
             recovered) — the charge's second control, passed.
  CONTROL C  NEGATIVE.  f = y with g = x²+y³, x³+y⁴, and f = y², g = x+y³: J = −2x, −3x²,
             −2y, none constant; the general law d/dx f(τ)·g_y(τ) = J(τ) still holds, the
             KELLER value does not.  Charged jacfibre.py CONTROL C: the four non-Keller
             two-tower rows of N-ON-THE-TREE have ord_t(f g_y)(τ) ∈ {−3}, {−6,−17/3},
             {−20/3}, {−5,−9/2} — never the Keller value −1: polynomiality of the time
             function FAILS on every one, as charged.
  CONTROL D  (BOTTOM) forces simple roots: three planted degeneracies (double root of P,
             double root of Q, common root) each drive γ to 0.
  CONTROL E  TF-EXH's identity Σ_i V_iC_i·cond_i = Σ_{i<j} V_iV_j verified symbolically for
             k = 2,…,6 with indeterminate C_i, V_i.
  CONTROL F  Moh's six published rows pass (10) and (10)_1 (§3.3) — fail-closed assertion.
```

---

## 7. Corrections to charged inputs and to the record

1. **`d1-subtree-review-grok46` item (d)**: "intra-`f` clustering below `δ_1` is free" —
   **REFUTED**. Moh Prop 4.6 (`r = 1`) forces `Q = p_f` to have simple roots (TF-0), so no
   two `f`-roots of a bottom-major disc share a leading `π`-coefficient. "Invisible to `N`"
   is correct; "free" is not.
2. **`moh_skeleton_N.py` / `d1floor.py` / `general.py` census**: implements Moh (1)–(7) and
   Def 5.1(2) but **not (8)–(11)**. Every integration-#17 filter number
   ("98.98% of `V`-assignments", "60.04% of groups", the per-degree `264/209`, `824/419`,
   `1163/795`, `60/47`, `4104/2390`, "NO degree is emptied") is therefore computed on a
   strict superset of Moh's admissible skeletons. The numbers are correct *as stated about
   that superset*; they are not statements about Moh's search space.
3. **The charge's framing** of `general.log` ("killed 9 of them at `N ≥ 6`"): that log ran
   `N ∈ [4,16]` with `CAP = 6·10^4`. At `N ∈ [6,16]` with `CAP = 2·10^5` the `D = 48`
   figures are 11 killed, 0 capped, 39 alive (§2.1).
4. **`OPEN[STAR-REALISABILITY]`** (integration #17 §C) is **ANSWERED NEGATIVE** at the level
   at which it was posed: the bottom polynomial's roots are never *forced* to collide; the
   ODE is solvable at every `(d,e,V)` (TF-DESSIN). The census filter that the Open was
   hoping for exists, but it is the Galois congruence (10)₁, not a repeated root.
5. **`PIN-NOT-CEILING`** is untouched; **`D1-PIN`** gains an interpretation:
   `A + B − 1 + δ_1 = 0` — i.e. floor = ceiling at `r = 1` — is precisely the reason Moh's
   `r = 1` clause has a **nonzero constant** on the right, rather than `0` (levels `r ≥ 2`,
   where Appendix I A.1 applies) or `c·p(π)` (Appendix I A.3).

---

## 8. Opens raised, with bounded quantities

- **`OPEN[TF-ORDER2]`** — impose (♦) at `ν = 2ε` (and the next tame order) on a surviving
  skeleton. *Bounded quantity*: the quadratic form `R_{2ε}` in the 9 order-`ε` unknowns
  (`V_2 = 1`) plus the 5 new order-`2ε` unknowns; one `14 × (6+…)` linear system over `Q(ν̃)`
  after the quadratic is expanded. Nothing here claims what it yields.
- **`OPEN[MOH-11]`** — reconstruct Moh's `α = 0` alternative (11) at `j ≥ 2` from a clean
  scan of p.201, and re-measure §5.1. *Bounded quantity*: one inequality; the affected count
  is at most `3760 − 329 = 3431` `V`-assignments and `1012 − 287 = 725` groups over
  `D ≤ 120`.
- **`OPEN[TF-NOTAME-SCOPE]`** — decide when the star tails are genuinely silent at
  `ν = ε = δ_1 − δ_2`. The tame exponents lie in `(1/r_ρ)Z`; `ε` is an allowed tame exponent
  iff `den(ε) | r_ρ`. *Bounded quantity*: the branch indices `r_ρ` of the `a_1` star roots,
  a divisor of `u·e` at each of at most `u` bottom discs.
- **`OPEN[CENSUS-REBASE]`** — rerun the integration-#17 integrality/knapsack programme on
  the census **with** (8)–(11), and re-derive the "no degree emptied" reading.
  *Bounded quantity*: 287 groups at `D ≤ 120` (233 after the knapsack) instead of 10 637.
- **`OPEN[DESSIN-COUNT]`** — the number of `(BOTTOM)` solutions modulo the 4-dimensional
  symmetry group equals the number of the cubic plane maps of TF-DESSIN. *Bounded quantity*:
  plane trees with `V+1` leaves and `V−1` trivalent vertices, with a loop attached at each
  leaf; `1` at `V = 1`, `1` at `V = 2`.

---

## 9. FALLACY-v2 audit

- **Flag/place/series.** Kept apart: the *skeleton* `(n,m,M_*,V_*)`, the *radii* `δ_i`
  (place), the *leading forms* `p_i` (series). (10)₁ is about the first two; `h'(C)=0` is
  about the third and is never promoted to a census filter.
- **Carrier/attainment.** TF-DESSIN gives **existence** (Riemann existence + explicit
  witnesses at `V = 1,2`), not a count — `OPEN[DESSIN-COUNT]` records the gap. (10)₁ is
  necessary only; no skeleton is asserted realisable.
- **Floor/attainment.** §5.1's kill numbers are a **ceiling** (unreconstructed `α = 0`
  clause); §5.2's are exact for the conditions imposed. Emptying is asserted only for
  `D = 48, 66, 78`, all `< 100`, where Moh's theorem is stronger anyway.
- **Prime label/derivative.** `P'`, `Q'`, `h'`, `p_2''` are `d/dπ` in the stated chart;
  `F_i'` is `d/dx` along a branch; `λ_f, λ_g` are order functions, not derivatives.
- **Variable/ring map.** The chart `π = (y−σ_1)x^{δ_1}` is declared with its Jacobian
  `x^{δ_1}`; coefficient field `C`; Puiseux field `C((x^{-1/r}))`, `ord_t x = −1`.
- **Target/arrival index.** `Δ_j` indexes the *radius* `δ_j`, `V_j` the *multiplicity at
  level `j`*, `v_j = V_{j+1}d_j/d_{j+1}` the *degree of `p_j`* — three distinct indices,
  never identified.
- No exit-price assertion is made, so no `charge_basis` line is required.

---

## 10. Typed verdict block

```text
LANE       TIME-FUNCTION CALIBRATION D = 48 (Opus 5), 2026-09-02
INPUTS     8/8 SHA-256 verified; flagship REPORT not read (prompt only)

PROVED-HERE
  (♦)        exact order-graded decomposition of [f,g] = c at a bottom-major disc;
             A + B − 1 + δ_1 = 0 is D1-PIN, and is why Moh's r=1 right side is a
             nonzero CONSTANT.
  TF-0       (BOTTOM) d Q P' − e Q' P = γ ≠ 0 forces simple roots for BOTH p_g and
             p_f and gcd(p_g,p_f) = 1.  [second proof of D1-STAR(d); refutes
             "intra-f clustering is free"]
  TF-DESSIN  Q^e/P^d is a genus-0 Belyi map with profile (d^{eV} | e^{dV} |
             ((d+e)V−1, 1^*)); the dessin exists for every (d,e,V) ⟹ (BOTTOM) is
             ALWAYS solvable ⟹ Moh's leading order NEVER kills a skeleton.
             Witnesses V = 1, 2 at (d,e) = (2,3).
  (10)_1     a_1 = eV_2 ≡ 0 or 1 (mod Δ_1), Δ_1 = den(L_1 δ_1),
             L_1 = lcm{den δ_s,…,den δ_2}.  = Moh (8)–(11) at r = 1, sharpened by
             simple roots.  All six published Moh rows pass.
  TF-NOTAME  on the tame-silent subspace, L_ν is injective for every ν ≠ 1 − δ_1;
             geometrically h'(C) = 0 with h = p_2/(π−C)^{V_2}.
  TF-EXH     bottom-major discs exhausting their D_2 (ceiling N = U) ⟹ at most ONE
             of them, under TF-NOTAME.  Identity checked k = 2..6.

RECONSTRUCTED / UNREVIEWED
  (10) j≥2   Δ_j V_j ≤ V_{j+1} d_j/d_{j+1}.  OCR-damaged source; α = 0 branch (11)
             NOT reconstructed, so its kill numbers are a CEILING.

MEASURED
  D = 48     50 groups / 1301 V-assignments; knapsack N∈[6,16]: 39 alive, 11 killed.
             SELECTED skeleton M = (−32,−12,46), V = (1,3), δ = (−1, 7/22, 3/8),
             a_1 = 3, q = 3/4, N ∈ {6,9}:  DEAD at ORDER 0 by (10)_1 (Δ_1 = 4).
             All 33 (10)-passing assignments fail (10)_1 ⟹ D = 48 EMPTY.
  D ≤ 120    902 893 V-assignments → 3 760 → 329 ; 10 637 groups → 1 012 → 287 →
             233 knapsack-alive.  Degrees emptied: 48, 66, 78.  D = 105: 264 → 3.
  (10)_1 alone, D ≤ 90: 83 860 → 11 150 V-assignments (86.7%); 2 080 → 1 792 groups.

NOT CLAIMED
  any degree > 100 emptied; realisability of any surviving skeleton; the value of
  order 2ε; sufficiency of (10)_1; that (10) at j ≥ 2 is Moh's exact inequality.

READING
  The time-function programme's leading order is Moh's r = 1 ODE, and that ODE is a
  BELYI CONDITION that is always satisfiable — it is not the missing filter.  The
  missing filter sits at the SAME order but in the Galois layer, and it is Moh's own
  conditions (8)–(11), which the campaign census does not implement.  At D = 48 the
  method detects the unrealisability at order 0 and the degree empties; the
  correction orders are not needed there.  The campaign's next move is
  OPEN[CENSUS-REBASE], not a deeper Puiseux order.
```

<!-- BODY-END -->
