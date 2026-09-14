# FIRST static gate: one literal solver pin in the accepted actual caller (fable5, 2026-09-10)

status=COMPLETE for A-C; verdict A CONFIRMED, B CONFIRMED (under the accepted 17z/17zh premises and ROOT's documented tail qualification), C CONFIRMED (scope only); no REFUTED; no blocking GAP; no new OPEN; smallest actual defect: none blocking (two documentary notes). STATIC-UNREVIEWED packet reviewed as text only; NO authority, registration, clock, host, worker, source acceptance or execution granted.

## 0. Custody and method

Launch (own `date -u`) 2026-09-10 02:29:11 UTC; controlling stop 02:36:30 UTC (earlier than launch+8 min = 02:37:11); final 2-min publication reserve; never reset. Own-only absence check at 02:30:42: this report and box/f10-quotient-actual-caller-migration-gate-fable5-20260910/ were both absent before the first write. All six ordered snapshots in /tmp/jc2-lane.qzO8Hy/inputs were hashed with sha256sum BEFORE any body read; all six equal the assignment pins (table below is pasted from that output). All six then read WHOLE: ROOT-CARD.md, caller.diff, both callers by `cat -n` (231 lines each), the 17z gate and the 17zh gate; the three-file parallel read was not clipped (each gate result ended at that gate's own final completion line). Operations: date, ls, wc, sha256sum, cat, diff, cmp, grep, tail, test, apply_patch. ZERO python, compile, import, AST, syntax, fixture, test, CAS, network, AWS, SSH, agents, provenance, corpus or Git access; no solver, checker, controls or registration file was read (none charged).

## A. Literal diff regenerated independently: CONFIRMED

- `diff -u accepted-dispatch_batch.py dispatch_batch.py` yields exactly one hunk, `@@ -163,7 +163,7 @@`, with one `-` and one `+` content line (grep count 2 in caller.diff). Its body (after the two file headers) is byte-identical to the body of the supplied caller.diff (cmp via process substitution). The changed line is line 166, the `solver.py` value of the `known` dict, 28df2b21... to 58cdc472... Both files are 231 lines and 15704 bytes; `cmp -l` lists 61 differing byte positions, all inside that one 64-hex value.
- Old snapshot 0f375da8... is the 17z custody row 8 (dispatch_batch.py) accepted there; the new snapshot digests to a7c0cf17... as pinned by the assignment.
- Every other byte is preserved, read in the old file: docstring "Existing supervisor unchanged" (L1-4); the dynamic ROOT self-pin, i.e. the caller's own hash is registration-supplied, not literal (L190 base includes dispatch_batch.py, L193 exact vector, L198-199 on-disk digest of every supplied pin), which is why the migration is one line with no self-referential edit; frozen per-child authority (L85-87 exclusive write, chmod 0444, digest; L100 re-digest after return); exact parent CAPRUN argv (L56-61) and child argv (L53); trailing-input pinning into the authority (L62-70); source-acceptance binding (L175-181, L200); checker and controls dispatch with the unchanged decision-status, certificate-digest and univariate binding requirements (L211-220, L213-218); STOP with no retry (L137, L226-231); five defect refusals and the dummy sequence (L204-208, L109-135).
- No new supervisor and no transplant: the diff adds no line other than the hash. The repaired generic caller hash 54c55be3 occurs in none of the six inputs; no barrier, externals-SHA CLI or other generic-caller text appears in the delta.

## B. One hash selects the new kernel; counts, binding, checker and controls unchanged: CONFIRMED under premises

- Consumption path of the single changed value, all unchanged code: L194-195 require registration file_sha256 for ROOT/solver.py to equal 58cdc472...; L198-199 require the on-disk solver.py to digest to it; L201 copies the vector into fixed_files and L62/L77 place it in every child authority as `file_sha256`. Per the accepted 17zh gate (section D), evidence.verified L85-87 requires solver.py pinned in that flat vector and checker.main L167-168 compares the certificate's `solver_sha256` against the same pin; no new key or schema is involved.
- Argument counts: the caller's solve trailing vector is still four items (L210-211), child vector nine; check and controls trailing are still five and six (L212, L219). The new solver's argv expectation is covered by ROOT's direct old/new main-to-EOF tail comparison (identical, 21c068ac..., ROOT-CARD), which is the documented gate qualification closing 17zh GAP-D1; this gate did not read either solver and does not re-verify it.
- Candidate binding (L216-218) and the two accepted decision statuses (L214) are unchanged and are produced by the unchanged checker (17z section B). Certificate schema: 17zh section C records that the new kernel's certificate() requires the full 1638/217 layout with the column index law matching checker L129, consistent with ROOT-CARD.
- Unchanged pins agree across both premises: checker 122842e5..., evidence cbe5a9e0..., algebra 7d565299..., execution_gate cbfe55ff... at caller L167-170 equal 17zh rows 4-7 and 17z rows 6, 9, 4, 10. semantic_controls.py is not literal-pinned in the caller (L190 base membership only, value registration-supplied); ROOT-CARD states it unchanged at 238ae674..., which equals 17z row 12.
- Not proved by this literal migration: syntax/import (17zh GAP-1), python-flint API semantics (17zh GAP-2), runtime cost of the new kernel against the registration's `solve` profile caps, and any actual result. A failing kernel yields STOP at L137; no cap raise or retry exists in the delta.

## C. Scope: CONFIRMED

- Retained as before: cooperative (not enforced) frozen authority (L86 comment, chmod only), startup source checks (L198-199) and post-source checks (L99-100), admission margin and stored hard cutoff (L45-51, L108).
- Retained limitations, none new: the live-PGID sweep at L98 is a /proc snapshot after wait (race window); caller_stat at L94 and the vendor/asset-tag/hostname checks at L148-150 are metadata reads; CAPRUN sampling is a 17z premise. No generic-caller hardening is inherited or claimed.
- The generic R3 runtime gate is not an input and was not inspected. This packet contains no registration file; ROOT's separate registration must carry file_sha256 for dispatch_batch.py = a7c0cf17... and solver.py = 58cdc472... to satisfy L193-199, and both the generic runtime evidence gate and this gate precede that registration. No test farm, blanket readiness, automatic retry, cap raise or JC2 claim.

## Smallest actual defect and GAPs

- Blocking: none.
- Documentary 1: caller.diff headers name `accepted-dispatch_batch.py` / `proposed-dispatch_batch.py` while the charged snapshot is `dispatch_batch.py`; the hunk is identical, so no custody effect.
- Documentary 2: the `known` dict retains three literal pins that 17z lists as not charged (run_capped.py, admissibility.md, frontier.json); unchanged here and out of this delta's scope.
- GAP: old/new solver tail identity and argv count rest on ROOT's 21c068ac... qualification, not re-read here (by mandate).

## Input custody table (pasted from own sha256sum output)

| # | file | sha256 |
|---|------|--------|
| 1 | ROOT-CARD.md | f00bab656e249e46002fab229776a8129a2a25b4db8075e350e3979a473944b7 |
| 2 | accepted-dispatch_batch.py | 0f375da83d17d695cb0d502d842f8be82bf12bb4bdba38d6735ab0ac8efc06ed |
| 3 | dispatch_batch.py | a7c0cf17379b624358e8cc010226c7b179a0218330191540918e15e9ee4303d2 |
| 4 | caller.diff | 411cbf292c1d4828bff260f39d1db67ee722c888feb1f8d6f2bdfe7995499e82 |
| 5 | f10-r1-exact-linear-decision-gate-fable5-20260909.md | 4c3f5932e9ff77d73314fe02b3c088677f8fc3bc0971acad9ba56610cf7d405f |
| 6 | f10-r1-quotient-remainder-static-gate-fable5-20260910.md | a797cbed9ad4483ec453599fc8154e4d5ce2dd64b06d0796a79a0ad69655cbef |

## OPEN(S) RAISED

None. No exit-price assertion, no charge_basis line, no Seal and no closing hash section are authored.

## COLLISIONS

status: EMPTY. Own-only check of the two owned targets at 02:30:42 UTC before creation; no corpus scan and no broad listing claimed.

## Own whole-read and completion

Own whole-read at 02:32:34 UTC by `cat -n` of lines 1-54: title, status line, sections 0, A, B, C, defects/GAPs, custody table (6 rows), OPEN(S) RAISED, COLLISIONS. The owned box/expected-sha256.txt (pasted from own sha256sum output) verified 6 of 6 OK by `sha256sum -c` against the charged inputs at 02:32:34; all 64-hex tokens in this report equal, by comm in both directions, exactly those six digests. The 8-hex prefixes in the body (28df2b21, 58cdc472, 54c55be3, 21c068ac, 122842e5, cbe5a9e0, 7d565299, cbfe55ff, 238ae674) are assignment, ROOT-CARD or caller-literal values, not custody rows. No placeholder, TODO, Seal, charge_basis or closing hash exists; no marker precedes this section. Owned box final inventory: expected-sha256.txt only. Verdict unchanged after the whole-read: A CONFIRMED, B CONFIRMED under premises, C CONFIRMED. Nothing executable was created or authorised; ROOT's separate registration remains the only next step. Completed before the 02:36:30 UTC stop; all writers idle after the marker.

<!-- BODY-END -->
