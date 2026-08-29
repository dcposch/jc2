# K00 V27 BASE3 R2 exact rank recursion

Date: 2026-08-27

Lifecycle: **PRODUCER-CHECKED / INTERNAL-UNREVIEWED / SPECULATIVE /
ROLLBACK-TAGGED ON BASE4 R1 / NOT PROMOTED**.

This is the second exact producer execution in the V27 rank recursion.  It
was scheduled from the unreviewed BASE4 R1 endpoint, but the executed algebra
independently reconstructs and rechecks that endpoint before testing the new
ideal.  It is not campaign evidence until a different model performs hostile
replay and review.  No canonical ledger is edited by this report.

## Exact producer result

Work in

```text
R = Q[d0_1,d1_1,d2_1,d3_1,d4_1,d5_1]
```

with the byte-frozen V26 `7 x 7` matrix `A` and

```text
B = (G2_row1,G2_row2,G2_row3,G2_row4,G2_row5,G2_row7,F10).
```

Set

```text
J4base = B + I5(A)
J3base = B + I5(A) + I4(A)
J2base = B + I5(A) + I4(A) + I3(A).
```

The producer replay returns

```text
J4base and J3base are freshly rechecked proper of dimension 3
I4(A) is contained in J4base
J2base is proper
dim(R/J2base) = 3
I3(A) is contained in J3base
J2base = J3base = J4base.
```

The new equality is stronger than mere rank-`<=2` survival.  The run reduces
all 813 stored nonzero `3 x 3` minors to zero against a fresh standard basis
of `J3base`; the marker is `I3OUTSIDE=0`.  The reverse inclusion is by
construction.  The resulting nine-element standard basis has SHA-256
`c8aa23e4...`, byte-identical to both BASE4 R1 and the reviewed V26R1F basis
of `B+I5(A)`.

Consequently, subject to hostile review of both R1 and R2, the entire promoted
rank-`<=3` coefficient-base scheme is already rank-`<=2`
scheme-theoretically.  Its rank-exactly-three geometric difference is empty,
while the rank-`<=2` closed scheme survives with affine dimension three.
R2 therefore does **not** prove rank purity at three.  A test of `B+I2(A)`
would be the next rank-filtration question, but it must be separately
preregistered and may not consume this endpoint as reviewed evidence.

The equivalent notation `B+I3(A)` uses the elementary determinantal
containments `I5(A) subset I4(A) subset I3(A)`; the executed ideal retained
all summands literally.

## Frozen construction, replay, and censuses

The runner consumes the frozen V26 atlas without recompilation and rechecks:

| ideal | literal row/column labels | stored nonzero determinants |
|---|---:|---:|
| `I6(A)` | 49 | 0 |
| `I5(A)` | 441 | 90 |
| `I4(A)` | 1,225 | 594 |
| `I3(A)` | 1,225 | 813 |

`MINOR_SOURCE_LABELS_RANK3_TO_6.json` retains every row/column subset at all
four ranks.  Before deciding R2, the run freshly proves `J4base` proper of
dimension three, reduces every stored `I4(A)` entry to zero, and proves the
rebuilt `J3base` proper of dimension three.  R1 bytes serve as custody and
scheduling controls only.

The R2 preflight markers are

```text
K00_V27_R2_PREFLIGHT=PROPER
K00_V27_R2_DIM=3
K00_V27_R2_NGEN=354
K00_V27_R2_I3PICK=1
K00_V27_R2_I3OUTSIDE=0
```

The tracked producer serializes a nine-generator `Graw` and a `354 x 9`
transform `T`.  A fresh Singular process verifies entrywise

```text
matrix(J2base)*T = matrix(Graw),
```

recomputes `G=std(Graw)`, and reduces every generator of `B` plus all stored
nonzero entries of `I5(A)`, `I4(A)`, and `I3(A)` to zero.  It rederives
`NF_G(1)=1` and `dim(R/G)=3` only from the replayed basis.  Dropping the first
nonzero `I3(A)` slot changes that literal slot; deleting or adding the selected
nonzero transform coefficient breaks the exact identity; adjoining `1`
forces the unit ideal; and `(d0_1)` remains a proper control.  Singular stderr
and outer streams are empty.

## AWS execution and caps

The immutable R2 source ran on idle AWS r6a
(`ip-172-30-0-34`, `r6i.16xlarge`) under the registered lane

```text
max12_812_order2_u2_62_k00_v27_r2_base3_20260827T184800Z_r6a
```

with one process/core at nice level 5, a 21,600-second outer cap, a
21,000-second per-Singular cap, and a 402,653,184-KiB virtual-memory cap.  It
used Singular 4.3.2, finished with engine rc 0 in 3.62 seconds, reached maximum
RSS 509,168 KiB, and used zero swap.  Live preflight and postflight snapshots
show no competing exact-algebra process.  Box02's protected R2/R5 processes
were not touched, and the independent LF40 lane selected another r6 host.

## Custody

- R2 source-freeze manifest:
  `f5659ad2a8d8e992125e764160ad0722057f5279b6a7d8b813ca44faa6d44a21`
- immutable R2 source archive:
  `1a002197297e8e5ea2d28ed0990cc956be834fbdb916de78259b37df4cfd0988`
- producer endpoint `RESULT.json`:
  `d9d9d9dba1b06f1cb9773066924268a5162774779de9f86339d2c3306fbffdb3`
- AWS relative-path evidence manifest:
  `75ff30e00b95c4901103f38bce9668eb22f9ced9fc831692d44ceff7486f6b9e`
- portable harvest manifest `HARVEST_REPLAY_BASE3_R2.sha256`:
  `96b6f5f555a8d68e4f7be6be8f7bfc343175d2fabed24d2d6619415784ea4285`
- standard basis:
  `c8aa23e46f909e70c2c8d302ca67a415496df9a969f99817d2ef593f60f614c0`
- tracked transform:
  `b86238ea55b89dc2ca47d7753ae3de5fd490fc63cec2b8fbc93a2e28fc33eb23`
- literal minor-label set:
  `02bea82cbdd96a946c894a83cc86b77c613727c933312d110372e34e7892516f`

The source manifest replays 46 frozen entries, including every harvested R1
endpoint byte.  The portable R2 manifest replays all 26 harvested objects:
the 25 AWS-manifested files plus the AWS evidence manifest itself.

## Review target

A hostile reviewer should independently:

1. rehash the source, endpoint, AWS evidence, and portable manifests;
2. reconstruct `A`, `B`, and every rank-3/4/5/6 minor from the frozen atlas;
3. verify the literal/nonzero censuses and row/column label completeness;
4. independently rederive the R1 equality `J3base=J4base` rather than trusting
   the dependency prose or endpoint;
5. reduce every `I3(A)` generator to zero modulo a fresh basis of `J3base`, or
   verify an independent exact coefficient matrix for the containment;
6. verify `matrix(J2base)T=matrix(Graw)`, independently recompute a standard
   basis, and rederive properness and dimension;
7. replay the deletion, transform, forced-unit, known-proper, full-literal,
   source, cap, and swap controls; and
8. reject every stronger reading listed below.

## Firewall

No rational point is exhibited.  This result does not decide whether rank is
exactly two, one, or zero anywhere, the full prior ideal `P6`, grade-seven
compatibility, any rank-five chart, nilpotent or later-grade lifting, a finite
jet, a formal or convergent arc, source reachability, closure incidence, a
counterexample, or JC2.  It does not consume any sampled pencil claim.  Until
independent review, the equalities and rank-filtration consequence above
remain producer-unreviewed, speculative, and rollback-tagged on BASE4 R1.
