# Selected-Q8 fixed-`w` fibre discriminators (AWS-only)

This package specializes the exact generic quotient at a nonzero finite-field
value of `w`, localizes `x5*(x3-2*x5)`, and eliminates to `v`.  It reports the
zero-dimensional degree, eliminant degree/squarefreeness, and exact factor
list.

At a prime such as `ell=89`, corrected Q8 has four rational roots and all four
selected branches have nonzero six-by-six Jacobian determinant.  If one
degree-preserving fixed-`w` eliminant is irreducible, the generic eliminant is
irreducible over `F_ell(w)`: a proper generic factorization would specialize
at every value avoiding its finitely many leading/denominator zeros.  The
equal-degree/squarefree checks are needed to make `v` a primitive element of
the finite generic algebra.

This is still modular component evidence.  A characteristic-zero conclusion
requires the exact generic-fibre run or a flat/good-reduction certificate.
Run every shard on AWS; the runner has a four-hour / 64-GiB guard.

