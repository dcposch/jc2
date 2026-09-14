# F10 r1 caller v2 gate: final narrow delta review before one engineering measurement (Fable 5.1)

tag=f10-r1-caller-v2-gate-fable5-20260909
reviewer=Claude Fable 5.1 (claude-fable-5-1); final narrow caller-v2 delta gate, not an ideal decision, runtime representation pass or worker invitation
launch=root invitation; actual start 13:16:38 UTC; hard stop = earlier of 13:25:38 and 13:26 UTC, i.e. 13:25:38, no reset
subprocesses=sha256sum/cat/date/grep/sed; one stdlib custody check (artifact body hash, diff-line consistency); ONE metadata-only predicate regression (box/predicate_regression.py: AST-extracts predicates from the charged v2 caller and exec's them in isolation against dictionary fixtures; RLIMIT_AS 64 MiB, alarm 10 s, `timeout 10`, under 1 s; no import of dispatch_batch/probe/precision/checker/builder, no main(), no fork, no signal, no /proc scan). ZERO mathematical subprocess, no CAS, no network, no worker action.

## 0. Custody and read scope

All TWELVE charged objects were hashed with sha256sum BEFORE their WHOLE reads; the twelve digests equal the invitation list exactly (section 5, box/inputs.sha256). Cross-links inside the charged set: the Astra artifact JSON's body_sha256 afc13d9e…, body_bytes 6984, full_sha256 bb55f78f… and file_bytes 7316 are reproduced from the charged report bytes (exactly one standalone body-end marker line). REGISTRATION.disabled.json's caller pin aaafa62a… equals the charged dispatch_batch.py; its precision pin 56400dd3… equals the charged precision.py and the caller's main() constant (line 135); its probe pin 02913a1c… equals the prior gate's charged probe hash (probe.py itself is NOT charged here and is not promoted). The frozen old caller da3d8d50… and precision 130a4496… are NOT charged: the two `.diff` files were checked only for consistency with v2 (every `+` line present in v2, every `-` line absent, every context line present: 29/7 and 37/13 lines); root's byte-identical diff reproduction is consumed, not re-derived. The prior gate 946e07d0… is consumed as the specification of the proposed correction; its underlying math/static gate is not re-audited. Builder, checker e2970c71…, execution_gate cbfe55ff… and CAPRUN 4435279d… are treated as accepted and unchanged (the two charged ones rehashed).
## A. Exact implementation of the prior gate's proposal

**CONFIRMED.** The caller delta is exactly: ROOT/JOB/DEADLINE constants (lines 9, 11, 12), `hard = None` (41), the +15 margin (46), `returned=time.time()` (80), three record fields (88-89), the post-return NONDECISION require (91), RESOURCE_CAP (96), the four-event block (103-118), and the probe/precision pins with the self-hash comment (134-136). No other line changed.

- Typed four-event sequence: lines 103-111 compare the tuple list (stage, result, signal) against the literal before-term/MATCH, before-term-send/SENT/15, before-kill/MATCH, before-kill-send/SENT/9. This is the proposed predicate verbatim.
- MATCH consistency: lines 112-116 chain `observed_pid == telemetry['pid'] == telemetry['pgid'] == observed_pgid` and require the observed start identity to equal the telemetry's start_identity. Because the tuple equality precedes it, the `else` branch (117) is exactly the two SENT records.
- Int-only signals: line 118 `type(...) is int`, which rejects 15.0 and bool.
- RESOURCE_CAP: line 96 beside rc==125 and resource=='rss'.
- Fixed helper pins: probe 02913a1c… (134) and corrected precision 56400dd3… (135) at main-entry before any run(); closes prior defect C1. Every authority still records and post-rechecks dispatch_batch.py, probe.py and precision.py digests (57-60, 83).
- Unchanged contract: INSTANCE i-08d2a40f272ee9fa2 (10, 125), hostname literal (126), interpreter constant (127), admissibility/frontier/builder/checker/gate/CAPRUN constants (128-133), argv construction (47-56), RLIMIT_FSIZE 16 MiB in preexec_fn before exec (26-27, 76), start_new_session=False (76), one child by sequential Popen/wait (75-79), exclusive `x` opens (19-21, 74), STOP handler (150-155). Prior defect C2 is satisfied by construction: same retained instance only.
- Caller self-hash: not embedded (136); REGISTRATION records aaafa62a… for root preflight; the regression confirms main() carries no dispatch_batch self-pin.

Behavioural note: `hard = None` plus the short-circuit `not mathematical or returned < hard` avoids a TypeError on non-mathematical stages (regression row "hard None").
## B. Timing contract

**CONFIRMED** as admission policy plus a post-return rejection; not a real-time proof, and none is requested.

- DEADLINE is the literal 13:35:00 UTC (line 12) and equals the registration's prospective cutoff. Root's 13:40 task stop appears only in REGISTRATION/report as external and grants no mathematical time.
- hard = min(DEADLINE, first_math+360) (45) with first_math set once (44): every mathematical stage recomputes the same value from the same two constants. It is never derived from the return time. Regression: a later stage's hard is identical; the absolute deadline governs when first_math+360 is later.
- Admission is strict `now+wall+15 < hard` (46): equal room fails; +2 s (old margin) and +14 s room fail; 15.001 s passes.
- `returned` is captured immediately after process.wait (79-80), before the telemetry read, PGID quiet scan, digest recheck and dispatch record (81-90). The record stores hard_cutoff_epoch, returned_epoch and admission_margin_seconds (88-89). The NONDECISION require (91) precedes the defect/dummy/rc==0 branches (92-120) and does not read rc, so a returncode-0 mathematical child returned at or after hard is a STOP (regression: equal, +0.001 s, +300 s all fail; -0.001 s passes). The STOP handler writes batch.STOP.json carrying those fields (153).
- Budget arithmetic: caps 60+7×30+30 = 300 s inside 360; the last stage admits while now < first_math+315, so a full-cap progression (270 s plus per-stage overhead) fits; any cap hit is a STOP anyway.
- Stated limits (Astra §2, PENDING-CONTROLS): the 15 s margin is conservative policy; CAPRUN's sampled RSS/lifecycle, 0.25 s grace and POST_KILL_OBSERVE_SECONDS=1.0 (read by root at CAPRUN line 47; CAPRUN uncharged here, value consumed) persist; a delayed process is rejected, not made earlier. With grace plus observe = 1.25 s the prior gate's +2 s GAP is closed by margin, not by a scheduler proof.
## C. Static precision delta

**CONFIRMED** (static; not executed).

- Guard precondition: lines 12-14 require rows[-1].polynomial[0] == [[0]*12,"-1","1"], the same constant the checker's own `remove_constant` precondition targets (checker 223-227, 241-243). guard = omega·a·b − 1 (checker 203) has constant −1 and read() enforces sorted keys (57), so the origin term is first.
- Genuine rounding: large = −(2^80+1) needs 81 significant bits and a double carries 53, so int(float(large)) = −2^80 ≠ large with magnitude above 2^53; line 18 asserts difference, magnitude and canonical string. Reasoned from the source, not run.
- Float-type case, separately labelled: lines 20-29 require the reason exactly "floating point anywhere in artifact" (checker 32, the no_floats sweep at 40 before schema).
- Canonical STRING case: lines 30-39 put the rounded integer's decimal string into the guard numerator. The parser path (checker 59-62) accepts it: str, int round-trip, num≠0, den 1, gcd 1. rows[-1].polynomial is read nowhere before line 205 (the E1/E0 loop 166-176 covers rows 0-18; restoration 199-204 reads restored[...]), so the first failing demand is exactly "full guard row" (205). v2 requires that exact string, which implies no parser rejection fired. This is the prior gate's D correction, items 1-4, exactly.
- Receipt: sha256 of the raw artifact bytes (42), both synthetic integers, both rejection labels, explicit limited scope (48); the old generic "string_roundtrip" field is gone.
- Runs only behind authorize: lines 5-6 before `from checker import` (8); the caller registers it as operation 'check' with exact.json pinned (caller 60, 146; gate 66). Checker e2970c71… unchanged.
- Not claimed and correctly not consumed: actual coefficient sizes or positive parser fidelity (Astra §1 declines the prior gate's "no coefficient exceeds 2^53" sentence; no artifact exists).

Cosmetic, old-accepted: the receipt file object is not explicitly closed, the same pattern as the frozen helper; CPython closes it immediately. Not blocking.
## D. Metadata-only regression: tested vs remaining LIVE

**EXECUTED: 53/53 rows as expected** (box/predicate_regression.py, .out).

What ran: `ast` parse of the charged v2 caller; extraction of (a) the dummy-descendant branch minus the three statements reading the uncharged stdout file (100-102), (b) the `if mathematical` admission block, (c) the post-return require, (d) the DEADLINE expression, (e) the main() pin constants; (a)-(c) exec'd with a stub require against the pinned telemetry and mutations; (e) compared with charged bytes. Under 1 s, 64 MiB.

- Sequence: actual passes. EMPTY, deleted SENT, deleted kill pair, both reorders, extra fifth event, MISMATCH, NOT_FOUND, GROUP_GONE, wrong signal, "15" string, bool, renamed stage all fail with "unexpected dummy identity/signal sequence".
- Types/identity: 15.0 and 9.0 fail with "dummy signal is not an exact integer" (tuple equality passes, the type check fires). Foreign observed pid, pgid, start identity, a missing observed_pid key and top-level pid≠pgid fail with "dummy MATCH identity inconsistent with registered leader".
- Status: NORMAL_EXIT with rc 125, resource cpu, rc 0 fail with "dummy did not exercise RSS cap"; cleanup false and RSS at cap fail on the retained requires.
- Timing: stored hard = first_math+360, or the absolute 13:35 epoch when earlier; no refresh at a later stage; admission equal/+2/+14 fail, +15.001 passes; post-return equal/+0.001/+300 fail regardless of rc, -0.001 passes; non-mathematical with hard None passes. Line order 79 < 80 < 90 < 91 < 120 asserted from the AST.
- Pins: precision/checker/gate constants equal the charged bytes; one appended or one flipped byte fails; probe constant equals REGISTRATION and the prior gate; REGISTRATION caller pin equals the charged caller; enabled and dispatch_authorized are false.

NOT tested here (LIVE same-caller dummy remains, under NEW root authority only): the stdout-custody requires (100-102), the quiet() PGID scan and PID-namespace check, actual CAPRUN emission of the four events in the fresh job directory, wall/CPU/RSS enforcement, the five refusal modes and valid sentinel, the seven checker modes and the precision helper at runtime. These are the PENDING-CONTROLS items.

Blocking delta: NONE. Minimal fix required: none.
## Verdicts

A CONFIRMED: v2 implements the proposed four-event tuple, MATCH identity chain, int-only signals, RESOURCE_CAP, probe/corrected-precision pins, and leaves host/argv/source-pins/filelimit/one-child/exclusive-output unchanged on the same retained instance; caller self-hash is root preflight. B CONFIRMED: stored hard = min(13:35, first_math+360), strict +15 admission, returned ≥ hard is NONDECISION before any rc acceptance, no refresh; 15 s is policy, CAPRUN limits persist. C CONFIRMED: guard precondition, genuine >2^53 rounding, separate float-type rejection, canonical-string mutation reaching exactly "full guard row", artifact sha and explicit scope; behind authorize; checker unchanged; no coefficient-size or fidelity claim. D EXECUTED: 53 metadata rows behave as required; live dummy and all runtime controls remain PENDING. No dispatch, worker, allocation or follow-on authority is created.
## 5. Input pins (generated from sha256sum, hash order)

| sha256 | file |
|---|---|
| 2ac296b13ab168a36bdc56dbf2227fb6fbabdf214cdfdef866e79717ca11b0e1 | f10-r1-engineering-caller-v2-astra-20260909.md.artifact.json |
| 48a96693ac727ef22e5856aec9e0c90c0df890154db686ed8a6fd50651256de1 | dummy-descendant.telemetry.json |
| 56400dd32f4940a0e77b2da79e9b90792b51588d01f0f1a2fded30efebb0af90 | precision.py |
| 578b728248b4f896cc5e810140290af79aca15f3fdd27668a47aca3ddbaddb57 | REGISTRATION.disabled.json |
| 946e07d0f33507d6a4a5322fb6055ea802e91577a3ca2890b75e5e4dc46b30c5 | f10-r1-caller-stop-gate-fable5-20260909.md |
| a0ad0986c1b132c4abdfb3cbd5867635726df3688e7e3f4c141ae481d609b2f2 | PENDING-CONTROLS.md |
| a6a02533681a057b6f27b11e320e2d6bda8c0e70f3f1776d4be12c7055c4cb1d | precision.py.diff |
| aaafa62a7aa96ab7823e889c7d8800add04b9699a9e736ccdeb883557e812640 | dispatch_batch.py |
| bb55f78ffeb773bb07c9501b08b22af82c971073634829354464d3d4e4a5a50a | f10-r1-engineering-caller-v2-astra-20260909.md |
| c3af896c2ada82ee661eaf7cd9f6700862cd6958d0e62cb41eb0b31a811fbe02 | dispatch_batch.py.diff |
| cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6 | execution_gate.py |
| e2970c71774607e211ecc7e0f001a0dc02d02410e303ca58cf7c17ab77b9f545 | checker.py |

Own box: predicate_regression.py, predicate_regression.out, inputs.sha256.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check over this body; no corpus scan.

<!-- BODY-END -->
