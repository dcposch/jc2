# Global-predecessor SAT-survivor gate

Search each of the 79 exact compatible structural bases from the corrected
aligned `D=7`, `p=3` predecessor census with the raw-variable formula in
`cases/as_fonly_d7_global_predecessor_rawq7_20260825`.

For every solver SAT endpoint, independently reconstruct the literal integer
polynomials from the emitted predecessor, Q9, Q8, and Q7 digits.  Require all
20 predecessor rows, the corrected degree-12/11/10 rows, all 23/22/19 source
rows, recursive-versus-literal `/243` agreement, and all 46 terminal
degree-12-through-9 rows to vanish.  A SAT endpoint is retained only when that
direct replay passes.

A passing model is a successor state at this bounded gate.  It is not yet a
Q6 completion, a lift to the next modulus, an all-depth formal lift, a
characteristic-zero polynomial map, a counterexample, or a statement about
JC2.
