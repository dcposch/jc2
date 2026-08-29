# Preregistration: D1 `a=8,d=2` load-first split

Date: 2026-08-26

Status: **PREREGISTERED EXACT-Q AWS PRODUCER WITH TWO PRIME SCREENS.**

## Literal scope

Treat only

```text
ord(A)=8, ord(C)=10, ord(R)>=8
```

after the frozen square/D1 gates on `D(p*k0)`.  Write
`k6=k60+sigma*k60_1+...` and use the exhaustive scheme-theoretic split
`D(k60) union V(k60)`.

## `D(k60)` branch

The unique grade-27 source is

```text
(3/4)*k60*C/L.
```

This precedes the row-2 target at grade 28.  The first two literal/analytic
rows must be exactly `(3/4)k60*c1` and `(3/4)k60*c0`.  On either exact
`C` chart they generate the unit ideal after inverting `k60`.

## `V(k60)` branch

At grade 28, the first surviving pole-one column is

```text
(3/4)*C*(A+k60_1)/L.
```

The compiler must verify its multiplication determinant
`Delta_C=c0^2+(p/2)c1^2` and retain both rank chambers.  The complete source
through grade 30 has global pole ceiling two and sole pole-two primitive

```text
(3/8)*C^2/L^2.
```

For both moving roots, verify

```text
Psi_+ = Phi4+lambda*(Phi3+(p/4)*Phi1),
Psi_- = Phi4-lambda*(Phi3+(p/4)*Phi1),
q_+=(3/8)*(c1*lambda+c0)^2,
q_-=(3/8)*(-c1*lambda+c0)^2.
```

All pole-one columns pair to zero, and `(q_+,q_-)` must be the unit ideal
on both `D(c1)` and `D(c0)`.  The row-2 target and its jets through grade
30 must be retained, but rows 1,3,4 are target-free and hence the dual
functionals are source-exact.

## Acceptance and firewall

Independently enumerate all six primitives, derive every jet ceiling,
bridge all seven literal rows to the analytic source, and verify every
quotient, moving-root equation, rank identity, recurrence, target timing,
and chart unit ideal.  Run exact Q plus independent `F_65521` and
`F_65519` screens on distinct AWS hosts, capped and fail-closed.

A PASS closes only this strict `a=8,d=2,ord(R)>=8` tail.  It says nothing
about `a=8,d=3` (whose load-first grade 28 is already row-2-target
shadowed), `a=9`, equality faces, positive-order leading loads outside the
explicit split, target-shadow successors, another D1 face, `p=0`, `k0=0`,
the square component, maximum twelve, or JC2.
