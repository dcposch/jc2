You are the hostile independent tropical/commutative-algebra referee for the
symbolic cone of one exact corrected witness in the plane Jacobian-conjecture
campaign.  This is a text/source/custody review only.  On the local Mac do not
run Singular, Sage, msolve, gfan, Lean, Python algebra, or any solver.  You may
read files, recompute SHA-256, use cmp/diff/sed/jq for literal inspection, and
do hand rational arithmetic.  If substantive computation is required, fail
closed and request an AWS replay.

The prerequisite first-q2 lift has already passed hostile review.  Pin and
audit, rather than silently strengthening, this exact prerequisite:

```text
2a2ff048c299a8878ea28211b72f0d0ad98f27216ae5c3462eb3bc076083ac7d
  xmodel/max12-912-order3-d1-double-root-control2-q2-syzygy-lift-review-grok-20260826.md
```

Review the complete frozen cone package

```text
cases/max12_912_order3_d1_double_root_control2_q2_cone_v3_20260826/
```

Required package anchors are

```text
c54c33be036410957d02ede886e3d237c9bc2675d73493b028c2fd4d4f1ff4de  FREEZE.sha256
0ed5eab56c10e7114850a9cbb915825d9a4f5f2360c97b25a644c8a64c6a14d7  RESULT.md
ee0639963d1d4788e6a4ba04fbf1c6f98246921d19dc29f2822c0cb136eae9c2  each cone_certificate.json
```

Also inspect the charged support semantics in

```text
xmodel/max12-912-order3-d1-control2-slope-uniform-review-grok-20260826.md
cases/max12_912_order3_d1_double_root_control2_q2_cone_v3_20260826/PREREGISTRATION.md
```

Charges:

1. Recompute all `FREEZE.sha256` entries and all stated report/review hashes.
   Audit both AWS host/tag/job/PID records, frozen source closure and hash
   gates, opposite traversal orders, caps, return codes, empty compiler
   stderr, timing/RSS/swap, result custody, and literal equality of the two
   certificate JSON files.  Fail closed on any diagnostic or custody gap.
2. Starting from the prerequisite review and compiler source, verify that the
   cone compiler reconstructs the literal 37-term corrected witness `W'`,
   with canonical witness SHA
   `ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b`.
   Check that it does not silently drop, combine, specialize, or rederive a
   different polynomial.  Reconcile the 37 terms as target `la^20`, the
   positive-split target `la^20*tau`, and 35 other terms.
3. Charge term-by-term the weight map

   ```text
   wt/L = e_q2*delta + (e_q1+e_q0)*beta
          + (e_r2+e_r1+e_r0)*alpha + 20*e_la
          + (T/L)*e_tau + (H/L)*e_rho,
   ```

   including coefficients, repeated forms, target subtraction, and the
   relation `L=3T+H` only where actually used.  Verify exhaustively that the
   35 non-target terms yield exactly the 15 distinct strict inequalities in
   `RESULT.md`, while the certificate retains all repetitions.  Explain why
   37 terms, 17 forms including the two target forms, and 15 non-target
   halfspaces are mutually consistent.
4. On the slice `alpha=15/2`, independently reduce all 15 inequalities.
   Prove or refute the claimed **necessity and sufficiency**

   ```text
   beta>5 and delta>5
   ```

   for this same witness to have unique least term `la^20` (with `T>0`).
   Charge necessity from actual present monomials, not merely from a relaxed
   halfspace list, and charge sufficiency for every repeated term.  Verify the
   substitution `beta=5+u`, `delta=5+v` and all nonnegative margins exactly.
5. Audit the semantic premise `delta>beta` separately from the algebraic cone.
   State precisely why it is licensed only when `q1,q0` form the charged
   leading control-2 Q-layer at valuation `beta` and `q2` is a later
   activating coefficient (not a simultaneous leading coordinate).  Decide
   whether, under that hypothesis and `5<beta<6`, it indeed implies
   `delta>5` and closes the identically-zero versus later-activating `q2`
   alternatives in this fixed source/load chart.  Do not turn `delta>beta`
   into a fact about arbitrary support masks or equality faces.
6. Charge the exact tie sets on `beta=5,delta>5`,
   `delta=5,beta>5`, and `beta=delta=5`, including counts and monomials.
   Enforce the firewall: this is the complete strict halfspace region of one
   explicit ideal-membership witness, not a full Groebner cone, tropical fan,
   initial-ideal classification, or conclusion on any equality face.
7. State the strongest exact promotion text or the smallest repair.  Preserve
   fixed `a=1,h=0,k=nu=0,mu=2/3`, fixed loads/support, and all moving-axis,
   moving-cusp, moving-load, other-normal-direction, formal-arc,
   whole-double-root, D1, and JC2 firewalls.

Write exactly one review to

```text
xmodel/max12-912-order3-d1-double-root-control2-q2-cone-review-grok-20260826.md
```

Do not edit any producer file, top-level file, or other report.  End with
exactly one of `Q2_WITNESS_CONE_CONFIRMED`, `Q2_WITNESS_CONE_REPAIRED`, or
`Q2_WITNESS_CONE_REJECTED`.
