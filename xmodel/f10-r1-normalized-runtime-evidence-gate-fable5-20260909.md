# f10-r1 normalized runtime EVIDENCE gate (Fable 5.1, 2026-09-09)

FIRST actual runtime-evidence review of the root-owned normalized generate / full-check /
controls batch. Launch 20:38:59 UTC; controlling stop 20:57:00 UTC (earlier of 20:57:00 and
launch+20 min), never reset. Premises, all qualifications retained: accepted STATIC 17n backend
gate (0f653f53...) and STATIC 17r runtime gate (4968f8d3...). Source and code unchanged. Read
scope: the exact 30-file charged snapshot only. No CAS, subprocess, arithmetic, import, compile
or test of any size ran; no Python was invoked; only sha256sum, grep, sed, head, diff and cat.
No provenance follower, corpus, ledger, peer, live or protected file, network, AWS, SSH, /proc
or agent was touched. normalized.json and exact.json were read HASH/SHAPE only (head/tail bytes
and key-name inventory; no coefficient was evaluated). Owned outputs: this file and
box/f10-r1-normalized-runtime-evidence-gate-fable5-20260909/ only.

## Custody

All 30 ordered SHA256 values matched before any body read, both for the repo paths and for the
lane copies in /tmp/jc2-lane.yU0Uo8/inputs (30/30 and 30/30; the digest sequence of
charged-inputs.list equals the charge's list line for line). The sha256sum output is
box/f10-r1-normalized-runtime-evidence-gate-fable5-20260909/input-custody.sha256.
Read WHOLE: coordinator report and artifact.json, REGISTRATION.md, dispatch.registration.json,
full.receipt.json, all three mathematical authorities and telemetries, dummy stdout and
telemetry, batch.PASS.json, preflight.PASS.json, controls.receipt.json (mutation_evidence wires
inspected only as strings for nonzero-ness and h3_retained), terminal.sha256, checker.py,
execution_gate.py, probe.py, semantic_controls.py, dispatch_batch.py, generator main.
Selected slices: custody.json (non-remote fields whole, the 99 remote entries by extracted
path/hash pairs), run_capped.py (grep of identity, RSS-cap, termination and default-telemetry
lines; whole text was the 17r premise), the two premise gates (verdict, qualification and
GAP sections). Root's host, process, AWS and timing observations remain root evidence; I did
not observe them.

## Verdict summary

A CONFIRMED. B CONFIRMED. C CONFIRMED. D CONFIRMED as qualified ENGINEERING representation
success, and the genuine normalized full receipt MAY serve as the evidence prerequisite for the
separately reviewed adapter under root-owned acceptance. No REFUTED item. Smallest actual
defect: the administrative publication overrun (below); it has no evidential consequence.
No hardening is requested. No OPEN is raised.

## A. Actual custody / runtime binding: CONFIRMED

- **Root report transaction.** The first 11514 bytes of the coordinator report, ending at the
  standalone marker line, hash to 5657c756..., equal to artifact.json body_sha256; artifact
  full_sha256 4ed33d0b... equals the charged file hash; custody.json names the artifact hash
  d9e40894... as report_transaction_sha256. The custody file excludes itself, as it declares.
- **Manifest reconciliation.** terminal.sha256 has 99 lines; custody.json has exactly 99 remote
  entries; the extracted (hash, name) pairs are set-identical to the manifest (diff empty). All
  22 charged remote files carry the manifest hash. The 10 authority/telemetry hashes in the
  three mathematical and dummy records and the 12 gate-* authority/telemetry hashes are all
  present in the manifest. Uncharged remote files (admissibility.md, frontier.json, the caller
  stdout/stderr and dispatch.json files, fixtures) are manifest-bound only; not read.
- **Registration.** dispatch.registration.json pins eleven local files plus /usr/bin/python3,
  the set dispatch_batch.py:174-175 demands; the nine constants at :164-172 equal the charged
  copies (generator d444d022..., checker 091bbf35..., algebra 7d565299..., helper cbfe55ff...,
  CAPRUN 4435279d..., probe 02913a1c..., exact 168bdfd3..., admissibility 02952e1b...,
  frontier f9d1fddc...); caller 8cb4d31f... and harness c0c83c73... are the charged copies.
  Every per-operation authority repeats this vector plus dispatch.registration.json 8f957b08...;
  the semantic-controls authority additionally pins normalized.json e62734b0... and
  full.receipt.json 062cf0c0..., exactly the fresh-registration rule of dispatch_batch.py:63-70.
- **One generate.main, one checker.main.** batch.PASS holds ten records, exactly one named
  generate (operation build, child argv length 7, telemetry argv_count 7) and one full-check
  (operation check, argv length 8, argv_count 8); the caller has one run() call for each
  (:189-190), refuses pre-existing outputs (:72, :181-182), and generator.py / checker.py open
  their outputs exclusively. generate.authority child_argv is python3 -I -B generator.py auth
  exact normalized, and the parent_argv is the exact CAPRUN vector execution_gate.py:46-57
  requires; the full-check authority is the analogous 4-argument checker vector.
- **Genuine full receipt.** full.receipt.json (1564 B) binds source 168bdfd3..., artifact
  e62734b0... at 432282 bytes (equal to the charged normalized.json size and hash), authority
  65e0e72e... (equal to the charged full-check.authority.json hash and to the full-check batch
  record's authority_sha256), job tag, host and instance, status
  PASS-NORMALIZED-REPRESENTATION-NOT-IDEAL-DECISION, and the declared 20 original / 9 G / 2 H /
  8 bracket-band / 10 pole scope. These five integers are the typed constants of
  checker.py:228 and are backed by the code paths the 17r gate traced (slots :101, rows
  :181-188, G :217-219, H :220, bands :175-176, poles :198-211); the eleven measured rows are
  computed at :225-227 from the same objects. The receipt is consistent with checker.main:
  :242 adds execution custody, artifact hash, SOURCE and byte count, and the key set of the
  receipt is exactly that union. Timing: telemetry utc_start 20:15:58.086 to utc_end
  20:16:01.981 lies inside the batch record started 20:15:58.042 / ended 20:16:02.007, exit 0,
  NORMAL_EXIT, stdout 50 bytes with the hash the manifest lists for full-check.stdout, stderr
  empty. normalized.json's documentary strings (schema, source_sha256, implementation_sha256
  d444d022..., job tag, host, instance, scope) match generator main; the artifact was generated
  under the same authority chain (generate telemetry 20:15:56.577 to 20:15:58.016, exit 0).
- **Root-only evidence, preserved.** Terminal unit state, absence of PID 1466 and the cgroup,
  MemAvailable, DMI, the 20:17 stop and the pre-pull hash capture order are root observations.
  The 307729-byte older representation cited for size comparison is uncharged and unverified
  here. CAPRUN argv_sha256 values were not regenerated by root or by me.

## B. Caps, admission, batch/preflight, dummy-descendant cleanup: CONFIRMED

| item | evidence |
|---|---|
| stored absolute cutoff | records 1-7 hard_cutoff_epoch 1788985860.0 = 20:31:00 UTC, the min of the two registered deadlines (dispatch_batch.py:153-154) |
| aggregate cutoff | records 8-10 hard_cutoff_epoch 1788985706.533481 = first_math_epoch + 750 (:50) |
| admission | every record admission_margin_seconds 15; :46 and :51 require now+wall+15 below the cutoff; the largest child (controls, wall 300, start 20:16:02) satisfies it |
| profiles | registration probe 5/3/2 GiB, dummy 5/3/32 MiB, generate 180/170/2 GiB, check 180/170/2 GiB, controls 300/280/2 GiB; every authority's caps and every telemetry caps block repeat its profile literally |
| ten records | 5 refusals rc 1, valid rc 0, dummy rc 125, generate/full-check/semantic-controls rc 0; every returned_epoch precedes its hard_cutoff_epoch (:106); every remaining_group_live is [] |
| preflight equality | preflight.PASS records are byte-identical to the first seven batch.PASS records (same pids, stats, hashes, epochs); preflight utc 20:15:56.533315 precedes the first admission 20:15:56.533481 |
| ordinary vs resource | refusals are ordinary nonzero exits under NORMAL_EXIT (:108); the only RESOURCE_CAP is the dummy (resource rss); the three mathematical telemetries have resource null and empty stderr |

Dummy descendant. probe.py forks a child that ignores SIGTERM and allocates 64 MiB, then the
leader exits 0 (:19-21). Telemetry: child_exit_code 0 for leader 1498; stdout line 2 shows child
1500 in pgid 1498 with PPID 1 in its stat, so a genuine orphaned same-PGID descendant was
exercised. max_observed_group_rss_bytes 78012416 exceeds the 33554432 cap; status RESOURCE_CAP,
resource rss, runner_exit_code 125, termination reason rss_cap; identity_checks are exactly
MATCH (pid 1498 = pgid, start identity equal to the registered one), SENT 15, MATCH, SENT 9;
term_sent, kill_sent, cleanup_complete and leader_reaped true; group_live_before_reap [],
zombies [1498]. This is the identity-matched cleanup path of run_capped.py (validate_identity
368-388, send_group_signal 437-450, rss_cap 876). The caller re-checked the sequence, pin equality
and the non-zombie PGID quiet state (:96, :110-133).

Conventions. The three normal exits carry termination reason null, cleanup_complete null,
term/kill false, leader_reaped false and identity_checks []: these are the untouched defaults
of run_capped.py:767-778 when no termination path fires, not dummy-type flags. No live child
tree capture exists (unit already inactive at 20:16:23), no outer transient-unit CPU or peak is
recorded, the enforcement strings state overshoot is possible, and the CAPRUN wall_elapsed values
are not CPU, billing or headroom figures. Nothing here invents them.

## C. Eight negatives / controls receipt / harness binding: CONFIRMED

controls.receipt.json lists eight cases, each with entrypoint "checker.verify IN-PROCESS, not
checker.main", exception ValueError, status EXPECTED-REJECTION, a distinct fixture hash and the
exact reason strings of the 17r trace: source-bound completed matrix; full affine forcing
including third correction; full Pi; H0 whole constant target; H1 whole linear target; float
forbidden; canonical rational; H0 whole constant target (large integer). Fixture sizes
(432282, 432328, 432284, 432308, 432308, 432302, 432283, 418739 bytes) are consistent with the
mutations (one entry, two c3 wires, sign flips, constants, one float key, one plus sign, one
single-term H0). The harness requires the fixture to differ, rereads it, demands the exact
class and string, and raises on acceptance (semantic_controls.py:46-64); a receipt therefore
exists only if all eight rejected. The receipt binds harness c0c83c73..., code hashes,
source 168bdfd3..., normalized e62734b0..., genuine_production_receipt 062cf0c0... (the
full receipt above) and authority a0668a4f..., equal to the charged semantic-controls
authority and to the batch record; the authority pins the current normalized.json and
full.receipt.json, so the finite harness ran against the genuine current objects (:25, :38-42).

Historic control. mutation_evidence records literal_old_rule N_i=-W_i+(6-i)*gap*D_(i+1) against
correct_rule N_i=-W_i+(7-i)*gap*D_i, gap z-U*d0 with d0=maps[2][2], i_range 0..4, h3_retained
true, and delta_c3 as two wires each containing nonzero rational terms (inspected as strings;
not evaluated), so the :85 nonzero precondition actually passed and the forcing vector, not the
column, was mutated. Matrix and third-forcing failures are early source bindings
(checker.py:121, :145); Pi and H failures are late projections (:172, :220) reached with
unchanged A/B, bracket and poles, which the receipt's negative_limit states: no altered-pair
late bracket/pole coverage. Float, noncanonical and the 9007199254740993 case are rejection
controls; the precision block claims no positive round-trip fidelity. No control computation
was repeated here.

## D. Acceptance scope: CONFIRMED (qualified)

What may be reported: one genuine generation and one genuine original-bound full check of the
normalized representation completed on the registered worker, artifact 432282 bytes; CAPRUN
wall_elapsed 1.44 s, 3.89 s and 13.67 s with sampled group peaks 22880256, 25280512 and
28762112 bytes for generate, full-check and semantic-controls; the G/H inventory (G1..G9 terms
56, 49, 35, 70, 56, 49, 35, 21, 28; H0 84, H1 70; max v-degree 6 throughout) as reported by the
receipt. No solver speedup, height improvement or CPU cost follows. No unitness, properness,
point, source closure, univariate result or JC2 resolution follows; the 17n/17r
qualifications (c2 length not inventoried, gauges not a resonance theorem, any left inverse
passes, h3/h4 runtime-enforced) persist unchanged.

Prerequisite verdict: the observed genuine normalized full receipt 062cf0c0..., bound to
artifact e62734b0..., source 168bdfd3..., authority 65e0e72e..., manifest ced92c65... and the
eight-control receipt 03c7b0e1..., MAY now serve as the accepted evidence prerequisite of the
separately reviewed adapter, under root-owned acceptance. This says nothing about whether that
adapter has run or is correct. No normalized_acceptance is issued by this gate; custody.json
correctly records downstream_normalized_acceptance false until root sets it.

## Smallest actual defect and consequence

Administrative only: the artifact was finalized 20:34:45Z and custody.json prepared 20:36:00Z,
after the 20:34:00 task/collection cutoff that was not reset; the root report records this
openly. Consequence: the report and custody are late collection records, not deadline-compliant
ones, and nothing infers post-cap computation from them: every mathematical child ended by
20:16:15.749 (batch end_epoch), the manifest was captured before payload reads per root, and
the worker was stopped per root. No evidential field is contradicted. Nothing blocks scope D.

## Raised OPEN

None. No new bounded scientific quantity with a cheapest test was found in this evidence review.

## Own-only collision check

This report makes no exit claim, prices no OPEN and carries no exit-price line or seal block. It does
not restate the accepted 17n/17r verdicts as new findings; it consumes them as premises. Its
only new assertions are the reconciliations above (body hash, manifest equality, hash chain,
timing containment), each checked against the charged snapshot in this lane. No overlap with
another owned file: the box directory contains only input-custody.sha256.

## Own whole-read and completion

Own whole-read at 20:46 UTC by cat -n and grep of the section list: custody, verdict summary,
A, B, C, D, smallest defect, raised OPEN (none), own-only collision check. No placeholder
remains. The report contains no full 64-hex token; all 23 eight-hex prefixes it uses were
matched by grep against the charged-input list, terminal.sha256, custody.json, artifact.json,
dispatch.registration.json and controls.receipt.json, none unmatched. The owned box directory
holds only input-custody.sha256 (30 lines, sha256sum -c 30/30 OK). No worker, registration,
cap, authority or computation was created or run. Completed before the 20:57:00 UTC stop; all
writers idle; nothing follows the marker.

<!-- BODY-END -->
