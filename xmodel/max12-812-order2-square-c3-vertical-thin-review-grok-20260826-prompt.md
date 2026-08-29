# Hostile review: order-two generic-square vertical `c=3,r>=2` thin gate

You are the independent hostile reviewer.  Work read-only except for the
single report named below.  Do not run Singular, Sage, msolve, Lean, or any
heavy/exhaustive computation.  Do not run broad `git status` or inventory the
dirty worktree; inspect only the files named here and their explicitly pinned
transitive sources.  Recompute the small rational identities by hand or with
tiny textual checks only.  Stored PASS strings are evidence, never authority.

Write exactly one report:

`xmodel/max12-812-order2-square-c3-vertical-thin-review-grok-20260826.md`

## Frozen target

- producer report
  `cases/max12_812_order2_square_owner_c3_vertical_thin_20260826/RESULT.md`,
  SHA `c03ad20443cc24c1346e779d98172583bb9193beb89826d327e85f203d574557`;
- evidence manifest
  `cases/max12_812_order2_square_owner_c3_vertical_thin_20260826/RESULTS.sha256`,
  SHA `cb474217cfaef16773d296318973833edbbc133d4930bb74695f233719674551`;
- frozen source manifest SHA
  `a13d10fb845c1b5cafe249eb700af2e8dd49f3d847c9092478c7f121306fda24`;
- compiler SHA
  `3f4d3ecb050090755bf39b9f2fc740495613dce9de4bb69afc77cb4e9d28da70`;
- final design lemma
  `xmodel/max12-812-order2-square-c3-vertical-residue-lemma-20260826.md`,
  SHA `dd4005a92440e8241807bbe3bea4f9305de06c2d08fd0e095dc5dddba4bc7707`;
- exact-Q compiled input/output SHAs
  `ca1f0692893ba485e2407a6c3a49a397422abb075f97467da0923fdd4b682d29`,
  `af96bae652206831e66737c63c490f036fdea962c22c618467a5d04096dac62c`;
- `F_65521` compiled input/output SHAs
  `5b2a7a24ae0fea5fb016e603804779f985672f2556fdd40ec6ffa118d152cadf`,
  `feba24463e9443631b4d008cc6ed4819835457bc5b2d179ca1987b97ac529186`.

First verify all hashes and both `rc=0`/validator records from the manifest.
Read the actual compiler, exact-Q input/stdout, registration, report, and
design lemma.  Read transitive files only where the compiler/freeze points to
them and only as needed to audit source typing.

## Load-bearing questions

Give an explicit verdict on each item.

1. Does the frozen compiler really regenerate the complete seven source
   rows from the frozen shared-Faber tails, with the correct square first-
   normal substitutions, loads, target rows, and absolute grades 13--15?
   Detect any missing lower load, gauge, row, or denominator convention.
2. Independently recompute the displayed `H13,H14,H15` coefficients from
   the common Laurent receiver after `B1=0`, including every moving-`L`,
   moving-`p`, moving-`k`, `A`, `C`, `B2`, and `B3` correction that can
   reach grade 15.  Check every rational coefficient and sign.
3. Verify the three common-numerator bridge identities used by
   `SQUARE_C3_SOURCE_BRIDGE=1`; ensure they compare the actual source rows
   to the claimed rational coefficients rather than two copies of one
   analytic guess.
4. Prove, rather than trusting the hardcoded unit-diagonal print, that the
   seven zero source tails and the exact lower-unitriangular row transform
   force polynomiality of `H13,H14,H15`.  Charge the proper-fraction degree
   bounds and denominator recurrences explicitly.
5. On `D(p*k0)` with nonzero leading linear `A0,E3`, is the etale split
   `L=uv` faithfully flat, and does `L|A0E3` force exactly the two opposite
   root allocations used by the client?  Check descent and both deck charts.
6. Verify `D2`: after `L|A0E3`, reduction of `L^2 H14` modulo `L` is exactly
   `-(3/8)B2A0^2`.  On the complementary root, is the coefficient genuinely
   invertible on the stated chart, and does polynomiality force the claimed
   linear factor of `B2` for `r=2`?
7. Verify `D4`: after that factor constraint, reduce the complete
   `L^3 H15` modulo the complementary factor and show every connection/load
   term vanishes except `-(1/16)A0^3`.  Check the deck-conjugate computation.
8. Does independence from `B3` really cover every `r>=3` symbolically, and
   can any higher correction enter grades 13--15?  Check that `r=2` and
   `r>=3` exhaust precisely the advertised vertical family.
9. Audit the negative controls and the fact that exact Q, not the modular
   control, carries the characteristic-zero claim.
10. Audit the scope: this may give only an arcwise/set-theoretic exclusion
    of `a=0,c=3,r>=2` on `D(p*k0)`.  It must not claim scheme structure,
    fan exhaustion, horizontal contacts, `r=1`, `p=0`, `k0=0`, zero/infinity
    sections, the square stratum, order two, maximum twelve, or JC2.

Search for the smallest failing coefficient, identity, hypothesis, or scope
statement.  If any load-bearing point is missing, issue `REPAIR` or
`REFUTED`, quote the exact smallest obstruction, and do not rescue it by
assuming a result not present in the frozen chain.

End the report with exactly one final token:

- `ORDER2_SQUARE_C3_VERTICAL_CONFIRMED`
- `ORDER2_SQUARE_C3_VERTICAL_REPAIR`
- `ORDER2_SQUARE_C3_VERTICAL_REFUTED`
