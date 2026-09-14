# Coordinator-owned retirement timer binding — minimal admission correction

ROOT producer, first action2026-09-11 09:51:20UTC; original reserve09:59,
HARD10:02UTC, never reset. Own targets absent before writing; basis
0d39df3c9fd69c939a8420c54d03228b9077777d. STATIC UNEXECUTED, pending
different-model DELTA review. No worker, enabled registration or source run.

## Exact inputs and finding

Three inputs hashed before bodies and read WHOLE:
- Old outer admission99cb19a535c8233143db8a4dc68ac0dd93f1ae9b2e68211af9522fb6145d611c:
  box/caprun-closed-scope-admission-astra-20260911/outer-admission.template.sh.
- Actual selected worker-launch template5f0cc7a9146c055b09ca0dd0db79e80cbb38ed64e79d64acfb177bbf0ffce9a4:
  box/caprun-closed-scope-deployment-prep-root-20260911/launch-worker.template.sh.
- Collected FIRSTc8912f2e54cdd207268383abe384fca3e5806743cfd3d17ad0973705c2f9c72d:
  xmodel/caprun-closed-scope-admission-gate-fable5-20260911.md.
  Accepted static scope only. It did not receive the worker launcher.

The old outer runs on the worker and calls systemctl is-active on the
WORKER_STOP_TIMER placeholder using that worker's system-systemd. The actual
launcher runs on the coordinator and creates the retirement timer with
systemd-run --user, invoking aws ec2 terminate-instances for the exact new
instance. Its subsequent systemctl --user is-active also runs on the
coordinator. No worker-local retirement service or AWS credentials are
provided. The old outer therefore asks the wrong systemd manager.

This is an actual deployment-interface mismatch, not an assertion that the
standalone FIRST missed a defect visible in its input packet. In particular,
the FIRST's D only says the outer asserts active status, not that the actual
selected launcher provides a matching worker unit.

## Single executable change

New file:
box/caprun-admission-timer-binding-root-20260911/outer-admission.template.sh
SHA d08e05c66d2c874f00f0485aef929a829217e89488546601c73145b11121fba1.

Exactly ONE executable line is deleted:
systemctl is-active 'JC2_WORKER_STOP_TIMER_PLACEHOLDER'

Four comment lines replace it, requiring ROOT to authenticate the actual
coordinator timer immediately before remote admission and bind its receipt
to the execution card. Full documentary diff was read and confirms no other
change. The holder is unchanged; no literal argv/env/cap/TERM/KILL/CPU origin/
FIFO/namespace/capture/STOP path is altered. All placeholders still disable
this new copy. No fake worker-local timer, unrelated active unit, permissive
fallback or new retirement mechanism is introduced.

## Mandatory external ROOT precondition, not a local proof

Before invoking the worker admission, ROOT must on the coordinator:
1. Confirm the original exact-ID retirement timer is active, its triggered
   service is the expected worker-stop service, and its original UTC deadline
   matches the frozen clock card and is still in the future.
2. Read that triggered service's full ExecStart and compare the entire AWS
   command/profile/region/instance ID to the actual allocated instance. Read
   the timer/unit identities as actual current output, not a filename or an
   old receipt. The existing launch script's arming check is not a substitute
   for this immediately preceding observation.
3. Freeze/hash that observation and bind it with the actual worker ID and
   original deadline in the execution card; do not reset or recreate a timer
   merely to obtain a favorable observation.
4. If any check is absent or fails, do NOT invoke admission. Preserve evidence
   and use existing exact-ID retirement; do not create a surrogate worker unit.

This external coordinator duty is a trusted ROOT release precondition, like
the existing ACL/namespace/exclusive-writer duties. Comments do not implement
or prove the check; no such check has been performed on a future worker.
The remote admission itself still arms its actual absolute TERM/KILL before
holder launch and requires both active. Independent original worker
retirement remains obligatory. A compromised/careless ROOT is not defeated
by this metadata contract, nor was it by the parent.

## Scope and deferred optional changes

The FIRST's stale-file sentinel note is covered by the selected new fresh
tmpfs/no-retry prerequisite; no optional stdout guard patch is selected.
Missing children-file ambiguity stays a conservative observation issue,
not new accepted child-absence proof. The token is public in root0444 code;
authentication rests on the root-only channel/ACL and exclusive writer.
No strict real-time overshoot bound or future-host signal/FIFO/native
qualification follows from static source inspection. Same-PID execution can
be observed only during the separately authorized actual transition, not
manufactured as a past prerequisite.

No source/CAPRUN/dispatcher/probe/mutator modification, test/import/AST/syntax/
dummy/CAS execution of any size, AWS/SSH/process control or agent delegation
was performed for this correction. Administrative text/hash/diff/publication
only. No enabled registration, token or launch is produced.

QUANTITY: whether deleting the wrong-host query while preserving actual
coordinator-side retirement as a mandatory ROOT precondition resolves this
specific deployment mismatch without changing the holder/worker safety
controls. CHEAPEST TEST: different-model review of this exact one-line delta,
the actual launcher and collected FIRST; planning5minutes UNMEASURED, not
runtime clearance. No canonical OPEN id or follow-on authorization.

Own-only COLLISIONS: none. Other reports/sources remain frozen. This corrects
an identified interface; it is not a JC2 result or a new foundation review.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5717`.
- Body SHA-256:
  `4b27f15929204f1ee269909bcd966e4602667e6c611f34263c59649a74398acd`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
