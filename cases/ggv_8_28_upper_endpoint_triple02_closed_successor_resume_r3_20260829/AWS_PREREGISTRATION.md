# TRIPLE02 node-1 closed-successor resume: AWS preregistration R3

Date: 2026-08-29 (packet authored 2026-08-28)

Status: `SOURCE_READY_AWS_NOT_AUTHORIZED`

No AWS launch is authorized by this document.  The only next action this
packet licenses is a hostile source review by a different model; R3 itself
does not authorize even a disposable rehearsal.  After that review passes,
a disposable-instance rehearsal (below, extended with the R2 review's four
items) and a separate coordinator `GO` are both mandatory before any
pilot.

## Exact scope

This packet computes only on the TRIPLE02 node-1 closed successor
`V(I_node1 + (Delta_node1))` over `R = Q[q0,q2,c4,c6]` with `dp` order, by
the frozen r5 finite chart recursion with global node numbering starting at
node 2 and at most 6 new nodes.  It does not touch the settled node-1 proper
open, the whole TRIPLE02 stratum, any other component, the ambient endpoint
problem, or `jc2-lean`.  The mathematical terminal markers are exactly the
four preregistered classifications in `PREREGISTRATION.md`; everything else
is `CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT`.

## Frozen inherited inputs

| artifact | SHA-256 |
|---|---|
| R3 terminal archive `cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r3_20260828/custody/terminals/ggv_endpoint_complement_triple02_r3_20260828T175423Z_i0f089.terminal.tar.gz` (exact census 454 = 391 files + 63 dirs) | `e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1` |
| Reviewed proper-open R5 terminal archive `cases/ggv_8_28_upper_endpoint_triple02_proper_open_resume_r1_20260828/custody/terminals/ggv_triple02_proper_open_resume_r5_20260828T233745Z_r6d.terminal.tar.gz` (exact census 574 = 490 files + 84 dirs) | `4b8ffc1c16828b22b2e76a3aa92a25e8c1f472190a708f30a7b71ba952cbef7e` |
| Frozen r5 recursor `cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r5_20260828/recurse_component.py` | `d679a4d7fb4bf2619fbb3ff47ea6f386ba1c75fdc477276cabf3bec8a2b2cd90` |
| Frozen transcript gate `cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r5_20260828/transcript_gate.py` | `0e0efd5ada59039a373a731038f2f88a3794b376b208879c2459bff97d0e7316` |

The preparer verifies both archive hashes AND the exact member censuses
above as hard gates, performs a complete member safety census (no links,
devices, specials, absolute paths, traversal, or duplicate names), requires
a unique exact path and pinned hash for every consumed member, and refuses
to extract the node-1 open-route products
(`NODE_001_OPEN_SAT_STANDARD_BASIS.txt`, `saturation.sing`).  The archived
node-1 saturation record must read cap 900 s, rc 1, `timed_out: true`, with
the exact six-marker prefix and no completion marker, and stays
`TIMEOUT_NO_VERDICT`.  From the proper-open archive only
`output/VERDICT.txt`, `output/SUMMARY.json`, and
`custody/CANDIDATE_MATHEMATICAL_VERDICT.txt` are extracted, all of which
must read `EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY` with scope
`TRIPLE02_NODE1_D_DELTA_ONLY`; they are routing provenance only.

## One-job binding (C2 repair)

Launch identity is a triple: `JOB_STAMP` (`YYYYMMDDTHHMMSSZ`), a **nonempty
schema-checked nonce** `JOB_NONCE` (`^[a-z0-9]{8,32}$`), and
`JOB_TAG = ggv_triple02_closed_successor_resume_r3_<STAMP>_<NONCE>` (exact
composition enforced by the launcher, the contract, the supervisor, the
worker, every stage runner, and the classifier; R3 additionally enforces
the exact stamp shape inside `require_job_tag` itself, so a direct
supervisor entry cannot use a malformed stamp).

The launcher acquires the atomic namespace lease (`mkdir $JOB_ROOT`),
verifies its own bytes against the charged `LAUNCH_MANIFEST.sha256`,
installs a read-only copy of itself at `$JOB_ROOT/launch_preflight_copy.sh`,
and banks the content-addressed `LEASE.json` (+ `LEASE.sha256`) binding job
tag, nonce, source-archive hash, launcher hash, launch-manifest hash, and
launcher PID/start time.  Direct supervisor entry verifies the same lease
and takes an atomic supervisor sub-lease (`mkdir $JOB_ROOT/.supervisor_lease`)
or fails closed.  The worker re-verifies the lease and the launcher copy.

Every Singular stage runs through `run_singular_stage.py`, which before
launch re-verifies: job tag and nonce against its environment, the exact
source-archive bytes, the exact Singular binary bytes (digest recorded at
worker preflight in `custody/singular_binary.sha256`), the live worker and
supervisor PID identities by start time, and its own inherited PGID/SID;
after launch it requires the Singular child to share PGID/SID/uid/cgroup
with the runner.  The stage identity record carries job tag, nonce, lease
hash, source hash, binary digest, argv, cap, and the supervisor/worker/
runner/child identities with start times and cgroups; the stage result
record repeats the binding and hashes the identity record.  The driver
verifies each result's binding as it runs and banks per-stage result-record
hashes into its summary.

The independent classifier **regenerates every dynamic script** (witness
replay, reduce, every rank size, saturation, chart) from the frozen r5
builders plus this packet's validated repaired templates and byte-compares
them against what ran; requires every stage's identity record, its hash
binding, and its equality with this exact job; verifies caps, argv, binary
digest, source hash, PGID/SID/uid/cgroup consistency; and closes every
production directory over an exact expected artifact set (a timed-out final
stage's Singular write set is the only optional remainder).  Bounded
no-verdicts are re-derived from the stage evidence (which stage timed out,
where the reverse search exhausted, how many nodes completed) and must
equal the driver's recorded reason and exact remainder
generators/hashes/bound.  R3 adds three exact laws in both the driver and
the classifier: the runner's captured stdout must be exactly the three
`SINGULAR_STAGE_*` lines consistent with the verified result record and
its stderr must be empty (O-N2); the identity record's key set is censused
exactly (O-N6); and each node standard basis must be exactly one identical
single-line append per completed header-writing stage (O-N1; the archived
node-1 write confirms `string(NODE_SB)` is newline-free, and a doubled
file is refused).

## Decision record and late authority (C1 repair; R3 O-B1 archive binding)

After the classifier passes, the worker banks one content-addressed
decision record `custody/DECISION_RECORD.json` (+ sidecar).  The record's
candidate is **derived** (production `VERDICT.txt` and classifier
`VERDICT.txt` must be equal and allowlisted; it is never an argument) and
the record binds: job tag, nonce, source-archive hash, exact Singular
binary digest, containment mode (must be `systemd_scope`), lease hash,
launcher hash, worker and supervisor identities and identity-file hashes,
production and classifier summary/verdict hashes, and the complete worker
artifact-manifest hash.

The supervisor banks the sticky fault-latch state in
`custody/FAULT_LATCHES_PRE_ARCHIVE.json`, freezes the terminal archive
(complete manifest over regular files AND directories via
`custody/TERMINAL_DIRS.list`, independent replay, fresh private
extraction) and installs it with a no-replace hard link.  The late
terminal authority then authenticates the **frozen archive bytes** (R3,
O-B1): it re-hashes the installed archive against the charged digest,
re-runs the complete member-safety, embedded-manifest, and directory
censuses from the archive bytes alone, requires the fresh extraction to be
byte-identical member-for-member (a same-uid edit, deletion, replacement,
symlink, or archive/extraction mix-and-match after the freeze fails
closed), and reads every decision input from the archive bytes held in
memory: it re-derives the candidate from the archived decision record plus
the archived production and classifier verdicts and replays every recorded
equality (lease — also against the live lease file, identities, summary
and verdict hashes, artifact manifest, Singular digest, five-property
runtime limits, containment mode, fault latches — refusing any regression
against the live flags and any worker-rc disagreement).  The live
candidate file is never read at decision time; the supervisor's decision
command has no live candidate argument at all.  The public
`TERMINAL.marker` is published with a no-replace hard link and contains
three lines: the classification, the terminal-archive SHA-256, and the
decision-record SHA-256 (or `NONE` where no archive/decision exists); a
mathematical first line can appear only if the decision re-authenticated
exactly the archive digest on the second line.  The post-freeze
`FINALIZATION_LATCHES.txt` binds the job tag and archive digest and
carries a `FINALIZATION_LATCHES.sha256` sidecar.  All custody failures
remain `CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT` with sticky latches.

## Containment (C3 repair)

- The worker runs inside a transient user systemd scope with
  `RuntimeMaxSec=21600` (independent deadline enforced by the user manager,
  which survives supervisor death), `KillMode=control-group`,
  `MemoryMax=274877906944`, `TasksMax=512`, and `MemorySwapMax=0`.  The
  probe requires every property; the supervisor then reads back
  `KillMode/RuntimeMaxUSec/MemoryMax/TasksMax/MemorySwapMax` from the live
  scope through the contract's `runtime-limits-record` predicate — which
  the late decision authority replays — and latches
  `systemd_runtime_fault` unless **all five** properties carry their exact
  charged values, with `RuntimeMaxUSec` equal to exactly 21600 s (accepted
  renderings `6h`/`21600s`/`21600000000us`; any other honest rendering
  downgrades, never promotes, until the rehearsal captures the live shape).
- Supervisor-death containment: a watchdog inside the worker scope polls the
  exact supervisor PID start time every 5 s and kills the whole scope cgroup
  (`systemctl --user kill --kill-whom=all --signal=KILL`) when the
  supervisor is gone; independently, `RuntimeMaxSec` bounds the tree even if
  the watchdog dies with it, and the scope is owned by the external user
  systemd manager, not by the supervisor process.
- **The exact-PGID fallback is NO_VERDICT-only.**  In fallback mode the
  worker refuses to run any Singular stage or production and banks nothing;
  the decision builder refuses to build; and the late authority requires
  `containment_mode == systemd_scope` (recorded, archived, and live) plus a
  verified runtime-limit record for any mathematical terminal.
- Host gates unchanged from the reviewed R1/R5 stack: Amazon EC2 DMI,
  IMDSv2 instance and `CodexJob` tag binding, one pinned core, at most 1 TiB
  RAM, 256 GiB process virtual memory, 64 GiB file size, zero configured
  swap before/during (10 s telemetry, plus scope `memory.current`
  telemetry)/after, stage caps 60 s (controls) / 900 s (witness replay) /
  3600 s (node stages), whole-job 21600 s, sticky TERM/KILL, exact
  PID-start-time custody, tagged orphan censuses, strict `cgroup.procs`
  content parsing.
- Singular normalized-version SHA-256 (random seed normalized):
  `f16fa01f3d3bdb83ac08dc7dbc25ebd84ba147bf3433779a0f5c695cee9ad9ec`;
  `elim.lib` SHA-256
  `cb39b70a6cff9f1bf6b6397b9de3a597f6bb9d91dad468243bed9bfb2552fcd1`; the
  exact Singular binary digest is measured at worker preflight and bound
  into every stage record and the decision record.

## Fixture realism (disclosed)

Every fixture in `generator_selfcheck.py` and `containment_selfcheck.py` is
pure/parser-level: real contract and classifier code driven on synthetic
trees and injected records.  No fixture executes the launcher, supervisor,
stage runner, systemd, or live `/proc` custody paths, and none claims to.
That live behavior is AWS rehearsal debt, discharged only by the rehearsal
below.

## Mandatory disposable-Linux rehearsal (before any pilot)

One disposable EC2 instance on the exact pinned AMI, entered through the
exact charged launcher and source archive, must demonstrate:

1. the real diagnostic and adapter Singular controls plus the complete
   node-1 witness replay, including the triple-copy standard-basis
   comparison, byte comparison of pivots/residual, and confirmation that no
   node-1 saturation/chart stage exists;
2. a real stage-runner timeout with TERM/KILL and current-job identity
   verification (identity/result records present and bound);
3. real same-group, `setsid`, reparented, tagged, and tag-cleared child
   fixtures; final PGID, tag, and cgroup censuses must all be empty;
4. supervisor TERM and forced `SIGKILL` rehearsals proving the external
   scope owner plus in-scope watchdog kill the worker/CAS tree, that
   `RuntimeMaxSec` fires on schedule, and that no mathematical marker can
   appear in either case;
5. launcher starttime/zombie/hung-reap and systemd collected/non-collected
   paths against live `/proc`/`cgroup.procs`;
6. injected candidate swaps before manifesting and after archive
   installation, copied prior-job stage trees, missing/wrong identity
   files, archive regular and empty-directory extras, terminal-marker
   collisions, and final swap/timeout/containment/archive faults; every
   case must yield only a custody no-verdict and no surviving process;
7. the PGID fallback path, demonstrating that production is refused, no
   candidate is banked, and the decision layer refuses promotion;

and, added by the R2 hostile review (§8) and mandatory here:

8. **O-B1 regression**: after `archive-extract-verify` and before
   `terminal`, inject the review's §5 forgery (rewritten verdicts and
   summaries plus a re-run `decision-build`) into the live
   `.terminal_archive_replay.*` extraction and confirm the repaired
   terminal refuses and publishes only a custody no-verdict;
9. **exact systemd read-back**: capture `systemctl --user show` for the
   real worker scope, confirm `RuntimeMaxUSec` equals exactly 21600 s plus
   the other four exact values, record the live rendering, and confirm
   `custody/systemd_runtime_limits.json` records them all with
   `verified: true`;
10. **watchdog degradation**: rehearse supervisor `SIGKILL` with a healthy
    user manager AND with the user manager made unavailable, confirming
    the scope's own `RuntimeMaxSec` still bounds the tree in the second
    case;
11. **runner-log discipline**: capture real `*.runner.stdout.txt` /
    `*.runner.stderr.txt` for a successful stage and a timed-out stage and
    confirm they match the R3 three-line law and empty-stderr law exactly
    (the law is derived from the runner source; the rehearsal confirms the
    live shape).

Also to capture during the rehearsal, since they are cheap once a host
exists: the byte-identity of the witness replay's produced
`NODE_001_STANDARD_BASIS.txt` against the 4,961-byte archived unit (the
single live assumption behind the appended-copy law) and the archived
pivot/residual byte comparisons.

Only after that rehearsal may a bounded node-2 AWS pilot be considered.
Node-2 saturation cost and later chart sizes remain performance
uncertainty, correctly classifiable as bounded no-verdicts.

## Launch integration

The archive-external `aws_launch_preflight.sh` (frozen in
`LAUNCH_MANIFEST.sha256` together with the archive sidecar and this
packet's documents) pins the literal source-archive hash, validates every
member name/type/prefix and the exact 23-file member count before
extraction, verifies itself against the charged launch manifest, installs
the archive read-only, verifies `SOURCE_MANIFEST.sha256`, write-protects
the source tree, installs its own read-only copy, builds the lease, exports
`EXPECTED_SOURCE_ARCHIVE_SHA256` and `JOB_NONCE`, and `exec`s the
supervisor.  The expected launch environment is `SOURCE_ARCHIVE`,
`JOB_ROOT`, `JOB_TAG`, `JOB_STAMP`, `JOB_NONCE`, `CPU_ID`,
`EXPECTED_INSTANCE_ID`, `EXPECTED_HOSTNAME`, `LAUNCH_MANIFEST`.

R3 (O-N5): `LAUNCH_MANIFEST.sha256` no longer lists the producer report,
so the R3 report tables the launch manifest's own hash and the coordinator
charges BOTH values independently: the launch-manifest hash (from the
report) and the report hash (from `REPORT_BINDING.sha256`, written after
the report exactly as the R2 launch manifest was).  No nearby branch,
open-route, or whole-stratum job may be launched from this packet.
