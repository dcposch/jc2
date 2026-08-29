# Hostile review: TRIPLE02 node-1 proper-open resume R5

Date: 2026-08-28
Reviewer: independent Fable 5 hostile lane (launch referee)
Charge: `xmodel/triple02-proper-open-resume-r5-review-request-gpt5-20260828.md`,
SHA-256 `ee02e0f70fd0e6f86d0544979a29749eeb9bec0578d82c6f9392e774aac25c6b`
(verified before reading).

Verdict: **PASS / AWS PILOT AUTHORIZED** — subject, per the charge itself, to
the coordinator's separate `GO`.  All four R4 launch blockers are repaired in
the sealed R5 sources, every repair is enforced by mandatory fail-closed
terminal inputs, the inherited R4 mathematics is byte-identical with unchanged
claim scope, and every negative test I constructed independently was rejected.
One non-blocking custody hardening note is recorded in section 2.

No AWS job, no Singular or other CAS process, and no `jc2-lean` access
occurred in this review.  The producer packet was not modified; this report is
the only file written to the repository.

## 1. Charged inputs: all verified

Every hash charged in the review request replayed exactly:

```text
60f83a1d4e2eae0f974027059bc1cb1e6de8c3fc687b6cce4af4072ab18c2310  custody/ggv_triple02_proper_open_resume_r5_SOURCE.tar.gz
4b5b4c641a40f12a7b873adeafd1afee156f046e5207b8e1cc7b1aa574a504a4  aws_launch_preflight.sh
513051d9807c61d27fb92b18bff14c00b1b438201fbe3e4ac92882e6b319ceda  LAUNCH_MANIFEST.sha256
2cbb4f3af845dfb3a8402779c2bec425de5c7fb7e6112b6c81b0ef371f215676  PREFLIGHT_REPORT.md
2b82cafa902e22221fd4edab74c5e1d8c4dacf9adc9675e9049c9b4dbe622c7f  REPORT_MANIFEST.sha256
7d5e13f1c5874081cd8c13f83d528efbe18c7fcd30691346734aede3ce711509  preflight/R5_CUSTODY_SELFCHECK.json
3e55f6f334c67d4ced74651dd612f174d2ea0cde205698a98e92c2c19a7ef7b9  xmodel/triple02-proper-open-resume-r4-hostile-review-gpt56-20260828.md
```

Root-relative replays: `LAUNCH_MANIFEST.sha256` 7/7 OK,
`REPORT_MANIFEST.sha256` 18/18 OK, `PREREGISTRATION.sha256`,
`SOURCE_ARCHIVE.sha256`, `SOURCE_ARCHIVE_R4_PRESERVED.sha256`,
`R5_CUSTODY_SELFCHECK.sha256`, `HOSTILE_REVIEW_R2.md.sha256`, and the three
R1–R3 lineage sidecars all OK.

## 2. Archive custody and R4→R5 change surface

The R5 archive was inventoried before extraction: exactly 20 unique members,
all regular files, numeric-owner-normalized metadata, no links, devices,
absolute paths, or traversal, all under the three allowed `jc2/cases/...`
prefixes.  A fresh private `/tmp` extraction replayed all 19 embedded
`SOURCE_MANIFEST.sha256` entries, and **every extracted member is
byte-identical to the corresponding live file**.

Extracting the preserved R4 archive
(`d22774d3f6f1607cd8d29428392e5e4d900339e7e6152979290fe6b11113c7d6`, replayed)
and diffing member-by-member confirms the producer's claimed change surface
exactly.  Changed: `aws_supervisor.sh`, `containment_contract.py`,
`containment_selfcheck.py`, `AWS_PREREGISTRATION.md`, `PREREGISTRATION.sha256`,
`README.md`, `SOURCE_MANIFEST.sha256`, `runtime_expectations.env` (only the
preregistration-hash pin line).  Byte-identical: `prepare_resume.py`,
`build_resume.py`, `classify_resume.py`, `generator_selfcheck.py`,
`run_singular_stage.py`, `adapter_selfcheck.sing`, `diagnostic_hostile.sing`,
`aws_job_worker.sh`, `EXPECTED_GENERATED_SCRIPT.sha256`, both frozen R5
dependencies, and the frozen R3 terminal tarball.  No member was added or
removed.  In the contract diff, `MATH_TERMINALS`, `NO_VERDICT`,
`SCOPE_MARKER`, and `WORKER_GATE` are unchanged; the R4 lines removed are
precisely the six-gate `decide_terminal`, the conflated scope/artifact gate,
and the exception-swallowing `signal_exact` — each replaced by something
strictly stronger.

**Custody note (non-blocking).** The live R5 tarball is mode `0600`,
owner-group `dc:wheel`, with no macOS immutable flag, whereas R1–R4 are
`0444`.  The archive is therefore owner-writable in place.  This does not open
a fail-open path: the exact hash is pinned in five independently frozen places
(the charged review request, `SOURCE_ARCHIVE.sha256`, `LAUNCH_MANIFEST.sha256`,
`REPORT_MANIFEST.sha256`, `PREFLIGHT_REPORT.md`), the archive-external
launcher re-verifies the literal hash at launch before extraction
(`aws_launch_preflight.sh` line 16, `set -e`), and the worker re-verifies the
installed copy against `EXPECTED_SOURCE_ARCHIVE_SHA256`.  Any in-place
modification is detected before any use and detection aborts the launch.
Recommended hardening before `GO`: `chmod 444` the R5 tarball to match prior
rounds.

## 3. Inherited mathematics: byte-identical, scope unchanged

- From the **fresh /tmp extraction only**, `prepare_resume.py` on the frozen
  R3 terminal followed by `build_resume.py` regenerated the 11,446-line
  Singular program at exactly
  `f5050f1204f3d990be64f18c5776eb7204f2587273a64a533e6d56d37b49132a`,
  byte-identical (`cmp`) to the live frozen
  `preflight/TRIPLE02_NODE1_PROPER_OPEN_RESUME.sing`.  My builder stdout is
  byte-identical to the frozen `R5_BUILDER_REPLAY.stdout.txt`, including
  `FULL_C4_MATRIX_RECONSTRUCTION_PASS=1` and the zero proper-route
  pure-Delta/closed-successor censuses.
- The frozen R3 terminal archive hashes to the preregistered
  `e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1`, and the
  frozen recursor to
  `d679a4d7fb4bf2619fbb3ff47ea6f386ba1c75fdc477276cabf3bec8a2b2cd90`.
- The preregistration's "Exact scope" section is untouched by the R4→R5 diff;
  only status lines and custody/containment prose changed.  The worker's
  candidate allowlist, the contract's `MATH_TERMINALS`, and the classifier are
  byte-identical to R4.  The only possible mathematical terminals remain
  `EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY` and
  `RING_LEVEL_ENDPOINT_NONZERO_ON_NODE1_PROPER_OPEN_PENDING_NILPOTENCE_RADICAL`,
  both scoped to TRIPLE02 node 1 on `D(Delta)` only.  No complement,
  whole-component, geometric-survivor, or ambient claim is reachable.
- I re-ran `generator_selfcheck.py` from the fresh extraction against my
  regenerated script: rc 0, stdout byte-identical to the frozen
  `R5_GENERATOR_SELFCHECK.stdout.txt`.  I verified in source that the five
  right-transform rejections are **actual value mutations** of the five
  concrete `C` operations in the generated program (identity initialization
  `C[i,i]=1→0`, pivot swap entry zeroed, elimination sign flip,
  open-basis base-change entry zeroed, recorded `CTFILE` entry value replaced
  by `0`), each required to trip the builder validator's
  `FULL_RIGHT_TRANSFORM_CONTRACT_CENSUS`, with a single-anchor census guard.

## 4. R4 blocker 1 — sticky swap/whole-timeout latches: REPAIRED

`aws_supervisor.sh` latches `swap_violation`, `whole_timeout`,
`containment_preflight_failure`, `launcher_reap_failure`, and
`systemd_final_fault` as one-way variables; the post-archive refresh (lines
453–461) can only raise them.  All five are passed to the single terminal
decision, where they are `argparse` `required=True` with strict
`choices=("0","1")`, and `decide_terminal` conjoins their negations with every
other gate.  The R4 counterexample (clean final swap + worker rc 0 after an
observed fault) is now structurally impossible: I replayed it as a CLI fixture
and got `CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT`, exit 3.  Omitting any latch
argument, or passing `2`/`true`/empty, is an argparse error (exit 2), which
the supervisor converts to a forced NO_VERDICT marker.

## 5. R4 blocker 2 — cgroup emptiness by contents: REPAIRED

`parse_cgroup_procs` reads the file text and strictly validates every
non-blank line as an ASCII decimal strictly positive PID; the metadata-size
test is gone (grep census: zero occurrences, and the selfcheck now hard-fails
if the old pattern reappears).  The `cgroup-census` subcommand returns 0 only
on an empty parse, 1 on any PID, and a traceback on malformation or a missing
file; the supervisor maps every non-zero outcome to `systemd_final_fault=1`.
`systemd_empty_gate=1` additionally requires `systemctl show` rc 0 with
literal `ActiveState=inactive` and `Result=success`.  A disappeared cgroup is
accepted only on the explicit collected-unit route — missing cgroup directory
AND `LoadState=not-found` (or show failure) AND prior verified membership AND
bounded launcher reap already clean — and is recorded with a dedicated marker;
every other missing/unreadable/nonempty combination is a fault.  An unreadable
`cgroup.procs` under an existing cgroup directory falls through to the fault
branch, not to the collected route.

## 6. R4 blocker 3 — bounded, identity-bound launcher reap: REPAIRED

The launcher PID and `/proc` start time are captured immediately
(`pid-start`, which also rejects foreign-UID PIDs).  All polling and signals
go through `wait-pid`/`signal-pid`, which revalidate PID + start time + UID on
every touch and raise `PID_IDENTITY_CHANGED_OR_FOREIGN` on drift (exit 2 →
sticky preflight/reap failure).  After TERM/KILL the supervisor polls the
exact identity for at most 10 seconds; the shell builtin `wait` is entered
only when the PID is absent (bash has already internally reaped its own
child; `wait` returns the stored status immediately) or a same-start-time
zombie (reaped instantly).  If the launcher never becomes reapable,
`launcher_reap_failure` stays 1 — a mandatory decision input — and the
supervisor proceeds to a NO_VERDICT terminal instead of blocking.  The R4
unbounded `wait` hang is gone; the monitor loop itself is bounded by the
1,800-second latch, identity failure breaks it immediately, and a missing
worker-identity file is bounded at 20 seconds.  If `pid-start` fails at spawn,
`launcher_identity_gate=0` forces preflight failure and reap failure, and
`worker_rc` stays 125: fail closed.

## 7. R4 blocker 4 — terminal manifest and archive replay: REPAIRED

The pipeline is now: (1) `manifest-build` (rc recorded) walks the frozen
include roots (`source`, `source_archive.tar.gz`, `work`, `custody`, optional
`output`), excludes only the manifest itself, and rejects symlinks and
non-regular members; (2) `manifest-verify` (rc recorded) independently
re-walks the roots and requires **exact census set equality both directions**
plus every hash; (3) `sha256sum -c` replays the same manifest with an
independent tool; (4) the archive is created under a temporary name, listed,
then `archive-extract-verify` extracts it into a fresh private 0700 directory
that must not pre-exist, rejecting duplicate, extra, traversal, absolute,
symlink, hardlink, FIFO, and device members, requiring the embedded manifest's
regular-file census to equal the archive's exactly, and re-verifying every
hash in the extraction; (5) `sha256sum -c` replays the embedded manifest in
the extraction; (6) only then the atomic rename to the final archive name,
outer checksum generation, and outer replay set `archive_ready=1`.  All of
`manifest_generator_rc`, `manifest_replay_rc`, `archive_replay_rc`, and
`archive_ready` are mandatory terminal inputs.  On any failure the temporary
archive and any final-name archive/sidecar are removed, so no
positive-looking artifact survives a downgrade.  Finalization is itself inside
the sticky time/swap contract via the post-archive latch refresh, which
precedes the decision.

## 8. Whole-job containment, descendants, orphans

Both containment modes end with TERM→KILL of the primary boundary plus
`cleanup`, which scans all of `/proc` for the exact PGID and for any same-UID
process carrying the inherited `JOB_TAG` environment, revalidates start time
and UID before every signal, and writes both censuses.  Promotion requires the
cleanup gate, `CONTAINMENT_EMPTY.marker` (which itself requires clean
preflight, reap, systemd, scope, and cleanup gates), and — re-checked
independently inside the decision — both census files parsing as literal
empty JSON lists.  In systemd mode the literal cgroup census is additionally
gated (section 5).  Every abnormal exit path (signals, early guard exits)
runs `emergency_cleanup` (scope kill / exact PGID kill / exact-launcher KILL /
tagged census) before publishing the emergency NO_VERDICT marker.  The stage
runner (unchanged from R4) creates no session, verifies inherited PGID/SID on
itself and on the spawned Singular child, and kills the stage tree
deepest-first with identity revalidation.

## 9. Duplicate launch and lease races

The archive-external launcher requires `[[ ! -e "$JOB_ROOT" ]]` and then
`mkdir -m 0700` under `set -e`: the atomic mkdir is the lease, so exactly one
launcher can create a given JOB_ROOT.  The supervisor independently refuses a
pre-existing terminal marker or terminal archive (exit 70 → emergency
NO_VERDICT), so a crashed-then-relaunched job cannot re-run or double-publish;
it downgrades.  Two same-tag jobs cannot both promote: in systemd mode the
scope unit name collides (second launch's worker fails, nonzero rc); in pgid
mode each job's JOB_TAG census sees the other's processes, kills them, and
both decisions see nonempty censuses — mutual downgrade, which is the safe
direction.  A path census confirms only the supervisor ever writes
`TERMINAL.marker` (emergency path and decision path, both existence-guarded
or ordered); the worker writes only the candidate file, atomically.

## 10. Terminal-path coherence

I walked every terminal path; each ends in exactly one of the two states
"single allowlisted mathematical marker" or "NO_VERDICT/no marker", with no
path that leaves a contradictory positive:

- early guard failure (bad JOB_ROOT/tag, pre-existing artifacts, missing
  worker/contract, nonzero initial swap) → emergency cleanup + NO_VERDICT;
- TERM/INT/HUP at any point → trap → emergency cleanup + NO_VERDICT;
- containment preflight failure (identity, membership, launcher identity,
  poll identity drift) → sticky latch → kill + NO_VERDICT;
- observed swap or whole-timeout at any monitor tick → sticky latch →
  TERM/KILL → NO_VERDICT regardless of any later clean snapshot or rc 0;
- launcher unreapable within 10 s → `launcher_reap_failure=1` → NO_VERDICT
  without blocking;
- worker nonzero rc (including stage timeout 124/137/143 escalations that
  bypass the worker's own no-verdict candidates) → NO_VERDICT;
- worker rc 0 with a no-verdict candidate (`TIMEOUT_NO_VERDICT`,
  `ADAPTER_FAILURE_NO_VERDICT`,
  `REVERSE_CONTAINMENT_SEARCH_EXHAUSTED_NO_VERDICT`) → decision exit 3 →
  NO_VERDICT marker; the archive retains the candidate as evidence, which is
  the designed candidate/promotion separation, not a contradiction;
- nonempty/malformed/missing cgroup census, missing scope record, or
  non-success unit result → `systemd_final_fault=1` → NO_VERDICT;
- manifest generation/replay failure, archive replay failure, outer-checksum
  failure → gate rcs nonzero and/or `archive_ready=0`, final-name artifacts
  removed → NO_VERDICT;
- post-archive time/swap latch raise → NO_VERDICT;
- decision tool crash, missing python, malformed/omitted argument → forced
  NO_VERDICT write; decision-output rename failure → exit 74 → emergency
  NO_VERDICT attempt; if even that write fails, no marker exists and no claim
  is made;
- all gates clean + allowlisted candidate → the candidate string is promoted
  by one same-filesystem atomic rename as the supervisor's final successful
  action (`exit 0` immediately follows; nothing executes after the rename).

Contradiction audit: the custody latch files are written before finalization
and can only *understate* the final latch values recorded in
`FINALIZATION_LATCHES.txt`, so a mathematical marker implies every recorded
latch file is also clean; the archive contains the candidate and gate
evidence but never a promoted marker; and the marker file is the single
publication authority.  No reachable state pairs a mathematical marker with
any recorded fault, and no state pairs two markers.

## 11. Independent negative tests

Producer suite, re-executed by me against the live sources: rc 0, all eleven
PASS lines, and the emitted JSON **byte-identical** to the frozen
`preflight/R5_CUSTODY_SELFCHECK.json`.  Its 13 `late_failure_mutations`
include every R4 blocker fixture demanded by the charge.

My own suite (staged under `/tmp`, 83 fixtures, all passing in the
adversarial sense):

- terminal CLI: positive promotion of both allowlisted candidates; omission
  of each of 11 mandatory arguments → exit 2, no promotion; 18
  malformed-latch values → exit 2; each of the five sticky latches set alone
  → NO_VERDICT; each manifest/archive gate rc nonzero → NO_VERDICT;
  `archive_ready=0`, final swap-total and swap-free nonzero, worker rc 137 →
  NO_VERDICT;
- candidate attacks: missing file, `TIMEOUT_NO_VERDICT`, trailing garbage,
  two-line file, truncated marker, NO_VERDICT-as-candidate → never promoted;
- marker byte-exactness: trailing space on the scope marker, `=0` worker
  gate, missing trailing newline on the containment marker → rejected;
- censuses: nonempty pgid census, malformed JSON, empty file → rejected;
- cgroup census: empty and blank-line files accepted as empty; `4242` →
  exit 1; `0`, `-5`, `0x10`, Arabic-Indic digit line (the `isascii()` guard
  is load-bearing: those pass `isdecimal()` and `int()`), missing file → all
  rejected;
- archive replay: symlink, hardlink, FIFO, `..`-traversal, absolute-path,
  duplicate, extra root member, dropped member (census drift), missing
  embedded manifest, and reuse of an existing replay destination → all
  rejected; positive replay returns the exact entry count;
- manifest: rebuild is stable and self-excluding, in-tree symlink breaks
  build, traversal include rejected;
- reap bound: negative timeout rejected; a never-exiting identity returns
  not-ready in ~0.6 s of a 0.6 s bound (measured); identity drift raises;
  absent PID reports ABSENT/ready.

Also independently rerun from the fresh extraction: the deterministic builder
replay and the full generator/classifier mutation suite (section 3), both
transcript-byte-identical to the frozen R5 records.  `bash -n` passes on
launcher/supervisor/worker and `py_compile` on all nine Python sources, with
bytecode confined to `/tmp`.

## 12. Execution gaps disclosed

This review ran on macOS.  All fixtures above are platform-independent
file/CLI semantics and executed here; the live-`/proc` behaviors (pid-start,
wait-pid on real Linux PIDs, signal revalidation, cgroup reads, systemd
probing) were verified by source inspection plus injected-reader fixtures,
not by live Linux processes.  Two mitigations bound this gap: the R4 review
already exercised the producer's containment suite in its environment, and
the worker re-executes `containment_selfcheck.py` on the actual AWS host and
hard-gates on its PASS line before any production stage.  No Singular
execution of the mathematical program occurred here (none was requested); its
correctness inheritance rests on the unchanged R4-reviewed mathematics and
the byte-identical regeneration in section 3.

## 13. Verdict

**PASS / AWS PILOT AUTHORIZED.**  Every charged R4 blocker is repaired and
fixture-enforced; every terminal path is coherent, replayable, orphan-free,
and fail closed; the mathematical payload is byte-identical at
`f5050f1204f3d990be64f18c5776eb7204f2587273a64a533e6d56d37b49132a` with its
claim scope unchanged and confined to the literal TRIPLE02 node-1 proper-open
endpoint.  Launch remains gated on the coordinator's separate `GO`.
Recommended (non-blocking) before `GO`: restore `0444` permissions on the R5
source tarball (section 2).

Per the launch-referee charge this review writes exactly one repository file
and therefore omits the sidecar the request asks for; the coordinator can
seal it with:

```text
shasum -a 256 xmodel/triple02-proper-open-resume-r5-hostile-review-fable5-20260828.md \
  > xmodel/triple02-proper-open-resume-r5-hostile-review-fable5-20260828.md.sha256
```
