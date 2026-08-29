You are Fable 5 acting as an equal, independent hostile mathematical reviewer in the plane Jacobian-conjecture campaign. Work in /Users/dc/code/math/jc2.

Review this producer claim:

- xmodel/max12-812-order2-p0-total-rees-section-all-depth-v21-producer-sol-20260827.md
- cases/max12_812_order2_p0_total_rees_section_all_depth_v21_20260827/PREREGISTRATION.md
- cases/max12_812_order2_p0_total_rees_section_all_depth_v21_20260827/FREEZE.sha256
- cases/max12_812_order2_p0_total_rees_section_all_depth_v21_20260827/replay_section_all_depth_v21.py
- cases/max12_812_order2_p0_total_rees_section_all_depth_v21_20260827/RESULT.json

Try to refute it. At minimum:

1. Rehash every frozen input and output, including the producer report (expected SHA-256 `172755de690977d90448a6b6c6ac0abf0d9437dfecb46983638919eb241c7ffe`).
2. Independently derive the four specialized coefficient-series tuples from the literal source formulas in the hash-pinned V20 emitter. Check carefully the `p`, `r`, `c`, `n3`, `n2`, `n1`, `n0` shifts, coefficient-index ordering, rho powers, and the fact that every load series is zero on all four named assignments.
3. Independently evaluate all 569 canonical tails in an untruncated exact ring, preferably with a separately written implementation or a transparent hand reduction. Do not rely on the V21 program's expected-answer assertion.
4. Confirm or refute the exhaustive output:
   - `A00`: only `Tg15_6=-1/16`;
   - `A10`: only `Tg15_3=-1/16`, `Tg15_5=-(3/32)rho^2`, `Tg15_7=-(3/128)rho^4`;
   - `CS0` and `Z00`: all seven full row series are identically zero.
5. Audit why this is genuinely all coefficient grades rather than a hidden truncation. Check whether omitted higher jet variables, delayed loads, or a tail containing a load could survive any named assignment.
6. Verify the claimed V20 grade-13/14 bridges and modular reductions.
7. Judge the exact scope: grade 15 kills only the two displayed horizontal points; all-depth persistence concerns the frozen finite-tail literal source and does not establish a formal arc, chart nonemptiness, or resistance to Rees/chart equations.

This is a 0.06-second, 13-MB exact replay. You may run bounded light local exact scripts, but no heavy/uncertain local algebra. Do not mutate AWS, do not access or alter jc2-lean, and do not edit any campaign file except your report.

Write exactly one report:

xmodel/max12-812-order2-p0-total-rees-section-all-depth-v21-hostile-review-fable5-20260827.md

Give a clear verdict (CONFIRMED, CONFIRMED WITH REPAIRS, NOT CONFIRMED, or REFUTED), independent calculations and observed values, any defect and mathematical effect, the strongest justified statement, and the exact producer-report SHA-256. Do not write anywhere else.
