# Promotion: TD6 all-q P13/FIRST coordinate-12 unit

Date: 2026-08-26

Status: **PROMOTED AT THE NORMALIZED LOCALIZED SCOPE BELOW.**

## Theorem

On the frozen normalized three-center slice

```text
p=t^15,
q=t + sum_{e=2..14,16..24} q_e*t^e + t^25,
F=C*U-V^2+U^3=0,
D(U*H*B3),
```

with q15 absent only under the reviewed target shear, all 22 displayed q
coordinates arbitrary and untruncated, and all 94 quotient variables free,
the exact normal form of literal CURRENT degree 13 modulo all 38 original
FIRST rows has E3 coordinate 12

```text
(3500000000/9)*(U/V).
```

It has no q or quotient-variable dependence.  On `F=0`,

```text
B3=V^4,  U*H=V^2-4*U^3.
```

Hence `U` and `V` are units on the registered open and this coordinate is a
unit.  Therefore literal P13 together with original FIRST has no common zero
on this exact slice; P12 is unnecessary.

## Evidence and review

- H15 producer result SHA-256:
  `29d5723b0d920840dbdfe72398624cfc0672843dbbf1d713b2fdd29dea52712c`;
- complete P13 normal-form SHA-256:
  `9af3240d4016ad99766122303465d2cea7a10dc5e71b489f62564b9c3540c2d8`;
- H18 combined result SHA-256:
  `0f152a88ba6422b04a3b4274ad5a0e71996c1c65395c7518b6e725321ab32d7f`;
- H18 combined evidence SHA-256:
  `bc9590017fb0f6942c9b7d396ba2b95e56fd1cbad2fc8c2b84e2b753bf79932d`;
- H15 terminology erratum SHA-256:
  `27d8289d7215d16806d1f1197b137acc7d49b0d75a05c766833eaaa38db44418`;
- independent hostile-review SHA-256:
  `cb4a85e298aacbbe5e1dc68c23d3f3819b7aa880d705da683d20fb61a06c1fc8`,
  verdict `CONFIRMED`.

The reviewer rechecked the full transitive hash closure, audited the literal
P13 and FIRST construction, parsed both AWS copies independently, confirmed
the corrected census of 238 E3-vector records and 535 nonzero scalar entries,
and verified the localized-ring implication.  The two H18 runs are custody
replays of the same H15 output, not independent algebraic recomputations.

## Scope firewall and certificate debt

This is a quotient/no-common-zero theorem on the displayed normalized
`F=0,D(U*H*B3)` slice.  The package does not yet emit original-FIRST
membership multipliers or a denominator-cleared identity retaining total
`F`; H19R1 is the certificate successor.  It also does not restore q15 as an
independent source modulus, cover omitted source moduli or boundary charts,
give a total-Rees/source cover, close TD6, prove SP-2, or resolve JC2.
