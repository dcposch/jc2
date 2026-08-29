# AWS launch metadata: D1 primary-C2 `c=8` connection split V3

Date: 2026-08-26

All three V3 executions used source archive SHA-256

```text
5830f73cc677c7765b6114c798f003004b49c7842b0ba5430655c7c33021c081
```

and passed the frozen on-host source check before compilation.  Mathematical
stdout is byte-identical across the three characteristics, SHA-256
`a59389d2d1b2f8b979aaec101cdfc6a7d879154c48fe94bb03a98f5ee71a2244`.

| field | exact `Q` | `F_65519` control | `F_65521` control |
|---|---|---|---|
| host | Box03 / `ip-172-30-0-249` | Box02 / `ip-172-30-0-186` | r6d / `ip-172-30-0-45` |
| tag | `max12_812_order2_square_d1_c2_c8_connection_q_box03_v3_20260826T2148Z` | `max12_812_order2_square_d1_c2_c8_connection_p65519_box02_v3_20260826T2148Z` | `max12_812_order2_square_d1_c2_c8_connection_p65521_r6d_v3_20260826T2148Z` |
| start UTC | `2026-08-26T21:44:20Z` | same | same |
| end UTC | `2026-08-26T21:44:21Z` | `2026-08-26T21:44:20Z` | `2026-08-26T21:44:20Z` |
| wall | `0:00.10` | `0:00.09` | `0:00.09` |
| peak RSS | `20,396 KiB` | `19,692 KiB` | `20,424 KiB` |
| VM cap | `67,108,864 KiB` | same | same |
| engine rc / swaps | `0 / 0` | `0 / 0` | `0 / 0` |
| validator | `PASS_D1_C2_C8_CONNECTION_SPLIT_CLOSED_TAIL` | same | same |

Exact Q is the characteristic-zero endpoint.  The two fresh primes are
independent host/software controls only.  The earlier V2 runs are quarantined
separately in `RESULT_V2_FAILED.md` and are not evidence for this endpoint.
