# AWS launch metadata: `r=1` V15 validator telemetry repair

Preregistered `2026-08-26T11:50Z`.  This is a fresh dual replay of the frozen
V14 input through a validator-only delta.  V14 finished in 0.03 seconds and
about 15 MiB peak RSS on each host.  No local CAS or substantive algebra
process is used.

| field | exact Q | `F_65521` control |
|---|---|---|
| AWS host | Box03, `98.80.65.144` | r6d, `100.26.198.153` |
| tag | `max12_812_order2_square_r1_v15_validator_telemetry_repair_q_20260826T115000Z_box03` | `max12_812_order2_square_r1_v15_validator_telemetry_repair_p65521_20260826T115000Z_r6d` |
| remote job dir | `/home/ubuntu/jobs/max12_812_order2_square_r1_v15_validator_telemetry_repair_q_20260826T115000Z_box03` | `/home/ubuntu/jobs/max12_812_order2_square_r1_v15_validator_telemetry_repair_p65521_20260826T115000Z_r6d` |
| characteristic | `0` | `65521` |
| virtual-memory cap | 24 GiB | 24 GiB |
| compile / engine caps | 600 s / 1800 s | 600 s / 1800 s |
| final state | engine `rc=0`; validator PASS | engine `rc=0`; validator PASS |

Timeout, nonzero return, a missing/duplicate marker, or a rejected diagnostic
is no verdict.
