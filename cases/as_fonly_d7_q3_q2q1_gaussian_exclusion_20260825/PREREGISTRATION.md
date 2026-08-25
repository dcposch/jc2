# Exact Gaussian exclusion of the three displayed Q3 fibres

Consume V3 source SHA
`4f6b94ce223e60b9023b8e3fe91a1113b0978a4ff74e986aa1227e01217006b9`.
For each displayed parent, enumerate the exact 27 accepted assignments of the
eight-variable `/27` source cone.  On each branch prove the `/81` map affine by
the full quadratic design and row-reduce it while tracking every row operation.

For every inconsistent branch emit a sparse vector `lambda` satisfying
`lambda^T M = 0` and `lambda^T rhs = 1` over F3.  Also find a one-row omission
control where possible, reconstruct its raw digit assignment, and literally
check that every `/27` row and every retained `/81` row vanishes while the
omitted row is nonzero.  Store full matrices/RHS so a separate implementation
can verify certificates without trusting the reducer.

If and only if all 27 branches have checked certificates, conclude that the
complete displayed Q3 affine fibre has no continuation making every
determinant coefficient divisible by 243 with the specified degree-two/three
order-27 and order-81 digits.  This is pointwise-parent, fixed-support,
finite-depth only; it is not the whole Q5 locus, all-depth, or JC2.

All substantive runs and certificate replay are AWS-only.
