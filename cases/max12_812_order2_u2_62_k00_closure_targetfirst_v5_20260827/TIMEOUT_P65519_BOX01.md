# Capped V5 screen: p=65519 on Box01

Status: **TIMEOUT / NO VERDICT**

The frozen target-first V5 source was run on AWS host
`ip-172-30-0-237` under lane
`max12_812_order2_u2_62_k00_closure_targetfirst_v5_p65519_20260827T080414Z_box01`.
It reached `K00_STAGE_GOPEN_SOURCE_START` after passing every source, type,
`Jdet`-separation, invariant-core, restriction-before-saturation, and
equivalence guard.  No later stage or endpoint was emitted.

```text
start_utc=2026-08-27T08:04:55Z
end_utc=2026-08-27T08:24:55Z
engine_rc=124
validator=TIMEOUT_NO_VERDICT
elapsed=20:00.10
max_rss_kib=2359300
swaps=0
stdout_bytes=433
input_sha256=20d5be90a6710a2941c0d7d47cf7f155f146c052825029cd75c40abc9716b0ac
```

The ordering reduced peak memory substantially relative to V2/V4 but did
not reach an endpoint.  This finite-field timeout neither proves nor
disproves the K00 incidence, does not test the characteristic-zero endpoint,
and has no JC2 consequence.  The raw compiler/run custody is preserved under
`aws_p65519_box01_timeout/`.  No further monomial-order variants are planned.
