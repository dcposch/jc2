# Repaired-V2 localized-fibre review custody cleanup

Date: 2026-08-25  
Status: **NONMUTATING CUSTODY NOTE**

The first detached Grok attempt (PID 91728) failed closed: both intended
report and log are zero-byte files with SHA256 `e3b0c44298fc...`, and no run
record exists.  They are not evidence.

The fresh managed review is the `v2b` endpoint recorded in
`max12-912-order3-nu-q8-w0-localized-fibre-classification-repaired-v2-review-grok-20260825-v2b.run`.
Its report SHA256 is
`fefd0fa7637a9f5565e2204db469d9b10eae4123fde512a7d73f542e48889362`
and its verdict is `CONFIRMED_WITH_REPAIRS` at the finite affine localized
scope only.

The reviewer found no mathematical hole in the repaired fibre theorem.  The
remaining minor debts are preserved rather than silently erased:

1. cite computed `eq8` (the associate `-Q8`) when naming the loaded singular
   ideal;
2. the stratum runner alone does not gate `dim=-1,size=1`; the frozen replay
   does;
3. some negative-control/replay-v1 and factor-runner custody files are not
   first-class rows in the V2 manifest;
4. the retained statement that replay-v1 failed because `rg` was unavailable
   is unsupported and must not be consumed;
5. the factor generator copies the independently checked mod-7 octic rather
   than deriving it inside that same process.

These are custody/process hardenings, not an expansion or contraction of the
localized affine theorem.  The source-horizontal boundary gate remains the
next mathematical dependency.
