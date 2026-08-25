# Candidate-H exact F127 point count

This AWS-only case enumerates all `127^2` affine pairs `(w,v)`, evaluates the
pinned candidate `H(w,v)` and both partial derivatives, and records all smooth
and singular rational affine points.  If the smooth count exceeds `128`, then,
conditional on the separately proved geometric integrality of `H`, its smooth
projective normalization cannot have genus zero: a genus-zero curve over
`F_127` with a rational point is `P1` and has exactly `128` rational points,
while distinct smooth affine points inject into the normalization.

The count by itself proves no source-component membership, specialization,
trajectory exclusion, maximum-twelve theorem, or JC2 conclusion.
