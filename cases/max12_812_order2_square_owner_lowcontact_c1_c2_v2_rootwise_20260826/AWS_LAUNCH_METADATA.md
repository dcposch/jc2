# AWS launch metadata

Preregistered 2026-08-26T09:11:00Z after a live read-only audit.  Box03 had
492230 MiB available at load 15.18 and zero swap; r6d had 356724 MiB
available at load 13.56 and zero swap.  Each lane is capped at 32 GiB,
10 minutes for compilation, and 2 hours for Singular.  The broad V1 radical
controls and the c>=3 V3 membership controls remain live independently.

| Field | Host | Registered tag | Remote job directory | Caps | State |
|---|---|---|---|---|---|
| `Q` | Box03 | `max12_812_order2_square_lowcontact_rootwise_q_20260826T091100Z_box03` | `/home/ubuntu/jobs/max12_812_order2_square_lowcontact_rootwise_q_20260826T091100Z_box03` | 32 GiB / 600 s / 7200 s | launched, PID `192557` |
| `F_65521` | r6d | `max12_812_order2_square_lowcontact_rootwise_p65521_20260826T091100Z_r6d` | `/home/ubuntu/jobs/max12_812_order2_square_lowcontact_rootwise_p65521_20260826T091100Z_r6d` | 32 GiB / 600 s / 7200 s | launched, PID `257687` |

Heavy computation is AWS-only.  Exact `Q` is the producer and `F_65521` is
an independent modular control.  Neither endpoint is a square-branch or an
order-two verdict.

Launch archive: `/tmp/jc2_square_lowcontact_rootwise_20260826T091100Z.tar.gz`,
SHA-256 `24cfd40fb6af7fd64f844ac91a78bc03a8fb3320f245932798a201094848bb10`.

The first archive omitted the shared `ops/aws_exact_lane.sh` wrapper.  Both
compilers passed, but both engine wrappers therefore failed closed with
`rc=127` before starting Singular.  These are custody failures and carry no
mathematical endpoint.  Replacement archive
`/tmp/jc2_square_lowcontact_rootwise_v2_20260826T091400Z.tar.gz`, SHA-256
`3f76edd39aa7d144a3e43bf44fd4fc61d15ced3e720f6396128fbb688e54e14f`,
adds only the missing frozen wrapper.  Replacement lanes were preregistered:

| Field | Host | Registered tag | Remote job directory | Caps | State |
|---|---|---|---|---|---|
| `Q` | Box03 | `max12_812_order2_square_lowcontact_rootwise_v2_q_20260826T091400Z_box03` | `/home/ubuntu/jobs/max12_812_order2_square_lowcontact_rootwise_v2_q_20260826T091400Z_box03` | 32 GiB / 600 s / 7200 s | launched, PID `192910` |
| `F_65521` | r6d | `max12_812_order2_square_lowcontact_rootwise_v2_p65521_20260826T091400Z_r6d` | `/home/ubuntu/jobs/max12_812_order2_square_lowcontact_rootwise_v2_p65521_20260826T091400Z_r6d` | 32 GiB / 600 s / 7200 s | launched, PID `258041` |
