# Hostile review: localized low-contact `c=1,2` square gate

You are the hostile reviewer for one sharply scoped exact-algebra producer result
in the plane Jacobian-conjecture campaign.  Work read-only except for writing the
single requested report.  Do **not** run Singular, Sage, Lean, a solver, or a
substantive symbolic Python computation on this Mac.  Do not run broad `git
status`, do not inspect unrelated files, and do not read any live or historical
`.run` transcript.  Small textual inspection, checksum verification, and hand
algebra are allowed.

Write exactly one report:

`xmodel/max12-812-order2-square-lowcontact-c1-c2-localized-review-grok-20260826.md`

The producer target is

`cases/max12_812_order2_square_owner_lowcontact_c1_c2_v4_localized_delta_20260826/RESULT.md`

with SHA-256

`b8ae74e5ca69b50ee346c2a11acf3282bf68bd42522fa9a10bab537d7ab14e7d`.

Its result manifest has SHA-256

`6931164bb265fc94deb4241b280a02a1110c120dc4cfe1664e38e3a3e3af7da1`,

and its source freeze file has SHA-256

`beea0c90fad4da24b386333917f2fea445ae941ad059e0ec2a4ceb69fe77123e`.

The frozen unlocalized V3 negative-control freeze file is

`cases/max12_812_order2_square_owner_lowcontact_c1_c2_v3_namespaced_20260826/FREEZE.sha256`

with SHA-256

`676f97810cc0c758ba864efe3463c2798f3c5d8f3fd70d57dee8ba0fb7457b57`.

## Files licensed for inspection

Inspect only the target and the named V4/V3 package trees, together with files
that those frozen compilers explicitly vendor and pin.  In particular inspect:

- V4 `FREEZE.sha256`, `REGISTRATION.md`, `compile_delta_v4.py`, compiled exact-Q
  Singular source, `compiler.stdout`, `compiler.validation`, `compiled.sha256`,
  engine stdout/stderr/meta/validation, `freeze_check.stdout`, and
  `RESULTS.sha256`;
- the analogous frozen V3 sources and its exact-Q and `F_65521` evidence under
  `aws_q_box03_failed` and `aws_p65521_r6d_failed`;
- any frozen parent source files reached through the compiler's explicit hash
  chain, but no unrelated campaign synthesis.

## Load-bearing questions

Give a verdict of `CONFIRMED`, `REPAIR`, or `REJECTED`.  Fail closed and identify
the smallest failing identity or hypothesis.

1. Verify every stated SHA and the complete frozen-source -> compiled-input ->
   AWS-output custody chain.  Verify the exact engine exit status and validator,
   not merely a printed PASS token.
2. Verify that the compiler replays the complete seven source/Faber rows in the
   advertised moving square chart, with no silently dropped correction or load
   term at the relevant grades.  Check the normalization and the meaning of
   `p`, `k0`, `L`, `A`, `R`, `C`, `ell1`, and all leading variables.
3. Verify the lower-unitriangular moving Laurent-coordinate transformation and
   that the rootwise equations are equivalent to the required negative-tail
   divisibility conditions, not only necessary projections.
4. Verify the integral `c=1` argument.  In particular the grade-11 divisibility
   and grade-12 double-pole/root remainder must force the advertised leading
   correction to vanish on `D(p*k0)` without a hidden reducedness assumption.
5. Verify that both V3 controls pass every source/Laurent/recurrence/`c=1`
   sentinel and fail only the unlocalized `c=2` membership, in exact Q and
   `F_65521`.  Confirm the raw obstruction is exactly

   `(3/8)*ell1*a0*a1*bs1 + (3/32)*ell1*a1^2*br1`

   modulo harmless syntax/normal-form conventions.  Treat this as a negative
   control, not as a theorem failure.
6. Audit the exact Singular semantics of `sat(c2G,ideal(p*k0))`: it must be
   localization to the open `D(p*k0)`, the localized ideal must remain proper,
   and the displayed obstruction/delta must reduce to zero there.  Check that
   no list/ideal coercion or standard-basis flag issue can discard generators.
7. Reconstruct the pointwise/rootwise implication.  The lower rows give the
   required grade-12 and grade-13 relations; at a root where `A` is nonzero,
   `L | A E` kills `E`; at a root where `A` vanishes, the localized grade-14
   equation kills `E^2`.  Explain why `p != 0` makes `L` squarefree and why the
   two roots exhaust the linear correction.  Check the role of `k0 != 0`.
8. Distinguish exact ideal membership after localization from a reduced-scheme
   assertion.  Decide whether it licenses the producer's **arcwise,
   set-theoretic contact-raising** conclusion, including nilpotent arcs, and no
   more.  Attack saturation/pointwise commutation and any use of algebraic
   closure or root allocation.
9. Enforce the firewall exactly: at most the finite `c=1,2` leading corrections
   on the generic-square first-normal chart `D(p*k0)`.  It does not cover
   positive horizontal contact of `A`, `p=0`, `k0=0`, the exact-square zero
   section, fan exhaustiveness, the whole square branch, exact order two,
   maximum twelve, or JC2.

The report must state all target/evidence hashes it actually verified, give a
short lemma chain, and end with exactly one of:

`ORDER2_SQUARE_LOWCONTACT_LOCALIZED_CONFIRMED`

`ORDER2_SQUARE_LOWCONTACT_LOCALIZED_REPAIR`

`ORDER2_SQUARE_LOWCONTACT_LOCALIZED_REJECTED`
