# Preregistration: K00 V27 R4 selected exact-rank-two chart

Date: 2026-08-27

Lifecycle after hostile review and storage erratum:
**SINGULAR-STORAGE-REPAIRED DESIGN / UNRUN / NOT LAUNCHED / CURRENTLY HELD
AS REDUNDANT EXCEPT FOR AN EXPLICIT POINT / NOT EVIDENCE**.

Planned result paths, which must not exist before an authorized launch:

```text
cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/aws_r6a_r4_rank2_chart_r5r7_c6c7/output/RESULT.json
cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/RESULT_V27_RANK2_CHART_R4.md
```

## Purpose and dependency firewall

The frozen R3 producer reports that `B+I2(A)` is a strict scheme-theoretic
cut of `J2base=B+I3(A)`.  The hostile Fable 5 review independently confirms
dimensions three and two, so the radicals are distinct and an exact-rank-two
geometric stratum over an algebraic closure already follows
nonconstructively.  R4 is therefore held: its remaining value would be to
put one explicit principal-open chart behind that existence statement.  The
runner must still reconstruct the raw frozen objects and freshly replay every
consumed containment and corrected census if a later authorization revives
it.

Work in

```text
Rz = Q[d0_1,d1_1,d2_1,d3_1,d4_1,d5_1,z]
J2 = B+I5(A)+I4(A)+I3(A).
```

The independently frozen selection is

```text
m = A[5,6]*A[7,7] - A[5,7]*A[7,6]
  = -I2A[37] in literal minor-object column 37,
SHA256(m) = 51007fc35085e65bd7b19936b492949c9edcd04f4f34716c1ff6fc9e8f6d5616,
SHA256(NF_J2(m)) = 8748e6f901332974919b80383deb9a3cca37f84f46da5252e34885485380157c.
```

The sole target is

```text
K = J2 + (z*m-1).
```

No alternate minor may be tried in this run.  This Rabinowitsch chart is
equivalent to testing whether `D(m)` meets `V(J2)`; an exact saturation could
replace it only under a separately frozen byte-identical design.

## Frozen source and census replay

The runner must pin the V26 atlas, compiler endpoint and manifest, the frozen
R1-R3 endpoints/reports, the origin replay, the clean chart-selection
evidence, and both serialized selected polynomials.  It must then rebuild
`A` and `B` from the atlas and require these complete label/storage counts:

| ideal | combinatorial labels | Singular `ncols` | stored nonzero | unique nonzero |
|---|---:|---:|---:|---:|
| `I6(A)` | 49 | 1 | 0 | 0 |
| `I5(A)` | 441 | 90 | 90 | 54 |
| `I4(A)` | 1,225 | 594 | 594 | 491 |
| `I3(A)` | 1,225 | 813 | 813 | 725 |
| `I2(A)` | 441 | 441 | 351 | 326 |

The full stored 441-column `I2(A)` normal-form pass must visit every slot,
including 90 zeros, using `ncols()`.  It must return 291 nonzero
normal forms and 60 zero normal forms among the 351 nonzero determinants,
with first outside literal column 37.  The labelled determinant must equal
`-I2A[37]`, and its freshly computed normal form must match the frozen bytes.
An exact AWS Singular 4.3.2 tool-semantics preflight, frozen in
`RESULT_V27_RAW_COLUMN_SEMANTICS_PROBE.md`, independently confirms that the
empty-ideal assignment and comma-concatenation forms below preserve repeated
columns.
The actual storage census and its failed-closed discovery are frozen in
`DESIGN_ERRATUM_SUCCESSOR_MINOR_STORAGE_NCOLS.md` and the full-`P6` R0
no-verdict report.
The runner must freshly rederive, in the seven-variable extension, the base
dimensions `dim(J4)=dim(J3)=dim(J2)=4` and `dim(J1)=3`, corresponding to
affine dimensions three and two before adjoining the free `z` variable.

## Origin-negative control

Every entry of `A`, every raw generator of `B`, every stored `I3(A)`
generator, and `m` must vanish at
`d0_1=...=d5_1=0`.  At that origin cylinder,

```text
z*m-1 = -1,
(d0_1,...,d5_1,z*m-1) = (1).
```

Thus the trivial homogeneous rational origin is excluded.  The mutation
that deletes the constant term, replacing the chart equation by `z*m`, must
make the origin ideal proper.  Add-one mutations in a raw `B` generator and
the selected stored minor must also break origin vanishing.  Failure of any
origin control is a source/engine failure, not a geometric endpoint.

## Exact producer replay and mutations

1. Refuse non-EC2 Linux, an unregistered or malformed lane, a writable
   source tree, nonzero swap, an existing output directory, or any
   archive/freeze/hash mismatch.
2. Validate the actual stored `ncols`/`size` tuple above and traverse every
   stored position with `ncols()`.  Consume the already-nonzero 90 `I5(A)`,
   594 `I4(A)`, and 813 `I3(A)` columns directly; scan all 441 stored `I2(A)`
   positions only where its 351 nonzero entries must be filtered.  Construct
   `K` with comma concatenation from the seven raw `B` generators, the three
   direct minor objects, and the single chart equation.  Require exactly
   1,505 target columns.  Singular `+` compaction, a deduplicated list, or a
   sampled pencil does not substitute for this raw list.
3. Decide `K` exactly by `slimgb`, then use `liftstd` only to propose a
   certificate.  A fresh Singular process must rebuild every raw generator.
4. On a proper branch, serialize `Graw,T`, verify entrywise
   `matrix(K)T=matrix(Graw)`, recompute `std(Graw)`, reduce every raw
   `B/I5/I4/I3` generator and `z*m-1` to zero, rederive properness and exact
   nonnegative dimension, and fire transform drop/add plus forced-unit
   mutations.  Deleting the raw generator selected by a nonzero tracked
   coefficient must also destroy the tracked identity.
5. On a unit branch, serialize a rational coefficient column `C` satisfying
   `matrix(K)C=1`.  A fresh process must verify that identity entrywise from
   the raw generator list and require coefficient drop/add mutations to
   destroy it.  Deleting the raw generator selected by a nonzero Bezout
   coefficient must destroy the unit identity.  Removing the chart equation
   must recover the freshly checked proper `J2` control.
6. Singular warnings/diagnostics or stderr, missing or empty required bytes,
   failed mutation, nonzero swap, wall/RSS cap, or evidence replay mismatch
   is fail-closed `RESOURCE_CAP_NO_VERDICT` or dependency/source/replay
   failure.  It is never mathematical evidence.

## Allowed mathematical endpoints

If `K` is proper, the only pass is

```text
PASS_V27_R4_SELECTED_I2_CHART_PROPER_ALGEBRAIC_RANK2_POINT_PRODUCER_UNREVIEWED_ROLLBACK_R1_R2_R3
```

Over an algebraic closure, `I3(A)=0` gives rank at most two and `m!=0`
gives rank at least two, so this endpoint exhibits a nonempty exact-rank-two
geometric locus on this selected chart.

If `K=(1)`, the only pass is

```text
PASS_V27_R4_SELECTED_I2_CHART_UNIT_ONLY_THIS_CHART_EMPTY_PRODUCER_UNREVIEWED_ROLLBACK_R1_R2_R3
```

The replayed unit certificate kills only `D(m)` inside `V(J2)`.  It does not
kill any other `2 x 2` minor chart, and the run stops without selecting one.

## Exact-Q certificate rule

Properness over `Q` is not a rational-point certificate.  No status or
report may claim a `Q`-point unless it additionally serializes all six
rational coordinates and `z`, checks `m!=0`, and in two independent exact
processes evaluates every raw `B/I5/I4/I3` generator and `z*m-1` to zero.
Without those bytes the payload must explicitly say
`rational_point_claim=false`.

## AWS envelope and one-minor stop

This six-variable alternative is not currently authorized.  On a later new
authorization only, use a freshly audited idle r6a lane, one process
and one core at nice level 5, outer wall cap 21,600 seconds, per-Singular cap
21,000 seconds, virtual-memory cap 402,653,184 KiB, and required zero swap.
Do not touch Box02 R2/R5 or stack on unrelated work.

After either exact endpoint, freeze and harvest it and stop.  Do not run a
second minor, `I1(A)`, saturation/projectivization, source-open search,
full-`P6` alternative, grade-seven compatibility, later grade, lift, jet,
arc, closure, counterexample, or JC2 step without new authorization.  No
sampled-pencil claim is consumed.
