# r3-exec-bootstrap-repair-gate-fable5-20260912 — focused DELTA FIRST of ROOT's four-insertion bootstrap repair

Lane: Fable 5.1, different-model hostile DELTA FIRST of ROOT's immutable-copy repair
`box/r3-exec-bootstrap-repair-root-20260912/bootstrap.py` (517 lines) against the exact
parent alias `PREDECESSOR.py` (508 lines, SHA-verified equal to the FIRST-reviewed parent),
the repaired `CONTRACT.md`, and ROOT's binding `INTAKE.md`. STATIC / UNEXECUTED /
UNPROMOTED. No program was executed, imported, parsed or compiled; manual source
comparison plus read-only `diff` and `sha256sum` only. This is not a foundation review;
the predecessor interface acceptance is imported only through INTAKE.md.

First action 2026-09-12 16:41:53 UTC. Reserve 16:50 UTC, HARD 16:53 UTC, never reset.
Destination absent before authoring. All six inputs were hashed in
`/tmp/jc2-lane.V6gQb7/inputs` before any body and read WHOLE, COORDINATION first
(807 lines), then bootstrap.py 517, CONTRACT.md 155, PREDECESSOR.py 508, predecessor
report 273, INTAKE.md 54. No inherited, linked, peer or corpus file was read.

## Pre-read pins (all six equal the expected manifest)

| basename | sha256 |
|---|---|
| COORDINATION.md | 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597 |
| bootstrap.py | f04f1b7b16bed194e5d7b503a78fe9bd36e3bd58da3696adf6a40bfdbdcd17d2 |
| CONTRACT.md | 21c1c0bd6840ac7aa80a33e9ff2c7a88bab87f51fd7a669ed6e27ba30b32bfeb |
| PREDECESSOR.py | fb37ce50c4acee5f1fd2495dda476fee5d38b63a4d88a04440a9db8e3c4697b8 |
| r3-exec-bootstrap-gate-fable5-20260912.md | 4f17271e788aae8ae489ba03e80b508c4a5d01d9496f4c03a48a4cf5e39004a3 |
| INTAKE.md | 7e581d2c276743ae89eea0c8b63782b0b5b68d48ab890647bba5e3992837b775 |

## 1. Exact delta

**Delta is exactly four insertions — CONFIRMED.** Read-only `diff PREDECESSOR.py bootstrap.py`
prints only `a` hunks: `224a225-227`, `281a285`, `389a394-397`, `461a470` (9 added lines,
zero deleted or changed lines; 508 -> 517). Every other byte, including imports (lines 6-23),
constants 26-47, `commands()`, `exclusive()`, `observe()`, `leaf()`, `main()`, is identical.
CONTRACT.md:124-136 lists the same four edits; INTAKE.md:28-35 selects the same four.

- **I1 absolute bounds (bootstrap.py:225-227, `__init__`).** Placed after `self.outer_start`
  (224) and after `self.ends` (222), so both operands exist; `ends[2]` is index 2 of the
  literal tuple `(admission, mathematical, task, worker)`, i.e. `task_deadline_utc`, which is
  the ROOT-selected custody-inclusive bound (INTAKE.md:28-30), stronger than the parent
  review's math-deadline line. Types: `deadline()` returns aware datetimes (suffix `+00:00`
  enforced, line 60), `datetime.timedelta` from the already-imported module (15); aware plus
  timedelta and aware-vs-aware `<=` never raise `TypeError`. Failure is `RuntimeError` via
  `need`, caught by `main()` -> `BOOTSTRAP_STOP`, exit 2. Runs once, on immutable spec data,
  before the first `clock()` (266 -> 276) and before any native read or creation. Because
  `clock()` (269-273) requires `utc() < bind_end` and `utc() < ends[0] <= ends[1] < ends[2]`,
  I1 makes every later clock check imply `utc() < outer_start+120` and `< outer_start+3000`
  absolutely; the relative `monotonic-BEGIN < 120` (269) remains an additional bound only.
- **I2 registration-parent exclusion (285, `audit_static`).** Placed immediately after the
  native-closure shape check (282-284), which guarantees `n['directories']` exists; before the
  pin-hash loop (306-308), the directory loop (311-316) and all creation. `str(reg_path.parent)`
  is canonical (`literal()` at 237 requires `resolve()==s`); native keys are forced canonical
  by `directory(d)` at 312 (a trailing-slash key would STOP there), so no spelling mismatch can
  evade the `in` test. A registration parent nested deeper inside an inventoried tree cannot
  evade either: 316 forces every child of a listed directory to be listed, recursively.
  `audit_static` reruns at 479 (after leaves, before the registration write) and 490 (after
  both writes), so the check repeats after each binding stage as CONTRACT.md:135-136 claims.
- **I3 stdin check (394-397, `outputs`).** First statement of `outputs()`, called at 266
  (pre-creation), 479 (pre-write) and 490 (post-write, pre-exec). `os.fstat(0)` on a closed fd 0
  raises `OSError` (caught -> STOP); `os.stat('/dev/null')` follows symlinks; equality of
  `(st_dev, st_ino, st_rdev)` plus `S_ISCHR` on both plus `readlink('/proc/self/fd/0') ==
  '/dev/null'` rejects any pipe, socket, regular/cgroupfs file, directory, tty, `/dev/zero`,
  a mknod'd copy elsewhere (different inode), a deleted node (`' (deleted)'` suffix) and a
  symlinked `/dev/null` (readlink names the target). `stat` is already imported (22). The
  binding receipt (481-488) is unchanged, so the check adds no bytes to any output.
- **I4 umask (470, first statement of `run()`).** Before the nine `os.mkdir(p, 0o755)` calls;
  `0o755 & ~0o022 == 0o755`, so `directory()`'s `o+rx` and no-`g/o-w` predicates (103-104) are
  now consistent with the request. The later `exclusive()` opens use `0o444` plus explicit
  `fchmod` (157-159), unaffected. Line 492 still sets `0o077` before exec, exactly as the parent
  (483), so the dispatcher's inherited mask is unchanged. The old mask is not recorded (minor,
  not required).

**Contradiction search — none found (CONFIRMED satisfiable).** Constraint set on spec data:
`bind <= adm <= math < task < worker`, `bind <= outer+120`, `task <= outer+3000`,
`outer_deadline <= task`, `retirement == worker`; per-check: `outer <= utc < bind`,
`utc+20 s < math`, `utc < adm`, `utc < outer_deadline`, `monotonic-BEGIN < 120`. Example
`outer=T, bind=adm=T+120, math=T+2500, task=outer_deadline=T+3000, worker=T+3100` passes
every predicate at `utc=T+50`. A binding deadline earlier than `outer_started_utc` passes I1
trivially but STOPs at the first `clock()` (impossible window), which is fail-closed, not a
contradiction. No repair is needed. Feasibility caveat (not a contradiction): I1 turns the
parent's process-relative 120 s into an absolute window that also covers interpreter start
and all pin hashing; CONTRACT.md:110-111 already labels this a possible self-consuming limit,
to be settled only by the host qualification.

**Residual on I3 — GAP (minor, host-trust).** The check binds fd 0 to whatever node the path
`/dev/null` currently names; it does not compare `st_rdev` to the canonical `(1,3)` device.
A hostile bind mount or replaced node at `/dev/null` is thus accepted. This lies inside the
asserted `exclusive_root_contract`/host trust, the bootstrap never reads fd 0, and no repair is
required for this delta; recorded for the launcher qualification only.

## 2. Negative cases by source reasoning

Each trace is source reasoning; nothing was run. `BOOTSTRAP_STOP` means `main()` prints
`{status: BOOTSTRAP_STOP, science_outcome: NONE, error_type, reason}` to fd 1, fsyncs, exits 2.

- **N1 binding beyond outer+120** (e.g. `outer=T`, `bind=T+121`, all else legal): I1 line 225
  fails -> `RuntimeError('binding and whole-task absolute bounds from original outer start')`.
  Position: `__init__` before `audit_static`/`observe`/`outputs` (266) and before `run()`.
  Side effects: none on cgroupfs, tmpfs or the registration parent; only the STOP line on fd 1.
  CONFIRMED rejected before writes.
- **N2 task/custody beyond outer+3000 with acceptable math deadline** (`math=T+2500`,
  `task=T+3500`, `outer_deadline=T+3000 <= task`): ordering (223) passes, external cutoff
  (234) passes, I1 line 226 fails with the same reason, same position, zero writes. The parent
  accepted this spec (it checked only elapsed-at-bootstrap < 3000). CONFIRMED rejected.
  Boundary: `task == outer+3000` and `bind == outer+120` are accepted (`<=`), consistent with
  CONTRACT.md:84-87 "no later than".
- **N3 fd 0 another character device or a cgroup fd**: `/dev/zero` or a tty is `S_ISCHR` but
  `(st_dev, st_ino, st_rdev)` differs from `/dev/null` and readlink differs -> STOP `stdin actual
  /dev/null`. A cgroupfs interface file is `S_ISREG`, a cgroup directory `S_ISDIR`, a pipe
  `S_ISFIFO`: `S_ISCHR(incoming)` is false -> same STOP. Closed fd 0 -> `OSError` STOP. All at
  266 before creation. CONFIRMED rejected before writes; repeated at 479 and 490.
- **N4 registration parent in `native.directories`**: I2 at 285 fails -> STOP `registration
  parent outside native inventory` during the first `audit_static` (266), before creation. In
  the parent this spec survived until the post-write audit (`native directory inventory`
  mismatch), i.e. after the registration existed. CONFIRMED rejected before writes. If the
  parent is instead an unlisted child of a listed directory, 316 STOPs; if listed with a
  trailing slash, 312 STOPs; no passage.
- **N5 inherited umask 077**: no longer a STOP; the first leaf is requested `0o755` under mask
  `022`. What mode cgroupfs actually reports for that mkdir, and whether `populated 0`/empty
  `cgroup.procs` hold, remain host observations (CONTRACT.md:150-151); the source only
  guarantees that the request is now consistent with `directory()`. CONFIRMED (source), GAP
  (kernel outcome, external).
- **Failure side effects after partial creation (unchanged path).** A STOP raised at 479/490
  retains created leaves and any written registration/binding; there is no deletion, retry or
  signal (505). The four insertions add no new side effect on any failure path.

## 3. Unchanged interface

Because the diff contains only insertions, the following are byte-identical to the parent and
are CONFIRMED unchanged by construction, not re-derived: the nine canonical authority objects
and expanded CAPRUN/setpriv/probe/science argv (`commands()`, 424-467 vs parent 416-459);
all imports (6-23, no new import); `DISPATCH`/`CAPRUN`/`AUTHORITY` pins, `JOB`, `LABELS`,
`NAMES`, `ENV`, `LIMITS`, `BATCH`, `PROFILES`, `REG_KEYS`, `SPEC_KEYS`; the registration
schema/skeleton predicates (205-213) and `outer_argv` literal (254); `exclusive()` O_EXCL /
O_NOFOLLOW / 0444 / fsync / parent-fsync / byte readback (154-162) and the final re-hash (491);
fd 1/2 bound to `outer.stdout`/`outer.stderr` on the tmpfs (413-416); `closerange(3, ceiling)`
with the finite hard-limit predicate (493-495); same-process `os.execve` with the pinned
interpreter and `ENV` (496); `aggregate_cpu_start_usec == '0'` (213) and the `usage_usec`
cutoff (385); the 64 KiB ASCII `small()` ceiling (139-143) for every kernel read including
maps and mountinfo, with no ceiling increase (INTAKE.md:37-39 honoured: future host snapshots
must fit or STOP). No new enabled specification, child, retry, batch revival or science
authority appears anywhere in the diff.

The predecessor static interface acceptance is imported solely as INTAKE.md:23-26 states it
(nine authority objects/digests and argv agree with the unchanged dispatcher; no self-hash/PID
cycle; auth/frozen/writer empty; same-process exec). The dispatcher, authority, CAPRUN and
guard bodies were not attached here and are not freshly reviewed. Since the binding receipt,
registration serialization and authority inputs are untouched by the four insertions, that
acceptance transfers to the repaired bytes without any new claim.

## 4. Decision, negative control, acceptance perimeter

**Discharge of the named source issues — CONFIRMED with typed remainders.**

- Parent G1/R3 (absolute wall not bound to `outer_started_utc`): discharged as a data
  predicate by I1, in the stronger custody-inclusive form ROOT chose. What I1 proves is only
  that the ROOT-supplied deadlines are consistent with a 120 s binding window and a 3000 s
  whole task measured from the supplied `outer_started_utc`. The dispatcher's own monotonic
  counter still restarts at exec (CONTRACT.md:83-84, INTAKE.md:31-33); the bootstrap cannot
  enforce anything after `execve`. The genuine end-to-end bound therefore rests on (a) the
  truthfulness of `outer_started_utc`, which the source can only require to precede `utc()`,
  and (b) the independently armed external supervisor whose `outer_deadline_utc <= task`
  is asserted (234), not observed. UTC predicates are consistency checks, not a realtime bound.
- Parent G2/R1 (umask): discharged at source by I4; kernel mode outcome remains external.
- Parent G4 (fd 0): discharged by I3 with the minor rdev remainder noted in section 1.
- Parent G5 (registration parent): discharged by I2, now pre-write.
- Parent G3/R2 (64 KiB cap): deliberately NOT changed; disposition is byte-count
  qualification or STOP, per INTAKE.md:37-39. Not a defect of this delta.

Not imported from the predecessor review: PEP 538 behaviour, minimum kernel/Python versions,
the mapped-library subset, and any concrete `SystemCallFilter` exec-refusal fixture. No test,
runtime readiness, strict dummy result, timing or mathematical progress is established.

**Negative control (independently reasoned, static, unexecuted).** Spec identical to a
legal one except `outer_started_utc` moved 130 s earlier (so `bind - outer = 250 s` while the
launcher would still start the process inside its real 120 s window). Expected: STOP at line
225 with reason `binding and whole-task absolute bounds from original outer start`,
`error_type RuntimeError`, exit 2, zero leaves, no registration, no binding, tmpfs inventory
unchanged, no dispatcher. The parent would have accepted this spec and run. This control
separates I1 from the pre-existing `clock()` predicates (which all still pass at that instant)
and is meaningful because it flips exactly one inserted line. Not executed; no outcome claimed.

**Acceptance perimeter.** Accepted, statically: the delta is exactly the four contracted
insertions; each is correctly placed before creation and repeated where claimed; each named
negative (N1-N4) rejects before any write; N5 no longer STOPs at source; the imported
interface acceptance transfers unchanged; no cap, authority, child or specification was
added. Source-visible blocker: NONE. Exact remaining external preconditions before the one
separately authorized AWS-only nine-phase observation: ROOT approval of the new
`bootstrap_sha256` f04f1b7b... and its spec; a genuine `outer_started_utc` from the launcher
with an already-armed, no-restart monotonic supervisor covering descendants whose cutoff is
at or before `task_deadline_utc`; launcher `StandardInput` actually `/dev/null` and fd 1/2 on
the bounded tmpfs; measured maps/mountinfo/cgroup snapshots under 64 KiB ASCII on the host;
observed cgroupfs leaf mode/population under mask 022; native closure, namespace, ACL/xattr
and watchdog qualification. This review grants no authority for that observation, raises no
OPEN, and asserts no exit price.

## Custody

- First action 16:41:53Z (pre-read hash of all six inputs, all equal to the manifest);
  skeleton without marker 16:45:02Z; sections 1-2 written 16:45:52Z; sections 3-4 written
  16:46:24Z; this custody section and the seal are the fourth and last write.
- Post-write re-hash of all six inputs at 16:46:24Z, after sections 3-4 and immediately
  before this final write, equals the pre-read table above; no input changed.
- Only this file was written, in four bounded writes via the installed `apply_patch`
  (each invocation reported exactly this one path); no other file, no finalizer, no
  `charge_basis` line (no exit price is asserted), no interpreter, CAS, import, compile,
  test, network, git or process inspection, and no execution of any inspected program.
  The only non-hash read-only commands were `diff`, `ls`, `wc`, `grep -c` and `date`.
- Whole readback of this report follows the seal in the lane log; no write after it.

<!-- BODY-END -->
