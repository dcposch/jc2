# APPENDIX-II COMPILER — Grok 4.6 — 2026-09-03

Lane `appendix2-compiler-grok46-20260903`. Frozen inputs in
`/tmp/jc2-lane.SaQtV7/inputs` verified SHA-256 (13/13 match) before any
read; stop-on-mismatch did not trigger. Moh 1983 read from
`refs/moh1983_jram340_configurations_of_roots.pdf` (sha256 `6c8847a8…`,
matches). Journal page N = PDF page N−139. Pages opened as images:
**207–211**. Every Moh citation below is `SOURCE-READ` or typed
`SOURCE-UNVERIFIED`.

Discipline: no canonical ledger edited; `jc2-lean` not inspected; no
`ideation-*` file opened; no running lane's report opened. Drivers in
`box/appendix2/`. Charged machines (descent, Φ, control2, skeleton,
whole-tree JSON) consumed as frozen copies.

## 0. Headline

1. **The compiler exists and is fail-closed on Moh's six.** Prop 6.3
   descent, Φ radii, (8)–(13) on the descended tower, Moh's SHAPE
   reduction, and exact Gröbner of every in-budget system are one
   machine (`box/appendix2/compile.py`). p.207 signatures match on all
   five `u_s = 1` rows. The (15,10; `V_2 = 3`) pp.210–211 reduction and
   kill replay the charged control2: printed `α` reproduced, printed `γ`
   not reproduced (`ERRATUM[APPII-GAMMA-B]`), Case 1 contradiction
   reproduced, Case 2 saturates to `[1]` at `a_9 ≠ 0`. Positive drop-one
   and negative toy controls pass. §1–§3.

2. **`s' = 2` means (10)/(11) are vacuous; only (12)/(13) is active.**
   Conditions (10)/(11) constrain `V_{r-1}` for `r = s,…,3`, i.e. levels
   `j = s-1,…,2`. At `s' = 2` the loop `range(s-1, 1, -1)` is empty.
   `SOURCE-READ` p.201; identical to `moh_skeleton_full.Skel.full_ok`.
   Φ-`(12)/(13)` holds on all five Moh descended rows. §2.

3. **SHAPE rule, gated on Moh.** D1 order `i ≤ δ_1'(j+1)` for `h` and
   `i ≤ δ_1'(j+d')` for `β`, plus total-degree and `deg_x` bounds; when
   `δ_2' = -1` the degree-`K` form is fixed to the split leading form
   (`u' = 1`: `y^{V_2}(y-x)`; `u' = 2`: `y^{V_2}(y^2-x^2)` from the
   inverse-transform minor disc, p.210). Free `h` after the fix is the
   D1-lower monomials. This reproduces Moh's (15,10) shapes (5)–(6)
   (8 free in `h`) and (16,12) shape (1) (4 free, `y`-only lower).
   Coefficient counts: **22** = 8+14 order-`β` for (15,10) `V_2 = 3`;
   **15** = 11+4 A,B-`β` for (15,10) `V_2 = 2` (Moh's bracket 15 or 13);
   **17 → 10** is SOURCE-READ p.208–209 (A,B inventory of `α_i, β_i`,
   then the `η`-reduction). G2: **14+27+`c` = 42**, agrees with the
   charged descent-radii lane. §3.

4. **In-budget Moh rows die uniformly at `J = c x^k`, `c ≠ 0`.**
   Two-point (`δ_2' = -1`) systems with `≤ 30` unknowns:

   | row | unknowns | verdict | unsat / neg |
   |---|---:|---|---|
   | (15,10) `V_2=3` | 12 (control2) | **SATURATED-EMPTY** | drop-one + toy pass |
   | (15,10) `V_2=2` | 16 (A,B+`c`) | **SATURATED-EMPTY** | unsat  non-triv; neg OK |
   | (21,14) `V_2=5` | 16 (A,B+`c`) | **SATURATED-EMPTY** | unsat non-triv; neg OK |
   | (16,12) | 18 (`b,c_i,c`) | **SATURATED-EMPTY** | unsat 258 gens; neg OK |

   (21,14) `V_2=2` has `δ_2' = -1/2 ≠ -1`: **COUNTING-BOUND** (68).
   (99,66): `u_s = 3`, Prop 6.3 N/A. Planted descended automorphism:
   **NONE** (0/25 autoscan2 pairs have `M_s = n-2`). SURVIVES uncalibrated.
   §4.

5. **The 52 C_FULL_TREE_ODE excess rows at `n ≤ 100` all have `u_s = 1`,
   and none is an Appendix-II `s' = 2` problem.** One Prop 6.3 step
   leaves `s' ∈ {3,4}`. The `s = 2` shape (and `u' = d_2' − V_2'`) is
   not applicable: `V_2` is not the top multiplicity of a 2-level tower.
   Verdict **S-PRIME-GT-2** on 52/52. Coefficient-level kills: **0**.
   Positive-dimensional survivors: **0**. Out of the `s' = 2` budget:
   **52**. Generalized Def 5.1(3) on the actual `s'` tower has vanishing
   denominator `n' − M_{s'} − 1 = 0` on **38/52** (typed
   `OPEN[DEF51-MONOMIAL-MS-NMINUS2]`). A second descent with `u_{s'} = 1`
   exists on **exactly one** row. D = 108 C_FULL_TREE `u_s = 1`: **19**
   rows, all `s' = 3`, all **S-PRIME-GT-2**. G2/G3: COUNTING-BOUND 42 / 66,
   shape rule agrees. §5.

6. **Candidate (T)-shape, MEASURED not proved.** Every in-budget
   two-point descended pair (`δ_2' = -1`) saturates empty at `c ≠ 0`
   under D1+leading+A,B and `J = c x^k`. That is one class, not “always
   the same `h`-adic component”: Moh's (15,10) `V_2 = 3` kill is the
   `c_2 − 3γ ∈ k` system; the compiler's uniform test on the other three
   is the full Jacobian polynomial. Cheapest next experiment: a
   Newton-tight slice of the remaining Moh row (21,14) `V_2 = 2`
   (`δ_2' = -1/2`, 68 unknowns), in the same class as G2. §6.

No `charge_basis` line: this report asserts no new exit price.

## 1. Frozen-input gate and method

SHA-256 of `/tmp/jc2-lane.SaQtV7/inputs` (13/13 match the launch
manifest):

```text
2482ae1e8550cbaf6042a59ff20ca990eef78d7b77c590c1958a816c66a4e512  descent-radii-grok46-20260903.md
8aa3ba20567cb810cb6f540ef451e7fb4cadb8ad89f77418837f5d65fae55668  m2-descent-opus5-20260903.md
9497e23140ca2c92f99f706e23affbaaaf4dfdab63ce7b93b5dea76933aabf6d  whole-tree-review-grok46-20260903.md
dfb81ffef2050c582451b1e096c8ae20b6ff0c15b61c1be0aaf5be530c10948b  descent.py
4bcb512d47cf9f935c6a2c0c7b8251ae16b3e4f73b4794abbef2d1702846c7c1  phi_delta.py
5ea3845b6e6f7022a59b0620b22f017c632ef08e6e5d0675f9c3d0274032566b  moh_1510_control2.py
add00ccc08951cc356891e3198bb39bf8ae5b55ffd182354ace7ba8a8ef3aa8a  moh_1510_controls_pm.py
aad83d39a8830f2eb3ff888997394bbc9cbf58e1074fe61f3695f3e797764c87  descent_table.py
e84fa92ff380f90558ace924d924b777f723f845cd1809534390fa3268a1328f  autoscan2.py
334e6fd87521741d2c7c35e647fad28a8d9cd245c0daf33b9f6151ef85b154d5  full-tree-ode-excess-witnesses.json
01a5341fec7e5f26a31671c5227b3851bf6635f6ef0f3f1f9f00d0172431ffd2  candidate-results.json
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  moh1983_jram340_configurations_of_roots.pdf
```

Prime marks `n', m', M_i', d_i', V_i', δ_i', k` are *labels* for
descended data, never derivatives. `f_i'(x)` in Lemma 2.1 *is* a
derivative (Moh p.151). Prop 6.3 variables are `(γ, π)`; Appendix II
reuses `(x, y)` for the descended pair and `γ` for a remainder
polynomial — this report never identifies the two `γ`'s.

Load-bearing checks use `require()` (not `ast.Assert`). `python3 -O`
replay: `box/appendix2/test_replay.py` (gates + Φ 10/10 + G2=42 +
descent of (75,50)). Assert scan: three documentation `assert`s in
`test_replay.py`, all duplicated by `require()`.

## 2. Task (1) — emit: descent, Φ, (8)–(13), SHAPE, system

### 2.1 Descent (Prop 6.3 / 6.4)

One step, `u_s = d_s − V_s = 1` required (else `US-GT-1`). Transformation,
`SOURCE-READ` p.207 / charged `descent.py`:

```text
n' = n/d_s,  m' = m/d_s,  M_i' = M_i/d_s (i < s),  d_i' = d_i/d_s,
V_i' = V_i (i < s),  k = v_s − u_s − 1,  s' = s − 1.
```

p.207 gate (this lane, identical to charged `descent_table.py`):

```text
  (64,48)                 -> (16,12) M2'=13 V2'=3 k=1  s'=2
  (84,56) M2=64,V2=2      -> (21,14) M2'=16 V2'=2 k=1  s'=2
  (84,56) M2=72,V2=5      -> (21,14) M2'=18 V2'=5 k=1  s'=2
  (75,50) V2=3            -> (15,10) M2'=11 V2'=3 k=2  s'=2
  (75,50) V2=2            -> (15,10) M2'=11 V2'=2 k=2  s'=2
  (99,66)                 u_s=3  Prop 6.3 N/A
```

All five `u_s = 1` rows: `True`. G2/G3: `(15,10; k=4, M2'=4, V2'=1)` and
`(21,14; k=2, M2'=8, V2'=1)`. G1: `u_s = 2`.

### 2.2 Radii by Φ

Charged closed rule, reproduced:

> **Φ.** `δ_i' = (k+1) · Def 5.1(3)(n', m', M_2', V_2'; s' = 2)`.

10/10 printed p.207 rationals MATCH (`shape.phi_s2`, same arithmetic as
charged `phi_delta.py`). G2/G3: `(-1/2, 5/4)` and `(-1/4, 9/8)`.

Convention: `t = x^{-1}`; `δ = min ord_t(τ_i − τ_j)` (Prop 5.1). Φ is
Def 5.1(3) on the descended characteristic data, converted from the
Jacobian-normalized parameter to that `t` by the factor `k+1`. Not a
reindexing, not `δ_i' = δ_{i+1}`, not `v_s − u_s δ_old`.

When the actual descended tower has `s' ≠ 2`, Φ-as-`s'=2` is a
*truncation* to `(M_2', V_2')`. The compiler records it, and does **not**
feed it to the `s = 2` shape (that would make `u' = d_2' − V_2'`
negative on typical `s' ≥ 3` rows). Generalized Def 5.1(3) on the real
`s'` tower is attempted separately; it hits a vanishing denominator on
a majority of the excess (§5.2).

### 2.3 (8)–(13) on the descended tower; what `s' = 2` means

p.201 `SOURCE-READ`: (8) defines `A_{r-1}` from `δ_{r-1}` and
`lcm(den δ_s, …, den δ_r)`; (9)(10)(11) constrain `V_{r-1}` for
`r = s, …, 3`; (12)/(13) is the separate bottom (`r = 2`) condition.

At `s' = 2`:

- (8) is used to form `A_1'` from the Φ radii:
  `L = den(δ_2')`, `A_1' = den(L · δ_1')`.
- (10)/(11) are **vacuous** (`j` runs through the empty range
  `s-1, …, 2`).
- **Only (12)/(13) is active.**

This is not an inference from a validator: it is the same loop as
`Skel.full_ok` / `Skel.cond1011` in the charged skeleton.

Φ-`(12)/(13)` on Moh's five, all pass:

```text
  (16,12) V2=3   A1=4  (12)  n*=4 m*=3
  (21,14) V2=2   A1=3  (12)  n*=3 m*=2
  (21,14) V2=5   A1=3  (12)
  (15,10) V2=3   A1=2  (13)
  (15,10) V2=2   A1=3  (12)
```

The p.188 identity `A_1 | (n*+m*)V_2 − 1` holds on these five.

At `s' ≥ 3`, (10)/(11) at `j = s'-1, …, 2` *would* be active, but only
after radii of the full descended `V`-path are defined. That is blocked
on `OPEN[DEF51-MONOMIAL-MS-NMINUS2]` for 38 of the 52 excess rows.

### 2.4 SHAPE: the general rule

Parameters of an `s' = 2` descended pair: `K' = gcd(n', m') = deg_y h`,
`d' = m'/K'`, `e' = n'/K'`, `d_2' = K'` on every row in this run,
`u' = d_2' − V_2'`, `v' = V_2'`, `δ_1', δ_2'` from Φ,
`deg_x h = u'`, `deg_x f = u' d'`, `deg_x g = u' e'`.

**D1 order** (p.208 `ord h(σ) ≥ −δ_1` at `σ = π t^{δ_1}`, `x = t^{-1}`):

```text
  val(x^i y^j) = −i + δ_1 j
  h:    i ≤ δ_1 (j+1),   i+j ≤ K,   i ≤ u',   j ≤ K
  β:    i ≤ δ_1 (j+d'),  i+j ≤ m',  i ≤ deg_x f,  j ≤ K−1
```

**Leading-form fix, only when `δ_2' = −1`** (two points at infinity;
Lemma 5.3 for constant `J`, and the monomial analogue
`δ_s = −(k+1)/(n−M_s−1) = −1` when `n−M_s−1 = k+1`):

```text
  u' = 1:  y^{V_2}(y − x)                         # (16,12)
  u' = 2:  y^{V_2}(y^2 − x^2)                     # (15,10) V2=3; p.210 three subdiscs
  u' ≥ 3:  y^{V_2}(y − x)^{u'}                    # (15,10) V2=2: y^2(y−x)^3
```

The `u' = 2` split into two complementary linear factors is Moh p.210
`SOURCE-READ`: *“the inverse transformation implies that there is a
minor disc. Thus in the major disc `D_2` there are precisely three
subdiscs which contains 2, 2, 6 of roots `f`.”* The compiler applies
that split to every Prop 6.3 descendant with `u' = 2` and `δ_2' = −1`.
Degree-`K` monomials not in the leading support are set to 0 (this is
what kills `x y^4` in (15,10) `V_2 = 3`, which D1 alone would allow).
Remaining free `h`-monomials are the D1-lower terms (`tot < K`).

**A,B form of `β`, only when `δ_2' = −1` and `d' = 2`.** Horner:
`h = y A + const`. Then `β = p A + q y + r x + s` (Moh (6); four
parameters). This is the forced form Moh computes with, not a slice.
When `δ_2' > −1` (one point at infinity) the `(y−x)` Horner is the
*wrong* shape (descent-radii G2 warning); the compiler emits the full
D1 monomial count and does not A,B-reduce.

**Unknown counts emitted:**

- `n_ord = #h_free + #β_D1 + 1` (`c`).  G2: 14+27+1 = **42**.
- `n_ab  = #h_free + 4 + 1` when two-point `d' = 2`.  (15,10) `V_2=3`:
  8+4+1 = 13; Moh computes with 12 (`c` not counted, or absorbed).

`g = h^{e'} + G_{e'−2} h^{e'−2} + …` with `G_{e'−1} = 0`. For `d' = 2`,
`e' = 3` the approximate-root expansion sets `G_1 = 3β`,
`G_0 = (3/2)α` (`β^2 = α h + γ`). Those `G_i` are not extra unknowns
at stage 2. Stage 1 (before the `η`-reduction) is Moh's 22 [15 or 13]
and 17.

### 2.5 Gate on Moh's printed shapes and counts

```text
  (15,10) V2=3 h lower == (5):  y^4, x y^3, y^3, x y^2, y^2, x y, y, 1     MATCH
           leading y^5 − x^2 y^3, no x y^4                                   MATCH
           n_h + n_beta = 8+14 = 22                                          MATCH
           n_ab = 13 (8+4+c); Moh computes 12                                MATCH shape
  (15,10) V2=2 n_h = 11; n_h+4 = 15  [Moh's bracket 15 or 13]                MATCH 15
  (16,12) h lower == (1):  y^3, y^2, y, 1   (no leftover x)                  MATCH
           A,B inventory 4+1+2+2+3+3+3 = 18; Moh prints 17 (α1 absorbed)    MATCH 17
           η-reduction 17 → 10  SOURCE-READ p.209                            MATCH 10
  G2       n_h=14, n_beta=27, n_ord=42, δ2'≠−1 so no A,B                     MATCH charged
  G3       n_ord=66 > 30                                                     COUNTING-BOUND
```

The “13” of Moh's bracket 15 or 13 is not reproduced as a second
forced count; 15 is. Typed: the 13 is OPEN as an alternate further cut
(translations, or a tighter `β`), not used to kill or save a row.

### 2.6 The emitted polynomial system

For two-point `d' = 2`, `e' = 3` (the (15,10) family and (21,14) `V_2=5`):

```text
  h     = leading form + sum_{D1-lower} a_{ij} x^i y^j     (monic in y)
  β     = p A + q y + r x + s,   A = (h − h|_{y=0})/y
  f     = h^2 + 2 β
  α     = quot_y(β^2, h)
  g     = h^3 + 3 β h + (3/2) α
  J(f,g) − c x^k  = 0     as a polynomial in (x,y)
  saturate T c − 1        (c ≠ 0); ring Q[a_{ij}, p,q,r,s, c, T], grevlex
```

Lemma 2.1 for a monomial Jacobian is equivalent to `J = c x^k`
(charged m2-descent §4.3, SOURCE-CHECKED on Moh's `η^9` term of
`x`-degree 3 = `k+1`). The `M_2'` vanishing pattern is not imposed as
extra equations on these in-budget systems: emptiness at `c ≠ 0`
already kills them. Unit leader of `h` is 1 (monic, fixed).

For (16,12): `d' = 3`, `e' = 4`, Moh p.208 (1)–(5) with `α_1 = 0`
(the absorption that turns 18 into 17), `J = c x`, 4+13+`c` = 18
unknowns.

If `#unknowns > 30`: emit the count and stop (**COUNTING-BOUND**).

## 3. Task (2) — SOLVE; controls

### 3.1 Negative control: (15,10; 11; 3) must be SATURATED-EMPTY

Byte-faithful subprocess replay of the charged
`moh_1510_control2.py` and `moh_1510_controls_pm.py` (2.9 s):

```text
  printed alpha = a9^2 B + 2 a9 a10 reproduced : True
  printed  (B-coeff −a9^2 a10) : gamma reproduced = False
  audited  (B-coeff −a9^2 a8 ) : gamma reproduced = True
  Case 1 a9=0 : deg_y β^3 < 5  CONTRADICTION  reproduced
  Case 2 : 5 eqs c2−3γ ∈ k, saturate T a9−1, lex, Q[a1..a12,T] : EMPTY [1]
  MAIN     : saturate all 5 at a9!=0 -> EMPTY  [1]
  POSITIVE : drop (2,0),(1,1),(0,2) -> NON-TRIVIAL; drop (1,0),(0,1) -> EMPTY
  NEGATIVE : a9=1, a10=2, a11=3 -> NON-TRIVIAL
```

**SATURATED-EMPTY.** Ring, order, Rabinowitsch generator, and both
controls declared. Emptiness is of the `a_9 ≠ 0` component, not a
wrapper artefact. `ERRATUM[APPII-GAMMA-B]` confirmed (not re-opened).

This gate passed **before** any new row was solved.

### 3.2 Positive control: planted descended automorphism

Charged autoscan2 population (seed 7717, 25 pairs, table in the charged
m2-descent report). Prop 6.3 needs `δ_s = −1`, which for constant
Jacobian is `M_s = n−2` (Lemma 5.1). **0 of 25** have `M_s = n−2`.
`V_s` is not in the `η`-expansion; `u_s` is not invented.

**Planted: NONE.** The SURVIVES branch of the solver is uncalibrated.
The SATURATED-EMPTY branch is calibrated by §3.1 and by the unsaturated
/ negative controls on the Jacobian systems of §3.3.

(The twelve `M_2 ≤ m` witnesses were already known to fail (4); this
lane adds that the thirteen `M_2 > m` pairs in the same scan also fail
`M_s = n−2`.)

### 3.3 Every in-budget emitted system

Desk: one core, per-system cap 180 s via a killable subprocess
(`solve_worker.py`). Gröbner over `Q`, grevlex, `T c − 1`. Unsaturated
basis of the same equations (no Rabinowitsch) and a toy `c = 1` system
in the same ring are the FALLACY-v2 controls.

```text
  (64,48) -> (16,12; X)     18 unk, 77 eqs
      MAIN c!=0 : EMPTY [1]     13 s (J only); 144 s with unsaturated GB
      UNSATURATED : NON-TRIVIAL (258 gens)   c=0 lives
      NEGATIVE    : toy c=1, Tc-1 NON-TRIVIAL
      verdict SATURATED-EMPTY
  (84,56) V2=2 -> (21,14; X; δ2'=-1/2)
      n_ord=68 > 30   COUNTING-BOUND   (one-point-at-infinity; not two-point)
  (84,56) V2=5 -> (21,14; X; δ2'=-1)    16 unk, 40 eqs, 16 s
      MAIN EMPTY [1]; unsat NON-TRIVIAL; neg NON-TRIVIAL
      verdict SATURATED-EMPTY
  (75,50) V2=3 -> (15,10; X^2)          12 unk (control2), 3 s
      verdict SATURATED-EMPTY   (calibration)
  (75,50) V2=2 -> (15,10; X^2; δ2'=-1)  16 unk, 48 eqs, 41 s
      MAIN EMPTY [1]; unsat NON-TRIVIAL; neg NON-TRIVIAL
      verdict SATURATED-EMPTY
  (99,66)  US-GT-1
```

No SURVIVES. No TIMEOUT. No COUNTING-BOUND among two-point in-budget
rows.

(16,12) was solved as the p.208 A,B system (17 printed + `c`), not as
the further `η`-reduced 10. Emptiness of the 18-unknown system is
stronger than emptiness of a 10-unknown specialisation.

## 4. Task (3) — run sets and totals

### 4.1 Moh's six (calibration)

Already §3.3. Summary: 4 SATURATED-EMPTY, 1 COUNTING-BOUND
((21,14) `V_2=2`), 1 `US-GT-1`. Fail-closed: the printed (15,10)
`V_2=3` kill is reproduced before the other three Jacobian kills are
trusted.

### 4.2 The 52 C_FULL_TREE_ODE excess rows at `n ≤ 100`

Keys: frozen `full-tree-ode-excess-witnesses.json` (52 entries).
**All 52 have `u_s = 1`.** Parent `s ∈ {4,5}`, so one Prop 6.3 step
gives `s' ∈ {3,4}` (37 at `s'=3`, 15 at `s'=4`).

The Appendix-II shape is an `s' = 2` machine (Moh pp.207–211; charged
normal form with one `M_2'`). Applying `u' = d_2' − V_2'` at `s' ≥ 3`
makes `u'` negative on typical rows (`V_2` is a lower-level
multiplicity, not the top form). The compiler **does not** emit a
coefficient system for those rows.

```text
  u_s = 1                         52 / 52
  verdict S-PRIME-GT-2            52 / 52
  coefficient-level SATURATED-EMPTY    0
  SURVIVES (positive-dimensional)      0
  COUNTING-BOUND (s'=2, >30 unk)       0
  out of the s'=2 Appendix-II budget  52
```

Generalized Def 5.1(3)·`(k+1)` on the *actual* `s'` tower:

```text
  n' − M_{s'} − 1 = 0     38 / 52     OPEN[DEF51-MONOMIAL-MS-NMINUS2]
  denominator defined     14 / 52     (10)/(11) and (12)/(13) evaluated;
                                      none failed  ->  stayed S-PRIME-GT-2
  second descent u_{s'}=1  1 / 52     (96,72; M=(36,78,94); V2=1,V3=1,V4=5)
                                      first step -> (16,12) M2'=6 V2'=1 k=3 s'=3
                                      d_3'=2, V_3'=1, u'=1
```

The 38 vanishing denominators are not a bug in Φ-as-`s'=2` (that uses
`M_2'`, and `n' − M_2' − 1 ≠ 0`). They say: after dropping `M_s = n−2`,
the new top exponent `M_{s−1}'` often equals `n' − 2`, so the constant-`J`
formula `δ_s = −1/(n−M_s−1)` and the monomial formula
`δ_s = −(k+1)/(n−M_s−1)` are both singular. Typed OPEN, not filled by
setting `δ_{s'} = −1` by analogy with Lemma 5.1.

**How many of the 52 die by the compiler (a coefficient-level kill
beyond the tree)? 0.** The tree already kept them; the compiler does
not produce an `s' = 2` system to kill. This is a typed gap, not a
silent pass.

### 4.3 D = 108 screened survivors with `u_s = 1`

`candidate-results.json` `C_FULL_TREE` at D = 108: 21 V-assignments,
13 groups, 8 pinned. Re-enumeration via charged
`full_tree_partition.full_tree_ok` + `census(108, Kmin=16, full=True)`:
21 C_FULL_TREE rows, **19 with `u_s = 1`**. All 19 have parent `s = 4`,
`s' = 3`. Verdict **S-PRIME-GT-2** on 19/19. `n' − M_{s'} − 1 = 0` on
12/19. Second-descent `u_{s'} = 1` on 2/19.

ODE at D = 108 is 20 V-assignments / 19 `u_s = 1` (one ODE kill among
the 21); the 19 `u_s = 1` C_FULL_TREE rows are the run set named by
the charge.

No coefficient system, no SATURATED-EMPTY, no SURVIVES, no
COUNTING-BOUND at `s' = 2`.

### 4.4 D = 105 G2/G3 cross-check

```text
  G2 (15,10; X^4; M2'=4, V2'=1, d2'=5; δ2'=-1/2, δ1'=5/4)
      n_h=14  n_beta=27  n_ord=42   COUNTING-BOUND
      two_point=False  (δ2' > −1; one point at infinity)
      shape rule AGREES with the charged descent-radii 42
  G3 (21,14; X^2; M2'=8, V2'=1, d2'=7; δ2'=-1/4, δ1'=9/8)
      n_ord=66   COUNTING-BOUND
  G1 u_s=2   US-GT-1   (OPEN[MINOR-DICHOTOMY], untouched)
```

A,B reduction is *not* applied to G2 (wrong shape). The Newton-tight
12-unknown slice of the charged descent-radii lane is a slice, not
emitted here as a kill of G2.

### 4.5 Totals (the 52)

| bucket | n |
|---|---:|
| `u_s = 1` | 52 |
| coefficient-level kill (SATURATED-EMPTY) | **0** |
| SURVIVES (positive-dimensional family) | **0** |
| COUNTING-BOUND (`s'=2`, >30 unknowns) | **0** |
| S-PRIME-GT-2 (out of Appendix-II `s'=2` budget) | **52** |

Moh calibration (not part of the 52): 4 coefficient kills, 1
COUNTING-BOUND, 1 `US-GT-1`. D = 108 `u_s = 1`: 19 S-PRIME-GT-2.

## 5. Task (4) — reading: uniform kill? candidate (T)? cheapest next

### 5.1 Is the kill uniform?

On the *two-point* class (`δ_2' = −1`, in-budget): **yes, at the
Jacobian**. Four independent systems, four rings, four empty `c ≠ 0`
components. Unsaturated non-triviality (where computed) says `c = 0`
still lives, so the kill is exactly the monomial-Jacobian condition,
not “no polynomials of this shape exist at all.”

It is **not** always Moh's `c_2 − 3γ` `h`-adic component. That
computation is special to (15,10) `V_2 = 3` and the `η`-expansion
(3)–(4) of pp.210–211. The compiler's uniform test on (15,10) `V_2 = 2`,
(21,14) `V_2 = 5`, and (16,12) is `J(f,g) − c x^k = 0` as a polynomial.
Those three have different `(n', m', k, u')` and different leading
forms (`y^2(y−x)^3`, `y^5(y^2−x^2)`, `y^3(y−x)`). The common pattern
is: two-point + D1 + A,B (or the p.208 `α,β` inventory) + `c ≠ 0` is
empty.

The non-two-point Moh row (21,14) `V_2 = 2` and G2/G3 are a different
class (`δ_2' > −1`, one point at infinity) and sit at COUNTING-BOUND.
No uniform kill is claimed for that class. A G2 Newton-tight slice
emptying (charged descent-radii) is a slice.

**Candidate (T)-shape, MEASURED on the calibration set, not a theorem:**

> There is no pair `f, g ∈ k[x,y]`, monic in `y`, of the D1+leading+A,B
> shape forced by a Prop 6.3-descended two-point datum
> `(n', m', M_2', V_2', k)` with `δ_2' = −1`, such that
> `J_{x,y}(f,g) = c x^k` with `c ≠ 0`.

This is the two-point specialisation of charged (T) (m2-descent §5).
It is verified on every two-point Moh descendant that fits in 30
unknowns (4 rows). It is not verified on any of the 52 excess rows
(wrong `s'`). It is not a source theorem Moh states for general
`(n', m', k)`.

### 5.2 OPENs, bounded quantity, cheapest test

**`OPEN[S-PRIME-GT-2]`** (new). Appendix-II SHAPE and the `s' = 2`
Jacobian system do not apply after one Prop 6.3 step when the parent
has `s ≥ 4`. Bounded: 52 excess + 19 D = 108 `u_s = 1`. Cheapest test:
the unique excess row with `u_{s'} = 1`,
`(96, 72, M = (36, 78, 94), V = {2:1, 3:1, 4:5})`. First descent:
`(16, 12)`, `M_2' = 6`, `V_2' = 1`, `k = 3`, `s' = 3`, `d_3' = 2`,
`V_3' = 1`. A second Prop 6.3 step is formally available; the composed
Jacobian exponent is **not** `k_1 + k_2` by any source identity this
lane owns (`k_2 = V_3' − 1 − 1 = −1` is a warning, not a value). Desk:
one more descent_once plus Φ if the Jacobian can be named. Do not fill
the Jacobian by cap or analogy. Typed OPEN.

**`OPEN[DEF51-MONOMIAL-MS-NMINUS2]`** (new). Def 5.1(3) has denominator
`n − M_s − 1`. After descent this vanishes on 38/52 excess and 12/19
D = 108 `u_s = 1` (`M_{s'} = n' − 2` with `k > 0`). Lemma 5.1's
`δ_s = −1` is for *constant* Jacobian. The monomial rule
`δ_s = −(k+1)/(n−M_s−1)` is singular at the same place. Cheapest test:
one such row, measure `δ` numerically on a random pair with
`J = c x^k` and `M_s = n−2` (the descent-radii two-point-fit engine
already exists). If the measurement is `−(k+1)` or `−1` or neither,
that names the rule or keeps OPEN. Desk: the charged `measure_numpy.py`
path, one pair, minutes.

**`OPEN[PLANTED-AUTO]`** (charged residual, confirmed). No autoscan2
pair has `M_s = n−2`, so no planted descended automorphism. The
SURVIVES branch remains uncalibrated. Cheapest test: enlarge the
elementary-composition scan until a pair with `M_s = n−2` appears, or
prove that Moh-gauge automorphisms never have `M_s = n−2`. The charged
n=4 witness has `M_s = 1 ≠ 2`. Not closed here.

**(21,14) `V_2 = 2` COUNTING-BOUND** (not an OPEN: a typed out-of-budget
row). 68 order-condition unknowns, `δ_2' = −1/2`, same class as G2.
Cheapest coefficient experiment in the whole residue: a Newton-tight
slice of this row (leading `y^7 + a x^{q} y^{r}` matching `δ_2' = −1/2`,
plus y-polynomial plus four-parameter `β`), saturate `J = c x` at
`c ≠ 0`. That is the G2-slice experiment already run by the
descent-radii lane, transplanted to the one remaining Moh `u_s = 1`
row. If the slice empties, it is a slice. If it SURVIVES, that is the
first positive signal and must be investigated (the SURVIVES branch
would then have a witness). Desk: 12–20 unknowns, the same 16 s class
as (21,14) `V_2 = 5`.

No `OPEN[MOH-PROGRAM]` sharpening is claimed. Fable's 28-row cut still
rests on the refuted `M_2 > m` theorem. The 52 excess remain after
C_FULL_TREE_ODE; this compiler does not cut them at coefficient level.

## 6. FALLACY-v2 check

- No cv-flag / physical-place / cover-series identification.
- No per-ray / exit-set charge. No `charge_basis` line.
- `REPRESENTATIVE` vs `FULL_ACTUAL_EXIT` does not arise.
- No pole identity. **Floor/attainment:** Φ is an equality matching 10
  printed rationals (not a floor). SATURATED-EMPTY is emptiness of a
  declared component, not a lower bound. S-PRIME-GT-2 is a classification,
  not “the pair does not exist.”
- **`sat()` wrapping:** control2 declares `Q[a_1..a_{12}, T]`, lex,
  `T a_9 − 1`, and both controls. Jacobian kills declare
  `Q[h_free, p,q,r,s, c, T]` or `Q[b_1..b_4, c_1..c_{13}, c, T]`,
  grevlex, `T c − 1`; unsaturated basis non-trivial; negative toy
  non-trivial. (16,12) unsaturated (258 gens) was computed in a
  follow-up worker after the main 77 s run, which had already returned
  MAIN EMPTY and negative non-trivial; the follow-up is recorded in
  `compile_out.json`.
- **Raw remainder degree:** control2 divisions are `sympy.div` in `y`
  by a polynomial monic in `y` (`h` monic, verified by the charged
  driver). Jacobian systems impose a polynomial identity, no remainder.
- **Variable/ring map:** Prop 6.3 `(γ, π)` vs Appendix II `(x, y)` and
  remainder-`γ` never identified. Generator order declared per system.
- **Prime label/derivative:** as §1.
- **Merge-free / target-arrival:** do not arise.
- Unconstrained leading forms that would not match printed `δ_1'` were
  not used. G2 A,B is not applied (`δ_2' > −1`). AUDIT 17(p) is not
  consumed. The 52 are not declared empty as Jacobian pairs.

## 7. Typed block

```text
LANE         appendix2-compiler-grok46-20260903 (Grok 4.6)
SOURCE       Moh 1983 pp.207-211 SOURCE-READ; charged descent, Φ, control2
GATE         hashes 13/13; p.207 5/5 u_s=1 signatures; Φ 10/10;
             shapes (5)-(6) and p.208 (1) MATCH; 22 and 15 MATCH;
             17->10 SOURCE-READ; G2 n_ord=42 MATCH; control2
             SATURATED-EMPTY + pos/neg PASS; planted NONE (0/25)
PROVED-HERE  s'=2 => (10)/(11) vacuous, only (12)/(13) active
PROVED-HERE  SHAPE: D1 order i<=δ1(j+1) (h) and i<=δ1(j+d') (β);
             leading fix iff δ2'=-1; A,B β iff δ2'=-1 and d'=2
PROVED-HERE  two-point in-budget Moh descendants SATURATED-EMPTY at
             J=c x^k, c!=0: (16,12), (21,14)V2=5, (15,10)V2=3,
             (15,10)V2=2.  Unsaturated non-trivial where computed.
MEASURED     52/52 excess u_s=1 and s'∈{3,4}: S-PRIME-GT-2.
             Coefficient kills of the 52: 0.  SURVIVES: 0.
             COUNTING-BOUND at s'=2: 0.  D=108 us1: 19, all S-PRIME-GT-2.
             G2 COUNTING-BOUND 42 (agrees). G3 COUNTING-BOUND 66.
NOT CLAIMED  any coefficient kill of the 52 or of D=108; any SURVIVES;
             any kill of G2/G3 as a whole; any sharpening of
             OPEN[MOH-PROGRAM]; (T) as a theorem
OPEN         OPEN[S-PRIME-GT-2] (52+19); OPEN[DEF51-MONOMIAL-MS-NMINUS2]
             (38/52, 12/19); OPEN[PLANTED-AUTO] (SURVIVES uncalibrated)
NEXT         Newton-tight slice of (21,14) V2=2 (the remaining Moh
             u_s=1 row, same class as G2); or measure δ on one
             descended pair with M_s'=n'-2 and J=c x^k
```

## 8. Drivers

```text
box/appendix2/compile.py          main: descend, Φ, (8)-(13), shape, run sets
box/appendix2/shape.py            Φ, D1 monomials, leading split, Moh gates
box/appendix2/descent_core.py     one-step Prop 6.3 (no gates.py import)
box/appendix2/solve.py            control2 replay, J-systems, planted parse
box/appendix2/solve_worker.py     killable Gröbner subprocess
box/appendix2/test_replay.py      python3 -O replay; require()+assert scan
box/appendix2/compile_out.json    machine-readable totals
```

Reproduce:

```text
  python3 -O box/appendix2/test_replay.py
  python3 -u box/appendix2/compile.py
```

Wall: compile.py 77 s one core (control2 3 s; three Jacobian systems
13+16+41 s; 52+19 classification < 1 s). Follow-up (16,12) unsaturated
Gröbner 144 s, recorded in `compile_out.json`. Peak RAM well under
6 GB. Per-system cap 180 s; no TIMEOUT fired.

Page images not kept. Journal page N = PDF page N−139.

## COLLISIONS

status: EMPTY

- `OPEN[S-PRIME-GT-2]` (this report: raised): NONE
- `OPEN[DEF51-MONOMIAL-MS-NMINUS2]` (this report: raised): NONE

<!-- BODY-END -->
