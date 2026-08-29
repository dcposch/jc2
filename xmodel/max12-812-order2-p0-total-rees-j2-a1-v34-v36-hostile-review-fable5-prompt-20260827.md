# Independent hostile review: V34--V36 grade-19 orbit obstruction

You are Fable 5 acting as an independent mathematical and computational
reviewer in the JC2 campaign.  Work from `/Users/dc/code/math/jc2`.

Review the frozen chain

- `cases/max12_812_order2_p0_total_rees_j2_a1_grade18_curve_cut_v34_20260827/`
- `cases/max12_812_order2_p0_total_rees_j2_a1_grade19_rational_orbit_v35_20260827/`
- `cases/max12_812_order2_p0_total_rees_j2_a1_grade19_orbit_unit_v36_20260827/`

and only the directly referenced upstream artifacts needed to audit it.
The proposed narrow conclusion is:

> The normalized V34 degree-five scheme inside the V32 six-coordinate
> ordered-`a1`, `rho=0` support has no grade-19 prolongation.  This says
> nothing about the rest of the ordered T-a1 chart.

Audit at least:

1. the V34 Kummer parametrization, reducedness, and sigma scaling to the
   V35 rational representative;
2. all source-series depth endpoints and 63-row bridge logic in V35;
3. the known V35 weakness that its p65521 path reconstructs over Q before
   modular reduction and that its validator is not by itself promotion
   grade;
4. whether V36 actually repairs the evidentiary gap: Q/p row shadow,
   homogeneity, absence of every sigma-weight-19 receiver, independent
   Singular reductions, nonzero normal forms, unit ideals, validators,
   freezes, and evidence manifests;
5. the mathematical inference from
   `NF(Tg19_7)=(110592/35)*rs2` and the V34 relation
   `rs2*aa0=210`;
6. any hidden possibility that a new or previously zero source jet can
   cancel the obstruction without leaving the precise V34 scheme;
7. exact scope language and whether promotion is PASS, PASS WITH
   AMENDMENT, or FAIL.

You may use lightweight shell reads, hashes, and exact scalar checks.  Do
not run heavy CAS or symbolic jobs locally; AWS artifacts are already
present.  Do not use the web, AWS, or any network service.  Do not modify
any campaign file except the required report, and do not read or touch
`jc2-lean`.

Write the complete report to exactly:

`xmodel/max12-812-order2-p0-total-rees-j2-a1-v34-v36-hostile-review-fable5-20260827.md`

Give concrete file/hash evidence, separate defects from scope limitations,
and make the final verdict explicit.  End after writing that report.
