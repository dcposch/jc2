# Hostile review — selected Q8 `b=1` slope-two next-order control

Reviewer: Grok via the read-only external review adapter  
Verdict: **CONFIRMED**  
Repairs: **none**

This file is a custody-preserving substantive transcription of the streamed
session-48248 review.  The adapter output was returned in two chunks and was
not independently frozen as one raw byte stream; the companion `.run` makes
that limitation explicit.

## Scope actually confirmed

After locking the selected slope-two leading cone at
`(d2,d4)=(2,1)`, normalizing `x5=t`, and allowing the displayed ordinary
first jets, the six next Taylor coefficients generate `(1)` over `Q`, for
every finite constant term `c`.  This proves no ordinary `k[[t]]` point of
that exact shape.  It does not exclude ramified/mixed-order Puiseux arcs,
moving earlier base coordinates, full horizontal saturation, coefficient
infinity, terminal/Taylor realization, trajectories, all `(9,12)`, maximum
twelve, or JC2.

## Source and coefficient convention

The reviewer checked that the pinned compiler imposes exactly rows
`(1,3,5,7,2,4)` and that the frozen Singular map is

```text
w  -> -4/9*t^2 + W3*t^3
c  -> c + C1*t
d2 -> 2 + (B1+Q1)*t
d4 -> 1 + B1*t
x1 -> U2*t^2
x3 -> 5/3*t + X2*t^2
x5 -> t.
```

Thus `u=d2-d4-1=Q1*t`.  Odd leading/next orders are `t,t^2`; even
leading/next orders are `t^2,t^3`.  The extractor divides the `k`th
derivative by `k!`, so it returns the Taylor coefficient, not a raw
derivative.  Every displayed leading coefficient vanishes identically.

Within the strict ordinary normalization `x5=t`, the first-jet list
`C1,B1,Q1,U2,X2,W3` is complete.  A term `x5=t+Z2*t^2+...` is absorbed by
reparametrizing with `s=x5`.  `C1` is present but invisible at this depth.
Earlier motion of `c,d4,u` relative to `x5` requires a ramified/mixed-order
chart and is outside the theorem.

## Exact next coefficients and unit

The reviewer independently re-expanded all six frozen coefficients:

```text
n1 =  4/81*c  - 8/27*B1 - 4/27*Q1 + 4/9*U2             - 4/27
n3 = 184/243*c +16/81*B1 -16/81*Q1 + 4/27*U2            -56/729
n5 =  4/729*c - 8/243*B1+68/243*Q1 + 4/81*U2           +116/729
n7 =  8/6561*c-16/2187*B1-224/2187*Q1+8/729*U2         +152/2187
n2 = 64/243*c             -4/27*U2 -4/27*X2 +2/9*W3    +16/243
n4 =-64/729*c            -20/81*U2+28/81*X2+4/27*W3   +124/729.
```

The even pair has invertible `(X2,W3)` determinant `-8/81` and creates no
constraint on `(c,U2)`.  Clearing denominators in the three odd equations
`n1,n5,n7` gives

```text
P1: c - 6*B1 -  3*Q1 + 9*U2 =   3
P5: c - 6*B1 + 51*Q1 + 9*U2 = -29
P7: c - 6*B1 - 84*Q1 + 9*U2 = -57.
```

The first two force `Q1=-16/27` and
`c-6*B1+9*U2=11/9`; substitution into the third gives the nonzero constant
incompatibility `108`.  Hence already `(n1,n5,n7)=(1)`.  `GNext=(1)` is an
exact unit basis.  Elimination to `Q[c]` is then tautological and is not an
exceptional-`c` calculation.

## Independence and custody

The accepted endpoints are Box02 `std/dp` and Box03 `slimgb/block`, on
different AWS hosts with rc0, empty generator stderr, no diagnostic pattern,
the same pinned compiler/parent, and identical coefficient blocks.  The
frozen replay regenerates both scripts and audits their hashes/markers; it is
custody-only, not a third CAS.  V1 permission failures generated no inputs and
remain software negative controls.

## Reconciliation with the ramified audit

The surviving raw leading cone is

```text
(X1, 3*X3-5*X5, 9*W+4*X5^2).
```

This case normalizes the `D(X5)` ordinary chart and proves that cone has no
next ordinary lift.  It does not contradict the raw audit's
`NOT_CONFIRMED`: earlier coefficient drift and mixed-order/Puiseux
realisations remain outside the chart.  The smallest exact closer is the
already-registered pointed moving-coefficient saturation

```text
d4=1+v, d2=2+v+u,
sat((e1,e3,e5,e7,e2,e4), w*x5*(x3-2*x5)),
landing (v,w,u,x1,x3,x5)=0
```

over `Q[c,...]`, together with the line-level moving-`b` companion.  A frozen
`d4=1` saturation or another finite jet cannot close arbitrary ramification.

**CONFIRMED**
