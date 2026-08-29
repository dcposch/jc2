# AWS launch metadata: low-`a` D1 `d=2,3` local-row batch

Date: 2026-08-26

Frozen source archive:

```text
7f0cab79346f218977ca380d44949512a65358e64ebbc00502623b4ed1c7c218
  /tmp/d1_lowa6_localrow_v7_20260826.tar.gz
```

| Field | exact Q | `F_65521` control |
|---|---|---|
| host | Box03, `ip-172-30-0-249` | r6d, `ip-172-30-0-45` |
| tag | `max12_812_order2_square_d1_unique_ac_d23_lowa6_localrow_v7_q_20260826` | `max12_812_order2_square_d1_unique_ac_d23_lowa6_localrow_v7_f65521_20260826` |
| launcher PID | 249616 | 313357 |
| characteristic | 0 | 65521 |
| registered start | 2026-08-26T17:50:46Z | same |
| engine end | 2026-08-26T17:50:57Z | 2026-08-26T17:50:53Z |
| timeout | 1,800 s | same |
| virtual-memory cap | 33,554,432 KiB | same |
| engine rc | 0 | 0 |
| validator | `PASS_D1_D23_LOWA6_LOCAL_ROW_ELEVEN_EMPTY` | same |
| wall | 11.13 s | 7.62 s |
| peak RSS | 2,486,060 KiB | 1,961,792 KiB |
| swaps | 0 | 0 |
| compiled input SHA-256 | `d05e9da879ec67edb83129dbdb5c389b2ba03732350ef9beeadd3d9aee049912` | `5a02901959c347bf372fe04bce396c75ed75c6a48041f56dade57f590574fec2` |
| stdout SHA-256 | `ad447f4daae1c62374c392e8fb297052fde2eafe20efcf8ba1595384ff457775` | same |

The stdout streams are byte-identical exact boolean/census markers.  The
compiled scripts are characteristic-specific.  GNU `time -v` is the only
engine-stderr content; compiler stderr is empty on both hosts.

The prior V5 dual run also returned rc zero for the eleven positive blocks,
but its `E` control certified only source support.  V7 supersedes it by
reconstructing and checking the actual `RA^2/L^2` second correction.
