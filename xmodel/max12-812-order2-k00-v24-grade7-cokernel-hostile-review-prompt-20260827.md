# Hostile review request: V24 exact grade-seven compatibility block

Audit V24 independently and fail closed.  Write the final review to

```text
xmodel/max12-812-order2-k00-v24-grade7-cokernel-hostile-review-20260827.md
```

Do not edit canonical ledgers.  Do not touch `jc2-lean`.  Heavy algebra must
run only on AWS.  A PASS must remain at the narrow chartwise grade-seven
scope below.

## Charged producer

- report:
  `cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827/RESULT_V24.md`
- preregistration:
  `cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827/PREREGISTRATION.md`
- compiler and runner in the same case directory
- frozen harvest:
  `cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827/aws_r6b_pass/`
- exact compatibility artifact SHA256:
  `4f4c2bac49270fdd220e2333fbf82ba8bd4cc507cff90ea3eb8c2bf8c614ddd2`
- exact left-basis SHA256:
  `6c857c91220965ee25d4483b122277c174a0dc0b9f740311fce02390b92893e1`
- exact inhomogeneous-vector SHA256:
  `dc7696e1c1552533418eba1f91e14227ef8663aeded38b111d3295d1afb3f289`
- RESULT JSON SHA256:
  `22cbd6acb79fc5788afc4b1220cc9eaa19d0a987a2126a49eace67e89ce7921b`
- evidence-manifest SHA256:
  `8fedd7c3ea3c693679b1fa96a9ebce849c0455c44021cb86ad699bc8592b7c60`

## Mandatory independent checks

1. Rehash every charged input, source-freeze entry, and every endpoint
   evidence entry.  State counts and any self-listing issue explicitly.
2. Independently parse the seven normalized unloaded rows and K10 loads.
   Reconstruct the literal coefficients through Lambda grade seven after
   imposing the honest boundary `k6_0=0`.  Compare the grade-seven newest
   matrix byte-for-byte or coefficientwise with V23 and independently
   replay the frozen V20R2 literal DAG.
3. Recompute V23's rank-five witness `W`.  Verify the chosen five pivot rows
   and columns are invertible on `D(W)`, and verify that all required
   rank-at-most-five identities used from V23 are exact.  Do not infer rank
   merely from the displayed determinant.
4. Independently derive the two Cramer left covectors.  Verify all fourteen
   entries and all seven column-annihilation identities coefficientwise.
   Explain why they span the complete left kernel after localizing at `W`.
   Apply a sign/minor mutation and require it to fail.
5. Independently reconstruct the grade-seven inhomogeneous vector `b` and
   re-contract it.  Compare both 110,117- and 83,298-term compatibility
   polynomials exactly, preferably by a second implementation or exact
   coefficientwise hashes.  Prove, rather than assert, that on `D(W)` their
   vanishing is necessary and sufficient for the seven linear newest-
   coefficient equations to be solvable.
6. Replay the two modular normal forms, but keep them strictly diagnostic.
   The producer did not test whether the localized prior ideal is proper;
   therefore reject any claim that modular zero proves genuine membership
   until the separate properness repair lands.  In no event infer exact-Q
   membership merely from one prime.
7. Check all type boundaries: normalized `C6=1`, valuation-one source,
   `k10_0!=0`, `W!=0`, prior rows/grades 2..6 and `F10=0`; distinguish the
   coefficient name `C6` from the compatibility-polynomial label `C6`.

## Allowed adjudication

A PASS may certify only this statement: conditional on the complete honest
prefix and on `D(k10_0*W)`, the exact literal grade-seven newest-coefficient
system is solvable iff the two frozen exact compatibility polynomials vanish.
It may not certify chart nonemptiness, modular or exact membership in the
prior ideal, the `W=0` locus, later grades, a full jet/arc, closure incidence,
order two, maximum twelve, or JC2.
