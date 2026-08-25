You are the hostile different-model reviewer for a potentially decisive exact
algebra checkpoint in the plane Jacobian conjecture campaign.  Work from
`/Users/dc/code/math/jc2` at the current dirty worktree, but treat all existing
producer, case, prompt, canonical, coordination, and run files as immutable.
Do not edit them.  Write exactly one new report:

`xmodel/max12-912-order3-double-b-q-algebraicity-review-claude-20260824.md`

The frozen producer is:

- report `xmodel/max12-912-order3-double-b-q-algebraicity-20260824.md`,
  SHA-256 `ea849b39ce35455d72a654ff280d1b8b5c12fe959568b66142a1ea44df184bba`;
- case `cases/max12_912_order3_double_b_q_gb_20260824/`;
- manifest SHA-256
  `f705e7dfcdf75185a626341cc4f4696313ed5dad21e9942e4d93b766e83c0e81`;
- freeze SHA-256
  `1f5f04323e932a340d175395b7d41f050cf5d38c76aac2a5c1bfc136c78307cd`;
- uncompressed exact basis SHA-256
  `6ce7d394989dedcffe303ff8aaf4fb3cb89e750cbf57ad6c15eb9231e11f399e`.

Audit the claim from source, not from the producer's prose.  Required attacks:

1. Run `shasum -a 256 -c` on the manifest and run the frozen verifier.  Inspect
   its code; do not merely quote PASS.
2. Check that the corrected msolve input really declares nine variables first,
   characteristic zero second, and exactly the eight normalized double-B rows
   plus `p*ip-1`.  Trace it independently to the pinned order-three compiler
   and verify the specialization `k=mu=0`, `nu=r6=1`,
   `r1=...=r5=r7=0`, `3*p+10*r8=0`.  Look specifically for denominator,
   row-order, sign, normalization, or missing-equation errors.
3. Inspect the full msolve metadata/log/output.  Decide whether this is a real
   reconstructed characteristic-zero non-unit Groebner basis, as opposed to
   the known first-prime `[1]` short circuit or the earlier malformed
   one-variable input.  Check 126-prime reconstruction, zero bad primes,
   characteristic, variable order, basis length, and hashes.
4. Independently recompute the DRL leading monomials and the finite staircase
   if practical.  In particular test whether pure powers of all nine variables
   truly occur as leading monomials and whether the standard-monomial count is
   1188.  Do not confuse a leading monomial `p^5` with a univariate equation.
5. Attack the exact p=0 claim.  Re-run the Singular scripts, check the direct
   two-way normal-form equality with the displayed intersection, correct the
   raw non-standard-basis dimension diagnostic, and test reducedness/primality
   of the two components.
6. Audit the logical implication: a field-valued point has either p=0 or
   extends by ip=p^{-1} to the saturated zero-dimensional quotient; hence p is
   algebraic over Q; in a trajectory field containing algebraically closed
   constants C it is constant; `3p+10r8=0` makes r8 constant; the reviewed
   terminal row `9 r8'=j/u !=0` contradicts this.  Try to find a loophole in
   the constant-field, nilpotent, embedded-component, saturation, or
   field-valued-point steps.
7. Inspect the consumed reviewed norm and terminal-row inputs, including their
   pinned hashes and scopes.  Ensure this is precisely the retained
   double-root-off-W leaf, not the already-killed full-absorption leaf or a
   broader generic fibre.
8. State the exact trust boundary.  If the frozen evidence verifies only the
   combinatorics of a list but not that msolve's list generates the source
   ideal, decide whether exact msolve 0.10.1 plus source-replay is sufficient
   for confirmation, or whether the verdict must remain INCONCLUSIVE pending
   an independent membership/transformation certificate.  Be conservative
   and explicit; distinguish an engine-trust caveat from an actual mathematical
   error.

Never run msolve locally: the Mac has 32 GB.  Local exact Python/Singular checks
are allowed in scratch only.  Do not mutate any frozen byte.  Give one of
`CONFIRMED`, `REJECTED`, or `INCONCLUSIVE`, then the smallest failing identity
or missing certificate, exact promotable sentence, and strict scope firewall.
No result here may be promoted to all `(9,12)`, maximum twelve, a
counterexample, or JC2.
