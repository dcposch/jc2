# Degree-one/constant influence audit for the Q2/Q1 obstruction

Consume the exact two-level compiler
`../as_fonly_d7_q3_two_level_q2_q1_20260825/solve_two_level.py` at
SHA-256 `cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd`.

The frozen Gaussian gate omitted order-27 and order-81 homogeneous degree-one
digits.  Add arbitrary `(W1,Z1)` at order 27 and `(H1,J1)` at order 81 to the
entire displayed Q3 affine fibre.  Rebuild the literal determinant and:

1. extract the exact `/27` affine system on all 91 degree-0-through-12 slots;
2. parameterize its complete active-coordinate solution space rather than
   sample it;
3. for every accepted active assignment, prove the `/81` map affine by the
   complete quadratic design and solve all 91 rows;
4. isolate row 8 (`x^2 y`) and record whether any added degree-one coordinate
   changes it;
5. on any SAT branch, direct-replay the literal determinant.

Constant output corrections are excluded from variables because their partial
derivatives are exactly zero; this is an algebraic identity at every modulus,
not a gauge assumption.  Degree-one digits are not normalized away in this
audit.

Strict scope is each of the three displayed Q3 fibres.  Even exhaustive
degree-one independence would not by itself prove that every possible source
normalization or the global Q5 scheme is covered.  All substantive execution
is AWS-only.
