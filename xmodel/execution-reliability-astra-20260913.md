# Execution reliability: one-service durable batch pilot

September13,2026; Astra software lane. IMPLEMENTED / MANUAL-STATIC-READ /
INTERNAL-UNREVIEWED / RUNTIME-UNTESTED. No mathematical claim or JC2 advance
is asserted. The smallest next gate is the one-worker no-CAS regression, not
another interactive qualification attempt.

## Outcome and causal target

The first implementation slice is four new files: `ops/fleet/job.sh`,
`ops/fleet/JOB.md`, `ops/fleet/tests/job-probe.sh`, and
`ops/fleet/tests/job-regression.sh`. It is opt-in; no existing caller migrated.
The changed source pins and exact proposed execution plan are in
`box/execution-reliability-astra-20260913/PINS.sha256` and `TEST-PLAN.md`.

V6 actually passed metadata but missed its separately bound dummy admission
while ROOT composed another launch call. V5 reached its dummy and failed at
the root-to-setpriv credential transition before probe execution. Those are
different observed failures. This patch removes those two architectural
interfaces for newly registered clients: a single systemd launch sequences
all predeclared phases, and systemd directly creates a nonroot service.
It does not claim to have repaired or qualified the old F10 science harness.

The script uses one pinned root-owned bundle and one actual systemd cgroup.
The manifest contains argv arrays, expected exits and finite limits; there is
no eval or implicit shell expansion. The worker's exact DMI identity and an
explicit HQ deny precede job creation. Tag admission is no-overwrite. A phase
begins only after the actual controller has recorded its PID/cgroup, kernel
CPU/memory/task limits, capabilities and rlimits; it checks the principal
kernel caps itself. This replaces the narrow external observer window with
evidence collected by the actual controlled process before any payload.

Systemd owns all descendants, even if a child creates a new session or process
group. A successful phase cannot release its successor while an extra cgroup
member remains. Runtime expiry stops the entire job. The root post-stop hook
records manager-supplied outcome fields even when the main controller could
not run a trap. The official systemd documentation describes both post-stop
execution on startup/runtime failure and the special privilege prefix used
for this small hook; these are documentary support, not a worker runtime
test. [Service documentation](https://raw.githubusercontent.com/systemd/systemd/main/man/systemd.service.xml),
[exit environment documentation](https://raw.githubusercontent.com/systemd/systemd/main/man/systemd.exec.xml).

## Reliability and traceability built into the patch

- Phase argv, start/end, separate stdout/stderr and actual wait exit are
  durable files on EBS. Unexpected exits stop the sequence and surface the
  failing stderr in the controller error log. A missing exit is INCOMPLETE.
- Root-owned manifest, copied sources, runner hash, admission output and raw
  terminal result remain outside the nonroot writable output directory.
- The existing ubuntu group can read diagnostic logs, partial outputs and
  collected archives. `status` is unprivileged and read-only. No account,
  group membership, CLI configuration or user-home setting is changed.
- `collect` requires both terminal manager state and the exact cgroup absent,
  then archives raw evidence including the unit journal. It serializes
  collectors, recovers partial archive/hash publication, and reuses an already
  published archive byte-for-byte. Failed/missing receipts remain visible.
- `stop` names one exact unit. There is no process-name kill, EC2 API call,
  evidence deletion, automatic restart, calendar rebinding or broad cleanup.
  ROOT continues to own exact-instance retirement and retained EBS.

The legacy `dispatch.sh` and user-dirty `fleet.sh` were inspected but are
unchanged. Their hashes still match their initial state. This is not another
layer around that dispatcher: the pilot invokes systemd directly and has no
dependency on its SSH/background or broad-kill mechanics. `run_capped.py`
was inspected only through line220 as a comparison; it is unchanged and is
not a dependency of this pilot.

## Verification scope and remaining software gaps

I whole-read the final four source/document files and checked their explicit
Git diff whitespace scope. I did not execute these scripts, Bash syntax,
jq schema validation, imports, interpreter/CAS tests or dummy payloads on HQ
or elsewhere. There was no AWS API/SSH action. Therefore every runtime claim
remains a design intention until the registered regression actually passes.

The fixture driver covers normal two-phase operation/literal arguments;
exit17 with partial evidence and blocked successor; first exec127; a timeout
with a TERM-ignoring new-session descendant; main-controller SIGKILL; bad-pin
failure before service start; path/symlink/wrong-instance/HQ refusals;
duplicate-tag refusal; unprivileged diagnostic access; repeat collection;
and a real failed collector invocation followed by recovery. Its PASS strings
are code, not observed results. A failed suite preserves the first failure
and stops. No unchanged retry is authorized by this report.

The proposed worker is one c7i.large or explicitly assigned equivalent,
10-minute root test service, independent child caps of <=30seconds active
plus <=10seconds cleanup/receipt, 256MiB, CPU80%, Tasks32 and FSIZE8MiB.
ROOT must register the worker and arm exact-ID retirement with retained EBS
before testing. The explicit stage, command, finite tag list, evidence paths,
collection procedure and stop/retirement ownership are in TEST-PLAN.md.

Important limitations remain: per-file size is not aggregate disk quota;
payloads must have separately registered bounded output. Native/library
completeness and mathematical source fidelity are not supplied by this runner.
Its trusted-job isolation is not a hostile-code sandbox. It does not prove
power-loss durability, actual SSH-disconnect recovery, OOM behavior or the
absence of every early filesystem failure. A pre-service crash before minimal
identity metadata exists can still require exact-path manual recovery; no
missing record is interpreted as success. FIRST and route-specific migration
are still required before scientific use.

## Policy, ownership and handoff

Whole COORDINATION.md and FLEET.md were read before implementation; applicable
ancestor/owned-path AGENTS.md checks found none. V5/V6 closeouts and the entire
274-line operator procedure were read. ROOT recorded the first advisory at
04:23UTC; the first explicit clock read retained by this lane was04:25:49UTC.
Design/patch progress was sent before04:40. Original reserve04:55/HARD05:00,
ROOT collector, were never extended. No extra agent or external model was used.
Selected official systemd documentation sections were consulted via web;
freedesktop HTML returned403, so the official repository XML was used. This
was not a whole documentation sweep or a frozen worker-version comparison.

ROOT intentionally amended only the allocation policy during this task.
The initial whole-read bytes remain frozen in the immutable COORDINATION
snapshot with SHA33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597.
I read the new allocation-only lines502–525 and reproduced current policy SHA
517fca6f67f3d705f9b4045e10f9039aaf11bf3280dfd27bb90bf003ee4a3ead.
This is a recorded policy transition, not an assertion that mutable policy
stayed unchanged. All other input pins match their initial observation.

No shared strategy/audit/live-state ledger, mathematical source, protected
repository/workload, user-dirty fleet code or evidence archive was changed.
Only the four announced new source/document paths, this transactional report
and its own metadata directory were written. Source, report and metadata
custody hashes accompany the terminal handoff; the source writers will be
idle before ROOT intake. The next action is different-model FIRST on this
frozen slice, followed by one registered AWS test if its gate permits. Neither
the code nor this report is a successful qualification or a JC2 resolution.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8157`.
- Body SHA-256:
  `307235eae05d164049d84e8125f0b0fa75c59951948790f3c4e57b4832a47a42`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
