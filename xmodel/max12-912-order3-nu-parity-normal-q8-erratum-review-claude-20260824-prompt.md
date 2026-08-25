# Hostile review — corrected `Q8` parity-normal boundary

Act as a hostile different-model mathematical reviewer in
`/Users/dc/code/math/jc2`. Read in full:

- `xmodel/max12-912-order3-nu-parity-normal-q8-erratum-20260824.md`;
- every file in `cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/`;
- the pinned source compiler and reviewed parity-genus-five producer/review;
- the quarantined `Q12` producer and its hostile refutation, only as an
  adversarial control.

Charged hashes:

```text
report    7f1ed3c7874c743b35ba4f519acdc2555f65c93c467ccb2e894d8d0b7ade1cc2
manifest  aecc0762d4211633c0d0a60c513b6c16cd9e20f9d4798c5ac1269d3454f0f1e7
freeze    998a967ba565edaa3af0e8e35b526391067292ae60ac26e3a33a7d5efd0cac0d
```

Independently reconstruct and attack:

1. all eight source Faber tail rows and the parity specialization;
2. the distinction between the wrong constant `1/3` and the required
   polynomial numerator `1+3v` in `x1`, including direct checks of `r2,r4`;
3. the reversible chart, excluded factors, and formula for `r6`;
4. the full normal determinant from the source rows and its factorization
   with residual polynomial `Q8`;
5. the numerical `p=v=1` control and the old-`Q12` pass/new-fail controls;
6. squarefreeness and every stated gcd; and
7. whether the exact scope and quarantine boundary are sound.

Do not inherit any identity solely from either producer. Run the replay, make
independent symbolic or exact-rational spot checks, and look specifically for
another substitution/chart-denominator error. Do not review or promote the
newer formal-branch computation: this charge concerns only the corrected
first-order rank boundary.

Write exactly
`xmodel/max12-912-order3-nu-parity-normal-q8-erratum-review-claude-20260824.md`.
Do not edit producer, case, canonical, coordination, or other review files.
End with exactly one verdict: `CONFIRMED`, `GAP`, or `REFUTED`, and identify
the smallest failing identity or missing hypothesis if applicable.
