# Mixed dummy live-limits source delta

Status: **IMPLEMENTED SOURCE-ONLY / UNEXECUTED / UNREVIEWED / NO AUTHORITY**.
First action `2026-09-12T21:57:02.062095313Z`.

The immutable v2 probe closes the previously identified terminal-data gap in
source form. It preserves CLI, fork/parent exit, ignored TERM,64MiB page touch,
marker timing and infinite sleep. Its same post-touch canonical JSON now adds
actual CPU/AS/FSIZE getrlimit pairs; real/effective UID/GID; NoNewPrivs/CapEff;
cgroup namespace; one validated cgroup-v2 membership; canonical resolved path
and stat identity; and bounded exact reads of cpu.max, cpu.max.burst,
memory.max, memory.swap.max, cgroup.type, cgroup.controllers and
cgroup.subtree_control.

Every metadata read is O_NOFOLLOW and capped4096 bytes. Cgroup resolution must
stay beneath `/sys/fs/cgroup` without `..`; every numeric JSON value is a
string. Exact accepted values are CPU3/4, AS32GiB/32GiB, FSIZE256MiB/256MiB,
nonroot equal identities, NoNewPrivs1, zero CapEff, CPU80%/100ms, burst0,
memory32GiB, swap0, domain type and empty subtree control. Any missing,
malformed, inaccessible, oversized or mismatched datum stops before marker.

This does not guarantee the marker precedes CAPRUN's RSS kill. ROOT still must
bind exact two-line output to CAPRUN/service identities and telemetry, new
source/native pins, physical nondelegated/no-escape cgroup custody, sampled
RSS, identity-safe TERM/KILL/reap and terminal kernel emptiness. Self-reported
bytes are not a no-escape or true-peak theorem. The25-second total including
cleanup, separate256MiB tmpfs and all installed/native facts remain external.

Fresh WHOLE reads covered all eight inputs in PINS. No interpreter/import/
syntax/AST/test/dummy/CAS/AWS/network action or external source change occurred.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `1812`.
- Body SHA-256:
  `6bc9c62d2155aad12b8621740323845e310580ac17f45b539dd343755d9f7d2e`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
