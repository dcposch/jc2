# TD6 V89H6 splitting-independent q14 class modulo F

Date: 2026-08-26

Status: **producer-tier exact theorem; dual AWS confirmed; hostile review not
yet charged.**

## Exact scope

Rebuild literal P12 and all 38 original packed FIRST sources from the pinned
V87 source with

```text
q2,...,q13 = 0,
q15 absent only under the separately reviewed target shear,
q14,q16,...,q24 independent and untruncated.
```

Work on `F=C*U-V^2+U^3=0` in `D(U*H*B3)`, using the two-sided coordinate
identification `C=(V^2-U^3)/U`.  This is a statement over
`Frac(Q[V,U])`; it does not use the V89H5 chosen generic splitting.

## Result

The full retained-q 38-by-38 FIRST pivot block is polynomially invertible.
Its only cyclic SCC is `(0,1,2,3,4,5,6,13)`, whose determinant is exactly
one.  Normalizing by this inverse gives exact two-sided pivot identities and
an exact replay as combinations of all 38 original FIRST sources.

The canonical remainder of literal P12 modulo those monic FIRST rows has a
scalar-unit q-zero part and a nonzero positive-q part.  The latter consists
of exactly 17 parameter records, all with q-support exactly `(14,)`:

```text
positive_q14_cokernel_class_zero=false
positive_class_sha256=56ebf08a3f9814f714920a4fcb3ae7fb0957db0c0f6d231382f9b5efbf3321a2
canonical_remainder_sha256=61deb3b3c5ce2098a88b8ad4d8e12f8c6916d2e698a7fab052ed7f60c4d7787a
```

Therefore the q14-positive coefficient of literal P12 represents a nonzero
class modulo the full original FIRST module after exact specialization by
`F=0`, over the fraction field.  In particular this class cannot become zero
over the smaller registered localization.  This is a cokernel obstruction;
it is not a unit-ideal conclusion.

## Independent cross-characteristic gate

An independent 18-dimensional finite-algebra implementation at

```text
p=1000003, (C,V,U)=(8,3,1), F=0, H=5, B3=81
```

separately inverted the evaluated original-FIRST matrices at `q14=0` and
`q14=1`, divided literal P12, and took the difference.  That difference is
nonzero and equals the evaluation of the exact positive class term for term.
The first parameter monomial is `()` with coordinates

```text
(593656,117614,597617,138226,23919,100111,517135,758569,0,0,0,0,0,0,0,0,0,0).
```

The witness SHA256 is
`bf9b47cbb3a075bd6bc31ea61f5a71949bd0ac04530b91fb03c4c82d876194fd`.
Box02 and r6d produced byte-identical mathematical artifacts and stdout,
with rc=0 and no swap.

## Denominator and omission firewall

The literal pre-specialization common denominator is
`U*(C-3*U^2)=U*H`, coprime to F and registered.  No unregistered factor is
inverted.  This result does not cover low-q unit charts, an independent q15
source modulus, total-Rees/source lifting, omitted correction or
moving-center variables, a source point, whole fixed A3, TD6, SP-2, or JC2.

The live monitoring display correction is recorded separately in
`DISPLAY_ONLY_CORRECTION.md`; it changed neither source nor custody.

