# AWS launch metadata: tied D1 `(a,r)=(1,2)`, `c>=6`

Date: 2026-08-26

All three hosts received source archive SHA256
`682a8d9ab3c04e7ebd4dd7e04f23d114b0c064b5269c8df3563d4cf5acb0c5a6`,
used the frozen 1,800-second / 16,777,216-KiB runner, and passed the source
freeze before compilation.

| host | characteristic | tag | launcher PID | UTC interval | rc / RSS KiB / swap |
|---|---:|---|---:|---|---|
| Box02 `ip-172-30-0-186` | 0 | `max12_812_order2_square_d1_tied_a1r2_cge6_maxpole2_v1_q_box02_20260826T1955Z` | 316460 | 19:55:16--19:55:16 | 0 / 19716 / 0 |
| Box03 `ip-172-30-0-249` | 65519 | `max12_812_order2_square_d1_tied_a1r2_cge6_maxpole2_v1_p65519_box03_20260826T1955Z` | 265116 | 19:55:16--19:55:16 | 0 / 20040 / 0 |
| r6d `ip-172-30-0-45` | 65521 | `max12_812_order2_square_d1_tied_a1r2_cge6_maxpole2_v1_p65521_r6d_20260826T1955Z` | 335217 | 19:55:16--19:55:16 | 0 / 20064 / 0 |

Per-host registrations, exact argv, compiled sources and inventories,
stdout/stderr, `/usr/bin/time -v` telemetry, and validators are frozen in
`EVIDENCE.sha256`.
