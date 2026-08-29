# AWS launch metadata: `r=1` V14 hand-anchor repair

Preregistered `2026-08-26T11:47Z` on the same two lightly loaded hosts used
for the fail-closed V13 control.  V13 finished in 0.03 seconds with about
14 MiB peak RSS and no swap, so this syntax-only delta adds no material
contention.  No local CAS or substantive algebra process is used.

| field | exact Q | `F_65521` control |
|---|---|---|
| AWS host | Box03, `98.80.65.144` | r6d, `100.26.198.153` |
| tag | `max12_812_order2_square_r1_v14_hand_anchor_repair_q_20260826T114700Z_box03` | `max12_812_order2_square_r1_v14_hand_anchor_repair_p65521_20260826T114700Z_r6d` |
| remote job dir | `/home/ubuntu/jobs/max12_812_order2_square_r1_v14_hand_anchor_repair_q_20260826T114700Z_box03` | `/home/ubuntu/jobs/max12_812_order2_square_r1_v14_hand_anchor_repair_p65521_20260826T114700Z_r6d` |
| characteristic | `0` | `65521` |
| virtual-memory cap | 24 GiB | 24 GiB |
| compile / engine caps | 600 s / 1800 s | 600 s / 1800 s |
| final state | engine `rc=0`; all math markers clean; validator rejected expected time telemetry; no verdict | engine `rc=0`; identical marker output; same validator failure; no verdict |

Every diagnostic, timeout, missing marker, or nonzero return is no verdict.
