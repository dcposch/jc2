# Preregistration — canonical Q9 signature census

Date: 2026-08-25  
Status: source frozen before any census output is consumed.

## Question

Across the exact `3^13 = 1,594,323` canonical Q9 survivor chart below the
corrected F-only D7 source, how many distinct **zero-section presentation
signatures** occur when the signature includes:

1. exact integer source/carry rows at Q9, at the canonical Q8 affine
   particular, and at the canonical Q7 affine particular;
2. the complete Q8 and Q7 affine matrices/RHSs;
3. deterministic RREF work matrices, pivots, affine particulars, and kernel
   bases; and
4. direct substitution in the original reconstructed integer source rows at
   every consumed state?

The ordered state range is the base-three order on the 13 free Q9 coordinates
`free_q9 = (0,...,18) \ {10,11,12,13,15,17}`, with `t17=1` and the other five
forced coordinates zero.

## Frozen outcomes

- `PASS`: every one of the `3^13` states directly satisfies Q9, its canonical
  Q8 particular satisfies all 22 rows, its canonical Q7 particular satisfies
  all 19 rows, all exact divisions occur before reduction, all deterministic
  shard ranges are disjoint/exhaustive, and the aggregate fixed-record stream
  and class table verify.
- `SOURCE_FAIL`: any direct source substitution or exact division fails.
- `RANK_ESCAPE`: any Q8 or Q7 rank/dimension differs from the frozen expected
  `(13,13,19)` or `(9,9,9)` presentation.
- `DEPLOYMENT_FAIL`: missing source, range overlap/gap, malformed record, or
  nonzero launcher/shard/aggregate exit.

## Interpretation firewall

Equality of the frozen signature is an exact equality of the displayed
zero-section integer-carry/source/RREF presentation.  It is **not yet** a
theorem that the whole 19-dimensional Q8 fibres have identical transition
circuits.  One representative full-fibre experiment per signature is licensed
only as the next discriminator.  Fibre equivalence requires a separate
source-derived carry-translation/sufficiency proof or exhaustive equality.
Zero-section death never implies fibre death.

