# TD6 V89 addendum: global q-radical shortcut

Date: 2026-08-26

Status: **standalone exact design only; no radical-membership result claimed.**
The V89H1-derived shortcut is withdrawn after its unregistered `K=2 R38`
denominator.  Only a fresh full-ring proof of the 22 coordinate-power
certificates below can activate this route.

## Algebraic shortcut

Work in the literal V87 section-polynomial ring localized at the registered
unit `U H B3`, and let

```text
J = (P12, FIRST_0,...,FIRST_37, F),
Q = (q2,...,q14,q16,...,q24).
```

The V87 identity says

```text
1 in J+Q
```

after dividing its displayed unit target by `U^12 H^3 B3`.  Therefore it is
enough to prove

```text
Q subset radical(J).
```

Indeed, modulo `radical(J)` every q coordinate then vanishes, while the V87
identity says one vanishes.  Hence `radical(J)=(1)` and the whole retained
V87 slice is empty.  V88 makes q15 an independent target-shear coordinate,
so q15 is not a missing generator of Q.

An output-explicit sufficient certificate is, for each licensed exponent e,

```text
(U H B3)^M_e q_e^N_e
 = A_e P12 + sum_i B_ei FIRST_i + F H_e,       N_e > 0,
```

with polynomial multipliers and no q, F, or unregistered-base inverse.  One
common containment `Q^N subset J` is stronger than necessary; the 22
coordinate powers already prove the radical inclusion.

## Why this can beat 22 unit charts

This route retains every q coefficient and never chooses or normalizes a
unit coordinate.  It therefore avoids both the unlicensed projectivizing
`G_m` action and the 22 principal-open atlas.  It also converts V87's
positive-q DVR theorem into an affine ideal-theoretic closure statement,
which is stronger than a collection of generic chart ranks.

The cost is that radical membership is nonlinear.  A tangent syzygy, a
reduced P12 zero, or membership after setting the other q coordinates to
zero is not enough.  Every certificate must replay in the full literal
22-q source ring.

## Shared bounded solve

Because V87 measured every literal source to have total q-degree one, build
one Macaulay/source-DAG matrix for a preregistered multiplier support and use
the 22 coordinate powers as simultaneous right-hand sides.  The matrix, row
typing, denominator audit, and pivot stratification are shared; only the RHS
changes.  Search powers in the order `N=1,2,3,...`, enlarging multiplier
support only after an exact cokernel obstruction at the previous bound.

The original scheduling suggestion was to start with the nine high
coordinates `q16,...,q24`:

- their reviewed genuine-P12 sensitivities are source syzygies;
- their V87 augmentation quotients have only 358--391 terms each;
- the V89H1 triangular test can expose either a finite source-row
  automorphism or the first exact cycle/positive-q remainder, which gives a
  focused support for `N=2` rather than a generic Macaulay box.

H1 did find an algebraic triangular replay, but its final common denominator
contains the unregistered factor `K=2 R38`.  Consequently no high-earliest
exclusion, polynomial-coordinate theorem, or global-radical reduction is
banked from H1.  Its multiplier supports may be used only as discovery hints;
every coefficient must be solved anew and replayed in the full literal ring
on `D(U H B3)`.

## Comparison with triangular integrability

| route | cost | exact strength |
|---|---|---|
| V89H1 triangular row automorphism | exact algebra completed, but denominator gate failed at `K=2 R38` | withdrawn on `D(U H B3)`; no residue stratum eliminated |
| coordinate radical certificates | shared Macaulay solve with increasing q degree and 22 RHS columns | stronger; combined with V87 empties the whole retained 22-q slice without charts |
| 22 principal-open clients | repeated localized solves with a retained unit radial parameter | fallback; geometrically direct but duplicates source compilation and pivot work |

H1 has served as a low-cost discriminator and failed closed.  A successor may
test whether `K` is a unit modulo the literal q-zero source ideal or find a
registered alternate pivot, but the full-ring radical block does not consume
H1 while those gates remain open.

## Fail-closed output

For every claimed coordinate membership, emit the literal target power,
all original source multipliers, F multiplier, clearing power, exact replay,
denominator factorization, and negative controls omitting P12, F, one active
FIRST row, the transport q source, and the direct q-prime source.  A complete
radical promotion additionally needs an exact list of all 22 coordinates and
the one-line ideal implication above.

This remains a theorem only about the retained fixed-center/F1/pole/dead-
stretch source family.  It does not restore omitted moduli or prove whole
A3, TD6, SP-2, or JC2.
