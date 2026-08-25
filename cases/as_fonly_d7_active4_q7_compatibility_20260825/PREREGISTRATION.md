# Active four-coordinate Q7 compatibility cube

The low-weight predecessor sampler identified exactly four basis directions
whose nonzero scalar multiples fail Q7: Q9 Kuranishi coordinates `t6,t8`
and Q8 solution-kernel coordinates `s15,s17`.  Exhaust their combined
`3^4=81` cube, holding all other predecessor coordinates at the canonical
base state.

For every point, reconstruct canonical Q9/Q8 digits and assert the complete
Q9 and Q8 source rows.  Build the exact Q7 affine system, test whether its
matrix is constant, compute a fixed left-cokernel presentation, and derive
an exact quadratic formula for its ten compatibility residuals.  Emit the
full zero locus and explicit nonzero terms.

This is exhaustive only on the four-coordinate cube.  It does not classify
the other 28 predecessor directions, mixed active/inactive terms, subsequent
high carry, full fixed-cap lifting, or JC2.
