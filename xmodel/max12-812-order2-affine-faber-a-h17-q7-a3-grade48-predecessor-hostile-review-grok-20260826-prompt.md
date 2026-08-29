# Hostile review assignment: affine-Faber `A`, H17/q7/a3 predecessor

Work in `/Users/dc/code/math/jc2`.  Produce an independent hostile review at
exactly

```text
xmodel/max12-812-order2-affine-faber-a-h17-q7-a3-grade48-predecessor-hostile-review-grok-20260826.md
```

Do not edit any charged artifact, producer, shared top-level ledger, or
`jc2-lean`.  Recompute every SHA-256 pin.  Exact Q is mathematical evidence;
F65521 is only a software/collection control.  Do not infer validity from
PASS prose.

## Charged custody

```text
6e6e5cf16b6b99400ee92e610966d99b70bae46fa6719ad94e9804ec28bef6b8
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_predecessor_g48_sparse_v4_20260826/RESULT.md
051b9cfc18910e40da63da9ce5115397775f6ce9fdb34065da6bfd3359184f85
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_predecessor_g48_sparse_v4_20260826/EVIDENCE.sha256
1bd52a1b6074537d11693ba9bd5d0589ead68f7a9d037f21e4c2a20edbf78713
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_predecessor_g48_sparse_v4_20260826/FREEZE.sha256
d9f95300ed1a6d91ce5239263b3bd4628606b987ba3e5f13cdefe72181ea0db4
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_predecessor_g48_sparse_v4_20260826/RESULTS.sha256
39632462be45678e3d7d94ab03e9836a121bd281dcbfed3aed3d2078fa006896
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_predecessor_g48_sparse_v4_20260826/evidence/Box03/aws_qcheck/output/grade48_rows.json
064de62d5158224bfbca7f68d3383eb26b2986949997cdf93942846876b1abf8
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_predecessor_g48_sparse_v4_20260826/evidence/Box02/aws_pcheck/output/grade48_rows.json
9758ca40336c36b5b268b1d91ab57df767cd4b3b53eb8b00934d07d581d1463e
  cases/max12_812_order2_affine_faber_a_h17_q7_a3_predecessor_g48_sparse_v4_20260826/check_h17_q7_g48_v4.py
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
```

V2 is a deliberate failed-closed negative: it omitted the center/load terms
and must not be treated as evidence.  V3 only emitted the complete block.
The broad ordinary-Singular V1 timed out and has no verdict.  V4 is the
controlling sparse exact replay.

## Required attacks

1. Reconstruct all seven complete abstract rows independently from frozen
   `tails.json` and the two-sided normalized affine coordinate substitution.
   Check the H17 weights `lambda=17`, `X=Y=7`, complements `=14`, `a=3`,
   loads `=42`, deviations/`mu4=48`, and targets `mu6=54,J=57`.  Verify no
   monomial or target reaches below grade 48 after graph cancellation.
2. Independently recover all 26 exact-Q grade-48 terms and coefficients.
   In particular attack the new terms
   `+15*kk*a^2*p^5/128` in row 2 and
   `-15*kk*a^2*p^7/1024` in row 6.  Check that arbitrary positive-excess
   center, `E`, `M`, and `K10` jets cannot add another grade-48 term.
3. Check the finite-field file only by coefficient reduction/support.  Do
   not use it to prove the Q formulas.  Audit that the custom sparse engine
   uses ordinary exact dictionaries, not Singular quotient-ring equality.
4. Re-derive the odd redundancies
   `C5=(3p^2/32)C1-(p/4)C3` and
   `C7=(p^2/32)C3-(p^3/64)C1`.  On `D(p*m)`, eliminate the grade-48 block
   by hand and confirm or refute the displayed formulas for
   `s0,xy,d2,dm,d4` in `RESULT.md`.
5. Replay both unit-center projective witnesses with `p=m=a=kk=1`.  Decide
   whether the correct endpoint is genuinely SURVIVES rather than a hidden
   unit.  Check the row-4 omission negative.
6. Audit scope.  The strongest licensed statement is a fixed integral
   `(H,q,alpha)=(17,7,3)` normalized-graph predecessor on `D(p*m)`.  It is
   not grade-51 closure, rational-regrading, literal-source/total-Rees,
   order-two, max12, or JC2 coverage.  The grade-51 Kummer tie in RESULT is
   navigation only and must not be silently promoted.

## Verdict format

Start with a table of charged pins, recomputed hashes, reviewer/model,
smallest failed identity or missing hypothesis, and overall verdict
`CONFIRMED`, `REPAIR`, or `REFUTED`.  Give enough independent exact algebra
to audit every row and elimination.  End with the verdict token alone.
