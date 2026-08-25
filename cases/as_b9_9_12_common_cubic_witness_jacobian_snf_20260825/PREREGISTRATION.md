# Preregistration — common-cubic witness Jacobian/SNF

At the source-replayed normalized B9 common-cubic witness modulo `3^11`,
reconstruct from scratch the 299 equations in 149 variables:

- all 276 determinant coefficients in the `(P<=9,Q<=12)` box;
- all 10 coefficients of `P9-P_(0,9)H^3`;
- all 13 coefficients of `Q12-Q_(0,12)H^4`;
- the 146 P/Q coefficients and three non-monic coefficients of
  `H=y^3+h1*x*y^2+h2*x^2*y+h3*x^3`.

Compute the exact integer Jacobian, rational rank, mod-3 rank, Smith
invariants, primitive rank profile, and residual valuations.  Let `e_min` be
the 3-adic valuation of the maximal-rank determinantal ideal.  Compute the
largest `N_best` for which the rows whose residuals have valuation at least
`N_best` still have full rational Jacobian rank.  If
`N_best <= 2*e_min`, record a rigorous failure of every classical
full-rank-minor Hensel inequality at the current precision.  Do not infer
nonexistence.  If the inequality can pass, emit an actual minor and proceed
only after local row-ideal generation is certified.

All execution is AWS-only.
