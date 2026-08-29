# K00 V27 alternate full-P6 rank-two chart: failed-closed R0

Date: 2026-08-27

Lifecycle: **DEPENDENCY/SOURCE-REPLAY FAILURE / EXACT NO-VERDICT / OLD
SOURCE FREEZE IMMUTABLE / NO RELAUNCH**.

## Endpoint

The authorized one-minor full-`P6` launch

```text
max12_812_order2_u2_62_k00_v27_alt_full_p6_rank2_20260827T201000Z_r6a
```

started on AWS r6a (`ip-172-30-0-34`) at `2026-08-27T20:08:59Z` and
ended at `2026-08-27T20:09:01Z` with engine return code 1 and validator

```text
DEPENDENCY_SOURCE_REPLAY_OR_ENGINE_FAILURE.
```

This is an exact **no-verdict** endpoint.  The branch stopped at
`K00_V27_P6R4_FAIL=STORED_MINOR_CENSUS`, before constructing the raw target
ideal and before `slimgb`, `liftstd`, or either certificate branch.  It says
nothing about properness or emptiness of the selected full-`P6` chart.

## Exact failure mechanism

The frozen source incorrectly equated each Singular minor object's number of
stored columns with its full combinatorial label count.  A separate tiny
read-only diagnostic on the same AWS host and frozen generated matrix returned

```text
I6_NCOLS=1   I6_SIZE=0
I5_NCOLS=90  I5_SIZE=90
I4_NCOLS=594 I4_SIZE=594
I3_NCOLS=813 I3_SIZE=813
I2_NCOLS=441 I2_SIZE=351
```

Thus the runner's demanded `ncols` tuple
`(49,441,1225,1225,441)` was false.  Singular stores the zero `I6` ideal as
one zero column, compacts the nonzero `I5`, `I4`, and `I3` generators, and
retains interior zero slots in `I2` through its last stored column.  The
earlier `size()`-loop repair remains necessary: positional iteration must
still use `ncols()` of the actual object.  The error was a guard expectation,
not a mathematical result.

## Custody and resource envelope

- Old source freeze SHA-256:
  `ffd2e4da109e2701499152eb5561f97005b06f536077abc6fd7242b87fc9f7f7`.
- Immutable source archive SHA-256:
  `d7d21850913496da618cf8b15ad09b7d225a3de6f002fd73edaba081746a8ee9`.
- Remote/local evidence manifest SHA-256:
  `ff7ff169ee327df91b76249f88cb9b2b31ca6df76bd8eed517c0f61868082df1`.
- Portable harvest manifest SHA-256:
  `ce2a00d59d1b8165a5400606178e815b27f791af2365937df104792867551e7f`.
- Outer/inner wall caps were 21,600/21,000 seconds and the virtual-memory
  cap was 402,653,184 KiB.  Actual wall time was 2.38 seconds, maximum RSS
  509,364 KiB, and swaps were zero.  Preflight and postflight recorded zero
  swap; r6a remained otherwise idle.
- Both the on-node evidence manifest and the portable harvest manifest replay
  with zero mismatches.  Source/archive/freeze checks passed before execution.

## Firewall

No `RESULT.json`, standard basis, tracked transform, Bezout certificate,
algebraic point, rational point, rank-two compatibility verdict, grade-seven
claim, or later successor was produced.  The six-variable R4 was not launched.
This R0 source and endpoint remain immutable historical evidence of a
fail-closed guard.  Any corrected successor requires a fresh freeze, fresh
hostile static review, and new launch authorization.
