# Capped V4 screen: p=65521 on Box01

Status: **TIMEOUT / NO VERDICT**

The frozen repaired positive-weight global-block V4 source was run on AWS
host `ip-172-30-0-237` under lane
`max12_812_order2_u2_62_k00_closure_weighted_v4_p65521_20260827T075700Z_box01`.
It reached `K00_STAGE_GOPEN_SOURCE_START` after passing every source, type,
`Jdet`-separation, invariant-core, restriction-before-saturation, and
equivalence guard.  No later stage or endpoint was emitted.

```text
start_utc=2026-08-27T07:56:58Z
end_utc=2026-08-27T08:16:59Z
engine_rc=124
validator=TIMEOUT_NO_VERDICT
elapsed=20:01.23
max_rss_kib=23459296
swaps=0
stdout_bytes=436
input_sha256=6406b8b73d5e744f1f6d676011a799a5f24e5ac261af356cd481fc39ee6cd363
```

This finite-field timeout neither proves nor disproves the K00 incidence,
does not test the characteristic-zero endpoint, and has no JC2 consequence.
The raw compiler/run custody is preserved under `aws_p65521_box01_timeout/`.
