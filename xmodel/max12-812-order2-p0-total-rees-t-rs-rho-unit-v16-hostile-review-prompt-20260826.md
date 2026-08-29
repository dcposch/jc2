You are the hostile independent reviewer of a producer-tier algebraic chart
lemma in the plane Jacobian-conjecture campaign.  Work in
`/Users/dc/code/math/jc2`.  Do not trust producer PASS strings, prose, or
finite-field agreement.  Inspect and independently rederive the exact
characteristic-zero claim.

Write your final report, and make no other repository edits, at exactly

`xmodel/max12-812-order2-p0-total-rees-t-rs-rho-unit-v16-hostile-review-grok-20260826.md`.

Primary package:

`cases/max12_812_order2_p0_total_rees_t_rs_rho_unit_v16_20260826/`

Upstream frozen packages used by its compiler:

- `cases/max12_812_order2_p0_total_rees_t_rs_rho_unit_v14_20260826/`
- `cases/max12_812_order2_p0_total_rees_t_rs_rho_unit_v13_20260826/`
- `cases/max12_812_order2_p0_total_rees_t_rs_rho_unit_v12_20260826/`
- `cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826/`

Claim to audit: on the actual total-Rees T-rs chart
`cs=rs*qcs,c0=rs*qc0,c1=rs*qc1`, the complete source prefix through grade 12,
after saturation by `rs` and restriction to `D(k)`, forces `rho` to be a
unit.  The asserted exact certificate is recorded in `RESULTS.md` and yields

`rho^(-1)=-32*rho*qcs^2*(8*rho^2*qcs^2+3)`.

Required hostile checks:

1. Verify all V16 and V14 source freeze hashes and the harvested result,
   script, stdout/stderr, and artifact hashes.  State any custody gap.
2. Diff the V16 generated scripts conceptually against frozen V14.  Confirm
   that V16 changes only the registered final `SpecialDk` standard-basis
   construction plus token/version labels, and that the sequential call is
   exactly the ideal extension `J+(rho,1-v*k)`.
3. Trace `Tg10_1,Tg10_2,Tg10_3,Tg12_6` back to the exact-Q V9 exports and
   verify that no finite-field polynomial enters the characteristic-zero
   proof.
4. Independently substitute the T-rs chart and check the multiplication-back
   valuations.  Pay special attention that total `Tg10_3` is divisible by
   `rs`, not generally by `rs^2`.
5. Independently expand and verify the four-term Delta identity, the B
   decomposition, and

   `35*rs^2*k*U = 32768*P126+4096*P2+8192*qcs*P3+12288*rho^2*qcs*P1`,

   with `V=8*rho^2*qcs^2+3` and `U=1+32*rho^2*qcs^2*V`.  Check both negative
   controls are genuinely nonzero; do not infer this only from printed tokens.
6. Check the commutative-algebra step carefully: if the right side lies in
   the unsaturated chart ideal, saturation by `rs` puts `35*k*U` in `J`;
   over Q and then on `D(k)`, this puts `U` in the localized ideal.  Check the
   actual Singular saturation and elimination encodings implement these
   statements and do not rely on quotient-ring assignment normalization.
7. Verify directly that `rho*(-32*rho*qcs^2*V)-1=-U`, hence the claimed
   inverse follows.  Verify independently that `J+(rho,1-v*k)` is the unit
   ideal and that `J+(rho)` contains `k`.
8. Adjudicate the role of the F65521 elimination lane correctly: it is an
   independent software/encoding control, not the characteristic-zero proof.
9. Audit the fail-closed history V12--V15 and ensure no failed predecessor is
   silently used as evidence.
10. Enforce scope.  The package concerns only the T-rs standard chart on
    `D(k)` for the prefix through grade 12.  It does not cover other charts or
    prove global Gate T, order two, maximum twelve, or JC2.

Use exact algebra for any recomputation.  Do not launch heavy local CAS; if a
large calculation unexpectedly becomes necessary, report that as a review
gap rather than loading the workstation.  End with exactly one verdict label:

- `VERDICT: CONFIRMED`
- `VERDICT: CORRECTED`
- `VERDICT: REFUTED`

For `CORRECTED`, state whether the narrow rho-unit lemma survives and give the
clean corrected statement.  For `REFUTED`, exhibit a concrete failed identity,
invalid ideal implication, or source/custody mismatch.
