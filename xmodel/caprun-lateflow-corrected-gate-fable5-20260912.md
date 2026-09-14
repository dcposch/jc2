# caprun-lateflow-corrected-gate-fable5-20260912

reviewer: Fable5.1 (claude-fable-5-1), independent hostile reviewer of Astra
tag: caprun-lateflow-corrected-gate-fable5-20260912
started_utc: 2026-09-12T05:46:03Z
reserve_utc: 2026-09-12T06:07:00Z  hard_utc: 2026-09-12T06:10:00Z (never extended)
mode: source-static FIRST review; MANUAL/model-side reasoning only; no execution of any input.
authorizes: NOTHING (no allocation/SSH/admission/install/FIFO release/observation/source run/FULL13/cap/retry/rank client).

## 0. Input custody (26 immutable snapshots, pre-read hashes)
(pending)

## A. Composer / manifests / freeze order
(pending)

## B. ROOT entries / phase ordering / tool-handle contracts
(pending)

## C. Record / private parent / absence / readback / freeze
(pending)

## D. Admission / observation / decision identity; metadata plumbing
(pending)

## E. Candidate / INSTALL / RELEASE chain
(pending)

## F. Fresh release guards; SOURCE vs future ROOT binding
(pending)

## G. Collection-only interruption semantics
(pending)

## H. Ten manual negative controls + two historical defects
(pending)

## 9. Disposition and remaining GAPs
(pending)

## 10. Unreviewed roles (if capped)
(pending)

<!-- write 1 of 3, 05:5x UTC -->
### 0. Input custody (filled)
All 26 snapshots in /tmp/jc2-lane.OH1Gp0/inputs hashed BEFORE reading; every digest equals the expected list in the charge (sha256sum -c: 26 OK, 0 FAILED). Whole reads of all 26 followed. Every source treated as inert text; nothing executed, parsed by a tool, imported or compiled. ROOT-INTAKE.md is consumed only as the eight-defect target list. Postpins are emitted to stdout at the end, not into this file.

### A. Composer / manifests / freeze order (filled)
- CONFIRMED (defect 1 corrected). compose-preholder.template.sh:4 rejects any `JC2_[A-Z0-9_]+_PLACEHOLDER` in its own text; the only such token left is line 10 (`JC2_REVIEWED_TAIL_SHA256_PLACEHOLDER`), which ROOT must bind to the reviewed tail digest. Selection now uses `@@ENTRY@@` (line 20 sed, line 22 residue grep), which the guard does not match. FLOW.tail.template.js contains no `JC2_*_PLACEHOLDER` token (its line 105 regex `/PLACEHOLDER|UNBOUND/` is a config check, not a token). Old trace: Sol's line 21/24 carried `JC2_ENTRY_SELECTOR_PLACEHOLDER`, so a fully bound composer still exited 2 at line 4. New trace: bound line 10 → guard passes → line 15-16 absence of four targets → line 20 `set -o noclobber` + sed concatenation kernel+tail → line 21 exactly one `const JC2_ENTRY = ` → line 22 no residue → 0444. An unbound line 10 still exits 2; an existing target fails `test ! -e` at line 15 before any composition.
- CONFIRMED kernel+tail composition. Kernel ends in a newline byte (documentary od check), so concatenation cannot glue its last comment to tail line 1. The tail references kernel symbols jc2Stop, jc2Quote, jc2Hex, jc2Path, jc2Admin, jc2HashReadback, jc2SSH, jc2ExactProperties, jc2HolderData; all are defined in ORCHESTRATION-KERNEL.js:4-153. jc2Names and jc2ChecksumText are unused by the tail (harmless).
- CONFIRMED role census. Tail 109-115 requires exactly 14 local roles: 4 entries derived from the JC2_CONFIG directory, the config, cfg.local.caller, the literal latebind/stage_patch paths (110-111), prepared pins, the local copy of the remote manifest, and four prepared files; `same(cfg.local.fixed_paths, requiredLocal)`. LOCAL-PREHOLDER-MANIFEST.template.sha256 has 14 rows whose path placeholders map one-to-one onto config fixed_paths (14 entries). Remote: 8 roles (113) = REMOTE manifest 8 rows = config remote.fixed_paths (8). fixedChecks 55-62 hashes local rows locally, remote rows over pinned SSH, then runs `sha256sum --strict -c` on the remote installed manifest and native list. Defect 2 corrected.
- CONFIRMED integration constants agree: caller.py:12-13 resolves latebind/stage_patch to `/home/ubuntu/jc2/box/caprun-latebinder-code-astra-20260911/latebind.py` and `/home/ubuntu/jc2/box/caprun-candidate-stage-root-20260911/stage_patch.py` (HERE.parent = /home/ubuntu/jc2/box), identical to tail 110-111; caller DEPENDENCY_SHA256 equals the charged digests of latebind.py (ff2beb…) and stage_patch.py (f7c61d…).
- CONFIRMED no hash cycle. FROZEN-CONFIG stores manifest paths (55-56), never its own digest; the tail embeds only the config path (line 4); the local manifest lists config+entries; nothing lists the local manifest. Freeze order that works: freeze tail → bind composer line 10 → compose entries → bind/freeze config → write local manifest → ROOT pins it externally.
- GAP-A1 (binding, by design). No code path verifies the local manifest's own digest; the only in-code authentication of the local manifest is the census of the paths it lists. The "independent ROOT pin" is therefore an external procedure with no field in the packet (adding one would create the cycle). ROOT must record and re-check that digest outside the tail before every entry.
- GAP-A2. The composer is not one of the 14 roles; its bound line-10 value is not otherwise recorded. Acceptable because it never runs at runtime, but the reviewed-tail digest must be logged by ROOT.
- Answer to "can the stated preholder binding produce a coherent packet without altering algorithms": YES statically; every placeholder is a constant, and the four algorithms (kernel/caller/binder/stage) are consumed unmodified at frozen paths and digests.

### B. Four ROOT entries / ordering / tool-handle contracts (filled)
- CONFIRMED four separately selected entries: tail 229 rejects any selector outside ADMIT/ATTEST/INSTALL/RELEASE; loadConfig 105 requires `entry_authorities[JC2_ENTRY] === "ROOT_EXPLICIT_SEPARATE_"+JC2_ENTRY`, armed true, review_state DIFFERENT_MODEL_REVIEWED_BOUND, no PLACEHOLDER/UNBOUND in raw. Template values (armed false, UNREVIEWED_UNBOUND, exclusive_no_concurrent_writer false, clocks 0) all stop at 105-107 or in beforeStops 71. This gate does not and cannot set review_state.
- CONFIRMED ordering. ADMIT alone checks all five records absent (117-118); ATTEST needs the admission record (loadAdmission 123 → sed of a missing file exits 2 → kernel 63 stop); INSTALL needs admission+observation+decision (164-166); RELEASE needs all five (204-210). Double replay guard: phaseKey per entry (230-238) and, independently, record absence in addRecord 34 and the mutating observe script (test ! -e leaf, observe 57).
- CONFIRMED admission DATA extraction. outer-admission 77 prints `MainPID=`/`InvocationID=` exactly once, 79 prints the /proc stat row, 92 prints ADMITTED_NOT_RELEASED; jc2HolderData 140-151 takes field 22 via `tail[19]` after the last ") ", and observe/release/installer take the same field via `sed 's/^.*) //' | awk '{print $20}'`. ps (78) and cgroup.procs (83) rows cannot match `pid + " ("`.
- CONFIRMED tool result handling against the stated contract: kernel 58 stores session_id when present; 60 treats an integer exit_code as sole terminal authority; 67-70 stops on neither. Non-zero exit stops (63); completion after the absolute stop stops (64). No model or tool was executed here.
- GAP-B1 (tool-name binding). The stated contract says "wait resumes same handle"; the frozen kernel's only resume/wait primitive is `tools.write_stdin({session_id, chars:"", ...})` (77). If the host exposes `wait` and not `write_stdin`, every long-running admin call and the whole collection path (tail 235) throws at the first poll. ROOT must confirm write_stdin-with-empty-chars is the supported wait.
- GAP-B2 (byte-faithful output). oneHash 65 anchors on a single trailing `\n`; jc2HashReadback 86 and checksumMap 45 require `endsWith("\n")`; addRecord 39 requires readback === JSON+"\n". If exec_command output is trimmed, re-wrapped or annotated, every phase stops (fail-safe, but the flow cannot complete).
- GAP-B3 (execution model). load/store/notify/text/tools are undeclared host globals, and the tail uses top-level await (235, 240-244). The host must run each `*.functions.exec.js` as a module or async body with persistent store. This is a premise of the charge, not a defect, but it is unverified by any input.

### C. Record / private parent / absence / readback / freeze (filled)
- CONFIRMED (defect 3 corrected). addRecord 30-43: target must be one of the five configured records and a direct child of records_directory (32-33); privateParent 17-23 runs `readlink -e "$1" = "$1"`, `! -L`, `stat %d:%i:%u:%g:%a = identity` (regex forces mode 700), then `! -e`/`! -L` per target; phase state set to publication (35) BEFORE apply_patch; isError stops; readback must equal `JSON.stringify(value,null,2)+"\n"` (39); freeze chmod 0444 + sync of file and parent (40); parent identity re-checked (41). Candidate: mktemp 0700 identity must end in owner_uid:owner_gid:700 (173-174), all 14 paths plus `authority` checked absent (175), mkdir 0700 authority (176), patch, parent re-check, chmod 0444 of all 14, sync, sha256 readback against packet.expected_sha256 (179-181).
- CONFIRMED all 14 candidate paths: tail candidateNames (7) = stage_patch NAMES (8-10) = 9 authority JSON + registration, card, FINAL-INSTALL-INPUTS.sha256, final-install.sh, SUMMARY.json; census enforced at 172 and again at RELEASE 215. Nine authority files are produced only locally and never transferred (182); remote authority/frozen/writer dirs checked empty by observe 53 and release-check 55.
- CONFIRMED premise statement: comment at 42 and CONTRACT line 8 state apply_patch is not O_EXCL; the 0444 records live in a coordinator-owned 0700 directory, so the owner can still replace them. Cooperative exclusive writer is explicit, not claimed as hostile-root safety.
- GAP-C1 (nit). Emptiness checks of the form `test -z "$(find DIR ... -print -quit)"` (observe 53, release-check 55) pass vacuously if DIR is absent, because the substitution's exit status is not tested. Harmless for "no preinstalled authority", but ROOT should ensure the three directories exist so the check is not vacuous.

<!-- write 2 of 3 -->
### D. Admission / observation / decision identity; metadata plumbing (filled)
- CONFIRMED (defect 4 corrected). validateObservation(cfg,o,d) line 96 requires `String(o.holder_pid)===d.holder_pid`, `String(o.start_ticks)===d.start_ticks`, `o.invocation_id===d.invocation_id`; it is called with d in ATTEST 152, INSTALL 165 and RELEASE 205. loadAdmission 126-127 re-parses the stored raw and requires equality with the stored numeric fields, so a record whose fields were edited but whose raw was not (or vice versa) stops. RELEASE 212 additionally requires commit.holder and receipt.holder to JSON-equal d.
- CONFIRMED argv positions. ATTEST passes `[observe, pid, start, inv]` (151); observe requires `$#`=3 and the three regexes (5-8). RELEASE passes `[release_check, phrase, pid, start, inv, regsha]` (226); release-check requires `$#`=5 with $1 phrase, $2..$5 typed (5-9). Observe emits leaves in `$jc2_names` order (14), which equals tail `phases` (6) and binder PHASES; tail 99 enforces `x.name===phases[i]` and unique device:inode across outer+9 leaves; binder 271-280 repeats it.
- CONFIRMED caller/binder/stage plumbing. Tail 169 invokes caller with exactly the six positional arguments packet() expects (57): prepared_directory, prepared_pins, observation, decision, made, context. Binder keys(observation) 252-254 = tail exactObject list 92 (16 keys). decision.observation_sha256 is the sha of the observation FILE bytes (ATTEST 154, sha256sum) and the caller hands the same file bytes to binder 261. Binder converts the observed ints with str() into argv positions checked for multiplicity 1 (304-308) and into installer/card tokens with exact counts (336-360). final-install.template.sh multiplicities match the binder table: CAPTURED_HOLDER_PID 1 (line 14), START_TICKS 1 (15), INVOCATION_ID 1 (16), FINAL_REGISTRATION_SHA 2 (22, 75), FINAL_INSTALL_RELEASE 1 (5), FINAL_CARD_SHA 1 (23), FINAL_INSTALL_MANIFEST_SHA 1 (20).
- CONFIRMED the frozen installer is a REFERENCE only: it still carries INSTANCE ×2 (7, 44), BOOT ×2 (8, 45), HOLDER_CUTOFF ×3 (9, 69, 79), literal 20260911d base/stage/unit (10-12) and holder argv (33). Binder replace_exact 110 refuses any leftover placeholder, so the frozen file as-is cannot be bound; the CONTRACT (line 17) correctly requires a constants-only copy with those substituted. Binder 333-335 checks `jc2_base=`, instance and boot lines of that copy.
- CONFIRMED holder constants inventory: holder.preallocation.py hard-codes ENABLED, RELEASE, TOKEN, INSTANCE, BOOT, PIDNS, CUTOFF, ADMISSION (11-18, both dated 2026-09-11), BASE, CHANNEL, OUTER_CGROUP (19-22); FIFO/OUTER derive from them. CONTRACT line 17 lists exactly these. The holder's 120 s window is start-relative (82) and matches the observe/release `< 120` tick checks (observe 64, release-check 44).
- GAP-D1 (binder coverage). Binder verifies only `jc2_base=` in the installer copy; `jc2_stage`, `jc2_unit`, `jc2_cgroup` and the holder argv literal (installer 11-13, 33) are not compared with cfg.remote.stage/unit/cgroup/holder anywhere in code. Consistency is ROOT's binding duty; a mismatch would surface only as an installer stop at 29-33 or a release-check stop.
- GAP-D2 (deadline literals). Independent deadline constants with no code cross-check: config clocks (3, ms), observe/release-check/fifo `EARLIEST_ORIGINAL_STOP_EPOCH`, receiver `ORIGINAL_ADMISSION_STOP_EPOCH`, admission `ADMIT_CUTOFF`, `TERM_DEADLINE`, `KILL_DEADLINE`, installer `HOLDER_CUTOFF` ×3, holder CUTOFF and ADMISSION. ROOT must derive all of them from one original clock and record the derivation; nothing in the packet does.

### E. Candidate / INSTALL / RELEASE chain (filled)
- CONFIRMED (defect 5 corrected). INSTALL writes the commitment (185) with expected (14 local digests from the caller packet, verified by readback 181), staged (4 transfer names under cfg.remote.stage plus native.sha256 = cfg.coordinator.native_list_sha256, 183) and installed (registration and card under base/metadata, 184) BEFORE the receiver preflight and streams (187-193). Commitment digest taken at 186; receipt written after the installed readback (197-198) carrying commitment_sha256 and holder.
- CONFIRMED RELEASE consumes the commitment, not the target: 207-221 read commitment and receipt, re-hash the commitment file and require receipt.commitment_sha256 equality, check the three censuses, require staged/installed digests to equal expected candidate digests and the native digest to equal config; 222 re-hashes the 14 local candidate files; 224 re-hashes staged+installed on the worker via SSH; 225 takes regsha from commit.installed; 226 passes it to release-check, which compares both the installed and the staged registration to it (45, 50) and cmp's them (51-52). No current-SHA-as-expected path remains (Sol's 199-201 removed per diff).
- CONFIRMED transfer: pipefail (191), dd | ssh sudo receiver NAME; receiver allowlists the five names (21), refuses existing targets (25-26), and creates with `conv=excl,fsync oflag=nofollow` (32). Preflight checks all five absent (16-19). Missing source ⇒ dd fails ⇒ pipefail non-zero ⇒ kernel stop; a retry re-uses a used key and stops (tail 13). Remote readback (194) is against the commitment's staged map.
- CONFIRMED no preinstalled authority: transfer list (182,188) is exactly registration, card, FINAL-INSTALL-INPUTS.sha256, final-install.sh, native.sha256; FINAL-INSTALL-INPUTS rows (binder 351-354) are relative names verified after `cd stage` (installer 19-21, release-check 47-49).
- GAP-E1. The remote native list (cfg.remote.native_list, closure-checked by fixedChecks) and the coordinator native list (streamed as native.sha256) are never asserted equal. Both are individually verified; ROOT must state whether they are the same inventory.
- GAP-E2 (binding). Remote scripts are invoked directly (`sudo -n -- /path`), so admission, observe, receiver, release-check and fifo-writer need execute permission and root-owned immutable placement; final-install is invoked via `/bin/bash` (196). Not code-checked beyond the remote manifest digests.

### F. Fresh release guards; SOURCE versus future ROOT binding (filled)
- CONFIRMED (defect 6 corrected). release-check now checks, in order: original stop −5 s (11), EC2 vendor/instance/hostname/boot (12-14), unit active/MainPID/InvocationID (15-17), start ticks (18), pid namespace literal (19), pid/mnt/cgroup/user namespaces equal to PID 1 and to the holder (20-23), exact holder argv and exe (24-25), cgroup2 mount target/fstype/root (26-28), canonical outer path and 0:0:755 (29-30), cpu.max.burst 0 (31), memory.swap.max 0 (32), domain type (33), empty subtree_control (34), three root-only migration surfaces 0:0:-rw-r--r-- (35-37), membership and sole population (38-39), cpu.max 6900 10000 / memory.max 8 GiB / pids.max 32 (40), Delegate=no (41), holder age 0..119 s (42-44), registration digest and mode (45-46), stage manifests strict (48-49), staged=installed cmp (50-52), card mode (53), registered-source pins (54), empty authority/frozen/writer (55), exactly nine leaves (56), per-leaf canonical/mode/domain/subtree/no-descendant/path/iface/empty/unpopulated/device/inode (57-71), outer device/inode (72-73), FIFO type/mode (74), stop −3 s and re-authentication of MainPID/InvocationID/ticks (75-78), then exec of the fixed FIFO writer (79), which is itself 2 s-bounded (fifo-write 20-21). Observe carries the same physical set (16-54) before creating leaves. No sleep, no substring success.
- SOURCE establishes: every predicate above against literal constants. ROOT binding must establish: the constants themselves (instance/boot/pidns/cgroup/unit/stage/base/FIFO/token), the exec bits, and the retirement timer's actual deadline.
- GAP-F1 (retirement deadline not source-verified). freshCoordinator 83-88 compares `systemctl --user show` output to cfg.coordinator.timer_properties {ActiveState, LoadState, Unit} and service_properties {LoadState, Type, ExecStart}. No property names the calendar or next elapse (e.g. `NextElapseUSecRealtime`, `TimersCalendar`), so a loaded, active timer with the wrong deadline passes. jc2ExactProperties accepts any key set, so ROOT can add the exact expected deadline string to the map at binding; until then "exact timer/service authentication" is unit identity only. No new cap promise is made anywhere in the packet.

<!-- write 3 of 3 -->
### G. Collection-only interruption semantics (filled)
- CONFIRMED (defect 8 handled by narrowing). Tail 230-238 run before loadConfig and before any seedStop: prior=load(phaseKey); if present, only when prior.current names a key whose stored kernel state is non-terminal with a session_id does it call `jc2Admin(c.key, state.argv, state.absoluteStopMs, resume=true, c.limit, collectOnly=true)`; the kernel's resume guard (33-34) then compares argv and absoluteStopMs with the same stored values, polls without launching (31, 72 skipped under collectOnly), and returns COLLECTED_NO_SUCCESSOR on an integer exit_code (62). The tail then unconditionally stops (237). Every admin call records `current` before launch (14) and every publication clears it (35, 177), so an interrupted apply_patch, an unknown launch (no session_id), a completed or failed phase all reach the stop without collection. The wait is bounded by the original `timeout` wrapper (kernel 42). No downstream continuation exists in code. Full resumability is correctly NOT claimed.
- GAP-G1. Collection depends on GAP-B1 (write_stdin as wait) and on store persistence across separate ROOT invocations; both are premises.

### H. Ten manual controls + two historical defects (source traces, not executed tests)
1. Composer: bound → passes line 4; unbound line 10 → exit 2; existing target → line 15 exit. Old Sol line 21 self-refused. PASS as traced.
2. Remote path in local manifest → fixedChecks 58 census stop; also loadConfig 115. Changed worker file → remote sha256sum (60) mismatch in jc2HashReadback; runs in every entry before the remote call (ADMIT 141 precedes 142). PASS.
3. Existing record → privateParent `test ! -e` non-zero → kernel 63 stop before patch; symlinked/moved parent → readlink/stat mismatch; candidate collision → 175. Not atomic (stated). PASS.
4. Valid-but-different pid/start/inv → 96 stop in all three later entries. PASS.
5. Both staged and installed changed → RELEASE 224 mismatch against commitment; commitment changed → 212 csha ≠ receipt; consistent rewrite of commitment+receipt+records would pass, which is exactly the trusted-ROOT premise. PASS with stated limit.
6. Each listed drift hits a literal `test` in release-check before line 79. PASS.
7. outer-admission.template.sh contains no `2026-09-11` literal and no dated batch token (diff hunks confirm all seven replacements); holder/installer keep dated literals and are references. PASS.
8. Traced in G. PASS.
9. Missing input → pipefail stop; changed bytes → 194/197 readback stop; no retry (13). PASS.
10. Transfer list literal; receiver allowlist; remote dirs empty (observe 53, release-check 55, with GAP-C1 vacuity nit). PASS.
Historical defect 7 (rebinding inventory): CONFIRMED complete for holder (11 constants) and installer (7 binder tokens + INSTANCE/BOOT/CUTOFF/base/stage/unit/argv), with GAP-D1/D2 on cross-consistency. Historical defect 8 (interruption): CONFIRMED narrowed contract, see G.

### 9. Disposition
STATIC_COHERENT_UNBOUND_UNEXECUTED. No blocking source-level incoherence found: the corrected composition implements CONTRACT.md as written, subject only to (i) ROOT's future physical binding/trust and (ii) the UNMEASURED 120 s holder-window liveness. Both remain open and neither is narrowed by this review.
Liveness, static structure only (not a measurement): after the holder starts inside ADMIT, the remaining tail issues roughly the following sequential tool calls, each a separate exec with ≥1 s yield and ≈33 of them SSH sessions, across three separately human-invoked entries:

| entry | approx. tool calls | of which SSH |
|---|---|---|
| ADMIT (post-holder record) | 5 | 0 |
| ATTEST | 37 | 7 |
| INSTALL | 63 | 20 |
| RELEASE | 29 | 6 |

fixedChecks runs twice per entry (loadConfig 119 and freshCoordinator 89) and three times in INSTALL. This is the structural reason OPEN2 is serious; it is not evidence either way and authorizes nothing.
Remaining GAPs, all binding-side: A1 external manifest pin, B1 wait/write_stdin name, B2 byte-faithful output, B3 host globals/top-level await, D1 installer stage/unit/argv cross-check, D2 deadline literal derivation, E1 native-list identity, E2 exec bits, F1 retirement deadline property, C1 vacuous emptiness nit.
No allocation, SSH, admission, install, FIFO release, observation, source run, FULL13, cap change, retry or rank client is authorized by this file. review_state stays UNREVIEWED_UNBOUND until ROOT binds; this review is one input to that decision, not the decision.

### 10. Unreviewed roles
Absent from the 26 inputs and therefore unreviewed: the prepared ROOT-REGISTRATION.preholder.json, AUTHORITIES.preholder.json, ROOT-EXECUTION-CARD.preholder.md (its placeholder multiplicities for the binder's card table are unverified), the constants-only holder and installer copies, prepared-pins JSON, coordinator receipt, native list, remote installed-source manifest, the host tool runtime for `*.functions.exec.js`, and every bound FROZEN-CONFIG value.

### 11. Own readback and postpins
Whole-file readback of this report performed at 2026-09-12T05:56Z before this marker; all 26 input postpins re-hashed to stdout at 05:56:12Z and equal the expected digests (no drift). Final word count is under the 4000-word cap; three bounded appends, no rebuilds. No artifact_finalize, no charge_basis (no exit-price assertion is made), no side files. Completed inside the 06:07 reserve.

<!-- BODY-END -->
