# Corrected execution runner: first bounded AWS regression

Verdict: **PASS for the registered no-CAS regression. Engineering tranche
closed.** The corrected opt-in runner actually executed its nine registered
case groups; partial output, failure diagnostics, terminal cleanup and
collection recovery passed. This is not mathematical qualification, migration
of the frozen scientific harness, or a JC2 result.

## Reviewed source and actual execution

The [registration](REGISTRATION.md), SHA256
`a66f2f8025ab746e83b9a644149265a5058aaa5b75ee15a12763ab30a890ae7f`,
bound one c7i.large and fixed setup/dispatch05:19UTC and retirement05:30UTC.
Both deadlines were met, with no retry, second worker or extension.
The correction report is
`909c95efa05c3577d3b9b7d2c01683887c6e1910d896a36a9c18109c64101614`;
different-model Sol delta FIRST is
`37cb39fedac0add3b3c2962aa4a04723f9d442c93c59b472e9888d3a538ad34a`.
Their completed state, custody, pins, expected manifests and whole reports
were checked before allocation. Sol's static conditional approval did not
itself assert a runtime pass.

The tested files, installed root0444 under canonical root0755 ancestors at
`/opt/jc2-job-pilot-fix`, matched locally, remotely and after execution:

- job.sh: `9c2255c7dcb7c91a8abeb2bd0ea7db30b4d4e8182abdbbd08cc1dc76f33d094d`
- job-regression.sh: `25181501dae8b2833a1106843a908cd4b19d3e9e5d0ebbb00f408d85c62636e7`
- job-probe.sh: `9ec63784453264a67224a5d9355ecd9df3cf9e20b4f7b8b3454e8b6eccab1808`

Worker `i-0b881da911e659481`, private172.30.0.60, was born05:15:31UTC;
Ubuntu24.04.4, boot `db6fa419-560b-4d44-83e6-2a82735ac88e`, exact DMI and
cloud-init completion were observed. The existing image supplied OS tools
only; no baked campaign or protected tree was accessed and no package was
installed. The ED25519 key matched the AWS console-generated fingerprint
before strict-host-key SSH/SCP.

Driver `jc2-job-pilot-erfix20260913a.service`, invocation
`62c43728d5894099b04655a4e1ec2b79`, PID1331, was confirmed actually running.
Its controls were RuntimeMax600s, stop5s, control-group kill, restart=no,
memory1GiB, swap0, CPU80%, tasks128 and per-file64MiB. Each child had its
own finite service controls. No model response was needed between phases.

The recorded regression interval is05:18:23.839603024--05:18:48.041363905UTC,
**24.201760881 seconds**. `REGRESSION_PASS` and all nine PASS groups are
present. The systemd journal reports successful deactivation at05:18:48.
The driver and every exact child cgroup were independently absent before
result consumption. Successful transient units unload: later not-found
manager defaults, including apparent infinite limits and exit0, are NOT
retained runtime evidence. Actual live controls and terminal receipts are.

## Observed case outcomes

- Normal two-phase completion, literal argument preservation, duplicate
  refusal, shared-lock admission/collection exclusion and identical repeat
  archives passed. The lock fixture is a controlled writer, not an assertion
  that every possible admission failure was simulated.
- Expected phase exit17 released its successor and ended the batch at0.
  Unexpected exit17 preserved partial output and visible stderr, skipped
  the successor and failed the batch. A missing executable recorded127,
  not an empty success.
- The8s timeout removed a TERM-ignoring, new-session descendant. Controller
  SIGKILL retained partial evidence and a KILL terminal receipt; the missing
  phase exit was not upgraded to success.
- Bad payload SHA and symlink admission failures were collectible UNKNOWN
  jobs with missing terminal receipts. Path escape, wrong instance and HQ
  invocation were refused for their exact registered causes. The badpath
  job directory was never created.
- A deliberately file-size-limited collection failed at153 with visible
  `File size limit exceeded` diagnostics; normal collection recovered.
  The shell's core-dump wording is not evidence that a core file exists.
  The suite also checked unprivileged diagnostic access.

For example, actual success-controller PID1499 recorded all four UID/GID
values65534, groups65534, all capability sets0, NNP1 and Seccomp2;
`cpu.max=80000 100000`, memory268435456, swap0, pids32 and both FSIZE limits
8388608. These are process/kernel observations, not just requested settings.
The driver journal's1.865s CPU and10.9M memory peak cover the driver cgroup
only, NOT the sum of the separately capped child services.

## Evidence custody and retirement

[EVIDENCE.tar](EVIDENCE.tar) is849920bytes, SHA256
`7ae15428c6428623bbb32cf448ab847505fbf08153ad355e3affff152fb881f9`.
It contains the three installed sources and postpins, driver journal/manager,
the explicit regression base, and the eight actually created job directories.
Each job's inner archive is retained. ROOT read the whole regression log,
empty error streams and actual terminal evidence after stopping; the local
copy's whole log and journal messages were read again during closeout.

The remote archive and parent were flushed. SCP completed, local SHA/size
matched, a second WHOLE-byte SSH stream compared equal under pipefail, and
the local archive and parent were flushed before the exact termination
request. The archive contains deliberate symlink/FIFO fixtures: inspect
explicit regular members with `tar -xOf`; do not blindly unpack it on HQ.

Direct API confirmed the instance TERMINATED by05:27UTC and retained100GiB
gp3 `vol-013b5a506f1b7bb03` AVAILABLE with no attachments. Both registered
personal/us-east-1 nonterminal campaign selectors returned[] successfully.
The independent HQ **user-manager** exact-ID05:30 retirement timer was
stopped only after terminal verification, then not-found/inactive/dead.
An initial stop against the system manager found no unit; ROOT resolved the
correct user-manager handle and stopped that actual active timer. The earlier
rejected termination-property CLI option caused no mutation; the authoritative
property was alreadyfalse. No evidence volume or unrelated resource was
deleted. Retained EBS remains billable; exact credits/dollar cost are unknown.

## Scope and handoff

This removes a demonstrated orchestration obstacle: one bounded service owns
the sequence, records its own controls and leaves readable failure evidence.
The corrected four source/documentation files remain hash-frozen; the old
reviewed versions are preserved in the correction box. Legacy user-dirty
fleet.sh and dispatch.sh remain unchanged.

Not tested: actual SSH disconnect, reboot/power loss, OOM, aggregate disk
quota, malicious-code isolation, native scientific dependencies or mathematical
fidelity. Per-file size limits are not disk quotas. Opt-in use still requires
an explicit workload registration and applicable source/result gates. There
is no automatic scientific migration, extra hardening round or worker launch
from this PASS. JC2 and the current mathematical source gaps remain open.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6955`.
- Body SHA-256:
  `63c33ecf869e583e57352f6d61fabaae796f9495b4aec92e55bf132788e2a459`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
