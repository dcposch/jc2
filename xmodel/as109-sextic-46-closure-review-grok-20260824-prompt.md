# Hostile different-model review — AS109 sextic `(4,6)` closure

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
artifacts on top.

Read in full:

- `xmodel/as109-sextic-46-local-normalization-gate-20260824.md`
- every file under `cases/as109_sextic_46_local_normalization_20260824/`
- `xmodel/as109-sextic-survivor-discriminator-20260824.md` and its landed
  different-model review
- the sextic-frontier preflight producer and its landed different-model review

Frozen child hashes:

- report: `587a142a09ac70805264f56ed408545fa6dd0b771d4712459fad6eddcf9902ac`
- replay: `a705526c12675d7fba0330f9f45d17db34d87a085f877b30bc6d73de81a7e404`
- freeze: `45134ff283f6cee97030f288ad9a1645d3f00f4b35e85fecf25c6610f1ff0aaa`

Independently rerun the replay and attack exactly:

1. Verify that the parent normal-form derivation and unique weighted-infinity
   point are now genuinely covered by landed reviews. Re-derive every child
   equation after the local substitutions; do not inherit them merely because
   the replay says PASS.
2. Audit the `L!=0` valuation proof for all rational Puiseux valuations,
   including zero/infinite `Q,Y,Z`, coefficient cancellations, and ramified
   local extensions.
3. Audit the `L=0` Newton strata. Prove the beta/non-beta and delta/non-delta
   tie tables exhaustive; search for missed equal-valuation faces and cases
   where a displayed leading coefficient can vanish.
4. Recompute the `beta=delta=0` shift and component split. Check the `k2!=0`
   valuation argument and every `k2=0` component, especially the nonlinear
   `AB^2=theta!=0` component, the use of both boundaries, and the monic
   quartic.
5. Attack the square/nonsquare descent: parity of `h,r,B`, descent and
   integrality of `K=B^2` and `M=hB`, every unit-product inference, and hidden
   zero cases.
6. Prove or refute the polynomial degree-cone classification for `L!=0` and
   each `L=0` stratum. Check that the claimed leading term of the pulled-back
   one-form is unique and nonzero and that constants exhaust the residue.
7. Verify hashes, exact replay, dependencies, and scope. The admissible result
   is closure of the actual `(4,6)` pair only after its reviewed parent; it is
   not by itself a `y`-degree-at-most-six theorem, an AS109 lift obstruction,
   or JC2.

Use a genuinely independent derivation or second engine wherever practical.
Try hard to find a missing Puiseux face, invalid descent, false integrality
step, or non-exhaustive degree cone. Do not edit producer/canonical files or
launch AWS.

Write exactly one report file:

`xmodel/as109-sextic-46-closure-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hashes, independent algebra/replay, exact dependency status, scope exclusions,
and promotion advice.
