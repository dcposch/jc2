You are Grok, the independent hostile reviewer for the `8_28` Keller-face R3
rational-mode normal form and squarefree replacement-edge exclusion.  Work
only in `/Users/dc/code/math/jc2`.  Never enter, read, build, status-inspect,
or modify `jc2-lean`.  Do not edit frozen producer artifacts, launch AWS,
run heavy CAS, perform a web sweep, or edit canonical ledgers.

Review these exact charged artifacts:

```text
e1ed280ee1f5d7c997fe1ab6fdeaf40b689de71e1682ba8e13b1c4ba5047ae01
  cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/verify_r3.py
3d69dfbd6c0e28afafdfc7bbb0cf4ebe57d8522938ddd46b418f71123c1da006
  cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/RESULT_R3.json
06053fc175d1a7e212aecb23523bd91287fd33afe4ba181254e236995dc45216
  cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/README.md
b1851156c83657fa85eb875df7e191a99fd339bfcb79ca1a752742ddff9f70b7
  xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-sol-20260827.md
e752b86b5a8953649a3ce8c55379d18eca2dc1bdc8ab4fcd030c63dd64071823
  cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/FREEZE.sha256
```

The completed R1 review

```text
d40cd78f4f0afc12d09f8d1e99724de9fd5125fddc064089d6ca0870c7d777e
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-r1-hostile-review-grok-20260827.md
```

confirmed only the raw/local type repair and two named polynomial ansatzes.
R2 is in a separate pending review.  R3 must stand on its own derivation in
`K(X)[[t]]`; do not borrow any unreviewed R2 conclusion.  Do not accept
producer `PASS`, the Python tables, R0/R1 reviews, or the prior rootwise
fixture as evidence for the new exclusion.

Independently rederive and attack:

1. **Custody, history, scope.** Rehash every charged artifact and pinned
   dependency.  Confirm additivity.  Check that R3 is genuinely distinct:
   it claims a complete rational differential-field normal form including
   negative-power modes, not merely R1's two ansatzes or R2's local carrier
   classification.
2. **Coefficient field and square-root branch.** State exact hypotheses on
   `K`, `H=X^8-1`, and `F,G`.  Decide whether

   ```text
   F0=H^2  =>  sqrt(F)=H+O(t) exists uniquely in K(X)[[t]]
   ```

   through the charged order.  Check whether algebraic closure, analytic
   convergence, raw support, or a global polynomial square root is being
   smuggled in.  Only a formal rational-function branch is allowed.
3. **Linearization and signs.** Starting from

   ```text
   E(F,G)=12F_XG-8FG_X-t(F_XG_t-F_tG_X),
   R=G-F^(3/2),
   ```

   independently verify `E(F,F^(3/2))=0` and

   ```text
   E(F,G)=12F_XR-8FR_X-t(F_XR_t-F_tR_X).
   ```

   A sign, component order, or derivative-at-fixed-variable error is a
   refutation.
4. **Exact modes.** For arbitrary integer `n` and rational `alpha`, derive

   ```text
   E(F,t^n F^alpha)=t^n F^alpha F_X(12-8alpha-n).
   ```

   Verify all exact modes below 22 and their branches:

   ```text
   n=0:  F^(3/2)
   n=4:  t^4 F
   n=8:  t^8 F^(1/2)
   n=12: t^12
   n=16: t^16 F^(-1/2)
   n=20: t^20 F^(-1).
   ```

   In particular, attack the two negative-power modes.  They are rational
   proof terms, not claimed polynomial source transformations; decide whether
   subtracting them inside `K(X)[[t]]` is legitimate for a contradiction
   starting from polynomial `F,G`.
5. **Normal-form completeness.** Suppose the residual first appears at
   weight `n`.  Independently derive

   ```text
   2H*((12-n)H'*r_n-4H*r_n')=0.
   ```

   Prove or refute that every nonzero rational solution is
   `r_n=c H^((12-n)/4)`, with `c` in the constant field, and that squarefree
   `H` permits it exactly for `n=0 mod 4`.  Check valuations at every finite
   root and at infinity, possible different constants on factors, algebraic
   extensions, and zero-divisor issues.  Then audit the induction which
   subtracts an exact mode at `4,8,12,16,20` and forces every other residual
   coefficient through 21 to zero.  Look for interactions among modes or
   higher coefficients of `F` that the argument may have omitted.
6. **Endpoint reduction.** After the five positive modes are subtracted,
   verify that `D=t^22 d+O(t^23)` and that no lower `D` or positive-grade `F`
   coefficient enters

   ```text
   E22=-20H H'd-8H^2d'.
   ```

   Check the target exponent 22 and all factors/signs.
7. **Denominator provenance.** Prove or find a counterexample to the claim
   that `d in K(X)` has finite denominators only along `H=0`.  Trace this
   from polynomial `F_i,G_i` and every coefficient of positive and negative
   formal powers in the normal form.  Check whether cancellation or a
   denominator from a mode coefficient can introduce another finite pole.
8. **Pole lemma.** At a simple root, recompute the leading term for
   `d=aH^-m+...` and verify

   ```text
   E22 leading = (8m-20)a H' H^(1-m).
   ```

   Determine whether two terms can cancel the leading pole, whether `m=5/2`
   can occur in the rational function field, and whether regular `E22=1`
   really forces `m<=1` at every root.  Recheck the target-weight mutation:
   target 20 admits the double-pole homogeneous mode, while target 22 has
   scalar `-4` at `m=2`.
9. **Global polynomial reduction.** Given only `H`-poles of order at most
   one and squarefree `H`, verify that `d=-Y/(2H)` for a polynomial `Y`,
   including any polynomial part and behavior at infinity.  Substitute it
   independently and check

   ```text
   E22=4HY'+6H'Y=M(Y).
   ```

10. **No endpoint.** For `H=X^8-1`, prove or refute that every nonzero
    degree-`d` polynomial `Y` gives `deg M(Y)=d+7` and leading coefficient
    `(4d+48)lc(Y)`.  Treat `Y=0` separately.  Recompute
    `M(X/48)=1+(13/12)H` as a mutation/consistency check.  Decide whether
    `M(Y)=1` is impossible over every charged characteristic-zero field.
11. **Exact firewall.** The maximum permitted conclusion is: no
    polynomial-`X` formal jet with
    `F0=(X^8-1)^2`, `G0=(X^8-1)^3`, and
    `E=t^22+O(t^23)` exists.  This excludes the exact squarefree
    Keller-compatible replacement edge only.  It does not exclude the
    original non-Keller control with `F0=X^16-1`, the whole GGV `8_28`
    family, arbitrary multiple-root/square-cube edges, construct a Keller
    pair, prove the GGV-to-Eggers-Wall functor, `G2-PSC`, `G2-BD`, or JC2.

Return separate `CONFIRMED`, `REFUTED`, or `GAP/REPAIR` verdicts for custody;
formal branch; linearization; each of the six modes; rational-mode
completeness; negative-mode legitimacy; endpoint coefficient; denominator
provenance; pole lemma and mutation; `d=-Y/(2H)`; `M` identity; degree
obstruction; the exact theorem; and scope.  Give the smallest failing mode,
weight, pole, coefficient, field hypothesis, or omitted denominator and the
minimal additive repair if anything fails.

Desk-scale hashes and independent exact arithmetic only.  Write the complete
review to exactly

`xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-hostile-review-grok-20260827.md`

and touch no other campaign artifact.
