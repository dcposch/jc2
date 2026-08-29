# TD6 V82QST1R arbitrary-pivot DAG repair

Date: 2026-08-26

V82QST1 correctly changed the pivot selector but exposed an ascending-only
presentation assumption: its form builder substituted pivots in descending
variable-index order.  Sparse q2 and q10 therefore stopped at the same
source-side assertion before any CURRENT denominator verdict.  Those bytes
remain deployment-negative evidence only.

V82QST1R makes the minimal algebraic repair.  A forward echelon row has been
reduced against every earlier inserted pivot, so it can introduce only later
insertion-order pivots.  Raw-row restriction and polynomial reduction follow
forward insertion order, while affine form reconstruction follows reverse
insertion order.  Every pivot/source replay and omission control remains
active.

Run the four cells `reverse:q2`, `sparse:q2`, `reverse:q10`, and `sparse:q10`
on both Box03 and r6d.  Each cell has a 2 GiB/2 h fail-closed cap.  Compare
exact reduced-coordinate tables and factor ideals across hosts and against
ascending Gate 0.  Expand to q3..q9 only if a pilot changes the radical factor
ideal or yields a credible principal-open cover with an explicit localized
Bezout/Cech identity.  A gcd or selected-minor factor difference is not a
cover.

Fixed source-typed A3 and already-empty-base diagnostic only.  No tangent
family, nonlinear family, TD6, SP2, or JC2 inference.

