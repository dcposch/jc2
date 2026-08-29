# TRIPLE02 node-1 closed-successor resume R1 (source packet)

Source-only, fail-closed resume packet for the TRIPLE02 closed successor
`V(I_node1 + (Delta_node1))`, continuing the frozen r5 finite chart recursion
at global node 2 with inherited rank upper bound 6.  See
`PREREGISTRATION.md` (mathematics) and `AWS_PREREGISTRATION.md` (custody).

**No AWS launch is authorized.**  A hostile source review by a different
model must pass, and a coordinator `GO` must be issued, before any launch.

## Contents

- `prepare_resume.py` — dual frozen-archive validation and selective safe
  extraction (R3 terminal archive + reviewed proper-open R5 terminal archive
  as routing provenance; node-1 open-route products are never extracted).
- `build_resume.py` — pinned r5 import, byte-identical reconstruction of the
  archived node-1 `reduce.sing`/`rank_size_6.sing`, witness-replay script and
  node-2 reduce script generation, `RESUME_NODE_INPUT.json`.
- `resume_recursor.py` — the resumed recursion driver (nodes 2..7) with the
  repaired saturation/chart stage templates and route guards.
- `classify_resume.py` — independent fail-closed classifier.
- `run_singular_stage.py`, `containment_contract.py`,
  `containment_selfcheck.py` — containment stack (no nested sessions; exact
  PID/starttime custody; complete terminal manifest + archive replay).
- `generator_selfcheck.py` — no-CAS hostile mutation suite.
- `adapter_selfcheck.sing`, `diagnostic_hostile.sing` — Singular-side
  controls.
- `aws_job_worker.sh`, `aws_supervisor.sh`, `aws_launch_preflight.sh` —
  worker/supervisor/launcher.
- `runtime_expectations.env`, `EXPECTED_GENERATED_SCRIPTS.sha256`,
  `SOURCE_MANIFEST.sha256`, `SOURCE_ARCHIVE.sha256`,
  `LAUNCH_MANIFEST.sha256` — pins.
- `preflight/` — local (macOS, no-CAS) dry-run evidence: prepared inputs,
  generated scripts, selfcheck stdout, and hashes.
- `custody/ggv_triple02_closed_successor_resume_r1_SOURCE.tar.gz` — the
  frozen source archive (mode 0444).

## Expected source archive

`custody/ggv_triple02_closed_successor_resume_r1_SOURCE.tar.gz`, whose
SHA-256 is recorded in `SOURCE_ARCHIVE.sha256` and pinned inside
`aws_launch_preflight.sh` (both outside the archive to avoid
self-reference).  The archive contains exactly, under `jc2/`:

- every file listed in `SOURCE_MANIFEST.sha256` plus that manifest itself
  (all inside this case directory);
- `cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r5_20260828/{recurse_component.py,transcript_gate.py}`;
- `cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r3_20260828/custody/terminals/ggv_endpoint_complement_triple02_r3_20260828T175423Z_i0f089.terminal.tar.gz`;
- `cases/ggv_8_28_upper_endpoint_triple02_proper_open_resume_r1_20260828/custody/terminals/ggv_triple02_proper_open_resume_r5_20260828T233745Z_r6d.terminal.tar.gz`.

To rebuild and verify the archive hash from a clean checkout:

```
cd /path/to/jc2 && shasum -a 256 -c \
  cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r1_20260829/SOURCE_ARCHIVE.sha256
```

## Launch shape (after review + GO only)

```
SOURCE_ARCHIVE=.../ggv_triple02_closed_successor_resume_r1_SOURCE.tar.gz \
JOB_ROOT=/home/ubuntu/jobs/$JOB_TAG JOB_TAG=ggv_triple02_closed_successor_resume_r1_<UTC>_<nonce> \
CPU_ID=<core> EXPECTED_INSTANCE_ID=<i-...> EXPECTED_HOSTNAME=<host> \
bash aws_launch_preflight.sh
```

The supervisor publishes exactly one terminal in `TERMINAL.marker` and the
terminal archive `$JOB_TAG.terminal.tar.gz` next to it.
