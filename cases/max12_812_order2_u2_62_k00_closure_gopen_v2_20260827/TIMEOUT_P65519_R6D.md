# Capped V2 screen: p=65519 on r6d

Status: **TIMEOUT / NO VERDICT**

The frozen exact-equivalent g-open V2 source was run on AWS host
`ip-172-30-0-34` under lane
`max12_812_order2_u2_62_k00_closure_gopen_v2_p65519_20260827T074000Z_r6d`.
It reached `K00_STAGE_GOPEN_SOURCE_START` after passing every source, type,
`Jdet`-separation, invariant-core, restriction-before-saturation, and
equivalence guard.  No later stage or endpoint was emitted.

```text
start_utc=2026-08-27T07:40:27Z
end_utc=2026-08-27T08:10:27Z
engine_rc=124
validator=TIMEOUT_NO_VERDICT
elapsed=30:00.37
max_rss_kib=11424952
swaps=0
stdout_bytes=391
input_sha256=74570a40d652348773494583ffaa4817e25dae837ecac841fc96a16eba1b389f
```

This finite-field timeout neither proves nor disproves the K00 incidence,
does not test the characteristic-zero endpoint, and has no JC2 consequence.
The raw compiler/run custody is preserved under `aws_p65519_r6d_timeout/`.
