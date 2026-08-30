# Hostile review: rank-four branch topology and acyclic obstruction

You are Opus 5 acting as an independent mathematical co-researcher and
hostile reviewer for the plane Jacobian-conjecture campaign. Work in
`/Users/dc/code/math/jc2`. Reconstruct every claimed implication rather than
trusting the producer summary, actively seek counterexamples, and report the
maximum safe scope. Do not modify charged inputs, Git state, canonical
ledgers, or unrelated files. Do not read sibling external-model prompts,
logs, reports, or receipts. Do not inspect, list, search, stat, build, modify,
or control `jc2-lean`.

Hash-check and audit only these charged repository files:

```text
768cf08fe2be7a72e9e17cd15acd56976b6743cefa293bf11472a4fb4e701805
  xmodel/block-descent-a1-quartic-branch-topology-acyclic-obstruction-sol56-20260830.md
fddb00d108a229ccaf34b9a398f33f263d80831f73bba18c5f3a8019bb22db12
  xmodel/block-descent-a1-quartic-branch-topology-acyclic-obstruction-sol56-20260830.md.artifact.json
6326c5821a9b011f60021da54c133c19863b3593f75f91c211814335a1455b5b
  ops/block_descent_a1_quartic_branch_topology_replay.py
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d
  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
b72e39220f9e8d75e94214d2e5669bda072fcbbd644cfed97f97d9a2b820ad57
  xmodel/block-descent-a1-euler-ledger-sol56-20260830.md
c229cbc4eb93722eb9d5c247c5e0616901a0e5cfce0278613cffc7f9e4fcbe85
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-coordinator-integration-sol56-20260830.md
41245c20b1b61a0dcf8116340672d037b977e6759d5d99054fc06c292d5c36fc
  refs/arzhantsev_zaidenberg_acyclic_curves_arxiv1110.3028v2.pdf
```

Audit these load-bearing points:

1. Reconstruct the four fibre partitions and prove, or refute, that the
   reduced ramification-to-branch map has exactly one reduced preimage except
   for exactly two at `(2,2)` points. Check the quotient-graph homotopy claim,
   including self-identifications, parallel edges, singular branches, and the
   formulas `e(B)=h-n22` and `b1(B)=n22-h+k`.
2. Recompute the constructible Euler ledger
   `e(U)=4-2h-e(T31)-2n4` and its two ruling equations. Treat `e(T31)` as a
   signed constructible Euler number; do not infer positivity that is not
   proved.
3. Reconstruct the connected-acyclic obstruction. Check the comb centralizer
   argument and the weighted-cone global/local group identification. Most
   importantly, audit the Cohen--Macaulay parameter-multiplicity inequality
   used to prove that a generic ramified factor cannot lose rank on
   specialization, the direction of the resulting inequality for `u(z)`,
   and the conclusion `e(U)<=0`. Test the control
   `w^4+a*w+b=0`, its cusp discriminant, full `S4` monodromy, and `e(U)=0`.
4. Audit the transitive-subgroup argument forcing global monodromy `S4`.
   Check normal generation by divisorial meridians, the `D4` normal closure,
   the `A4` exclusion at `(2,2)`, and the disconnected `A4` Euler row. Look
   for overlooked local decomposition groups or allowed inertia types.
5. Reconstruct the normalized cubic resolvent. Check integrality,
   normality, finite flatness over the regular surface, equality of reduced
   branch support, and every row of the local fibre table. Pay special
   attention to the claim that `(2,2)` forces the full pair group rather than
   only its diagonal, and to the `(4)` collision/decomposition alternatives.
   Do not reason from a possibly nonnormal classical resolvent polynomial.
6. Determine the exact surviving rank-four horns and whether any actually
   falls to the promoted cubic theorem. Assess the proposed minimal
   `h=k=1,n22=b1=1` nodal one-place successor and name a cheaper decisive
   invariant if one exists.
7. Rerun the replay under ordinary, `-O`, and `-OO`; reproduce its payload
   and deliberate rank-drop mutation failure. Separate finite group/ledger
   checks from geometric proof.

Return itemized `CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or `REFUTED`,
then a maximum-safe theorem and the cheapest useful successor. This review
makes no exit-price assertion: emit no `charge_basis={...}` line; receipt
status `ABSENT` is expected. Do not run heavy local CAS.

Write exactly one repository file:

```text
xmodel/block-descent-a1-quartic-branch-topology-acyclic-obstruction-hostile-review-opus5-20260830.md
```

End it with one standalone `<!-- BODY-END -->` line and no seal block.
