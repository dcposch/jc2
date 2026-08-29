# Preregistration: K00 V27 alternate full-P6 exact-rank-two chart

Date: 2026-08-27

Lifecycle after failed-closed R0: **SINGULAR-STORAGE-REPAIRED R1 DESIGN /
UNRUN AT THIS REVISION / READY FOR FRESH HOSTILE STATIC REVIEW / NOT
AUTHORIZED / NOT EVIDENCE**.

This is a separate choice from the six-variable R4 discriminator.  Neither
design authorizes the other, and this alternative must not launch until the
coordinator explicitly selects it after review.

The immutable R0 failure and its exact no-verdict report are preserved at
`aws_r6a_alt_full_p6_rank2_chart_r5r7_c6c7/` and
`RESULT_V27_FULL_P6_RANK2_CHART_ALTERNATIVE.md`.  Any later authorized R1
uses fresh paths, which must not exist before launch:

```text
cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/aws_r6a_alt_full_p6_rank2_chart_r5r7_c6c7_r1/output/RESULT.json
cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/RESULT_V27_FULL_P6_RANK2_CHART_ALTERNATIVE_R1.md
```

## Exact target

Work in the 34-variable ring

```text
S = Q[d0_1,...,d0_5,...,d5_1,...,d5_5,k10_0,k10_1,k10_2,z].
```

Let `P6` be the complete frozen prior ideal through Lambda grade six plus
`F10`, not the seven-generator leading ideal `B`.  Retain the same selected
labelled determinant

```text
m = A[5,6]*A[7,7] - A[5,7]*A[7,6] = -I2A[37].
```

Here 37 is the literal minor-object column, not the 37th nonzero stored
generator.  The corrected Fable 5 review (SHA-256 `738f4603...`) proves that
291 of the 351 nonzero `I2(A)` determinants lie outside `J2base` and 60 lie
inside; every positional scan uses the actual stored object extent via
`ncols()`.
An exact AWS Singular 4.3.2 tool-semantics preflight, frozen in
`RESULT_V27_RAW_COLUMN_SEMANTICS_PROBE.md`, independently confirms that the
empty-ideal assignment and comma-concatenation forms below preserve repeated
columns.

The sole target is

```text
Kfull = P6 + I3(A) + (z*m-1).
```

Because `P6` contains `B`, a proper result gives an algebraic exact-rank-two
point compatible with the complete prior prefix through grade six on this
selected chart.  This is not the grade-seven solvability ideal: it contains
neither the augmented matrix `E=[A|-b]` nor `I3(E)`, and it asserts no
grade-seven or later lift.

## Raw provenance and census

The runner must consume the byte-frozen V26 atlas without recompilation and
pin its compiler/manifest custody.  It must replay all 49 literal `(row,
Lambda-grade)` positions for rows 1 through 7 and grades 0 through 6,
including the 15 literal zeros.  The 34 nonzero literal rows, followed by
the independently frozen `F10`, must agree coefficientwise and in order with
all 35 entries of `P6_nonzero_generators_plus_F10`.  The six nonzero literal
grade-two rows `(1,2,3,4,5,7)` plus `F10` must agree with `B`.

It must serialize the independent complete combinatorial label universes of
all 1,225 `3 x 3` and 441 `2 x 2` determinants without pretending that their
list indices are Singular slots.  On Singular 4.3.2 it must require the exact
minor-object storage census from
`DESIGN_ERRATUM_SUCCESSOR_MINOR_STORAGE_NCOLS.md`:

```text
rank             6      5       4        3       2
ncols             1     90     594      813     441
size              0     90     594      813     351
```

The 813 stored `I3(A)` columns are already all nonzero and must be consumed
directly without deduplication.  The 441-column `I2(A)` object must be scanned
through `ncols()` to filter exactly 351 nonzero entries; column 37 and the
`(5,7);(6,7)` determinant must bind to both frozen selected-polynomial hashes
by exact polynomial identity.  Comma-concatenating the 35 raw `P6` entries,
813 stored `I3(A)` entries, and one chart equation must produce exactly 849
target columns.  Singular `+` compaction is forbidden.

## Origin-negative and dependency controls

At the full 33-variable affine origin, every literal `P6` row, `F10`, every
entry of `A`, every stored `I3(A)` generator, and `m` must vanish.  The
origin-plus-chart ideal must be unit because `z*m-1=-1`; deleting the
constant `-1` must make the origin control proper.  Add-one mutations in a
nonzero literal `P6` generator, `F10`, and the selected minor must break
origin vanishing.

The run must separately rebuild `B+I3(A)`, reproduce the frozen R1/R2
containments and dimension after extension by the unused prior variables and
`z`, and require `NF(m)!=0` there.  Those checks prevent a full-`P6` result
from silently changing the selected base chart.  They do not assume that the
strict R3 ideal relation yields distinct radicals.

## Exact replay, certificates, and mutations

1. Refuse non-EC2 Linux, a malformed lane, writable source, existing output,
   source/archive/freeze mismatch, nonzero swap, a generated `<=size(` loop,
   actual-storage census/provenance drift, or either R0 historical artifact
   mismatch.
2. Decide `Kfull` exactly by `slimgb`.  `liftstd` may only propose a tracked
   proper basis or unit Bezout column.
3. Proper branch: in a fresh Singular process verify
   `matrix(Kfull)T=matrix(Graw)`, recompute `std(Graw)`, reduce all 35 raw
   `P6` entries, all 813 stored `I3(A)` entries, and `z*m-1` to zero, rederive
   properness and dimension, and fire transform drop/add, raw-generator
   deletion, and forced-unit mutations.
4. Unit branch: serialize exact rational `C` with
   `matrix(Kfull)C=1`; freshly replay it from all raw generators and require
   coefficient drop/add mutations to break the identity.  This certificate
   kills only the selected chart.
5. The chart-constant deletion and origin controls must fire on both
   branches.  A warning, diagnostic, stderr, missing/empty artifact, failed
   mutation, cap, swap, or replay/hash mismatch fails closed with no verdict.

## Allowed endpoints and exact-Q rule

```text
PASS_V27_ALT_FULL_P6_SELECTED_I2_CHART_PROPER_ALGEBRAIC_RANK2_POINT_PRODUCER_UNREVIEWED_ROLLBACK_R1_R2_R3
PASS_V27_ALT_FULL_P6_SELECTED_I2_CHART_UNIT_ONLY_THIS_CHART_EMPTY_PRODUCER_UNREVIEWED_ROLLBACK_R1_R2_R3
RESOURCE_CAP_NO_VERDICT
DEPENDENCY_SOURCE_REPLAY_OR_ENGINE_FAILURE
```

A proper endpoint proves only an algebraic-closure point of the full prior
grade-through-six scheme with rank exactly two on `D(m)`.  A unit endpoint
kills only this chart.  Neither outcome describes other `I2` charts.

No rational-point claim is allowed unless all 33 prior coordinates and `z`
are explicitly serialized as rationals and two independent exact processes
evaluate every one of the 35 raw `P6` generators, all 813 stored `I3(A)`
generators, and `z*m-1` to zero with `m!=0`.  Otherwise the payload must say
`rational_point_claim=false`.

## AWS envelope and firewall

On separate explicit authorization only, use a freshly audited idle r6a
lane, one process/core at nice level 5, outer wall cap 21,600 seconds,
per-Singular cap 21,000 seconds, virtual-memory cap 402,653,184 KiB, and zero
swap.  Stop after this one selected chart and freeze its endpoint.  Do not
touch Box02 R2/R5, launch the six-variable alternative concurrently, try
another minor, or schedule projectivization, source-open search, `I1(A)`,
`I3(E)`, grade-seven/later compatibility, lift, jet, arc, closure,
counterexample, or JC2 work.  No sampled-pencil claim is consumed.
