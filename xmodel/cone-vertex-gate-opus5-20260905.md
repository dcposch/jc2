# Hostile gate on the cone-vertex theorem: the Jacobian identity is exact, the
# consistency reruns reproduce, and the engines carry a leading-row defect

Opus 5 · 2026-09-05 · lane `cone-vertex-gate-opus5-20260905` · basis `148ae18a`

**Disposition: `CONFIRMED-WITH-FIX`.** Every load-bearing claim of the charged
report re-derives independently on the engine code as built, with negative
controls: the Jacobian identity on `Δ` is an exact algebraic cancellation
(not a truncation artifact), the outer `D1` rows cannot reach the four
constants at *any* offset, the `h2`-only pole systems reproduce Fable's row and
pivot counts to the unit (129 / 102 / 0 at D=108 with a witness verified
by direct substitution into the raw rows; 105 / 76 / 0 at (99,66) δ=2;
130 / 94 / 0 at δ=5/2), the historical Δ-subsystems return the literal constants `a_4 = 8`
and `a_8 = 8` on both old engines and *nothing* on the corrected one, and the
localizers `c ≠ 0`, `Hc_5_3 ≠ 0` are satisfied on `Δ`. `T_0 = n+m−2` stands.
**The fix is material and is a defect the gate found in the engines, not in the
theorem:** `raw_minor_support` emits the *leading* pole power (`n = 96`/`64` at
D=108, `81`/`54` at (99,66) δ=2, `189`/`126` at δ=5/2) as a homogeneous
`coefficient = 0` row with no target subtraction, and that row is unsatisfiable
on the *whole* chart — reduced, it is literally `1 = 0` (the `π^8` coefficient
of the forced target `(π²−c)^4`). So the engines as coded would return a
spurious `UNIT` at stage 92 / 60 (D=108) and 77 / 50 ((99,66) δ=2), far below
`T_0`. Fable's `R_T` is the corrected row set ("including the leading targets
when `T_p` reaches them") and the theorem is true of it; the emitted row set
must be repaired before any deep run, or the retirement claim will be
contradicted by an artifact of exactly the kind it was written to explain.
Two further scope fixes are recorded in §7.

No ledger was edited; no `jc2-lean`; no `ideation-*`. No new exit-price
assertion is made, so no FALLACY-v2 `charge_basis=` line applies.

## 0. Custody

The manifest was built mechanically from the numbered `_basename`/`_sha256`
fields of `xmodel/cone-vertex-gate-opus5-20260905.run.v2` with `awk`, prefixed
by `lane_inputs_dir`; `sha256sum -c` returned `OK` on all six frozen inputs, no
content mismatch (`box/cone-vertex-gate-20260905/manifest.sha256`,
`manifest.check`). The engines were imported read-only from
`box/d108-rekill-20260905/work/rekill_engine.py`,
`box/g9966-repair-gate-20260905/corrected_face_engine.py`,
`box/g9966-d2-precise-20260905/band_engine.py`, and the charged
`/tmp/jc2-lane.zr6VVM/inputs/band_engine.py`. **No artifact of
`box/joint-degenerate-20260905/` was read or executed**: every number below is
produced by my own drivers `cvg_t1..cvg_t8` in
`box/cone-vertex-gate-20260905/`, and agreement with the charged report is
therefore independent reproduction, not transcription. Everything ran locally
in SymPy over `Q`; no fleet worker, no modular result, no Singular call.

## 1. Ring map and the exact identity (gate item 1, first half)

Declared once, verbatim from the code: `t = 1/x`, `w = ty`, `z = w−1`,
`K2 = t^{d} h2(1/t,(1+z)/t)` with `d = deg h2` (36 at D=108, 33 at (99,66)),
and (`rekill_engine.py:385-392`, `corrected_face_engine.py:467-476`)

```text
   KF = K2^3 + t·KA2·K2 + t·KA3 ,    KG = K2^2 + t·KB1·K2 + t·KB2
   KJ = n·KF·(KG)_z − t(KF)_t·(KG)_z − m·(KF)_z·KG + (KF)_z·t(KG)_t
```

The explicit `t` is `outer_effective_tz`, which shifts `(r,q) → (r+1,q)`.
Block degrees are `nF−d−1, nF−1, nG−d−1, nG−1` (`outer_specs`,
`OUTER_SPECS`): 71, 107, 35, 71 at D=108 and 65, 98, 32, 65 at (99,66). A block
constant `a_{00}` of a degree-`D` block sits at `t^D z^0` in that block's `K`,
because `t^D A(1/t,(1+z)/t) = Σ a_{ij} t^{D−i−j}(1+z)^j`, hence at `t^{D+1}`
after the shift. So on `Δ`, writing `u := K2`,

```text
   D=108 :  KF = u^3 + b t^72 u + c' t^108 ,  KG = u^2 + d t^36 u + e t^72
   (99,66):  KF = u^3 + b t^66 u + c' t^99  ,  KG = u^2 + d t^33 u + e t^66
```

Grouping `KJ = (KG)_z[n·KF − t(KF)_t] + (KF)_z[t(KG)_t − m·KG]` and using
`n = 3d`, `m = 2d`:

```text
   n·KF − t(KF)_t   =  (3u^2 + b t^{2d})·(d·u − t u_t)
   t(KG)_t − m·KG   = −(2u + d t^{d})·(d·u − t u_t)
   (KF)_z = (3u^2 + b t^{2d})u_z ,   (KG)_z = (2u + d t^{d})u_z
   ⇒ KJ ≡ 0 .
```

The cancellation is exact and needs no truncation: it is forced by `2n = 3m`
(216 = 216; 198 = 198) **together with** the block degrees being exactly
`nF−d−1, nF−1, nG−d−1, nG−1`, which is what puts `b` at `t^{2d}` and `d` at
`t^{d}`. Both facts are properties of the chart as built, not assumptions.

Mechanical check with the engines' own `build_FG` and `jacobian_band`
(`cvg_t2_identity.py`, 9.8 s, `t2_identity.json`): with the four constants
symbolic and `K2` generic, the constants land at `t`-powers `KF: 72, 108` and
`KG: 36, 72` (D=108) and `66, 99 / 33, 66` ((99,66)) — exactly as derived — and
**every probed Jacobian band is identically zero**, at `tp = 1,2,3,7`, at
`d−1..d+2`, at `2d`, at `nG−d..nG+2` and at `nF..nF+2` (up to `t^110` / `t^101`,
i.e. past all four constant sites). Two negative controls fire, so the test has
power: switching on **one** extra outer coordinate off `Δ` makes bands `1..6`
nonzero, and pairing the wrong degree (`m → m−1`) makes bands `1..6` nonzero on
the same `Δ`.

## 2. `Δ` on the chart as built, and the localizers (gate item 1, second half)

`cvg_t1_d108.py` (109 s, `t1_d108.json`) rebuilds the D=108 δ=3 saturated
`T = 8` system exactly as `step4_saturated.py` does and evaluates **all 1420
rows** with every outer coordinate set to zero:

```text
   h3 incidence residual rows            0        (empty at the corrected radius)
   resolved outer entries that are not homogeneous-linear-in-outer   0 / 0 / 0
   F pole rows  12  → all identically 0        (K2^3 has no band below t^9)
   G pole rows  12  → 3 nonzero, all h2/h3-only
   Jacobian rows 1396 → ALL identically 0
   KF|Δ == K2^3 : True
```

The three survivors are `G_local6_coord0 = (K2c_3_26 + 8·jet2)^2`,
`G_local7_coord0`, `G_local8_coord0` — polynomials in `K2c`, `Hc_5_4`, `jet1`,
`jet2` with **no outer coordinate**. This is exactly Fable's (ii) verified on
the chart: `Δ` alone does not satisfy the system; `Δ` cut by the `h2`-only rows
does. The theorem is correctly stated about `Δ_T`, and I record that the raw
coordinate subspace `Δ` is *not* a solution locus — a reader who takes the
headline "`Δ` satisfies every row" literally will be wrong on three rows at
`T = 8` alone.

**The four constants are permanently free, and for a stronger reason than the
report gives.** Fable checks that the constants are free symbols at the run
depth and notes only that the `B1` offset-4 band is empty. In fact the number
of `D1` rows in a block's weight-`W` band is `max(0, threshold − d1_mult·W)`,
and at the constants' own positions this is negative in all eight cases:

```text
   D=108   A2 (71,0) W=284 2W=568 thr=566 → 0 rows      offset 8
           A3 (107,0) W=428 2W=856 thr=853 → 0 rows     offset 12
           B1 (35,0)  W=140 2W=280 thr=279 → 0 rows     offset 4
           B2 (71,0)  W=284 2W=568 thr=566 → 0 rows     offset 8
   (99,66) A2 (65,0) W=195 3W=585 thr=583 → 0           A3 (98,0) 294/882/879 → 0
           B1 (32,0) W=96  3W=288 thr=287 → 0           B2 (65,0) 195/585/583 → 0
```

Since `outer_state` builds each `D1` row from positions of one block at one
weight, a constant can appear in no row at all, at any `max_offset`. So the
`b, c', d, e` directions survive arbitrarily deep outer accounting; Fable's
depth-limited evidence supports a depth-independent fact.

**Localizers.** `c ≠ 0` is the sole declared localization (`Zc·c − 1`); `ρ ≠ 0`
is its (99,66) δ=2 analogue; `D2`-minimality `Hc_5_3 ≠ 0` is a property the
rekill report checks at its point, not an imposed row. All are `h3`/minor-level
data, untouched by the outer coordinates, so `Δ` does not constrain them. At my
own witness (§3) `cvg_t6_localizers.py` returns `c = 1` and **`Hc_5_3 = 2`**,
and the `K3` `D2` face `π³(4π⁴ − 7)/4` — five distinct roots, `D2`-minimal,
with the `π³ × poly(π⁴)` Galois shape that `A_2 = 4` forces. `Δ` is in the
chart.

## 3. Where the constants enter (gate item 2)

Recomputed from the sites of §1 and the tag schedules
(`raw_minor_support`, verified by direct enumeration):

```text
  chart              b·h2(σ)      d·h2(σ)      c'       e      F target   G target
  D=108 δ=3          72+32 = 104  36+32 =  68  108      72        96        64
  (99,66) δ=2        66+27 =  93  33+27 =  60   99      66        81        54
  (99,66) δ=5/2 (τ) 132+63 = 195  66+63 = 129  198     132       189       126
```

Every entry point is strictly above its target, reproducing the charged
numbers exactly. The mechanism deserves one sentence of precision the report
omits: the `b`-contribution to `[t^n]KF(σ)` is `b·a_{n−72}`, which vanishes for
`n ≤ 96` **because `a_p = 0` for `p < 32` is imposed**, not because of any
degree bound. So the correct statement is the inclusion
`Δ_T ⊆ V(R_T)` — which is the only direction the theorem needs — and not an
equality of loci.

## 4. The `h2`-only systems, rerun (gate item 3)

`cvg_t3_d108_depth.py` (184 s, `t3_d108_depth.json`) rebuilds the corrected
D=108 chart, imposes `a_p = 0` for `p = 1..31` and `a_32 = (π²−c)^4` (the
target derived independently from `K3(σ) = −t^8(π²−c)+O(t^9)` and `K2 = K3^4 +
t^36·(lower tower)`), and `Q*`-reduces on the `K2c`/`Hc` coordinates only:

```text
   D=108 δ=3   rows 129   Q* pivots 102   dependent-zero 27   RESIDUAL 0
```

identical to the charged `129 / 102 / 27 / empty`. The **witness** is then
built by setting the 16 surviving free coordinates to `0`, `jet1 = jet2 = c = 1`,
resolving the pivots, and substituting into the *raw* local rows — never
through the elimination:

```text
   a_p = 0 for every p < 32 :  0 violations
   a_32 = (pi−1)^4 (pi+1)^4  =  (pi^2−1)^4  =  target at c = 1     MATCH
```

Since `ord_t K2(σ) = 32` exactly, `ord KF(σ) = 96` with leading `a_32^3 =
(π²−1)^12` and `ord KG(σ) = 64` with `a_32^2 = (π²−1)^8`: **all 1200 F and 544
G pole rows of the whole chart are then satisfied by pure algebra**, not by
spot check, because `K2` has `r ≤ 36` and the series is complete. The witness'
`K3` `D2` face is `π³(4π⁴−7)/4` and its `K2` `D2` face is `(π⁴−1)^7` on the
sites `(5k, 28−4k)` (my §2 print truncates the `k=7` site at `r=35` because
that run built `K2` only to `max_t = 32`).

`cvg_t5_g9966_depth.py` does the same on the corrected (99,66) engine, with the
leading target computed independently by cubing the `K3` minor lead:

```text
   K3 lead at t^9   =  zeta^2 (zeta + 3 rho)        rows strictly below the lead: 0
   K3 lead at tau^21 = -zeta (c − zeta^2)           rows strictly below the lead: 0
   δ=2   rows 105 (100 nonzero)  Q* pivots 76  dependent-zero 29  RESIDUAL 0  (359 s)
   δ=5/2 rows 130 (120 nonzero)  Q* pivots 94  dependent-zero 36  RESIDUAL 0  (1608 s)
```

All three pivot counts — `102`, `76`, `94` — and all three empty residuals
reproduce the charged numbers to the unit, and the two `K3` leading forms are
the charged targets with nothing below them. Gate item (3) is confirmed on all
three corrected charts.

## 5. The historical units (gate item 4)

`cvg_t4_historical.py` (6.4 s, `t4_historical.json`) runs the Δ-subsystem —
`h2`-only pole rows to the depth of the reported kill stage, no Jacobian rows,
no outer coordinates, localizer excluded from the pivots — on each engine:

```text
   engine      branch    rows  pivots  residual   CONSTANT residual
   pristine    δ=2         1      0        1      a4_pi0 = 8
   pristine    δ=5/2       1      0        1      a8_pi0 = 8
   precise     δ=2         1      0        1      a4_pi0 = 8
   precise     δ=5/2       1      0        1      a8_pi0 = 8
   corrected   δ=2         0      0        0      —   (a_1..a_4 ≡ 0)
   corrected   δ=5/2       0      0        0      —   (a_1..a_8 ≡ 0)
```

Exactly the charged table, obtained without reading it. On both old charts the
Δ-subsystem is a *single nonzero constant row*, so `Δ_T = ∅` there and the old
units were forced before any Jacobian row was written; `8^2 = 64` is the
literal old δ=5/2 kill row `stage8_G_local16_coord0 = 64`, and the old δ=2 kill
`stage4_J_d159_k35 = 6264` is a Jacobian row, identically zero on `Δ`, so by
the contrapositive of Corollary (b) it can only be a transported form of the
same emptiness. That inference is sound as stated: `Δ_T ≠ ∅ ⇒ no unit`, hence
`unit ⇒ Δ_T = ∅`, independently of which row displays the constant.

## 6. The consequence, and the row the engines actually emit (gate item 5)

**`T_0 = n+m−2` is exact on the corrected row set.** The Jacobian schedule
puts degree `d` at `KJ` `t`-power `n+m−2−d` (`stage_spec`); the degree-0 row
sits at `t^178` (D=108) and `t^163` ((99,66)), and `w_powers = range(179−stage)`
collapses to the single slot `k = 0` there. No engine row of positive Jacobian
degree, no outer offset row and no `h3` incidence row excludes `Δ_T`, so `J_0 =
1` is the first and only exclusion. Both named candidates are absorbed rather
than refuting:

* **the `h3`-on-`D1` probe** is the row `2·jet1·jet2 + 1 = 0`; the frozen
  `h3D1-conditional-probe.json` shows it costs one dimension and leaves
  `reduce_1 = 1` at `T = 8` (stage 4: `14 → 13`; saturated: `7 → 6`). I took
  this further than the record, because a `T = 8` survival says nothing about
  full depth: `cvg_t9_probe_point.py` pins `jet1 = 1, jet2 = −1/2` into the
  `h3` chart *and* into the minor substitution and reruns the whole `h2`-only
  system to `p = 32` — **rows 130, pivots 102, residual 0**, with the all-free-
  zero point satisfying all 130 **raw** rows by direct substitution. So the
  probe cuts `Δ_T` without emptying it at any depth, and it is an `h3`-level,
  single-polynomial row, exactly the class Fable's criterion isolates.
* **the `K3` conjugacy constraints** are not extra rows at all: the `A_2 × V_2`
  face `(π^4−1)^7` at sites `(5k, 28−4k)` is *pinned into* `k2_face_sites()`,
  and the `π^j × poly(π^{A_2})` shape is a property my witness has. A new
  conjugacy row would again be `h3`-only, so it could break the theorem's
  proviso (the `h2`-only consistency) but never its Jacobian content.
* **the weight pull-forward.** 17(ppppppp)'s order-chart statement — every row
  of weight `< D` is `c`-free and satisfied by `z = 0, c = 1`, so the forcing
  threshold is `D` — is the same *shape* of argument but not the same number,
  and the two must not be identified: the order chart normalizes `J = c·x^ℓ`
  and its threshold is the weight carrying `c`; the band chart normalizes
  `J = 1` and its threshold is `t`-power `n+m−2`. Here the degenerate direction
  is a coordinate subspace with an exact algebraic cancellation, not a graded
  cone vertex — Fable says this and is right; the band rows are not
  weighted-homogeneous (the `K2` face carries the constant 1).

**The fix.** `raw_minor_support` includes the leading local power in its tag
set (verified by enumeration: `max n = 96` and `64` at D=108 with `k = 0..23`
and `0..15`; `81`/`54` at δ=2; `189`/`126` at δ=5/2), and both
`step4_saturated.py:44-46` and `step3_joint.py` / `cumulative_rows` emit it as
`rows.append((label, table.get((n,k), 0)))` — a homogeneous `= 0` row, with no
target subtraction anywhere in either engine. Under that literal reading `Δ`
would additionally need `a_32 = 0`. `cvg_t7_leadrow.py` decides it:

```text
   D=108,   a_p = 0 for p ≤ 32 : rows 129 pivots 102 residual 2  CONSTANT a32_pi8 = 1
   D=108,   a_p = 0 for p ≤ 33 : rows 137 pivots 109 residual 3  CONSTANT a32_pi8 = 1
   (99,66)  a_p = 0 for p ≤ 27 : rows 105 pivots  76 residual 4  CONSTANT a27_z9  = 1
            δ=2 residual in full:  a27_z6 = 27ρ³, a27_z7 = 27ρ², a27_z8 = 9ρ, a27_z9 = 1
```

The (99,66) residual is decisive twice over. Those four values are precisely
the `ζ`-coefficients of `(ζ²(ζ+3ρ))³ = ζ^6(ζ³ + 9ρζ² + 27ρ²ζ + 27ρ³)`, so the
corrected chart **forces** `a_27` to equal the charged target — Fable's leading
target is derived by the chart, not assumed by the analyst — and the emitted
`= 0` row therefore reduces to `1 = 0` with `ρ` still free. The same at D=108:
`[t^32 π^8] K2(σ) ≡ 1`, the `π^8` coefficient of `(π²−c)^4`, the top of the
`h3` tower, which no chart coordinate reaches. So the emitted leading row is
not merely unsatisfied on `Δ`; **it is unsatisfied at every point of the
chart**, and an engine run reaching stage 92 or 60 at D=108 (or 77 / 50 at
(99,66) δ=2) would report `UNIT` — a kill below `T_0`, and a spurious one of
exactly the species the theorem was written to diagnose. This does not refute
the theorem, because a row no point satisfies is no evidence about `Δ`; it does
mean the theorem is a statement about the corrected `R_T`, and that
`raw_minor_support`'s top tag must be given its target before any deep run.

I found no other row type, expressible in the band language, that is below
`T_0` and unsatisfied on `Δ_T`. Rows outside that language do exist — a
resultant or coprimality row separates `Δ` instantly, since `F = h2^3` and
`G = h2^2` share `h2` — but they involve the deepest outer coordinates and are
not a truncation of the band system, so they are new instruments, not cheaper
depths. I record that as a correction of emphasis to Fable's §6 ("only a
single-polynomial one"): a *joint* non-band row can also exclude `Δ`.

## 7. Scope fixes attached to the promotion

1. **Leading-row defect (material, engine).** As §6. The theorem holds for the
   corrected `R_T`; the emitted `R_T` contains an unsatisfiable row at the top
   pole tag on all three charts.
2. **`Δ` vs `Δ_T` (statement).** The abstract's "`Δ` carries … so every row is
   satisfied" is false for `Δ` itself: three `G` pole rows are already nonzero
   on `Δ` at `T = 8` (§2). Only `Δ_T` — `Δ` cut by the `h2`-only system — is
   the locus. The body says this; the headline does not.
3. **Constants free at all depths (strengthening).** §2: zero `D1` rows in all
   eight constant bands, so the four-constant enhancement never dies. Note also
   that the constants are *invisible* at every truncation any engine has run
   (`max_t = T ≤ 22 < 33`), so all recorded results concern `Δ_0 = {outer = 0}`,
   where `F = h2^3`, `G = h2^2`, `F^2 = G^3` exactly.
4. **Not claimed.** That any branch is alive; that the full system with `J_0`
   is consistent; that no single-polynomial kill exists below `T_0` — §5 and
   §6 both exhibit charts where one does.

## 8. FALLACY-v2

* *Floor/attainment*: `T_0` is stated as an exact depth and I verified both
  halves — every row below it is satisfied on `Δ_T` (exact identity + explicit
  witness), and the row at it is not. Not a floor dressed as equality.
* *Variable/ring map*: §1 declares the map, generator order and the block
  degrees, and the constants' `t`-sites are confirmed by the engines' own
  `build_FG` rather than asserted.
* *`sat()` wrapping*: none used. The historical units are constant residual
  rows, units without any Rabinowitsch wrapper; the localizer was excluded from
  the pivot pool in every run (`eligible = inner_free − {ρ or c}`).
* *Raw remainder degree*: the D=108 witness is verified by substitution into
  the **raw** local rows, not into the reduced ones.
* *Carrier/attainment*: `Δ_T ⊆ V(R_T)` is the direction proved; I do not claim
  equality, and §3 names the reason the reverse inclusion is not established.
* *Pole/interior*: the pole targets are derived from `K3(σ)` and the tower on
  each chart, and §6 shows the chart forces the leading coefficient rather than
  the analyst choosing it.
* Positive and negative controls: two independent negative controls on the
  Jacobian identity (§1), a positive/negative pair on the historical engines
  (old → constant, corrected → empty, §5), and the reading-(A)/reading-(B)
  discrimination (§6).

## 9. Artifacts (`box/cone-vertex-gate-20260905/`)

```text
manifest.sha256, manifest.check        receipt-built manifest, 6/6 OK
note1_identity.md                      the hand derivation of §1
cvg_t1_d108.py  t1_d108.json           §2  1420-row Δ evaluation, constants, D1 bands
cvg_t2_identity.py  t2_identity.json   §1  engine-native KJ identity + 2 controls
cvg_t3_d108_depth.py  t3_d108_depth.json   §4  D=108 depth ledger + raw-row witness
cvg_t4_historical.py  t4_historical.json   §5  three engines × two branches
cvg_t5_g9966_depth.py t5_g9966_depth.json  §4  (99,66) corrected depth ledgers
cvg_t6_localizers.py  t6_localizers.json   §2  Hc_5_3, D2 faces, tag schedule
cvg_t7_leadrow.py     t7_leadrow.json      §6  reading (B) at D=108
cvg_t8_g9966_leadrow.py t8_g9966_leadrow.json §6  reading (B) at (99,66) δ=2
cvg_t9_probe_point.py t9_probe_point.json  §6  h3-on-D1 probe at full depth + witness
t1..t8.log                             stdout of each driver
```

**VERDICT: `CONFIRMED-WITH-FIX`. The cone-vertex theorem is correct on the
corrected row set: `J(F,G) ≡ 0` on `Δ` is an exact cancellation forced by
`2n = 3m` and the block degrees, the outer `D1` rows can never reach the four
constants, the `h2`-only systems are consistent to full depth with explicit
witnesses (pivot counts 102 / 76 / 94, all residuals empty), and the three
historical units are single-polynomial (`a_4 = 8`,
`a_8 = 8`). `T_0 = n+m−2` (178 / 163 / 163) is the exact first exclusion, so
the staged band-engine family is retired as a kill instrument below `T_0`.
The fix: the engines emit the top pole tag as `= 0` with no target, a row that
reduces to `1 = 0` on the whole chart and would manufacture a spurious unit at
stage 92 / 60 / 77 / 50; repair `raw_minor_support`'s leading tag before any
deep run.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `22161`.
- Body SHA-256:
  `555a2cb0e3d480f0378f5858b0adc6755a6c5fd9d67c7803e8355e7e1b464a88`.
- Frozen basis: `148ae18a7d8682bc97a0ed716a554e7e8245d630`.
