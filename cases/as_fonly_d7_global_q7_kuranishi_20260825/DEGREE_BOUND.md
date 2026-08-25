# Source degree bound for the global Q7 Lyapunov--Schmidt chart

Work only over the frozen **unreduced affine-lift** fixed-predecessor F-only
`p=3,D=7` chart.  Its Q9 Kuranishi zero locus has 13 free parameters and its
Q8 accepted-image kernel has 19 parameters.

1. The Q9 digit `x(t)` is affine in the 13 free `t` coordinates.
2. The accepted Q8 rows `E_2,F_3,F_5` are affine in `(x,y)`.  Their
   13-by-32 coefficient matrix in `y` is constant of rank 13.  Therefore its
   fixed-RREF right inverse gives an unreduced affine section in `t`.  The
   frozen Q8 Kuranishi presentation
   proves that on the displayed 13-dimensional Q9 locus the remaining `G_8`
   rows vanish for every vector in the fixed 19-dimensional kernel.  Hence
   `y(t,s)=section(t)+K*s` is affine in all 32 parameters.
3. In the source `q7_rows`, `E`, `M`, the divergence terms, and `T` are
   linear in the digit polynomials.  The only nonlinear expression is
   `N_7=[C,D]_7`, which is bilinear.  Exact integer divisions by three occur
   before reduction and do not increase polynomial degree.  Thus the Q7 rows
   have total degree at most two in `(t,s,q7_unknowns)`.
4. Consequently the Q7 unknown-coefficient matrix is affine in `(t,s)`, and
   the right side at zero Q7 unknowns has total degree at most two.  The basis
   shard checks the coefficient matrix at zero and both nonzero scalar
   multiples of every basis vector.  If all agree, every affine variable
   coefficient is zero and the Q7 matrix is constant on the whole
   32-dimensional unreduced chart.

It follows that constant, both nonzero scalar multiples of every basis vector,
and every pair sum uniquely determine the exact reduced quadratic Q7 cokernel
map on this unreduced chart.

This is **not** a canonical-digit degree bound.  Reducing affine integer digit
representatives to `0,1,2` before an exact division by three can introduce a
carry function of higher parameter degree.  The existing Q9-to-Q8 producer
checked canonical translation at only 36 points.  A carry-translation theorem
or extra carry state is still required before treating this 32-parameter map
as a global canonical-state classification.  The argument also does not
license the six frozen Frobenius spectators in the predecessor source data.
