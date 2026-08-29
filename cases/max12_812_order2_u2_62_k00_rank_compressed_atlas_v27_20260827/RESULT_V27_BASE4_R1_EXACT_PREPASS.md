# K00 V27 BASE4 R1 exact rank-purity prepass

Date: 2026-08-27

Lifecycle: **PRODUCER-CHECKED / INTERNAL-UNREVIEWED / SPECULATIVE / NOT
PROMOTED**.

This is the first exact producer execution of the previously unrun V27
rank-compressed atlas design.  It is not campaign evidence until a different
model performs hostile replay and review.  No canonical ledger is edited by
this report.

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
J3base = B + I5(A) + I4(A).
```

The producer replay returns

```text
J3base is proper
dim(R/J3base) = 3
I4(A) is contained in J4base
J3base = J4base
```

The last equality is stronger than mere survival.  The run freshly computes
a standard basis of `J4base`, then reduces every stored nonzero `4 x 4` minor
to zero against it.  The frozen/literal census is 1,225 row/column labels,
of which 594 determinants are nonzero and 631 are zero.  The marker is
`I4OUTSIDE=0`.  Since the reverse inclusion `J4base subset J3base` is by
construction, the ideals are equal.  The tracked nine-element standard basis
of `J3base` is also byte-identical to the reviewed V26R1F standard basis of
`J4base` (SHA-256 `c8aa23e4...`).

Consequently, subject to hostile review, the entire promoted rank-`<=4`
coefficient-base scheme is already rank-`<=3` scheme-theoretically.  Its
rank-exactly-four geometric difference is empty, while the rank-`<=3` closed
scheme survives with affine dimension three.  BASE4 therefore does **not**
prove rank purity at four; V27 must recurse to `B+I3(A)` before any exact-rank
claim.

The equivalent notation `B+I4(A)` uses the elementary determinantal
containment `I5(A) subset I4(A)`; the executed ideal retained both summands
literally.

## Frozen construction and censuses

The runner consumes the frozen V26 atlas without recompilation and rechecks:

| ideal | literal row/column labels | stored nonzero determinants |
|---|---:|---:|
| `I6(A)` | 49 | 0 |
| `I5(A)` | 441 | 90 |
| `I4(A)` | 1,225 | 594 |

`MINOR_SOURCE_LABELS.json` retains every row/column subset at ranks 4, 5,
and 6.  The fresh V26 control rederives that `J4base` is proper of dimension
three before deciding the V27 target.  No compacted generator set substitutes
for the full ideal: in the second process, all generators of `B`, all 90
stored nonzero `I5(A)` entries, and all 594 stored nonzero `I4(A)` entries
reduce to zero against a freshly recomputed standard basis.

The preflight markers are

```text
K00_V27_BASE4_PREFLIGHT=PROPER
K00_V27_BASE4_DIM=3
K00_V27_BASE4_NGEN=74
K00_V27_BASE4_I4PICK=1
K00_V27_BASE4_I4OUTSIDE=0
```

The tracked producer serializes a nine-generator `Graw` and a `74 x 9`
transform `T`.  Fresh replay verifies entrywise

```text
matrix(J3base)*T = matrix(Graw),
```

then recomputes `G=std(Graw)`, checks the full literal reverse inclusion, and
derives `NF_G(1)=1` and `dim(R/G)=3` only from that fresh basis.  Both the
tracked-transform and forced-unit controls fire as registered.  Deleting the
first nonzero literal `I4(A)` slot changes that slot; deleting or adding the
selected nonzero transform coefficient breaks the exact identity.

## AWS execution and caps

The immutable R1 source ran on idle AWS r6a
(`ip-172-30-0-34`, `r6i.16xlarge`) under the registered lane

```text
max12_812_order2_u2_62_k00_v27_base4_r1_20260827T183300Z_r6a
```

with one process/core at nice level 5, a 21,600-second outer cap, a
21,000-second inner cap, and a 402,653,184-KiB virtual-memory cap.  It used
Singular 4.3.2, finished with engine rc 0 in 3.28 seconds, reached maximum RSS
509,120 KiB, and used zero swap.  Box02's protected R2/R5 processes were not
touched; the fleet coordinator placed this job on the idle r6a host instead.

## R0 fail-closed history

The first immutable source froze an incorrect validator assumption that
`size(minor(A,r))` retained zero polynomial slots.  Singular stores only the
nonzero occurrences here, so R0 stopped at `I6_LITERAL_CENSUS` before the
target standard basis.  R0 took 1.87 seconds, 509,120 KiB RSS, and zero swap.
It is preserved in `aws_r6a_r0_failed/` with a replayable relative evidence
manifest and supplies no mathematical verdict.

`DESIGN_ERRATUM_BASE4_R0_MINOR_STORAGE.md` freezes the only repair: the typed
stored-entry guards changed from the combinatorial totals to `0`, `90`, and
`594`.  No matrix, polynomial, target ideal, term order, algorithm, cap,
mutation, replay rule, or firewall changed.

## Custody

- R1 source-freeze manifest:
  `7ffc61ba3aa1286205f3fc6e9f8b77792e3eff6f6790d91b737beb8d0f18d060`
- immutable R1 source archive:
  `ec7763abf137a6e88032bca348c6802420b985c59d468f96fff31784c3f20597`
- producer endpoint `RESULT.json`:
  `f886f17ca2c626ec476e695418002185d2223d556721759900f6cdbe89635073`
- AWS relative-path evidence manifest:
  `3e7fac6cd993c8afa581fa037d6f69df757a6a8db08ccdeda6c5770d1d7e8d9c`
- portable harvest manifest `HARVEST_REPLAY_BASE4_R1.sha256`:
  `279bdc80febfe7a309bcd279f30caeb25d58e74476aa7bcf62dd13557bbbe2f4`
- standard basis:
  `c8aa23e46f909e70c2c8d302ca67a415496df9a969f99817d2ef593f60f614c0`
- tracked transform:
  `88e306e97062271d2cf4b3351c7d1fbe27a0ac1ec16056b63719f76fe0e611b6`
- literal minor-label set:
  `69d274d5783e915b98b06012064440f23a8102319c0d34572be851baf14da697`

The portable manifest replays all 24 harvested R1 files, including the AWS
evidence manifest, launch/freeze/telemetry records, scripts, serialized basis
and transform, result, source labels, and empty stderr/outer streams.

## Review target

A hostile reviewer should independently:

1. rehash the R1 source, endpoint, evidence, and portable manifests;
2. reconstruct `A`, `B`, and all rank-4/5/6 minors from the frozen atlas;
3. verify the 1,225/594, 441/90, and 49/0 censuses with row/column labels;
4. prove `J4base` equals the frozen V26R1F ideal and independently verify its
   standard basis;
5. reduce every `I4(A)` generator to zero modulo `J4base`, or verify an exact
   coefficient matrix giving `I4(A) subset J4base`;
6. verify `matrix(J3base)T=matrix(Graw)`, recompute a standard basis, check
   every Buchberger pair or use an independent exact engine, and rederive
   properness and dimension;
7. replay the transform deletion/addition, forced-unit, and full-literal
   reverse-inclusion controls; and
8. reject every stronger reading listed below.

## Firewall

No rational point is exhibited.  This result does not decide whether rank is
exactly three or lower anywhere, the full prior ideal `P6`, grade-seven
compatibility, any rank-five chart, nilpotent or later-grade lifting, a finite
jet, a formal or convergent arc, source reachability, closure incidence, a
counterexample, or JC2.  Until independent review, even the ideal equality
and rank-filtration consequence above remain producer-unreviewed speculative
claims.
