# `(8,12)` order two: nonsquare discriminant K3 elimination

Date: 2026-08-26

Status: **PRODUCER THEOREM.  THE NONSQUARE DISCRIMINANT FIRST-NORMAL
COMPONENT IS EXCLUDED ON THE FIRST-CONTACT OPEN.  THE SQUARE COMPONENT AND
THE REST OF ORDER TWO REMAIN OPEN.**

## 0. Charged results

Analytic K2 support and its scope repair:

```text
20fa404c10c6fdafe59247967db8234f3479ae9a06740b521650b8a8aa88e341
  xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-20260826.md
f93ecb4320fadff500638fc6fa7bdfca904ed5556b7a13add4cddb9b40a76b70
  xmodel/max12-812-order2-discriminant-halfweight-k2-support-review-terra-20260826.md
f1cbb203ca26c66c3c57178460912610ba978206043b2bf22bc1b2b73aaac68b
  xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-v2-20260826.md
```

Exact complete-source/analytic K2 row equality:

```text
6e00100d10f5d05b5351d2ca7fd8535a9b0df49671860d51862b73d64e6319c9
  cases/max12_812_order2_disc_halfweight_kuranishi_v3_row_identity_20260826/FREEZE.sha256
d0327db2e2214bc897be85d4373bf35e063c2a540254b2b33986f88755eca0e8
  cases/max12_812_order2_disc_halfweight_kuranishi_v3_row_identity_20260826/RESULT.md
6eb104a3288bf663aced9b8aa6f0bdac3a91c9cb6bd26d44e4b4989a5efe7c36
  cases/max12_812_order2_disc_halfweight_kuranishi_v3_row_identity_20260826/RESULTS.sha256
0763ca918737335ea7f77e08941cf568692d9fc67fbb6d85ab64ea35f1b7fe56
  exact-Q stdout
```

Normalized-ray source theorem and hostile confirmation:

```text
94fbced433f2677333417456f20b519d39ac8cc8650e745724a1104d87b34601
  xmodel/max12-812-order2-discriminant-halfweight-k3-normalized-ray-unit-theorem-20260826.md
c06739690386752ec336f8f8e5de58414ef4ed75ae48522ff616b13e38731691
  xmodel/max12-812-order2-discriminant-halfweight-k3-normalized-ray-unit-review-terra-20260826.md
```

The characteristic-32003 row endpoint is an independent control.  All
characteristic-zero claims below use the exact-Q coefficient identities.

## 1. Exact source ideal equals the analytic K2 ideal

Let `S_l` be the seven complete frozen-source half-weight K2 rows and let
`H_j` be the seven analytic negative-Laurent rows, normalized by the factor
sixteen used in the analytic theorem.  Put

```text
A=z-a,  b=4*a,  e=d+3*a^2,  v=1/w,  q=A/w.
```

Since `w^4=A^2(A^2+b*A+e)`, one has

```text
q^4+b*v*q^3+e*v^2*q^2=1.                            (1.1)
```

Expansion of `A^-j=v^j*q^-j` gives a lower unitriangular matrix
`T(b,e)` over `Q[b,e]`.  The exact-Q client verifies coefficientwise, before
any standard-basis or saturation operation,

```text
16*S_l=sum_(j<=l) T_(l,j)(b,e)*H_j,
l=1,...,7.                                           (1.2)
```

Because `16` is a unit and `T` is unitriangular, (1.2) proves equality of
the two seven-row ideals over Q.  This is a polynomial identity and remains
an equality after every localization and base change used below.  It
replaces the older exact-Q two-sided Groebner run, which timed out and has no
verdict.

## 2. The complete source K2 scheme on the discriminant open

Localize first by the first-contact coordinate `m`, and then on the
nonsquare discriminant chart by `b`.  By Section 1, the complete frozen
source rows have the same ideal as the analytic rows.  The repaired analytic
support theorem therefore applies in

```text
R_bm=Q[b,e,h,y,kappa,m][(b*m)^(-1)].
```

After its two triangular complementary rows are solved, the exact raw K2
scheme is

```text
(kappa,e,U^2,F),
U=h+b*y,
F=m^3+6*h*y+6*y*U.                                  (2.1)
```

Its reduced support is exactly

```text
e=kappa=U=F=0,
m=6*b*t^2,  y=6*b*t^3,  h=-6*b^2*t^3,
b*t!=0,                                               (2.2)
```

where `t=y/m`.  The two free complementary-kernel parameters retained by
the source are not specialized in the successor calculation.

The locus `m=0` is the removed zero-normal section, not a missing
first-contact point.  On `b=0,e=0`, the quartic is `K=A^4`, so this is the
square intersection and is routed to the square analysis.

## 3. Exhaustive correction-aware K3 obstruction

For the local triangular complete intersection (2.1), every formal or
Puiseux successor must satisfy

```text
ord(e),ord(kappa),ord(F)>=ord(rho),
2*ord(U)>=ord(rho).                                  (3.1)
```

Thus the only new primitive fractional normal ray is represented, after a
common ramified base refinement, by

```text
rho=sigma^2,
wt(U,e,kappa,F)=(1,2,2,2).                           (3.2)
```

Strict inequalities are coordinate faces of this chart.  The reviewed
normalized-ray client retains all normal corrections and the first tangent
motion along (2.2), reconstructs all seven complete source rows, and checks
their exact Laurent-to-Faber transforms before unit saturation.

Its last three analytic rows are, with `W=U1^2` and
`c_n=binom(5/2,n)b^n`,

```text
L5=-6*b*W-216*b^3*t^7+16*chi*c15,
L6= 6*b^2*W            +16*chi*c16,
L7=-6*b^3*W            +16*chi*c17.                 (3.3)
```

Since `c17=-(27/34)b*c16`, the combination `b*L6+L7` forces
`chi=0` on `D(b)`.  Then `L6` forces `W=0`, and `L5` becomes the nonzero
monomial `-216*b^3*t^7`.  Hence the complete source successor ideal is the
unit ideal on `D(b*t)`.  The argument retains the raw doubled direction; it
does not replace `U^2` by its radical.

## 4. Conclusion and firewall

Combining Sections 1--3 gives the unconditional source conclusion:

> In the source-typed `U=2`, terminal profile `[6,2]`, exact-order-two
> client, the entire nonsquare discriminant first-normal component is
> excluded on the first-contact open `D(b*m)` by its correction-aware K3
> necessary tail gate.

No later lower load, scalar target, terminal row, or Taylor condition can
restore a branch whose necessary tail ideal is already the unit ideal.

This theorem does **not** exclude the arbitrary-load square component or
its `b=0` intersection, finish either finite Taylor receiver globally,
close all exact order two, close `(8,12)`, prove maximum twelve, or prove
JC2.  The highest-value successor is the correction-aware square route.
