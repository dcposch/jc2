# Fleet access + job rules (for ALL agents: Fable subagents, Sol, Grok)

## HARD RULE (strengthened 2026-08-24 after local swap incident)
Run **all heavy campaign computation on AWS**, never on the local Mac. This
includes Singular/msolve/other CAS jobs, Lean builds, and long or potentially
multi-GB Python exact-algebra replays/enumerations. The Mac is reserved for
editing, orchestration, hashing, process/status checks, and genuinely short,
low-memory validation. If a job's memory or duration is uncertain, ship it to
AWS. Do not use the former `<8 GB` local-Python allowance: several concurrent
"small" jobs can still exhaust the Mac's 32 GB and thrash swap.
New route-specific heavy runners must fail closed unless `uname -s` is
`Linux`, require a nonempty registered job tag, and record `hostname` before
starting the computational payload.  `ops/aws_exact_lane.sh` enforces Linux,
an Amazon EC2 DMI identity, and a nonempty registered lane tag for clients
that use the shared wrapper.

## Inventory

September13 05:28UTC CLOSEOUT: corrected one-service runner regression
[PASSED](../box/execution-reliability-pilot-root-20260913/RESULT.md), nine
registered groups in24.20seconds, no CAS. Worker i-0b881da911e659481 is
TERMINATED; retained100GiB vol-013b5a506f1b7bb03 is AVAILABLE/unattached.
Archive849920bytes was flushed, transferred, hash-checked and independently
whole-byte-compared before termination. Both regional campaign selectors[];
exact HQ USER-manager retirement timer stopped, now not-found/inactive/dead.
No active worker or automatic scientific migration. This supersedes older
inventory snapshots below; newest LIVE STATE still owns subsequent changes.

September13 02:05UTC revalidated CLOSEOUT: V5 i-052458938409563d3 is
TERMINATED; retained100GiB vol-031e6cfa94f277e68 is AVAILABLE/unattached.
Both personal/us-east-1 nonterminal campaign selectors returned[] with
successful exits. Exact HQ retirement timer is not-found/inactive/dead.
[V5 result](../box/f10-mixed-qualification-v5-root-20260913/RESULT.md)
records successful native observation and four metadata stages, then dummy
exit127 at setresuid BEFORE probe execution. No algebra ran. Evidence archive
4710400bytes, SHAd590b9fa9a6a1b920d8c92a0840c6f76633319e106230e245aee772c17f20889,
was durably retained before the01:57 termination request. No worker remains,
no new allocation or volume deletion this turn; retained EBS remains billable.
This supersedes the01:45 live inventory, not its historical registration.

September13 01:45UTC LIVE: V5 i-052458938409563d3 /172.30.0.113,
r7i.2xlarge8vCPU/64GiB, launched01:44:51UTC; root100GiB
vol-031e6cfa94f277e68 DeleteOnTermination=false, termination enabled verified.
Independent HQ exact-ID jc2-mixed-v5-retire-20260913.timer ACTIVE within
seconds, original RETIRE02:10UTC. Qualification TERM02:04:55/STOP02:05UTC.
ROOT owns; no dummy/science yet. Registered corrected limits parser only.
[Registration](../box/f10-mixed-qualification-v5-root-20260913/REGISTRATION.md).
An earlier CLI call rejected an unknown option before API allocation;
fresh selectors remained empty before the ONE actual launch. No old worker
or clock reused; HQ and evidence volumes excluded from termination targets.

September13 01:32UTC CLOSEOUT: V4 i-0404e5972feacb9ba was requested
terminated about01:31:20 after verified local/remote archive SHA and second
whole-byte comparison. Direct API confirms TERMINATED, root100GiB
vol-0d978b14264cc4f52 AVAILABLE/unattached, retained. HQ01:47 retirement
timer stopped only after termination confirmation and verified inactive.
Both personal/us-east-1 nonterminal campaign selectors returned[] with
successful exits by01:32:02UTC. No campaign worker/timer remains active.
[Result](../box/f10-mixed-qualification-v4-root-20260913/RESULT.md): observer
exit1/empty streams means failed qualification despite four metadata stages
passing; no dummy or science. No fifth allocation authorized by this record.
No evidence volume deleted; retained EBS billable. Other infrastructure
untouched. This supersedes the01:25 live inventory below.

September13 01:25UTC LIVE: separately registered V4 worker
i-0404e5972feacb9ba, private172.30.0.92, r7i.2xlarge8vCPU/64GiB,
launched01:19:58UTC. Root100GiB vol-0d978b14264cc4f52 retained from launch;
API termination enabled. Independent HQ exact-ID retirement timer
jc2-mixed-v4-retire-20260913.timer verified ACTIVE, deadline01:47UTC.
Qualification TERM01:41:55/STOP01:42UTC are original and unextended.
Cloud-init is done without errors; no metadata, dummy or science has run yet.
[V4 registration](../box/f10-mixed-qualification-v4-root-20260913/REGISTRATION.md)
supersedes the prior no-worker snapshot, not prior failure conclusions.
ROOT owns this worker; HQ i-0252f535410c26ebc is excluded. No other worker
allocated, no evidence volume deleted. Boot711b1aff-0566-4db6-8438-a48d9d5ee729.

September13 01:06UTC closeout: qualification-v3 worker i-05ceda98fbb668717
(r7i.2xlarge8vCPU/64GiB) launched00:57:44, requested exact-ID termination
about01:03:15 and independently confirmed TERMINATED by01:05:46. Root100GiB
vol-0631318e161fe3a98 is AVAILABLE/unattached, retained. Evidence archive
4f1f4051bf76910d297862e004fc2c382f5e1ee1d8d11ce3b5097cf76593de8e matched
remote/local SHA and a second whole-byte SSH cmp before termination; all
tmpfs evidence is retained. [Closeout](../box/f10-mixed-qualification-v3-root-20260913/RESULT.md):
four metadata stages passed, but the required live process/kernel observation
was missed, so qualification failed; no dummy or science. Original01:20STOP/
01:25RETIRE not extended. HQ timer stopped only after confirmed termination,
then inactive; both regional nonterminal campaign selectors returned[].
No active/idle campaign worker remains, no fourth allocation authorized by
this record. Retained EBS is billable; no volume deletion or unrelated action.

September12 23:29UTC closeout: the ONE qualification-v2 worker
i-0e074c341fc759521 (r7i.2xlarge,8vCPU/64GiB) launched23:08:28;
ROOT requested exact-ID termination23:28:04 after local/remote archive
SHA and whole-byte cmp matched. Direct API confirmed TERMINATED by23:28:51;
100GiB root vol-0476f3604d2003ed5 is AVAILABLE/unattached and retained.
The independent23:30 retirement timer was stopped only after confirmation,
then observed inactive. Both regional nonterminal campaign selectors[] at
23:29 with successful exits. No active or idle campaign worker remains.
[Closeout](../box/f10-mixed-qualification-v2-root-20260912/RESULT.md):
four metadata stages passed; no dummy or science ran before fixed23:25.
No third allocation on unchanged orchestration. Retained EBS remains billable;
other volumes and separately owned infrastructure were untouched.

September12 22:51UTC recheck: both personal/us-east-1 nonterminal campaign
selectors returned[] with successful exits. No worker allocated or needing
termination; retained evidence EBS and separately owned infrastructure were
untouched. This is a scoped instance check, not billing/storage coverage.

September12 22:15--22:16UTC recheck: both personal/us-east-1 nonterminal
campaign selectors, `jc2fleet=1` and `Name=jc2-worker-*`, returned[] with
successful exits across pending/running/stopping/stopped/shutting-down states.
No active or idle campaign worker remains to retain or terminate; no AWS
mutation or new allocation this turn. Prior retained evidence EBS remains
untouched and billable. This is not an all-region or storage/billing audit.

September12 21:41UTC closeout: the ONE mixed-scalar metadata qualification
worker i-0ffb0b24da98f32a8 (r7i.2xlarge,8vCPU/64GiB) launched21:00:16;
ROOT requested termination21:22:38 after local evidence custody. The original
21:25 independent retirement timer fired and found it already TERMINATED.
Direct21:25:28 and21:40 checks confirm termination. Its100GiB root volume
vol-08866d1c6bd6b386e is AVAILABLE/unattached and retained, not deleted.
Both personal/us-east-1 nonterminal campaign selectors were empty in the
successful21:40:43 check. No campaign worker or retirement cap remains live.
The [execution closeout](../box/f10-mixed-qualification-execution-root-20260912/RESULT.md)
records actual metadata fit but incomplete qualification: no dummy or algebra
ran before the original21:20 cutoff. No automatic retry or successor worker.
Local archive custody is verified; retained EBS storage remains billable.
This is not an all-region, exact billing or historical-storage-cost audit.

Operator recheck September12 00:53UTC: fresh personal/us-east-1 queries for
both `jc2fleet=1` and `Name=jc2-worker-*` returned [] successfully across
pending/running/stopping/stopped/shutting-down states. No campaign worker
remains to retain or terminate. No AWS mutation was needed; retained
evidence volumes and separately owned infrastructure were untouched.
Scope is the configured regional campaign fleet, not all regions or storage.

Operator recheck September11, completed by23:55UTC: fresh personal/us-east-1
queries for BOTH jc2fleet=1 and Name=jc2-worker-* returned [] with exit0
across pending/running/stopping/stopped/shutting-down states. No campaign
worker remains to retain or terminate. No AWS mutation or allocation was
needed; retained evidence volumes and separately owned infrastructure were
untouched. This is not an all-region or retained-storage-cost audit.

Operator recheck September11 21:59:22--21:59:24UTC: fresh personal/us-east-1
queries for both `jc2fleet=1` and `Name=jc2-worker-*` returned [] with exit0
across pending/running/stopping/stopped/shutting-down states. No active or
idle campaign worker remains to retain or terminate. No AWS mutation,
allocation, protection change or retained-evidence deletion was needed.
Scope is the configured regional campaign fleet; separately owned
infrastructure and retained volumes were untouched. This check does not
audit other regions or historical volumes.

Operator recheck September11 21:20:53--21:20:55UTC: fresh personal/us-east-1
queries for both `jc2fleet=1` and `Name=jc2-worker-*` returned [] with exit0
across pending/running/stopping/stopped/shutting-down states. No campaign
worker remains to retain or terminate. No AWS mutation, allocation,
protection change or retained-evidence deletion was needed. Scope is the
configured regional campaign fleet; separately owned infrastructure was
untouched. This check does not audit other regions or historical volumes.

Operator recheck September11 20:56UTC: fresh personal/us-east-1 queries for
both `jc2fleet=1` and `Name=jc2-worker-*` returned [] with exit0 across
pending/running/stopping/stopped/shutting-down states. No campaign worker
remains to retain or terminate. No AWS mutation, allocation, protection
change or retained-evidence deletion was needed. Scope is the configured
regional campaign fleet; separately owned infrastructure was untouched.

Operator recheck September11 20:27UTC: fresh personal/us-east-1 queries for
both `jc2fleet=1` and `Name=jc2-worker-*` returned [] with exit0, including
pending/running/stopping/stopped/shutting-down states. No campaign worker
remains to retain or terminate. No AWS mutation, allocation, evidence-volume
deletion or separately owned infrastructure action was needed. Scope is the
configured regional campaign fleet, not an all-region or historical-disk audit.

Operator recheck September11 20:00:18UTC: fresh personal/us-east-1 queries
for both `jc2fleet=1` and `Name=jc2-worker-*` returned [] with exit0 across
pending/running/stopping/stopped/shutting-down states. No active or idle
campaign worker remains; no termination was needed. No AWS mutation or
allocation was made. Retained evidence volumes and separately owned
infrastructure were untouched. Scope is the configured regional campaign
fleet, not an all-region or retained-volume audit.

Operator recheck September11 19:28:13UTC: fresh personal/us-east-1 queries
for both `jc2fleet=1` and `Name=jc2-worker-*` returned [] with exit0 across
pending/running/stopping/stopped/shutting-down states. No active or idle
campaign worker remains to terminate. No allocation, termination, protection
change or retained-volume deletion was needed. Separately owned infrastructure
and retained evidence were untouched. Scope is the configured regional
campaign fleet, not all regions or historical disks.

Operator recheck September11 19:09UTC: fresh personal/us-east-1 queries
for `jc2fleet=1` and `Name=jc2-worker-*` both returned [] with exit0,
including pending/running/stopping/stopped/shutting-down instances. There
are no active or idle campaign workers to terminate. No AWS mutation or
new allocation was made; retained evidence volumes and separately owned
infrastructure were untouched. This is a regional campaign-fleet check,
not an all-region or retained-volume audit.

Operator recheck September11 18:49:04UTC: fresh personal/us-east-1
describe-instances selections for `jc2fleet=1` and `Name=jc2-worker-*`
both returned [] with exit0 across pending/running/stopping/stopped/
shutting-down states. No active or idle campaign worker remains to terminate.
No launch, termination, protection change or volume deletion was performed;
retained evidence and unrelated infrastructure were left untouched. Scope
is the configured regional campaign fleet, not all regions or retained disks.

Operator recheck September11 18:21UTC: separate personal/us-east-1 queries
for `jc2fleet=1` and `Name=jc2-worker-*` both returned [] with exit0,
covering pending/running/stopping/stopped/shutting-down states. No active
or idle campaign worker remains; no further termination was needed under
the renewed operator directive. No launch, protection change, retained EBS/
evidence deletion or separately owned infrastructure action. This is not
an all-region or historical-volume audit.

Operator recheck September11 17:24UTC: personal/us-east-1 queries for both
`jc2fleet=1` and `Name=jc2-worker-*` returned EMPTY for pending/running/
stopping/stopped/shutting-down instances. No active or idle campaign worker
remains, so no additional termination was necessary. The current manual K16
research requires no fleet worker. Retained evidence volumes and separately
owned infrastructure were untouched; this is not an all-region or disk audit.

September11 17:07UTC research closeout: both personal/us-east-1 nonterminal
fleet-tag and worker-name queries again returned EMPTY. No worker was used
or newly allocated for the manual research; no termination or volume action
was needed. Retained evidence and protected infrastructure were untouched.

Operator recheck September11 16:48UTC: personal/us-east-1 queries for both
`jc2fleet=1` and `Name=jc2-worker-*` returned EMPTY across every nonterminal
state. No active or idle campaign worker remains; no additional termination
was necessary. The manual research tasks used no worker. Retained volumes,
evidence and protected infrastructure were untouched; prior recovery records
below retain their exact scope. This is not an all-region or historical-disk audit.

Current September11 16:21UTC: no active or idle campaign workers remain.
Batch-c i-033947c617e8ad0e5 is TERMINATED after both evidence archives were
compared, hash-checked and secured locally and on retained EBS before the
16:15:12 termination request. Root100GiB vol-0854f6d63c84a4d11 is independently
AVAILABLE/unattached. Exact original coordinator retirement timer was checked
and stopped after termination; fresh16:21:15 raw receipt shows inactive/dead
timer/service and EMPTY personal/us-east-1 queries for both jc2fleet=1 and
Name=jc2-worker-* in every nonterminal state. The cumulative recovery records
now cover22 retired workers; this is not a new audit of all historical disks.
No retained EBS/evidence deletion or protected-infrastructure control.
[Batch-c closeout and recovery](../box/caprun-closed-scope-c-execution-root-20260911/RESULT.md).
Allocate no successor automatically; the failed sequencing mechanism requires
reconsideration. Current owners and subsequent decisions belong in notes.md.

Historical September11 batch-c allocation: i-033947c617e8ad0e5 c7i.2xlarge launched
15:54:24UTC for ROOT's active strict-nine setup. Private172.30.0.224,
root100GiB vol-0854f6d63c84a4d11 retained (DeleteOnTermination=false), API
termination protection false. Exact-ID coordinator16:30UTC retirement timer
armed15:54:24.831250914 and independently checked; retire earlier after
secured terminal evidence. No other campaign worker or idle capacity.
Original setup16:12 remains binding; no science authority. See newest notes.

Operator recheck, September11 15:43--15:44 UTC: exact personal/us-east-1
queries for both `jc2fleet=1` and `Name=jc2-worker-*`, including all
pending/running/stopping/stopped/shutting-down states, returned EMPTY.
A regional nonterminal instance-metadata cross-check found only math-hq and
three separately owned formalization instances, not unused campaign workers.
No termination, launch, protection change or volume action was necessary.
Retained evidence and separately owned infrastructure were not modified;
no remote process or filesystem inspection was made. This does not claim a
fresh inspection of historical retained volumes or other AWS regions.

**Ephemeral fleet retirement, 2026-09-10 13:44 UTC:** DC directed termination
of every idle fleet worker after lifting the old policy locks. All nine
remaining jc2fleet=1 instances, including the former 2 TB worker and the three
recently stopped research workers, are now TERMINATED. All nine EBS root
volumes were preserved and independently confirmed AVAILABLE; the 2 TB
worker's instance-store data was archived and compared on its retained EBS
volume before termination. See the [retirement and recovery record](../box/fleet-retirement-20260910T1339/RESULT.md).
Old instance restart/keep instructions are historical. Sole-source
vol-0eb6450d18ffa89f1 remains protected data, now without an instance.
The coordinator and separate formalization infrastructure were untouched.

A subsequent one-batch c7i.xlarge worker i-09de82a596b4a6023 was launched
14:01:55, used for the registered r2 preflights, and TERMINATED after custody
at14:14–14:16. Root vol-0c485cc58dbb6d92e is retained AVAILABLE; no nonterminal
tagged fleet workers remain. [Batch and recovery record](../xmodel/f10-r2-semantic-execution-root-20260910.md).
The installed AWS CLI uses `--enable-api-termination`, not the rejected
`--no-disable-api-termination`; fleet.sh now uses the supported flag.

The subsequent two-refusal diagnostic worker i-0a30e221e2d8b2d29, launched
15:01:12, was TERMINATED at15:22 after terminal custody, complete archive
comparison/sync/download and local hash replay. Root vol-010c7206456e5ff17
is retained AVAILABLE. The15:22:49 tagged-fleet query returned no nonterminal
workers. Eleven retired workers now have their EBS retained; no idle compute
is being kept. [Diagnostic retirement and recovery](../box/f10-r2-map-observer-execution-prep-20260910/RESULT.md).

The cache-corrected preparation worker i-0df0e858f98e614ad launched15:47:10
but reached its16:00 setup cutoff before ROOT completed registration. No
science was installed or run. It was terminated16:00–16:02; root
vol-0d2e61d8edb77ffdd is AVAILABLE and retained. Fresh native metadata was
hash-checked and saved locally first. Twelve workers retired in total;
the16:02:42 tagged-fleet query was empty. [Preparation closeout](../box/f10-r2-semantic-cache-execution-prep-20260910/RESULT.md).
Finish worker-independent deployment preparation before any next allocation.

The prepared semantic6/10 worker i-0f5058733b2e2b130 launched16:16:18 and
completed both tests successfully. After remote/archive comparison, download,
274 local pin checks and fsync, it was terminated16:34. Root100GiB
vol-01cfedb237b01edbb is retained AVAILABLE; tagged nonterminal fleet is empty.
Thirteen workers retired in total, no idle compute retained. Original worker
termination timer closed16:35:15 after confirmation. [Evidence and recovery](../box/f10-r2-semantic-ready-execution-20260910/RESULT.md).

The highest-certificate worker i-05b82c8e457c586ce launched17:17:15,
completed its13-call registered batch in10.53804wall/8.93415CPU seconds,
and was terminated17:30 after archive comparison/download,302 local pin
checks and fsync. Root100GiB vol-036bd8601bfa8db53 is retained AVAILABLE.
Fourteen workers retired in total; the17:43 tagged nonterminal query is empty.
No idle compute is held for review. [Highest batch and recovery](../box/f10-r2-highest-ready-execution-20260910/RESULT.md).

The fullunit worker i-0941baf1a7ff9131b launched17:55:33 and was terminated
18:20:55 after secured evidence. The first initialization refused a ROOT
metadata string/integer mismatch before any preflight/science. A separate
corrected release on the SAME worker kept all original deadlines/caps and
completed the13-call batch in11.74867wall/10.17074CPU seconds. Both attempts
are archived, compared, downloaded and302 local pins verified/fsynced.
Root100GiB vol-014fe0fec618fbc8f independently AVAILABLE/unattached18:21:56.
Fifteen workers retired, EBS retained; no idle worker held for review.
[Fullunit batch and recovery](../box/f10-r2-fullunit-ready-typefix-execution-20260910/RESULT.md).

Operator recheck, September10 20:48 UTC: the exact personal/us-east-1
tagged nonterminal fleet query again returned EMPTY. No additional
worker termination or evidence/volume deletion was needed. The active model
review uses the coordinator, not an allocated fleet worker.

Earlier19:45 checkpoint: the exact personal/us-east-1
jc2fleet=1 query for pending/running/stopping/stopped/shutting-down workers
again returned an empty list. No further termination was necessary, and no
EBS or evidence was deleted. The coordinator and protected infrastructure
were not inspected or controlled by this fleet query.

Fresh operator checkpoint, 2026-09-10 17:08 UTC: the exact jc2fleet=1 query
for pending/running/stopping/stopped/shutting-down instances again returned
an empty list. The last-batch vol-01cfedb237b01edbb, archive-holding
vol-0be96430c433dfbe2 and sole-source vol-0eb6450d18ffa89f1 were independently
AVAILABLE with no attachments. No additional termination was needed and no
retained volume was deleted. Allocate future workers only for ready work.

Operator checkpoint, September10 21:24 UTC: exactly one tagged worker is
running, i-0d991a2cfbf613ac6 (c7i.xlarge), actively used by ROOT for the
registered contact-Gram batch. No idle workers remain to terminate. Its root
vol-053557174f6dc0652 is retained with DeleteOnTermination=false; original
21:51 UTC automatic termination remains active, with earlier retirement after
secured terminal custody. See the latest LIVE STATE for exact job clocks.
The fifteen earlier workers remain terminated; protected infrastructure and
retained volumes were untouched.

Contact-Gram closeout, September10 21:35 UTC: the sole batch worker
i-0d991a2cfbf613ac6 is TERMINATED after archive comparison/download and309
local hash checks/fsync. Its100GiB rootvol-053557174f6dc0652 is independently
AVAILABLE/unattached. All16campaign workers are terminated with EBS retained;
the tagged nonterminal fleet is empty. No idle worker is held for review.
[Contact-Gram evidence and recovery](../box/f10-contact-gram-execution-prep-root-20260910/RESULT.md).

Operator recheck, September11 01:34 UTC: exact personal/us-east-1 jc2fleet=1
nonterminal query returned EMPTY. All16 previous workers remain retired;
no further termination or data deletion was needed. Current model reviews
run on the coordinator. Future workers are allocated only for ready work.

September11 first-r3-source batch: i-09bac011c7e8b9368 (c7i.2xlarge) launched
01:44:14, actively used by ROOT. The original exact-ID03:11UTC retirement timer
is armed; retire earlier after secured terminal custody. Root100GiB
vol-0d25c29e5d1378a76 has DeleteOnTermination=false. The13-call registered
batch started01:54:32. Earlier16workers remain terminated; no idle capacity.
See box/f10-source-cone-r3-execution-root-20260911/ and newest LIVE STATE.

September11 02:16 UTC closeout: that sole r3 worker i-09bac011c7e8b9368
is now TERMINATED, after its producer hit the original900second wall cap
without a completed baseline. Evidence was archived/compared/downloaded,
218 local pins checked and fsynced before the02:15:37 termination request.
Root100GiB vol-0d25c29e5d1378a76 is AVAILABLE/unattached and retained.
All17 campaign workers are retired; the fresh tagged nonterminal query is
EMPTY. No worker is held for review. No volume/evidence deletion or protected
infrastructure action. [Timeout and recovery](../box/f10-source-cone-r3-execution-root-20260911/RESULT.md).

Operator recheck, September11 02:46 UTC: exact personal/us-east-1
jc2fleet=1 query for pending/running/stopping/stopped/shutting-down instances
returned EMPTY again. All17 campaign workers remain retired. No additional
termination, volume deletion or protected-infrastructure action was needed.
There is no worker being held for the pending design/review work.

Operator recheck, September11 03:29:27 UTC: the exact personal/us-east-1
jc2fleet=1 query for pending/running/stopping/stopped/shutting-down instances
returned EMPTY. All17 campaign workers remain retired; no additional
termination was necessary. No retained evidence volume was deleted or
modified, and no protected infrastructure was inspected or controlled.
The three active Astra tasks are worker-independent static preparation.
Allocate a future worker only when its reviewed registered batch is ready.

Operator recheck, September11 03:58:18 UTC: the exact personal/us-east-1
jc2fleet=1 query for pending/running/stopping/stopped/shutting-down instances
returned EMPTY. No active or idle fleet worker remains, and no additional
termination was necessary. The17-worker retirement/recovery records above
remain authoritative; no EBS volume or evidence was deleted or modified.
Current model reviews do not require a fleet worker. Protected infrastructure
was not inspected or controlled; allocate only for ready registered work.

Operator recheck, September11 04:29 UTC: the exact personal/us-east-1
jc2fleet=1 query for pending/running/stopping/stopped/shutting-down instances
returned EMPTY. No active or idle fleet worker remains; no additional
termination was necessary. All17 prior workers remain retired according to
the custody/recovery records above. No EBS/evidence deletion or protected
infrastructure action. Current Python documentary review and offline ROOT
registration preparation require no AWS worker. Allocate only for ready work.

September11 direct-row batch: i-031b57c489417e1d1 (c7i.2xlarge) launched
04:48:33UTC for ROOT's ready registered source observation. Exact-ID automatic
termination06:16UTC armed04:48:34.095547621, independently checked active and
correct target. Root100GiB vol-0d500f329b88c6152 has DeleteOnTermination=false;
API termination protection is false. Actively collecting actual metadata,
not held idle for review. Original setup05:08/latestdispatch05:10; retire
earlier after terminal custody. Earlier17workers remain retired. See
box/f10-direct-rows-execution-root-20260911/ and newest LIVE STATE.

Operator check September11 05:02:43 found exactly that one running worker,
i-031b57c489417e1d1, and no idle nonterminal fleet instances. Metadata setup
completed05:02:45 and registered direct-row dispatcher launched05:03:31;
independent05:03:47 observation found its actual producer running. Original
06:16 exact-ID retirement and06:10/06:10:05 science stops remain active; retire
earlier after secured terminal custody. Rootvol-0d500f329b88c6152 remains retained.
No volume deletion or protected-infrastructure action.

September11 direct-row closeout05:15:35: i-031b57c489417e1d1 is TERMINATED
after224local/remote pin checks, full native postcheck, archive comparison,
download and fsync. The producer stopped at its internal100000term guard,
without a baseline; no worker is held for redesign/review. Its100GiB root
vol-0d500f329b88c6152 is AVAILABLE/unattached and retained. All18campaign
workers are retired and the fresh tagged nonterminal fleet is EMPTY.
No EBS/evidence deletion or protected action. [Term-cap and recovery record](../box/f10-direct-rows-execution-root-20260911/RESULT.md).

Operator recheck, September11 05:34:51 UTC: the exact personal/us-east-1
jc2fleet=1 query for pending/running/stopping/stopped/shutting-down instances
returned EMPTY. No active or idle campaign worker remains, and no further
termination was needed. All18 retirement/recovery records above retain their
evidence volumes. No EBS/evidence deletion or protected-infrastructure action.
Current static research and review require no allocated fleet worker.

Operator recheck, September11 06:09:26 UTC: the exact personal/us-east-1
jc2fleet=1 query for pending/running/stopping/stopped/shutting-down instances
returned EMPTY. No active or idle campaign worker remains, so no additional
termination was necessary. All18 retirement records above remain authoritative;
retained evidence volumes and protected infrastructure were not modified.
Source-review preparation requires no allocated worker. Allocate only for
ready registered work, and retire promptly after secured terminal custody.

Read-only preallocation check, September11 06:30:15 UTC: tagged nonterminal
fleet remains EMPTY. Intended c7i.2xlarge image/subnet/key/group are available;
Standard On-Demand quota1920vCPU, delayed account usage84vCPU at06:25 (not an
instantaneous free-capacity claim). No worker allocated or retained for review.
No resource, volume or protected-infrastructure mutation. Snapshot:
box/f10-necessary-rows-preallocation-root-20260911/AWS-READONLY.json.

Operator recheck, September11 06:45 UTC: exact personal/us-east-1 jc2fleet=1
nonterminal query returned EMPTY. No active or idle fleet worker remains and
no additional termination was necessary. Retained volumes and protected
infrastructure were untouched. Next worker requires ready registered work.

September11 necessary-row batch: one c7i.2xlarge i-0de792cdaff6b0682 launched
06:51:13 for ROOT's ready registered work. Exact-ID08:16UTC retirement timer
armed06:51:13.584775326 and independently checked. Root100GiB
vol-0fcc863483b3e06e5 has DeleteOnTermination=false; no idle worker is retained.
Physical metadata collected06:53; native/setup binding in progress under
original07:18 setup cutoff. Retire earlier after secured terminal custody.
Earlier18 workers remain retired; protected volumes/infrastructure untouched.

Necessary-row closeout, September11 07:10UTC: that worker is now TERMINATED.
Its batch stopped at the dummy process-cleanup gate before mathematical
production. ROOT archived/compared/fsynced/downloaded and checked127 terminal
pins plus1226 native pins before termination. Root100GiB
vol-0fcc863483b3e06e5 is AVAILABLE/unattached and retained. All19 workers are
retired; tagged nonterminal fleet EMPTY, all original timers closed. No worker
is held for diagnosis/review. [Evidence and recovery](../box/f10-necessary-rows-execution-root-20260911/RESULT.md).

Operator recheck, September11 07:28UTC: exact personal/us-east-1 jc2fleet=1
query for pending/running/stopping/stopped/shutting-down instances returned
EMPTY. No active or idle fleet worker remains and no additional termination
was needed. All19 retirement records retain their evidence volumes; no disk
or protected-infrastructure action. Static repair/review uses no fleet worker.

Operator recheck, September11 07:49UTC: the exact personal/us-east-1
jc2fleet=1 nonterminal query returned EMPTY. No active or idle fleet workers
remain, so no additional termination was needed. All19 prior retirement
records retain evidence EBS. No disk or protected-infrastructure action.
Current Astra repair and Fable static proof review use no fleet worker.

Operator recheck, September11 08:59UTC: the exact personal/us-east-1
`jc2fleet=1` query for pending/running/stopping/stopped/shutting-down returned
EMPTY at08:59:03.927785813. No active or idle fleet worker remains; no further
termination or volume action was needed. All19 prior workers are retired,
their evidence volumes retained. No worker was allocated or held for the
completed model reviews; protected infrastructure remains outside inspection.

Operator recheck, September11 09:27UTC: the exact personal/us-east-1
`jc2fleet=1` query for pending/running/stopping/stopped/shutting-down returned
EMPTY, observed09:27:04UTC. No active or idle fleet worker remains, so no
additional termination was needed. All19 previous retirements and retained
evidence volumes remain recorded above. No volume deletion or protected
infrastructure inspection/control; current model work needs no fleet worker.

Earlier recheck, September11 08:21UTC: the exact personal/us-east-1
jc2fleet=1 query for pending/running/stopping/stopped/shutting-down instances
returned EMPTY. No active or idle fleet worker remains, so no additional
termination was needed. All19 prior retirement/recovery records retain their
evidence EBS. No disk or protected-infrastructure inspection/control action.
Completed model reviews require no worker; allocate only for ready work.

Latest closeout, September11 12:16UTC: batch-b worker i-07553b89026949246
is TERMINATED after secured archive custody. Its 100GiB root EBS
vol-097211997797395f2 is AVAILABLE/unattached and retained. The fresh exact
personal/us-east-1 jc2fleet=1 nonterminal query returned EMPTY. All21 campaign
workers are retired according to cumulative recovery records; no idle compute
is retained. The batch-b coordinator USER backup timer is inactive/dead after
actual retirement. No volume deletion or protected-infrastructure action.
[Batch-b evidence and recovery](../box/caprun-closed-scope-b-execution-root-20260911/RESULT.md).
The previous strict-nine worker was likewise retired with evidence retained;
see its [setup-failure record](../box/caprun-closed-scope-execution-root-20260911/RESULT.md).

### Historical pre-retirement inventory — recovery references only

The worker entries below describe their former deployments. Their launch,
restart, utilization and retention directions are superseded by the retirement
records above; they are not active assignments or restart authorization.

- **box01** (AWS x8i.16xlarge, 64 vCPU / 1 TiB): instance
  i-029d0899cdb7c1ed1 (profile `personal`), 100 GiB gp3 root;
  ubuntu@54.175.21.169, key ~/.ssh/claude-cli.pem. Runs the deg<=150 farm
  lanes (`~/jc72108`, `farm.log`/`farm2.log`). Current us-east-1 on-demand
  price checked 2026-08-24: ~$7.00/h; verify current pricing before a cost
  decision. Do not stack big-memory jobs without checking live RSS, and do
  not stop it until all active/checkpointed campaign processes are identified.
- **Box02** (AWS x2idn.32xlarge, 128 vCPU / 2 TiB, 3.8 TB local NVMe):
  instance i-010201a5da47795c4 (profile `personal`), 150 GiB gp3 root. IP CHANGES on stop/start —
  resolve with:
    aws ec2 describe-instances --instance-ids i-010201a5da47795c4 \
      --profile personal --query \
      'Reservations[0].Instances[0].PublicIpAddress' --output text
  (current IP also cached in /tmp/box02_ip). Start/stop with
  aws ec2 start-instances / stop-instances. ~$13/h — STOP IT when its
  queue drains (coordinator's call; don't stop it while lanes run).
  After start: `sudo ldconfig` once before msolve.
  Job dir: ~/res32 (screens + stuck7), ~/jc72108 (older Q2 work).
  Current 2026-08-25 boot IP: `34.203.207.55`.
- **Box03** (AWS r6i.16xlarge, 64 vCPU / 512 GiB): instance
  i-0ece0b9a3b4a7512f (profile `personal`), 200 GiB gp3 root, launched 2026-08-14 for the
  3 stuck7 farm big-cores idle since the Box02 cull. Same SG/subnet/key
  as Box02 (claude-ssh / subnet-948915c9 / claude-cli), us-east-1a,
  IP CHANGES on stop/start — resolve like Box02
  (cached in /tmp/box03_ip; currently 54.167.215.189). ~$4.03/h —
  STOP IT when the stuck7 lanes finish. msolve from Ubuntu apt.
  Job dir: ~/stuck7 (out/ + lanes.log).
  Current 2026-08-25 boot IP: `98.80.65.144` (the older IP in the preceding
  historical sentence is stale).
  **STATUS 2026-09-02 ~10:30Z: STOPPED by the coordinator (idle after the corrected_869 timeout; 964 control done). Restart only for a declared braid/SIROCCO or realization job; IP will change.**
- **r6a** (AWS r6i.4xlarge, 16 vCPU / 128 GiB): instance
  `i-02cb2b4a379ffcc64`, current IP `34.229.212.201`.
- **r6b** (AWS r6i.4xlarge, 16 vCPU / 128 GiB): instance
  `i-0f089e64c378f5da3`, current IP `54.224.45.13`.
- **r6c** (AWS r6i.4xlarge, 16 vCPU / 128 GiB): instance
  `i-040b7a1c2ed72d4cc`, current IP `18.209.172.161`.
- **r6d** (AWS r6i.8xlarge, 32 vCPU / 256 GiB): instance
  `i-07eeaf8ba6f0bc419`, current IP `54.84.212.87`.  Its TD6 environment is
  `/home/ubuntu/venvs/td6` (Python 3.12 / python-flint 0.9.0).

The seven campaign instances total **336 vCPUs when all are running**. A
separate user-owned 16-vCPU formalization instance (`box-lean`) is outside
this campaign's inspection/control scope. Use `sh ops/status.sh`, which
queries only the seven named campaign instance IDs and explicitly excludes
the separate instance.

**Account quotas (DC, 2026-09-02 — the prior 512-vCPU campaign policy cap is
RETIRED; launch instances as needed up to these AWS limits):**

| Family (what counts)                           | Live use | AWS quota | Headroom |
|------------------------------------------------|----------|-----------|----------|
| Standard (r6i: Box03 + box-lean + stopped r6*) |       80 |     1,920 |    1,840 |
| X (x8i box01 + stopped Box02)                  |       64 |       548 |      484 |
| Combined running (at directive time)            |      144 |       n/a |        — |

Standing directive: keep current instances fully utilized before adding
more; stop idle paid capacity as always; new instances follow the same
registration, telemetry, and kill-safety rules as the existing fleet.

Do not inspect, stop, retag, or repurpose the separate formalization
instance. The coordinator may add smaller workers of at most 1 TiB
RAM, or replace an audited idle instance, when independent lanes benefit from
job-level parallelism; stop/replace only after every live process and output
has been identified and preserved. The four `r6*` nodes were resized/restarted
on 2026-08-28. Their public IPs change on stop/start; resolve from the instance
IDs before use. Do not stop or repurpose one until its exact live processes and
output custody are audited.
- **ultramem** (GCP): RETIRED 2026-08-16 per DC (AWS-only policy).
  Instance stopped/terminated; two disks remain in dclanker (jc-b 200G,
  ultramem-1 100G, ~$15-30/mo) holding old run outputs — deletion is
  DC's call, not the loop's.

## SG auto-update (2026-08-20)
DC's local public IP drifts (three ssh-breaking incidents 2026-08-19,
latest 149.22.81.x -> 149.88.22.138). Fix: `ops/sg_autoupdate.sh` keeps
the current IP authorized for port 22 on the fleet security group
sg-09ffa8932558f0a79 (profile `personal`).
- Usage: `ops/sg_autoupdate.sh` — no args. Idempotent, safe every tick,
  exactly one status line: "SG: current" (no change), "SG: added
  <ip>/32 (pruned ...)", or "SG: ip-lookup failed (no change)". Exit
  nonzero ONLY on AWS CLI errors.
- CONSERVATIVE PRUNE POLICY: after adding a new IP it removes ONLY
  stale /32 rules inside the two known personal ranges 149.22.81.* and
  149.88.22.*. It NEVER touches 69.181.195.82/32 or any rule outside
  those ranges — other rules may be intentional. If DC's ISP moves to a
  new range, add it to PRUNE_RE in the script (old-range stragglers are
  pruned on the next drift, not before).
- STANDING INSTRUCTION (all agents): on ANY ssh timeout to a fleet box,
  run `ops/sg_autoupdate.sh` once BEFORE diagnosing further — IP drift
  is the most common cause. If it prints "SG: added ...", retry the ssh;
  only then escalate to instance/network debugging.

## Run conventions (remote)
- The minimal process-control recipe below is for legacy screening only; it is
  not evidence-grade because it omits the full metadata ledger. Launch every
  such lane orphan-safe and self-recording:
    nohup sh -c "timeout 43200 msolve -g 2 -t 8 -f X.ms -o out/X.out; \
      echo \"LANE X: rc=\$? size=\$(wc -c < out/X.out | tr -d ' ') \
      \$(date +%H:%M)\" >> lanes.log" >/dev/null 2>&1 &
- For evidentiary work, use a route-specific hardened wrapper that enforces the
  characteristic-zero caveat and records every field in the metadata rule
  below. Do not promote output from the minimal recipe.
- 0-byte .out = still running or timeout (check lanes.log rc), NEVER
  read it as a verdict (R6 §19.2 hygiene).
- Ship work as files via scp (scp-script pattern), not long inline ssh
  commands.
- Threads: -t 8 on Box02 (128 cores), -t 2..4 on box01.
- Caps: 43200 s default; raise only with a reason.

## Historical job snapshot (2026-08-13; never live state)

This section is incident provenance only. The newest `LIVE STATE` block in
`notes.md` and direct process checks determine current jobs.
- Box02 ~/res32: 6 nolog screens (DECISIVE for residue-A), 4 plain/ctl0
  screens, 3 stuck7 farm cores; lanes.log self-records.
- Box02 ~/jc72108 (2026-08-19 restart): 3 ROW22R-B2 decisive reduced
  systems (directionb_row22red p105337/p105673/p200257), msolve 0.10.1,
  -t 32, -v2 telemetry, 48h caps expire 2026-08-21 06:46Z; lanes.log
  self-records. IP 35.175.192.141 this boot (/tmp/box02_ip).
- box01: farm lanes (13 EMPTYs banked so far).
- ultramem: sat23 (r1_23sat).
- Box03 ~/stuck7 (2026-08-14): 3 stuck7 big-cores (12_33 c10.RED,
  6_15 c1.RED, 6_15 c2.q), 48h cap, lanes.log self-records.

## Version caveat (2026-08-14)
Box03 runs apt msolve 0.6.5 (not the campaign-standard 0.10.1). Any
verdict produced there is SCREENING-TIER until re-confirmed on a
0.10.1 box (Box02 post-drain) — record the version in every AUDIT
citation of a Box03 result. Rationale: our hazard ledger is calibrated
to 0.10.1; 0.6.5 may lack fixes or carry different bugs.

## Characteristic-zero `-g` caveat (2026-08-23)
In msolve 0.10.1, a characteristic-zero `-g` run whose first machine-prime
basis is `[1]` may take a unit-basis short circuit before CRT/rational
reconstruction even though the output header repeats characteristic 0.
Therefore:
- a char-0-header `[1]` is `FIRST-PRIME-EMPTY` trace evidence, never a Q
  verdict;
- a successful char-0 non-unit output has continued through rational
  reconstruction and is a Q-level nonemptiness result within engine trust;
- finitely many modular `[1]` results do not certify characteristic-zero
  emptiness without an effective prime bound or a reconstructed exact
  cofactor;
- theorem-tier emptiness requires an independently verified identity
  `1 = sum h_i f_i` (or an equivalent exact rational certificate);
- every hardened probe lane sets and records `--random-seed` (default 0,
  overridable through `MSOLVE_SEED`), plus input hash, input characteristic,
  msolve version, host, UTC start, and, when verbose output exposes it, the
  initial prime.

## Telemetry
- ops/lane_eta.py (INTERNAL TOOLING, UNREVIEWED): msolve -v2 lane telemetry
  reader — `python3 ops/lane_eta.py --status lane.v2log` (phase / F4 rounds /
  matrix trajectory / honest NO-ETA fallback), `--compare log1 log2`
  (cross-prime divergence check), `--gates` (parse-completeness over
  ops/telemetry_samples/). -v2 goes to STDERR: launch lanes with
  `msolve -v 2 ... 2> lane.v2log`. Read-only — safe on live lanes.

## Local CAS etiquette (superseded 2026-08-24)
Do not run campaign CAS locally. Ship even exploratory Singular/Maple/etc.
jobs to AWS. If a trivial local parser/version check is ever unavoidable, it
must be batch-only with browsers disabled (`ESINGULAR_BROWSER=cat`,
`BROWSER=cat`; never interactive `help`).
