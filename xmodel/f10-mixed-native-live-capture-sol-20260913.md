# F10 mixed native live-capture observer

Status: **SOURCE COMPLETE, UNEXECUTED, UNREVIEWED**. This packet supplies one disabled AWS-only read-only observer template. It is not a controller, launcher, qualification pass, retry, worker authority, or scientific result.

First action: `2026-09-13T01:04:47.070421595Z`. All five inputs matched before use and the four current evidence/source bodies were read WHOLE.

## Narrow correction

The V3 evidence proves why the old two-turn observation was insufficient: the native unit was loaded/active with `MainPID=1617` at `01:00:13`, but the later process command at `01:00:49` found no process after the collector became terminal at `01:00:38`. Successful metadata outputs do not repair that missing live identity/kernel-control attachment.

`observe-native-live.template.sh` closes only this ordering gap. After exact physical identity, namespace, cgroup-path and original-cutoff bindings, it silently polls at one-second intervals for at most sixty iterations. The future operator must additionally run it under an external `timeout --foreground 60` concurrently with unchanged PREPARE in the same orchestration, with no model turn between discovery and capture.

Once one `systemctl show` snapshot says the exact unit is loaded/active with a positive MainPID, the script irrevocably leaves the polling loop. In that same shell execution it validates the fixed service command and literal controls, then captures bounded `/proc/PID` stat/start ticks, executable, two-argument cmdline, status, limits, cgroup and PID/cgroup namespace identities. It reads and checks the exact prebound cgroup2 path and `cpu.max=80000 100000`, burst zero, memory 1 GiB, swap zero, pids 64 and domain type, with the PID present in `cgroup.procs`. A second stat and systemd identity snapshot must retain the same PID, InvocationID, ControlGroup, active state and executable. Disappearance or any mismatch fails without retry.

Every kernel/proc read is capped at 4096 bytes, each systemd snapshot is capped, aggregate successful stdout is checked below 64 KiB, and no target or remote evidence file is written. Nothing is emitted on stdout until all checks pass; output is a fixed labeled record ending `NATIVE_LIVE_CAPTURE_COMPLETE`. The observer never starts, stops, signals, or otherwise controls the target.

Binding and execution remain future ROOT obligations: fresh exact instance/boot/host/namespaces/cutoff; canonical source hash and review; native availability/pins for every invoked administrative executable; concurrent orchestration with PREPARE; external 60-second foreground timeout and bounded SSH transport; authenticated stdout/stderr/exit capture; and comparison to PREPARE terminal evidence. The original cutoff always dominates. Failure does not authorize another worker or attempt.

No PREPARE, collector, native, CAPRUN, dispatcher, controller, science source, cap, phase, or authority was changed. No AWS, systemd job, worker, dummy, interpreter, import, AST, syntax, test, CAS, native, or scientific execution occurred.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3091`.
- Body SHA-256:
  `66f1f5b34f3e072e5fdb8ca00a16b6700bb2a81e436042bbbcd146d7081364ef`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
