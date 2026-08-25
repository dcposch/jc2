# Frozen V3 pointwise result

Box02 ran the source-frozen V3 compiler under tag
`as_q9_q8_kuranishi_v3_20260825T020224Z` with return code zero and empty
standard error.  For the first canonical Q9 witness, the accepted 13-row
system has rank pair `(13,13)`, while the full 22-row system has rank pair
`(13,14)`.  Thus the nine-row Kuranishi map has rank zero on the
19-dimensional accepted-image kernel, and this representative is obstructed.

The emitted sparse certificate is `lambda=e_21` in zero-based ordering of
the 22 rows.  This is the `x^8` coefficient of `G_8`.  Direct checks give
`lambda*A=0` and `lambda*b=2` in F3.  Adding one to that RHS coordinate
changes the pairing to zero, supplying a sign/orientation control.

This is a pointwise result only.  The 16--19 affine Q9 coordinates above a
predecessor can change the Kuranishi RHS and perhaps the transition matrix.
Nothing here kills a predecessor, rank class, the D7 branch, or an
all-depth lift.

The earlier V1 and V2 runs are preserved as assertion-failure negative
controls.  V1 assumed compatibility.  V2 intended to emit an obstruction
but compared a 13-row partial substitution against all 22 rows.  Neither
earlier failure is mathematical evidence.
