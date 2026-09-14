# r3-bootstrap-launch-gate-fable5-20260912 — hostile FIRST of the service-entry launcher

Tier: STATIC/UNEXECUTED different-model FIRST (Fable 5.1) of Astra's completed
launcher.py and CONTRACT.md. No code executed, no interpreter, no test, no
network, no git. First action 2026-09-12T17:24:51Z; reserve 17:40Z, hard
17:43Z. All six snapshots in /tmp/jc2-lane.yo31V9/inputs were hashed before
any body and matched the six expected pins (table in Custody). Whole
unclipped reads: COORDINATION.md (806 lines) first, then launcher.py (272),
CONTRACT.md (154), bootstrap.py (517), INTAKE.md (57), ROOT-INTAKE.md (59).
Dispatcher/guard/science acceptance is imported only via INTAKE.md; those
bodies were not read. No uncharged file, corpus, peer output or prior report
was read. Line references are launcher.py:N unless prefixed.

## 1. Launcher correctness and the acyclic approval interface

CONFIRMED (source), with external premises. Acyclic: KEYS (26) carries
spec_sha256 and no card/unit digest; SPEC_KEYS (bootstrap.py:42-47) has no
card key; outer_unit() (123-137) renders the card SHA into ExecStart. Chain
spec->card->unit, no cycle; bootstrap.py:280-281 forbids spec/registration/
binding in pins. Epoch observed, not predicted: the card triple epoch_utc/
epoch_timestamp_raw/epoch_timer_monotonic_usec is compared by dict equality
with the live timer's ActiveEnterTimestamp/ActiveEnterTimestampMonotonic plus
loaded/active/waiting/FragmentPath/DropInPaths='' (205-207); the service's
ExecMainStartTimestampMonotonic >= mono (216-217), its own
ActiveEnterTimestampMonotonic in [mono, now] (230-231), MainPID=ExecMainPID=
getpid() and 32-hex InvocationID (213-215); all recorded under actual_service
separately from the card epoch (241-244). What the source cannot prove: a
re-armed timer with re-approved card/spec is indistinguishable from a fresh
experiment; ROOT_APPROVED_PREFLIGHT_LAUNCH (153) is trust, not
authentication. GAP-external: single arming and approval custody.

Canonical JSON: load() (90-94) requires the digest before parsing, rejects
duplicate keys, floats, NaN/Infinity, and requires byte-identical
re-encoding (sorted, compact, ASCII, newline); integers of any size pass;
device/inode are `type is int` (bool excluded, 221); monotonic epoch and
quota are decimal strings (191-198). CONFIRMED. Keys/paths/modes/ACLs: all
26 KEYS are consumed; launcher_first/accounting/retirement qualification
SHAs are shape-pinned only (156-158) and dereference nothing, i.e. opaque
references, not installed qualification. path() (39-43) admits only
`/[A-Za-z0-9_./-]+`, str(Path)==s, resolve()==s, non-symlink, so `..`, `.`,
`//`, trailing slash and symlinked tool paths (/bin/env on merged usr) are
refused; rooted() (46-50) walks to `/` requiring uid 0, no g/o write bit, no
POSIX ACL xattr; raw() requires a regular 0444 file <=256 KiB for card,
spec, bootstrap and the three unit texts. CONFIRMED.

Loaded versus on-disk: the source proves unit file bytes (201-203),
FragmentPath/DropInPaths='' of the loaded units and the slice's effective
cgroup files (224-225). It never reads NeedDaemonReload, RuntimeMaxUSec,
TimeoutStopUSec, KillMode or the loaded timer's next elapse; a stale loaded
unit with matching file bytes passes. CONTRACT step 5 and ROOT-INTAKE line
47 assign this to ROOT. GAP-external, not a defect.

Cross-artifact coupling P-TOOLS (premise, not defect): 171-172 require the
launcher and the three tool pins inside registration.pins; bootstrap.py:
306-308 then applies regular(p, p in native.files or p in {python,setpriv})
to every pins entry, so env and systemctl must be listed in
native_manifest.files or carry no write bit at all; a 0755 binary outside
the manifest fails 'pinned file mode' after the exec. No source-visible
incompatibility preventing a legitimate execution was found: with LC_ALL=C
set, CPython's PEP 538 coercion inserts no LC_CTYPE, so dict(os.environ)==
ENV (154) is satisfiable; sys.orig_argv (161) needs Python >= 3.10 and
/proc/self/exe must be the pinned real binary (external version premises).

## 2. Clock/cap composition

CONFIRMED (source), premises listed. Rendered bytes: timer OnActiveSec=115s,
AccuracySec=1us, RandomizedDelaySec=0, Persistent=no, RemainAfterElapse=yes
(141-143); guard oneshot `systemctl --system stop UNIT SLICE`,
TimeoutStartSec=10s, no Slice= line (144-146), hence in the default system
slice, outside the accounting slice. Outer: RuntimeMaxSec=2875s,
TimeoutStopSec=5s, KillMode=control-group, SendSIGKILL=yes, Restart=no
(132-133). The only systemctl verb in the source is `show` (109-115); nothing
starts, stops, resets or cancels a unit, so no binding-only cancellation
exists. Admission: 0 <= now_mono-mono < 100 s and 0 <= now-epoch < 100 s
(232-233), paired drift <= 2 s (234), now < binding_deadline <= epoch+120 s
and task_deadline <= epoch+3000 s (235-236), monotonic and realtime
rechecked immediately before execve (251-252). Bootstrap windows
(bootstrap.py:225-226, 269-273) unchanged.

Microsecond versus whole second: epoch_utc must have microsecond 0 and
render as `%a %Y-%m-%d %H:%M:%S UTC` (196); systemd floors the rendered
second, so true activation is epoch+f, 0 <= f < 1 s. Every use of the
floored epoch overstates elapsed realtime and understates remaining budget
(admission, epoch+120, epoch+3000, bootstrap outer_start+120/+3000), i.e.
conservative by f; the monotonic side is exact. The OnActiveSec base is the
timer's activation instant, at or microseconds before
ActiveEnterTimestampMonotonic, so the elapse is at or before mono+115 s.
Realtime rollback after entry: bootstrap realtime predicates could pass
longer; its monotonic bound is 120 s from BEGIN (bootstrap.py:25,269), i.e.
< epoch+220 s, and nothing bounds the dispatcher phase from inside; the
armed 115 s monotonic timer stops unit and slice together at <= epoch+115 s
with the 5 s TERM/KILL budget, whole experiment ~epoch+120 s under the OS
supervision premise. A rollback before entry beyond 2 s is caught at 234; a
forward jump only shortens windows. CONTRACT 113-119 describes the source
accurately; no hard-realtime claim is made (109-110). RuntimeMax fallback:
counted from service start, which precedes entry (< epoch+100 s), so expiry
< epoch+2975 s and KILL by ~epoch+2980 s < 3000 s. No declared cap rises
(BATCH 3000/2100 unchanged, bootstrap.py:36-37). CPU origin: 227 and
bootstrap.py:385 test only usage_usec < 2050 s; the message 'whole-task
accounting origin zero' overclaims (non-blocking); the slice counter covers
only work inside the slice since creation, work outside is uncharged by
construction, as CONTRACT 91-94/125-127 state. Nine preflights plus custody
fitting in 115 s: unmeasured; the source asserts nothing, timeout is STOP.

Premises required (GAP-external, none evidenced here). P-SYSTEMD:
`show --property` prints empty values; `*Timestamp` pretty format is
`%a %Y-%m-%d %H:%M:%S %Z` in the client's TZ (launcher passes TZ=UTC,
LC_ALL=C); `*Monotonic` prints raw microseconds; OnActiveSec is relative to
activation and survives daemon-reload without rebase; stopping a slice stops
its members; KillMode=control-group kills the sub-cgroup leaves. P-SLICE:
the slice unit carries the same five outer_resources values (its bytes are
unchecked; only effective files at entry are read). P-KERNEL:
CONFIG_PROC_CHILDREN, unified cgroup2 only, cpu.max.burst present, xattr
listing on cgroupfs. P-ROOT: one arming; spec/card/unit freeze, reload,
verification and start inside the 100 s window; administrative members
inside the slice with <= 5 s stop contracts; retirement mechanism.
P-DURATION: systemctl replies within the 2 s timeout under the chosen quota.
P-TOOLS as in section 1.

## 3. Bootstrap boundary

CONFIRMED. ExecStart (125-126) is `ENV -i PATH=.. LANG=C LC_ALL=C TZ=UTC
PYTHON -I -S -B LAUNCHER --card CARD --card-sha256 SHA`; systemd's injected
INVOCATION_ID, SYSTEMD_EXEC_PID, PATH, LANG are wiped; no `$`/`%` tokens,
no whitespace in paths. The launcher verifies flags (11), exact orig_argv
and exe (160-161), environment (154), then execve's `[PYTHON,-I,-S,-B,
BOOTSTRAP,--spec,SPEC,--spec-sha256,SHA]` with ENV (253), byte-for-byte
what bootstrap.py:255-256 demands (files.python==c.python forced at 169,
canonical paths at 165-166). Same PID: systemd->env->python->python->python
by exec. Stdio: fd0 must be the real char device 1:3 with the /dev/null
inode and readlink (180-183), which closes for the entry process, and by
fd inheritance across execve, the major/minor gap INTAKE.md lines 42-45
named for the bootstrap; fd1/fd2 must be the regular files
output_mount/outer.stdout|stderr by dev/ino and readlink (184-187). The
entry record (241-246) is <= 16 KiB, one os.write to fd 1 (systemd append),
fsynced; no other file is created, so bootstrap.py:409-412 inventory holds.
Children/threads/fds: subprocess.run with close_fds and pipes reaps the
systemctl child on return, or kill+wait on timeout then STOP;
`/proc/self/task/PID/children == ''` and one task (237-238) are checked
after the three show() calls; os.closerange(3, hard NOFILE) with a finite
3..1048576 ceiling (248-250) precedes the last clock check and execve.
Outer domain: '/sys/fs/cgroup'+ControlGroup == registration.cgroup_path and
/proc/self/cgroup (218-219); its parent == task_scope with the card's
device/inode (220-223). Leaf creation, native closure, source placement,
64 KiB snapshots and the 0o077 pre-exec umask remain the bootstrap's
INTAKE-accepted scope, not re-reviewed; chdir(wrapper_dir)/umask(0o022)
(247) precede the bootstrap's own repeat of both.

## 4. Negative traces and failure records

CONFIRMED, static only. T1 wrong approved spec SHA: load(c['spec'],
c['spec_sha256']) at 166, raw() then digest(data)==pin(h) fails,
'approved input SHA mismatch', LAUNCH_STOP exit 2, before any systemctl
call (205) and any exec; a malformed digest raises 'SHA256 shape' there.
T2 false epoch with card and spec rehashed and re-approved together, unit
re-rendered with the new card SHA, real timer retained: 152-203 all pass
(194 compares card to spec, both false; 196 only checks rendering
consistency; 201-203 pass because the unit was re-rendered). Rejection is
at 205-207: the live timer's ActiveEnterTimestamp/Monotonic differ from the
card, 'original timer still armed, never restarted'. Semantic comparison,
not a hash failure. Only the monotonic field falsified: same site. Future
epoch (predicted start): 207 first; if the timer were also faked, 232
(negative elapsed) rejects. T3 genuine expired epoch: elapsed in [100,115)
s fails 232-233; >= 115 s the timer shows SubState=elapsed so 207 rejects
first; binding deadline passed fails 235. T4 stale card bytes with the
correct CLI SHA: load(card) at 151 fails on digest, the hash path, not
counted as exercising the epoch predicate. All STOP, no retry (Restart=no,
main() has no loop).

Failure records: every exception reaches main()'s single handler, one line
`{"error_type","reason"[:400],"science_outcome":"NONE","status":
"LAUNCH_STOP"}` appended to outer.stdout, fsync, exit 2. Side effects before
that: none; run() writes nothing before 246 (no leaf, registration,
authority, standalone file), and 247-253 (chdir, umask, closerange, execve)
leave no artifact. outer.stdout shapes: (a) LAUNCH_STOP alone; (b) entry
record then LAUNCH_STOP when 247-253 fail, e.g. execve ENOENT; (c) entry
record then bootstrap output; (d) entry record then nothing if killed. A
short write at 246 leaves a truncated record with LAUNCH_STOP on the same
line; if the handler's print itself fails (ENOSPC/FSIZE) Python exits 1
with a traceback on outer.stderr. LAUNCH_ENTRY_CHECKED_NOT_BOOTSTRAP_RESULT
asserts only that 151-246 passed: neither preflight nor exec success.

## 5. Verdict

No blocking source defect. CONDITIONAL ACCEPTANCE at STATIC SOURCE-REVIEW
tier of the charged launcher interface only, conditional on P-SYSTEMD,
P-SLICE, P-KERNEL, P-ROOT, P-DURATION, P-TOOLS, all ROOT-registered and none
evidenced here; installed readiness is not accepted. Non-blocking
observations, no repair required: (i) the loaded-unit gap could be narrowed
inside the existing show() lists by adding NeedDaemonReload with expected
'no' to the three property sets; (ii) reword the message at 227 to
'whole-task CPU below cutoff'; (iii) epoch_utc admits any ISO variant
fromisoformat parses, kept consistent by card/spec byte-equality and
identical bootstrap parsing. No worker, enabled card/spec, scientific
outcome, batch retry or unchanged-foundation review follows.

## Custody

First action 2026-09-12T17:24:51Z (date -u), then sha256sum of all six
snapshots before any read; six of six matched the expected pins:

| basename | sha256 (pre = post) |
|---|---|
| COORDINATION.md | 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597 |
| launcher.py | c3b42e78f01e469594c9d17f105bdffb42fcff2e79e33a131f72be9bff91b7e7 |
| CONTRACT.md | c6b034149a550451ad11d69a12be389bde68f3159d6bf688f31cc887fe38780f |
| bootstrap.py | f04f1b7b16bed194e5d7b503a78fe9bd36e3bd58da3696adf6a40bfdbdcd17d2 |
| INTAKE.md | ec471d42f87a156295daa068d3778bba0470bf39fa891f007d7d124e61a1f765 |
| ROOT-INTAKE.md | f3b5e36b1a64b8a163edd44911eca9eaca9fe934ae032484811f8f78ccf44101 |

Postpins: all six re-hashed at 17:39:00Z after the body write, byte-identical
to the table. Writes: skeleton without marker at 17:37:58Z, one bounded body
patch, this custody patch with the seal; every write via the installed
apply_patch, no Write/Edit tool, no shell file redirection. Only this file
was written: xmodel/r3-bootstrap-launch-gate-fable5-20260912.md. No
charge_basis line is declared (no exit-price assertion). No finalizer, no
execution of inspected code, no interpreter, no network, no git. Own WHOLE
readback performed after the seal; ROOT owns terminal custody, TERM/KILL and
timer retirement. Hard 17:43Z not reset.

<!-- BODY-END -->
