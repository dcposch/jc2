# AWS launch metadata: `r=1` V13 standard-basis repair

Preregistered `2026-08-26T11:41Z`.  The live prelaunch audit found Box03 at
load `4.00` with `512333216` KiB `MemAvailable`, and r6d at load `5.00` with
`333165188` KiB `MemAvailable`.  Both previously owned broad-control PIDs
were absent.  No local CAS or substantive algebra process is used.

| field | exact Q | `F_65521` control |
|---|---|---|
| AWS host | Box03, `98.80.65.144` | r6d, `100.26.198.153` |
| tag | `max12_812_order2_square_r1_v13_standard_basis_repair_q_20260826T114100Z_box03` | `max12_812_order2_square_r1_v13_standard_basis_repair_p65521_20260826T114100Z_r6d` |
| remote job dir | `/home/ubuntu/jobs/max12_812_order2_square_r1_v13_standard_basis_repair_q_20260826T114100Z_box03` | `/home/ubuntu/jobs/max12_812_order2_square_r1_v13_standard_basis_repair_p65521_20260826T114100Z_r6d` |
| characteristic | `0` | `65521` |
| virtual-memory cap | 24 GiB | 24 GiB |
| compile cap | 600 s | 600 s |
| engine cap | 1800 s | 1800 s |
| final state | engine `rc=0`; validator FAIL at undefined hand-remainder anchor; no verdict | engine `rc=0`; same validator FAIL; no verdict |

Each remote launcher records its PID, hostname, start UTC, caps, engine exit
code, stdout/stderr, and fail-closed validation.  Any timeout, diagnostic,
nonempty engine stderr, or missing/nonunique marker is no verdict.
