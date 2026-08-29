# TD6 V89H7 minimal q14 dual-functional preregistration

Date: 2026-08-26

Status: producer validation client; no result claimed before dual AWS replay.

## Parent and scope

Consume only the frozen V89H6 producer result and rebuild its literal source:
`q2,...,q13=0`, q15 absent only under the reviewed target shear, and
`q14,q16,...,q24` independent and untruncated.  Specialize exactly by
`F=C*U-V^2+U^3=0` on `D(U*H*B3)`.

## Exact dual functional

Recompute the two-sided polynomial inverse of the full 38-row original FIRST
pivot block and the canonical normal form modulo those rows.  Define

```text
lambda(g) = scalar-coordinate 0 of the coefficient of
            q14 * (empty parameter monomial)
            in NF_FIRST(g mod F).
```

Verify explicitly that the normalized rows have monic distinct pivot
variables and pivot-free tails, that the original and normalized FIRST
modules agree by two-sided maps, and that all 38 original FIRST sources reduce
to zero.  Emit the exact rational-function value of `lambda(P12)` and its
licensed denominator.  Require it to be nonzero.  This is the smallest
single-coordinate dual witness selected before fresh-prime evaluation.

## Fresh-prime validation

Independently rebuild the 18-dimensional finite algebra at the fresh prime
and base point

```text
p=1000033, (C,V,U)=(15,4,1), F=0, H=12, B3=256.
```

Invert original FIRST separately at q14=0 and q14=1, divide literal P12, and
compare the complete difference against the evaluation of the exact class.
Require coordinate zero of the empty parameter monomial to equal the exact
functional value modulo p and to be nonzero.  The prime and base point are
immutable even if a denominator or pivot fails.

Both Box02 and r6d must run exact-Q and fresh-prime paths from one immutable
archive and produce byte-identical mathematical artifacts.  No unit-ideal,
source-point, low-q-chart, total-Rees, whole-TD6, or JC2 conclusion is in
scope.

