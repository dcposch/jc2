# Correction-aware discriminant triple-root K3 receiver

Date: 2026-08-26

Status: **AWS-ONLY PREREGISTRATION DESIGN; NO COMPUTATIONAL RESULT.**

## 1. Frozen source and scope

This receiver imports the exact seven ordinary tails from
`tails.json` and the frozen half-weight compiler.  Its charged source SHAs
are embedded in `compile_k3.py`.  It consumes the analytic K2 support theorem
only provisionally while the full-source exact-Q V2 comparison remains the
promotion gate.

On `D(b*m)` the analytic K2 scheme is

```text
(kappa,e,U^2,V+6*y*U),
U=h+b*y,
V=m^3+6*h*y.
```

Its reduced triple-root support has the birational coordinates

```text
a=b/4,                  d=-3*b^2/16,
m=6*b*t^2,              x=-2*b*t,
y=6*b*t^3,
kc=C,                   kr=-b*C/4+t^2,
ns=S,                   nt=-b*S/4+3*b*t^2*C,
kappa=0,                b*t!=0.                       (1.1)
```

The two free variables `C,S` retain the tangent/kernel directions left after
the first two complementary K2 rows are solved.  The relation `m!=0` is
licensed by the first-contact saturation; `b=0,e=0` gives `K=A^4` and is
routed to the separate square-intersection chart.

## 2. Correction-aware nested jet

The receiver does **not** merely substitute (1.1).  It gives every variable
of the half-weight chart an independent first correction:

```text
a       = b/4             + rho*ja,
d       = -3*b^2/16       + rho*jd,
m       = 6*b*t^2         + rho*jm,
x       = -2*b*t          + rho*jx,
y       = 6*b*t^3         + rho*jy,
kc      = C               + rho*jkc,
kr      = -b*C/4+t^2      + rho*jkr,
ns      = S               + rho*jns,
nt      = -b*S/4+3*b*t^2*C+ rho*jnt,
kappa   =                     rho*jk.                 (2.1)
```

These are substituted into the complete half-weight family

```text
K=z^4+(d-3a^2)z^2
    +(2a(a^2-d)+rho*x+rho^2*kc)z
    +(a^2d-rho*a*x+rho^2*kr),

N=mz^3+amz^2
  +((d-2a^2)m+rho*y+rho^2*ns)z
  +(-adm+rho(-ay+mx/2)+rho^2*nt),

f=K^2+rho^2*N.                                      (2.2)
```

The lower loads remain exactly

```text
rho^4*k10 = rho^7*jk,
rho^12*k6,
rho^20*k2,                                           (2.3)
```

and the scalar targets remain at orders

```text
mu2:rho^28,  mu4:rho^32,  mu6:rho^36,  J/4:rho^38.   (2.4)
```

Thus every emitted `Phi_l` is the exact source row, not a tail projection.
The compiler must prove divisibility by `rho^7`, divide exactly, and print

```text
K3_l=(Phi_l/rho^7) mod rho,       l=1,...,7.          (2.5)
```

The seven rows (2.5) are affine-linear in the ten correction variables.
Their elimination on `D(b*t)` is navigation only.  In particular, a nonunit
elimination ideal is not a lift: the doubled normal `U^2` predicts a kernel
direction whose first obstruction can occur at `rho^8`.

## 3. Nonreduced/conormal obligation

At the reduced support, write the raw ideal as

```text
(kappa,e,U^2,W),       W=V+6*y*U.                    (3.1)
```

Its conormal has three linear directions `kappa,e,W`; `U` is invisible to
the linearized K3 rows and must be retained as a kernel direction.  A
successor may extract `rho^8` only after solving the linear K3 rows while
keeping an explicit `U` correction.  Replacing (3.1) by its radical before
that calculation is forbidden.

The first AWS client therefore records the full correction-variable rows,
their generic elimination ideal, and exact source/load/target valuation
sentinels.  It makes no K4 or lifting claim.

## 4. Taylor firewall

The tail source retains the complete terminal variables and their exact
orders.  The two finite Taylor families are separately charged by the
source theorem at SHA
`e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7`:

```text
P_l=u^l/l! * partial_z^l f(uR0) in L[x],  0<=l<=8,
Q_l=u^l/l! * partial_z^l g(uR0) in L[x],  0<=l<=12,
```

at both branch charts `x=0` and `x=1`.  They are **charged but not compiled
in this K3 tail client**.  Therefore even a K3 unit/nonunit endpoint cannot
be promoted to a Taylor or order-two verdict.  The first surviving K3/K4
ray must be fed to both exact Taylor receivers before any source conclusion.

## 5. AWS lanes and fail-closed endpoint

Run the immutable client independently over exact Q and at a good prime.
Each lane must check:

1. all frozen parent hashes and the canonical all-tail digest;
2. AWS identity, registered tag, hostname, PID, caps, and engine return code;
3. the reduced-support identities in (1.1);
4. exact `rho^7` divisibility and multiplication-back identity;
5. absence of `k6,k2,mu2,mu4,mu6,J` from K3;
6. exact lower-load and target valuations (2.3)--(2.4);
7. the seven printed K3 rows and the `D(b*t)` correction-elimination ideal;
8. no `?`, `FAIL`, timeout, or missing/nonunique sentinel.

The endpoint is a correction-aware K3 **necessary gate** only.  It neither
proves a formal lift nor excludes all weighted successors, handles the
square component, discharges Taylor, closes order two, closes `(8,12)`,
proves maximum twelve, nor proves JC2.
