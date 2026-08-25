# Preregistration — exact subsignature refinement

Input: a completed V3 census with exactly `3^13` fixed 128-byte records.

Each record is parsed as four SHA-256 digests:

```text
full zero-section signature | exact carry | Q8 RREF | Q7 RREF
```

The refinement computes global counts, first state indices, status incidence,
and class-size histograms for the three proper subsignatures.  It must recover
the full-signature counts from `classes.tsv` exactly and preserve the ordered
record-stream hash.

It also records, for every 27-point full-signature class, the raw-coordinate
value masks.  The proposed compression is that every class is label-homogeneous
and is exactly one three-coordinate cube; the varying coordinate names are
reported rather than assumed.

It also tests, without assuming, the source-suggested zero-section criterion
`q7_compatible <=> t6=t8=0` in the fixed base-three coordinate order.  Every
mismatch is counted and its first state index retained.

The independent source cross-tab must reconstruct every fixed record from the
pinned integer source, including both RREF particulars and exact carry hashes.
It reports the actual `(s15,t6,s17,t8)` table, searches all nonempty zero-subset
criteria, and pins state 729 as a canonical-zero-section negative control.

This is deterministic metadata compression.  Equality of a subsignature is
not full-19D transition equivalence and is not a fibre/lift theorem.
