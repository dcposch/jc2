# AWS launch metadata: D1 `a=8,d=2` load-first split

Date: 2026-08-26

Frozen source archive:

```text
952330121f34f99a4c14bde319766373d14d2da69c47aed2c40071e701231dfb
  /tmp/d1_a8_d2_loadfirst_dual_v1_20260826.tar.gz
```

| Field | exact Q | `F_65521` screen | `F_65519` screen |
|---|---|---|---|
| host | Box03, `ip-172-30-0-249` | r6d, `ip-172-30-0-45` | Box02, `ip-172-30-0-186` |
| tag | `max12_812_order2_square_d1_a8_d2_loadfirst_dual_q_box03_20260826` | `max12_812_order2_square_d1_a8_d2_loadfirst_dual_p65521_r6d_20260826` | `max12_812_order2_square_d1_a8_d2_loadfirst_dual_p65519_box02_20260826` |
| launcher PID | 254161 | 318941 | 298666 |
| characteristic | 0 | 65521 | 65519 |
| start/end UTC | 18:28:03 / 18:28:03 | same | same |
| timeout / VM cap | 1,800 s / 33,554,432 KiB | same | same |
| engine rc | 0 | 0 | 0 |
| validator | `PASS_D1_A8_D2_LOADFIRST_DUAL_EMPTY` | same | same |
| wall | 0.57 s | 0.33 s | 0.33 s |
| peak RSS | 136,780 KiB | 111,048 KiB | 111,360 KiB |
| swaps | 0 | 0 | 0 |
| inventory SHA-256 | `7c9cdf0aa93fb541fd4f1895ed6fe81ef21226f0522b4f53404324ceb485ec3c` | `7a4a765c60d1f57d3a820452c045a6b9e9f208f78e22c5a110e01d60568bec4d` | `613b4453031c72828deb16b6bd6398bceaa97398e5ede8bf8b2e6955becce9c1` |
| stdout SHA-256 | `3c95b429d092c487e676477cf807272e7beec1dfa4338514744d1fb8999495df` | same | same |

GNU `time -v` is the only engine-stderr content.  The characteristic-specific
compiled scripts differ as expected; the exact boolean/census streams are
byte-identical.
