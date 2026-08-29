# AWS launch metadata: exceptional D1 `E`

Date: 2026-08-26

Frozen source archive:

```text
d516f23b4800080677322d6940ab1e5b82f6fa2bead32798a046097d476fb25a
  /tmp/jc2_d1_e_a1d3_opposite_root_pole3_20260826_v1.tgz
```

| Field | exact Q | `F_65519` screen | `F_65521` screen |
|---|---|---|---|
| host | Box02, `ip-172-30-0-186` | Box03, `ip-172-30-0-249` | r6d, `ip-172-30-0-45` |
| tag | `max12_812_order2_square_d1_e_a1d3_opposite_root_pole3_q_box02_20260826T1855Z` | `max12_812_order2_square_d1_e_a1d3_opposite_root_pole3_p65519_box03_20260826T1855Z` | `max12_812_order2_square_d1_e_a1d3_opposite_root_pole3_p65521_r6d_20260826T1855Z` |
| launcher PID | 303084 | 257871 | 323913 |
| characteristic | 0 | 65519 | 65521 |
| start UTC | 18:55:16 | 18:55:16 | 18:55:16 |
| end UTC | 18:58:29 | 18:58:16 | 18:58:26 |
| timeout / VM cap | 1,800 s / 16,777,216 KiB | same | same |
| engine rc | 0 | 0 | 0 |
| validator | `PASS_D1_E_A1D3_OPPOSITE_ROOT_POLE3_EMPTY` | same | same |
| wall | 3:13.26 | 3:00.48 | 3:09.87 |
| peak RSS | 783,392 KiB | 618,052 KiB | 617,032 KiB |
| swaps | 0 | 0 | 0 |
| compiled Singular SHA-256 | `577dd40a9de627dd3fa831b8558a8ec84d66aed116cabf8a719fe09ae381cb51` | `cb1e9b44e623e443508835057b4a64b1c85c2b0a7e617706d1cdde78c6f8a858` | `d4b8aa28b06d262eca3499120c89bbe8b1d863e2e5e2fc11b70d507bebb0802b` |
| stdout SHA-256 | `0eaede5fdaa3b7a87d91c70d3e210ba74c416cc6654e19a5c03946fbb61bd888` | same | same |

GNU `time -v` is the only engine-stderr content.  The compiler stderr files
are empty.  Characteristic-specific generated scripts and JSON custody
differ as expected; the exact boolean/census streams are byte-identical.
