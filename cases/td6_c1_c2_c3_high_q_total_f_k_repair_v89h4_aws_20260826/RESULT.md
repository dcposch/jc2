# TD6 V89H4 high-q total-F denominator-repair result

Date: 2026-08-26

Producer verdict: **PASS on Box02 and r6d.**

## Exact family and identity

Set `q2,...,q14=0`, retain independent untruncated `q16,...,q24`, and keep
q15 absent under its separately reviewed target shear.  Both clients rebuilt
literal V87 transport, all 38 packed raw FIRST sources, and genuine raw P12.
Their q-zero source digests match frozen V85 byte for byte.

The reviewed q-zero FIRST pivot block gives an exact 242-edge DAG with
`N^2=0`; the finite polynomial inverse, both matrix products, normalized
original-source replay, literal P12 reduction, and P12/FIRST omission
controls all pass.  The P12 remainder is exactly the frozen q-zero unit and
has no positive high-q term.

The complete rational certificate denominator factors as

```text
(1/8) * K * B3 * U^2 * H^2,
```

where

```text
K = 2*C*V^2*U + 16*C*U^4 - V^4 - 14*V^2*U^3 + 16*U^6.
```

Thus K occurs to exponent exactly one.  The client clears that relation
coefficientwise and consumes the separately frozen exact identity

```text
B3 = K + 2*F*(2*C*U - V^2 + 2*U^3)
```

without inverting K or F.  The resulting literal identity has P12, all 38
original FIRST sources, and F on its right-hand side, and target

```text
(1/8) * B3^2 * U^2 * H^2.
```

All 2,651 nonzero multiplier coordinates are emitted exactly.  The final
family common denominator is `U*H`, so every denominator factor and the
target are units on the registered `D(U H B3)` open.  No q expression is
inverted.  Omitting P12, one active FIRST source, or F breaks the composed
identity.

Consequently, on this exact retained high-q residue block and registered
open, the literal ideal `(P12,FIRST,F)` is the unit ideal.  This is a total-F
identity, not a P12/FIRST-only identity.

## Scope firewall

The result sets q2 through q14 to zero.  It does not cover any low-q unit
chart, total-Rees/source lifting, omitted correction or moving-center
variables, a source point, whole fixed A3, TD6, SP-2, or JC2.

## Custody

- source archive:
  `84199204a41f7d26bcc6a1329cd72bedf2c60a0ae9590cf1cd04ee5373230d91`;
- source manifest:
  `c9f6b7078bfbf8b0bdd3df71e50e54303b36d88c25e748b2802a7cdab48bc842`;
- client:
  `6e810be852691aa5aa2f60b85a3996c3146ae72e6bae28fed1903c35de05bf61`;
- exact result:
  `d51b6cbc6beb807e8a220c0a097139f4e033d6135caf44c56e89b4493161f098`;
- cleared multiplier table:
  `e3793a7add52c22a7fff745ce196f5dad8c0cd7e4d5407c0e11295484df3ecf2`;
- byte-identical mathematical stdout:
  `41df45c84197b5ec44d7d779c24b81e35f1297ed0ea49d7cb66186c887a5d288`.
