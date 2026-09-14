# F10 r1 retained17-row runtime evidence gate (independent, fable5)

2026-09-09. Independent runtime-evidence review of the one frozen validation
run reported in xmodel/f10-r1-retained-runtime-execution-astra-20260909.md.
Tool scope used: SHA-256, byte counts, JSON/argv/telemetry metadata and
literal string/decimal comparison only. No CAS, no import or execution of
any charged source, no coefficient arithmetic, no remote or process access.

## 0. Pins and read scope

All 115 charged inputs were hashed with sha256sum -c against the ordered
list (box/.../expected.sha256, written first) before any body was read:
115 OK, 0 mismatches, basename set identical. The 100 remote files, exact.json,
retained.json and the twelve fixtures were used by hash and byte count only.
Accepted premises: the static code gate and the runtime-client gate (charged
inputs 113-114) are taken as the code tier; no source was executed, imported
or re-reviewed beyond locating the contracts named below. The 55.8 KB and
43.5 KB raw dumps of the ten operation records were not read as prose; every
field named in A-D was compared by a metadata-only script
(box/.../meta_compare.py, output meta_compare.out) plus literal reads of the
stderr, sentinel, telemetry, stop and launch records.

Rebased paths: every absolute remote path in the authorities, telemetry and
manifest was compared only through its charged basename. No remote, AWS,
process or corpus access occurred.

## A. Registration and actual batch binding

CONFIRMED (with the declared trust boundaries). The enabled registration
(charged hash 453c2a9dc6f00acf13f0c35a01afe61050fa99a25a98ce8dd41f53e3a396d125)
carries enabled=true, the instance, hostname, cwd and job tag, mathematical
deadline 18:14:00+00:00, task deadline 18:17:00+00:00, aggregate 750 s,
file size limit 16777216 and the five profiles exactly as charged
(probe 5/3/2147483648, dummy 5/3/33554432, transform 180/170/2147483648,
check 180/170/2147483648, controls 300/280/2147483648). Ten of its eleven
file pins match the charged basenames byte for byte; the interpreter pin
a92f0f95... cannot be checked locally and rests on physical-preflight.txt
line 5, which records the same digest for /usr/bin/python3 together with
Linux, ip-172-30-0-72, i-08d2a40f272ee9fa2 and Amazon EC2 on lines 1-4.
worker-stopped.json is the same instance, c7i.4xlarge, 172.30.0.72, Owner
tag f10-r1-exact-artifact-validation-20260909, state stopped, volume
vol-0574e0fa5aed1f5e3 attached.

Batch binding, from the raw records rather than metadata-audit.json:

- Order is the required ten; each dispatch.json equals its batch.PASS record
  and (first seven) its preflight.PASS record field for field.
- Every authority and telemetry file hashes to the digest stored in its
  dispatch record; every telemetry stdout/stderr digest and byte count equals
  the charged stream file.
- Every telemetry argv_sha256 equals the SHA-256 of the authority child_argv
  serialised as compact JSON plus newline (my recomputation, ten of ten), and
  equals the ten MATCH digests in argv-fingerprints.json.
- Parent argv is the registered CAPRUN vector with the child vector as its
  tail after "--" in nine operations; the exception is gate-argv (see B).
  Authority caps equal the profile and the parent --wall/--cpu/--rss values
  in nine operations; the exception is gate-cap (see B). Telemetry caps equal
  the profile in all ten.
- All ten children report pid=pgid, namespace pid:[4026531836], the same
  boot id 00b7a876-... with monotonically increasing start_ticks
  (18878 to 19284), and caller_stat ppid=pgid=session 1408.
- hard_cutoff_epoch 1788977640.0 is 18:14:00Z in every record; every
  returned_epoch precedes it; admission margin 15 in every record.
  first_math_epoch converts to 18:01:32.576026Z and end_epoch to
  18:01:41.890709Z (the report quotes the batch utc string .890711; a 2 us
  float-formatting difference, not a discrepancy).

launch-observation.json shows dispatcher 1408 started 18:01:30 with the
exact frozen argv and a later absent /proc/1408/stat, as the report says.
The remote-prepull manifest lists exactly 100 files and all 100 digests
equal the charged copies. custody.json records 115 owned and 15 inputs,
expected transaction 1f62dcfea55499ded352547c9b43cd25da847ee4fe9ff58c611832535b378484
equal to the charged artifact JSON, and worker "STOPPED; EBS retained".
The no-concurrent-authority-writer rule is a registration flag and a
cooperative assumption; nothing in the records can prove it, and this gate
does not claim to.

## B. Refusals, valid sentinel and descendant cap

CONFIRMED. The five refusals returned 1 as NORMAL_EXIT with runner exit 1,
no sentinel in the charged set, and no refusal sentinel in the 100-line
remote manifest (only gate-valid and dummy sentinels exist, both the 14-byte
POSTAUTHORIZE line). Each terminal stderr names the expected reason and each
authority carries exactly the prescribed defect: gate-disabled has
enabled=false ("no active registered authority"); gate-wronghost has
hostname NOT-THE-REGISTERED-HOST ("not the registered AWS host"); gate-argv
has the token EXTRA appended to the parent vector ("full parent argv differs
from registered capped runner"); gate-cap has authority rss_bytes "1" against
parent --rss-bytes 2147483648 ("registration is not the exact required CAPRUN
argv"); gate-missing-input omits the frontier.json pin, eleven pins against
twelve ("checker input artifact must be explicitly hash-registered"). The
accepted caller does not assert these strings; this read is the independent
corroboration. gate-valid returned 0 and wrote its sentinel.

dummy-descendant: status RESOURCE_CAP, resource rss, reason rss_cap, runner
exit 125 while child_returncode is 0 (the leader), max observed group RSS
77971456 against cap 33554432. identity_checks are MATCH (pid 1490, pgid
1490, start_ticks 18991), SENT 15, MATCH, SENT 9; cleanup_complete true,
leader_reaped true, zombies [1490]. The dummy stdout records leader 1490,
child 1492, same pgid and namespace, and the child stat shows ppid 1 (leader
already gone) with sigign 16797696, whose bit 14 is SIGTERM. The overshoot
of the sampled cap is expected and is not instantaneous enforcement.
owned-process-absence.txt and worker-stopped.json are historical records
with empty process tables; no current process state is asserted here.

## C. Transformer and genuine production checker

CONFIRMED at authorized-checker tier. transform (operation build, child
1503) exited 0 in 0.814091058 s wall with 22761472 B sampled RSS and printed
the 47-byte EMITTED-REPRESENTATION-ONLY line. Its authority pins exact.json
168bdfd3a791f24a6631de66ae4e71c3f209ee9eb0d21fc466f9aa802f5ad576, whose
charged copy is 88634 bytes. The charged retained.json hashes to
88de7ea789cd77696e4e73015921554b57c10356017df8ee6d71fe5c51c21037 and is
307729 bytes; that digest is pinned in the full-check and semantic-controls
authorities and repeated as retained_sha256 in the receipt.

full-check (operation check, child 1520) exited 0 in 1.557439739 s with
26034176 B and printed the 39-byte verdict. The receipt charged as
d356240c68f2fef7b511d66df0265fcead95402f3ebc93e46b4ed4041aea1916 carries
checker_sha256 equal to the registration pin, the full-check authority
digest, the host/instance/job tag, verdict PASS-REPRESENTATION-NOT-IDEAL-
DECISION, original_slots 20, retained_slots 17, full_bracket_bands 8,
inverse_pole_slots 10. Its 20 rows have 17 with nonzero retained terms and
zero at E1/S8, E0/S9 and the guard; maximum lower degree 6, minimum s
exponent -6, v degree 6, maximum rational bits 69 at E0/S7, largest row
E0/S3 with 271 retained against 78 original. Every number in section 2 of
the report is a literal match. These are checker measurements; no local
replay, speedup, CPU total or ideal statement is added. Documentary note:
the receipt itemises counts and verdict only; the "forcing, envelopes, gauge,
substitution, restoration" wording in the report credits the accepted code
tier, not separate receipt fields.

## D. Twelve changed-fixture controls

CONFIRMED. controls.receipt.json lists exactly twelve cases, all
EXPECTED-REJECTION, each with entrypoint "checker.verify IN-PROCESS, not
checker.main". Every fixture_sha256 and fixture_bytes equals the charged
fixture file (twelve of twelve). Exceptions and reasons: dropped row "all20
original slots"; L inverse "L inverse identity"; scale and negative-s loss
"retained scale/parameter mapping"; modulus "wrong modulus"; lower exponent
"Laurent/basis exponent domain"; omitted pole "all ten pole slots"
(inventory only); omitted restoration is a KeyError whose reason is the
single-quoted letter a; leading B5 "leading B coefficient"; float "floating
point forbidden anywhere"; the 9007199254740993 and 9007199254740992 strings
both "original row substitution E1/S0". These match VALIDATION.md lines
64-75. The receipt states the precision scope as two rejections plus harness
persistence with no successful nested-parser claim, the negative limit for
late bracket/pole equations, and that the positive scope is the separate
checker.main run. semantic-controls (child 1550) exited 0 in 6.726916533 s
with 30838784 B; its authority pins the harness digest equal to the
registration pin and the genuine receipt digest above. That fixture hashes
were reread before verify is accepted-code behaviour, not separately
receipted at runtime.

## E. Deviations, unread scopes and remaining doubts

- Unread but referenced: custody.json owns input-pins.json,
  remote-input-pins.txt and publication.json and lists ops/FLEET.md,
  ops/fleet/fleet.sh and the runtime-code report as inputs; none is charged
  here, so their contents are not corroborated by this gate.
- custody.json carries two owned entries with basename
  dispatch.registration.json (root and remote copies); only the charged copy
  was compared.
- The EBS volume has DeleteOnTermination true; "recoverable" holds only
  while the instance is never terminated, which the report also states.
- "Regular copies, not links" for the staged inputs is documentary; the
  charged snapshot cannot distinguish it.
- Cap values are configured limits; only the dummy exercised one.
- No new OPEN is raised. The prior gate raised
  OPEN[F10-R1-RETAINED-RUNTIME-PREFLIGHT-AND-BATCH]; its quantity (one
  seven-record preflight, one batch with a PASS receipt and twelve
  rejections) is met by these records at this scope. Own-only collision
  check: this report and its box only, no corpus scan.

## Verdict

A CONFIRMED, B CONFIRMED, C CONFIRMED, D CONFIRMED. Engineering PASS at the
qualified retained17-row representation-validation scope: the one frozen run
is bound by hash, argv, identity and cutoff to the registered worker and
sources, and the receipts say what the report says they say. No ideal
decision, point, unit, exclusion, solve, worker, timer or hardening authority
follows. No Seal and no charge_basis are authored.

## OPEN(S) RAISED

- NONE. No new bounded quantity is needed at this scope; the prior
  OPEN[F10-R1-RETAINED-RUNTIME-PREFLIGHT-AND-BATCH] is met as stated in E.

## COLLISIONS

- NONE. Own-only check: this report and its box only, no corpus scan.

## Own whole-read and completion

Own whole-read at 18:38:24 UTC with cat -n, 182 lines: sections 0, A, B, C,
D, E, Verdict. All five 64-hex tokens in this report were cross-checked by
comm against the own expected.sha256 pin list (5/5 matched, none unmatched).
Pins were verified at 18:32:37 UTC before any body read. Box contents:
expected.sha256, meta_compare.py, meta_compare.out, report-hex.txt,
pin-hex.txt. No placeholder remains, no Seal, no charge_basis, no marker
before this line. Completed before the 18:48 UTC stop; no worker, timer,
solve, code edit or validation run was touched.

<!-- BODY-END -->
