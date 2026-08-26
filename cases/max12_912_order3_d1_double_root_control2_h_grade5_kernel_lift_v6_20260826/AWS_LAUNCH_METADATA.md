# AWS launch metadata

Observed in `WAITING_GO` state before GO at 2026-08-26T04:12Z:

- Box03 `98.80.65.144`, tag/job
  `max12_912_order3_d1_double_root_control2_h_grade5_kernel_lift_v6_20260826T041000Z_box03_forward`,
  worker PID `155376`, forward, 4 GiB / 900 s, nice 10.
- r6d `100.26.198.153`, tag/job
  `max12_912_order3_d1_double_root_control2_h_grade5_kernel_lift_v6_20260826T041000Z_r6d_reverse`,
  worker PID `222945`, reverse, 4 GiB / 900 s, nice 10.

Neither run directory contained GO when metadata was read.  Source-closure
manifest SHA-256:

```text
cdd6f99c5060682f205d2fd0e9acc2bb78a758eec43135cf29a524bd3e4cba6d
```
