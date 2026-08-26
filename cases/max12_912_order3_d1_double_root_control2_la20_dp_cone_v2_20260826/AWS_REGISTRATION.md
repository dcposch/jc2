# AWS registration

- host: Box03, `98.80.65.144`
- tag: `max12_912_order3_d1_double_root_control2_la20_dp_cone_v2_20260826T021500Z_box03_DP`
- remote job root: `/home/ubuntu/jobs/max12_912_order3_d1_double_root_control2_la20_dp_cone_v2_20260826T021500Z_box03_DP`
- remote run directory: job root plus `/repo/cases/max12_912_order3_d1_double_root_control2_la20_dp_cone_v2_20260826`
- CPU: one Singular process, `nice -n 10`
- compiler cap/timeout: 2 GiB / 300 s
- solver cap/timeout: 128 GiB (`134217728` KiB) / 21600 s
- launch protocol: upload frozen archive, verify source closure, start worker in
  WAITING state, record PID/caps, then separately release compile and solve.
