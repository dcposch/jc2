# Unique-output hostile review request

Read and hostile-review the following frozen producer and AWS-only compiler:

```text
xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-client-20260825.md
SHA-256 2a7c5b6e09818d523954f8896a339d5f31407650b1777dd83f7a5bbbe5eda4fa

cases/max12_812_order4_mu4_nonzero_curve_20260825/compile_curve.py
SHA-256 5c1add225079ff56454654bcbb893326bc95dc34cf5c3f763aa58a0ef012b8de

cases/max12_812_order4_mu4_nonzero_curve_20260825/FREEZE.sha256
```

Charged parents are named and hashed in the producer.  Recompute every hash.
Read the source audit and frozen shared Faber implementation directly; do not
trust earlier verdict language.  This is a source-reading and hand-derivation
review only: run no CAS, solver, substantive exact Python, Sage, Singular,
msolve, or Lean locally.

Attack at least these points:

1. Starting only from the stated tail convention, rederive the sign and
   constant in
   `g^2-f^3+2 mu_4 f=-2R_7 z^5+O(z^4)` and check that no `E^2` term can
   contaminate a nonnegative degree.
2. Prove or refute exact equality of the two unsaturated ideals:
   `(r1,r2,r3,r4-1,r5,r6)` and the coefficients of
   `g^2-f^3+2f` in degrees 11 through 6.  Check the triangular diagonal and
   the claimed `[z^5]=-2r7` identity after quotienting.
3. Check the weighted normalization of nonzero `mu_4`, including the
   direction `lambda^16 mu_4=1`, the weight 19 open condition, field
   extension, residual symmetry, and whether normalization can create or
   lose geometric points.
4. Audit the compiler independently: no hidden order-two loads, correct
   depressed `(8,12)` Faber polynomial, sufficient inverse-series depth,
   correct tail signs/weights, independent shifted-polynomial construction,
   ideal-containment checks, mandatory `r7` saturation, fail-closed behavior,
   and AWS guards.  Identify any Singular syntax or interpretation hazard.
5. Enforce the firewall: coefficient-infinity necessity is not source
   exactness, Taylor polynomiality, a Keller pair, order-four closure, or JC2.

Classify every issue as fatal, repairable, or cosmetic.  State the smallest
failing identity/hypothesis if any and the strongest exact result that
survives.  Mention that live AWS outputs were not used as evidence.

Write exactly one file and no other file:

```text
xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-review-grok-20260825.md
```

End with exactly one overall verdict token: `CONFIRMED`, `REPAIR`, or
`REJECTED`.
