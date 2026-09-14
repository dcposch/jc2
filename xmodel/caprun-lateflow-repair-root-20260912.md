# ROOT late-flow repair: banked primitives, incomplete integration

Date2026-09-12. Basis0d39df3c9fd69c939a8420c54d03228b9077777d.
Selected04:06:18UTC; original reserve04:27/HARD04:30. Publication transaction
opened04:13:12. Author ROOT. Evidence INTERNAL-UNREVIEWED/static code;
lifecycle DISABLED/INCOMPLETE. No mathematical result or runtime qualification.

## Outcome

New versioned code addresses specific defects in Sol v1, but does NOT finish
the complete fixed-code/late-data workflow. Stop the bounded engineering
attempt with explicit gaps; do not silently extend the clock, invite a
confirm-only gate on an incomplete flow, or allocate a worker to debug it.

The source package is box/caprun-lateflow-repair-root-20260912. PINS.json
gives exact input/output hashes and read scopes. ORCHESTRATION-KERNEL.js
defines, but does not call, administrator/session handling, exact hash
readback, LF checksum framing, bounded SSH argv construction, exact raw
property comparison, and admission PID/start/invocation extraction.
receive.template.sh supplies all-five fail-fast absence checks and exclusive
single-file creation. fifo-write.template.sh puts the potentially blocking
FIFO open inside a timed child. Both shell templates remain unbound and
disabled; neither is a complete authority-bearing operation.

## Six-defect disposition

1. Running handle loss: proposed helper stores/announces every known session,
   polls the same handle, distinguishes observation errors from terminal
   exit, and prevents a same-key relaunch. Expired handles have a separate
   collection-only mode with no successor permission. Session-local metadata
   does not replace durable ownership across a coordinator process loss.
2. Checksum framing: real LF separators replace literal backslash-n; direct
   hash readback additionally compares complete exact path/digest census.
3. Stage clobber: every preflight target fails closed; actual writes use dd
   conv=excl with oflag=nofollow. No overwrite/retry. Partial new files remain
   evidence. Trusted stable parent/no concurrent ROOT writer still required.
4. Authentication: exact digest and property equality primitives supplied,
   but concrete receipt/list reads and actual exact retirement-unit queries
   remain uncomposed. A supplied map or source hash is not liveness evidence.
5. Late data: exact admission output is parsed as restricted metadata; no
   script text is rewritten. Fixed late leaf/observer/release consumers are
   NOT implemented. This defect is not solved end-to-end.
6. Blocking: administrator timeout and SSH transport options supplied; FIFO
   redirect happens in a timed bash, not its untimed parent. Complete remote
   writer/transport composition is still missing. No real-time guarantee
   against uninterruptible kernel I/O, no replacement of original caps.

SELF-CONTROLS.md records concrete manual negative traces for all six cases,
including a yielded session, changed digest, occupied first stage target,
unknown pre-admission PID and dead FIFO reader. These were NOT executed
tests. Own static review corrected collection after cutoff and exact marker
grammar before source freeze. No syntax/AST/import/runtime/mock validation
or scientific execution occurred.

## Retained gaps and authority

GAP[FIXED-LATE-CONSUMERS]: full fixed leaf/observer and separately authorized
release, preserving all historical host/holder/namespace/cgroup/registration/
FIFO identity, original-clock and no-writer predicates.

GAP[CONCRETE-COMPOSITION]: actual separate ADMIT/ATTEST/INSTALL/RELEASE
entry points, fresh exact retirement service/timer evidence, bounded exclusive
five-file transfers and readback, unchanged caller/installer orchestration.

GAP[BOUND-QUALIFICATION]: exact new source/native inventory, bound packet,
different-model gate and appropriate scoped controls before new allocation.

GAP[LIVE-LATENCY]: actual complete120-second sequence remains unmeasured;
historical365ms caller/patch/readback timing is not whole-flow evidence.

No accepted scientific, dispatcher, caller, binder or installer algorithm
changed. No old artifact overwritten; nine authority candidates remain
EXPECTED_RUNTIME_OUTPUTS_DO_NOT_PREINSTALL. No new batch, science, remote
helper, holder, AWS allocation or release was selected or executed.

## Scheduling and scope

This bounded systems attempt yields reusable unreviewed primitives, not a
ready deployment. It ends at its original cap; no automatic engineering
successor. Mathematical terminal intake and the highest-value independent
finite-place gate take priority next. Astra's concurrently running six-node
manual task is not an input or promoted result of this report.

No new global mathematical premise, ranking change, source exclusion, rank,
baseline, all-r result or JC2 resolution. This is a scoped systems
micro-round; FULL/BROAD clocks and previous debts remain unchanged.

## Custody and source-read scope

V1 RECIPE and ROOT-INTAKE freshly pin-before-WHOLE read. Historical c leaves
freshly pinned and WHOLE read; earlier exploratory read before that fresh
pin disclosed. Historical d admission only its capture/output tail was
freshly charged here. Other source names in PLAN are design context, not
qualification of a complete executable composition. All four new source/
control artifacts WHOLE-read after final edits; exact hashes in PINS.
No claim of new replay, optimized mode, local dummy or whole-flow review.
Transactional seal authenticates this report's bytes, not code correctness.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5542`.
- Body SHA-256:
  `0861042d97218c6bee79af2297d3685191c51dc5829a5d7ae5f43488dbab1824`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
