# Q9-fibre to Q8 Lyapunov--Schmidt discriminator

For the predecessor of the first frozen Q9 witness, reconstruct the exact
23-by-32 Q9 affine system, use the frozen witness as origin, and compute a
basis of its 19-dimensional kernel.  Use unreduced integral affine lifts of
the F3 parameters so that the source formulas give a degree-at-most-two
Kuranishi system without digit-reduction discontinuities.

Split the next 22 rows into the accepted 13-row image problem and nine
degree-eight rows.  Emit the exact system

`B(t) s + kappa(t) = 0`,

where `B` is checked affine and `kappa` is checked quadratic.  Verify the
interpolation at deterministic off-grid points.  Compare linear-lift and
canonical-digit compatibility on every bounded search point, and substitute
any survivor into both the Q9 and Q8 source equations.

A survivor proves only that this one predecessor has at least one Q9 state
extending through the displayed Q8 rows.  Failure of the bounded search does
not classify the 3^19-point fibre.  Any disagreement between affine-lift and
canonical-lift compatibility fails closed and records the precise missing
state/gauge translation problem.
