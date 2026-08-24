# Hostile different-model review — AS109 sextic `(5,6)` exclusion

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
artifacts on top.

Read in full:

- `xmodel/as109-sextic-56-exclusion-20260824.md`
- every file under `cases/as109_sextic_56_next_gate_20260824/`
- the sextic-frontier preflight producer and landed different-model review

Frozen child hashes:

- report: `31420c0cd667640f340f4d127f185edd4515aac7df3733560e6d1fda5ec6c7a4`
- Python replay: `cab6e8597403f5c19d03fcf2da42c37ee3523ce7de2e825812ba1a5cbc47d5d0`
- Singular certificate: `0b0c36722f64365ddb0e1c891569124a658c86a77a967c415a5f41da631f61ca`
- freeze: `4c3fa8e19b2e5c9a2c8abb962d5c13427db4e7c45922a06b3081782c77920f9b`

Independently rerun both replays and attack exactly:

1. Re-derive the reviewed `(5,6)` normal form, which functions initially lie
   in `k(x)`, why `h` is a nonzero polynomial, all Jacobian rows, and both
   `y=0` boundary equations.
2. Recompute the new third-integral identity
   `dI1=omega-(2A/5)dI3`, including every coefficient and parameter. Audit
   whether it is valid at rank-drop points and whether constants of
   integration are handled correctly.
3. Independently derive the characteristic minors and the weighted binary
   Jacobian identity. Verify the common-factor lemma: its UFD step,
   characteristic-zero derivative argument, coprime exponents 5 and 6,
   monicity, and the depressed coefficient forcing the common linear form.
4. Audit finite-pole elimination. Check that regular values of both boundaries
   and all three integrals really yield a shared finite root of the two binary
   forms, that lower parameter terms vanish at the leading weight, and that no
   fractional valuation or zero-leading case is lost.
5. Recompute the zero-dimensional Singular certificates, including dimensions,
   lengths 126 and 42, and `r^21`; determine whether the filtered-finiteness
   prose is valid or unnecessary to the valuation proof.
6. Audit polynomial infinity. Check the weighted degree `q`, the assertion
   `H10!=0`, the coefficient `(6q/125)H10` at degree `10q-1`, possible
   cancellation from lower parameter terms, the inequality `10q-1>0`, and
   the constant-coefficient case.
7. Verify hashes, deterministic replay, dependencies, and exact scope. The
   admissible result is exclusion of actual `(5,6)` only; do not infer the
   full `<=6` theorem without independently confirmed `(4,6)` and chain
   coverage, and make no AS109/JC2 inference.

Use a genuinely independent derivation or second engine wherever practical.
Try hard to find a sign error, missing boundary, common-factor loophole,
rank-drop trajectory, or weighted cancellation. Do not edit producer/canonical
files or launch AWS.

Write exactly one report file:

`xmodel/as109-sextic-56-exclusion-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hashes, independent algebra/replay, dependency status, scope exclusions, and
promotion advice.
