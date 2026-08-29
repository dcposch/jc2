You are the independent hostile reviewer for a frozen exact-Q diagnostic in the
JC2 campaign. Work in `/Users/dc/code/math/jc2`. The producer was Sol; you are
Grok and therefore a different model. Do not trust PASS banners or the prose
result. Rehash, inspect source, reconstruct the logic, and seek the smallest
counterexample or scope inflation.

Write exactly one report:

`xmodel/td6-v89h19r1-raw-p13-coordinate12-hostile-review-grok-20260826.md`

Do not edit any producer artifact, top-level ledger, other xmodel file, or
`jc2-lean`. Do not launch heavy local computation. Small parsing/hash/source
checks are allowed. The report must give one overall verdict—`CONFIRMED`,
`REFUTED`, or `GAP`—and separately adjudicate each charged claim below.

The frozen case directory is:

`cases/td6_c1_c2_c3_allq_mod_f_unitriangular_functional_v89h10_aws_20260826`

Start with these controlling files:

- `P13_RAW_COORDINATE12_AUDIT_R1_RESULT.md`, SHA-256
  `6573626441e58560935e6c4efac15f7a2cda873afc42f56e42ae5f4ca56837e8`;
- `P13_RAW_COORDINATE12_AUDIT_R1_EVIDENCE.sha256`, SHA-256
  `f90f821879f1cc48b344db18aa1b63d113588025b2dc38b71cbe6e1cf30c55c1`;
- `P13_RAW_COORDINATE12_AUDIT_R1_FREEZE.sha256`, SHA-256
  `35368feef910383f6199c9c95e91d4adb1ac0819cd6f1e3f930bd14b78c7d6a4`;
- `PREREGISTRATION_RAW_P13_COORDINATE12_AUDIT_R1.md`;
- `replay_v89h19r1_raw_p13_coordinate12_audit.py`;
- `run_v89h19r1_raw_p13_coordinate12_audit.sh`;
- `SOURCE_RAW_P13_COORDINATE12_AUDIT_R1.sha256`.

Also inspect both complete harvests
`harvest_h19r1_{r6a,r6b}_20260826T234603Z`, the upstream frozen H15/H12/H11
source and manifests, the frozen H15 vector-count erratum, and the confirmed
H15+H18 review
`xmodel/td6-v89h15-h18-p13-coordinate12-combined-hostile-review-sol-20260826.md`.

Charges:

1. Verify all freeze/evidence manifests, both per-host evidence manifests,
   exact runtime identity/caps, rc/state, and byte agreement. Distinguish the
   differing timing stderr/meta from mathematical output.
2. Confirm that R1 actually repairs original H19's two defects: transitive
   H15→H12→H11→compiler custody, and a genuine source-addend omission before
   aggregation rather than removal of an output record.
3. Compare `raw_degree_contributions(...,13)` term for term with the six loop
   families in H15's `compile_current_degree`. Check indices, derivative
   multipliers, signs, the `-45*g3` term, canonicalization, and the assertion
   that the reconstructed sum equals the exact frozen parent polynomial.
4. Check that the claimed 2,757 parameter terms, 68 nonzero source addends,
   all 132 transport variables, and all 22 q variables are enforced rather
   than merely printed. Identify any omitted source family or specialization
   that could change coordinate 12.
5. Independently parse the active-addend TSV and raw-coordinate TSV. Confirm
   the exact four-label ordered census, the two total/F=0 records, and that
   omitting `f1_times_dg2:i=13:j=1` changes the `(29,)` record exactly as
   stated.
6. Decide whether those raw records really differ from H18's normalized unit
   `(3500000000/9)*(U/V)`, and whether the narrow conclusion is correct: the
   direct raw-unit shortcut fails and an explicit FIRST
   membership/cancellation bridge remains. Attack any inference stronger than
   this.
7. Check that Python assertions were enabled, python-flint was pinned, no
   Singular qring comparison semantic contaminates this client, and the
   source-census preflight did not leak an unfrozen choice into the final
   producer.
8. State explicitly that a confirmation does not prove original-FIRST
   membership, a total-F lift, a whole-TD6 theorem, or JC2.

If there is any defect, name the smallest affected statement and the cleanest
correction. Include exact artifact hashes and replayable commands used.
