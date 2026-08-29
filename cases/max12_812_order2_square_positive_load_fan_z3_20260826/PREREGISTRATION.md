# Positive-order square fan: exact rational cell enumeration

Date: 2026-08-26

## Question

For the post-`M=0` generic-square positive-load weights

```text
AC=a+c,              C2=2c,
RA2=2+r+2a,          A3=5+3a,
kR3=q+3r,            kRC=1+q+r+c,
kA2=4+q+2a,
```

enumerate every exact set of lower-face minimizers on

```text
a,r,c >= 0,   q > 0,
```

including all `a,r,c` zero/positive boundary patterns.  Rational valuations
are retained; no finite integer box is a substitute.

The four source-completeness sentinels are checked by the hand identities

```text
RAC=AC+2+r,   RC2=C2+2+r,   kAC=AC+4+q,
```

and the two-comparator proof for `kR2A` in the frozen lower-hull note.  They
are not offered to the solver as possible face labels.

## Method and status

Enumerate all `2^7-1` candidate exact minimizer sets and all eight zero/
positive patterns for `(a,r,c)` using Z3 exact linear rational arithmetic.
For each satisfiable cell, emit an exact rational witness.  A dependency-free
checker re-evaluates every witness with Python `Fraction`, verifies the exact
minimizer set and boundary pattern, checks uniqueness, and verifies the
reported candidate count.

Z3 is pinned to `z3-solver==4.13.3.0`; its wheel and installed versions are
recorded.  The run is AWS-only.  Solver UNSAT outcomes are navigation until
the resulting finite H-cell list is independently rederived or reviewed;
witnesses certify only feasibility, not infeasibility of omitted cells.

## Decision rule

- PASS supplies an exact finite sharding table for source-client design.
- It does not prove source-support completeness, initial-ideal emptiness,
  contact raising, fan closure, the square branch, order two, maximum twelve,
  or JC2.
- Every feasible cell remains a proof debt until the complete source/Faber
  module and all root orientations have a reviewed endpoint.

