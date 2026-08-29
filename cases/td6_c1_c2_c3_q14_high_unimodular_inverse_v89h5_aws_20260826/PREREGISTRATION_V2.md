# TD6 V89H5V2 q14 remainder localized-`(F)` membership preregistration

Date: 2026-08-26

Status: exact producer diagnostic; no result claimed before byte-identical dual
AWS replay.

## Frozen input and exact question

V89H5V1 rebuilt literal P12 and all 38 raw FIRST rows on the residue block

```text
q2=...=q13=0, q15 absent, q14,q16,...,q24 independent and untruncated.
```

Its dual replays emitted the same 17-record normalized P12 remainder:

```text
eb939448f5636a3084ca129aa3a5cdf44709ac3a8ca28be77a14c2e5fdea7c14
```

There is one q-zero record and exactly seventeen positive records, all carrying
the monomial `q14`.  This V2 client consumes those frozen bytes and asks only
whether the seventeen-record positive remainder belongs coefficientwise to the
principal ideal `(F)` in

```text
Q[C,V,U,1/(U*H*B3)],
F = C*U - V^2 + U^3,
H = C - 3*U^2.
```

No source row may be changed and no additional factor may be inverted.

## Exact gate

1. Pin the V1 client and both byte-identical remainder files by SHA256.
2. Parse all 17 exact rank-18 extension coefficients and reproduce the
   frozen TSV digest exactly.
3. Require one q-zero record, seventeen `q14` records, and no other positive q
   support.
4. Audit that every original denominator is supported only on the registered
   open `D(U*H*B3)` and is coprime to `F`.
5. Divide every one of the 288 scalar coefficient coordinates formally by
   `F`, replay the multiplication in the exact fraction field, and emit a
   complete coordinate/denominator inventory.
6. If all formal quotient denominators remain registered and coprime to
   `F`, emit the explicit polynomial-localized quotient.
7. Otherwise emit the first exact negative certificate: source coordinate,
   numerator modulo `F`, formal quotient denominator, its factorization and
   its nontrivial gcd with `F`.  Verify independently that `U`, `H`, and `B3`
   are each coprime to `F`.
8. Remove one quotient record as an omission fixture and require the frozen
   replay digest to change.

Dual Box02/r6d output and every emitted artifact must be byte identical.

## Fail-closed scope

A negative result proves only that this particular normalized positive-q14
remainder is not coefficientwise in the localized principal ideal `(F)`.
It does not exclude another combination of the original FIRST rows, and it
is not a negative result for `(P12,FIRST,F)` as an ideal.  A positive result
would supply only the missing quotient for this exact normalization.

Neither verdict covers any low-q unit chart, total Rees, a source point,
whole fixed A3, TD6, SP-2, or JC2.
