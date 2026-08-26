# AWS launch metadata

Observed `WAITING_GO` before GO at `2026-08-26T04:50:00Z`:

- Box03 tag/job
  `max12_912_order3_d1_double_root_control2_axis_covariance_v9_20260826T044900Z_box03_forward`,
  worker PID `162034`, forward, 8 GiB / 1800 s, nice 10.
- r6d tag/job
  `max12_912_order3_d1_double_root_control2_axis_covariance_v9_20260826T044900Z_r6d_reverse`,
  worker PID `229414`, reverse, 8 GiB / 1800 s, nice 10.

Neither run directory contained a GO sentinel.  Both remote source manifests
and remote syntax compilation passed before worker launch.  Source manifest
SHA:

```text
084cc8ddc9523c7208556bfb12d68e545a81221034e9ed108743127cc9805274
```
