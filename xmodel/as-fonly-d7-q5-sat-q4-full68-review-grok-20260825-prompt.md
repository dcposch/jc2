# Hostile review: AS F-only D7 full chronological Q4 gate

Audit only the frozen producer report and case:

- `xmodel/as-fonly-d7-q5-sat-q4-full68-producer-20260825.md`
- `cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825/`
- its pinned parent
  `cases/as_fonly_d7_q5_sat_full_q4_restore_20260825/replay_full_q4_restore.py`
  and that file's transitive source-pinned replay ancestry.

Return `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REJECTED`.  Hostile checks:

1. independently derive the orientation and constants in the five Q4 rows
   and the 63 terminal rows after adding coefficient-81 `(H5,J5)`;
2. check the exact 68-by-12 matrix extraction, RHS sign, RREF ranks,
   particulars, and kernel dimensions for all three models;
3. confirm that the complete 197-row parent replay precedes consumption;
4. check every exact division and verify that the literal Q4 modulus is 243
   while the terminal modulus is 729;
5. independently replay at least base0270, including the two-row omission
   negative control, and compare source/manifest/result hashes;
6. attack the claim that these are chronological Q4 lifts and the strict
   pointwise/refusal scope.  Do not silently promote to whole-fibre, lower
   rows, complete-map, all-depth, counterexample, or JC2 coverage.

Write the review to
`xmodel/as-fonly-d7-q5-sat-q4-full68-review-grok-20260825.md` and record all
consumed hashes and any independent replay custody.
