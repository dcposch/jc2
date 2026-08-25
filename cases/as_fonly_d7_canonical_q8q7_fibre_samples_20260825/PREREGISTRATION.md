# Canonical Q8-to-Q7 fibre discriminator

The exact global Q7 map is currently proved only on an unreduced affine-lift
chart.  Sample 64 canonical Q9 states inside its 11-dimensional Q7-compatible
`t` locus (`t6=t8=0`): zero, both nonzero multiples of every basis direction,
and 41 deterministic off-axis points.

For each state:

1. substitute all canonical Q9 source rows;
2. solve the full canonical 22-row Q8 system;
3. if compatible with a 19-dimensional fibre, reconstruct the Q7 left-cokernel
   function on that entire fibre from the degree-two design in its 19 RREF
   coordinates and test 64 deterministic off-grid points;
4. if the design is exact, solve a linear map exactly or exhaust only a
   quadratic support of size at most 12; otherwise stop at the explicit first
   degree-bound counterexample.

This is exhaustive within each reported Q8 fibre only when the polynomial
design passes and the zero-locus solver reports `solved=true`.  It is sampled,
not exhaustive, in the 11 Q9 coordinates.  Six Frobenius spectators remain
pinned.

