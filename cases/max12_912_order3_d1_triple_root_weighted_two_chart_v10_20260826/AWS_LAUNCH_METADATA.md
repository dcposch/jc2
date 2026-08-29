# AWS launch metadata

Date: 2026-08-26 UTC

The registered source payload was deployed as an isolated `jc2` tree below
each registered job root.  The source archive was byte-identical on both
hosts:

```text
6c648fa7de7ae26c5bdbb54fb93127c9717dbc76e08559a1b422ac0881ebbdec  source_payload.tgz
```

Before either worker saw `GO`, both hosts passed the complete frozen source
closure, whose manifest SHA is

```text
a4f5b5fa169115d586f4ed3cbe4fe8c6e1c2b78630f0e5e1f9645d44d859bbba.
```

The V10 compiler also passed remote syntax compilation on both hosts.
Neither run directory contained `GO`, `DONE`, or `FAILED`.  The workers then
self-recorded `WAITING_GO` with the following live process custody:

- Box03 `98.80.65.144`, hostname `ip-172-30-0-249`, tag
  `max12_912_order3_d1_triple_root_weighted_two_chart_v10_20260826T050400Z_box03_forward`,
  worker PID `165189`, forward, 8 GiB / 1800 s, nice 10.
- r6d `100.26.198.153`, hostname `ip-172-30-0-45`, tag
  `max12_912_order3_d1_triple_root_weighted_two_chart_v10_20260826T050400Z_r6d_reverse`,
  worker PID `232475`, reverse, 8 GiB / 1800 s, nice 10.

At the live fleet audit at `2026-08-26T05:28:21Z`, Box03 had load 8.00 and
451 GiB available; r6d had load 5.01 and 333 GiB available.  The unrelated
r6d Singular worker PID `185517` and every other existing process were left
untouched.  Both `GO` sentinels were released at exactly
`2026-08-26T05:33:05Z`.

The first orchestration-side background-PID capture expanded to the literal
value `0`.  No computational state depended on that field: each waiting
worker had already self-recorded its own shell PID in `worker.metadata`.
Before `GO`, the bad value was preserved as `worker.launch.pid.initial_zero`,
an erratum was written, `worker.launch.pid` was restored from the
self-recorded metadata, and both corrected PIDs were checked live with `ps`.

The macOS tar writer also included `._*` AppleDouble sidecars.  Linux tar
reported the unsupported provenance xattr while extracting them.  They are
preserved in the remote-tree manifests, were not named by the source closure,
and were never imported by the compiler.  Every charged source file passed
its registered SHA after extraction.

