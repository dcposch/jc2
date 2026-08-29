# AWS launch metadata: D1 finite band `a=2..5`

Preregistered `2026-08-26T12:05Z`.  Both hosts were checked immediately
before launch.  Box03 had about 488 GiB available and load 4; r6d had about
311 GiB available, load 5, zero swap, and one unrelated registered Singular
worker.  This package is capped at 24 GiB per lane.

| field | exact Q | `F_65521` control |
|---|---|---|
| AWS host | Box03, `98.80.65.144` | r6d, `100.26.198.153` |
| tag | `max12_812_order2_square_d1_finite_band_a2_a5_fullsupport_q_20260826T120500Z_box03` | `max12_812_order2_square_d1_finite_band_a2_a5_fullsupport_p65521_20260826T120500Z_r6d` |
| remote job dir | `/home/ubuntu/jobs/max12_812_order2_square_d1_finite_band_a2_a5_fullsupport_q_20260826T120500Z_box03` | `/home/ubuntu/jobs/max12_812_order2_square_d1_finite_band_a2_a5_fullsupport_p65521_20260826T120500Z_r6d` |
| characteristic | `0` | `65521` |
| virtual-memory cap | 24 GiB | 24 GiB |
| compile / engine caps | 600 s / 1800 s | 600 s / 1800 s |
| launcher PID | `214524` | `275139` |
| current state | engine `rc=0`; validator PASS | engine `rc=0`; validator PASS |

Timeout, nonzero return, a missing/duplicate marker, or a rejected diagnostic
is no verdict.  No substantive computation is run locally.
