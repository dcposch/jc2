# Active-c2 D11--D15 exact extension

Status: **INTERNAL INDEPENDENT AUDIT / REPAIR / EXACT PRODUCER-CHECKED**

This standard-library case independently rebuilds the complete characteristic
recurrence through weight 13, audits the charged D8--D11 identities, repairs
the valuation overstatement at D11, and extends the exact `D=0`, `c2!=0`
branch through the next paired lift and product rung.  It also replays one
literal raw-window survivor with `c2=c6=1` through `D15` and independently
keeps the `c2=0,A|V0` companion separate.

Replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/verify_active_c2_extension.py
```

Expected marker:

```text
PASS_REPAIR_ACTIVE_C2_D8_D13_EXTENSION
```

Scope is characteristic-zero field/radical necessity plus one exact rational
raw specialization.  This is not a scheme statement, q1 theorem, endpoint
exclusion, unrestricted branch-P theorem, Keller theorem, or JC2 result.
