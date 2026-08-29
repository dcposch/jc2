# Preregistration: auxiliary exact constant-kernel replay

Date: 2026-08-27

Lifecycle before launch: **FROZEN AUXILIARY DESIGN / UNRUN / SPECULATIVE /
NOT A RANK-STRATUM VERDICT**.

## Question and source discipline

A blind producer proposed the following constant vectors for the frozen V26
matrix `A`:

```text
l0 = (5/1024,0,3/128,0,1/8,0,1)
v1 = (2,0,1,0,1,0,0)^T
v2 = (0,1/16,0,1/2,0,1,0)^T.
```

This auxiliary run independently substitutes the byte-frozen exact matrix and
tests `l0*A=0`, `A*v1=0`, and `A*v2=0` over the full 33-variable rational
polynomial ring.  It also computes `l0*b`, requires it nonzero with exactly
690 exact terms, and serializes it.  The source consumes no sampled pencil,
sample point, numerical rank, or prose report from the proposing producer.

The V27 BASE4 R1 and BASE3 R2 endpoints are already frozen.  This replay may
offer structural context, but it cannot retroactively certify or explain away
their ideal containments.  In particular, the identities hold globally before
imposing `B`, whereas R1/R2 concern `I4(A),I3(A) subset B+I5(A)`.

## Exact checks and mutations

1. Verify frozen atlas/compiler hashes and matrix/vector shapes.
2. Reconstruct `A` and `b` independently in two fresh Singular processes.
3. Check all seven entries of each proposed product are identically zero.
4. Require at least one nonzero `5 x 5` minor and no stored nonzero `6 x 6`
   minor, agreeing with exact generic rank five.
5. Require `l0*b` nonzero, `size(l0*b)=690`, serialize it twice, and require
   byte identity between processes.
6. Add `1` to the first coefficient of `l0`, `v1`, and the second coefficient
   of `v2`; each mutated product must have a nonzero entry.
7. Fail closed on a source mismatch, unexpected output, Singular diagnostic,
   nonempty Singular stderr, cap, swap, mutation failure, or replay mismatch.

## AWS envelope and outcome

Use r6a only after a fresh idle/memory/swap audit.  One process/core at nice
level 5; 600-second outer and 540-second per-process caps; 8,388,608-KiB
virtual-memory cap; required zero swap.

The sole pass status is

```text
PASS_V27_AUX_CONSTANT_KERNEL_IDENTITIES_EXACT_EXPLANATORY_ONLY
```

It means only that the global constant identities and the nonzero 690-term
`l0*b` obstruction replay exactly.  It supplies no BASE4/BASE3 containment,
no rank-purity verdict, and no authority to launch R3.

