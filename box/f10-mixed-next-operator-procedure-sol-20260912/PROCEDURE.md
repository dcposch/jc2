# PRE-SCIENCE dummy operator procedure — GAP, no launch command

This document is inert and contains no executable launch authority. The prior
attempt is CLOSED. None of its instance, host, boot, namespace, cgroup, unit,
clock, package, manifest or registration values may bind a successor.

## Unqualified successor placeholders

`__NEW_INSTANCE_ID__`, `__NEW_BOOT_ID__`, `__NEW_HOSTNAME__`,
`__NEW_PID_NAMESPACE__`, `__NEW_UID__`, `__NEW_GID__`, `__NEW_UNIT__`,
`__NEW_CGROUP_PATH__`, `__NEW_TMPFS__`, `__NEW_NOT_BEFORE__`,
`__NEW_ABSOLUTE_DEADLINE_WITHIN_25S__`, `__PYTHON_PATH_SHA__`,
`__SETPRIV_PATH_SHA__`, `__CAPRUN_PATH_SHA__`, `__PROBE_PATH_SHA__`, and all
actual native/qualification pins remain unbound. No substitution is selected.

## Exact blocking step

A complete literal command sequence cannot meet the requested *actual rlimit
and cgroup verification without a separate live observer* using the selected
bytes.

The new probe emits, after touching all 64MiB pages, only child PID, PGID,
start_ticks, boot ID, PID namespace, cgroup text and payload size. It does not
emit `RLIMIT_CPU`, `RLIMIT_AS`, `RLIMIT_FSIZE`, or the contents/identities of
`cpu.max`, `cpu.max.burst`, `memory.max`, `memory.swap.max` and relevant cgroup
delegation/controller files. CAPRUN telemetry records its requested CPU/RSS
arguments, leader PID/PGID/start identity, sampled maximum group RSS and
TERM/KILL/reap results; it does not record the child's actual AS/FSIZE limits
or kernel cgroup-control bytes.

After CAPRUN kills/reaps the group, `/proc/__CHILD_PID__/limits` is gone. A
transient unit's cgroup can also disappear before a sequential terminal read.
Configured systemd properties are not themselves a read of the child's actual
inherited limits or live kernel files. Starting asynchronously and polling
`/proc`/cgroupfs races the deliberate 32MiB sampled RSS threshold against the
probe's 64MiB touch-before-marker path; there is no source-guaranteed live
observation interval and this task forbids adding an observer merely to win
that race. Therefore no honest fixed command can promise these required facts.

## What terminal evidence would otherwise be available

One bounded CAPRUN invocation could preserve exact stdout/stderr/telemetry
bytes, CAPRUN numeric exit125, `RESOURCE_CAP/rss`, leader identity, maximum
sampled group RSS, identity-matched TERM then KILL, leader reaping and its last
exact-PGID sample. The new stdout could provide the exact two-line marker/JSON
child identity for correlation. A blocking `systemd-run --wait` return and the
unit's retained `ExecMainStatus` could preserve numeric service exit evidence,
and ROOT could separately require terminal cgroup absence/emptiness. None of
those terminal artifacts reconstructs the missing live rlimit/control-file
observations.

The intended unchanged envelope remains 25 seconds total including cleanup,
`cpu.max=80000 100000`, burst0,32GiB memory and AS,swap0,256MiB FSIZE, a
separate256MiB tmpfs, one nondelegated no-escape cgroup, bounded streams,
canonical `-E -s -S -B`, and exact source pins. These are requirements, not
facts or commands in this GAP document.

## Smallest future resolution (not implemented)

Subject to a new source selection and different-model review, extend the
existing probe's same post-touch JSON record to report its actual three
`getrlimit` pairs and bounded reads of its own resolved cgroup control files
before the marker. ROOT would still compare them with registered values,
CAPRUN telemetry and terminal kernel emptiness. This avoids a concurrent
observer and new framework. No such edit is authorized or made here.
