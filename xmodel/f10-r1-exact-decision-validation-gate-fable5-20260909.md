# f10-r1 exact-decision validation gate (Fable 5.1, 2026-09-09)

tag=f10-r1-exact-decision-validation-gate-fable5-20260909
reviewer=Claude Fable 5.1 (claude-fable-5-1); ONE bounded different-model acceptance of the root's FINAL/VERIFIED runtime evidence. NOT a source-proof gate, design review, solver authorization, ideal decision, certificate or JC2 result.
launch=first command 14:56:49 UTC; deadline = earlier of 15:06:49 and 15:07:00, i.e. 15:06:49 UTC; no reset. Basis 0d39df3c9fd69c939a8420c54d03228b9077777d.

## 0. Custody, archive safety, manifest

All nine charged inputs were hashed in invitation order BEFORE reading; all nine equal the ordered list (box/input-pins.sha256 vs expected-pins.txt, 9 MATCH). Inputs 1, 2, 4, 5, 6, 7, 8, 9 read WHOLE.

Input 3 (runtime-evidence.tar, dee83032…): member list inspected first (box/tar-members.txt): 88 regular files + 1 directory (`remote/`), zero symlinks, zero absolute paths, zero `..` components. Unpacked ONLY into box/…/unpack/.

remote/TERMINAL.sha256 hashes to 3ca47331a86068f167cc73777d8fee349c99b7a5f23b4486cf980d1d60e4aefd = the root report's pin. `sha256sum -c` over its 76 entries: 76 OK, 0 FAILED (box/terminal-check.txt) BEFORE any output was consumed. The only remote file outside the manifest is TERMINAL.sha256 itself. Root's collect.stdout hashes to 239339a6… as the root report states, and its journal line shows the service completed 14:49:57 with MainPID absent (`test ! -e /proc/1312`, cgroup path absent) before the manifest was built.

exact.json: HASH ONLY = 168bdfd3a791f24a6631de66ae4e71c3f209ee9eb0d21fc466f9aa802f5ad576 (accepted 16w); never parsed. admissibility.md 02952e1b…, frontier.json f9d1fddc… hashed only.

## A. Exact correction — CONFIRMED

- remote/engine.py = 81e52951192afbbcbfcd7c11ef604ec45a470ca35a93afec2c8416dac985a5d1. `diff` against charged input engine.py (1cd21042…) is exactly one hunk, `40d39`, deleting `'option(nostdhilb,noprobabilistic);',` (box/engine.diff). FLAGS line 12, receipt dict (old 90–97), argv binding, `expression()`, exporter loop and every other byte are unchanged; no `set_int_max_str_digits`, no receipt pgid/namespace cross-check was added. This is precisely the smallest fix my prior code gate (2ee02c1a…, §A) prescribed conditionally.
- The conditional hypothesis is established by actual metadata, not by document comparison: api-metadata.stdout (693a7ad7…, 14:35:08Z) is a STDOUT capture showing `? unknown option \`nostdhilb\``, `? unknown option \`noprobabilistic\`` and `? error occurred in or before STDIN line 2`. metadata.stdout (fb87fbf1…) pins /usr/bin/Singular 90ab699b… as "version 4.3.2 (4330, 64 bit) Apr 1 2024", package 1:4.3.2-p10+ds-1.1build1, and /usr/bin/python3 a92f0f95… as Python 3.12.3. Both hashes are the ones bound in ROOT-REGISTRATION.json and in every one of the eight authorities.
- Fail-closed either way: those `?` lines precede the `F10-DECISION/1` header, so certificate.py line 48 (`framing/ring`) would refuse the transcript; with the line deleted the default std path uses neither option.
- Qualification: api-metadata.stdout does not itself show the command, exit code, or the stderr stream; the root's "exit 0, empty stderr" reading is documentary. Engine mathematics, input conversion and the exporter remain UNTESTED: the 76-file manifest contains no input.sing, singular.stdout/stderr, engine.receipt.json or decision.json, and caller.py lines 145–148 return before the engine stage in validate mode.

## B. Bindings — CONFIRMED

One metadata replay process (box/metadata_replay.py 11f56075…, stdout b90da8bd…; `timeout 10 prlimit --cpu=5 --as=134217728 python3 -I -B`; stdlib only, no charged import, wall < 1 s) parsed the 8 authority + 8 dispatch + 8 telemetry records, batch.FINAL.json, preflight.PASS.json, semantic-validation.json and ROOT-REGISTRATION.json: 194 checks, all OK, ALL-OK.

- Registration 79f6aa3d… enabled, compatibility_confirmed, mode validate, math deadline 14:57:00Z (epoch 1788965820), task deadline 15:00:00Z (1788966000). Engine SHA used everywhere is the recorded installed binary 90ab699b…; no local engine path was consulted.
- Stage order gate-disabled, gate-wronghost, gate-argv, gate-cap, gate-missing-input, valid, dummy, semantics: each dispatch record equals its batch.FINAL record; preflight.PASS records equal the first seven. Each dispatch's authority_sha256 and telemetry_sha256 equal the retained files' hashes.
- Every telemetry `argv_sha256` equals sha256(compact JSON UTF-8 of the authority child_argv + `\n`) with matching argv_count; that is CAPRUN's `canonical_argv_hash` (run_capped.py 184–188, the only CAPRUN lines read, for this named doubt; PARTIAL).
- child_argv and parent_argv of all eight equal the caller's line 78–85 construction (probe.py plain/descendant, semantic_tests.py for semantics); gate-argv carries `EXTRA`, gate-cap has rss_bytes '1', gate-disabled enabled=false, gate-wronghost hostname NOT-REGISTERED, gate-missing-input lacks the exact.json pin. Caps 5/3/2 GiB for controls, 32 MiB for dummy, 30/25/2 GiB for semantics. Every authority's file_sha256 equals the root's 13 pins plus the registration self-pin (minus the one designed omission).
- All stdout/stderr stream pins (path, bytes, sha256) match the retained files. Every telemetry has pid == pgid; every CAPRUN parent has ppid/pgrp/session 1312 = the original caller PID, namespace pid:[4026531836].
- Deadlines: seven non-mathematical stages carry hard = 1788966000.0 (task deadline); semantics carries first_math 1788965396.9842567, hard = first_math + 120 = 1788965516.9842567 < 14:57 < 15:00 (the 120 s bound dominates); returned 1788965397.0972862 < hard. All eight returned epochs are strictly increasing (one child at a time, sequential Popen/wait).
- Refusals: rc 1, NORMAL_EXIT, empty stdout, stderr tracebacks naming execution_gate.py lines 20, 30, 43, 57, 67 in that order; no disabled/wronghost/argv/cap/missing-input sentinel exists in the manifest. valid: rc 0, valid.sentinel = `POSTAUTHORIZE\n`.
- Same reviewed caller: c52a2f4c… in INPUT.sha256 (checked at dispatch and collect), in all authorities, and equal to the byte hash of remote/caller.py, which I read WHOLE and which is identical to the copy my code gate reviewed. certificate.py 0906a9d2…, semantic_tests.py 5d038617…, execution_gate.py cbfe55ff…, probe.py 02913a1c…, run_capped.py 4435279d… likewise.
- Remote hostname/DMI/systemd/journal observations (prepare/dispatch/collect stdout) are documentary custody, not remote attestation.

## C. Outcomes — CONFIRMED

- Dummy: leader PID = PGID 1344, forked child 1346 (dummy.stdout line 2 stat: pgrp 1344, ppid 880 after the leader's `os._exit(0)`), same namespace. Leader exited 0 and wrote POSTAUTHORIZE; the TERM-ignoring child's 64 MiB bytearray drove the sampled group RSS. Measured CAPRUN value: max_observed_group_rss_bytes 77,963,264 > 32 MiB cap → status RESOURCE_CAP, resource rss, rc 125. Identity events exactly MATCH / SENT 15 / MATCH / SENT 9 with observed pid = pgid = 1344 and start_identity `boot=c52b8d83…;start_ticks=9144` on both MATCH events; term_sent, kill_sent, cleanup_complete, leader_reaped all true; group_zombies_before_reap [1344], live group empty; wall 0.328 s. The journal's "2.2M memory peak" is the outer systemd service-cgroup figure and is NOT the RSS measurement; only CAPRUN's PGID sampling is the cap evidence.
- Normal-exit stages (five refusals, valid, semantics) show term_sent/kill_sent false and cleanup_complete null: these are null flags of a normal exit, not termination-path evidence. The actual TERM/KILL path is evidenced by the dummy alone.
- Semantics: rc 0, NORMAL_EXIT, empty stdout and stderr, CAPRUN 14:49:57.025365–14:49:57.087181, wall 0.06181923 s, sampled peak 8,982,528 B, no identity events. Receipt f6bf16c7… lists exactly the 19 designed labels in semantic_tests.py source order (lines 23–76). Retained malformed payloads fail in their intended controls by static match of the `reject` reason substrings (tests 27, 29, 49, 50, 56, 58, 63, 65, 73, 75, 76) against certificate.py messages (lines 105, 41, 68, 53, 110, 113, 23, 128, 127, 48); the two zero-residual controls assert the weak residual passes first (line 55). Nothing was rerun.
- `actual-twenty-row-readback` is Python readback of the artifact's own rows against themselves (tests 22–23): it is NOT Singular row conversion, which never ran. No new coverage is invented; the coverage limits stated in my code gate §D stand.
- Qualification: my replay checked the gate-cap telemetry caps only loosely (the refusal there comes from execution_gate line 57, before any cap applies); every other stage's telemetry caps were matched exactly.

## D. Q12/20 decision support — CONFIRMED with limitations; no blocking runtime mismatch

This exact semantic receipt satisfies every decide-mode precondition of the unchanged caller (lines 60–66): status PASS-DESIGNED-SEMANTICS, artifact 168bdfd3…, certificate_sha256 = sha(certificate.py) 0906a9d2…, tests_sha256 = sha(semantic_tests.py) 5d038617…, and its execution block equals the semantics authority d3c526ac… on the registered host/instance/job. It can therefore support ONE separately registered decide run only if root's new registration pins semantic_validation_path to this file and semantic_validation_sha256 = f6bf16c738d324f8565ab81530d720320e9ff87d3db26dbef13ddc0af98d232c, keeps engine.py 81e52951… and the same checker/tests, and sets fresh absolute clocks. No solver authorization, ideal, F10 or JC2 result arises here.

Limitations carried, none blocking: engine.py has zero executions (conversion, `--no-stdlib` quiet framing, exporter, `lift` four-argument form — present in the retained 4-3-2 reference.doc lines 3938–3943, with leadexp 3836 and numerator/denominator 5247/1466 read as pointers only); the semantic stage's 0.06 s is no forecast of the 60 + 30 s decide budget inside 120 s; Python 3.12.3 means the 4300-digit int/str limit is live and, by root's choice, unhardened, so a huge unit-branch cofactor fails closed as INCONCLUSIVE; the engine receipt pgid/namespace cross-check from my code gate remains unadded.

## Read/tool scope and qualifications

Tools: sha256sum, tar -t/-x, diff, cat/sed/grep, date, one prlimit-bounded python3 metadata replay. No AWS/SSH/network, no forks beyond that process, no /proc census, no execution of any charged source, CAS, artifact arithmetic, probe, caller, tests, engine or CAPRUN main; no shared /tmp writes; no source mutation; no JSON numeric transformation of artifact bytes. Read WHOLE: inputs 1, 2, 4–9; remote caller.py, certificate.py, semantic_tests.py, execution_gate.py, probe.py, ROOT-REGISTRATION.json, REGISTRATION.md (root-level and remote copies byte-identical), batch.FINAL.json, semantic-validation.json, preflight.PASS.json, INPUT.sha256, all 32 stage streams, dummy/semantics/gate-disabled telemetry, gate-disabled authority, prepare/dispatch/collect scripts and streams. The other seven authorities and five telemetries were consumed field-by-field by the replay parser (every field the caller writes or checks) rather than eyeballed line by line. PARTIAL: run_capped.py lines 184–188 plus a name grep; reference.doc only the four section pointers above. No corpus, provenance, peer, live receipt or log reads.

## Verdicts

A CONFIRMED. B CONFIRMED. C CONFIRMED. D CONFIRMED with the recorded bounded scope and its limitations; smallest concrete action for the next lane is the registration pinning in §D, not a source change.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check over this body; no corpus scan.

<!-- BODY-END -->
