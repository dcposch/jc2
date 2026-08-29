# AWS launch metadata: tied D1 `(a,c,r)=(3,3,2)` C2 maximal-pole producer

Date: 2026-08-26

All three executions used source archive
`/tmp/jc2_d1_tied_a3c3r2_c2_maxpole2_20260826_v1.tgz`, SHA256
`a5380e75cdc897e61d1ce88f508d7f343a90ca43b4e917b9304c2744a9b325c1`.
Each remote launcher rehashed the archive, extracted into a fresh unique job
directory, and verified `FREEZE.sha256` before compilation.

| endpoint | host | registered tag | characteristic | launcher PID |
|---|---|---|---:|---:|
| exact Q | Box02 (`ip-172-30-0-186`) | `max12_812_order2_square_d1_tied_a3c3r2_c2_maxpole2_q_box02_20260826T201345Z` | 0 | 321837 |
| control | Box03 (`ip-172-30-0-249`) | `max12_812_order2_square_d1_tied_a3c3r2_c2_maxpole2_p65519_box03_20260826T201345Z` | 65519 | 268065 |
| control | r6d (`ip-172-30-0-45`) | `max12_812_order2_square_d1_tied_a3c3r2_c2_maxpole2_p65521_r6d_20260826T201345Z` | 65521 | 338016 |

The route-specific compiler and runner refuse non-Linux, non-Amazon hosts,
require the registered lane tag, use an ordinary polynomial ring, cap virtual
memory at 16 GiB, and fail closed on missing/nonunique sentinels, engine
diagnostics, nonzero swap, timeout, or nonzero engine status.
