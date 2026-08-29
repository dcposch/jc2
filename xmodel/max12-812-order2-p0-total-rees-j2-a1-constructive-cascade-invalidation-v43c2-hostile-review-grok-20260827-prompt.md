# Hostile review task: V43C1/C2 crossed-assumption invalidation

Work in `/Users/dc/code/math/jc2`.  Independently and adversarially review the
negative result in:

- `cases/max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_v43c2_20260827/INVALIDATION.md`
  (SHA-256 `dbea733345b2a707ee5834b90889eca6b41013b6694786317f54362e97d96b89`),
- its freeze manifest (SHA-256
  `10217738bc86e415050b667f226907b891bf2bb8e94e6f331fad8939bc562abe`),
- the v3 resource-cap and v4 exact-failure artifacts in that case, and
- `xmodel/max12-812-order2-p0-total-rees-j2-a1-constructive-cascade-invalidation-v43c2-sol-20260827.md`
  (SHA-256 `59d1e39c5abc1c1afd68bdc71cac8ff12654dc95e48aeb3ed1516cc4e4d64b1c`).

Charge all of the following independently:

1. Rehash every pinned artifact and audit source/row custody.
2. Check the exact semantics of DAG nodes 170, 619, and 642 from the frozen
   producer.  Confirm or refute the reported 24,429-term nonzero expansion of
   node170 and its hash.
3. Derive the exponent-three `ClearPower` geometric factor and verify that
   node619 is `K=a1^36+a1^18*m*ell1+(m*ell1)^2`; check the decisive
   specialization `K|ell1=0=a1^36`.
4. Decide whether the right a57 certificate truly retains a nonzero old
   `assume:e1` multiplier and therefore cannot enter the strict final
   `CombineBranches(e1,G)` rule.
5. Audit scope: this must invalidate only the uncorrected explicit `M=104`
   derivation and its conditional `628` converter, not V42 radical closure or
   V43G4's exact `5*t^6*a1^4` identity.
6. Independently check the proposed repair identity
   `e1=G+4*a1*ell1`, `ee0=Q0-4*aa0*ell1` and the resulting multiplier update
   `c_ell -> c_ell+4*a1*c_e1-4*aa0*c_ee0`.  Treat it only as a prospective
   repair, not as a proved certificate.
7. Look for any alternative explanation (wrong node isolation, zero divisor,
   sign convention, stale source, compiler artifact, or rule bug) that would
   defeat the negative result.

Write exactly one report and no other file:

`xmodel/max12-812-order2-p0-total-rees-j2-a1-constructive-cascade-invalidation-v43c2-hostile-review-grok-20260827.md`

End with one verdict token:
`GROK_CONFIRMED_INVALIDATION`, `GROK_REVIEW_REPAIR`, or
`GROK_REVIEW_REFUTED`.

