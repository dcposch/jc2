# AWS launch metadata: universal odd-pole recurrence V2

Frozen V2 archive SHA-256:

```text
480526ed192a1553b0ac44f6154efdbace72c0e2a3b624811e2472341a31595c
  /tmp/jc2_d1_oddrec_universal_20260826_v2.tgz
```

| Field | Exact Q | `F_65521` control |
|---|---|---|
| host | Box03, `ip-172-30-0-249` | r6d, `ip-172-30-0-45` |
| tag | `max12_812_order2_square_d1_odd_pole_recurrence_q_v2_20260826_box03` | `max12_812_order2_square_d1_odd_pole_recurrence_p65521_v2_20260826_r6d` |
| launcher PID | 240508 | 301104 |
| characteristic | 0 | 65521 |
| start | 2026-08-26T16:39:00Z | same |
| end | 2026-08-26T16:40:11Z | same |
| timeout / VM cap | 600 s / 4,194,304 KiB | same |
| rc / validator | 0 / PASS | 0 / PASS |
| wall | 1:11.36 | 1:11.13 |
| peak RSS | 31,960 KiB | 31,656 KiB |
| swaps | 0 | 0 |
| stdout SHA-256 | `c70cd641...` | same |

The failed V1 plumbing launches used distinct earlier tags and are not
evidence. They stopped at the output-directory guard before any coefficient
check. V2 is the only producer custody.
