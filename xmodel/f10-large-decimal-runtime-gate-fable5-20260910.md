# f10 giant-integer regression, FIRST Fable 5.1 RUNTIME gate (2026-09-10)

Status: UNSEALED body, no charge_basis, no Seal. First action 06:50:29 UTC: all 20 charged
snapshots in /tmp/jc2-lane.yZDBlI/inputs hashed BEFORE any body read, every SHA-256 equal to
the charge list (copy in box/f10-large-decimal-runtime-gate-fable5-20260910/input-hashes-verified-0650Z.txt).
Own targets checked absent 06:53:33, after hashing and before the only writes. Controlling stop
07:04:29 UTC (first+14 min, earlier than 07:06:00), final two minutes reserved from 07:02:29, never reset.
Method: cat/grep/cmp/sha256sum and jq restricted to structure, string length, regex and key
listing; no integer was converted, no Python/CAS/AST/compile/test ran; no network, AWS, SSH,
git, process, live-file, corpus or other-lane read.
Read scope: WHOLE for both ROOT reports, the static gate, helper, interface, addendum, the three
result summaries, both telemetry files and both fixture files. EXCERPTS by exact field for the
bundle, certificate and mutation (witness slot structure, lengths, regex, cmp after deleting slot 0),
both authorities (all non-pin fields, pin count, selected pins), ROOT-OBSERVATIONS (top keys,
first_dispatch, hard_math_cutoff, pids, groups, backup line, control tails, launch captures, stop
and copy outputs) and the final manifest (length, presence of each charged hash).
Premises, not re-hardened: accepted 17zu repair and 17zx static gate; oldsolver.py, solver.py,
checker.py, generic_controls.py, algebra.py, evidence.py and execution_gate.py are UNCHARGED here,
so every statement about their internals is a citation of the static gate or of retained runtime bytes.

## A. OLD failure site; NEW repair, unchanged versions, common fixture — CONFIRMED

- Old site is observed, not inferred: old.result.json retains sites main:216 (the generic_candidate
  call, after fixture construction at helper 206 and import at 209), oldsolver.generic_candidate:243
  with source text `solution[pivot] = rational(reduced[k, columns])`, and oldsolver.rational:218
  `int(pieces[0])`; message `value has 7422 digits`. That is post-RREF solution extraction, not
  import or fixture construction. entered 4300, final 0, helper_set_zero_only_after_old_failure true;
  helper 220-222 accept only the exact message with policy still 4300, and 228 sets zero afterwards.
- New entry repair: helper 143 and 212 require 4300 before the selected API; 234 requires 0 after,
  with no helper setter on that branch. new.result.json: entered 4300, final 0, status reachable only
  through the need() chain 234-255. Its stdout hash a06b354d equals my sha256 of the status string
  plus newline (34 bytes), exit 0, stderr empty (e3b0c442).
- Unchanged versions: helper be4de57f in both results, FROZEN and my charged hash; both authorities
  pin /usr/bin/python3 a92f0f95 and flint 0.9.0 module 2e5f8f17 and the seven FROZEN siblings with
  the FROZEN digests; descriptor c9f2e6b7 is input_sha256 of old and new and pinned in both authorities.
- Arithmetic-first N: helper 62 builds 10**7421+1 by integer arithmetic; the descriptor carries only
  N_exponent 7421 (helper 199-200). The fixture wire is created only at 262, after the API outcome.
- Common fixture: old and new fixture files both hash d371a534 and cmp reports byte equality (my own
  run); both results record fixture_sha256 d371a534. Fixture content: p monic 8 wires, q = [1],
  fs[0] = [0,0,1], fs[1] = [1,N,0,1] with N a 7422-character string, all other rows zero.
- Trace: splits 0, small_rows 14, small_columns 112, rref_calls 1, one leaf degree 2 pivot 0 whose
  modulus equals raw modulus divided by its trailing coefficient -924844032 (hand check of the first
  two entries: 741975/-924844032 = -247325/308281344 and -15127560/-924844032 = 30015/1835008).
- The 217/9/25 and ALL1638 statements are gated by need() at helper 249-250 and 255 in the executed,
  hash-matched helper. DenseFixture and read_fraction themselves are uncharged (premise).

## B. Cofactor identity, slot convention, bundle/candidate identity, wires — CONFIRMED

- Hand derivation: f1 = T^2, f2 = 1 + N T + T^3. Mod T^2, f2 = 1 + N T and (1 + N T)(1 - N T) = 1 - N^2 T^2,
  so h2 = 1 - N T. Then 1 - h2 f2 = N^2 T^2 - T^3 + N T^4 = T^2 (N^2 - T + N T^2), so h1 = N^2 - T + N T^2,
  h3..h9 = 0, q = 1. Sum: (N^2 - T + N T^2) T^2 + (1 - N T)(1 + N T + T^3) = 1 exactly.
- Slot convention from the certificate itself: column_order `input i=0..8 then multiplier j=0..25 then
  v-degree ell=0..6`, so slot = (26 i + j) 7 + ell; rows 217 = 31 x 7, columns 1638 = 9 x 26 x 7.
  h1 constant, T, T^2 are slots 0, 7, 14; h2 constant and T are 182, 189.
- Observed bundle witness: 1638 entries, exactly five not equal to ["0","1"]: slot 0 numerator 14843
  chars matching ^1 0{7420} 2 0{7420} 1$ (the decimal spelling of N^2), slot 7 = ["-1","1"], slot 14
  7422 chars matching ^1 0{7420} 1$ (N), slot 182 = ["1","1"], slot 189 7423 chars matching
  ^-1 0{7420} 1$ (-N); 1633 zero slots. Every denominator is "1". This is text/regex inspection only.
- Candidate identity: the certificate file, key-sorted, is byte-identical to bundle.certificate (cmp);
  keys are exactly branch, column_order, columns, construction_trace, row_order, rows, schema, status,
  witness; status CANDIDATE-ONLY; none of binding/execution/engine/solver_sha256/input_evidence.
- Retained envelopes: input schema F10-R1-NINE-UNIVARIATE/v1, variable T, nine rows with ids and
  degree bounds [3,3,2,4,3,3,2,2,5]; E1/S1 has only coefficient 2 = 1, E1/S2 has 0, 1, 3 = 1, N, 1
  (N as a 7422-char wire), all other rows empty lists; raw modulus 8 integer wires 741975 ... -924844032;
  guard q = 1 in six slots, r = 1 in two, h0 = 1 in five, exactly helper 81-94.
- Not independently replayed: checker.verify arithmetic, bparse, DenseFixture (uncharged sources).
  What is replayed: the symbolic identity, the slot map, and the byte-level artifacts above.

## C. Fresh-check input, isolation, entry setter, sole mutation — CONFIRMED

- INPUT: fresh authority operation check, large_decimal_mode fresh-check, child_argv[2] is the bundle
  path; 215 pins = the 213 of the new authority plus new.authority.json df20f1e9 and
  new.result.json.bundle.json c77596bd. fresh-check.result.json input_sha256 c77596bd equals my hash
  of the charged bundle. Registration after the new terminal/hash gate is stated by ROOT (06:41:06)
  and consistent with telemetry (new end 06:39:52.054, fresh start 06:41:34.449); the exact
  registration timestamp inside ROOT-OBSERVATIONS was not re-derived here.
- Isolation and setter: helper 163-165 require no solver/oldsolver/flint module and policy 4300
  immediately before checker.verify; 167 requires 0 after. Result: entered 4300, final 0; positive
  branch UNIT, 217 coordinates, 9 multipliers, degree bound 25; stdout hash 0815ea44 equals my sha256
  of the status string plus newline (44 bytes). The generic scope label in positive.scope is the
  checker wording, applied here to a synthetic bundle.
- Sole mutation: with witness slot 0 deleted, mutation and bundle normalise to identical bytes (cmp);
  slot 0 numerator is 14843 chars matching ^1 0{7420} 2 0{7420} 2$, i.e. N^2 + 1, denominator "1".
  Helper 184-186 freeze and re-read it before the negative verify.
- Residual by hand: (h1 + 1) f1 + h2 f2 = 1 + T^2, so the T^2 row of the full sum is 1, not 0, and the
  identity check fails while parsing succeeds (canonical spelling, denominator 1). Recorded reason is
  exactly `full 217-coordinate sum h_i f_i equals q^5`; helper 190 rejects any other message.
- No source-acceptance path: the helper contains no checker.main or evidence.verified call; both
  results carry source_acceptance null and synthetic_only true.

## D. Prospective envelope, clock, captures, controls, closure — CONFIRMED with declared GAPs

- Argv/caps: parent_argv wraps run_capped.py with wall 60, CPU 55, RSS 1073741824, sample 0.05,
  grace 0.25; child_argv has 8 items = telemetry argv_count 8 in both children; telemetry caps match;
  file_size_limit_bytes 16777216 and the helper checks RLIMIT_FSIZE (119-120). Absolute root cutoff
  06:56:00Z is in the authority.
- Clock: ROOT-OBSERVATIONS first_dispatch 06:39:51.587635700Z, hard_math_cutoff 06:43:51.587Z
  (rounded down). New ended 06:39:52.054, fresh ended 06:41:35.019, both more than 75 s before the
  aggregate cutoff and before 06:56:00.
- Same-call captures: the launch script polls /proc/PID/cmdline, ps and /proc/PID/stat in one script;
  observed lines show parent 6404 (stat field 22 = 26061) and child 6425 for new, parent 10559 (36341)
  and child 10580 for fresh; telemetry start_identity 26066 and 36346 on boot 7dd71b36. pids lists 19,
  groups 9.
- Controls: five refusals exit 1 with named RuntimeError (excerpted: no active registered authority;
  not the registered AWS host); valid control POSTAUTHORIZE; dummy RESOURCE_CAP with group RSS
  92516352 over 32 MiB, two identity MATCH lines, cleanup_complete true, leader_reaped true;
  ALL_CONTROLS_QUIET_213_MATCH 06:39:28.947 before math.
- Terminal quiet/copy-before-stop: `ALL 80 LOCAL FILES SHA/SIZE MATCH 2026-09-10T06:43:05.673Z`,
  then StoppingInstances, three instances stopped, backup canceled 06:43:37 after all stopped. Final
  manifest has 80 entries and contains each charged artifact hash once (results, bundle, certificate,
  mutation, fixture, telemetry, both authorities, helper, descriptor). The old result 4b2e9c35 is not
  in this manifest; it belongs to the earlier execution lane, and only the old fixture was pinned here.
- Recorded limitations, all present in the retained bytes and honestly labelled: normal-exit
  telemetry has cleanup_complete null and leader_reaped false with term_sent/kill_sent false; the valid
  unit tail shows MainPID=0, CPUUsageNSec not set, ActiveState inactive, empty InvocationID (unloaded
  accounting, no invented CPU total); the bash `read error: 0: No such device` sits in the gate-valid tail
  after exit 0; the first native inventory shows repeated `rg: command not found` and was rejected in
  favour of the second. No billing, CPU-total or root-authentication claim is made anywhere.
- GAPs (declared, not defects): native closure completeness (190 paths) is a ROOT declaration I cannot
  verify from the charge; the dummy control exercised TERM/KILL on a control unit, not on a math unit.
- Sufficiency: the synthetic regression (old failure site, repaired entry, byte-identical common
  fixture, hand-verified identity, fresh-process sole-coefficient negative, prospective caps and
  clock) is sufficient support for a FUTURE separately registered genuine-source retry under
  unchanged limits. This gate grants no launch, no source/unit/exclusion/JC2 claim, and no credit for
  the earlier missed new/fresh stage, which stays retained and unrerun.

## Verdict

A CONFIRMED. B CONFIRMED. C CONFIRMED. D CONFIRMED with the two declared GAPs above. No REFUTED item.

## Collision scan (own / own-only)

New canonical OPEN IDs raised here: zero. Writes: this report and the box directory only, both absent
at 06:53:33. Own-only scan at the final write: no raised-OPEN heading, no charge_basis line, no Seal.

<!-- BODY-END -->
