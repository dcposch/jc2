# AWS launch metadata

Registered and observed in `WAITING_GO` state before GO at
2026-08-26T04:01Z:

- Box03 `98.80.65.144`: job/tag
  `max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826T035900Z_box03_forward`,
  worker/launcher PID `154388`, forward traversal, 4 GiB / 900 s, nice 10.
- r6d `100.26.198.153`: job/tag
  `max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826T035900Z_r6d_reverse`,
  worker/launcher PID `222147`, reverse traversal, 4 GiB / 900 s, nice 10.

Neither run directory contained a GO sentinel when the worker PID and caps
were read.  Source-closure manifest SHA-256:

```text
530fb09744f1b7101959e1a9c46e272e306468c63d029876ecaf11d04ab8bd29
```
