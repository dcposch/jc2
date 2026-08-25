# Source-honest Q6 plus divided-high gate on the SAT survivors

The Q9/Q8/Q7 SAT states are filtered source states, not complete maps modulo
81.  Do not append a chronological `+81` digit to the whole pair.

For each exact survivor, reconstruct the frozen nested carry.  Adjoin only
the licensed homogeneous degree-seven fourth-digit pair `(H7,J7)` (16
trits).  Impose:

1. the seven Q6 source rows
   `G6 + (H7)_x + (J7)_y = 0`; and
2. every following divided-carry row in degrees 12 through 7.

The degree-12-through-9 rows are positive controls already forced by the
parent SAT formula.  Degrees 8 and 7 are the first genuinely unencoded high
rows.  Compute the complete affine matrix over `F3`, its rank and augmented
rank, a canonical solution/kernel when compatible, or an explicit reduced
contradiction row when incompatible.  Replay every equation by direct
substitution into the integer nested carry.

This is one filtered transition only.  It does not license a chronological
modular lift, a lower-row completion, an all-depth formal lift, a
characteristic-zero map, a counterexample, or JC2.
