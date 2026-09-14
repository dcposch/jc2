# FIRST (Fable 5.1): closed-child CAPRUN/runtime attachment — code gate

status=COMPLETE started_utc=2026-09-11T07:57:36Z body_closed_utc=2026-09-11T08:07Z reserve=08:20Z hard=08:23Z (unchanged)
verdict=A CONFIRMED(1 live-host GAP) B CONFIRMED(+1 REAL fail-closed defect) C CONFIRMED D CONFIRMED E CONFIRMED F CONFIRMED(hazard=B defect) G DISABLED-DRAFT-ONLY; no execution/science clearance
scope=STATIC_SOURCE_TEXT_ONLY no_execution=true no_import=true no_syntax_check=true
owned=xmodel/caprun-closed-scope-code-gate-fable5-20260911.md,box/caprun-closed-scope-code-gate-fable5-20260911/input_custody.md

## Custody

All 22 frozen inputs at /tmp/jc2-lane.ZRZxkQ/inputs hashed with sha256sum -c BEFORE any body read; 22/22 OK (see input_custody.md).

## Verdicts A-G

Basis: static text + manual reasoning only. ZERO execution/import/syntax/AST/test. Line refs are to the NEW files in the frozen inputs dir.

### Read scopes (actual)

- run_capped.py, dispatch.py, probe.py, mutate.py: FRESH_WHOLE (1385/744/217/289 lines). All four .diff files WHOLE.
- Old aliases: own `diff -u old-X.py X.py | tail -n +3` sha256 == retained `X.diff` tail for all four (436/232/72/61 lines) => every hunk identical; old files read DIFF/CONTEXT only, no expansion needed.
- Report/manifest/CONTRACT/PINS/custody/artifact/diagnosis/kernel.source.json/python.source.json: WHOLE.
- kernel-v7.0-cgroup-v2.rst: SELECTED 257-613 and 855-990 via keyword extraction (zombie/procs 283-290, populated 421-437, no-internal-process 507-533, procs write access 896-898, events 955-965). Not a whole-manual read.
- cpython-v3.12.3-posixsubprocess.c: SELECTED 560-850 and 895-914 via keyword extraction: make_inheritable 599, close(errpipe_read) 609, setsid 678, setpgid 684, preexec_fn call 708-717, _close_open_fds AFTER preexec 725-727, execve 736, vfork asserted off when preexec_fn set 811.

### A. Positive placement — CONFIRMED (one GAP)

- Order is right by CPython text: setsid (678) precedes preexec (708), so `attach()` run_capped.py:284-311 sees pgid==pid (300); close_fds runs after preexec (725) and execve after that (736); with preexec_fn set, vfork is excluded (811), so the closure runs in a real child.
- `attach()` closes the reader (286), revalidates, requires origin==outer and leaf populated==0 (288), writes own PID to leaf cgroup.procs with O_CLOEXEC|O_NOFOLLOW and closes it (290-296), rechecks membership and populated==1 (297), applies the unchanged CPU rlimit (302-303), writes a <=2048 B record and closes the writer (307-310). No cgroup or pipe fd survives to exec; the `pass_fds` pair is only kept so the closure can close it deterministically.
- Parent side: writer closed (995), non-blocking bounded read (314-317), record must equal a fresh /proc identity of the HELD pid (319-325) and /proc/pid/cgroup must equal the leaf (326). The record is written before exec and Popen returns only after exec/EOF on errpipe, so the read cannot race; a fast-exiting leader stays a zombie (SIGCHLD=SIG_DFL at 981) and /proc/pid/{stat,cgroup} remain readable (kernel 283-290), so fast exit is attested, never promoted.
- Migration by the workload: cgroup.procs/threads/subtree_control/events must be root-owned with no g/o write (254-258); setpriv drops to unprivileged with no-new-privs; kernel 896-898 requires write access to destination AND common-ancestor procs. No descriptor path exists.
- No fallback: eight args `required=True` (148-153); `scope_quiet()` raises when `_CLOSED_SCOPE is None` (340-343).
- GAP (live-host, ROOT): `relative()` (230-231) assumes the root cgroup namespace and the cgroup2 root mounted exactly at /sys/fs/cgroup; the mountinfo test (240-243) checks the mount, not the namespace.

### B. Completion/error paths — CONFIRMED with one REAL fail-closed defect

- Normal path 1029-1040 completes only on `scope_quiet(require_placement=True)`; empty ps while populated increments the counter and keeps monitoring (1041-1042); RSS/wall still fire (1043-1052).
- Every cleanup/bootstrap path gates TERM/KILL and the reap on kernel quiet (655, 663, 677, 704, 737, 757, 766, 775); `CleanupResult.complete` requires kernel_quiet (107-109). Bootstrap direct kill uses os.kill on the held pid (734). Identity-checked TERM/KILL unchanged (597-620).
- Fail closed: malformed events/missing populated (262-274), identity drift (validate 237-260), Popen/preexec failure (process stays None; CPython reaps its own failed child 717 and the trusted closure has no descendants), ESRCH (703-716), and the terminal guard (1298-1307) that turns any non-quiet or non-attested outcome into RUNNER_FAILURE even when telemetry was already NORMAL_EXIT.
- Zombie semantics support the design: kernel 283-290/421-427 make a leaf holding only zombies populated=0, so the held zombie leader does not block quiet.
- REAL DEFECT (fail-closed, defeats a legal run): `wait_for_group_quiet` 630-638 samples ps FIRST (631) and returns that sample when the kernel is quiet (633-634). If the SIGKILLed orphan is still exiting when ps reads it but has exited before cgroup.events is read, the returned `final_sample.live_pids` is stale-positive while kernel_quiet is true, so `complete` (109) is False and telemetry says "process group remained live" (1071-1077). The old code could not do this because it returned only on an empty ps list. Same shape at 649/653 when quiet at entry. Smallest correction: after `scope_quiet()` is true, return a FRESH `sample_group(pgid)` (also fold its rss into maximum_rss) instead of the pre-quiet sample; the conservative predicate is preserved. Any correction changes the CAPRUN hash and re-opens D.
- Exact ROOT dependence: a descendant that leaves the PGID (setsid) or sits in D-state is not reachable by killpg; the leaf stays populated, cleanup is bounded, RUNNER_FAILURE is emitted and dispatch.py:391-399/543 STOPs. No cross-PGID kill (e.g. cgroup.kill) is added; ROOT outer unit recovery remains required. Stuck Popen/preexec I/O is uncovered by any CAPRUN timer.

### C. Ownership/topology — CONFIRMED (obligations listed)

- dispatch.py:300-325 requires per-label direct child, dev/inode/uid/mode identity for outer and leaf, `domain` type and EMPTY subtree_control on both, root-owned interfaces, exact leaf inventory (317), leaf has no subdirs (318), populated in {0,1}, and ==0 when `empty=True`. probe.py:91-113 and mutate.py:91-113 repeat this from inside the leaf.
- Legal populated-outer topology: kernel 507-533 restricts internal processes only when domain controllers are enabled in subtree_control; outer subtree_control is required empty, so leaves inherit the outer resource domain and the outer memory.max/cpu.stat remain effective. No leaf memory.max is read anywhere (correct; it would not exist).
- Live-host assumptions a future ROOT registration must discharge: cgroup2 unified root at /sys/fs/cgroup in the root cgroup namespace; the outer unit is not a systemd Delegate= subtree that systemd will prune or repopulate; leaves are created empty before dispatch and never re-created (inode pin); `/proc/<pid>/task/<pid>/children` available; ps present at /bin/ps or /usr/bin/ps and pinned in the native closure (374-375).

### D. Dispatcher composition — CONFIRMED

- Eight new arguments in fixed order inside the whole expanded command (473-481) compared whole to the ROOT vector (497). `CAPRUN_SHA` (24) equals the frozen run_capped.py hash (matched pin). Runner must stay outer (516), captured child must be in its leaf (528). Terminal `closed_scope` binding (550-561) needs placement_attested, last populated==0 and attestation == leader pid/pgid/start/leaf/boot/ns/dev/ino. `group_quiet()` (391-399) checks every leaf populated==0 before any telemetry read (543), freeze (678) and durable copy (692).
- Schema/mode/guard consumed consistently: dispatch 155-161/184-192/291-292, probe 69-79/91-113/180-185 (`closed_scope` key matches authorize() 419-423), mutate 69-79/91-113. mutate.py main 205-285 is unchanged (diff confirms only identity/root_policy hunks). No science/native/output/CPU/cap check is relaxed.

### E. PREFLIGHT_ONLY_9 — CONFIRMED

- labels = LABELS[:9] (158), allowed_phases/commands/leaves must equal exactly that set (159, 190, 282); typed_slot_policy must be {} and phase_policy null (291-292); `run()` refuses other labels (444) and never substitutes a typed token (488-496). After the strict dummy, execute() requires exactly nine records and returns CLOSED_SCOPE_PREFLIGHTS_9_CHECKED_NO_SCIENCE (618-625); produce/check-positive/mutate/check-negative authorities are never formed. mutate.py:79 refuses outside FULL_13. FULL_13 scientific interface unchanged and still pending fresh ROOT registration. The seven refusal phases still invoke the real entrypoints and still mint REGISTERED-shaped refusal authorities as before; none is successful science.

### F. Strict discriminator — CONFIRMED mechanics, one legal-run hazard

- probe.py:199-213 keeps single fork, R handshake, parent _exit(0), TERM-ignore, 64 MiB touch, pause; identity adds only `cgroup` (63). dispatch 599-617 keeps RESOURCE_CAP/rss, TERM and KILL sent, MATCH identities, leader_reaped, cleanup_complete, empty live list, four-event order/identities, RSS>32 MiB, and adds leaf membership + kernel_quiet. No sleep/two-scan, cap raise, or retry.
- Hazard: the B stale-positive race yields cleanup_complete=False => dummy predicate fails => STOP with no retry. Fail-closed, but it can consume the single authorized run.

### G. Disposition

ROOT may draft a DISABLED PREFLIGHT_ONLY_9 registration against these exact bytes; nothing here clears execution or science. Recommendation: apply the one-line fresh-sample correction first (new hash, new pin, focused re-read of that hunk) or explicitly accept the spurious-STOP risk. Remaining ROOT obligations: actual outer/leaf dev/inode/boot/ns/host values; cgroup namespace/mount facts above; installed CPython and ps identity vs the v3.12.3/v7.0 upstream snapshots; native closure, argv vectors, clocks, release. 120 s stays UNMEASURED planning.

### Adverse traces (manual)

1. Historical schedule: ps misses 8744, leader is Z. New loop: `scope_quiet` reads populated=1 (8744 live in leaf) => no completion; counter+1; later RSS>32 MiB => TERM/KILL. Closed.
2. Stale-positive: KILL sent (664); ps sees 8744 exiting (state R); cgroup_exit flips populated to 0; events read => quiet; returns sample with live 8744 => complete False => RUNNER_FAILURE. Fail-closed, legal run lost.
3. PGID escape: descendant setsid; killpg misses it; leaf populated=1; bounded waits; RUNNER_FAILURE; dispatcher group_quiet STOP; ROOT outer recovery.

QUANTITY: one REAL fail-closed defect (B/F), zero false-success paths found. CHEAPEST TEST: none executable here; after correction, the single AWS-only nine-phase discriminator. UNMEASURED: ps-vs-exit window width, 120 s allowance, kernel populated latency. COLLISIONS: own two targets only, absent at 07:57:36Z, no other writer.

## Postpins and closure

All 22 inputs re-verified with the same list after the body write: 22/22 OK at 08:06:22Z (generated rows in input_custody.md). Own WHOLE readback of both owned files done before this marker. No author Seal, charge_basis or artifact transaction; adapter seals. All writers IDLE after the marker below.

<!-- BODY-END -->
