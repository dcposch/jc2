# The k = 4 ray DEGREE-BOUND TOWER — the tower collapses into one theorem, and the gap does **not** close

Lane `k4ray-degree-tower-opus5-20260903`; adapter opus.
Drivers, logs and `artifacts.sha256`: `box/k4raytower-20260903/` (16 files).

## 0. Provenance and verdict up front

**Input verification.** The manifest was generated mechanically from
`xmodel/k4ray-degree-tower-opus5-20260903.run.v2` with `awk` on the
`charged_input_<i>_sha256=` / `_basename=` lines and checked with
`sha256sum -c`: **10/10 OK**, no digit retyped. (An earlier lane attempt left a
`manifest.sha256` in the box directory pointing at `/tmp/jc2-lane.iifzhb`; my
check is independent, against `/tmp/jc2-lane.fyCwIX`, and the digests agree.)
Per the round's no-collision rule no in-flight lane report was opened.

**VERDICT: the numerical tower SATURATES at `c = 3`; the gap does not close.**
But the tower is *replaced* by a single, strictly stronger, `K`-uniform theorem.

| item | status |
|---|---|
| (1) reconstruction of `3 deg β ≥ 2K+1` — which coefficient, at which degree | **DONE** (§2). It is the total-degree-`(3b−K−2)` band of `J`, i.e. `3J(β_b, α_{2b−K})`, under the hypothesis `ρ ∈ k`. |
| (2) the next band — does it give `4 deg β ≥ 3K + r₄`? | **NO.** The next band gives a *divisibility*, `H² ∣ β_b³` (§5, `LEVEL 4`), whose numerical shadow is **exactly** `3 deg β ≥ 2K+1` again. The numerical tower `c·deg β ≥ (c−1)K + r_c` **saturates at `c = 3`** (§6). |
| new `K`-uniform structure | **PROVED** (§4): `deg(g²−f³−λf) = K+6` for a unique `λ ∈ k`; hence `deg(g²−f³) ≤ 2K`, `deg_y(g²−f³) ≤ 2K`, and the leading form is the *explicit* degree-`(K+6)` form `Θ` of §4.3. This single theorem re-proves the charged TOP-BAND lemma and the charged ρ-DEGREE lemma in one line each; fed into the charged §3.3 one-liner it returns `3 deg β ≥ 2K+1`; and it adds `H² ∣ β_b³`, `deg ρ = 3b−2K` exactly, `ρ ∉ k[x]`, `3 deg_y β ≥ 2K+1`. |
| (3) do the tower + the composite arm leave a finite set of `(K, deg β)`? | **NO, and the premise is wrong.** The charged composite arm (17(vvvvv) §3.2) kills `β ∈ k`, i.e. `deg β = 0` — **not** `deg β < K`. There is no "meeting point" to reach. Separately, the *divisibility* tower `H^{c−1} ∣ β_b^c` would kill every row at depth `c = K` (§6.3), not at any bounded depth. |
| (4) residual stratum and its width | **EXPLICIT** (§7): `max(⌈(2K+1)/3⌉, ⌈2(K−1)/3⌉+1) ≤ deg β ≤ 2K−1`, width `→ 4K/3`, **growing linearly in `K`**. |
| (5) controls | **ALL PASS** (§8): `K = 1` positive control reproduces `deg E = K+k+2` and the terminal identity exactly; the composite pair is consistent (it fails the hypothesis `c ≠ 0`, not the conclusion); `K = 4, 5` are covered; FALLACY-v2 exclusion check stated and run. |
| actionable by-product | **The wall rows are pinned.** At `K = 8, b = 6` and `K = 9, b = 7` — rows that timed out in 17(yyyyy) — LEVEL 4 forces `β_b = μ·y^{K−3}(y−x)`: **one** scalar, down from `b+1` (§7.2). |

**The one sentence a reader should carry away:** the conjectured ladder of
degree bounds is not a ladder — its second rung already re-derives the first, and
what actually holds is a *single* uniform statement, `deg(g²−f³−λf) = K+6`, from
which every charged bound falls out; the residual stratum it leaves is
`⌈2(K−1)/3⌉+1 ≤ deg β ≤ 2K−1`, of width `∼ 4K/3`, and it is **not** bounded.

**FALLACY-v2 posture.** No exit claim is made, so no `charge_basis` line is
emitted. *Floor/attainment:* `deg(g²−f³−λf) = K+6` is an **equality**, proved in
both directions (`≥` from the Jacobian degree count, `≤` from the band lemma plus
`deg_y(g²−f³) ≤ 3K−1`); the leading form `Θ` is *attained*, not bounded.
*Carrier/attainment:* `H² ∣ β_b³` is a **necessary condition on `β`**, not a
kill; §8.3 runs the exclusion check and reports that the admissible band is
non-empty for every `K`. *Prime label/derivative:* every `'` below is `d/dy` and
is defined where used. `sat()` was not used. No modular-only result is promoted;
no Gröbner chart was submitted at all (§9).

---

## 1. Instrument and notation

Ray coordinates as charged (17(vvvvv) §2), unchanged:

```text
R_4 = { (n,m; M2',V2'; k) = (3K,2K; 3K-6; K-1; 4) : K >= 4 },  (x,y) = (gamma,pi)
H := y^(K-1) (y-x)        the two-point leading form,   deg H = K
h                          monic in y, deg_y h = K, lf(h) = H
beta                       deg_y beta <= K-1 (approximate-root bound, PROVED in 17(vvvvv) §2.3)
b := deg beta (total),     P := beta_b  (leading form),  b <= 2K-1
alpha := quo_y(beta^2,h),  rho := rem_y(beta^2,h)   so   beta^2 = alpha h + rho,  deg_y rho <= K-1
f := h^2 + 2 beta          g := h^3 + 3 beta h + (3/2) alpha
J := f_x g_y - f_y g_x  =  c x^4,  c != 0          (Moh p.207: the Jacobian column is X^4)
```

Filtered-division bounds re-verified: `deg α ≤ 2b−K`, `deg ρ ≤ 2b`,
`deg_y α = 2 deg_y β − K`. Charged identity **ID6** `J = 3[J(β,α) − J(h,ρ)]`
re-verified at `(K,b) = (4,3), (4,5), (5,4), (5,7), (7,6), (7,9), (9,7)`:
`MARK_ID6_* 0`, all seven (`tower_ident.out`).

Throughout, `E := g² − f³`, `[·]_D` is the total-degree-`D` band, and for binary
forms `x·J(F,G) = (deg F)·F G_y − (deg G)·F_y G` (Euler), used repeatedly.

> **LEMMA BF.** For nonzero binary forms `F` (degree `n`), `G` (degree `m`),
> `J(F,G) = 0` ⟺ `G^n = λF^m` for some `λ ≠ 0`.
> *Proof.* `∂_y(G^nF^{−m}) = G^{n−1}F^{−m−1}(nFG_y − mGF_y) = xG^{n−1}F^{−m−1}J(F,G)`,
> and a degree-`0` homogeneous rational function constant in `y` is a constant. ∎

> **LEMMA INJ (charged, re-verified).** `deg_y R ≤ K−1`, `deg R = e ≥ 1`,
> `J(H,R) = 0` ⟹ `R = 0`.
> *Proof.* LEMMA BF gives `R^K = λH^e`; matching the valuation at `y−x` gives
> `K ∣ e`, then at `y` gives `R = λ'H^{e/K}`, whose `y`-degree is `e ≥ K`. ∎
> *Machine.* `MARK_C1_INJ only_trivial 196 of 196` for `K = 4…10` and every
> `e = 1…4K` (`struct_checks.out`); `MARK_C1_SHARP` prints `J(H,1) = 0`, so
> `e ≥ 1` cannot be dropped.

---

## 2. (1) The charged `3 deg β ≥ 2K+1`, reconstructed exactly

The charged proof (17(yyyyy) §3.3) is a two-coefficient argument. Written out
with the coefficient and the degree named:

**Coefficient A — the `ρ`-degree lemma.** With `d := deg ρ ≥ 1`, the highest
band of `J = 3[J(β,α) − J(h,ρ)]` that `J(h,ρ)` can occupy sits at total degree
`K + d − 2` and equals `−3·J(H, ρ_d)`; `J(β,α)` cannot reach it once
`d > 3b−2K`, because `deg J(β,α) ≤ b + (2b−K) − 2 = 3b−K−2`. Since
`K+d−2 ≥ K−1 > 4` for `K ≥ 7`, **that coefficient of `J` must vanish**, so
`J(H,ρ_d) = 0`, so `ρ_d = 0` by LEMMA INJ. Hence `deg ρ ≤ max(0, 3b−2K)`.

**Coefficient B — the kill.** Assume `3b ≤ 2K`. Then `ρ ∈ k`, `J = 3J(β,α)`, and
the *top* band of `J`, at total degree

```text
                D0 := 3b - K - 2 ,
```

is `3·J(P, A)` with `P = β_b`, `A = α_{2b-K}`. The top band of `β² = αh + ρ`
gives `P² = A·H`, whence the cofactor identity `H·J(P,A) = A·J(H,P)`. For
`D0 ≠ 4` this coefficient of `J` must vanish, so `J(H,P) = 0`, so `P = 0` by
LEMMA INJ — contradiction. The single exception `D0 = 4`, i.e. `3b = K+6`,
forces `K = 9, b = 5` and is killed by hand. ∎

So the answer to (1) is: **the coefficient is `[J]_{3b−K−2} = 3J(β_b, α_{2b−K})`,
and what forces the bound is its vanishing together with `β_b² = α_{2b−K}·H`.**

---

## 3. The reformulation that makes iteration mechanical

Band-chasing on `J` is awkward because `α` and `ρ` are *quotient and remainder*,
so their bands are not free. The whole difficulty disappears on `E = g² − f³`.

> **IDENTITY (E-CUBIC, new).**
> `g² − f³ = β³ − 3ρh² − 9βρ + (9/4)α²`.

Verified exactly at all seven `(K,b)`: `MARK_ECUBIC_* 0` (`tower_ident.out`).
Two further facts, both machine-checked:

> **IDENTITY (JfE).** `J(f, E) = 2g·J(f,g) = 2c x⁴ g`, of degree `3K+4`.
> (`MARK_JfE_* 0`, all seven.)

> **LEMMA YDEG.** `deg_y(g²−f³) ≤ 3K−1`, and the bound is **sharp**.
> *Proof.* In E-CUBIC: `deg_y(ρh²) = deg_yρ + 2K ≤ 3K−1`;
> `deg_y(αβh) = 3 deg_yβ ≤ 3K−3`; `deg_yα² = 4deg_yβ−2K ≤ 2K−4`;
> `deg_y(βρ) ≤ 2K−2`. ∎
> *Machine.* `MARK_YDEGE_* 0` in all seven instances, with `deg_y E = 3K−1`
> attained in every one (`11, 11, 14, 14, 20, 20, 26`).

`E` is a *polynomial*, so its bands are honest binary forms; no Puiseux series,
no `f^{1/2}`, no completion is needed anywhere below.

---

## 4. The BAND LEMMA and the MASTER theorem

### 4.1 The band lemma

> **BAND LEMMA.** Let `J(f,g) = c x^k`, `c ≠ 0`, `lf(f) = H²`, `lf(g) = H³`, and
> let `Φ ∈ k[f,g]` with `Φ_g ≠ 0`, `Φ(f,g) ≠ 0`, `D := deg Φ(f,g)`. Then
> ```
>            k + deg Phi_g(f,g)   <=   2K + D - 2 ,
> ```
> with **equality iff** `J(H, Φ_D) ≠ 0`;
> and if `J(H,Φ_D) = 0` then `K ∣ D` and `Φ_D = λH^{D/K}` with `λ ≠ 0`.
>
> *Proof.* `J(f, Φ(f,g)) = Φ_g(f,g)·J(f,g) = c x^k Φ_g(f,g)`, of degree
> `k + deg Φ_g(f,g)`. On the other side `deg J(f,Φ) ≤ deg f + D − 2` with leading
> form `J(H², Φ_D) = 2H·J(H,Φ_D)`. The last clause is LEMMA BF applied to
> `(H, Φ_D)` exactly as in LEMMA INJ. ∎

Applied to `Φ = g²−f³` (so `Φ_g = 2g`, `deg Φ_g(f,g) = 3K`) with `k = 4`:

```text
   either  D = K + 6      (and J(H, E_D) != 0),
   or      D > K + 6,  K | D,  E_D = lambda H^(D/K),  lambda != 0.
```

### 4.2 MASTER

> **MASTER THEOREM (uniform in `K ≥ 7`).** For a ray-`R_4` tower pair with
> `J(f,g) = c x⁴`, `c ≠ 0`, there is a **unique** `λ ∈ k` with
> ```
>                 deg ( g^2 - f^3 - lambda f )  =  K + 6 .
> ```
> Consequently `deg(g²−f³) ≤ 2K` and `deg_y(g²−f³) ≤ 2K`.
> For `4 ≤ K ≤ 6` one has `λ = 0` and `deg(g²−f³) = K+6` exactly.

*Proof.* `E ≠ 0` (else `g² = f³` and `J = 0`). By the band lemma, either
`D = K+6` (take `λ = 0`), or `K ∣ D`, `E_D = λH^{D/K}`, `D > K+6`. In the second
case `deg_y E_D = D`, because `H` is monic in `y` of `y`-degree `K`, so
`deg_y H^{m} = mK`; and `deg_y E = max_D deg_y E_D` because distinct bands share
no monomial. LEMMA YDEG then forces `D ≤ 3K−1`. The multiples of `K` in
`(K+6, 3K−1]` are exactly `{2K}` for `K ≥ 7` and **none** for `K ≤ 6`
(`MARK C2` table, `struct_checks.out`, `K = 4…15`). So `D = 2K` and
`E_{2K} = λH² = λ·lf(f)`. Put `E' := E − λf ≠ 0` (else `J(f,E) = 0`). Then
`J(f,E') = 2cx⁴g` still, `deg E' < 2K`, `deg_y E' ≤ 3K−1`, and the same
dichotomy applies to `E'`: `deg E' = K+6`, or `K ∣ deg E'` with
`K+6 < deg E' < 2K` — and there is no multiple of `K` in `(K+6, 2K)` for
`K ≥ 7`. Uniqueness of `λ` is immediate from `deg f = 2K > K+6`. ∎

### 4.3 The terminal form `Θ` is explicit

Comparing leading forms in `J(f, E−λf) = 2c x⁴ g` gives, with
`Θ := (E−λf)_{K+6}`,

```text
                    J( H , Theta )  =  c x^4 H^2 .
```

Solved exactly over **Q** as a linear system in the `K+7` coefficients of `Θ`,
for `K = 7…14`: `MARK_THETA_UNIQUE 0` (zero free parameters),
`MARK_THETA_RESID 0`, `MARK_THETA_DIV 0` in all eight (`theta_solve.out`). The
solution is

```text
   Theta = y^K (y-x)^2 * Theta_1 ,     Theta_1 = sum_{i=0..4} e_i x^(4-i) y^i ,
   e_0 = c/(5K-6) ,    e_i = (5-i) K e_{i-1} / ( (5-i) K - 6 )   for i = 1..4 .
```

(The denominators `(5−i)K−6` are nonzero exactly when `K ∤ 6`; `K = 6` is the
excluded case.) Printed at `K = 7, 8, 9`:

```text
K=7  Theta_1 ∝ 110 x^4 + 140 x^3 y + 196 x^2 y^2 + 343 x y^3 + 2401 y^4
K=8  Theta_1 ∝ 195 x^4 + 240 x^3 y + 320 x^2 y^2 + 512 x y^3 + 2048 y^4
K=9  Theta_1 ∝  35 x^4 +  42 x^3 y +  54 x^2 y^2 +  81 x y^3 +  243 y^4
```

The valuation reading of `y^K(y−x)² ∣ Θ` is worth recording: `v_y(Θ) ≥ K` and
`v_{y−x}(Θ) ≥ 2` follow from the ODE `Kηθ' − (K+6)η'θ = cη²`
(`η := H(1,y) = y^{K−1}(y−1)`) because the indicial roots
`σ = (K+6)(K−1)/K` and `τ = (K+6)/K` are **non-integral** exactly when `K ∤ 6`.

---

## 5. What MASTER gives: the whole charged tower, one line each

**Scope: `K ≥ 7` throughout this section**, where MASTER reads `deg E ≤ 2K`;
`4 ≤ K ≤ 6`, where the threshold is `K+6` instead, is done in §8.4.
Write `P := β_b`, `A := α_{2b−K}`, `R := ρ_{3b−2K}`, `d := deg ρ`. Degrees in
E-CUBIC: `deg β³ = 3b`, `deg(ρh²) = d+2K`, `deg(βρ) = b+d`, `deg α² = 4b−2K`;
and `b < 2K` makes `b+d < d+2K` and `4b−2K < 3b`.

**LEVEL 2 (= charged TOP-BAND).** `[E]_{2b+2K} = −3·[ρ]_{2b}·H²`
(`MARK_EBAND_TOP_* 0` and `MARK_A2_ALL 0`, four instances, `eband_top.out`;
the other three E-CUBIC terms have degrees `3b`, `b+d ≤ 3b`, `4b−2K`, all
`< 2b+2K`). Since `2b+2K > 2K`, MASTER kills the band, so `[ρ]_{2b} = 0`, i.e.
`H ∣ P²`, i.e. `y^{⌈(K−1)/2⌉}(y−x) ∣ P`. **This is 17(vvvvv) §4.2.**

**LEVEL 3 (= charged ρ-DEGREE).** If `d > 3b−2K` then `d+2K > 3b` and
`[E]_{d+2K} = −3ρ_d H² ≠ 0` with `d+2K > 2K` — killed by MASTER. Hence
`deg ρ ≤ 3b−2K`. **This is 17(yyyyy) §3.2, with no `J`-band bookkeeping at all.**

**LEVEL 4 (NEW).** Now `deg(ρh²) ≤ 3b` and `[E]_{3b} = P³ − 3RH²`. Feeding
LEVEL 3 into the charged one-liner reconstructed in §2 gives `3b ≥ 2K+1 > 2K`
(LEVEL 4 is therefore *downstream* of that bound, not an independent proof of
it), and MASTER then kills the band:

> **LEVEL-4 LEMMA (uniform in `K ≥ 7`).**
> ```
>            H^2  |  beta_b^3       and       rho_{3b-2K}  =  beta_b^3 / (3 H^2) ,
> ```
> and `deg ρ = 3b−2K` **exactly** (if `R` were `0`, `P³ = 0`).

*Machine.* The closed form is verified directly: for `K = 7, 8, 9, 10, 12` and
four shape families each, `A·J(H,P) = H·J(H,R)` holds with `A = P²/H`,
`R = P³/(3H²)`, together with `deg_y P ≤ K−1`, `deg_y A ≤ K−2`,
`deg_y R ≤ K−1`, `deg R = 3b−2K`: `MARK_E_SOLVES 0` in **20 of 20**,
`MARK_E_ALL 0` (`level4_closed.out`). The competing homogeneous solution
`R + (2/3)λH^{(3b−2K)/K}` of the same first-order equation is excluded by
LEMMA INJ plus `deg_y R ≤ K−1`: it needs `K ∣ 3b` **and** `3b−2K ≥ K`, i.e.
`b ≥ K`, **and** `b ≤ K−1` — empty for every `K` (`MARK E2`, `K = 7,8,9,12`).

**LEVEL 4′ (NEW, the `y`-degree side).** MASTER also gives `deg_y E ≤ 2K`. In
E-CUBIC the two `y`-leading terms are `−3ρh²` (`deg_y = deg_yρ + 2K`) and `β³`
(`deg_y = 3 deg_yβ`), the other two being strictly smaller. Therefore:

* if `deg_y ρ = 0` then `R = c_R x^{3b−2K}` and LEVEL 4 reads
  `P³ = 3c_R x^{3b−2K} y^{2K−2}(y−x)²`, whose `(y−x)`-multiplicity is `2 ≢ 0 mod 3`
  — **not a cube**. Contradiction. So `ρ ∉ k[x]`.
* hence `deg_yρ ≥ 1`; and if `deg_yρ + 2K > 3 deg_yβ` the `y`-band
  `[y^{deg_yρ+2K}]E = −3·(y‑lead of ρ) ≠ 0` would give
  `deg_y E = deg_yρ+2K > 2K`, contradicting MASTER. So `deg_yρ + 2K ≤ 3 deg_yβ`,
  hence
  ```
                3 * deg_y(beta)  >=  2K + 1 ,      1 <= deg_y(rho) <= 3 deg_y(beta) - 2K <= K-3 .
  ```

This is sharper in kind than the charged bound (it constrains `deg_y β`, not just
`deg β`), and `deg_y ρ ≤ K−3` improves the structural `deg_y ρ ≤ K−1`.

---

## 6. (2)+(3) The iteration, and why it saturates

### 6.1 The next band is a divisibility, not a bound

The band one deeper than the charged argument's is exactly `[E]_{3b}`, and what
it yields is `H² ∣ P³` — a *divisibility*, not an inequality. Its numerical
shadow is obtained from `P = y^s (y−x)^t x^u Q̃` with `gcd(Q̃, xy(y−x)) = 1`:

```text
   H | P^2   =>  2s >= K-1, 2t >= 1  =>  s >= ceil((K-1)/2), t >= 1
                 =>  deg_y P >= ceil((K-1)/2) + 1   =>  2 deg beta >= K + 1      [charged, c=2]
   H^2 | P^3 =>  3s >= 2(K-1), 3t >= 2 =>  s >= ceil(2(K-1)/3), t >= 1
                 =>  deg_y P >= ceil(2(K-1)/3) + 1 =>  3 deg beta >= 2K + 1      [charged, c=3]
```

using `deg β ≥ deg_y β_b = s+t+deg Q̃`. **The second line is the charged
17(yyyyy) bound verbatim** — and LEVEL 4 was derived *assuming* that bound, so
its shadow adds no numerical strength whatever. That is precisely what
saturation means. The next band does **not** produce `4 deg β ≥ 3K + r₄`.

> **SATURATION.** The numerical tower `c·deg β ≥ (c−1)K + r_c` saturates at
> `c = 3` with `r_3 = 1`. Level 4 of the *band* filtration is level 3 of the
> *numerical* tower.

### 6.2 The tower that is actually running

The correct statement of the ladder is the divisibility ladder

```text
   LEVEL c :   H^(c-1)  |  beta_b^c        (c = 2 charged, c = 3 proved here, c >= 4 OPEN)
```

whose numerical shadow is uniformly `c·deg β ≥ (c−1)K + 1`, i.e. `r_c = 1` for
every `c` — matching the two charged data points `r_2 = r_3 = 1` and answering
the prompt's "find `r_c`".

### 6.3 Where the ladder would have to reach

`H^{c−1} ∣ P^c` gives `s ≥ ⌈(c−1)(K−1)/c⌉` and `t ≥ 1`, so
`deg_y P ≥ ⌈(c−1)(K−1)/c⌉ + 1`. Against `deg_y P ≤ deg_y β ≤ K−1` this is a
contradiction iff `c ≥ K`:

```text
   c = K  :  s >= ceil((K-1)^2/K) = K-1,  t >= 1  =>  deg_y P >= K  >  K-1   DEAD
```

Machine table `MARK C5` (`struct_checks.out`) prints the whole ladder for
`K = 7, 8, 9, 12`; the first `DEAD` row is `c = K` in every case. So the ladder
would close every row for every `K` — but its required depth is `K`, **not**
bounded, and only `c = 2, 3` are proved.

### 6.4 The prompt's "meeting point" does not exist

The charged composite arm (17(vvvvv) §3.2, LEMMA B2-CONST) proves: `B₂ ∈ k`
⟹ `h ∣ J(f,g)` ⟹ dead. That is `deg β = 0`, one point, **not** the half-line
`deg β < K`. I re-verified the scope by reading §3.2–§3.3 of the charged report;
the hypothesis printed there is `B₂ ∈ k`, and §3.3 adds that the weaker `α = 0`
is *not* enough (control `β = x²−y`). So the plan "tower pushes `deg β ≥ K`,
composite kills `deg β < K`, the two meet" has no lower half. What the composite
arm *does* do is guarantee the residual stratum is the nonconstant one; nothing
more.

---

## 7. (4) The residual stratum

### 7.1 Its width grows

After LEVEL 4 the admissible band for `b = deg β` is

```text
     max( ceil((2K+1)/3) , ceil(2(K-1)/3) + 1 )   <=   b   <=   2K - 1 .
```

(`struct_checks.out` C4, `controls.out` D3.)

```text
   K :   b_min  b_max   width      K :   b_min  b_max   width
   7  :    5     13       9        12 :    9     23      15
   8  :    6     15      10        20 :   14     39      26
   9  :    7     17      11        50 :   34     99      66
```

`width / K → 4/3`. **The residual stratum is not bounded; it grows linearly in
`K`.** This is the honest answer to (4).

### 7.2 …but its bottom is *pinned*, and that is the wall row

LEVEL 4 does not only bound `b`; it determines the shape of `β_b` at the bottom
of the band. Writing `P = μ y^s (y−x)^t x^u Q̃` with `3s ≥ 2(K−1)`, `t ≥ 1`,
`s+t+deg Q̃ = deg_y P ≤ min(b, K−1)`, the count of admissible shapes at
`b = b_min` is **one** for every `K = 4…14` (`struct_checks.out` C4, column
"pinned"):

```text
   K = 7,  b = 5  :  beta_5 = mu * y^4 (y-x)                 (1 scalar, was 6)
   K = 8,  b = 6  :  beta_6 = mu * y^5 (y-x)                 (1 scalar, was 7)   <-- MEASURED wall row
   K = 9,  b = 7  :  beta_7 = mu * y^6 (y-x)                 (1 scalar, was 8)   <-- MEASURED wall row
```

and then `ρ_{3b−2K} = μ³ y^{3s−2K+2}(y−x)/3` is forced too. The two rows that
`SCUT_K7_B6`/`SCUT_K9_B7`/`MOD_K7_B6` could not finish at 55–80 parameters are
exactly the rows where the top band of `β` is now a single scalar. That is a
concrete, cheap cut for the next chart lane — it is *not* a kill, and I do not
present it as one.

Two consistency notes, both against the charged census:

* `K = 9, b = 5` — the exceptional case `3b = K+6` that 17(yyyyy) §3.3 had to
  kill by hand — is below `b_min = 7`, so LEVEL 4 excludes it outright.
* `K = 7, b = 5` **is** admissible under LEVEL 4 (pinned to `μy⁴(y−x)`), yet the
  charged machine killed it (`UNIT_IDEAL_CHAR0`, 9.8 s). So LEVEL 4 is strictly
  weaker than the exact chart there: the ladder is genuinely incomplete, and I
  say so rather than claiming coverage.

---

## 8. Controls

### 8.1 Positive control — `K = 1`, target `x¹` (`PC_K1_B1_x1` of 17(yyyyy))

`h = y−x`, `β = μx`, `α = 0`, `f = (y−x)²+2μx`, `g = (y−x)³+3μx(y−x)`,
`J(f,g) = 6μ²x`. Then `E = g²−f³ = −μ²x²(8μx + 3(y−x)²)`, `deg E = 4 = K+k+2`
with `k = 1` — the band lemma's terminal degree, **attained**; and
`Θ = E₄ = −3μ²x²(y−x)²` satisfies `J(H,Θ) = 6μ²x·H²` exactly
(`MARK_PC_TERMINAL 0`), with `deg_y E = 2 = 3K−1` (`MARK_PC_YDEG_E 0`) — LEMMA
YDEG sharp here too. This control also exhibits the exceptional branch honestly:
`K ∣ k+2` holds (`1 ∣ 3`), and correspondingly `y^K(y−x)² ∤ Θ` — the divisibility
of §4.3 is claimed only for `K ∤ k+2`.

### 8.2 Composite arm — consistent, and it shows `c ≠ 0` is load-bearing

`β ∈ k` gives `α = 0`, `J(f,g) = 0`, `E = −8β³ − 3β²h²`, `deg E = 2K`, and
`E + 3β²f = −2β³` has degree `0 ≠ K+6` (`controls.out` D1, `K = 4, 7, 9`). The
MASTER conclusion fails here — as it must, because MASTER's hypothesis `c ≠ 0`
fails. A composite pair survives *as composite*, not as a counterexample.

### 8.3 FALLACY-v2 exclusion check

A degree bound kills a row only if it **excludes every admissible `deg β`**.
`controls.out` D3 evaluates the admissible band at `K = 7, 8, 9, 10, 12, 20, 50`
and finds it **non-empty in every case** (widths `9, 10, 11, 13, 15, 26, 66`).
So LEVEL 4 is a necessary condition on `β`, not a kill, and no row of the census
is claimed dead on its strength.

### 8.4 `K = 4, 5` — the bounds must hold where the row is known dead

Note first that `deg E ≤ 2K` is a `K ≥ 7` statement: for `K ≤ 6` MASTER reads
`deg(g²−f³) = K+6 > 2K`, and the band-vanishing threshold is `K+6`, not `2K`. So
LEVELS 2–4 must be re-run at that threshold; the general form of LEVEL 3 is
`deg ρ ≤ max(3b−2K, deg E − 2K)`.

Two `Θ`-valuations, machine-checked for `K = 4, 5, 7, 8, …, 14`
(`small_k.out` F1, `free = 0` in every case, `K = 6` the excluded solve):

```text
                v_y(Theta) = K   exactly ,      v_(y-x)(Theta) = 2   exactly ,
                so  H^2 = y^(2K-2)(y-x)^2  does NOT divide Theta for any K >= 3.
```

`K = 4`: the `D = 2K` escape is empty (`MARK C2`), so `deg(g²−f³) = 10` exactly.
LEVEL 2 fires for every `b ≥ 1` (`2b+2K > 10`), giving `H ∣ β_b²` and `2b ≥ 5`,
so `b ≥ 3`. At `b = 3`: `3b = 9 < 10`, and `deg ρ ≤ max(1, 2) = 2`, so the only
term of E-CUBIC that can reach degree `10` is `−3ρ₂H²`; hence `Θ = −3ρ₂H²` and
`H² ∣ Θ` — contradicting `v_y(Θ) = 4 < 6 = v_y(H²)`. So `deg β ≤ 3` is dead at
`K = 4`, reproducing the charged `CAL_K4_B3` `UNIT_IDEAL_CHAR0`
(`small_k.out` F2).

`K = 5`: `deg E = 11` exactly; LEVEL 2 gives `2b ≥ 6`, `b ≥ 3`; `b = 3` dies by
the same `H² ∣ Θ` route (`v_y(Θ) = 5 < 8`). `b = 4` has `3b = 12 > 11`, so the
band `3b` gives only LEVEL 4 (`H² ∣ β_4³`, forcing `β_4 = μy³(y−x)`), which is
**not** a kill: the charged `CAL_K5_B4` kill of `b = 4` is **not** reproduced by
MASTER (`small_k.out` F3). Stated as a gap, not glossed.

### 8.5 Instrument agreement

Every identity of §3 was checked on seven independent random instances
(`ID6`, `E-CUBIC`, `JfE`, `YDEG`); `ALL_A_OK`. The `y`-degree ledger
(`deg_yα = 2deg_yβ − K`, `deg_yρ ≤ K−1`, `deg_y E = max(3deg_yβ, deg_yρ+2K)`)
matches prediction in 4/4 instances (`controls.out` D2).

---

## 9. Dependency chain, stated honestly

```text
  Moh p.207-209  ->  ray R_4 data, Jacobian column X^4, deg_y B2 < deg h   [charged, primary]
  17(vvvvv) §2.3 ->  deg_y beta <= K-1, lf(f)=H^2, lf(g)=H^3               [charged, PROVED]
  17(vvvvv) §3.2 ->  beta in k => h | J => dead                            [charged, PROVED, deg beta = 0 only]
  LEMMA BF + LEMMA INJ                                                     [re-proved, 196/196 machine]
  E-CUBIC + JfE + LEMMA YDEG (deg_y E <= 3K-1, sharp)                      [PROVED HERE, 7/7 machine]
  BAND LEMMA                                                              [PROVED HERE]
     |
     +-- MASTER: deg(g^2-f^3-lambda f) = K+6, deg E <= 2K                  [PROVED HERE, K >= 7]
             |
             +-- LEVEL 2  H | beta_b^2            = 17(vvvvv) §4.2 TOP-BAND      [re-proved, 1 line]
             +-- LEVEL 3  deg rho <= 3b-2K        = 17(yyyyy) §3.2 rho-DEGREE    [re-proved, 1 line]
             +-- 17(yyyyy) §3.3 one-liner (reconstructed §2) applied to LEVEL 3 => 3b >= 2K+1
             +-- LEVEL 4  H^2 | beta_b^3, rho_{3b-2K} = beta_b^3/(3H^2)          [NEW; needs 3b > 2K]
             |     `-- numerical shadow  3 deg beta >= 2K+1                      [reproduced, NOT independent
             |                                                                    => SATURATION]
             +-- LEVEL 4' rho not in k[x];  3 deg_y beta >= 2K+1;  deg_y rho <= K-3   [NEW]
             +-- Theta explicit, unique                                          [NEW, K = 7..14 machine]
     |
     X   LEVEL c >= 5  (H^(c-1) | beta_b^c)                                      [OPEN -- the gap]
```

**Where it stops.** MASTER kills every band of `g²−f³` above degree `2K`. The
bands it kills that are *expressible in leading forms alone* are `2b+2K`
(level 2), `d+2K` (level 3) and `3b` (level 4). The next such band is `4b−2K`,
where `α²` and `βρ` first enter, with leading-form part
`(9/4)A² − 9PR = −(3/4)P⁴/H²`; but it is separated from `3b` by `2K−b` bands
carrying the sub-leading forms `β_{b−1}, h_{K−1}, ρ_{3b−2K−1}, …`, which absorb
it. Concretely the band at `3b−1` reduces to the single condition
`H ∣ A·β_{b−1} − (2/3)·(P³/H²)·h_{K−1}`, which two free forms satisfy.
**That is exactly why the ladder saturates.**

---

## 10. What was not done, and why

* **No Gröbner chart was submitted.** The lane instruction was to bypass the
  17(yyyyy) wall by derivation; every result above is exact CAS *checking* of
  closed-form identities (sympy over **Q**, foreground, all runs < 5 min).
  `guided_gb`, `gen_certif.py`, `gen_lemmas.py`, `hint_control.py`,
  `gen_k4ray2.py` were read as charged context and not invoked.
* **LEVEL `c ≥ 5` not attempted by chart.** The pinned shapes of §7.2 make
  `K = 8, b = 6` and `K = 9, b = 7` a 1-scalar top band; testing them is a chart
  job, not a derivation job, and is raised as an OPEN rather than half-run.
* **`b = 2K−1` edge.** The step `4b−2K < 3b` still holds there, so nothing in
  §5 degrades, but the degenerate band spacing `2K−b = 1` of §9 was not analysed
  separately.
* **Second instrument.** Everything is sympy; there is no Singular port. All
  claims are identity checks with printed residuals, so a second engine adds
  confidence, not coverage.

---

## OPENS RAISED

**OPEN[K4RAY-TOWER-LEVEL5].** Is `H³ ∣ β_b⁴` (LEVEL 5 of the divisibility
ladder) a theorem? QUANTITY: the numerical shadow would be
`4·deg β >= 3K + 1`, which at `K = 8` gives `deg β >= 7 > 6` and kills the
measured wall row `(168,112)`. Blocker: the band `4b−2K` of `g²−f³` is separated
from `3b` by `2K − b >= 1` bands carrying free sub-leading forms.

**OPEN[K4RAY-TOWER-DEPTH].** The ladder `H^{c−1} ∣ β_b^c` closes every row at
depth `c = K`. QUANTITY: required depth `c >= K`, versus proved depth
`c <= 3`. Is there a uniform argument for all `c`, or is the ladder genuinely
finite?

**OPEN[K4RAY-THETA-OBSTRUCTION].** `Θ = y^K(y−x)²Θ₁` is explicit and unique, with
`v_y(Θ) = K` and `v_{y−x}(Θ) = 2` exactly (machine, `K = 4…14`). At `K <= 5` this
kills the low stratum outright, because there the degree-`(K+6)` band of
`g²−f³` is forced to be `−3ρ_{6−K}H²` and QUANTITY: `v_y(Θ) = K < 2K − 2` for
every `K >= 3`. For `K >= 7` the same band carries `β³` and sub-leading `ρ`
terms, so the forcing is lost. Can the `v_y(Θ) = K` obstruction be transported to
`K >= 7`? QUANTITY: `deg E <= 2K` leaves `K − 6 >= 1` further form-level band
conditions between `K+7` and `2K` for every `K >= 7`, none of them exploited
here.

**OPEN[K4RAY-PINNED-CHART].** With `β_b = μ y^{K−3}(y−x)` forced at
`(K,b) = (8,6)` and `(9,7)`, the chart parameter count drops. QUANTITY: top-band
unknowns drop from `b + 1 = 7` and `8` to `1`; total chart parameters
`63 -> <= 57` and `80 -> <= 73`. Both are still `>= 55`, i.e. still inside the
MEASURED wall band, so this is a cut worth trying and not a predicted win.

**OPEN[K4RAY-COMPOSITE-SCOPE].** The charged composite arm covers `deg β = 0`
only. QUANTITY: the lane brief assumed coverage of `deg β < K`, a gap of
`K − 1 >= 6` degrees at the census rows. Is there a composite-type kill for
`1 <= deg β <= K−1`, or must that range go through the ladder?

---

## Artifacts

`box/k4raytower-20260903/` — `artifacts.sha256` covers 16 files.

```text
tower_ident.py / .out       A.  ID6, E-CUBIC, JfE, LEMMA YDEG on 7 instances     ALL_A_OK
eband_top.py / .out         A2. [E]_{2b+2K} = -3 [rho]_{2b} H^2 on 4 instances     MARK_A2_ALL 0
theta_solve.py / .out       B.  J(H,Theta) = c x^4 H^2 solved, K = 7..14; K=1 positive control
struct_checks.py / .out     C.  LEMMA INJ 196/196; band-lemma escapes; mod-3 obstruction;
                                residual stratum K = 4..14; ladder depth table
controls.py / .out          D.  composite arm; y-degree ledger; FALLACY-v2 exclusion check
small_k.py / .out            F.  v_y(Theta)=K, v_(y-x)(Theta)=2 for K=4..14; K=4,5 controls
manifest.sha256 / .check.log    stale, from an earlier attempt (/tmp/jc2-lane.iifzhb); digests agree
```

## Reproduction

```bash
python3 -u box/k4raytower-20260903/tower_ident.py     # ~5 min, exact over Q
python3 -u box/k4raytower-20260903/eband_top.py       # ~2 min
python3 -u box/k4raytower-20260903/theta_solve.py     # ~1 min
python3 -u box/k4raytower-20260903/struct_checks.py   # ~1 min
python3 -u box/k4raytower-20260903/controls.py        # ~2 min
python3 -u box/k4raytower-20260903/small_k.py         # ~3 min
```

Grep the markers, do not trust exit status: `MARK_ID6_`, `MARK_ECUBIC_`,
`MARK_JfE_`, `MARK_YDEGE_`, `ALL_A_OK`, `MARK_THETA_*`, `MARK_PC_TERMINAL`,
`MARK_C1_INJ`, `MARK_E_SOLVES`, `MARK_E_ALL`, `MARK_A2_ALL`.

<!-- BODY-END -->
