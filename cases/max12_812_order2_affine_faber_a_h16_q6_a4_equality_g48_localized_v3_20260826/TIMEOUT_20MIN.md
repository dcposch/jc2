# Localized V3 20-minute timeout custody

Date: 2026-08-26

Status: **DUAL-AWS TIMEOUT; NO MATHEMATICAL VERDICT.**

The exact-Q and characteristic-`65521` runs both compiled and passed the
frozen-source check, then reached the registered 1200-second engine timeout
before emitting any row, chart, or endpoint output.  Both validators say

```text
engine_rc=124
validator=FAIL_ENGINE_OR_TIMEOUT
```

The exact-Q run used 20:00.48 wall time and at most 12,526,236 KiB RSS; the
finite-field software control used 20:00.64 and at most 11,841,232 KiB RSS.
Both stayed at approximately one full CPU and reported zero swap.  Memory
continued rising through the run, so identical frozen bytes were relaunched
separately with a longer cap; that later run is independent custody.

The copied output is under `evidence_v3_timeout20/` and is pinned in
`EVIDENCE_TIMEOUT20.sha256`.  This timeout establishes neither a unit ideal
nor a survivor and makes no rational-regrading, source/Rees, order-two,
maximum-twelve, or JC2 claim.
