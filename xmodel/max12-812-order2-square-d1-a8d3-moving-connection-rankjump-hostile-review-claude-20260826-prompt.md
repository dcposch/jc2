# Hostile review charge: D1 a=8,d=3 moving-connection rank jump

You are an independent hostile reviewer.  Read the repository evidence and
write exactly one report:

`xmodel/max12-812-order2-square-d1-a8d3-moving-connection-rankjump-hostile-review-claude-20260826.md`

Do not edit any producer, ledger, prompt, source, or other file.  Do not
launch computation.  End the report with one standalone verdict:
`CONFIRMED`, `CONDITIONAL`, or `REJECTED`.

## Primary frozen custody

- `cases/max12_812_order2_square_owner_d1_a8d3_k6rc_isolated_bridge_20260826/RESULT.md`
  SHA-256 `64f731aa4a518b467d2b60489643178c2e6f0c069b7f9c0a568ae685f9378ba2`
- its `DIAGNOSTIC_FREEZE.sha256`
  SHA-256 `84262c311e3a7944ba945df630bfb254a0d838a9c0065098295835cb64db80ab`
- `cases/max12_812_order2_square_owner_d1_a8d3_connection_rankjump_20260826/RESULT.md`
  SHA-256 `2c422f36cecec94e870c1bab4767d3dc61b689f100fc583ad3509a2a176f90bc`
- its `EVIDENCE.sha256` SHA-256
  `0b63361de1f29c16eba1ce28e22c81a4febc7560ed4f97395c985f45622dca3d`
- its `PRODUCER_FREEZE.sha256` SHA-256
  `a28e20033d4e0d5cd8fd3303a371d802147db65875cace445904a48f9f4fc83e`
- complete frozen source inventory
  `cases/max12_812_order2_square_owner_d1_d23_a8a9_j38_r3_tail_20260826/aws_v2_failed_a8d3_q_box02_highmem/evidence/compiled/source_inventory.json`
  SHA-256 `de195a2a005c32a53c3802dc1ee5f8429bb94a7337543d4f1419be5ad4c14cf6`

## Required hostile checks

1. Rehash every cited freeze/evidence entry, nested AWS result, stdout,
   stderr, and validator.  Check exact Q plus both distinct primes, engine
   rc, zero swap, and archive identity.
2. Independently derive the moving-inverse-root correction.  Starting with
   `f0=L^4`, `delta_R f=2L^2R`, `delta_C f=C`, and exponent `3/4`, decide
   whether

   `q_RC+(partial_z q_C)z_R=-(3/16)R C'/(zL^2)`

   is exact, including signs, factors, and the translation to rows 4,5,7.
   Decide whether this vindicates the canonical literal tails and falsifies
   only the fixed-z bridge.
3. Independently extract the family-15 `k6A^2` cross column from the frozen
   inventory.  Audit why it has no analogous inverse-root correction at
   this order (`q_A` has no negative part).  Verify rows 5,7 are
   `(-3/16,+3p/64)`.
4. Verify corrected `k6RC` rows 5,7 are
   `(-3/16,-3p/64)`, the two forced alpha values are `+1/4,-1/4`, the
   determinant is `9p/512`, and

   `e7=(32/(3p))*col(k6A^2)-(32/(3p))*col(k6RC)`.

5. Charge scope aggressively.  Confirm that this proves only failure of a
   normalized coefficientwise universal odd functional on `D(p)`.  It must
   not be called an a=8,d=3 cell verdict, a nonlinear solution, a point, or
   an existence/counterexample result.  State the legitimate next gate:
   saturation/chamber splitting by the two source products in the complete
   earlier zero locus.
6. Audit the recent Singular qring noncanonical-assignment hazard.  State
   whether any conclusion here depends on qring `==0`, `subst`, or `diff`
   without explicit reduction.  Do not import unrelated campaign results.

If any formula, hash, source identity, or firewall fails, identify the
smallest exact defect and reject or condition accordingly.
