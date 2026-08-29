# N=6 R1 additive control preregistration

Date: 2026-08-27

This additive lane does not recompute or replace the frozen exact N=6
functional.  It discharges the repair items in the Opus5 review while
preserving the reviewed producer bytes.

The lane must:

1. run the pinned V42 replay and require its exact `Tg19_7` row-data mutation
   control;
2. load the frozen N=6 exact functional, regenerate the literal V43 rows,
   and apply that same V42 coefficient mutation to the unspecialized source
   identity before multiplying `Tg19_7` by every weight-11 monomial;
3. require all 607 original `Tg19_7` products to have functional residual
   zero and require the mutated row to be detected in exactly six products,
   with canonical residual-record SHA-256
   `a9649ec4df7dded55e30600c7eebbc06631978bb5b02c836151a1cd123521398`;
4. verify the recovered original compiler source manifest (834 entries,
   manifest SHA-256 `033213c1...`) and its frozen source snapshot;
5. explicitly record that the first compiler-harvest C++ link returned
   `rc=1` from missing Givaro/GMP libraries and that the later resume build,
   solve, and exact validator are the successful certifying chain; and
6. pin the forward census addendum in this new source freeze.

Failure, timeout, OOM, a changed source row, a zero mutation residual, or a
custody mismatch gives no R1 promotion.  This is an exact-Q AWS replay with a
64-GiB / one-hour cap and no mathematical search.

