# TRIPLE02 node-1 closed-successor resume R4 (source packet)

Atomic-archive-authentication successor to the reviewed R3 packet
(`.../triple02_closed_successor_resume_r3_20260829`, hostile review verdict
`PASS_SOURCE_FOR_DISPOSABLE_REHEARSAL` with blocking-before-pilot finding
`O2-B1`).  The mathematical recursion is byte-for-byte the R1/R2/R3
recursion (same frozen r5 builders, same repaired saturation/chart
templates, same generated-script hashes, same rank census, same
terminal allowlist); R4 repairs only custody:

- **O2-B1 (blocking)**: the charged terminal archive is now opened
  **exactly once**.  The late authority opens the archive path a single
  time with `O_NOFOLLOW`/`O_NONBLOCK`, requires a regular file via `fstat`
  on the descriptor, streams the outer SHA-256 from that descriptor,
  rewinds, and hands the **same open object** to `tarfile`; the extraction
  walk and every member/manifest/directory census and retained-member read
  run while that descriptor is held.  No archive-path reopen exists on the
  decision path, so a concurrent same-uid `rename()`/replacement of the
  path cannot redirect any decision read (the R3 review's 6/6 promoted
  race).  In-place mutation/truncation of the inode during the read is
  refused by a pre/post `fstat` identity/size/mtime/ctime stability gate.
  The published marker's `TERMINAL_ARCHIVE_SHA256` is the digest actually
  computed from that descriptor, never merely the CLI string.
- **O2-N2**: archived fault-latch values are type-checked; JSON booleans
  (and any non-int) are refused for `worker_rc` and the six sticky faults.
- **O2-N4**: the terminal CLI always publishes the custody no-verdict
  marker on a malformed late `--archive-sha256` instead of dying markerless.
- **O2-N1 (prose)**: the previously untested `swap_zero` gate is now
  exercised; `decide_terminal` has 19 load-bearing gates.

All R3 custody repairs are retained unchanged (hostile-review findings
O-B1 archive-bytes late authority; O-N1 exact single-line append law; O-N2
runner-log content law; O-N3 five-property runtime read-back; O-N4
in-archive fault latches; O-N5 report-free launch manifest; O-N6 identity
key census; O-N7 divisor `identical_copies`; O-N8v job-tag stamp schema).

See `PREREGISTRATION.md` (mathematics) and `AWS_PREREGISTRATION.md`
(custody + mandatory rehearsal plan, now including the R3 review's O2-B1
regression as a mandatory live-instance step).

**Status: `SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`.**  The only next
action this packet licenses is a hostile source review by a different
model.  No AWS launch; R4 does not authorize a pilot, a mathematical run,
or even a disposable rehearsal — those remain gated on a passing review
and a separate coordinator `GO`.

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
- `containment_contract.py` — lease, decision record, single-open
  frozen-archive-bytes late authority (`open_frozen_archive` +
  `require_stable_archive_stat`), complete file+directory terminal
  manifest, five-property runtime-limit record, fault-latch custody
  (integer-typed), no-replace publication, terminal decision gates.
- `containment_selfcheck.py`, `generator_selfcheck.py` — no-CAS hostile
  fixture suites (pure/parser-level; live behavior is rehearsal debt),
  including the R2 review's working O-B1 forgery and the R3 review's
  genuine concurrent-rename O2-B1 exploit as mandatory refusing controls.
- `adapter_selfcheck.sing`, `diagnostic_hostile.sing` — Singular-side
  controls (byte-identical to R1/R2).
- `aws_job_worker.sh`, `aws_supervisor.sh`, `aws_launch_preflight.sh` —
  worker/supervisor/launcher.
- `runtime_expectations.env`, `EXPECTED_GENERATED_SCRIPTS.sha256`,
  `SOURCE_MANIFEST.sha256`, `SOURCE_ARCHIVE.sha256`,
  `LAUNCH_MANIFEST.sha256`, `REPORT_BINDING.sha256` — pins.
- `preflight/` — local (macOS, no-CAS) dry-run evidence.
- `custody/ggv_triple02_closed_successor_resume_r4_SOURCE.tar.gz` — the
  frozen source archive (23 file-only members; the archive FILE is
  installed mode 0444; member modes are the inherited originals and every
  extraction is hash-verified).

## Expected source archive

`custody/ggv_triple02_closed_successor_resume_r4_SOURCE.tar.gz`, whose
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
  cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r4_20260829/SOURCE_ARCHIVE.sha256
```

## Launch shape (after review + rehearsal + GO only)

```
SOURCE_ARCHIVE=.../ggv_triple02_closed_successor_resume_r4_SOURCE.tar.gz \
LAUNCH_MANIFEST=.../LAUNCH_MANIFEST.sha256 \
JOB_ROOT=/home/ubuntu/jobs/$JOB_TAG \
JOB_STAMP=<UTC YYYYMMDDTHHMMSSZ> JOB_NONCE=<[a-z0-9]{8,32}> \
JOB_TAG=ggv_triple02_closed_successor_resume_r4_${JOB_STAMP}_${JOB_NONCE} \
CPU_ID=<core> EXPECTED_INSTANCE_ID=<i-...> EXPECTED_HOSTNAME=<host> \
bash aws_launch_preflight.sh
```

The supervisor publishes exactly one three-line terminal in
`TERMINAL.marker` (classification, terminal-archive SHA-256,
decision-record SHA-256) via a no-replace hard link, next to the terminal
archive `$JOB_TAG.terminal.tar.gz`.  A mathematical line can appear only
if the late authority has re-authenticated that exact archive's bytes
against the charged digest at decision time.
