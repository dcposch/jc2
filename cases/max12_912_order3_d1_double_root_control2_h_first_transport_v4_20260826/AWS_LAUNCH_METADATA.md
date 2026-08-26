# AWS launch metadata

Registered before GO at `2026-08-26T03:46:56Z`.  Local heavy-process audit:
zero campaign-owned workers; none stopped.

- Box03 `98.80.65.144`: tag/job root
  `max12_912_order3_d1_double_root_control2_h_first_transport_v4_20260826T034500Z_box03_forward`,
  worker PID `153321`, forward, 4 GiB / 900 s, nice 10, `WAITING_GO`.
- r6d `100.26.198.153`: tag/job root
  `max12_912_order3_d1_double_root_control2_h_first_transport_v4_20260826T034500Z_r6d_reverse`,
  worker PID `221060`, reverse, 4 GiB / 900 s, nice 10, `WAITING_GO`.

Each run directory is the package under the job root's `cases/`.  Neither
had a GO sentinel when PID/caps were read.  Source-closure manifest SHA-256:

```text
817f45ebc4b87beaff940124994b79294472aba89f392a8ce41c20641d1abc12
```
