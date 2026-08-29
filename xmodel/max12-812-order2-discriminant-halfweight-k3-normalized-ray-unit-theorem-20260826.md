# `(8,12)` order two: discriminant K3 normalized-ray source unit theorem

Date: 2026-08-26

Status: **PRODUCER THEOREM FOR THE EXPLICIT NONSQUARE DISCRIMINANT SOURCE
BRANCH.  EXHAUSTIVE DISCRIMINANT PROMOTION IS CONDITIONAL ON THE FROZEN
EXACT-Q K2 SOURCE/ANALYTIC EQUALITY ENDPOINT.  NO ORDER-TWO VERDICT.**

## 0. Charged artifacts

```text
a2c1749993807ee9f8398d99f8e8e459d56252974a9efd6196a2c0ea89aa6ae2
  xmodel/max12-812-order2-discriminant-halfweight-k3-correction-aware-design-20260826.md
13ae545507753ccc60a44c3495ce6a2afdfb3b1ac9fc60e1e838b3c7953b374a
  cases/max12_812_order2_disc_halfweight_k3_normalized_ray_20260826/FREEZE.sha256
1f8dc7e3b5436490dc53b7c828d122bde4022d042d74c1fe7069e034861d0008
  cases/max12_812_order2_disc_halfweight_k3_normalized_ray_20260826/RESULT.md
bdb33aa6d3731ded2155825d87c11e7f4a7a6851924b8b131daab94fb5d42ca8
  cases/max12_812_order2_disc_halfweight_k3_normalized_ray_20260826/RESULTS.sha256
f1cbb203ca26c66c3c57178460912610ba978206043b2bf22bc1b2b73aaac68b
  xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-v2-20260826.md
```

The exact-Q stdout and the independent characteristic-32003 stdout are
byte-identical, with SHA
`8e03635fab8e3158f8df5ce74b6c888dbcd5640a72131004e1078c03a55bdf7f`.
The exact-Q lane is the characteristic-zero producer endpoint; the prime
lane is a control, not a lifting argument.

## 1. Local K2 scheme and the necessary normalized ray

On the first-contact open `D(m)` and the nonsquare triple-root open `D(b)`,
the exact analytic K2 ideal after triangularly solving its first two rows is

```text
I_K2=(kappa,e,U^2,F),
U=h+b*y,
F=m^3+6*h*y+6*y*U.                                  (1.1)
```

Its reduced support is parametrized by

```text
m=6*b*t^2,   y=6*b*t^3,   h=-6*b^2*t^3,   x=-2*b*t,
b*t!=0.                                               (1.2)
```

The raw square `U^2` in (1.1) is load-bearing.  If `rho` is the existing
half-weight parameter, a Puiseux lift may have `U` of order `rho^(1/2)`.
The primitive correction chart is therefore

```text
rho=sigma^2,
wt(U,e,kappa,F)=(1,2,2,2).                           (1.3)
```

This chart also contains the ordinary successor as the closed subchart in
which the weight-one coefficient of `U` is zero.  More generally, after the
K2 rows vanish, any correction capable of cancelling the intrinsic
`rho^7` term must satisfy

```text
ord(e),ord(kappa),ord(F)>=ord(rho),
2*ord(U)>=ord(rho).                                  (1.4)
```

If one inequality is strict, its initial coefficient is simply zero in
(1.3); if all are strict, the intrinsic row remains by itself.  Corrections
violating (1.4) encounter an earlier nonzero initial form of (1.1).  Thus
the normalized chart (1.3), including its coordinate faces, is the smallest
exhaustive successor of the *local analytic scheme* (1.1) at this grade.
This is not a claim that normalizing the analytic component alone covers an
unverified full source ideal; that is the separate promotion gate in
Section 4.

## 2. Exact source calculation

Retain the two free complementary-kernel parameters `q,s`.  The nested
source section is the one displayed in the charged design: it uses

```text
M=6*b*t^2-6*sigma*t*xi+sigma^2*nu,
X=-2*b*t+sigma*xi+sigma^2*omega,
Y=6*b*t^3,                                            (2.1)
```

and the exact triangular complement through weight two.  The raw variables
have

```text
U1=9*b*t^2*xi,
F2=36*b^2*t^4*nu+216*b^2*t^5*omega
   +432*b*t^4*xi^2.                                  (2.2)
```

The compiler also inserts independent first tangent coefficients in
`b,t,q,s`.  Every complete-source `sigma^14` row is independent of them;
their first possible change to the intrinsic coefficient is
`sigma^15`.  The exact-Q endpoint verifies this rather than freezing the
tangents silently.

After multiplying by sixteen, let `L_j` be the seven negative `A^-j`
coefficients.  Put

```text
W=U1^2,
c_n=binom(5/2,n)*b^n.                                (2.3)
```

The last three are exactly

```text
L5=-6*b*W-216*b^3*t^7+16*chi*c_15,
L6= 6*b^2*W             +16*chi*c_16,
L7=-6*b^3*W             +16*chi*c_17.                (2.4)
```

This is not inferred from the analytic ideal after it becomes unit.  For
each of all seven rows the exact-Q client reconstructs the complete frozen
Faber tail and verifies, before any unit saturation,

```text
16*S_l=sum_(j<=l) T_(l,j)*L_j.                       (2.5)
```

Here `T` is the exact unitriangular Laurent-to-Faber matrix obtained from

```text
qv^4+b*w^(-1)*qv^3=1,       qv=A/w.                  (2.6)
```

All seven identities, the truncated inverse identities used in the
complement, the `sigma^12` divisibility/base zero, the `sigma^13` kernel
zero, and the raw formulae (2.2) pass in exact characteristic zero.

## 3. Unit certificate

The load recurrence gives

```text
c_17=-(27/34)*b*c_16,
b*c_16+c_17=(7/34)*b*c_16.                           (3.1)
```

Since `c_16` is a nonzero rational multiple of `b^16`, equations (2.4) on
`D(b)` imply successively

```text
b*L6+L7=0  =>  chi=0,
L6=0       =>  W=0,
L5=0       =>  -216*b^3*t^7=0.                      (3.2)
```

The last equation contradicts `b*t!=0`.  Consequently both the analytic
seven-row ideal and the complete frozen-source seven-row ideal are the unit
ideal after adjoining the inverse of `6*b*t^2`.  There is no formal or
Puiseux K3 successor in the explicit source branch (1.2), including the raw
square-zero `U` direction.

## 4. Promotion, routing, and exact scope

The full-source K2 V2 package has freeze SHA
`bbaa31fa56398f255b47d6d74307149bd35166272f6bcf7ae73a9957193739e6`.
Once its exact-Q, fail-closed endpoint proves equality of the seven pulled
source K2 rows with the analytic K2 ideal, the analytic support theorem plus
this theorem gives the following corollary:

> Every nonsquare discriminant K2 point on `D(b*m)` is excluded at its
> correction-aware K3 gate.

Until that endpoint is retrieved and frozen, the corollary is conditional;
the explicit source unit result of Section 3 is unconditional.

The omitted `b=0,e=0` locus has `a=d=0` and `K0=A^4`; it belongs to the
rank-two square analysis.  It is routed, not declared empty here.  The
contact-zero locus `m=0` was removed by the charged first-contact
saturation.

The lower loads `k6,k2`, scalar targets, terminal `J/4`, and both Taylor
families do not enter this low grade.  Because the necessary tail ideal is
already unit, they cannot restore this explicit branch.  This theorem does
not analyze the square route, close all order two, close `(8,12)`, prove
maximum twelve, or prove JC2.
