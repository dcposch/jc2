# TD6 V89H16R1 augmented-gate V1 fixture erratum

Date: 2026-08-26

Both V1 AWS runs rebuilt the frozen 22-by-22 compatibility system and reached
its exact inconsistent augmented row.  The client then stopped with
`StopIteration` while selecting an omission-control row, because it assumed
the normalized dual functional must use at least one row with a nonzero q
coefficient.  In fact the first contradiction may be supported entirely on
q-zero rows.  No result artifact or PASS banner was emitted.

R2 changes only the fixture selector: it removes an active row with nonzero
contribution to the normalized constant value.  This is a valid negative
control whether or not that row has q support.  It also reports the number of
active q-supported rows.  All source equations, ranks, row reduction, and
dual-functional algebra are unchanged.  Only an agreeing dual-AWS R2 output
may support a producer claim.
