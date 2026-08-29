# V1 dual-AWS negative control: omitted formal `k60`

Date: 2026-08-26

Status: **NO VERDICT FOR THE COMPLETE `a=8` CLIENT.**  Preserve this package
immutably as a fail-closed software control.

## What passed

Both exact Q on Box03 and `F_65521` on r6d completed the engine with rc 0.
In both fields the `D(k60)` section passed every source, quotient, support,
row, denominator, and numerator sentinel, ending with

```text
A8Q0_ENDPOINT=PASS_A8_Q6_ZERO_SIMPLE_POLE
```

Thus V1 is dual-field producer evidence for the fixed-`a=8`, `D(p*k10*k60)`
simple-pole branch only.  This partial endpoint is not the preregistered
two-section theorem.

## Exact failure

The `V(k60)` section uses a source-support filter that differentiates with
respect to `k60`, but its generated source/target rings and four maps omitted
that formal symbol.  The first Singular diagnostic in both fields was

```text
? `k60` is not defined
```

at the construction of `A8QP_Rem28_1`; all later undefined-name messages are
cascades.  The validator correctly rejected the run at
`A8QP_SOURCE_DIVISIBLE=1`.  Engine rc 0 is therefore not a mathematical
endpoint.

The intended positive-valuation load remains
`k6=sigma*k61+sigma^2*k62`; adding an unused formal `k60` to the six
ring/map declarations is the minimal software repair and does not change
the branch equations.

## Custody

Exact-Q stdout SHA-256:
`1c84808aabcc29347caeb62c290a36d575e77d6ce1e8b3d85634635a199c51c9`.

`F_65521` stdout SHA-256:
`8702188009cfa1ab562254ca4725f7dc636671ee9ae36fa234e7807cb846aad0`.

Exact-Q stderr SHA-256:
`650aa6e49ca880fc2b623b61edb82fa489f75a3e33ae354794865cb4a69ed081`.

`F_65521` stderr SHA-256:
`dc6ccad36f4f4622d7737c3c7fc9322fc128650e5754cbb323b505355c110f0b`.

Both validation files have SHA-256
`fc097f0d8c97343df66b808c94e0315a0414195c5f8ad65d177f62d3838e1d8c`
and contain

```text
engine_rc=0
validator=FAIL_MISSING_OR_NONUNIQUE:A8QP_SOURCE_DIVISIBLE=1
```

Frozen V1 source manifest SHA-256:
`c18bdd9f55a108470ef166e6c0cfa243ab61b63f45742537046fdb6e583b5dc8`.

## Firewall

Nothing here proves the `V(k60)` section, all fixed `a=8`, any `a>=9`, the
square stratum, order two, `(8,12)`, maximum twelve, or JC2.  In particular,
no blanket square-forcing statement is licensed in the presence of tied
`k10,k6,k2` loads; the exact Chebyshev/Pell survivor remains mandatory.
