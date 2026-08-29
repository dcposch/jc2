# Hostile review request: complete-source D1 finite band `a=2..5`

You are the sole hostile reviewer.  Work read-only except for exactly one
final report at

```text
xmodel/max12-812-order2-square-d1-finite-band-a2-a5-hostile-review-grok-20260826.md
```

End the report with exactly one verdict line `CONFIRMED`, `REPAIR`, or
`REJECTED`, followed by the unique sentinel

```text
ORDER2_SQUARE_D1_FINITE_BAND_A2_A5_<VERDICT>
```

where `<VERDICT>` is the same verdict.  Do not edit the target package,
ledgers, or `jc2-lean`.  Do not run local Singular, Sage, msolve, Lean, or
substantive exact Python.  This is a text/evidence review; all producer CAS
was on AWS.

## Immutable target and custody

```text
17c3baa20232dad9dd1356c8e903a863a44480344d81d8aa587216414aad0a61
  cases/max12_812_order2_square_owner_d1_finite_band_a2_a5_fullsupport_20260826/RESULT.md
9c53eecf7aa3a1fbc75012d9566a2d564e7a39da7e9011c6d5fd63cd53431920
  cases/max12_812_order2_square_owner_d1_finite_band_a2_a5_fullsupport_20260826/FREEZE.sha256
49264a8d6ae24724ee1005dfac9b4602946f2f3b7a77c0512df237369470f254
  cases/max12_812_order2_square_owner_d1_finite_band_a2_a5_fullsupport_20260826/EVIDENCE.sha256
```

Verify every manifest and named artifact byte-for-byte before reading the
claim.  The source archive recorded in the report is ephemeral provenance;
the repository freeze and retrieved evidence are the canonical custody.

## Required hostile checks

Fail at the smallest false identity or missing hypothesis.  In particular,
charge all of the following independently.

1. The compiler really reconstructs all seven exact frozen Faber tails from
   the pinned `tails.json`, with load weights `k10,k6,k2` and target rows
   `mu2,mu4,mu6,J/4`; it is not merely replaying the eight-term analytic
   truncation.
2. The source coefficient substitution is exactly
   `f=K^2+sigma^5 D`, `K=L(sigma)^2+sigma^2 R`, `D=LA+C`, with
   `L(sigma)=z^2+p/2+sigma*ell1`, and the fixed powers used for
   `A,C,R` correspond to `ord(A)=a`, `ord(C)=a+1`, `ord(R)>=a` after all
   outer sigma factors in the source compiler are accounted for.
3. For each `a=2,3,4,5`, grades `g=11+2a` and `g+1` are the first two
   relevant grades.  Verify by support inequalities that every unlisted
   unloaded/k10 term lies later except `RC` for `ord(R)=a` and `R^3` only
   for `a=ord(R)=2`.
4. Verify directly from the complete source extraction—not just order
   heuristics—that `k6,k2,mu2,mu4,mu6,J` do not occur through `g+1` in
   these four blocks.  Check that the Singular `diff` sentinels are
   sufficient for this coefficient-independence claim.
5. Verify the exact moving lower-unitriangular row relation at both grades:
   the `g+1` relation must include both the denominator connection from
   `L(sigma)` and the first row-basis connection
   `T1=2*ell1*dT0/dp`.  Inspect the imported `row_checks` implementation;
   do not infer this from marker names.
6. Verify the analytic Laurent emitter is complete through `g+1`, including
   the coefficients of `AC/L`, `C^2/L^2`, `k10*RC/L`, and the exceptional
   `k10*R^3/L`; find any missing term or wrong sigma/t power.
7. Verify the first `L` recurrence and next `L^2` recurrence/numerator
   formulas.  In particular check every `p` and `p^2/4` coefficient rather
   than trusting the prior V12 formula.
8. Check both ring maps have the right number/order of source images and
   implement the two possible root allocations.  Prove the allocation is
   exhaustive for nonzero linear `A0,C0` when `L` is squarefree.
9. Recompute the next cleared numerator at the allocated root.  It must be
   exactly `(3/2)*lambda^2*cv^2`; every moving-p, A/C correction, RC, and
   R3 term must vanish there for a licensed reason.
10. Check the `eta` scope carefully.  Arbitrary `eta` represents only the
    grade-a section for exact `ord(R)=a`; `eta=0` must genuinely be
    truncation-equivalent through `g+1` for all `ord(R)>a`.  Fail if this is
    another disguised unbounded substitution.
11. Verify `D(p*k10)` and nonzero A/C contact supply every inversion used in
    the root argument.  Distinguish set-theoretic/arcwise exclusion from
    scheme structure.
12. Audit both AWS records: engine rc0, validators PASS, no rejected
    diagnostics, `/usr/bin/time -v` only in stderr, memory/time claims, and
    exact-Q versus finite-field roles.
13. Confirm the firewall: no `a>=6`, no positive-order `k10`, no p=0/k10=0,
    no fan/full-square/order-two claim.  The all-load Chebyshev/Pell survivor
    must remain compatible with the finite early-grade statement.

Do not repair a substantive gap silently.  If an endpoint is still true but
wording/custody/software is incomplete, return `REPAIR` with the minimum
nonmutating delta needed.

