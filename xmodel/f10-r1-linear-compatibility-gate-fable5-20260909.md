# Gate: FIRST static read of the finite generic verifier and installed-API harness (compatibility.py, generic-only caller delta, plan, docs)

status=COMPLETE; verdict A CONFIRMED, B CONFIRMED, C CONFIRMED, D CONFIRMED (static design adequacy only; NOTHING executed; no installed-API, timing or runtime result is known); no REFUTED; no blocking GAP; no new OPEN; smallest concrete defect: none blocking (documentary nits and one acknowledged coverage limit in the GAP section). This acceptance licenses at most ONE separately ROOT-registered finite generic/API batch. It is not a PASS, not actual-source engine validation, not source acceptance, not dispatch readiness.

## 0. Custody, clock and read scope

Launch 2026-09-09 22:21 UTC (inputs directory timestamp; first shell 22:21:34); controlling stop 22:37:00 UTC (earlier than launch+18 min), never reset. Both own targets were absent at 22:26 UTC before the first write; the box's final inventory is expected-sha256.txt only (see the completion section). All 19 charged snapshots in /tmp/jc2-lane.sNHqeA/inputs were verified by sha256sum against the ordered assignment list BEFORE any body read: 19 of 19 OK (table below generated from sha256sum output).

Read WHOLE by cat -n, all 19 files: compatibility.py (195 lines), dispatch_batch.py (223), caller.diff, probe.py, execution_gate.py, checker.py, evidence.py, algebra.py, READ-SCOPE.md, STATIC-CHECKS.md, VALIDATION.md, generic.plan.json, dispatch.registration.DISABLED.json, root-api-note.md, custody.json, the producer report with its artifact.json, the parent code report and the parent gate. Nothing else was read. Explicit premises, not own reads: the old caller body (caller.diff is root's regenerated literal diff with original timestamp labels) and accepted 17z (parent code accepted with unchanged solver/checker/evidence/authority contracts, no blocking defect). Not re-reviewed from scratch: the 17m theorem, checker.verify internals beyond the lines the fixtures reach, CAPRUN.

Documentary operations only: date, ls, sha256sum, cat -n, head -c, wc, two shell grep -F -x loops over the diff lines, apply_patch. ZERO python (including empty), compile, import, AST, test, CAS, arithmetic subprocess, fixture, matrix, coefficient, network, AWS, SSH, proc, git status, agents. Every number below is hand arithmetic shown inline.

Root qualification applied: with q=T^5 the target is q^5=T^25 and (T^20/K)*(K*T^5)=T^25, NOT K*T^25; the large-integer rounding control uses denominator K-1 (compatibility.py:170), not coefficient 0. The new harness implements both exactly as stated, and this report does not repeat the parent gate's wrong wording.

## A. Exact finite generic fixture inventory

CONFIRMED.

- Twelve IN-PROCESS checker.verify calls at compatibility.py:148-181 in the plan's order, five positive and seven negative; the tally require at :182-183; the recorded entrypoint string at :147 names checker.verify, not checker.main. No solver import, no evidence.verified, no source fields (:116-119: no implementation_sha256, input_evidence, acceptance or execution keys).
- Fixture shape. Nine literal ids/bounds :73-74 equal checker.py:87-88; every dense slot is present (:88 and monomial :80-83 emit degree+1 slots, empty wire = zero); the modulus :87 is algebra.modulus() as canonical string pairs, the same three-polynomial formula the checker recomputes densely (both length 8, so checker.py:46-47 accepts it); guard keys, variable xi, equation string and factors r,h0 literal (:90-92); r two slots, h0 five, q six; witness 1638 or 217 canonical '0','1' pairs (:94); row_order/column_order strings :113-114 equal checker.py:115-116.
- Hand traces, first failing need in checker.py:
  1. unit: f1=1 at rows[0] slot 0, h index 0 = 1, so total[0]=1 equals q^5=1 with q=r=h0=1 (q=r*h0 passes :105): VERIFIED-GENERIC-ZERO-QUOTIENT. Negative h=2 gives total[0]=2: :133 'full 217-coordinate sum h_i f_i equals q^5'.
  2. separator-zero: all f=0, lambda=e_(0,0). Every column value is 0; lambda*q^5=witness[0]*1=1: NONZERO-QUOTIENT. Negative 2*lambda keeps all columns 0 and gives target 2: :154 'dual target normalization equals one'.
  3. separator-T: f1=T (rows[0] slot 1). Column (i=0,j,l) has its only entry at row index (j+1)*7+l, at least 7, where lambda vanishes; rows i>0 are zero; lambda*1=1: NONZERO. Negative adds witness[7] (row T^1 v^0): the FIRST column (0,0,0) has value witness[7]=1: :150 with reason 'dual column annihilation i=0 j=0 ell=0'.
  4. precision: f9=K*T^5 at rows[8] slot 5, r=T, h0=T^4, q=T^5, so q=r*h0 passes and q^5=T^25 (26 slots, slot 25). h9 at index (8*26+20)*7=1596 is Fraction(1,K), canonical since K is odd, so h9*f9=T^25 and the identity holds: ZERO-QUOTIENT. extra_check :161-164 verifies the literal K and 1/K strings after the plain-JSON reread, before the parser. high-T30: index (8*26+25)*7=1631 set to 1 adds K*T^30 at total[30] (31 slots exist): :133. rounded: denominator str(int(float(K)))='9007199254740992'=2^53=K-1, gcd 1, so the parser passes and (K/2^53)*T^25 differs from T^25: :133. float: the denominator is a float, type(b) is str fails: :22 'canonical rational strings only'. K=2^53+1 is a tie between 2^53 and 2^53+2 and rounds to the even mantissa 2^53, so K>2^53 and int(float(K))=K-1; the harness re-asserts this at :46.
  5. zero-guard: monomial(...,0) yields all-empty slots, so r=0, q=0, h0=1, q=r*h0 passes, q^5=0, all f=0, UNIT witness 0, total 0 equals target 0: ZERO-QUOTIENT (q=0 lies in the multiplicative set). False separator: branch SEPARATOR with witness e_0, all columns 0, lambda*0=0 not 1: :154.
- Exercise discipline: negatives must differ from the positive object (:126), exact ValueError type and reason (:137-138), positive branch status by branch (:142-144), exclusive write, plain reread equality, hash before and after verify (:128-131, :145). Fixture names and order equal generic.plan.json fixture_names.
- Coverage limit, stated by the packet itself (VALIDATION.md:64-66, report section 3): every coefficient in every fixture is a v^0 constant, so the checker's bmul reduction against the monic modulus runs only with zero leading terms, and no nonconstant B coefficient or product-component path is exercised. This harness also has no unreduced-fraction, negative-denominator or wrong-modulus control; those are the parent's semantic controls, not this batch.

## B. Installed-API miniatures

CONFIRMED as design; installed behaviour is unknown until run.

- Three scalar checks :49-53: fmpq(0,1) must print '0', fmpq(K,1) '9007199254740993', fmpq(K,2) '9007199254740993/2' (K odd, already reduced). Two fmpq_mat(2,5) constructors (:61), ten entry constructions each (:64), two rref calls (:65): 3+20=23 explicit fmpq constructions, equal to the plan and the receipt literals.
- Hand RREF, consistent [1,2,3,1,0],[2,4,6,0,1]: R2-2R1=(0,0,0,-2,1); R2/(-2)=(0,0,0,1,-1/2); R1-R2=(1,2,3,0,1/2). Pivots 0,3, rank 2, equal to expected_rows :57. The b column (index 2) is not a pivot, and c=(3,0) gives Mc=(3,6)=b.
- Hand RREF, separating [1,2,3,1,0],[2,4,7,0,1]: R2-2R1=(0,0,1,-2,1); R1-3R2=(1,2,0,7,-3). Pivots 0,2, rank 2, equal to :59. The pivot sits in the b column; its identity-block entries lambda=(-2,1) give lambda*M=(-2+2,-4+4)=(0,0) and lambda*b=-6+7=1. So both outcomes of the parent's target-column extraction rule are exercised on tiny data without solver.py.
- Requires on rank (:66), exact string rows (:68), pivots as the first entry != 0 (:69-70). If str spelling, the (matrix, rank) tuple, tuple indexing or int comparison differ from the root note, a require or exception stops the child; an unsupported != would even yield pivots [0,0] against [0,3]. Fail-closed, never a false PASS. No 217-row matrix, solver.candidate, evidence.verified or source point exists in the file.

## C. Authorization order and pins

CONFIRMED.

- Order: :11-12 argv length 4; :13 authorize(argv[1], __file__, 'check') before any other import; :14 evidence (hashlib/json/pathlib only); :16-17 generic_only true and neither acceptance key; :18-20 plan = argv[2] resolved strictly, pinned in file_sha256, equal to generic_plan_sha256 and to the on-disk hash; :22-25 plan schema, generic_only, actual_source_inputs empty, 12 and 2; :26-33 four frozen code pins equal to the charged hashes and to the authority; :34 producer_environment (module path/hash pinned, interpreter pin, never verified()); :35-38 import flint, then version, resolved path and module hash; only then :40-44 checker, copy, json, Fraction and algebra.modulus. execution_gate.py:66 additionally needs argv[2] pinned for operation 'check', and generic.plan.json is in the caller's known set, so the valid path is consistent.
- The plan is a scope specification. The harness reads no acceptance, receipt or artifact; the receipt status is GENERIC-COMPATIBILITY-PASS-NOT-ACTUAL-SOURCE (:185) with an explicit scope string (:191). No installer, fallback, repair or retry exists; every mismatch is a require.
- Nit: positive_calls, negative_calls, explicit_flint_fmpq_constructors, flint_matrix_shapes, actual_solver_calls and fixture_names in the plan are frozen by hash but not cross-checked by the harness (only 12 and 2 are). Harmless: the plan digest is a literal in the caller (:170) and in the authority.

## D. Narrow caller delta

CONFIRMED.

- Literal delta: all 33 '+' lines of caller.diff occur verbatim in dispatch_batch.py and none of its 41 '-' lines survives (two grep -F -x loops); hunk positions match the new file (:1, :74 and :78, :143-147, :160-218). The old side is root's premise.
- run() (:41-138) changes only the admissibility digest source (:74) and the two payload keys (:78). Retained: admission margin and stored cutoffs (:45-51, :108), full child and CAPRUN vectors (:53-61), trailing-input pins (:62-70), seven exclusive per-operation outputs (:71-72), 0444 authority (:86), namespace and stat (:93-94), start_new_session=False (:92), live-PGID sweep (:98), post-return source hashes (:99-100), refusal, dummy and STOP branches (:109-137).
- main(): generic schema, enabled, generic_only and no acceptance keys (:143-147); -I -B, cwd, vendor, physical instance, host not math-hq, freeze contract (:148-154); two UTC deadlines, integer aggregate, 16 MiB, exactly three profiles with positive integer caps, dummy 32 MiB (:155-167); known pins including compatibility.py aaec…, generic.plan.json 1fe7…, unchanged run_capped 4435… (:168-176); FLINT metadata, closure, disjointness, exact vector, on-disk digests (:178-192); four exclusive job outputs (:194-195); five refusals, valid sentinel, dummy (:196-200) = seven preflight children; ONE compatibility child (:202-203) with trailing plan and receipt, so the full vector has 7 elements and sys.argv 4; receipt status, generic_only, three hash bindings and the exact counts dict (:204-212), byte-equal to the harness literal at compatibility.py:189-190; batch.PASS (:213-216). Eight children total; STOP file on any exception (:218-223).
- Template: enabled false, job/instance/host/cwd/deadlines/aggregate/profiles/package all null, file_sha256 empty, so main() refuses at :143-145. The proposed probe 5/3/2 GiB, dummy 5/3/32 MiB, compatibility 180/170/2 GiB, 16 MiB files and aggregate 240 (VALIDATION.md:110-116) are unmeasured recommendations, not authority. A future run still needs a separate ROOT registration with real caps, worker, cwd and clocks, and a FIRST evidence intake of its receipt.

## GAPs and limitations (documentary, non-blocking)

- The twelve generic-fixture-*.json files are written into the batch cwd with open('x') but are not in run()'s or main()'s pre-existence lists (:71-72, :194-195). A stale fixture from an aborted attempt stops the child inside write_exclusive as a generic failure, not as a named refusal. Fail-closed.
- Receipt counts (:189-190) are source-level literals, not runtime counters; verifier calls are enforced by len(outcomes)==12, the matrix and fmpq counts are structural. The docs say so.
- Producer report section 2 says "normalizing the identity pivot" for the consistent case and omits the back-elimination R1-R2; the printed rows are correct.
- The coverage limit in A is acknowledged by the packet; one v-dependent coefficient fixture would be the cheapest addition, but that is a producer choice, not a defect of this batch.
- Installed version, module path, native closure, str spelling, timing, RSS and every result remain unknown; this report establishes nothing about them.

## Input custody table (generated from sha256sum output)

| # | file | sha256 |
|---|------|--------|
| 1 | READ-SCOPE.md | 83de4974091942e6e5bbb977f6c94c2a502c7a2ba7700228ab6b8c0d331f259d |
| 2 | STATIC-CHECKS.md | a0b45b45f8d1ca9cd9971ebe87cae1f3f299b1302679541759cf97c2b3b88e54 |
| 3 | VALIDATION.md | 308c5d333215f632c6852b19e685729a631f95cfe17153cdc81224668e9a2454 |
| 4 | algebra.py | 7d565299faba1a8921fdb36f345af2cae49254fa59730e0e3c7a1f98e587d9dc |
| 5 | caller.diff | 605a1ec5acdaadf1f463426150c774ef66ff412f3aff91e2f1d006860ec3ccb7 |
| 6 | checker.py | 122842e5cf38a0eab2585c7e894c1ca9d9758dd643830d5447800642554fdf69 |
| 7 | compatibility.py | aaec1e2c56d7d4e77f7cf040a86371b813744368c9272b4f5cbe629af18af38b |
| 8 | dispatch.registration.DISABLED.json | e7b3bac7992d6215f85a191c2446babda77d44a4088e52c52d555e48a1081b14 |
| 9 | dispatch_batch.py | e1780f99c939ac37e0c149f1d22fb1d7741ad76c8ff183d3d3cc0f4da3e11b72 |
| 10 | evidence.py | cbe5a9e05c1718cd7911e68302611e0131774e10c501ca0fa890510d0ccb7767 |
| 11 | execution_gate.py | cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6 |
| 12 | generic.plan.json | 1fe704aaaa125dc8d40d5915ea74ae651277ba3f2336ab76579adc104fc305e5 |
| 13 | probe.py | 02913a1caf8cb5ebe2ec7c404ede0247a1954baee3751af8b2645496f6b6e1a7 |
| 14 | f10-r1-linear-compatibility-code-astra-20260909.md | 420f429803baa7b746d2ceffbaf3e675424fe75ee05e041619e9ce555c8f6177 |
| 15 | f10-r1-linear-compatibility-code-astra-20260909.md.artifact.json | 72830909112bdffab6016639017222fa146b83e4596ea2c3279eecb3bb8ed068 |
| 16 | custody.json | 1c65ae815fce921c3f7636812ace127cb984f1d96c0599212d41513fa44e2e53 |
| 17 | f10-r1-exact-linear-decision-code-astra-20260909.md | e73075e3b3564538c69a0a0a3fbd925c80c57d0a21122d37269bb3539b73ce93 |
| 18 | f10-r1-exact-linear-decision-gate-fable5-20260909.md | 4c3f5932e9ff77d73314fe02b3c088677f8fc3bc0971acad9ba56610cf7d405f |
| 19 | root-api-note.md | 52d0ccc730883a33ef1ba17b6d42080e40c59b1aa0d677ba4bee8f80f5a1bf3f |

## OPEN(S) RAISED

None. Quantity: new OPEN count = 0. The single remaining obligation (one separately ROOT-registered finite generic/API batch, then a separate actual-source batch) is already declared by the producer and is a registration matter, not a new OPEN. No exit-price assertion or declaration line, no seal section, no closing hash section.

## COLLISIONS

status: EMPTY

- NONE. Own-only check: the report and box were absent at 22:26 UTC before the first write; no corpus scan.

## Own whole-read and completion

Own whole-read at 22:29 UTC by cat -n of lines 1-96: title, status line, sections 0, A, B, C, D, GAPs, custody table (19 rows), OPEN(S) RAISED, COLLISIONS. All 19 distinct 64-hex tokens in this report equal, by comm in both directions, the 19 digests of the owned expected-sha256.txt, which sha256sum -c re-verified 19 of 19 against the charged inputs at 22:29 after the whole-read. The three 8-hex prefixes in section D (aaec, 1fe7, 4435) are pin literals read at dispatch_batch.py:169-175, not custody rows; 20260909 is the date. Disclosure: the two comm scratch lists (report-hex64.txt, list-hex64.txt) were produced by shell redirection inside the owned box, contrary to the apply_patch-only write rule; both were removed before this section was written, and the box's final inventory is expected-sha256.txt alone. Two wording fixes were applied in this final patch (box inventory sentence in section 0; reserved-token wording in OPEN(S) RAISED); no verdict text changed. No placeholder, TODO, exit-price line, seal or closing hash section exists; no marker precedes this section. Verdict unchanged after the whole-read: A, B, C, D CONFIRMED at static design tier only. Nothing was executed; no fixture, registration, worker, package, acceptance or actual decision was created; the first validation may proceed only by a separate ROOT registration of this exact packet followed by a FIRST evidence intake of its receipt. Completed before the 22:37:00 UTC stop; all writers idle after the marker.

<!-- BODY-END -->
