# Preregistration: bounded exact residual-minor/factor census r3

Date: 2026-08-28

The clean r2 theorem leaves an exact 11 by 10 residual on each of nine
genuine generic-dead strata.  R3 consumes the frozen terminal archives,
replays every evidence hash, and computes only the next exact Fitting-minor
census and literal factor diagnostics.  It performs no full Groebner basis,
no saturation, no cancellation of raw minors or their gcd/content, and no
endpoint pullback.  Every clean result remains
`NO_VERDICT_MINOR_FACTOR_CENSUS_ONLY`.

For C8, P, and C8P02 the exact residual rank is 9.  Preserve all 550 signed
9 by 9 determinant slots in lexicographic row-subset/column-subset order,
including zeros; factor each exact nonzero determinant and record the common
gcd only as a diagnostic.  A frozen support precheck finds 172 structurally
matchable slots, but this is not used to discard any raw determinant.

For Q1, C8_Q1, Q1P02, Q1P03, TRIPLE02, and TRIPLE03 the exact residual rank
is 6 and the support graph is block diagonal: rows (4,7,9,11) against columns
(1,2,4,6,7,8,9,10), and rows (1,2,3,5,6,8,10) against columns (3,5).
Recheck the zero off-block entries and exact block ranks 4 and 2 in Singular.
Preserve all 70 signed 4 by 4 minors of the first block and all 21 signed 2 by
2 minors of the second.  Preserve a complete 97,020-slot formal I6 census:
95,550 structural-zero slots and 1,470 signed products, with exact sign and
block-minor indices.  Emit the exact 1,470 product polynomials.  The block
identity licenses the scheme-level equality
`I6(residual)=I4(blockA)*I2(blockB)`; no radical or component verdict is
inferred until the factor outputs are reviewed.

Each component retains the r2 EC2 identity except C8_Q1, which is scheduled
after C8 on r6a.  The existing r6d host is deliberately kept idle and
zero-swap for a pending reviewed root-aware pole census.  Eight r3 jobs may
run concurrently, followed by C8_Q1.  Each job has one CPU, 96-GiB address
cap, 32-GiB file cap, 3,600-second algebra cap, 7,200-second group cap,
immutable source, exact Singular SHA `90ab699b...`, zero total swap, and
starttime/no-orphan custody.  Adapter/resource failure is always
`NO_VERDICT` and never mathematics.

