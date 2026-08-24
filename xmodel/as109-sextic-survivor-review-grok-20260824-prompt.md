# Hostile different-model review — AS109 sextic `(4,6)` survivor discriminator

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer/review artifacts on top.

Read in full:

- `xmodel/as109-sextic-survivor-discriminator-20260824.md`
- every file under `cases/as109_sextic_survivor_discriminator_20260824/`
- the frozen sextic-frontier producer and its review, if the review has landed

Frozen hashes:

- report: `b2f6a16eb8399d4de408c41070c666000b324409a5332fa211eff011b5624552`
- replay: `d2c29ef530f7bd3aa511d245db2f9fb6eb72cfb001f5dc14d92b74c16345723f`
- freeze: `6bdf4935fb32a3506c32a19167c65ecf675f13cefe77ae1ab240510ee5cc99e7`

Independently rerun the replay and attack exactly:

1. Re-derive the common depressed normal form for both `kappa=0` and
   `kappa!=0`, including the quadratic algebraic differential extension,
   the meaning of constant `L`, and every hidden division/zero case.
2. Recompute all eight Jacobian rows, the five integrations for `P,...,T`,
   and the two first integrals `I_2,I_1`, including all constants and the
   chain-rule factor `h`.
3. Verify the `U=A^2-4C` complete-intersection equations `J_2,J_1`, the
   one-form `eta`, and the claim that no intermediate Pfaffian row remains.
   Check singular components, dimension jumps, or cases lost by coordinate
   changes.
4. Independently derive both `y=0` polynomial boundary equations after
   `q=r^2+A/2`. Audit which variables/functions must be polynomial and which
   live only in the algebraic function-field extension.
5. Recompute the weighted compactification and prove or refute that there is
   exactly one infinity point `[r:q:B:U]=[1:0:0:0]`, with square/cube
   compositional initial form. Look for missed weighted charts/components.
6. Audit the `L=0` plane reduction, the closure of the two stated line
   families, the degree-eight resultant and unit square/nonsquare argument,
   and the nonlinear rational control. Ensure the control is not being used
   as a Keller solution.
7. Verify hashes, deterministic replay, and scope. The admissible conclusion
   is an exact algebraic survivor only: no degree-`<=6` theorem, no stronger
   AS109 degree floor, no lift/counterexample, and no JC2 decision. State the
   smallest valid next gate, preferably local normalization/Puiseux analysis
   over the unique infinity point using both boundary equations and `eta`.

Try hard to find a sign error, missed branch, illegal algebraic extension,
false dimension assertion, or boundary equation that fails to descend.
Do not edit producer/canonical files, continue the Puiseux successor, or
launch AWS.

Write exactly one file:

`xmodel/as109-sextic-survivor-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
full hashes, independent algebra/replay, dependency status, exact scope
exclusions, and promotion advice.
