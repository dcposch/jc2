# Hostile review: repaired normalized order-two square `r=1` receiver

You are the independent hostile reviewer.  Work read-only except for the
single report named below.  Do not run Singular, Sage, msolve, Lean,
Groebner-basis computations, exhaustive Python, or any heavy computation.
Do not inventory the broad dirty worktree.  Read only the named target,
evidence/custody files, and exact transitive compiler/freeze inputs needed to
audit it.  Stored PASS markers are evidence, never authority.

Write exactly one report:

`xmodel/max12-812-order2-square-r1-v15-hostile-review-grok-20260826.md`

## Frozen target and custody

- producer report
  `cases/max12_812_order2_square_owner_r1_v15_validator_telemetry_repair_20260826/RESULT.md`,
  SHA `fba49ea691edf8f272308d745fc5918f076d1b1670e875deea439777ed26ed69`;
- result manifest in that directory, `RESULTS.sha256`, SHA
  `10dc7bcfa1acb05d97df1f36ed4291bb8c66b416c928eaf32177fb92527a88a8`;
- evidence manifest `EVIDENCE.sha256`, SHA
  `dc26e462ff415e9d6e8fc4c228e1f3012f0490e7ecf00b695e2348b9b709441b`;
- source freeze `FREEZE.sha256`, SHA
  `5eec15866895da7692121cf9e1300f34e9914c45608d631751a24a0fb21bdc97`;
- V15 registration and validator SHAs
  `86d7d0048f7a43f6419a5e8e878da0f689b2af642758815b797d9ccbcfedd753`,
  `43f0da6d0b45f25686cf3a1df8bfbe1e5fd70c2c6b4ac6d0b949b1821fc1bd3b`;
- frozen V14 compiler SHA
  `acdfd2a4bb4a02e4ce65c26159f2f8f85a6c5979fe8535d66715aac0c19d7521`;
- exact-Q / `F_65521` Singular-input SHAs
  `0b1efd2f1db5938ea18d488787d2346a9c253688719db5d673425fc76be13296`,
  `d9aafc5304ccff369815814a2cbb8b6752b9754718c435ea2e29644d2708ca7c`;
- identical marker stdout SHA
  `fc6ba5c3ec390a8aebf2991920cf8e05c63f64b275e253d79d3222eeac135dff`;
- identical PASS validation SHA
  `c3a4c8e66bdf91563cd73c2f06524ec7b70334a90f57b5442d9c86d8a1a121e2`;
- V12 source-support erratum
  `xmodel/max12-812-order2-square-r1-d1-v12-source-support-erratum-20260826.md`,
  SHA `997dda081223d99283bff92851e7da8bc260b7b3e52ff89b97fb0a50c817a114`;
- prior hostile review
  `xmodel/max12-812-order2-square-r1-d1-v12-hostile-review-grok-20260826.md`,
  SHA `509c9edf1c613fa4ff997d3da4acbfeccd7e0895fd76e2f471fad37d90ec15aa`;
- V13 and V14 negative-control reports, respectively SHA
  `0946651a9dbdfd37a2ae22559bde0524a5e7a6d81088e6357c794e1f5c737865`
  and
  `db047d7f665b1a130d4fa62b696ac10f5258341974097cec0a108e17ca604c2d`.

First perform lightweight hash checks of all named manifests.  Inspect both
actual AWS inputs, stdout/stderr, metadata, engine return records, and
validators.  Trace V14 through the pinned V13--V1 compiler/freeze chain to
the original frozen shared-Faber tails.  Do not accept a generated analytic
surrogate in place of the exact source rows.

## Load-bearing questions

Give an explicit verdict on every item and identify the smallest failing
identity, hypothesis, or scope sentence if any.

1. Does the transitive ancestry reconstruct all seven exact loaded source
   rows with the stated generic-square coordinates, signs, load weights,
   target exponents, and row ordering?  Does V15 freshly compile the frozen
   V14 source without silently consuming D1?
2. Independently derive the first nonpolynomial grade-thirteen contribution
   on

   ```text
   L=z^2+p/2, ord(A)>=1, ord(C)>=3, R=sigma*R0+...,
   p*k10!=0.
   ```

   Verify its coefficient is exactly `(5/16)*k10*R0^3/L`, and prove every
   unloaded term, `k6`, `k2`, Taylor target, and terminal target is either
   polynomial or of strictly larger absolute grade.  The quarantined
   unbounded-D1 extrapolation may not be used.
3. Verify the seven source rows at grade thirteen are related to the first
   seven Laurent coefficients by the claimed invertible lower-unitriangular
   Faber transform.  Check the recurrence and proper-numerator construction,
   not only the final marker.
4. Recompute

   ```text
   (b1*z+b0)^3 mod (z^2+p/2)
   ```

   and verify both displayed coefficients.  Over exact Q on `D(p*k10)`, do
   their common zeros force `b0=b1=0`?  Check all divisions/characteristic
   exclusions and distinguish reduced support from scheme structure.
5. Audit the actual Singular ideal.  Is `inv*p*k0-1` the intended
   localization?  Is `radical(R1_I)` standardized before every `reduce`, and
   is the support test meaningful?  Confirm the old `// ** ... no standard
   basis` warning is absent in both fresh runs.
6. Audit V13 and V14 as negative controls: V13 must fail at the premature
   hand-check anchor; V14 must have clean mathematical output but fail only
   because expected `/usr/bin/time -v` telemetry made stderr nonempty.  V15
   must alter only validator treatment of that telemetry.  Its validator
   must still reject `?`, `// **`, `error occurred`, `=FAIL`, timeout,
   nonzero engine return, and missing/duplicate markers in either relevant
   stream.
7. Check that `R0=0` contradicts only the normalized nonzero leading section
   and therefore contact-raises `ord(R)`; it is not an empty square-branch
   conclusion and says nothing about the zero section.
8. Enforce the firewall exactly.  A positive verdict licenses only
   arcwise/set-theoretic elimination of the normalized `r=1` receiver on
   `D(p*k10)` after the frozen first-normal, half-weight, and `M=0` gates.
   It does not license V12's unbounded D1 claim, any all-load fan, `p=0`,
   `k10=0`, positive-order loads, terminal/Taylor closure, scheme structure,
   the whole square branch, order two, `(8,12)`, maximum twelve, or JC2.

Verdict must be `CONFIRMED`, `REPAIR`, or `REFUTED`.  End the report with
exactly one final token:

- `ORDER2_SQUARE_R1_V15_CONFIRMED`
- `ORDER2_SQUARE_R1_V15_REPAIR`
- `ORDER2_SQUARE_R1_V15_REFUTED`
