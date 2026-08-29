# AWS launch metadata: D1 `a=9`, `d=2,3` grade-38 producer

Date: 2026-08-26

All launches used the same source archive SHA256
`01cca2d13adfd6685dd628b89f7eace7344b5c778b828d29563f8b8279040f53`,
the frozen `launch_host.sh`/`run_aws.sh` path, a 10,800-second timeout, and
a 134,217,728-KiB virtual-memory cap.

| host | characteristic | cell | tag | launcher PID | UTC interval | rc / max RSS KiB / swap |
|---|---:|---|---|---:|---|---|
| Box02 `ip-172-30-0-186` | 0 | `a9,d2` | `max12_812_order2_square_d1_a8a9_d23_j38_r3_tail_v2_a9d2_q_box02_20260826T1900Z` | 303783 | 19:00:27--19:22:01 | 0 / 107644548 / 0 |
| Box03 `ip-172-30-0-249` | 65519 | `a9,d2` | `max12_812_order2_square_d1_a8a9_d23_j38_r3_tail_v2_a9d2_p65519_box03_20260826T1900Z` | 258839 | 19:00:27--19:18:17 | 0 / 98951104 / 0 |
| r6d `ip-172-30-0-45` | 65521 | `a9,d2` | `max12_812_order2_square_d1_a8a9_d23_j38_r3_tail_v2_a9d2_p65521_r6d_20260826T1900Z` | 324851 | 19:00:27--19:17:49 | 0 / 98951420 / 0 |
| Box02 `ip-172-30-0-186` | 0 | `a9,d3` | `max12_812_order2_square_d1_a8a9_d23_j38_r3_tail_v2_a9d3_q_box02_20260826T1900Z` | 303831 | 19:00:27--19:14:31 | 0 / 62252144 / 0 |
| Box03 `ip-172-30-0-249` | 65519 | `a9,d3` | `max12_812_order2_square_d1_a8a9_d23_j38_r3_tail_v2_a9d3_p65519_box03_20260826T1900Z` | 258829 | 19:00:27--19:11:31 | 0 / 56589900 / 0 |
| r6d `ip-172-30-0-45` | 65521 | `a9,d3` | `max12_812_order2_square_d1_a8a9_d23_j38_r3_tail_v2_a9d3_p65521_r6d_20260826T1900Z` | 324878 | 19:00:27--19:11:03 | 0 / 56589548 / 0 |

The retrieved per-lane launch registrations, exact argv, hostnames,
timestamps, return codes, `/usr/bin/time -v` telemetry, compiled sources,
inventories, validators, and stdout/stderr are all pinned by
`EVIDENCE_A9.sha256`.
