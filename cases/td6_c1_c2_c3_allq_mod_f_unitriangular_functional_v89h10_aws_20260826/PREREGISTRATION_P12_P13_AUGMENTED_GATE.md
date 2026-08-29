# TD6 V89H16R1 P12/P13 augmented compatibility gate

Date: 2026-08-26

The frozen H16 coefficient matrix has exact rank 12 rather than the proposed
rank 22 at `(U,V,C)=(1,3,8)`.  Compute the exact augmented rank without
changing any P12/P13 row or q column.  If the affine system is inconsistent,
emit a normalized dual row functional that annihilates all 22 q columns and
sends the constant vector to 1.  If it is consistent, emit its full affine
solution space and test the canonical particular solution plus deterministic
nullspace samples against the remaining four y-dependent P12/P13 equations.

Any obstruction is scoped to this one denominator-safe rational base fibre.
Any point is scoped to the frozen P12/P13 normal forms modulo FIRST.  Neither
outcome supplies a literal total-source theorem or a later-CURRENT result.
