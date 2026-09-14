# sol56 small audit note

- Frozen receipt: `xmodel/ideation-20260906T0000Z-sol56.run.v2`.
- Input directory: `/tmp/jc2-lane.I83ieI/inputs`.
- Custody check: paired every numbered `_basename`/`_sha256` receipt field with
  `awk` and streamed the 12-line manifest to `sha256sum -c -`; result 12/12 `OK`.
- Roster check (`jq -s`): 66 frozen rows, 20 rows with `source.u_s >= 2`,
  `sum(split_window.leaf_count)=36`, and
  `sum(length(split_window.leaves))=36`. This is the basis of
  `OPEN[C-LEAF-CUSTODY-38-VS-36]` in the report.
- Charge-basis validator: `charge_basis=ABSENT` (no new exit-price assertion).
- Seal verification: PASS; body 24,460 bytes,
  SHA-256 `9f760760ec3cc503033a79acc61a4cd3b0a8cf045f277e367553337a2cfc14c6`,
  frozen basis `de78ca950def644a22c1bf5b6c877be8d043d0de`.
- Sealed full-file SHA-256:
  `23fd5cca53b615f3d93b0fd4b1126a26916c7ea493523e4d2ed8bbd9808f13b7`.
- Checked at 2026-09-06T00:27:52Z. No ledger edit, no `jc2-lean`, and no
  non-charged `ideation-*` submission was read.
