# f10-r2 disabled two-refusal map-observer instrument gate (Fable 5.1, 2026-09-10)

FIRST different-model SOURCE/INSTRUMENT delta gate. Reviewer Fable 5.1; author Astra (completed 14:38:59 UTC); executor ROOT.
Lane first action 2026-09-10 14:46:38 UTC; deadline min(ROOT launch+18 min, 15:06:00 UTC); final 3 min reserve, never reset.
Status: UNSEALED (no Seal section by instruction); sections A-F complete. Method: sha256sum, whole text reads, manual reasoning only. No subprocess/import/AST/compile/test/CAS/network/git/process/agents.

## Custody (11 frozen inputs, sha256 from sha256sum at 14:46:38 UTC)

| sha256 | basename |
|---|---|
| b4cea19b474a3238caf0871369baa5fc8497e1d1ac5cc6e107815372297640e2 | dispatch.py |
| d80b72eaf86f9f2ad8b0716a89337d86aad4243b6ebbdbcd20b679128f6bdbbb | dispatch.diff |
| 1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde | probe.py |
| f62f7480201d89cf7a6bcd6419a8d239f661f3dc8fd30be3000248d7c86a5496 | CONTRACT.md |
| 9116e41d1664ba28917e8e3e4110dd23c7ec037a727aba870fda7d4d7fc569b7 | DISABLED-REGISTRATION.json |
| 2bcceb23b3fe9c71f409578b99af8c51446bce2232e47b6167cd1bf0543010c0 | READ-SCOPE.md |
| 255a5805733716b188744ad08f109f154653045a642b635fc1c5bc3fb1ac0519 | f10-r2-map-observer-code-astra-20260910.md |
| 469fd1c701a2af3149ff7401c7592a4fb313ad7ee64b922105d86c27700eb09b | f10-r2-semantic-code-gate-fable5-20260910.md |
| 7577c1d50b5350044f2d2e844980655effea7b49f21b05059e883682012d9be4 | f10-r2-native-map-diagnosis-astra-20260910.md |
| 2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b | authority.py |
| 4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2 | run_capped.py |

All 11 match the charged pins; distinct basenames. Both owned targets verified ABSENT at 14:46:38 UTC before this skeleton.

## Prior involvement disclosure

The charged semantic code gate (469fd1c7) is Fable 5.1 authored, same model as this reviewer; it is imported only at its STATIC source/instrument scope and observed no native closure pass. The old 673-line source 6c232bb0 is not charged (basename collision) and was not opened; the complete literal diff is charged instead and was read whole. authority.py and probe.py are same-byte reuse of the accepted sources. The diagnosis and author report are Astra authored.

<!-- SECTIONS-BEGIN -->

## Read scope

Whole reads 14:46-14:48 UTC: CONTRACT.md (37 lines), READ-SCOPE.md (15), DISABLED-REGISTRATION.json (31), author report (42), diagnosis (54), probe.py (68), authority.py (77), dispatch.py (515, one read ending at line 515), semantic gate (107), dispatch.diff (567, 21 hunks), run_capped.py (1198). Every read ended at the file's last line; no clipping. Nothing executed, imported, compiled, parsed by tool or patched; the diff was compared against dispatch.py by eye, hunk by hunk (added lines at diff 150-186 = dispatch.py 280-316, 198-213 = 324-333, 230-267 = 345-361, 304-341 = 387-411, 362-363 = 439-440, 468-546 = 447-465, 555 = 485, 564 = 511). Line numbers below are the charged files' own.

## A. Two labels, authorize only, literal vectors, unchanged authority — CONFIRMED

LABELS is exactly ('refuse-status', 'refuse-caps') (dispatch.py:34); execute iterates the ordered pair at 448-451; run requires `label in LABELS and label not in self.used_labels` (346) and the completed tuple must equal LABELS (455); the registration must carry exactly these two command keys (223). The child script is built with the literal `'--mode', 'authorize'` (357-358); nothing reads a mode from the registration, so probe.py's dummy branch (probe.py:42-64, reachable only via mode 'dummy' at 23) cannot be selected. The full CAPRUN vector (363-367) must equal the registered list by plain equality (368-370); the token block of the semantic dispatcher (diff 275-288) is deleted, so no placeholder expansion exists. Vector literals match CONTRACT.md:11: wall 5, cpu 3, rss 2147483648, sample 0.05, grace 1 (PROFILES at 33, 350, 363-366), science cwd (367), setpriv `--reuid/--regid/--clear-groups/--no-new-privs --` (360-361), child `-E -s -S -B` probe (359) with the 8-element tail (355-356); outer argv `-I -S -B dispatcher --registration ROOTFILE` (182-183).

Authority: probe.py:20 accepts exactly 14 argv, 25 requires the exact five-name science listing, 28 imports only `authority`; authority.py refuses DISABLED at 51-52 and the 499 cpu cap at 55-56, both before any source read (57-65) or interpreter hash (71-73), and authority.py contains no import of arithmetic, produce or check anywhere. The two mutations are exactly 339-340. SystemExit with a string yields exit 1 and the newline-terminated line, matching 444 and 454. Fixed outer job/schema: CONTROL_JOB (23), schema and `enabled is True` (157), jobtag (158); the disabled template has enabled false and null commands, so it dies at 157. SCIENCE (25-30) and CAPRUN_SHA (24) are outside every diff hunk except as context (diff 18-22); CAPRUN_SHA equals the charged run_capped.py digest and SCIENCE['authority.py'] equals the charged authority.py digest. Wrapper is exactly two files (250) and the probe must be a wrapper sibling (180-181).

## B. Ordered rejection and first-failure record before raise — CONFIRMED

check_maps (280-316) keeps the original order: resolved-file membership first, then alias membership, with the original two reason strings (291; old diff 147-149). It breaks on the first failure (295) and records raw_path, resolved_path, file_member, alias_required, alias_member (292-294). The record (302-309) has exactly the fourteen keys CONTRACT.md:23 lists; snapshot is the whole identity item, which carries pid, pgid, state, start_ticks, boot_id, pid_namespace, argv, uid/gid, caps, limits, cgroup, mapped_files and the two observation times (136-145; timestamps added at 125 and 144-145). Missing identity gives reason 'live identity unavailable' (283), null snapshot and null first_rejected (308), and still STOPs (316). The write precedes the raise (314-316); the path is fixed and exclusive (emit opens O_EXCL, 99), fsynced with its directory (101, 315). Non-atomicity is disclosed in code (281, 309) and in CONTRACT.md:23. No native files or aliases are added anywhere, no mapping is skipped, the poll sleep is the unchanged 0.05 s (414, diff context 344), and no import was added (6-20 unchanged). No culprit pathname appears in code, contract, diagnosis or author report.

Transparent limitation, not a defect: identity raises on a ' (deleted)' mapping (134) and catches only FileNotFoundError (146), and resolve at 286 or the write itself can raise; each of those STOPs without a record, exactly as CONTRACT.md:25 says. The observed original failure class was the membership reason at old line 299 (diagnosis:13), which the new record path covers.

## C. Caps, custody ordering, tightened handler, completion requirements — CONFIRMED

Record cap 65536 with a typed reason (311) and again inside emit (98); metadata reserve checked with the record's bytes added before creation (312, 325-333, META at 36); tmpfs capacity at most TOTAL (276). size_budget no longer has packet paths (diff 194-214 versus 324-333), so every mount file is metadata under 1 MiB; PACKET survives only as the runner RLIMIT_FSIZE (380). Any need failure or OSError propagates to main, which records STOP_NONDECISION (499-500); durable failure is STOP_CUSTODY_INCOMPLETE (505-508); exit 0 requires the literal success status (511), set only at 457 after every check. The `self.revalidate(); self.group_quiet()` tail is removed from __init__ (diff 105) and placed at the head of execute (447), which runs only after main has bound batch (497-498) and before the label loop (450), so an initial self-map rejection now reaches durable_copy (503-504). check_maps is never called from __init__ (only 278, 389, 409). The FileNotFoundError handler wraps only the children read (395-398); the per-child loop, check_maps and emit sit outside it (401-411), unlike the old form (diff 314-327). Completion requires runner argv equality (439) and a captured probe identity (440), both after the post record (438); a fast refusal can therefore STOP with no retry (346).

End of sections A-C.

## D. Preserved guards, no circularity, caps and cleanup — CONFIRMED

All of the following are diff context or outside every hunk: ROOT uid and Linux (153), registration immutable and 0444 (154-155), environment equality (160), science uid/gid (161), EC2 vendor and instance tag (162-164), host, boot, PID namespace (165-167), owned cgroup and memory.max (168-171), five roles and interpreter identity (173-176), wrapper cwd and siblings (177-181), live outer argv (182-183), role and science pins (184-189), native manifest pin, six fields, sys.path closure and bounds (190-196), output children, writer ownership, fresh and empty children, exact tmpfs (197-205), code, native and registration outside tmpfs (207-211), outer fd binding (212-216), absent ext4/xfs durable target (217-219), deadlines (220-222), root-owned traversable ancestry (76-84), and every revalidate predicate for pins, directories, aliases, absent paths, ps aliases and manifest drift (242-277). No new guard permits anything: every code deletion removes a role (mutator, baseline, fixtures, token, tracebacks), and the only behavioural changes are stricter (runner None now STOPs, 389 versus diff 306-307; label must be in LABELS, 346; packets no longer exempt from the 1 MiB reserve).

Circularity: the authority object (336-338) contains SCIENCE, LIMITS, the interpreter pin and the native manifest hash, all registration-known, and not the registration hash; the command vector (363-367) contains paths and that digest only. ROOT can compute both digests and vectors before launch, and the registration hashes nothing that contains itself. Caps: joint 600/500/2 GiB/16 MiB (31-32, 36, 171, 276), sampled 480 (239), 15 s margins (351, 377, 413), post-return 600/500 (423); per child 5 wall/3 soft CPU, CAPRUN hard = soft+1 (run_capped.py:650-657), so 10 wall and 8 hard CPU over two children. These are ceilings; CONTRACT.md:17 says so and nothing in the package claims measured runtime. CAPRUN's new session and pgid==pid invariant (run_capped.py:827, 357) are bound at 429; the leader must be reaped (431); group quiet precedes every terminal read (419); the finally sends TERM and waits 15 s (415-418); CAPRUN's own forwarded-signal path cleans its group (run_capped.py:940-1033). The external ROOT TERM/KILL remains a stated requirement (CONTRACT.md:31), not code. Distinction requested: no missing guard permits an unauthorized payload; the remaining fail-closed liveness items are the ESRCH-class identity race (146, unchanged) and the new mandatory probe capture (440), both of which STOP.

## E. Durable custody of the failure record — CONFIRMED with disclosed limits

durable_copy (467-490) runs only after group quiet (468), walks the whole mount, so the fixed map-rejection.UNVALIDATED.json is included automatically, copies each file with exclusive create, fsync, 0444 and a byte-identity hash (479-482), records the inventory (483), writes CUSTODY.json (485-486) and fsyncs every directory (487-489). main calls it whenever batch was bound (501-504), including after a STOP from execute. If __init__ itself fails, batch is None and no custody is attempted (501-502); since check_maps cannot run inside __init__, no map record can be stranded there, but pre-custody failures still require ROOT external capture, and custody, deadline (469, 474, 490), 200-file (484) or live-group (468) failures yield the explicit STOP_CUSTODY_INCOMPLETE (505-508), never a silent accept. Non-atomicity is stated (281, 309, CONTRACT.md:23) and the package claims no total native closure from static pins (CONTRACT.md:33, author report:25). One non-blocking note: if the post-rejection `p.wait(timeout=15)` at 418 expires, the TimeoutExpired replaces the map reason in the result string, although the record file still exists and is still copied.

## F. Outcome grammar and next registration — CONFIRMED

Only NORMAL_EXIT, resource null, child_returncode 1 (452, 444), absent payload, empty stdout and the exact stderr line (453-454), both labels in order (455), empty writer and frozen (456), and both identities per label (439-440) reach DIAGNOSTIC_NO_MAP_FAILURE_OBSERVED with science_outcome NONE (457-464); exit 0 only for that status (511). The result carries no_repair_or_retry_permission true (460). Nothing in these sources states runtime, mathematics, source promotion or JC2. CAPRUN's own status line goes to the runner stream (run_capped.py:1172-1176, dispatch.py:383), not to the child stdout that 453 requires empty. The probe payload is opened only after authorize returns (probe.py:30-34), so refusal leaves none.

One separately ROOT-registered two-refusal observation is reasonable after this gate. Exact remaining registration duties: (1) a new 0444 root-owned registration with schema f10-r2-map-observer-runtime/v1, enabled true, jobtag f10-r2-native-map-observer-v1, exclusivity, the literal limits, profiles and environment, actual instance, host, boot, PID namespace, cgroup path with memory.max 2147483648, science uid/gid, the five role paths, science and wrapper directories, pins for the five roles, five science files and native manifest, the six-field native manifest whose python_path equals the -I -S sys.path, a fresh 16 MiB tmpfs with empty authority/frozen children and a science-owned 0700 writer, an absent ext4/xfs durable path with its device number, the literal outer argv, both UTC deadlines, and exactly two command vectors reproducing 363-367 byte for byte with the precomputed authority digests; (2) dispatch.py b4cea19b and probe.py 1e3bea3a installed root 0444 as the only two wrapper files; (3) outer stdout/stderr bound to outer.stdout/outer.stderr on the mount, cwd the wrapper directory, environment exactly ENV; (4) external TERM/KILL timers; (5) reads only after the writer and cgroup are terminal. Expected non-discriminating STOP to plan for, not to retry: 'probe live identity unobserved' at 440 if the 50 ms poll misses the fast refusal; that outcome can only motivate a changed, re-reviewed instrument. A failed observation guides a changed instrument or registration only; no unchanged semantic retry is authorized by this gate.

## Verdict table

| item | verdict |
|---|---|
| A two ordered labels, no repeat, authorize only, literal vectors, no token, unchanged five science and CAPRUN literals, two-file wrapper | CONFIRMED |
| B ordered file-then-alias rejection, fourteen-key UNVALIDATED record before raise, null-snapshot STOP, no resampling or allowlist change | CONFIRMED |
| C 65536 cap, 1 MiB reserve, exclusive fsynced path, revalidation moved to execute, narrowed handler, runner and probe identities mandatory | CONFIRMED |
| D preserved guards, no self-hash circularity, 600/500/2 GiB/16 MiB and 10/8 child ceilings, cleanup retained | CONFIRMED |
| E automatic durable inclusion, STOP_CUSTODY_INCOMPLETE, pre-init failures need ROOT capture | CONFIRMED with disclosed limits |
| F only the literal diagnostic status, one registered observation reasonable | CONFIRMED |

Smallest blocking correction: none found. Non-blocking: the wait-timeout reason substitution at 418; alias_member is False by construction for non-alias paths in the record (289) and should be read together with alias_required.

End of sections D-F.

## OPEN(S) RAISED

None. No new canonical OPEN; the remaining quantities are the separately ROOT-registered observation listed in F and the unobserved original pathname, neither authorized or resolved here.

## COLLISIONS

status: EMPTY

- NONE — own-only check: this lane wrote exactly xmodel/f10-r2-map-observer-gate-fable5-20260910.md and box/f10-r2-map-observer-gate-fable5-20260910/custody.sha256, both absent at 14:46:38 UTC; no corpus scan; no other file touched.

## WHOLE check and attestation

All 11 inputs were read whole as itemised in Read scope; the eleven digests equal the box custody file, which was generated from sha256sum output. This report was re-read by tail and heading inventory before the marker; section order is Custody, Prior involvement, Read scope, A-F, Verdict table, OPEN(S), COLLISIONS, this section. Disclosure: the imported semantic gate is same-model (Fable 5.1) and was consumed only at its static scope; it observed no native closure pass. Authoring: every byte of both owned files was written by apply_patch (custody rows piped from sha256sum into apply_patch's stdin); no Write/Edit tool, no shell redirection into any file, no helper, no source or input edit, no Seal, no charge_basis, no execution, import, AST, syntax, compile, test, CAS, network, AWS, SSH, Git, agents, corpus, shared, protected, other-lane or live file, no patch replay by tool. Timeline: hashes and absence 14:46:38 UTC, skeleton 14:47, whole reads 14:46-14:48, sections A-C 14:52, D-F and this section before the 15:03:00 reserve, deadline 15:06:00 UTC, never reset. The standalone marker below is the only such line in this file and nothing follows it.

<!-- BODY-END -->
