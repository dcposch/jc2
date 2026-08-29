# Preregistration: K00 V27 R3 exact `B+I2(A)` recursion

Date: 2026-08-27

Lifecycle before launch: **FROZEN DESIGN / UNRUN / SPECULATIVE ROLLBACK TAG
ON UNREVIEWED BASE4 R1 AND BASE3 R2 / NOT EVIDENCE**.

Planned result paths, which must not exist before launch:

```text
cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/aws_r6a_r3_exact_base2/output/RESULT.json
cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/RESULT_V27_BASE2_R3_EXACT_PREPASS.md
```

## Purpose and dependency discipline

Frozen producer endpoints R1 and R2 report, without independent review,

```text
B+I5(A)+I4(A)+I3(A) = B+I5(A),
dim R/(B+I5(A)) = 3.
```

R3 may use those claims only for provisional scheduling.  Its runner must
independently reconstruct `A`, `B`, `I5(A)`, `I4(A)`, and `I3(A)` and freshly
rederive both containments and dimensions before testing

```text
J1base = B+I5(A)+I4(A)+I3(A)+I2(A),
```

equivalently `B+I2(A)` by determinantal containment.  It then asks whether
the provisional rank-`<=2` base scheme has a rank-`<=1` closed subscheme and
whether `I2(A)` is already redundant.

## Mandatory origin correction

The separately frozen exact origin replay checked all seven generators of
`B`, all 90 stored nonzero generators of `I5(A)`, and all 49 entries of `A`:
they vanish at `d0_1=...=d5_1=0`.  R3 must independently repeat this check
for `B`, `A`, and all stored `I2(A)` generators.

Therefore `J1base` is known proper before launch.  A unit result is not a
rank-purity pass; it contradicts the mandatory origin control and is an
engine/source/replay failure.  Mere existence of a rational point is also
not a useful target, because the homogeneous affine origin is already one.
A useful point target must instead be nonzero/projective, source-open, or
compatible with the full prior ideal `P6`.  R3 decides none of those.

## Frozen census validators

Retain every literal row/column label.  The compiler comparison census and
the required fresh Singular stored-nonzero census are:

| ideal | literal labels | zero determinants | stored nonzero | unique nonzero |
|---|---:|---:|---:|---:|
| `I6(A)` | 49 | 49 | 0 | 0 |
| `I5(A)` | 441 | 351 | 90 | 54 |
| `I4(A)` | 1,225 | 631 | 594 | 491 |
| `I3(A)` | 1,225 | 412 | 813 | 725 |
| `I2(A)` | 441 | 90 | 351 | 326 |

Any mismatch is a dependency/source/engine failure, not a mathematical
endpoint.  No deduplicated ideal or sampled pencil substitutes for the full
stored generator lists.

## Exact replay, mutations, and stop rules

1. Refuse non-EC2 Linux, malformed/unregistered lanes, writable source trees,
   missing bytes, or any source/archive/manifest mismatch.
2. Freshly prove `J4=B+I5(A)` proper of dimension three; reduce every stored
   `I4(A)` generator to zero; rebuild `J3`; reduce every stored `I3(A)`
   generator to zero; and require the resulting `J2` proper of dimension
   three.  A failed inherited control stops R3 with no verdict.
3. Recheck the origin entrywise for `A`, `B`, and `I2(A)`.  Add `1` to one
   `B` and one `I2(A)` generator and require both origin mutations to fail.
4. Reduce all 351 stored nonzero `I2(A)` generators against a fresh basis of
   `J2`, record the exact number outside, and compute `J1base` by exact
   `slimgb`.  Require it proper with dimension in `[0,3]`; a unit is a hard
   contradiction, not a pass.
5. Serialize `Graw,T` from `liftstd(J1base,T)`.  In a second Singular process,
   verify entrywise `matrix(J1base)T=matrix(Graw)`, recompute `std(Graw)`, and
   reduce every generator of `B`, `I5(A)`, `I4(A)`, `I3(A)`, and `I2(A)` to
   zero.  Recheck properness and dimension from that basis.
6. Delete the first nonzero stored `I2(A)` slot; delete and add the selected
   nonzero transform coefficient; adjoin `1`; preserve `(d0_1)` as a known
   proper control; and require every mutation to trigger its registered
   behavior.
7. Stop after the frozen R3 endpoint.  Do not schedule `I1(A)`, saturation,
   projectivization, or a source-open/full-`P6` point search without a new
   preregistration and explicit coordinator authorization.
8. A wall/memory cap, nonzero swap, Singular warning/diagnostic/stderr,
   missing telemetry, empty required artifact, or replay/hash mismatch is
   `RESOURCE_CAP_NO_VERDICT` or dependency/engine failure, never evidence.

## Outcomes

The only mathematical pass is

```text
PASS_V27_R3_EXACT_RANK_LE1_SURVIVES_PRODUCER_UNREVIEWED_ROLLBACK_R1_R2
```

It records properness, dimension, and the exact `I2OUTSIDE` count.  If that
count is zero, it additionally gives the producer-unreviewed equality
`B+I2(A)=B+I5(A)`.  If it is positive, it proves only strict
scheme-theoretic enlargement of the ideal; without radical/saturation work it
does not by itself establish a nonempty exact-rank-two geometric stratum.

## AWS envelope

On authorization only, use freshly audited idle AWS r6a, one process/core at
nice level 5, outer wall cap 21,600 seconds, per-Singular cap 21,000 seconds,
virtual-memory cap 402,653,184 KiB, and required zero swap.  Do not touch
Box02 R2/R5 or any unrelated lane.

## Firewall

R3 is an intrinsic six-variable affine rank-filtration computation.  It
asserts no nonzero/projective point, source-open point, full-`P6` point,
grade-seven compatibility, rank-five chart, later-grade or nilpotent lift,
jet, arc, source reachability, closure incidence, counterexample, or JC2
result.  It consumes no sampled-pencil claim.
