# f10-r1 exact-decision extended cap/receipt delta gate (Fable 5.1, 2026-09-09)

tag=f10-r1-exact-decision-extended-gate-fable5-20260909
reviewer=Claude Fable 5.1 (claude-fable-5-1); ONE narrow static review of two source deltas. NOT execution evidence, not an ideal decision, source-validity theorem, certificate, worker, allocation or dispatch authority.
launch=first command 15:26:05 UTC; deadline = earlier of 15:34:05 and 15:34:00, i.e. 15:34:00 UTC; no reset. Basis 0d39df3c9fd69c939a8420c54d03228b9077777d.
owned: this report and box/f10-r1-exact-decision-extended-gate-fable5-20260909/ only.

## 0. Custody

All 12 charged inputs were hashed from /tmp/jc2-lane.TFJeqt/inputs in the prompt order BEFORE any whole read; all 12 equal the ordered list (12 OK, table in §5 generated from sha256sum output). The two prior-source copies carry exactly c52a2f4c… (prior-caller.py) and 81e52951… (prior-engine.py); their identity with the earlier boxes is asserted by the prompt and by my two prior gates (inputs 9, 10), not re-derived here (no provenance follow). All 12 inputs were then read WHOLE.

My own `diff prior-caller.py caller.py` gives hunks 74c74 and 149,150c149,150 only; `diff prior-engine.py engine.py` gives 6c6, 88c88, 96c96,99 and 97a101 only. The +/- lines of my `diff -u` output are byte-identical to the +/- lines of the charged caller.diff and engine.diff (box/…: the compare printed CALLER-HUNK-LINES-IDENTICAL / ENGINE-HUNK-LINES-IDENTICAL). So the two literal diffs are complete and honest.

## 1. Verdicts

A CONFIRMED. B CONFIRMED (with the stated informativeness limits). C CONFIRMED as a code-consistency statement with one typed GAP outside the charged inputs (certificate.py's receipt key handling); the one-longer-attempt rationale is accepted as bounded diagnostics, not as a forecast. No blocking code mismatch demonstrated. No execution or allocation authority follows.

## 2. A — cap delta (caller): CONFIRMED

- Exactly three executable sites change (caller.py vs prior-caller.py): line 74 `first_math+120` → `first_math+690`; line 149 engine `60,50` → `600,550`; line 150 verify `30,25` → `60,50`. Semantics stays `30,25` (line 146, unchanged). Nothing else differs (diff above).
- Unchanged and verified by line: RSS default `rss=2147483648` (69); RLIMIT_FSIZE 16 MiB preexec (20, 106); fresh same-caller controls five refusals/valid/dummy before any mathematics in both modes (139–143) with the unchanged dummy predicate (121–135); +15 admission `now+wall+15<hard` (75); absolute root cutoffs `deadline`/`task_deadline` required strictly ordered (47–48) and folded into `hard` (71–74); post-return `returned<hard` (118) and post-run pinned-file recheck (112); registration re-hash before each stage (76); host/instance/cwd/job_tag guards (41–46); source pins (50–59); decide-mode semantic-receipt precondition (60–66); CAPRUN parent argv/authority spec (78–102); namespace check (108); `quiet(pgid)` (111); strict cap/failure refusal (136); STOP record on any exception (154–156). `start_new_session=False` (106): no new PGID.
- Budget arithmetic. In decide mode `first_math` is set at engine admission (73), so at engine admission `hard = t0+690` provided root's clocks allow; admission needs `t0+615 < hard` (75), i.e. `math_deadline > t0+615`. Verify admission at `t1 = t0 + e + o` (e = engine CAPRUN elapsed, o = post-run overhead: quiet scan, full pinned-file re-hash at 112, record write) needs `t1+75 < t0+690`, i.e. `e+o < 615`. So 690 = 600+15+60+15 exactly, the same identity as the old 120 = 60+15+30+15 (my code gate §C). An engine that reaches its 600 s wall cap is already refused at 136 (RESOURCE_CAP), so the operative window is NORMAL_EXIT with elapsed+overhead under 615 s: the 15 s overhead allowance is unchanged in absolute size. Verify admitted by t0+615 with 60 s wall returns by about t0+675 plus grace, leaving 15 s for the late-return check at 118. CPU 550 < 600 and 50 < 60: for single-threaded exact std CPU ≈ wall, so the per-process inherited RLIMIT_CPU binds first at ~550 s; that outcome is typed at the nested level only via §3, not by CAPRUN (telemetry `enforcement.cpu`: "typed only on SIGXCPU").
- Root duty (fail-closed, not a code defect): the fresh `math_deadline_utc` must exceed the expected `first_math` by more than 690 s, else `min(...)` at 74 shrinks the window and admission or the late-return check refuses. CAPRUN acceptance of `--wall-seconds 600 --cpu-seconds 550` is an accepted-interface assumption; run_capped.py is not a charged input and no maximum-cap argparse rule was recorded by my code gate.

## 3. B — engine delta: CONFIRMED

- Changes (engine.py vs prior-engine.py): line 6 adds `resource` to the import; line 88 `usage=resource.getrusage(resource.RUSAGE_CHILDREN)` immediately after `rc=child.wait()` (87) inside the same `with`; lines 96–98 add `children_rusage` (ru_utime, ru_stime, ru_maxrss, scope string); line 99 `'ENGINE-FAILED-INCONCLUSIVE' if rc!=0 else 'CANDIDATE-ONLY-NOT-DECISION'`; the unchanged refusal `need(rc==0 and sha(executable)==authority['engine_sha256'], …)` moves from before the dict (old 88) to after the exclusive receipt write (new 101). Nothing else differs: FLAGS (12), VARIABLES/IDS (10–11), `expression()` (20–34), `script()` exporter/std/lift/protocol (36–60), argv binding (73–74), Popen with `start_new_session=False` (79–80), /proc identity and PGID checks (81–86) are byte-identical. No new PGID, flag, exporter, order, row, solver or checker change.
- Signed nested returncode: `rc=child.wait()` (87) is the Popen value (negative signal number on signal death) and is stored unchanged at 95 whenever wait() returns and the receipt construction (four sha() reads, 90–95) and the `open('x')` write (100) succeed. A SIGXCPU death would appear as `returncode: -24` with status ENGINE-FAILED-INCONCLUSIVE; never a candidate (99). The wrapper then raises at 101 → rc 1 → caller 136 refuses → batch.STOP.json (155). Not crash-proof: a CAPRUN wall/RSS group TERM/KILL, an identity failure at 85–86, or a failed sha/write still leaves no receipt (CAPRUN telemetry then carries the typed cap).
- rc 0 with a hash mismatch: the receipt is written with status CANDIDATE-ONLY-NOT-DECISION (99) and then 101 raises; the caller's post-run recheck of the pinned engine binary (caller 112, 'post-run input changed') and the rc/status check (136) both stop the run, and verify never dispatches, so the receipt stays a candidate only. Informativeness limit only: that receipt's status does not itself record the hash failure (visible only in the stderr traceback). Not requested hardening; noted, not raised.
- Limits of RUSAGE_CHILDREN vs CAPRUN group telemetry: it is post-mortem accounting for children the wrapper has waited for (here exactly one Singular child; `--no-shell` suppresses shell escapes), cumulative, not the wrapper's own usage (RUSAGE_SELF), not a live sample, not enforcement, and not attestation. On Linux ru_maxrss is the largest waited child's high-water mark in KiB, not the PGID RSS sum; CAPRUN's max_observed_group_rss_bytes is a sampled aggregate over the non-zombie PGID including the Python wrapper at 0.05 s intervals (telemetry lines 18–20), so the two numbers are different measures and cannot be equated. ru_utime+ru_stime ≈ 550 together with rc −24 would be strong diagnostic evidence for CPU exhaustion, but still not a CAPRUN-typed cap.

## 4. C — one same-Q12/20 followup after fresh same-caller controls: CONFIRMED with one typed GAP

- First-attempt evidence in my inputs: engine.telemetry.json shows caps 60/50/2 GiB, status NORMAL_EXIT, child rc 1, resource null, term/kill not sent, wall 51.599 s, peak sampled group RSS 139,493,376 B, wrapper stdout 0 bytes. engine.stderr is the prior-engine.py refusal at its line 88 (traceback line numbers 15/88/99 match prior-engine.py exactly), raised before any receipt, so the nested Singular status was lost. 51.6 s ≈ 50 s CPU cap + wrapper overhead is consistent with an inherited-RLIMIT_CPU kill of Singular but equally with any nonzero Singular exit; it remains an inference. The twenty-row-block/no-branch transcript is root-supplied context; I did not inspect it.
- Code consistency of the followup: the decide-mode precondition (caller 60–66, unchanged) binds the pinned semantic-validation receipt to status, artifact 168bdfd3…, `sha(root/'certificate.py')` and `sha(root/'semantic_tests.py')` only, never to caller.py or engine.py hashes. The exporter/protocol the checker was validated against (engine.py 36–60) is byte-identical. So no code path requires a semantic rerun, and none was added. Fresh same-caller controls are not optional: 139–143 run before the engine stage in decide mode. Root must pin the new caller 386a352d… and engine 6123faf9… in `file_sha256` (56–59), keep certificate.py/semantic_tests.py at the hashes the receipt binds, pin `semantic_validation_path`/`_sha256` (61–62), use a fresh job_tag directory (41–42; all `open('x')` writes, 19/76/100, refuse an existing file), and set fresh absolute clocks per §2.
- GAP (outside charged inputs, not demonstrated): certificate.py consumes engine.receipt.json at the verify stage (my code gate §C cited its lines 137–145 as field re-binding). If it enforced an exact key set, the added `children_rusage` key would fail closed at verify and waste the attempt. My prior gates recorded no such exact-key rule, so no mismatch is shown; root should confirm the checker's receipt-key handling by reading before registering. Fail-closed either way; no soundness exposure.
- Rationale: accepted as ONE bounded diagnostic attempt. The decision-changing content is precisely §3: a wait-returned failure now records the signed nested rc and child CPU/RSS, so a second failure would be typed at the nested level (SIGXCPU vs Singular error vs normal) instead of being lost. It is not evidence that 550 CPU-seconds suffice for this std over Q; nothing in these inputs bounds the solve. Low RSS in a 51 s run is no forecast for a 10× longer one, but the 2 GiB sampled cap still fails closed. A second non-informative or capped result forces redesign, as root states; a CAPRUN-killed run is informative only at the CAPRUN level.

## 5. Custody table (generated from sha256sum output, prompt order)

| sha256 | file |
|---|---|
| 3ae4232abe7cf91f7f50b5cab12d1063222b86718143daa128cd0147b7bc0122 | f10-r1-exact-decision-extended-code-astra-20260909.md |
| 2bcf76aa6d0e29e711e6c497ec130ad01ffd90db763cb540d210b8dcda742a09 | f10-r1-exact-decision-extended-code-astra-20260909.md.artifact.json |
| 386a352d654fb72a81026dc39a2a13aeb72020d69f5c11b0b10e8d01a099523b | caller.py |
| 6123faf96ab70abcd1d00f545619eaa9c64145c621035d7c8f37be801cf09d4b | engine.py |
| a8b751c2b7a77d6fcf56dd810a790595051ea66a2d0862908ea242bad9ad8091 | caller.diff |
| 73ab3a75b7937ebae46144f3ae35c1fa3601e1686199bfbf5ac8bde3d0881f25 | engine.diff |
| c52a2f4cdbfe477b97f7cef2c162df3d73a1a221ebc32825acaf9aa2ad62c943 | prior-caller.py |
| 81e52951192afbbcbfcd7c11ef604ec45a470ca35a93afec2c8416dac985a5d1 | prior-engine.py |
| 2ee02c1a4494ef086ef75c2943c98b46733302fc52e5866ef68eb479014d254b | f10-r1-exact-decision-code-gate-fable5-20260909.md |
| 4a6c986430e17d47ffe5fe70b371f7eeec830ca10a6b2d6bb61f5fc7d8a45b9a | f10-r1-exact-decision-validation-gate-fable5-20260909.md |
| ca1b8770537f57663c9e65b404b5205bc0889870d0046421245d53b08e066eca | engine.telemetry.json |
| b1215e53012f38f2e1243892dc8418c119b74d64f34522aa0c5ea6ed4a4bc501 | engine.stderr |

Own box: input-pins.sha256 (the sha256sum output above), custody-table.md.

## 6. Read/tool scope and limitations

Tools: sha256sum, cat -n, diff/diff -u, grep, awk, wc, date, mkdir, heredoc writes. All 12 inputs read WHOLE after the ordered hash check. ZERO compile/import/test/probe/CAS/subprocess-experiment/mathematical execution; no AWS/SSH/network/web, no process census, no corpus, peer, provenance or transcript reads, no shared temporary files, no source mutation, no run_capped.py/certificate.py/execution_gate.py/probe.py reads (not charged; cited only through my two prior gate reports). Static review only; nothing here is runtime evidence. Deadline pressure: 8-minute lane; every claim above is tied to a line of the charged sources.

## OPEN(S) RAISED

None. (The §4 certificate.py receipt-key question is a root pre-registration check, not a mathematical OPEN.)

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check over this body; no corpus scan.

Scratch disclosure: my first hash command created and immediately removed two transient scratch files (an expected-hash list under /tmp and a hash list at box/f10-r1-exact-decision-extended-gate-fable5-20260909-actual.tmp, outside my owned directory); both were deleted in the same command and verified absent before this line. No other write outside the owned report and box occurred.

<!-- BODY-END -->
