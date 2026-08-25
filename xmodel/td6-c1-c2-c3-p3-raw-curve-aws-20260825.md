# TD6 `H=P3=0` raw-curve gate — AWS exact replay

## Verdict

**PRODUCER-EXACT PASS in two pivot orders; hostile review pending.**

At the fixed licensed three-center section, both exact AWS runs over

```text
Frac(Q[U,V]/(V^4-32V^2U^3+128U^6))
```

rebuild transport and first band, reduce genuine P12 to the constant unit
`-k/50`, lift the identity to original transported first rows, and pass a
plus-one negative control.  All certificate divisors are powers of `U`, so
the raw curve is killed off `U=0`.  Its `U=0` intersection is exactly the
origin, already rebuilt and killed by a unit-chart first-band certificate.
Thus the whole set-theoretic `H=P3=0` curve is producer-exactly empty, and the
earlier three-center cover has no remaining raw debt on `H=0`.

## Exact invariants

- field tower degree: 4 over `Q(U)`;
- transport rank: `3470/3602`;
- first-band rank: `38/132`;
- ascending source lift: 28 rows, 1,540 terms, chart `U^17`;
- reverse source lift: 38 rows, 2,152 terms, chart `U^19`;
- stdout SHA-256: ascending `c38471a004ac311ae01ae851bc98d6223829292ad74db20e2e6d9b7cd79c17b8`, reverse `900c38298b6dcaf8ed420afd3d947ca237b5581428d396b063de0875b595a30f`;
- archive SHA-256: `b207bbba13ee20d2719ef15504df632f66674d69072d97b83f4c9970d53e0e98`.

The complete report, archive, run metadata, source checks, stdout, and
resource stderr are frozen in
`cases/td6_c1_c2_c3_p3_raw_curve_aws_20260825/`.

## Review questions

1. Is the degree-four tower a faithful function-field model of the raw P3
   curve, with no hidden scaling or component loss?
2. Do the original-row replay, termwise denominator checks, and pure-`U`
   charts license the whole `D(U)` statement?
3. Does `U=0` intersect `H=P3=0` only at the already frozen raw origin, so
   the cross-package whole-curve conclusion is valid?

No neighborhood, full-centering, boundary/dead-stretch, SP-2, or JC2 claim is
made.
