# Hostile review: global fresh elimination and 176-coordinate Kuranishi map

Write the verdict to
`xmodel/as-b9-9-12-common-cubic-global-fresh-elimination-review-grok-20260825.md`.
Do not mutate producer files.  Do not run substantive computation locally;
any independent replay must be staged on AWS and its exact custody recorded.

Audit the following exact, provisional producer claim.

1. Read the reviewed parent family source and frozen inputs:
   - `cases/as_b9_9_12_common_cubic_3p11_20260825/INDEPENDENT_AUDIT_BOX02/independent_common_core.py`
   - `cases/as_b9_9_12_common_cubic_global_row22_20260825/AWS_BOX02_V1/global_row22_v1.py`
   - `cases/as_b9_9_12_common_cubic_global_row22_20260825/compile_fresh_block.py`
   - `cases/as_b9_9_12_common_cubic_global_row22_20260825/AWS_BOX02_FRESH_BLOCK/result.json`
   - `cases/as_b9_9_12_common_cubic_global_row22_20260825/AWS_BOX02_FRESH_BLOCK/fresh_block.json.gz`
   Verify every pinned SHA and the complete-family dimensions
   `17 active + 78 spectator + 55 final fresh`.

2. Check the source/valuation proof that the next `205 x 55` fresh block is
   independent of all 95 predecessor parameters: predecessor changes begin
   at output order `3^5`, final fresh-kernel changes at output order `3^10`,
   and all predecessor/fresh cross terms vanish after division by `3^11`
   modulo 3.  Check determinant and common-core rows, not determinant alone.
   Independently verify rank 29, fresh kernel 26, and canonical left quotient
   176.  The 447 sampled rank-29/UNSAT points are diagnostics only and must
   not be used as the constancy or global-exclusion proof.

3. Audit
   `cases/as_b9_9_12_common_cubic_global_row22_20260825/emit_kuranishi_map.py`
   line by line against the original integer `residual` source.  In
   particular charge:
   - exact RREF transforms and the canonical `17+78` predecessor chart;
   - all 276 determinant plus 23 common-cubic rows;
   - signs and chronological divisors `3^10`, `3^11`;
   - the use of arithmetic modulo `3^12=531441`;
   - sufficient widening before every modular add/multiply and absence of
     modulus-as-zero or overflow bugs;
   - exact composition of the `205` next cokernel with the `176` fresh left
     quotient;
   - why setting the 55 final fresh-kernel coordinates to zero is licensed
     only after applying that quotient;
   - embedded source-row/divisibility controls and strict 95-parameter scope.

4. Inspect the AWS row-block metadata after it is materialized.  Require the
   same pinned source/quotient hashes on Box02, Box03, and r6d, exact coverage
   of rows 0..175, matching overlaps 30--31, 60--61, 90--91, 120--121,
   150--151, and the common all-coordinate structural hash
   `557123112e5c3e4ea5d3a5a95709d816254080e0eeef2d995d028013db468b48`.
   The aggregate full-formula SHA should be
   `108cfdaae0c897ab66518e18d5e38d0969a1f8f936eeb488fd9144e4fbfe0f4c`.

5. Keep solver and source claims separate.  A SAT model is not accepted until
   the original integer evaluator reconstructs the eliminated fresh fibre,
   solves the new 149-digit system, and replays all 299 rows modulo `3^12`.
   An UNSAT solver return is not promoted without an independently checked
   proof/certificate.  Do not infer all-depth lifting, nonexistence,
   maximum-12, a counterexample, or JC2 from this finite chart.

Return `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REJECTED`, list every exact
defect or missing premise, and state the strongest theorem licensed even if
the full producer wording is too broad.
