# Hostile different-model review — AS109 A_INFINITY / DECK DESCENT

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer/review artifacts on top.

Read in full:

- `xmodel/as109-ainfinity-deck-descent-gate-20260824.md`
- every file under `cases/as109_ainfinity_20260824/`
- the predecessor Hensel-to-degree producer and its running/completed review
- the dual-confirmed Hensel/carry and secant-idempotent materials

Frozen hashes:

- report: `f1cf4991e92e502459ca6c61a3cb4d0e346a65e6221890c8c64a808ec2e3b64b`
- replay: `84941b672e04fab735b5de31f39de28487672167d233caeffa08870a57665b7f`

Independently rerun the replay and attack exactly:

1. Audit the formal fibre algebra
   `B=R[X,Y]/(P-pS,Q-pT)`, `R=Z_p[[S,T]]`: etaleness,
   finite presentation/quasi-finiteness, and the exact split special fibre.
   After height-one localization/completion, prove or refute that precisely
   the p=109 simple generic roots with both source coordinates integral are
   the Hensel lifts of `(a,0)`, while every residual root has a negative
   source valuation.
2. Prove or refute
   `dim A_infinity=d-p=sum_{min(w_x,w_y)<0} mult_w(I)` using the correct
   valued tropical/initial-ideal theorem for a fixed zero-dimensional simple
   system. Check axes, torus saturation, geometric versus residue degrees,
   multiplicities, and whether the proposed finite support test really is
   finite and exact. Do not replace fixed-coefficient multiplicity by generic
   mixed volume.
3. Verify the implication `B finite over R => rank p => d=p`, and attack the
   negative Zariski-Main control `R^p x R[1/p]^r`: finite presentation,
   etaleness, special fibre, and arbitrary generic rank. Check exactly what it
   rules out under general etale data and what it does not model about a
   polynomial Keller extension.
4. Recompute the Newton polygon of
   `g_N=X-X^p+pX^N-pS`, all root valuations and multiplicities, residual rank
   `N-p`, and non-Keller status. Independently prove or refute triviality of
   its rational deck group for `N>=p+2`, including the unique-pole/Mobius and
   coefficient comparisons.
5. Audit the self-fibre/deck graph equivalence in
   `C_L=L tensor_M L`. Check that an L-linear factor is exactly a rational
   deck automorphism. Enforce the producer's correction: one off factor or
   one `0->1` branch match does **not** give a p-cycle. Verify that a descended
   full p-cycle implies `p|d`, and with `A_infinity=0` implies a Galois
   degree-p extension; check the invoked classical Galois Keller consequence
   and Hensel contradiction.
6. Attack every trace, idempotent, secant, and monodromy no-leverage claim.
   In particular distinguish formal permutations of `E^p` from automorphisms
   of `L/M`, and check the normalizer/orbit interpretation. Identify any
   smaller descent criterion that the producer missed.
7. Decide the exact campaign utility: a fixed-support negative-weight
   discriminator and a separate finite graph-factor/p-cycle test, not an
   automatic lift obstruction. Verify all scope exclusions and dependency on
   the predecessor degree theorem.

Try hard to find a completion, tropical-multiplicity, or deck-group error.
Do not edit producer/canonical files, implement the support compiler, or
launch AWS.

Write exactly one file:

`xmodel/as109-ainfinity-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
full hashes, independent algebra/replay, dependency and valued-field caveats,
exact scope exclusions, and promotion advice.
