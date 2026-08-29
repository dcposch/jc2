# V24R3 independent-prime properness preflight

Date: 2026-08-27

Status: **PASS — THEOREM-INELIGIBLE MODULAR PREFLIGHT.**

The frozen Box02 scan changed only the coefficient field of the same literal
35-generator prior ideal plus the localization equation at `k10_0*W`.  All
three preregistered primes returned

```text
              normal form of 1    dimension    classification
p = 32003             0               -1            UNIT
p = 65519             0               -1            UNIT
p = 65537             0               -1            UNIT
```

The forced-unit mutation fired in each process.  The result agrees with the
earlier `p=65521` unit fibre, so `65521` does not look exceptional among these
four primes.  This observation is only a prioritization signal for the live
tracked exact-Q V24R2 computation.

- tag:
  `max12_812_order2_u2_62_k00_v24r3_multiprime_20260827T141134Z_box02`
- wall/CPU: 5:03.89 / 881.85 user seconds across three independent one-core
  Singular processes
- maximum recorded RSS: 1,840,900 KiB; swaps: zero
- result JSON SHA256:
  `413216635dd886a0e5e4893bfa74491a4fe3265cde80603bbf8c641f66b5d16c`
- evidence-manifest SHA256:
  `3a785562f366355fa84a3b4ecccb5e4e601b26e0fb3538ab906b9440ed38fa8d`
- independent local harvest replay: 15/15 evidence entries

## Firewall

No finite set of special fibres proves that the characteristic-zero ideal is
unit.  Conversely, a modular proper fibre could arise from a denominator in
an exact-Q certificate.  V24R2 remains the sole exact gate.  V24R3 proves no
exact-Q membership, compatibility, chart emptiness, stratum statement,
finite jet, arc, closure incidence, order-two, maximum-twelve, or JC2 claim.
