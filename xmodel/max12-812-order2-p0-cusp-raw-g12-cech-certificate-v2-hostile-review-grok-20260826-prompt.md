# Hostile review: direct raw cusp grade-12 Čech certificate V2

Act as an independent hostile mathematical reviewer.  Work read-only except
for the one report below.  Do not edit case packages, shared ledgers,
`jc2-lean`, or any other `xmodel` file.

Write exactly:

`xmodel/max12-812-order2-p0-cusp-raw-g12-cech-certificate-v2-hostile-review-grok-20260826.md`

The V2 producer is provisional.  Verify these custody hashes:

- `cases/max12_812_order2_p0_cusp_raw_g12_cech_certificate_v2_20260826/RESULT.md`
  `bb6cea00d5665e81769b9f687cfde345569e82e4273cbb22d0c1f172af103675`;
- its `RESULTS.sha256`
  `e32ab337c37eebedc81d901b4c465accca087d8909fb9db62bc6dafc9695b706`;
- its `FREEZE.sha256`
  `9616ff0af8d551a6becb482d95ea1ca7d899a3b9d04df05c7f2cc04af863de7c`;
- its compiler
  `8abeda327a7362e0cd5bdc8b73135bc59e1883664e3824783e34c9182743686d`;
- V1 compiler/freeze
  `feb3711636b57457069c36f79904325d901f68a3cda93742ac5dc737cc1a3c7a` /
  `213e55fe0b59b3979edd2dfe6c2265109a5739438bef7fec6c7beefe1c6b3721`;
- `xmodel/cross-iterated-blowup-cech-valuative-propagation-20260826.md`
  `6995a991b1e7803a26bbf5374b10d54a0cda7d17158ad9f1595db76218aadb92`.

Audit from the complete frozen source, not PASS tokens:

1. V2 changes only V1's wrong ordinary/Faber row assertion and explicit
   multipliers.  Preserve V1 as a genuine fail-closed negative control.
2. Recompute the unparameterized row
   `g12_6=(15/32768)k0 rs^4-(3/64)rs a0 c0-(3/64)cs c0 c1-(3/256)rs c1^2`.
3. Verify literally, coefficient by coefficient,
   `32768*g12_6-35*k0*rs^4=-4096*rs*g10_2-8192*cs*g10_3`, using the raw
   source rows, with no normalization, radical, saturation, or grade-11
   pivot.
4. Verify that omitting `g10_3` leaves exactly
   `-1536*cs*c0*c1`; explain why the nilpotent/raw row is essential.
5. Check all seven tails, corrections, `k10,k6,k2`, and targets remain in
   the source, and that later loads/targets are truly absent at grade 12.
6. Check exact Q independently of the `F_65521` control and all evidence
   hashes/tags/resource records.
7. Decide the exact logical consequence on `D(k0*rs)`: this may remove the
   cusp normalization/finite-cover debt, but it does not establish the
   total unspecialized-`p` Rees base-change map or any other Čech chart.
8. Enforce the firewall: no positive-moving-`p`, all-zero receiver, `k0=0`,
   square-branch, order-two, maximum-twelve, or JC2 conclusion.

End with exactly one token on its own line: `CONFIRMED`, `REPAIR`, or
`QUARANTINE`.  If not confirmed, give the smallest exact correction and
downstream quarantine.  If confirmed, state the maximal source theorem and
remaining glue debt precisely.
