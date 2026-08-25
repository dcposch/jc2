# Complete 27-branch Gaussian carry classifier V4

Consume V3 source SHA
`4f6b94ce223e60b9023b8e3fe91a1113b0978a4ff74e986aa1227e01217006b9`.
V3 stopped incorrectly when its first `/81` affine branch was inconsistent.

Enumerate all 27 accepted `/27` active assignments.  On each, prove the `/81`
map affine by the full quadratic design, compute RREF, and retain exact
contradiction rows instead of asserting consistency.  Only consistent branches
may proceed to the `/243` high-row affine-design test.  Any nonaffine later
carry remains open.  All-branch `/81` inconsistency is an exact finite-field
exclusion for the displayed Q3 fibre, subject to source review; no solver-only
inference is used.

AWS-only; strict pointwise-parent/fixed-support/finite-depth scope.
