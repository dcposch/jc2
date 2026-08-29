# Registration: D1 `a=9` recursive Faber census V3, parenthesized loads

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS NAVIGATION REPAIR; NO THEOREM ENDPOINT.**

V2 is fully quarantined because multi-term load jets were inserted without
parentheses into the frozen factor-joining emitter.  V3 pins V2 byte-for-byte
and changes only the return value of `series()` for `k0,k60,k20`, wrapping
each complete jet in one parenthesis pair.  It then requires byte-level
sentinels proving that every load occurrence is followed by its full Faber
weight:

```text
(k10 jet)*(sigma^2)^2    exactly 190 occurrences,
(k6 jet)*(sigma^2)^6     exactly 72 occurrences,
(k2 jet)*(sigma^2)^10    exactly 27 occurrences.
```

The counts are the exact monomial census of the seven frozen tail rows.  V3
also rejects every unparenthesized `*k...+sigma*...` pattern before Singular.
All recursive grade/status/dependency checks are inherited unchanged.

Run exact Q on Box03 and `F_65521` on r6d, 16-GiB virtual-memory, 600-second
compiler, 1800-second Singular caps.  Require the three distributivity
sentinels, recursive identities, exactly 224 row-status markers, rc 0, no
diagnostics, and zero swap.

## Firewall

A PASS is a corrected finite source-support census only.  It does not reduce
later rows modulo earlier equations or prove a contact empty/nonempty.  There
is no `a=9`, square, order-two, `(8,12)`, maximum-twelve, or JC2 conclusion.
The tied-load Chebyshev/Pell solution remains a mandatory positive control.

