# Proposed one-worker pilot; UNRUN, not an allocation

ROOT owns execution admission and exact-instance retirement. The software
lane has performed no AWS API/SSH action, scientific execution, import, syntax
check or dummy. Its bounded deliverable is an implemented, manual-static-read
pilot plus this ready runtime plan. The script is not production-qualified.

One disposable Ubuntu24.04 c7i.large (2vCPU/4GiB), or one explicitly reassigned
compatible worker. No installer, package upgrade, baked-tree inspection or
mathematics. Existing bash, jq, systemd, util-linux and coreutils are required;
absence fails visibly in the test record. The runner requires Amazon DMI,
exact instance ID, cgroup v2 and the existing ubuntu group, and denies HQ.

Before allocation, ROOT fixes original allocation/setup/test/retirement times,
confirms current regional campaign ownership and quota, and names one returned
ID. Root EBS100GiB retained from launch. Arm a verified independent HQ
exact-ID retirement timer within60seconds, no later than allocation+15minutes.
No extension or automatic successor. Failure leaves original evidence on EBS.

Transfer only these three frozen sources to fresh /opt/jc2-job-pilot, root0444:

- ops/fleet/job.sh -> job.sh
- ops/fleet/tests/job-regression.sh -> job-regression.sh
- ops/fleet/tests/job-probe.sh -> job-probe.sh

Compare all three local/remote hashes from PINS.sha256. The test driver is
started once in a root systemd service named jc2-job-pilot-er20260913a, using
Type=exec, RuntimeMaxSec=600, TimeoutStopSec=5, KillMode=control-group,
Restart=no, MemoryMax=1GiB, MemorySwapMax=0, CPUQuota=80%, TasksMax=128,
LimitFSIZE=64MiB. Persistent outer stdout/stderr go into the staged /opt
directory, never /dev/null. This is the literal argv, with only INSTANCE bound:

```text
/usr/bin/bash /opt/jc2-job-pilot/job-regression.sh INSTANCE er20260913a /opt/jc2-job-pilot/job.sh /opt/jc2-job-pilot/job-probe.sh
```

Each child job is independently bounded, even if the driver dies: <=30seconds
active, <=5seconds TERM/KILL plus <=5seconds final receipt; 256MiB, CPU80%,
Tasks32, zero swap, per-file8MiB. No mathematical source or CAS is imported.
The eight fixed suffixes are success, failure, missing, timeout, killed,
badpin, badpath, symlink. They are not retry slots. Some intentionally fail
admission and create no unit or job directory; the driver checks that scope.

Only a final REGRESSION_PASS with all earlier PASS lines, true driver exit0,
terminal driver/cgroups and matched source pins qualifies the registered suite.
Do not call a killed driver, absent receipt, missing phase or early refusal a
successful empty result. A test failure ends the initial pilot, preserves
all source/log/error/partial bytes, and names the first actual failing check.
Do not patch and repeat on an implicitly renewed clock.

Collection is independently recoverable. Inspect only this exact driver's
unit/cgroup and the eight exact child units. Once terminal, each created job
must have its cgroup absent; collect via job.sh without relaunch. Explicitly
archive /opt/jc2-job-pilot, /opt/jc2-job-regression-er20260913a and the actual
/var/lib/jc2-jobs/er20260913a-SUFFIX directories from that finite list. Include
outer systemd journal/manager outcome even if the driver failed. Never search
the baked campaign tree or another workload. Keep all originals on EBS.

ROOT syncs the EBS archive and parent, pulls to a fresh local custody path,
compares SHA plus a second whole-byte stream under pipefail, and syncs local
archive/parent. Terminate only the registered instance, confirm TERMINATED
and retained volume AVAILABLE, then retire the exact HQ timer. If download
fails, preserve the retained volume and report incomplete local custody.

The suite exercises real controller SIGKILL, timeout/setsid cleanup, unexpected
exit, first exec failure, pre-service bad-pin failure, path/symlink/duplicate
refusal, literal argv, unprivileged log visibility and failed-collection
recovery. It does not claim actual SSH-disconnect, power-loss, OOM, aggregate
disk-quota or malicious-source testing. FIRST and route-specific migration
remain required before scientific use.
