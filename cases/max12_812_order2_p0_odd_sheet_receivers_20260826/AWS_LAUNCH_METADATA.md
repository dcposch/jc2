# AWS launch metadata

Date: 2026-08-26

All three frozen lanes completed with validator PASS:

| client | host | field | cap | timeout | state |
|---|---|---:|---:|---:|---|
| terminal raw grades `13..38` | Box03 | `Q` | 32 GiB | 5400 s | PASS, 17.46 s, 417204 KiB RSS |
| Taylor branch `x=0` | r6d | `Q` | 32 GiB | 5400 s | PASS, 2.28 s, 26716 KiB RSS |
| Taylor branch `x=1` | Box03 | `F_65521` control | 32 GiB | 5400 s | PASS, 2.29 s, 26636 KiB RSS |

These are one-core source compilers.  The Taylor lanes intentionally stop at
`TYPED_WAITING_GATE_A`.

The immutable source freeze has SHA-256
`50ca8894f273ff47f69b6b32f410b811cb22e144b4a3602da326dd0e68ecc0d0`.

## Exact launch custody

```text
terminal:
  tag=max12_812_order2_p0_odd_terminal_p0_20260826T095705Z_Box03
  outer_pid=198413
  remote_job=/home/ubuntu/jobs/max12_812_order2_p0_odd_terminal_p0_20260826T095705Z_Box03/source/cases/max12_812_order2_p0_odd_sheet_receivers_20260826/aws_Box03_terminal_p0
  result.json=31a1e8663a4f4dfbecac2bc59bd20953fa111b83bc644076c45cd035075a83e5
  terminal_raw_dag.json.gz=94e9b039d8390a41add35aa94a7db0f705bb9448638003be9a99f476f5b83f45
  validation=fb15048335c3e3d4c0e5cf2e6185d6738e67b8a66df4fbf228f3f7f0fbb08425

taylor0:
  tag=max12_812_order2_p0_odd_taylor0_p0_20260826T095705Z_r6d
  outer_pid=262743
  remote_job=/home/ubuntu/jobs/max12_812_order2_p0_odd_taylor0_p0_20260826T095705Z_r6d/source/cases/max12_812_order2_p0_odd_sheet_receivers_20260826/aws_r6d_taylor0_p0
  result.json=fe6863d7580eb3aa12cbff35c27f4e28d78a941d2e1aff3a5a1f7ff3ccebaa94
  taylor_x0_typed_terms.json.gz=20766c43a16892a99e7acc137ad79dd68bf1fc07a1d48e3b89c6c2e9dae17b5f
  validation=3b8b62403d0eb926285c79d38dbe5e9134dd8ab1c5274163d4a696926fd80bce

taylor1:
  tag=max12_812_order2_p0_odd_taylor1_p65521_20260826T095705Z_Box03
  outer_pid=198628
  remote_job=/home/ubuntu/jobs/max12_812_order2_p0_odd_taylor1_p65521_20260826T095705Z_Box03/source/cases/max12_812_order2_p0_odd_sheet_receivers_20260826/aws_Box03_taylor1_p65521
  result.json=4f25586cfc65ddf4d6065342a2fed9eea1b1a4938525390e62755af53fb2f32f
  taylor_x1_typed_terms.json.gz=e64c51fa2d03a01ee9086427ae53219e7d67af8c6f201ff116390db70172f10b
  validation=4db7b02e748f80fcefe16b79dbc593c0ac63eafab4fc79958e1ee8c03c07b2d1
```

No lane swapped.  The complete 19 MiB terminal DAG and the two small Taylor
term archives remain at the recorded remote paths; their deterministic
compiler and exact hashes are frozen locally.
