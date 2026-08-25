# Preregistration — 19+9-trit reduced full-fibre solver

Consume the separately frozen constant-Q7-matrix audit provisionally.  For one
fixed Q9 state, retain all 19 canonical Q8-kernel trits.  Build the exact Q7
right-hand side with zero restoration digits, solve nine independent Q7 rows
using the fixed rank-nine matrix, and parameterize the restoration fibre by
nine free trits.  Impose the ten remaining Q7 compatibility rows and every
terminal high row in degrees 12 through 9.

All arithmetic uses the same 32-bit, reduce-after-every-gate `Z/729Z` circuit
as the raw 19+18-trit solver.  The largest unreduced product remains
`728^2 < 2^20`.  A SAT model is theorem-level only after direct integer source
substitution and recursive-versus-literal determinant `/243` agreement.
UNSAT/UNKNOWN remains diagnostic without an independent certificate.

