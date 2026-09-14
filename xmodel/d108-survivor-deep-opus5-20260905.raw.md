# D=108 δ=3 — the deep obligations of the necessary chart, on the surviving locus

Opus 5 · 2026-09-05 · lane `d108-survivor-deep-opus5-20260905`

**Disposition: `COMPUTE-BOUND AT LOCAL POWER 11`, with the survivor intact
everywhere it was tested. Restricted to the exact stage-4/saturated survivor
locus `V(u,v)`, the D=108 δ=3 split branch survives every row the chart
expresses at depths 8, 9, 10 and 11 — 1,945 rows, exact `Q`, dimension
`(0) → (0) → 5 → 9`, never a unit. Two of the four listed deep obligations are
now DISCHARGED IN FULL (the outer D1 ladder, which is finite and ends at offset
10; the degree-178 Jacobian top band, identically zero), one is partly
discharged (`t = 5..11` of the requested `t = 5..12`), and the pole rows are
pushed from local power 8 to 11. `D108-DELTA3-DEAD` remains not
re-certifiable, and nothing here promotes the branch to a Keller pair.**

The charged re-kill lane left a codimension-2 locus with a rational point
satisfying all 1,420 saturated rows. This lane asks what comes next: does the
*necessary chart* ever close if you keep going? At every depth reached, no —
and two of the deep families turn out to be **finite and now exhausted**, which
changes what "keep going" can even mean.

No ledger was edited; no `jc2-lean`; no `ideation-*`. No new exit-price
assertion is made, so no FALLACY-v2 `charge_basis=` line applies.

## 0. Custody

The manifest was built mechanically from
`xmodel/d108-survivor-deep-opus5-20260905.run.v2` with `awk` over its numbered
`charged_input_<i>_basename=` / `_sha256=` fields, prefixed with
`lane_inputs_dir`, and checked with `sha256sum -c`. All six frozen files in
`/tmp/jc2-lane.BCrOyu/inputs` returned `OK`; no digest was retyped and there
was no content mismatch.

No fleet worker was launched — the lane host (16 cores, 123 GB) carried the
whole program. Two deeper one-shot systems (`T = 16`, `T = 22`) were still
inside `qstar_reduce` at the deadline and were terminated before sealing; no
compute is left running and no result of theirs is used below. Repo files
outside the frozen set were read read-only at basis `fb9f12f4`. Only
`box/d108-survivor-deep-20260905/` and this report were written; the charged
engine directory `box/d108-rekill-20260905/` was imported, never modified.
Every ideal below was decided in Singular over `Q` (`dim`, `reduce(1,std)`),
never modularly.

## 1. The locus, and why restricting to it is licensed

The charged saturated system (1,420 rows, depth 8) has the three-generator
residual `I = ⟨u², −2uv, uL + v²⟩` in

```text
  u = K2c_3_26 + 8*jet2
  v = K2c_4_25 − K2c_4_26 − 20*jet1²
  L = −120*Hc_5_4 − 2*(K2c_5_25 − K2c_5_26) − 52*jet1*K2c_3_26 − 96*jet1*jet2 − 14
```

`u ∈ rad I` from `u²`; `v² = (uL + v²) − u·L ∈ I` so `v ∈ rad I`; and
`I ⊆ ⟨u,v⟩`, which is prime because `u` is monic linear in `K2c_3_26`, `v` is
monic linear in `K2c_4_25`, and neither variable occurs in the other generator
— so the quotient is a polynomial ring. Hence

```text
  rad(I) = ⟨u, v⟩   EXACTLY,      so   V(I) = V(u,v)  as a SET.
```

**Control B** (`ctl-radical.json`, `LIB "primdec.lib"; radical(I)`, exact `Q`)
checks both inclusions mechanically: `reduce(rad I, std⟨u,v⟩)` and
`reduce(⟨u,v⟩, std(rad I))` are both `0`; `dim I = dim⟨u,v⟩ = 6` in the 8
residual variables; and `reduce(⟨u,v⟩, std I) ≠ 0`, i.e. `I ⊊ ⟨u,v⟩` — `I` is
genuinely non-radical, which is exactly why the argument has to be
set-theoretic and not ideal-theoretic.

**The licence.** Because the survivor *set* of the saturated system is exactly
`V(u,v)` (intersected with the resolved `Q*` pivots), imposing `u = v = 0`
discards no point over any extension field. So: a unit ideal after restriction
proves no point satisfies the extended system, i.e. the branch is dead; a
non-unit after restriction proves nothing beyond survival, exactly as before.
The restriction is implemented as the substitution
`K2c_3_26 ↦ −8·jet2`, `K2c_4_25 ↦ K2c_4_26 + 20·jet1²` applied to `K2`
immediately after `build_major_h2`. That is *identical* to adding `u` and `v`
as two extra rows — both are `Q*` unit pivots on those two variables — and it
is not a floor: no unknown is dropped, two are RESOLVED, and the two resolved
values are recorded in every output JSON (`k2meta.locus_substitution`).

## 2. Engine changes, and the five controls that pin them

The charged engine is used verbatim for the mathematics
(`box/d108-rekill-20260905/work/rekill_engine.py`); `deep_engine.py` changes
only *how* the same rows are computed, and every change is pinned by replaying
the charged saturated-`T8` row set and comparing `rows_sha256`.

```text
  change                                          why                  control
  build_major_h2(max_t = T), not 40               k2 rows with r > T
                                                  are unread at T        A
  J = (KG)_z[108KF − t(KF)_t] − (KF)_z[72KG −     4 products -> 2,
      t(KG)_t]; one pass at max_t, bands sliced   one pass not T         C
  coefficients in sympy's sparse ring, not Expr   ~15x on tz_mul         D
  z-band -> w-band extraction in the ring         the next wall          D
  local_rows skips w-power j when r + 2j > n      n >= r + 2j exactly    E

  A ctl-replay-T8.json  rows_sha256 68201f86…cc6d == charged      MATCH
  B ctl-radical.json    rad(I) == <u,v>, both inclusions          MATCH
  C ctl-jband.json      single-pass J == per-band J, t = 1..5     MATCH
  D ctl-fastpath.json   rows_sha256 68201f86…cc6d == charged      MATCH
  E ctl-localcut.json   local_rows_fast == frozen local_rows      MATCH
```

A and D are the strong ones: the *entire* 1,420-row saturated system at depth 8
is regenerated through the new path and hashes to the charged digest
`68201f86f8103fad3ad5b8dbe5b36a8d35a4a81ce85338a6957beb1dc5bfcc6d` byte for
byte, so the optimisations are identities, not approximations. C also records
that the `t⁰` band of `J` — the degree-178 top form — is identically zero on
the *corrected* chart, reproducing the frozen engine's "proportional top forms"
assertion rather than inheriting it.

## 3. The deep schedule on the locus

Stage `n` imposes, on the locus, **everything the chart expresses at depth `n`**:
the stage-0 common-`h3` incidence residual, all `F` and `G` minor pole rows at
local powers `1..n`, all Jacobian bands at `t = 1..n` with every `w`-power, and
the **complete** outer D1 ladder (offsets `0..10`, §4) at every stage — the
outer state is built once at offsets `0..T−1` and reused. Every stage is exact-`Q`: `qstar_reduce` inverts only
elements of `Q*`, then Singular `std` over `Q` with the `Zc·c−1` wrapper and the
three frozen wrapper controls (all three returned the required `(0,1,1)` at
every call).

```text
  n    raw rows     F    G      J   Q*piv   zero  resid   dim          UNIT   §6 point
  8      1420      12   12   1396     60    1360     0    (0) = FULL   False  holds
  9      1596      15   15   1566     66    1530     0    (0) = FULL   False  holds
 10      1771      18   18   1735     72    1698     1    5 of 6       False  FAILS
 11      1945      21   21   1903     78    1865     2    9 of 10      False  FAILS
```

**`n = 8` is a cross-check.** The charged saturated run on the unrestricted
chart had 60 `Q*` pivots, 1,357 zero rows and 3 residual generators; on the
locus those 3 vanish identically, giving 60 pivots, 1,360 zero rows, residual
`(0)`. The two agree exactly — the arithmetic form of "the locus is the
survivor set".

**`n = 9` imposes no new condition at all.** Six new pole rows and 170 new
Jacobian rows are absorbed by six new `Q*` unit pivots and 170 identical zeros;
the residual is still `(0)`.

**`n = 10` produces exactly one new generator, and it is a perfect square:**

```text
  G_local10_coord0 = ( 60*Hc_5_4 + K2c_5_25 - K2c_5_26 - 160*jet1*jet2 + 7 )^2
```

so its radical is a single hyperplane; Singular over `Q` gives `dim = 5` in 6
active variables (codimension 1), `gb_size = 2`, `reduce(1, std) = 1`. Not a
unit, and not close to one.

**The §6 point dies here, and is repaired.** The charged point evaluates the
new form to `−153`, so the row to `23409 ≠ 0`
(`sec6_point_failures = [["G_local10_coord0","23409"]]`). Because the radical
generator is *linear with rational coefficients*, a replacement is immediate
(`point-deep_locus_T11_n10.json`):

```text
  Hc_5_4 = 51/20 ,  jet1 = jet2 = c = 1 ,  every other free unknown 0 ;
  locus resolutions  K2c_3_26 = -8*jet2 = -8 ,  K2c_4_25 = K2c_4_26 + 20*jet1^2 = 20 .
  point_annihilates_residual = true ,  c = 1 != 0 ,
  D2-minimality  Hc_5_3 = 2*jet1*jet2 = 2 != 0 .
```

so `D_2` is still a minimal disc at the new point and the sole declared
localization holds.

**`n = 11` reproduces the depth-8 shape exactly.** Two generators,

```text
  G_local10_coord0 = w^2
  G_local11_coord0 = 2*w*x
  w = 60*Hc_5_4 + K2c_5_25 - K2c_5_26 - 160*jet1*jet2 + 7
  x = K2c_4_26*jet1 - K2c_6_24 + K2c_6_25 - K2c_6_26 - 308*jet1^3 + 280*jet2^2
```

with `rad⟨w², 2wx⟩ = ⟨w⟩`: `dim = 9` in 10 active variables, still codimension
1, `gb_size = 5`, `reduce(1,std) = 1`. This is the `⟨u², uv, …⟩` pattern of the
charged depth-8 residual, one depth later and in the next pair of `K2c`
coordinates. The §6 point fails on both rows (`23409`, `8568`); the repaired
point is `Hc_5_4 = 51/20`, `K2c_6_24 = −28`, `jet1 = jet2 = c = 1`, everything
else `0`, which annihilates both generators, keeps `c = 1 ≠ 0` and
`Hc_5_3 = 2 ≠ 0`. (The finder solves *every* radical factor, i.e. `w = x = 0`,
which is stricter than `V(⟨w⟩)` requires; the point is on the survivor set a
fortiori.)

### The mechanism, stated as an observation

Every constraint the chart has produced so far — at depth 8 and at depth 10 —
is a **power of an affine-linear form that is monic in a freshly-appearing
`K2c` coordinate**:

```text
  depth 8   u  = K2c_3_26 + 8*jet2                       (monic in K2c_3_26)
            v  = K2c_4_25 - K2c_4_26 - 20*jet1^2         (monic in K2c_4_25)
            residual = <u^2, uv, uL + v^2>,  rad = <u,v>
  depth 10  w  = 60*Hc_5_4 + K2c_5_25 - K2c_5_26 - 160*jet1*jet2 + 7
            residual = <w^2>,               rad = <w>
  depth 11  x  = K2c_4_26*jet1 - K2c_6_24 + K2c_6_25 - K2c_6_26
                 - 308*jet1^3 + 280*jet2^2                (monic in K2c_6_24)
            residual = <w^2, 2wx>,          rad = <w>
```

The `K2c` supply is what makes this possible: the coordinates `K2c_r_q` with
`4r + 5q > 140`, `q ≤ 26` first appear at `t`-power `r` — one at `r = 3`, two at
`r = 4` and `r = 5`, three at `r = 6`, and so on, the same "fresh unknown per
depth" pattern the outer blocks show in §4. As long as the
new generator at a depth is monic-linear in a coordinate that appears at that
depth and nowhere shallower, its radical is a hyperplane, the codimension grows
by at most one, a rational point can always be repaired by solving that one
linear equation, and **a unit is impossible**. This is an observation about the
depths computed here (8, 9, 10) and the charged depth-8 residual, not a
theorem; but it is the structural reason the necessary chart does not close,
and it is checkable at every further depth by the same one-line test
(`sp.factor` of the new generator). Four depths — 8, 9, 10, 11 — have now been
checked and all four conform.

## 4. The outer accounting: two families are FINITE, and now exhausted

The charged report listed "outer D1 offsets beyond 4" as an untested obligation.
It is not an infinite family. For a block with weight floor `W0` and D1
threshold `θ`, offset `s` contributes rows `k = 0 .. θ − 2(W0+s) − 1`, so it
contributes **nothing** once `s ≥ (θ − 2W0)/2`:

```text
  block   degree   W0    θ     last offset with rows
  B1        35     136   279          3
  A2        71     276   566          6
  B2        71     276   566          6
  A3       107     416   853         10
```

Every run in this lane imposes offsets `0 .. T−1` with `T ≥ 11`, so the outer
D1 system is imposed **in full**. The engine confirms the saturation
numerically — per-offset `Q*` pivots at offsets `0..10` are

```text
  34, 32, 30, 26, 21, 17, 13, 7, 5, 3, 1     cumulative 189
```

— against 180 cumulative at the charged offsets `0..7`; offsets 8, 9, 10 (all
`A3`, the only block still alive there) add 5, 3, 1, and **every offset from 11
on contributes an empty row set**, so the counts stay at 189 for offsets
`0..13`, `0..15`, `0..21`, `0..23`, `0..29`. Obligation **discharged in full**,
not deferred.

The other outer obligation — "`A2`/`A3`/`B2` are invisible at `t ≤ 8` because
their surviving coordinates start at `r ≥ 26, 61, 26`" — resolves structurally.
Exactly **one** coordinate of each block survives the D2 preblock at its first
`r` (`outer-visibility.json`):

```text
  block  kept  first r  coords at first r   first visible t-power
  B1     176      0     B1c_0_28 .. _0_35            1
  A2     252     26     A2c_26_35                   27
  B2     252     26     B2c_26_35                   27
  A3     288     61     A3c_61_35                   62
```

and one can say exactly which row first carries it (`outer-first-row.json`).
`k2`'s `t⁰` band is `z²⁸(1+z)⁸` (hard-coded, and re-derived by control C's top
band), and `outer_effective_tz` shifts `r → r+1`, so

```text
  B2c_26_35 enters KG at t^27 multiplying z^35        -> w-order 0
            -> first G pole row at minor local power 27
  A2c_26_35 enters KF at t^27 multiplying z^63(1+z)^8 -> w-order 8
            -> first F pole row at minor local power 27 + 2*8 = 43
  A3c_61_35 enters KF at t^62 multiplying z^35        -> w-order 0
            -> first F pole row at minor local power 62
```

(A pole row at minor local power `n` needs `n = r + 2a + 3b + 4k` with `a+b+k`
the `w`-power, so a coordinate of `w`-order `m` first shows at `n = r + 2m`.)
Each of these coordinates is **fresh** — it occurs in no row of
smaller depth — and enters linearly with a rational coefficient (`(−1)³⁵ = −1`
for `B2c_26_35` in `G_local27_coord0`). So at first visibility the `A2`, `A3`
and `B2` blocks contribute *new free unknowns with `Q*`-pivotable
coefficients*, not new constraints: they can only enlarge the survivor set at
that depth. The outer accounting can only start to bite where the rows added at
a depth outnumber the outer coordinates that depth introduces — and the
`r`-profile (`{26:1, 27:2, 28:3, 29:4, 30:4, 31:5, …}` for `A2` and `B2`) shows
the coordinate supply growing steadily. This is why the charged report's call
for "a genuinely different instrument (the joint chart / the outer accounting
theorem)" is the right diagnosis: *no* finite truncation of this chart reaches
a depth where the outer supply is exhausted.

## 5. The Jacobian: which bands are testable, and where `J = 1` actually lives

`deg J = n_F + n_G − 2 = 178`, and the engine's `t^m` band is the
degree-`(178−m)` homogeneous part of `J` (`J_t{m}_d{178−m}_k{k}`, `k` the
`w`-power, `k = 0..178−m`). So

```text
  J ≡ 1   <=>   bands t^0 .. t^177 all vanish   AND   band t^178 = 1 .
```

* **Band `t⁰` (degree 178) — DISCHARGED.** Imposed explicitly (not assumed) in
  every one-shot run and computed in every build: `0` nonzero `w`-slots, i.e.
  identically zero on the corrected chart. The frozen engine asserted this
  ("proportional top forms"); here it is a computation at the corrected radius.
* **Bands `t¹ .. t^n` — imposed in full**, every `w`-power, at every stage of
  §3; the deepest completed stage is `n = 11`, so of the requested `t = 5..12`
  window the bands `t = 5..11` are imposed and survived, and only `t = 12`
  remains untested (the `T = 16` and `T = 22` one-shot systems, which carry them,
  were still in `qstar_reduce` at the lane deadline).
* **The degree-0 normalization `J = 1` is the `t^178` band**, and it is not
  merely deep — it lies *behind the entire outer system*. `KF` reaches
  `t`-power 108 and `KG` reaches 72, and the `t^178` band pairs their deepest
  bands, i.e. it is supported on the top of `A3` (`r` up to 107) and `B2`
  (`r` up to 71). Since `A3` does not appear at all until `t^62`, no truncation
  of this chart at any depth this lane (or any lane of this shape) can reach
  it. `J = 1` is a *non-vanishing* condition, not a vanishing row: it can only
  kill by being forced to `0`, and forcing it requires the whole outer
  accounting. It is therefore correctly typed as `OPEN — needs the outer
  accounting theorem`, not as "untested at depth `k`".
## 6. The §6 rational point as a running control

The charged point is `jet1 = jet2 = c = 1`, `K2c_3_26 = −8`, `K2c_4_25 = 20`,
every other free unknown `0`. It lies **on** the locus: `u = −8 + 8·1 = 0` and
`v = 20 − 0 − 20·1² = 0`. In the locus chart those two coordinates are
RESOLVED, so the same point reads "all free unknowns `0` except
`jet1 = jet2 = c = 1`", and that is the point carried as a control at every
stage below (`sec6_point_survives_residual`).

The control is meaningful because `qstar_reduce` performs only invertible row
operations, so the solution set of the full row list equals that of
`{pivot equations} ∪ {residual}`: a point built by fixing the free unknowns and
resolving the pivots satisfies *every* raw row exactly when it satisfies the
residual. The charged lane verified that the hard way over all 1,420 raw rows
(`NEGATIVE_CONTROL_all_raw_rows_vanish = true`); this lane checks the residual
per stage.

## 7. Verdict, and what is left

**VERDICT: `COMPUTE-BOUND AT LOCAL POWER 11` on the pole schedule, with two of
the four deep obligations DISCHARGED IN FULL and the branch alive at every
depth tested.** Precisely:

```text
  obligation (charged §7)                          status after this lane
  F pole rows 9..95, leading p^12 at 96            9, 10, 11 imposed and
  G pole rows 9..63, leading p^8  at 64            survived; 12..96 untested
  Jacobian bands t >= 5, degrees <= 173            t = 1..11 imposed in full
                                                   (every w-power); t >= 12
                                                   untested
  Jacobian degree-178 top band (t^0)               DISCHARGED: identically 0
  Jacobian degree-0 normalization J = 1            NOT REACHABLE by truncation
                                                   (t^178, behind all of A3/B2)
  outer D1 offsets beyond 4                        DISCHARGED IN FULL: the
                                                   ladder ends at offset 10 and
                                                   every run imposes 0..10 in full
  A2/A3/B2 first visible offsets                   structurally resolved (§4):
                                                   one fresh Q*-pivotable
                                                   coordinate each, at
                                                   t-power 27, 27, 62
```

This is **not** `SURVIVOR of the FULL chart` and emphatically **not** a Keller
pair: pole rows from local power 12 to 96 are untested and `J = 1` is not
reachable. Nor is it a re-certification of `D108-DELTA3-DEAD`: no unit appeared
at any depth, on a strictly larger system than the charged lane ran, with a
licensed restriction — a unit would have been decisive if it existed.

What did change is the *character* of the remaining gap. Before this lane the
honest statement was "the deep rows are untested". After it:

1. Two of the four families are **finite**, and both are now closed — the outer
   D1 ladder (10 offsets, all imposed) and the degree-178 top band
   (identically zero on the corrected chart).
2. The one family that could in principle close the argument — `J = 1` — is not
   deep, it is *inaccessible*: it lives at `t`-power 178, behind the whole `A3`
   block, so no truncation of this chart at any depth reaches it.
3. The families that remain are exactly the ones whose new constraints keep
   arriving as **squares of hyperplanes monic in fresh coordinates** (§3), which
   is the pattern that makes a unit structurally impossible depth by depth.

Taken together this sharpens the charged lane's call: the necessary chart is not
merely expensive to push, it is the wrong instrument. Something that can see
`t`-power 178 without computing bands 1..177 — the joint chart, or an outer
accounting theorem — is required.

**Ledger consequences (stated, not edited).** `17(ddddd)`
`CONFIRMED[D108-DELTA3-DEAD]`: still not re-certifiable, now against a strictly
larger row set (1,945 rows at depth 11 vs 1,420 at depth 8) on the licensed
locus. `17(hhhhhhh)` "D=108 OPEN on both arms": further strengthened on the
split arm. The charged `NECESSARY-CHART SURVIVOR` typing stands; the charged §6
rational point does **not** — it is refuted at local power 10 and again at 11,
so downstream uses must be re-pointed at `point-deep_locus_T11_n11.json`.

## 8. FALLACY-v2 notes

* **Locus restriction (the load-bearing one).** A unit on the locus proves the
  branch dead only because the locus is the *exact* survivor set of the
  saturated system, and that is a set-theoretic statement about the radical,
  verified mechanically in both directions (control B). `I` is strictly smaller
  than `⟨u,v⟩`, so the ideal-theoretic version of this argument would be wrong;
  the set-theoretic one is not. Nothing is dropped by a floor: two unknowns are
  RESOLVED by two rows that are `Q*` unit pivots, and their resolved values are
  printed in every artifact.
* **Truncation drops ROWS, never unknowns.** Depth `T` omits pole rows at local
  power `> T` and bands at `t > T`; §7 lists those as remaining obligations. All
  779 free outer and 114 free `K2c` unknowns are carried at every stage.
* **Speed is not a mathematical change.** Every optimisation is pinned by
  regenerating the charged 1,420-row saturated system and matching its
  `rows_sha256` (A, D), plus two function-level identities (C, E). No modular
  computation was consumed; every `dim` and `reduce(1,std)` is over `Q`.
* **`sat()` wrapping.** Not used. The sole localization is `c ≠ 0` through the
  Rabinowitsch variable `Zc`, with the frozen wrapper controls
  `⟨c, Zc·c−1⟩` unit / `⟨c−1, Zc·c−1⟩` non-unit / raw-unlocalized non-unit
  carried on every Singular call that has a non-empty residual.
* **Floor/attainment.** "The outer D1 ladder ends at offset 10" is an equality
  derived from `k ∈ [0, θ − 2W)` being empty, not a bound; the engine's own
  per-offset pivot count, ending `5, 3, 1, 0, 0, …`, is the witness.
* **Empty residual is `(0)`, not `(1)`.** A stage whose residual is empty has
  every imposed row consumed by a `Q*` unit pivot or identically zero: the
  ideal is zero and the whole remaining free space survives (`dim = FULL`,
  `UNIT = False`). Reading an empty generator list as a unit would have
  inverted the verdict, so it is handled explicitly.
* **Gauge.** The charged §8 ledger is carried verbatim into every artifact
  (`gauge_ledger`) and nothing is spent twice; `jet0` stays pinned here, and the
  charged lane showed releasing it only *raises* the dimension (stage 4:
  14 → 15), so survival on the pinned chart implies it on the `jet0`-free one.

## 9. Artifacts

All under `box/d108-survivor-deep-20260905/`; every `dim` / `reduce(1,std)` is
exact `Q` with the emitted `.sing` and `.sing.out` retained beside it.

```text
  deep_engine.py            locus restriction, sparse-ring products,
                            single-pass Jacobian, banded local rows
  step7_deep.py             staged schedule, one exact-Q stage per local power
  step8_deepshot.py         one-shot depth-T system (adds the t^0 top band)
  step9_point.py            radical -> rational point, with side conditions
  deep_locus_T11.json       stages n = 8..11 (rows, pivots, residual, dim)
  point-deep_locus_T11_n{10,11}.json   the replacement rational points
  outer-visibility.json     kept coords, first r, D1 ladder length per block
  outer-first-row.json      first row carrying A2c_26_35, B2c_26_35, A3c_61_35
  ctl-replay-T8.json        A  rows_sha256 == charged saturated T8
  ctl-radical.json          B  rad(I) == <u,v>, both inclusions, I != <u,v>
  ctl-jband.json            C  single-pass J == frozen per-band J, t = 1..5
  ctl-fastpath.json         D  rows_sha256 == charged, through the fast path
  ctl-localcut.json         E  local_rows_fast == frozen local_rows
```

Timing: the wall is `qstar_reduce`, still `Expr`-based — 287 s at `n = 8`,
724 s at `n = 9`, 1,374 s at `n = 10`, 2,272 s at `n = 11`. Porting it to the sparse ring (as the
products already are) is the obvious next lever and would be worth roughly
another five local powers. It would not change the verdict: the binding
constraint is `J = 1` at `t`-power 178, not the depth.

<!-- BODY-END -->

## Seal

Charged inputs verified mechanically from the `.run.v2` receipt: 6/6 `OK`.
Fallacy guardrail: `FALLACY-v2.md` (1985 bytes). No ledger edit, no
`jc2-lean`, no `ideation-*`, no fleet worker. No new exit-price assertion, so
no `charge_basis=` line. All compute terminated.
