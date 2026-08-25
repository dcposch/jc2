# Preregistration — tame right-composed AS max-12 frontier seeds

Date: 2026-08-25

The replay must check, without importing a campaign solver:

1. both displayed `B_m=(u,v)` maps and their displayed inverses compose to
   the identity over `Z` and have determinant one;
2. `A=(s-s^3,t)` composed with `B_3` has partial `y`-degrees `(9,12)`;
3. after the determinant-preserving target swap/sign, `A` composed with
   `B_4` has partial `y`-degrees `(8,12)`;
4. both leading `y`-face coefficients are constants that are units modulo
   three;
5. both reduced maps have literal polynomial Jacobian one over `F_3` and are
   noninjective on `F_3^2`, with exact fibre census;
6. over `Z`, the unswapped composite determinant is `1-3*u^2`, so the
   replay is a residue-seed check, not a determinant-one characteristic-zero
   lift.

Any failure is `TYPE-FAIL`.  Success proves only the two finite-field seed
identities.  It proves no lift modulo nine, all-depth branch, counterexample,
Q8/TD6 landing, maximum-twelve theorem, or JC2.
