# Frozen corrected Box02 result

The AWS execution tagged
`as_d7_corrected_q11_20260825T003952Z` completed all 27 shards and the
fail-closed aggregate with return code zero. Raw output, timing, return-code,
deployment, and source-check files are preserved byte-for-byte under
`REMOTE_RESULTS_as_d7_corrected_q11_20260825T003952Z/`.

Verify the transported bytes and recompute only the lightweight aggregate:

```sh
./verify_frozen_results.sh
```

This check does not rerun the finite-state compiler. That computation is
AWS-only. The result and refusal scope are in
`../../xmodel/as-fonly-d7-vertical-next-top-corrected-shards-20260825.md`.

