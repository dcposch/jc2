# Result: affine-Faber `A` graph-relative support

Date: 2026-08-26

Status: **DUAL-AWS PASS; EXACT-Q 365-TERM SUPPORT INVENTORY.**

The frozen client reconstructed all seven ordinary-Faber rows from the
literal tails after the exact two-sided load-coordinate change

```text
d6 = K6-(15*E^2/32)*K10,
d2 = K2-(15*E^4/256)*K10,
dm = mu2+(5*E^6/4096)*K10,
d4 = mu4.
```

The exact-Q lane on Box03 and the independent characteristic-65521 software
lane on r6d each emitted 365 nonzero terms with identical exponent vectors.
Both lanes passed every registered reconstruction control: the `mu6` and
`J/4` target remainders vanish, the `d4` and `dm` targets are exact, the
intrinsic cubic is `-E*lambda^3*M^3/16`, the two transverse identities are
exact, all raw `q,n,k` coordinates disappear, and a one-coefficient load-
graph mutation is detected.

The mathematical stdout hashes are

```text
exact Q: 40953daef89c5d57ecd14619e6ead4870f81f9c75c1b3e2c33ed029848716a30
F65521:   37961e6a9b120c85d95fc6bc16912cff946050106529cffcb0ce3dacfebba6f5
```

This is a complete support/navigation result in the registered coordinates.
It does not itself prove a predecessor reduction, a Newton-fan coverage
statement, a source/Rees theorem, order two, maximum twelve, or JC2.
