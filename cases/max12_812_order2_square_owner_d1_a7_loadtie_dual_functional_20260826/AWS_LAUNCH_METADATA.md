# AWS launch metadata: D1 `a=7` load-tie dual-functional wall

Date: 2026-08-26

Frozen source archive:

```text
961160487ad73db79475f37b7d7868733141bc5b65fed3261d08fc54efa86be1
  /tmp/d1_a7_loadtie_dual_v2_20260826.tar.gz
```

| Field | exact Q | `F_65521` screen | `F_65519` screen |
|---|---|---|---|
| host | Box03, `ip-172-30-0-249` | r6d, `ip-172-30-0-45` | Box02, `ip-172-30-0-186` |
| tag | `max12_812_order2_square_d1_a7_loadtie_dual_q_box03_20260826` | `max12_812_order2_square_d1_a7_loadtie_dual_p65521_r6d_20260826` | `max12_812_order2_square_d1_a7_loadtie_dual_p65519_box02_20260826` |
| launcher PID | 251884 | 316263 | 296213 |
| characteristic | 0 | 65521 | 65519 |
| registered start | 2026-08-26T18:09:55Z | same | same |
| engine end | 2026-08-26T18:09:56Z | same | same |
| timeout | 1,800 s | same | same |
| virtual-memory cap | 33,554,432 KiB | same | same |
| engine rc | 0 | 0 | 0 |
| validator | `PASS_D1_A7_LOADTIE_DUAL_FUNCTIONAL_D2_D3_EMPTY` | same | same |
| wall | 1.63 s | 1.00 s | 0.98 s |
| peak RSS | 336,972 KiB | 268,448 KiB | 268,068 KiB |
| swaps | 0 | 0 | 0 |
| inventory SHA-256 | `68e20dc4a4cd64006a642deea5d70d25e11936ba0f612e20b20dcad8f771a679` | `4ecf966e6c5661b4cd4a0df69fdccb85ab89ee36887cc9b67ea25629a149c23f` | `9fd3609b1678e0ed47842d113b2a13de6d656d73672fcda90af1bda400e187e7` |
| stdout SHA-256 | `de1f2dd8288da29a84fd29a96a79b9d80de167732ce94768609680702643766b` | same | same |

The stdout streams are byte-identical exact boolean/census markers.  The
compiled scripts are characteristic-specific.  GNU `time -v` is the only
engine-stderr content, and compiler stderr is empty on all three hosts.

The first frozen Box03 preflight exposed only a generator-parenthesization
bug in the moving-root sentinel: the source expression passed to the sigma
extractor was parsed as a square of only its last summand.  No mathematical
endpoint was reached.  The final frozen compiler encloses the complete root
series before squaring; exact Q and both prime screens then pass every
sentinel.  No failed run is imported into the result.
