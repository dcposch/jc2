# Hostile review — AS D7 complete three-fibre output cones modulo 729

Producer:

`xmodel/as-fonly-d7-q3-full-output-cone-z27-producer-20260825.md`

Frozen case:

`cases/as_fonly_d7_q3_full_output_cone_z27_20260825/`

Required output:

`xmodel/as-fonly-d7-q3-full-output-cone-z27-review-grok-20260825.md`

## Charges

1. Trace the complete pinned source chain back through the reviewed Q3 and
   mod243 parents.  Confirm the inputs are exactly fibres `0000`, `0270`, and
   `0513`, including their full Q3 kernels, not reset representatives.
2. Independently derive, with the source orientation, the exact identity
   `det J(F0+27T)-1=D0+27*A*T+729*det J(TP,TQ)`.  Confirm that modulo 729 the
   complete 91-row problem is the linear congruence
   `D0/27+A*T=0 mod27`, with all 72 D7 output coefficients present and no
   support outside total determinant degree 12 omitted.
3. Audit all three Bockstein stages, especially integer representatives,
   exact divisions, kernel directions, the stage-one-to-T affine constant,
   and the claimed injective parametrizations.  Recompute or otherwise check
   ranks/kernel dimensions `27/45 -> 36/81 -> 47/106` and
   `27/45 -> 43/74 -> 49/97`.
4. Audit the projection from the final affine solution space to the complete
   prior mod243 modules.  Confirm the liftable-prior dimensions are exactly
   61 of 81 and 52 of 74, and that adding the 45-dimensional fresh top-digit
   kernel gives new exponents 106 and 97.  Look for duplicated parameter
   representations or a mistaken row/column-rank calculation.
5. Check that each literal reconstructed P,Q has degree at most seven,
   reduces exactly to `(x-x^3,y)` modulo three, and makes every coefficient
   of the determinant residual divisible by 729.  Do not accept stored
   booleans without source/payload consistency.
6. Charge all 1,296 P/Q pair controls and the 1,008/720/720 Q3-kernel/fresh
   controls.  Verify that Q3-kernel absorption remains valid modulo 729 and
   does not hide a nonlinear parameter direction.
7. Audit both-host/source/result/rc/manifest/freeze custody.  Treat Box02 and
   r6d as independent executions of one implementation, not independent
   implementations.
8. Check the next-modulus firewall.  Modulo 2187 the term
   `729*det J(TP,TQ)` survives and varies quadratically, so no fourth global
   linear-Bockstein claim is licensed.  State the strongest theorem and
   refuse whole-predecessor, all-depth, collision, characteristic-zero,
   counterexample, no-lift, or JC2 overreach.

Do not run Bash, Python, CAS, or solvers on the local Mac.  Prefer a no-shell
source/mathematical review.  If independent replay is essential, run it only
on AWS and record exact custody.

Return `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REJECTED`, separating
mathematics, source typing, software, custody, and wording/scope issues.
