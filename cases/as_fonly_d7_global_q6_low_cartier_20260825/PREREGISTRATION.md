# Global Q6/high survivor low-Cartier successor

Consume only a direct-replayed SAT model from the frozen global Q6/high gate.
Reconstruct its exact integer cap-seven pair `(P,Q)` and determinant.

1. Require every coefficient of `det(P,Q)-1` to be divisible by `243`.
2. Let `R=(det(P,Q)-1)/243`.  The parent gate already imposed all 63
   coefficients in degrees 7 through 12.  Inspect the 28 previously omitted
   coefficients in degrees 0 through 6.
3. Independently build the divergence matrix from two total-degree-7
   simplices to the total-degree-6 simplex over `F3`.  Require rank 27 and
   unique cokernel monomial `x^2*y^2`.
4. If the Cartier coefficient vanishes, construct a deterministic canonical
   `+243(K,L)` correction, directly verify the full determinant is one modulo
   `729`, and compute the next quotient `(det-1)/729 mod 3`.
5. Report the next quotient's 63 terminal coefficients in degrees 7 through
   12 and its low Cartier coefficient.  A nonzero next signature kills only
   this canonical correction, because the 45-dimensional divergence-free
   kernel has not yet been searched.

No filtered-state equation is substituted for the literal integer
determinant.  No all-fibre, all-depth, characteristic-zero, or JC2 inference
is licensed.

