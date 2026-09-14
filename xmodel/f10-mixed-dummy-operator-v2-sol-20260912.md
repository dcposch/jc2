# Mixed dummy operator v2 procedure

Status: **COMPLETE INERT PROCEDURE / UNBOUND / UNEXECUTED / NO AUTHORITY**.
First action `2026-09-12T22:03:30.508720538Z`.

`box/f10-mixed-dummy-operator-v2-sol-20260912/PROCEDURE.md` gives one finite
fresh-worker sequence for the accepted v2 probe and unchanged CAPRUN. All host,
boot, namespaces, UID/GID, unit, deadline, mount, executable and native facts
remain explicit placeholders; the closed worker and clocks are forbidden.

The procedure creates one separate256MiB noexec tmpfs with exact admin/output
siblings, arms independent exact-unit retirement, and performs one blocking
`systemd-run --wait`. The service is root CAPRUN with only KILL/SETUID/SETGID
capabilities, NNP, no delegation, protected cgroupfs, fair scheduling,
CPU80%/100ms, memory/AS32GiB, swap0, FSIZE256MiB, RuntimeMax20s plus
TimeoutStop5s. CAPRUN retains its exact flags and dummy values: wall5, CPU3
(hard4), sampled RSS32MiB; setpriv drops to the bound nonroot UID/GID with
cleared groups/NNP; probe startup is exactly `-E -s -S -B`.

The expected nonzero `systemd-run --wait` return is explicitly captured and
must equal125 along with ExecMainStatus and CAPRUN telemetry. No polling or
observer exists. Terminal predicates require bounded streams; exact canonical
two-line v2 stdout; child/leader/PGID/start/boot/namespace/cgroup correlation;
actual rlimits and control bytes; sampled RSS; genuine TERM/KILL/reap; then
persisting-cgroup emptiness or final exact path absence before timer removal.
Missing marker, short write, cap race or any mismatch is STOP without retry.

This is not a claim that systemd properties, self-reported controls or sampled
RSS alone prove no escape or true peak. ROOT must still bind actual qualified
executables (including the terminal JSON parser), source/native/import facts,
physical cgroup/mount custody, no writers, absolute deadline, durable transfer
and retirement. No science import or launch is included.

Fresh WHOLE reads covered all nine inputs in PINS. Final WHOLE readback covers
PROCEDURE, PINS, report and manifest; strict postpins precede custody. No AWS,
network, interpreter, import, syntax, AST, dummy, CAS or protected-tree action
occurred.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `2234`.
- Body SHA-256:
  `03c6f637f97e4a1e535cd5934a67911d24bcecc06eaecb35019009db1b51ce50`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
