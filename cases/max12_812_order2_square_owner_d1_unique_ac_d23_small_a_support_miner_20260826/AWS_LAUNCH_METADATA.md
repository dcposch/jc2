# AWS launch metadata: small-`a` D1 `d=2,3` support miner

Date: 2026-08-26

Frozen source archive:

```text
f8f1538c8ae29911c9df76cb1304c0ab5aee50b3f4720c8256021fbd6f11d218
  /tmp/jc2_d1_unique_ac_d23_support_20260826_v1.tgz
```

| Field | Exact Q | `F_65521` control |
|---|---|---|
| host | Box03, `ip-172-30-0-249` | r6d, `ip-172-30-0-45` |
| tag | `max12_812_order2_square_d1_unique_ac_d23_support_q_20260826_box03` | `max12_812_order2_square_d1_unique_ac_d23_support_p65521_20260826_r6d` |
| launcher PID | `242590` | `305367` |
| characteristic token | `0` | `65521` |
| registered start | `2026-08-26T17:09:45Z` | same |
| timeout / VM cap | 600 s / 4,194,304 KiB | same |
| engine rc / validator | `0` / `PASS_D1_D23_SMALL_A_SUPPORT_CENSUS` | same |
| wall / peak RSS / swaps | 0.08 s / 18,528 KiB / 0 | 0.08 s / 18,340 KiB / 0 |
| inventory SHA-256 | `373552623cf15658efbef868be26f54dadea7712d417f884ab9c39d5475f45ce` | same |

The characteristic-independent inventories and stdout streams are
byte-identical.  The result JSON differs in the registered host/tag and
characteristic token.  The prime lane is only a coefficient/software
control; exact rational arithmetic is the support endpoint.

