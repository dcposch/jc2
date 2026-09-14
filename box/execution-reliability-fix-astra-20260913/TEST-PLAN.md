# Corrected one-worker pilot — UNRUN; delta FIRST required

This supersedes the prospective runtime plan for the new corrected sources
only. The old plan/report/PINS remain immutable historical bytes. No worker,
syntax/import/test, AWS API or SSH action occurred in this corrective lane.

ROOT owns the gate, one worker and exact-ID retirement. Use one disposable
Ubuntu24.04 c7i.large (2vCPU/4GiB) or one explicitly reassigned equivalent,
with existing bash, jq, systemd, util-linux and coreutils; no installer, baked
campaign tree, mathematics or protected workload is involved. The original
10-minute test service and independent child caps remain unchanged.

## Install exact, immutable sources before invocation

Fresh stage is /opt/jc2-job-pilot-fix. Its ancestors / and /opt and the stage
must be actual directories, root-owned, with no group/other write bits and no
symlink component. Install these three exact files root-owned0444:

| Local source -> installed basename | SHA256 |
|---|---|
| ops/fleet/job.sh -> job.sh | 9c2255c7dcb7c91a8abeb2bd0ea7db30b4d4e8182abdbbd08cc1dc76f33d094d |
| ops/fleet/tests/job-regression.sh -> job-regression.sh | 25181501dae8b2833a1106843a908cd4b19d3e9e5d0ebbb00f408d85c62636e7 |
| ops/fleet/tests/job-probe.sh -> job-probe.sh | 9ec63784453264a67224a5d9355ecd9df3cf9e20b4f7b8b3454e8b6eccab1808 |

ROOT records realpath, stat owner/mode and local/remote SHA for every file,
plus stat/realpath for those three directory ancestors, before launching.
The fixture's generated /opt/jc2-job-regression-erfix20260913a and per-case
bundle directories must likewise be root-owned0755. It creates job.json and
probe.sh as root0444. The runner checks the canonical file path, root0444,
all root-owned nonwritable ancestors, manifest/payload hashes, and an explicit
expected runner hash; it compares the installed hook copy too. These checks
are not an authorization to execute a mutable/unreviewed source. Root remains
a trusted operator and can alter root-owned files; postpins remain mandatory.

## One bounded invocation; no manual phase timing

Before allocation ROOT records fixed original setup/test/retirement times,
current quota and exact campaign ownership, retains100GiB root EBS from
launch, and arms a verified HQ exact-ID retirement timer within60seconds,
no later than allocation+15minutes. No automatic extension or successor.

Root systemd driver unit: jc2-job-pilot-erfix20260913a, Type=exec,
RuntimeMaxSec=600, TimeoutStopSec=5, KillMode=control-group, Restart=no,
MemoryMax=1GiB, MemorySwapMax=0, CPUQuota=80%, TasksMax=128,
LimitFSIZE=64MiB. Persistent outer stdout/stderr go in the installed stage.
Only INSTANCE is mechanically bound in this argv:

```text
/usr/bin/bash /opt/jc2-job-pilot-fix/job-regression.sh INSTANCE erfix20260913a /opt/jc2-job-pilot-fix/job.sh /opt/jc2-job-pilot-fix/job-probe.sh
```

The driver logs directly to its base, without tee. It passes the frozen
runner digest on every start. No model response lies between job phases.
Each child remains independently capped: <=30seconds active plus <=5seconds
TERM/KILL and <=5seconds receipt,256MiB, CPU80%, Tasks32, swap0,
per-file8MiB. There is no aggregate disk quota; this finite no-CAS fixture
writes only bounded small outputs. The nine exact suffixes are success,
expected, failure, missing, timeout, killed, badpin, badpath, symlink.

## Required interpretation

New tests: a completed fast job plus a separately controlled, same-lock
admission-log writer must reject concurrent collection with exact exit70/error,
then collection must contain byte-identical final admission logs after the
writer exits. This deliberately exercises the admission/collection lock with
a controlled writer; it is not a simulated claim of actual SSH/power loss.
The expected17 phase must record actual17 and release a successful successor.

Every refusal must have its exact registered error line, saved exit70,
expected absent/admitted/unchanged directory state, MainPID0 and absent exact
cgroup. Unexpected exit17, first exec127, timeout/new-session descendant,
controller SIGKILL, partial evidence, unprivileged log reading and repeat
archive identity remain checked. Failed collection must have exit153 and the
C-locale file-size-limit diagnostic, then recover without deleting originals.
Actual full UID/GID vectors and FSIZE soft/hard bytes are enforced in source
and retained in live-controls; manager output includes LimitFSIZE/User/Group.

Accept only true driver exit0, final REGRESSION_PASS and every named PASS,
actual terminal driver/child cgroups, unchanged source hashes and complete
evidence. A failed test stops this initial slice with all failures/partials
retained. No unchanged retry or changed clock is authorized. No mathematical
qualification follows even from a passing software regression.

## Terminal evidence and retirement

Inspect only the named driver and nine child units. Preserve exact outer
manager/journal status, direct regression logs, and all created job evidence.
For each created job, collection requires the shared lifecycle lock plus
inactive/failed unit and absent exact cgroup. If the test itself died holding
a controlled writer, its independent outer cap owns that writer; verify the
driver cgroup is absent before retrying collection. Do not relaunch a job.

Explicit archive members are /opt/jc2-job-pilot-fix,
/opt/jc2-job-regression-erfix20260913a and only the actual
/var/lib/jc2-jobs/erfix20260913a-SUFFIX directories from the nine-name list.
No wildcard/baked-tree traversal. ROOT flushes archive/parent, pulls to a
fresh custody path, compares SHA and a second whole-byte stream, and flushes
local archive/parent. Then terminate only the registered ID, verify TERMINATED
and retained EBS AVAILABLE, and stop the exact HQ timer. If transfer fails,
preserve EBS and report incomplete local custody. No volume deletion.

Still untested: actual SSH disconnect, power loss, OOM, aggregate disk quota,
malicious root/host code, native-library completeness and scientific fidelity.
Different-model delta FIRST precedes this pilot; scientific migration is a
separate gate after actual runtime evidence.
