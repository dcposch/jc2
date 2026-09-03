# R3 Preprocess Lane, 2026-09-03

Status: `OPEN`, not `SATURATED-EMPTY`.

This lane attacked the three delta1'=0 two-point rows
`(21,14;15;6;k=4)`, `(24,16;18;7;k=4)`, and
`(27,18;21;8;k=4)` through the level-1 Moh R3 ODE chart.  I did not obtain
a complete covering-chain unit certificate for any row.  I also did not find
a surviving R3 component with a point.  Therefore no row is promoted to the
Theorem-1.2 honest 98-unknown chart, and no row is killed at level 1.

## Custody

MEASURED.  The frozen inputs in `/tmp/jc2-lane.upiUoe/inputs` were verified
mechanically from `xmodel/r3-preprocess-gpt55-20260903.run.v2`.  The manifest
was generated from the receipt's `charged_input_<i>_sha256=` and
`charged_input_<i>_basename=` lines with `awk`; `sha256sum -c` returned `OK`
for all 14 charged inputs.  The lane audit is
`box/r3pre-20260903/r3_preprocess_audit.json`; it records
`"all_ok": true` and manifest hash
`be8f9d9c7b0518fbc5b1c7cca99a788d60c5abe8bf2270d18cde840445137a0c`.

The frozen set contains charged full R3 scripts for rows 21 and 24 only:

```text
R3ode_21_14_15_6_k4_Q.sing          09aa99706819c08a433e1e21df94003865d2026787297168b0fa7ad6795500fa
R3ode_21_14_15_6_k4_mod32003.sing   719e094cbdc3fdd35b20c766755b5c826743082c2d5d012cf1f79c1760cd8752
R3ode_24_16_18_7_k4_Q.sing          0268e3d47b99c0892b89d229960648e95beeeb860a3d9ff2b37f0d4461fe38fb
R3ode_24_16_18_7_k4_mod32003.sing   af4a1cca33cd6bded366fcdb65a8eef63215a1365f024556889bbedde6f7cd3a
```

No `R3ode_27*` file is present in the frozen input directory.  I generated
row 27 full R3 scripts from the frozen `gate_ode.py` into
`box/r3pre-20260903/indep/`:

```text
R3ode_27_18_21_8_k4_Q.sing          1b2da87c849aa2156904b39e189fe7ecfb4a944ad0c2c1065da15b6d0cc8cd27
R3ode_27_18_21_8_k4_mod32003.sing   2029f497ebd6ad90442d37eff23267786c2288508f7ba84435aac13f6d5fb06a
```

## Chart Check

MEASURED/DERIVED.  In the descended coordinates `x=gamma`, `y=pi`, the
d'=2,e'=3 level-1 chart writes

```text
f = f2(y)*x^2 + lower x terms
g = g3(y)*x^3 + lower x terms
coeff_x4 J(f,g) = 2*f2*g3' - 3*f2'*g3.
```

The full R3 wrapper sizes are:

```text
row 21: a=12, b=18, unknowns excluding T = 31, equations = 29
row 24: a=14, b=21, unknowns excluding T = 36, equations = 34
row 27: a=16, b=24, unknowns excluding T = 41, equations = 39
```

The generic `deg_x J=4` control is
`box/r3pre-20260903/generic_degx_control.py`.  It uses the specialization
`f2=y^(2s)+1`, `g3=-y^(3s)` and returned:

```text
ROW 21_14_15_6_k4 coeff_x4_specialization=-36*y**17
ROW 24_16_18_7_k4 coeff_x4_specialization=-42*y**20
ROW 27_18_21_8_k4 coeff_x4_specialization=-48*y**23
GENERIC_DEGX_J_EQ_4_PASS
```

Thus the honest level-1 ansatz has `deg_x J=4` generically.  This is separate
from the A/B instrument failure: the charged reports correctly record
`deg_x J=2<4` in the A/B family for these rows.

## Preprocessing

DERIVED and implemented in `box/r3pre-20260903/r3_pade_branches.py`.  For
`s=V2'`, set

```text
F(z) = z^(2s) f2(1/z) = 1 + F1*z + ... + F_(2s)*z^(2s)
G(z) = -z^(3s) g3(1/z) = 1 + G1*z + ... + G_(3s)*z^(3s).
```

The coefficient map is declared, not name-matched:

```text
F_i = a_(2s-i)
G_i = b_(3s-i)
c is fixed
```

The R3 ODE becomes a single reciprocal coefficient system whose low equations
give affine `Q*` pivots on `G_1,...,G_(3s)`.  The pivot coefficients are the
rational constants `2,4,...,6s`; in characteristic zero their norms are those
integers, and no pivot-zero branch exists.  The modular prime 32003 divides
none of them.  No parameter-dependent leading coefficient was divided.

After these pivots, `G_j` is the coefficient `h_j` of `F^(3/2)` for
`j<=3s`.  The residual necessary and sufficient R3 branch equations are

```text
h_(3s+1) = ... = h_(5s-2) = 0
h_(5s-1) != 0
c = -2*(5s-1)*h_(5s-1).
```

The residual is positively graded by `wt(F_i)=i`, with `wt(c)=5s-1`.  The
open condition `c!=0` is equivalent on the residual to `h_(5s-1)!=0`.  If all
`F_i` vanish then `h_(5s-1)=0`, so the open chart is covered by the finite
first-nonzero branches:

```text
F_1=...=F_(r-1)=0, F_r=1, 1 <= r <= 2s.
```

This is a branch cover, not an unjustified unit division.  Each branch keeps
the Rabinowitsch equation `T*h_(5s-1)-1`.  A branch is declared empty only
when Singular returns `reduce(1,G)==0`; modular closures are typed modular
unless an exact characteristic-zero run also returned `[1]`.

The requested triangular/number-field continuation was not reached on these
R3 systems.  No base polynomial/factor-field chain was extracted for the
remaining low branches, because those branches timed out before yielding a
component or a unit ideal.

## Branch Results

All branch scripts and JSON run records are in `box/r3pre-20260903/`.
The summary below prefers exact characteristic-zero closures where present.
`MODULAR-EMPTY` means `[1]` over `GF(32003)` only.

```text
row (21,14;15;6;k=4), first range 1..12
  EXACT-EMPTY:       r = 4,5,6,7,8,9,10,11,12
  MODULAR-EMPTY:     r = 3
  OPEN/TIMEOUT:      r = 1,2
  details: r=1 GF(32003)/slimgb timeout 240.267s
           r=2 GF(32003)/slimgb timeout 60.117s
           r=2 GF(32003)/std timeout 180.164s
           r=2 GF(32003)/facstd timeout 120.119s

row (24,16;18;7;k=4), first range 1..14
  EXACT-EMPTY:       r = 5,6,7,8,9,10,11,12,13,14
  MODULAR-EMPTY:     r = 4
  OPEN/TIMEOUT:      r = 1,2,3
  details: r=1 not run after lower branches consumed cap
           r=2 GF(32003)/slimgb timeout 120.198s
           r=3 GF(32003)/slimgb timeout 60.226s
           r=3 GF(32003)/facstd timeout 120.139s

row (27,18;21;8;k=4), first range 1..16
  EXACT-EMPTY:       r = 6,7,8,9,10,11,12,13,14,15,16
  MODULAR-EMPTY:     r = 4,5
  OPEN/TIMEOUT:      r = 1,2,3
  details: r=1,2 not run after lower branches consumed cap
           r=3 GF(32003)/slimgb timeout 180.316s
```

No branch printed `BRANCH_NONEMPTY`; hence no dimension or point is available
from this lane.  The absence of a printed point is not a proof of emptiness.

The original centered row-21 residual script
`r3_21_14_15_6_k4_centered_c1_p32003.sing` was also tried directly.  It
timed out/interrupted after about 132 seconds and 1028844 KiB RSS without
`MAIN_DONE`; it is not used as a verdict.

## Controls

MEASURED.  The K=16 t=3 normalized K-field control was rerun from the charged
preprocessed script:

```text
CONTROL_ACTUAL_PAIR_PASS J=gamma
CONTROL_C_UNIT_PASS
CONTROL_EMPTY_PASS
CONTROL_NONEMPTY_PASS
CONTROL_RING_PASS RK
MAIN_START t=3 normalized_q4_1=1 coefficient_field=quadratic residual_equations=6 residual_unknowns=3
MAIN_DONE basis_size=
1
MAIN_QUADRATIC_FIELD_EMPTY
G[1]=1
TIME_SEC=0.07 MAX_RSS_KB=13064 EXIT=0
```

MEASURED.  The direct actual-pair control
`box/r3pre-20260903/actual_pair_control.sing` computes
`(f,g)=(pi, pi-gamma^2/2)` in `Q[gamma,pi]` and returned:

```text
CONTROL_ACTUAL_PAIR_PASS J=gamma
CONTROL_ACTUAL_PAIR_DEG_GAMMA_J=
1
CONTROL_ACTUAL_PAIR_TUPLE_FAIL_FOR_REQUESTED_K4
```

This is a wrapper/tuple negative control.  It is not evidence that this
actual pair belongs to any of the three `d'=2,e'=3,k=4` R3 charts.

## Verdicts

`(21,14;15;6;k=4)`: `OPEN[LOW-R3-BRANCH]`.  Exact-empty is known only for
first-nonzero branches `r>=4`; `r=3` is modular-empty only; `r=1,2` remain
open.  No saturated-empty theorem applies.

`(24,16;18;7;k=4)`: `OPEN[LOW-R3-BRANCH]`.  Exact-empty is known only for
`r>=5`; `r=4` is modular-empty only; `r=1,2,3` remain open.  No saturated-empty
theorem applies.

`(27,18;21;8;k=4)`: `OPEN[LOW-R3-BRANCH]`.  Exact-empty is known only for
`r>=6`; `r=4,5` are modular-empty only; `r=1,2,3` remain open.  No frozen
charged `R3ode_27*` input was supplied; the full scripts here are generated
from frozen `gate_ode.py`.

The theorem requested for the empty case would be: if the saturated R3 chart
for a row is empty over characteristic zero after a complete branch-covering
chain, then no monomial-Jacobian pair with that descended level-1 datum
satisfies Moh's `r=1` ODE with the required nonzero constant.  This lane does
not satisfy the hypothesis for any of the three rows.

## FALLACY-v2 Audit

No exit-price claim is made; no `charge_basis=...` line is due.

`sat()` wrapping: each first-nonzero branch is in its declared Singular ring
and includes `T*h_(5s-1)-1`.  The full R3 scripts include `T*c-1`.  Empty
claims are only made from `reduce(1,G)==0`.

Raw remainder degree: the residual equations are normal forms after the
declared `Q*` pivots on `G_j`; no parameter-dependent leader was shed.

Variable/ring map: the map `F_i=a_(2s-i)`, `G_i=b_(3s-i)` is declared above;
prime marks are labels.  The ODE derivative is the ordinary `y` derivative in
the univariate top-coefficient chart.

Floor/attainment: modular `[1]` is not promoted to exact `[1]` unless the
characteristic-zero run also returned `[1]`.  Timeout is not evidence of a
component or of emptiness.

Generated-artifact hashes are in
`box/r3pre-20260903/SHA256SUMS.generated`.

<!-- BODY-END -->
