# F10 r1 runtime evidence gate: the complete v2 artifact (Fable 5.1)

**Verdict: RUNTIME PASS at the permitted scope.** All four review groups A–D are CONFIRMED by documentary recomputation against the 143 immutable charged snapshots. The permissible promotion is exactly: the frozen builder emitted a complete exact 12-variable, 20-slot representation (`exact.json`, 88,634 bytes) and the fixed accepted checker's ordinary runtime modes accepted it on the registered host under the recorded caps. This is NOT properness, NOT the unit ideal, NOT a point, NOT a degree exclusion, NOT a counterexample and NOT a JC2 solution. No solver ran and none is licensed here.

## 0. Custody and read scope

Intake 2026-09-09 13:44:07 UTC. All 143 charged snapshots in the lane inputs directory were hashed first and every one matched the charged vector byte-for-byte (recomputation: `sizes.txt`, `expected.txt`, `actual.sha256` in my box). Read whole: producer report, READ-SCOPE, REGISTRATION, both prior Fable gates, `dispatch_batch.py`, `execution_gate.py`, `precision.py`, `probe.py`, `batch.PASS.json`, `preflight.PASS.json`, all 16 authority/dispatch/telemetry triples, all seven checker receipts, the precision receipt, final process audit and instance poststate. `builder.py` and `checker.py` were read for schema, wire format, mode dispatch and failure strings only, at their accepted 16u scope. `run_capped.py` was consulted only for the argv-digest encoding (its `canonical_argv_hash`). Every stdout/stderr of the 16 operations was inspected whole. `exact.json` was byte-hashed and schema-inspected with a float-rejecting, integer-preserving parser; coefficients were never re-serialized or hand-checked.

Interpreter boundary: the caller pins `/usr/bin/python3` to `a92f0f95…f96223` and every authority records it, but no interpreter binary is in the snapshot. That pin is root/producer established and is not independently verified here. CAPRUN source is accepted; only its argv-hash interface was inspected, and no discrepancy was found.

All checks below were executed as stdlib-only hashing/JSON/schema scripts, each under 10 s and well under 128 MiB, with no subprocess, signal, `/proc`, or network use. Their consolidated output is pinned as `bind.out` (SHA `2afb499296f1cba449ebc7f014220c794dee89881ccacbbe4534a795acf76ce6`).

## A. Batch binding, ordering, budget and caps. CONFIRMED.

Tested predicates, all TRUE for all 16 entries unless stated:
- The 16 batch records equal the 16 `*.dispatch.json` files, in the frozen caller's order (five refusals, valid, dummy, build, seven checks, precision); `preflight.PASS.json` records equal the first seven.
- `authority_sha256` and `telemetry_sha256` in each record equal the snapshot bytes of the authority and telemetry files; telemetry `stdout`/`stderr` path, byte count and SHA equal the snapshot stdout/stderr files after remapping the remote cwd to basenames.
- `argv_sha256` recomputed from the recorded `child_argv` with CAPRUN's declared encoding (compact JSON, `ensure_ascii=False`, trailing newline) matches 16/16; `argv_count` matches.
- Intended parent argv equals the exact required CAPRUN form built from the authority's own caps, cwd, output files and child argv; caps, cwd and executable in telemetry agree with the authority.
- The nine helper/source pins plus the interpreter pin in every authority equal the caller's hard-coded pins and the snapshot bytes of those nine files (frozen caller `aaafa62a…`, corrected precision `56400dd3…`).
- Check operations pin their input: `frontier.json` for probes, `exact.json` (`168bdfd3…`) for the seven checks and precision, matching the snapshot.
- Deliberate controls accounted for, not glossed: `gate-disabled` has `enabled=false`; `gate-wronghost` records the bogus hostname; `gate-argv` records parent argv plus `EXTRA`; `gate-cap` records `rss_bytes="1"` so its parent argv deliberately differs from the required form; `gate-missing-input` omits exactly the `frontier.json` pin. Each of these five refused with return code 1, `NORMAL_EXIT`, the expected `RuntimeError` line in stderr, and no sentinel file. No missing-pin exception reached any mathematical operation: the eight mathematical authorities are complete.
- Single mathematical budget: all nine mathematical records share `first_math_epoch` 1788960573.8219447 and `hard_cutoff_epoch` 1788960900.0 (13:35 UTC, the smaller of the deadline and first-math + 360 s); every `returned_epoch` precedes it; the seven controls have null budget fields. Returns are strictly serial; each wall time is below its cap.
- Return codes/status: refusals 1/NORMAL_EXIT, valid 0, dummy 125/RESOURCE_CAP, eight mathematical 0/NORMAL_EXIT with `resource` and `error` null. `remaining_group_live` and `group_live_before_reap` are empty for all 16. The final audit's PGID list equals the 16 telemetry PGIDs in order with `live=[]`; poststate shows `stopped`, same volume and Owner tag.
- Caller identity: every `caller_stat` shows the recorded PID with parent/PGID/session 1851, namespace `pid:[4026531836]`, and telemetry `pid == pgid`, consistent with "no inner PGID by the caller; CAPRUN owns the leader group".

Honest reading of the null cleanup fields: on the 15 NORMAL_EXIT operations `cleanup_complete`, `reason`, `term_sent`, `kill_sent` and `leader_reaped` are null/false because no termination path ran. That is expected, and it is not evidence of cleanup capability; that capability is evidenced only by the dummy test in B. Nothing here is a cryptographic external attestation of the host; the host binding is the DMI/hostname check inside the gate plus root's SSH observations. RSS is sampled and may overshoot; CPU is a per-process limit; no strict scheduler bound is claimed.

## B. Actual same-caller refusal, sentinel and descendant controls. CONFIRMED.

These are the new v2 runtime results, not the prior dummy or metadata tests. The five refusals are as in A, each with a distinct gate line (20, 30, 43, 57, 67 of `execution_gate.py`) matching the mutation. `gate-valid` wrote `POSTAUTHORIZE\n` (sentinel SHA `6c6419e9…`), exit 0. The dummy descendant: probe forked a child that ignored TERM and allocated 64 MiB; stdout holds exactly two JSON lines with leader 1882, child 1884, PGID 1882, namespace `pid:[4026531836]`, and the child's stat shows PGID 1882 with SIGTERM in its ignored mask. Telemetry: `RESOURCE_CAP`/`rss`, cap 33,554,432, observed 77,922,304, runner exit 125; `identity_checks` is exactly the typed four-event sequence before-term MATCH, SENT 15, before-kill MATCH, SENT 9, with both MATCH events reporting PID 1882 = PGID 1882 and start identity `boot=e4ba2da1…;start_ticks=31611` equal to the telemetry's own; `term_sent`, `kill_sent`, `cleanup_complete`, `leader_reaped` all true, `group_zombies_before_reap=[1882]`, live empty. The caller's stricter post-conditions for this record (source lines in the `dummy-descendant` branch) are consistent with these bytes. The dummy's sentinel also exists (probe writes it before forking), which is expected.

## C. Checker modes bound to execution. CONFIRMED.

Each `check-<mode>` child argv is exactly checker, its authority, `exact.json`, its receipt path and the mode; each receipt carries the matching `authority_sha256`, `artifact_sha256` `168bdfd3…`, schema `F10-L1-CHECK/v1` and stdout `PASS-REPRESENTATION-NOT-IDEAL-DECISION`, stderr empty. From the receipts, copied not recomputed: full and u-zero both report 8 full bracket slots, 10 inverse-pole slots, 20 ideal slots, low rows checked; full B term counts `[112,54,23,7,3,1]`, u-zero `[70,32,15,5,2,1]`; u-zero retains a first slot of term count 0 and degree −1 rather than dropping it. Negative modes rejected the intended defect with the intended string: dropped-constant and u-zero-dropped-constant `full low bracket E0` (weakened upper-only check PASS, so the defect is caught only by the full low check, as designed); upper-coefficient `nonzero full upper bracket t3`; guard `guard restoration`; leading-top `saved leading coefficient restoration`. Artifact schema inspected: `F10-L1-EXACT/v1`, variables `u,ell,d0,d1,v0,v1,v2,k1,k2,k3,k4,omega`, 20 rows (E1/S0–S8, E0/S0–S9, guard `omega*a*b-1`), rational coefficients as numerator/denominator strings, no float token anywhere, and its `execution` block carries the build authority SHA `c9c8f7a6…`. Low residual reconstruction is a representation identity check, not vanishing at a point.

## D. Corrected precision. CONFIRMED at its stated narrow scope.

The precision child ran under authority `8280815d…` on the same artifact, and its receipt shows the guard precondition held, synthetic exact `-1208925819614629174706177` versus float-rounded `-1208925819614629174706176` (different, magnitude above 2^53), float payload rejected as `floating point anywhere in artifact`, canonical rounded string rejected as `full guard row`. Its stdout is empty by design. This is two mutated guard payloads. It is not generic positive large-coefficient parser fidelity and says nothing about the sizes of the actual coefficients.

## Pins (generated from sha256sum of the snapshot)

| File | SHA-256 |
|---|---|
| `f10-r1-engineering-v2-execution-astra-20260909.md` | `de36618ca8b68857f6a2b80e62604f0bd9245d9bfbd4a3aa66eebf06f3713ebd` |
| `f10-r1-engineering-v2-execution-astra-20260909.md.artifact.json` | `6975256408563fa54b113fbc07119aa23ccfd7a5365d328e287c11e300ba1186` |
| `READ-SCOPE.md` | `23d0d4b1273fb62a99a4d0d048be3b2c4f0c3fd1c545ed0d6f3ffedb8f604f49` |
| `REGISTRATION.md` | `636f043f76fca1a2feb6e666fd7bc3e2b59c5b643b97aef8fc36ce4751028be6` |
| `custody.json` | `b46ed4c7e0190b7b0f5d18fe36c7ecf90787ed23345c13439f8b1942e02622f4` |
| `final-process-audit.json` | `47095e1b57374dff22aa5b366a22f23d33561db3c49c2e9ead58e7d46efdbdad` |
| `instance-poststate.json` | `e51ad341091ad5525f0383693eadcfceb8fedcc228166b0859943948fbe54754` |
| `f10-r1-caller-v2-gate-fable5-20260909.md` | `0fa06c13eb330aef8e8ad489cb451922ad34f03708e2df82413b870a031b0c5d` |
| `f10-r1-complete-builder-gate-fable5-20260909.md` | `481d2a2edb12855cbdfa11f1cc1d0d15d7933b039896612827a683c3d70a09d7` |
| `dispatch_batch.py` | `aaafa62a7aa96ab7823e889c7d8800add04b9699a9e736ccdeb883557e812640` |
| `execution_gate.py` | `cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6` |
| `precision.py` | `56400dd32f4940a0e77b2da79e9b90792b51588d01f0f1a2fded30efebb0af90` |
| `builder.py` | `2dcba70d4f14080535c4a58f06bfd50ba4949148e819a6827ab9326828d314b8` |
| `checker.py` | `e2970c71774607e211ecc7e0f001a0dc02d02410e303ca58cf7c17ab77b9f545` |
| `run_capped.py` | `4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2` |
| `probe.py` | `02913a1caf8cb5ebe2ec7c404ede0247a1954baee3751af8b2645496f6b6e1a7` |
| `batch.PASS.json` | `cb811b3463b412a04d8d32c6a475499940c5fd9f531ebeec9035c7b8ca0ddd47` |
| `preflight.PASS.json` | `0dbaf6396999f8608e2c05392296b7e1e1f45f155439f93b663f60dc0140c0fb` |
| `exact.json` | `168bdfd3a791f24a6631de66ae4e71c3f209ee9eb0d21fc466f9aa802f5ad576` |
| `check-full.receipt.json` | `1b7502d6fda3bcd2c8b3f89b6adcdcae90f4d07f7403da5362438e9b143bf152` |
| `check-u-zero.receipt.json` | `0d6795cba18a81982a911575b04a3d78bba081fbafce1365c90b7b7004a5037e` |
| `precision.receipt.json` | `68ebfaceca487cf2b2f21df230e7eecd96543c3a273b470165be203ac010f953` |
| `dummy-descendant.telemetry.json` | `cda439a5e0bfc5c007c29c7340a81469aab7387df234ade28c112cdb210759da` |
| `build.authority.json` | `c9c8f7a6eb30f8776db23e091d49ab0fcae0a14b3b3dffa040efa9b6423e801f` |

## OPEN(S) RAISED

- NONE.

## COLLISIONS

- NONE — own-only raised-OPEN check over this body; no corpus scan.

<!-- BODY-END -->
