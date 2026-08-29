# Different-model hostile review: td=12 exact first-trunk charge

Act as Fable 5, independently and adversarially. Work only in
`/Users/dc/code/math/jc2`. Never access, list, search, build, status, or
control `jc2-lean`. Do not use web or AWS. Do not edit canonical files,
source packets, prompts, adapters, or the target. Do not commit or push.
Short exact desk checks are allowed; no heavy local computation.

Review this target:

- `xmodel/m2-td12-u1-next-trunk-discriminator-r1-sol56-20260829.md`
- expected full SHA-256
  `2a151eef1e661464ada47b0e387051733f9c2cb39cc7893366f5b1e09e15e829`
- expected body SHA-256
  `b25217e9b733efcc28d263c9df057d6ebcac61976002dd1c815e8063591caaae`

Verify hashes first and rebuild the mathematics from the printed source and
hash-pinned reviewed dependencies. The producer alleges that the td=12 U1
first-trunk B-direction has exact first-exit charge 8 (not `{8,9}`), and
that its next source gate is 24 successive pure-power child levels.

Charge every load-bearing point:

1. Recompute the pinned row, including `i_G=2`, `i=6n`, `D_F=25i`,
   `kbar_F=17`, B-root multiplicity `i`, AF2 gap 8, and `psi=2`. Separate
   what is needed for exact charge from direct-entry-specific sheet counts.
2. Does every ray through the nearrow B-direction remain finite and acquire
   a unique critical-value flag? If sheets split before the cv level, must
   there be at least two distinct flags, with no quotient/orbit or same-fibre
   identification loophole?
3. Does corrected Statement 9.3 give each such flag actual weight at least
   8? Does actual-weight Corollary 7.1 directly rule out two flags at td=12,
   independent of first-exit ownership conventions?
4. If there is one flag, does non-remerging force `N(tau)=i` throughout,
   hence `tau_0=25`? Is `kappa_H/kappa_F` a positive integer, and does the
   td12 budget force it to 1, giving exact charge 8 and excluding 9?
5. Check the endpoint and indexing claim: are child polynomials necessarily
   pure i-th powers at normalized levels 1 through 24, with a split allowed
   exactly at 25? Verify the first gcd/binomial criterion and whether the
   source's kappa grading introduces skipped or fractional levels.
6. Audit the A/B interpolation and residue/degree calculation. Decide only
   whether it proves formal top/weight/arrival compatibility; do not upgrade
   it to Keller-pair realization or a global source jet.
7. State the maximum safe consequence for the two reviewed P1-fitting td12
   terminals, and enforce the no-overclaim perimeter: no landing, full-book
   exclusion, counterexample, or JC2 conclusion.

Try to construct a charge-9 or early-split counterexample within the reviewed
grammar. Return `PASS`, `PASS_WITH_REPAIR`, `REPAIR_REQUIRED`, or `FAIL`,
with clause-level findings and the smallest remaining source datum.

Write only
`xmodel/m2-td12-u1-next-trunk-discriminator-r1-hostile-review-fable5-20260829.md`,
including full provenance and a body SHA-256 footer. Your final CLI response
must be only the concise verdict, report path, and seals.
