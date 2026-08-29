# Independent hostile review: TD6 V89K1 `K` modulo `F`

Date: 2026-08-26

Review the frozen producer package
`cases/td6_c1_c2_c3_k_b3_mod_f_unit_v89k1_aws_20260826/` skeptically and
write exactly one report to
`xmodel/td6-v89k1-k-b3-mod-f-unit-hostile-review-20260826.md`.
Do not edit the producer, campaign ledgers, top-level files, or `jc2-lean`.

Pins:

- `RESULT.md` SHA256 `2c57d8924eba299906b73ba1889eae309fc7baf01d91322561d6be62d5327907`;
- `EVIDENCE.sha256` SHA256 `d19f252b8c8fd94544bebb522d1022aaf36268ff12793259124a5a202ea42a8f`;
- `FREEZE.sha256` SHA256 `bffb3a6ff3b176a9e8d3367cd7e65a3accd2b351626d9b0863e96af428d2e7b3`;
- V2 archive SHA256 `9a23e8b31eef977fc1ca952dfbcfacdb10f27a93b9b4ef80b6b1a3fdc78e4e49`;
- exact result SHA256 `f2455554a58366f0100333dd5717d421dafad0b5574ee312e8376a3265f5683e`.

Verify manifests and dual-host custody; independently expand the literal
V85 formulas and check

```text
B3 = K + 2*F*(2*C*U - V^2 + 2*U^3).
```

Check the negative control and the `F=0` specialization, including why the
diagnostic's cleared forms use different powers of `U`.  Decide whether the
precise consequence is valid: on `D(B3)`, the class of K is a unit modulo
every ideal containing F, with inverse class `B3^-1`.  Explicitly reject any
claim that this makes K a unit modulo `(P12,FIRST)` without F, or that V89K1
alone repairs H1's rational source multipliers.  Return `CONFIRMED`,
`REPAIRABLE`, or `REJECTED`, with the smallest repair if needed.  Make no
fixed-A3, TD6, SP-2, JC2, source-point, or omitted-moduli promotion.
