# Independent hostile review: TD6 V89H3 q14 alternate-pivot diagnostic

Date: 2026-08-26

Review the frozen producer package
`cases/td6_c1_c2_c3_q14_alternate_pivot_fitting_v89h3_aws_20260826/`
skeptically and write exactly one report to
`xmodel/td6-v89h3-q14-alternate-pivot-hostile-review-20260826.md`.
Do not edit the producer, campaign ledgers, top-level files, or `jc2-lean`.

Pins:

- `RESULT.md` SHA256
  `2a04389015c743d706c08af2607871bdbd3329095a30663de0c9fbd95a3b5771`;
- `EVIDENCE.sha256` SHA256
  `e912542256e01e6d655d0214ed82fdac188e9e81f3635b7002cebe75e7d3d3ca`;
- `FREEZE.sha256` SHA256
  `33af33d9781181950c881d720518746ceda4870008acd5029ce03fb660673abe`;
- V4 archive SHA256
  `a1c6eb18828897ac16b5af2c433553e54bfbe5318d4cae559d0b35aa9a465494`;
- exact result SHA256
  `5c7623252d67cb2786f5f2b52db5b5060505292f771c0a65c4e8e2b570cd684f`;
- determinant file SHA256
  `6d618994ff0f15810466984f8a01c866299024766baa80266e4878487ee44a59`;
- exchange inventory SHA256
  `1e87d5fcd576b40ce7b32e92d18a08aa3c8257dcc74a9a6e74eb8b0dab417147`.

Audit fail closed:

1. Verify source/evidence/freeze manifests, dual-host independence and byte
   identity, and that V1--V3 stopped before source algebra.
2. Trace the exact q scope: independent q14 and q16 through q24, q2 through
   q13 zero, and q15 absent under the separately reviewed target shear.
3. Independently check that the current support graph's only cyclic SCC is
   `{0,1,2,3,4,5,6,13}` and that the division-free determinant of its exact
   8 by 8 block is the constant polynomial 1, not merely degree zero.
4. Check all 1,004 invertible and 62 registered single exchanges were
   inventoried; confirm the best score and the absence of a registered
   acyclic single exchange.  Do not interpret the bounded scan as excluding
   multi-exchanges or a Fitting cover.
5. Audit the denominator ledger, in particular `(1/4) B3 H^3`, and verify
   that no q expression, F, or unregistered factor was inverted.
6. Enforce the central scope distinction: the unit SCC determinant is only a
   lead until a successor constructs an explicit full polynomial inverse,
   verifies both products, reduces literal P12, replays original sources,
   and passes omission controls.

Return `CONFIRMED`, `REPAIRABLE`, or `REJECTED`, with the smallest repair if
needed.  Make no radical-membership, source-point, nonintegrability,
fixed-A3, TD6, SP-2, JC2, or omitted-moduli promotion.
