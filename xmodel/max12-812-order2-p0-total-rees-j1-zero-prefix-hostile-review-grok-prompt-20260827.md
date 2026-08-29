# Task: hostile review of the exact `J1=0` prefix specialization

Work in `/Users/dc/code/math/jc2`.  Review

`xmodel/max12-812-order2-p0-total-rees-j1-zero-prefix-producer-sol-20260827.md`

against the preregistration and replay in

`cases/max12_812_order2_p0_total_rees_j1_zero_prefix_20260827/`.

Do not trust or execute the producer replay.  Independently rehash all 22
frozen V9/V17 inputs and parse them with exact rational arithmetic.  Set
`rs=cs=c0=c1=0` and verify every row's zero/nonzero status, term count,
variable support, canonical digest, and the first surviving grade.  Check
that all seven grade-10 rows vanish; that the five previously consumed
stage-one rows vanish; that the `e1`-only restriction of `Tg12_2` is exactly
`(3/32)e1^2`; and that the `A00`/`A10` assignments kill all 22 rows.

Attack the inference from those rational points to
`a0,a1` not belonging to the radical of the 22-row specialized ideal, and
the operational conclusion that a `J2` emptiness search using only this
prefix is futile.  Separate source-prefix facts from any unexported/full-
source or Rees-chart statement.

Use only a fresh lightweight parser.  No CAS/Groebner, AWS, web, or
`jc2-lean`.  Write exactly one file and no other file:

`xmodel/max12-812-order2-p0-total-rees-j1-zero-prefix-hostile-review-grok-20260827.md`

Begin with `CONFIRMED`, `REPAIRABLE`, or `REFUTED`; include exact telemetry,
ranked findings, accepted theorem, and nonclaims.
