# One service-entry launcher — STATIC / UNEXECUTED

This packet supplies launcher.py, not an installer/controller, enabled card,
unit deployment or worker authority. It has one entry and one successful
exec path. Python is justified by exact JSON/pin/clock handling without
shell substitution, jq or an additional helper. It imports no campaign code.
The repaired bootstrap f04f1b7b... is unchanged. Its reviewed scope is
imported from the frozen INTAKE, not re-reviewed here.

## Original epoch and acyclic ordering

The bootstrap field outer_started_utc is interpreted here as the ORIGINAL
OUTER-TASK/WATCHDOG EPOCH, not the later service process-start timestamp.
This is the expressly permitted conservative interpretation. ROOT observes
the actual first activation of the independently managed monotonic timer:
ActiveEnterTimestamp (UTC, whole seconds) and
ActiveEnterTimestampMonotonic (decimal microseconds). The former rounds
down within the observed second; it is not a future or guessed timestamp.
The launcher compares both literal properties to its approved card, checks
the elapsed monotonic and UTC intervals, and records the distinct actual
ExecMainStartTimestamp/Monotonic, ActiveEnterTimestampMonotonic, MainPID and
InvocationID. No timestamp is manufactured from a planned service start.

ROOT performs these finite steps, with no holder/FIFO:

1. Before allocation, finish source FIRST, method/schema review, known code
   vectors, unit-name/path choices and the host qualification procedure.
   No installed/native/host fact can yet be asserted.
2. On the separately authorized host, qualify the exact installed tools,
   native closure, cgroup/ACL/null/namespace/stdio behavior. Prepare immutable
   source files and a fresh constrained task slice. Prepare the exact two
   ordinary watchdog units whose bytes watchdog_units() specifies. ROOT owns
   the independent worker retirement mechanism and its qualification.
3. Arm the monotonic watchdog once, BEFORE producing the epoch-bearing spec.
   Record its actual paired activation properties. This is the original
   epoch. All subsequent spec/card freezing, unit installation/readback and
   handoff time is charged from it. Worker-side administrative CPU/RSS/PIDs
   after this epoch must be in the fresh accounting task slice; the supplied entry
   requires the literal parent slice and its original zero-origin counters.
4. ROOT finalizes and approves the immutable bootstrap spec, then the launch
   card containing its SHA. The card contains no card SHA or outer-unit SHA.
   ROOT creates the exact outer unit rendered by outer_unit(), which includes
   the card SHA in ExecStart. The watchdog references only the already chosen
   outer-service and task-slice NAMES; no hash cycle exists. ROOT separately binds the final
   unit/card/spec readback in its launch commitment OUTSIDE these artifacts.
5. ROOT reloads and independently verifies the EFFECTIVE loaded properties,
   absence of overrides/old invocation/outer cgroup, unchanged timer and
   original clocks, then explicitly starts the one unit. The source does not
   start a unit, mint approval, install, arm/reset/cancel a timer or retry.
   A stale cached unit is not qualified merely by matching the file bytes.

Step5 is a concrete ordinary systemd start of the rendered unit, not an
unimplemented second controller. The source implements the service entry:
env -i clears systemd's injected variables; that execs pinned Python with
-I -S -B and the launcher; launcher observes/reaps its read-only systemctl
children, then execve's pinned Python with the bootstrap's exact argv/ENV.
Finally bootstrap execs the dispatcher. These execs keep the service PID;
no entry parent/holder remains in the outer cgroup. Actual active/running
state and same MainPID/ExecMainPID are required before handoff, so the
RuntimeMax clock is already active rather than merely promised.

## Exact source interface and bounds

CLI: PYTHON -I -S -B LAUNCHER --card CARD --card-sha256 SHA256.
Metavariables are explanatory, never runtime substitutions. All paths are
canonical ASCII without spaces/metacharacters. Exactly the KEYS in source
form schema r3-bootstrap-launch/v1. No example with approval is issued.
The only passing approval string, ROOT_APPROVED_PREFLIGHT_LAUNCH, must be
issued externally together with the CLI expected SHA and reviewed source.
It is not authentication by itself. The card is canonical UTF-8 JSON plus
newline, ROOT0444, no writable ancestry/ACL, at most256KiB; duplicate keys,
floats, nonfinite numbers and noncanonical bytes are rejected.

The card pins launcher, its FIRST, launcher/native/accounting/retirement
qualification references, the three exact tools (Python/env/systemctl),
bootstrap path and spec SHA. Tool and launcher pins must also appear in the
bootstrap registration vector. It fixes four distinct simple names matching
r3bootstrap[a-z0-9]+ with service/slice/timer suffixes, the earlier epoch's
literal UTC/raw/monotonic values, exact task-slice path/device/inode and
qualified integer CPU quota percent. Qualification references concern the
reviewed method and prior installed observations; they cannot recursively
contain this card or future unit digest. Final actual launch readback is
retained separately by ROOT.

The three rendered unit texts are literal and must exist ROOT0444 under
/etc/systemd/system; no drop-ins are accepted. The outer uses Type=exec,
env -i, exact bootstrap-compatible ENV, actual null stdin, original appended
tmpfs streams, root UID/GID, no delegation/restart, control-group TERM/KILL,
8GiB/swap0/Tasks32, normal scheduler, 10ms CPU period and the SAME qualified
quota as the spec (1..69 percent). cpu.max.burst=0 remains an observed
outer/ancestor condition. The task slice accounts the administrative and
outer hierarchy; entry checks its literal identity/resources/current CPU,
while historical coverage and absence of uncharged administrative work
remain an explicit ROOT qualification, not something a counter proves.

Entry requires both clocks to be less than100seconds from the original
epoch, paired drift at most2seconds, and the original binding deadline still
future. This leaves nominal20seconds before epoch+120 but is NOT a liveness
forecast. RuntimeMaxSec=2875 plus TimeoutStopSec=5 is a conservative service
envelope: active entry before epoch+100 implies termination budget before
epoch+2980, hence below the unchanged3000-second whole-task ceiling. The
independently prearmed OnActiveSec=115 watchdog is the SELECTED stricter
original monotonic stop path: stop at epoch+115, with the outer's five-second
TERM/KILL budget. Its exact stop command names BOTH the outer service and
the exclusive task slice, covering any still-running administrative unit.
ROOT must qualify that slice-stop propagation and every administrative
member's at-most-five-second termination contract. The watchdog service
itself stays OUTSIDE that slice. It bounds this ONE experiment as a whole
by epoch+120 under the qualified OS supervision contract. These are not hard realtime
proofs under unbounded scheduling/I/O delay. No scientific phase cap changes.
All nine old preflights and strict dummy remain the sole future workload.

Original binding/admission/math/task/retirement UTC deadlines are unchanged;
the bootstrap additionally checks its own120-second monotonic interval.
The bootstrap checks ALONE do not establish an epoch-relative120-second
monotonic binding bound if realtime rolls backward after entry. The chosen
whole-experiment115+5 watchdog closes that ordering issue without a separate
binding monitor or cancellation protocol: binding and all subsequent work
are stopped together. It is not cancelled on successful bootstrap exec.
All setup, entry, bootstrap, dispatch and custody costs consume the SAME
interval. No assertion that they fit is made; a timeout remains STOP even
if all metadata or preflights have not finished. ROOT suggested this stricter
configuration during the task; no observation is imported. Missing actual
watchdog qualification is STOP/no registration, not a
reason to relax the bootstrap. CPU origin zero in the outer remains intact;
whole-task ancestor accounting is additional external coverage, not an
inference that outer counters contain work done before the outer existed.

## Evidence and negative traces

The entry emits one bounded16KiB record into the original stdout and fsyncs it.
LAUNCH_ENTRY_CHECKED_NOT_BOOTSTRAP_RESULT means only the entry checks passed.
It records actual service identities separately from the original epoch.
It then closes descriptors>=3 and uses literal execve. Any exception yields
LAUNCH_STOP/exit2, never retry or fallback. No authority, registration, cgroup
leaf or standalone output file is written by this launcher. ROOT retains
unit/card/spec/timer records and streams; bootstrap/dispatcher retain their
own failure/custody obligations. No positive preflight result is exported.

Static controls, NOT run: (a) change the epoch in a canonically rehashed,
newly approved card/spec while preserving the real timer; the exact paired
timer-property comparison rejects. A genuine but older epoch with elapsed
100seconds or more fails admission even if the timer is still waiting.
(b) Keep the approved card SHA but provide different spec bytes: load(spec)
fails before systemctl observations or bootstrap exec. These controls do
not count stale-card-hash failure as exercising the epoch predicate.

Unqualified future facts: exact systemd property rendering and cached/effective
unit correspondence; env/exec/PID behavior; scheduler/watchdog operation;
native completeness, cgroupfs/ACL/null modes,64KiB ASCII snapshots; clocks;
fresh task accounting and outputs; total admission/lookup/hash duration.
One different-model actual-code FIRST and separately ROOT-registered AWS
qualification are required. No execution, installed readiness, source result,
worker allocation or fallback authority follows from this packet.
