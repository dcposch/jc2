# FIRST runtime evidence gate: automatic quotient generic R3 (fable5, 2026-09-10)

lane=f10-quotient-generic-r3-runtime-gate-fable5-20260910
reviewer=Fable 5.1
start_utc=2026-09-10T02:24:36Z
stop_rule=min(start+18min, 2026-09-10T02:42:00Z)=2026-09-10T02:42:00Z; publication reserve 02:39:00Z-02:42:00Z
inputs=113 frozen copies in the lane inputs dir; all 113 SHA-256 recomputed before any body read (see box/sha-recheck.txt)
scope=NEW runtime/custody/receipt evidence only; 17zh (science/harness/static) and 17zk (caller static delta) are accepted premises; original R1/R2 are closed failures and are NOT reused
own_targets=xmodel/f10-quotient-generic-r3-runtime-gate-fable5-20260910.md and box/f10-quotient-generic-r3-runtime-gate-fable5-20260910/ (both confirmed absent at start)
method=read-only text, sha256sum/wc, standard-library Node JSON metadata extraction (no scientific module, no coefficient/fixture JSON parse, no subprocess of any solver/checker)

## 0. Read ledger

WHOLE text reads (cat): root report (169 lines, body 9986 B, own recompute of its body SHA-256 through the standalone marker = 63e9b49e05ad2c97b5cd820bdea7fc2fcb100ef82c202c3d76e58650a326b0e5, matching its printed Seal; that Seal is ROOT's, not authored here), 17zh static gate (a797cbed), 17zk caller gate (d2dd5cc2), ROOT-REGISTRATION.md, root-preflight.txt, ssh-preflight.txt, remote-before-pins.txt, same-launch-identities.txt, terminal-metadata.txt, pulled-file-hashes.txt, worker-stop.txt, metadata-reconciliation.json, remote-manifest.json, dispatch_batch.py (336 lines, cat -n), generic.plan.json, generic.receipt.json, batch.PASS.json, preflight.PASS.json, all 8 dispatch.json, all 8 telemetry.json, all 8 x (stdout, stderr, caller.stdout, caller.stderr) and the 2 sentinels.

STRUCTURED-METADATA/EXTRACT (stdlib Node, box/node-metadata-extract.js, node-sidecar-bind.js, node-recheck.js with .out files): dispatch.registration.json, all 8 authority.json, all 8 prelaunch.json, parsed for field-level comparison. This is NOT claimed as a model whole textual read of the 112-entry pin maps; every map entry was compared by program, not by eye. Two lines of the first pass (engine dict, UNIT check dict) compared key-ordered JSON strings and printed false; the third pass compares order-independently and both are true. That was my artifact, not a defect in the run; both passes are retained.

HASH ONLY (sha256sum + wc -c, never parsed): solver.py, checker.py, evidence.py, algebra.py, execution_gate.py, generic_controls.py, run_capped.py, probe.py, and all 20 .input/.candidate/.negative sidecars. No subprocess of any solver/checker/CAS, no import, no compile, no fixture read. No Git, network, SSH, AWS or process inspection.

## A. Prospective exact frozen registration

Verdict: CONFIRMED, with one documentary GAP (A1).

- Registration: 31175 B, SHA 976a8c76...49e8 recomputed locally; root-preflight.txt records mode 444 and size 31175 locally at 02:13:30, remote-before-pins.txt records the same mode/size/SHA remotely at 02:16:01.167, before the launch at 02:16:01.754. Same-launch cmdline of Main 1411 carries that SHA as the sole argv, as the caller (dispatch_batch.py L201-205) requires.
- Pin vector: registration file_sha256 has 111 entries = 11 base (10 task files incl. dispatch_batch.py + /usr/bin/python3) + 100 python_flint_files, base and package disjoint, module binding true, 9 known task pins equal the caller's literal table (L236-245) and equal my local hashes; dispatch_batch.py pin 54c55be3 equals the local copy. The caller adds the registration as the 112th fixed pin (L262). Schema, enabled, generic_only true; no univariate_acceptance / normalized_acceptance key; deadlines 02:26:00 and 02:30:00 UTC, aggregate 240, fsize 16777216, profiles exactly the L227-230 literal.
- Before/after: remote-before-pins.txt has 112 hash lines, 112/112 equal the registered vector. terminal-metadata.txt has 212 hash lines: 112/112 fixed equal, and the other 100 are owned outputs, 100/100 equal my local input hashes. pulled-file-hashes.txt 100/100 and remote-manifest.json 100/100 equal local; 100 SIZE lines equal local byte counts.
- Host/identity: ssh-preflight.txt at 02:15:17.089 shows hostname ip-172-30-0-72, vendor Amazon EC2, instance i-08d2a40f272ee9fa2, boot 32d14755-..., pid ns 4026531836, unit LoadState=not-found / MainPID=0, EXACT_NEW_DIRECTORY_ABSENT, interpreter a92f0f95 and flint __init__ 2e5f8f17 matching the registration. Known-hosts file hash 82c1f458 in root-preflight.txt equals the ROOT-REGISTRATION pin.
- Stop-before-start: the independent timer is ACTIVE with NextElapse 02:29:00 at 02:13:30.104 (raw), which precedes the first SSH contact 02:15:17.089 (raw).
- GAP-A1 (documentary): the pre-start state of the three instances (STOPPED) and the start-instance return (STOPPED->PENDING 02:13:32.175) exist only in the root report narrative; no charged raw artifact carries them. Ordering timer < first SSH contact is the only raw-verifiable part. Not a runtime defect.
- R1/R2: no authority, clock or control record from earlier attempts appears in any charged file; all prelaunch/dispatch stamps fall in 02:16:01-02:16:05. Full OS/stdlib hermeticity is not claimed and not needed.

## B. Single system launch, prelaunch/authority records

Verdict: CONFIRMED.

- One launch: same-launch-identities.txt at 02:16:01.754 shows the unit active, InvocationID 8fd1670f9fb74516a3bf5a4b6d13b9bd, MainPID 1411, cgroup /system.slice/jc2-f10-quotient-generic-r3-20260910.service; Main 1411 cmdline is the exact Exec line with the registration SHA. Same call observes MainPID=0 / inactive / dead / ExecMainStatus=0 at 02:16:05.226.
- Principal children: 42 OWNED_PID lines, 42 distinct, nine distinct PGIDs (1411 and the eight child PGIDs 1431, 1454, 1473, 1501, 1530, 1559, 1588, 1639). For each of the 8 operations the CAPRUN leader (1424, 1447, 1472, 1500, 1528, 1558, 1587, 1638) has ppid 1411 and start ticks equal to the caller_stat in its dispatch record (14603, 14632, 14660, 14688, 14716, 14744, 14772, 14827); each child has pid = pgid and start ticks equal to telemetry start_identity (14608, 14636, 14664, 14692, 14721, 14749, 14776, 14831). Every same-launch cmdline contains the exact prelaunch parent argv and child argv for all 8, including generic 1638/1639.
- Transients: 5 DISAPPEARED_STAT, 4 missing cmdline, 6 tr read errors, all ps samplers in PGID 1411, disclosed by ROOT; no principal leader or child is missing.
- All 8 authorities: schema F10-R1-REGISTERED/v1, job/instance/host equal the registration, admissibility and plan pin equal the plan SHA, python_flint equal (order-independent), univariate_acceptance null, generic_only true. file_sha256 count 112 for seven; missing-input has 111 with exactly the plan path deleted and all other 111 equal the original. Mutations exactly as coded (L119-123): disabled enabled=false; wronghost hostname NOT-THE-REGISTERED-HOST; argv parent_argv 32 entries ending EXTRA while its prelaunch parent has 31 and matches the real cmdline; cap caps.rss_bytes "1" while the launched argv keeps 2147483648; dummy child tail "descendant" and rss 33554432; generic operation build with child generic_controls.py AUTHORITY OUTPUT.
- All 8 prelaunch records: fixed_file_sha256 equals the 112 original pins for all 8 (including missing-input); authority SHA equals my recompute and the dispatch record; prelaunch SHA equals the dispatch record; checked_utc < started_utc for all 8 and equals dispatch.prelaunch_checked_utc; each operation's checked_utc is after the previous operation's ended_utc.
- Clocks: hard_cutoff 1789007160 = 02:26:00 UTC = min(math, task) for the seven non-mathematical runs; generic first_math 02:16:04.147 and hard 02:20:04.147 = first_math + 240; returned < hard for all 8 (margins 595.9-597.8 s, generic 239.0 s); admission wall+15 satisfied. Nothing renewed. Telemetry utc_start/utc_end sit inside dispatch started/ended for all 8. The recorded evidence is the caller's own prospective barrier (L128, L141, L152); ROOT's later reconciliation is read as a cross-check only, and its 8 rows agree with my extraction.

## C. Seven controls in order

Verdict: CONFIRMED.

- Order gate-disabled, gate-wronghost, gate-argv, gate-cap, gate-missing-input, gate-valid, dummy-descendant by dispatch start times 02:16:01.967, 02.255, 02.535, 02.816, 03.097, 03.378, 03.657; preflight.PASS.json holds exactly these 7 records byte-equal to the standalone dispatch records.
- Five refusals: NORMAL_EXIT, child and runner rc 1, stdout 0 B, stderr 372/366/420/412/426 B whose sha and size equal the telemetry block, each a RuntimeError from execution_gate.py lines 20/30/43/57/67 with the exact REFUSALS string (no active registered authority; not the registered AWS host; full parent argv differs from registered capped runner; registration is not the exact required CAPRUN argv; checker input artifact must be explicitly hash-registered). No gate-disabled/wronghost/argv/cap/missing-input sentinel exists in the 100 owned files. No unrelated error anywhere; all caller.stderr are empty.
- Valid: NORMAL_EXIT rc 0, stdout/stderr 0 B, sentinel 14 B = POSTAUTHORIZE plus newline.
- Dummy: RESOURCE_CAP, runner rc 125, resource rss, max sampled group RSS 80064512 > 33554432, wall 0.394 s; identity_checks exactly before-term MATCH, SENT 15, before-kill MATCH, SENT 9, with observed pid = pgid = 1588 and start ticks 14776 on both MATCH rows; term_sent, kill_sent, cleanup_complete, leader_reaped all true; group_zombies_before_reap [1588]. stdout has 2 lines, leader 1588, descendant 1603, pgid 1588, same namespace; the same-launch capture shows 1603 with ppid 1 and pgid 1588 at 02:16:03.773, i.e. the leader had already exited 0 and the SIGTERM-ignoring descendant carried the RSS. child_exit_code 0 is consistent with that; no leader SIGKILL is asserted.
- Normal-exit telemetry (6 runs) has leader_reaped false and cleanup_complete null; those are honestly unset fields, not cleanup evidence. Independent quiet evidence: dispatch remaining_group_live [] after the caller's own /proc scan (L151), and ALL_ORIGINAL_PIDS_GROUPS_CGROUP_ABSENT at 02:16:49.548.

## D. Generic build authority output, sidecars, receipt/batch binding

Verdict: CONFIRMED; 17zk GAP-D1 observed resolved.

- Exactly one mathematical run: generic authority 3b9d0cf7 (operation build, AUTHORITY OUTPUT argv), prelaunch 02:16:04.176573, dispatch 02:16:04.205683, CAPRUN interval 02:16:04.251301-02:16:05.121259, wall 0.86996585 s, max sampled group RSS 50745344 B, NORMAL_EXIT 0, no cap fired, stderr 0 B, stdout 593 B with 8 POSITIVE VERIFIED lines, 4 NEGATIVE EXPECTED REFUSAL lines and the status line. These are synthetic-batch timings only.
- Receipt 10b40aaf, 6482 B: exactly the 9 keys; schema F10-GENERIC-CONTROLS/v1; status ALL-12-GENERIC-CONTROLS-VERIFIED-NO-SOURCE-ACCEPTANCE; scope synthetic rank-seven fixtures only; execution = {job, hostname, instance, authority 3b9d0cf7} equal to registration and the local authority hash; engine = {module_file, module_sha256, version 0.9.0} equal to registration python_flint key by key (this is the 17zk GAP-D1 equality, observed to hold with no code edit); harness c369dc11 and solver 58cdc472 equal the known pins.
- Positives 8 in plan order: allzero-q0 UNIT, allzero-q1 SEPARATOR, constant-degree25 UNIT, raw-two-T UNIT, nonreduced-remainder UNIT, lost-component SEPARATOR, varying-pivot UNIT, all-generators UNIT, all VERIFIED-SYNTHETIC-ONLY; UNIT check = {217 coordinates, 9 multipliers, degree bound 25}, SEPARATOR check = {1638 columns, 217 targets}, all integers. Negatives 4 in plan order, EXPECTED-REFUSAL, ValueError, reasons byte-equal to the plan.
- 20 sidecars hash-only: every embedded path equals the remote path and every embedded SHA equals my local hash (20/20); observed sizes 908, 16899, 913, 2694, 1275, 16895, 1051, 16896, 1134, 16899, 1040, 2739, 1233, 16977, 1057, 16897, 3573, 17919, 3563, 983 B, all equal the terminal SIZE lines and the batch artifacts list (20/20 hash and bytes). No sidecar was parsed.
- batch.PASS.json 29c34969: status QUOTIENT-GENERIC-ENGINEERING-PASS-NOT-ACTUAL-SOURCE, receipt sha/bytes equal local, plan pin ce193898, 8 records byte-equal to the 8 standalone dispatch records, first_math equal to the generic dispatch, end 02:16:05.202 before the stored generic cutoff 02:20:04.147.
- Accepted as harness execution evidence only: no actual-source speedup, decision, point, or JC2 claim; no theorem about untested inputs.

## E. Terminal state, AWS stop, scope of what this gate licenses

Verdict: CONFIRMED, sharing documentary GAP-A1 for the backup-cancel stamp.

- Terminal unit at 02:16:49.548: MainPID=0, Result=success, ExecMainStatus=0, ExecMainStart/Exit blank, MemoryPeak and CPUUsageNSec [not set]. No outer accounting number is fabricated anywhere in the packet; the CAPRUN numbers in C/D are the only measurements.
- ALL_ORIGINAL_PIDS_GROUPS_CGROUP_ABSENT precedes the 02:16:49.571 rehash: 112 fixed pins unchanged, 100 owned files hashed and sized, all equal the pulled copies and my local inputs (Section A). Payload/receipt reading therefore came after custody freeze.
- Stop: RUNNING->STOPPING at 02:16:51.600; three instances STOPPED at 02:18:25.910 with volumes retained (worker-stop.txt raw). The backup cancel is stated there as after positive STOPPED, but its 02:21:28.400 return exists only in the root narrative (GAP-A1).
- Scope licensed: the R3 packet is qualified generic runtime evidence for the accepted 17zh/17zk code under this exact registration. It licenses considering a separately registered actual-source run next. It is not a runtime authority, source acceptance, or a migration licence for a different actual caller.

## F. Smallest defect, verdict

A CONFIRMED (GAP-A1 documentary), B CONFIRMED, C CONFIRMED, D CONFIRMED, E CONFIRMED (GAP-A1 shared). No REFUTED item.

Smallest actual defect: two AWS-console stamps cited by ROOT (pre-start STOPPED->PENDING 02:13:32.175 and backup-cancel inactive 02:21:28.400) have no charged raw artifact; the raw files prove only timer-active 02:13:30.104 < SSH preflight 02:15:17.089 < launch 02:16:01.754 and stop 02:16:51.600 < STOPPED 02:18:25.910. Repair, for ROOT if desired: charge the two describe/cancel outputs. Nothing in the runtime, custody or receipt chain depends on them.

Own artifacts: box/sha-recheck.txt (113 rows), sizes.txt, node-metadata-extract.{js,out}, node-sidecar-bind.{js,out}, node-recheck.{js,out}. These are documentary extraction scripts over metadata JSON only; no helper for any producer, no test, no repair.

OPEN(S) RAISED: none. New OPEN count = 0; GAP-A1 is a documentary custody gap, not a bounded research quantity. Own-only collision check: both own targets were absent at 02:24:36 before creation, and nothing outside them was written. No Seal, no exit-price declaration line and no closing hash section is authored; ROOT owns independent intake.

<!-- BODY-END -->
