# AWS launch metadata

Date: 2026-08-26

Both lanes used the frozen complete source, a 16 GiB virtual-memory cap,
600-second compiler timeout, and 1800-second engine timeout.  No local CAS
was run.

| lane | host | characteristic | tag | start UTC | elapsed | peak RSS | swap | validator |
|---|---|---:|---|---|---:|---:|---:|---|
| theorem | Box03 / `ip-172-30-0-249` | `0` | `max12_812_order2_p0_a_c1_20260826T115224Z_Box03_q` | `2026-08-26T11:52:34Z` | `0.29 s` | `39788 KiB` | `0` | `PASS_P0_A_C1` |
| control | r6d / `ip-172-30-0-45` | `65521` | `max12_812_order2_p0_a_c1_20260826T115224Z_r6d_p65521` | `2026-08-26T11:52:34Z` | `0.13 s` | `29124 KiB` | `0` | `PASS_P0_A_C1` |

Exact-Q input SHA:
`13633ff1800863f9fac80ba720eb6c1051cef8ceb504e9a4f71557ff9c537a47`.
Control input SHA:
`a7c43f23cdc74737279b1c2df3b30e281d13be995d311663cea46498e5b8badb`.
