# Hostile different-model review — AS109 QUADRATIC-Y NO-GO

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer artifacts on top.

Read in full:

- `xmodel/as109-quadratic-coupling-gate-20260824.md`
- every file under `cases/as109_quadratic_coupling_20260824/`
- the Hensel noninjectivity lemma and its review in
  `xmodel/as109-support-gate-20260824.md` and
  `xmodel/as109-support-review-grok-20260824.md`
- the carry erratum only to verify independence from digit bookkeeping

Frozen producer hashes:

- report: `10ee0b91d4be7ced8d6c053ba66e6d677d7c4cc83af89fc481d215f145e38ea1`
- replay: `846aaef1be5be8efd402ce8c596cf6985b6f9fb19a5553d5bcd2757de746ed69`
- freeze: `e0ae3f4dded38cb96bf149c3e035fbdff3976187fc7f396c0416cba65577e5ae`

Independently rerun and attack exactly:

1. Over an arbitrary characteristic-zero field, recompute the `y^3`
   coefficient of the Jacobian of two quadratic-in-y polynomials. Check all
   zero-leading-coefficient cases and the constant target GL2 reduction to
   one affine coordinate.
2. With one coordinate affine in y, recompute the `y^2` coefficient and
   justify `b2=k*a1^2`, including the `a1=0` case. Verify that the target
   shear `(f,g)->(f,g-kf^2)` is invertible and removes the remaining
   quadratic term.
3. Prove independently that every affine-in-y Keller pair is a polynomial
   automorphism, checking both-nonzero and one-zero leading coefficients and
   the explicit inverse.
4. Decide whether this really proves the field theorem: every Keller pair
   with both y-degrees <=2 is an automorphism. Flag any hidden algebraic
   closure, denominator, or coordinate-change hypothesis.
5. Apply the theorem over `Q_109` to an exact integral lift. Check that
   correction y-degree <=2 implies coordinate y-degree <=2 and that target
   transformations need not preserve the integral seed. Recheck the banked
   residue-ball noninjectivity rather than assuming a marked collision.
6. Scope: arbitrary x-degree/support/coupling is excluded only within both
   y-degrees <=2. Cubic and higher remain open. There is no lift, char-zero
   counterexample, arbitrary-AS109 no-go, or JC2 conclusion.

Use independent exact algebra rather than producer verdict strings. Identify
the smallest missing hypothesis or overclaim. Do not edit producer/canonical
files and do not widen to a search.

Write exactly one file:

`xmodel/as109-quadratic-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim, with
replay/hashes, scope exclusions, and promotion advice.
