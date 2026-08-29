# Hostile theorem review: D43 coefficient algebra K0

You are Grok 4.6 acting as a different-model mathematical referee.  Review
Opus 5's K0 theorem from first principles; do not trust its executed-output
claims or the coordinator's favorable reading.

Do not access `jc2-lean`, launch AWS, or run a heavy/local CAS job.  Bounded
stdlib exact arithmetic and direct source inspection are authorized.  Write
only the final report named below.

## Charged report and source

- `xmodel/d43-k0-splitting-primary-research-opus5-20260828.md`, SHA-256
  `6d3d53c20387d324766daaf40eb502df42d9e2776c6ab6053041bc1f3dee1430`.
- `cases/d43_common_integral_emitter.py`, source hash stated in the charged
  report; independently recompute it and verify the displayed relations are
  literal.
- The displayed E polynomial is a conditional input from
  `xmodel/d43-e5-e6-elimination-bridge-gpt56-20260828.md`; verify its hash and
  exact formula before reviewing the conditional q0 claim.

## Required attacks

Give separate `CONFIRMED`, `REPAIR`, or `REFUTED` verdicts for:

1. free rank 432 of the quotient and free rank 48 of its pre-cubic base;
2. the explicit isomorphism `B = Q(zeta_168)`, including both map directions,
   generator recovery, exact degree, and every cyclotomic exponent identity;
3. the abelian-descent lemma for cubes and/or an independent proof that the
   two classes `[3+sqrt3]`, `[3-sqrt3]` span `(Z/3)^2`; recompute the cubic
   characters at 673 and at a second prime, and attack every hidden
   denominator/specialization assumption;
4. the conclusion that K0 is one field of degree 432, Galois but nonabelian,
   with idempotents only 0 and 1;
5. finite etaleness of the stated `Z[1/42]` model and the exact ramified
   rational-prime set `{2,3,7}` (especially whether a nonmaximal-order or
   Kummer-layer subtlety invalidates the argument, and why 5 is absent);
6. both registered frames, complete splitting/count 432, and the claimed
   uniqueness of the registered p^2 lift;
7. conditional on the literal E formula, the identities
   `u^3=2-sqrt3`, `c=-u^10`,
   `q0=u*(1+i)*(sqrt3-1)/2`, `q0^4=c`, the four distinct K0-rational
   branches, the four-term normal form, and both pointbank regressions;
8. every proposed solve-graph consequence: what component splitting can be
   deleted, when a nonzero normal form may be inverted, whether the five
   coefficient relations form a maximal ideal, and what Fitting/chart/claim
   obligations remain.

Do not count modular frame totals as a proof of fieldness.  Try to construct
a product-algebra countermodel, a missed Kummer relation, a faulty Galois
stability argument, a ramification counterexample, and a sign/branch error in
q0.  Distinguish the theorem, conditional E theorem, evidence, and unexecuted
GP recipe exactly as the charge does.

Write only:

`xmodel/d43-k0-field-theorem-hostile-review-grok46-20260829.md`

Seal the report with SHA-256.  State the maximum promotion allowed and every
remaining artifact/replay debt.  No edits to canonical ledgers.
