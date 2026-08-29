# V29 preregistration: whole ordered-a1 rho=0 stratum through grade 16

Date: 2026-08-27

V27 proved that the grade-15 prefix does not generate `a1^3` on `rho=0`.
V28 then exhibited one rational `a1=1` prefix point and proved that this
particular point is killed by `Tg16_4=-47/384`.  V29 asks the required
set-theoretic question for the whole registered boundary stratum.

Because every input row is positively sigma-homogeneous and `a1` has weight
5, an algebraic-closure point with `a1 != 0` can be weighted-rescaled to
`a1=1`.  Specialize `rho=0` and `a1=1` in all 49 hash-pinned rows of grades
10--16 and test whether their ideal is the unit ideal.

- exact Q on Box02 and characteristic 65521 on Box03;
- complete `std` only: no `degBound`, truncation, quotient ring, or hidden
  localization;
- old-point evaluation is a negative control for the grades 10--15 prefix;
- its exact nonzero `Tg16_4=-47/384` value is a grade-16 source control;
- two-hour wall cap per basis and host-sized virtual-memory caps.

This is a producer-tier screen.  A unit-ideal verdict must be followed by an
explicit lift/certificate; a nonunit verdict must be followed by a point or
prime/component witness.  No result alone is a Jacobian-conjecture theorem.

