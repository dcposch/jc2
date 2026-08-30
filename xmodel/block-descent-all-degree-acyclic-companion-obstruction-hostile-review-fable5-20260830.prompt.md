# Hostile review: all-degree acyclic-branch companion obstruction

You are Fable 5 acting as an independent mathematical co-researcher and
hostile reviewer for the plane Jacobian-conjecture campaign. Work in
`/Users/dc/code/math/jc2`. Reconstruct every implication rather than trusting
the producer summary, actively seek counterexamples, and report the maximum
safe scope. Do not modify charged inputs, Git state, canonical ledgers, or
unrelated files. Do not read sibling external-model prompts, logs, reports,
or receipts. Do not inspect, list, search, stat, build, modify, or control
`jc2-lean`.

Hash-check and audit only these charged repository files:

```text
28f29711366f58f4a1c9e6e5d7f16d8e6ca29fddf730bfd436100da04e4d2eda
  xmodel/block-descent-all-degree-acyclic-companion-obstruction-sol56-20260830.md
3d0b72c7001bf403fa334f746dd09a21d8a55fc8074f9b4680e249b92f73beb3
  xmodel/block-descent-all-degree-acyclic-companion-obstruction-sol56-20260830.md.artifact.json
a75a91d65f2f95766581edb5b6dcf4a8e958844a0e66987ec7d94c898800cb98
  ops/block_descent_all_degree_acyclic_companion_replay.py
41245c20b1b61a0dcf8116340672d037b977e6759d5d99054fc06c292d5c36fc
  refs/arzhantsev_zaidenberg_acyclic_curves_arxiv1110.3028v2.pdf
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d
  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
8ccb92fd3676e9f8b58e3ace4eb9157d0fa290ea24abc84d9913e94ec407e16d
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-coordinator-integration-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
b3bdd87cb27b614ca4bac476fd7f4c676b9551026397f3a895dbf84f4f195419
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-coordinator-addendum-sol56-20260830.md
```

Audit these load-bearing points:

1. Check Arzhantsev--Zaidenberg Theorem 1.3(b) and Corollary 1.2 from the
   pinned primary source. Verify exactly the connected comb/weighted-cone
   classification and the disconnected union-of-parallel-lines statement,
   including the meaning of “simply connected” for a disconnected curve.
2. Reconstruct the normal height-one inertia argument in arbitrary degree.
   Decide whether generic ramification really gives a nonidentity tame
   permutation and a generic unramified factor exactly gives a fixed sheet.
   Test the nonnormal conductor control and all residue-degree issues.
3. Verify the all-degree comb proof: complement presentation, central spine
   meridian, fixed-set centralizer lemma, line degenerations, based-meridian
   issues, and the absence of any illicit global companion label.
4. Verify the weighted-cone proof twice: first with a pointwise rank-one
   factor at the vertex; then with only generic companions and `e_c(U)>0`.
   Check the weights and direct radial deformation, constructibility and
   lower-semicontinuity direction of the etale fibre count, every Euler sign,
   and the sharp `w^4+a*w+b` zero-Euler control.
5. Reconstruct the disconnected parallel-line inequality. Use individual
   nontrivial cycle trees rather than treating a permutation's whole support
   as connected. Check transitivity, `sum(s_i-c_i)>=d-1`, special fibre
   drops, and the conclusion `e_c(U)<=-1` for all degrees.
6. Audit the canonical-normalization endpoint independently: finiteness,
   `S subset C[x,y]`, finite flatness, quasi-finite birational open immersion,
   avoidance of ramification, generic companion over every branch component,
   affineness/smoothness/rationality/units/log Kodaira dimension of `U`, and
   the ruling conclusion `e_c(U)>=1`. Identify any hidden use of `d1>1`.
7. Audit the generic-field-degree-three corollary: finite point-bijectivity
   `R_red->B`, the Chau/nonproperness component interface, source forest,
   compactly supported Euler census, `S0` finiteness, uniqueness of
   `h=1,S0=empty,Q=0`, contractibility, and application of the reviewed cubic
   monodromy theorem. Keep `B subset A(F)` distinct from equality and do not
   use Picard/Hartogs.
8. Rerun the replay ordinarily, with `-O`, and with `-OO`; reproduce stdout
   and payload hashes and the deliberate `--mutate-drop-centrality` failure.
   Separate bounded permutation checks from the arbitrary-degree geometry.

Return itemized `CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or `REFUTED`,
then a maximum-safe theorem, exact endpoint corollary, and cheapest useful
successor. This review makes no exit-price assertion: emit no
`charge_basis={...}` line; receipt status `ABSENT` is expected. Do not run
heavy local CAS.

Write exactly one repository file:

```text
xmodel/block-descent-all-degree-acyclic-companion-obstruction-hostile-review-fable5-20260830.md
```

End it with one standalone `<!-- BODY-END -->` line and no seal block.
