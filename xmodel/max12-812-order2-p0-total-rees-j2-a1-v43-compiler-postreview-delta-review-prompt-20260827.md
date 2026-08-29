# Narrow review request: V43 compiler c7ed7309 -> 0de6a2b2

Review only the additive custody report
`xmodel/max12-812-order2-p0-total-rees-j2-a1-v43-compiler-postreview-delta-sol-20260827.md`
and the current
`cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827/compile_total_dvr_w30_v43.py`.

Check:

1. the displayed diff is the complete byte delta from reviewed SHA
   `c7ed730905592b571ef6746ad369297916810c671e4c6f2e6f1af0995caeade0`
   to current SHA
   `0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00`;
2. a cyclic core with identically zero right-hand side is solved soundly by
   setting its variables to zero before reverse leaf substitution;
3. the mandatory full-product exact replay prevents a false dual
   certificate;
4. on the reported actual census `forced_core_equations=1`, both versions
   fail closed, so this delta cannot change the current weight-30 verdict;
5. consumers used by the launched total-dehom and LinBox lanes do not call
   `leaf_peel_dual`.

Do not review or endorse any AWS outcome not yet frozen.  Preserve the
statement that only `c7ed7309...`, not `0de6a2b2...`, was covered by the
earlier Fable correction review.

Return `CONFIRMED`, `REFUTED`, or `GAP` for each item and write the complete
report to exactly
`xmodel/max12-812-order2-p0-total-rees-j2-a1-v43-compiler-postreview-delta-hostile-review-fable5-20260827.md`.
Touch no other campaign artifact. Do not enter, read, build, status-inspect,
or modify `jc2-lean`. Desk-scale checks only; no AWS launch, web sweep, or
canonical-ledger edit.
