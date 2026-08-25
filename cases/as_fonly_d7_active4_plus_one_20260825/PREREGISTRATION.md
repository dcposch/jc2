# Active-four plus one predecessor coordinate

There are 13 free Q9 Kuranishi coordinates and 19 Q8 solution-kernel
coordinates in the current affine chart.  Remove the four directions already
proved active (`t6,t8,s15,s17`), leaving 28 coordinates.

For each remaining coordinate, exhaust the `3^5=243` cube obtained by adjoining
it to `(t6,t8,s15,s17)`.  Reconstruct Q9, solve the exact Q8 affine system,
use its canonical RREF kernel chart, assert all Q9/Q8 source rows, and test Q7
pointwise compatibility.  Report every compatible point having a nonzero
active-four projection; such a point is a mixed-cancellation witness.

The 28 shards are disjoint by the identity of the fifth coordinate, although
their `u=0` faces deliberately overlap as a common control.  This is not a
classification of combinations involving two or more of the remaining
coordinates, the six pinned Frobenius spectators, or later lifting.

