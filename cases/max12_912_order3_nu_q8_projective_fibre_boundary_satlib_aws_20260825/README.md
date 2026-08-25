# Independent Singular `sat` route for the Q8 projective boundary

This AWS-only implementation mirror consumes the pinned saturated-boundary
generator and replaces only its explicit Rabinowitsch elimination
`eliminate(J+(z*t-1),z)` by Singular `elim.lib`'s exact
`sat(J,ideal(t))[1]`.  It tests the same seven charts after the same global
saturation and `w=25` specialization.  Agreement is an implementation
cross-check; disagreement fails closed.

