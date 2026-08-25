# Q7-kernel next high-carry census

Fix the cumulative canonical Q9 `e17` survivor and zero Q8 vector.  Use the
exact nine-dimensional kernel of the Q7 transition, hence all `3^9=19683`
Q7 accepted digits.  For every state, reconstruct canonical digit
representatives and derive the fifth-order rows `R12,R11,R10,R9` both from
the recursive carry and the literal integer determinant divided by 243.

The fourth-digit `H7,J7` variables can affect the next carry only in total
degree at most eight; certify that degree bound on every coordinate basis.
Consequently the rows of degree at least nine are independent of the
nine-dimensional Q6 solution fibre.  The Q6 divergence map has full row
rank seven, so every Q7 state has some accepted Q6 digit.

Run 27 disjoint deterministic shards, aggregate all 19683 states, and test
whether the complete high-row map is represented by a quadratic polynomial
in the nine Q7-kernel coordinates.  A zero-free high-row census kills this
fixed Q9/Q8 branch through every Q7/Q6 choice.  A survivor is only a
successor state, not an all-depth lift.

No claim concerns the other thirteen Q8-chart directions, the six pinned
Q9 Frobenius spectators, the full fixed-cap locus, an all-depth lift, or JC2.
