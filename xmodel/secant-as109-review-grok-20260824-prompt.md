# Hostile different-model review — SECANT-IDEMPOTENT x AS109

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer/review artifacts on top.

Read in full:

- `xmodel/secant-as109-cross-gate-20260824.md`
- every file under `cases/secant_as109_20260824/`
- the now independently confirmed parent and review:
  `xmodel/fresh-connection-gate-20260824.md` and
  `xmodel/secant-idempotent-review-grok-20260824.md`
- the banked AS109 Hensel bridge and carry erratum cited by the producer

Frozen hashes:

- cross report: `f4bd8ff7708469dd4ca1a6a6880634fb60ea2975fa1c7aa9fb3ecf5d61ba80cf`
- replay: `8024f629060624d86c88029452c8c4df85c0728a1e5388ae789965311c0ef98c`
- secant parent: `666bde51ea8bb78bd2c031122183148708b2b7de08547dc407191e633a712c4b`
- parent review: `6b0cb25dd3d1769f9f6c15116b6869b37c6cb1c89f17d9831ff19c67f20f09e9`

Independently rerun the replay and attack exactly:

1. Recompute the characteristic-109 seed collision ideal after `t=x-u`,
   the secant idempotent `e0=1-t^108`, the diagonal/off product, and the
   splitting of the off algebra into 108 sectors. Check all ordered-pair and
   rank counts and the CRT-projector formula; do not trust JSON labels.
2. Check what Hensel actually supplies for a hypothetical exact lift: analytic
   collision graphs/idempotents over the 109 residue balls, not bounded
   polynomial factors. Audit every trace/norm claim and distinguish the
   second-source and target-fiber decompositions.
3. Prove or refute the decisive redundancy claim on each off sector:
   `(f1,f2,e)_(x-u)=(f1,f2)_(x-u)` from the adjugate identity. Differentiate
   it scheme-theoretically at an off collision and verify that the `de` row
   has coefficient/tangent rank zero, including possible derivative/product
   terms and nilpotent concerns.
4. Audit the packed secant expansion and claim that its digit equations,
   including carries, cannot add an independent constraint when collision
   equations are already included. State the precise compiler hypothesis
   needed for that conclusion.
5. Independently check the triangular/tame controls and the growing-support
   all-Witt control through the registered levels. Check whether degree,
   support, factor count, trace, or norm gives any overlooked global bounded
   equation.
6. Decide the trichotomy at exact scope: `CONTRADICTION`,
   `NEW-FINITE-CONSTRAINT`, or `COSTUME`. Distinguish raw local secant-row
   redundancy from every possible global normalization/factorization use.
   No result may infer a lift, a characteristic-zero point, or JC2.

Identify the smallest failing hypothesis or overclaim. Do not edit producer
or canonical files and do not launch a support search.

Write exactly one file:

`xmodel/secant-as109-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
full hashes, independent replay/algebra, scope exclusions, and promotion advice.
