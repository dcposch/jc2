# Preregistration: quotient replay-marker diagnostic r1

Date: 2026-08-28

This is a diagnostic-only mutation of the two exact r6 scripts whose
quotient-ring syzygies reported `KERNEL_REPLAY_ZERO=0`. It cannot produce a
mathematical survivor or component-death verdict.

The exact frozen inputs are C8P branch 02
`bed61e93582dfefab3ffa5da5ea43a527887572c2c4b602e2249a2f251ccc076`
and triple branch 02
`e1c50b669a90e3c5a8a6984d34e13365600b11d19b9be5fbabc673edc7e9c021`,
extracted from r6 result archive
`cfd2c020b204beecaca5b60ee062aed8a1fe274a399c2ebda93d0d300a00c0f4`.
The original mathematical payload manifest remains
`ecd5dba798ab3157f4bf362361b630744fbadfbfe582dbc0d85523f6183f33c6`.

For each script, retain the exact ring, quotient ideal, 106-by-105 matrix,
syzygy call, kernel, and endpoint calculation. Compare the original
`size(module(M*N))==0` predicate against an entrywise quotient-ring equality
count. Then mutate the first kernel generator by adding the first coordinate
basis vector; the receiver matrix has exact first entry `1/4`, so this must
make the replay nonzero and supplies a negative control.

The narrow adapter diagnosis passes only if both scripts have all of:

- original size predicate false;
- every exact quotient-ring entry of `M*N` equal to zero;
- mutated replay nonzero, including its first pivot;
- unchanged quotient reducer/defining-ideal guards;
- zero swap and clean process-group closure.

Any disagreement is strict `NO_VERDICT_REPLAY_DIAGNOSTIC_DISAGREEMENT`.
Only a passing diagnostic licenses a new frozen adapter using entrywise replay
equality, followed by full unchanged-math AWS replay. No r6 verdict is
retrospectively promoted by this diagnostic alone.

Run one core on pinned r6a under
`ggv_lambda0_endpoint_strata_replay_diag_r1_20260828T143500Z_r6a`, with a
900-second master cap, 16-GiB address-space cap, zero swap, exact source
hashes, continuous process-group monitoring, and final no-orphan census.
