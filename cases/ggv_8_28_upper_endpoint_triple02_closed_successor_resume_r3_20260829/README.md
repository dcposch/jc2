# TRIPLE02 node-1 closed-successor resume R3 (source packet)

Custody-repair successor to the reviewed R2 packet
(`.../triple02_closed_successor_resume_r2_20260829`, hostile review verdict
`PASS_FOR_DISPOSABLE_LIVE_LINUX_REHEARSAL` with blocking-before-pilot
finding `O-B1`).  The mathematical recursion is byte-for-byte the R1/R2
recursion (same frozen r5 builders, same repaired saturation/chart
templates, same generated-script hashes); R3 repairs only custody:

- **O-B1 (blocking)**: the late terminal authority now authenticates the
  FROZEN ARCHIVE BYTES — it re-hashes the installed terminal archive
  against the charged digest, re-runs the complete member/manifest/
  directory censuses from the archive bytes, requires the fresh extraction
  to be byte-identical member-for-member (edit, deletion, replacement,
  symlink, and archive/extraction mix-and-match all fail closed), and reads
  every decision input from the archive bytes in memory.  The review's
  working forgery is a mandatory refusing fixture.
- **O-N1**: exact node standard-basis census (single-line append law; a
  doubled file is refused; the EXACT_EMPTY_NODE census is non-vacuous).
- **O-N2**: runner-log content is bound (stdout must be exactly the three
  SINGULAR_STAGE_* lines consistent with the verified result record;
  stderr must be empty).
- **O-N3**: the systemd read-back verifies all five charged properties by
  exact value, including RuntimeMaxUSec exactly 21600 s.
- **O-N4**: sticky fault latches are banked inside the archive before the
  freeze and the late authority refuses fault regressions; the post-freeze
  latch file binds the archive digest and carries a hash sidecar.
- **O-N5**: `LAUNCH_MANIFEST.sha256` no longer lists the producer report,
  so its hash is fully tabled in the R3 report and chargeable; the report
  hash lives in the post-report `REPORT_BINDING.sha256`.
- **O-N6**: exact identity-record key census in driver and classifier.
- **O-N7**: divisor-only `identical_copies` (same behavior, O(sqrt n)).
- **O-N8v**: the job-tag stamp shape is enforced by the contract itself.

See `PREREGISTRATION.md` (mathematics) and `AWS_PREREGISTRATION.md`
(custody + mandatory rehearsal plan, extended with the R2 review's four
rehearsal items).

**Status: `SOURCE_READY_AWS_NOT_AUTHORIZED`.**  The only next action this
packet licenses is a hostile source review by a different model.  No AWS
launch, and R3 itself does not authorize even a disposable rehearsal.

## Contents

- `prepare_resume.py` — dual frozen-archive validation with exact member
  censuses and selective safe extraction (byte-identical to R2).
- `build_resume.py` — pinned r5 import, byte-identical reconstruction of the
  archived node-1 `reduce.sing`/`rank_size_6.sing`, witness-replay script and
  node-2 reduce script generation, `RESUME_NODE_INPUT.json` (byte-identical
  to R1/R2).
- `resume_recursor.py` — the resumed recursion driver (nodes 2..7) with the
  repaired stage templates, route guards, full job binding of every stage,
  the triple-copy witness standard-basis comparison, and the R3 runner-log/
  identity-census/single-line-append laws.
- `classify_resume.py` — independent fail-closed classifier: regenerates and
  byte-compares every dynamic script, verifies every stage identity/result
  binding (exact key censuses), binds runner-log bytes, closes exact
  artifact sets, applies the exact node-SB append law, and re-derives
  bounded no-verdicts from stage evidence.
- `run_singular_stage.py` — one-job-bound stage runner (byte-identical to
  R2; no nested sessions; binary/source/lease/identity verification before
  every launch).
- `containment_contract.py` — lease, decision record, frozen-archive-bytes
  late authority, complete file+directory terminal manifest, five-property
  runtime-limit record, fault-latch custody, no-replace publication,
  terminal decision gates.
- `containment_selfcheck.py`, `generator_selfcheck.py` — no-CAS hostile
  fixture suites (pure/parser-level; live behavior is rehearsal debt),
  including the R2 review's working O-B1 forgery as a mandatory refusing
  control.
- `adapter_selfcheck.sing`, `diagnostic_hostile.sing` — Singular-side
  controls (byte-identical to R1/R2).
- `aws_job_worker.sh`, `aws_supervisor.sh`, `aws_launch_preflight.sh` —
  worker/supervisor/launcher.
- `runtime_expectations.env`, `EXPECTED_GENERATED_SCRIPTS.sha256`,
  `SOURCE_MANIFEST.sha256`, `SOURCE_ARCHIVE.sha256`,
  `LAUNCH_MANIFEST.sha256`, `REPORT_BINDING.sha256` — pins.
- `preflight/` — local (macOS, no-CAS) dry-run evidence.
- `custody/ggv_triple02_closed_successor_resume_r3_SOURCE.tar.gz` — the
  frozen source archive (23 file-only members; the archive FILE is
  installed mode 0444; member modes are the inherited originals and every
  extraction is hash-verified).

## Expected source archive

`custody/ggv_triple02_closed_successor_resume_r3_SOURCE.tar.gz`, whose
SHA-256 is recorded in `SOURCE_ARCHIVE.sha256` and pinned inside
`aws_launch_preflight.sh` (both outside the archive to avoid
self-reference).  The archive contains exactly, under `jc2/`: every file
listed in `SOURCE_MANIFEST.sha256` plus that manifest itself.  The 22
manifest entries are the 18 in-case files (all packet files except
`aws_launch_preflight.sh`, `SOURCE_MANIFEST.sha256` itself,
`SOURCE_ARCHIVE.sha256`, `PREFLIGHT_REPORT.md`, `LAUNCH_MANIFEST.sha256`,
`REPORT_BINDING.sha256`, and the archive) plus the four frozen
dependencies (r5 `recurse_component.py` + `transcript_gate.py` and the two
terminal archives).

```
cd /path/to/jc2 && shasum -a 256 -c \
  cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r3_20260829/SOURCE_ARCHIVE.sha256
```

## Launch shape (after review + rehearsal + GO only)

```
SOURCE_ARCHIVE=.../ggv_triple02_closed_successor_resume_r3_SOURCE.tar.gz \
LAUNCH_MANIFEST=.../LAUNCH_MANIFEST.sha256 \
JOB_ROOT=/home/ubuntu/jobs/$JOB_TAG \
JOB_STAMP=<UTC YYYYMMDDTHHMMSSZ> JOB_NONCE=<[a-z0-9]{8,32}> \
JOB_TAG=ggv_triple02_closed_successor_resume_r3_${JOB_STAMP}_${JOB_NONCE} \
CPU_ID=<core> EXPECTED_INSTANCE_ID=<i-...> EXPECTED_HOSTNAME=<host> \
bash aws_launch_preflight.sh
```

The supervisor publishes exactly one three-line terminal in
`TERMINAL.marker` (classification, terminal-archive SHA-256,
decision-record SHA-256) via a no-replace hard link, next to the terminal
archive `$JOB_TAG.terminal.tar.gz`.  A mathematical line can appear only
if the late authority has re-authenticated that exact archive's bytes
against the charged digest at decision time.
