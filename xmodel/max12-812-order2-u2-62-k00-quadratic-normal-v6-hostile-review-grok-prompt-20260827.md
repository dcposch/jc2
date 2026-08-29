You are the hostile different-model reviewer for a small exact K00
normal-cone claim. Work in `/Users/dc/code/math/jc2`.

Producer:
`xmodel/max12-812-order2-u2-62-k00-quadratic-normal-v6-sol-20260827.md`
SHA-256:
`d7849d1af5dbb8f9e11db6563759a87c1e3a689cc51f15c9f7affc9257efeea3`

Replay:
`cases/max12_812_order2_u2_62_k00_quadratic_normal_v6_20260827/replay_k00_quadratic_normal_v6.py`
SHA-256:
`5e2f100de529cb3980fd9db08e74adae89cfcc60f5377d7c60bc67f6ed798835`

Independently parse the frozen tails and verify:

1. the K00 transverse coordinate substitution and the fact that all seven
   pure coefficient tails have zero constant and linear normal parts;
2. the seven quadratic term counts and, coefficientwise over `Q[C6,d0,...,d5]`,
   the three displayed identities for `Q5,Q6,Q7`;
3. that setting the scaled loads to zero is correctly scoped to the pure
   `Lambda=0` coefficient-normal slice, not silently a closure-first
   saturation or full normal-cone calculation;
4. the exact strategic consequence: quadratic `Phi7` gives no new class
   modulo odd rows 1 and 3, while higher normal/mixed Lambda-load order remains
   open.

Run the producer replay and also use an independent expansion or direct
coefficient check. Return separate `CONFIRMED`, `REFUTED`, or `GAP` verdicts
for the substitution/census, identities, and strategic scope. State the
smallest correction for any defect and whether the lemma is eligible for
`AUDIT.md` promotion.

Write the complete report to exactly
`xmodel/max12-812-order2-u2-62-k00-quadratic-normal-v6-hostile-review-grok-20260827.md`.
Touch no other campaign artifact. Do not enter, read, build, status-inspect,
or modify `jc2-lean`. Desk-scale exact checks only; no heavy local CAS, no
AWS launch, no web sweep, and no canonical-ledger edits.
