# Narrow implementation API check — 2026-09-09 21:23 UTC

Root read the official python-flint 0.9.0 documentation at
https://python-flint.readthedocs.io/en/latest/fmpq_mat.html . This was a narrow
API lookup, not a campaign web sweep or a mathematical execution.

The documented dense rational matrix constructor accepts row/column counts
and rational entries. fmpq accepts an integer numerator and denominator.
fmpq_mat.rref() returns a pair (reduced matrix, rank); it does not return
pivot indices or a transformation matrix. Entries are indexed by row,column.
The documented solve() requires a square invertible input, so it is not a
direct solver for the rectangular 217-by-1638 contract.

Implementation suggestion, NOT a new proved campaign theorem: RREF the one
augmented rational matrix [M | b | I_217]. A pivot in column1638 identifies
a normalized dual obstruction via that row's identity-block entries. If b
is not a pivot column, zero free variables and the b entries in M-pivot rows
give a candidate primal witness. The separate exact verifier must validate
the full identity or every dual column, regardless of solver behavior.

Installed availability/version on the exact future worker is UNKNOWN; this
note supplies no package-import, installation, worker-start or solve authority.
No package code is imported locally. Keep unknown runtime/cost explicit.
