# Fused Q3--Q0 affine completion after the full Q4 gate

Consume the exact full-68 Q4 producer at SHA-256
`ed19ea87d2252e9e483a5c3970549eeac2db62d064e7bd900698b600739180a4`.
For each consistent point, retain the entire affine kernel of its `(H5,J5)`
solutions and adjoin every coefficient of homogeneous
`(H4,J4),...,(H1,J1)` at order 81.  Constant translations are Jacobian-free
spectators and are canonically set to zero.

Build one literal-integer affine system over F3 consisting of:

- all source rows Q4,Q3,Q2,Q1,Q0 (5+4+3+2+1 = 15 rows);
- every over-cap terminal row in degrees 7 through 12 (63 rows).

The determinant is quadratic in the added order-81 digits, but every
quadratic digit-digit bracket is a multiple of `81^2`; after division by 81
or 243 it vanishes modulo three.  Certify the affine reduction by the full
quadratic design (zero, each basis point, twice each basis point, and every
pair sum), not by sparse sampling.

As a staged-equivalence control, separately solve the exact Q3+terminal
subsystem using the whole H5/J5 kernel plus H4/J4 before consuming the fused
answer.  On fused SAT, reconstruct the integer map, replay all Q4--Q0 rows
modulo 243 and all terminal rows modulo 729, verify the full determinant is
one modulo 243 coefficientwise, preserve cap D=7 and the exact AS seed mod3,
and emit three explicit target-zero preimages modulo 243 in the three source
residue balls.

Strict scope: one finite-depth, pointwise construction.  It is not an
inverse-compatible tower, a Q3-adic/algebraic/complex point, a counterexample,
or a JC2 result.  All substantive execution is AWS-only.

