# Different-model hostile review: td=8 trunk exit-set charge

Act as Opus 5, independently and adversarially. Work only in
`/Users/dc/code/math/jc2`. Never access, list, search, build, status, or
control `jc2-lean`. Do not use web or AWS. Do not edit canonical files,
source packets, prompts, adapters, or the target. Do not commit or push.
Short exact desk checks are allowed; no heavy local computation.

Review this target:

- `xmodel/m2-td8-trunk-exact-charge-r1-sol56-20260829.md`
- expected full SHA-256
  `3c2c9a7ed79cc6d05ec3ba7098c1dc89cabb3547791d777c4bf8971d1ae28e39`
- expected body SHA-256
  `688dbf41e3e3b6c777ec7267c8114569c4507261eb6dea9003dc6236c330494c`

Verify the hashes first. Reconstruct the claim from the printed source and
the target's hash-pinned reviewed dependencies, especially your own exact
separation primary, Fable's review, the corrected Section-9 pricing law,
the selected/global first-exit repair, and actual-weight Corollary 7.1.
Do not defer to the target or to prior campaign summaries.

The central alleged regression is that the old trunk criterion computed one
selected ray's weight and then consumed it as the total exit-set charge.
Attack every point needed to decide whether the repaired total really is
always at least three:

1. For the trunk root direction of multiplicity `2i`, does Statement 7.3
   supply a critical-value flag for every Puiseux series/ray in the group?
   If the group splits later, are the resulting flags necessarily distinct
   (no remerging), and can their actual weights all be used simultaneously?
2. Does corrected Statement 9.3 give each such descendant flag the same
   lower bound `17i/(2i)-7=3/2`, hence integral weight at least two? Check
   all direction-orbit, cyclic-quotient, same-fibre, and multiplicity typing.
3. Is it legitimate to call the sum a stronger trunk first-exit charge? If
   local ownership would attach later flags to later vertices, decide
   whether direct application of actual-weight Corollary 7.1 to the distinct
   flags nevertheless proves the same route contradiction without that
   terminology. Explicitly test the quotient/orbit attachment caveat in the
   global first-exit hostile review.
4. In the single-flag case, does uniqueness force the entire `2i` group to
   remain unsplit through the cv level? Does the area identity then force
   `tau_0=17/2`? Is `kappa_H/kappa_F` a positive integer, and does integrality
   of `kappa_H(pi(H)-1)=3q/2` force even `q` and weight at least three?
5. Re-evaluate the old proposed `tau=8`, `2i -> i` profile. Does it really
   create at least two distinct cv flags with total at least four, or can a
   valid identification/selection make its total two?
6. Check that the two A-exit witnesses, every selected trunk witness, and
   the x-side unit are pairwise distinct on one fibre, and that the reviewed
   actual-weight bound is exactly `td-1=7`. Determine whether
   `2+2+3+1=8` genuinely excludes the whole affine family uniformly in `t`.
7. Enforce the perimeter: this may kill one reviewed formal route, but not
   all td=8 configurations, a degree range, a counterexample, or JC2.

Return `PASS`, `PASS_WITH_REPAIR`, `REPAIR_REQUIRED`, or `FAIL` at claim
level. Separate theorem truth from terminology/consumer repairs. State the
maximum safe consequence and the next campaign implication.

Write only
`xmodel/m2-td8-trunk-exact-charge-r1-hostile-review-opus5-20260829.md`,
including full provenance, clause-level findings, and a body SHA-256 footer.
Your final CLI response should contain only the concise verdict, output path,
and seals.
