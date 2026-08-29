# Fail-closed timeout sidecar

The following four archives stopped in the first-node Singular saturation stage
at the explicit 900-second stage cap. Each `saturation.result.json` records
`timed_out: true`, elapsed time approximately 900 seconds, nonzero return code,
empty stderr, and only pre-terminal saturation markers. No node result was
accepted.

| Component | Saturation elapsed (s) | Archive SHA-256 |
|---|---:|---|
| `p` | 900.020597 | `f13a0986f1aad135eaa81a166387d9220d8c90d0569ff910524993a8c20dfc33` |
| `c8p02` | 900.011391 | `3d57d2cdb6798503fe37254c717d66c15999c31f5658df13ede433f9d736e9e6` |
| `q1p02` | 900.019921 | `fee56da2770f3bfd5ec4a6a816362ec0fc25475d313352fe3cd28b7fc7c16c3b` |
| `triple02` | 900.006164 | `e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1` |

Strict sidecar classification for every row: `TIMEOUT_NO_VERDICT` with zero
mathematical content. The archive bytes and their original internal labels are
preserved unchanged.
