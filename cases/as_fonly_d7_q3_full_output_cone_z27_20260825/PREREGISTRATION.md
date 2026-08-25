# Preregistration: complete fixed-D7 output cone modulo 729

Date: 2026-08-25

Consume one of the three reviewed Q3 parents and write

`F = F0 + 27*T`, with `T` ranging over both complete degree-at-most-seven
output polynomials modulo 27 (72 coordinates).

Use the exact identity

`det J(F)-1 = D0 + 27*A*T + 729*det J(T_P,T_Q)`.

Thus the complete determinant condition modulo 729 is the linear congruence
`D0/27 + A*T = 0 (mod 27)`.  Solve it by three exact F3 Bockstein stages,
not by enumerating the previously frozen `3^81` / `3^74` modulo-243
families.  Report the dimension and count of the subset of prior modulo-243
solutions that lifts, the complete new module dimension, exact integer replay
of all 91 rows, and pair/mixed controls.

SAT proves only a fixed-D7 determinant-one congruence modulo 729 over the
displayed Q3 fibre.  UNSAT would empty that displayed fibre only.  Neither
outcome licenses another predecessor, all-depth lifting, collision, a
characteristic-zero point, a counterexample, or JC2.  Substantive execution
is AWS-only.
