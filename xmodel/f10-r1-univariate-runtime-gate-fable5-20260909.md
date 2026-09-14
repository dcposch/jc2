# Gate: FIRST static delta over the univariate runtime caller and seven controls (hostile manual read)

status=COMPLETE; verdict A CONFIRMED, B CONFIRMED, C CONFIRMED, D CONFIRMED; no REFUTED; no blocking GAP; no new OPEN; smallest concrete defect found: none

## 0. Custody and read scope

Launch 2026-09-09 20:43:31 UTC; controlling stop 21:02:00 UTC (earlier than launch+20 min = 21:03:31 UTC), never reset. Both own targets (this report and box/f10-r1-univariate-runtime-gate-fable5-20260909/) were absent before any write. All 17 charged snapshots in /tmp/jc2-lane.ddmroW/inputs were hashed with sha256sum before any body read; every digest equals the ordered list of the assignment (custody table below, taken from that sha256sum output). The old accepted caller and old harness are not charged; caller.diff is consumed as the premise for the old side, together with root's cmp=0 statement.

Read WHOLE by cat -n: caller.diff, dispatch_batch.py, semantic_controls.py, checker.py, adapter.py, algebra.py, execution_gate.py, input_evidence.py, probe.py, dispatch.registration.DISABLED.json, READ-SCOPE.md, VALIDATION.md, the producer report, its artifact.json and custody.json (15 files). Read as heading/verdict SLICE only, hash-verified: the two accepted gates (adapter gate 17p, normalized runtime gate 17r); their verdicts are premises and were not re-hardened. Not charged and not read: input-pins.json and publication.json named in custody.json, run_capped.py, admissibility.md, frontier.json, exact.json, and any normalized runtime artifact, receipt or evidence gate.

Documentary operations only: sha256sum, wc, head, grep, sed, one shell while/grep -F -x loop, apply_patch. ZERO python (including empty), compile, import, test, CAS, arithmetic, fixture, network, AWS, SSH, proc, agents. Nothing executed; every path below is a static trace.

## A. Narrow caller delta: CONFIRMED

- Diff is literal. All 33 `+` lines of caller.diff occur verbatim in dispatch_batch.py and none of its 16 `-` lines survives (grep -F -x both directions). Hunk offsets match the new file: run() +78; main() 142, 159, 165-167, 174-182, 191, 199-216.
- run() (dispatch_batch.py:41-137) changes only by the added key at :78, copying registration['normalized_acceptance'] into every per-operation authority. Present and untouched by any hunk: five defect injections :79-83; exclusive authority open('x') :22/:84, chmod 0o444 :85, re-digest :99; CAPRUN parent argv :56-61 with cap strings :54-55; PID-namespace equality :87/:92 and caller stat :93; fixed 15 s admission :46/:51; hard cutoff min(DEADLINE, first_math+AGGREGATE) :45-50 stored in the record :104 and post-return check :107; RLIMIT_FSIZE 16777216 via preexec_fn :28-29/:91; start_new_session=False :91 (no new PGID); live-PGID sweep :31-39/:97; source re-digest after return :98; defect refusal :108-110; dummy sequence :111-134 (rc 125, RESOURCE_CAP rss, TERM then KILL, exactly four identity events, integer signals, leader reaped); cap/failure STOP :136. Seven preflight children :193-197 unchanged.
- main() binds 13 local files + interpreter: nine literal pins :164-173 (adapter 11ebf430, input_evidence d262f3d4, checker 6547063b, algebra 7d565299, execution_gate cbfe55ff, probe 02913a1c all equal the charged snapshots; run_capped, admissibility, frontier are external instruments), the two root-accepted digests :181-182, and dispatch_batch.py plus semantic_controls.py taken from the registration :184 and verified on disk :188-189. Exact vector equality :185, literal pin equality :187, registration self-pin :190, exclusive job outputs :191-192.
- Acceptance is required before any child: dict with status ROOT-ACCEPTED-GENUINE-CHECKER-RECEIPT :174-176 and the two normalized backend version hashes :177-179. Those two hashes are metadata constants only; the vector's checker.py is pinned at 6547063b, so no conflicting normalized checker is staged and no basename conflict exists.
- Check authorities pin adapter.py: files=dict(fixed_files) :62 inherits all 14 pins into every authority, so checker.main:138-139 and semantic_controls.py:31-33 find adapter.py registered.
- DISABLED template: enabled false; null job, instance, host, cwd, both deadlines, aggregate, all five profiles and acceptance; empty file_sha256; profile names probe/dummy/adapt/check/controls equal :159. It is refused at :142 before anything else. No new supervisor, allocator, cap or solver.

## B. Production sequence and receipt distinction: CONFIRMED

- adapt :199: three trailing paths, child argv length five; adapter.py:80 requires 5; authorize(...,'build') :81 matches operation='build'; verified_input(auth, normalized.json, normalized.full.receipt.json) :84; output univariate.json opened 'x' :87.
- full-check :200: four trailing, length six; checker.py:131 requires 6; operation check :132, and execution_gate.py:66 needs argv[2]=normalized.json pinned (it is fixed). checker.main:136-137 needs univariate.json pinned: run() :63-70 adds it because it exists after adapt. Output univariate.full.receipt.json 'x' :142; the trailing loop skips it because it does not yet exist, and its pre-absence is enforced at :191-192.
- semantic-controls :210: five trailing, length seven; semantic_controls.py:12 requires 7; the four inputs argv[2:6] must be registered :22-25, satisfied because univariate.json and univariate.full.receipt.json now exist and are added by :63-70; controls.receipt.json 'x' :104-105; each fixture 'x' :47-49 beside it.
- Receipt binding :201-209: status PASS-NINE-ROW-ADAPTER-NOT-IDEAL-DECISION equals checker.py:124; expected_evidence :202-206 is key-for-key the dict returned by input_evidence.py:40 with the same three constants (input_evidence.py:8-10); univariate_sha256 equals checker.main:141. The receipt is read only after run() has required rc==0 and NORMAL_EXIT :136 of the child that wrote it, and it could not pre-exist :191. A spelled JSON status alone therefore never passes: the full input_evidence helper (original source digest, generator/checker versions, 20/9/2/10/8 scope, both artifact pins, acceptance binding) runs inside every mathematical child, and root acceptance is consumed, never produced (input_evidence.py:37-39, dispatch_batch.py:180).
- normalized.full.receipt.json is only ever an input (:199, :200, :210; VALIDATION.md:44-45); univariate.full.receipt.json is only ever the new output. No generator.py, exact.json or generate step exists in the vector, so the prior normalized batch is not replayed. The harness contains no positive verify call (:42-95), so nothing replaces the genuine checker.main.

## C. Seven controls traced in checker.verify: CONFIRMED

Common path: reject() (semantic_controls.py:43-61) deep-copies the genuine artifact, requires changed!=data, writes the fixture 'x', hashes it, rereads, requires reread==changed, calls checker.verify IN-PROCESS, requires type(exc) is ValueError and str(exc)==reason, then rehashes the fixture. plus_one :63 is ring.read, ring.add with c(1), ring.wire (algebra.py:127-140); its output satisfies checker.parse :21-35 (seven nonnegative ints, v<7, s=0, all six geometric exponents zero, sorted keys, reduced nonzero string rationals), so no earlier parser refusal can pre-empt the designed reason. Every require in the chain is algebra.require, which raises ValueError (algebra.py:10-12), giving the exact type. Earliest failing line for each fixture, with every earlier check untouched by that mutation:

| control | mutation | first failing line | reason |
|---|---|---|---|
| Phi3-coefficient | coefficients.a + 1 | checker.py:60 (p3 x^3 term differs by 1) | all Phi3 coefficients |
| c-inverse | c_inverse + 1 | :62 ((ci+1)c = 1+c; c is nonzero because the genuine :62 passed) | actual c inverse identity |
| affine-r-constant | r[0] + 1 | :67 (r0 = -ci*a on the genuine) | affine r constant |
| indexed-row-coefficient | rows[0].coefficients[0] + 1 | :117, slot 0 of equal() | literal univariate row E1/S1 |
| missing-guard-factor | factors.pop(), q unchanged | :119, factors==['r','h0'] clause | guard equation and both factors retained |
| guard-q-coefficient | guard.q[0] + 1 | :120, slot 0 of equal() | entire guard q=r*h0 |
| omitted-dense-slot | rows[0].coefficients.pop() | :113 via dense() :64, length 3 not 4 | every univariate coefficient slot including zeros |

- No b division exists in the harness; c is a unit only through the genuine receipt bound at :36-38; nine row slots and both guard factors are required of the genuine receipt :39; :109 reads only ids before the loop, so no earlier row check sees a mutation; the removed slot is recorded as a wire, never assumed zero :89-95; changed!=data holds for every fixture because a +1 always alters the constant term and a pop always shortens the list.
- The seven reason strings occur in checker.py at lines 60, 62, 67, 117, 119, 120, 64 (grep -F); VALIDATION.md:86-94 and the producer table use the same seven strings.
- These are designed, unobserved outcomes. No new original-source bracket/pole negative, no positive parser precision, and no cover proof is claimed; checker.py:121 remains a literal COVER identity.

## D. Documentation, scope, execution plan: CONFIRMED

- VALIDATION.md:29-33 lists exactly the 13 local files + /usr/bin/python3 of dispatch_batch.py:164-185; :58-60 give the three argv shapes matching :199-210; :86-94 the seven controls; :116-120 states no measured or forecast quantity; :8-18 requires root's genuine normalized acceptance first. The producer report (lines 19-35, 43-51, 63-67) matches the code and raises no OPEN. custody.json counts (12 inputs, 16 owned, 6 copied, 2 new) and its report/transaction digests equal the charged 1155363c and c99465aa; the artifact.json body (11069 bytes, 4dcc0eb4) reproduces from lines 1-69 of the report by head and sha256sum.
- No caps, costs, fixture bytes, degrees, coefficients, solver, certificate, point, properness, unitness, source closure or JC2 outcome is stated anywhere in the packet, and none is stated here. Accepted 17p qualifications (U-slot identification via the genuine normalized checker and Pi) and the cooperative root-owned authority trust are retained unchanged (VALIDATION.md:113-114).
- Failure is STOP without retry: dispatch_batch.py:136, :218-223; VALIDATION.md:74-75.
- All current code stays DISABLED; nothing here authorizes a worker, cap, fixture or mathematical run. One separately root-registered batch may follow only after root's genuine normalized evidence acceptance and this gate. The separate normalized runtime EVIDENCE gate was not inspected and is not assumed to pass.

## GAPs and limitations (documentary, non-blocking)

- The old caller and old harness are uncharged; the "only run() change" claim rests on caller.diff and root's cmp=0, both premises.
- run_capped.py, admissibility.md and frontier.json digests at dispatch_batch.py:170-173 are constants inherited from the accepted 17r gate, not re-verified here.
- Syntax and installed-runtime compatibility of the two new files remain unmeasured, by design of a static gate.

## Custody table (sha256sum output, assignment order)

| # | file | sha256 |
|---|---|---|
| 1 | READ-SCOPE.md | 85a98b9994307f4803e07fe6c11eea3bd9335e5168df1aa312d04e79327531ca |
| 2 | VALIDATION.md | 38d46e7bb21792e696635320a39efa9aea4da75b3ba0dc789d7c88c76492a0ac |
| 3 | adapter.py | 11ebf4307e7cff9b7909020dcdf69cda32f689236453763ce9433fff66fd7b67 |
| 4 | algebra.py | 7d565299faba1a8921fdb36f345af2cae49254fa59730e0e3c7a1f98e587d9dc |
| 5 | caller.diff | 636d4a8a8e5cf2af8cf0181cbf9870eb99362c4508e4928b8745f799f262e37f |
| 6 | checker.py | 6547063b8cf2970ce0aa1e47e5a49db31c2fd4b1e97d87690c954487500a61f0 |
| 7 | dispatch.registration.DISABLED.json | c9f318bfde0235341933fd703e69650776023be7e9efa5a6d10818235ec8ceab |
| 8 | dispatch_batch.py | 9be0c70a3ab8342a79509e039860d31b6d46401ee3aeb211e24f913b3ef69558 |
| 9 | execution_gate.py | cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6 |
| 10 | input_evidence.py | d262f3d498323b4606c51828a647b7334e8885095b099acbff41d17dd6db88b9 |
| 11 | probe.py | 02913a1caf8cb5ebe2ec7c404ede0247a1954baee3751af8b2645496f6b6e1a7 |
| 12 | semantic_controls.py | cc04757ed669dab0a506579079478bf71f41ba8debde0de83944ecdd7b416a90 |
| 13 | f10-r1-univariate-runtime-code-astra-20260909.md | 1155363cbd3071900002aeac2f2d6d729ee05fa9de4af9ec04297d4f8de281e4 |
| 14 | f10-r1-univariate-runtime-code-astra-20260909.md.artifact.json | c99465aaab9ef8c7eb42bd9da348734259db42d0f75a1a223ce6a5a826c9f2e4 |
| 15 | custody.json | 36edd333fb975ee92a0960544e8d703dbba620ce36e29b5c41352468c0d77b0b |
| 16 | f10-r1-univariate-adapter-gate-fable5-20260909.md | e169b3e42828885e38f74ef7ed53e2d022151bb9588ea44d71e45eeb3a9c44c2 |
| 17 | f10-r1-normalized-runtime-gate-fable5-20260909.md | 4968f8d32261d073a7bef8d3d4a8bf1e193ed1e0eba73bb2f5237ba735d6d783 |

## OPEN(S) RAISED

None. No new bounded scientific quantity exists in this packet, so no exit-price declaration is made and no closing hash section is appended.

## COLLISIONS

Own-only check: xmodel/f10-r1-univariate-runtime-gate-fable5-20260909.md and box/f10-r1-univariate-runtime-gate-fable5-20260909/ were both absent at 20:43 UTC before the first write. No corpus scan is claimed.

## Own whole-read and completion

Own whole-read at 20:50 UTC by cat -n of lines 1-91: title, status line, sections 0, A, B, C, D, GAPs, custody table, OPEN(S) RAISED, COLLISIONS. All 17 distinct 64-hex tokens in this report were cross-checked by comm in both directions against the owned box/f10-r1-univariate-runtime-gate-fable5-20260909/input-custody.sha256, which sha256sum -c verified 17 of 17 against the charged inputs; no other 64-hex token exists here, and every 8-hex prefix in the prose is a prefix of one custody digest except 4dcc0eb4, the producer body digest reproduced by head and sha256sum. No placeholder, no exit-price line, no closing hash section, no marker before this line. Verdict unchanged after the whole-read: A, B, C, D CONFIRMED; no blocking defect; no OPEN raised; own-only collision check clean. Completed before the 21:02:00 UTC stop; all writers idle after the marker; no execution authority, worker, cap, fixture or registration was created.

<!-- BODY-END -->
