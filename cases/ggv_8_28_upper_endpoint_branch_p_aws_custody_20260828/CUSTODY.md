# Branch-P upper endpoint AWS custody

This standalone directory preserves terminal AWS outputs without changing the
byte set or `SOURCE.sha256` of the active branch-P source case.

## Exact raw-dp v4

- Remote source namespace:
  `/home/ubuntu/jobs/ggv_8_28_upper_endpoint_branch_p_20260827T191242Z_exact_raw_dp_v4/source`
- Remote output namespace:
  `/home/ubuntu/jobs/ggv_8_28_upper_endpoint_branch_p_20260827T191242Z_exact_raw_dp_v4/output`
- Audited host: Box03, `i-0ece0b9a3b4a7512f`, `r6i.16xlarge`.
- Start/end: `2026-08-27T19:13:02Z` / `2026-08-28T01:13:03Z`.
- Caps: 104857600 KiB virtual memory, 21600 seconds, one thread.
- Terminal state: exit 124 / `RUN_FAILED`; stdout stopped after the raw 303
  variable, 513 generator banner and `START_STD`; no decision marker.  Status
  is `RESOURCE_CAP_NO_VERDICT`.
- Remote evidence-manifest SHA-256:
  `0293646488bc86ed8f1b4e90c14bb44c3e00415a2be973449749ff0dcc019b07`.
- The remote `EVIDENCE.sha256` verified every output file before transfer.
  Every transferred file was then checked independently against the same
  remote manifest by basename.

This terminal output is neither a unit certificate nor a point witness and is
not promotable evidence for either endpoint outcome.

## Exact row-RREF v6

- Remote source/output tag:
  `ggv_8_28_upper_endpoint_branch_p_20260827T192127Z_exact_row_rref_v6`.
- Audited host: Box03, `i-0ece0b9a3b4a7512f`, `r6i.16xlarge`.
- Start/end: `2026-08-27T19:21:43Z` / `2026-08-28T01:21:46Z`.
- Caps: 134217728 KiB virtual memory, 21600 seconds, one thread.
- The deterministic exact-Q row-RREF check passed: 303 variables, 202 pivots,
  101 free variables, 497 generators, system SHA-256 `9b1d9f83...`.
- Terminal state: exit 124 / `RUN_FAILED`; CAS stdout stopped after the 303
  variable, 497 generator banner and `START_STD`; no decision marker.  Status
  is `RESOURCE_CAP_NO_VERDICT`.
- Remote evidence-manifest SHA-256:
  `04bff79f0b7d9db04a98ec02454956800d6c5c1371dd84f25627dfbb9b18ab3e`.
- The remote manifest verified before transfer; every transferred file was
  independently checked against it by basename.

This generator-change acceleration remains non-authoritative and produced no
promotable endpoint result.

## Box02 exact 466-generator prefix `std` r1

- Remote source/output tag:
  `ggv_8_28_upper_endpoint_branch_p_20260827T223028Z_exact_prefix_quotient_box02_r1`.
- Audited host: Box02, `i-010201a5da47795c4`, `x2idn.32xlarge`.
- Start/end: `2026-08-27T22:30:48Z` / `2026-08-28T00:28:48Z`.
- Caps: 134217728 KiB virtual memory, 7200-second global wall cap, one thread,
  zero swap, and cap plus 150 GiB start-headroom gate.
- Deterministic compile, exact 47-omission cofactor replay, source coverage,
  and source manifest checks all passed.
- Terminal state: exit 124 / `RUN_FAILED`; CAS stdout stopped after the 303
  variable, 466 generator banner and `START_STD`; no decision marker.  Status
  is `RESOURCE_CAP_NO_VERDICT`.
- Remote evidence-manifest SHA-256:
  `d93c43b76c0f0ad7dab3f0c60fad23a08f2fcdc86e0d267ea9b01a37e6d1e584`.
- The remote manifest verified before transfer; every transferred file was
  independently checked against it by basename.

This capped predecessor is preserved as non-evidence and was not modified or
rerun.  The live r2 lane uses a distinct `slimgb` reducer.

## Exact row-RREF dp/slimgb v11

- Remote source/output tag:
  `ggv_8_28_upper_endpoint_branch_p_20260827T203645Z_exact_row_rref_dp_v11`.
- Audited host: Box03, `i-0ece0b9a3b4a7512f`, `r6i.16xlarge`.
- Exact inputs: raw system SHA-256 `ead2fa404a74...`, row-RREF system SHA-256
  `9b1d9f83e369...`, dp/slimgb Singular source SHA-256 `77497060dcbf...`,
  and source-manifest SHA-256 `770c4aa73cf8...`.
- Start/end: `2026-08-27T20:36:58Z` / `2026-08-28T02:37:01Z`.
- Caps: 104857600 KiB virtual memory, 21600 seconds, one thread; swap stayed
  zero.  The largest RSS observed by the independent guard was 20,788,260 KiB;
  the timed stderr is empty, so this is explicitly a sampled maximum rather
  than a `/usr/bin/time` maximum.
- Deterministic row-RREF check passed (303 variables, 202 pivots, 101 free,
  497 generators).  Literal CAS stdout is only `ROW_RREF variables=303
  generators=497`, `START_STD`, blank line, `halt 1`.
- Terminal state: exit 124 / `RUN_FAILED`, with no `END`, `UNIT`, basis, or
  dimension marker: `RESOURCE_CAP_NO_VERDICT`.
- Remote evidence-manifest SHA-256:
  `2d658203ad439f3f982f5ac8e24d7734efe2ba6db42f4f739f382d71008efbf1`.
  It verified remotely, and all 15 transferred files replayed against it.

This acceleration produced neither a unit certificate nor a point witness.

## Box02 exact 466-generator prefix `slimgb` r2

- Remote source/output tag:
  `ggv_8_28_upper_endpoint_branch_p_20260828T004311Z_exact_prefix_quotient_slimgb_box02_r2`.
- Audited host: Box02, `i-010201a5da47795c4`, `x2idn.32xlarge`.
- Exact inputs: raw system SHA-256 `ead2fa404a741c5b...`, prefix-quotient
  system SHA-256 `8e25502c5f8e7b73...`, `slimgb` Singular source SHA-256
  `06bd3a5abaecf0c...`, and source-manifest SHA-256 `c3c6b19cb35885e2...`.
- Start/end: `2026-08-28T00:43:29Z` / `2026-08-28T02:41:29Z`.
- Caps: 134217728 KiB virtual memory, 7200-second global wall cap, one thread,
  zero swap, and cap plus 150 GiB start-headroom gate.  The largest RSS
  observed by the independent poller was 13,457,084 KiB; timed stderr is empty,
  so this is a sampled maximum rather than a `/usr/bin/time` maximum.
- Deterministic compile, source coverage, and exact 47-omission cofactor replay
  passed: 303 variables, 513 raw generators, 466 retained generators, 697
  cofactor entries / 994 terms, all 18 endpoint generators, no `D23`, and no
  `G22`.
- Literal CAS stdout is only `PREFIX_QUOTIENT variables=303 generators=466`,
  `START_SLIMGB`, blank line, `halt 1`.
- Terminal state: exit 124 / `RUN_FAILED`, with no `END`, `UNIT`, basis,
  dimension, or witness marker: `RESOURCE_CAP_NO_VERDICT`.
- Remote evidence-manifest SHA-256:
  `465a313113af3f9b690ce2bb96e50f1b4030492b58ed7d979ec5b3f28fb868a1`.
  It verified remotely, and all 21 transferred files replayed against it.

This distinct reducer produced neither a unit certificate nor a point witness
and is not promotable evidence for either endpoint outcome.

## Box03 weighted-homogeneous saturation v12

- Remote source/output tag:
  `ggv_8_28_upper_endpoint_branch_p_20260827T204925Z_exact_homogeneous_sat_v12`.
- Audited host: Box03, `i-0ece0b9a3b4a7512f`, `r6i.16xlarge`.
- Exact inputs: raw system SHA-256 `ead2fa404a741c5b...`, homogeneous system
  SHA-256 `f348529e0dab8b69...`, Singular source SHA-256
  `58be75cabfacf7d8...`, and source-manifest SHA-256 `a9e318d9f321cb03...`.
- Start/end: `2026-08-27T20:49:39Z` / `2026-08-28T02:49:41Z`.
- Caps: 104857600 KiB virtual memory, 21600 seconds, one thread; swap stayed
  zero.  The largest RSS observed by the independent guard was 76,565,792 KiB;
  timed stderr is empty, so this is a sampled maximum rather than a
  `/usr/bin/time` maximum.
- Deterministic compile, homogeneous check, and raw-to-homogeneous replay all
  passed: 513 raw generators, 514 homogeneous generators, normalization
  `lambda-u^22`, saturation variable `lambda`, no `D23`, and no `G22`.
- Literal CAS stdout is only `HOMOGENIZED variables=305 generators=514`,
  `START_SAT`, blank line, `halt 1`.
- Terminal state: exit 124 / `RUN_FAILED`, with no `END`, `UNIT`, basis, or
  dimension marker: `RESOURCE_CAP_NO_VERDICT`.
- Remote evidence-manifest SHA-256:
  `2dea07031dc3f6162608aa2da3be287613d6a7510ac621a8efaab083cc03e375`.
  It verified remotely, and all 18 transferred files replayed against it.

This homogeneous/saturated acceleration is a cross-check only.  It produced
neither a unit certificate nor a point witness and is not promotable evidence
for either endpoint outcome.

## Box03 authoritative literal raw `lp` v13

- Remote source/output tag:
  `ggv_8_28_upper_endpoint_branch_p_20260827T210412Z_exact_raw_lp_280g_v13`.
- Audited host: Box03, `i-0ece0b9a3b4a7512f`, `r6i.16xlarge`.
- Exact inputs: raw system SHA-256 `ead2fa404a741c5b...`, literal Singular
  source SHA-256 `8647c6e73c9e23dd...`, and source-manifest SHA-256
  `af2a1f8c5b42ef47...`.
- Start/end: `2026-08-27T21:04:24Z` / `2026-08-28T03:04:26Z`.
- Caps: 293601280 KiB virtual memory, 21600 seconds, one thread; swap stayed
  zero.  The largest RSS observed by the independent guard was
  290,082,384 KiB; timed stderr is empty, so this is a sampled maximum rather
  than a `/usr/bin/time` maximum.
- Deterministic raw compile and source checks passed: 303 variables, 513
  generators, all 18 `D22` coefficient generators, and five later modes.
- Literal CAS stdout is only `RAW_DIRECT variables=303 generators=513`,
  `START_STD`, blank line, `halt 1`.
- Terminal state: exit 124 / `RUN_FAILED`, with no `END`, `UNIT`, basis,
  dimension, properness, or witness marker: `RESOURCE_CAP_NO_VERDICT`.
- At release the independent guard encountered the exited process briefly as
  a zero-RSS `[Singular]` zombie and failed closed with identity status 77.
  The wrapper had already recorded normal wall-cap exit 124; no guard signal
  was sent, no safety threshold was reached, and no residual process remained.
- Remote evidence-manifest SHA-256:
  `c911a9482656ff2bc58caa1d2975a58d40540073d717bc51b862b4d4b1b8d135`.
  It verified remotely, and all 12 transferred files replayed against it.

This is the authoritative literal raw formulation, but its capped output is
neither a unit certificate nor a point witness and is not promotable evidence
for either endpoint outcome.
