# Hostile review — squarefree Poisson recurrence rows 18–12

Review the producer report
`xmodel/max12-912-order1-squarefree-poisson-recurrence-rows18-12-aws-20260825.md`
(SHA-256 `c8504fdd510ccd638e4e2e0e76e849169f170113f54d619a2b77988e16ca723e`)
against aggregate freeze
`cases/max12_912_order1_binary_cubic_squarefree_poisson_recurrence_aws_20260825/FREEZE.sha256`
(SHA-256 `6bf8f555aa79e4a570cda877623b33269e2c6a5cbf309eb51a0b824e301913b2`).

Do not run Singular, Sage, a solver, a build, or substantial Python on the
local Mac.  Source reading, hashes, and short hand algebra are allowed.  Any
substantive independent replay must run on a registered AWS host and be
reported separately.

Charge all of the following:

1. Verify every aggregate and subcase manifest/freeze record and every
   `replay.py` conclusion.  Confirm dual-host agreement is same-source
   custody, not source independence.
2. Confirm V1/V2 and launcher-permission failures are quarantined and that no
   apparent marker from a parser-error run is consumed.
3. Starting from the original bracket rows, audit the degree-18 through
   degree-15 packages and the homogeneous centralizer calculation.  Check
   signs, factors 3, and every denominator.
4. Independently attack the degree-14 identity `E14=3K[K,Z10]`, the corrected
   target-shear term `(lambda/3)KB`, the old-formula negative control, and
   `729R=324CW`.
5. Audit the degree-13 rational denominator clearing and the direct collapsed
   polynomial row.  Check that `K|CW` plus the new rootwise condition really
   forces both `K|C` and `K|W` over every geometric point, and state the
   squarefree/reduced hypotheses.
6. Audit the degree-12 original-row clearing, the `3NR-AKL^3` factorization,
   and the eight root allocations.  Do not infer a nonreduced ideal equality.
7. Recompute all dimension counts and distinguish a parameterized reduced
   family from the full incidence scheme and its nilpotents/components.
8. Enforce the classical-closure firewall: strict total degrees `(9,12)` are
   counterexample-closed by the degree-gcd theorem.  Determine exactly what,
   if anything, transfers to weighted or partial-`y` unbounded-total models;
   require separate bracket-filtration and rational-centralizer hypotheses.
9. Attack the provisional formal-completion idea in
   `xmodel/sol-max12-912-squarefree-poisson-recurrence-20260825.md`, especially
   existence/uniqueness of `R=P^(1/3)`, completeness and degree filtration,
   the claim that the rational centralizer of `K=xy(x-y)` is `k(K)`, and the
   degree threshold needed to identify the nonnegative part of `Q`.  Keep
   this formal lemma separate from the producer-exact rows.

Write only
`xmodel/max12-912-order1-squarefree-poisson-recurrence-rows18-12-review-grok-20260825.md`
with verdict `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `NOT_CONFIRMED`, exact
files/hashes read, and the smallest scope-corrected statement for every
defect.  Do not edit producer or case bytes.
