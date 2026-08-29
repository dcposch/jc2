# Frozen lambda=0 emitted-packet resume preregistration V3

Frozen at `2026-08-28T10:39:42Z`. This is a lambda=0-only adapter repair.
It does not recompile any q-gate equation and does not alter the independent,
healthy lambda=1 V2 job.

V1 rejected unpinned AppleDouble names before reduction. V2 used a clean
30-file archive and replayed the exact six-file census, all six byte hashes,
canonical JSON, and all 263 embedded equation hashes; it then fail-closed
because the validator compared a historical provenance path to the relocated
successor path. Both failures are adapter/custody failures, not algebraic
results. Exact details are in `SOURCE_ORIGIN.json`.

V3 preserves the recovered JSON byte-for-byte, including its original path
`cases/ggv_8_28_upper_endpoint_q1_fixed_a_full_raw_20260828/compile_fixed_q1_raw.py`
and digest `82284eff...`. It pins that historical path/digest map exactly and
separately hashes the byte-identical executable copy in this successor. No
provenance field is rewritten.

## Frozen target and procedure

- Input system: 58,975,191 bytes, SHA-256
  `7c4beff1ec5b6e64fafcf800d965e2ea614bcd5d53d14195551f5322f418ab78`.
- Upstream compiler SHA-256:
  `b487d8b532d303421386c66638a6d7953aa5a4dcf74208cd07c6db885c511201`.
- Exact reducer SHA-256:
  `47d644bf803dfc2c3e65b57110aca8e4ae32a878794b9def6787adf21f4128b6`.
- The new validator hash is frozen by `SOURCE.sha256`. It must replay exact
  input bytes, canonical JSON, 263 equation hashes, the original provenance
  map, all live source hashes, and five regenerated Singular scripts before
  invoking the unchanged reducer.

Run only on audited r6a (`ip-172-30-0-34`, Amazon EC2 `r6i.16xlarge`,
instance `i-02cb2b4a379ffcc64`) in fresh namespace
`/home/ubuntu/jobs/ggv_q1_fixed_lambda0_resume_r3_20260828T103942Z_r6a`.
The exact entry point is:

```text
aws_run_remote.sh /home/ubuntu/jobs/ggv_q1_fixed_lambda0_resume_r3_20260828T103942Z_r6a resume_lambda0
```

The job has a 7,200-second hard cap, one pinned CPU, 64 GiB address-space cap,
16 GiB file cap, fresh PGID/SID registry, no-orphan cleanup, 10-second monitor,
Linux/Amazon EC2/job-tag/host/instance checks, at least 450 GiB available
memory, exact 30-file archive/extraction census, and zero-swap gates.

Exact rational constant compatibility is
`EXACT_Q_TRIANGULAR_CONSTANT_OBSTRUCTION`. Three modular units followed by
tracked exact `UNIT=1`, `BASIS_REPLAY_ZERO=1`, and `UNIT_REPLAY_ZERO=1` is
`EXACT_Q_UNIT_REDUCED_WITH_REPLAY`. Every disagreement, timeout, modular
nonunit, or incomplete exact replay remains `NO_VERDICT`; nonunit is not a
survivor. This necessary q1..q13 gate screen is not a raw endpoint system.

No live HENS-CT, arbitrary-Q origin, or lambda=1 namespace is altered. No
top-level canonical file, peer ideation submission, or `jc2-lean` content is
touched.
