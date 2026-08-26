# AWS registration

- host: r6d, `100.26.198.153`
- tag: `max12_912_order3_d1_double_root_control2_la20_syzygy_v2_20260826T021500Z_r6d_LPDP`
- remote job root: `/home/ubuntu/jobs/max12_912_order3_d1_double_root_control2_la20_syzygy_v2_20260826T021500Z_r6d_LPDP`
- remote run directory: job root plus `/repo/cases/max12_912_order3_d1_double_root_control2_la20_syzygy_v2_20260826`
- CPU: one Singular process, `nice -n 10`
- compiler cap/timeout: 2 GiB / 300 s
- solver cap/timeout: 192 GiB (`201326592` KiB) / 21600 s
- launch protocol: upload frozen archive, verify source closure, start worker in
  WAITING state, record PID/caps, then separately release compile and solve.
