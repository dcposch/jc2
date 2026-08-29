# TD6 V89H8 q13 polynomial extension of the q14 functional

Date: 2026-08-26

Status: **producer-tier exact theorem; dual AWS passed; hostile review
pending.**

## Result

Restore q13 as an independent untruncated variable in the frozen V89H7
scope, retaining `q14,q16,...,q24`, keeping `q2,...,q12=0`, and omitting
q15 only under the reviewed target shear.  After exact `F=0` specialization
on `D(U)`, the registered 38-pivot original-FIRST graph has one cyclic SCC,

```text
(0,1,2,3,4,5,6,12,13),
```

and its exact determinant is one.  Hence the full pivot block has a
two-sided polynomial inverse over
`Frac(Q[V,U])[q13,q14,q16,...,q24]`; no q polynomial or new base factor is
inverted.  The normalized rows recover all 38 original FIRST sources and
have monic distinct pivots with pivot-free tails.

The canonical literal-P12 normal form has exactly two nonconstant q
monomials:

```text
(13,), (14,).
```

Its total q-degree and q13-degree are both one, and there is no q13*q14
term.  The pure-q14, empty-parameter, E3-coordinate-0 functional is exactly
the promoted V89H7 value and remains nonzero.  Thus that quotient functional
extends polynomially across arbitrary q13 on this residue block.

## Custody

- SCC determinant SHA256:
  `2dcec6d73c86d77135f2e8d493aa388f3f8409400e3e3b84538a4961da33dc56`.
- Canonical remainder SHA256:
  `82694db3910d86d87061d86626c4ac1f481577dcde50f4954c3963693c02637a`.
- Exact q-support SHA256:
  `0068f57c118fb81e115596086ee08c4ab8104f987ab07b90835f91c0d23d1832`.
- Exact result SHA256:
  `bb220c3f46e3f5bfe45c3b6819d08d8f66262e99b57e01e67b0a563b728c9cef`.

Box02 and r6d returned rc=0 with byte-identical mathematical artifacts and
stdout, maximum RSS below 298 MiB, and zero swap.

## Firewall

This restores q13 only.  It does not restore q2,...,q12, totalize q15 as a
source modulus, prove a unit ideal or source-point exclusion, supply a
total-Rees lift, close whole fixed A3 or TD6, or resolve JC2.

