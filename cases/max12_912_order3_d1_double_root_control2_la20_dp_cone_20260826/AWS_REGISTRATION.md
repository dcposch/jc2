# AWS registration

- tag:
  `max12_912_order3_d1_double_root_control2_la20_dp_cone_20260826T020348Z_box03_DP`
- host: Box03, `98.80.65.144` (Amazon EC2; hostname
  `ip-172-30-0-249`)
- job:
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_control2_la20_dp_cone_20260826T020348Z_box03_DP`
- blocked worker PID: `136826`
- compiler cap: 2 GiB virtual, 300 seconds, nice 10
- Singular cap: 128 GiB virtual, 21600 seconds, one process, nice 10
- repository source-closure SHA-256:
  `9840e30e767e882967e77b41ff45e52c52e649663c9c323df9482d8f58a813e7`

The worker was observed in `WAITING_COMPILE`; all five flattened remote
source files verified and no `GO_COMPILE` sentinel existed when this
registration was written.  The most recent fleet check before placement was
load 11 with 190 GiB available.  The 128-GiB hard cap preserves headroom and
all existing registered Box03 jobs were left untouched.

