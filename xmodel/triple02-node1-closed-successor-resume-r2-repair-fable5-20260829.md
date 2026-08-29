# TRIPLE02 node-1 closed-successor resume R2 — custody-repair producer report

Author: Fable 5 (source producer, not reviewer).  Date: 2026-08-28
(packet dated 20260829).  Working directory: `/Users/dc/code/math/jc2`.

Deliverable: the fresh directory
`cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r2_20260829/`
and this report.  R1 was not overwritten or patched; the R1 packet and R1
report are untouched.  Nothing was launched, no CAS was run, no canonical
file was edited, nothing was committed, `jc2-lean` was not accessed, no
repository-wide command was run, and no web/AWS operation was performed.
Bounded scratch replays ran under `/tmp/triple02-r2-preflight`,
`/tmp/triple02-r2-stage`, and `/tmp/triple02-r2-probe`.

## Verdict

**`SOURCE_READY_AWS_NOT_AUTHORIZED`**

The only next action licensed by this report is a hostile source review of
this R2 packet by a different model.  No AWS launch, rehearsal, or pilot is
authorized; after a passing review, the disposable-instance rehearsal in
`AWS_PREREGISTRATION.md` and a separate coordinator `GO` remain mandatory.

## 1. Charge

This packet repairs the custody blockers of the hostile source review

- R1 producer report
  `xmodel/triple02-node1-closed-successor-resume-r1-fable5-20260829.md`,
  SHA-256 `93b894306401e1e2e1965788708b9fe071f93336d4db01446ad7f58c3b0dcca9`
  (re-verified this session);
- hostile review
  `xmodel/triple02-node1-closed-successor-resume-r1-hostile-review-sol56-20260829.md`,
  full SHA-256
  `ad25f49675f26128d220a5954c8e7f72580060b929e42868eeefaefd75cfafb2`,
  body hash
  `019ac48bef4ff4999e76d17dde7a4428c48accb1c8d35b26702e0283df898caf`
  (full hash re-verified this session; verdict `REPAIR_REQUIRED`, blockers
  C1–C3 plus the "other custody findings" table),

while keeping the R1 mathematical recursion fixed.  All seven frozen
dependencies named by the packet/review were re-verified byte-exact this
session: the R1 report (above), R1 `SOURCE_MANIFEST.sha256`
(`9d593d61c74f01df39e5b69a3ec4d0d5538e2fa280f2cf9f7a9d4ebcb4f39655`), the
R1 source archive
(`6a4dc35fe31cdbd1ca3eed7064b417e798072d75240e31b60d0e4b70462e6a9f`), the
R3 terminal archive
(`e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1`), the
proper-open R5 terminal archive
(`4b8ffc1c16828b22b2e76a3aa92a25e8c1f472190a708f30a7b71ba952cbef7e`), the
frozen r5 recursor
(`d679a4d7fb4bf2619fbb3ff47ea6f386ba1c75fdc477276cabf3bec8a2b2cd90`), and
the frozen transcript gate
(`0e0efd5ada59039a373a731038f2f88a3794b376b208879c2459bff97d0e7316`).

## 2. What is mathematically unchanged

The source-confirmed mathematics of the R1 review is preserved exactly:

- node-2 seed `(g1, g2, Delta_node1)` with the three literal hashes
  `2b9d29b7...8206` / `fecd1d43...9336` / `84b4c2c4...1d02`, inherited
  bound 6 (rank archive `b947a2d3...b809`, certificate member
  `cc6dc1c4...99d2`), no node-1 open reentry (three firewalls), the
  structural rank bound 6, the repaired two-containment saturation theorem,
  the complete rank-0..6 chart templates with exact endpoint
  coefficients/plants, and the narrow four-string allowlist with no
  radical/geometric/whole-component/JC2 widening.
- `build_resume.py`, `adapter_selfcheck.sing`, and `diagnostic_hostile.sing`
  are byte-identical to the reviewed R1 files (same hashes `3763ac7a...`,
  `e616b595...`, `01be8175...`).
- The repaired saturation/chart template builders and their validators in
  `resume_recursor.py` are byte-identical functions; the regenerated
  witness-replay and node-2 reduce scripts reproduce the R1 pins exactly:
  `27cb85082e8ea56a4a9bc8d0cb38b889edc4e981529d6697b0ff2800e0159d0d` and
  `d9e79b427dd22718683b2ac3f5f50dbd9839622ee07bf95cb61f02bdd380d8b8`
  (verified in this session's builds, byte-identical across two
  independent builds and under `python3 -O`).

## 3. New latent defect found and repaired (disclosed)

While deriving the classifier's exact artifact sets I probed the archived
node-1 artifacts and found a defect the R1 review did not reach (it had
correctly marked the live Singular replay as rehearsal debt):

**The archived `NODE_001_STANDARD_BASIS.txt` (pinned `bd95508c...640d`,
14,883 bytes) is exactly three identical concatenated copies of a
4,961-byte unit.**  Singular's `write()` appends, and the archived node-1
directory ran three stages (reduce, rank_size_6, saturation) whose shared
`node_header` each wrote the standard basis.  The R1 witness replay writes
one copy and byte-compares it against the archived file in both the driver
and the classifier, so the R1 job was guaranteed to end
`ADAPTER_FAILURE_NO_VERDICT` at the witness replay on the live host.

R2 repairs the comparison in both places to the exact appended-copy law
`archived == produced * 3` (the count 3 is the deterministic number of
archived node-1 header-writing stages), keeps the stage-unique pivot and
residual TSVs as byte-exact comparisons, and extends the same law to the
resumed nodes: each node's standard-basis file must be a whole-number
stack of one repeated unit matching the completed header-writing stage
count (skipped only for a node containing the timed-out final stage, whose
partial append is undecidable).  Selfcheck fixtures cover the
decomposition positives and the full-archive-submission refusal.

## 4. The R2 custody architecture

### C1 — content-addressed decision record; archive-only late authority

- After the classifier passes, the worker banks
  `custody/DECISION_RECORD.json` + `custody/DECISION_RECORD.sha256`
  (`containment_contract.py decision-build`).  The candidate is derived,
  never an argument: production `VERDICT.txt` and classifier `VERDICT.txt`
  must be equal, allowlisted, and equal to both summaries'
  `classification`; both summaries must carry this job's binding block.
  The record binds job tag, nonce, source-archive hash, exact Singular
  binary digest, containment mode (`systemd_scope` required), lease hash,
  launcher hash, worker/supervisor identities and identity-file hashes,
  production and classifier summary/verdict hashes, and the complete
  `WORKER_ARTIFACT_MANIFEST.sha256` hash.
- The supervisor freezes the terminal archive, keeps the fresh private
  extraction on disk, and the terminal decision
  (`containment_contract.py terminal`) reads **only that fresh
  extraction**: sidecar-checks the decision record's content address,
  re-derives the candidate from the archived record plus the archived
  production and classifier verdicts, and replays every recorded equality
  (lease — also against the live lease file, identities, all four
  summary/verdict hashes, artifact manifest, Singular digest sidecar,
  containment mode, runtime limits).  The supervisor's decision command
  has no live-candidate argument at all (`containment_selfcheck` gates the
  supervisor text for this), and fixtures prove that mutating or deleting
  the live candidate after the archive freeze cannot change the decision.
- The public `TERMINAL.marker` is three lines — classification,
  `TERMINAL_ARCHIVE_SHA256=...`, `DECISION_RECORD_SHA256=...` — published
  by no-replace hard link; emergency/no-verdict markers carry `NONE`
  fields.  `FINALIZATION_LATCHES.txt` gains the runtime-fault and mode
  fields; the pre-archive custody record set (decision record, candidate,
  identities, mode, runtime limits, lease) is inside the reviewed archive.

### C2 — every dynamic stage bound to this job and regenerated

- `run_singular_stage.py` now verifies, before each launch: job tag and
  schema-checked nonce against its environment, the exact source-archive
  bytes, the exact Singular binary bytes, the live worker and supervisor
  PID identities by start time and uid, and its inherited PGID/SID; after
  launch, the child's PGID/SID/uid/cgroup must equal the runner's.  The
  identity record carries argv, cap, lease hash, source hash, binary
  digest, and the supervisor/worker/runner/child identities with cgroups;
  the result record repeats the full binding and hashes the identity
  record.
- `resume_recursor.py` reads the binding fail-closed from the environment
  (`JobBinding`), passes it to every stage, validates each result's
  binding and key census, and banks per-stage `result_sha256` into the
  summary together with a `job_binding` block, so the summary transitively
  binds every stage record.
- `classify_resume.py` is rewritten: it regenerates every dynamic script
  (witness replay via the builder module, reduce/rank via the frozen r5
  builders, saturation/chart via the packet's validated repaired-template
  builders) and byte-compares each against what ran; requires and verifies
  every stage's identity record and hash binding against this exact job
  (tag, nonce, lease, source, binary, caps, argv, PGID/SID/uid/cgroup,
  worker/supervisor start times); regenerates each rank census JSON and
  byte-compares it; closes every production directory over an exact
  expected artifact set (`Ledger`) in which only the timed-out final
  stage's statically known Singular write set is optional; and re-derives
  each bounded no-verdict from the stage evidence (unique timed-out final
  stage, reverse-exhaustion counts and file censuses, node count for
  max-nodes exhaustion), requiring the driver's recorded reason, exact
  remainder generators/hashes/bound, and stage-record list to equal the
  re-derivation.  The runner/driver/classifier result-record schemas were
  independently extracted and agree exactly.

### C3 — systemd-only success; PGID fallback is NO_VERDICT-only

- The worker scope is launched with `RuntimeMaxSec=21600`,
  `KillMode=control-group`, `MemoryMax=274877906944`, `TasksMax=512`, and
  `MemorySwapMax=0`; the probe requires every property, and the supervisor
  reads the live scope's properties back, records them in
  `custody/systemd_runtime_limits.json`, and latches
  `systemd_runtime_fault` (a new sticky gate and a new
  containment-preflight condition) if any is missing, `infinity`, or
  wrong.
- Supervisor-death containment: a watchdog inside the worker scope polls
  the exact supervisor PID start time every 5 s and kills the whole scope
  cgroup on loss; independently the scope is owned by the external user
  systemd manager whose `RuntimeMaxSec` bounds the tree even if the
  watchdog dies with it.  This is a design plus rehearsal plan; **no claim
  is made that the live behavior has run** (see §7).
- The PGID fallback is NO_VERDICT-only three times over: the worker in
  fallback mode refuses all Singular stages and production and banks
  nothing; `decision-build` refuses outright
  (`DECISION_REQUIRES_SYSTEMD_SCOPE`); and the late authority requires
  recorded == archived == live mode `systemd_scope` plus a verified
  runtime-limit record for any mathematical terminal
  (`systemd_mode_ok`/`runtime_limits_ok` gates in `decide_terminal`).

### Other repaired findings

- **Nonce/lease**: `JOB_NONCE` (`^[a-z0-9]{8,32}$`) and
  `JOB_TAG = prefix_<STAMP>_<NONCE>` composition are enforced by the
  launcher (bash regex), the contract (`require_nonce`/`require_job_tag`),
  the supervisor, the worker, every stage runner, and the classifier; the
  R1 empty-suffix glob acceptance is a refusing fixture.  The launcher
  builds the content-addressed `LEASE.json`+`LEASE.sha256`; direct
  supervisor entry verifies the lease and takes an atomic
  `mkdir $JOB_ROOT/.supervisor_lease` sub-lease or fails closed; worker
  and stage runners re-verify.
- **No-replace publication**: terminal archive install and both marker
  paths (normal and emergency) publish via hard link (`ln`/`os.link`),
  which is atomic and never replaces; a collision fixture proves the first
  marker survives.  The R1 `mv`-publication line is a refusing source gate
  in `containment_selfcheck`.
- **Directory-exact archives**: `manifest-build` records
  `custody/TERMINAL_DIRS.list` (itself manifest-covered);
  `manifest-verify` and `archive-extract-verify` require the on-disk and
  tar directory sets to equal it exactly.  The review's
  `unmanifested_empty_directory_accepted` attack is now a refusing fixture
  alongside the regular-extra fixture.
- **Launcher self-binding**: the launcher verifies its own bytes against
  the charged `LAUNCH_MANIFEST.sha256` (exact line match) plus the archive
  line, installs a read-only copy of itself into the job root, and records
  its measured hash and the launch-manifest hash in the lease; the worker
  re-hashes the copy against the lease, and the decision record binds the
  launcher hash.  The archive pins the launcher's counterpart direction
  (launcher pins archive; launch manifest pins launcher), avoiding hash
  self-reference.
- **Stale censuses**: the R3 and proper-open archive censuses are now hard
  preparer gates and correct prose everywhere: **454 = 391 files + 63
  dirs** and **574 = 490 files + 84 dirs** (verified against the real
  archives this session; R1's 437/374 and 565 prose was stale).
- **Fixture realism**: both selfchecks and all packet documents state
  explicitly that every custody fixture is pure/parser-level and that
  launcher/supervisor/runner/systemd//proc behavior is untested rehearsal
  debt; no fixture claims live process coverage.

## 5. Packet contents and hashes

Case dir `cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r2_20260829/`:

| file | SHA-256 |
|---|---|
| `prepare_resume.py` | `1eb8ed781843fd0efd633722ddd74853266d0e361b6e78a0d7e5ab9e1b302528` |
| `build_resume.py` (byte-identical to R1) | `3763ac7a5ce2915ede7c21c9d9b8dcb3fc1ab12075c998daa646a375b640f780` |
| `resume_recursor.py` | `f3a069495afcb7f4eef95cb0de4b1aa05f2dfde61ce598576098ac45defdb84e` |
| `classify_resume.py` | `a8887f05d59a3b1fae45491fac8eaa076ffa679cbf7fc8fb0ce0ef1e0d9fe345` |
| `generator_selfcheck.py` | `6ea8bd981f31ceea9d50d867fd7989f004017043849cfeafd1e0ebf3ff6ea3de` |
| `run_singular_stage.py` | `766bebf02496c2bcdd34c575219b819d4d332f404f286cc49dedab793ffe9564` |
| `containment_contract.py` | `0f47a460ec8c579b5e9782292b4d2ab92758996ada8e6cb7df2d038ee7b1ed55` |
| `containment_selfcheck.py` | `f285b577d76f181384999327536a3b80cb25f34caa5a80323404021ec91627b8` |
| `adapter_selfcheck.sing` (byte-identical to R1) | `e616b59542a977dd9daa6865dbf18b60feaae06f784d98f72cf8cced27ee4490` |
| `diagnostic_hostile.sing` (byte-identical to R1) | `01be817524da040ad97eeb52adc461d6556e2d8cd179c9447c4c5101a2f15e02` |
| `aws_job_worker.sh` | `e34f4fe2b8d3c2c32e83a3ff1a27e7bcabc9c37b4de35835475775224b601039` |
| `aws_supervisor.sh` | `62e68a6d3de7da61116eaf19e79a3ecfb6dd2c0fddf33851fe8be10a2a23d31d` |
| `aws_launch_preflight.sh` | `fce26e922f2ebfa797436d6894840b092dc224226d6cfac5d2a7893309892851` |
| `runtime_expectations.env` | `d4bfe8cb6d8223b2939c3afe503f7b1283449022c6efcbc481387465afa4ba32` |
| `EXPECTED_GENERATED_SCRIPTS.sha256` (byte-identical to R1) | `9912dd2279223347d461b5640583b84283216d4873b56e3be34770314f2b5696` |
| `SOURCE_MANIFEST.sha256` (22 entries) | `cd4e47ee6f9c0fc48c49b4718a0aa762e946b90efd85b28aa1736c9ab5d05733` |
| `AWS_PREREGISTRATION.md` | `c1a906b42f3fd14a0f7d26af8dd0d47cf13f69285ece9a45bd4b942f65beb216` |
| `PREREGISTRATION.md` | `95100ac755991d1a7f0d83ca3d33f9cebd80f2746b3885de8de0bea71640b67a` |
| `PREREGISTRATION.sha256` | `ed66a65aeaaca13cabf208b3ccaf29b21949c8046d2798de47ce4fa4b0d7a8f8` |
| `README.md` | `4297eb105be4f76e0fdab9c444c6cadb97ef057f878a20ff334cd47c0f7867fb` |
| `PREFLIGHT_REPORT.md` | `22316004c500f0ebedabf1bdf239f62d9d07e2936f792cd7d24ccc6818f69503` |
| `SOURCE_ARCHIVE.sha256` | `c58a5f678cd4b89c3c5c048e597a8f9e452a0f4de13b9f285bd1732b8944baf9` |
| source archive `custody/ggv_triple02_closed_successor_resume_r2_SOURCE.tar.gz` (23 file-only members, mode 0444) | `183ab5e0139cf6b68482f58ed72e63262f3423c6ffa3f3b5568a014c44a65987` |

`LAUNCH_MANIFEST.sha256` is written immediately after this report (it
lists this report's full-file hash, so it cannot be tabled here); it
covers the launcher, both sidecars, the archive, `SOURCE_MANIFEST.sha256`,
both preregistrations, and this report.  Reviewers must charge the exact
launcher hash `fce26e92...2851` and this report's hash independently.
`preflight/` holds the local evidence (prepared-inputs census, build
stdout, both selfcheck stdouts, the containment fixture JSON, the
fail-closed dry-run summary, the archive-replay note, and the five build
products).

The archive's 22 manifest entries are the 18 in-case files (everything
above except `SOURCE_ARCHIVE.sha256`, `PREFLIGHT_REPORT.md`,
`LAUNCH_MANIFEST.sha256`, and the archive itself) plus the four frozen
dependencies; a fresh extraction verified all 22, and the launch-census
replay confirmed 23 file-only members under the four allowed `jc2/`
prefixes.

## 6. Local verification (all pass; exact counts)

1. `python3 -m py_compile` and `python3 -O -m py_compile` over all eight
   Python files; `bash -n` over the three shell scripts.
2. `prepare_resume.py` against the real frozen archives, with the new
   exact census gates; `build_resume.py` reproducing both R1 script pins;
   determinism re-run into fresh directories with all five build products
   byte-identical.
3. `generator_selfcheck.py` under `python3` and `python3 -O`: **41 hostile
   fixtures refused + 15 positive controls** (34 `expect_rejection` call
   sites, two of which are 3-way loops, so 38 rejection executions, plus 3
   manual refusal controls: wrong member selection, open-route member
   selection, Singular-diagnostic transcript).  The hostile set includes
   the C2-mandated candidates: missing identity, copied prior-job
   nonce/starttime, identity-hash mismatch, fabricated one-line script,
   wrong cap/binary/source, artifact-set extra, fabricated timeout reason,
   remainder/stage-record/binding tampers, and the witness-SB full-archive
   submission; the positive controls include the strict-classifier dead/
   survivor/restore runs over fixtures whose stage scripts are the real
   regenerated builder outputs under a full synthetic job binding, and the
   archived-SB triple-decomposition checks.  38 pass markers printed.
4. `containment_selfcheck.py` under `python3` and `python3 -O`: **53
   hostile fixtures refused + 16 positive controls** (25
   `expect_rejection` call sites plus 28 manual refusals: the 18-way
   `decide_terminal` mutation table — now including systemd-runtime-fault,
   pgid-mode, runtime-limits, lease, and decision gates — the foreign
   candidate, wrong recorded PGID, launcher starttime mutation, hung-reap
   bound, and six terminal-CLI refusals).  Covers candidate swaps before/
   after archive freeze, the live-candidate-never-read control (mutation
   and deletion both inert), copied decision record, decision-build
   split-candidate and pgid refusals, no-replace terminal collision,
   directory-exact archive controls with the empty-directory negative
   fixture, lease/nonce schema mutations, and the three-line marker
   binding.  25 pass markers printed.
5. Driver fail-closed dry runs under `python3` and `python3 -O` with a
   full synthetic binding environment: both rc 2,
   `ADAPTER_FAILURE_NO_VERDICT`, exact cause
   `RuntimeError:STAGE_RESULT_MISSING:witness_replay`, remainder = 3
   generators at bound 6, byte-identical summaries.
6. Independent probe of the archived node-1 artifacts (§3): census
   454/391/63 reconfirmed, standard-basis triple decomposition
   14,883 = 3 × 4,961 bytes, pivot/residual single-header confirmation.
7. Result-record schema agreement probe: runner-emitted keys ==
   driver-required census == classifier-required census.
8. Source archive: build, 23-file-only-member census replay, fresh
   extraction with 22/22 manifest `OK`, sidecar verification, mode 0444.

Grand total: 94 hostile refusals + 31 positive controls per interpreter
across the two suites, run under both interpreters (250 fixture
executions), plus the compile/prepare/build/determinism/dry-run/archive
verifications above.

## 7. Remaining risks and rehearsal debt (for the reviewer)

1. **No Singular ran locally** (unchanged from R1); the witness replay and
   node stages first run on AWS, now with the triple-copy comparison that
   makes the replay satisfiable.
2. **All custody fixtures are pure/parser-level.**  The launcher,
   supervisor, stage runner, systemd scope (RuntimeMaxSec enforcement,
   KillMode, MemorySwapMax, scope collection), supervisor-death watchdog,
   and live `/proc` gates have never executed; the seven-point
   disposable-instance rehearsal in `AWS_PREREGISTRATION.md` (which
   includes the review's minimum rehearsal list plus the PGID-refusal and
   marker-collision cases) is mandatory before any pilot and is the only
   place those behaviors become evidence.
3. **systemd feature dependence**: `RuntimeMaxSec`/`MemorySwapMax` on user
   scopes require a reasonably recent systemd; on hosts that reject any
   probe property the job degrades to the NO_VERDICT-only fallback rather
   than running unbounded — fail-closed, but it means an unsuitable AMI
   yields no mathematics.
4. **Appended-copy law scope**: the count 3 for the archived node-1
   standard basis is derived from the archived stage set; if a future
   frozen input has a different stage history the constant must be
   re-derived (it is a named constant with fixtures, not a magic number).
5. **Classifier strictness risk**: the exact-artifact-set and
   full-binding checks are new rejection surface; an honest run that
   produces an unforeseen artifact would be downgraded to a custody
   no-verdict, never promoted — conservative by construction, but a
   reviewer should probe the expected-set derivation (stage write sets,
   timeout partials, `NODE_RESULT.json` presence rules) against the frozen
   r5 script builders.
6. **Performance unknowns** (node-2 saturation cost, lower-size rank
   census size, reverse bound 64) are unchanged from R1 and remain
   preregistered bounded no-verdicts.

## 8. Repair crosswalk (review finding → R2 repair → evidence)

| Review finding | R2 repair | Where | Fixture/evidence |
|---|---|---|---|
| C1: allowlisted live candidate accepted; post-archive reread; marker unbound; latches/decision outside archive | Content-addressed decision record binding tag/nonce/source/lease/launcher/binary/identities/summary+verdict hashes/artifact manifest/candidate; late authority reads only the fresh archive extraction and replays every equality; marker carries archive+decision digests; no live-candidate argument exists; pre-archive custody records archived | `containment_contract.py` (`decision-build`, `derive_late_decision`, `terminal`), `aws_job_worker.sh`, `aws_supervisor.sh` | `CANDIDATE_SWAP_BEFORE_ARCHIVE_REJECTED`, `CANDIDATE_SWAP_AFTER_ARCHIVE_INERT`, `LIVE_CANDIDATE_NEVER_READ_CONTROL_PASS`, `COPIED_DECISION_RECORD_REJECTED`, `TERMINAL_MARKER_ARCHIVE_AND_DECISION_BINDING_PASS`, supervisor-source gate on `--candidate` |
| C2: stages self-hashed, not job-bound; classifier accepts fabricated one-line stages, ignores identities, no regeneration; no-verdicts by allowlisted string | Full one-job binding in runner/driver/classifier; identity record hashed into result; classifier regenerates every script and census, requires identities, closes exact artifact sets, re-derives reasons/remainder/records | `run_singular_stage.py`, `resume_recursor.py` (`JobBinding`, bound `run_stage`), `classify_resume.py` (rewrite) | `MISSING_STAGE_IDENTITY_REJECTED`, `COPIED_PRIOR_JOB_STAGE_NONCE_REJECTED`, `COPIED_PRIOR_JOB_IDENTITY_STARTTIME_REJECTED`, `STAGE_IDENTITY_HASH_MISMATCH_REJECTED`, `FABRICATED_ONE_LINE_SCRIPT_REJECTED`, `WRONG_STAGE_CAP/SINGULAR/SOURCE...REJECTED`, `NODE_ARTIFACT_EXTRA_REJECTED`, `FABRICATED_NO_VERDICT_REASON_REJECTED`, `REMAINDER/STAGE_RECORD/SUMMARY_BINDING..._REJECTED`, schema-agreement probe |
| C3: no fail-safe on supervisor SIGKILL; no independent runtime; PGID fallback promotable | Worker scope with RuntimeMaxSec/KillMode=control-group/MemorySwapMax=0/MemoryMax/TasksMax, live property read-back with sticky `systemd_runtime_fault`; in-scope supervisor-death watchdog; PGID fallback refuses production, decision-build, and promotion | `aws_supervisor.sh`, `aws_job_worker.sh`, `containment_contract.py` (`systemd_mode_ok`/`runtime_limits_ok` gates) | `PGID_FALLBACK_PROMOTION_REJECTED`, `RUNTIME_LIMITS_PROMOTION_GATE_PASS`, `STICKY_RUNTIME_FAULT_NEGATIVE_CONTROL_PASS`, decision `pgid`/runtime fixtures; live behavior explicitly rehearsal debt (§7.2) |
| Empty nonce accepted; no nonce schema; records not nonce-bound | `^[a-z0-9]{8,32}$` nonce + exact tag composition enforced in launcher/contract/supervisor/worker/runner/classifier; nonce in every stage record, lease, decision, marker chain | all custody files | `EMPTY_AND_MALFORMED_NONCE_REJECTED`, empty-suffix tag fixture, stage nonce fixtures |
| Direct supervisor entry has no lease | Supervisor verifies the launcher's content-addressed lease and takes an atomic `.supervisor_lease` mkdir sub-lease or exits 70 | `aws_supervisor.sh`, `containment_contract.py` (`lease-build`/`lease-verify`) | `LEASE_BINDING_CONTROLS_PASS`, supervisor source gates |
| `mv` publication; same-UID rerun races | No-replace hard-link publication for archive and both marker paths | `aws_supervisor.sh`, `publish_no_replace` | `TERMINAL_COLLISION_NO_REPLACE_PASS`, source gate on the old `mv` line |
| Unmanifested empty directory accepted | Directory census (`TERMINAL_DIRS.list`) required equal in manifest-verify and archive-extract-verify | `containment_contract.py` | `UNMANIFESTED_EMPTY_DIRECTORY_REJECTED` (plus retained regular-extra fixture) |
| Launcher does not self-verify its manifest | Launcher verifies own bytes + archive line against the charged `LAUNCH_MANIFEST.sha256`, installs a self-copy, records both hashes in the lease; worker re-verifies the copy; decision binds the launcher hash | `aws_launch_preflight.sh`, lease/decision schemas | worker lease/copy gates; decision `launcher_sha256` equality |
| Stale 437/374 and 565 censuses | Exact censuses 454=391+63 and 574=490+84 as preparer hard gates and corrected prose | `prepare_resume.py`, both preregistrations, this report | `R3_ARCHIVE_EXACT_CENSUS=454:391:63`, `PROPER_OPEN_ARCHIVE_EXACT_CENSUS=574:490:84`, probe |
| Producer overclaimed fixture coverage of production custody | All fixtures labeled pure/parser-level in both selfchecks, both preregistrations, the preflight report, and §7.2 | docs + fixture JSON `fixture_realism` field | explicit rehearsal-debt statements |
| (self-found) witness replay byte-compare unsatisfiable against 3-copy archived SB | Appended-copy law `archived == produced * 3` in driver and classifier; node-SB stack census; fixtures | `resume_recursor.py`, `classify_resume.py` | §3 probe; `ARCHIVED_SB_TRIPLE_DECOMPOSITION_CONTROLS_PASS`, `WITNESS_SB_FULL_ARCHIVE_SUBMISSION_REJECTED` |

## 9. Session evidence

Local preflight evidence is preserved under the packet's `preflight/`
directory.  The frozen source archive replayed cleanly (sidecar hash,
23-file-only-member census, 22/22 embedded-manifest verification from a
fresh extraction).  The R1 packet directory, the R1 report, and every
canonical file are unmodified; this packet directory and this report are
the only additions, plus the bounded `/tmp` scratch trees named above.

Report-body SHA-256 (all preceding bytes, including the newline immediately before this line): fbefb5011f91274f00ebe75b472b12cf1422da7f487d66b858f37aac678dd6c0
