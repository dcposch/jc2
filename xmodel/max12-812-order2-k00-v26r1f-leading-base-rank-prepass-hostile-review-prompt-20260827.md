# Hostile review: V26R1F exact leading-base rank-`<=4` survivor

You are the nonproducer hostile reviewer.  Assume every prose claim is wrong
until independently reconstructed from frozen bytes.  This review is narrow:
it must not edit canonical ledgers, launch descendants, or infer an arc,
closure statement, counterexample, or JC2 result.  If you execute nontrivial
algebra, run it only on registered AWS capacity, one core, with an explicit
cap.  Touch the requested output file early and keep it fail-closed.

Write only:

`xmodel/max12-812-order2-k00-v26r1f-leading-base-rank-prepass-hostile-review-20260827.md`

## Claimed result to audit

Producer report:

`cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/RESULT_V26R1F_EXACT_PREPASS.md`

Expected SHA-256:

`86742147085332881b3c44ba041172ac5a032d656df3992ceff5da7d0a5b46dc`

The claim is that in
`Q[d0_1,d1_1,d2_1,d3_1,d4_1,d5_1]`, for the frozen `7 x 7` matrix `A` and

`B=(G2_row1,G2_row2,G2_row3,G2_row4,G2_row5,G2_row7,F10)`,

all `6 x 6` minors of `A` vanish, the `5 x 5` minor list is nonzero, and
`B+I5(A)` is proper of affine dimension `3`.  Thus only the six-variable
leading-base rank-`<=4` locus is proved nonempty.  The result is explicitly
`PROVISIONAL_ROLLBACK_TAG_OPUS5_PENDING` because its interpretation as the
`W=0` descendant depends on an upstream cross-audit that has not landed.

## Frozen inputs and evidence

- held compiler output:
  `cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/aws_box02_r2_held_compile/output/`
- exact polynomial source:
  `ATLAS_EXACT_POLYNOMIALS.json`
- exact job specification: `EXACT_Q_JOB_SPECS.json`
- compiler result SHA:
  `f1a6f1fc988fc77816daaab13b294b1321de7e476d2891cf7fbfa2e033868d97`
- R1F output:
  `cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/aws_box02_r1f_exact_prepass/output/`
- R1F result SHA:
  `f455c7b2177eb260df2ebfa97f174381591792683c80fdeb779f1184f6e6d70e`
- AWS evidence SHA:
  `f012cc1ad1b1e01ad2dbd93b718861951852c9ee9cda0fd87ddeb58983646e17`
- portable harvest manifest:
  `cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/HARVEST_REPLAY_R1F.sha256`
  with SHA
  `a9933ef5779411e7508b48c926506744ec47d5f67637658e16eeebd748545e9f`
- R1F source freeze:
  `cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/SOURCE_FREEZE_R1F_FULLY_ENTRYWISE_REPLAY.sha256`
  with SHA
  `3d04cc180e653736d4d0cf677b942f62894f02877a4a8a86804769286aaaaa06`
- notation custody:
  `cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/NOTATION_CLARIFICATION_R1_GRADE2_ROWS.md`
- history errata R1B through R1E in the same case directory.

## Mandatory independent checks

1. Rehash the report, source-freeze chain, compiler manifest/result, portable
   harvest manifest, result, basis, transform, scripts, stdout, and stderr.
   Note that the original AWS evidence manifest uses absolute producer paths;
   adjudicate whether the portable additive manifest closes local custody.
2. Independently parse `ATLAS_EXACT_POLYNOMIALS.json`.  Verify the ring has
   exactly the six leading variables, `A` is `7 x 7`, and the base-generator
   source map is literal rows `(1,2,3,4,5,7)` plus `F10`.  Reject any silent
   use of the logical zero row 6 as literal row 7.
3. Recompute all `6 x 6` and `5 x 5` minors from the frozen `A`.  Test each
   zero/nonzero assertion entrywise; direct ideal/matrix comparison with
   scalar zero is forbidden.
4. Reconstruct `J=B+I5(A)` independently over exact `Q`.  Verify the producer
   preflight reports properness, normalized generator count `9`, and
   dimension `3`, with no error or standard-basis warning.
5. From serialized bytes, verify entrywise `matrix(J)*T=matrix(Graw)`.  Then
   independently recompute `G=std(Graw)`, reduce every generator of `J`
   modulo `G`, require every entry zero, and derive `NF_G(1)=1` and dimension
   `3` only from this recomputed standard basis.  This must establish both
   ideal inclusions; do not trust a lost `isSB` attribute.
6. Replay the transform-entry deletion, forced-unit, and nonzero-`I5`
   deletion controls.  At least one exact identity must fail after its
   registered mutation.
7. Inspect R1B/R1C/R1D/R1E.  Confirm each is a pre-algebra or validator
   failure and that R1F, not an earlier marker, is the only consumed endpoint.
8. Decide explicitly whether the intrinsic `B+I5(A)` algebra uses the `W`
   syzygy.  Separately enforce that calling it the honest `W=0` descendant
   remains rollback-tagged until the pending Opus5 V24R6R1 audit is
   adjudicated.
9. Try to falsify every overreading: a rational point, rank-exactly-5
   nonemptiness, full-`P6` compatibility, rank-atlas coverage, later grades,
   Lambda/source/Jdet reachability, arc existence, closure, counterexample,
   or JC2.  None is claimed.

## Required verdict

Return `PASS`, `FAIL`, or `GAP`, with a short theorem statement you believe is
actually proved, exact hashes you replayed, any custody defects, and an
explicit lifecycle recommendation.  A pass may cover only the intrinsic
six-variable exact rank-locus theorem.  It must retain the rollback/Opus-
pending label on the `W=0` descendant interpretation.
