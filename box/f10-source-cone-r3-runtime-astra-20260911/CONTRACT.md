# Fixed-r3 runtime contract — DISABLED / STATIC / UNEXECUTED

No file here authorizes AWS, registration, installation, a dummy or science run.
ROOT alone may act after FIRST review of this new runtime and mutator. Source
FIRST clearance was subsequently attested by ROOT during authoring; no new
review body is an input and no measured feasibility is asserted.

## Fixed layout and startup trust

ROOT registers a canonical root0444 JSON at a literal absolute path. Exact
five-file science directory is root0755 with the five pinned root0444 source
files. A separate root0755 wrapper directory has exactly dispatch.py, probe.py,
mutate.py, each root0444. No frozen source or accepted CAPRUN is changed.
Paths have root-owned traversable ancestry, no group/other write, no symlink
ambiguity, spaces or shell syntax. Native OS files may remain owner-writable,
but are ROOT-owned, not group/other-writable and rehashed at each barrier.
This is a trusted ROOT/no-concurrent-writer model, not protection from hostile
ROOT changing inputs after their checks.

Outer argv is `PYTHON -I -S -B DISPATCH --registration ROOT_JSON`, exact literal
canonical interpreter and wrapper cwd. Its environment is exactly PATH=/usr/bin:/bin,
LANG=C, LC_ALL=C, TZ=UTC. Science/probe use `PYTHON -E -s -S -B SCRIPT ...`;
the probe inserts only the checked science directory and imports actual
authority, never arithmetic. Mutator uses `PYTHON -I -S -B MUTATE ...` and
imports scientific arithmetic only after its registration/host/source/input
barriers. setpriv drops to the literal nonzero UID/GID, clears groups and sets
no-new-privileges; it execs the Python child in CAPRUN's existing session.
No second supervisor or inner process group is introduced.

ROOT pins python, setpriv, unchanged CAPRUN, dispatcher/probe/mutator, source,
both native manifests and all actual paths. The FULL native manifest has
exactly schema/files/directories/aliases/absent/python_path, schema
f10-native-closure/v1, at most1MiB,3000files/1000directories. Exact recursive
directory inventories include startup stdlib/pyc/extension/shared-library
bytes, loader/ps aliases, expected absent ZIP paths and exact outer sys.path.
All observed mapped files of caller/runner/child must be in that closure.

The distinct SOURCE native manifest is at most64KiB, exact keys job_tag/files,
with the r3 source tag and a nonempty canonical file subset INCLUDING the actual
interpreter. Every entry must equal its FULL closure pin. The subset is
ROOT-selected for the source's extra native check; it does not replace the
full startup closure. ROOT must form actual inventories later; none exists here.

## ROOT authority and thirteen commands

The disabled template fails before writes. An enabled ROOT registration binds
the original EC2 instance, hostname, boot ID, PID namespace, exclusive cgroup,
8GiB memory.max, all caps, exact command vectors and four immutable UTC stops:
admission <= mathematical < task < worker. ROOT registers the cgroup's
aggregate_cpu_start_usec before launch; it is no later than observed usage,
so initialization/runner/child/copy CPU is not omitted from aggregate accounting.
This origin is not reset between phases. The independent ROOT external stop
is still required; sampled cgroup CPU is not a hard aggregate quota.

Nine no-math preflights, in order: refuse-status, refuse-caps, refuse-inventory,
refuse-source, refuse-hash, valid, startup-produce, startup-check, dummy.
Then produce, check-positive, mutate, check-negative, exactly once each.
Any unexpected outcome stops; no retry or repeated positive reconstruction.

Every CAPRUN argv is `PYTHON -I -S -B CAPRUN --wall-seconds W --cpu-seconds C
--rss-bytes R --rss-sample-seconds 0.05 --term-grace-seconds 1 --stdout-file OUT
--stderr-file ERR --telemetry-file TEL --cwd SCIENCE -- SETPRIV --reuid UID
--regid GID --clear-groups --no-new-privs -- PYTHON FLAGS SCRIPT ...`.
ROOT supplies every literal path/argument. Science tail is the actual eight
arguments `--registered-job TAG --authorization AUTH --authorization-sha256 SHA
--output OUT` (produce/probe) or `--input IN` (checker). Wrong-tag entries use
WRONG-JOB. Probe prefix is `--science-dir SCIENCE --mode authorize|dummy --`.
Mutator tail is `--registration ROOT_JSON --root-registration-sha256 ROOT_SHA
--positive-record AUTHORITY_DIR/positive.json`.

Science authority has EXACT keys job_tag/status/authority/mode/artifact/files/
runtime/limits; status REGISTERED, authority ROOT-CAPRUN, fixed source tag/pins,
mode produce or check, artifact exact path and UNFORMED for producer or actual
frozen SHA for checker. Runtime contains interpreter SHA plus SOURCE native
inventory PATH and SHA. Authority files are derivative records of ROOT's
registered exact program, phase policy, paths, caps and pins—not child-supplied
or predeclared mathematical outcomes. They are exclusive-written, fsynced,
root0444 and rehashed immediately before launch.

Necessary binding amendment expressly approved by ROOT during this task:
only check-positive/check-negative may contain token AUTHORIZATION_SHA256,
exactly once immediately after their unique --authorization-sha256 flag.
It is replaced only by the newly frozen actual authority hash, after independent
quiet/freeze of its input and exact fixed ROOT mode/path/source/native/limit
derivation. Only mutate may contain ROOT_REGISTRATION_SHA256 exactly once at
its unique named flag. Missing, duplicate, misplaced or other-phase tokens
are rejected. No other argv byte is substituted, and expanded argv is captured.
This is necessary because future artifact SHA cannot be stored literally in
pre-run ROOT JSON; no general expansion or finder-selected metadata is allowed.

Positive phase record is root0444 at ROOT's literal authority_dir/positive.json,
created ONLY after normal exit0, exact success stdout, empty stderr, quiet,
input rehash and all current barriers. It binds ROOT SHA, literal phase policy,
baseline path/SHA/bytes, source pins, positive authority path/SHA and stdout SHA.
Mutator checks that immutable record against ROOT policy, host and source pins,
then invokes actual authorize('check') on the same baseline before parsing it.
No free future input-pin placeholder is needed for mutator.

## Exact preflight and scientific predicates

Probe catches the actual authorize ValueError, emits only `ValueError: MESSAGE`
plus newline, exits1 and never creates its sentinel on failure. Five exact
messages are respectively `no ROOT registration`, `registered limits/source
inventory`, the same inventory message, `source pin: produce.py`, and
`authority/inventory byte pin`. These are real exception values, not old r2
SystemExit strings. Changes are status DISABLED, source CPU string599 instead
of600, removed check.py entry, zeroed produce.py SHA, and supplied authority SHA
all zero. The valid authorize probe produces only its POST_AUTHORIZE identity
event. Both actual wrong-tag entries must exit1 with exactly `REFUSED: registered
CLI contract` plus newline, empty stdout, no output/input file. Their unused
checker authority carries a zero pin for an absent path; no fixture is created
and the literal tag must reject before loading it.

Dummy preserves the inherited no-math fork/pipe control: leader emits/start
identity, descendant ignores TERM, leader exits, descendant touches64MiB and
waits. Required four events retain actual parent/child identities. CAPRUN must
report RSS above32MiB, resource=rss, matched original leader PID/PGID/start
identity before both signals, TERM15 then KILL9 sent, complete cleanup and
leader reap. Dummy failure is not a mathematical outcome.

Producer success is exact stdout
`FORMED_UNCHECKED_R3_25_SLOTS_NO_SOURCE_OUTCOME` plus newline, exit0, empty stderr.
Positive checker requires exact stdout
`CHECKED_R3_25_GRAPH_SLOTS_45_LOW_108_JACOBIAN_NO_SOURCE_OUTCOME` plus newline,
exit0, empty stderr. Both run actual unchanged source files; no wrapper verdict
replaces the checker.

Mutator performs exactly `graph.slots[24] += X1^27`. It uses four decimal-string
exponents and seven reduced rational coordinates; only coordinate0 of exponent
(27,0,0,0) changes by1. Absent term is inserted in numeric exponent order; an
all-zero changed vector deletes its term. All other document content is retained.
Canonical whole input bytes must be restored by replacing the original slot;
fixture and baseline hashes must differ. Mutator neither calls a checker nor
claims PASS. Baseline plus fixture must fit120MiB jointly. Term/decimal/wire
caps can still cause NONDECISION; no feasibility promise or quota expansion.

Negative checker must have NORMAL_EXIT/exit1, no signal/resource, empty stdout,
and the ENTIRE bounded ASCII traceback. Four exact frames are check.py540
module/main(), check.py536 main/print(check_file(path)), check.py520 check_file/
eq(p,rawrow,'all25 literal graph rows '+label), check_arithmetic.py227 require/
raise ValueError('CHECK FAILED: '+label), with the exact literal source spacing
encoded in dispatch.py. Only one bounded native caret line per frame is allowed.
Final line is exactly `ValueError: CHECK FAILED: all25 literal graph rows T`.
No extra frame, exception chain, substring match, parser refusal or resource
stop counts. The other five semantic controls remain NOT_RUN/SPEC.

## Caps, physical capture and custody

Source LIMITS remain900wall/600CPU/8GiB/128MiB PER invocation. NEW aggregate
planning envelope is3000wall/2100CPU/8GiB exclusive cgroup/128MiB tmpfs.
Three science profiles each900wall/599softCPU (hard600); mutator30/20 (hard21);
nine preflights5/3 (hard4), with dummyRSS32MiB. Thus2775wall and1857hard child
CPU, leaving225wall/243CPU for caller/runner/cleanup. All quantities UNMEASURED.
Code samples aggregate CPU and terminates an in-flight phase at2050 with50
seconds remaining nominal cleanup allowance; every return/custody step must
remain within2100. This is not a kernel hard aggregate CPU quota. ROOT's original
external stops remain necessary. Late/missing telemetry or capture is a GAP,
never a retry or a mathematical negative.

Output mount is a fresh exact128MiB-or-smaller tmpfs with root0755 authority
and frozen directories and UID/GID0700 writer directory, all initially empty.
All code/native/registrations stay outside it. Outer stdout/stderr are literal
regular files on this mount. Packet bytes are summed across producer/baseline/
fixture paths and limited to120MiB; all other files/logs jointly8MiB. The full
source's128MiB individual wire allowance does not promise two packets fit.
Live size checks are stat-only; inherited RLIMIT_FSIZE is120MiB, core zero.
Quota checks are sampled within the aggregate tmpfs hard bound.

Actual runner/child captures include argv, PID/PGID/start ticks, boot/namespace,
UID/GID, caps, limits, cgroup and mapped files. Fast preflights may miss live
capture and report that honestly; producer, positive checker, mutator and
negative checker require observed runner and Python identity, else GAP/no retry.
Revalidate ROOT/source/native/host/caps immediately before every launch, and
authority/input pins before and after. Terminal group-quiet is checked BEFORE
telemetry, stream bodies/hashes, event/receipt/baseline/fixture reads or custody.

Producer packet is MOVED, fsynced, root0444 and hashed before positive check.
Fixture and mutation receipt are likewise MOVED/frozen before negative check;
frozen directory becomes0555 after its complete inventory. Source baseline is
never copied to create a second live working baseline. Durable copying begins
only after owned cgroup quiet, to a fresh registered ext4/xfs EBS target with
registered device identity; every file is byte-rehashed and fsynced, then all
directories and durable parent fsynced. Working artifacts remain. No deletion,
unmount, restart, worker control or hidden cleanup is included.

Final runtime status, if all future observations pass, is only
RECONSTRUCTION_AND_MIXED_ROW_REJECTION_CHECKED_NO_SOURCE_OUTCOME. It implies
neither a source point nor source zero, rank, place, fieldness, solver result,
degree exclusion or JC2. This publication reports NONE of those observations.
