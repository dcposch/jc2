# r3-exec-bootstrap-gate-fable5-20260912 — hostile FIRST of the same-process preflight bootstrap

Lane: Fable 5.1, different-model FIRST of Astra's actual 508-line `bootstrap.py` and
`CONTRACT.md` against the exact unchanged dispatcher (`dispatch.py` 52b3d916…) and
scientific interlock (`authority.py` 804c7aff…). STATIC / UNEXECUTED / UNPROMOTED.
No program was executed, imported, parsed or compiled; manual source comparison only.
No runtime, timing, native-completeness or scientific result is claimed.

First action 2026-09-12 16:17:58 UTC. Reserve 16:34 UTC, HARD 16:37 UTC, never reset.
Owned destination was absent before authoring. All eight inputs were hashed in
`/tmp/jc2-lane.ujuAfR/inputs` before any body and read WHOLE, COORDINATION first
(806 lines), then TASK 152, CONTRACT 107, CLOSED-CHILD-CONTRACT 60, Astra report 91,
bootstrap.py 508, authority.py 133, dispatch.py 744. No other body was read.

## Pre-read pins (all eight equal the expected manifest)

| basename | sha256 |
|---|---|
| COORDINATION.md | 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597 |
| TASK.md | 90257d2f73bf8fc07e8fdec377ac3232866792a5d4ab8f5baf37a6fe4bd5066d |
| bootstrap.py | fb37ce50c4acee5f1fd2495dda476fee5d38b63a4d88a04440a9db8e3c4697b8 |
| CONTRACT.md | 6d764e0060238b3bb4d1799a4cd1904fdd4d6f756f7ba0ff7e4c678f0e9b13c5 |
| r3-exec-bootstrap-astra-20260912.md | d8b055715c60dae43ce6b74ed3f940d293d0bea6080e6b83d614659b310db790 |
| dispatch.py | 52b3d916f4fc3941bb98c8b4f7698ab940680d09ee4e065de1f167857e3fd436 |
| authority.py | 804c7aff56538fc332bf68638b03b7167eccdb49f73337f1a5f1823348b522a4 |
| CLOSED-CHILD-CONTRACT.md | af7a2fab4aa6317f7386e438f2f03acc6daffdd04c3deee6a6554b675089ee81 |

## Verdict in one paragraph

No REFUTED item. The byte/argv interface (A) is CONFIRMED: the nine in-memory
authority objects and the nine expanded CAPRUN vectors that `bootstrap.commands()`
registers are field-for-field and byte-for-byte what `dispatch.Batch.authorize` and
`dispatch.Batch.run` recompute, and no registration-SHA/self-hash/PID cycle exists.
The closed-scope handoff (B) is CONFIRMED as observed-versus-registered with one
launcher-conditional STOP (umask). Clocks and failure semantics (C) are CONFIRMED
with one source-visible GAP: the dispatcher's 3000 s monotonic wall restarts at exec
and the bootstrap does not bind the absolute deadlines to `outer_started_utc`, so the
"3000 wall includes bootstrap" reading is ROOT-data-supplied, not source-enforced.
Decision (D): acceptable for ONE separately authorized AWS-only nine-phase
discriminator only after three one-line repairs (R1 umask, R2 kernel-read cap for
maps/mountinfo, R3 absolute-wall binding) or their explicit launcher preconditions.

## A. Byte/argv interface — CONFIRMED

**Authority objects.** For `valid`/`dummy`, dispatch.py:420-423 builds
`{schema, root_registration_path=str(self.path), job_tag, label, artifact=str(target),
science_outcome='NONE', source_files, limits=LIMITS, closed_scope=guard.leaves[label],
profile}`; bootstrap.py:424-426 builds the identical key set with
`root_registration_path=str(self.reg_path)` (the same string later passed as
`--registration`), `closed_scope=leaf` after `run()` has filled integer device/inode
(bootstrap.py:466-468), and `profile=PROFILES['control'|'dummy']` matching
dispatch.py:423 (`valid`→control, `dummy`→dummy). For the seven source entries,
dispatch.py:427-438 and bootstrap.py:429-437 agree on every key, on
`artifact.sha256 = '0'*64` for `startup-check` (dispatcher: `input_hash or '0'*64`
with `input_path=None`) and `'UNFORMED'` for produce modes, on the four per-label
mutations (`DISABLED`, `cpu_seconds '599'`, `del files['check.py']`,
`produce.py = '0'*64`) applied to copied dicts, and on
`runtime.native_inventory_sha256`: the dispatcher hashes the file live, the bootstrap
uses `pins[source_native_manifest]`, which bootstrap.py:329 requires to equal the
live hash. `mode` is `'produce'` for refuse-*/startup-produce and `'check'` for
startup-check in both. Serialization: dispatch.py:98 `json.dumps(sort_keys, (',',':'))
+'\n'` with default `ensure_ascii=True`, `.encode()` utf-8; bootstrap.py:69-71 the
same plus `allow_nan=False`, which changes nothing for int/str payloads. Byte
identity of the nine digests therefore holds whenever the registration the
dispatcher loads is the one the bootstrap serialized (bootstrap.py:471, dispatch.py:152).

**Expanded vectors.** dispatch.py:456-481 versus bootstrap.py:441-458: interpreter
flags `-E -s -S -B` for science/probe; probe tail `--registration REG --policy AUTH
--policy-sha256 DIGEST --mode LABEL --output TARGET` (dispatcher passes `digest`, the
bootstrap `supplied`; equal because only `refuse-hash` differs and it is not a probe);
science tail `--registered-job (WRONG-JOB|JOB) --authorization AUTH
--authorization-sha256 SUPPLIED (--input|--output) TARGET` with `WRONG-JOB` on the
two startup labels; `setpriv --reuid U --regid G --clear-groups --no-new-privs --`;
CAPRUN head `python -I -S -B caprun` with the eight closed-scope flags in the same
order, `--wall-seconds/--cpu-seconds/--rss-bytes` from the same profile row,
`--rss-sample-seconds 0.05 --term-grace-seconds 1`, stdout/stderr/telemetry files
`mount/<label>.{stdout,stderr,telemetry.json}`, `--cwd science --`. The typed-slot
tokens never occur (hex digests only), so dispatch.py:488-496 accept every label and
dispatch.py:497 compares equal. `supplied_sha256='0'*64` for `refuse-hash` matches
dispatch.py:454; authority.py:70-74 then fails the byte pin, which is the intended
refusal. `wrong-tag` reaches authority.py:25-29 (`REFUSED: registered CLI contract`).

**Numbers and strings.** The spec is loaded with `parse_float`/`parse_constant`
refused but integers permitted (bootstrap.py:134), which is necessary for
`uid/gid/durable_device/binding_wall_seconds` and the device/inode ints the
dispatcher demands (dispatch.py:303-304, 322-323). `place` stays four string
containers under the same `0|[1-9][0-9]{0,9}` regex as dispatch.py:211-215 and is
re-checked as strings by authority.py:110-116; no arithmetic is performed. Non-ASCII
kernel or path bytes raise in `small()`/`encoded()` and become BOOTSTRAP_STOP.

**No cycle.** Authority bytes carry the registration PATH only (dispatch.py:420,
bootstrap.py:424); the registration carries the nine authority digests inside
`commands`; the binding receipt carries `registration_sha256` and is not inside the
registration (bootstrap.py:472-479); the spec carries `bootstrap_sha256`; the CLI
carries the spec SHA; bootstrap.py:278 forbids spec/registration/binding paths in
`pins`, `source_pins` and the native file map. `outer_argv` is literally
`[python,-I,-S,-B,dispatcher,--registration,REG]` (bootstrap.py:251,
dispatch.py:219-220) with no PID or SHA. CONFIRMED, and TASK.md:37-44's claims hold.

**Untouched until dispatcher.** `authority_dir`/`frozen_dir` must be empty 0755 and
`writer_dir` empty 0700 child-owned (bootstrap.py:395-399) at every `outputs()` call
including the last one before exec; the only added file is
`mount/bootstrap-binding.json` (bootstrap.py:400-404), which dispatch.py:263 does not
forbid and dispatch.py:401-416 counts as metadata. Size boundaries agree:
registration and authority 65536 B (bootstrap.py:155,438 vs dispatch.py:66,99),
native manifest 1 MiB, simple/policy 64 KiB, `source_pins` 5..64, native files ≤3000,
directories ≤1000. Repeated pins: each science file must hash equal in `source_files`,
`pins` and `source_pins` and be 0444 (bootstrap.py:296-299), the same triple
authority.py:98-109 and dispatch.py:208,240,357-359 demand. Environment, cwd and
interpreter: the bootstrap evaluates on itself the same predicates the dispatcher
will evaluate after exec (`dict(os.environ)==ENV`, realpath(sys.executable),
`/proc/self/exe`, `sys.path==native.python_path`, mapped-file closure) and execs with
`ENV` after `chdir(wrapper)`; PEP 538 coercion is skipped because `LC_ALL=C` is set, so
`os.environ` survives exec unchanged. The mapped-closure the bootstrap needs is a
subset of the dispatcher's (its imports are a subset).

## B. Closed-scope handoff — CONFIRMED with one launcher-conditional STOP

- **One ROOT process, no outer parent, no thread.** bootstrap.py:370-372 requires
  outer `cgroup.procs` and `cgroup.threads` to equal exactly its own PID,
  `/proc/self/task` to be a singleton and `task/<pid>/children` empty, at every
  `observe()` (three times). A persistent launcher parent inside the domain makes
  this fail closed before any write. CONFIRMED (observed, not asserted).
- **Observed versus asserted.** Instance id via DMI asset tag with `i-[0-9a-f]{17}`,
  hostname, boot id, PID/cgroup/mount namespace links compared to both the
  registration/spec strings and to `/proc/1/ns/*`, exactly one cgroup2 mount at
  `/sys/fs/cgroup` with root `/`, own `/proc/self/cgroup` equal to the registered
  outer path, outer dev/inode captured once and rechecked, `cgroup.type=domain`,
  empty `subtree_control`, and five resource files compared literally to the spec
  (`memory.max 8589934592`, `memory.swap.max 0`, `pids.max 32`, `cpu.max.burst 0`,
  finite `cpu.max`). These are read from the kernel, not trusted from the spec. The
  `external_supervisor` block (armed/no-restart/covers-descendants/unit/deadlines)
  and `exclusive_root_contract` are asserted only, exactly as CONTRACT.md:190-193
  states. CONFIRMED / correctly labelled.
- **Fresh nine leaves.** `observe(False)` requires zero subdirectories; `run()` does
  `os.mkdir` per label (EEXIST stops), records dev/inode, and `leaf()` requires
  identity unchanged, domain, empty subtree_control, no subdirectories, root-owned
  0644/0444 interface files, `populated 0`, empty procs/threads; repeated after
  `commands()` and after the binding write. Matches dispatch.py:300-325. CONFIRMED.
- **GAP G2 (launcher-conditional STOP, partial creation).** `os.mkdir(p, 0o755)`
  (bootstrap.py:464) is subject to the inherited umask; `leaf()` calls
  `directory(p)` which demands `st_mode & 0o005 == 0o005` (bootstrap.py:103-104).
  Under a launcher umask that masks other-rx (077) the first leaf is created 0700 and
  the run stops with `ROOT traversable ancestry`, leaving one leaf for ROOT recovery.
  The dispatcher's `child_scope` does not need o+rx, so this is bootstrap-only.
  Repair R1: `os.umask(0o022)` before the creation loop (or `os.chmod(p,0o755)` after
  each mkdir). Until then, `UMask=0022` is a literal launcher precondition.
- **Native directory conflicts (GAP G5, minor).** bootstrap.py:278 excludes the
  registration path from the native file map but never checks
  `str(reg_path.parent) not in native.directories`; a registration placed inside an
  inventoried directory fails only at the post-write `audit_static` (bootstrap.py:481),
  i.e. after the side effect. Repair: add that one `need` to `audit_static`.
- **Stdio and descriptors.** fds 1/2 must be regular files on the tmpfs with the
  literal names (bootstrap.py:405-408, same as dispatch.py:269-273); all fds ≥3 are
  closed before exec (bootstrap.py:484-486). **GAP G4 (minor):** fd 0 is neither
  checked nor rebound, so `no_inherited_cgroup_fds` is enforced only for fd ≥3.
  Repair: require `/proc/self/fd/0 -> /dev/null` (or reopen it) before exec.
- **Immutable inputs / fresh outputs.** Spec and bootstrap 0444 with ancestry checks,
  re-hashed in each of three `audit_static` passes; registration and binding must be
  absent, distinct, outside the tmpfs (registration) or exactly
  `mount/bootstrap-binding.json` (binding); durable directory absent on ext4/xfs with
  integer device. Consistent with dispatch.py:256-276. CONFIRMED.

## C. Clocks, side effects and failure — CONFIRMED with GAP G1, G3

- **BEGIN placement.** `BEGIN = time.monotonic()` is bootstrap.py:25, after only the
  platform/euid/flag refusals and stdlib imports; every `clock()` requires
  `monotonic-BEGIN < 120` AND `utc() < binding_deadline_utc` AND
  `outer_started_utc <= utc() < outer_started_utc+3000 s` AND
  `utc()+20 s < mathematical_deadline` AND `utc() < admission_deadline` AND
  `utc() < external outer_deadline` (bootstrap.py:265-270). `clock()` runs at
  `audit_static` entry, per pinned file, per native directory, per leaf creation, and
  before the two writes and the exec. Both a relative and an absolute stop are
  checked, as TASK.md:91 requires. Deadline ordering `bind ≤ admission ≤ math < task
  < worker`, `outer_deadline ≤ task`, `retirement == worker` (bootstrap.py:223,231-232)
  is compatible with dispatch.py:281. CONFIRMED.
- **GAP G1 (source-visible, not fail-closed).** After exec, dispatch.py:150 sets
  `self.begin = time.monotonic()` afresh; its 3000 s joint wall (dispatch.py:332,546,
  717) therefore starts at dispatcher start, not at `outer_started_utc`. Nothing in
  bootstrap.py binds `mathematical_deadline_utc` (or `task_deadline_utc`) to
  `outer_started_utc + 3000 s`; bootstrap.py:267 only checks that fewer than 3000 s
  have elapsed *at bootstrap time*. So "exec does not reset clocks" is true for the
  external unit and the cgroup CPU counter (origin `'0'`, dispatch.py:193-195 accept
  it and bootstrap.py:381 bounds usage < 2050 s) but false for the dispatcher's
  logical wall; the end-to-end 3000 s wall is supplied by ROOT's absolute deadline
  data and the external supervisor, not by source. Repair R3: add
  `need(self.ends[1] <= self.outer_start + timedelta(seconds=3000))` in `__init__`
  (one line), which makes CONTRACT.md:237-238 source-enforced. Not a blocker if the
  spec is filled that way, but the contract sentence currently over-claims.
- **GAP G3 (host-conditional STOP).** `small()` caps every kernel read at 64 KiB
  including `/proc/self/maps` (bootstrap.py:322) and `/proc/self/mountinfo`
  (bootstrap.py:167); the dispatcher reads both unbounded (dispatch.py:116,131). A
  CPython process mapping libcrypto plus a snap-heavy mountinfo can plausibly exceed
  64 KiB, giving a bootstrap-only STOP (`kernel metadata cap`) that the dispatcher
  would never raise. Repair R2: a separate 1 MiB ceiling for those two files, or
  record the measured byte counts on the qualification host as a precondition.
- **Pre-side-effect barrier.** Everything in `__init__` (spec pin, own pin, skeleton
  shape, all static pins, native closure, identity, resources, empty topology, fresh
  outputs) precedes the first `mkdir`. A wrong CLI SHA fails at bootstrap.py:133
  before any write. CONFIRMED.
- **Exclusive writes and readback.** `exclusive()` uses
  `O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC`, mode 0444 plus explicit `fchmod`,
  `fsync`, parent `fsync`, whole-byte readback through the 0444/ancestry check, and
  both files are re-hashed against the recorded digests immediately before exec
  (bootstrap.py:154-162, 482). Registration is serialized once; the binding is a
  separate exclusive file that binds spec/bootstrap/registration SHA, process
  identity, guard, authority metadata, dispatcher argv, supervisor block and the
  original deadlines, and does not contain its own hash. CONFIRMED.
- **Failure and exec refusal.** `main()` catches `Exception`, prints
  `{status: BOOTSTRAP_STOP, science_outcome: NONE, error_type, reason}` to fd 1 (the
  capped `outer.stdout`), fsyncs, returns 2; a failed `os.execve` raises `OSError`
  and takes the same path with registration, binding and leaves retained; there is no
  retry, deletion, signal or fallback. Partial leaf creation is retained. The STOP
  record does not list which leaves/files exist (minor; ROOT inspects). CONFIRMED.
- **Not invented.** No aggregate CPU or realtime bound is claimed from sampling; the
  120 s and 64 KiB figures are planning restrictions; the supervisor is asserted.
  Interpreter preconditions visible in source: `sys.orig_argv` (≥3.10),
  `str.removeprefix` (≥3.9), `cpu.max.burst` (kernel ≥5.14), `/proc/<pid>/task/*/children`.

## D. Scoped decision

**Decision:** this exact code is suitable for ONE future separately authorized
AWS-only nine-phase discriminator, conditional on the genuine external
qualifications the contract lists, PROVIDED the three one-line repairs R1 (umask
before mkdir), R2 (maps/mountinfo read ceiling) and R3 (absolute wall bound to
`outer_started_utc`) are applied and re-pinned, or their launcher preconditions
(`UMask=0022`, measured maps/mountinfo < 64 KiB, spec deadlines ≤ outer start +
3000 s) are stated literally in the launch specification. The dispatcher interface
needs no change. G4/G5 are optional hardening. Code acceptance here is distinct from
actual preflight success, timing, strict dummy behaviour, native completeness,
source rows or any scientific outcome, none of which this review touches.

**Negative control (independently reasoned).** Launch under umask 077 with an
otherwise valid spec: expected `BOOTSTRAP_STOP`, `error_type RuntimeError`, reason
`ROOT traversable ancestry`, exit 2, exactly one leaf `refuse-status` present with
mode 0700 and `populated 0`, no registration, no binding, tmpfs inventory unchanged,
no dispatcher process. It exercises the partial-creation retention path and
distinguishes the bootstrap's `directory()` predicate from the dispatcher's.

**Minimal decisive matrix.** (1) Positive: dispatcher terminal
`CLOSED_SCOPE_PREFLIGHTS_9_CHECKED_NO_SCIENCE`, `CUSTODY.json` present, and the
binding's `registration_sha256` equal to custody `root_sha256`. (2) Wrong
`--spec-sha256`: STOP `metadata bytes/pin`, zero writes. (3) Pre-existing leaf
`cg/dummy`: STOP `exact outer leaf inventory`, zero writes. (4) Pre-existing
registration file: STOP `fresh distinct outputs`, zero writes. (5) `execution_mode
FULL_13` or a typed slot in the skeleton: STOP `disabled nine-only skeleton`, zero
writes. (6) `binding_deadline_utc` in the past: STOP `original bootstrap/outer
deadline; no reset`, zero writes. (7) Spec from a previous boot: STOP `ROOT namespace
bindings`. (8) Unit `SystemCallFilter=~execve`: STOP `PermissionError` after both
writes, registration and binding retained, no dispatcher. (9) umask 077 as above.
Each must fail without dispatch or retry and leave partial state visible.

**Acceptance perimeter.** Accepted: the byte/argv equivalence of the nine
authorities and vectors; acyclic pin structure; observed-versus-registered identity,
topology and resources; exclusive/fsynced/readback writes; fail-closed STOP with
retained evidence. Remaining preconditions before the discriminator: R1–R3 (or their
literal launcher statements); ROOT approval of spec/code hashes; launcher, native
closure, host namespace, cgroupfs/xattr support and watchdog qualification; the
seven refusal strings in the preflight policy; the CAPRUN-CC-1 runtime scope as
already accepted. No authority for that test is granted by this review.

## Custody

- First action 16:17:58Z; skeleton+A+B written 16:26Z; this section written after
  the second input postpin at the UTC printed in the lane log.
- Post-write re-hash of all eight inputs (taken immediately before and again after
  this final write) equals the pre-read table above; no input changed.
- Only this file was written, via the installed `apply_patch`, in two bounded
  writes; no other file, no finalizer, no `charge_basis` line (no exit price is
  asserted), no execution of any inspected program.
- Whole readback of this report follows the final write in the lane log.

<!-- BODY-END -->
