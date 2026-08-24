# Hostile different-model review — bounded partial-`y` degree six synthesis

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
artifacts on top.

Read in full:

- `xmodel/as109-bounded-y6-chain-audit-20260824.md`
- every file under `cases/as109_bounded_y6_chain_audit_20260824/`
- every producer and landed hostile review named in its trust-state matrix
- the now-landed leaf reviews
  `xmodel/as109-sextic-46-closure-review-grok-20260824.md` and
  `xmodel/as109-sextic-56-exclusion-review-grok-20260824.md`

Frozen synthesis hashes:

- report: `1078bbdd47ccf085900b93b165ee268d314d2cc4e387b30ad81c4a40817e12f3`
- replay: `5c57325e602e2ef13f87f87fd50bc33e368117abf060576936bc7f7e8460df57`
- freeze: `2a94df9f42fb2d5e6c4609971cdbf5d23999d7bacd1f0aca3c2dff76bf4110dd`

New leaf-review hashes:

- `(4,6)` review: `183ad7d6eab8b9f74041c2eb7d29180b2c75a4bc84d82bfeb681f29a55b9c32c`
- `(5,6)` review: `d7b4f0e033f63f5e8f1f62b44f98ae23b566071cd34c810c18199cd099f88b70`

Independently rerun the coverage replay and attack exactly:

1. Verify the field statement uses **actual partial `y`-degrees**, not total
   degrees or a generic-coordinate convention, and that all target/source
   operations preserve the needed automorphy implication.
2. Re-derive the top Jacobian equation
   `n*a_m'*b_n-m*a_m*b_n'=0`. Check the equal-degree `GL_2` reduction,
   divisible-degree target shear, degree-zero cases, and affine-in-`y`
   reduction over an arbitrary characteristic-zero field, including all
   constant-leading-coefficient cases.
3. Independently enumerate all 28 unordered and 49 ordered degree pairs.
   Verify termination of recursive reductions and that maximum six has only
   the genuine leaves `(4,6)` and `(5,6)`. Scrutinize `(6,6)`: one target
   `GL_2` operation must lower exactly one actual degree and leave no hidden
   third sextic case.
4. Audit every dependency and hash. Confirm that each lower-degree leaf and
   the sextic normal-form skeleton has an applicable landed review and that
   the two new leaf reviews really discharge their exact hypotheses. Do not
   treat producer PASS strings as substitutes.
5. Verify descent from an algebraic closure to an arbitrary
   characteristic-zero field, both for nonexistence strata and for polynomial
   automorphy after reductions.
6. Check the conditional AS109 corollary: coordinate `y`-degrees equal the
   correction bounds for the fixed seed, automorphy conflicts with the
   reviewed Hensel noninjectivity, and the correct conclusion is only that
   every exact lift has at least one correction of `y`-degree `>=7`.
7. Enforce scope. The theorem is bounded partial degree only. It is neither
   an arbitrary-support AS109 no-go nor a JC2 decision, and it makes no
   novelty or priority claim. Note separately any simpler known theorem that
   subsumes part of the pair table, without replacing the dependency audit.

Use an independently written enumeration or hand audit as well as the frozen
replay. Try hard to find a missing pair, a bad UFD/root extraction, a
constant-field descent error, or an illicit partial-to-total-degree switch.
Do not edit producer/canonical files or launch AWS.

Write exactly one report file:

`xmodel/as109-bounded-y6-chain-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hashes, exact dependency status, scope exclusions, and promotion advice.
