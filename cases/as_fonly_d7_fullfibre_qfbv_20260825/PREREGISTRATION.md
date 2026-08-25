# Preregistration — exact widened-BV full-Q8-fibre witness gate

For each pinned Q9 presentation-class representative in `STATE_REPRESENTATIVES.tsv`,
solve existentially for all 19 canonical Q8-kernel trits and all 18 raw Q7
restoration trits.  Impose every Q7 source row and the next high rows in total
degrees 12 through 9.

The circuit works coefficientwise in `Z/729Z`.  Every residue lies in
`[0,728]`; every multiplication is performed in 32 bits before `URem 729`,
so the largest unreduced gate product is `728^2 = 529,984 < 2^20 < 2^32`.
Addition is reduced after each binary gate.  Each exact `/3` gate first
asserts divisibility modulo 3 and uses unsigned division on a residue in
`[0,728]`.  Modulus 729 retains more than the three successive carry divisions
require.

For every SAT result, reconstruct the integer digits, assert Q9/Q8/Q7 rows,
and compare the recursive carry with the literal determinant divided by 243.
Also report the typed next-correction divergence Jacobian: at cap seven it has
28 output rows, rank 27, and Cartier cokernel carrier `x^2 y^2`, so ordinary
surjective smooth Hensel is unavailable even for a SAT hit.

SAT plus direct replay is positive evidence.  UNSAT/UNKNOWN without DRAT/LRAT
or an algebraic certificate is diagnostic only.  No selected-state result is
a full-chart or all-depth theorem.

