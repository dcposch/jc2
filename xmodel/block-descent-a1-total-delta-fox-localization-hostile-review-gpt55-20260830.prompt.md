# Hostile review: total-delta and Fox/localization quartic obstructions

You are GPT-5.5 acting as a fresh hostile reviewer for the Plane Jacobian
Conjecture campaign. Work in `/Users/dc/code/math/jc2`. Reconstruct every
claim independently and seek explicit counterexamples. Do not modify charged
inputs, Git state, canonical ledgers, or unrelated files. Do not read any
sibling external-model prompt, report, `.log`, `.run`, or receipt. Do not
inspect, list, search, stat, build, modify, or control `jc2-lean`.

Hash-check and audit only these charged repository files:

```text
03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa
  xmodel/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md
6d495706aaab256710a263681816dfab6b9c562f163aa9efe11dd4a025429a00
  xmodel/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md.artifact.json
f5438492f6092eaa032371fdecf3215dca1a74aea67dd53b53dbe3e983166923
  ops/block_descent_a1_total_delta_two_iterated_knot_s4_replay.py
60ba8f433f4ecd98ead9820dc627c9a88f927851d3289af07de2c68b005824a0
  xmodel/block-descent-a1-quartic-double-plane-fox-localization-kernel-sol56-20260830.md
5e628a08e5d3cedbdbb657d7df64dc5aede5d40f1c2ca93c7557faff70417921
  xmodel/block-descent-a1-quartic-double-plane-fox-localization-kernel-sol56-20260830.md.artifact.json
a83e110935c96f934b80b61a2cd5a2323d4f6cbfd3212004b3be4b3256b5b39c
  xmodel/block-descent-a1-quartic-double-plane-constant-unit-pic3-reduction-sol56-20260830.md
43c83d47d864537aae6fec7203111aaa3c6c52fa4bbc0e95c6877c61aa86ad57
  xmodel/block-descent-a1-quartic-cycle0-polynomial-link-obstruction-sol56-20260830.md
c61f0cebdc06bdca88ad76f3714047a1998ff7aeb885a79e84b060a091c23329
  xmodel/block-descent-a1-one-ordinary-node-all-degree-meridional-rank-obstruction-sol56-20260830.md
```

Use the primary sources cited inside the artifacts when needed. Fetch them
only into a temporary directory, record exact bibliographic interfaces, and
do not substitute later summaries for the cited theorem statements.

Audit these load-bearing points:

1. Starting from an irreducible affine plane curve with normalization
   `A1`, verify that a small good nearby fibre has one boundary component and
   genus exactly the sum of the affine delta invariants. Check the corrected
   Neumann--Rudolph goodness hypothesis and rule out missing vanishing cycles
   at infinity or disconnected nearby fibres.
2. Verify that one normalization place at infinity makes the infinity knot
   an iterated cable of the unknot and hence prime or trivial. Check the exact
   rooted-splice/cabling theorem and whether affine self-identifications can
   produce a connected-sum infinity knot.
3. Reconstruct the complete genus-zero, genus-one, and genus-two graph-knot
   census. Check all winding/sign conventions and the genus and determinant
   of the `(2,+/-1)` cable of a trefoil.
4. Prove or refute the determinant lemma: a transitive meridian-
   transposition representation to `S4` forces a quotient
   `pi1(Sigma_2(K))->A4` and hence `3|det(K)`. Check the passage from the knot
   group to the branched-cover group and the boundary-to-affine group
   surjection.
5. Rerun the replay ordinarily and under `-O` and `-OO`, reproduce the
   mutation failure, and independently check the `T(3,4)` coloring. Separate
   what the replay proves from the cited topology interfaces.
6. Audit the constant-unit/Kummer reduction on the possibly singular double
   plane `D={s^2=q}`: normality, the Kummer exact sequence, constancy of units,
   anti-invariance, and the identification with `Pic(D)[3]`.
7. Reconstruct the exact localization kernel
   `Pic(D)[3] = ker[H1(U,L_sign) -> sum H1(M_p,F3)]`. Check extension across
   smooth ramification, isolated singular links, local-coefficient actions,
   and whether an anti-invariant or quotient qualifier is missing anywhere.
8. Verify the infinity injection and Fox/double-branched-cover identity.
   Decide whether `3` dividing the determinant is only necessary, and audit
   the trefoil tangency control and the claimed infinite false-positive
   family by exact algebra and group relations.
9. Check that combining the two artifacts licenses precisely the exclusion
   of irreducible `A1`-normalized quartic horns with total affine delta at
   most two. Test whether the `T(3,4)` delta-three control really fails the
   local `C2` gate and whether any reducible, multi-place, or non-simple lane
   was accidentally included.
10. Give the strongest safe successor theorem. In particular, decide whether
    the remaining higher-delta global-overlap kernel can be attacked by a
    general Alexander-module, splice-diagram, or singularity-localization
    argument, and state the cheapest exact falsification test.

Return itemized `CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or `REFUTED`,
then a maximum-safe theorem and a concrete successor. This review makes no
exit-price assertion: emit no `charge_basis={...}` line; receipt status
`ABSENT` is expected. Do not run heavy local CAS.

Write exactly one repository file:

```text
xmodel/block-descent-a1-total-delta-fox-localization-hostile-review-gpt55-20260830.md
```

End it with one standalone `<!-- BODY-END -->` line and no seal block.
