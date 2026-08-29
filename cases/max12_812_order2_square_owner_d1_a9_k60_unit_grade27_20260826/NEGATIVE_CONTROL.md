# Negative control: V1 target-precedence failure

Date: 2026-08-26

Status: **PRESERVED FAIL-CLOSED SOFTWARE CONTROL; NO MATHEMATICAL VERDICT.**

Both registered AWS lanes compiled and ran the corrected V3 complete-source
parent.  Before the failing line, both exact Q and `F_65521` printed

```text
D1A9_K60_GRADE27_IDENTITIES=1
D1A9_K60_MOVING_CONNECTION_AND_K6JET=1
D1A9_K60_DELAYED_K2_K10_K6=1
D1A9_K60_PARENT_COUNTS=1
```

The V1 target check wrote `sigma^38/4`; Singular parsed this as raising a
polynomial to the nonintegral exponent `38/4`.  This left the target boolean
undefined, caused later diagnostic cascades, and prevented the exact-contact
endpoint.  Both validators rejected the output.  V1 is immutable and is not
evidence for or against the branch.

Telemetry:

- exact Q / Box03: engine `rc=0`, wall `5.91s`, peak RSS `1255360 KiB`,
  swaps `0`, stdout SHA-256
  `6f701e314f3312767bbe48ae2c98019a7f7abda41592dd2e4cbd15ead177f0f6`;
- `F_65521` / r6d: engine `rc=0`, wall `3.97s`, peak RSS `889160 KiB`,
  swaps `0`, stdout SHA-256
  `5234b0737f5a2fe7d1db4a575170e9a0ee0003e1b7d6319e98c4e04fcf96221c`;
- identical validator SHA-256
  `1943309f158a6b2da1522e1349a7a5c835b14aed4c0f8f1df5b231fe97113cb4`.

The nonmutating V2 successor changes only that expression to
`(sigma^38)/4`.

