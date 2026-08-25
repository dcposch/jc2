# Frozen Box02 result

The AWS execution tagged
`as_d7_next_top_shards_20260825T001733Z` completed all 27 shards and the
fail-closed aggregate with return code zero.  Raw output, timing, return-code,
deployment, and source-check files are preserved byte-for-byte under
`REMOTE_RESULTS_as_d7_next_top_shards_20260825T001733Z/`.

Verify the transported bytes and recompute only the lightweight aggregate:

```sh
./verify_frozen_results.sh
```

This check does not rerun the finite-state compiler.  That computation is
AWS-only.  The theorem and refusal scope are in
`../../xmodel/as-fonly-d7-vertical-next-top-shards-20260825.md`.
