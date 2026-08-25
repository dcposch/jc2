# Frozen exhaustive Q7-kernel high-carry result

At fixed canonical Q9 vector `x23=x30=1` and fixed zero Q8 vector, the Q7
transition is homogeneous of rank nine on eighteen variables.  The AWS
census evaluates all `3^9=19683` points of its kernel.  The Q6 divergence
map has rank seven on seven rows and a nine-dimensional kernel, while its
variables affect the following carry only through degree eight.

For every one of the 19683 Q7 states, the recursively derived rows
`R12..R9` equal the rows from the literal integer determinant divided by
243.  Their exact quadratic presentation is the constant row
`R10=x^10`; there are no other terms.  Hence every Q7 state and every
compatible Q6 choice is terminal at the next cap-seven carry.

This kills one fixed Q9/Q8 branch.  It does not cover the thirteen other
directions in the preceding Q8 affine chart or the six pinned Q9 Frobenius
spectators.
