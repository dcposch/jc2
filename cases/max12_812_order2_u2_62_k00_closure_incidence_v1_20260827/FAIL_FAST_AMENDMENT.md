# Fail-fast amendment

Date: 2026-08-27

The frozen V1 Singular input uses `quit(code)` on internal gate failures.
Singular 4.4.1 reports that form as undefined and may continue.  The external
validator still fails closed: it rejects every `K00_FAIL` marker and every
`?` diagnostic, and therefore cannot promote such a run.  The defect is
failure to stop early, not acceptance of a bad endpoint.

Both registered V1 lanes passed every pre-saturation source, type, invariant
core, explicit identity, and restriction-first unit gate, so this defect has
no effect on their current mathematics or stage.  Successors should use
`exit(code)` (or a proven supported termination form) to fail fast as well as
fail closed.
