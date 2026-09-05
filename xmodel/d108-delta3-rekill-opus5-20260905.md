# D=108 δ=3 — re-attacking the split branch at the proved D2 radius

Opus 5 · 2026-09-05 · lane `d108-delta3-rekill-opus5-20260905`

**Disposition: `NECESSARY-CHART SURVIVOR`. The D=108 δ=3 split branch survives
the FULL staged elimination (stages 0–4, the sibling `(99,66)` schedule) on the
chart Moh Def 5.1(3) licenses. `D108-DELTA3-DEAD` is not re-certifiable.**

The frozen `17(ddddd)` kill was refuted at stage 0 by the charged centre lane.
That refutation only showed the *necessary* stage-0 block is vacuous; it did not
touch the higher bands, the D1 block, or the outer accounting, and the gate's
certificate never used them. This lane rebuilt the whole engine at the corrected
radius and ran them. Result at every stage 0,1,2,3,4: exact-`Q` localized
dimension `10, 10, 10, 13, 14` — never `−1`. The residual ideal at stage 4 has
radical `⟨K2c_3_26 + 8·jet2, K2c_4_25 − K2c_4_26 − 20·jet1²⟩`, codimension 2,
and I exhibit a rational point that annihilates **all 715 raw rows by direct
substitution** while obeying `c ≠ 0` and `D_2`-minimality. The same driver at
the frozen radius returns `dim = −1`, `UNIT` at stage 0 *and* at stage 4, so the
pipeline can still kill.

This is **not** a counterexample to the Jacobian conjecture and no such claim is
made: the survivor satisfies the rows the stage-≤4 schedule expresses and leaves
the deep pole obligations and the higher Jacobian bands untested (§7).

No ledger was edited; no `jc2-lean`; no `ideation-*`. No new exit-price
assertion is made, so no FALLACY-v2 `charge_basis=` line applies.

## 0. Custody

The manifest was built mechanically from
`xmodel/d108-delta3-rekill-opus5-20260905.run.v2` by joining its numbered
`_basename` and `_sha256` fields with `awk` and prefixing `lane_inputs_dir`; no
digest was retyped. `sha256sum -c` returned `OK` for all seven frozen files in
`/tmp/jc2-lane.YBnSCv/inputs`. Retained as
`box/d108-rekill-20260905/frozen-inputs.sha256` and `.check.log`. No content
mismatch.

No fleet worker was launched: the whole program ran on the lane host (16 cores,
123 GB); nothing to terminate. Repo files outside the frozen set were read
read-only at basis `67baf4af`. Only `box/d108-rekill-20260905/` and this report
were written. Every ideal below was decided in Singular over `Q` (`dim`,
`reduce(1,std)`), never modularly.

## 1. What had to be rebuilt, and what did not

The frozen D=108 engine `box/g108gate-20260903/band_engine.py` implements
**stage 0 only** — `main()` refuses any later stage ("stage 0 is terminal
(DEAD)"). So there was no staged D=108 driver to patch. What exists is
(a) `major_structure()`, a pure combinatorial certificate for the h3/h2 D2 and
h2 D1 blocks, and (b) `continuation_schedule()`, the pole and Jacobian
schedules. I therefore ported the *sibling* architecture
(`box/g9966band-20260903/band_engine.py`, stages 0..n) onto the D=108 row.

Radius-**dependent** (rebuilt): the D2 weight, the K3 and K2 face weights, the
K2 D2 face polynomial, the D1 line, the h2 D1 rows, the outer `W0` and D1
thresholds.

Radius-**independent** (transplanted verbatim from the frozen charged engine):
the minor series `y = jet1 t + jet2 t² + π t³`, the target
`K3 = −t⁸(π²−c)+O(t⁹)`, `raw_minor_support` (`e = 12−i+j+b+2k`, shift 96, for
`F`; `pole 8`, shift 64, for `G`), the Jacobian formula
`108·KF·(KG)_w − t(KF)_t(KG)_w − 72(KF)_w·KG + (KF)_w·t(KG)_t`, and the stage
schedule (prior local powers 1,2,3 + ten `J177` rows; stage `s` adds local power
`4+s` and its `J` band).

```text
                          frozen engine            Moh Def 5.1(3)
  D2 substitution         t=s^4, z=pi*s^6          t=s^4, z=pi*s^5
  D2 weight W             4r+6q                    4r+5q
  K3 D2 face weight       42                       35   (= ord_s K3 exactly)
  K2 D2 face weight       168                      140
  D1 line                 s=e^2,t=e^8,z=e^12(1+Pi*e)  ... z=e^10(1+Pi*e)
  K2 D1 leading e-exp     344                      287
```

## 2. Two corrections the centre lane did not reach

The centre lane proved the *slope* wrong from `δ_2 = 1/4` and from
`ord_s K3(σ_{D2}) = 35`. Rebuilding the engine forced two further, independent
consequences, and each is a second witness to the same defect.

**(a) The K2 D2 face polynomial.** The frozen engine hard-codes
`D2_K2_face = π^12(π²−1)^8` (`face_values = (−1)^k C(8,k)` at sites
`(3k, 28−2k)`). The face is the product over the 28 roots of `K2` in `D_2` of
`(π − π_root)`; roots inside one `D_1` share a `π`-value, so the face is
`∏_{conj}(π − ω)^{V_2}`. Def 5.1(1) gives `T_2` exactly
`(36/36)·V_2 = 7` roots in `D_1`, and `A_2 = den(L_2 δ_2) = 4` gives the
conjugate count. `4 × 7 = 28` exactly, so the source face is

```text
  (pi^4 - 1)^7   at sites (5k, 28-4k), k=0..7, values (-1)^k*C(7,k)
```

with **no** `π = 0` factor. The frozen `π^12(π²−1)^8` has multiplicity **8** at
each of **2** conjugates plus a spurious `π^12`: neither number is `V_2 = 7`
nor `A_2 = 4`. The sibling passes the same test exactly: `(99,66)` has
`A_2 = 3`, `V_2 = 8`, `3 × 8 = 24 = deg` and the sibling engine literally
encodes `(π³−1)^8`. This is `17(ddddd)`'s defect seen from the multiplicity
side rather than the exponent side.

**(b) The outer constants are radius-derived, and the derivation is
controlled.** The frozen `(99,66)` `OUTER_SPECS` are four `(degree, W0,
threshold)` triples. I re-derived them from the radius alone —

```text
  W0(block)        = W(container) - W(K2)*[block multiplies K2] - tshift
  threshold(block) = e(container) - e(K2)*[same] - d1_mult*tshift
```

— and the derivation reproduces the frozen `(99,66)` numbers **exactly, all
twelve** (`A2 (65,189,583)`, `A3 (98,285,879)`, `B1 (32,93,287)`,
`B2 (65,189,583)`; `step2-major.json:control_outer_spec_derivation_9966.MATCH =
true`). Applied to D=108 it gives

```text
              degree   W0(4r+6q)  thr      W0(4r+5q)  thr      kept coords
  A2            71       332      680        276      566     42  ->  252
  A3           107       500     1024        416      853      0  ->  288
  B1            35       164      336        136      279    108  ->  176
  B2            71       332      680        276      566     42  ->  252
```

At the frozen radius the **entire `A3` block is deleted** by the D2 preblock
(0 of 3258 coordinates survive). That is not a mild difference in bookkeeping:
it removes `F`'s whole free constant term from the chart. At the source radius
288 `A3` coordinates survive. The frozen weight was suppressing the outer
system it then declined to promote.

## 3. The corrected major structure (exact, combinatorial)

`work/major_corrected.py` recomputes `major_structure()` at both radii with the
frozen selection rule (`r` up, `q` down; C4 for `q≤8`, C3 for `9≤q≤17`, C2 for
`q≥18`) and the frozen unit-triangular-leader assertion.

```text
                        frozen 4r+6q      source 4r+5q
  h3 lower ambient           45                45
  h3 strict-below rows       36                31
  h3 face rows                2 {(3,5),(6,3)}   1 {(5,3)}
  h3 surviving coords         7                13   (14 with the face retained)
  h2 nominal slots          566               497
  h2 face slots               8                 7
  h2 identity sites      {(1,27)}          {(1,27)}
  h2 D2 rank                565               496   (leader failures 0)
  ambient H+C2+C3+C4        628               634
  free after D2              63               138
  h2 D1 raw rows              4                 9   (W=141 k0..4, 142 k0..2, 143 k0)
  h2 D1 rank                  4                 9   (residual 0)
```

At `wz = 6` this is byte-for-byte the frozen certificate (45/36/2/7,
566/558/8, sole identity `(1,27)`, rank 565, pivots `{C4:288, C3:198, C2:79}`,
ambient 628) — the positive control on the re-emitter. At `wz = 5` the single
identity site is still `(1,27)` and it still has no source and no target
support, so it is still vacuous; every other slot still has a unit-triangular
leader (`leader_failure_count = 0`). The 125 `K2c` output coordinates are
exactly `138 − 13`, so the re-coordinatization is a bijection, not a cap.

## 4. Six controls, all passing

1. **Old radius must reproduce `[1]`.** `ctl_frozen_cut43_jet0pinned`: 7 coords,
   12 nonzero rows, 7 `Q*` pivots, residual `{r60,r70,r71,r80,r81}`, localized
   ideal `= [1]`. `ctl_frozen_cut42_jet0pinned`: 9 coords, 9 pivots, 2 residual,
   `[1]`. Both match the charged gate's Stage-0 Replay counts exactly.
2. **The centre lane's witness must satisfy stage 0 in the rebuilt engine.**
   Substituted into all thirteen raw rows of `src_cut35_jet0pinned`:
   `all_rows_vanish = true`.
3. **Outer-spec derivation vs the frozen `(99,66)` constants.** MATCH (§2b).
4. **Jacobian normalization.** `J[t¹,w¹⁵] = 1712·f0 = (108−1)·16·f0`, and `15`
   is the lowest nonzero `w`-power — the frozen `continuation_schedule()`
   record, reproduced. (This also certifies the K2 top form `z^28(1+z)^8`; a
   wrong top shifts that `w`-power.)
5. **Pole schedule.** `raw_minor_support` reproduces the frozen assertions
   `1200` (`F`) and `544` (`G`) raw tags, local powers `1..96` and `1..64`.
6. **The pipeline can still kill.** The *same* staged driver run at the frozen
   radius returns `dim = −1`, `UNIT = True` at stage 0 (21 rows) **and** at
   stage 4 (717 rows). The survival below is a property of the chart, not of a
   defanged driver.

Every Singular call carried the frozen wrapper controls
`⟨c, Zc·c−1⟩` unit / `⟨c−1, Zc·c−1⟩` nonunit / raw-unlocalized nonunit; all
eight runs returned `(0, 1, 1)`.

## 5. The staged elimination

Rows per stage are the sibling's: prior `F`/`G` local powers 1,2,3 (3 rows
each) + ten `J177` rows; stage `s` adds `F`,`G` at local power `4+s` and its
Jacobian band (`s=0`: `d177 w25`; `s=1`: `d177 w26..177`; `s≥2`: `d(178−s)`,
all `w`). The stage-0 common-`h3` incidence **residual** is carried as rows at
every stage (empty at the source radius; it is the frozen kill at the frozen
radius). Outer D1 offsets `0..s` are imposed.

```text
  tag                          rows  free  Q*piv  zero  resid  dim  UNIT
  joint_wz5_jet0pinned_stage0    19  1052     0     18     1     10  False
  joint_wz5_jet0pinned_stage1   175  1020     8    166     1     10  False
  joint_wz5_jet0pinned_stage2   356   990    16    339     1     10  False
  joint_wz5_jet0pinned_stage3   536   964    24    510     2     13  False
  joint_wz5_jet0pinned_stage4   715   943    32    680     3     14  False
  joint_wz5_jet0free_stage4     715   943    32    680     3     15  False
  joint_wz6_jet0pinned_stage0    21   224     0     18     3     -1  True
  joint_wz6_jet0pinned_stage4   717   198    30    682     5     -1  True
  sat_wz5_jet0pinned_T8        1420   906    60   1357     3      7  False
```

The last row is the *saturated* system (§7): every row the chart expresses at
truncation depth 8 — `F`/`G` pole rows at all local powers `1..8`, all Jacobian
bands at `t = 1..8` with all `w`-powers (1396 `J` rows), and outer D1 offsets
`0..7` (180 outer pivots). It is strictly more rows than stage 4 and it still
does not close.

Reading the structure rather than the counts:

* The stage-0 pivots force `Hc_1_7 = Hc_1_8 = 0`, so `h3` has no `r = 1` row,
  so `K2` and hence `KF` have **no `t¹` band**. The ten prior `J177` rows and
  the stage-0 `J177 w25` row are therefore identically zero: `J₁`'s lowest
  nonzero `w`-power is 31, not 15. The frozen prior/stage-0 `J` window
  `w ∈ 15..25` is empty on this branch. That is a property of the branch, not
  a dropped row — the rows are imposed and evaluate to `0`.
* The first informative rows are the stage-1 `J177` rows `w = 31..38`. They form
  a unit-triangular chain that annihilates the whole `B1` `r=0` band:
  `B1c_0_35 = 0`, then `B1c_0_34 = 7·B1c_0_35 = 0`, … , `B1c_0_28 = 0`.
* Each stage then leaves one `G`-local row of the shape
  `(alternating sum of B1c_r_q)·(K2c_3_26 + 8·jet2)`, which the next stage's
  `J` chain kills on the `B1` factor. The regress is not an accident: at stage 3
  the residual acquires `(K2c_3_26 + 8·jet2)²`, and that is a genuine
  constraint, not a factorization artifact.

## 6. The surviving locus, and a rational point

Stage-4 residual (three rows, exact `Q`, `work/witness-stage4.json`):

```text
  stage2_G_local6_coord0 = (K2c_3_26 + 8*jet2)^2
  stage3_G_local7_coord0 = -2*(K2c_3_26 + 8*jet2)
                              *(K2c_4_25 - K2c_4_26 - 20*jet1^2)
  stage4_G_local8_coord0 = [B1c_4_* terms]*(K2c_3_26 + 8*jet2)
                           + (K2c_4_25 - K2c_4_26 - 20*jet1^2)^2  + ...
```

The substitution

```text
  K2c_3_26 = -8*jet2 ,   K2c_4_25 = K2c_4_26 + 20*jet1^2
```

annihilates all three generators **identically as polynomials** (checked
symbolically, not at a point: `residual_vanishes_symbolically_on_solve = true`).
So the surviving locus contains a codimension-2 subvariety on which
`jet1, jet2, c, Hc_5_4, Hc_9_0, K2c_4_26`, the remaining 116 `K2c` and 825 outer
coordinates are all free. Singular over `Q` reports `dim = 14` in 16 active
variables — `16 − 2` — so codimension 2 is exact, and `reduce(1, std) = 1`.

Explicit rational point (`work/witness-stage4.json`):

```text
  jet1 = jet2 = c = 1 ,  K2c_3_26 = -8 ,  K2c_4_25 = 20 ,
  every other free unknown = 0 ;
  the 32 Q* pivots and the 12 stage-0 pivots then resolve to rationals.
```

**Negative control.** The point is substituted into **all 715 raw rows** —
never through the pivots — and every one vanishes:
`NEGATIVE_CONTROL_all_raw_rows_vanish = true`, `raw_rows_failing = []`. It also
clears every sourced side condition:

* `c = 1 ≠ 0`, the sole localization the gate declares.
* `Hc_5_3 = 2·jet1·jet2 = 2 ≠ 0`, so the K3 D2 face is `π³(π⁴+2)` with five
  distinct roots and `D_2` is a minimal disc in the sense of Prop 5.2.
* The face is `π³ ×` (a polynomial in `π⁴`), the Galois shape forced by
  `A_2 = 4`.
* `ord_s K3(σ_{D2}) = 35` exactly — the point sits **on** the proved floor.

The gauge-honest chart agrees: with the minor constant `jet0` freed (Repair R,
§8) stage 4 gives `dim = 15`, `UNIT = False`, same three residual rows. Survival
on the `jet0`-pinned chart implies survival on the `jet0`-free chart, since the
pinned locus is the `jet0 = 0` slice; I ran both rather than rely on that.

## 7. What this survivor is, and what it is not

Typed exactly: **necessary-chart survivor**. It satisfies every row the
stage-≤4 schedule expresses on the Def 5.1(3) chart. It leaves untested:

* `F`'s pole rows at local powers `9..95` (1188 of its 1200 tags) and the
  leading target `p^12` at local power 96; `G`'s at `9..63` (532 of 544) and
  `p^8` at 64. Stage `s` reaches local power `4+s`, so stages 5..92 remain.
* Jacobian bands at `t`-power `≥ 5` (degrees `≤ 173`) and the degree-0
  normalization `J = 1`.
* Outer D1 offsets beyond 4; the `A2`/`A3`/`B2` blocks are invisible at
  `t ≤ 8` because their surviving coordinates start at `r ≥ 26`, `61`, `26`
  respectively, so the outer accounting is genuinely untouched at these stages.
* Whether `K3` must additionally vanish on `D_1`. Def 5.1(1) at `i = 1` returns
  `(μ_3/d_2)·V_2 = (9/36)·7 = 7/4`, not an integer, so the printed criterion
  does not constrain `T_3` at level 1 and I imposed no such row — imposing it
  unsourced would have been the same class of error as the transplanted
  exponent. But I did price it as a clearly-labelled conditional probe: such a
  row would force the K3 D2 face `π³(π⁴ + Hc_5_3)` to vanish at the D1 centre
  `π = 1`, i.e. `Hc_5_3 = −1`, i.e. `2·jet1·jet2 + 1 = 0`. Adjoining that
  generator (`work/h3D1-conditional-probe.json`) costs exactly one dimension and
  **does not kill**: stage 4 goes `14 → 13`, saturated goes `7 → 6`, and
  `reduce(1, std) = 1` in both. So the cheapest missing row, even if it turns
  out to be sourced, does not restore `17(ddddd)`.

So this is a survivor of a *necessary* system, exactly as `17(ddddd)`'s
certificate was a claim about a *necessary* system. The asymmetry is the point:
a unit on a necessary system is a proof of death, a point on one is not a proof
of life. What died today is the kill, not the row.

**The saturated test.** Because the staged schedule is a driver convention (the
frozen engine says so in as many words), I also ran the union of everything the
chart expresses at truncation depth 8: `work/step4_saturated.py`, 1420 rows —
all `F`/`G` pole rows at local powers `1..8`, all Jacobian bands at `t = 1..8`
with all `w`-powers, outer D1 offsets `0..7`. Adding rows can only shrink the
locus, and it does shrink it — the `B1` block is now eliminated outright and the
active-variable count falls from 16 to 9 — but the ideal is the same one:

```text
  G_local6_coord0 = (K2c_3_26 + 8*jet2)^2
  G_local7_coord0 = -2*(K2c_3_26 + 8*jet2)*(K2c_4_25 - K2c_4_26 - 20*jet1^2)
  G_local8_coord0 = ... same two forms, B1 terms now absent
  exact Q: dim = 7 in 9 active variables, reduce(1,std) = 1, codimension 2
```

Same radical, same codimension, same witness family — and the **same rational
point**: the point of §6, unchanged, annihilates all **1420** saturated raw rows
by direct substitution (`work/witness-saturated-T8.json`,
`NEGATIVE_CONTROL_all_raw_rows_vanish = true`, `raw_rows_failing = []`,
`Hc_5_3 = 2 ≠ 0`, `c = 1`). The survivor is therefore not an artifact of the
stage-4 cut-off.

## 8. Gauge ledger

Every normalization, its group element, and whether it is spent (FALLACY-v2
requires the element, and each may be spent once):

```text
  z = w-1, D3 cluster leading coefficient 1      y -> lambda*y      SPENT
  top_K3 = z^7(1+z)^2, other cluster at w=0      y -> y + mu*x      SPENT
  D2 centre a_1 = 0  (Lemma C: the sole centre
    exponent below the D2 radius is j=1)         y -> y + a_1       SPENT
  minor constant jet0                            none left          FREE
  p = pi^2 - c  (no linear term in pi)           child generic-point
                                                 reparametrisation,
                                                 not in the affine
                                                 group              SPENT
  D1 centre at pi = 1                            choice of one of the
                                                 A_2 = 4 Galois
                                                 conjugates         no parameter
```

The `4r+5q` weight is only valid when the D2 centre is zero: with `z = a_1 t +
π s^5` the `s`-order of `t^r z^q` collapses to `4r+4q`. So the corrected radius
*requires* the translation, which is why `jet0` must be released — the frozen
chart spends `y ↦ y + a_1` twice. Both charts are reported.

## 9. FALLACY-v2 notes

* **Dropping rows vs dropping unknowns.** Nothing was dropped by a floor. The
  `local_power ≤ 8` truncation drops ROWS (higher pole rows are simply not
  imposed at stages ≤ 4) and is declared in §7 as an untested remainder. Seven
  `h3` coordinates and one `jet` are FREED relative to the frozen chart, never
  pinned.
* **`Q*` only.** `qstar_reduce` accepts a pivot only when the coefficient is in
  `Q*` and the variable is absent from the remainder. No `jet`, `Hc_*`, `K2c_*`
  or outer coordinate is ever inverted. The sole localization is `c ≠ 0`, via
  the Rabinowitsch variable `Zc`; `Zc` is not an extra nonvanishing hypothesis.
  No `sat()` wrapper is used.
* **Modular unit → exact-Q.** No modular computation was consumed anywhere;
  every `dim` and `reduce(1,std)` is over `Q`.
* **Floor/attainment.** `ord_s K3(σ_{D2}) = 35` and `ord_e K2(σ_{D1}) = 287`
  are equalities derived from Def 5.1(1) root counts plus transcendence of `π`
  and `Π`; the support statements `4r+5q ≥ 35` and `2W+k ≥ 287` are used only
  as floors, and the witness sits on the first.
* **Flag/place/series.** The major `D_2` disc, the `D_1` sub-disc, the minor
  `δ' = 3` place and the child `δ' = 4` continuation are kept distinct; `a_1` is
  a major-place object and `jet0` a minor-place object, related by one
  translation, never identified.
* **Variable/ring map.** Every Singular ring is `0,(vars,Zc),dp` with the
  variable list printed in the emitted `.sing`; the `K2c` coordinate change is
  asserted bijective by the `138 − 13 = 125` count and the zero
  leader-failure certificate, not by name matching.

## 10. Consequences for the ledger (stated, not edited)

| claim | status after this lane |
|---|---|
| `17(ddddd)` `CONFIRMED[D108-DELTA3-DEAD]` | **not re-certifiable.** The kill fails on the corrected chart at stage 0 *and* survives the full staged elimination through stage 4, with an exact-`Q` rational point of all 715 rows. |
| `17(hhhhhhh)` "D=108 OPEN on both arms" | **strengthened** on the split arm: OPEN is now backed by a staged survivor, not only by the vacuity of one block. |
| frozen `D2_K2_face = π^12(π²−1)^8` | **wrong shape**, independently of the exponent audit: it encodes `A_2 = 2, V_2 = 8` where the row has `A_2 = 4, V_2 = 7`. Source face `(π⁴−1)^7`. |
| frozen `A3` outer block (0 surviving coordinates) | an artifact of `W0 = 500` at the wrong weight; the source `W0 = 416` keeps 288. |
| the frozen `(99,66)` `OUTER_SPECS` | **re-derived and confirmed**, all twelve constants, from the radius alone. |
| `17(pppp)` / `17(tttt)` `(99,66)` D2 blocks | untouched here; the centre lane's radius-SOUND finding is corroborated by control 3 (their outer constants are exactly what the source radius predicts). |

## 11. Artifacts

```text
box/d108-rekill-20260905/frozen-inputs.sha256 / .check.log   7/7 OK
work/major_corrected.py, major-structure-both.json           both radii, exact
work/rekill_engine.py                                        corrected engine
work/step1_stage0.py, step1-stage0.json                      stage-0 + controls 1,2
work/step2_major.py, step2-major.json                        h2 D2/D1 + control 3
work/step3_joint.py, joint_wz{5,6}_jet0*_stage{0..4}.json    staged elimination
work/step4_saturated.py, sat_wz5_jet0pinned_T8.json           saturated, 1420 rows
work/step6_sat_witness.py, witness-saturated-T8.json          saturated witness
work/step5_witness.py, witness-stage4.json                   witness + neg. control
work/h3D1-conditional-probe.json                             priced conditional row
work/*.sing, *.sing.out                                      exact-Q Singular
```

**VERDICT: `NECESSARY-CHART SURVIVOR`.** On the chart Moh Def 5.1(3) licenses,
the D=108 δ=3 split branch survives stages 0–4 of the sibling staged
elimination; the surviving locus has codimension 2 in the stage-4 residual
variables and carries an explicit rational point satisfying all 715 raw rows —
and the same point satisfies all 1420 rows of the strictly larger saturated
system — with `c ≠ 0` and `D_2`-minimality. The same driver kills the branch at the frozen
radius. `D108-DELTA3-DEAD` cannot be re-certified.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23110`.
- Body SHA-256:
  `b1c87c8863a8c6a7389b213cddc101ac5fe0dc56fb359983b013c4d91c2cb33b`.
- Frozen basis: `67baf4af14b4ac5758f78e1c6107b71dabcdbd47`.
