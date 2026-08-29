# V24 exact-Q R2/R5 monitoring handoff

Snapshot: `2026-08-27T17:31:53Z`.  Both jobs are healthy and must be left
running untouched on Box02 (`34.203.207.55`, host `ip-172-30-0-186`).  Each
uses one core, has a 943,718,400-KiB virtual-memory cap and a six-hour wall
cap; host swap is zero.

- R2 tracked exact-Q lane:
  `/home/ubuntu/jobs/max12_812_order2_u2_62_k00_grade7_v24r2_exact_q_20260827T135458Z_box02`
  (PID `366878`, start `13:55:35Z`).  At the last poll: elapsed 12,949 s,
  CPU 99.9%, RSS 32,200,156 KiB, VSZ 32,219,352 KiB, state `R`, no
  `output/RESULT.json`.
- R5 direct exact target-lift lane:
  `/home/ubuntu/jobs/max12_812_order2_u2_62_k00_v24r5_direct_exact_lift_20260827T152151Z_box02`
  (PID `371365`, start `15:22:23Z`).  At the last poll: elapsed 7,740 s,
  CPU 99.9%, RSS 5,468,160 KiB, VSZ 5,487,884 KiB, state `R`, no
  `output/RESULT.json`.

Box02 had 48 GiB used and about 1.9 TiB available.  There was no contention
or anomaly.  On a terminal result, first replay the remote evidence manifest,
then harvest immutable bytes into a new local directory and adjudicate the
exact certificate/witness.  If a process exits without a result, inspect
`run/FINAL.validation`, runner stderr and cap markers; partial stdout is not
theorem evidence.  Neither lane licenses a later-grade, full-jet, arc,
closure, counterexample or JC2 conclusion by itself.
