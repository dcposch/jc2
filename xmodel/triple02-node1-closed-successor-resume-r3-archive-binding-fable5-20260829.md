# TRIPLE02 node-1 closed-successor resume R3 — archive-binding producer report

Author: Fable 5 (source producer, not reviewer; same model as the R2
producer).  Date: 2026-08-28 (packet dated 20260829).  Working directory:
`/Users/dc/code/math/jc2`.

Deliverable: the fresh directory
`cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r3_20260829/`
and this report.  R2 was treated as immutable: every R2 packet file was
re-hashed this session and matches the R2 report's §5 table and the
hostile review's §1 table byte-for-byte (including
`LAUNCH_MANIFEST.sha256 = ba697115...dc34`), and neither the R2 packet nor
the R2 report was modified.  Nothing was launched, no CAS was run, no
canonical file was edited, nothing was committed, `jc2-lean` was not
accessed, no repository-wide command was run, and no web/AWS operation was
performed.  Bounded scratch replays ran under `/tmp/triple02-r3-preflight`.

## Verdict

**`SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`**

The only next action licensed by this report is a hostile source review of
this R3 packet by a different model.  R3 itself does not authorize an AWS
launch, a pilot, or even a disposable rehearsal; after a passing review,
the disposable-instance rehearsal in `AWS_PREREGISTRATION.md` (now
including the reviewer's four added items) and a separate coordinator `GO`
remain mandatory.

## 1. Charge

This packet repairs the blocking O-B1 finding and the directly adjacent
custody findings of the hostile source review of R2:

- R2 producer report
  `xmodel/triple02-node1-closed-successor-resume-r2-repair-fable5-20260829.md`,
  full SHA-256
  `c6322ccf5e25c27575c8b0f3e1b8f7b37a5a8add70d2687e9dcf4feb41dc8757`,
  body hash
  `fbefb5011f91274f00ebe75b472b12cf1422da7f487d66b858f37aac678dd6c0`
  (both re-verified this session);
- hostile review
  `xmodel/triple02-node1-closed-successor-resume-r2-hostile-review-opus5-20260829.md`
  (Opus 5), full SHA-256
  `e524ba78a0ebe3468259f85fec148494b5ec6c4f160941333f67013b1dfb518e`,
  body hash
  `c4f90652eb665dad8b396150704340a12a9bef746e67d17cc5fe83ecab5b451d`
  (both computed this session; verdict
  `PASS_FOR_DISPOSABLE_LIVE_LINUX_REHEARSAL`, blocking-before-pilot
  finding `O-B1`, nonblocking findings `O-N1`–`O-N8`),

while keeping the R1/R2 mathematical recursion byte-for-byte fixed.  All
seven frozen dependencies were re-verified byte-exact this session: the R1
report (`93b89430...ccca9`), the R1 review (`ad25f496...cfafb2`), the R3
terminal archive (`e5bdd2b2...53a1e1`), the proper-open R5 terminal
archive (`4b8ffc1c...cbef7e`), the frozen r5 recursor
(`d679a4d7...b2cd90`), the frozen transcript gate (`0e0efd5a...97e316`),
and the R2 source archive (`183ab5e0...65987`).

## 2. The O-B1 repair: the late authority authenticates the frozen archive bytes

R2's `derive_late_decision` read every decision input from the fresh
extraction directory — a plain writable directory inside `$JOB_ROOT` —
and never tied it to the archive or re-verified the manifest at read
time.  The review demonstrated a working promotion of a bounded
no-verdict to the dead string by rewriting the extraction and re-running
`decision-build` over it.

R3 restructures the late authority (`containment_contract.py`):

1. **The archive bytes are the decision source.**
   `derive_late_decision` now takes the installed terminal archive path,
   the charged archive digest, and the manifest parameters
   (`--terminal-archive`, `--archive-sha256`, `--manifest-relative`,
   `--include ...`, `--dirs-relative`, passed by the supervisor from the
   freeze variables).  Its first act, before reading any classifier input
   or record, is `authenticate_frozen_archive`, which (a) requires the
   archive path to be a regular non-symlink file whose SHA-256 equals the
   charged digest; (b) re-runs the complete member-safety census from the
   archive bytes (safe names, allowed include prefixes, no duplicates,
   file/dir members only); (c) walks the fresh extraction with
   `followlinks=False`, refusing any symlink or special file anywhere,
   and requires its exact file and directory sets to equal the archive
   member sets; (d) streams every file member once, byte-comparing it
   against the extraction file and hashing it; (e) replays the embedded
   `TERMINAL_MANIFEST.sha256` and `TERMINAL_DIRS.list` censuses and
   per-member hashes from the archive bytes alone; and (f) retains the
   fourteen decision-input members
   (`DECISION_RETAINED_MEMBERS`) in memory.
2. **Nothing later is read from disk inside the extraction.**  The
   decision record, sidecar, containment mode, runtime limits, fault
   latches, lease + sidecar, Singular digest sidecar, both identity
   files, both verdicts, and all five recorded artifact hashes are taken
   from the retained archive bytes / archive member hashes.  Only the two
   intentionally live cross-checks (the live lease file and the live
   containment-mode file) still touch the filesystem outside the
   extraction, exactly as recorded in the decision equalities.
3. **Every attack class in the charge fails closed**, each with a
   refusing fixture executed this session: the review's working forgery
   (rewritten verdicts + summaries + re-run `decision-build` inside the
   extraction) refuses with `DECISION_FRESH_ROOT_BYTES_DRIFT`; a same-uid
   single-file edit refuses (`..._BYTES_DRIFT`); a deletion or extra
   member refuses (`..._CENSUS_DRIFT`); a symlink substitution refuses
   (`DECISION_FRESH_ROOT_SYMLINK`); an archive/extraction mix-and-match
   (clean extraction of a different job's archive) refuses; an archive
   replacement or wrong charged digest refuses
   (`DECISION_ARCHIVE_HASH_DISAGREEMENT`); an archive-path symlink
   refuses (`DECISION_ARCHIVE_NOT_REGULAR_FILE`).  If any late input is
   missing while `archive_ready=1`, the terminal CLI refuses with
   `LATE_DECISION_INPUTS_MISSING` and publishes only a custody
   no-verdict.
4. The published marker is unchanged (three lines), but a mathematical
   first line can now appear only if the decision re-authenticated
   exactly the archive digest on the second line — closing the
   archive/marker disagreement Sol 5.6's C1 named and O-B1 re-opened.

## 3. Adjacent custody findings closed

- **O-N1 — exact node standard-basis census.**  Source semantics warrant
  it: `node_header` writes `string(NODE_SB)`, and the real archived
  4,961-byte unit contains exactly one newline, at its end (verified this
  session and pinned as a selfcheck anchor,
  `ARCHIVED_SB_UNIT_SINGLE_LINE_ANCHOR_PASS`).  The new law
  (`require_single_line_append_stack`, applied by
  `Classifier.verify_node_sb`): the file must split into exactly
  `header_stage_count` identical blocks, each containing exactly one
  newline at its end.  The R2 divisibility acceptance of 6 or 9 copies
  over 3 stages is gone (a doubled file's per-stage block carries two
  newlines), and the `EXACT_EMPTY_NODE` single-stage census is no longer
  vacuous.  The witness-replay law `archived == produced * 3` is
  unchanged (already exact).  The timed-out-node skip (partial append
  undecidable) is unchanged and documented.
- **O-N2 — runner-log content bound.**  New `expected_runner_stdout` /
  `require_runner_logs` in `resume_recursor.py`, enforced by BOTH the
  driver (`run_stage`, including timed-out stages) and the classifier
  (`check_stage`): the runner's captured stdout must be exactly the three
  `SINGULAR_STAGE_RETURNCODE/TIMED_OUT/ELAPSED_SECONDS` lines derived
  from the verified result record, and its stderr must be empty.  A probe
  confirmed the law matches the runner's three `print` statements
  exactly (including the timed-out shape) and that the float `repr`
  round-trips (`preflight/SCHEMA_AGREEMENT_PROBE.txt`).  The review's
  `FATAL_ANYTHING\nrc=99\n` replacement is a refusing fixture.
- **O-N3 — five-property systemd read-back.**  New contract predicate
  `runtime_limits_verified` + CLI `runtime-limits-record`: KillMode
  `control-group`, MemoryMax `274877906944`, TasksMax `512`,
  MemorySwapMax `0`, and RuntimeMaxUSec **exactly 21600 s** (accepted
  renderings `6h`/`21600s`/`21600000000us`; anything else — including an
  unexpected honest rendering — downgrades, never promotes, and the
  rehearsal captures the live shape).  The supervisor's read-back now
  calls this CLI (its R2 inline three-property heredoc is gone), and
  `derive_late_decision` replays the identical predicate on the archived
  record.  Mutations of RuntimeMaxUSec/MemoryMax/TasksMax that R2's
  derive accepted are refusing fixtures at both layers.
- **O-N4 — latches under authenticated custody.**  The supervisor banks
  `custody/FAULT_LATCHES_PRE_ARCHIVE.json` (schema-checked; job tag,
  nonce, mode, worker_rc, and the six sticky faults) immediately before
  `manifest-build`, so it is inside the reviewed archive; the late
  authority requires it from the archive bytes, requires
  `worker_rc` equality with the live flag, and refuses any fault
  regression (archived 1, live 0) — post-freeze sticky re-checks can
  only worsen the live flags, which already downgrade.  The post-freeze
  `FINALIZATION_LATCHES.txt` now binds the job tag and the charged
  archive digest and carries a `FINALIZATION_LATCHES.sha256` sidecar, so
  an auditor authenticates it through the marker chain (marker → archive
  digest → latches).
- **O-N5 — launch manifest chargeable.**  `LAUNCH_MANIFEST.sha256` no
  longer lists the producer report; it is now fully determined by the
  packet (6 lines: launcher, `SOURCE_ARCHIVE.sha256`, archive,
  `SOURCE_MANIFEST.sha256`, both preregistrations) and its hash
  `10fbc308...dac5` is tabled in §5 below.  The report's own hash lives
  in the post-report `REPORT_BINDING.sha256` (written after this file,
  charged by the reviewer/coordinator exactly as R2's launch manifest
  was).  The launcher's own verification set is unchanged (self hash +
  archive line); its counterpart direction (launcher pins archive,
  launch manifest pins launcher) is preserved with no self-reference.
- **O-N6 — identity-record key census.**  New `IDENTITY_RECORD_KEYS`
  (17 keys) in `resume_recursor.py`, enforced by the driver and the
  classifier; a probe confirmed the runner's emitted identity dict is
  the identical 17-key set.  The review's injected-key fixture is now
  refused directly (`STAGE_IDENTITY_KEY_CENSUS`), not transitively.
- **O-N7 — `identical_copies` divisor iteration.**  Now enumerates
  divisors in O(sqrt n) instead of scanning every count; behavior
  (maximal count, same errors) is unchanged and all R2 decomposition
  fixtures replay.
- **O-N8v — job-tag stamp schema.**  `require_job_tag` itself now
  enforces the exact `YYYYMMDDTHHMMSSZ` stamp
  (`JOB_TAG_STAMP_SCHEMA_FAILURE`), so a direct supervisor entry cannot
  use a malformed stamp; two refusing fixtures added.
- **O-N8 prose corrections adopted here**: the 22 manifest entries are
  the 18 in-case files — all packet files except
  `aws_launch_preflight.sh`, `SOURCE_MANIFEST.sha256` itself,
  `SOURCE_ARCHIVE.sha256`, `PREFLIGHT_REPORT.md`,
  `LAUNCH_MANIFEST.sha256`, `REPORT_BINDING.sha256`, and the archive —
  plus the four frozen dependencies; "mode 0444" is a claim about the
  archive FILE, member modes are the inherited originals (every
  extraction is hash-verified); `decide_terminal` has **19** gate
  parameters (the R2 prose said 18-way); the terminal-CLI collapse of
  `mode/runtime/lease/decision` gates into one derive outcome is
  retained and disclosed (the underlying checks all run inside
  `derive_late_decision`); the classifier's hard-coded
  `START_NODE/MAX_NODES/FINAL_NODE` remain and disagree fail-closed with
  any non-default driver `--max-nodes`.

Nothing on the review's list is silently deferred.  The only obligations
that remain open are inherently live-host items, all named in
`AWS_PREREGISTRATION.md` as mandatory rehearsal steps 8–11 (O-B1
regression on the live extraction, exact systemd read-back capture,
watchdog degradation, runner-log shape capture) plus the pre-existing
seven-point plan; every one of them fails closed at the pilot boundary
because the corresponding gates refuse by default until satisfied.

## 4. What is mathematically unchanged (verified, not asserted)

- `prepare_resume.py`, `build_resume.py`, `run_singular_stage.py`,
  `adapter_selfcheck.sing`, `diagnostic_hostile.sing`, and
  `EXPECTED_GENERATED_SCRIPTS.sha256` are **byte-identical files** to R2
  (same hashes as the reviewed table; see §5).
- In `resume_recursor.py`, an AST comparison of every top-level
  definition and constant against R2 shows the entire frozen set
  byte-identical: `build_repaired_saturation_script`,
  `validate_saturation_script`, `build_repaired_chart_script`,
  `validate_chart_script`, `replace_once`, `require_count_markers`,
  `require_archived_append_copies`, `identical_copies`' contract (see
  O-N7), `Recursor.run`, `Recursor.write_summary`,
  `Recursor.replay_witness`, `JobBinding`, and all mathematical
  constants (`GENERATOR_SHA256`, `DELTA_NODE1_SHA256`,
  `WITNESS_REPLAY_MARKERS`, `ARCHIVED_NODE1_SB_APPEND_COUNT`, ...).
  Exactly two definitions changed (`Recursor.run_stage`,
  `identical_copies`) and four custody symbols were added
  (`IDENTITY_RECORD_KEYS`, `expected_runner_stdout`,
  `require_runner_logs`, `require_single_line_append_stack`).
- The regenerated witness-replay and node-2 reduce scripts reproduce the
  R1/R2 pins exactly:
  `27cb85082e8ea56a4a9bc8d0cb38b889edc4e981529d6697b0ff2800e0159d0d` and
  `d9e79b427dd22718683b2ac3f5f50dbd9839622ee07bf95cb61f02bdd380d8b8`;
  all five build products are byte-identical across two independent
  builds, and the rank-census rebuild reproduces
  `bb8f7ee0...8c51` (formal_slots 97020, structural_zero 95920,
  support_matchable 1100, support_entries 36).
- The four-string terminal allowlist, the three no-reentry firewalls, the
  scope statements, and the three-line marker format are unchanged.
- `PREREGISTRATION.md` changes only its header/status prose and the
  appended-copy-law paragraph (the exact single-line strengthening); the
  objective, starting ideal, recursion contract, terminal
  classifications, and epistemic separations are word-for-word R2.

## 5. Packet contents and hashes

Case dir `cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r3_20260829/`:

| file | SHA-256 |
|---|---|
| `prepare_resume.py` (byte-identical to R2) | `1eb8ed781843fd0efd633722ddd74853266d0e361b6e78a0d7e5ab9e1b302528` |
| `build_resume.py` (byte-identical to R1/R2) | `3763ac7a5ce2915ede7c21c9d9b8dcb3fc1ab12075c998daa646a375b640f780` |
| `resume_recursor.py` | `648d28aa11f4eb2666b4d01654ee73d4069d87c89950598a014ef5ee9c0550f9` |
| `classify_resume.py` | `38677c06b1ac22862e59f0026de815bd86c55177a162c7dcde09125820f829bb` |
| `generator_selfcheck.py` | `a6f32db0e81d9d8089670c69ed9e42f355c1f5d5564a6875ba084617d8ba4d39` |
| `run_singular_stage.py` (byte-identical to R2) | `766bebf02496c2bcdd34c575219b819d4d332f404f286cc49dedab793ffe9564` |
| `containment_contract.py` | `a44d70228a09e522ed8fc00fde010f7696d390e023337aa7e7eb06fd831a3ab1` |
| `containment_selfcheck.py` | `77db3d3966d4ddc70ec6e9b1f8f3dc8e257551266553e640d340f9e68bcf116b` |
| `adapter_selfcheck.sing` (byte-identical to R1/R2) | `e616b59542a977dd9daa6865dbf18b60feaae06f784d98f72cf8cced27ee4490` |
| `diagnostic_hostile.sing` (byte-identical to R1/R2) | `01be817524da040ad97eeb52adc461d6556e2d8cd179c9447c4c5101a2f15e02` |
| `aws_job_worker.sh` | `58f000c9109fd72448a198a17b4f88ab5ac21f9243aed0651205bca0f612ea1d` |
| `aws_supervisor.sh` | `20c806977cf1a55b339b26520ae40e1752ffa427356e19fe15cf8856f8704209` |
| `aws_launch_preflight.sh` | `4d252ddfc232592ca07f5f582427c75d636bfc5e9d2914ed4fcd42dd533bd58e` |
| `runtime_expectations.env` | `d3dfa8b99a67e82ae35b8574f0a2bcb95567540c9c03df5d80ab52d4a4932ec3` |
| `EXPECTED_GENERATED_SCRIPTS.sha256` (byte-identical to R1/R2) | `9912dd2279223347d461b5640583b84283216d4873b56e3be34770314f2b5696` |
| `SOURCE_MANIFEST.sha256` (22 entries) | `85e75a1352362b86d579d3e454d4909fcf7dbb71cc75c2b20c64259095bcfdac` |
| `AWS_PREREGISTRATION.md` | `8147c0b7e1677038d2610f9e69e3df8ec75e87b9545d8b79de49e465d117354c` |
| `PREREGISTRATION.md` | `161c3011e1f3b316f8a7315e3aac732ce80207c027fbc22a63727efde3456b61` |
| `PREREGISTRATION.sha256` | `849828b4e064920bdd80235707fd1b4a7ca4d11c74291980e6b42fd181ad1844` |
| `README.md` | `a680b2bcd5fd1be0dac33b79819d60fafaae9b313f1073144752d38d615bf837` |
| `PREFLIGHT_REPORT.md` | `7b02674c9ec97f58f28e1178b6e1766e0d6bed5c348944d1c6e576b9b3716be3` |
| `SOURCE_ARCHIVE.sha256` | `21b690037aa9f725f44a15868792259d0ee6b08f84cc15d31b9ba99919564049` |
| **`LAUNCH_MANIFEST.sha256`** (6 lines, report-free — the O-N5 repair makes this tabulable) | `10fbc308aefbb2dfbe6c45d987feb27a7e930841aa0c76eb853c8e8a9a87dac5` |
| source archive `custody/ggv_triple02_closed_successor_resume_r3_SOURCE.tar.gz` (23 file-only members; archive file mode 0444) | `2f129c2258a6d512bd8fe873db97c142c436bafdf0d7fee37997e4a3086e0bc1` |

`REPORT_BINDING.sha256` is written immediately after this report (it
lists this report's full-file hash, so it cannot be tabled here); the
reviewer must charge this report's hash independently and may then use
`REPORT_BINDING.sha256` as the coordinator-facing pointer.  The launcher's
literal pins are `expected_archive_sha=2f129c22...0bc1` and the r3 case
path/tag prefix; `LEASE_SCHEMA`/`DECISION_SCHEMA`/`FAULT_LATCH_SCHEMA`
and `JOB_TAG_PREFIX` are bumped to `..._r3_...`, so no R2-era lease,
decision record, or tag can be replayed into an R3 job.  The archive's 22
manifest entries are the 18 in-case files plus the four frozen
dependencies (§3, O-N8 arithmetic); a fresh extraction verified all 22,
and the launch-census replay confirmed 23 file-only members under the
four allowed `jc2/` prefixes.  `preflight/` holds the local evidence
(prepared-inputs census, prepare/build stdouts, both selfcheck stdouts,
the containment fixture JSON, the fail-closed dry-run summary, the
archived-node-1 probe, the schema-agreement probe, the archive-replay
note, and the five build products).

## 6. Local verification (all pass; exact commands and counts)

1. `python3 -m py_compile` and `python3 -O -m py_compile` over all eight
   packet Python files; `bash -n` over the three shell scripts (re-run
   after the launcher's archive-hash fill).
2. `prepare_resume.py` against the real frozen archives (census gates
   454:391:63 and 574:490:84, 294 + 3 extracted files, open-route
   exclusion, archived-timeout and settled-open revalidation);
   `build_resume.py` reproducing both R1/R2 script pins; determinism
   re-run into fresh directories with all five build products
   byte-identical and prepare stdout byte-identical.
3. `generator_selfcheck.py` under `python3` and `python3 -O` (stdout
   byte-identical across interpreters): **45 `expect_rejection` call
   sites → 49 rejection executions** (one 3-way adapter-anchor loop, one
   3-way wrong-cap/binary/source loop) **+ 3 manual refusal controls =
   52 hostile refusals per interpreter**, 46 pass markers (48 stdout
   lines including the two script-hash lines).  New over R2: the five
   O-N1/O-N2/O-N6 classifier fixtures (`RUNNER_STDOUT_TAMPER_REJECTED`,
   `RUNNER_STDERR_TAMPER_REJECTED`, `NODE_SB_DOUBLED_STACK_REJECTED`,
   `NODE_SB_MULTILINE_STACK_REJECTED`, `IDENTITY_INJECTED_KEY_REJECTED`)
   and six unit fixtures for the single-line stack and runner-log laws,
   plus 4 new positive controls (archived-unit single-line anchor,
   archived and synthetic stack positives, runner-log positive); the
   dead/survivor/restore strict-classifier positives and every R2
   fixture are retained (the stage fixtures now write the exact
   three-line runner logs).
4. `containment_selfcheck.py` under `python3` and `python3 -O` (stdout
   byte-identical): **38 `expect_rejection` call sites → 41 rejection
   executions** (the four-way runtime-limits mutation loop) **+ 34
   manual refusals = 75 hostile refusals per interpreter**, 32 pass
   markers.  The manual set is R2's 28 (the 18-parameter
   `decide_terminal` mutation table — the function has 19 gate
   parameters, `swap_zero` and `swap_violation` exercised jointly and
   singly — foreign candidate, wrong recorded PGID, launcher starttime,
   hung reap, six terminal-CLI refusals) plus the five
   `runtime-limits-record` refusals and the wrong-archive-digest CLI
   refusal.  Every late-decision fixture now runs through a real freeze
   (`build_complete_manifest` → `tar` → `extract_and_verify_archive`);
   new controls include `O_B1_WORKING_FORGERY_REJECTED` (the review's
   §5 forgery, byte-for-byte in spirit: rewritten verdicts + summaries +
   re-run `decision-build` inside the extraction),
   `EXTRACTION_EDIT_DELETE_EXTRA_SYMLINK_REJECTED`,
   `ARCHIVE_EXTRACTION_MIX_AND_MATCH_REJECTED`,
   `ARCHIVE_REPLACEMENT_AND_SYMLINK_REJECTED`,
   `FAULT_LATCH_REGRESSION_REJECTED` (+ worker-rc disagreement),
   `RUNTIME_LIMITS_FIVE_PROPERTY_CONTROLS_PASS`,
   `JOB_TAG_STAMP_SCHEMA_REJECTED`, and 3 new positive controls (honest
   bounded-no-verdict chain, `runtime-limits-record` positive, stamp
   positive); the R2 positives (clean CLI promotion with real archive
   digest and decision hash in the marker, live-candidate
   mutation/deletion inertness, no-replace collision,
   directory-exactness, lease/nonce controls) are retained.
5. A final containment replay from the fully packaged directory is
   byte-identical to the banked stdout.
6. Driver fail-closed dry runs under `python3` and `python3 -O` with a
   full synthetic binding environment: both rc 2,
   `ADAPTER_FAILURE_NO_VERDICT`, exact cause
   `RuntimeError:STAGE_RESULT_MISSING:witness_replay`, remainder = 3
   generators at bound 6, byte-identical summaries.
7. Independent probes (banked in `preflight/`): archived node-1 exact
   censuses and SB triple decomposition with the single-newline unit
   anchor (unit SHA-256 `84872c7a1562c25933964706d65fc4394ca88ca674b41084d5e4109f4b1ef575`);
   result-record schema agreement (runner == driver == classifier,
   19 keys); identity-record schema agreement (runner == census
   constant, 17 keys); runner-stdout law == runner print statements,
   float-repr round-trip control.
8. Source archive: build, 23-file-only-member launch-census replay,
   fresh extraction with 22/22 manifest `OK`, sidecar verification,
   `LAUNCH_MANIFEST.sha256` self-check 6/6 `OK`, archive file mode 0444.

Grand total per interpreter: **127 hostile refusals + 38 positive
controls** across the two suites (the R2 report's 15 + 16 retained
positives plus the 7 new ones named above), run under both interpreters
(330 fixture executions), plus the compile/prepare/build/determinism/
dry-run/probe/archive verifications above.

## 7. R2 → R3 file/function diff inventory

Byte-identical files (6): `prepare_resume.py`, `build_resume.py`,
`run_singular_stage.py`, `adapter_selfcheck.sing`,
`diagnostic_hostile.sing`, `EXPECTED_GENERATED_SCRIPTS.sha256`.

Changed files and their exact function-level deltas:

| file | changed definitions | added definitions | purpose |
|---|---|---|---|
| `containment_contract.py` | `require_job_tag` (stamp), `verify_lease` (split), `derive_late_decision` (archive-bytes rewrite), `main` (new CLI args/paths) | `FrozenArchiveView` (+ its `data`/`text`/`json`/`sha256` accessors), `walk_fresh_root`, `authenticate_frozen_archive`, `verdict_from_bytes`, `parse_sha_sidecar_text`, `validate_lease_record`, `runtime_limits_verified`, `build_runtime_limits_record`; constants `STAMP_RE`, `RUNTIME_LIMIT_EXPECTED`, `RUNTIME_MAX_USEC_21600`, `FAULT_LATCH_SCHEMA`, `FAULT_LATCH_FIELDS`, `DECISION_RETAINED_MEMBERS`, r3 schema/prefix strings | O-B1, O-N3, O-N4, O-N8v |
| `resume_recursor.py` | `Recursor.run_stage` (runner-log + identity census), `identical_copies` (divisors) | `IDENTITY_RECORD_KEYS`, `expected_runner_stdout`, `require_runner_logs`, `require_single_line_append_stack`; docstring paragraph | O-N1, O-N2, O-N6, O-N7 |
| `classify_resume.py` | `Classifier.check_stage` (runner-log + identity census), `Classifier.verify_node_sb` (exact law) | — (docstring paragraph) | O-N1, O-N2, O-N6 |
| `aws_supervisor.sh` | r3 case path; runtime read-back via `runtime-limits-record`; `FAULT_LATCHES_PRE_ARCHIVE.json` write before `manifest-build`; `FINALIZATION_LATCHES.txt` binding + `.sha256` sidecar; terminal call gains `--terminal-archive`/`--manifest-relative`/`--dirs-relative`/includes | | O-B1, O-N3, O-N4 |
| `aws_job_worker.sh` | r3 case path only | | rename |
| `aws_launch_preflight.sh` | r3 archive name/hash/case path/tag prefix/allowed prefixes; O-N5 header comment | | rename, O-N5 |
| `containment_selfcheck.py` | `build_decision_fixture` (candidate parameter + latches), `derive` (archive args + faults), `main` (freeze-based C1 flow, new CLI args, new token gates, stamp/runtime fixtures) | `freeze_fixture`, `rebank_decision`, `rewrite_extracted`, `refreeze`, fixture constants | O-B1 forgery + variants, O-N3/O-N4/O-N8v fixtures |
| `generator_selfcheck.py` | `FixtureJob.write_stage` (exact runner logs), `main` (new unit controls + fixtures 19–23) | — | O-N1/O-N2/O-N6 fixtures |
| `runtime_expectations.env` | `EXPECTED_PREREG_SHA256` re-pinned to the R3 `AWS_PREREGISTRATION.md` | | doc chain |
| `README.md` / `PREREGISTRATION.md` / `AWS_PREREGISTRATION.md` | R3 status/prose; exact append-law paragraph; O-B1/O-N3/O-N4/O-N5 descriptions; rehearsal items 8–11; corrected manifest arithmetic and mode wording | | docs |
| manifests/sidecars/archive | regenerated from the R3 source (`SOURCE_MANIFEST.sha256`, `PREREGISTRATION.sha256`, `SOURCE_ARCHIVE.sha256`, archive, `LAUNCH_MANIFEST.sha256` now report-free, new `REPORT_BINDING.sha256`) | | derived |

No definition was removed anywhere.

## 8. Repair crosswalk (review finding → R3 repair → evidence)

| finding | repair | evidence |
|---|---|---|
| **O-B1** (blocking): late authority authenticated the mutable extraction; working promotion forgery | archive-bytes authentication at decision time: charged-digest re-hash, full member/manifest/directory census from archive bytes, member-for-member byte binding of the extraction, in-memory decision inputs; supervisor passes `--terminal-archive` + manifest args; missing inputs refuse | `O_B1_WORKING_FORGERY_REJECTED`, `EXTRACTION_EDIT_DELETE_EXTRA_SYMLINK_REJECTED`, `ARCHIVE_EXTRACTION_MIX_AND_MATCH_REJECTED`, `ARCHIVE_REPLACEMENT_AND_SYMLINK_REJECTED`, wrong-digest CLI refusal, honest DEAD and honest NO_VERDICT chains promote |
| O-N1: divisibility-only node-SB census; vacuous empty-node census | exact single-line append law anchored on the archived unit (one newline) | `ARCHIVED_SB_UNIT_SINGLE_LINE_ANCHOR_PASS`, `SINGLE_LINE_APPEND_STACK_CONTROLS_PASS`, `NODE_SB_DOUBLED_STACK_REJECTED`, `NODE_SB_MULTILINE_STACK_REJECTED` |
| O-N2: runner logs unbound | exact three-line stdout + empty stderr law in driver and classifier | `RUNNER_LOG_LAW_UNIT_CONTROLS_PASS`, `RUNNER_STDOUT_TAMPER_REJECTED`, `RUNNER_STDERR_TAMPER_REJECTED`, schema probe |
| O-N3: read-back verified 3 of 5 properties, no exact RuntimeMaxUSec | five-property exact predicate shared by supervisor CLI and late authority | `RUNTIME_LIMITS_FIVE_PROPERTY_CONTROLS_PASS`, four archived-limits mutations refused at derive |
| O-N4: latches outside the archive | in-archive `FAULT_LATCHES_PRE_ARCHIVE.json` + regression gate; bound `FINALIZATION_LATCHES` + sidecar | `FAULT_LATCH_REGRESSION_REJECTED`, worker-rc disagreement refusal |
| O-N5: launch manifest uncharged | report-free 6-line launch manifest tabled here; `REPORT_BINDING.sha256` carries the report hash | §5 table; launch-manifest self-check 6/6 OK |
| O-N6: identity keys not closed | 17-key census in driver + classifier | `IDENTITY_INJECTED_KEY_REJECTED`, schema probe |
| O-N7: Θ(n) count scan | divisor enumeration, identical behavior | R2 decomposition fixtures replay unchanged |
| O-N8v: stamp unenforced in the contract | stamp regex inside `require_job_tag` | `JOB_TAG_STAMP_SCHEMA_REJECTED` |
| O-N8 prose (manifest arithmetic, member modes, 18-vs-19 gates) | corrected in §3/§5/§6 and in the packet documents | this report; README/PREFLIGHT_REPORT wording |
| review §8 rehearsal items 1–4 | added verbatim-in-substance as mandatory rehearsal steps 8–11 plus the witness-unit capture note | `AWS_PREREGISTRATION.md` |

## 9. Remaining risks and rehearsal debt (for the reviewer)

1. **No Singular ran locally** (unchanged); the witness replay and node
   stages first run on AWS.
2. **All custody fixtures are pure/parser-level.**  The freeze-based
   fixtures exercise the real manifest/tar/extraction/decision code
   paths, but the launcher, supervisor, stage runner, systemd scope,
   watchdog, and live `/proc` gates have never executed; rehearsal steps
   1–11 are mandatory before any pilot and are the only place those
   behaviors become evidence.
3. **RuntimeMaxUSec rendering set** (`6h`/`21600s`/`21600000000us`): an
   honest host rendering outside this set downgrades to a custody
   no-verdict rather than promoting; rehearsal step 9 captures the live
   shape.
4. **Decision-time cost**: the late authority now re-hashes and
   byte-compares the whole terminal archive once (one streaming pass plus
   the outer hash); for the expected archive sizes this is seconds and it
   runs inside the whole-job budget; failure mode is a custody
   no-verdict.
5. **Single-line append law scope**: anchored on the archived node-1
   unit and on `string(...)` semantics; if a future frozen input's write
   were ever multi-line the law refuses (downgrade, never promote), and
   the constant/fixtures make the assumption explicit.
6. **Classifier strictness** (unchanged direction from R2): the new
   runner-log, identity-census, and node-SB laws are additional rejection
   surface; an honest deviation downgrades, never promotes.
7. **Performance unknowns** (node-2 saturation cost, reverse bound 64)
   are unchanged and remain preregistered bounded no-verdicts.

## 10. Session evidence

Local preflight evidence is preserved under the packet's `preflight/`
directory.  The R3 source archive replayed cleanly (sidecar hash,
23-file-only-member census, 22/22 embedded-manifest verification from a
fresh extraction, 6/6 launch-manifest self-check).  The R1 and R2 packet
directories, the R1/R2 reports, the hostile reviews, and every canonical
file are unmodified; this packet directory and this report (plus the
post-report `REPORT_BINDING.sha256`) are the only additions, plus the
bounded `/tmp/triple02-r3-preflight` scratch tree.

Report-body SHA-256 (all preceding bytes, including the newline immediately before this line): ea71583070a6c51c11c6201b8a3f8f74d541652116a880dd8f6ed412c0759f76
