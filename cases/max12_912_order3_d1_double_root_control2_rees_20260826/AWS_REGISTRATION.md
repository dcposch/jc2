# AWS registration

Source archive SHA-256:

```text
8e5d2adbee776f8a2d3e7fe981d686a2c236edd8be9446e33b679de0d90278a7
```

## Encoding A

- tag: `max12_912_order3_d1_double_root_control2_rees_20260826T004241Z_box02_A`
- host: Box02 `34.203.207.55` (Amazon EC2)
- job: `/home/ubuntu/jobs/max12_912_order3_d1_double_root_control2_rees_20260826T004241Z_box02_A`
- blocked worker PID: `260763`
- encoding: factored charged rows; principal `s` saturation; `dp`
- caps: one compiler / one Singular process; nice 10; compiler 64 GiB and
  3600 s; solver 256 GiB and 21600 s

## Encoding B

- tag: `max12_912_order3_d1_double_root_control2_rees_20260826T004241Z_r6d_B`
- host: r6d `100.26.198.153` (Amazon EC2)
- job: `/home/ubuntu/jobs/max12_912_order3_d1_double_root_control2_rees_20260826T004241Z_r6d_B`
- blocked worker PID: `190844`
- encoding: independently expanded charged rows; `u*s-1` contraction;
  `(lp(2),dp(8))`
- caps: one compiler / one Singular process; nice 10; compiler 64 GiB and
  3600 s; solver 256 GiB and 21600 s

Both workers were recorded in `WAITING_COMPILE` before either GO sentinel was
created.  The pre-existing tied-ray solver races remain separate and live.

