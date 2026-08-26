You are an independent hostile algebraic-geometry reviewer. Work in
`/Users/dc/code/math/jc2`. Review exactly

`xmodel/max12-812-order2-first-normal-principal-part-ufd-theorem-20260826.md`

whose required SHA-256 is

`988d659f0a25f14a612d316608a8dc7c36d839c3f253c35e7e785d33e5923fb5`.

Do not trust the target's status, prior verdict tokens, modular endpoints, or
this prompt's summary. Recompute the target hash and every charged parent
hash. Use source reading and hand derivation only: no Singular, Sage, msolve,
Lean, substantive Python, or solver computation.

Attack these points explicitly:

1. Derive at fixed `z` and then fixed tail coordinate `w` the exact
   `Lambda^2` identity. Check that the coefficient is `+3/8`, the `k10`
   term is `+k10 K^(5/2)`, the polynomial-part convention is in `z`, and
   substituting `z_Lambda(w)` introduces no hidden order-two term.
2. Check that `w0=K^(1/4)=z+O(z^-1)` really gives a unitriangular map on
   the first seven negative coefficients, and that four vanishing
   coefficients of the proper fraction `N^2/K` force the degree-at-most-three
   remainder to vanish.
3. Re-derive `K|N^2 iff D_K|N`, including repeated-root profiles and the
   `[1,1,1,1]` zero-normal case. Verify every coefficient in the square and
   discriminant parameterizations (3.3)--(3.6), including depression.
4. Audit the projective-irrelevant and nonzero-normal saturations carefully:
   distinguish removal of components from exclusion of individual affine
   closure points. Decide whether the asserted reduced-support equality on
   `k10=0` follows when saturation is taken before the slice.
5. Verify that the square parameterization solves the full first gate for
   arbitrary `k10`. Fail the target if it claims nonsquare/nonzero-`k10`
   exclusion, full radical equality, reducedness, nilpotent structure, or
   strict-Rees/order-two closure without proof.

Return `CONFIRMED`, `REPAIR`, or `REFUTED`, naming the smallest failing
identity or missing hypothesis. State the strongest exact theorem that
survives and keep the full scope firewall.

Write the complete report to exactly

`xmodel/max12-812-order2-first-normal-principal-part-ufd-review-grok-20260826.md`

and do not edit any other file.
