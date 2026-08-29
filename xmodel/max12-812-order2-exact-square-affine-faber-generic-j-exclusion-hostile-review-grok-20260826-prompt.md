# Hostile review request — generic affine-Faber complete-local `J` exclusion

Act as a different-model hostile mathematical reviewer.  Work independently
from producer conclusions and do not trust PASS strings, modular evidence,
or prose summaries as proofs.

Review this exact theorem:

```text
fe1193abe8c45c590f7653d96998a7b053e8de0e09a751cd8fb686d2cbf72fc1
  xmodel/max12-812-order2-exact-square-affine-faber-generic-j-exclusion-theorem-20260826.md
```

Charged producer custody:

```text
a9cb98448d0ff6bdd13120966c870cfc3be95c54bb3a7d67ac80e975e1fd3cc2
  cases/max12_812_order2_exact_square_faber_generic_j_exclusion_20260826/RESULT.md
ec59a48c4d121ec43b0cc43f36edd3b5da2d7f76bef86447b12201a3f4862093
  cases/max12_812_order2_exact_square_faber_generic_j_exclusion_20260826/EVIDENCE.sha256
149ae5131ccbeccfeea6b86151471703bb4620cc1e4c0a56d6d0b1ea21f2800d
  cases/max12_812_order2_exact_square_faber_generic_j_exclusion_20260826/FREEZE.sha256
0098b72df237d5f32490ab41c14db8503156280c47948729ced31d4137495e11
  cases/max12_812_order2_exact_square_faber_generic_j_exclusion_20260826/compile_generic_j_exclusion.py
```

Also read the charged corrected support/source inputs named by the theorem.
Verify every hash and both manifests before reviewing the claim.

Required attacks:

1. Re-derive the triangular coefficient isomorphism `F=Q^2+N` and verify
   that `(c,u,n3)` exhaust all odd directions in the centered monic octic.
   Flag any hidden moving-center or gauge direction rather than assuming it
   away.
2. Derive parity of the literal ordinary Faber rows, including the inverse
   root convention.  Check that `R1=R3=R5=R7=0` at odd coordinates zero for
   arbitrary even coefficient, load, target, and nilpotent/formal jets.
3. Independently derive the full matrix (4.3), not from the producer PASS
   output, and check
   `det=-25 D^3(5D+2s)(5D-2s)^2/2^17` with no missing divisor.
4. Audit the formal implicit-function step carefully: the completion,
   parameter ring, existence and uniqueness, equality
   `(R1,R3,R5)=(c,u,n3)`, parity membership of `R7`, and the exact
   `J`-saturation conclusion.  Try to construct a nilpotent or ramified
   counterexample to the claimed all-orders statement.
5. On the `A` and `K` faces, recompute rank, kernel, and `dR7`; check the
   displayed kernel basis and the claim that every first-order kernel is
   `R7`-null.  Recheck raw identities (6.1) and (6.3).
6. Inspect the compiler and exact-Q evidence for source fidelity and
   non-tautological controls.  Confirm V1 is parser-negative only and V2 is
   a parenthesization repair.  Treat characteristic 65521 only as a software
   control.
7. Enforce the theorem's firewall.  Decide explicitly whether the theorem
   is valid only in the normalized ordinary-Faber coefficient completion or
   whether its stated Section-7 total-Rees gate has actually been discharged.
   Do not promote it to a total-Rees, terminal, Taylor, order-two, maximum-12,
   or JC2 result without literal evidence.

Give the smallest failing identity and strongest surviving theorem if any
attack succeeds.  Otherwise end with `CONFIRMED` and state the exact scope.

Write the review only to:

```text
xmodel/max12-812-order2-exact-square-affine-faber-generic-j-exclusion-hostile-review-grok-20260826.md
```

Do not edit any other file, especially `jc2-lean`.

