# F10 r1 normalized runtime packet: FIRST static gate over the caller delta and eight finite controls

2026-09-09, Fable 5.1 (claude-fable-5-1). STATIC TEXT REVIEW ONLY. Launch 19:57:51 UTC; controlling stop 20:17:51 UTC (launch+20 min, earlier than 20:18:00), never reset. No compile, import, execution, test, fixture, mathematical subprocess, CAS, arithmetic script or Python of any size ran. No network, AWS, SSH, /proc, agent, corpus, ledger, live peer or provenance follower was touched. Owned outputs: this file and box/f10-r1-normalized-runtime-gate-fable5-20260909/ only. Nothing here is a runtime PASS, a dispatch authorization, a cap, a worker choice, a solver or an ideal decision.

## Custody and read scope

All fifteen charged inputs were hashed with sha256sum in /tmp/jc2-lane.y34DNP/inputs before any body read; all fifteen digests equal the ordered list in the charge, line for line (15/15). The same sha256sum output, in charged order, is box/f10-r1-normalized-runtime-gate-fable5-20260909/input-custody.sha256. Both owned targets were absent at launch. All fifteen inputs were read WHOLE with cat -n (1598 lines). The five accepted copies carry exactly the hashes the new caller pins at dispatch_batch.py:164-169 and the harness at semantic_controls.py:31-33: generator d444d022..., checker 091bbf35..., algebra 7d565299..., helper cbfe55ff..., probe 02913a1c...; helper and probe equal the accepted retained gate's rows 8 and 9 (input 15). They are premises at their accepted tier and are not re-hardened. CAPRUN 4435279d..., exact.json 168bdfd3..., admissibility and frontier pins are future literal runtime bindings only; no body of theirs exists here. The old caller named on the minus side of caller.diff is not charged; every plus line and every context line of the diff was checked against the new file (below), but the old/new literal comparison against both frozen files remains root's check, as charged.

## Verdict summary

A CONFIRMED. B CONFIRMED. C CONFIRMED. D CONFIRMED: ready for root to CONSIDER one separately registered bounded engineering validation. No REFUTED item. Smallest real defect found: none that blocks; the smallest real observations are listed under GAPs and are documentary, not code repairs. No repair is recommended.

## A. Caller adaptation: CONFIRMED

Literal delta. The four hunks of caller.diff are internally consistent (old/new line counts 7/7, 14/15, 7/7, 12/16) and every plus line appears verbatim in dispatch_batch.py at lines 141, 158, 164-166, 181, 189-190, 192-195 and 197-198; every context line matches. All changes lie inside main(). run() (41-136), quiet() (31-39), the dummy identity block (110-133), preexec RLIMIT_FSIZE (28-29, 90), start_new_session=False (90), the namespace check (86, 91), the post-return PGID check (96), the pre/post pins (68, 97), the frozen authority (83-85, 98) and the admission and cutoff logic (45-51, 106) are untouched.

Normalized fixed vector. Lines 163-172 pin nine constants (generator, checker, algebra, helper, CAPRUN, probe, exact.json, admissibility, frontier); line 174 adds the caller, the harness and /usr/bin/python3; line 175 demands set equality, so the vector is exactly eleven local files plus the interpreter, as VALIDATION.md:12-13 states. Lines 176-179 force the nine constants and the actual digest of every entry, so the caller and harness pins are root-preflight values that must equal 8cb4d31f... and c0c83c73... for these charged copies. The registration is hashed into fixed_files (180), so it enters every authority.

Exact argv. generate: trailing exact.json, normalized.json gives generator.py an argv of length 4 (generator.py:124) with operation build (:125; caller 189). full-check: length 5 (checker.py:231), operation check (:232; caller 190). semantic-controls: length 6 (semantic_controls.py:12), operation check (:14; caller 195). Probe: argv[2] is frontier.json, a fixed pin, so the helper's check-side rule at execution_gate.py:66 is satisfied; argv[3] sentinel, argv[4] plain or descendant (probe.py:7-8).

Backend pin in every operation. algebra.py is in fixed_files, hence in every per-operation authority (62, 77) and re-hashed by the helper before any work (execution_gate.py:68-70) and by the caller after return (97). batch.PASS binds normalized, receipt, generator, checker and backend hashes (196-199).

Receipt bindings. Line 192 requires status PASS-NORMALIZED-REPRESENTATION-NOT-IDEAL-DECISION, the string checker.py:228 returns and semantic_controls.py:38 requires; 193-194 bind source_sha256 to the exact.json constant (checker.py:242 writes SOURCE, identical to caller 170 and generator.py:10) and artifact_sha256 to the live digest of normalized.json. normalized.json is re-hashed fresh at full-check and at semantic-controls (63-70) rather than carried, and the harness closes that under the cooperative rule at semantic_controls.py:25 and :40.

Sequence and inherited discipline. Five refusals (183-184), valid sentinel (185-186), dummy (187), preflight.PASS (188), then generate, full-check, receipt binding, semantic-controls (189-195): seven preflight children, three mathematical children. Refusal tracing against the helper is unchanged from the accepted retained gate: disabled hits execution_gate.py:19-20, wronghost 29-30, argv 41-43, cap 56-57, missing-input 66-67, each before probe.py:7 writes its sentinel; 108-109 demand nonzero NORMAL_EXIT and no sentinel. The dummy still requires rc 125, RESOURCE_CAP rss, TERM and KILL sent, cleanup and reaping, group RSS above the 32 MiB pin (162), two custody lines in the recorded PGID, and the exact event list MATCH, SENT 15, MATCH, SENT 9 with integer signals (118-133); quiet() excludes zombies, so no live non-zombie group may remain (96). AGGREGATE is wall seconds, not CPU (155); per-operation CPU and RSS are CAPRUN wrapper limits; no strict real-time guarantee exists (VALIDATION.md:24-25).

## B. Eight controls: CONFIRMED

Entry. The harness authorizes first (semantic_controls.py:14) and imports copy, hashlib, json, checker and algebra only afterwards (16-18); importing checker executes no mathematics (checker.py:230-246 guard). It binds the original to checker.SOURCE (34), the three code files to the expected constants and to its own registration (35-36), the producer hash (37), the genuine receipt status, source and artifact (38-40) and the five inventory fields (41-42), all of which checker.py:228 emits. It never imports generator and never calls checker.verify on the unmodified object; the eight cases are labelled checker.verify IN-PROCESS (64) and counted at 118.

Fixture discipline. reject() (46-64) deep-copies, mutates outside the try, requires an actual change (49), writes exclusively (51-52), hashes (53), rereads and requires equality (54-55), calls verify on the reread object (56), requires the exact exception class and string (58-59), raises on acceptance (60) and rehashes (61). A wrong reason raises out of the handler, a precondition failure raises outside the try, and any uncaught exception is a nonzero child exit and caller STOP (135). Control inputs are rehashed at 119 before the receipt.

Trace against checker.verify (order: nofloat 69, schema 70-73, units 74-85, D and ODE 86-88, maps 89-93, matrices 110-128, backmaps 129-137, third and fourth stages 138-151, A/B 154-168, Pi 172, bracket 173-176, poles 197-211, G 217-219, H 220):

| Fixture | First failing line | Reason string |
|---|---|---|
| completed-matrix-entry | 121 (band 1, i=0, j=0 is the first comparison) | source-bound completed matrix |
| historic-third-forcing-index | 145 (n=0 if deltaC1 nonzero, else n=1) | full affine forcing including third correction |
| full-Pi-sign | 172 (first use of data['Pi']; -Pi differs, char 0) | full Pi |
| H0-projection | 220 | H0 whole constant target |
| H1-projection | 220, second half (H0 untouched) | H1 whole linear target |
| float-anywhere | 69, nofloat(data) precedes everything | float forbidden |
| noncanonical-rational-string | 61 inside Flat.read at 74: int('+25') is 25 but str(25) is not '+25' | canonical rational |
| canonical-wrong-large-integer | 220 after Flat.read accepts the exact string | H0 whole constant target |

All mutated wires are produced by the production Ring (sorted, canonical Fraction strings, v-degree below 7, no s axis), so Flat.read accepts them and the failure is semantic, not a parse accident. eqz at 121 and 145 compares z-to-s^2 images; the mutated objects are s-free, on which that map is injective, so a nonzero delta cannot vanish in the image. Every expected class is ValueError because algebra.require raises ValueError (algebra.py:10-12) and Flat.read uses it (checker.py:13). The precision precondition at 111-112 is genuine: 2^53+1 rounds to even, to 2^53.

Historic fixture. Lines 77-78 take U=maps['2'][0] and d0=maps['2'][2] and gap=z-U*d0 with z=atom(2), not D[0]; 79 forms deltaN_i=gap*((6-i)D[i+1]-(7-i)D[i]) for i=0..4 with D[5]=1 (generator.py:19-25 orders D by theta power, D[0]=b); 80-84 are exactly the displayed propagation; 85 requires an actual c3 change; 86-88 retain h3. Manual derivation from the displayed operator 4CV'-4C'V with C=theta^3+F theta^2+H theta+a and V=V0+V1 theta+V2 theta^2: CV' = 2V2 theta^4+(V1+2F V2)theta^3+(F V1+2H V2)theta^2+(H V1+2a V2)theta+a V1, and C'V = 3V2 theta^4+(3V1+2F V2)theta^3+(3V0+2F V1+H V2)theta^2+(2F V0+H V1)theta+H V0, so the difference times 4 has coefficients -4V2, -8V1, -12V0-4F V1+4H V2, 8a V2-8F V0, 4a V1-4H V0, which are the producer's lines 56 and 58. Solving the theta^4, theta^3, theta^2 rows for the displacement gives deltaV2=-deltaN4/4, deltaV1=-deltaN3/8, deltaV0=(-4F deltaV1+4H deltaV2-deltaN2)/12, and the residual rows give deltaC1=8a deltaV2-8F deltaV0-deltaN1, deltaC0=4a deltaV1-4H deltaV0-deltaN0: the harness lines 80-84 verbatim. c3[0] is row(1,5), the theta^1 residual, and c3[1] is row(0,6), the theta^0 residual (generator.py:70), so zip order at 87 is right. deltaN4 is nonzero on any genuine artifact (gap carries the bare z monomial, and 2-3D4 with D4=6F/5 is nonconstant), but whether deltaC1 or deltaC0 survives is a runtime precondition guarded at 85: its failure is STOP, never a false rejection. The operator itself and the residual sign convention are premises from the accepted third band; the rejection at 145 is invariant under both, since any nonzero c3 displacement fails the original-source affine forcing there. No alternative bad source pair is claimed (producer :66; VALIDATION.md:60-65).

Early versus late. Matrix and third forcing fail at original-source bindings (121, 145) before A/B. Pi and H0/H1 fail at projections (172, 220); the H fixtures traverse the bracket and pole code positively with unchanged A and B before 220, which is not negative late coverage, exactly as the harness negative_limit (126) and VALIDATION.md:73-74 say. The large integer is one exact semantic rejection, not nested-parser fidelity (124).

## C. Genuine positive receipt scope: CONFIRMED

The five inventory constants at checker.py:228 are typed values; the conditions behind them are code: 20 slots by ids (101), all 19 low rows with the unsquared S^0 additions (181-187) and the guard (188, 196); 9 G (217-219); H0/H1 (220); 8 bands as six identically zero upper bands (175-176) plus bands 0 and 1 bound row-wise (187); 10 poles as the whole negative part of the direct inverse (198-211). Custody boundary: the receipt is accepted only when CAPRUN reports rc 0 NORMAL_EXIT under the caller (135), the record stores the telemetry hash (102), and the receipt carries the helper custody (242). Backend immutability: algebra.py is hashed in every authority and named in the batch receipt. Known STATIC17n qualifications persist unchanged: c2 length not inventoried (132-135) while generator.py:67 emits two; rows not containers; gauges (189-190) not a resonance theorem; the f5 literal at generator.py:17 and checker.py:81 is byte-identical; any left inverse passes 142. h3/h4 are runtime-enforced at 146 and are not re-proved here.

## D. Readiness: CONFIRMED (to consider, nothing more)

The only registration is dispatch.registration.DISABLED.json with enabled false and null worker, cwd, deadlines, aggregate and profiles; the caller refuses it at 141-142 and the helper at execution_gate.py:19-20. After root creates a fresh exclusive directory on an owned EC2 instance, pins the eleven files and the interpreter (including caller 8cb4d31f... and harness c0c83c73...), writes both +00:00 deadlines, the integer aggregate and five profiles, and observes its own preflight, this packet is ready for root to CONSIDER ONE bounded validation of generate, full-check and semantic-controls. I choose no cap, deadline or worker; no count, height, speed or memory is measured or forecast; no univariate adapter or solver is involved. No repair is necessary; generic hardening stays DEFAULT-OFF.

## Custody table (from sha256sum output, charged order)

| # | input | sha256 |
|---|---|---|
| 1 | dispatch_batch.py | 8cb4d31f9c7673107116a93d0b1b5f13bbc517f46a31a9075e0d3f4815c28163 |
| 2 | semantic_controls.py | c0c83c734a4a70e9d0320cd8cbc58f822ef180cc1ce297b772273754dfbd7f55 |
| 3 | caller.diff | fe0fe96682b5ba4c69a776110d3c0b6db3061cd6de73c3975588a17ce2811ac2 |
| 4 | checker.py | 091bbf35693c52833f2de936eeecd2e734f8404f26e9c68039bb8ab6aaecb551 |
| 5 | generator.py | d444d022593c99a8d5a22d9cd9cbcac2bea9c88ef1a305d3c1c8ddf1635a6d8e |
| 6 | algebra.py | 7d565299faba1a8921fdb36f345af2cae49254fa59730e0e3c7a1f98e587d9dc |
| 7 | execution_gate.py | cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6 |
| 8 | probe.py | 02913a1caf8cb5ebe2ec7c404ede0247a1954baee3751af8b2645496f6b6e1a7 |
| 9 | dispatch.registration.DISABLED.json | b6f569d12712a5418be801f60fb2d701695e12cf4b162281d5170dbeff5d326f |
| 10 | VALIDATION.md | 102cc0f35706b15e557c142a3642099d017ec4c1fe412194a352e92e5bd8ef13 |
| 11 | READ-SCOPE.md | df75c0a94e6531c27210cdfaa5ee09a30f8f141de37595a4125a787e6e5caf43 |
| 12 | f10-r1-normalized-runtime-code-astra-20260909.md | c56eb0b81661fee66a170099a9e0655a5b5fe86456829e59b9e3c237e27feb0a |
| 13 | ...code-astra-20260909.md.artifact.json | 19475021ccafc7a55e2b5da31f42b1504ffcda41b03386ca029296732a50e96d |
| 14 | f10-r1-normalized-backend-gate-fable5-20260909.md | 0f653f5311a55f8fce8aa04ef9e56e6f8c8e5e82284a8c92c7077aa20cb104de |
| 15 | f10-r1-retained-runtime-gate-fable5-20260909.md | f8a34d1c96be944fa28f8d5c5b7d60ee9ad093d7a81634c34b404524b7949435 |

## GAPs and limitations

(i) No compilation: syntax of the caller and harness is verified by reading only; I found no syntax or API error, including the chained comparison at semantic_controls.py:36 and the ValueError raised from inside the except handler at 58, which still exits nonzero. (ii) The minus side of caller.diff rests on the diff text; root verifies it against the frozen old caller. (iii) The inventory check at semantic_controls.py:41-42 compares constants that checker.py:228 always emits; it is a typing check, not evidence, and the packet does not claim otherwise. (iv) The historic fixture's fidelity to the old rule depends on the accepted third-band operator and sign convention; its rejection does not. (v) Whether deltaC1 or deltaC0 is nonzero, artifact and fixture bytes against the 16 MiB cap, and the cost of eight full in-process verifications are runtime facts; no forecast is offered. (vi) Staging notes inherited from the retained gate stand: stage exact.json as a regular file, and keep no file named plain or descendant in ROOT. (vii) Own-only collision check; no corpus scan. Deviations from the charge: none. The custody file was written by redirecting sha256sum; this report was written with the editor tools only, no heredoc or script.

## OPEN(S) RAISED

- OPEN[F10-R1-NORMALIZED-RUNTIME-PREFLIGHT-AND-BATCH] QUANTITY: one preflight.PASS.json with exactly seven records (five refusals with nonzero NORMAL_EXIT and no sentinel, one valid sentinel, one dummy with the MATCH/SENT15/MATCH/SENT9 sequence) followed by one batch.PASS.json whose full.receipt.json carries status PASS-NORMALIZED-REPRESENTATION-NOT-IDEAL-DECISION with the artifact and backend hashes bound, and whose controls.receipt.json lists exactly eight EXPECTED-REJECTION cases; value <= 1 of each, or exactly one named STOP string in batch.STOP.json. CHEAPEST TEST: the single root-registered run described in D on a fresh directory with this exact caller and harness, after root's own preflight and fresh physical, source and caller pins. WALL: unknown; the preflight is seconds-scale by construction and the three mathematical children are bounded only by root's caps; no estimate is offered. COLLISION: own-only; this OPEN supersedes the retained gate's OPEN[F10-R1-RETAINED-RUNTIME-PREFLIGHT-AND-BATCH] (input 15, line 94) for the normalized packet and repeats no other identifier.

## COLLISIONS

status: EMPTY

- NONE - this report and its box were absent at launch; own-only publication. Scan at 20:08 UTC found three non-owned items carrying the gate name, none a competing report: the harness files xmodel/f10-r1-normalized-runtime-gate-fable5-20260909.log and .run.v2, and the root invite directory box/f10-r1-normalized-runtime-gate-20260909/. None was written or relied on.

## Own whole-read and completion

Own whole-read at 20:08 UTC by cat -n and grep of the section list: custody and read scope, verdict summary, A, B, C, D, custody table, GAPs and limitations, OPEN(S) RAISED (one entry with quantity, relation token, cheapest test, wall stated as unknown, own-only collision), COLLISIONS. Every 64-hex token in this report was cross-checked by comm in both directions against the owned input-custody.sha256: all fifteen custody digests appear, none is unmatched, and no other 64-hex token exists in the report. No placeholder remains. No Seal, no charge_basis, no marker before this line. Completed before the 20:17:51 UTC stop; all writers idle; no execution authority, worker, cap or registration was created.

<!-- BODY-END -->
