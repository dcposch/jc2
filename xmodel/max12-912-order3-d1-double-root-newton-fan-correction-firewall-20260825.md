# D1 double-root Newton-fan correction firewall

Date: 2026-08-25  
Status: **EXPLICIT GAP / NEGATIVE CONTROL; INDEPENDENT REVIEW REQUIRED**

## Charged setting

At the remaining depressed-cubic point put

```text
L=z-1, U=z+2=L+3,
K0=L^2*U, N=L*U.
```

For the exact normal division `f=K^3+KQ+R`, the first pure ordinary negative
layers charged by the frozen reconstruction are

```text
(4/9)*Q*R/K + (2/9)*R^2/K^2 - (4/81)*Q^3/K^2 + ... .       (1)
```

The exact source is

```text
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
```

## Finding

The tempting seven-case classification by the three raw valuations

```text
beta+alpha, 2 alpha, 3 beta
```

is **not proved** by imposing exact `K0`/`K0^2` divisibility on each pure
leading numerator separately.  Once an earlier `QR/K` numerator is a
polynomial, higher coefficients of that same layer can arrive at the next
pure weight and cancel the `R^2/K^2` or `Q^3/K^2` tail.  At the nonreduced
factor this is a real effect, not an exposition technicality.

Consequently the frozen experiment

```text
cases/max12_912_order3_d1_double_root_toric_blowup_20260825/
```

is exact for its preregistered `alpha=2 beta` chart, but a unit result there
must **not** be promoted to a whole double-root or whole-D1 exclusion.

## Negative control 1: a non-target correction cancels the next pure layer

Choose any rational valuations

```text
3 beta/2 < alpha < 2 beta,  beta<6,
```

and pass to a finite ramification so their powers are integral.  Take

```text
Q=t^beta*N,
R=t^alpha*L + t^(2 beta)*(U/9) + higher terms.               (2)
```

At weight `beta+alpha`,

```text
Q0*R0/K0 = N*L/(L^2*U)=1,
```

so the whole first `QR/K` contribution is polynomial and has no negative
tail.  Because `2 alpha>3 beta`, the next candidate weight is `3 beta`.
At that weight the displayed correction in R contributes

```text
(4/9)*(N*(U/9)/K0) = (4/81)*(U/L),
```

while the cubic layer contributes

```text
-(4/81)*(N^3/K0^2) = -(4/81)*(U/L).
```

They cancel identically.  Thus the usual proposed step
`K0^2|Q0^3`, and hence the claimed immediate contradiction, is false once
the allowed higher normal coefficient is retained.  This does not prove a
formal lift; it proves that this Newton ray survives the advertised gate and
needs a successor equation.

## Negative control 2: the row-3 target creates another live ray

Put

```text
alpha=15/2,  5<beta<6,
Q=t^beta*L,
R=t^alpha*N - (1/2)*t^(2 alpha-beta) + higher terms.          (3)
```

Here `beta<alpha<3 beta/2`.  The weight `beta+alpha<15` layer is again
polynomial because `L*N=K0`.  At weight `2 alpha=15`, (1) gives exactly

```text
(4/9)*((-1/2)*L/K0) + (2/9)*(N^2/K0^2)
 = (2/9)*(1/L^2-1/(L*U))
 = (2/3)*(1/K0).                                           (4)
```

Since `K0(z0(w))=w^3`, `1/K0` is precisely a row-3 tail and has no other
row.  Equation (4) therefore matches the allowed target with `mu=2/3`
(up to the obvious amplitude rescaling).  The simple-factor order argument
does not kill this ray: the higher `QR` coefficient supplies the missing
multiple of K before reduction modulo `K^2`.

Again, (3) is a finite successor, not a formal D1 trajectory.  It is an
explicit negative control showing that weight-15 coincidences cannot be
discarded from the double-root fan.

## What remains valid

For the tied first-weight case `alpha=2 beta`, no lower `QR/K` layer exists,
so its leading calculation is sound:

```text
Q0*(9*R0*K0-Q0^2) is K0^2-divisible
```

if and only if

```text
Q0=A*N,  R0(1)=A^2/3.
```

The frozen toric chart

```text
Q=x*Qhat, R=x^2*Rhat, x*y=Lambda^6
```

with

```text
Qhat(1)=Qhat(-2)=0,
Qhat'(1)!=0,
27*Rhat(1)=Qhat'(1)^2
```

therefore covers this tied ray exactly, including all other Rhat directions,
the moving axis/cusp, fixed load variables, and exact charged tails.  Its
solver result remains useful as one branch of the full Newton tree.

## Required repair

A whole double-root theorem needs a correction-aware Newton--Puiseux tree.
At each visible weight it must retain the image of every earlier rational
layer's next coefficient before taking a quotient by `K0` or `K0^2`.
Equivalently, it should track the remainder maps

```text
rem_K(Q_i*R_j),
rem_(K^2)(R_i*R_j and Q_i*Q_j*Q_k)
```

jointly, rather than assigning independent divisibility conditions to the
three pure leading terms.  The first required new branches include at least

1. `3 beta/2<alpha<2 beta` with the forced `R_(2 beta)=U/9` correction from
   (2), and
2. the target face `alpha=15/2, 5<beta<6` containing (3).

An efficient compiler should quotient tail-invisible polynomial directions
at every step and launch the adversarial source review in parallel.  Until
that tree is complete, the exact meaning of a terminal from the current
toric package is:

- `H=1`: the tied `alpha=2 beta`, `0<beta<6` chart is empty;
- `H!=1`: only a total-load-space survivor in that chart, not a fixed-load
  lift;
- neither verdict closes the other correction-enabled rays, D1, or JC2.
