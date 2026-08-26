# AWS registration

- A: Box03 `98.80.65.144`, tag
  `max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826T031500Z_box03_A`,
  global `dp`, 8-GiB cap, 1800-s timeout.
- B: r6d `100.26.198.153`, tag
  `max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826T031500Z_r6d_B`,
  `(lp(2),dp(8))`, 8-GiB cap, 1800-s timeout.
- One nice-10 compiler and one nice-10 Singular process per host.  Both
  workers must be registered in `WAITING_COMPILE` before either GO sentinel.
  Existing registered jobs are not stopped or modified.
