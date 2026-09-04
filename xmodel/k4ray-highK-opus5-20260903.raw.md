# The UNSPLIT-CONFIGURATION LEMMA at K = 7, 8, 9 on the full stratum — PARTIAL

Lane `k4rayhighk-20260903`; adapter opus5. Drivers, scripts and logs:
`box/k4rayhighk-20260903/`.

## 0. Provenance and verdict up front

**Input verification.** The manifest was generated mechanically from
`xmodel/k4ray-highK-opus5-20260903.run.v2` with `awk` on the paired
`charged_input_<i>_basename=` / `charged_input_<i>_sha256=` lines and checked
with `sha256sum -c`: **13/13 OK**, no digit retyped
(`box/k4rayhighk-20260903/inputs.sha256`).

**VERDICT: PARTIAL — the full stratum `deg β ≤ 2K−1` is NOT decided at
K = 7, 8, 9.** Typed exactly:

| item | status |
|---|---|
| (1) full-stratum system built at K = 7, 8, 9 | **NO for the monolithic chart** — the Jacobian itself does not fit: at `K = 7, Bdeg = 13` the expanded `J` has **2 564 984** terms and `coef(J,x*y)` did not return in 420 s (§2). Built and solved **stratum by stratum** instead (§4). |
| (2) `guided_gb` verdict, full stratum `deg β ≤ 2K−1` | `INCONCLUSIVE_TIMEOUT` at all three rows. Deepest exact-`Q` stage reached: `deg β ≤ 5` at K = 7, `deg β ≤ 5` at K = 8, `deg β ≤ 6` at K = 9 (§5 for the exact table). |
| (3) case (A) / D = 108 / the `δ₁'=0` row dead | **NO.** None of the three rows is closed. The chain in §7 is written but its hypothesis is not discharged. |
| (4) `K`-uniform killing combination | **A `K`-uniform kill is PROVED, but for a sub-stratum, not for the row.** New theorem, uniform in `K ≥ 7`: `β ∉ k ⇒ 3·deg β ≥ 2K+1` (§3.3). This strictly sharpens the charged TOP-BAND bound `2 deg β ≥ K+1` and it is the first `K`-uniform *kill* on the nonconstant arm. It does not by itself close any row. |
| (5) controls | 4 of 5 as specified; **one control is vacuous for a theorem-level reason** and is reported as such, one **did not fail as designed** and is reported as such (§6). |

**The one sentence a reader should carry away:** the nonconstant arm now has a
`K`-uniform *kill* — every `k = 4` ray pair with `β ∉ k` must have
`3 deg β ≥ 2K+1`, so the whole low-degree part of the stratum dies for all
`K ≥ 7` at once — and the census rows are closed by exact-`Q` computation only
up to `deg β ≤ 5, 5, 6` out of the required `13, 15, 17`; the residual is a
compute wall at ≈ 55 chart parameters, measured, not conjectured.

**FALLACY-v2 posture.** No exit claim is made, so no `charge_basis` line is
emitted. *Floor/attainment:* every `UNIT_IDEAL_CHAR0` below is an exact-`Q`
attainment statement (`reduce(1,G)=0` in a characteristic-zero standard basis),
never a floor; every `INCONCLUSIVE_TIMEOUT` is reported as a timeout and is
**not** read as a kill. *Carrier/attainment:* a stratum verdict carries only
`deg β ≤ b`; reading `deg β ≤ 5` at K = 7 as "the (21,14) row is dead" is exactly
the error this file refuses to make. *No modular promotion:* the `MODULAR_ONLY`
rows in §5 are evidence about `F_32003` and nothing else — our ideals are the
dehomogenised (inhomogeneous) localisations, so the homogeneous-properness scope
does **not** apply to them. *`sat()`* was not used.

---

## 1. Instrument

### 1.1 The chart

`box/k4rayhighk-20260903/gen_hk.py` emits, for `(K, Bdeg, char, tk)`, the
charged ray-`R_4` tower chart in the charged normalisation
(`x = γ`, `y = π`, `H := y^{K−1}(y−x)`):

```text
unknowns  h_ij  (i+j ≤ K−1),   B_ij  (j ≤ K−1, i+j ≤ Bdeg)
h  = H + Σ h_ij x^i y^j                 (monic in y, deg_y h = K, lf h = H)
B  = Σ B_ij x^i y^j  = 2β               (deg_y B < K  — PROVED, charged §2.3)
Al = quo_y(B², h) = 4α ,  Rh = B² − Al·h = 4ρ
f  = h² + B ,   g = h³ + (3/2)Bh + (3/8)Al
J  = f_x g_y − f_y g_x
ROWS = every coefficient of J in k[x,y] except the x^tk one ;  CSTP = the x^tk one
```

This is the charged `gen_k4ray3.py` chart with one extra, *justified*, slice: the
translation `y ↦ y + ν` (ν ∈ k) fixes `x`, fixes `J`, preserves monicity and
preserves `lf(h) = H`, and changes the `y^{K−1}`-coefficient `c_{K−1}(x)` of `h`
by `Kν`. Since `deg c_{K−1} ≤ 1` with leading part `−x`, choosing
`ν = −c_{K−1}(0)/K` gives `c_{K−1} = −x` exactly, i.e. `h_{0,K−1} = 0`. The chart
therefore drops one parameter and remains a **complete slice**. At `K = 4, Bdeg = 3`
this gives 19 parameters against the charged 20, 39 rows against the charged 39,
`deg CSTP = 14 = 5K−6`, `homog(ROWS) = homog(CSTP) = 1` — i.e. the charged
grading `w(h_ij) = K−i−j`, `w(B_ij) = 2K−i−j` is reproduced independently.

### 1.2 The kill test: dehomogenise, do not Rabinowitsch

`ROWS` is weighted-homogeneous in **strictly positive** weights and `CSTP` is
`w`-homogeneous of weight `5K−6 > 0`; `V(ROWS)` is a weighted cone containing the
origin, so `dim ≥ 0` always and "`dim = −1`" is never the test. The charged lane
used `CSTP^N ∈ ROWS`, which needs `std(ROWS)` over `Q` — the expensive object.
The test used here is the **dehomogenisation**

```text
V(ROWS) ∩ {CSTP ≠ 0} = ∅   ⟺   1 ∈ ( ROWS , CSTP − 1 )   over an algebraically closed field
```

(the `⇐` is trivial; for `⇒`, if `p ∈ V(ROWS)` has `CSTP(p) = γ ≠ 0` then the
weighted action `t·p` has `CSTP = t^{5K−6}γ`, and `t^{5K−6} = γ^{−1}` is solvable
over `k̄` because `5K−6 > 0`). Over `Q`, `reduce(1, std(ROWS, CSTP−1)) = 0` is an
exact characteristic-zero unit certificate; `guided_gb` types it
`UNIT_IDEAL_CHAR0` through `PromotionPolicy.exact_q`, with no modular step and no
extra Rabinowitsch variable.

**Measured cost of the change** (same machine, same `Q`, same chart):

| chart | charged route `std(ROWS)` then `CSTP^N ∈ ROWS` | this route `std(ROWS, CSTP−1)` |
|---|---|---|
| K = 4, Bdeg = 3 | `std` size 75, `dim` 10, `CSTP ∈ ROWS` (`N = 1`), `lift` verified, 12 nonzero cofactors | **unit ideal, 0.04 s** |
| K = 5, Bdeg = 4 | charged: `N = 2`, ≈ 30 s+ | **unit ideal, 0.17 s** |

Both routes agree at `K = 4, 5` — two-instrument agreement for the *kill test*,
though not for the chart (§6.5). The `K = 4` cofactor identity `CSTP = Σ q_i ROWS_i` was recomputed and
`lift`-verified in this lane (`runs/cert_K4_B3.out`,
`CERT__LIFT_VERIFY 1 1 support 12`), so `MEASURED[K4RAY-K4-EMPTY]` is replayed
independently on the reduced slice.

### 1.3 What `guided_gb` supplied

Every Singular job below is `box/lib/guided_gb.py` `guided_groebner` under
`stdbuf -oL -eL`, with its full marker battery: `GG__NF_ZERO` for **every**
submitted generator, `GG__UNIT`, `GG__DIM`, `GG__BASIS_SIZE`, `GG__LEAD_DIM`,
`GG__LEAD_VDIM`, `GG__ACCEPT`, per-run `.guided.json` with command, hashes and
timings, and an aggregate `guided_gb_result.json` carrying the promotion policy
text. No verdict below was read from an exit status; all were read from markers.
Row counts come from a separate prelude-only pass, so the generator list handed
to the helper is explicit (`runs/*.rowcount.json`).

---

## 2. Why the monolithic full-stratum chart is out of reach — measured

`Bdeg = 2K−1` gives parameter counts `h : K(K+1)/2 − 1`, `B : 2K² − K(K−1)/2`:

```text
K = 7   27 + 77 = 104 parameters      K = 8   35 + 100 = 135      K = 9   44 + 126 = 170
```

Four formation probes, `Singular 4.3.2`, 420 s each
(`runs/probe_*_K7_*.{sing,out}`, `runs/probe.status`):

| chart | K | Bdeg | outcome |
|---|---|---|---|
| direct | 7 | 6 | `deg J = 19`, `size J = 106 343`, **150 rows, 55 params**, formed |
| direct | 7 | 13 | `deg J = 33`, **`size J = 2 564 984`**, `coef(J,x*y)` **did not return in 420 s** (`EXIT 124`) |
| quad (α, ρ as their own unknowns; every generator quadratic) | 7 | 6 | 241 rows, 146 params, formed |
| quad | 7 | 13 | 605 rows, **377 params**, formed |

Rebuilding `J` through the charged identity ID6
(`J = 3[J(β,α) − J(h,ρ)] = (3/8)J(B,Al) − (3/4)J(h,Rh)`; re-verified here, §3.1)
avoids expanding `h³` but produces the **same** polynomial: at `K = 4, Bdeg = 5`
both routes print `deg J = 14`, `size J = 5645`, 67 rows, `deg CSTP = 14`; at
`K = 7, Bdeg = 13` the ID6 route also reaches `size J = 2 564 984` and stalls in
`coef`. So the obstruction is the size of `J` itself, not the way it is built.
The `quad` route trades degree for 377 unknowns, which is worse for `std`.

> **MEASURED[K4RAY-HIGHK-MONOLITH-DEAD].** At `K = 7` and `Bdeg = 2K−1 = 13` the
> Jacobian of the ray-tower chart has 2 564 984 terms and its `k[x,y]`-coefficient
> extraction does not complete in 420 s. A single Gröbner attempt on the full
> stratum at `K = 7, 8, 9` is not a plan; it is not even a formable ideal.

This is why everything below is stratified by `b := deg β`.

---

## 3. New structure: an injectivity lemma, a ρ-degree lemma, and a K-uniform kill

Notation as in §1.1: `H = y^{K−1}(y−x)`, `b = deg β`, `β_b` its leading form,
`ρ = β² − αh` with `deg_y ρ ≤ K−1`, `ρ_d` its leading form, `d = deg ρ`.

### 3.1 Re-verification of the charged identities on this instrument

`box/k4rayhighk-20260903/lemmas.{sing,out}`, all markers grepped, not trusted by
exit status:

```text
V1_ID6            K=4 b=5 / K=5 b=6 / K=7 b=9 / K=7 b=13 / K=9 b=11   resid 0   (all five)
V4_DEGS           deg α = 2b−K and deg ρ = 2b in every generic instance
                  (e.g. K=7 b=13: deg β 13, deg α 19, deg ρ 26, deg J 31)
V4_DEGY           deg_y ρ = K−1 in every instance
V4_TOPBAND        [J]_{K+d−2} + 3·J(H, ρ_d) = 0   resid 0   (all five)
V7_COMPOSITE      β ∈ k ⇒ α = 0, J = 0, g = h³+3βh   (K = 4,5,7,9)
```

`V4_DEGS` matters twice: it confirms the filtered-division bounds
`deg α ≤ 2b−K`, `deg ρ ≤ 2b` that §3.2 uses, and it shows that **the conclusion
of §3.2 is a real restriction** — a generic `(h, β)` has `deg ρ = 2b`, not
`3b−2K`.

### 3.2 The two lemmas

> **LEMMA INJ.** Let `K ≥ 2`, `H = y^{K−1}(y−x)`, and let `R` be a binary form
> with `deg_y R ≤ K−1` and `deg R = e ≥ 1`. If `J(H,R) = 0` then `R = 0`.

*Proof.* `J(H,R) = 0` for binary forms forces `R^K = λH^e` with `λ ≠ 0` (or
`R = 0`). `H = y^{K−1}(y−x)` has exponent gcd `gcd(K−1,1) = 1`, so it is not a
proper power; `R^K = λH^e` then forces `K ∣ e` and
`R = λ' y^{e(K−1)/K}(y−x)^{e/K}`, whose `y`-degree is `e ≥ K`, contradicting
`deg_y R ≤ K−1`. ∎

*Machine check.* `V3_INJ` runs the linear system "coefficients of `J(H,R)` = 0"
for `K = 4,5,6,7,8,9` and **every** `e = 1 … 4K` (156 instances) and verifies that
the only solution is the trivial one: `only_trivial 1` in **156 of 156** cases.
Sharpness: `C4_INJ_SHARP` prints `J(H,1) = 0`, so the hypothesis `e ≥ 1` cannot
be dropped.

> **LEMMA ρ-DEGREE (new, uniform in `K ≥ 7`).** Let `(h, β)` be a point of the
> ray-`R_4` tower chart with `J(f,g) = c·x⁴`, `c ≠ 0`. Then
> ```
>                 deg ρ  ≤  max( 0 , 3·deg β − 2K ).
> ```

*Proof.* Write `b = deg β`, `d = deg ρ`, and suppose `d ≥ 1` and `d > 3b−2K`.
By ID6, `J = 3[J(β,α) − J(h,ρ)]`. Filtered division by the `y`-monic `h` of total
degree `K` gives `deg α ≤ 2b−K` (`V4_DEGS`), hence
`deg J(β,α) ≤ b + (2b−K) − 2 = 3b−K−2`. The top band of `J(h,ρ)` sits in degree
`K+d−2` and equals `J(H, ρ_d)`. Since `d > 3b−2K` we have `K+d−2 > 3b−K−2`, so
```
                [J]_{K+d−2}  =  −3·J(H, ρ_d).
```
`d ≥ 1` and `K ≥ 7` give `K+d−2 ≥ 6 > 4`, so this band of `J = c·x⁴` vanishes:
`J(H,ρ_d) = 0`. But `ρ_d` is a form of degree `d ≥ 1` with `deg_y ρ_d ≤ K−1`, so
LEMMA INJ gives `ρ_d = 0` — contradicting `d = deg ρ`. Hence `d ≤ 0` or
`d ≤ 3b−2K`. ∎

The band identity used is exactly the machine-checked `V4_TOPBAND`.

### 3.3 The K-uniform kill

> **THEOREM (uniform in `K ≥ 7`).** For a ray-`R_4` tower pair with
> `J(f,g) = c·x⁴`, `c ≠ 0`, and `β ∉ k`,
> ```
>                       3·deg β  ≥  2K + 1 .
> ```
> Equivalently the whole stratum `deg β ≤ ⌊2K/3⌋` is **dead**, for every `K ≥ 7`.

*Proof.* Suppose `3b ≤ 2K`. LEMMA ρ-DEGREE gives `deg ρ ≤ 0`, i.e. `ρ ∈ k`, so
`J(h,ρ) = 0` and `J = 3J(β,α)`. Since `deg ρ < 2b` we get `β_b² = α_{2b−K}·H`
from the top band of `β² = αh + ρ`; write `P := β_b`, `A := α_{2b−K}`, so
`P² = AH` and `A ≠ 0`. The top band of `J` is `3J(P,A)`, in degree `3b−K−2`.

*Case `3b ≠ K+6`.* Then `3b−K−2 ≠ 4` and the band vanishes: `J(P,A) = 0`.
From `A = P²/H`, `J(P,A) = −(P²/H²)·J(P,H)`, so `J(H,P) = 0`; `P` is a form of
degree `b ≥ 1` with `deg_y P ≤ deg_y β ≤ K−1`, so LEMMA INJ gives `P = 0`,
contradicting `b = deg β`. (`V5_COFACTOR` verifies the cofactor identity
`H·J(P,A) = A·J(H,P)`; its printout also records that a *generic* `β` does **not**
satisfy `P² = AH`, i.e. the hypothesis is the charged TOP-BAND lemma and is not
automatic.)

*Case `3b = K+6`.* The charged TOP-BAND lemma gives `y^{⌈(K−1)/2⌉}(y−x) ∣ β_b`,
hence `b ≥ ⌈(K−1)/2⌉ + 1`. Together with `b = (K+6)/3` this forces `K ≤ 9`, and
`3 ∣ K+6` then leaves only `K = 9`, `b = 5`. There `deg β_5 = 5 = deg y⁴(y−x)`,
so `β_5 = μ y⁴(y−x)` with `μ ≠ 0`, `A = μ²(y−x)`, and
`[J]_4 = 3J(β_5, A) = 12 μ³ y³(y−x)`, which is not of the form `c·x⁴` unless
`μ = 0`. Contradiction. (`V6_K9B5`: `P²−AH = 0`, `J(P,A) = 4μ³y³(y−x)`,
`resid 0`.) ∎

This is strictly stronger than the charged TOP-BAND consequence `2b ≥ K+1`:
`(2K+1)/3 > (K+1)/2` for every `K ≥ 2`. At the three census rows:

```text
K = 7   charged  b ≥ 4      new  b ≥ 5
K = 8   charged  b ≥ 5      new  b ≥ 6
K = 9   charged  b ≥ 5      new  b ≥ 7
```

### 3.4 Why the ρ-cut is a legitimate chart cut

For the `b`-th stratified run we append to `ROWS` the coefficients of
`ρ − jet(ρ, max(0, 3b−2K))`, i.e. we force `deg ρ ≤ max(0, 3b−2K)`. This is sound
on the *whole* sub-stratum `deg β ≤ b`, not merely on `deg β = b`:

* if `β ∈ k` then `α = 0` and `ρ = β²` is constant (`V7_COMPOSITE`), so the added
  generators vanish;
* if `β ∉ k` with `deg β = b' ≤ b`, LEMMA ρ-DEGREE gives
  `deg ρ ≤ max(0, 3b'−2K) ≤ max(0, 3b−2K)`, so the added generators vanish.

Hence `1 ∈ (ROWS_b , RCUT_b , CSTP−1)` proves exactly

> no point of the ray-`R_4` tower chart with `deg β ≤ b` has `J = c·x⁴` with
> `c ≠ 0`,

which is the stratum statement quoted in §5. The runs are therefore **cumulative**:
the largest `b` reaching `UNIT_IDEAL_CHAR0` is the closed sub-stratum.

---

## 4. The stratified run: instrument settings

For each `(K, b)` the submitted system is

```text
generators = ROWS(K, Bdeg=b)          all coefficients of J except the x^4 one
           + RCUT(K, b)               coefficients of  rho - jet(rho, max(0,3b-2K))   [§3.4]
           + (CSTP - 1)               the dehomogenised target                        [§1.2]
policy     = PromotionPolicy.exact_q  ;  characteristic 0  ;  one core per job
verdict    = guided_gb                UNIT_IDEAL_CHAR0 / DIM0_CHAR0 / POSDIM / INCONCLUSIVE_TIMEOUT
```

Every generator is named individually and gets its own `GG__NF_ZERO` marker, so
a `UNIT_IDEAL_CHAR0` carries `NF(g_i,G) = 0` for all `g_i` **and**
`reduce(1,G) = 0`, both in characteristic zero.

A variant run (`TB_K7_B6`) additionally appends the charged TOP-BAND lemma in
its linear form — `B_ij = 0` for `i+j = b`, `j < ⌈(K−1)/2⌉`, together with
`Σ_{i+j=b} B_ij = 0` — which is legitimate on the *exact* stratum `deg β = b`
once the lower strata are dead. It did not change the outcome (§5).

---

## 5. Results

All rows exact over `Q` unless the characteristic column says otherwise. `cut`
is `max(0, 3b−2K)`; `params` is the number of chart unknowns; times are the
Singular wall time reported by `guided_gb`.

### 5.1 Calibration and replay

| tag | K | Bdeg | rows | params | verdict | s |
|---|---|---|---|---|---|---|
| `PC_K1_B1_x1` (positive control, target `x¹`) | 1 | 1 | 1 | 2 | **`DIM0_CHAR0`, unit = false — SURVIVES** | 0.02 |
| `CAL_K4_B3` (charged `MEASURED[K4RAY-K4-EMPTY]`) | 4 | 3 | 39 | 19 | `UNIT_IDEAL_CHAR0` | 0.04 |
| `CAL_K5_B4` (charged `MEASURED[K4RAY-K5-EMPTY]`) | 5 | 4 | 68 | 29 | `UNIT_IDEAL_CHAR0` | 0.17 |
| `cert_K4_B3` (homogeneous route, `CSTP^N ∈ ROWS`) | 4 | 3 | 39 | 19 | `std` size 75, `dim` 10, **`N = 1`**, `lift` verified, 12 cofactors | <1 (`CERT__STD_SECONDS 0`) |
| `CAL_K5_B9` (K = 5 **full** stratum `2K−1`, no cut) | 5 | 9 | 158 | 54 | `INCONCLUSIVE_TIMEOUT` | 1200 |
| `PC_K2_B1_x{1,2,3,4}` | 2 | 1 | 4–5 | 5 | `UNIT_IDEAL_CHAR0` (all four targets) | 0.02 |

The two charged kills are replayed on the reduced slice, by both routes, and they
agree. `CAL_K5_B9` shows that even at `K = 5` the *full* stratum `deg β ≤ 2K−1`
is already past the wall — the charged lane's `deg β ≤ K−1` scope was not an
oversight, it is where the computation stops.

### 5.2 The census rows, stratified by `b = deg β`

**K = 7**  (census target `deg β ≤ 13`; THEOREM §3.3 covers `b ≤ 4`)

| b | ρ-cut | rows | params | verdict | s |
|---|---|---|---|---|---|
| 1 | 0 | 35 | 30 | **UNIT_IDEAL_CHAR0** | 1.4 |
| 2 | 0 | 63 | 33 | **UNIT_IDEAL_CHAR0** | 1.5 |
| 3 | 0 | 99 | 37 | **UNIT_IDEAL_CHAR0** | 1.6 |
| 4 | 0 | 136 | 42 | **UNIT_IDEAL_CHAR0** | 2.0 |
| 5 | 1 | 174 | 48 | **UNIT_IDEAL_CHAR0** | 9.8 |
| 6 | 4 | 212 | 55 | INCONCLUSIVE_TIMEOUT | 420.1 |
| 7 | 7 | 244 | 62 | INCONCLUSIVE_TIMEOUT | 420.2 |

**K = 8**  (census target `deg β ≤ 15`; THEOREM §3.3 covers `b ≤ 5`)

| b | ρ-cut | rows | params | verdict | s |
|---|---|---|---|---|---|
| 1 | 0 | 43 | 38 | **UNIT_IDEAL_CHAR0** | 4.5 |
| 2 | 0 | 73 | 41 | **UNIT_IDEAL_CHAR0** | 5.7 |
| 3 | 0 | 111 | 45 | **UNIT_IDEAL_CHAR0** | 6.1 |
| 4 | 0 | 154 | 50 | **UNIT_IDEAL_CHAR0** | 6.9 |
| 5 | 0 | 198 | 56 | **UNIT_IDEAL_CHAR0** | 8.8 |
| 6 | 2 | 242 | 63 | INCONCLUSIVE_TIMEOUT | 450.1 |
| 7 | 5 | 286 | 71 | INCONCLUSIVE_TIMEOUT | 450.2 |

**K = 9**  (census target `deg β ≤ 17`; THEOREM §3.3 covers `b ≤ 6`)

| b | ρ-cut | rows | params | verdict | s |
|---|---|---|---|---|---|
| 1 | 0 | 52 | 47 | **UNIT_IDEAL_CHAR0** | 15.7 |
| 2 | 0 | 84 | 50 | **UNIT_IDEAL_CHAR0** | 16.1 |
| 3 | 0 | 124 | 54 | **UNIT_IDEAL_CHAR0** | 17.2 |
| 4 | 0 | 172 | 59 | **UNIT_IDEAL_CHAR0** | 18.7 |
| 5 | 0 | 221 | 65 | **UNIT_IDEAL_CHAR0** | 28.9 |
| 6 | 0 | 271 | 72 | **UNIT_IDEAL_CHAR0** | 49.1 |
| 7 | 3 | 321 | 80 | INCONCLUSIVE_TIMEOUT | 450.2 |

**K = 10**  (census target `deg β ≤ 19`; THEOREM §3.3 covers `b ≤ 6`)  *(beyond the census — a K-uniformity check of the theorem)*

| b | ρ-cut | rows | params | verdict | s |
|---|---|---|---|---|---|
| 6 | 0 | 299 | 82 | **UNIT_IDEAL_CHAR0** | 242.5 |

### 5.3 What §5.2 does and does not establish

**Closed, exactly over `Q`:**

```text
K = 7   (147,98) = the delta_1'=0 two-point row      deg beta <= 5   of the required 13
K = 8   (168,112) = the D = 108 no-split datum       deg beta <= 5   of the required 15
K = 9   (189,126) = (99,66) case (A)                 deg beta <= 6   of the required 17
```

Every stratum with `cut = 0` — i.e. exactly the range `3b ≤ 2K` that the
`K`-uniform THEOREM of §3.3 covers — closes in **seconds**, at up to 72 chart
parameters, and closes at all three rows. This is an independent exact-`Q`
confirmation of the theorem: the machine kills, one stratum at a time, the range
the theorem kills in one line. The one stratum closed **beyond** the theorem is
`K = 7, b = 5` (`3b = 15 > 14 = 2K`, `cut = 1`, 48 params, 9.8 s).

**The wall.** The first stratum at each row whose `ρ`-cut is genuinely positive
and whose parameter count exceeds ≈ 55 does not finish. It does not finish over
`Q` at 420 s, 900 s or **2400 s**, it does not finish with the charged TOP-BAND
lemma appended in its linear form, it does not finish under `slimgb`, and **it
does not finish modulo 32003 either**:

| tag | K | b | params | route | s | verdict |
|---|---|---|---|---|---|---|
| `SCUT_K7_B6` | 7 | 6 | 55 | exact `Q`, `ρ`-cut | 420 | `INCONCLUSIVE_TIMEOUT` |
| `MAIN_K7_B6` | 7 | 6 | 55 | exact `Q`, **no** `ρ`-cut | 900 | `INCONCLUSIVE_TIMEOUT` |
| `LONG_K7_B6` | 7 | 6 | 55 | exact `Q`, `ρ`-cut | **2400** | `INCONCLUSIVE_TIMEOUT` |
| `TB_K7_B6` | 7 | 6 | 55 | exact `Q`, `ρ`-cut + TOP-BAND cut | 360 | `INCONCLUSIVE_TIMEOUT` |
| `slim_K7_B6` | 7 | 6 | 55 | exact `Q`, `ρ`+TOP-BAND cut, **`slimgb`** | 900 | no `SG__SECONDS` marker |
| `slim_K7_B6` (stored artifact re-run) | 7 | 6 | 55 | same, `slimgb` | 300 | `TIMEOUT_RC=124` |
| `MOD_K7_B6` | 7 | 6 | 55 | **`F_32003`**, `ρ`-cut | 360 | `INCONCLUSIVE_TIMEOUT` |
| `MOD_K7_B7` | 7 | 7 | 62 | **`F_32003`**, `ρ`-cut | 360 | `INCONCLUSIVE_TIMEOUT` |
| `SCUT_K9_B7` | 9 | 7 | 80 | exact `Q`, `ρ`-cut | 450 | `INCONCLUSIVE_TIMEOUT` |

The modular timeouts are the informative ones: the obstruction is the
**combinatorics of the standard basis**, not coefficient growth in `Q`. A
good-prime / CRT strategy therefore does not open this door, and `guided_gb`'s
CRT machinery has nothing to lift. Neither does a sixfold increase in wall time
(420 s → 2400 s at `K = 7, b = 6`), nor a different Buchberger variant. This is
a measurement of *these* runs, not a theorem about what some other engine could do.

The contrast that pins the wall down is between equal parameter counts on
opposite sides of the `ρ`-cut:

```text
K = 10, b = 6   82 params   rho-cut 0   UNIT_IDEAL_CHAR0   242 s
K =  9, b = 7   80 params   rho-cut 3   INCONCLUSIVE       > 450 s
K =  9, b = 6   72 params   rho-cut 0   UNIT_IDEAL_CHAR0    49 s
K =  8, b = 6   63 params   rho-cut 2   INCONCLUSIVE       > 450 s
```

> **MEASURED[K4RAY-HIGHK-WALL].** On the ray-`R_4` tower chart with the
> dehomogenised kill test, the exact-`Q` standard basis completes at up to **82**
> chart parameters when the `ρ`-cut is `0` (`K = 10, b = 6`, 242 s), and fails to
> complete at **55–80** parameters whenever the `ρ`-cut is positive — at 360 s,
> 420 s, 450 s, 900 s and 2400 s, under `std` and under `slimgb`, over `Q` and
> over `F_32003`. The regime change tracks the cut, not the parameter count.

`K = 10, b = 6` is not a census row; it was run only to check that the THEOREM
of §3.3 keeps closing its stratum past `K = 9`, and it does.

---

## 6. Controls

### 6.1 Positive control — a survivor must survive

`PC_K1_B1_x1`: the same code path at `K = 1`, `Bdeg = 1`, target `x¹`, returns
`DIM0_CHAR0` with `unit = false`, `dim = 0` — a **nonempty** solution set. The
banked witness is `f = y²+x`, `g = y³+(3/2)xy`, `J = (3/2)x`, re-evaluated here
(`C1_SURVIVOR J 3/2x`). So the pipeline is not a machine that returns "empty" on
everything. The `K = 2` scan `PC_K2_B1_x{1..4}` returns `UNIT_IDEAL_CHAR0` for
all four targets, i.e. no two-point survivor at `K = 2, Bdeg = 1`; that is a
result, not a control failure.

### 6.2 Composite arm — survives *as composite*, not as a counterexample

`C2_COMPOSITE_K7` runs `β ∈ k` inside the `K = 7` chart: `α = 0`, `J = 0`
identically, `g = h³+3βh`. `V7_COMPOSITE` repeats it at `K = 4, 5, 7, 9`. So the
composite locus is a genuine solution locus of the tower equations and is killed
only by `c ≠ 0` — exactly the charged LEMMA B2-CONST, reproduced independently.
It is **not** a Keller counterexample: `J ≡ 0`. This is also why the `ρ`-cut of
§3.4 is sound at `β ∈ k` (there `ρ = β²` is constant).

### 6.3 Tame two-point automorphism — the control as specified is VACUOUS

The charged control asks for "a tame two-point automorphism of degrees
`(3K, 2K)`" to survive. No such object exists, for two independent reasons:

1. By Jung–van der Kulk, for any polynomial automorphism `(F,G)` of `A²`,
   `deg F ∣ deg G` or `deg G ∣ deg F`. For `K ≥ 1`, `2K ∤ 3K` and `3K ∤ 2K`, so
   **no automorphism has degrees `(3K, 2K)`**.
2. A coordinate polynomial of `A²` of degree `> 1` has leading form `c·L^d` for
   a **single** linear form `L` (Abhyankar–Moh / the same structure theorem).
   Both `2K` and `3K` exceed 1 for every `K ≥ 1`, so **no automorphism of these
   degrees has a two-point leading form at all** — "two-point automorphism of
   degrees `(3K,2K)`" is a contradiction in terms twice over.

Reported as vacuous rather than silently substituted. The substitute actually
run is §6.1 (a genuine two-point survivor of `J = c·x^k` at `K = 1`). Note this
cuts nothing for the campaign: a hypothetical Keller counterexample is *not*
assumed to be an automorphism, so the two-point ray is not excluded by
Jung–van der Kulk.

### 6.4 The `guided_gb` perturbed-series control DID NOT fail as designed

`HINT_K4_B3` ran the **homogeneous** `K = 4` chart through `guided_gb` with the
true Hilbert numerator

```text
GG__TARGET_HNUM main       1,0,-21,29,159,-566,546,558,-2037,2408,-1485,429,13,-42,8,0
GG__TARGET_HNUM perturbed  1,1,-21,29,159,-566,546,558,-2037,2408,-1485,429,13,-42,8,0
```

and `run_perturbed_control=True`. Result:

```text
main       NF_ALL_ZERO 1   BASIS_SIZE 75   DIM 10   LEAD_DIM 10   LEAD_VDIM NONTERMINATING
perturbed  NF_ALL_ZERO 1   BASIS_SIZE 75   DIM 10   LEAD_DIM 10   LEAD_VDIM NONTERMINATING
GG__PERTURBED_FAILED control 0
```

Singular recovered the **same, correct** standard basis from the deliberately
wrong numerator, so the negative control did not fire, `_controls_accepted`
rejected the run, and the aggregate verdict fell back to `POSDIM` (dimension 10,
which is the true dimension of the homogeneous chart cone). Diagnosis: the
helper's perturbed control discriminates through `predicted_length`
(`vdim` of the lead ideal), and a positive-dimensional cone has no such length —
with `predicted_length = None` the acceptance test degenerates to
`NF_ALL_ZERO`, which a wrong hint does not break. **The control is not
informative on positive-dimensional homogeneous charts**; it is informative on
the `dim = 0` fibres the helper was regression-tested against. Recorded, not
worked around.

`POSDIM` here is emphatically **not** a survivor claim: the same chart satisfies
`CSTP ∈ ROWS` with an exact `lift` certificate, so every point of that
10-dimensional cone has `CSTP = 0`. Reading `POSDIM` as "a component survived"
would be the FALLACY-v2 error; a component is a counterexample only once a point
is exhibited *and* checked against `J = c·x⁴`, `c ≠ 0`.

### 6.5 Instrument agreement

The two kill tests — charged `CSTP^N ∈ ROWS` (homogeneous, `lift`-verified) and
this lane's `1 ∈ (ROWS, CSTP−1)` (dehomogenised, exact `Q`) — agree at
`K = 4` and `K = 5`. Two independent constructions of `J` (`f_x g_y − f_y g_x`
and the ID6 route `(3/8)J(B,Al) − (3/4)J(h,Rh)`) produce byte-identical chart
statistics at `K = 4, Bdeg = 5` (`deg J = 14`, `size J = 5645`, 67 rows,
`deg CSTP = 14`). The chart itself is *not* cross-checked by a second, structurally
different chart; `OPEN[K4RAY-SECOND-INSTRUMENT]` from the charged report stands.

---

## 7. The dependency chain, and where it stops

What a complete proof of the UNSPLIT-CONFIGURATION LEMMA at `K = 7, 8, 9` would
give, written out so that the missing link is visible:

```text
UNSPLIT-CONFIGURATION LEMMA at K
    = [ B2 constant  => composite => dead ]        PROVED for all K   (charged LEMMA B2-CONST,
                                                    re-verified here as V7_COMPOSITE / C2)
   AND[ B2 nonconstant => inconsistent on deg beta <= 2K-1 ]   NOT PROVED at K = 7,8,9

  K = 9  =>  (99,66) case (A) dead
             =>  with (B) and (C) already banked, the (99,66) SKELETON verdict would be
                 complete for all three configurations modulo N1                 NOT OBTAINED
  K = 8  =>  D = 108 no-split arm dead  =>  D = 108 CLOSED at skeleton level     NOT OBTAINED
  K = 7  =>  the delta_1' = 0 two-point row (21,14) dead                         NOT OBTAINED
```

What today adds to the second line:

```text
THEOREM (§3.3), uniform in K >= 7:   beta not in k  ==>  3 deg beta >= 2K+1.
    => the sub-stratum deg beta <= floor(2K/3) of the nonconstant arm is DEAD for every K >= 7.
    => at the three census rows this kills deg beta <= 4, 5, 6 respectively, in one line,
       and the machine confirms it stratum by stratum in seconds (§5.2).
LEMMA rho-DEGREE (§3.2), uniform in K >= 7:   deg rho <= max(0, 3 deg beta - 2K).
    => a legitimate chart cut on every sub-stratum (§3.4), and the reason the cut-0 runs
       are cheap.
MACHINE (§5.2), exact over Q:   deg beta <= 5, 5, 6 at K = 7, 8, 9.
```

So the correct campaign position is unchanged in kind and improved in degree:
**the composite arm is closed for all `K`; the nonconstant arm now has a
`K`-uniform kill on an initial segment of the degree stratification, and the
census rows are closed on `deg β ≤ 5, 5, 6` out of `13, 15, 17`.** Case (A) of
`(99,66)` is **not** dead, `D = 108` is **not** closed, and the `δ₁' = 0` row is
**not** dead. Any statement to the contrary would be a carrier/attainment error:
a stratum verdict is `FULL_ACTUAL` only on its own stratum.

---

## 8. What was not done, and why

* **The full stratum was never formable at `K = 7, 8, 9`** (§2). The lane did not
  spend budget on a monolithic attempt after the 420 s formation probe failed;
  it spent it on the stratification and on the structure that makes the low
  strata cheap.
* **No modular result was promoted.** Both modular runs timed out, so there was
  nothing to promote; and our ideals are the inhomogeneous dehomogenisations, to
  which the helper's homogeneous-properness scope does not apply in any case.
* **The `K`-uniform *combination* of the charged ladder rows is still not
  exhibited.** §3.3 is a uniform kill obtained from the *top* band plus LEMMA
  INJ, not from a combination of the charged closed-form ladder rows
  `L1, L2, …`; `OPEN[K4RAY-UNIFORM-COMBINATION]` is untouched.
* **The `deg β ≤ K−1` question (`OPEN[K4RAY-BETA-DEG]`) was not decided.** §3.3
  gives a *lower* bound `3b ≥ 2K+1`; no upper bound on `b` was found, and the
  charged upper bound `b ≤ 2K−1` is still the only one. Note the two bounds are
  compatible for every `K ≥ 7`, so nothing here refutes `b ≤ K−1` either.
* **`OPEN[K4RAY-TOWER-INDUCTION]` was not touched.** Every chart here assumes the
  tower normalisation `a₂ = 0, a₁ = 3β, a₀ = (3/2)α`, whose forcing is proved
  only in the top band. All §5 verdicts are scoped by it.

---

## OPENS RAISED

**`OPEN[K4RAY-HIGHK-MIDSTRATUM]`** — close the strata
`⌈(2K+1)/3⌉ ≤ b ≤ 2K−1` at `K = 7, 8, 9`; these are the only ones left, and the
first of them (`K = 7, b = 6`; `K = 8, b = 6`; `K = 9, b = 7`) is where the wall
sits.
QUANTITY: the largest `b` with `1 ∈ (ROWS_b, RCUT_b, CSTP−1)` over `Q`; measured
`b = 5, 5, 6` at `K = 7, 8, 9`, target `b = 13, 15, 17`.
CHEAPEST TEST: not a bigger Gröbner — §5.3 shows the wall is combinatorial and
survives reduction mod 32003. The cheap test is to find the analogue of §3.2 for
the **second** band, i.e. to decide whether the band `3b−K−2` relation
`A·J(H,P) = H·J(H,ρ_d)` (`P² = AH`, `d = 3b−2K`) has any solution with
`deg_y P ≤ K−1`; that is pure binary-form factorisation, no CAS. ≈ 60
lane-minutes.

**`OPEN[K4RAY-VALUATION-LADDER]`** — the valuation refinement of §3.3 that this
lane derived but did **not** promote. Writing `P = β_b = x^m y^e (y−x)^f Q₀` and
`ρ_d = x^{m'} y^{e'} (y−x)^{f'} Q'`, the band identity
`P²[bP + K(y−x)P_x] = y^{2K−2}(y−x)²[dρ_d + K(y−x)(ρ_d)_x]` gives, **under the
genericity hypotheses `b ≠ K(b−e)`, `b ≠ Kf`, `m ≥ 1`**, the exact valuation
ladder `m' = 3m`, `e' = 3e−2K+2`, `f' = 3f−2`, hence `e ≥ ⌈(2K−2)/3⌉` — strictly
stronger than the charged `e ≥ ⌈(K−1)/2⌉` — and `deg Q' = 3 deg Q₀`.
QUANTITY: the `y`-valuation `e` of `β_b`; charged bound `e ≥ ⌈(K−1)/2⌉`,
conjectured bound `e ≥ ⌈(2K−2)/3⌉` (`= 4, 5, 6` at `K = 7, 8, 9`).
CHEAPEST TEST: discharge the three genericity hypotheses, or replace the
valuation argument by the exact identity `Q₀²Ψ = Ψ'` with
`Ψ = (b−Kf)xQ₀ + Km(y−x)Q₀ + Kx(y−x)(Q₀)_x`. Then feed `e ≥ ⌈(2K−2)/3⌉` into the
chart as extra linear rows on the top band (as `TB_K7_B6` does for the weaker
bound) and re-run `K = 7, b = 6`. ≈ 45 lane-minutes plus one Singular run.

**`OPEN[K4RAY-BETA-UPPER]`** — find any upper bound on `b = deg β` better than
`2K−1`. This is the single thing that would convert §5.2 from "an initial
segment" into "the row". The charged datum `M₂ = 3K−6` for the descended tuple
is the obvious candidate source, but Moh's `M_i` are contact orders in
`k[x]((g^{-1}))` (charged `g9966` §0.1), not degrees of `β`, and identifying the
two without a proof would be exactly the flag/place/series fallacy.
QUANTITY: `b = deg β`; known `⌈(2K+1)/3⌉ ≤ b ≤ 2K−1`; decide whether
`b ≤ K−1`, or whether `M₂ = 3K−6` forces `deg ρ = 4K−6` and hence `b = 2K−2`.
CHEAPEST TEST: compute `deg(g − f^{3/2})` in the degree filtration for the tower
— it equals `deg ρ − K` — and compare with Moh's `M₂` on a case where both are
independently known (the `(64,48)` control row). ≈ 40 lane-minutes.

**`OPEN[K4RAY-GUIDEDGB-POSDIM-CONTROL]`** — `guided_gb`'s perturbed-series
negative control does not fire on positive-dimensional homogeneous charts
(§6.4), because acceptance degenerates to `NF_ALL_ZERO` when
`predicted_length` is `None`. Any lane that uses a Hilbert hint on a cone rather
than on a `dim = 0` fibre currently gets an unguarded hint.
QUANTITY: `GG__PERTURBED_FAILED`; observed `0` where the protocol intends `1`.
CHEAPEST TEST: give `HilbertHint` an optional `predicted_hilb_series` acceptance
target (compare `hilb(G,1)` against the supplied numerator) so that a wrong
numerator is detectable without a finite `vdim`. ≈ 30 lane-minutes in
`box/lib/guided_gb.py`; it is a helper change, not a mathematics change.

---

## Artifacts

`box/k4rayhighk-20260903/` — **385 files**, 3.4 MB, `artifacts.sha256`
(`sha256(artifacts.sha256) = 9a3133e60aefff33005763da0be25cb4773a98a9168e9bb605c33676e8d04945`); `sha256sum -c` reports 385/385 OK.

```text
inputs.sha256                       manifest generated by awk from the run receipt; 13/13 OK
gen_hk.py                           chart generator (direct / ID6 / quad; rho-cut; TOP-BAND cut)
drive.py                            guided_gb driver (prelude row-count pass, then guided_groebner)
gen_lemmas.py, lemmas.sing/.out     V1..V7 machine verification (156 INJ instances)
gen_certif.py, runs/cert_K4_B3.*    homogeneous route: hilb numerator, CST^N in I, lift
hint_control.py, runs/HINT_K4_B3/   Hilbert hint + perturbed negative control
batch{1,2,3,4,5}.sh, runs/batch*.log
runs/probe_*                        formation probes (direct/quad/ID6, K=7 Bdeg=6 and 13)
runs/controls.sing                  C1..C4 controls
runs/<TAG>/<TAG>_p*_{Q,32003}.{sing,out,err,guided.json}, guided_gb_result.json, summary.json
runs/slim_K7_B6.{sing,out}          slimgb second-engine probe
```

Every Singular `.out` was read for `PRE__`, `CERT__`, `V*`, `C*`, `SG__` and
`GG__` markers, never by exit status — the `lift` naming collision in the first
certificate run (`identifier QQ in use`) was caught exactly this way.

## Reproduction

```bash
Singular --no-rc -q box/k4rayhighk-20260903/lemmas.sing | grep -E '^V[0-9]'
python3 box/k4rayhighk-20260903/drive.py SCUT_K9_B6 direct 9 6 --rhocut 0 --cores 1
python3 box/k4rayhighk-20260903/drive.py PC_K1_B1_x1 direct 1 1 --tk 1 --cores 1  # must SURVIVE
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `35578`.
- Body SHA-256:
  `f421e458f32b4fd9b82b83dc89a188d2cb0dabc9400ce7b9a7a820428b392657`.
- Artifact index: `box/k4rayhighk-20260903/artifacts.sha256`, 385 files,
  `9a3133e60aefff33005763da0be25cb4773a98a9168e9bb605c33676e8d04945`.
