# TD6 V89H7 minimal q14 dual quotient-functional witness

Date: 2026-08-26

Status: **producer-tier exact theorem; dual AWS and fresh-characteristic
validation passed; hostile review pending.**

## Scope and quotient

Use the literal V89H6 source with `q2,...,q13=0`, q15 absent only under the
reviewed target shear, and independent untruncated
`q14,q16,...,q24`.  Set `F=C*U-V^2+U^3=0` on `D(U*H*B3)` and work over

```text
K = Frac(Q[V,U]),  C=(V^2-U^3)/U.
```

The controlling replay recomputed the full polynomial inverse of the 38-row
original FIRST pivot block.  The normalized rows have distinct monic pivot
variables and pivot-free tails; exact two-sided maps recover all original
FIRST rows, and each of the 38 original sources reduces to zero.  Thus their
normal form defines the quotient by the full original FIRST module, not an
H5 chosen splitting.

## One-coordinate functional

Define the K-linear quotient functional

```text
lambda(g) = scalar coordinate 0 of the coefficient of
            q14 * (empty parameter monomial)
            in NF_FIRST(g mod F).
```

This single coordinate annihilates the full original FIRST module.  On
literal P12 it is

```text
N / [V^3*(V^2-4*U^3)^2],
```

where

```text
N = 3856216/375*V^10*U^2
  + 1625866424/375*V^8*U^5
  + 30525031264/375*V^6*U^8
  - 10638708808/375*V^4*U^11
  - 4168187296/75*V^2*U^14
  + 710528/15*U^17.
```

The numerator is a nonzero polynomial, so `lambda(P12) != 0`.  On `F=0`,
`B3=V^4` and `U*H=V^2-4*U^3`; hence every denominator factor is licensed on
`D(U*H*B3)`.  The exact functional artifact SHA256 is
`bdf711b8b1951e462111e497bc520448503ec700d4ad4f1e86827a5227633233`.

## Fresh-characteristic validation

An independent finite-algebra replay at the preregistered fresh point

```text
p=1000033, (C,V,U)=(15,4,1), F=0, H=12, B3=256
```

separately inverted original FIRST at q14=0 and q14=1 and divided literal
P12.  Its complete difference equals the evaluation of the exact 17-record
class (SHA256
`d06b9f29227c3ab081c301314a5567050de949dffd1638c9595e56ae42f64153`).
The selected functional evaluates to

```text
lambda(P12) = 159760 mod 1000033 != 0
```

with witness SHA256
`82101c4be864b9227e7a5526de3352724b43187a51589964be872211245b76b9`.
Box02 and r6d returned rc=0 with byte-identical mathematical artifacts and
stdout, maximum RSS below 296 MiB, and zero swap.

## Custody correction and firewall

V1 stopped before algebra because its minimized archive omitted a nested
compiler import.  It is preserved strictly as a packaging-negative run in
`V1_PACKAGING_ERRATUM.md`.  V2 audits the complete 56-file non-bytecode
payload closure before execution.

This functional witnesses only the narrow nonzero q14 cokernel class.  It is
not a `1 in (P12,FIRST,F)` identity, source-point exclusion, low-q unit-chart
result, total-Rees theorem, whole fixed-A3 result, TD6 theorem, SP-2 theorem,
or resolution of JC2.

