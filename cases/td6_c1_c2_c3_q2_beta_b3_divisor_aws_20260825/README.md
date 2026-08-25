# TD6 q2-beta closure of the raw B3=0 center divisor

Frozen status: **producer-exact whole-divisor closure; promotion held until
the independent V43 generic canonical-serialization gate; hostile review
pending.**

This package stays inside the fixed source-typed normalized A3 center
section with `q_beta=t+beta*t^2+t^25` and

```text
B3=4C^2U^2-4CV^2U+24CU^4+V^4-20V^2U^3+20U^6.
```

It retains the direct q-prime term, complete transport, genuine P12, staged
N13, original first rows, and every denominator.  The birational chart is an
exact parameterization, not a source scaling or gauge normalization.

## Canonical generic-B3 identity

Two independent V44 runs from one byte-identical archive, on r6d and Box03,
produced byte-identical mathematical stdout, SHA256

```text
a33dc711c1b8b7d215912aa8c86c43eac8b9be43cc30e1c219583bf952c937ee.
```

Both have transport rank `3470/3602`, first rank `38/132`, an exact
genuine-P12 lift through 28 original rows and 1,649 multiplier terms, and a
39,658-slot termwise source audit.  The P12 affine-beta tail is cancelled by
the exact staged `N13=(k/25)beta` contribution without beta division; the
combined residual is the constant unit `-k/50`.

Writing the birational parameters as `tau` and `w` (the producer variables
named `C` and `V`), the complete denominator radical is exactly

```text
tau * (tau-2) * w * (2tau-1) * (tau^2-4tau+2).
```

No other pivot, norm, or termwise factor occurs.

## Exact chart and complete raw cover

The producer verifies the raw B3 identity, inverse formulas, a plus-one
control, the line-intersection factorization, and the following boundaries:

- the chart requires `tau*w*(tau-2)!=0`;
- `tau=0`, the affine base point `(-5,0)`, and the parameter infinity route
  into `V=0`; there
  `B3=4U^2(C+U^2)(C+5U^2)`;
- `tau=2` and `w=0` specialize to the origin;
- the only new finite factors are `2tau-1` and `tau^2-4tau+2`.

The separately frozen all-beta rational-line package closes both non-U
components of `B3,V=0`.  The separately frozen all-beta `U=0` theorem closes
the U-component and origin.  The separately frozen exact N13 curve package,
fixed-beta P12 dependencies, and origin theorem close the two finite factors
`tau=1/2` and `tau^2-4tau+2=0` for every beta.

Together with the V44 unit identity on the remaining chart open, this exact
constructible cover closes the whole set-theoretic divisor `B3=0` for every
beta in the fixed A3 source scope.

## Canonicalization custody and negative control

V39 proved the same ranks, exact expressions, base P12, source identities,
denominators, and slot audit, but four reporter hashes included process
addresses through legacy `repr(E3)`:

```text
first_full_beta_P12_pivot_digest
remainder_beta_tail_sha256
N13_exact_value_sha256
N13_multiplier_sha256
```

V44 replaces these with serialization through all 18 exact rational E3
coordinates.  Every canonical field and the complete stdout agree
byte-for-byte across r6d and Box03.  V39 is retained only as a custody-
negative control; its mathematical expressions and unaffected base-P12
digest agree.

Campaign policy also requires V43's matching generic-open replay to finish
rc0 with byte-identical stdout on both hosts before promotion.  This package
is immutable now but remains policy-held until that gate lands.

## AWS custody

V44 archive SHA256:
`fd6f420bf88a832316077c77a421beb43f69054b1007d8653ae306f4d00bfe0b`;
V44 source-manifest SHA256:
`e72aa70e735cb807e014298feb5696146202d20f3843b87466f779c9a4bc93a9`;
producer SHA256:
`77194c4b9a30b9190da026e94c0f476449cbeeba8a679b1abfa6768c37caf2ef`.
Both hosts used Python 3.12.3, python-flint 0.9.0,
`PYTHONHASHSEED=0`, passed inherited source checks, and exited zero.

## Scope quarantine

This theorem closes only `B3=0` for the fixed q2-beta A3 source.  It does
not yet close the generic open, vary a fourth center/boundary/dead-stretch/
F1/pole modulus, kill whole TD6 or SP-2, prove a landing theorem, or resolve
JC2.
