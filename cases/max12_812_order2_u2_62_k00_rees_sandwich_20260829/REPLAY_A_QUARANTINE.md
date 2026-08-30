# K00-REES-SANDWICH triangular replay A quarantine

UTC: 2026-08-30  
Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`  
Lifecycle: `QUARANTINED / NO VERDICT / VALIDATOR REGRESSION`

Replay A used packet-manifest SHA-256
`10fbaeb91137b3bd1b035de912edd847b21a461e9a8184ed5e04022fcad9c8c4`
on r6b, instance `i-0f089e64c378f5da3`, boot
`3dca2ad4-9cbb-48f9-9c62-02d37a90bd19`.

The planted undefined-symbol process was correctly rejected by the shared
validator.  The subsequent triangular replay then used `IN` as an ideal
identifier, but `IN` is reserved by Singular 4.3.2.  Singular PID/PGID 46808,
start identity
`boot=3dca2ad4-9cbb-48f9-9c62-02d37a90bd19;start_ticks=12559328`, emitted 28
generic diagnostic matches, returned zero, and continued to downstream
unconditional output.  The route runner rejected it with
`RUNNER_FAIL=SEARCH_OUTPUT_VALIDATION`; it did not launch the subsequent
initial-strictness process.  PID 46808 and the negative-control PID 46792 were
both absent at the post-run audit.

The frozen rejected-output manifest `REPLAY_A_REJECTED.sha256` has SHA-256
`b4a3fad463e7ff843bf764867eba9af773e4ed39a733ed89105b4e1690114a5d`.
Every mathematical-looking line from replay A is `NO VERDICT`.  Replay B was
created in a new directory from immutable inputs, changed only the reserved
identifier to `transformedRows`, and used a new payload, packet, lane tag,
and process.

This incident independently demonstrates that the V2/replay-B validator
rejects a real unplanted Singular diagnostic even when the child exits zero
and later prints a nominal PASS marker.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `1606`.
- Body SHA-256:
  `fd2db8d702a1cf82d8a6027a8b1f6247f36536614c98c72ee6dea76088d8d796`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
