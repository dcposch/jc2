# Preregistration — raw-Q7 global chart formula (promotion target)

Construct one exact formula with all 13 accepted-chart Q9 trits, all 32 raw Q8
digits, and all 18 raw Q7 restoration digits symbolic.  Impose independently:

- the 23 Q9 source rows on the symbolic Q9 coefficients;
- all 22 Q8 source rows;
- all 19 Q7 source rows, without a fixed-matrix reduction; and
- all terminal high rows in degrees 12 through 9.

The producer may reuse hash-pinned polynomial/carry primitives, but it must not
consume the sampled Q7 matrix-constancy claim.  Arithmetic is exact in the
same widened 32-bit `Z/729Z` circuit, reducing after every gate.  SAT requires
direct replay through the independent integer Q9/Q8/Q7 and literal determinant
functions.  UNSAT promotes only after a predecessor SAT/direct-source control,
deterministic bit-blast, CaDiCaL proof, and independent proof checking.

