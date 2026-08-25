# State-complete Q2/Q1 bit-vector gate

For each pinned structural control, consume the complete Q3 affine kernel from
producer SHA-256
`14d69e65255482491293373bbbd212742e2077322931e65b8d5af215915d303b`.
Use its kernel coordinates as symbolic trits, add every order-27 homogeneous
degree-three/two source digit and every order-81 homogeneous degree-three/two
source digit, and reconstruct the determinant from the pinned integer source.

Avoid all RREF-representative carry assumptions.  Reduce every arithmetic gate
modulo 729 in 32-bit unsigned bit-vectors (the product bound 728^2 is below
2^20), constrain every total-degree 0..12 coefficient to be zero modulo 243,
and constrain every total-degree 7..12 coefficient to be zero modulo 729.
Assert the degree-zero residue separately.  Emit the exact QF_BV formula.

Race Boolector and Z3 on AWS.  SAT is accepted only after an independent
literal-integer reconstruction checks the inherited 67 Q3 rows, all `/27` and
`/81` rows, all high `/243` rows, support cap D=7, and exact degree zero.
UNSAT remains solver evidence until a checked DRAT/LRAT or independent exact
finite-field certificate exists.  A high-row-omission SAT formula is the
positive control.

Strict scope: three displayed Q5/Q4/Q3 structural controls only; fixed support
D=7 at the displayed finite precision; no all-depth, algebraization,
counterexample, or JC2 inference.
