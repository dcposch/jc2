You are Fable 5 acting as a genuinely different-model hostile mathematical
reviewer in the plane Jacobian conjecture campaign.  Work in
`/Users/dc/code/math/jc2`.

Review this frozen dependency chain.  Recompute all live hashes first:

1. `xmodel/ggv-upper-endpoint-lambda-nonzero-unit-s-order4-cancellation-sol-ultra-20260828.md`
   SHA256 `874bcd98b21c19546db67e6dc4599aebd800259687c45ecc0780ab282119e92d`.
2. `cases/ggv_8_28_upper_endpoint_lambda_nonzero_unit_s_order4_cancellation_20260828/verify_unit_s_order4_cancellation.py`
   SHA256 `a4e6f18b718fb99495aaf048a4b104109ef20b320b89e2016c50dfb63a608e40`.
3. `xmodel/ggv-upper-endpoint-lambda-nonzero-unit-s-order5-row-identity-sol-ultra-20260828.md`
   SHA256 `aa88f1904ac14f05cbac193dac12ef054ba3928306811a253abb840656fc7138`.
4. `cases/ggv_8_28_upper_endpoint_lambda_nonzero_unit_s_order5_row_identity_20260828/verify_unit_s_order5_row_identity.py`
   SHA256 `f683bd2a33e93ad2ecd3ca38155388b65d1f536b8ae33fad3c1eff4412112bc4`.

The reviewed R12r source is available for comparison, but its verdict is not
evidence.  Recompute any fact you use:

- `xmodel/ggv-upper-endpoint-active-c2-d8-d13-independent-audit-extension-20260828.md`
  SHA256 `da189b7fa2ce12656dfbd965c2ed76a0f26b90255a4c99e0fa1322d0c98d5577`;
- `cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/verify_active_c2_extension.py`
  SHA256 `112650dc27b0e13d76979d5adca9315919ee65cb8d9eaf717c1685f99d96de26`.

Do not accept either producer checker as a proof.  Reconstruct the local
series and characteristic independently and attack the following.

Order four:

- Verify the full characteristic
  `F^(3/2)+sum_{m=2,4,...,20} c_m t^m F^((12-m)/8)` under
  `t=epsilon*tau`, including the exact mode birth delays and every mode that
  can enter relative order four (`m=0,2,4,6,8`).
- Reconstruct the literal raw `F0,...,F6` formulas from the reduced prefix,
  exact `D=0`, and the D12 lifts
  `QS+4U=A*ell` and
  `2048F6-2SP1-4QSU-8U^2=A*e1`.  Check every sign and power of two.
- Verify the complete abstract order-four expression, the stronger
  `f1 in (L^3)` and `f2 in (L)`, the evaluation at
  `tau0=-4A'(alpha)/S(alpha)`, and the claimed cancellation of all jet terms
  in `B(tau0)`.  Test mutations of each D12 lift.
- Check hypotheses/licensing: simple root, characteristic zero,
  `S(alpha)=3 lambda A'(alpha) != 0`, active `c2`, exact-D branch, and that
  this is local face regularity rather than a raw-window or endpoint result.

Order five:

- Starting from the *reviewed* order-four divisibilities, enumerate every
  partition and every born mode at relative order five.  Explicitly include
  the newborn `c10*t^10*F^(1/4)` term and the linear `f5` contribution, even
  if they are regular.  Determine whether the displayed
  `L^-1*H2*(3*C3/4+5*c2*tau^2*H2/32-3*J1*H2/16)` is truly the sole polar
  part.  Note that the producer checker does not explicitly add `c10`; decide
  whether this is only checker coverage or a mathematical omission.
- Independently reconstruct `F0,...,F7` from the two D12 lifts and verify
  `H2(tau0)`, the bracket value, all powers of `a,s`, and the exact
  `8192*F7` load in `Nc=8192F7-e1*S+Q*Jc`.  The `8192 -> 8191` mutation must
  fail.
- Independently derive or refute the complete reviewed R12r pole
  `g12^-=Jc(20*c2*Jc+3*Nc)/(8388608*A)`.  Check that polynomiality licenses
  `A | Jc(20*c2*Jc+3*Nc)` at this exact stage, and that rootwise vanishing is
  sufficient to divide the face numerator by the linear `L`.
- Decide whether the dependency chain proves regularity through relative
  order five, or whether a missing mode/partition/window/license prevents
  that conclusion.  Do not infer any later-order, raw-window, endpoint,
  Keller, or JC2 result.

Use an independent derivation, not a producer replay.  A light exact
standard-library checker is encouraged, with mutations and a complete
mode/order census.  No heavy local CAS and no AWS.

Write a self-contained report to exactly

`xmodel/ggv-unit-s-order4-order5-dependency-hostile-review-fable5-20260828-v1.md`

with a terminal verdict exactly one of `PASS`, `REPAIR`, or `REFUTE`, and
state that this is Fable 5 different-model review.  If you create a checker,
write it only under
`cases/ggv_8_28_unit_s_order4_order5_fable5_review_20260828/`.

Do not edit any frozen input, canonical/top-level campaign file, or other
existing artifact.  Never enter, list, search, read, build, status, or modify
`jc2-lean`.  Preserve the dirty shared worktree.  Your only writes may be the
required review and optional new checker directory; the lane wrapper owns its
`.log` and `.run` files.
