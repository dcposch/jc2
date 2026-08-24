# Hostile different-model review — QUINTIC-Y FRONTIER

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer/review artifacts on top.

Read in full:

- `xmodel/quintic-y-frontier-preflight-independent-20260824.md`
- every file under `cases/quintic_y_frontier_20260824/`
- the quartic producer and its running/completed hostile review
- the confirmed cubic producer/review and the AS109 Hensel/carry materials
  needed only for the stated lift consequence

Frozen hashes:

- report: `598cdf3799d4abf40ec761f1fd2b0a5a6457ee2b578371bd864c296259d2a978`
- replay: `943676ec94a0e1829d80ca23f56e1ce8d919089c9eff8fecdbc5118200782bf5`

Independently rerun the replay and attack exactly:

1. Check that after equal-degree target reduction, zero/affine cases, and
   target shears, the only genuinely new actual pairs above the quartic
   theorem are `(2,5),(3,5),(4,5)`. Audit the affine-coordinate argument,
   leading UFD step `a=h^m,d=h^5`, depression alignment, field extensions,
   and descent. Treat the theorem as conditional on quartic unless that
   hostile review has independently confirmed it.
2. For `(2,5)`, derive the full normalized quintic and constant Jacobian row,
   verify every allowed target shear and constant, recompute the `y=0`
   expression and its uncancellable `3*rho^5/8` pole, and check the final
   polynomial unit-product contradiction including `h`, zero factors, and
   constant branches.
3. For `(3,5)`, independently recompute (3.1), the invariant (3.2), and the
   constant row. Attack the weighted finite-pole argument, including
   fractional valuations, the `q=s` step, all possible ties, the four leading
   equations, and the exact subresultant `441`. Verify polynomiality of
   `rho,A,B` without assuming it.
4. Audit the Weierstrass-cubic step in `(3,5)`: completion of the square,
   distinct-root UFD argument, every repeated/triple-root case, the
   parametrization by `R`, and direct substitution into the constant row.
   Recompute `deg Psi=6` and leading coefficient `-epsilon*35/27`; seek a
   singular branch or cancellation that permits a unit.
5. For `(4,5)`, independently derive the depressed normal form, both exact
   first integrals `I_2,I_1`, and the constant bracket. Recheck all signs and
   factors against direct symbolic differentiation.
6. Attack the weighted `(2,3,4)` pole lemma. Prove or refute that every
   nonzero initial point has `C!=0`, justify `q=s`, derive all four depression
   leading equations, exhaust `b=0` and `b!=0`, and independently verify the
   resultant `-12180258816`. Check that no lower-weight constant or valuation
   tie was dropped.
7. At polynomial infinity, exhaust all initial branches of the two
   invariants and recompute the degree `8q-1` coefficients of the bracket.
   Verify they cannot cancel with lower-weight terms and that `h*j` being a
   unit yields the claimed contradiction. Audit the Laurent controls as
   negative tests, not proof substitutes.
8. Verify the exact theorem over every characteristic-zero field and the
   scoped AS109 consequence: if the theorem and its quartic dependency both
   hold, an exact lift cannot have both correction `y`-degrees at most five.
   Make no JC2 or novelty inference. Check accessible local priority material
   only for attribution hygiene.

Try hard to produce an exact counterexample or the smallest missing
hypothesis. Do not edit producer/canonical files, start sextic work, or launch
AWS.

Write exactly one file:

`xmodel/quintic-y-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
full hashes, independent algebra/replay, dependency status, descent and scope
caveats, and promotion advice.
