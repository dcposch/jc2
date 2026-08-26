# AWS launch metadata

Observed `WAITING_GO` before GO at `2026-08-26T04:31:34Z`:

- Box03 tag/job
  `max12_912_order3_d1_double_root_control2_hq_linear_filtered_lift_v8_20260826T043000Z_box03_forward`,
  worker PID `158757`, forward, 4 GiB / 900 s, nice 10.
- r6d tag/job
  `max12_912_order3_d1_double_root_control2_hq_linear_filtered_lift_v8_20260826T043000Z_r6d_reverse`,
  worker PID `226117`, reverse, 4 GiB / 900 s, nice 10.

Neither run directory contained a GO sentinel.  Both remote source manifests
passed before worker launch; remote syntax compilation also passed.  Source
manifest SHA:

```text
b3b38b28d22320b4c64521912b232b789e859eb4521e664785f4d20ae945827b
```
