# Registration: H17 upper graph-load unit V10

Date: 2026-08-26

Status: preregistered exact-support producer; internal graph only.

Start from the complete frozen 630-term exact support of

```text
Hseries=2 E^2 P3+16 E P5+64 P7-E^3 P1/2.
```

Impose only the leading exceptional affine load graph

```text
K6=(15/32)K10 E^2,
K2=(15/256)K10 E^4,
```

while keeping every other abstract graph coordinate.  Independently perform
the same substitution over `Q` and `F65521`, combine like monomials, and
compare coefficient reductions.

Under the H17 equality-wall weights, check all reduced monomials against

```text
(5/4) K10 a^3 E^7,
```

whose weight is `93-6q`.  The preregistered expectation is that it is uniquely
least for the entire strict upper graph domain

```text
7<q<17/2.
```

At `q=7` it should tie only the intrinsic term
`-2 lambda^3 M^3 E^2`.  Stop on any hash/support/reduction mismatch, wrong
coefficient, additional tie, or narrower open interval.

This client sets positive-order load-graph deviations to their special-fibre
values.  A separate valuative composition must explain why such deviations
cannot cancel a strictly earlier unit.  It makes no literal source,
total-Rees, boundary, factor-degenerate, order-two, max12, or JC2 claim.
