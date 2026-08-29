# Frozen split/resume preregistration V2

Frozen at `2026-08-28T10:35:35Z`. V1 is rejected solely for a packaging
adapter failure: macOS provenance pax metadata materialized as six unpinned
AppleDouble names on Linux. The lambda=0 validator stopped before JSON parsing
or reduction; lambda=1 was stopped through its exact registered PGID while
compiling. V1 produced no accepted mathematical output or verdict.

V2 rebuilds the archive with `COPYFILE_DISABLE=1`, requires an exact 30-file
archive and extracted-source census before launch, and otherwise leaves every
mathematical source/input byte unchanged. The full cause and predecessor
custody are frozen in `SOURCE_ORIGIN.json`.

## Immutable inputs and programs

- The recovered `lambda_0_full_qgates/Q_GATE_SYSTEM.json` is 58,975,191 bytes,
  SHA-256 `7c4beff1ec5b6e64fafcf800d965e2ea614bcd5d53d14195551f5322f418ab78`.
  All six expected input sizes/hashes are pinned in `SOURCE_ORIGIN.json`.
- Validator SHA-256 is
  `54af9aac42385524951fd5228502fbb55dd64ad0436ebfc8a6091b5edd546c16`.
  It must replay exact bytes, canonical JSON, all 263 equation hashes, source
  pins, and byte-for-byte regeneration of five Singular scripts before
  lambda=0 reduction.
- Lambda=1-only compiler SHA-256 is
  `624dbdde607891769c0b692b6cdfc7f8b6c4b967568155186e1c6a3572dae396`.
  Frozen upstream compiler SHA-256 is
  `b487d8b532d303421386c66638a6d7953aa5a4dcf74208cd07c6db885c511201`.
  Lambda=1 is compiled directly; lambda=0 is never recompiled.
- Exact reducer SHA-256 is
  `47d644bf803dfc2c3e65b57110aca8e4ae32a878794b9def6787adf21f4128b6`.
- `SOURCE.sha256` pins every one of the 29 payload files other than itself;
  the archive listing must contain exactly those 29 plus `SOURCE.sha256`.

## Separate V2 jobs

1. `resume_lambda0` on audited r6a (`ip-172-30-0-34`, Amazon EC2
   `r6i.16xlarge`, instance `i-02cb2b4a379ffcc64`) at
   `/home/ubuntu/jobs/ggv_q1_fixed_split_lambda0_resume_r2_20260828T103535Z_r6a`.
2. `compile_lambda1` independently on audited r6d (`ip-172-30-0-45`, Amazon
   EC2 `r6i.16xlarge`, instance `i-07eeaf8ba6f0bc419`) at
   `/home/ubuntu/jobs/ggv_q1_fixed_split_lambda1_compile_r2_20260828T103535Z_r6d`.

Each has a separate 7,200-second hard master cap, one pinned CPU, 64 GiB
address-space cap, 16 GiB file cap, fresh PGID/SID registry, 10-second monitor,
no-orphan cleanup, Linux/Amazon EC2/job-tag/host/instance checks, at least
450 GiB available-memory gate, and zero-swap gates before and after every
stage. Any active-job conflict or extracted-source census disagreement refuses
the launch.

Exact entry points:

```text
aws_run_remote.sh /home/ubuntu/jobs/ggv_q1_fixed_split_lambda0_resume_r2_20260828T103535Z_r6a resume_lambda0
aws_run_remote.sh /home/ubuntu/jobs/ggv_q1_fixed_split_lambda1_compile_r2_20260828T103535Z_r6d compile_lambda1
```

## Frozen classifications and scope

- Exact rational constant compatibility is
  `EXACT_Q_TRIANGULAR_CONSTANT_OBSTRUCTION`.
- Three modular units followed by exact tracked `UNIT=1`,
  `BASIS_REPLAY_ZERO=1`, and `UNIT_REPLAY_ZERO=1` is
  `EXACT_Q_UNIT_REDUCED_WITH_REPLAY`.
- Every disagreement, timeout, resource event, modular nonunit, or incomplete
  exact replay is `NO_VERDICT`. A modular nonunit is not a survivor.

These are necessary q1..q13 de Rham gate systems, not raw D0..D22 endpoint
systems. Exact emptiness can exclude a literal fixed slice; nonempty or
unfinished output supplies neither a raw endpoint survivor nor existence.
Lambda=1 remains diagnostic; no nonzero-lambda normalization or raw-window
shear is claimed. The jobs do not touch live HENS-CT or arbitrary-Q origin
namespaces, top-level canonical files, peer ideation, or `jc2-lean`.
