# AWS launch metadata

Date: 2026-08-26 UTC

The registered V11 payload was deployed below the two isolated job roots.
The source archive was byte-identical on both hosts:

```text
4627164bc879e2268c2eb3187443a2b5fd348ade732077ca2b4657bd58f6c34d  v11_moving_load_payload_20260826T054500Z.tgz
```

Before either worker saw `GO`, both hosts passed the complete frozen source
closure and remote syntax compilation.  The source-closure manifest has SHA

```text
c170e8cb2343b20bb70a8d3051b64dba72c482789e3fd8e154d049c1496604ba.
```

Neither run directory contained `GO`, `DONE`, or `FAILED` at launch.  Both
workers self-recorded `WAITING_GO`, and live process custody was checked:

- Box03 `98.80.65.144`, hostname `ip-172-30-0-249`, tag
  `max12_912_order3_d1_triple_root_moving_load_v11_20260826T054500Z_box03_forward`,
  PID `168130`, forward, 8 GiB / 1800 s, nice 10.
- r6d `100.26.198.153`, hostname `ip-172-30-0-45`, tag
  `max12_912_order3_d1_triple_root_moving_load_v11_20260826T054500Z_r6d_reverse`,
  PID `235150`, reverse, 8 GiB / 1800 s, nice 10.

The live fleet audit at `2026-08-26T05:48:06Z` found Box03 load 9.00 with
445 GiB available and r6d load 6.02 with 330 GiB available; both had zero
swap.  The unrelated r6d worker PID `185517` and every other existing process
were left untouched.  Both workers started at `2026-08-26T05:49:57Z`; both
`GO` sentinels were released at `2026-08-26T05:50:25Z`; both workers finished
at `2026-08-26T05:50:32Z`.

The macOS tar writer attached unsupported provenance xattrs, which Linux tar
warned about while extracting.  No AppleDouble sidecar was present in this
V11 payload.  Every charged file passed its registered SHA before and after
the run.  The warnings are provenance-only and are preserved by the remote
custody manifests.
