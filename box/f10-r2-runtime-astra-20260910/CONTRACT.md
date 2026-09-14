# First r2 runtime entry — STATIC ONLY

No command, fixture, authorization or mathematical import was run. This is a
new source candidate requiring FIRST independent static review and a separate
ROOT registration. The disabled JSON rejects before creating a file. Its
placeholders are not deployment values or authority.

## Exact layout and native intake

ROOT prepares a root-owned traversable 0755 science directory containing ONLY
authority.py, arithmetic.py, produce.py, check_arithmetic.py, check.py, each
root-owned 0444 with the five literal accepted hashes. No copy or edit of those
files is part of this publication. A DIFFERENT root-owned 0755 wrapper directory
contains ONLY dispatch.py and probe.py, root-owned immutable readable files.
ROOT registration and native manifest live outside both directories.

The outer invocation is the literal registered vector:
PYTHON -I -S -B DISPATCH --registration ROOT_REGISTRATION.
ROOT clears the environment to exactly PATH=/usr/bin:/bin, LANG=C, LC_ALL=C,
TZ=UTC. The wrapper itself imports standard-library metadata modules only.
Science uses PYTHON -E -s -S -B SCRIPT so sibling imports remain possible;
the probe explicitly inserts ONLY the checked five-file directory before
importing the actual authority module. No arithmetic is imported by the probe.

The native manifest uses the already-reviewed f10-native-closure/v1 shape:
schema, files, directories, aliases, absent, python_path. files maps canonical
absolute paths to hashes; directories maps canonical directories to sorted
EXACT immediate names, each recursively classified as file/directory/alias;
aliases maps every allowed noncanonical path to its canonical registered target;
absent records absent paths (including a nonexistent Python ZIP search entry);
python_path is the exact outer -I -S sys.path. Include interpreter, setpriv,
CAPRUN's ps aliases, libraries, extensions, all selected stdlib files and pyc
bytes. A present ZIP is pinned as a file; a missing ZIP is checked absent.
No site/PYTHONPATH loading is enabled. Actual mapped native files and aliases
of the ROOT wrapper, observed runner and observed scientific child must belong
to that manifest. The manifest is not inferred from the science's format-only
native digest check. ROOT obtains and freezes the inventory separately.

The wrapper authenticates root registration bytes, each actual path role,
science bytes, complete inventoried directory contents, native bytes/aliases,
host/instance/boot/PID namespace, exclusive cgroup and its memory.max before
each launch. All ancestors must be root-owned, traversable and not writable by
group/other. Files in native OS paths may be root-writable, but are freshly
hashed; science is exactly 0444. ROOT registration is exactly 0444. This is a
trusted-ROOT/no-concurrent-writer contract, not an attacker-resistant filesystem
snapshot against another root writer.

## Registered output ownership

Working output is a fresh exact tmpfs mount of at most 16777216 bytes, root 0755,
with three empty immediate children: authority_dir root0755, frozen_dir root0755,
writer_dir registered UID/GID0700. Outer fd1 and fd2 MUST be literal
output_mount/outer.stdout and output_mount/outer.stderr on that tmpfs. ROOT
creates those two redirected files; all code/native files remain outside it.
The producer packet has a 15728640-byte cap and all other files together a
1048576-byte metadata reserve. The aggregate mount cap is hard; the partition
checks are sampled stat-only checks and fail closed if exceeded, not a claim
of a hard per-directory quota. RLIMIT_FSIZE=15728640/core0 is inherited by each
CAPRUN. ROOT provisions the exclusive cgroup memory.max=2147483648 and an
independent original wall/worker stop. No caller command sets up mounts, units,
accounts, installation, worker state or runtime authority.

ROOT also registers an ABSENT durable directory under root-owned ext4/xfs EBS
with the literal parent device. The caller copies there ONLY after its owned
cgroup is quiet, verifies every copied file hash, fsyncs each file, every
directory and the durable parent. Working artifacts are not deleted. ROOT
collects only after the dispatcher is terminal and owns recovery/capture on
STOP, signal, incomplete copy, or an occupied cgroup.

## Commands, authority and allocation

The fresh registration fixes exactly the eleven commands named in the disabled
template. Each contains the unchanged CAPRUN SHA, absolute interpreter and
setpriv roles, exact argv, output paths and the deterministic hash of that
label's science authority. Authority bytes are canonical sorted compact JSON
plus newline; they are created exclusively and fsynced 0444 INSIDE the run,
then current hash/native/role/cap barriers run again before Popen. No posthoc
manual authorization is permitted. The exact accepted authority fields are:
job_tag, status=REGISTERED, authority=ROOT-CAPRUN, files=five literal SHA map,
runtime={python_sha256,native_inventory_sha256}, limits=the four original
string-valued joint limits. No extra field is added to science's exact schema.

CAPRUN launches setpriv --reuid UID --regid GID --clear-groups --no-new-privs --
PYTHON -E -s -S -B ENTRY followed by the science's exact eight CLI arguments.
The setpriv process execs in CAPRUN's recorded child session: no inner PGID.
All full command vectors must equal fresh ROOT commands before Popen.

Nine mandatory preflights precede mathematical work:

1. Wrong status: exact no-ROOT-contract refusal; no payload.
2. CPU-limit string changed to 499: exact limits/inventory refusal.
3. check.py removed from derivative inventory: same exact refusal.
4. produce.py digest replaced by zeros: exact source-pin refusal.
5. supplied authority hash replaced by zeros: exact bytes/pin refusal.
6. Valid actual authorize call through the no-math probe: POST_AUTHORIZE only.
7. Actual produce.py startup with WRONG-JOB: explicit-tag refusal before math.
8. Actual check.py startup with WRONG-JOB: same, before any input read.
9. Reviewed descendant mechanism: leader exits, orphan touches 64MiB, ignores
   TERM; a 32MiB group-RSS cap must produce actual TERM then KILL and complete
   reaping with the exact four-event identity sequence. No fabricated fixture.

Controls are 5 wall/3 soft CPU each. Dummy has 32MiB RSS; other controls use the
original 2GiB ceiling. Producer is 300 wall/239 soft CPU, checker 210 wall/169
soft CPU. Nine controls plus two phases total 555 registered wall seconds.
Including CAPRUN's +1 hard CPU per child gives 446 child CPU seconds, leaving
54 of the original500 for wrapper/runner/cleanup; 45 of600 wall remains.
The caller samples cgroup CPU from its initial baseline, stops launching at480
and demands <=500 after return. This is not an assertion that sampled CPU is
a new hard cgroup CPU quota. CAPRUN supplies each hard child limit. ROOT's
fresh cgroup and original external cutoff cover the runtime envelope. Expensive
metadata or slow phases may cause a NONDECISION, never a cap extension.

Every launch reserves wall+15 within original600 and absolute mathematical
cutoff. One producer only, conditional one checker only, no retry. Actual full
CAPRUN/science argv, PID/PGID/startticks/boot/ns/UID/GID/caps/native mappings and
limits are captured promptly. Fast controls may honestly miss live capture;
either mathematical phase missing required live capture gives GAP, no retry.
Terminal telemetry, stream hashes and payload bodies are read only after
quiet. Live checks read process metadata and output sizes, not output bodies.

## Terminal science binding and limitations

Producer must return the literal FORMED_UNCHECKED_19_ROWS_NO_SOURCE_OUTCOME.
Its packet is not parsed by this caller: it is hashed, MOVED (not copied) into
the root-owned frozen directory, chmod0444, with directory fsync. The checker
receives that exact input; its pre/post SHA and source/native pins are bound to
the exact CHECKED_STATIC_CONTRACT_19_ROWS_32_RESIDUALS_80_SLOTS_NO_SOURCE_OUTCOME
stdout and CAPRUN telemetry. The frozen directory becomes0555. Any failure is
STOP_NONDECISION or STOP_CUSTODY_INCOMPLETE, never source acceptance.

Science gate qualifications remain: the fifteen original controls are SPEC,
not executed results; 103 wire_p calls; corrected late -6; nonlinear Psi length
is checked late; formal forcing mutations need not be packet mutations. This
caller neither reruns those fifteen controls nor claims them passed. No actual
reconstruction, full-source point, ideal/unit decision, rank, speed or JC2
conclusion is supplied. ROOT alone schedules FIRST review and later runtime.
