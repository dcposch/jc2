# TD6 q2-beta closure of the raw H=0 center divisor

Frozen status: **producer-exact whole-divisor closure; promotion held until
the independent V43 generic canonical-serialization gate; hostile review
pending.**

This package stays inside the fixed source-typed normalized A3 center
section with

```text
q_beta=t+beta*t^2+t^25,
H=C-3U^2,
P3=V^4-32V^2U^3+128U^6.
```

It retains the full source transport, direct
`q_beta'=1+2 beta t+25t^24`, genuine P12, staged N13, original first rows,
and every denominator.  No source scaling or weighted-projective
normalization is used.

## Canonical generic-H identity

Two independent V44 runs from one byte-identical archive, on r6d and Box03,
produced byte-identical mathematical stdout, SHA256

```text
609349a53624531c1617104e2998ecf057192fea45bbe0ab41d7c2f24a1daf81.
```

Both have transport rank `3470/3602`, first rank `38/132`, an exact
genuine-P12 lift through 28 original rows and 1,640 multiplier terms, and a
39,013-slot termwise source audit.  P12 reduces to a three-term affine-beta
remainder with constant part `-k/50`; its two-term beta tail is cancelled by
the staged `N13=(k/25)beta` contribution without beta division.  The exact
combined residual is the constant unit `-k/50`.

The complete denominator radicals on `H=0` are exactly

```text
U, V, P3.
```

Specifically, raw P12 and the first rows use `UV`; the lifted first
relations use `U^2 V P3`; the termwise products use `U V^2 P3`; the N13
multiplier has denominator one.  No other norm or pivot factor occurs.

## Complete raw cover

- `U=0` is empty for every beta by the separately frozen unit-compatibility
  theorem.
- `V=0,H=0` is empty for every beta by the separately frozen rational-line
  P12/N13 unit identity; its only denominator is a power of `U`.
- `P3=0,H=0` is empty for every beta by the separately frozen N13 curve
  theorem, the fixed-beta genuine-P12 curve theorem, and the all-beta origin
  closure.  Its only new chart factor is `U`.

Together with the V44 identity on `D(UVP3)` this exact constructible cover
closes the whole set-theoretic divisor `H=0` for every beta in the fixed A3
source scope.

## Canonicalization custody and negative control

V39 already proved the same ranks, exact algebraic identities, base P12,
denominator factors, and source-slot audit.  Four SHA reporter fields were
not portable because its imported digest hashed `repr(E3)` even though E3
has no custom representation; process object addresses entered:

```text
first_full_beta_P12_pivot_digest
remainder_beta_tail_sha256
N13_exact_value_sha256
N13_multiplier_sha256
```

V44 serializes every E3 value by its 18 exact rational coordinates before
hashing.  The two hosts agree byte-for-byte on every canonical field.  The
V39 stdout and archive are retained here as a custody-negative control, not
as promotion evidence.  Its unaffected base P12 digest, ranks, identities,
denominators, and term counts agree with V44.

Campaign policy additionally requires the matching V43 generic-open replay
to complete rc0 with byte-identical stdout on both hosts before promotion.
This package is immutable now but remains policy-held until that gate lands.

## AWS custody

V44 archive SHA256:
`fd6f420bf88a832316077c77a421beb43f69054b1007d8653ae306f4d00bfe0b`;
V44 source-manifest SHA256:
`e72aa70e735cb807e014298feb5696146202d20f3843b87466f779c9a4bc93a9`;
producer SHA256:
`77194c4b9a30b9190da026e94c0f476449cbeeba8a679b1abfa6768c37caf2ef`.
Both hosts used Python 3.12.3, python-flint 0.9.0,
`PYTHONHASHSEED=0`, passed all inherited source checks, and exited zero.

## Scope quarantine

This theorem closes only `H=0` for the fixed q2-beta A3 source.  It does not
yet close generic `B3=0` or the generic open, vary a fourth center/boundary/
dead-stretch/F1/pole modulus, kill whole TD6 or SP-2, prove a landing
theorem, or resolve JC2.
