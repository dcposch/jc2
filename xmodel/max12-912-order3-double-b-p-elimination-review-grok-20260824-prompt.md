Hostile-review the frozen exact univariate `p`-elimination certificate for the
plane Jacobian conjecture campaign.  Work in `/Users/dc/code/math/jc2`.
Treat every existing producer, case, canonical, coordination, prompt, log, run,
and review byte as immutable.  Write exactly one new report:

`xmodel/max12-912-order3-double-b-p-elimination-review-grok-20260824.md`

Frozen target:

- report `xmodel/max12-912-order3-double-b-p-elimination-20260824.md`,
  SHA-256 `37667ebaa943b5f1a4a7afc46331ac0cdf3d1ab0bd0ead82047bce0677aead87`;
- case `cases/max12_912_order3_double_b_p_elimination_20260824/`;
- manifest SHA-256
  `576485096ba84b4fc8b329fb2e3d10c48a2e8b45ed85ce83d4a902238e6bc68d`;
- freeze SHA-256
  `198b9daa41ee299f5720d8024ce06606ec19598539a78edda2bb3c2c32ddb256`;
- result SHA-256
  `50d71a0b76239db801e5c75ff9497f33d62086c4b8f7b5fd0a3e1bfb67852a75`.

Required attacks:

1. Run the manifest check and verifier, then inspect the verifier rather than
   trusting PASS.  Independently parse the polynomial if possible.
2. Verify the first input line declares exactly nine variables in p-last
   order, the second line is characteristic zero, and there are exactly the
   eight source-honest normalized double-B equations plus `p*ip-1`.  Regenerate
   from the pinned parent compiler and audit signs/denominators/specialization.
3. Audit msolve 0.10.1 telemetry: ELIM(8), nine valid equations, one polynomial
   lifted, 120 primes, no bad primes, coefficient height, output characteristic
   and variable order.  Rule out the malformed earlier one-variable trials and
   the characteristic-zero `[1]` short circuit.
4. Inspect the telemetry anomaly `homogeneous input? 1` despite visible
   constants in `r6-1` and `p*ip-1`.  Determine whether it exposes a parsing or
   mathematical error, an elimination-mode/internal-homogenization label, or
   only a tool-reporting caveat.  This is load-bearing: be conservative.
5. Check the exact polynomial has degree 630, primitive integer content one,
   exactly 71 nonzero terms at exponents `0,9,...,630`, and nonzero constant.
   Independently reduce it modulo 32003, 100003, and 104729, normalize the lead,
   and compare all coefficients against the frozen Singular product-order
   outputs.  Inspect those Singular scripts for source equivalence.
6. Audit the elimination logic: if the exact output is a basis for
   `J=I+(p*ip-1)`, then `P(p) in J`; every p!=0 field point of I extends to J;
   p=0 is already constant; hence p is algebraic over Q at every field point.
   In a trajectory field containing algebraically closed constants C, p is
   constant; `3p+10r8=0` makes r8 constant; reviewed `9r8'=j/u!=0` contradicts
   it.  Attack saturation, nilpotent, embedded-component, constant-field, and
   differentiation loopholes.
7. State the precise CAS trust boundary.  Decide whether the reconstructed
   exact elimination output plus input replay and three independent modular
   Singular matches is sufficient to CONFIRM, or whether exact ideal
   membership/transformation from a second characteristic-zero engine is still
   mandatory and the result must remain INCONCLUSIVE.  Do not turn an engine
   caveat into invented wrong math, but do not waive a missing certificate.

Never run msolve locally (32-GB Mac).  Scratch-only local Singular/Python is
allowed.  Give `CONFIRMED`, `REJECTED`, or `INCONCLUSIVE`; identify the smallest
failing identity or missing certificate; give the exact promotable sentence
and strict scope.  Do not promote beyond this normalized double-B leaf to all
`(9,12)`, maximum twelve, a counterexample, or JC2.
