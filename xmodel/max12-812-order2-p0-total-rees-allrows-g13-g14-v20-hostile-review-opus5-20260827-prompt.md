You are Opus 5 acting as an independent hostile mathematical and computational reviewer in the plane Jacobian-conjecture campaign. Work in /Users/dc/code/math/jc2.

Review the producer claim in:

- xmodel/max12-812-order2-p0-total-rees-allrows-g13-g14-export-v20-producer-sol-20260827.md
- cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/PREREGISTRATION.md
- cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/HARVEST_CUSTODY.md
- cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/FREEZE.sha256
- the frozen scripts and both harvested aws_q_v20/ and aws_p65521_v20/ evidence trees in that case.

Your job is to try to break the claimed result, not to paraphrase it. At minimum:

1. Rehash the freeze, RESULT.json files, EVIDENCE.sha256 manifests, compiler results, and all evidence entries, carefully remapping the manifests' remote absolute paths to the local harvested roots where needed.
2. Audit whether the source reconstruction actually includes all 569 canonical tails in all seven rows and respects the row-weight contracts. Check the code path, variable/exponent conventions, coefficient arithmetic, total/restricted source construction, and coefficient extraction.
3. Independently establish or refute all exact bridges: the 21 grade-10--12 coefficients versus the reviewed V9 artifacts, and Tg14_5 versus reviewed V17. Do not trust RESULT.json assertions alone.
4. Independently compare all fourteen exact-Q coefficients with their F65521 reductions, including monomial supports and reduced coefficients.
5. Independently evaluate all 56 combinations (14 rows times CS0, A00, A10, Z00) as polynomials in Q[rho]. Look for parser omissions, variable-name collisions, negative exponents, or unsupported syntax.
6. Audit rho-evenness, nonzeroness, term counts, and the seven frozen-tail +1 source-sensitivity controls.
7. Judge precisely whether the inference is valid: rows through grade 14 cannot break any of the four named sections, hence the first possible section-breaking source grade is at least 15. State every dependency and scope limitation; distinguish an exported-prefix section from a full formal source arc.

The computation was measured at about 34 seconds and 35 MiB per field. You may run a bounded exact local replay under timeout/ulimit if useful, but do not start any uncertain or heavy local algebra. Do not mutate AWS, do not access or alter jc2-lean, and do not edit any campaign file except your single report below. Read-only shell work is allowed.

Write exactly one report:

xmodel/max12-812-order2-p0-total-rees-allrows-g13-g14-v20-hostile-review-opus5-20260827.md

The report must give a clear verdict (CONFIRMED, CONFIRMED WITH REPAIRS, NOT CONFIRMED, or REFUTED), exact checks performed with observed hashes/counts, any defect and its mathematical effect, the strongest justified theorem, and the exact SHA-256 of the producer report you reviewed. Do not write anywhere else.
