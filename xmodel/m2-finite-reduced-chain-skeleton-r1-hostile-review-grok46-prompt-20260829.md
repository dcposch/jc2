# Independent hostile review: finite reduced P0 chain skeleton

You are Grok 4.6.  Independently falsify or verify Sol's cap-free theorem for
the reduced P0 chain layer.  This is narrower than the general `(w,M)`
budget quotient you already falsified; do not transfer either verdict by
analogy.

Read in full:

- `/Users/dc/code/math/jc2/xmodel/m2-finite-reduced-chain-skeleton-sol56-20260829.md`
  (current full SHA-256
  `239393d7747b6166544342100cfe56b9353860fc7f36cd31620f8fdd04299bad`,
  body `8587625b2f12e486f9a3a3773ee5f4dcac7f853edcaddf69221dbab9ea7b1bcb`);
- `/Users/dc/code/math/jc2/cases/m2_finite_reduced_chain_skeleton_r1_20260829/`
  in full, whose principal hashes are:
  `finite_chain_skeleton_r1.py` =
  `6e413ff68a0b75f6a7fe28e091f1989b5cb74ed5f2d0f123630cb7520add8218`,
  `test_finite_chain_skeleton_r1.py` =
  `cd80757dd068c2af6bc1d0c2e15575e7a696224664dffa9645fc877c144ac38e`,
  `td7_caseiii_special_nu_r1.py` =
  `f064e0930dc11d05c7276fa0420418ecf1efc62eed9a9b10a69bc626b88fa558`,
  and its test =
  `f4cfa83df42cd38975482160848bc35146f8c26a5c66a7f5b5190638201ab7a8`;
- the exact P0/R1/R2 sources cited by the report, especially the current
  `BOOK-OFFAXIS.md`, `DEPTH.md`, `MULTIPOLE.md`, and your earlier
  `/Users/dc/code/math/jc2/xmodel/m2-budget-quotient-falsifier-grok46-20260829.md`.

Do not access, list, search, build, status, or control `jc2-lean`.  Do not run
`git status` or another workspace-wide command.  No web, AWS, local Singular,
msolve, Sage, PARI, or heavy computation; no canonical edits; no commit/push.
Bounded exact-rational Python and source mutations are allowed.  Do not modify
the packet or producer report.

Write only
`/Users/dc/code/math/jc2/xmodel/m2-finite-reduced-chain-skeleton-r1-hostile-review-grok46-20260829.md`.

Mandatory charges:

1. Re-derive the cap-free finiteness argument from the literal P0 laws.  Check
   separately `eps>0` and `eps=0`, every sign/strict inequality, the claimed
   bounds on `ell`, `nu`, `M`, `num(w)`, and whether zero-cost/neutral moves,
   case-III arrivals, or unpriced lex can enter the theorem's declared chain
   layer.  Give a concrete counterchain if any state variable can grow at
   fixed charged budget.
2. Audit the implementation against that mathematical state space.  Search
   for a hidden cap, omitted branch, cached-versus-derived invariant,
   rational normalization collision, or permissive assertion.  Run normal
   and `python -O` tests and write independent exhaustive checks at the
   smallest budgets, including mutations designed to create an infinite or
   silently omitted successor.
3. Independently reproduce or refute the charged `(w,M)=(3/2,2), B=5`
   result: 69 states, 295 edges, maxima, state hash, exact equality with the
   legacy `close_p` map, and the conclusion that the canonical old count 70
   is stale.  Distinguish a duplicate representation from a missing state.
4. Re-derive the special td-7 case-III neutral-ray equation and its domain.
   Decide whether `g*((3h-4)l-2)=3h` follows from the actual handshake and
   P0 laws, and whether `h=3,l=1,g=3` is the unique odd solution while every
   odd `h>=5` is empty.  Check that this result is not silently generalized
   to other chain states or merge types.
5. Compare the exact theorem with your earlier general falsifier.  State
   precisely which objection is repaired (if any), which survives at merges,
   and whether the theorem can safely replace only the old claim that the
   reduced P0 chain numerator/`M` is unbounded at fixed budget.
6. Report all findings in severity order with exact source locations and
   minimal reproducers.  Scope any PASS as conditional on the imported P0
   sheet laws; do not infer landing completeness, merge finiteness, a global
   topological-degree bound, or JC2.

Allowed verdicts: `PASS_AT_STATED_CHAIN_SCOPE`, `REPAIR_REQUIRED`, or
`REJECT`.  End with a body self-hash and full-report hash instructions.
