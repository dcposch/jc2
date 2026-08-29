# Promotion: TD6 V89H8 q13 extension of the q14 quotient functional

Date: 2026-08-26

Lifecycle: **PROMOTED / HOSTILE-REVIEW CONFIRMED.**

## Promoted theorem

On the literal normalized three-center source slice, set

```text
q2=...=q12=0,
q15=0 only in the reviewed target-shear coordinate,
q13,q14,q16,...,q24 independent and untruncated,
F=C*U-V^2+U^3=0,
```

and work on `D(U*H*B3)`.  For all 38 original packed raw FIRST sources,
the registered pivot block has one cyclic SCC,

```text
(0,1,2,3,4,5,6,12,13),
```

whose determinant is exactly one.  The full block therefore has an exact
two-sided polynomial inverse over
`Frac(Q[V,U])[q13,q14,q16,...,q24]`; no q polynomial or new base factor is
inverted.  The normalized sources recover all original FIRST rows and give
a unique monic, distinct-pivot, pivot-free-tail normal form.

The canonical normal form of literal P12 has nonconstant q support exactly

```text
(13,), (14,).
```

It has total q-degree one and no mixed q13*q14 term.  The pure-q14,
empty-parameter, E3 scalar-coordinate-zero functional is exactly the
promoted V89H7 functional

```text
N / [V^3*(V^2-4U^3)^2] != 0.
```

Thus the V89H7 splitting-independent q14 quotient functional extends
polynomially across arbitrary q13 on this exact residue block.

## Validation and custody

- Producer result:
  `cases/td6_c1_c2_c3_q13_q14_mod_f_functional_extension_v89h8_aws_20260826/RESULT.md`,
  SHA256 `646dd1162cc2e6aa36c3fe72bea5c64a44e19361323593a12fc4c7f137cc0292`.
- Producer freeze SHA256:
  `56c0f208bb3e988577b11ca375089cd4586f413a11bfff2619b79d183dd296bd`.
- Hostile review:
  `xmodel/td6-v89h8-q13-functional-extension-hostile-review-report-20260826.md`,
  SHA256 `49865ee96582302b6bb9a1aa6aa47733ab88dc738d28ed67861b804a2d90240a`,
  verdict `CONFIRMED`.
- Box02 and r6d exact artifacts and stdout are byte-identical with rc=0.
  The SCC determinant, canonical remainder, and q-support artifact SHAs are
  respectively `2dcec6d73c86d77135f2e8d493aa388f3f8409400e3e3b84538a4961da33dc56`,
  `82694db3910d86d87061d86626c4ac1f481577dcde50f4954c3963693c02637a`,
  and `0068f57c118fb81e115596086ee08c4ab8104f987ab07b90835f91c0d23d1832`.

## Scope firewall

This restores q13 only beyond V89H7.  It is not a unit-ideal or source-point
exclusion, a q2,...,q12 theorem, q15 as a source modulus, a total-Rees/source
lift, whole fixed A3, TD6, SP-2, or JC2 result.
