# CAPRUN false-quiet diagnosis

STATIC DIAGNOSIS / NO FIX IMPLEMENTED / NO EXECUTION. First action 2026-09-11 07:11:56 UTC; owned targets absent and all eight input pins matched before fresh WHOLE reads. Original publication reserve 07:25 UTC / hard stop 07:28 UTC remain unchanged. No worker is available or authorized; ROOT reports the worker terminated and its EBS retained.

The named CAPRUN completion predicate can admit NORMAL_EXIT after a non-atomic empty-live sample while a same-PGID descendant remains. The concrete records establish a failed completion/control outcome, not the exact kernel/ps interleaving. The outer caller independently fails closed before science; no mathematical result follows.

## Witnessed outcome and exact control-flow site

The initial eight inputs were all pinned before fresh WHOLE reads. ROOT subsequently authorized one ninth immutable input, the seven-row outer-unit journal; its pin matched before its separate fresh WHOLE read at 07:16:03. No archive, native closure, uncharged source or recovery link was followed.

`dummy.runner-live.json` records CAPRUN PID 8737, outer PGID 8678, and exact expected argv. `dummy.python-live.json` records the actual probe leader PID/PGID 8738, start tick62530, uid/gid65534, NoNewPrivs1 and inherited CPU soft3/hard4. Both use the recorded boot a051707c-61a9-407b-8921-f2a6f240a5cf and PID namespace pid:[4026531836]. The child CAPRUN telemetry names that same leader/start identity.

The four payload events are exactly parent_started(8738), child_ready_ignoring_term(8744), parent_exit_pending(8738), orphan_allocated_64MiB(8744). Parent and child use PGID8738, and the two child records share start tick62558. Frozen probe lines168–182 fork once, make the child ignore TERM, handshake before the parent's `_exit(0)`, wait for parent departure, allocate/touch64MiB, then pause indefinitely. The last event is source-side allocation/touch completion, not an independent CAPRUN peak-RSS measurement.

CAPRUN telemetry ends at07:01:47.130154Z with NORMAL_EXIT, child/runner code0, elapsed0.306042660s, max observed group RSS18,366,464B, no signal, no error, no identity checks, and no TERM/KILL. Its configured dummy limits were wall5s, CPU3soft, RSS33,554,432B and sample0.05s. These are observed telemetry values, not evidence that the true group peak stayed below the RSS cap.

The added journal has the same invocation d5c71b159ca94180ad520fc3f3e0e8e3. It records main exit2 at07:01:47.220592, stop-TERM timeout at07:01:52.237257, and systemd sending SIGKILL to PID8744 at07:01:52.237613. Thus the lingering descendant and the outer cleanup are documented, not inferred merely from an error string. The exact ps/kernel interleaving remains unrecorded.

CAPRUN `sample_group` lines393–428 consumes one `ps -axo pid=,pgid=,rss=,state=` result, skips malformed rows, and excludes rows whose state starts Z. In the main loop, lines861–871 treat the single condition `not sample.live_pids` as sufficient to call `process.wait`, mark the local `reaped=True`, and break. With no termination reason and returncode0, lines934–936 then assign NORMAL_EXIT0. There is no fresh group query between that reap and success. The observed null cleanup and empty identity-check records match this path.

The telemetry field `termination.leader_reaped=false` is NOT evidence that wait failed: it is the initialized cleanup-field value, updated through `record_cleanup` only on cleanup paths. Normal completion sets the separate local `reaped` variable and obtains returncode0 without updating that field. Likewise empty terminal group arrays are defaults here, not a recorded final quiet sample.

## A smallest consistent counter-schedule, not an observed schedule

1. A successful ps query begins its process enumeration before the probe forks child8744; its candidate view does not include that new PID.
2. Before ps reads/classifies leader8738, the fork/handshake completes and the leader exits. The leader is seen only as Z and excluded from live_pids.
3. The returned query therefore has no live row for PGID8738, although child8744 now exists. CAPRUN takes861–871, reaps the leader, and reports its zero exit.
4. The child observes parent departure, completes its allocation and remains paused until the outer service kills it.

This schedule uses only a non-atomic enumeration/state-read view; neither the frozen caller nor retained telemetry provides a linearizable snapshot guarantee. I have not read the installed ps implementation and do not assert it used this exact order. A missed or filtered process row is another unresolved mechanism compatible with the unchecked-empty predicate. Raw final ps output and scan timing are absent. What is established is that a sampled absence was allowed to stand in for lifetime closure; leader termination alone cannot close descendants.

Repeated empty queries or a sleep do not establish atomic closure: successive forks/exits can move the live frontier during each scan. Confirming the leader's death before another scan would close this particular one-fork schedule under additional persistence assumptions, but does not justify the generic arbitrary-descendant contract. Neither is selected as a sound general fix.

## Safety and completeness consequences

The CAPRUN header's claim that completion waits for every live group member is refuted for this execution. RSS enforcement ended prematurely; the normal leader code is valid only as leader status, not group completion. The same sampling-only predicate also appears in `wait_for_group_quiet`467–468 and cleanup decisions489/497, so repairing only the normal-return status string would leave the underlying cleanup doubt.

The outer dispatcher detects the live cgroup at345–349, called at484 before reading dummy telemetry or appending its post record. The absence of dummy.post and later phases is consistent with that barrier. `durable_copy` repeats group_quiet and fails, yielding STOP_CUSTODY_INCOMPLETE at650–654. ROOT's separately reported recovery secured bytes after terminal cleanup; it does not turn the failed dummy into PASS. The original execution remains STOP/NONDECISION, with eight earlier phases recorded and all four scientific phases NOT_RUN. No new custody failure, live worker duty or scientific conclusion is asserted by this diagnosis.

## One selected prospective repair: kernel-backed child-scope completion

The smallest general repair I can justify without assuming descendants stop forking is to replace the **completion authority**, not the RSS sampler: require a ROOT-owned, exclusive per-operation Linux cgroup-v2 leaf containing the registered child and all its descendants, while CAPRUN and the dispatcher stay outside that leaf. Use the kernel's leaf/subtree `cgroup.events` populated predicate as the necessary quiet certificate. Keep existing argv, caps, PGID identity checks, RSS sampling and TERM/KILL sequence. This is a narrow attachment to existing OS containment, not a new supervisor implementation or a source-algebra change.

The exact hypothesis is essential: ROOT creates and identifies the initially empty leaf; places the child there before it can fork/execute untrusted code; denies migration/delegation and external entrants; preserves the leaf identity; and verifies on the selected kernel that populated=0 means no live task in the complete descendant subtree. The minimal placement candidate is the existing trusted child pre-exec stage, before setpriv/workload exec, with placement/identity failure aborting launch; no later migration of a running workload is allowed. This kernel contract and closed spawn/placement arrangement are prospective review obligations, not facts observed on a future worker. The existing shared outer cgroup cannot be used directly for this predicate because its live dispatcher/CAPRUN keep it populated. Moving only the leader after its workload starts is unsound and is not proposed.

Under that attachment, the actual placed leader's membership must be attested before any completion check; an initially empty, never-entered leaf cannot certify a launch. An empty ps live list while populated=1 is **not completion**. Preserve the unreaped leader anchor and continue the same bounded RSS/wall monitor; if RSS crosses the same threshold, perform the same identity-validated TERM/KILL. Normal completion and every cleanup/bootstrap path must require populated=0 before treating the group as quiet or reaping away the sole anchor. `CleanupResult.complete` and terminal telemetry must reflect that kernel check, not just a cached ps sample. Missing/malformed guard data, an identity/placement violation, remaining population after bounded cleanup, or original cutoff exhaustion is RUNNER_FAILURE/STOP with ROOT recovery, never NORMAL_EXIT or successful cleanup. No signal may target a guessed/reused identity.

Why this addresses the counter-schedule: while child8744 lives in the leaf, its population cannot be zero merely because ps omitted it. Once the closed leaf actually has no live member, no internal process can create another descendant; the no-external-entrant rule makes that empty state stable. A sleeping, stopped or transiently omitted member still prevents certification. Escaping the PGID does not produce false completion if it remains in the contained subtree; PGID cleanup failure instead remains bounded STOP for outer recovery. This does not make sampled RSS a hard instantaneous memory limit or remove deadline/cleanup overshoot qualifications.

The repair is **not** a metadata-only native-list adjustment or a drop-in same-hash patch. It needs one focused FIRST instrument/source review of the CAPRUN completion paths and narrow dispatcher/probe authority attachment for separate outer/child cgroup identities, then a new pinned registration. The probe's actual fork/handshake/parent-exit/64MiB/TERM-ignore behavior and strict existing dummy success predicate must remain. No such code or ROOT setup was authored here. If that attachment cannot be made within the retained architecture, the precise remaining GAP is an authoritative closed child-membership predicate; do not substitute repeated ps absence or relax the regression.

## Cheapest discriminating validation, planning only

After that review, ROOT could register one fresh AWS-only preflight-only batch: the same eight early phases, then exactly one unchanged-behavior dummy, no scientific producer/checker/mutator phase. Preserve per-phase wall5s/CPU3soft (4hard inherited per process), dummy RSS32MiB,0.05s sampling and1s TERM grace. Nine nominal child-wall allowances total45s; the nine launched leaders' soft/hard allowances total27/36 CPU-seconds, **not** a joint descendant CPU bound. A120s outer observation/collection planning allowance is an UNMEASURED estimate within, not an increase to, the old outer cap; ROOT must choose actual clocks and retain independent cleanup. It may STOP earlier and has no automatic retry or budget escalation.

Earned success requires the actual parent/child identities and event order, the leader's departure with the child still contained, observed same-group RSS above32MiB, matched TERM and KILL identities/sends, eventual kernel populated=0 plus terminal group/owned-PID evidence, and full durable custody. The added bounded diagnostic should retain the final ps result and kernel-population observations with their times; no favorable scheduling is manufactured or inferred. A pass without an observed false-empty sample validates the ordinary orphan cleanup path, **not** reproduction of the historical interleaving. The static closure argument remains load-bearing. Any non-RSS cap, missing observation, surviving member or quiet-certificate failure is STOP/NONDECISION.

OPEN quantity: one authoritative closed-membership attachment and its focused FIRST, followed only if authorized by one nine-phase AWS discriminator. The historical interleaving itself remains UNKNOWN and need not be guessed to remove the unsound predicate. All new repair costs/feasibility are UNMEASURED. Existing source execution stays closed; no restart, fix implementation, result promotion or follow-on authority is given.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12231`.
- Body SHA-256:
  `4e00960767c88c9cc9f79cff7af285e4bb7058f1d852167a22886dbf3f2570b9`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
