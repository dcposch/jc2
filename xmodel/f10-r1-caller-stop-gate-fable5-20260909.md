# F10 r1 caller STOP gate: narrow failure review and proposed correction (Fable 5.1)

tag=f10-r1-caller-stop-gate-fable5-20260909
reviewer=Claude Fable 5.1 (claude-fable-5-1); narrow NEW caller gate, not an ideal or representation-runtime result
launch=root invitation; actual start 12:56:37 UTC; hard stop = earlier of 13:08:37 and 13:12 UTC, i.e. 13:08:37, no reset
subprocesses=sha256sum/cat/date/grep and ONE metadata-only event-dictionary replay (box/predicate_replay.py, stdlib, RLIMIT_AS 64 MiB, under 1 s, reads only the pinned telemetry JSON; no import of dispatch_batch.py/probe.py, no fork, no signal, no /proc scan). ZERO mathematical subprocess, no CAS, no builder/checker/precision import or run, no network, no worker action.

## 0. Custody and read scope

All FIFTEEN charged objects under /tmp/jc2-lane.uVMbnO/inputs were hashed BEFORE their WHOLE reads; the fifteen digests match the invitation list exactly (pins generated from sha256sum in section 5 and box/inputs.sha256). Cross-links inside the charged set: the STOP record's dummy entry cites telemetry_sha256 48a96693 and authority_sha256 3f23889e, both charged files; the dummy authority pins dispatch_batch.py da3d8d50, probe.py 02913a1c, precision.py 130a4496, execution_gate.py cbfe55ff, checker.py e2970c71, all equal to the charged bytes. CAPRUN 4435279d and builder 2dcba70d are pinned by the caller but not charged; the CAPRUN excerpt is used only as the literal interface. The six gate-* telemetry files are NOT charged; nothing about their bodies is promoted here.

## A. Original failing predicate and scope. CONFIRMED.

Predicate. The failure is `require(all(x.get('result')=='MATCH' for x in telemetry['identity_checks']), 'TERM/KILL identity not matched')` at dispatch_batch.py:99, the LAST require of the dummy branch (lines 91-99). batch.STOP.json carries exactly that message at 12:44:22.648882Z, 0.4 ms after the dummy dispatch record was written (ended_utc 12:44:22.648495), so lines 92-98 (rc 125 + resource rss, all four termination flags, RSS 77955072 > 33554432, two stdout lines with namespace/PGID custody) had already passed; only line 99 fired.

Interface semantics. In the accepted CAPRUN excerpt, `validate_identity` appends one record per stage with result MATCH/MISMATCH/NOT_FOUND (excerpt lines 4-17) and `send_group_signal` then appends a SEPARATE record `stage+"-send"` with result SENT and the integer signal, or GROUP_GONE (lines 74-85). `terminate_group_and_reap` calls it for "before-term" and, if the group stays live through the grace period, "before-kill" (lines 121-138). The preserved telemetry is exactly that: before-term MATCH (pid=pgid=2628, start identity boot=e4cc45da…;start_ticks=39218) at .357571Z, before-term-send SENT 15 at .357612Z, before-kill MATCH at .615202Z (257.6 ms later = grace 0.25 s plus one sample), before-kill-send SENT 9 at .615231Z, utc_end .622272Z. So every signalled CAPRUN run necessarily contains SENT records and the frozen predicate rejects every correct TERM/KILL sequence. It is also vacuous: on an empty identity_checks list `all()` is True (replay row EMPTY). The defect is the caller's event-type model, not CAPRUN, builder, checker or gate.

Scope. (1) Observed descendant cleanup: telemetry termination block cleanup_complete/leader_reaped/term_sent/kill_sent all true, group_live_before_reap empty, zombies [2628]; final-process-audit.json lists all seven PGIDs 2599…2628 with live [] and mathematical_artifact_exists false. (2) Overall preflight STOP: status STOP-NONDECISION, first_math_epoch null, seven records all mathematical=false, no build/check/precision record, so no preflight.PASS.json and no mathematical launch: CONFIRMED. (3) The five refusal controls and the valid control are accepted here ONLY by control flow: the caller reached line 119 (dummy) only if lines 89-90 and 101 passed for all six, and their returncodes 1,1,1,1,1,0 are in the STOP record. Their telemetry bodies are uncharged and NOT promoted. (4) No frozen CAPRUN/builder defect is asserted; Astra's report says the same (lines 94-97).

## B. Hostile review of the proposed four-event predicate. CONFIRMED with one residual GAP and a minimal correction.

Replay (box/predicate_replay.out, frozen event dictionaries only):

| case | old (line 99) | proposed | strengthened |
|---|---|---|---|
| ACTUAL four events | False | True | True |
| EMPTY list | True | False | False |
| delete a SENT / delete kill pair | False | False | False |
| reorder (send before MATCH; kill before term) | False | False | False |
| MISMATCH / NOT_FOUND / GROUP_GONE | False | False | False |
| wrong signal (term=9, kill=2) | False | False | False |
| SENT without preceding MATCH | False | False | False |
| extra fifth SENT; renamed stage; signal "15" string | False | False | False |
| signal 15.0 float-typed | False | True | False |
| MATCH with foreign observed pid/pgid 9999 | False | True | False |
| MATCH with foreign start identity | False | True | False |

The proposed predicate (CALLER-FIX-PROPOSAL.md lines 19-31, diff lines 5-13) fails the frozen sequence never and rejects every deleted, reordered, MISMATCH, NOT_FOUND, GROUP_GONE, wrong-signal, SENT-without-MATCH, extra-event and string-typed case. For THIS dummy the four-event sequence is deterministic: the child ignores TERM and sleeps 20 s under a 5 s wall and 32 MiB RSS cap, so TERM then KILL must both occur.

Residual validation. The tuple compares only (stage, result, signal). It does not compare the two MATCH records' observed_pid/observed_pgid/observed_start_identity with the telemetry's top-level pid/pgid/start_identity, and Python `15.0 == 15` lets a float-typed signal through. Authentic CAPRUN cannot emit either (MATCH means observed == expected, and the signal is an int), so these are consistency gaps in accepting the telemetry, not evidence of a runtime hole. Residual pid/PGID/namespace/cleanup coverage already in the caller: PID namespace of the CAPRUN process (line 76), post-exit /proc scan of the recorded PGID (line 80), stdout custody of both dummy processes (lines 96-98), termination flags (line 94), plus the separate final audit.

Distinction. Accepting this predicate means accepting pinned CAPRUN's self-reported signal sequence as internally consistent with its interface, not proving a new supervisor: the caller never observes killpg; that correctness rests on the accepted CAPRUN tests (96775b17, not rerun).

Minimal material correction (one require, no redesign): after the four-tuple equality, for each MATCH record require observed_pid == telemetry['pid'] == telemetry['pgid'] == observed_pgid and observed_start_identity == telemetry['start_identity']; for each SENT record require `type(signal) is int`. Optionally require telemetry['status']=='RESOURCE_CAP' beside resource=='rss'. The strengthened column above is exactly this and rejects all 17 negatives.

## C. Static caller delta before any NEW separately authorized dispatch. CONFIRMED as a contract, two named defects, one GAP.

CONFIRMED: physical host by DMI asset tag and literal hostname (lines 106-107; EC2 vendor is re-checked in the child gate); interpreter pin (108); admissibility/frontier/builder/checker/gate/CAPRUN constants (109-114); full parent CAPRUN argv and child argv built once (47-55), recorded in the authority and matched element-for-element by execution_gate (lines 34-57); caps as literal strings; RLIMIT_FSIZE soft=hard=16 MiB set in preexec_fn BEFORE exec of CAPRUN (26-27, 75), inherited by CAPRUN and child; start_new_session=False so the caller creates no session and CAPRUN owns the recorded PGID (STOP caller_stat shows CAPRUN pid 2627 in the caller's group 2597 while the child leader is pid=pgid 2628); one child at a time by sequential Popen/wait (74-78); exclusive 'x' opens for authority, caller stdout/stderr, dispatch, PASS and STOP files (19-21, 73); STOP on any mismatch via RuntimeError → BaseException handler → exclusive batch.STOP.json → re-raise (23-24, 128-133); post-run re-hash of every pinned file (81). Admission: DEADLINE is the literal 12:53:00 UTC (line 12); at each mathematical stage hard = min(DEADLINE, first_math+360) and `now + wall + 2 < hard` (40-45), strict; the nine configured caps sum to 60+7×30+30 = 300 s, inside 360, and the per-stage check enforces the aggregate dynamically. The old authority, deadline and directory cannot be reused: every authority binds absolute paths under ROOT and the exact argv, the gate compares cwd and argv literally, DEADLINE is past, and a reused directory would make the exclusive STOP write itself fail.

Defect C1 (material for the precision stage). probe.py, precision.py and dispatch_batch.py digests are RECORDED in each authority (56-57) and re-checked for change, but never asserted against a root constant at main(); builder/checker/gate/CAPRUN are. A reviewed copy must add constants for probe.py and for the corrected precision.py (whose hash is new by D). This is two require lines, not a runner redesign.

Defect C2 (registration scope). Root's rule "only job/cwd/deadline constants plus the reviewed predicate" holds if the SAME instance i-08d2a40f272ee9fa2 is restarted (private-IP hostname and EBS interpreter persist); any other worker changes INSTANCE, the hostname literal (107) and possibly the interpreter constant (108), which is beyond that rule and would need explicit root approval.

GAP. The +2 s admission margin must cover term_grace 0.25 s plus POST_KILL_OBSERVE_SECONDS, whose value is outside the charged excerpt (used at lines 135, 144). If it exceeds about 1.75 s a capped stage could overrun its admitted slot; the direction is a late STOP, never a false pass. Likewise no artifact-size expectation is charged, so 16 MiB RLIMIT_FSIZE is unverified against exact.json; an oversize write fails closed (EFBIG), never silently.

## D. Unexecuted precision helper. Mechanics CONFIRMED; artifact-parser fidelity claim REFUTED; minimal correction specified.

CONFIRMED: precision.py runs as an ordinary `/usr/bin/python3 -I -B` registered child (caller line 124, operation check, exact.json pinned by line 59); `from checker import verify, InvalidArtifact` sits AFTER `authorize` (lines 6-8) and checker's main is __name__-guarded; the >2^53 precondition is genuine (2^80+1 is not float-representable, and both halves of line 13 are asserted); the changed-payload rejection is real.

REFUTED (root's concern stands): the rejection at line 18 is produced by checker's `no_floats` type sweep (checker.py:31-40), which fires before `read` (checker.py:47-65) is ever entered, and the positive "string_roundtrip":"EXACT" is json.dumps/json.loads of a synthetic dict (lines 12-13), not the artifact rational parser. Hence precision.py establishes "floats are rejected", not exact coefficient fidelity. A rounded integer disguised as a canonical decimal string is accepted by `read` by design (it is a valid canonical rational); it can be caught only by the exact identity comparisons (row-vs-projection at checker.py:176, guard equality at 205), which precision.py never exercises with a big value.

Minimal static correction (through the actual parser and a changed payload; not run here):
1. Precondition: `changed["rows"][-1]["polynomial"][0] == [[0]*12, "-1", "1"]` (the guard row's constant term, sorted first; same precondition mutation() uses).
2. Replace the float assignment by the canonical STRING of the rounded integer: `s = str(int(float(-(2**80+1))))`; assert `int(s) != -(2**80+1)`, `abs(int(s)) > 2**53`, `str(int(s)) == s`.
3. Require `verify(changed)` to raise InvalidArtifact with reason exactly "full guard row" (checker.py:205) and assert the reason is none of "floating point anywhere in artifact", "rational not strings", "noncanonical integer strings", "noncanonical rational": this proves the parser ACCEPTED the disguised string and the exact identity rejected the value.
4. Keep the existing float case as a separately labelled "float_type_rejection"; delete or rename the generic-JSON "string_roundtrip" field; add the artifact sha256 to the receipt.
5. Positive parser fidelity beyond this cannot be shown at runtime on this artifact (no constrained coefficient exceeds 2^53); record it as static inspection: `read` uses int(str) and Fraction only (checker.py:60-64), no float path. GAP: Python's default 4300-digit int-string limit would raise ValueError (fail-closed, unclassified) on an absurdly long coefficient; interpreter version is uncharged.
The corrected file is a new hash and must become a root constant (C1).

## Verdicts

A CONFIRMED (line 99 is the sole failing predicate; SENT records are by-design interface events; descendant cleanup observed; batch-level preflight STOP; nothing mathematical launched; uncharged refusal telemetry not promoted; no frozen defect). B proposed predicate CONFIRMED for this dummy with a residual GAP closed by the one-line MATCH/int cross-check. C caller contract CONFIRMED; defects C1 (helper pin constants) and C2 (host constants on a different worker); GAP on POST_KILL_OBSERVE_SECONDS and artifact size, both fail-closed. D mechanics CONFIRMED, artifact-parser fidelity REFUTED, five-line correction specified. No execution, dispatch or follow-on authority is created by this gate.

## 5. Input pins (generated from sha256sum, hash order)

| sha256 | file |
|---|---|
| 02913a1caf8cb5ebe2ec7c404ede0247a1954baee3751af8b2645496f6b6e1a7 | probe.py |
| 129e879ce81684714d2d5dc2ffd81d55e3c5c0537fbc564a46f7417e2560cd0b | f10-r1-engineering-execution-astra-20260909.md.artifact.json |
| 130a44964c3d824926f9054a7c7913f8c8401c7baa4f6ba5a8bb4eba3f639720 | precision.py |
| 38b89ef75c63edc0b3759fcdc39d83b42295b10aea937b0ae004b07ce1c87e42 | final-process-audit.json |
| 3f23889e748a49d1836f1ac7e9b9fd9c7e5829d3487aaa20265b9ace2ac59c20 | dummy-descendant.authority.json |
| 481d2a2edb12855cbdfa11f1cc1d0d15d7933b039896612827a683c3d70a09d7 | f10-r1-complete-builder-gate-fable5-20260909.md |
| 48a96693ac727ef22e5856aec9e0c90c0df890154db686ed8a6fd50651256de1 | dummy-descendant.telemetry.json |
| 4d0cc7ef5643ad6cf10a02ffa7b39a72e447932f746bb9c844f65831c360c339 | f10-r1-engineering-execution-astra-20260909.md |
| 5f86ae397eaf70419dced53836ef7a701c6c663c5cf3cf23974a20dc9a010d70 | caprun-signal-interface.txt |
| 744d3a9f6698e1a9efeb9597cd73d6d6801a401233dc26d4793c8b1a407f80cc | caller-identity.proposed.diff |
| 7f166b56f3e3cd6730718a549cf966081c0886ebbf3e31b2bdfce5fb1d97ed15 | CALLER-FIX-PROPOSAL.md |
| c0b02698533b0e12bcd6dfe5729849fdbedf327b6229abee4f0e1a9524eacf98 | batch.STOP.json |
| cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6 | execution_gate.py |
| da3d8d503f9246fd33d0cde372ccb642140e174c53a0599921ee4ab07b399b67 | dispatch_batch.py |
| e2970c71774607e211ecc7e0f001a0dc02d02410e303ca58cf7c17ab77b9f545 | checker.py |

Own box: predicate_replay.py, predicate_replay.out, inputs.sha256.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check over this body; no corpus scan.

<!-- BODY-END -->
