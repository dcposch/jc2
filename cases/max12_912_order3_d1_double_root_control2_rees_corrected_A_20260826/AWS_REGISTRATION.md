# AWS registration

Both workers were observed blocked behind `WAITING_COMPILE` with no GO
sentinel after their complete frozen source closures verified.

## LPDP direct saturation

- tag:
  `max12_912_order3_d1_double_root_control2_rees_corrected_A_20260826T013127Z_box03_LPDP`
- host: Box03, `98.80.65.144` (Amazon EC2)
- job: `/home/ubuntu/jobs/` followed by the tag
- worker PID: `133163`
- compiler: 4 GiB / 600 s; solver: 192 GiB / 21600 s; one process; nice 10

## DP direct saturation

- tag:
  `max12_912_order3_d1_double_root_control2_rees_corrected_A_20260826T013127Z_r6d_DP`
- host: r6d, `100.26.198.153` (Amazon EC2)
- job: `/home/ubuntu/jobs/` followed by the tag
- worker PID: `200483`
- compiler: 4 GiB / 600 s; solver: 320 GiB / 43200 s; one process; nice 10
