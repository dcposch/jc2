# Quarantine: V2 load-series precedence bug

Date: 2026-08-26

Status: **FULLY QUARANTINED; NO SOURCE-SUPPORT RESULT.**

The V2 compiler passed unparenthesized multi-term strings such as

```text
k60+sigma*k60_1+...+sigma^4*k60_4
```

to the frozen `tail_text` emitter.  For a load of exponent one, that emitter
joins factors by `*` but does not add parentheses around the supplied load
string.  The compiled source therefore contains terms of the form

```text
coefficient*k60 + sigma*k60_1 + ... + sigma^4*k60_4*(sigma^2)^6
```

instead of

```text
coefficient*(k60 + sigma*k60_1 + ... + sigma^4*k60_4)*(sigma^2)^6.
```

The same defect affects the V2 `k10` and `k2` jet series.  It explains the
spurious low grades and invalidates the reported counts `155` total / `120`
below grade 27, every printed row and dependency marker, and all prose in
`RESULT.md` that interprets them as source support.  Engine/validator PASS
only certifies internally consistent execution of the malformed compiled
polynomial.

V1 remains an independently useful fail-closed negative control: it made an
unlicensed direct division and its validator rejected the endpoint.  V2 is
preserved only as exact software-failure custody.  V3 must change only load
parenthesization, demand byte-level distributivity/count sentinels for all
three load families, and replay exact Q plus a good prime.  There is no
`a=9`, square, order-two, `(8,12)`, maximum-twelve, or JC2 conclusion.
