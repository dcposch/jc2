# Preregistration — one-formula global Q9-chart existential gate

Build one exact QF_BV formula whose inputs are all 13 trits of the accepted Q9
chart, all 32 raw Q8 digits, and the nine free Q7 restoration digits supplied
by the reviewed constant rank-nine Q7 matrix.  Impose the complete Q8 source
rows, the ten Q7 cokernel rows, and all terminal high rows in degrees 12--9.

Arithmetic is coefficientwise in `Z/729Z`, with 32-bit operands reduced after
every binary operation; `728^2 < 2^20`.  Exact `/3` gates first assert the
numerator modulo three and then use unsigned division.  A SAT result is
accepted only after reconstructing every integer digit and directly checking
Q9, Q8, Q7, recursive carry, and literal determinant divided by 243.

An UNSAT solver response is diagnostic until the frozen SMT is bit-blasted to
DIMACS, a DRAT/LRAT proof is produced, and an independent checker accepts it.
No statement concerns other Q9 components, larger caps, all depths, a lift, or
the Jacobian conjecture.

