# Preregistration

For each predecessor `sample_00.json` through `sample_63.json` from the frozen
canonical Q8-to-Q7 fibre sampler:

1. require the predecessor's exact Q9 rows to vanish, Q8 rank pair to be
   `(13,13)`, and solved Q7 compatibility locus to contain the zero
   Q8-fibre coordinate; retain the displayed (generally nonzero) Q8
   particular vector exactly;
2. reconstruct the source polynomials at that exact canonical predecessor;
3. solve the 19-row Q7 system, recording rank, augmented rank, particular
   solution, and kernel dimension;
4. when the Q7 kernel dimension is at most ten, exhaust all its F3-points;
5. compare recursive divided carries with direct division of the literal
   integer Jacobian at degrees 12, 11, 10, and 9 for every point;
6. record the number of points at which all four high rows vanish, plus the
   ordered residual-stream and quadratic-coefficient hashes.

Any source hash mismatch, predecessor mismatch, nonexact division, recursive
versus direct mismatch, missing output, nonempty stderr, or aggregation
inconsistency fails closed.

Interpretation is fixed in advance:

- a positive high-row zero count is an explicit compatible survivor at this
  next gate;
- a zero count kills only the chosen Q8 zero section over that sampled Q9
  predecessor;
- even 64 zero counts do not kill the 17 other Q8 fibre directions, the full
  Q9 chart, fixed-cap lifting, or JC2.
