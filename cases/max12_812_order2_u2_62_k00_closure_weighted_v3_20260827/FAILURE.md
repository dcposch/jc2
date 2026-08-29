# V3 failed screen

Date: 2026-08-27

Status: **REJECTED IMPLEMENTATION; NO ENDPOINT.**

The registered Box01 lane emitted

```text
K00_WEIGHT_ORDER=FABER_LAMBDA_EXACT
K00_FAIL=INVARIANT_CORE_ROW_MAP
```

before any source saturation.  The `wp(...,0,...,0)` order therefore failed
the mandatory invariant-core membership gate and cannot be used for this
calculation.  Singular also diagnosed `quit(81)` as undefined and continued;
the lane was explicitly terminated at PID 586851 after the failed marker was
observed.  Runner state is `engine_rc=1`, `validator=FAIL_ENGINE`.

No V1 or V2 process was touched.  No mathematical statement follows from
this lane.  A repaired ordering must use a genuine positive global block,
for example structural `wp(1,8,7,6,5,4,3,2)` followed by `dp(7)` on the
retained loads, and must pass the same core gate before launch is interpreted.
