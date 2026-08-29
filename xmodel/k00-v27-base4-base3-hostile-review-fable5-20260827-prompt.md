# Hostile different-model review: K00 V27 rank filtration R1/R2/R3

You are Fable 5, acting as a hostile exact-algebra reviewer.  Review the three
frozen producer reports, in dependency order:

1. `cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/RESULT_V27_BASE4_R1_EXACT_PREPASS.md`
   SHA-256 `19c8795589ce076c2414474a6341c7929d578958ea122a6745f26ea6ab46bd9c`
2. `cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/RESULT_V27_BASE3_R2_EXACT_PREPASS.md`
   SHA-256 `c42c0482f0b5861f5099e6e121c60a93d018c87a9619749ee1844f5954545c39`
3. `cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/RESULT_V27_BASE2_R3_EXACT_PREPASS.md`
   SHA-256 `5f9700c7e67eaa5255ef642ff4e784983d71da9f8c5394d6cb01245c9c0a873d`

Their review manifests have SHAs `41d1107589f33b7f7fab4ec5cac6e47f...`,
`e3cd6586c2db1b51aabedb613f3de5a1...`, and
`86c561915a5336792674c7c7c3fd5e181d626b470ae9a4302166dad824adadcd`;
verify the full bytes from the reports rather than trusting
these abbreviated reminders.

Write exactly one report to

`xmodel/k00-v27-base4-base3-base2-hostile-review-fable5-20260827.md`

and edit nothing else.  Do not enter or inspect `jc2-lean`.  Heavy algebra is
AWS-only.  A desk-scale independent parser/replay is allowed only if it stays
small; the frozen Singular replays may be inspected and, if needed, executed
on an audited idle AWS node.

Required audit:

1. Rehash every source/evidence/portable manifest and verify path coverage.
2. Reconstruct the exact `7 x 7` matrix `A`, base ideal `B`, and every literal
   `6 x 6`, `5 x 5`, `4 x 4`, `3 x 3`, and `2 x 2` determinant from the frozen atlas.
   Verify total/nonzero/distinct censuses and row/column-label completeness.
3. Independently prove or refute both containments
   `I4(A) subset B+I5(A)` and
   `I3(A) subset B+I5(A)+I4(A)`, including all 594 and 813 stored nonzero
   minors, without trusting status strings or a prior standard basis.  Then
   verify all 351 stored nonzero `I2(A)` normal forms, the claimed outside
   count 237, and the strict ideal cut `J1 != J2`.
4. Replay all three tracked transform identities, recompute
   characteristic-zero standard bases afresh, and rederive properness and
   affine dimensions three, three, and two at the stated stages.  Verify the
   claimed byte-identical nine-element basis only as custody, not as proof.
5. Replay the deletion, transform, forced-unit, known-proper, census,
   source-freeze, cap, and zero-swap controls.  Audit the R0 census failure and
   confirm it cannot contaminate R1/R2.
6. Check the coordinator's scope correction: since the ideal is homogeneous,
   does the origin give a trivial rational point?  If so, state that the next
   useful point target must be nonzero/projective and satisfy the necessary
   source open/full-`P6` compatibility; a bare `Q`-point is not informative.
7. Audit the producer's refusal to infer distinct radicals or a rank-exact-two
   geometric point from `J1 != J2`.  Specify the correct next one-minor
   discriminator `J2+(z*m-1)` and its exact interpretation; do not launch it.

Verdicts must distinguish `CONFIRMED`, `CONFIRMED WITH REPAIR`,
`PROVISIONAL`, `REFUTED`, and `SCOPE-CONFLICT`.  State exactly what may be
promoted and forbid every inference to full `P6`, later grades, an arc,
receiver, order two, maximum twelve, a counterexample, or JC2.  End with the
output path, SHA-256, exact model identity, checks run, and scope firewall.
