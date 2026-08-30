# Hostile review: cubic one-place Euler obstruction

You are GPT-5.5 acting as a fresh hostile reviewer for the plane Jacobian-
conjecture campaign. Work in `/Users/dc/code/math/jc2`. Reconstruct the proof
independently and actively seek a counterexample. Do not modify charged
inputs, Git state, canonical ledgers, or unrelated files. Do not read any
sibling external-model prompt, log, report, or receipt. Do not inspect, list,
search, stat, build, modify, or control `jc2-lean`.

Hash-check and audit only these charged files:

```text
8b457a752434ac0c7cb6a2a83dd680b4a66dbe3631ab761c43dc789965ff2d2d
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-sol56-20260830.md
f98149567b865f15a97b1e53c8f1ccd15fde116292e2d0c64a2935d3c45d95ae
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-sol56-20260830.md.artifact.json
931afe2d89c890d841575780bf66c3625ae54e7aa51a275ef6f27da7fb0955f2
  ops/block_descent_a1_cubic_euler_replay.py
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d
  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
b72e39220f9e8d75e94214d2e5669bda072fcbbd644cfed97f97d9a2b820ad57
  xmodel/block-descent-a1-euler-ledger-sol56-20260830.md
```

Audit each load-bearing step.

1. Check Nguyen Van Chau's published theorem from its primary source. Keep
   distinct: polynomial parametrization of each `A_F` component, one
   set-theoretic infinity point of the whole possibly reducible `A_F`, and
   one analytic place. Verify that every irreducible component of
   `B=g2(R)_red subset A_F` is an entire `A_F` component and has
   normalization `A1`.
2. For a finite-flat rank-three morphism to a smooth complex surface, prove
   or refute the local fibre criterion used to show that every branch value
   has exactly one reduced source ramification point. Audit singular points
   of normal `Y`, totally ramified fibres, residue fields, and reduction.
3. Decide whether `R_red->B_red` is genuinely finite and point-bijective at
   every closed point, hence a proper analytic homeomorphism. Do not upgrade
   it to a scheme isomorphism. Check component birationality and normalization
   transfer.
4. Reconstruct the affine incidence multigraph of `R`. Verify that embedded
   resolution over a possibly singular normal surface makes it a minor or
   subdivision of the actual morphic SNC boundary forest. Retain self-loops,
   parallel edges, affine singularities, unibranch cusps, exceptional
   clusters, and deleted infinity vertices. Re-derive
   `e_c(R)=b0(R)>=1` by normalization additivity.
5. Recompute the cubic Euler equations and the conclusions: `C=P1` empty;
   `C=A1` forces `b0(B)=1`, `S0=empty`, `Q=0`. Check the meanings of
   connectedness, an unramified sheet over every target, and one reduced
   `A1` component per ruling fibre.
6. Attack the degree-four `(2,2)` control and all target-conductor escapes.
   Confirm that the theorem is rank-three-only and does not exclude the
   surviving affine-base block, existence of a block, a map, or JC2.
7. Rerun the exact replay under ordinary, `-O`, and `-OO`; reproduce its
   source/output behavior, zero-assert guard, and both mutations. State which
   geometric and cited-theorem claims are not software outputs.

Return itemized `CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or `REFUTED`,
then a maximum-safe theorem and cheapest useful successor. This review makes
no exit-price assertion: emit no `charge_basis={...}` line; receipt status
`ABSENT` is expected. Do not run heavy local CAS.

Write exactly one report and no other file:

```text
xmodel/block-descent-a1-cubic-one-place-euler-obstruction-hostile-review-gpt55-20260830.md
```

End it with one standalone `<!-- BODY-END -->` line and no seal block.
