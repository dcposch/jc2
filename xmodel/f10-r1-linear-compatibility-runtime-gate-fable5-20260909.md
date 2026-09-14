# f10-r1 linear-compatibility FIRST runtime-evidence gate (Fable 5.1, 2026-09-09)

Lane: `xmodel/f10-r1-linear-compatibility-runtime-gate-fable5-20260909.md`
Owned box: `box/f10-r1-linear-compatibility-runtime-gate-fable5-20260909/`
Launch (local clock): 2026-09-09 22:51:30 UTC. Hard stop: 23:09:00 UTC.

## 0. Input custody

All 68 charged snapshots in /tmp/jc2-lane.KjnDPB/inputs were verified by sha256sum against
the ordered assignment list BEFORE any body read (22:52 UTC): diff of the 68 computed digests
against the 68 listed digests was empty. Both own targets were absent at launch.

Read tiers (honest WHOLE versus selected):
- WHOLE (cat): READ-SCOPE.md, ROOT-REGISTRATION.md, launch-and-identity.txt,
  local-readback-and-identities.txt, physical-before.txt, worker-after-stop.txt,
  terminal-owned-process-check.txt, generic.plan.json, compatibility.dispatch.json,
  compatibility.telemetry.json, compatibility.receipt.json, dummy-descendant.telemetry.json,
  dummy-descendant.stdout, gate-valid.sentinel, the five gate-*.stderr files,
  terminal-metadata-check.json, the Astra execution report and its artifact JSON.
- METADATA field scope (jq selectors, no prose claim): all eight *.authority.json
  (schema, enabled, hostname, instance_id, job_tag, operation, caps, child_argv, parent_argv,
  python_flint, file_sha256 count), all eight *.dispatch.json, the six remaining
  *.telemetry.json, batch.PASS.json and preflight.PASS.json (status and child count only),
  remote-before.sha256-and-modes.txt, remote-inputs-after.sha256 and
  remote-terminal-manifest-and-modes.txt (hash lines and header lines only).
- HASH/BYTE scope only: custody.json, dispatch.registration.json (pin equality checked),
  the twelve generic fixtures (sha256 and byte size, plus a documentary grep for K strings).
- Accepted premise, selected lines only: the 17zb static gate (grep of its launch line,
  hand-RREF lines, counts line and completion line). Its A-D static confirmation is a premise
  with root's qualifications: all fixtures constant-v, no full-product or nonconstant-B
  runtime coverage, counts 23/2 structural not native operations, its 22:37 cap was not
  controlling here, and its disclosed shell-written scratch-list workflow failure stands.
- NOT read: bodies of checker.py, compatibility.py, dispatch_batch.py, execution_gate.py,
  probe.py (code and theorem 17m/17z/CAPRUN are not re-proved here; only their pins).

No Python, CAS, import, compile, fixture, matrix or network execution was performed.
Only sha256sum, jq, grep, diff, sed and awk over the frozen copies were used.

## 1. Scope and premises

This is the FIRST runtime-evidence review of one finite generic/API batch. It reviews whether
the retained metadata shows a genuine execution chain and a genuine generic receipt. It does not
re-prove the 17m theorem, the 17z decision code, or the CAPRUN instrument, and it transfers no
generic status to any actual source ideal, point, or JC2 conclusion. Root's independent
facts (STOPPED 22:42:06, 110 source post-pins equal registration, 85 remote files
current-pin-checked, writers idle 22:47:03 before the original 23:01:54 cap) are taken as
lifecycle statements, not re-observed. The worker is already STOPPED; no live read exists.

## 2. Verdict A — genuine execution chain

**Verdict A: CONFIRMED** at the documented scope, with one disclosed evidentiary gap (section 6).

Registration and physical instance. ROOT-REGISTRATION.md names i-08d2a40f272ee9fa2,
us-east-1, 172.30.0.72, ip-172-30-0-72, c7i.4xlarge, Owner f10-r1-exact-artifact-validation-20260909,
vol-0574e0fa5aed1f5e3. physical-before.txt (22:38:10-11Z) shows the same ID, State running,
same type, private IP, Owner and volume; DMI "Amazon EC2"; hostname ip-172-30-0-72; interpreter
a92f0f95... and module 2e5f8f17...; REMOTE_CWD_ABSENT; service LoadState not-found. The ROOT
stop timer is recorded active. worker-after-stop.txt (22:41:46Z) shows State stopped with
unchanged Owner and volume.

Pins. remote-before carries 111 hash lines and remote-inputs-after carries 110; the sorted
diff is exactly one line, the registration file ba1b374b... itself, and the other 110 lines are
byte-identical. The nine task basenames in the pin vector are compatibility.py,
generic.plan.json, checker.py, evidence.py, algebra.py, execution_gate.py, run_capped.py,
probe.py, dispatch_batch.py; no solver name appears. The compatibility authority pins the
registration under file_sha256 with the same digest ba1b374b..., which equals my sha256 of
the charged registration copy. The terminal manifest carries 85 hash lines; every one of the
53 charged remote artifacts hashes to a line in that manifest (53 of 53, none missing).

Service launch. launch-and-identity.txt shows the unit
jc2-f10-linear-compat-runtime-20260909.service, invocation 2896d5f8..., MainPID 7155,
ExecMainStartTimestamp 22:39:21 UTC, ExecStart /usr/bin/python3 -I -B .../dispatch_batch.py,
ControlGroup /system.slice/<unit>, MemoryMax 3221225472, TasksMax 64, LimitFSIZE 16777216,
User ubuntu, KillMode control-group, empty LD_LIBRARY_PATH/LD_PRELOAD, OMP and OPENBLAS
threads 1, ActiveState active. The live /proc stat line for 7155 has field 22 = 16607, the
registered start ticks. Namespace pid:[4026531836] and cgroup line match the unit. All of this
equals the registration's required service contract.

CAPRUN vectors. All eight authorities carry schema F10-R1-REGISTERED/v1, job_tag
f10-r1-linear-compatibility-execution-20260909, operation check. Caps: the six probe
authorities 5 s wall / 3 CPU / 2 GiB RSS (gate-cap deliberately rss_bytes "1"), dummy
5 s / 3 CPU / 33554432, compatibility 180 s / 170 CPU / 2147483648, all equal to the
registration. The compatibility parent_argv is the exact run_capped.py vector with those caps
and the child_argv is python3 -I -B compatibility.py <authority> <generic.plan> <receipt>.
Telemetry caps for compatibility and dummy repeat these numbers. Each dispatch record's
authority_sha256 and telemetry_sha256 equal my sha256 of the corresponding charged file
(8 of 8 and 8 of 8). Each of the five refusal stderr digests in telemetry equals my sha256 of
the charged stderr file (5 of 5); the dummy stdout digest de7ee73c... likewise.

Five expected faults. Deliberate defects are visible in the authority metadata: gate-disabled
enabled=false; gate-wronghost hostname "NOT-THE-REGISTERED-HOST"; gate-argv parent_argv ends
with an extra token "EXTRA" and "plain"; gate-cap rss_bytes "1"; gate-missing-input has 110
file_sha256 entries against 111 for the valid record. Their stderr traces raise at
execution_gate.py lines 20, 30, 43, 57, 67 with the five distinct messages, exit 1, stdout 0
bytes, no sentinel. gate-valid exits 0 with 0 stderr bytes and the sentinel bytes
"POSTAUTHORIZE" plus newline.

Dummy control. Cap 33554432, observed group RSS 80072704, status RESOURCE_CAP, runner exit 125,
resource rss. Identity events: MATCH (pid 7192, pgid 7192, same boot id and ticks 16756),
SENT signal 15, MATCH, SENT signal 9; term_sent, kill_sent, cleanup_complete and leader_reaped
all true; the leader was a zombie before reap and the group live list was empty. Dummy stdout
records child 7195 in pgid 7192 with parent 1, so the leader had already exited while the child
lived, and the group kill covered the child. This is the passing cleanup control.

Terminal state. At 22:41:15Z all 18 recorded PIDs and all eight PGIDs were absent, the unit was
inactive/dead with Result=success, and the journal shows start 22:39:21.36 and deactivation
22:39:26.35. The WHOLE claim I can make: every retained identity, cap, pin and stream is
mutually consistent and bound by hash. The selected claim: the caller 7155 was observed live,
the eight children were not; their identities come from CAPRUN telemetry only.

## 3. Verdict B — genuine generic receipt

**Verdict B: CONFIRMED** as generic behaviour only.

The receipt is the charged file with digest c99eda146afc91cb521a6a27739422ac7f1928c9763586e34a0a1bd590d3e443
(5955 bytes). Status GENERIC-COMPATIBILITY-PASS-NOT-ACTUAL-SOURCE, generic_only true.
Its embedded pins equal the charged bytes: checker_sha256 = sha256(checker.py) 122842e5...,
harness_sha256 = sha256(compatibility.py) aaec1e2c..., generic_plan_sha256 = 1fe704aa...,
authority_sha256 = 5df53d63...; execution hostname ip-172-30-0-72 and instance
i-08d2a40f272ee9fa2; python_flint 0.9.0 at the pinned module path with digest 2e5f8f17...
equal to the physical-before observation.

Counts 12 verifier calls, 5 positives, 7 negatives, 2 matrix constructors, 2 rref calls,
23 fmpq constructors equal generic.plan.json. Twelve outcomes, all entrypoint
"checker.verify IN-PROCESS; generic-only, not checker.main". Every outcome's fixture_sha256 and
fixture_bytes equal my sha256 and stat of the charged fixture (12 of 12), and
terminal-metadata-check.json's pin_and_size_match is true on all twelve.

Branch statuses and first error messages as retained: unit-positive, precision-positive,
zero-guard-positive VERIFIED-GENERIC-ZERO-QUOTIENT with checked_coordinates 217, multipliers 9,
degree bound 25 and the printed cofactor contract; separator-zero-positive and
separator-T-positive VERIFIED-GENERIC-NONZERO-QUOTIENT with 1638 checked columns; unit-negative,
high-T30-negative and rounded-canonical-string-negative rejected by "full 217-coordinate sum
h_i f_i equals q^5"; separator-normalization-negative and zero-guard-false-separator rejected by
"dual target normalization equals one"; separator-column-negative by "dual column annihilation
i=0 j=0 ell=0"; float-type-negative by "canonical rational strings only". The canonical K-1
identity failure is thus distinct from the float parser failure, as claimed.

API strings. The three scalar observations are the strings "0", "9007199254740993" and
"9007199254740993/2"; the two 2x5 RREFs are string rows [[1,2,3,0,1/2],[0,0,0,1,-1/2]] with
pivots [0,3] and [[1,2,0,7,-3],[0,0,1,-2,1]] with pivots [0,2], both rank 2. These equal, as
strings, the hand traces printed in the accepted 17zb gate (its lines 34-36). I did not
re-derive them: zero arithmetic replay.

Wire fields, documentary only: the exact string "9007199254740993" occurs in
generic-fixture-precision-positive.json; "9007199254740992" occurs in the rounded negative;
the float negative contains the token 9007199254740992.0. The wire spells 1/K as the string
pair ["1","9007199254740993"] (numerator, denominator), and K as the pair with "1" as
denominator; a slash spelling "1/9007199254740993" does not occur. So exact K and 1/K reach
the parser as strings. All mathematical values remain strings in the receipt; no JSON number
carries a mathematical integer. Nothing here is a ROOT source acceptance or a nonzero point.

## 4. Verdict C — mathematical runtime bounds and CAPRUN contract

**Verdict C: CONFIRMED.**

compatibility: wall_elapsed 3.100202855 s against cap 180; max_observed_group_rss_bytes
34848768 against 2147483648; status NORMAL_EXIT, child exit 0, resource null, stderr 0 bytes,
stdout 54 bytes, no identity checks needed. Dispatch: mathematical true, first_math_epoch
1788993563.148 (22:39:23 UTC), hard_cutoff_epoch exactly first_math + 240 (the registered
aggregate), returned_epoch 1788993566.306, before the cutoff and before the fixed 22:47:00
mathematical deadline. The seven non-mathematical children carry hard_cutoff 1788994020.0,
which is 22:47:00 UTC, and all returned before it; all eight have admission margin 15 and an
empty remaining_group_live list. Eight children only: batch PASS lists 8, preflight PASS 7,
18 PIDs and 8 PGIDs in the readback, consistent with dispatch 22:53 and publication before cap.

Enforcement strings in telemetry state the accepted limitations verbatim: CPU is per-process
inherited RLIMIT_CPU typed only on SIGXCPU; RSS is sampled aggregate PGID RSS with overshoot
possible; wall is monotonic deadline plus lifecycle sampling with the leader reaped once after
group quiet. leader_reaped false with term_sent false, kill_sent false, empty live and zombie
lists on the six normal exits is the contract's normal-exit shape, not a new fault. Actual
terminal quietness is the independent 22:41:15 absence check, not that flag.

The unit journal figure 4.923 s CPU and 5.2M memory peak is a separate systemd accounting line.
It is retained verbatim and is not used as a substitute for the CAPRUN sampled group RSS; the
two figures are not comparable and I draw no bound from the unit figure.

## 5. Verdict D — scope boundary

**Verdict D: CONFIRMED.**

The installed 0.9.0 module path, hash and API were checked once, in the compatibility child, and
the same path and hash appear in physical-before.txt and the authority. The 100 package/native
pins are declared documentary pins from environment.json 35a9c322...; the registration and
READ-SCOPE both state they are not a hermetic OS/stdlib/import map, and nothing here upgrades
that. No solver.py, full 217x1856 matrix, source artifact, source acceptance or ideal decision
exists in the 110-pin vector, the 85-file manifest, the plan (actual_source_inputs empty,
actual_solver_calls 0) or the receipt (scope string says so). generic.plan.json's own scope line
calls itself a STATIC UNEXECUTED specification; its execution is the receipt, not the plan.
No method control masquerades as a frontier result: every positive is labelled generic and
every negative is an expected rejection. The actual source batch remains separate and is not
inferred from anything here.

## 6. Smallest actual defect

Smallest actual defect: no child process was ever observed independently of CAPRUN. The only
live observation is the caller 7155 (stat, cgroup, unit properties). Every child PID, PGID,
start identity, wall time and RSS figure is CAPRUN self-report, cross-bound by file hashes and by
the later absence check. The gate-valid sentinel and the five stderr traces are the only
child-authored bytes that do not pass through the telemetry writer. This gap is disclosed by
the producer, is inherent to a 5-second batch, and is not blocking for a promotion whose
content is generic behaviour only; it would matter for any actual-source batch, where a live
cgroup process snapshot should be captured.

Minor observations, not defects: all eight dispatch records have no status field (status lives
in telemetry); compatibility.stdout and the six gate-*.stdout files were not charged, so their
stdout_pin lines are taken from terminal-metadata-check.json rather than re-hashed.

No REFUTED item. No GAP in the A-D verdicts. Nothing generic serves as ROOT source acceptance.

## 7. OPENS RAISED

QUANTITY: new scientific OPENs raised = 0.
QUANTITY: OPENs retained unchanged = 1 (the separate, unauthorized actual-source batch).
No exit-price claim is made and no exit-price basis line is declared.

## 8. Own-only collision check

Own targets xmodel/f10-r1-linear-compatibility-runtime-gate-fable5-20260909.md and
box/f10-r1-linear-compatibility-runtime-gate-fable5-20260909/ were absent at 22:52 UTC before
the skeleton write; the skeleton (no marker) was written by apply_patch at 22:53, this body by
further apply_patch calls, and the box directory was never created because nothing needed to be
stored (no scratch lists were written by shell). No other path was written. Whole-read of this
report precedes the marker.

<!-- BODY-END -->
