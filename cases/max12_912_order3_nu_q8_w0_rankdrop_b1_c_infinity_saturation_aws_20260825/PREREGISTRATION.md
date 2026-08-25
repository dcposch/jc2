# Preregistration: pointed coefficient-infinity selected closure

Date: 2026-08-25

## Exact construction

Start from the pinned six-row source `(e1,e3,e5,e7,e2,e4)` **before any
specialization in the coefficient `c`**.  Introduce homogeneous coefficient
coordinates `[C0:C1]`, replace every monomial `c^k` in row `e_i` by
`C0^k*C1^(d_i-k)`, where `d_i=deg_c(e_i)`, and verify

```text
(d1,d3,d5,d7,d2,d4)=(1,2,3,3,2,2).
```

Then substitute the pointed moving-rank-drop chart

```text
d4=1+v,  d2=2+v+u.
```

Let `A=x3-2*x5` and `f=w*x5*A`.  The closure of the affine selected open
`C1*f != 0` in the coefficient-projective chart is computed source-honestly as

```text
Ibar = I^h : (C1*f)^infinity
```

using the Rabinowitsch ideal
`I^h+(zinv*C1*f-1)` and contraction of `zinv`.  Saturating by the product is
the same as sequential saturation by `C1` and by `f`.  Only **after that
contraction** impose the coefficient-infinity chart `C0=1,C1=0`.  Finally
test the pointed landing centre `v=w=u=x1=x3=x5=0`.

Run complementary exact characteristic-zero `std/dp` and `slimgb/block`
lanes.  Print the complete contraction, infinity-chart, and landing bases.
Require rc zero, exact source regeneration, and no diagnostics.

## Scope

A unit infinity-chart ideal excludes coefficient-infinity points in this
pointed affine coefficient/rank-drop chart of the selected closure.  A unit
landing ideal excludes only the displayed centre.  A survivor is routing,
not an actual Taylor/terminal trajectory.  Nothing here covers other
rank-drop centres, other projective coordinate boundaries, Taylor/terminal
realization, trajectories, the full `(9,12)` cell, maximum twelve, or JC2.
