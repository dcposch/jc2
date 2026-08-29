# Hostile review prompt: K00 unloaded global nonmembership versus filtered D7 compatibility

Date: 2026-08-27

Act as an adversarial algebraic-geometry/CAS reviewer.  Do not edit canonical
ledgers.  Independently reconstruct the mathematics from the frozen source
bytes; do not infer correctness from producer status strings.

## Claims under review

1. V8 claims exact global nonmembership

   ```text
   r7 not in (r1,...,r6) over Q[C6,C6^-1,d0,...,d5].
   ```

2. V9 claims that at the normalized generic K00 germ, the complete filtered
   Macaulay system is nevertheless compatible through transverse degree 7,
   with cumulative ranks

   ```text
   D2 4, D3 28, D4 106, D5 294, D6 676, D7 1372
   ```

   and equal augmented ranks at every cutoff.

These statements are not contradictory: global polynomial ideal
nonmembership does not identify the first filtered/local obstruction, and a
global `dp` remainder's lowest displayed degree is not invariant.

## Charged sources and artifacts

- frozen tails:
  `cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json`,
  SHA `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`;
- one-parameter theorem:
  `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md`,
  SHA `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b`;
- V6 quadratic replay:
  `cases/max12_812_order2_u2_62_k00_normal_quadratic_v6_20260827/RESULT.md`;
- V8 producer/result/evidence:
  `cases/max12_812_order2_u2_62_k00_unloaded_membership_v8_20260827/`;
- V9 producer/result/evidence:
  `cases/max12_812_order2_u2_62_k00_filtered_macaulay_v9_20260827/`.

## Mandatory review tasks

1. History/type-check the frozen tail schema and verify affine linearity in
   `k10,k6,k2`.  Keep terminal Jacobian `Jdet` distinct from collision ideals
   `J1,J2`; V8/V9 are unloaded coefficient tests and make no Jacobian
   elimination.
2. Reconstruct all seven unloaded rows after

   ```text
   C5=d5, C4=(3*C6^2+d4)/8, C3=d3,
   C2=(C6^3+d2)/16, C1=d1, C0=(C6^4+d0)/256.
   ```

   Verify constants and linear normal pieces vanish.
3. Independently test the direct `D(C6)` ideal membership, preferably by a
   fresh exact CAS script or a saved-basis/remainder replay.  Confirm that
   adjoining `1-t*C6` is the localization and that the standard basis is
   proper.  Audit the normalized Kummer argument and independently reproduce
   the `C6=1` result.
4. Confirm V8 has no diagnostic, that V7's unsupported `exit(0)` runs were
   correctly rejected, and that V8 uses plain `quit;` plus external failure
   markers.  Verify the saved residual and basis hashes.
5. Explicitly reject both V8 raw remainder degrees as canonical obstruction
   degrees.  Recheck

   ```text
   Q7=-(1/512)Q1-(1/128)Q3
   ```

   and explain why the normalized global remainder may still display a
   degree-2 term.
6. Independently construct the cumulative filtered Macaulay maps.  Include
   all constant syzygies, all later syzygies, and every multiplier monomial
   through degree `D-2`; do not test row pieces degreewise without compatible
   lifts.  Reproduce the D2--D7 matrix shapes, ranks, and augmented ranks.
7. Replay the exact D7 multiplier file coefficientwise against the freshly
   expanded rows.  Check the D7 matrix SHA
   `1a094f16...3473` and lift SHA `2fe2b6bc...d71db`.  Confirm the result is
   representation-independent because the full cumulative map, rather than
   one chosen quadratic correction, is used.
8. Independently audit the load-normal stencil.  Determine whether its stated
   minimal degrees are correct and whether they are sufficient only as input
   to, not a substitute for, the pending `Lambda^19` mixed reachability test.
9. Search for denominator loss, bad Kummer descent, row/column ordering bugs,
   truncated terms, characteristic leakage, a false rank replay, or an
   unjustified passage from finite compatibility to formal/local membership.

Return a line-item verdict: `PASS`, `REPAIRABLE`, or `FAIL`, with exact file
and equation citations.  State the strongest theorem the evidence supports
and the next unresolved obligation.  Do not promote an order-two, maximum-
twelve, or JC2 conclusion.

Write the complete report to exactly
`xmodel/max12-812-order2-k00-v8-v9-hostile-review-grok-20260827.md`.
Touch no other campaign artifact. Do not enter, read, build, status-inspect,
or modify `jc2-lean`. Desk-scale exact checks only; no heavy local CAS, no
AWS launch, no web sweep, and no canonical-ledger edits.
