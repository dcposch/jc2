# TRIPLE02 node-1 closed-successor resume R2 (source packet)

Custody-repair successor to the reviewed R1 packet
(`.../triple02_closed_successor_resume_r1_20260829`, hostile review verdict
`REPAIR_REQUIRED`).  The mathematical recursion is byte-for-byte the R1
recursion (same frozen r5 builders, same repaired saturation/chart
templates, same generated-script hashes); R2 repairs the custody stack:
content-addressed decision record and archive-only late authority (C1),
one-job binding and classifier regeneration of every dynamic stage (C2),
systemd-only success with independent RuntimeMaxSec/KillMode=control-group
and a NO_VERDICT-only PGID fallback (C3), schema-checked nonce, atomic
lease, no-replace publication, directory-exact archive verification,
launcher self-binding, exact frozen-archive censuses (454=391+63 and
574=490+84), and the archived-standard-basis triple-copy comparison law.
See `PREREGISTRATION.md` (mathematics) and `AWS_PREREGISTRATION.md`
(custody + mandatory rehearsal plan).

**Status: `SOURCE_READY_AWS_NOT_AUTHORIZED`.**  The only next action this
packet licenses is a hostile source review by a different model.  No AWS
launch.

## Contents

- `prepare_resume.py` — dual frozen-archive validation with exact member
  censuses and selective safe extraction (node-1 open-route products are
  never extracted).
- `build_resume.py` — pinned r5 import, byte-identical reconstruction of the
  archived node-1 `reduce.sing`/`rank_size_6.sing`, witness-replay script and
  node-2 reduce script generation, `RESUME_NODE_INPUT.json` (byte-identical
  to R1).
- `resume_recursor.py` — the resumed recursion driver (nodes 2..7) with the
  repaired stage templates, route guards, full job binding of every stage,
  and the triple-copy witness standard-basis comparison.
- `classify_resume.py` — independent fail-closed classifier: regenerates and
  byte-compares every dynamic script, verifies every stage identity/result
  binding, closes exact artifact sets, and re-derives bounded no-verdicts
  from stage evidence.
- `run_singular_stage.py` — one-job-bound stage runner (no nested sessions;
  binary/source/lease/identity verification before every launch).
- `containment_contract.py` — lease, decision record, late fresh-extraction
  authority, complete file+directory terminal manifest, no-replace
  publication, terminal decision gates.
- `containment_selfcheck.py`, `generator_selfcheck.py` — no-CAS hostile
  fixture suites (pure/parser-level; live behavior is rehearsal debt).
- `adapter_selfcheck.sing`, `diagnostic_hostile.sing` — Singular-side
  controls (byte-identical to R1).
- `aws_job_worker.sh`, `aws_supervisor.sh`, `aws_launch_preflight.sh` —
  worker/supervisor/launcher.
- `runtime_expectations.env`, `EXPECTED_GENERATED_SCRIPTS.sha256`,
  `SOURCE_MANIFEST.sha256`, `SOURCE_ARCHIVE.sha256`,
  `LAUNCH_MANIFEST.sha256` — pins.
- `preflight/` — local (macOS, no-CAS) dry-run evidence.
- `custody/ggv_triple02_closed_successor_resume_r2_SOURCE.tar.gz` — the
  frozen source archive (23 file-only members, mode 0444).

## Expected source archive

`custody/ggv_triple02_closed_successor_resume_r2_SOURCE.tar.gz`, whose
SHA-256 is recorded in `SOURCE_ARCHIVE.sha256` and pinned inside
`aws_launch_preflight.sh` (both outside the archive to avoid
self-reference).  The archive contains exactly, under `jc2/`: every file
listed in `SOURCE_MANIFEST.sha256` plus that manifest itself, i.e. the
18 packet files inside this case directory plus the four frozen
dependencies (r5 `recurse_component.py` + `transcript_gate.py` and the two
terminal archives).

```
cd /path/to/jc2 && shasum -a 256 -c \
  cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r2_20260829/SOURCE_ARCHIVE.sha256
```

## Launch shape (after review + rehearsal + GO only)

```
SOURCE_ARCHIVE=.../ggv_triple02_closed_successor_resume_r2_SOURCE.tar.gz \
LAUNCH_MANIFEST=.../LAUNCH_MANIFEST.sha256 \
JOB_ROOT=/home/ubuntu/jobs/$JOB_TAG \
JOB_STAMP=<UTC YYYYMMDDTHHMMSSZ> JOB_NONCE=<[a-z0-9]{8,32}> \
JOB_TAG=ggv_triple02_closed_successor_resume_r2_${JOB_STAMP}_${JOB_NONCE} \
CPU_ID=<core> EXPECTED_INSTANCE_ID=<i-...> EXPECTED_HOSTNAME=<host> \
bash aws_launch_preflight.sh
```

The supervisor publishes exactly one three-line terminal in
`TERMINAL.marker` (classification, terminal-archive SHA-256,
decision-record SHA-256) via a no-replace hard link, next to the terminal
archive `$JOB_TAG.terminal.tar.gz`.
