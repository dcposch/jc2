# Hostile review: D1 `a=6,7` complete `k6` transition V2

Read-only review, except write exactly one report:

```text
xmodel/max12-812-order2-square-d1-load-transition-a6-a7-v2-hostile-review-grok-20260826.md
```

End with exactly one verdict `CONFIRMED`, `REPAIR`, or `REJECTED`, followed
by `ORDER2_SQUARE_D1_A6_A7_V2_<VERDICT>`.  Do not edit producer files,
ledgers, or `jc2-lean`; do not run local CAS/Lean/substantive exact Python.

Immutable target:

```text
f3c987b630a2895defabcc1043768497f2e8caad538f58122bb4e17b317c0a9c
  cases/max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_v2_t2_20260826/RESULT.md
b2a38e4f5c38166789c5d73ecae989c30ed8168c5fc6a58fc3058eb5535e1ad5
  cases/max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_v2_t2_20260826/FREEZE.sha256
eb0058746a406c9d36c11d00c97884e7e937f93cf693763401aa957c432990ee
  cases/max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_v2_t2_20260826/EVIDENCE.sha256
```

Verify all manifests first.  Then charge every load-bearing point:

1. V1 is genuinely immutable/fail-closed and isolates only the analytic
   row alignment.  Recompute from the exact V1 remainder that the correct
   generating-series representative of `k6*C/L` is `t^2*C*Inv1`, not
   `t*C*Inv1`; check that V2 changes exactly two occurrences and nothing
   else.
2. The source compiler reconstructs all seven frozen Faber tails, all three
   loads, and all four target rows.  Verify source sigma powers for fixed
   `a=6,7` after every outer factor in `source_coefficients`.
3. Recompute complete support through grades 23/24 and 25/26.  The only new
   lower-load terms must be `S0` and `S1` as stated; check no k2, target,
   additional k6, unloaded, or k10 term is omitted.
4. Inspect `SOURCE_SUPPORT_FILTER`: verify its allowed variables are exactly
   correct grade by grade and that the `diff` checks cannot hide an omitted
   dependence.
5. Verify the moving `T0+T1` source-row transform, the analytic coefficients
   of `U0,U1,KRC,S0,S1`, and both L/L^2 recurrences.  Do not trust marker
   names or prior V12 formulas.
6. Audit all three negative controls.  Confirm they test deletion of a
   generically nonzero module rather than merely a presentation artifact.
7. At a=6, prove the leading root allocation is exhaustive and that S0/KRC
   are simple after clearing L^2, leaving exactly
   `(3/2)*lambda^2*cv^2`.
8. At a=7, derive the leading factor `C0*(A0+k60)`.  Verify both shifted root
   maps.  At the shifted-A root, explicitly check cancellation of the two
   moving-L terms using `A0=-k60`; verify every other S1/KRC term vanishes
   and the same C2 residue remains.
9. Check the eta truncation: arbitrary eta represents exact ord(R)=a;
   eta=0 is complete through the next grade for every ord(R)>a.  Reject any
   disguised unbounded substitution.
10. Verify every inversion/nonzero contact used, the exact-Q versus
    finite-field roles, AWS rc/validator/diagnostic/resource custody, and
    set-theoretic/arcwise rather than scheme-theoretic scope.
11. Enforce the firewall: no a>=8, positive-order k10, p=0/k10=0,
    fan/full-square/order-two claim.  Ensure the known all-load
    Chebyshev/Pell survivor is not contradicted.

Return the smallest failing identity/hypothesis.  Do not silently repair a
substantive gap.

