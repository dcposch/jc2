# Binding sequence contract — STATIC / UNEXECUTED

One entry: qualified PYTHON -I -S -B
/opt/jc2-r3-bootstrap-20260912/administration/bind_once.py
--seed-sha256 ACTUAL_ROOT_SEED_SHA. No seed or authority is issued here.
The exact original PATHS remains immutable. The inert additions are the
administration/bind_once.py source, metadata/binding-seed.json,
r3bootstrap20260912bind.service, and the private0700 directory
/var/lib/jc2-r3-bootstrap-20260912/preparation/binding.

## Exact pre-epoch seed interface

Canonical compact sorted ASCII JSON plus LF, no duplicate keys, floats or
nonfinite numbers, <=262144 bytes, ROOT0444 under ACL-free ROOT0755 metadata
ancestry. The independently registered CLI SHA authenticates its exact bytes.
Top-level keys are exactly:

schema, approval, source_sha256, source_first_sha256, qualification_files,
loaded_unit_mapping_qualification_sha256, spec, card, offsets,
epoch_not_before_utc, epoch_not_after_utc, worker_deadline_utc.

schema = r3-bootstrap-bind-once/v1. Only ROOT may issue approval
ROOT_APPROVED_BIND_PREFLIGHT_ONLY_9 after actual-code FIRST and actual-host
qualification. This author supplies neither. source_sha256 pins bind_once;
source_first_sha256 identifies its future actual-code FIRST. qualification_files
is a 1..16-entry canonical absolute path -> SHA map of immutable ROOT records
(each <=256KiB), containing every referenced FIRST and qualification SHA.
The code authenticates record bytes, NOT truth or approval semantics.
loaded_unit_mapping_qualification_sha256 names the separate prior installed
systemd mapping qualification. All these records precede the original epoch.

spec and card have exactly the unchanged bootstrap SPEC_KEYS and launcher
KEYS, respectively. ROOT supplies their genuine approval strings, all frozen
source/review/host/native/accounting/exclusivity/retirement fields and the
complete disabled PREFLIGHT_ONLY_9 registration skeleton. No source/authority
contract is synthesized here. Source limits/profiles, all source bindings and
the exact nine phases are retained; unchanged bootstrap remains the exhaustive
validator. No program source is imported, evaluated or executed to compose.

The ONLY late seed slots are:

- spec.outer_started_utc and binding_deadline_utc: null;
- spec.external_supervisor.already_armed and outer_deadline_utc: null;
- registration admission/mathematical/task_deadline_utc: null;
- card.spec_sha256, epoch_utc, epoch_timestamp_raw,
  epoch_timer_monotonic_usec, task_scope_device, task_scope_inode: null.

All registration outer/leaf device/inode nulls remain null; only bootstrap
later observes/fills them. Its commands remain {}, typed_slot_policy {},
phase_policy null, enabled false. Root supplies the actual independent absolute
worker_deadline_utc identically in seed/registration/external retirement field.
Other nulls/placeholders are not permissions to invent data; the complete
unchanged bootstrap validates the finished specification.

offsets has exactly binding/admission/mathematical/task/outer INTEGER seconds,
all positive <=3000; binding<=120; binding<=admission<=mathematical<task;
outer=120<=task. They are ROOT-chosen BEFORE the epoch, not adjusted to a run.
All absolute deadline strings are offset-explicit +00:00 UTC. The actual
watchdog activation must lie in the preapproved closed epoch window. A late
activation which pushes task cutoff past the fixed worker cutoff is STOP.
No passing example, current physical facts, dates or reference values are
fabricated. The exact field table plus frozen inherited schemas is the usable
seed contract; no generic template expansion exists.

## Service and installed-state contract

service.template is inert and cannot start with its unresolved seed hash.
ROOT installs the source first, then freezes the genuine seed, then renders
the ordinary administrative unit containing that SHA. It starts as ROOT in
the fresh constrained task slice; neither existing-session migration nor an
outer holder is used. Actual task cgroup must initially contain exactly this
administrative child directory, whose procs contains only this process.
The parent carries memory8GiB/swap0/pids32/cpu6900 10000/burst0. Its historical
zero-origin/exclusivity and root-only migration surfaces are externally
qualified. The administrative service has control-group TERM/KILL, no restart,
120-second RuntimeMax and five-second stop budget. The unchanged watchdog
stops BOTH eventual outer service and task slice and remains outside that slice.

The source checks actual service identity, own argv/environment, current
EC2/DMI/boot/namespaces, parent resource values and tool/source SHA bindings.
ROOT must separately qualify loaded admin RuntimeMax/dependencies/slice-stop
propagation, namespace/cgroupfs/ACL semantics, accounting, native closure and
independent worker retirement. No earlier seven-refusal replay is required.
Admin systemctl children inherit this cgroup and are waited/reaped. PID1/SSH
daemon CPU is not claimed as task-owned CPU. No detached helper is authored.

Before native collection ROOT has already installed all static sources and
created metadata, administrative evidence and unit-file parent directories.
Two consumed native manifests are already installed ROOT0444, byte-compared,
hashed and fsynced from PRIVATE0700 assembler outputs. This program does not
collect native data or copy the manifests. env/systemctl/Python require literal
canonical FILE entries. Metadata, /etc/systemd/system and evidence directories
must not be exact native-directory inventory members. Spec/card/registration,
seed and the seed-pinning admin unit cannot occur in native.files, source_pins
or registration.pins. Future targets cannot be native registered absences.
These exclusions remove self-hash cycles without altering science inventories.
The new administrative SOURCE is pinned in registration.pins before collection.

Private evidence initially contains only precreated admin.stdout/admin.stderr.
ROOT configures them as bounded regular streams on durable storage; file-size
limit1MiB applies to this administrative unit. Four <=64KiB records and two
<=256KiB JSON files plus <=16KiB unit text are separately bounded administrative
metadata, not new scientific payloads. Main runtime still has unchanged
128MiB working tmpfs inventory; no administrative file is added to it.

## Fixed operation order and evidence

After all pre-epoch checks, attempt.json is created O_EXCL/fsynced, consuming
the one-shot. Timer must be loaded/inactive/dead with original activation0;
watch service must be unused/inactive, outside the task slice. Their literal
bytes are the accepted launcher renderings. Exactly ONE start(timer) occurs.
The actual paired activation properties—not a planned later service time—set
the original epoch; epoch.json records them. Realtime/monotonic disagreement
over2seconds or elapsed>=100seconds refuses further admission. The watchdog
is never reset, cancelled, retried or replaced, including after any failure.

The source freezes spec O_EXCL, computes its raw SHA, freezes card containing
that SHA, then freezes the exact outer unit containing card SHA. This is a
narrow literal duplication of launcher.outer_unit, with its __file__ resolved
to the frozen installed launcher path. It reloads once, checks specified
loaded state/resource properties and original timer, rehashes the full
registration input vector and compares the three installed byte objects.
commitment.json, OUTSIDE spec/card, records raw hashes and loaded properties.
One start(outer) then one bounded status read occur. No waiting for phase results.

ExecStart effective parsing, all unqueried loaded properties and the
file-to-loaded-unit mapping are PRIOR EXTERNAL qualifications, not proved by
the code's nonempty ExecStart field or daemon-reload return. The exact queried
systemd renderings (including RuntimeMaxUSec='47min 55s') are selected,
UNOBSERVED host-compatibility requirements: mismatch is STOP, no fallback.
Code's byte comparison is complete; its effective-property comparison is not.

Exit0/ONE_START_RETURNED_NO_PREFLIGHT_VERDICT records only one returned start
and actual status (possibly already terminal). It is NOT active/positive phase
evidence. Any exception exits2/BIND_STOP_NO_RETRY in retained stdout; existing
partial outputs remain. A systemctl timeout may leave manager-side start
outcome unknown; no resubmission is allowed. The independently qualified
watchdog/worker retirement and ROOT terminal collection handle it. O_EXCL
targets plus trusted exclusive ROOT ownership prevent cooperative repeats;
no malicious-ROOT or atomic snapshot guarantee is claimed.

All binding/readback/start/custody work after activation consumes the SAME
original clocks and constrained task slice. The selected115+5 stop covers the
whole experiment under qualified OS scheduling/shutdown assumptions, not a
hard realtime proof or total120-second fit forecast. A timeout is STOP even
if no preflight has run. No caps, dummy predicates or science commands change.
