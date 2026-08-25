# Preregistration: full localized six-row `w=0` fibre

Date: 2026-08-25  
Status: **FROZEN BEFORE CAS LAUNCH**

## Exact source

Consume byte-for-byte the reviewed approximate-cubic quotient compiler.  Set
`w=0` in precisely the six imposed rows

```text
r1/t=r3/t=r5/t=r7/t=r2=r4=0
```

in `(c,d2,d4,x1,x3,x5)`.  Add only the graph and localization rows

```text
v*x5-x3+2*x5=0,
inv*x5*(x3-2*x5)-1=0.
```

Thus neither `x5` nor `x3-2*x5` may vanish, while `w` is not inverted.  The
output polynomials `e6=r6|_(w=0)` and `e8=r8|_(w=0)` are reconstructed from
the same compiler and are not added to the six-row ideal unless a named
stratum requires them.  No candidate plane equation or graph interpolation
is imported.

## Exact set-theoretic cover

Over an algebraic closure, the localized fibre is exhausted by

```text
V(e6)
union [D(e6) intersect V(Q8(v))]
union [D(e6) intersect D(Q8(v))].
```

The middle term is the reviewed corrected-Q8 contact locus.  The last term is
the complete loaded non-Q8 locus and is further exhausted by

```text
V(detJ) union D(detJ),
V(e8)   union D(e8),
```

where `detJ` is the determinant of the full eight rows (six source rows plus
the `v` graph and localizer) with respect to
`(c,d2,d4,x1,x3,x5,inv,v)`.  Every `D(...)` is encoded by a fresh inverse
row; no set-theoretic division or unrecorded saturation is allowed.

This cover is an identity of sets, not a claim of reducedness, primarity, or
component multiplicity.  Scheme multiplicities remain charged.

## Acceptance and fail-closed branches

1. The exact Q8 control must be zero-dimensional of length eight, have
   squarefree `v`-eliminant equal to the corrected octic up to a unit, and
   have `detJ` a unit.  Failure quarantines every successor.
2. The base and every named stratum must reduce every original generator to
   zero against its returned basis.  A missing PASS marker, nonzero return,
   parser/error token, positive dimension where elimination is attempted, or
   non-principal `v` elimination is not a classification.
3. A `v` factor list classifies geometric points only if the `v` eliminant is
   squarefree and its degree equals the quotient length.  Otherwise projection
   collisions/nilpotents must be resolved by primary decomposition or an
   additional separating coordinate.
4. For each rational irreducible non-Q8 factor, certify its Galois orbit and
   reconstruct the remaining coordinates, or explicitly retain it as an open
   factor stratum.  No factor may be dropped because it lacks rational roots.
5. Only after all loaded non-Q8 strata are isolated may the terminal row and
   both true-center Taylor polynomiality families be imposed.  The reviewed
   selected-Q8 positive-genus exclusion remains immutable and is not used to
   dispose of a non-Q8 point.

The initial routing order is: exact Q8 controls over `Q` and `F_127`; complete
base/loaded/non-Q8 factorization over `F_127` and one fresh good prime; then
characteristic-zero factorization with independent term-order/engine replay.
All substantive computation is AWS-only.

