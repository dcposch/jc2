# Leading pole row: coefficient minus the forced face

Grok 4.6 · 2026-09-05 · lane `band-leading-row-fix-grok46-20260905` · receipt basis `b33df0cc`

**Disposition: `INSTRUMENT-FIXED`.** The cone-vertex gate's leading-row defect is
repaired in the three band engines and in the frozen g108 compiler. The top
pole tag is now emitted as `coefficient − target`. Every strictly-lower pole
row is byte-identical to the old homogeneous emission. Controls (a)(b)(c) all
pass over `Q`. The only verdict this changes is the spurious `UNIT` the gate
named at stage 92/60 (D=108) and 77/50 ((99,66) δ=2). No ledger edit; no
`jc2-lean`; no `ideation-*`; no fleet. No new exit-price assertion, so no
FALLACY-v2 `charge_basis=` line.

## 0. Custody

The manifest was built from the numbered `_basename`/`_sha256` fields of
`xmodel/band-leading-row-fix-grok46-20260905.run.v2` with `awk`, prefixed by
`lane_inputs_dir=/tmp/jc2-lane.om6PQa/inputs`. `sha256sum -c` returned `OK` on
all five frozen inputs; no content mismatch.

```text
72dfcd371f338767e303c6da0eab02337f257ad29409a9fc6b60cd2e85c20ecd  cone-vertex-gate-opus5-20260905.md
078f179d36ba99d3069ded660b72f3f8bb8b28d4593b2d5c5c1f87a6c68bf0b8  joint-chart-degenerate-fable5-20260905.md
d26c3dd22893b474d70806f21474092ec55d8acfb7dd6be046ff208deb991b05  d108-delta3-rekill-opus5-20260905.md
3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9  band_engine.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
```

## 1. Location

`raw_minor_support` lists the leading local power among its tags:

```text
D=108 δ=3     F n=96  k=0..23 (1200 tags)    G n=64  k=0..15 (544 tags)
(99,66) δ=2   F n=81  k=0..26 (1134 tags)    G n=54  k=0..17 (513 tags)
(99,66) δ=5/2 F n=189 k=1..25                G n=126 k=0..16
```

The sibling emitters then wrote a homogeneous `= 0` row, with no target
anywhere in the engine:

| engine | emitter | old line |
|---|---|---|
| `box/d108-rekill-20260905/work/rekill_engine.py` | `step3_joint.py:94,109`, `step4_saturated.py:45` (also `step5`/`step6`) | `table.get((n,k), 0)` |
| `box/g9966-repair-gate-20260905/corrected_face_engine.py` | `cumulative_rows` prior/stage | same |
| `box/g9966band-20260903/band_engine.py` | `cumulative_rows:737,753` | same |
| frozen `box/g108gate-20260903/band_engine.py` (and `g108band`) | no F/G pole emitter (`main()` is stage-0 terminal); metadata already said `subtract p^12 at F local 96 and p^8 at G local 64` | — |

The top monomial of the face (`π^{24}` of `p^{12}`, `ζ^{27}` of `(ζ²(ζ+3ρ))^9`)
is *not* a tag. The unit is the tagged constant term: at D=108, `[π^0](π²−c)^{12}
= c^{12}`, which is `1` at the gate's witness `c=1`. That is the same `1=0` the
gate saw as `[π^8](π²−c)^4`.

## 2. The fix

Shared helper `box/band-leading-fix-20260905/leading_pole.py`, copied into each
engine as `pole_coeff` (engines stay import-self-contained). At the leading
local power only:

```text
pole_coeff(table, n, k, name) = table[(n,k)] − [var^k](forced face)
```

and `table.get` otherwise. Forced faces, from gate §6 and rekill §7:

```text
D=108:     F  (π²−c)^12 at 96     G  (π²−c)^8 at 64
(99,66) δ=2:  F  (ζ²(ζ+3ρ))^9 at 81   G  (ζ²(ζ+3ρ))^6 at 54
(99,66) δ=5/2: F  (π(π²−c))^9 at 189  G  (π(π²−c))^6 at 126
```

No new tags were added (the untagged top monomial is `1=1` on Δ after
subtraction would have been applied; leaving it untagged does not restore the
unit). Jacobian rows, outer D1 rows, and h3 incidence are untouched.

**Diffs (in place).** Header comment plus `leading_pole_power` /
`leading_pole_target_table` / `pole_coeff` after `raw_minor_support`, and the
one-token emitter swap `table.get((n,k),0)` → `pole_coeff(...)`.

```text
g9966band-20260903/band_engine.py          +40 / −2   (emitter + helper)
g108gate-20260903/band_engine.py           +33        (helper; no emitter)
g108band-20260903/band_engine.py           +33        (helper; no emitter)
d108-rekill-20260905/work/rekill_engine.py helper after raw_minor_support
  step3_joint.py, step4_saturated.py,
  step5_witness.py, step6_sat_witness.py   emitter calls pole_coeff
g9966-repair-gate-20260905/corrected_face_engine.py
                                          helper + cumulative_rows:799,815
```

`git diff` on the charged (99,66) engine is the two `rows.append` lines and the
helper; every other row-construction site (`h2_D1`, outer D1, Jacobian) is
unchanged.

## 3. Controls (exact `Q`)

**Identity (instant).** `pole_coeff == table.get` at every `n` other than the
lead, on a sentinel dummy table, for all four engine copies. Target tables
match the faces: D=108 `[π^{24}]p^{12}=1`, `[π^0]=c^{12}`; δ=2
`[ζ^{27}](ζ²(ζ+3ρ))^9=1`. Shared helper == engine copy. Artifact:
`ctl_identity.json`.

**(a) Old-radius D=108 stage-0 still `[1]`.** Stage 0 has pole local power 4,
strictly below 64, so `pole_coeff` is `table.get`. Frozen cut-43 localized
groebner is `[1]` (7 coords, 12 nonzero rows, 7 pivots). Full joint at `wz=6`
stage 0: 21 rows, `dim=-1`, `UNIT=True`, `reduce(1,std)=0`. The pipeline can
still kill. `ctl_a_frozen_stage0.json`.

**(b) D=108 leading stage, leading row alone, Δ-witness.** Rebuilt the gate's
h2-only witness (`a_p=0` for `p<32`, `a_{32}=(π²−c)^4`; remaining free → 0,
`jet1=jet2=c=1`). Counts reproduce: 129 rows, 102 `Q*` pivots, residual empty,
`a_{32}=(π−1)^4(π+1)^4`. On Δ, `KF=K2^3` and `KG=K2^2` were cubed/squared at
the point and fed through `pole_coeff`.

```text
          n   stage  tags  old k=0  old nonzero (even k)     NEW
F lead   96    92     24     1      1,−12,66,−220,495,…     all 0
G lead   64    60     16     1      1,−8,28,−56,70,…        all 0
```

The old `k=0` value `1` *is* the spurious unit. After the patch every tagged
leading row vanishes by direct substitution. Polynomial identity
`((π²−c)^4)^3=(π²−c)^{12}` holds. `stage_spec(92/60)` pole powers are 96/64.
Leading row alone is not a unit. `ctl_b_d108_leading.json` (760 s).

**(c) (99,66) δ=2 corrected engine, likewise.** Gate witness: `a_p=0` for
`p<27`, `a_{27}=(ζ²(ζ+3ρ))^3`, arc `u=0`, `jet0=ρ=1`. Reduce: 76 `Q*` pivots,
residual empty (gate 76/0). `a_{27}=ζ^6(ζ+3)^3`. Leading coefficients are
`a_{27}^3` / `a_{27}^2` on Δ (`ord_t K2=27` exactly). Through `pole_coeff`:

```text
          n   stage  tags  old constants (k=18..26 / 12..17)   NEW
F lead   81    77     27   19683,59049,…,2268,324,27           all 0
G lead   54    50     18   729,1458,1215,540,135,18            all 0
```

Old `F` `k=26` is the constant `27`; old `G` `k=17` is `18`. Either is `1=0`
over `Q`. After the patch, all tagged leading rows vanish. `stage_spec(77/50)`
pole powers are 81/54. `ctl_c_g9966_leading.json` (370 s).

**FALLACY-v2 (instrument fix).** (a) preserves the old-radius unit. Historical
(99,66) kills at stage 4/8 sit at local power 8/16, far below 54, and are not
touched. No other row type was added or deleted. `sat()` is unused. Targets
are the K3-lead powers after the vertex class of each corrected chart (gate
§6), not an interior pole identity. Floor/attainment: the leading row is now
the equation `coeff = face`, verified by a witness covering every tagged
coefficient, not a bound.

## 4. Artifacts (`box/band-leading-fix-20260905/`)

```text
leading_pole.py                 canonical helper (d108_* / g9966_*)
ctl_identity.py / .json         n≠lead identity + face tables
ctl_a_frozen_stage0.py / .json  old-radius [1] + joint UNIT
ctl_b_d108_leading.py / .json   D=108 Δ-witness, leading F/G
ctl_c_g9966_leading.py / .json  (99,66) δ=2 Δ-witness, leading F/G
```

**VERDICT: `INSTRUMENT-FIXED`.** The three engines (and the frozen g108
compiler) now emit the leading pole tag as coefficient minus the forced F/G
face. The old-radius D=108 stage-0 unit still reproduces `[1]`. At the
corrected radii the leading rows at stage 92/60 and 77/50 vanish on the gate's
Δ-witness by direct substitution and no longer manufacture a unit.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8050`.
- Body SHA-256:
  `5c0957608daa68370c66a864097b9927b3a2c1d5203f22729322766fcd6cf495`.
- Frozen basis: `b33df0cc96fe9b180afc41758a00ee4d84edef49`.
