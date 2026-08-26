# Preregistration: exact control-2 Rees initial residue

Date: 2026-08-26  
Execution: registered Amazon EC2 only  
Status: source freeze before compile or solve

## Question

Test whether the correction-enabled target ray already certified as a finite
successor is an actual point of the initial degeneration of the **full finite
eight-row D1 ideal**, not merely of a coefficient truncation.

Freeze the double-root cubic and loads at

```text
K=(z-1)^2(z+2)=z^3-3z+2,
a=1, h=0, q2=0,
k=0, mu=2/3, nu=0.
```

Write

```text
Q=q1*z+q0,
R=r2*z^2+r1*z+r0,
Lambda=tau^3*rho.
```

The finite polynomial ideal has the eight exact independently reconstructed
ordinary tails

```text
r_l(f,0)=Lambda^(12+l)*gamma_l,
gamma_3=2/3, gamma_8=1+tau,
gamma_l=0 otherwise,
f=K^3+KQ+R,
```

together with `Lambda-tau^3*rho=0`.  There is no series-coefficient cutoff.
The charged source is pinned at

```text
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
```

## Weight and support mask

Use the integral valuation vector

```text
v(Lambda,tau,rho,q1,q0,r2,r1,r0)=(4,1,1,22,22,30,30,30).
```

This is the ramification of normalized `(alpha,beta)=(15/2,11/2)`.
The coordinate support mask fixes `a-1=h=q2=k=nu=0` identically; every
displayed finite-ring coordinate is nonzero on the residue torus.  The fixed
initial residue is

```text
(Lambda,tau,rho,q1,q0,r2,r1,r0)=(1,1,1,1,-1,1,1,-2).
```

It is the leading part of

```text
Q=t^22*(z-1),
R=t^30*(z-1)*(z+2)-t^38/2+...,
Lambda=t^4, tau=t, rho=t.
```

The `-t^38/2` correction is a later coefficient of `r0`; it is not inserted
as a new finite-ring coordinate.  Exact Rees closure decides whether some
higher coefficients exist.

## Two independent exact encodings

Let `s` be the Rees parameter and replace every coordinate `X` by
`s^v(X)*X` in the complete finite ideal.

- Encoding A keeps the charged source in factored coefficient-image form,
  contracts from `s!=0` by Singular's `sat(I,<s>)`, and uses a global degree
  order.
- Encoding B independently expands every charged row over `Q`, contracts by
  the inverse equation `u*s-1` and elimination of `u`, and uses an
  `(lp(2),dp(8))` block order.

Each encoding first checks a pure-vertical negative control and a one-factor
positive contraction control.  The compiler also verifies on AWS that the
displayed residue kills the minimum-weight form of every submitted generator.
That prevariety check is not the result: the solver must include every
S-polynomial consequence through exact contraction.

## Exact semantics

Let `C` be the contraction of the Rees-transformed ideal from `s!=0`, and
let `H=C+(s)`.

- If `H` plus the displayed residue maximal ideal is the unit ideal in both
  encodings, then **this exact support/weight/residue has no lift**.
- If it is nonunit in both encodings, then the displayed residue lies in the
  special fibre of the closure of the exact finite ideal.  Algebraic curve
  selection / the valuative criterion yields a Puiseux lift after finite
  ramification in this frozen-axis, fixed-load support.
- Disagreement, nonzero rc, stderr, a missing/duplicate PASS marker, failed
  source hash, failed synthetic control, or resource termination is
  `INCONCLUSIVE_SOFTWARE`.

Neither verdict classifies other residues, moving-axis directions, `q2!=0`,
other loads, the full double-root fan, D1, or JC2.  A lift here is a formal
point of the exact D1 coefficient ideal, not by itself a polynomial Keller
counterexample.

