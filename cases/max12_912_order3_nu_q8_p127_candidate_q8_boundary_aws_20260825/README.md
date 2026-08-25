# Q8 candidate eliminant at the corrected-Q8 boundary

This AWS-only exact check specializes the interpolated monic degree-190
candidate `H(w,v)` at `w=0` and compares it with the corrected Q8 contact
polynomial modulo 127.

The check proves only a statement in the `(w,v)` projection: the reduction
of the corrected Q8 octic divides `H(0,v)` exactly once, its cofactor is
coprime to the octic, and the octic is squarefree.  Consequently the
hypersurface `H=0` contains all eight geometric corrected-Q8 projection
points and is smooth in the `v` direction at each of them.

This does **not** prove that `H` belongs to the selected-Q8 ideal, that the
hypersurface lifts to a component of that ideal, or that the remaining seven
coordinates have finite corrected-Q8 limits.  Those require the separately
running coordinate-reconstruction and direct-substitution certificates.

All substantive execution is on AWS.  The local machine may only create,
hash, transfer, and inspect this source and its returned bytes.

