# Registration: discriminant half-weight Kuranishi certificate V2

Date: 2026-08-26

Status: **PREREGISTERED IMMUTABLE V2; NO RESULT.**

V1 remains immutable and fail-closed: all mathematical/source sentinels
passed, but it compared an ideal-valued `reduce` result directly with scalar
zero and used unsupported `quit(84)`.  V2 changes only this control.  It
checks every generator separately in both directions and uses a valid plain
`quit` after a failure sentinel.

```text
tag=max12_812_order2_disc_halfweight_v2_q_20260826T063000Z_box03
host=Box03 / 98.80.65.144
job=/home/ubuntu/jobs/max12_812_order2_disc_halfweight_v2_q_20260826T063000Z_box03

tag=max12_812_order2_disc_halfweight_v2_p32003_20260826T063000Z_r6d
host=r6d / 100.26.198.153
job=/home/ubuntu/jobs/max12_812_order2_disc_halfweight_v2_p32003_20260826T063000Z_r6d

tag=max12_812_order2_disc_halfweight_v2_p65521_20260826T063000Z_box03
host=Box03 / 98.80.65.144
job=/home/ubuntu/jobs/max12_812_order2_disc_halfweight_v2_p65521_20260826T063000Z_box03
```

Each lane uses one core, at most 64 GiB virtual memory, a 600-second compiler
cap, and a 3600-second Singular cap.  V2 cannot promote any endpoint beyond
the frozen half-weight initial gate.
