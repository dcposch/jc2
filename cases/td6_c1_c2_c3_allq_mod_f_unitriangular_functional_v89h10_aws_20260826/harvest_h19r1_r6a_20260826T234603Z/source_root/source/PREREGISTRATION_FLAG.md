# TD6 V89H10T simultaneous triangular-flag gate

Date: 2026-08-26

Status: producer gate; no result claimed before dual AWS replay.

For the frozen V89H10G relative FIRST matrix, extract the thirteen exact
coefficient matrices of q2,...,q14 on the unique 14-node SCC.  Search over
the exact specialized E3 field for a complete common invariant flag by
successive common-kernel computations on quotient modules.  No q value is
specialized during this search.

If a 14-step flag exists, emit the constant basis matrix and its exact
two-sided inverse, require every coefficient matrix to become strictly upper
triangular, extend the basis by identity to all 38 FIRST rows, and require
the full all-22-q transformed N graph to be acyclic and strictly upper after
an emitted topological permutation.  Audit every basis/inverse denominator;
only the specialized `D(U*H*B3)` factors `U`, `V`, and `V^2-4U^3` are
licensed.

Passing gives a compact exact finite-Neumann theorem without expanding the
exponentially large polynomial inverse: the emitted strict-upper matrix has
nilpotence index at most 38 and its two-sided inverse is the finite sum
`I-N+...+(-N)^37`.  This gate does not expand that sum, divide P12, extend
the q14 functional, prove a unit ideal/source exclusion, totalize q15,
supply total-Rees, close whole TD6, or resolve JC2.
