# Independent hostile rereview: td=8 trunk exit-set charge

Act as Grok 4.6, independently and adversarially. Work only in
`/Users/dc/code/math/jc2`. Never access, list, search, build, status, or
control `jc2-lean`. Do not use web or AWS. Do not edit canonical files,
source packets, prompts, adapters, or the target. Do not commit or push.
Short exact desk checks are allowed; no heavy local computation.

Review exactly this target, independently of every other live reviewer:

- `xmodel/m2-td8-trunk-exact-charge-r1-sol56-20260829.md`
- expected full SHA-256
  `3c2c9a7ed79cc6d05ec3ba7098c1dc89cabb3547791d777c4bf8971d1ae28e39`
- expected body SHA-256
  `688dbf41e3e3b6c777ec7267c8114569c4507261eb6dea9003dc6236c330494c`

Verify hashes first. Reconstruct from the printed source and hash-pinned
reviewed dependencies, not from agreement. The alleged new theorem is that
the old trunk calculation was per-ray, while the actual first-exit set has
total weight at least three, killing the affine td8 route.

Charge all of the following:

1. Statement 7.3 existence and uniqueness of cv flags for every ray in the
   multiplicity-`2i` trunk direction; tree non-remerging after a split.
2. Corrected Statement 9.3 applied to every descendant flag, including
   cyclic-orbit, quotient, same-fibre, and full-multiplicity typing. Decide
   whether each flag indeed has weight at least `ceil(3/2)=2`.
3. First-separation ownership/additivity: test whether all later flags in
   that direction component belong to the trunk exit set. Also test the
   stronger fallback that actual-weight Corollary 7.1 may count them
   directly even if the local-charge terminology needs repair. Explicitly
   confront the quotient/orbit attachment caveat from the global first-exit
   review.
4. Single-flag case: does uniqueness imply `N(tau)=2i` until the cv level,
   hence `tau_0=17/2`? Is `q=kappa_H/kappa_F` integral, and does integral
   actual weight `3q/2` force `q>=2` even and total at least three?
5. Multi-flag case and the old `tau=8`, `2i->i` profile: does it cost at
   least four, or is there a legitimate way for distinct subgroups to share
   or discard a cv flag?
6. Global route budget: independently check pairwise distinctness of two
   A-exit flags, all selected trunk flags, and the x-side unit; check the
   exact `td-1=7` actual-weight ceiling and whether `2+2+3+1=8` excludes the
   entire affine family for every `t`.
7. Separate theorem truth from terminology/consumer repairs and from any
   broader td8, degree-ceiling, source-realization, counterexample, or JC2
   claim.

Return `PASS`, `PASS_WITH_REPAIR`, `REPAIR_REQUIRED`, or `FAIL`, with
claim-level findings, maximum safe consequence, and any precise countermodel.

Write only
`xmodel/m2-td8-trunk-exact-charge-r1-hostile-rereview-grok46-20260829.md`,
including full provenance and a body SHA-256 footer. Your final CLI response
must be only the concise verdict, report path, and seals.
