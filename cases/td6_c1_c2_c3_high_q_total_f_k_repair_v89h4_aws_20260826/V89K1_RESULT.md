# TD6 V89K1 `K` modulo `F` unit result

Date: 2026-08-26

Producer verdict: **PASS on Box02 and r6d.**

## Exact identity

For the literal V85 definitions

```text
F  = C*U - V^2 + U^3,
B3 = 4*C^2*U^2 - 4*C*V^2*U + 24*C*U^4
     + V^4 - 20*V^2*U^3 + 20*U^6,
```

and the H1 obstruction factor

```text
K = 2*C*V^2*U + 16*C*U^4 - V^4 - 14*V^2*U^3 + 16*U^6,
```

both exact clients verified coefficientwise

```text
B3 = K + 2*F*(2*C*U - V^2 + 2*U^3).                 (1)
```

The coefficient-perturbed expression with `2` replaced by `1` is nonzero.
Under `F=0`, direct exact substitution gives `K=B3=V^4`; the client records
the separately cleared forms `U*V^4` and `U^2*V^4` because `K` and `B3` have
different degrees in `C`.

## Consequence and firewall

Equation (1) proves that the residue class of `K` is the registered unit
`B3` modulo `(F)`.  Hence on `D(B3)`, `K` is a unit modulo every literal
source ideal containing `F`, with inverse class `B3^-1`.  No inverse of `K`
or `F` is used.

This does **not** say that `K` is a unit modulo the P12/FIRST-only ideal used
by H1's rational collapse.  To repair the total-F lane, a separate exact
client must first clear H1's K denominator, emit the resulting power and
original-source multipliers, and compose that relation with (1).  V89K1
alone makes no P12/FIRST, source-point, fixed-A3, TD6, SP-2, or JC2 claim.

## Custody

- V2 source archive:
  `9a23e8b31eef977fc1ca952dfbcfacdb10f27a93b9b4ef80b6b1a3fdc78e4e49`;
- source manifest:
  `c0536528edac94f756b753c33cceac8e0b02cfcdc99557f4c0d19d2ef33a32d6`;
- client:
  `d21e1492cc2248cbc325352ae93dd55538d7102470e0fd1d9bbabd3e1566a186`;
- exact result:
  `f2455554a58366f0100333dd5717d421dafad0b5574ee312e8376a3265f5683e`;
- byte-identical mathematical stdout:
  `8e8d47065655535ba352f33161935c296d4f5d95005a554c6f2a7fdb3a09c69e`.
