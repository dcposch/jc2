# Hostile review — AS D7 exact Q9 source-state gate

Act as a hostile different-model mathematical reviewer in
`/Users/dc/code/math/jc2`. Treat every existing producer, case, canonical,
coordination, prompt, log, run, and review byte as immutable. Do not use Bash
or run any local computation. Read in full:

- `xmodel/as-fonly-d7-vertical-q9-source-state-gate-20260825.md`;
- every registration, source, manifest, aggregate, metadata, and
  representative shard/result file in
  `cases/as_fonly_d7_vertical_q9_state_gate_20260825/`;
- the divided-Frobenius erratum and corrected Q11/Q10 parents pinned by that
  case, only as needed to audit source provenance and predecessor-state
  sufficiency.

Charged hashes:

```text
report                 6fb2ce4bcea7ab35102ca60198509f99b1bc1c058dea4181d87641f56ce847ae
result manifest        06b7c5401d5886b2646101683f8df97e3335ad7aeacb4a1481e579d3388817d5
result freeze          97755c630aede8876922dc6040f866d6654064bc28dd2a30010c66744e02c91c
source freeze          1aa89a7bebf557494970f7a6ed045d031a5999f35516caced58f3937dd0ea589
aggregate              ab38fefa43d3b2065f839bfed2deccd58b75e0570fc36324cce67db805b5d3d0
Merkle                 31b77bef882a784b43ee146d930f192385714efce730b9126c8c2df4038b7be7
```

The enumeration ran on AWS; do not rerun it locally. Inspect source and
frozen outputs rather than trusting PASS. Independently attack:

1. Derive the integer residual at degree nine, including
   `G9=M9/3+{C,D}_9+T9`, the definition and signs of `T`, and every required
   divisibility before reduction. Search for another single- or
   double-Frobenius quotient term analogous to the corrected Q11/Q10 error.
2. Prove or refute that the corrected-Q10 stored state is sufficient.
   Check the canonical reconstruction of all earlier integer representatives,
   and why exactly `C2,D2,C4,D4,W7,Z7` are restored while omitted layers and
   the six current degree-six Frobenius coefficients cannot affect these 23
   rows.
3. Audit the affine matrix construction: two E1 rows, four E3 rows, seven F6
   rows, ten G9 rows, 32 variables, ranks/augmented ranks, and explicit witness
   substitution. Look for an equation counted twice, a missing monomial, or a
   rank calculated after an illicit specialization.
4. Audit all predecessor controls, the 27-way partition, histograms, counts,
   aggregate/Merkle construction, return-code/stderr/source-closure metadata,
   and the arithmetic leading to `11881`, `8096356425843`, and the additional
   factor `729`.
5. Scope the conclusion as nonemptiness only of this displayed finite affine
   Q9 extension problem. Degree eight/lower, recurrence, all-depth lifting,
   characteristic-zero algebraization, collision persistence, counterexample,
   and JC2 remain open.

State the smallest false source identity, missing state coordinate, or count
gap if one exists. Give the exact promotable sentence and strict scope. Write
exactly `xmodel/as-fonly-d7-q9-source-state-review-claude-20260825.md`. Do not
edit any other file. End with exactly one verdict: `CONFIRMED`, `GAP`, or
`REFUTED`.
