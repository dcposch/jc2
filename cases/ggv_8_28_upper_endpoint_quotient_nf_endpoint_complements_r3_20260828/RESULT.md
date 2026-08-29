# R3 complement-recursion results

R3 produced one exact but incomplete recursion, four first-node timeouts, and one
adapter failure. It produced no whole-stratum or ambient endpoint theorem.

## Component classifications

- `q1p03`: `NO_VERDICT_OPEN_REMAINDER`. Twelve exact nodes were processed: ten
  opens were power-certified empty and two proper charts were endpoint-dead. A
  nonempty remainder remained after the registered node budget. Archive SHA:
  `dc5f44f8784281490c194d2956b6f2d6a9a6a3c1b8e0ceeddc5212e100afc42a`.
- `p`: `TIMEOUT_NO_VERDICT`; archive SHA
  `f13a0986f1aad135eaa81a166387d9220d8c90d0569ff910524993a8c20dfc33`.
- `c8p02`: `TIMEOUT_NO_VERDICT`; archive SHA
  `3d57d2cdb6798503fe37254c717d66c15999c31f5658df13ede433f9d736e9e6`.
- `q1p02`: `TIMEOUT_NO_VERDICT`; archive SHA
  `fee56da2770f3bfd5ec4a6a816362ec0fc25475d313352fe3cd28b7fc7c16c3b`.
- `triple02`: `TIMEOUT_NO_VERDICT`; archive SHA
  `e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1`.
- `triple03`: `ADAPTER_FAILURE_NO_VERDICT`; the post-saturation pivot replay
  incorrectly recomputed a transform rather than base-changing the banked one.
  Archive SHA:
  `ee949701e669cdabb8408c94e77ba931c70085c545fc8d36f14604ea96c7ed8d`.

The four timeout classifications supersede the archive-internal generic
`ADAPTER_FAILURE_NO_VERDICT` label only as operational taxonomy. They make no
mathematical inference. See `TIMEOUT_RECLASSIFICATION.md`.

R3 predates the mandatory planted-nonzero endpoint semantic control. Its valid
node-local results are retained as exact intermediates only and are not used for a
correlated whole-component claim.
