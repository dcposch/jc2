# Frozen AWS source-audit result

The exact integer replay ran on Box02 under tag
`as_d7_top_frob_erratum_20260825T003321Z` and returned zero.  Its output,
empty stderr, timing, metadata, and source-manifest check are preserved under
the `REMOTE_RESULTS_...` directory.

Local verification is intentionally hash-only:

```sh
./verify_frozen_result.sh
```

Do not rerun the symbolic source audit locally.  The companion report gives
the corrected equations, preservation table, and refusal scope.
