# Arbitrary-Q origin modular solver portfolio r3 — result

Date: 2026-08-28

## Verdict

`NO_VERDICT_MODULAR_SIGNAL_ABSENT_OR_CAP`

Four preregistered, target-faithful modular discriminator jobs completed their
AWS custody wrappers and each solver reached its 1800-second inner cap without
emitting a unit, zero-normal-form, basis, syzygy, witness, or replayable
certificate.  This is a bounded computational non-result.  It is not ideal
nonmembership, consistency, existence, or field nonemptiness over any field.
No exact-Q replay was authorized or run.

## Frozen mathematical input

All four jobs independently replayed the same immutable source archive and
exact receiver-row deduplication before invoking a solver:

```text
b2e67b162890eb8231ebb49fcfe90ac61cd25d605cbe5cec434eff831a8cf9c2  PORTFOLIO_SOURCE.tar.gz
f0385348f0057900bb82f1a68f7f66a4b095051773aedb77d8c8b5d55597ffb2  PREREGISTRATION.md
e08639816f9da99cec25b6a70b543eac715c83850c85b350aad80c21747c8816  PREREGISTRATION.sha256
455e70dc630983fcf85b91898ab4912f75d885e27ea2be987f1456e452dbd8ee  SOURCE.sha256
16a1d0ec3206a0c0a870c7a1395e4bb36e6788c847d30e6be3b445e453a05bd0  input/ORIGIN_Q15_SYSTEM.json
b3f1196f9d69fd060c8acfd21d867c6da1b5447af984bbce6013c5c9a4ec0ba6  input/REDUCTION.json
eabe45db71777edc56f3b3d1717a6fd4f3f3c71c44fdf318d71a9babe3447a57  output/compiled/DEDUP.json
```

The exact deduplication retained 5 q-compatibility, 1 G13, 5 G14, and
5 G15 receiver classes.  With the open equation the full system has 17
generators.  Every discarded receiver was checked as an exact nonzero
rational multiple of its retained representative.  The G15-only 11-generator
system is only a diagnostic subideal; its timeout has no implication for the
full ideal.

## AWS executions

| Variant | AWS host / instance | Modular input | Result | Wall time | Max RSS | Swap |
|---|---|---|---|---:|---:|---:|
| G15 core/endpoint/receiver block, Singular `std` | r6c / `i-040b7a1c2ed72d4cc` | p=65497, 40 variables, 11 generators | rc 124, no marker | 30:01.21 | 38,131,544 KiB | 0 |
| Full core/endpoint/receiver block, Singular `slimgb` | r6b / `i-0f089e64c378f5da3` | p=65521, 41 variables, 17 generators | rc 124, no marker | 30:00.20 | 5,854,376 KiB | 0 |
| Full reversed lexical variables, Singular `slimgb` | r6a / `i-02cb2b4a379ffcc64` | p=65519, 41 variables, 17 generators | rc 124, no marker | 30:00.35 | 10,344,584 KiB | 0 |
| Full endpoint ideal, one-thread `msolve` DRL | r6d / `i-07eeaf8ba6f0bc419` | p=65497, 41 variables, 18 equations | rc 124, no marker | 30:00.47 | 12,429,692 KiB | 0 |

Each job passed the Linux, Amazon EC2 DMI, pinned instance/hostname, immutable
job-tag, source/preregistration, memory, disk, idle-host, one-core,
zero-swap, process-group, and final no-orphan checks.  The four solver forms
are genuinely distinct in receiver subset, variable/block ordering,
algorithm, prime, or backend; nevertheless none produced a mathematical
signal within this cap.

After archive fetch and conflict audits found no remaining solver or unrelated
job, the four paid r6i instances were changed from `running` to `stopping`.
The active Box03 symbolic, symbolic-screen, and rankdrop namespaces were not
altered.

## Archive custody

```text
f49bd65aad408424b65320262b8b52d632eac24bba36ebc291c586572c4cac52  archives/ggv_origin_singular_g15_core_block_std_p65497_r1_20260828T112400Z_r6c.tar.gz
e9dd00384a8d0ead5b22f2b08740e480c30c70d2ddf0e48c935c195aba58846f  archives/ggv_origin_singular_full_core_block_slimgb_p65521_r1_20260828T112400Z_r6b.tar.gz
da1ccf3dad0c32916cc25b47f107844efd7f985005e96f0bda5e60d2291e9830  archives/ggv_origin_singular_full_reverse_dp_slimgb_p65519_r1_20260828T113000Z_r6a.tar.gz
2220f4a652136ab3e7843350012b2d9531ffb20dc0609795678717d7823c027c  archives/ggv_origin_msolve_full_endpoint_p65497_r1_20260828T113000Z_r6d.tar.gz
```

The tar member audit rejected absolute and parent-traversal names before local
extraction.  Local SHA-256 replay matches every solver/source/output member in
each remote `EVIDENCE.sha256`.  The sole mismatch in each archive is
`records/client_launcher.stdout`: the worker froze its evidence while that
outer-launcher file was still empty, after which the launcher appended only
`JOB_DIR`, `JOB_TYPE`, `WORKER_PID`, `WORKER_RC`, `MONITOR_RC`, and
`TERMINAL`.  The post-finalization bytes and their hashes are retained in the
archives and in `LOCAL_CUSTODY.sha256`; no mathematical output differs.

## Scope firewall and next action

- A timeout or absent modular marker is not mathematical evidence.
- No branch-P survivor, exact-Q certificate, endpoint syzygy, ideal unit, or
  field-emptiness certificate was produced.
- Do not rerun these same four order/backend/prime combinations serially.
- The separately running Box03 rankdrop lane must be harvested and classified
  before selecting a further bounded, non-equivalent portfolio.  Any modular
  signal must be followed by a separately frozen exact-Q replay.
- No canonical ledger, `jc2-lean`, HENS namespace, or unrelated AWS process
  was read or mutated by this freeze.
