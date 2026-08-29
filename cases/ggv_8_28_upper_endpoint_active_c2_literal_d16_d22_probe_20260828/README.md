# Active-c2 literal D16--D22 tail probe

Status: **EXACT PRODUCER / AWAITING DIFFERENT-MODEL REVIEW**

This standard-library checker continues the frozen rational `D0..D15`
survivor through the authoritative `G16..G21` windows and the absent-`G22`
endpoint.  It pins all load-bearing source bytes, replays the prefix, solves
the born modes exactly, checks the raw determinant rows, and runs two live
mutations.

Replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_upper_endpoint_active_c2_literal_d16_d22_probe_20260828/probe_literal_tail.py
```

Expected marker:

```text
PASS_EXACT_ACTIVE_C2_LITERAL_D16_D22_TAIL
```

The result kills one literal survivor at `D22=1`; it does not exclude the
general deep endpoint locus.

