# `(8,12)` order two: correction-aware discriminant K3 normalized-ray design

Date: 2026-08-26

Status: **EXACT HAND DERIVATION AND SOURCE-TYPED AWS DESIGN.  THE THREE-ROW
UNIT CERTIFICATE IS A PRODUCER CANDIDATE UNTIL THE COMPLETE FROZEN-TAIL
SOURCE COMPARISON PASSES.  FULL DISCRIMINANT COVERAGE ALSO AWAITS THE
EXACT-Q K2 SOURCE/ANALYTIC PROMOTION GATE.  NO ORDER-TWO VERDICT.**

## 0. Charged inputs and purpose

This design consumes the analytic half-weight formula and the repaired K2
support statement:

```text
ddbc758039621f70eae586b5482be3bfdd92754e990cdb015fa4c6d2e0eac0b1
  xmodel/max12-812-order2-discriminant-rank-halfweight-kuranishi-20260826.md
f1cbb203ca26c66c3c57178460912610ba978206043b2bf22bc1b2b73aaac68b
  xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-v2-20260826.md
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/
  aws_compile_v2_jsat/run/output/compiled_v2/tails.json
```

On `D(b*m)` the exact analytic K2 ideal, after the two triangular
complementary rows are solved, is

```text
(kappa,e,U^2,F),
U=h+b*y,
F=V+6*y*U=m^3+6*h*y+6*y*U.                         (0.1)
```

Its reduced support is

```text
e=kappa=U=F=0,
h=-b*y,
6*b*y^2=m^3.                                        (0.2)
```

The purpose here is to construct the smallest successor which retains the
square-zero direction `U`, rather than substituting only the radical.  The
result is a normalized weighted ray.  Its last three analytic rows have an
elementary unit certificate on `D(b*m)`.  The AWS client must reproduce
those rows from all seven complete frozen Faber tails before the certificate
is promoted.

The full-source K2 V2 freeze has SHA
`bbaa31fa56398f255b47d6d74307149bd35166272f6bcf7ae73a9957193739e6`.
Its exact-Q source/analytic equality endpoint is a coverage gate: without
that endpoint, this design excludes only the explicitly parametrized source
branch, not every source point represented by the analytic K2 ideal.

## 1. Opens, routing, and the reduced source section

Use

```text
A=z-a,                 b=4*a,
Q=A^2+b*A+e,
K0=A^2*Q,              N0=m*A*Q.                    (1.1)
```

The first-contact ideal pulls back to `(m)` on the discriminant family.
Thus `m!=0` is not a generic convenience: it is exactly the contact-one
open.  On the reduced K2 survivor, (0.2) gives the rational coordinates

```text
m=6*b*t^2,
y=6*b*t^3,
h=-6*b^2*t^3,
x=2*h/m=-2*b*t,                                      (1.2)
```

and `t=y/m`.  Hence `m!=0` on this chart implies `b*t!=0`.

The omitted locus `b=0,e=0` has `a=d=0` and

```text
K0=A^4.
```

It is the rank-two square intersection.  It is routed to the square client,
not called empty by this design.  Although (1.2) has no point with `m!=0`
and `b=0`, that observation cannot replace the routing: the exact raw ideal
(0.1) was proved only after localizing by `b*m`.

Retain the two free complementary-kernel coordinates `q,s`.  The complete
reduced K2 source section is

```text
a=b/4,                    d=-3*b^2/16,
m=6*b*t^2,                x=-2*b*t,
y=6*b*t^3,
kc=q,                     kr=t^2-b*q/4,
ns=s,                     nt=3*b*t^2*q-b*s/4,
kappa=0.                                                (1.3)
```

Indeed, in `A` coordinates,

```text
K1=x*A,                   N1=y*A+h,
K2=q*A+t^2,               N2=s*A+3*b*t^2*q,            (1.4)
```

and the first two K2 rows say exactly

```text
C0=kr+a*kc=y^2/m^2=t^2,
S0=nt+a*ns=m*kc/2=3*b*t^2*q.                           (1.5)
```

## 2. Ordinary `rho^7` and `rho^8` formulae

These formulae are useful both as an index check and as the unramified
successor.  Write

```text
K=sum_(i>=0) rho^i K_i,
N=sum_(i>=0) rho^i N_i,
R0=N0/K0=m/A,
E_i=N_i-R0*K_i.                                      (2.1)
```

At a K2 zero, put
`k10=rho^2(rho*kappa1+rho^2*kappa2+...)`.  Modulo polynomial
terms, the coefficient of `rho^7` in the full principal part is

```text
H7 = [
 (3/8)*(2*R0*N3-R0^2*K3
         +2*E1*E2/K0-E1^2*K1/K0^2)
 -(3/16)*R0^2*E1/K0
 +kappa1*K0^(5/2)
]_-.                                                  (2.2)
```

The coefficient of `rho^8` is

```text
H8 = [
 (3/8)*(2*R0*N4-R0^2*K4
   +(E2^2+2*E1*E3)/K0
   -2*E1*E2*K1/K0^2
   +E1^2*(K1^2/K0^3-K2/K0^2))
 -(3/16)*(R0^2*(E2/K0-E1*K1/K0^2)
           +R0*E1^2/K0^2)
 +(3/128)*R0^4/K0
 +kappa2*K0^(5/2)
 +(5/2)*kappa1*K0^(3/2)*K1
]_-.                                                  (2.3)
```

They follow by using

```text
N^2/K=R0^2*K+2*R0*E+E^2/K,
N/K=R0+E/K
```

in

```text
(3/8)*rho^4*N^2/K
 -(1/16)*rho^6*N^3/K^3
 +(3/128)*rho^8*N^4/K^5.                             (2.4)
```

Formula (2.3) displays where the raw doubled direction first appears in an
ordinary rho-jet: if `U=rho*U1+...`, then `U1^2` occurs at `rho^8`, not at
`rho^7`.  Therefore an ordinary K3 client alone is not exhaustive for
Puiseux approach to the nonreduced K2 scheme.

## 3. Why the normalized ray is mandatory

The normal cone of (0.1) assigns

```text
wt(U)=1,
wt(e)=wt(kappa)=wt(F)=2.                              (3.1)
```

Equivalently, introduce `sigma` by

```text
rho=sigma^2.                                          (3.2)
```

The slow direction `U~sigma` then competes with
`e,kappa,F~sigma^2`.  In the original full source `Phi_l`, the K2 grade
`rho^6` becomes `sigma^12`; the coefficient `sigma^13` is killed by the
linear kernel, and `sigma^14` is the correction-aware K3 obstruction.  It
combines the intrinsic `rho^7` row with `U1^2`.  Replacing (0.1) by its
radical would delete precisely this chart.

Here is an exact localized nested section.  Tangent series
`B=b+O(sigma), T=t+O(sigma), Qc=q+O(sigma), Sc=s+O(sigma)` may be retained;
they cancel from the `sigma^14` cokernel because (1.3) is an exact family.
For the smallest separator they can be frozen at their constant terms.  Put

```text
Y = 6*b*t^3,
M = 6*b*t^2 - 6*sigma*t*xi + sigma^2*nu,
X = -2*b*t + sigma*xi + sigma^2*omega,                (3.3)

e       = sigma^2*epsilon,
kappa   = sigma^2*chi,
kc      = q,
ns      = s.                                          (3.4)
```

Let `c_n=[v^n](1+b*v)^(5/2)`.  In the localization by `M`, take the exact
triangular K2 section, through the required order,

```text
C0=kr+a*kc
  =Y^2/M^2 +(8*kappa*c_12)/(3*M^2)+sigma^2*gamma,

S0=nt+a*ns
  =M*kc/2 -(4*kappa*c_11)/(3*M)+sigma^2*delta.         (3.5)
```

Finally insert

```text
a=b/4,                   d=e-3*a^2,
p=d-3*a^2,
c=2*a*(a^2-d)+rho*X+rho^2*kc,
r=a^2*d-rho*a*X+rho^2*kr,
n3=M,                    n2=a*M,
n1=(d-2*a^2)*M+rho*Y+rho^2*ns,
n0=-a*d*M+rho*(-a*Y+M*X/2)+rho^2*nt                (3.6)
```

with `rho=sigma^2` into the complete frozen coefficient source
`C=K^2+rho^2*N`.  Formulae (3.3)--(3.6) are the requested nested
substitution; no coefficient or load is projected.

For a polynomial compiler, expand `1/M` only through `sigma^2`.  If
`m0=6*b*t^2`, `m1=-6*t*xi`, `m2=nu`, and `i=m0^(-1)`, then

```text
1/M   = i-sigma*m1*i^2
          +sigma^2*(m1^2*i^3-m2*i^2),
1/M^2 = i^2-2*sigma*m1*i^3
          +sigma^2*(3*m1^2*i^4-2*m2*i^3).            (3.7)
```

The compiler retains the graph `m0*i-1`; hence (3.7) is exact modulo
`sigma^3` on the declared open.

The raw coordinates are visible directly.  With

```text
U=M*X/2+b*Y,
F=M^3+6*M*X*Y+6*b*Y^2,
```

one gets

```text
U=sigma*U1+O(sigma^2),       U1=9*b*t^2*xi,
F=sigma^2*F2+O(sigma^3),
F2=36*b^2*t^4*nu+216*b^2*t^5*omega
    +432*b*t^4*xi^2.                                  (3.8)
```

The first-order map from unrestricted `(delta x,delta m)` to `(U,F)` has
determinant `324*b^3*t^6`, so this is an etale chart on `D(b*t)`.  The
choice `delta m=-6*t*delta x` is exactly the kernel `F_1=0`, not a lost
direction.

## 4. Exact `sigma^14` rows and the three-row certificate

At (1.3), put `W=U1^2`.  The intrinsic `rho^7` negative tail from (2.2)
is

```text
(9/2)*b*t^3*s*A^-2
 -(27/2)*b^2*t^5*q*A^-3
 -27*b^2*t^7*A^-4
 -(27/2)*b^3*t^7*A^-5.                               (4.1)
```

For a direct check, use

```text
E1=6*b*t^3*(A+b),
E2=s*A-3*b*t^2*q-6*b*t^4/A
```

in (2.2).  Multiplying the seven `A^-j` rows by sixteen, the complete
correction-aware analytic rows are

```text
L1 = 12*m*delta,
L2 = -6*m^2*gamma + 72*b*t^3*s,
L3 = -F2 -216*b^2*t^5*q +16*chi*c_13,
L4 =  6*W -6*y^2*epsilon -432*b^2*t^7 +16*chi*c_14,
L5 = -6*b*W -216*b^3*t^7 +16*chi*c_15,
L6 =  6*b^2*W              +16*chi*c_16,
L7 = -6*b^3*W              +16*chi*c_17,             (4.2)
```

where `m=6*b*t^2`, `y=6*b*t^3`, and

```text
c_n=binom(5/2,n)*b^n.                                 (4.3)
```

The terms `6*(-b)^(j-4)*W` in rows `j>=4` are exactly the retained
`U^2` thickness.  They follow from

```text
v^2*(y-(U-b*y)*v)^2/(1+b*v+e*v^2)
 = y^2*v^2*(1+b*v)-2*y*U*v^3
   +U^2*v^4/(1+b*v)-y^2*e*v^4+O_wt(3).               (4.4)
```

The last three rows already have no solution on `D(b*t)`.  The load
recurrence at `n=16` gives

```text
c_17=-(27/34)*b*c_16,
b*c_16+c_17=(7/34)*b*c_16 != 0 on D(b).               (4.5)
```

Hence

```text
b*L6+L7=16*chi*(b*c_16+c_17)
```

forces `chi=0`; then `L6` forces `W=0`; and `L5` becomes
`-216*b^3*t^7=0`, a contradiction.  This is a scheme-theoretic unit
certificate after localization by `b*t`; it does not use `W` as an
independent square root and remains valid before reducing the raw K2
scheme.

## 5. Complete-source comparison required on AWS

The smallest proof client uses only this normalized ray.  It must:

1. pin the complete seven-tail JSON and its canonical all-tail digest;
2. reconstruct every frozen source tail, not a principal-part surrogate;
3. insert (3.3)--(3.7) with `rho=sigma^2` and the full coefficient map
   (3.6);
4. prove every source row is divisible by `sigma^12`, prove the
   `sigma^12` and `sigma^13` coefficients vanish modulo `m0*i-1`, and
   extract all seven `sigma^14` rows;
5. independently generate (4.2), including the raw `W=U1^2` terms;
6. compare every source coefficient with the corresponding transformed
   analytic coefficient.  If `v=1/w` and `qv=A/w`, the base relation is

   ```text
   qv^4+b*v*qv^3=1,
   A^-j=v^j*qv^-j.                                   (5.1)
   ```

   Expanding (5.1) through degree seven gives the exact unitriangular
   Laurent-to-Faber row matrix.  The client must check the seven identities
   `16*S_l=sum_j T_(l,j)L_j`, not merely compare two ideals after both have
   become unit ideals;
7. verify (4.5), the displayed `b*L6+L7` identity, and unit ideals for both
   the analytic and complete-source rows after adjoining `m0*i-1`;
8. run exact `Q` and an independent good prime with fail-closed validators.

Required unique sentinels are:

```text
K3NR_SOURCE_HASHES=PASS
K3NR_SIGMA12_DIVISIBLE=1
K3NR_SIGMA12_BASE_ZERO=1
K3NR_SIGMA13_KERNEL_ZERO=1
K3NR_FORBIDDEN_LOW_GRADES=1
K3NR_RAW_U1=<9*b*t^2*xi>
K3NR_RAW_F2=<the polynomial in (3.8)>
K3NR_ROW_COMPARE_1=1 ... K3NR_ROW_COMPARE_7=1
K3NR_C17_RECURRENCE=1
K3NR_LAST3_CERTIFICATE=1
K3NR_ANALYTIC_BT_UNIT=1
K3NR_SOURCE_BT_UNIT=1
K3NR_ENDPOINT=PASS_NORMALIZED_RAY_SOURCE_UNIT
```

Any missing, duplicate, or failed sentinel is no verdict.

## 6. Lower loads, terminal row, and Taylor receivers

In the unramified `rho` bookkeeping, after division by `rho^6`, the first
possible appearances in the original `Phi_l` are:

```text
k10 successor: rho^7 and rho^8,
k6:             rho^12,
k2:             rho^20,
mu2 target:      rho^28,
mu4 target:      rho^32,
mu6 target:      rho^36,
J/4 terminal:    rho^38.                              (6.1)
```

Thus `k6,k2,mu2,mu4,mu6,J` must be present in the source ring but must have
zero derivatives in both the `rho^7` and `rho^8` rows.  Under
`rho=sigma^2`, their exponents double.  The nonzero-`J` interior condition
is retained as source typing even though `J` does not enter the normalized
K3 separator.

The two finite Taylor families are not terms in `Phi_l` at any rho grade.
Their first nonzero grade cannot be inferred from the tail JSON or from
(6.1); it requires the global coefficient functions and `R0` at both branch
charts.  If the source unit endpoint above passes, this necessary tail gate
already excludes the branch and no Taylor computation is needed for that
exclusion.  If it does not pass, both Taylor families must be attached to
the surviving source chart before any lift or trajectory claim.

## 7. Hidden assumptions and firewall

- **K2 coverage.**  The exact-Q full-source V2 equality is still the gate
  from the analytic ideal (0.1) to exhaustive frozen-source coverage.
- **Row coordinates.**  Higher Faber rows cannot simply be identified with
  Laurent coefficients.  The exact unitriangular transformation (5.1) and
  all seven source identities are mandatory.
- **Normalized coverage.**  The ordinary rho-jet misses `U~rho^(1/2)`.
  The ray (3.1)--(3.2) is mandatory; any normalized-Rees claim must prove
  that no other ray of the full source ideal is omitted.  For the local raw
  complete intersection (0.1), its only new primitive ray is the displayed
  `(1,2,2,2)` ray, but promotion to the full source still uses the K2 gate.
- **Open charts.**  Divisions by `M`, `b`, and `t` are licensed only on
  `D(b*m)`.  The `b=0` divisor is square-routed, not excluded here.
- **Nilpotents.**  `W=U1^2` is retained through the last-three-row
  certificate.  No radical substitution is used.
- **Source scope.**  A PASS would exclude this nonsquare discriminant K2
  successor as a necessary tail branch.  It would not analyze the square
  chart, prove either Taylor family globally, close order two, close
  `(8,12)`, prove maximum twelve, or prove JC2.
