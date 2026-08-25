# Hostile review — B9 fixed-D12 full affine linear window through `3^10`

Producer reports:

- `xmodel/as-b9-max12-full-output-mod729-producer-20260825.md`;
- `xmodel/as-b9-max12-full-fibre-linear-window-producer-20260825.md`.

Frozen cases:

- `cases/as_b9_max12_full_output_mod729_20260825/`;
- `cases/as_b9_max12_literal_digit_ladder_20260825/`;
- `cases/as_b9_max12_full_fibre_mod2187_20260825/`;
- `cases/as_b9_max12_full_fibre_linear_window_20260825/`.

Required output:

`xmodel/as-b9-max12-full-fibre-linear-window-review-grok-20260825.md`

## Charges

1. Trace the exact B9 mod-243 parent and independently check that the complete
   fresh support really contains both copies of every total-degree-at-most-12
   monomial (182 columns), while the determinant ambient contains all 276
   rows through degree 22.  Distinguish 135 identically zero ambient rows from
   omitted equations.
2. Audit the source orientation and the integer identity
   `det J(F5+243T)-1=D5+243*A*T+243^2 det J(T)`.  Check all divisions and the
   8,281 P/Q pair controls.
3. Recompute or independently audit the first complete gate: rank 108,
   kernel 74, consistency modulo 729, actual total degrees `(11,12)`, partial
   `y` degrees `(9,12)`, and every-row integer replay.  Confirm that the TD6
   owner's 141-row implementation drops only identically zero rows and finds
   the identical 11-term RREF particular; treat it as parallel corroboration,
   not an independent mathematical solution.
4. Confirm the pointwise negative control: the deterministic mod-729
   particular is inconsistent at mod 2187.  Then verify that no fibrewise
   conclusion is drawn from it.
5. Audit the full 74D Bockstein/cokernel projection.  Check fresh rank/cokernel
   `108/168`, 70 nonzero affine obstruction equations of coefficient rank 39,
   combined rank/kernel `147/109`, consistency, and projection dimension 35.
6. Audit every later full-family Bockstein and the claimed table:
   `6561: 162/129/projection55`,
   `19683: 164/147/projection73`, and
   `59049: 164/165/projection91`.  Look for duplicate parameterizations,
   wrong affine constants, or a projection-rank orientation error.
7. Check literal integer witnesses, support/y-degree caps, both-host custody,
   manifests/freezes, and exact report hashes.  Box02/Box03 are two executions
   of one implementation.
8. Enforce the off-by-one firewall: `243^2=3^10` vanishes modulo `3^10` and
   first contributes after division by `3^10` in the transition from
   mod-`3^10` to mod-`3^11=177147`.  No linear Bockstein is licensed there.
9. State the strongest exact theorem and refuse complete earlier mod-243
   fibre, inverse-limit/`Z_3`, characteristic-zero collision, counterexample,
   maximum-twelve, no-lift, or JC2 overreach.

Do not run Bash, Python, CAS, or solvers on the local Mac.  Prefer a no-shell
source/mathematical review.  If replay is essential, run it only on AWS and
record custody.  Return `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REJECTED`,
separating mathematics, source typing, software, custody, and wording.
