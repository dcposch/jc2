# Branch B delta=2 kill gate for (99,66)

Date: 2026-09-03 UTC

Verdict: **CONFIRMED[DECLARED-NECESSARY-FINITE-CHART-KILL]**.

This report audits the stage-4 death of Moh branch B, `delta = 2`, split
`[2,1]`, packets `18 + 9`, in the charged joint `(99,66)` chart. The confirmed
theorem is scoped exactly as follows:

```text
No Keller pair of degrees (99,66) in Moh's gauge with
M = (-66,77,97), V = (8,8), and the delta=2 principal-minor split [2,1]
exists inside the declared joint chart.
```

It is not a theorem about the unrestricted Jacobian conjecture, not an
attainment claim, and not a `KELLER` or `REPRESENTATIVE` witness.

## Skeleton

- Degrees: `deg F = 99`, `deg G = 66`.
- Moh gauge skeleton: `M = (-66,77,97)`, `V = (8,8)`.
- Top two-line chart: `P = y^3(y-x)^8`, so
  `in F = P^9 = y^27(y-x)^72` and
  `in G = P^6 = y^18(y-x)^48`.
- Approximate-root chart:

```text
h3 = P + H
h2 = h3^3 + C2 h3 + C3
F  = h2^3 + A2 h2 + A3
G  = h2^2 + B1 h2 + B2
```

- Principal-minor branch: `delta = 2`, split `[2,1]`, face
  `p(pi)=pi^2(pi+3a)`, `q(pi)=pi^25(pi+3a)^14(pi-2a)`.
- Charged finite engine: `box/g9966band-20260903/band_engine.py`, SHA-256
  `3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9`.

## Custody And Drivers

`CONFIRMED[CUSTODY]`. I generated the 16-input checksum manifest mechanically
from `xmodel/g9966-branchB-kill-gate-gpt55-20260903.run.v2` by pairing its
indexed `charged_input_<i>_sha256` and `charged_input_<i>_basename` fields
with `awk`, then ran `sha256sum -c`. All 16 frozen files under
`/tmp/jc2-lane.NpHOYO/inputs` returned `OK`; no digest was retyped.

The pinned engine self-checks the earlier Sol lane
`/tmp/jc2-lane.cNPqDa/inputs`, which was no longer present. To avoid changing
the engine, I added
`box/g9966Bgate-20260903/reconstruct_sol_lane.py`; it parses the Sol receipt,
checks every repository file against that receipt, and recreates the expected
input lane as symlinks. The engine was not patched. The replay wrapper is
`box/g9966Bgate-20260903/run_delta2_stage.sh`; for stage `N` it executes:

```text
timeout 2400 /usr/bin/time -v -o box/g9966Bgate-20260903/runs/delta2/stageN.time \
  python3 box/g9966band-20260903/band_engine.py \
    --branch delta2 --stage N \
    --emit-singular box/g9966Bgate-20260903/runs/delta2/stageN.sing \
  > box/g9966Bgate-20260903/runs/delta2/stageN.json \
  2> box/g9966Bgate-20260903/runs/delta2/stageN.err
```

All stage jobs were run in the foreground, one at a time. The corrected run
directory `box/g9966Bgate-20260903/runs/delta2` validates with the charged
`validate_run_ledger.py`:

```text
status VALIDATED, final_verdict DEAD, stage_count 5
```

No ledger, `jc2-lean`, `ideation-*`, or named in-progress lane report was
edited.

## Replay

`CONFIRMED[EXACT-Q-REPLAY]`. The engine replays the charged 15-pivot endpoint
byte-identically to the frozen first-global-band result: rank `15`, residual
`0`, and `delta2_dimension = 6704 - 15 = 6689`
(`band_engine.py:90-101`). The staged continuation then gives:

| stage | pole `(F,G)` | Jacobian band | outer raw/rank | joint Q* cum | residue | dimension | wall/RSS |
|---:|---|---|---:|---:|---|---:|---:|
| 0 | `(-77,-50)` | `J162:k27` | `64/41` | 0 | 0 | 1065 | `68.21s / 72384K` |
| 1 | `(-76,-49)` | `J162:k28..162` | `52/38` | 9 | 0 | 1018 | `53.51s / 77048K` |
| 2 | `(-75,-48)` | `J161:all` | `40/33` | 18 | 0 | 976 | `76.03s / 82336K` |
| 3 | `(-74,-47)` | `J160:all` | `29/25` | 27 | 0 | 942 | `117.76s / 90944K` |
| 4 | `(-73,-46)` | `J159:all` | `20/19` | 35 | 118 constants | DEAD | `257.31s / 103876K` |

The requested dimension path is:

```text
1065 -> 1018 -> 976 -> 942 -> DEAD
```

`CONFIRMED[STAGE4-UNIT]`. Stage 4 has 659 cumulative joint labels, 513 raw
nonzero rows, 35 cumulative Q* pivots, 506 zero/dependent rows, and 118
residual rows. Every residual row is a nonzero integer constant; there are no
nonconstant residuals. The first residual is:

```text
stage4_J_d159_k35 = 6264
```

Thus `1 = (1/6264) stage4_J_d159_k35` in `Q`. The replayed stage-4
`all_labeled_rows_hash` and `residual_hash` match the frozen charged
`stage4.json` exactly:

```text
all rows: 26ab5cb622957b77dd558d9ea18f073f2380d0c1b1716e064674563f43365fc7
residue : 828864876f5068081c28aa1d2305ec124c96960000d714e0415f1a65effc25fe
```

`CONFIRMED[SINGULAR-REPLAY]`. The engine-emitted Singular file was replayed
independently under `timeout 2400`. It printed:

```text
BEGIN_DIM
-1
END_DIM
BEGIN_GB
1
END_GB
BEGIN_CONTROLS
0
1
0
END_CONTROLS
```

The output SHA-256 is
`236517b4a8e5567c586d39194059d49207001416a1d922efaec1fc3d2b9c7b73`.

## Necessity Audit

### Common h3 / Major h2

`CONFIRMED[NECESSARY-PREFIX]`. Moh Theorem 1.2 is used only as an order lower
bound: if `Q = h^d + sum Q_j h^(d-j)`, then
`ord Q_j(sigma_i) >= (lambda/d)j`. The charged design gate applies this to
the major tower as:

```text
ord h3(D2)=-1/3, ord h2(D2)=-1, ord F(D2)=-3, ord G(D2)=-2
ord h2(D1)=-1/9, ord A2>=-2/9, ord A3>=-1/3,
ord B1>=-1/9, ord B2>=-2/9
```

This is a necessary condition on any Keller pair in the skeleton because the
top forms and approximate-root tower are fixed. The simultaneous major block
starts from `21 + 187 + 308 = 516` variables after the `h3` rows; the projected
`h2` `D2` block has 389 unit-triangular `C2/C3` pivots after three identities,
and the first `h2` `D1` band has rank seven. Hence `516 - 389 - 7 = 120`.
The gate explicitly types these rows as a necessary prefix, not as a complete
system (`g9966-design-gate-grok46-20260903.md:91-121`).

### Outer D2 And D1 Rows

`CONFIRMED[NECESSARY-STRICT-OUTER-ROWS]`. The outer bridge imposes the same
Theorem 1.2 bounds on `A2,A3,B1,B2` at the major first point. For `D2`,
strictly below-threshold slots are set to zero; equality-face slots are not
set to a value. The report states the key distinction directly:

```text
Theorem 1.2 is >=; the equality face is allowed.
```

The imposed `D2` thresholds are `189,285,93,189`, giving 5598 unit coordinate
rows. The `D1` recentered finite gap has 225 raw slots and exact rational
rank 176; leftover rows reduce to zero. This is necessary order vanishing,
not equality-face attainment (`g9966-outer-bridge-grok46-20260903.md:114-187`).

### Direct Minor F,G Rows

`CONFIRMED[BRANCH-FACE-NECESSARY]`. The source review and review gate classify
the top principal-minor split. N5 supplies `den(delta) <= u_s = 3`; the ODE
and Galois screen leave, for `delta = 2`, only the `[2,1]` vector `(25,14)`.
Solving the face ODE gives:

```text
p = pi^2(pi+3a)
q = pi^25(pi+3a)^14(pi-2a)
```

The `(25,14)` vector is forced by the local order budget plus the extra-root
solve, not by analogy with Xu's generic all-simple iterate
(`g9966-review-gate-grok46-20260903.md:135-159`;
`g9966-source-review-opus5-20260903.md:158-201`;
`n5-gate-gpt55-20260903.md:8-20`).

The gauge issue is clean. The source review says `pi -> lambda*pi` sends
`a -> lambda*a`, so nonzero `a` may be normalized; the face is a single point
modulo that scaling. The charged stage engine is stronger than that: it does
not set the branch parameter to `1`. It keeps `rho` in the common `h3` leader
`zeta^2(zeta+3*rho)` and records `rho != 0` as the branch localization
(`band_engine.py:260-319`). Therefore an `a = 1` face presentation is a
licensed gauge, not a slice, and the replayed kill does not rely on it.

The direct `F,G` local rows are the necessary finite coefficients of:

```text
t^18 F(t^-1, u*t + z*t^2) = p(z)^9 + O(t)
t^12 G(t^-1, u*t + z*t^2) = p(z)^6 + O(t)
```

as continued into the next occupied pole bands. They impose only the branch
consequences of the classified face. They do not impose an unproved
`T2,T3 in K[F,G]` bridge; the Sol report explicitly leaves that bridge out.

### Direct Jacobian Rows

`CONFIRMED[CONSTANT-JACOBIAN-ROWS]`. The engine forms the normalized sparse
Jacobian:

```text
99*KF*(KG)_w - t*(KF)_t*(KG)_w
-66*(KF)_w*KG + (KF)_w*t*(KG)_t
```

(`band_engine.py:506-512`). The complete Keller condition is that `J(F,G)` is
constant; after the usual scalar normalization this is `J(F,G)=1`. All imposed
stage rows are high total-degree coefficients of that polynomial, so their
target is `0`. The constant `1`, or a free nonzero Jacobian scalar `kappa`,
contributes only in degree zero and is not touched by the bands `J162` through
`J159`. Thus the stage-4 contradiction does not invert or set a Jacobian
constant. The symbol `c` in the band engine is the `delta=5/2` branch
parameter, not a Jacobian scalar; there is no `c` in the replayed `delta=2`
branch.

The source-review N5 paragraph proposing a separate local
`J_{y,z}(Fbar,Gbar)=c` computation is not consumed by this kill
(`g9966-source-review-opus5-20260903.md:345-352`). The stage-4 rows are the
global sparse Jacobian coefficient rows appended in `cumulative_rows`
(`band_engine.py:702-720`).

### Pole Rows

`CONFIRMED[LOWER-POLE-VANISHING]`. The pole labels are grouped by normalized
local power. For `delta=2`, the engine shifts local powers by `81` for `F`
and `54` for `G`, corresponding to the leading factors `t^18 F` and
`t^12 G`; a row is included only when the raw local exponent is still
nonpositive (`band_engine.py:569-582`). Stage 0 therefore asserts the next
below-leader branch exponents `(-77,-50)`; stages 1-4 continue
`(-76,-49)`, `(-75,-48)`, `(-74,-47)`, `(-73,-46)`
(`band_engine.py:666-682`).

These rows say that no forbidden lower pole term occurs in the prescribed
principal-minor expansion. That is necessary for a Keller pair in this branch
because the branch leading polynomial has already been fixed by the split
classification. They are not equality-face rows and do not assert existence
of a polynomial map.

### Q*-Pivot Rule

`CONFIRMED[QUOTIENT-RING-ISOMORPHISMS]`. The reducer chooses a pivot only when
the coefficient is rational and nonzero:

```text
if not coefficient.is_Rational or coefficient == 0: continue
```

(`band_engine.py:191-220`). Such a row has the form `a*x + b` with `a in Q*`,
so eliminating `x` is the quotient-ring isomorphism
`A/(a*x+b) ~= A_without_x` with `x` mapped to `-b/a`. No branch parameter is
inverted by this step.

The replayed stage-4 new pivot coefficients are:

```text
8, -684, -585, -486, -387, -288, -189, -90
```

All 35 cumulative pivot coefficients are nonzero rationals. The charged
validator also checks the pivot-ledger shape, cumulative row accounting, and
dimension formulas for every stage.

## Localisation And The Unit Residue

`CONFIRMED[PRELOCALIZED-UNIT]`. The key line is in the stage runner:

```text
localized = symbol("rho" if branch=="delta2" else "c")
residual, linear_map, pivots, zero_rows =
    qstar_reduce(rows, set(all_free)-{localized})
```

(`band_engine.py:749-750`). The engine then asserts that the localized
parameter remains among the generators (`band_engine.py:751-754`). Only after
Q* reduction does `singular_dimension` add the wrapper `Zrho*rho-1` or
`Zc*c-1` (`band_engine.py:616-626`).

In the replayed `delta=2` stage 4, no pivot variable is `rho` or `c`, and the
118 residual expressions are all integer constants before Singular sees the
localization wrapper. Since `6264` is already a unit in `Q`, the unlocalized
residue ideal is the unit ideal. Localizing at `rho != 0` cannot create or
remove this contradiction; it only localizes the zero quotient. The kill
therefore does not depend on assuming `rho != 0`, and it does not involve any
assumption about `c != 0` because `c` belongs to the other branch.

## Hidden Specialisation Audit

`CONFIRMED[NO-UNLICENSED-SPECIALISATION]`.

- `P = y^3(y-x)^8` and the placement of the principal-minor line at `y=0` are
  linear/torus gauges of the two fixed lines at infinity, not row cuts. The
  design gate explicitly says the chart's minor-at-`y=0`, major-at-`y=x`
  convention is a linear gauge (`g9966-design-gate-grok46-20260903.md:77-85`).
- The missing `h3^2` and `h2^2` terms are characteristic-zero approximate-root
  normalizations, not discarded components.
- The split datum `delta=2`, `[2,1]`, `(25,14)` is the audited branch
  hypothesis forced by N5 plus the ODE/Galois split classification. It is not
  a numerical specialization inside the branch.
- The face parameter `a` may be set to `1` after `pi`-scaling when `a != 0`,
  but the charged stage replay keeps `rho` symbolic and never pivots on it.
- No value is substituted for `u`, `rho`, any outer coefficient, or a Jacobian
  scalar. The stage-4 residue is constant before any parameter localization.
- The source-review suggestion to gauge `c=1` in a future `delta=5/2` local
  N5 computation is not used by the `delta=2` stage-4 kill.

## Delta=5/2 Sanity Contrast

`CONFIRMED[BRANCH-SPECIFIC-KILL]`. The same pinned engine, common major rows,
outer `D2/D1` construction, pole-row mechanism, Q* reducer, and Jacobian row
builder were used for the charged `delta=5/2` branch. The branch data differ:
the common leader is `pi(pi^2-c)`, `c != 0`, with the `mu_2`-stable `[1,1,1]`
split. Its validated charged ledger remains consistent through stage 7:

```text
1063 -> 1016 -> 974 -> 940 -> 913 -> 894 -> 880 -> 869
```

All accepted `delta=5/2` stages have zero residue, and the next stage-8 system
is merely an executable manifest:

```text
python3 box/g9966band-20260903/band_engine.py --branch delta52 --stage 8
```

This contrast rules out the cheap explanation that the stage-4 death is an
artifact of the engine, the common outer rows, or the Q* pivot rule. The
observed difference is caused by the branch data.

## FALLACY-v2 Check

Flag/place/series: the major tower, the principal-minor split, the pole
filtration, and the Jacobian homogeneous filtration are kept separate.

Floor/attainment: Theorem 1.2 supplies `>=` bounds. Strict-below rows are
vanishings; equality faces are imposed only where the fixed leading form
requires them, and outer equality faces are deliberately not imposed.

Carrier/attainment: finite compatible prefixes are not promoted to actual
Keller maps. The `delta=5/2` survivor is only a counting-bound quotient.

`sat()` wrapping: the only wrapper used in the kill is the explicit
Rabinowitsch localization in the emitted Singular script, with empty/point/raw
controls. The unit constant appears before that wrapper.

Variable/ring map: computations are over `Q`; `K2c` is the declared
unit-triangular major basis; the report does not claim an unavailable full
inverse map back to all original `C2,C3` coefficients.

Prime mark/derivative: `p'` and `q'` in the split-face ODE mean `d/dpi`.

No exit-price assertion is made, so no `charge_basis` line is applicable.

## Final Verdict

`CONFIRMED`. Every imposed row family used by stages 0-4 is a necessary
condition for a Keller pair with the declared `(99,66)` skeleton and the
`delta=2` principal-minor split. All linear eliminations are Q*-pivot
quotient-ring isomorphisms. No unlicensed gauge, slice, or numerical
specialization is used. Stage 4 produces a genuine nonzero integer constant
in the unlocalized residue ideal, and Singular independently returns
dimension `-1` with basis `1`.

Therefore the stated theorem holds in the declared chart:

```text
No Keller pair with the (99,66) skeleton and the delta=2 principal split exists.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15235`.
- Body SHA-256:
  `b99a98ee8dd07585110638499e0deef4fa59774c8e444e4edbcd097ccc40bb39`.
- Frozen basis: `f899e3c3b973d2be4df5f6aa532679e9c80e5bec`.
