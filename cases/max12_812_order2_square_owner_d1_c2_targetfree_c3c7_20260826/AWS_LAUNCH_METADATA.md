# AWS launch metadata: D1 target-free primary-C2 cell, `3<=c<=7`

Date: 2026-08-26

All three executions used source archive
`/tmp/jc2_d1_c2_targetfree_c3c7_20260826_v1.tgz`, SHA256
`74f830bfce1546d415244a7bb646c6a288e6c63114200aba1c9db3a0d2b19bce`.
Each remote launcher rehashed the archive, extracted it into a fresh unique
job directory, and verified `FREEZE.sha256` before compilation.

| endpoint | host | registered tag | characteristic | launcher PID |
|---|---|---|---:|---:|
| exact Q | Box02 (`ip-172-30-0-186`) | `max12_812_order2_square_d1_c2_targetfree_c3c7_q_box02_20260826T203500Z` | 0 | 325142 |
| control | Box03 (`ip-172-30-0-249`) | `max12_812_order2_square_d1_c2_targetfree_c3c7_p65519_box03_20260826T203500Z` | 65519 | 269674 |
| control | r6d (`ip-172-30-0-45`) | `max12_812_order2_square_d1_c2_targetfree_c3c7_p65521_r6d_20260826T203500Z` | 65521 | 340721 |

The route-specific compiler and runner refuse non-Linux, non-Amazon hosts,
require the registered lane tag, use ordinary polynomial rings, cap virtual
memory at 32 GiB, and fail closed on missing/nonunique sentinels, engine
diagnostics, nonzero swap, timeout, or nonzero engine status.
