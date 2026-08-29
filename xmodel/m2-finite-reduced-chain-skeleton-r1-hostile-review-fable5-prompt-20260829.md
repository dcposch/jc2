# Hostile review: finite reduced P0 chain skeleton R1

You are Fable 5 at maximum reasoning, acting as a different-model adversarial
mathematics and source referee.  Review the provisional Sol-ultra theorem and
packet:

- `/Users/dc/code/math/jc2/xmodel/m2-finite-reduced-chain-skeleton-sol56-20260829.md`
  (full-file hash must be recomputed; body hash claimed
  `8587625b2f12e486f9a3a3773ee5f4dcac7f853edcaddf69221dbab9ea7b1bcb`);
- `/Users/dc/code/math/jc2/cases/m2_finite_reduced_chain_skeleton_r1_20260829/`;
- `ladder/BOOK-OFFAXIS.md` section 10 P0--P5 only;
- `ladder/REDUCTION.md` CRITICAL 4--7 and section 5.2 only;
- `ladder/SHEET6-DEPTH.md` only where P0/R1.2 or the neutral-ray laws are
  directly cited.

Do not read other ideation reports.  Do not access, list, search, build,
status, or control `jc2-lean`.  Do not run `git status` or workspace-wide
commands.  No web, AWS, Singular, PARI, msolve, Sage, or heavy CAS; no
canonical edits, commit, or push.  Bounded stdlib Python replay and private
temporary mutations are allowed.

Audit these points independently:

1. Prove or break finite reduced `(w,M)` closure at fixed entry/budget.  In
   particular, decide whether any zero-lambda P0 family outside the modeled
   clean neutral/resonant moves can increase reduced numerator or `M`, and
   whether “every non-clean step costs >=1” is actually justified when
   q-extras cost zero.
2. Re-derive both dirty `lex` bounds from `C,T,E`; check denominator factors,
   divisibility direction, `nu>=2`, `k/Sm` ranges, and whether the code omits
   any legal epsilon/k/lex family or silently assumes a global cap.
3. Audit the pure-epsilon congruence quotient exactly: `kbar` integrality,
   `M'=gcd(l-eps,nu+1)`, existence of `nu>=2`, and residue modulus.
4. Replay ordinary and optimized tests, independently compare the charged
   69-state/minimum-cost map to current `book_offaxis.close_p(3/2,2,5)`, and
   use mutations to try to make a legal step disappear or an illegal one
   enter.  Treat matching a capped legacy engine as corroboration, not proof.
5. Re-derive the special-nu case-III equation and its unique solution.  Check
   that the stated partner/shape scope matches P3 and that no legal `l=0`,
   `nu_G=1`, or alternative shape was silently included/excluded.
6. Decide precisely what part of P5/CRITICAL 5 is corrected.  Keep unbounded
   last `nu`, `kbar`, full degree, merge q-extra families, partner-dependent
   legality, full landing, ceiling, and JC2 outside any promotion.

Return `PASS`, `PASS_WITH_NARROWING`, `REPAIR_REQUIRED`, or `REJECT`, with an
exact statement safe to promote, all counterexamples/repairs, replay hashes,
and the cheapest next generic-AP discriminator.  Write only
`/Users/dc/code/math/jc2/xmodel/m2-finite-reduced-chain-skeleton-r1-hostile-review-fable5-20260829.md`
and end with a report-body self-hash.
