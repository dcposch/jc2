# AWS launch metadata: D1 `a=8,d=3` target-shadow chamber split

Date: 2026-08-26

All three executions used the identical source archive

```text
a6110b910ba4de57de9744b846f3bbbcdc41709a2d18bcf53522c3f145fbb6a5
```

and independently passed the frozen on-host `FREEZE.sha256` check before
compilation.  The retrieved mathematical stdout is byte-identical in all
three characteristics, with SHA-256
`389467ccb94d61c0c68e9615e4d21d68f7318a04b9b50c9d81ff8b475f1dc03c`.

| field | exact `Q` | `F_65519` control | `F_65521` control |
|---|---|---|---|
| host | Box02 / `ip-172-30-0-186` | Box03 / `ip-172-30-0-249` | r6d / `ip-172-30-0-45` |
| tag | `max12_812_order2_square_d1_a8d3_targetshadow_q_box02_20260826T2130Z` | `max12_812_order2_square_d1_a8d3_targetshadow_p65519_box03_20260826T2130Z` | `max12_812_order2_square_d1_a8d3_targetshadow_p65521_r6d_20260826T2130Z` |
| launcher PID | `335211` | `275814` | `348397` |
| start UTC | `2026-08-26T21:15:09Z` | same | same |
| end UTC | `2026-08-26T21:23:45Z` | `2026-08-26T21:21:54Z` | `2026-08-26T21:21:54Z` |
| wall | `8:36.60` | `6:44.53` | `6:45.47` |
| peak RSS | `26,628,184 KiB` | `21,419,004 KiB` | `21,415,716 KiB` |
| VM cap | `1,572,864,000 KiB` | `450,887,680 KiB` | `450,887,680 KiB` |
| engine rc | `0` | `0` | `0` |
| swaps | `0` | `0` | `0` |
| validator | `PASS_D1_A8D3_TARGETSHADOW_CHAMBER_EMPTY` | same | same |

Exact `Q` is the characteristic-zero producer endpoint.  The two fresh good
primes are independent host/software controls, not substitutes for the
characteristic-zero calculation.  Every retrieved source, compiled program,
transcript, resource record, and validation byte is pinned in
`EVIDENCE.sha256`.
