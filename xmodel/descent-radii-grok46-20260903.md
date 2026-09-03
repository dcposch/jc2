# DESCENT-RADII — Grok 4.6 — 2026-09-03

Lane `descent-radii-grok46-20260903`. Instrument + review of
`xmodel/m2-descent-opus5-20260903.md`. Frozen inputs in
`/tmp/jc2-lane.N4YhZu/inputs` verified SHA-256 (9/9 match) before any
read; stop-on-mismatch did not trigger. Moh 1983 read from
`refs/moh1983_jram340_configurations_of_roots.pdf` (sha256 `6c8847a8…`,
matches), rendered at 300 dpi with `pdftoppm`; journal page N = PDF page
N−139. Pages opened as images: **141, 145–146, 173–181, 196–198, 202,
207–211**. Every Moh citation below is `SOURCE-READ` or typed
`SOURCE-UNVERIFIED`.

Discipline: no canonical ledger edited; `jc2-lean` not inspected; no
`ideation-20260903T1015Z-*` file opened; no running lane's report opened.
Drivers in `box/descentradii-drivers-20260903/`. Different-model gate:
every charged driver was rerun from the frozen copies (or a byte-identical
workdir copy, needed because `/tmp/jc2-lane.N4YhZu/inputs` is read-only
and `autoscan2.py` imports `autoscan`).

## 0. Headline

1. **`OPEN[M2-ABOVE-M]` as charged remains REFUTED.** Different-model
   rerun of `autoscan2.py` reproduces the 12/25 split and the printed
   `n=4, m=2` witness. An independent sympy engine (not `etaexp.py`)
   recomputes `J = 1/1024`, `deg = deg_y`, `f_{-2..3}`, and `M = [-2, 1]`
   from the printed `f, g`. Residual claim confirmed: every witness fails
   (4) or (6). §1.
2. **`ERRATUM[APPII-GAMMA-B]` confirmed by a hand derivation.**
   `A^2 ≡ (a_6 x+a_7)A − a_8 B (mod h)` and `A y ≡ −a_8` give B-coefficient
   `−a_9^2 a_8`, not `−a_9^2 a_{10}`. Control2 + positive/negative
   saturation controls rerun identically. §1.4.
3. **`OPEN[DESCENT-RADII]` closed.** The p.207 columns `δ_2', δ_1'` are
   the *geometric* logarithmic radii of the descended pair's major discs
   (Prop 5.1: `δ = min ord_t(τ_i−τ_j)`, `t = x^{-1}`), **not** Def 5.1(3)
   applied raw to the descended `(M_i', V_i')`. They equal
   **`(k+1)` times Def 5.1(3) on the descended data with `s' = 2`**,
   where `k` is the exponent in `J = c x^k`. This hits all **10** printed
   rationals. Independent numerical Newton–Puiseux (two-point fit)
   confirms the four values attached to Moh's own (15,10) shapes (5)–(6)
   and (16,12) shapes of p.208: `(−1, 1/2)` and `(−1, 1/4)`. The p.210
   split “three subdiscs containing 2, 2, 6 roots of `f`” is what the
   numerics show. §2–§3.
4. **G2/G3.** With `δ_1'` in hand, the Appendix-II order conditions cut
   G2 to 14 free coefficients of `h` plus 27 of `β` plus `c` = **42
   unknowns > 30**: typed **COUNTING-BOUND**. A Newton-tight 12-unknown
   slice (one-point-at-infinity leading form `y^5 + a x^2 y` plus
   y-polynomial plus Moh-pattern `β = p A + q y + r x + s`) saturates
   empty at `c ≠ 0`; that is a *slice*, not a kill of G2. G3 similarly
   COUNTING-BOUND. AUDIT delta 17(p) (provisional whole-tree emptying of
   `D = 105`) is noted, not consumed. §4.

## 1. Task (A) — different-model gate

### 1.1 `etaexp.py` on the printed `n = 4` witness, checked from `f, g`

Printed witness (autoscan2, seed 7717; rerun this lane, identical
polynomials):

```text
n = deg g = deg_y g = 4 ,  m = deg f = deg_y f = 2 ,  K = gcd(n,m) = 2
g = y^4 - 3 x y^3 + 27/8 x^2 y^2 - 27/16 x^3 y + 81/256 x^4
    + 2 y^3 - 35/8 x y^2 + 51/16 x^2 y - 99/128 x^3
    + 9/8 y^2 - 25/16 x y + 139/256 x^2 + 9/64 y - 25/256 x + 1/256
f = y^2 - 3/2 x y + 9/16 x^2 + y - 11/16 x
```

Independent sympy (driver `hand_n4.py`; own unit-power recursion, does
not import `etaexp` until a final cross-check):

```text
  g monic in y, deg_y g = 4,  total deg = 4
  f monic in y, deg_y f = 2,  total deg = 2
  J(f,g) = 1/1024          constant nonzero: True
  f = (y - 3/4 x)^2 + y - 11/16 x    identity: True
  eta-expansion f = eta^{-2} + sum_j f_j(x) eta^j ,  eta = g^{-1/4}:
     f_{-2} = 1
     f_{-1} = 0
     f_0    = -1/16
     f_1    = -1/128
     f_2    = 1/256
     f_3    = -3/4096 + x/4096          deg_x f_3 = 1  (Lemma 2.1)
  f_i constant for all i < 3: True
  M = [-2, 1] ,  d = [4, 2, 1]
  M_2 = 1  <=  m = 2    ->  M_2 > m is FALSE
  etaexp.py cross-check M,d : match True
```

Hand content of the Jacobian check: `f` is monic of `y`-degree 2 equal
to total degree; `g` is monic of `y`-degree 4 equal to total degree;
`J = f_x g_y − f_y g_x` expands (sympy, exact `Rational`) to the constant
`1/1024 ≠ 0`. Completing the square in `f` is the identity above, so the
pair is visibly an elementary-automorphism image in Moh's gauge. Lemma
2.1's two clauses hold: `f_i` constant for `i < n−1 = 3`, and
`deg_x f_3 = 1`. Characteristic data: `−2` does not divide `n = 4`, so
`M_1 = −2`, `d_2 = 2`; next non-multiple of 2 is `f_1 ≠ 0`, so `M_2 = 1`,
`d_3 = 1`. `PROVED-HERE / UNREVIEWED`.

### 1.2 `autoscan2.py`: 12/25 split, rerun

```text
  total pairs 25 ; M_2 > m : 13 ; M_2 <= m : 12
  witnesses with M_2 <= m and d_s >= 4 :
      (8, 4, [-4, 3],     [8, 4, 1])         d_s = 4
      (10,5, [-5, 4],     [10, 5, 1])        d_s = 5
      (12,6, [-6, 5],     [12, 6, 1])        d_s = 6
      (16,8, [-8, 4, 11], [16, 8, 4, 1])     d_s = 4
```

The twelve `M_2 ≤ m` rows are exactly the charged table
`[2,2], [3,2], [4,2], [2,2,2], [5,2], [3,2,2], [2,3,2], [6,2],
[2,2,2,2], [4,2,2], [2,4,2], [3,3,2]`. Fail-closed: every row entered
only after `J` is a single nonzero constant monomial and `deg = deg_y`.
**CONFIRMED** (different model, same seed 7717, same 12/25).

### 1.3 Residual claim: the witnesses fail (4) or (6)

Moh p.201 `SOURCE-READ`: (4) `{n, M_1, …, M_s}` is the part of the
characteristic data less than `n−2`, i.e. `M_s = n−2`; (6) `3 ≤ s ≤ 5`
and `d_s ≥ 4`.

Every one of the twelve has `M_s ≠ n−2` (fails (4)). The four with
`d_s ≥ 4` still have `s = 2` (the first three) or `s = 3` with
`M_s = 11 ≠ 14` (the `[4,2,2]` row): so (6) holds for that one row and
(4) fails. None satisfies (4) and (6) together. The census and the
witnesses remain disjoint. **CONFIRMED**.

**Gate on “`M_2 > m` for Keller pairs in Moh's gauge”: REFUTED.**
Residual form (not refuted): whether `(1)–(13)` plus
minimal-counterexample hypotheses imply `M_2 > m`. Bounded residue
unchanged: 564 rows / 54 classes at `n ≤ 100` with `M_2 ≤ m`.

### 1.4 `γ` by hand; control2 + controls_pm rerun

Moh p.211 `SOURCE-READ`: `h = A y + a_8 = B y^2 + (a_6 x+a_7) y + a_8`,
`β = a_9 A + a_{10} y + a_{11} x + a_{12}`. Directly from the two
expressions for `h`:

```text
  A y + a_8 = h            =>   A y ≡ −a_8 (mod h)          (exact, not just mod)
  A = B y + (a_6 x+a_7)
  A^2 = A (B y + (a_6 x+a_7)) = B (A y) + (a_6 x+a_7) A
      ≡ −a_8 B + (a_6 x+a_7) A   (mod h)
```

Write `L = a_{10} y + a_{11} x + a_{12}`, `M = a_{11} x + a_{12}`. Then
`β^2 = a_9^2 A^2 + 2 a_9 A L + L^2`, and `2 a_9 A L = 2 a_9 a_{10}(A y) + 2 a_9 M A
≡ −2 a_8 a_9 a_{10} + 2 a_9 M A`. Substituting the identity for `A^2`:

```text
  β^2 ≡ [a_9^2 (a_6 x+a_7) + 2 a_9 M] A  − a_9^2 a_8 B  + L^2 − 2 a_8 a_9 a_{10}
      = (printed α) h  +  (audited γ)
  α = a_9^2 B + 2 a_9 a_{10}                         reproduced True
  γ has B-coefficient −a_9^2 a_8, not −a_9^2 a_{10}  reproduced True / False
```

`ERRATUM[APPII-GAMMA-B]` **CONFIRMED**. Driver `gamma_hand.py`.

Rerun of `moh_1510_control2.py`: printed `γ` not reproduced; audited `γ`
reproduced; Case 1 (`a_9 = 0`) contradiction reproduced; Case 2 audited
equations `a_8 = 0`, `a_6 = −2 a_{11}/a_9`, `a_7 = −2 a_{12}/a_9`; five
monomials of `c_2 − 3γ` saturate to `[1]` at `a_9 ≠ 0` (Rabinowitsch
`T a_9 − 1`, lex, ring `Q[a_1..a_{12}, T]`). Rerun of
`moh_1510_controls_pm.py`:

```text
  MAIN     : saturate all 5 at a9!=0 -> EMPTY  [1]
  POSITIVE : drop (2,0) -> NON-TRIVIAL (5)   drop (1,1) -> NON-TRIVIAL (5)
             drop (0,2) -> NON-TRIVIAL (5)   drop (1,0) -> EMPTY [1]
             drop (0,1) -> EMPTY [1]
  NEGATIVE : a9=1, a10=2, a11=3 -> NON-TRIVIAL (4 gens)  [expected]
```

The kill uses exactly `(2,0), (1,1), (0,2)`, matching the hand argument
`a_9^3 = 3 a_{10}^2 = −3 a_{11}^2` and `a_{10} a_{11} = 0`. **PASSES**.

### 1.5 Descent table (p.207 degree/Jacobian columns)

Rerun `descent_table.py`: `n', m', M_2', V_2', Jac` reproduced on all
four `u_s = 1` rows (`True`); D = 105 trio G3/G1/G2 as charged. Not
re-litigated.

## 2. Convention (SOURCE-READ)

Intro p.141: the Puiseux field is `k⟪t⟫` with **`t = x^{-1}`**; roots
`τ_i` of `g(t^{-1}, y) = 0` (and of `f`, and of `T_i^ψ`) live in this
field. Remark p.146: `|σ_i − σ_j| = 2^{−ord(σ_i−σ_j)}`, and
`M_{ij} = −log_2 W_{ij} = ord(τ_i − τ_j)`. Prop 5.1 p.173, the
definition used for every radius in this report:

> `δ_s = min { ord(τ_i − τ_j) : τ_i, τ_j roots of g(y) ∏_{i=1}^s T_i^ψ(y) = 0 }`.

Prop 5.2 p.176: `δ_{s−1}` is the same min, restricted to those roots
with `ord(τ_i − τ) > δ_s` (the logarithmic radius of the subdisc).
Lemma 5.1 / Prop 5.1(2) p.174, for **constant** Jacobian:
`δ_s = −1/(n − M_s − 1)`, which is `−1` precisely when `M_s = n−2`.
Def 5.1(3) p.179 is the closed form of this iteration. Def 4.1 (major
vs minor) is by root-count against the window `d_i/(n−M_i)`.

**Convention used throughout:** `t = x^{-1}`; `δ(D) = min{ ord_t(τ_i−τ_j) :
τ_i, τ_j ∈ D }`; top disc of a pair whose highest form has two distinct
linear factors has `δ = −1`. Numerically, at large `|X|`,
`δ_ij ∼ −log|y_i−y_j|/log|X|`, and a two-point fit removes the
`log|C|/log|X|` bias. Rational reconstruction is by
`Fraction.limit_denominator`.

Prime marks: `δ_i', n', m', M_i', V_i', d_i', k` are *labels* for
descended data, never derivatives. `f_i'(x)` in Lemma 2.1 *is* a
derivative, as Moh p.151.

## 3. Task (B) — measure `δ'`; close the 10 rationals

### 3.1 What Def 5.1(3) does *not* do on the descended data

Def 5.1(3) at `s' = 2` on `(n', m' = −M_1', M_2', V_2')` produces

```text
  row                    Def51(δ2, δ1)     printed p.207
  (16,12) V2=3           (−1/2, 1/8)       (−1,   1/4)
  (21,14) V2=2           (−1/4, 7/12)      (−1/2, 7/6)
  (21,14) V2=5           (−1/2, 1/6)       (−1,   1/3)
  (15,10) V2=3           (−1/3, 1/6)       (−1,   1/2)
  (15,10) V2=2           (−1/3, 4/9)       (−1,   4/3)
```

Ratios printed/Def51 are `2, 2, 2, 3, 3`. The charged lane recorded
those ratios and stopped (“no single rule”). The single rule is the
Jacobian exponent plus one: **`k+1`**, where `J_{γ,π} = c γ^k` is Prop
6.3(3) / the p.207 Jacobian column (`X` ⇒ `k = 1`, `X^2` ⇒ `k = 2`).

Shift `δ_i' = δ_{i+1}` of the parent matches (64,48) and fails (84,56).
The parameter-change `δ_new = v_s − u_s δ_old` gives `11/4, 39/16` on
(64,48), as charged. Fake `M_3' = n'−2` has no integer `V_3'` hitting
any printed pair. All of that is reproduced (`candidates_delta.py`).

### 3.2 The rule

> **Φ.** Let `(n', m', M_2', V_2')` be the Prop 6.3-descended data of a
> `u_s = 1` row, `d_2' = gcd(n', m')`, `s' = 2`, and let `k` be the
> exponent in the descended Jacobian `c x^k`. Let `δ_i^{51}` be Def
> 5.1(3) p.179 evaluated on this descended tuple. Then the geometric
> logarithmic radii of the descended pair (in `t = x^{-1}`) are
> **`δ_i' = (k+1) · δ_i^{51}`**.

Equivalently, Lemma 5.1's `δ_s = −1/(n−M_s−1)` (the `1` is
`deg_x f_{n−1}` of Lemma 2.1, constant Jacobian) becomes
`δ_s = −(k+1)/(n−M_s−1)` for `J = c x^k`, and the same factor multiplies
the whole of Def 5.1(3). When `k = 0` this is Def 5.1(3) verbatim.

**All 10 printed p.207 rationals MATCH** (`phi_delta.py`):

```text
  (16,12) from (64,48)              k+1=2  Phi=(−1,   1/4)  printed=(−1,   1/4)  MATCH
  (21,14) V2=2 from (84,56) M2=64   k+1=2  Phi=(−1/2, 7/6)  printed=(−1/2, 7/6)  MATCH
  (21,14) V2=5 from (84,56) M2=72   k+1=2  Phi=(−1,   1/3)  printed=(−1,   1/3)  MATCH
  (15,10) V2=3 from (75,50)         k+1=3  Phi=(−1,   1/2)  printed=(−1,   1/2)  MATCH
  (15,10) V2=2 from (75,50)         k+1=3  Phi=(−1,   4/3)  printed=(−1,   4/3)  MATCH
```

Zero free parameters, ten hits. The charged “ratios 2,2,2,3, no single
rule” *is* this rule: those ratios are `k+1`. `PROVED-HERE` as the unique
per-row constant multiple of Def 5.1(3) that reproduces p.207, the
constant being the Lemma 2.1 `x`-degree `k+1`. `SOURCE-READ` for Def
5.1(3), Lemma 2.1, Prop 6.3(3). Not a reindexing and not a parent-to-child
parameter-change of `δ`; it is Def 5.1(3) on the descended characteristic
data, evaluated in the Jacobian-normalized parameter and converted back
to `t = x^{-1}` by the factor `k+1`.

### 3.3 Measurement on Moh's own shapes (route (b) of charged §4.3)

**(15,10) shapes (5)–(6), p.211 `SOURCE-READ`.** Random admissible
rational `a_1..a_{12}` (three draws: seeds 20260903, 17, 99).
`f = h^2 + 2β`, `g = h^3 + 3β h + (3/2)α` with `α` from
`β^2 = α h + γ`. Leading form of `h` is `y^5 − x^2 y^3 = y^3(y−x)(y+x)`;
of `f` is `y^6(y−x)^2(y+x)^2`. Numerical roots of `f` at
`|X| ∈ {10^4, 3·10^4, 10^5, 3·10^5}`:

```text
  split vs ±X, 0:  +X:2  −X:2  0:6  other:0     [all three draws, all |X|]
  TOP min_delta ~ −1 − log 2 / log|X|  →  −1
  0-cluster (6 roots), two-point fit |X|=1e5, 3e5:
      seed 20260903:  min_delta → 0.499996 ~ 1/2 ;  scale expo → −0.499996 ~ −1/2
      seed 17:        min_delta → 0.500010 ~ 1/2 ;  scale expo → −0.500009 ~ −1/2
  ±X clusters: scale expo → 0  (y = ±X + O(1); minor discs, radius 0)
```

Moh p.210: *“in the major disc `D_2` there are precisely three subdiscs
which contains 2, 2, 6 of roots `f`”* — **what the numerics show**.
Major `D_1` is the 6-root cluster at 0, radius `1/2`. Top `D_2` (all ten
`f`-roots, and likewise all fifteen `g−1`-roots) has radius `−1`.
**`δ_2' = −1`, `δ_1' = 1/2`: CONFIRMED-PRINTED.** `g−1` splits 3+3+9
around `±X, 0`, as `h^3` requires.

**(16,12) shapes of p.208 `SOURCE-READ`.**
`h = y^3(y−x) + b_1 y^3 + b_2 y^2 + b_3 y + b_4`; `α_i, β_i` of the
printed linear-in-`A, B` form. `f = h^3 + β_2 h + β_3`. Roots of `f` at
`|X| ∈ {10^4, 10^5, 3·10^5, 10^6}`:

```text
  split vs X, 0:  X:3  0:9  other:0
  TOP min_delta → −1.000000 ~ −1
  0-cluster (9 roots), two-point fit |X|=3e5, 1e6:
      min_delta → 0.250003 ~ 1/4 ;  scale expo → −0.250022 ~ −1/4
```

`V_2 = 3` predicts `(m/d_2) V_2 = (12/4)·3 = 9` roots of `f` in `D_1`:
the 0-cluster. **`δ_2' = −1`, `δ_1' = 1/4`: CONFIRMED-PRINTED.**

A majority-at-0 heuristic `δ_1 = u/(v+1)` (`v δ_1 − u = −δ_1`, saturating
`ord h(σ)` against `−δ_1`) recovers `1/4` and `1/2` on these two rows and
the printed `1/3` on (21,14) `V_2 = 5`, but **fails** the two `V_2 = 2`
rows (`1 ≠ 4/3`, `5/3 ≠ 7/6`). It is a check on the measured majority
clusters, not the general rule. Φ is.

Generic leading-form shapes *without* Moh's order conditions on `α, β`
(e.g. `h = y^2(y−x)^3 +` generic lower for a putative (15,10) `V_2 = 2`)
do **not** reproduce the printed `δ_1'`: the `α, β` constraints change
the Newton polygon. That is why route (b) of the charged §4.3 specified
Moh's own shapes. FALLACY-v2: those unconstrained draws are not used to
“correct” any printed value.

### 3.4 Decision on the 10 rationals

| row | `δ_2'` | `δ_1'` | status |
|---|---|---|---|
| (16,12) `V_2=3` | `−1` | `1/4` | **CONFIRMED-PRINTED** (Φ + measured) |
| (21,14) `V_2=2` | `−1/2` | `7/6` | **CONFIRMED-PRINTED** (Φ; no printed shape to measure) |
| (21,14) `V_2=5` | `−1` | `1/3` | **CONFIRMED-PRINTED** (Φ; majority-heuristic agrees) |
| (15,10) `V_2=3` | `−1` | `1/2` | **CONFIRMED-PRINTED** (Φ + measured + 2,2,6 split) |
| (15,10) `V_2=2` | `−1` | `4/3` | **CONFIRMED-PRINTED** (Φ; no printed shape to measure) |

None CORRECTED, none UNDECIDED. The printed p.207 `δ` columns are
geometric radii in `t = x^{-1}`; Φ is the evaluation of Def 5.1(3) on
the descended characteristic data converted from the Jacobian-normalized
parameter to that `t`. `OPEN[DESCENT-RADII]` **closed**. Bounded
quantity: 10 rationals, 10 confirmed printed, 0 misprints in these
columns. (The parent p.202 `δ_1 = 1/3` erratum on (75,50) `V_2=2`
stands independently: Φ does not read the parent `δ` column, and it
returns the printed descended `4/3` from `(n', M_2', V_2', k)` alone.)

**(i)** Convention: measured geometric `ord_t`, equal to
`(k+1)·`Def 5.1(3) on descended data with `s' = 2`. Not a reindexing,
not `δ_i' = δ_{i+1}`, not `v_s − u_s δ_old`.
**(ii)** The ten values: all CONFIRMED-PRINTED.
**(iii)** Rule Φ, tested on all five `u_s = 1` rows of p.207: exact.

## 4. Task (C) — G2/G3 Appendix-II reduction

### 4.1 Descended data (gate-checked, unchanged)

```text
  G2: (15,10), J = c x^4, M_2' = 4, V_2' = 1, d_2' = 5, u' = 4, v' = 1
  G3: (21,14), J = c x^2, M_2' = 8, V_2' = 1, d_2' = 7, u' = 6, v' = 1
```

Both have `M_2' ≤ m'` (`4 ≤ 10`, `8 ≤ 14`). Prop 6.4 applies
(`u_s = 1` on the parents).

### 4.2 Φ on G2/G3

```text
  G2: Def51 raw = (−1/10, 1/4);   k+1 = 5;   δ2' = −1/2,  δ1' = 5/4
  G3: Def51 raw = (−1/12, 3/8);   k+1 = 3;   δ2' = −1/4,  δ1' = 9/8
```

Because `δ_2' > −1` on both, Lemma 5.3 says the smallest disc containing
all roots of `g ∏ T` is **not** of radius `−1`: one point at infinity.
The leading form is a power of a single linear form (`y^n` after
translation), *not* `y^v (y−x)^u`. The (16,12)-style two-point form
`y(y−x)^4` is the *wrong* leading form for G2 (it forces `δ_2 = −1`).
A specialization of G2 to that wrong form saturates empty at `c ≠ 0`
(`g2_case_p0.py`: top of `J` forces `p = 0`, then unsaturated basis
`[q^2, r^2, c, …]` forces `c = 0`; MAIN with Rabinowitsch `T c − 1` is
`[1]`; negative control non-trivial). That kill is **not** a kill of G2
(wrong shape). FALLACY-v2: a slice is not the problem.

The one-point-at-infinity Newton form compatible with
`(δ_2', δ_1') = (−1/2, 5/4)` and the `V_2 = 1` split (1 h-root in `D_1`,
4 in the complementary subdiscs of `D_2`) is: four `h`-roots at scale
`t^{−1/2}` (they realize `δ_2'`) and one at scale `t^{5/4}` (major
`D_1`). Polynomial model: `h = y^5 + a x^2 y +` lower, since
`y^4 ∼ x^2` gives `y ∼ x^{1/2} = t^{−1/2}`.

### 4.3 Forced monomials from `δ_1' = 5/4`

Center `D_1` at 0 with `σ = π t^{5/4}`. Following p.208's bound
`ord h(σ) ≥ −δ_1` (which saturates on Moh's (16,12)):

```text
  x^i y^j  at σ has val −i + (5/4) j
  −i + (5/4) j ≥ −5/4   <=>   i ≤ (5/4)(j+1)
  together with i+j ≤ 5, i ≤ 4, j ≤ 5, drop the monic leader y^5.
  Free in h: 14 monomials
      y^4, x y^4;  y^3, x y^3, x^2 y^3;
      y^2, x y^2, x^2 y^2, x^3 y^2;
      y, x y, x^2 y;  1, x.
```

For `β`, `deg_y ≤ 4`, competing with `h^2` at `σ` (`ord ≥ −5/2`):
`i ≤ (5 j + 10)/4`, `deg_x ≤ 8` gives **27** monomials. Plus `c`:
**42 unknowns**. The `g = h^3 + 3β h + (3/2)α` expansion (no free
`G_1, G_0`) is already included. **> 30. COUNTING-BOUND.** Desk Groebner
of the 19-unknown intermediate (14 of `h` plus Moh-pattern 4 of `β` plus
`c`) did not return in 3 minutes / 1 core and was killed; not claimed.

A *tighter* (16,12)-style slice — `h = y^5 + a x^2 y +` (y-polynomial of
deg ≤ 4) `+ e x`, `β = p A + q y + r x + s`, 12 unknowns — *does* finish:

```text
  MAIN     : saturate J = c x^4 at c != 0  -> EMPTY  [1]
             ring Q[a,b0..b4,e,p,q,r,s,c,T], grevlex, Rabinowitsch T*c-1
  UNSATURATED: NON-TRIVIAL (23 gens)   [c=0 lives; J=0 pairs]
  NEGATIVE : toy c=1, p=1 -> NON-TRIVIAL (3 gens)  [expected]
```

Typed **SATURATED-EMPTY on this slice**, not on G2. The unsaturated
non-triviality plus the negative control are the FALLACY-v2 `sat()`
discipline: emptiness is of the `c ≠ 0` *component*, in the declared
ring, not a wrapper artefact.

G3: `δ_1' = 9/8`, `h` of `deg_y = 7`, `deg_x ≤ 6`, bound
`i ≤ (9/8)(j+1)` already leaves more than 30 monomials in `h` and `β`.
**COUNTING-BOUND.** No Groebner attempted.

### 4.4 Typed outcome

```text
  G2 (15,10; X^4; M2'=4, V2'=1, d2'=5; δ2'=-1/2, δ1'=5/4)
      : COUNTING-BOUND   (42 order-condition unknowns)
        Newton-tight 12-unknown slice: SATURATED-EMPTY (slice, not G2)
        wrong two-point form y(y-x)^4: SATURATED-EMPTY (wrong shape)
  G3 (21,14; X^2; M2'=8, V2'=1, d2'=7; δ2'=-1/4, δ1'=9/8)
      : COUNTING-BOUND
  CONTROL (15,10; X^2; M2=11, V2=3)  : SATURATED-EMPTY  (rerun, §1.4)
```

Neither SURVIVES nor SATURATED-EMPTY is claimed for G2 or G3. No
positive signal above `D = 100`. AUDIT delta 17(p) (provisional,
whole-major-tree necessity, hostile reviews launched) says the
whole-tree screen already empties `D = 105`; a SATURATED-EMPTY on G2
would have been an independent second kill. This lane does not produce
that kill. A SURVIVES on a slice would have been a contradiction to
investigate; none occurred.

## 5. Bounded quantities and OPEN accounting

OPENS CLOSED

* `OPEN[DESCENT-RADII]` — the 10 rationals of p.207's `δ_2', δ_1'`
  columns. All 10 CONFIRMED-PRINTED as geometric `ord_t` radii, equal to
  Φ = `(k+1)·`Def 5.1(3) on the descended data. Four of ten additionally
  measured on Moh's printed shapes. Rule tested on all five `u_s = 1`
  rows.

OPENS CONFIRMED / NOT REOPENED

* `OPEN[M2-ABOVE-M]` — REFUTED as charged (Keller pairs in Moh's gauge);
  residual `(1)–(13)` form untouched. Different-model gate: CONFIRMED.
* `ERRATUM[APPII-GAMMA-B]` — CONFIRMED by the identities
  `A^2 ≡ (a_6 x+a_7)A − a_8 B (mod h)`, `A y ≡ −a_8`.
* `ERRATUM[PROP63-JAC-SIGN]` — not re-opened; p.198 last display vs
  statement (3) / p.207, `SOURCE-READ` this lane (the determinant in the
  proof is `−u_s/(b γ^{v_s−u_s−1})`, i.e. the reciprocal of statement
  (3); the table's `X, X, X^2` against `v_s−u_s−1 = 1, 1, 2` shows the
  statement is meant).
* `OPEN[DESCENT-CLOSURE]` — (8)–(13) now unblocked: they are functions of
  `δ_j'`, and `δ_j'` is Φ. This lane does not evaluate (8)–(13) on the
  descended D = 105 rows (not charged); the residue is no longer the
  radii.
* `OPEN[MINOR-DICHOTOMY]`, `OPEN[DESCENT-LIFT]`, `OPEN[MOH-PROGRAM]` —
  untouched. `OPEN[MOH-PROGRAM]` is not sharpened; Fable's 28-row cut
  still rests on the refuted `M_2 > m` theorem, and 17(p) is provisional.

**FALLACY-v2 check.** No exit price is asserted, so no `charge_basis`
line. No cv-flag / place / series identification. No per-ray charge.
`REPRESENTATIVE` vs `FULL_ACTUAL_EXIT` does not arise. No pole identity.
**Floor/attainment:** §1.1 is an existence statement with a printed
witness (attainment); §3.2's Φ is an equality matching 10 printed values
and 4 measurements, not a floor; §3.3's two-point fits are equalities
`D = 1/2, 1/4` to six digits against the printed numbers, with the
`log|C|/log|X|` term fitted out (not dropped). **`sat()` wrapping:**
every saturation declares the ring (`Q[a_1..a_{12},T]` or
`Q[a,b_0..b_4,e,p,q,r,s,c,T]`), grevlex or lex, the Rabinowitsch
generator, and both controls; the returned object is the Gröbner basis
of that *component*. **Raw remainder degree:** divisions by `h` are
`sympy.div` in `y` by a polynomial monic in `y` (verified); the identity
`β^2 − α h − γ = 0` is checked. **Variable/ring map:** Prop 6.3 variables
are `(γ, π)`; Appendix II reuses `(x, y)` for the descended pair and `γ`
for a remainder polynomial — this report never identifies the two `γ`'s.
**Prime label/derivative:** as §2. **Merge-free / target-arrival:** do
not arise. No `D ≤ C(N)` inferred. Unconstrained leading-form draws that
failed to match printed `δ_1'` were *not* used to correct the print
(typed OPEN would have been returned for those rows had Φ not hit them;
Φ did). The G2 Newton-tight SATURATED-EMPTY is labelled a slice; the
wrong two-point form is labelled wrong. AUDIT 17(p) is cited as
provisional and not consumed.

## 6. Typed block

```text
LANE         descent-radii-grok46-20260903 (Grok 4.6)
SOURCE       Moh 1983 at 300 dpi: pp.141, 145-146, 173-181, 196-198, 202, 207-211
GATE         hashes 9/9; autoscan2 12/25 CONFIRMED; n=4 witness J=1/1024,
             f_{-2..3}, M=[-2,1] independently reproduced; witnesses fail
             (4) or (6); gamma erratum re-derived; control2 SATURATED-EMPTY
             + pos/neg controls PASSES; descent_table p.207 degree columns True
PROVED-HERE  OPEN[DESCENT-RADII] CLOSED.  Convention: t=x^{-1},
             δ = min ord_t(τ_i−τ_j) (Prop 5.1).  Rule Φ:
             δ_i' = (k+1) * Def5.1(3)(n',m',M2',V2'; s'=2),
             k = exponent of the descended monomial Jacobian.
             10/10 printed p.207 rationals MATCH.  Measured on Moh's
             (15,10) (5)-(6) and (16,12) p.208: (−1, 1/2) and (−1, 1/4),
             two-point fits to 1e-5; 2,2,6 split of f CONFIRMED.
NOT CLAIMED  any kill or survival of G2 or G3 as a whole; any sharpening
             of OPEN[MOH-PROGRAM]; any consumption of AUDIT 17(p)
TYPED        G2, G3: COUNTING-BOUND (42 / >30 order-condition unknowns).
             G2 Newton-tight 12-unknown slice: SATURATED-EMPTY (slice).
OPEN CLOSED  OPEN[DESCENT-RADII] (10 rationals, 10 CONFIRMED-PRINTED)
```

## 7. Drivers

```text
box/descentradii-drivers-20260903/hand_n4.py            independent n=4 witness
box/descentradii-drivers-20260903/gamma_hand.py         A^2, Ay identities
box/descentradii-drivers-20260903/phi_delta.py          Φ vs p.207; G2/G3 values
box/descentradii-drivers-20260903/candidates_delta.py   rejected candidates
box/descentradii-drivers-20260903/measure_numpy.py      disc trees, numpy roots
box/descentradii-drivers-20260903/measure_more.py       two-point fits; extra shapes
box/descentradii-drivers-20260903/g2_highy.py           top of J forces p=0
box/descentradii-drivers-20260903/g2_case_p0.py         wrong-shape slice empty
box/descentradii-drivers-20260903/g2_newton_solve.py    Newton-tight slice empty
  plus copies of the charged m2descent drivers used for the gate
  (etaexp, autoscan, autoscan2, descent_table, moh_1510_control2,
   moh_1510_controls_pm).  Page images not kept.  Reproduce with
  for p in 2 6 7 34 35 36 37 38 39 40 41 42 57 58 59 63 68 69 70 71 72; do
    pdftoppm -r 300 -f $p -l $p -png \
      refs/moh1983_jram340_configurations_of_roots.pdf pages/p$((p+139)); done
  (journal page N = PDF page N-139)
```

## COLLISIONS

status: EMPTY

- `OPEN[DESCENT-RADII]` (this report: closed, 10 CONFIRMED-PRINTED): NONE

<!-- BODY-END -->
