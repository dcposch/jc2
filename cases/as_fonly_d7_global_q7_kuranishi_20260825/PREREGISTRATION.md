# Global Q7 quadratic Kuranishi design

Using the source degree bound, reconstruct the exact ten-coordinate Q7
left-cokernel map on the 32-dimensional **unreduced affine-lift** chart
consisting of 13 free Q9 Kuranishi parameters and 19 Q8 kernel parameters.

- shard 0: constant and both nonzero multiples of all 32 basis vectors;
- shards 1--31: a disjoint partition of all `binom(32,2)=496` pair sums;
- shards 32--35: 64 deterministic off-grid substitution controls.

At every point assert the complete Q9 and Q8 source equations, constant Q7
matrix, and exact left-cokernel multiplication.  Aggregate only after every
shard PASSes with empty stderr and pair coverage is exact.  Emit all nonzero
constant, linear, square, and cross coefficients and the support variables.

The control shards also report, without assuming equivalence, whether direct
coefficientwise reduction of each unreduced state happens to satisfy the
canonical source rows and what Q7 rank pair it then has.

This gate reconstructs the unreduced compatibility map; it does not by itself
prove global canonical-state equivalence or solve a large quadratic zero
locus.  Canonical carries and six predecessor Frobenius spectators remain
outside the licensed chart.
