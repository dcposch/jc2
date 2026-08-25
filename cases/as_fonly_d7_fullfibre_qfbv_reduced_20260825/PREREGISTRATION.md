# Preregistration — constant-Q7-matrix reduction

Before changing the full-fibre solver, independently reconstruct the Q7 source
matrix from the frozen integer-source compiler.  For every selected Q9 state,
solve its canonical Q8 affine system and evaluate the Q7 restoration matrix at
the zero Q8-kernel point and at both nonzero multiples of every one of the 19
kernel basis vectors.

The source formulas imply that the coefficients of the 18 Q7 restoration
digits are affine-linear in the Q8 digits: the only possible mixed term is the
binary bracket, and the Q7 restoration digits occur only linearly in total
degree seven.  Therefore equality at zero and at both multiples of every
basis vector proves constancy over the full Q8 affine fibre.  Pair-sum points
are included as implementation controls, not as the proof of the degree
bound.

The gate must emit the common matrix, its rank/RREF pivots/kernel, hashes, and
direct Q9/Q8/Q7 substitution checks.  Only after this audit passes may a
reduced 19+9-trit existential solver replace the raw 19+18-trit solver.

