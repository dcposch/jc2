# Opus5 hostile review: unit-root transport

Verdict: **REPAIR — THEOREM TRUE**

The independent checker reconstructs the complete local `D7..D22` ladder
from the general reduced prefix.  It repairs the producer's false claim that
the normalized pre-D7 prefix is already the pinned post-D7 fixed prefix, and
it proves the missing bridge directly.

Replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_upper_endpoint_unit_root_transport_review_opus5_20260828/verify_unit_root_transport_review_opus5.py
```

Expected final marker:

```text
RESULT: ALL CHECKS PASSED
```

Promotable conclusion: under the named reduced branch-P hypotheses, any
simple root of `A` where `V0` is a unit contradicts `D22=1`.  For squarefree
`A`, every endpoint stratum `gcd(A,V0) != A` is therefore field-empty.

