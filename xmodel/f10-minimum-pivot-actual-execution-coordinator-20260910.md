# Minimum-pivot genuine-source run: integer conversion failure, no decision

ROOT coordinator, 2026-09-10. OBSERVED execution failure, not a promoted
mathematical result. One mathematical invocation only. No arithmetic replay
on the coordinator host; coefficient bodies were hash-only throughout.

## Outcome and scientific information

The accepted minimum-pivot solver reached its UNIT-solution extraction path
after the RREF call and pivot-form checks, then failed converting one FLINT
rational numerator from decimal text to a Python integer. The traceback says
the value has 7422 digits, exceeding Python's 4300-digit conversion limit.
It stops at solver.py243, calling rational at218:

    solution[pivot] = rational(reduced[k, columns])
    num = int(pieces[0])

The exact failure is ValueError, not a resource cap or a mathematical
contradiction. This locates a concrete interoperability defect which the
small synthetic suite did not expose. It does NOT establish correctness of
the unexported solution, a completed UNIT witness, a source exclusion, or a
total-runtime improvement. Raw reconstruction, CRT, serialization and the
independent full checker were not completed. There is no candidate.json,
decision.receipt.json, controls.receipt.json or batch.PASS.json.

Actual child2457/PGID2457, original boot4687f1bd-f8c4-45ba-b653-0a4a730d88d0,
startticks59024, ran04:06:29.424180–04:06:55.332414 UTC:
wall25.908244593seconds, sampled group RSS271491072bytes, NORMAL_EXIT with
child/runner returncode1, no signal/resource. stdout0bytes; stderr1097bytes.
Telemetry2ff614da43971af59b73a4c2e4f32251bf548822206292ac30154de7457dbc6d;
stderr0d1d561744fa0a0bdfd1ac6ecd09889a3d0c05b838c841c0da21e44af118c530.
batch.STOP c7a3d77e7c065e1cd2e1c4aa9047e6bb5b54615fa5f19e3baefa58961d13f72c
is dated04:06:55.385859 and retains all8 dispatch records.
The caller's generic error text “cap/failure” is not a CAPRUN resource verdict.

Whole SYSTEM accounting CPU30.750869seconds/MemoryPeak112873472bytes is
separate from CAPRUN's sampled process-group RSS. The differing memory
measures are retained, not reconciled by inventing an equivalence. No billing,
token, available-credit or rolling24hour claim is made.

## Frozen authority, source and preflight

Basis commit0d39df3c9fd69c939a8420c54d03228b9077777d.
Fresh registration box/f10-minimum-pivot-actual-prep-20260910/
dispatch.registration.json SHA553dfe5687e70074d1978da26f8961bd332707b963f69d52b39a5c20101194a4;
ROOT registration card373dbfd9d1207bda79493292e0bbeb48ac3518303914db3047b9491d302dd7e1;
116-pin listfce334f7a0d024e016d524a38788c67880b70b9ce6472670748e1abbafd21a5b.

Accepted17zp solver961e22e64ec768da6d78a886aa987f7ebaf0325b21b87c68e04db88e91778589
and separate actualcallerae3df9a9320e1341b94108e1f8b2349e50dd39b8c77d0384309e2d04c8634def
were used after qualified FIRST generic-runtime acceptance17zq.
The generic caller was not transplanted. Checker122842e5, controls238ae674,
backend7d565299 and source interface siblings were unchanged.
Genuine17x univariate3cfec9aa/receipt0c22af83/acceptance90dcf4f3 unchanged;
actual112/196 endpoint applicability is inherited with its existing bounded
classical-admissibility qualifications, not a new openness theorem.

Exactly14task files+interpreter+100native pins=115supplied; frozenregistration
makes116fixed. All matched remotely04:05:12.721395282 BEFORE launch, including
registration nonsymlink/0444 and externally supplied SHA. Local initial
ROOT-TASK-INPUTS check used the prep cwd instead of campaign root and failed
14relative path opens; the hash output's following command hid its shell
exit code. It was corrected from campaign root before mathematics; this
was an orchestration error, not source drift or a mathematical retry.

Independent ROOT USER worker-stop timer04:28 ACTIVE03:56:32.817734131 BEFORE
instance start03:56:34.610145517. Strict pinned privateSSH used the accepted
82c1f458 hostfile and exact Ed25519 fingerprint; no trust downgrade.
DMI AmazonEC2/id i-08d2a40f272ee9fa2/hostname ip-172-30-0-72, originalboot/ns,
freshremote directory and exact SYSTEM unit absence checked04:04:44.941924722.
No installation, other instance, resize or new mathematical engine.

Profiles unchanged: probes5wall/3CPU/2GiB; dummy5/3/32MiB;
solve600/550/2GiB; check180/170/2GiB; controls300/280/2GiB;
aggregate1200seconds, file16MiB. Original math04:24/task04:27,
ROOTstopby04:26/independentbackup04:28 NEVERRESET.
Remote cwd/home/ubuntu/jc2-f10-minimum-pivot-actual-20260910.
Sole argv /usr/bin/python3 -I -B REMOTE/dispatch_batch.py, NO extraargv.
Exact SYSTEM jc2-f10-minimum-pivot-actual-20260910.service launched
04:06:27.405166585, invocationd862dcc1867744e888d67bd5c549b9af,
Main2120. OuterRuntime1250/TimeoutStop5/controlgroup/Userubuntu,
Memory3GiB/Swap0/Tasks64/File16MiB, emptyLD_LIBRARY_PATH and
OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=1; outercleanup is not a child cap.

## Live controls and independent terminal observation

The SAME launch orchestration captured18principal IDs with full argv,
PPID/PGID/SID, rawstat/startticks and PIDnamespace:
2120;2133/2143;2173/2183;2206/2216;2246/2256;2286/2293;
2319/2329;2357/2367/desc2381;2447/2457.
Nine groups2120,2143,2183,2216,2256,2293,2329,2367,2457.
ROOT-LIVE-LAUNCH.txt SHAd555453306aee8d771c0188976662d27e263105d9909e997a6f6a45ee47e5fe0.
The launch observer finished04:06:37.104031262 with solver live.
ROOT's next independent unit observation was04:10:18.725150801, after actual
failure. That collection delay is not the actual exit time or continuous
monitoring. No later mathematical stages existed in the collected manifest.

Five deliberate authority defects returned ordinary nonzero exits with no
postauthorize sentinel. Valid control returned0 and exact POSTAUTHORIZE
newline. Dummy2367/desc2381/PGID2367 exercised descendant RSS:
wall0.395842128s, sample80068608bytes>33554432, RESOURCE_CAP/rss/runner125,
MATCH→TERM15→MATCH→KILL9, cleanupcomplete and leaderreaped true.
The leader's own exit0 is consistent with a surviving capped descendant.
preflight.PASS e3e2101e2cf7e8429d285517d960e377d4c940d2b3094970fdbe7141f6074f1d.
Normal solver telemetry's unset cleanup/leader_reaped=false is NOT affirmative
reaping evidence; independent process/group/cgroup quietness is separate.

ROOT04:11:06.387542103 independently checked exactSYSTEM Main0/Exec1,
all18originalPIDs absent, all9groups without nonzombie members, exactcgroupabsent,
BEFORE116fixed rehash and75ownedmanifest04:11:06.424252477.
Terminal metadata34343e712d6250da64e05d78ec929970e77cb9d02030e9ea1822ee218629150d;
REMOTE-OWNED.sha256 3b0088ba048b0691381e6c45262adad044edbabd2e48269f3d10eec105f6b33d.

## Material custody failure and successful collection-only recovery

ROOT mistakenly proceeded while SCP session83317 was still copying.
A local hash command lacked set-e; its final date returned0 despite35missing
files. ROOT therefore requested stop04:11:16.961559263 BEFORE full secure
collection, violating the registered stop ordering. SCP exited255/connection
closed. A subsequent fail-closed check found46matched files and29missing.
No payload body had been read. Do not erase this error or claim uninterrupted
copy custody. The original remote75-file manifest and quietness predated it.

Collection-only recovery card2875bae3bc8d0214b7ae52cd7c302aa75e390ba71bad44d69409197cb4a7b311
authorized no mathematics, code changes, installation or rerun. After
positiveSTOPPED04:12:10.816178824 and original04:28backup stillACTIVE, ROOT
restarted only that worker04:12:49.618404627. StrictSSH verified physicalid,
hostname, newboot8f20e389-6d7c-442f-aab6-94a52349ac8c/ns4026531836,
oldunitnotfound/Main0/exactcgroupabsent, then all116originalfixed AND all75
originalowned hashes matched04:13:43.529417267. Reboot observations do not
substitute for the original pre-stop runtime/quietness evidence.

Only29missing files were copied; SCP terminalexit0 in7.118168891seconds.
All75local hashes matched04:13:51.054732811 BEFORE ANY payload intake.
Recoveryremote-pins33152abe7e8d4aba092d6cfea6dbd720116b05cadf0b6f4b5009b01d264da1ed;
local-pins287fbc10adb262712307c97c34796feeee3f813eb764f7710d0e44ba2b9ff853.
ROOT immediately requested stop04:13:51.151529144.
All3ownedworkers positivelySTOPPED04:14:40.368946875 before originalbackup
cancellation/inactive04:15:02.355275892, reconfirmed04:18:12.108074432.
All volumes retained: .72 vol0574e0fa5aed1f5e3, .56 sole-source
vol0eb6450d18ffa89f1 NEVERDELETE/TERMINATE, .63 vol09c6e3133f3442e56.
No active AWS duty/authority remains; old actual paths/clocks are retired.

## Intake and next decision

ROOT read WHOLE traceback, solvertelemetry, solve.dispatch, batchSTOP and
sourcecaller; metadata-only Node reconciliation parses all8authorities/
dispatches/telemetry, preflight and STOP, checks116inputvectors including
registered deliberate defects, exactargv/caps/host/engine/acceptance/streams,
originalclocks, controlsentinels/cleanup and absence of all candidate outputs.
Result313a14cb180b8d1a60ec85de7071243ebff01f7a1124be13582e07e62fedcb73,
generated04:17:48.165. This is metadata consistency, not mathematical replay
or a claim that every large JSON received fresh WHOLE visual inspection.

Selected response: bounded Astra decimal-wire interoperability repair, then
FIRST Fable code/interface review and fresh appropriate regression before
any actual rerun. CPU/RSS/wall/file caps remain unchanged. Disabling a
decimal-conversion safety limit requires explicit scoped justification;
it must not weaken canonical rational checks or assume a parent setting
survives into independently exec'd checker processes.

No automatic rerun/cap increase, separate timing-failure re-review, new general
framework or promotion is authorized by this report. Contact17zr remains an
independent whole-family eliminant route. JC2 remains unresolved.

## OPENS RAISED

NONE new. Existing fullsource certificate decision is still undetermined.
The immediate implementation defect is decimal integer conversion; the
cheapest prospective test is one giant-coefficient roundtrip/mutation under
the reviewed registered AWS harness, followed by source readback if eligible.

## COLLISIONS

Own report target was absent before begin. No corpus scan or other report
claims. This is the first actual minimum-pivot failure packet; earlier full
matrix and maximum-pivot CPU failures remain separate retained evidence.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10420`.
- Body SHA-256:
  `efa91e576f2ec52beb78f2821ad908053f63e0e19dc3aa661d9667f761bd4002`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
