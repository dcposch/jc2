# Hostile different-model review — AS109 CUBIC-Y NO-GO

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer/review artifacts on top.

Read in full:

- `xmodel/as109-cubic-coupling-gate-20260824.md`
- every file under `cases/as109_cubic_coupling_20260824/`
- the quadratic producer/review and banked AS109 Hensel/carry materials cited
  in the report
- local primary/secondary notes on Magnus, Appelgate--Onishi, and
  Nowicki--Nakai only for priority hygiene; do not infer attribution from a
  search snippet

Frozen hashes:

- report: `198f0b2ff39f91a7815b9be15f7fc3c3afdd00c00b1c4c0ada6b9f6438d62820`
- replay: `7939c0d708548cf4ba2a06a6ca7a7abe64783014fb494bb1c543d308db875b42`
- freeze: `a68afeca5c7e68e2e5df12b620eac6ab1356d9797f1007850f9476adb55a4a3a`

Independently rerun the replay and attack exactly:

1. Exhaust all top-degree cases for `deg_y f,deg_y g<=3`. Check the
   cubic/cubic leading Wronskian and constant target reduction, the zero-top
   cases, and the affine/cubic shear `g-k f^3` without assuming algebraic
   closure or nonzero coefficients prematurely.
2. In the genuine `(2,3)` case, recompute the `y^4` and `y^3` Jacobian
   coefficients. Verify the UFD valuation construction
   `a2=alpha h^2,b3=beta h^3`, constant scalings, the two depression shifts,
   and that a constant target addition aligns them. Check every factor and
   sign in the invariant and its `-2 lambda` shift.
3. Recompute the rational cusp normal form
   `f=z^2+U,g=z^3+Vz+W,z=hy+r` and its full Jacobian. Verify that coefficient
   vanishing gives `V'=3U'/2`, `W'=0`, and `h U' V=j` over `Kbar(x)`.
4. Attack the polynomiality step: derive the monic equation for `r`, check
   that its coefficients lie in `Kbar[x]`, apply integral closure legitimately,
   and then verify the unit-product contradiction. Look for hidden poles,
   zero factors, or a case lost when `h` is nonconstant.
5. Verify descent of automorphy from `Kbar` to an arbitrary characteristic-
   zero field `K` by uniqueness or faithful flatness. Check no source
   coordinate substitution or field denominator invalidates the theorem.
6. Recheck the AS109 consequence: correction `y`-degree <=3 gives coordinate
   degree <=3 over `Q_109`; field automorphy contradicts the previously
   reviewed residue-ball Hensel noninjectivity. Carries and marked collisions
   are irrelevant. Audit all scope exclusions.
7. Priority: decide only whether this exact theorem is already identifiable
   from accessible local primary material. Promote no novelty claim absent a
   directly supporting source; mathematical confirmation must not depend on
   priority.

Try hard to produce an exact counterexample or identify the smallest missing
hypothesis. Do not edit producer or canonical files, search quartic supports,
or launch AWS.

Write exactly one file:

`xmodel/as109-cubic-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
full hashes, independent algebra/replay, descent and priority caveats, scope
exclusions, and promotion advice.
