# f10 actual source-derived UNIT certificate, FIRST Fable 5.1 RUNTIME gate (2026-09-10)

Status: UNSEALED body, no charge_basis, no Seal. First action 07:20:39 UTC: all 29 charged snapshots in
/tmp/jc2-lane.CaZg0g/inputs hashed BEFORE any body read; every SHA-256 equals the charge list (sha256sum
output banked in box/f10-integer-wire-actual-gate-fable5-20260910/input-hashes-verified-0720Z.txt). Own
targets checked absent at 07:20:39 before the first write. Controlling stop 07:34:39 UTC (first+14 min,
earlier than 07:37:00), final two minutes reserved from 07:32:39, never reset.
Method: cat/grep/cmp/sha256sum/wc and jq restricted to keys, string lengths, prefixes, field selection and
byte comparison; no integer was converted or computed; no Python/CAS/AST/compile/test/network/AWS/SSH/
git/proc/live-file/other-lane read. This harness has no apply_patch tool; writes were bash heredocs,
append-only, skeleton first, marker last.
Read WHOLE: ROOT report, dispatch_batch.py, checker.py, semantic_controls.py, evidence.py, execution_gate.py,
ROOT-UNIVARIATE-ACCEPTANCE, univariate.full.receipt, decision.receipt, controls.receipt, batch.PASS, the four
telemetries, and the five accepted gates (17zu repair, 17zzc giant-integer runtime, 17m linear decision,
17l cover, 17x runtime evidence). EXCERPTS by exact field: dispatch.registration (all scalar keys, profiles,
task-file pins, pin counts), the three authorities (all non-pin fields, parent/child argv, pin-set diff
against the registration), candidate.json (every key except witness/construction_trace; witness length;
slot 0 string lengths and 60-char prefixes), fixture-wrong-primal-identity.json (keys, witness length,
slot 0, jq-normalised cmp of input against univariate.json and of certificate-minus-slot-0 against the
candidate), univariate.json (schema/variable/ring/guard/row ids/bounds/nonemptiness/modulus wires),
ROOT-OBSERVATIONS (key census, native counts, pid/group counts, first SSH failure, terminal check, stop
confirmation) and FINAL-REMOTE-MANIFEST (entry shape, count, presence of thirteen charged digests).
ROOT-only (not read here): witness coefficients, construction_trace beyond the one line quoted by ROOT, the
ROOT-OBS staging/launch/copy/local-verify blobs, manifest entries other than the thirteen greps.
Premises, not re-hardened: accepted 17zu, 17zzc, static supervisor, 17m, 17l, 17x; solver.py, algebra.py,
run_capped.py and probe.py are UNCHARGED and their internals are cited from those gates only.

## A. Prospective registration, bindings, authorities, clock, closure — CONFIRMED with three ROOT-only qualifications

- Registration 327b136f (my hash): schema F10-LINEAR-DISPATCH/v1, enabled true, job_tag
  f10-integer-wire-actual-20260910, instance i-08d2a40f272ee9fa2, host ip-172-30-0-72, cwd
  /home/ubuntu/jc2-f10-integer-wire-actual-20260910, deadlines 2026-09-10T07:38:00+00:00 and 07:40:00+00:00,
  aggregate_wall_seconds 1200, file cap 16777216, exclusive writer true, five exact profiles (probe 5/3/2 GiB,
  dummy 5/3/33554432, solve 600/550/2 GiB, check 180/170/2 GiB, controls 300/280/2 GiB). file_sha256 has 176
  entries = 14 task files + /usr/bin/python3 a92f0f95 + 161 python_flint_files; solve authority carries 177
  (the registration added), full-check 178 (candidate 6ab9f811 added), semantic 179 (decision 74c8af95 added);
  every other pin byte-identical across the four (jq -S diff). Task pins: solver 4e9bb9d2, checker bb4263e1,
  evidence cbe5a9e0, execution_gate cbfe55ff, dispatch_batch 8141a2fb, semantic_controls 238ae674, run_capped
  4435279d, probe 02913a1c, admissibility 02952e1b, frontier f9d1fddc, univariate 3cfec9aa, receipt 0c22af83,
  acceptance 90dcf4f3. The five charged code files and the three inputs hash to exactly these pins; the
  caller's `known` map (dispatch_batch.py:165-181) carries the same literals, and the acceptance payload in the
  registration equals ROOT-UNIVARIATE-ACCEPTANCE.json fields (schema, status, four version digests, five
  input_evidence digests, original 168bdfd3, normalized e62734b0).
- 17zu binding: 17zu names solver 4e9bb9d2 and checker bb4263e1 explicitly; the actual caller is named there
  only as "actual_dispatch_batch.py (231 -> 231): two literals in known". The charged dispatch_batch.py has
  231 lines and those two literals, but the digest 8141a2fb appears in no charged accepted gate; its
  "accepted immutable bytes" status rests on the ROOT card 6bdabf0e (uncharged). QUALIFICATION, not a defect.
- Authorities: operations build/check/check; caps 600/550, 180/170, 300/280 with 2147483648 RSS, sample
  0.05, grace 0.25; child_argv is exactly python3 -I -B script authority univariate receipt acceptance
  [candidate [decision [controls]]] with 9/10/11 elements = telemetry argv_count 9/10/11; parent_argv is
  exactly the execution_gate.py:277-286 required CAPRUN form (verified field by field). Telemetries: pids
  5212/24437/26995, start_ticks 12342/15290/15677 on boot 745dc9ea, NORMAL_EXIT, child rc 0, stderr 0 bytes,
  walls 29.353700488/3.739784194/5.529555619, peak RSS 261324800/27058176/27836416, utc windows
  07:11:44.385023-07:12:13.738716, 07:12:13.862372-07:12:17.602148, 07:12:17.727819-07:12:23.257363. All equal
  the ROOT figures. Normal-exit termination fields are null/false (no TERM/KILL), as ROOT states.
- Clock: batch first_math_epoch 1789024304.3355496, the three math records store hard_cutoff
  1789025504.3355496 = first+1200 (07:31:44.34 UTC) and the seven controls store 1789025880.0 = the 07:38:00
  math deadline; every returned_epoch precedes its cutoff (last 1789024343.2709136); batch end
  07:12:23.331406. dispatch_batch.py:46/51 admits each child only if now+wall+15 < cutoff.
- Controls: refusals 4102/4232/4362/4490/4620 rc 1, valid 4752 rc 0, dummy 4883 rc 125; dummy telemetry
  RESOURCE_CAP rss, peak 85987328 > 33554432, identity sequence MATCH/SENT 15/MATCH/SENT 9 on pid=pgid 4908
  start 12291, cleanup_complete true, leader_reaped true, wall 0.394335993. Descendant 4964 and the refusal
  telemetry pids (e.g. 4126) are present in the ROOT-OBS pid list (22 pids, 11 groups) but their stdout,
  authorities and telemetries are uncharged: observed here only through batch records and ROOT-OBS.
- Native: ROOT-OBS native_file_count 190, native_canonical_count 161, previous mismatches 0; registration
  python_flint_files has 161 entries; module 2e5f8f17 pinned in registration, all three authorities and the
  candidate engine field. Completeness of the closure is ROOT's declaration, bounded exactly as ROOT says.
- First SSH attempt: retained output "set: pipefail\ntest: invalid option name", exit 2, i.e. a shell
  `set` failure; that it preceded authentication is ROOT-only (consistent with the text, not provable from
  the excerpt). Terminal: TERMINAL_CHECK 07:13:55.984237327Z with MainPID=0, Result=success,
  ExecMainStatus=0, MemoryPeak/CPUUsageNSec not set, ActiveState inactive: matches the unloaded-accounting
  qualification, no final CPU total invented. Stop confirmation retains all three instances "stopped" with
  exit_code 1; the is-active 4-versus-3 explanation of that 1 is ROOT-only.
- Manifest: 106 entries of {name, sha256, bytes}; the eight fixture digests, candidate, decision, controls,
  batch and registration digests each occur exactly once. Local 106-hash verification is ROOT's record.

## B. Separate actual checker.main, full identity, guard identity — CONFIRMED

- Code path (checker.py:161-176): argv 7, authorize(check) with the full-check authority, evidence.verified
  on input/receipt/acceptance, bound(candidate) against the pinned 6ab9f811, binding equality, solver_sha256
  equal to the authority's solver.py pin (candidate carries 4e9bb9d2), then verify. verify reads only
  schema/rows/columns/row_order/column_order/branch/witness of the certificate; construction_trace, engine,
  status and any rank/pivot/split field are never read (lines 113-135), so the trace is diagnostic only.
- Modulus: p is recomputed from L,R,E (42-46) and compared literally against all eight wires (47-49); its
  leading coefficient 49*(-512)*192^2 = -924844032 by hand (192^2=36864, *512=18874368, *49=924844032)
  equals modulus[7] "-924844032" in univariate.json, and the trace leaf modulus -247325/308281344 is
  741975/-924844032 reduced by 3. Guard: factors r,h0 required and tmul(r,h0)==q checked directly (100-107).
  Target q^5 is 26 dense slots padded to 31 (108-112). Witness: 1638 canonical reduced string pairs (125).
  UNIT branch reconstructs h_i from slots (26i+j)7+ell for all nine i and 26 j, multiplies in the entire
  degree-7 algebra (bmul reduces by the monic p), and requires total==target on all 31 T-slots x 7
  v-coordinates = 217 (126-135). 1638 = 9*26*7, 217 = 31*7. All nine rows are nonempty in univariate.json,
  so the identity is non-vacuous.
- Receipt reconciliation: decision.receipt status VERIFIED-GENERIC-ZERO-QUOTIENT, checked_coordinates 217,
  multipliers 9, degree bound 25, certificate_sha256 = candidate hash 6ab9f811, checker_sha256 bb4263e1 =
  my hash of checker.py, execution.authority 2ab3307e = my hash of full-check.authority.json, binding equal
  to candidate/controls/batch bindings. full-check stdout 31 bytes with sha256 4eed574f: I reproduced that
  digest from the string VERIFIED-GENERIC-ZERO-QUOTIENT plus newline (banked in the box). Candidate
  1628285 bytes = my wc, status CANDIDATE-ONLY, engine 0.9.0/2e5f8f17, execution authority ffa87d9f.
- Guard identity by hand: xi^5 sum h_i f_i = xi^5 q^5 = (xi q)^5, and (xi q - 1) sum_{j=0..4} (xi q)^j
  telescopes to (xi q)^5 - 1; the difference is exactly 1, over any commutative ring, so 1 lies in
  (f_1..f_9, xi q - 1) with explicit cofactors. Matches the receipt's cofactor_contract string.
- No local coefficient replay: I inspected fields, lengths and prefixes only; the 217-coordinate arithmetic
  is the retained AWS checker's, exactly as ROOT states.

## C. Eight retained corruption tests — CONFIRMED; seven fixtures are manifest evidence only

- controls.receipt: eight cases, all EXPECTED-REJECTION, entrypoint checker.verify IN-PROCESS; reasons are
  the exact need() strings at checker.py:115, 124, 24, 27, 49, 98, 103, 135, produced by harness mutations
  at semantic_controls.py:55, 58, 61, 64, 67, 71, 74, 91-96; the harness requires type ValueError and the
  exact message (46) and rejects acceptance (49). harness_sha256 238ae674 = my hash; genuine_result 74c8af95,
  certificate 6ab9f811, authority fceb20d7 all equal my hashes; stdout 49 bytes sha256 15ab36fa reproduced
  from FINITE LINEAR CONTROLS COMPLETE; NO NEW DECISION plus newline.
- Independent positive prerequisite: lines 16-25 require the genuine decision receipt bound to the same
  binding, certificate hash and checker hash with status VERIFIED-GENERIC-ZERO-QUOTIENT before any mutation;
  no positive verify is rerun (27-53).
- Wrong-primal fixture ecf595e2, 1701031 bytes (my hash and wc, equal to the receipt and manifest): input
  is byte-equal to univariate.json after jq normalisation; certificate equals the candidate except witness
  slot 0; index = first row with a nonempty wire = row 0 (E1/S1), position 0 (line 92). Slot 0: denominators
  identical (7541 chars, cmp equal); candidate numerator 7422 chars, positive; fixture numerator 7541 chars
  whose first 60 digits equal the denominator's first 60 digits, exactly the shape of n+d with 0<n<d, and
  reduced since gcd(n+d,d)=gcd(n,d)=1. So every parse check passes and verify fails only at line 135: the
  change adds the nonzero row f_0 to the sum. A real identity rejection, not conversion/type/inapplicable.
- The other seven fixtures are charged only as receipt hashes/sizes (1700912, 1700902, 1693491, 1685952,
  1700912, 1700912, 1700907 bytes) present once each in the manifest, produced by the accepted executed
  harness; not body-reviewed here.

## D. Conditional composition 17m + 17x + 17l — CONFIRMED for the exact normalized family only

- 17m section C: the UNIT form is valid over ANY commutative B (c in Q^1638 solving the 217-window gives
  sum h_i f_i = q^5 in B[T], hence q^5 in I, hence B[T,q^-1]/I = 0); the etale/rank-7 hypothesis is needed
  only for the SEPARATOR direction. 17m's constants bind deg f_i <= 5 and deg q <= 5; the accepted receipt
  records actual_degrees [3,3,2,4,3,3,2,2,5] and guard degree 5, inside those bounds, and the checker's
  217x1638 window is 17m's. 17x accepted 3cfec9aa as the actual input representation (engineering only).
  Composition: R_uni = B[T, q^-1]/(nine rows) = 0 EXACTLY, conditional on the runtime custody of A-C, on
  the checker's hard-coded p being 17b's p (17p/17x adapter premise) and on the nine rows and guard being
  the faithful transport of 17l's rows (17x's U-slot and COVER premises).
- 17l sections C-D: Rcov = R_uni[x]/(x^3 - h0^2/r^7) is free of rank 3, faithfully flat, and isomorphic to
  the parent (17)-form normalized ring; R_uni = 0 iff Rcov = 0 iff the parent guarded ideal is the unit
  ideal. Hence the COMPLETE normalized 17j guarded ring is zero, not one coefficient field or a slice,
  conditional on 17l's own condition (parent composition d91b3e38, identification of the Lambda[Y1,Y2]
  presentation with the (17)-form).
- Discarded-component check: x=0 is forced empty on the guarded system (Phi3 = x(ax^2+by) = -cz with c a
  unit by 17l B and z a unit by the parent guard), not discarded; b=0 is allowed (only c is inverted);
  q = r*h0 with r <-> z and h0 <-> H0, both unit conditions of the parent guard (17) itself, so q=0
  components are outside the normalized ring by its definition, and 17m handles them as R_alpha = 0 in any
  case. Nothing inside the normalized ring is dropped. Source strata with z = 0 or H0 = 0 lie outside the
  normalized ring and remain the omitted strata ROOT names.
- What this is NOT: JC2; all-rF10; a global degree classification; an explicit cofactor in the original
  source variables (the cofactors live in B[T,xi]; transport through the chart and cubic cover is not
  executed). The 16q classical chain (112/196, U 28/49, V 84/147, admissibility 02952e1b, frontier
  f9d1fddc) is uncharged and remains an external upstream premise, not re-proved here.

## Verdict, smallest defects, remedies

A CONFIRMED (ROOT-only: pre-authentication timing of the SSH failure, is-active rc explanation, native
closure completeness, local 106-hash verification). B CONFIRMED. C CONFIRMED (seven fixtures hash-only).
D CONFIRMED as a conditional composition for the exact normalized 17j family. No REFUTED item.
Defects: (1) the actual caller digest 8141a2fb is not named in any charged accepted gate; remedy: cite the
ROOT card line that pins it, or charge the card. (2) Refusal-side authorities/telemetries, gate-valid
sentinel, dummy and solve stdout are uncharged; remedy: charge them in any later re-review. (3) Inherited
from 17x: no coefficient bit-length field; non-blocking. No code defect found in the charged bytes.

## OPEN(S) RAISED

None. No exit-price assertion; no charge_basis line.

## COLLISIONS

status: EMPTY

- NONE — own-only check: this report and box/f10-integer-wire-actual-gate-fable5-20260910/ (two banked
  text files) are the only writes; both absent at 07:20:39. No corpus scan.

<!-- BODY-END -->
