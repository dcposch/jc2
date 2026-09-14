# F10 r1 exact-decision code gate: one combined delta review (Fable 5.1)

tag=f10-r1-exact-decision-code-gate-fable5-20260909
reviewer=Claude Fable 5.1 (claude-fable-5-1); combined code/certificate-semantic delta gate, NOT an ideal decision, runtime pass, certificate or worker authority
launch=actual first command 14:14:51 UTC; hard stop = earlier of 14:29:51 and 14:29:00 UTC, i.e. 14:29:00, no reset
subprocesses=sha256sum/cat/grep/sed/find/date/diff/cp; two curl reads of official Singular spielwiese reference.doc and general.doc (narrow API check only); ONE bounded toy test of certificate.py functions (box/toy/toy_test.py, .out; `timeout --foreground 10 prlimit --cpu=5 --as=134217728 python3 -I -B`, wall under 1 s, no CAS, no fork, no network, no /proc census, no module main). ZERO engine/CAS/artifact evaluation, no AWS/SSH/worker action.

## 0. Custody and read scope

All 15 charged inputs were hashed in the invitation order BEFORE reading; the 15 digests equal the invitation list exactly (box/pins.txt, diff empty). Inputs 1–14 were read WHOLE. Input 15 (CAPRUN 4435279d…) was read only by grep for its docstring, argparse interface, identity/group sampling, terminate/reap and leader-exit handling (lines 8–15, 143–176, 288–360, 393–520, 626–660); its accepted implementation is not re-hardened. The caller's fixed pins CAPRUN 4435279d…, HELPER cbfe55ff… and PROBE 02913a1c… equal the charged bytes; execution_gate.py and probe.py are the accepted copies. The artifact 168bdfd3… is consumed as accepted (16q/r/u/w) and was neither present nor expanded. No source was mutated; the toy test imported byte-identical copies of certificate.py 0906a9d2… and execution_gate.py cbfe55ff… (box/toy/copies.sha256).

## A. Emitter and protocol — CONFIRMED (static), one installed-version question

- Ring line 39: `ring R=0,(u,ell,d0,d1,v0,v1,v2,k1,k2,k3,k4,omega),dp;` fixed Q, global dp, original order. `expression()` (20–34) re-validates canonical STRING rationals, sorted unique 12-vectors, emits `(num/den)*var^e` with no textual evaluation, and `'0'` for empty rows, so every one of the 20 slots including E1/E0 zero rows and the guard gets `poly fi=…; emitpoly(fi,"ROW/i")` (48–50). `ideal I=f0,…,f19` keeps zero generators (ncols 20).
- Export (41–45): `leadexp`, `numerator(leadcoef)`, `denominator(leadcoef)` as decimal strings, `f=f-lead(f)` loop; empty polynomial gives POLY/ENDPOLY only. One `std(I)` (52), unit test `deg==0` on nonzero entries (53), conditional `lift(I,target,U,"std")` on the unit branch only (54), dimension guard 1×1 / 20×1 (55), monic candidate export on the proper branch (59), `DONE` then `quit` (60). All in the same engine child under one cap.
- Official doc check (spielwiese reference.doc, sha in box/docs.sha256): the four-argument `lift(ideal, subideal, matrix_name, string)` form exists (lines 4488–4489). `option(stdhilb)` and `option(probabilistic)` are documented options in the CURRENT doc (lines 6015–6021), so `option(nostdhilb,noprobabilistic)` (line 40) is valid there. They are ABSENT from the retained Singular 4-3-2 reference.doc (box/d125-defect-order-gate-fable5-20260907/reference.doc has stdhilb only as a command). On an older installed binary the line raises an unknown-option error; certificate.py line 145 then refuses on nonempty stderr, so the outcome is INCONCLUSIVE on every run, never a wrong verdict. This is an installed-version/runtime question for root (PENDING item 2), not a demonstrated code fault. Smallest fix if the installed version lacks them: delete line 40 (default std already uses neither).
- `&&` in line 53: see the appended note.
- Runtime items that fail closed rather than mislead: a goodbye banner, `// **` warning or error text on stdout is rejected as unsupported/trailing output; nonempty stderr is rejected; a lift returning fewer than 20 rows prints `ERROR|lift dimensions`, which the parser rejects. Large literal coefficients are re-checked by the exact row read-back, so any misparse is caught.

## B. Certificate semantics — CONFIRMED

- dp comparator `key(e)=(deg, (−e_n,…,−e_1))` (75) is exactly the documented dp rule (smaller last differing exponent wins); it is injective so no ties exist. Toy checks: y² > x, x·y² > x²·z, x²yz > xy²z, u > omega.
- UNIT (109–114): `set(U)=={ZERO}` and nonzero forces a nonzero rational constant; `Σ row_i·T_i == U` is checked exactly with Fraction arithmetic against the ORIGINAL artifact rows, not engine echoes. U=0, U=u, U=1+u and a wrong cofactor are all rejected (toy). Dividing by U gives 1 ∈ I.
- PROPER (115–130): nonzero, monic, non-constant leading terms; every unordered S-pair (`basis[:i]`) fully reduced by `normal`; all 20 rows reduced. Buchberger's criterion then gives LT(J)=⟨LM(g)⟩ ∌ 1, so J is proper and I ⊆ J. Reverse containment is not needed and not claimed (scope string, line 130).
- `normal` (90–101) cancels the leading term exactly (`c/g[h]`), each step replaces a monomial by strictly dp-smaller ones, so it terminates; irreducible terms move to `rem`, giving a full normal form. Toy: {x²−y, xy−x, y²−y} with five rows needing multi-step reduction passes; {x², xy+1} fails its S-pair; {x²} fails containment; LM 1, non-monic and empty members are rejected.
- Parser (46–73): exact framing, DONE must be the last line, BRANCH only after 20 rows, per-tag duplicate/monomial/width/negative checks, canonical integer regex (rejects `01`, `-0`, `+3`, `3.0`, spaces, floats), reduced positive-denominator rationals. Toy: 11 malformed transcripts rejected with the designed reasons; 2^53+1 and 2^80+1 parse exactly and the rounded U is rejected.
- Robustness GAP (fail-closed, not soundness): certificate.py catches nothing but `Invalid`. Under Python ≥ 3.11, `int(s)`/`str(n)` raise ValueError above 4300 digits, and any KeyError/JSON error is an uncaught traceback. All give rc≠0, which the caller records as INCONCLUSIVE. Cofactors on the unit branch can be large; if the pinned interpreter is ≥ 3.11 the smallest fix is `sys.set_int_max_str_digits(0)` at the top of certificate.py (and semantic_tests.py) before any parse. Root duty to check the interpreter version.

## C. Caller/engine binding — CONFIRMED, two small non-blocking deltas

- Disabled root registration: enabled=false, compatibility_confirmed=false, all authority fields null; caller lines 38–40 refuse unless enabled, compatibility_confirmed and mode are set. Fixed pins (10–12, 52–53) equal the charged hashes; caller/engine/certificate/tests/interpreter/engine binary must be root-pinned externally (56–59) and are rechecked before every stage (76, 59) and after (112). Admissibility 02952e1b… retained (54–55).
- Physical worker: DMI vendor/asset tag, hostname ≠ math-hq, cwd = /home/ubuntu/<job_tag> with the new prefix (41–46). CAPRUN parent argv is the exact accepted form (81–85) and is re-verified inside every child by execution_gate lines 37–57 against /proc/ppid/cmdline. Nested engine argv `[engine,--no-rc,--no-stdlib,--no-shell,-q,-t,input.sing]` is registered in the authority (96), required by engine.py 75 and re-bound by certificate.py 141.
- Limits: RLIMIT_FSIZE 16 MiB set in preexec before CAPRUN exec (20, 106); CAPRUN's RLIMIT_CPU is inherited by the Python child and by the nested Singular (plain Popen, no preexec, `start_new_session=False`, engine.py 80–81), so both are in CAPRUN's sampled PGID. engine.py 87 checks namespace and `getpgid(child)==getpgrp()` in-process.
- Fresh controls: five refusals, valid sentinel and dummy descendant run before any mathematics in both modes (139–143); the dummy predicate is the accepted v2 four-event/int-signal/RSS block (121–135). One child at a time by sequential Popen/wait (105–109). Stored `hard=min(deadline, first_math+120, task_deadline)` (74), strict +15 admission (75), `returned` captured before telemetry (109), late return refused before any rc acceptance (118). Budget: engine 60 + verify 30 fits 120 with the verify admission at first_math+75. Exclusive `x` opens everywhere (19, 77, 79, 98, 104, 151). Verify-stage pins of receipt/input/stdout/stderr (87–89) are cross-checked by certificate.py 137–145.
- Too-fast/failed nested capture: if Singular exits before /proc reads, engine.py raises (FileNotFoundError or the line-86 mismatch) and exits nonzero; the caller records INCONCLUSIVE. If the leader exits while Singular still runs, CAPRUN waits for the exact PGID to go quiet or applies the wall/CPU/RSS caps with group TERM/KILL (CAPRUN lines 8–10, 457–520); the caller then verifies `quiet(telemetry['pgid'])` (111). Bounded and cleaned by the accepted supervisor; no attestation or scheduler proof is claimed.
- Delta 1 (non-blocking): the engine receipt's `pgid`/`namespace` (engine.py 93) are recorded but never compared with `telemetry['pgid']`/the caller namespace; the identity rests on engine.py's in-process check plus CAPRUN's pid==pgid invariant. Smallest fix: after the engine stage, `require(receipt['pgid']==telemetry['pgid'] and receipt['namespace']==namespace)`.
- Delta 2 (cosmetic, inherited from v2): the `missing-input` defect deletes exact.json from the shared `files` dict, so that stage's post-run recheck skips it; every other stage rechecks it.

## D. Designed controls and the one toy test — CONFIRMED with declared coverage limits

semantic_tests.py (designed only) covers: actual row/guard removal, swapped variables, positive unit and proper with machine-protocol round trip, truncated/trailing/wrong-ring protocol, U=0 and U=u with genuinely zero weak residual (line 55 asserts it), bad cofactor, 2^80+1 float-type and rounded-string attacks, failed S-pair and failed containment. Its statically checked reasons match certificate.py's messages. Not covered by it: any dp-versus-lex-sensitive leading term, a multi-step `normal` reduction, a multi-element Gröbner basis with non-trivial S-pairs, a U with constant plus variable terms, exponent-width/duplicate-monomial/branch-position parser paths. My toy test exercised those (box/toy/toy_test.out: 42 cases, all as expected). Deviation: the invitation capped the test at 40 cases; the script had 42 and was run once, not re-run. All cases are 12-exponent synthetic vectors, ≤ 16 nonzero terms per case (≤ 2 per polynomial), degree ≤ 3, rationals ≤ 81 bits. `semantic_tests.main`, engine, caller, probe and any artifact were not executed.

## E. Static readiness — CONFIRMED as static only; blocking deltas: NONE demonstrated

The code is statically ready for a separately registered validate job and then one decide job. Root duties remain: installed Singular path/version/hash, whether `option(stdhilb/probabilistic)` and four-argument `lift` exist in that version, `--no-stdlib` file-argument behaviour and quiet output framing, interpreter version for the 4300-digit limit, fresh absolute clocks, and the live same-caller controls. The validate/decide split grants no authority. A static pass is not a runtime pass, a certificate, or a JC2 conclusion. Recommended minimal edits before registration, none of which blocks review: delta 1 above; the int-digit limit lifted if Python ≥ 3.11; drop line 40 if the installed version predates those options.

## A-note: `&&` and the option line (official doc)

general.doc (sha in box/docs.sha256) documents `&&` as an operator at line 2603, so engine.py line 53 is valid syntax. reference.doc lines 6015–6021 state that the stdhilb shortcut "is unchecked and an unlucky prime may lead to an incorrect result over QQ" and is also activated by `option(probabilistic)`; disabling both on line 40 is therefore a meaningful exactness guard on any version that has them, and harmless to correctness on versions that do not because the run fails closed there.

## Verdicts

A CONFIRMED (static; option-name availability is an installed-version question, fail-closed either way). B CONFIRMED (exact rational unit identity and Buchberger/containment properness; 4300-digit interpreter limit is a fail-closed robustness gap). C CONFIRMED (two non-blocking deltas: receipt pgid/namespace not cross-checked against telemetry; inherited missing-input recheck skip). D CONFIRMED with declared coverage limits; toy 42/42 as expected, two over the stated 40 cap. E CONFIRMED as static readiness only; no blocking delta demonstrated; root runtime duties unchanged. No decision, certificate, worker or follow-on authority is created.

## Input pins (generated from sha256sum, invitation order)

| sha256 | file |
|---|---|
| 24b0ac8863694f949df44ceeab51415c9f0494741af8e757780f4e8a8fa45b15 | f10-r1-exact-decision-code-astra-20260909.md |
| 278b630cb76ea2265a9ffc93295c1fa0a84c6092ea3e9e9d2a5ec6eb0604b867 | f10-r1-exact-decision-code-astra-20260909.md.artifact.json |
| 1cd210424747b1c03220b8d2a8dea1ac1350d8259e81a9338f63c508681b675d | engine.py |
| 0906a9d25fbc4eb03c72b75e6b421074fb73e1f2ea3d2e33f59948ab7db4b066 | certificate.py |
| 5d03861778fcccda0e28899353427739f0d1dd4541ca97c8df873cfbdf816f74 | semantic_tests.py |
| c52a2f4cdbfe477b97f7cef2c162df3d73a1a221ebc32825acaf9aa2ad62c943 | caller.py |
| 381719c1d33d3f56313f2b9634f7b97d3e199d5334e05ee75e801aa1f7fb9a14 | caller-v2-to-decision.diff |
| cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6 | execution_gate.py |
| 02913a1caf8cb5ebe2ec7c404ede0247a1954baee3751af8b2645496f6b6e1a7 | probe.py |
| 449db5c802e1d3e65d808eb0c33d034d8cceb3e1e93b1a4f0e3a95520a9ce60c | REGISTRATION.disabled.json |
| 4468c8eca06cecda79ae3032bdb88dc99b99b9846397ed627adadb04e8a0089c | PENDING.md |
| 311d0f822970fecc363d92e6a1f8c38ac730414889bdee843875558f8362cab8 | READ-SCOPE.md |
| eee5cec3d2d819ae1bed721f1910c63384235cf1ee09f854b03f7435f0adf542 | f10-r1-exact-decision-design-astra-20260909.md |
| 0fa06c13eb330aef8e8ad489cb451922ad34f03708e2df82413b870a031b0c5d | f10-r1-caller-v2-gate-fable5-20260909.md |
| 4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2 | run_capped.py |

Own box: pins.txt, pins_only.txt, expected.txt, inputs.sha256, launch.txt, docs.sha256, toy/toy_test.py, toy/toy_test.out, toy/copies.sha256, toy/certificate.py and toy/execution_gate.py (byte-identical copies).

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check over this body; no corpus scan.

<!-- BODY-END -->
