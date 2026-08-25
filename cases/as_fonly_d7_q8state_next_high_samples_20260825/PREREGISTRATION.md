# Low-weight Q8-state / Q9-locus next-high classifier

Run two independent deterministic families below the reviewed Q9-to-Q8
Kuranishi presentation:

1. at the canonical `t=e17` Q9 point, take zero and both scalar multiples
   of all 19 basis directions in the Q8 solution kernel (39 states);
2. on the exact 13-dimensional Q9 Kuranishi zero locus, take the base point
   and both scalar multiples of all 13 free directions, choosing the
   canonical full-system Q8 section at each point (27 states).

For each state, build the exact Q7 affine system.  If compatible and its
fibre has at most `3^10` points, exhaust that fibre, compare recursive and
literal-determinant fifth-carry rows `R12..R9`, and classify the exact high
zero count and polynomial degree.  The Q6 divergence map and its degree
bound are checked source-honestly, so these high rows are independent of
the Q6 fibre.

This is sampled-canonical in the 19- and 13-dimensional predecessor axes,
but exhaustive in every reported Q7 fibre.  Do not extrapolate sample rates
to either whole predecessor fibre or to JC2.
