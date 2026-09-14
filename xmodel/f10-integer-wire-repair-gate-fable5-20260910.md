# f10 integer-wire repair gate (Fable 5.1, 2026-09-10) — FIRST hostile gate

Status: UNSEALED body. First write 04:41 UTC, sections filled 04:46 UTC, final own-only check 04:47 UTC. Hard stop 04:55:00 UTC (ROOT TERM), final two minutes reserved, never reset.
Charged inputs: 21 immutable snapshots in /tmp/jc2-lane.F4X5Qm/inputs. All 21 SHA-256 BEFORE bodies re-hashed locally at 04:41:01 UTC and matched the charge list exactly (copy in box/…/input-hashes-verified-0441Z.txt). Own targets verified absent before the first write.
Method: manual source/text reading, sha256sum, diff -u, sed/grep only. ZERO Python/CAS/import/AST/compile/fixture/test execution, no coefficient artifact, no network, no git, no live-file or other-lane reads. The retained API response was read as text with sed only; no JSON numeric conversion.
Premises, not re-hardened: accepted minimum-pivot gate 480a610a and qualified generic-runtime gate c706c364.

## A. Exact diff scope — CONFIRMED

I regenerated all five diffs myself from the frozen old/new snapshots (box/…/regenerated-diffs.txt). Exact content:

- solver.py (334 → 338 lines), two hunks. Hunk 1 inside generic_candidate, before `from algebra import …`: one comment line plus `sys.set_int_max_str_digits(0)` (new line 16). Hunk 2 inside main, after the installed-FLINT version/path/sha require and immediately before `certificate = candidate(data, flint)`: one comment plus the setter (new line 330).
- checker.py (177 → 179 lines), one hunk inside verify: comment word "pure function" → "function", one added comment, and the setter (new line 15) before `from fractions import Fraction`.
- generic_controls.py (425 → 425 lines): one literal, FROZEN['checker.py'] 122842e5… → bb4263e1….
- generic_dispatch_batch.py (336 → 336): three literals in `known` (generic_controls.py → 259990f7…, solver.py → 4e9bb9d2…, checker.py → bb4263e1…); plan literal ce193898 unchanged.
- actual_dispatch_batch.py (231 → 231): two literals in `known` (solver.py, checker.py).

Nothing else differs. The rational() spelling round-trip (solver 217–223), wire() string export (128–129), sole rref (207), pivot-form check (211–214), UNIT/SEPARATOR extraction, 26-slot/1638 witness packing (282–285), the checker's 217/1638 dimensions, canonical reduced-rational checks, guard product, and every caller cap/argv line are byte-identical outside these hunks. No hidden truncation, backend, algorithm or cap change exists in the charged bytes. Scope caveat: algebra.py was not a charged body; its unchanged pin 7d565299 is carried by both callers and FROZEN, so its content is a premise, not a re-read.

## B. Call order / process boundaries — CONFIRMED, one explicit limitation

- Import alone does not mutate policy: both setters in solver.py and the one in checker.py sit inside function bodies (indented, lines 16, 330, 15); module level only has `import sys`, dont_write_bytecode, sys.path and the authorize import.
- Actual solver order (solver 318–335): argc → authorize(build) → evidence.verified → producer_environment → `import flint` + version/path/sha requires → setter → candidate. candidate is where source-wire decimal parsing happens (Ring.read at line 302, modulus string compare at 295), so every actual int/str conversion is after the setter. generic_candidate's own setter (line 16) is then a harmless repeat and independently covers the direct authorized generic child.
- FLINT entry construction uses `flint.fmpq(c.numerator, c.denominator)` (line 180), integer arguments, no decimal conversion; the first decimal site on the extraction path is rational() (str at 217, int at 220), matching the observed stderr chain 243 → 218 in old numbering.
- Fresh checker: main (161–176) authorizes, evidence.verified, bound, binding/solver-pin requires, then verify. verify's first statement is the setter (15), before the Fraction import (16), int(a)/int(b) (25) and str round-trip (26). The checker imports neither solver nor FLINT.
- Pre-setter JSON loads: evidence.load (25–35) uses json.loads with parse_float/parse_constant forbidden and NO parse_int hook, so JSON integer literals are converted by the default int before any setter. That is safe only under the contract that all large values travel as string pairs (checker line 24 enforces str; solver wire() emits str). A giant JSON number literal would raise ValueError inside evidence.load, i.e. fail closed before verify. This is the explicit limit on the "unbounded malicious JSON service" question: not silently covered, but rejection not acceptance.
- Semantic controls (unchanged 238ae674): reject() calls checker.verify at line 44; the first invocation is omitted-high-coordinate (56), and verify sets policy at its first line even though it then rejects the dimension. The harness's own int()/str() conversions are at 68 (fifth control), 80 (SEPARATOR scaling) and 94 (UNIT +1), all after ≥4 verify calls; no finally/restore exists. json.dump/loads there handle string wires only.
- Generic harness (run_controls 272–374): fixture_table builds all eight fixtures from small Fractions (0, 1, 2, −1, e0 = product/720) before any candidate; freeze/parse_input on allzero-q0 converts only small strings; the first generic_candidate call (293) is on allzero-q0, so all later read-backs, DenseFixture verification, negative mutations (326–356) and candidate_refusal run after the setter in the same interpreter.
- Explicit limitation (agreeing with the Astra report §4): a fresh child that calls parse_input/read_fraction/DenseFixture.verify/fraction_wire on large strings BEFORE its first generic_candidate or checker.verify call runs at the default 4300 limit. This matters for E below.

## C. Binding closure — CONFIRMED

- The five "old" snapshots hash to exactly the ROOT-CARD's allowed accepted versions (961e22e6, 122842e5, c369dc11, e62e5dc4, ae3df9a9); semantic_controls 238ae674, evidence cbe5a9e0, plan ce193898, stderr 0d1d5617 and both gates match their charged pins.
- Chain: harness FROZEN carries the new checker; the generic caller's `known` carries the new harness, solver and checker with the plan literal unchanged; the actual caller's `known` carries only solver and checker. The harness never self-hashes (FROZEN lacks generic_controls.py and solver.py, lines 397–402); those two are bound by the authority spec's file_sha256 plus the caller `known` map, unchanged mechanism. Semantic controls bind the checker dynamically through the genuine result's checker_sha256 versus the sibling file (line 25).
- generic.plan.json is byte-identical (ce193898). The token `source_sha256` occurs in neither caller nor harness; the caller consumes only plan['positive_cases'] / ['negative_cases'] (lines 56–58, 304, 316) and the harness uses its own CASES/NEGATIVES constants. So both stale entries (harness c369dc11, solver 58cdc472) are documentary. The prior gate 480a610a already recorded the solver entry as non-consumed (its lines 23–24, 143–152); the harness entry now has the same status. Eight positives / four negatives unchanged.
- No synthetic acceptance: harness main still requires univariate_acceptance None (392–393); no new authority, argv, output path or reuse appears in any diff. Untouched supervisor code was not re-reviewed.

## D. Security / API — CONFIRMED with stated limits

- Retained doc text (python-api-response.json, rendered 3.12.14, lines 3123–3228 and 850–855): the limit is interpreter-wide, configured at startup by PYTHONINTMAXSTRDIGITS / -X int_max_str_digits or the 4300 default; the sys setter changes it for "this interpreter"; subinterpreters have their own limit; 0 disables it; affected APIs are int(str) base 10, str/repr/format of int. A separately exec'd /usr/bin/python3 -I -B child therefore starts at the default again; the claim that -I ignores PYTHON* env vars is the ROOT-CARD's statement and general interpreter behaviour, not inside the charged extract.
- The code calls the setter without the docs' hasattr guard: on an interpreter lacking it the child dies with AttributeError. That is fail-closed, not a silent fallback; acceptable for the registered interpreter.
- Trust change: the DoS guard is disabled (0), not raised to a finite value. Doc line 3126 states conversions are super-linear. The only containment left is the unchanged caps: CPU 550 s and wall 600 s (hard), RSS 2 GiB sampled (may overshoot between samples), aggregate wall and the 16 MiB file-size limit, plus immutable admitted inputs. None of these bounds coefficient height or promises completion; the 25.9 s observed wall was an exception exit, not a cap event or a runtime certificate. No performance claim is made here.

## E. Prospective large-rational identity — CONFIRMED math, GAP in the spec's ingestion path

- Hand check: mod T², f2 ≡ 1 + N·T and T·f2 ≡ T. Solving 1 = a(1 + N·T) + b·T gives a = 1, b = −N, so h2 = 1 − N·T. Then 1 − h2·f2 = N²T² − T³ + N·T⁴, divided by T²: h1 = N² − T + N·T². Expanding (N² − T + N·T²)T² + (1 − N·T)(1 + N·T + T³) cancels to 1. Matches PROSPECTIVE-CONTROL.md exactly; f1 = T² is the minimum-degree pivot (2 < 3).
- ACTUAL-schema representability: row envelopes [3,3,2,4,3,3,2,2,5] hold f1 (row 1, degree 2) and f2 (row 2, degree 3); zero rows are dense lists of empty coefficient wires (bparse of [] returns bzero); q = 1 as six dense slots, r = 1 (two slots), h0 = 1 (five slots) with tmul(r,h0) = q of length 6; q⁵ = 1 with 26 slots padded to 31. UNIT witness: 1638 string pairs with h1 at i=0 (j=0: N², j=1: −1, j=2: N) and h2 at i=1 (j=0: 1, j=1: −N), all others "0","1". N and N² = 10^14842 + 2·10^7421 + 1 are canonical spellings with denominator 1. So the checker can represent it. Mutation N² → N²+1 adds T² to total[2], all earlier need() checks still pass, and the failure is exactly the line-135 message `full 217-coordinate sum h_i f_i equals q^5`.
- Fresh checker: a separate child starts at the default guard and verify sets 0 at line 15 before its first int(); no solver state is used. Its fixture must carry the giant values as string wires, since evidence.load converts JSON number literals before verify (B above).
- Old first-failure site: OBSERVED only for the actual source (rational(), old line 218, after rref and pivot checks). For the prospective fixture it is predicted, not observed, at the same site because fmpq takes integer arguments; the spec correctly demands observation. GAP by design.
- SPEC defect (smallest actual defect found; code has none): the generic-path discriminator is silent about ingestion. If the future control feeds the fixture through the existing input_wire/parse_input/read_fraction path, int(N) runs before any generic_candidate call, so both old and new APIs fail at read_fraction and the old/new discrimination is void. The spec must require one of: construct N and the Fractions arithmetically and pass them straight to generic_candidate; or run one small generic_candidate first; or set the policy at the control's own authorized entry. This SPEC repair is needed before the regression.
- Cheapest sufficient regression (not authored here): one authorized generic child doing old-API fail (record site) then new-API UNIT certificate through DenseFixture, and one separate default-policy child calling new checker.verify on the padded ACTUAL-schema identity (pass) and the N²+1 mutation (exact message). No thirteenth plan case, no source acceptance.

## Verdict per section and smallest actual defect

- A CONFIRMED. B CONFIRMED with the explicit fresh-path limitation. C CONFIRMED. D CONFIRMED with stated limits. E CONFIRMED (identity, schema, mutation) with two GAPs: unobserved prospective failure site (by design) and the ingestion-path omission in PROSPECTIVE-CONTROL.md, which is the smallest actual defect and is spec-level, not code.
- No code defect found in the three setter placements or the pin propagation. No execution, promotion, launch or seal authority is exercised or implied.

## Collision scan (own / readscope / own-only)

New canonical OPEN IDs raised here: zero. This report and the box directory are the only writes; both were absent before the first write. Own-only scan of this body at the final write: no raised-OPEN heading, no exit-price basis line, no seal section.

<!-- BODY-END -->
