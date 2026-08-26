# AWS registration

- tag:
  `max12_912_order3_d1_double_root_control2_la20_syzygy_20260826T015817Z_r6d_LPDP`
- host: r6d, `100.26.198.153` (Amazon EC2; hostname
  `ip-172-30-0-45`)
- job:
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_control2_la20_syzygy_20260826T015817Z_r6d_LPDP`
- blocked worker PID: `203253`
- wrapper parent PID: `203250` (shell only; no computational payload)
- compiler cap: 2 GiB virtual, 300 seconds, nice 10
- Singular cap: 192 GiB virtual, 21600 seconds, one process, nice 10
- source-closure file SHA-256:
  `1e92f3fa684f9883de9125505e099dc5dcd84838c25a4a85c7f2d7c946b8777c`

The worker was observed in `WAITING_COMPILE`; all four source hashes passed
on r6d and no `GO_COMPILE` sentinel existed when this registration was
written.  Fleet state immediately before launch was load 3.02 with 351 GiB
available.  Existing registered slope, order-two, and tied-toric jobs were
left untouched.

