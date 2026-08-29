# Independent hostile review: TD6 V89H4 high-q total-F K repair

Date: 2026-08-26

Review the frozen producer package
`cases/td6_c1_c2_c3_high_q_total_f_k_repair_v89h4_aws_20260826/`
skeptically and write exactly one report to
`xmodel/td6-v89h4-high-q-total-f-k-repair-hostile-review-20260826.md`.
Do not edit the producer, campaign ledgers, top-level files, or `jc2-lean`.

Pins:

- `RESULT.md` SHA256
  `8db237a7c466b420060623576b9d778427392fd827a3af856d276707dd618546`;
- `EVIDENCE.sha256` SHA256
  `70625a4460778bab5b14ae736b548c963952f5ce052819f6491928ef1a08340d`;
- `FREEZE.sha256` SHA256
  `3406db430e1a23bae2e3755f5dca3135773aced2af032c621ae1bbc0e28c3721`;
- source archive SHA256
  `84199204a41f7d26bcc6a1329cd72bedf2c60a0ae9590cf1cd04ee5373230d91`;
- exact result SHA256
  `d51b6cbc6beb807e8a220c0a097139f4e033d6135caf44c56e89b4493161f098`;
- exact cleared-multiplier table SHA256
  `e3793a7add52c22a7fff745ce196f5dad8c0cd7e4d5407c0e11295484df3ecf2`.

Audit fail closed:

1. Verify all manifests, dual-host independence and byte identity, exact
   q16-through-q24 scope, q2-through-q14 zero specialization, and q15 target-
   shear omission.
2. Trace literal V87 FIRST/P12 reconstruction, frozen V85 q-zero digests,
   the 242-edge DAG and two-sided polynomial inverse, normalized replay,
   P12 division, q-zero-unit remainder, and P12/FIRST omission controls.
3. Independently verify that the complete preclear denominator is exactly
   `(1/8) K B3 U^2 H^2` and that K has exponent one.
4. Verify the consumed identity
   `B3=K+2*F*(2*C*U-V^2+2*U^3)` and the coefficientwise composition to
   target `(1/8) B3^2 U^2 H^2`.  No inverse of K, F, or q is licensed.
5. Replay the emitted 2,651 multiplier coordinates against literal P12, all
   38 original FIRST sources, and literal F.  Check that the final common
   denominator is `U*H`, that all denominator/target factors are units on
   `D(U H B3)`, and that omitting P12, the charged FIRST row, or F breaks the
   identity.
6. Enforce the scope: this is only a literal total-F unit-ideal theorem on
   the high-q residue block.  It is not P12/FIRST-only, a low-q cover,
   total-Rees/source lift, source point, whole fixed-A3, TD6, SP-2, or JC2.

Return `CONFIRMED`, `REPAIRABLE`, or `REJECTED`, with the smallest exact
repair if needed.
