# `(8,12)` order-one fixed-load probes: dual timeout controls

Date: 2026-08-26

Status: **DUAL AWS TIMEOUT BEFORE THE FIRST STANDARD BASIS; NO
COMPONENT, `r7`, DIVISOR, OR ORDER-ONE VERDICT.**

## 1. Frozen source and launches

The source package freeze has SHA-256
`bc8b149cb5b20245b494d99294cbcecd408123d3faf31b6cee326ff3788e6765`.
Both remote freeze checks and both AWS compilers returned successfully.
The compilers independently printed exactly one copy of each source sentinel

```text
ORDER1_SOURCE_HASHES=PASS
ORDER1_SHARED_FABER_REPLAY=PASS
ORDER1_GAUGES=h0,h4,h8
ORDER1_CONFIG=A or B
```

and emitted the frozen inputs

```text
064ae9342b944dfe489d6a3710f6833c7c34256ec262939b056d54b995eb4371
  tuple A / characteristic 32003
02e43376af5562fdc251802a48c9112ed5884b655eb95652258f1bac21507309
  tuple B / characteristic 65521.
```

## 2. Endpoints

| tuple | host | registered tag | cap | endpoint |
|---|---|---|---:|---|
| A / `p=32003` | Box03, `ip-172-30-0-249` | `max12_812_order1_fixedload_A_p32003_20260826T043500Z_box03` | 2400 s / 64 GiB | `rc=124`, `TIMEOUT_NO_VERDICT` |
| B / `p=65521` | r6d, `ip-172-30-0-45` | `max12_812_order1_fixedload_B_p65521_20260826T043500Z_r6d` | 2400 s / 64 GiB | `rc=124`, `TIMEOUT_NO_VERDICT` |

Both engines ran from `2026-08-26T04:35:39Z` through
`2026-08-26T05:15:39Z`.  Neither printed `ORDER1_STD_DONE`.  Inspection of
the frozen client shows that the next statement after the last printed
configuration sentinel is

```text
I=std(I);
print("ORDER1_STD_DONE");
```

so both jobs timed out while computing the first standard basis of the six
fixed-tail equations.  They never began `minAss`, either `a6` chart, the
`r7` graph, or the plane projection.  The copied `.meta`, `.stdout`,
`.stderr`, `.validation`, compiler records, and source snapshot agree
byte-for-byte with the remote jobs (apart from ignored Python bytecode,
which is not evidence).

## 3. Consumption by the reviewed `r7` screen

The confirmed terminal theorem requires the normalization of an actual
source-relevant component and the complete divisor or critical values of
the actual `R=r7` graph.  These probes produced none of those objects.
Consequently the `r7` one-pole/pure-power screen cannot be applied, and the
timeouts are neither survivors nor failures of that screen.

The correct successor is not a longer monolithic run.  It is to use the
terminal pure-power condition before or during component construction: graph
`r7`, impose a bounded pure-power/one-pole ansatz or its exact critical-value
equations, and split charts/components before any large standard basis.
Every infinity and chart-complement point remains mandatory.

## 4. Firewall

This artifact records two reproducible timeout controls only.  It proves no
fibre dimension, component count, characteristic-zero lift, source coverage,
`r7` divisor, branch-value statement, order-one exclusion, `(8,12)`, maximum
twelve, or JC2.
