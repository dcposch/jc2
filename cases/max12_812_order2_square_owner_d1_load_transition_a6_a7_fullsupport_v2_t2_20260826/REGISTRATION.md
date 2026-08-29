# Registration: D1 `a=6,7` V2 lower-load tail alignment

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS REPAIR.**

V1 failed closed at the first new `k6*C/L` source bridge.  Exact source
rows show that the Laurent generating-series term is

```text
(3/4)*sigma^17*t^2*k6*C*Inv1,
```

not the V1 `t^1` term.  V2 pins V1 and changes exactly the two generated
occurrences (one for `a=6`, one for `a=7`) from `t` to `t*t`.  All complete
source extraction, support filters, moving row transforms, recurrence/root
maps, negative controls, validators, caps, and scope remain unchanged.

Frozen negative control:

```text
158ebf84bf8c13143d606b0ffbd2cd4c56e0a6033f1a57d11d61ae30ce220a4e
  ../max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_20260826/compile_load_transition.py
71e076ff360c8bd7d0ca00feee153d7e1794619b980391aa49a473c098bcb721
  ../max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_20260826/FREEZE.sha256
df29e2d45d880d734dafbd2a26004d4dc3a32d27f002dd51cddc71c93e63fa22
  ../max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_20260826/RESULT_NEGATIVE_CONTROL.md
```

Dual exact-Q/`F_65521` AWS acceptance and the theorem firewall are exactly
those of V1.  Dual PASS remains producer-tier pending hostile review.

