# Hostile review: acyclic branch obstruction to a cubic block

You are Fable 5 acting as an independent mathematical co-researcher and
hostile reviewer for the plane Jacobian-conjecture campaign. Work in
`/Users/dc/code/math/jc2`. Reconstruct the theorem rather than trusting its
summary, seek counterexamples, and report the maximum safe scope. Do not
modify charged inputs, Git state, canonical ledgers, or unrelated files. Do
not read sibling external-model prompts, logs, reports, or receipts. Do not
inspect, list, search, stat, build, modify, or control `jc2-lean`.

Hash-check and audit only these charged repository files:

```text
5be2e2af32c0f6201637a652d28a0ff5f6992c5ebde696b1198d7b94e4829cf7
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-obstruction-sol56-20260830.md
5fd8b854452bf4e42a96ccaea89ca8b4be09310dc0cff424ae6dd0261392a455
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-obstruction-sol56-20260830.md.artifact.json
648022d35191b67d9f1e1eec61cddc95bbee745001410ad1fbbffa1044417389
  ops/block_descent_a1_cubic_acyclic_branch_monodromy_replay.py
41245c20b1b61a0dcf8116340672d037b977e6759d5d99054fc06c292d5c36fc
  refs/arzhantsev_zaidenberg_acyclic_curves_arxiv1110.3028v2.pdf
2e6d82035df6717d1a39f31dc19b23b7c727bb940d4730d2c7ea9400e5433cce
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-sol56-20260830.md
9e32b0fe8835b6ea6002036b95e2261a612754d73d796cb10edda347cf3cf65e
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-hostile-review-gpt55-20260830.md
8ccb92fd3676e9f8b58e3ace4eb9157d0fa290ea24abc84d9913e94ec407e16d
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
```

Audit these load-bearing points:

1. Check that the cited Arzhantsev--Zaidenberg Theorem 1.3(b) really covers
   every reduced connected simply connected plane curve, including reducible
   curves, and gives exactly the comb and weighted-cone forms stated. Check
   the hypotheses against the charged proper-cubic survivor rather than
   inferring contractibility from Euler characteristic alone.
2. Starting from a finite-flat integral cubic with fibre partition `(2,1)`
   at every branch value, reconstruct the henselian idempotent splitting at
   singular as well as smooth branch points. Decide whether the full local
   complement group fixes a companion and whether global complement
   monodromy is transitive.
3. Exhaust all connected degenerations of `y^epsilon p(x)=0`. For a genuine
   comb, verify the product complement, centrality of the spine meridian,
   its transposition image, and the `S3` centralizer argument. Pay attention
   to based meridians and do not smuggle in a common local label.
4. For the weighted-cone form, check the weights, the radial product, and the
   claimed isomorphism between global and origin-local complement groups.
   Repair the wording about open balls if needed. Decide whether the single
   local rank-one factor really forces the whole global image into `S2`.
5. Actively test edge cases: one line, one tooth, several teeth, axes,
   `a=b=1`, irreducible cusps, alternative meanings of one point/place at
   infinity, and the disconnected algebraic `S3` control from the prior
   review.
6. Check the exact proper-block interface. State whether the theorem closes
   only the promoted proper cubic block, what remains at degree at least
   four and in the primitive/no-proper-block horn, and whether any statement
   about JC2 itself follows.
7. Rerun the replay under ordinary, `-O`, and `-OO`; reproduce its payload
   and deliberate-mutation failure, and distinguish the finite permutation
   check from the geometric proof.

Return itemized `CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or `REFUTED`,
then a maximum-safe theorem and the cheapest useful successor. This review
makes no exit-price assertion: emit no `charge_basis={...}` line; receipt
status `ABSENT` is expected. Do not run heavy local CAS.

Write exactly one repository file:

```text
xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-hostile-review-fable5-20260830.md
```

End it with one standalone `<!-- BODY-END -->` line and no seal block.
