You are Grok, the independent hostile reviewer for the `8_28` Keller-face R2
rootwise cusp unit-carrier classification.  Work only in
`/Users/dc/code/math/jc2`.  Never enter, read, build, status-inspect, or modify
`jc2-lean`.  Do not edit frozen producer artifacts, launch AWS, run heavy
CAS, perform a web sweep, or edit canonical ledgers.

Review these exact charged artifacts:

```text
74c6c78e4faf527172703d5a115767562d89d9fa20868fc431dcc1f7cd258f15
  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/verify_r2.py
0dffbb36c20d0b80498d765168a47cdb9ed2889ffc7bd105dce7ec835f600b1d
  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/RESULT_R2.json
c95f194df15bce9db128e10329602a19ad3cf62bec88f829bc76182ae9fbdc83
  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/README.md
0f8f3833c8fa16349d52c6d68829e5c86200ab064f84e4172b0ba4039314b733
  xmodel/ggv-8_28-keller-face-cusp-unit-carrier-classification-r2-sol-20260827.md
453f7821f88add5d97b65cee41fe3a4df225db5768526746cf4ff1431aa73aa6
  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/FREEZE.sha256
```

Pinned reviewed/input context includes:

```text
171ff47c844331da8971a731c1ffaf20c31ed5b2ba86fdee2d0d81219eb002b0
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-hostile-review-grok-20260827.md
05cbb5c046f9aa4b89e1104448e77fd38ec3a146d2422bf84773f81d668bfe3c
  cases/ggv_8_28_keller_face_cusp_jet_pinning_r1_20260827/FREEZE.sha256
```

R1 itself is undergoing a separate additive review.  Do not make R2 depend
on that pending verdict beyond the exact frozen formulas it rederives.
Do not accept producer `PASS`, the Python symbolic ring, the R0 review, or
the R1 report as evidence for any new R2 assertion.

Independently rederive and attack:

1. **Custody/dedup.** Rehash every charged file and pinned dependency.
   Confirm that R2 is additive and does not alter R0/R1.  Check the history
   statement: R0 established a rootwise fixture, R1 repaired direct raw/local
   typing and tested two ansatzes, while R2 claims only the missing rootwise
   carrier exhaustion with unrestricted local sidecar.
2. **Formal Morse chart.** At a simple root `c` of squarefree
   `H=X^8-1`, decide whether `F_0=H^2` permits a parameter-dependent formal
   coordinate with

   ```text
   F=u^2+U(t),  u=H(X) mod t.
   ```

   State the coefficient field/completion and every needed hypothesis.
   Attack sign/orientation, square-root, critical-section, and convergence
   assumptions.  The result is allowed to be formal/root-local only; any
   global polynomial-coordinate reading is a scope failure.
3. **Coordinate/Jacobian naturality.** With `u=u(X,t)`, independently apply
   the chain rule to

   ```text
   E=12F_XG-8FG_X-t(F_XG_t-F_tG_X)
   ```

   and verify or refute `E=u_X L`, where

   ```text
   L=12F_uG-8FG_u-t(F_uG_t-F_tG_u)
   ```

   uses `t` derivatives at fixed `u`.  Check exact cancellation of `u_t`.
   Then justify the triangular inference from `E_<22=0,E_22=1` to
   `L_<22=0` and
   `H'(c)[t^22u^0]L=1`.  A missing determinant unit or sign is decisive.
4. **Unrestricted sidecar expansion.** Starting from

   ```text
   F=u^2+U(t),
   G=W(t)+V(t)u+Q(t)u^2+Gamma(t)u^3+sum_(m>=4)G_m(t)u^m,
   Gamma(0)=1,
   ```

   independently derive the `u^0,u^1,u^2` channels.  Verify or refute

   ```text
   [u^0]L = V*(tU'-8U)
   [u^1]L = 24W-2tW'+2Q*(tU'-8U)
   [u^2]L = 16V-2tV'+3Gamma*(tU'-8U).
   ```

   Check all derivative terms and whether any `u^4+` coefficient can enter
   these channels.  Audit the producer's sparse symbolic engine for omitted
   terms, truncation artifacts, aliasing, or hard-coded equality.
5. **Weights below eight and resonances.** Prove or find a counterexample to
   the induction that `U_1=...=U_7=V_1=...=V_7=0` over each geometric
   residue field.  Check that the first forbidden constant coefficient is
   exactly `3(k-8)U_k^2/2` at weight `2k`.  Verify that both `U_8` and `V_8`
   are resonant and that every occurrence of `U_8` in the charged channels
   is killed by its `(8-8)` factor.
6. **First post-eight coefficient.** Let `k>8` be minimal with `U_k != 0`.
   Check from the full `Gamma` convolution—not a specialization
   `Gamma=1`—that `V_k=3U_k/2`.  Decide whether an earlier `Gamma_r`, `Q_r`,
   `W_r`, determinant coefficient, or higher-`u` term can change the first
   constant-channel order.
7. **Carrier dichotomy.** Independently prove or refute both branches:

   - on a geometric root/factor with `V_8 != 0`, the first constant term is
     `(k-8)V_8U_k` at weight `8+k`, so the unit endpoint forces `k=14` and
     `6H'(c)V_8(c)U_14(c)=1`;
   - on a geometric root/factor with `V_8=0`, the first constant term is
     `3(k-8)U_k^2/2` at weight `2k`, so it forces `k=11` and
     `(9/2)H'(c)U_11(c)^2=1`.

   Look especially for cancellation by another pair at the same first
   weight, nilpotent/zero-divisor failures, and coefficients beyond weight
   22.  Keep the theorem over geometric residue fields unless a stronger
   etale statement is actually justified.
8. **Mixed-factor/deck typing.** Recompute

   ```text
   H=(X^4+1)(X^4-1), V8=X^4+1.
   ```

   Check that `V8=0` on the first factor and `V8=2` on the second, so both
   carrier cases can coexist.  Decide whether `gcd(H,V8)`/idempotent splitting
   suffices and which conjugation, factor, root, chart, orientation, and
   `H'(c)` tags must survive.  Reject any globally binary `V8=0/nonzero`
   interpretation.
9. **Firewall.** The maximum permitted result is formal/rootwise carrier
   completeness through weight 22, robust to arbitrary local higher-`u`
   sidecars.  It does not provide the raw `2S/3S` cleanup/provenance compiler,
   classify the global `H`-multiple at `E_22`, prove that every sidecar lies
   in R1's `M(Y)` image, exclude the `8_28` face/family, construct a Keller
   pair, establish GGV-to-tree transport, `G2-PSC`, `G2-BD`, or JC2.

Return separate `CONFIRMED`, `REFUTED`, or `GAP/REPAIR` verdicts for custody;
formal Morse existence/orientation; exact chain rule and determinant unit;
each low-`u` channel; independence from unrestricted sidecar; the lower
induction; each carrier branch; mixed-factor classification; compiler/global
image gap; and final scope.  Give the smallest failing coefficient, sidecar
term, root/factor, determinant, or hypothesis and the minimal additive repair
if anything fails.

Desk-scale hashes and independent exact arithmetic only.  Write the complete
review to exactly

`xmodel/ggv-8_28-keller-face-cusp-unit-carrier-classification-r2-hostile-review-grok-20260827.md`

and touch no other campaign artifact.
