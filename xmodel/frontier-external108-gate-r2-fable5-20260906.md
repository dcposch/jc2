# Frontier external-108 overlay: independent different-model gate (r2)

Status: **COMPLETE**.  Reviewer: Fable 5.1 (different model
from the producer, Sol).  Lane start 2026-09-06T13:11Z, due 13:35Z.
Corrected input path: the charged control artifact is `control-matrix.tsv`
(the earlier r1 attempt charged a nonexistent `matrix.json` and never
launched; no mathematical failure occurred there).

## Frozen inputs and pins

All nine files in `/tmp/jc2-lane.jEsjZp/inputs` were read from that directory.
Hashes below were computed by this lane.  The seven that have a live
workspace counterpart (`ops/frontier_gate.py`, both test files,
`control-matrix.tsv`, Sol's report, the GGHV PDF and text) are byte-identical
to it.  The gate hash equals Sol's pinned value and the suite's
`EXPECTED_GATE_SHA256`; the PDF hash equals the gate constant
`EXTERNAL_SOURCE_PDF_SHA256` and the AUDIT17(jjjjjjjjjjjj) pin; the text hash
equals `EXPECTED_GGHV_TEXT_SHA256`.  Sol's `output-pins.sha256` verifies 5/5
from the repository root (its paths are root-relative).

| Frozen input | SHA-256 |
|---|---|
| `frontier-external108-overlay-sol56-20260906.md` | `b9d8cf676e29205e41dcfa206a0f0b0124adb4fc0de4e294b7e437c961d8c677` |
| `frontier_gate.py` | `18367153f8b89126c57557edf8e5c53dddf8475bd617aed47848072c29516812` |
| `test_frontier_gate.py` | `824beb607381333eaf475dcec94d30bfe339a7c3674568a099d7331218904b01` |
| `test_frontier_external108.py` | `cd146c616a71034cf9c4d473abf922b2a1ec251aaff58e8f1aa4ae0e483ccf0a` |
| `control-matrix.tsv` | `b9250389406b87670499bf03c49fdd6faa96bae54f57c7f53e1a30e6938d5f66` |
| `ggvh-2204.14178v1.pdf` | `ac18e80cc2391f204f73b908a6a6557eb1141d9fbb5ebdb9f6e0a22121db80bd` |
| `ggvh-2204.14178v1.txt` | `f3eca2a560b98784ec787104c8b9049ca44bc3dde4bacb38f121376736d02368` |
| `ideation-20260906T1210Z-synthesis.md` | `e2aa98d754101057ffdd818f35ddd35808cc6e2c79eeb5eed475472b76770cf2` |
| `FALLACY-v2.md` | `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` |

Output-pin check from root: 5/5 OK.

## Theorem interface

The frozen primary bound is GGHV arXiv:2204.14178v1 Theorem 2.1 (text lines
97-98): if `(P,Q)` is a counterexample to the plane Jacobian Conjecture then
either `max{deg P, deg Q} >= 125` or `(deg P, deg Q)` is `(72,108)` or
`(108,72)`.  Its robust, representative-independent consequence is
`max{deg P, deg Q} >= 108` for every counterexample.  The gate implements
exactly the contrapositive of that consequence and nothing more:

- `external_max_bound_excludes` (`ops/frontier_gate.py:47-50`) is the strict
  test `actual_max < 108`.  A registered scope every member of which has
  actual maximum total degree below 108 contains no counterexample; a scope
  admitting a member with maximum `>= 108` is only `INCONCLUSIVE`.
- Fixed pairs use `max(deg_P, deg_Q)` (line 123), so the order of the pair is
  irrelevant; the inclusive cap `D` is used directly as the maximum bound (line
  141), and `D < 108` excludes the whole scope while `D >= 108` does not.
- The sub-125 pair list is not implemented.  Fixed `(108,108)` therefore stays
  `INCONCLUSIVE` although the literal list omits it.  That is the correct
  fail-safe reading: the list classifies normalized representatives, and a
  `(72,108)` pair becomes `(108,108)` under target addition, exactly the
  limit recorded in AUDIT17(jjjjjjjjjjjj) and the 12:42Z COORDINATION
  paragraph.  No arbitrary-representative filter exists in the code.
- Partial-y registrations set `actual_max_degree = None` (line 154) and are
  typed `OUT_OF_SCOPE_ACTUAL_TOTAL_UNBOUNDED`; they never reach the bound.
- Laurent, weighted, normalized-representative and nonconstant-Jacobian
  `J=x^k` chart degrees have no CLI spelling (argparse refuses unknown
  options, checked below); the accepted options are documented as original
  polynomial actual total degrees (docstring lines 4-9) and the JSON records
  `declaration_verified_by_gate=false` and
  `transformed_chart_degrees_supported=false`.  The gate cannot detect a
  caller who mislabels such degrees; that remains an unverified caller
  assertion, as Sol's report states.

Scope statement.  The frozen GGHV text rephrases the conjecture for
`(P,Q)` in `K[x,y]` with `[P,Q]` a nonzero constant (line 33) and inherits
its field conventions from GGV [1] without restating them (line 91).  The
gate's "characteristic-zero field, nonzero constant Jacobian" ambient is the
promoted AUDIT17(jjjjjjjjjjjj) interface, not a wider claim.  Gate note, not a
replay: passing from a characteristic-zero `K` to its algebraic closure
preserves both degrees and the absence of a polynomial inverse (the inverse,
if it existed over the closure, is unique and hence Galois-invariant), so an
algebraically-closed hypothesis inside the imported chain would not narrow
the gate's scope.  The imported reduction and classification chain stays
externally trusted; this gate did not replay it and `trust.
external_chain_internally_replayed=false` is accurate.

No new exit-price assertion is made by Sol or by this review, so the
FALLACY-v2 `charge_basis` rule is not applicable; Sol's `completion.json`
records the same.

Theorem interface verdict: **CONFIRMED**.

## Executable behaviour

Legacy fields.  `theorem`, `source`, `verdict` and `reason` are computed from
`gcd_closed` alone (`ops/frontier_gate.py:113-166`); their strings and the
`registered_scope` object are the HEAD (`git show HEAD:ops/frontier_gate.py`)
strings unchanged.  For actual 99/66 the legacy verdict is
`NOT_CLOSED_BY_THIS_GATE` with reason `gcd(99,66)=33`, as required.  The one
deliberate legacy-semantic change is that the legacy exit code is discarded
(`_legacy_exit_code`, line 166) and the process status comes from
`overall_closed = gcd_closed or external_closed` (lines 232-233), so either
exclusion yields `REFUSE_CLASSICALLY_CLOSED` / status 3 for `purpose=frontier`
and `METHOD_CONTROL_ONLY` / status 0 only for an explicit `--purpose
method-control`.  `excluded_by` lists each excluding theorem separately.

Independent oracle.  `box/frontier-external108-gate-r2-fable5-20260906/oracle.py`
encodes hand-derived expectations (status, legacy verdict, conclusion,
overall verdict, `excluded_by`) for the 10 charged matrix rows plus 10 extra
rows, and runs any gate copy under the 30 s / 512 MiB caps.  The production
gate matches 20/20, and its first ten rows are byte-identical to Sol's
`control-matrix.tsv` (`diff` empty).  Extra rows and their observed results:

| Extra registration | status | legacy | external | overall |
|---|---|---|---|---|
| actual 107/107 (gcd 107) | 3 | not closed | excluded | refuse |
| actual 72/108 (reversed order) | 0 | not closed | inconclusive | not closed |
| actual 64/96 (gcd 32) | 3 | not closed | excluded | refuse |
| actual 100/125 (gcd 25) | 0 | not closed | inconclusive | not closed |
| cap 16 (smallest gcd-inconclusive cap) | 3 | not closed | excluded | refuse |
| cap 15 | 3 | refuse | excluded | refuse (both) |
| actual 16/16, method-control | 0 | not closed | excluded | method control |
| actual 1/1000 | 3 | refuse | inconclusive | refuse (gcd only) |
| partial-y 1/1, totals unbounded | 0 | not closed | out of scope | not closed |
| cap 108, method-control | 0 | not closed | inconclusive | not closed |

Malformed inputs (`malformed.sh`, 13 cases): a single degree, a fixed pair
with `--total-unbounded`, partial-y without `--total-unbounded`, cap plus
pair, non-integer and decimal degrees, missing `--tag`, the unknown option
`--laurent-degrees`, cap 0, degree 0, an unknown purpose, a negative cap and
no arguments all exit 2 with empty stdout and an argparse usage diagnostic.
The positive-integer check keeps the prior message text.

Non-faults noted: `parser().error` builds a second parser (harmless);
the partial-y `scope` carries `registered_actual_max_total_degree: null`,
which the suite asserts.  No fault was found.

Executable behaviour verdict: **CONFIRMED**.

## Compatibility and consumers

A repository-wide search for invocations, imports and output readers of the
gate found:

- `ops/test_frontier_gate.py`: parses the JSON and checks only `verdict` and
  status on four legacy cases; unchanged and passing.
- `box/full-j-solver-pilot-20260906/harvest.py` and its `evidence/` twin:
  `subprocess.check_output` on a worker-local copy of the gate whose hash
  (`d709794d…`) is the legacy HEAD gate, called with actual 99/66 and
  `--purpose frontier`; stdout is written to `frontier.json` unparsed.  If the
  new gate were substituted, status 3 raises `CalledProcessError` and the
  harvest aborts.  That is fail-closed, the requested behaviour for a
  frontier registration; a method-validation replay must switch purpose.  The
  frozen evidence is untouched.
- `REGISTRATION.md` files of three pilots and several ideation reports quote
  the command or the legacy verdict as archived prose; no machine reader.
- `COORDINATION.md`: the older gate paragraph (lines 441-450) says a
  `REFUSE_CLASSICALLY_CLOSED` verdict blocks compute and `NOT_CLOSED` means one
  theorem is inconclusive.  The 12:42Z overlay paragraph (lines 452-464)
  already states that the legacy verdict is gcd-only and `overall_verdict`
  combines both bounds, so the canonical human-facing text is consistent with
  the code.  No Python import of the module and no parser of
  `registered_scope` or saved `frontier.json` exists.

Precise compatibility scope: the JSON change is purely additive; every legacy
key keeps its value for every input; the only behavioural change for an
existing caller is the process status 3 and `overall_verdict` refusal on
frontier registrations with `gcd >= 16` and declared actual maximum below 108
(actual 99/66, caps 16 through 107, and the like).  The unsafe pattern would
be a consumer that reads `verdict` alone and ignores both status and
`overall_verdict`; no such consumer exists in the repository.  Sol's
compatibility claim is accurate at this scope.

Compatibility verdict: **CONFIRMED**.

## Tests and independent controls

Own suite run (root's 0.78 s replay is not counted):

```text
timeout 30s prlimit --as=536870912 -- python3 -m unittest -v ops.test_frontier_gate ops.test_frontier_external108
Ran 14 tests in 0.745s  OK   elapsed=0.80 s  maxrss=20724 KiB
python3 -m py_compile ...  ok      git diff --check ops/frontier_gate.py  ok
```

Old-pass/new-fail control.  The legacy HEAD gate, extracted to scratch,
reproduces the four legacy-semantics cases (status and `verdict`) exactly and
fails all 20 oracle rows: actual 99/66 returns status 0 and no external keys.
The new behaviour is therefore a genuine change that the new suite captures.

Scratch mutants (each a one-token edit of a scratch copy; the production hash
was unchanged afterwards):

| Mutant | Detected by rows |
|---|---|
| drop the gcd side of `overall_closed` | 108/107, 1/1000 |
| drop the external side | 99/66, cap 107, both method-control rows, 107/107, 64/96, cap 16 |
| `min` for `max` on fixed pairs | 108/72, 72/108, 100/125, 108/107, 1/1000 |
| constant 108 to 109 | 108/72, 108/108, cap 108 (both purposes), 108/107, 72/108 |
| constant 108 to 107 | cap 107, 107/107 |
| `<` to `<=` (Sol's mutant) | same six rows as the 109 constant |
| partial-y treated as actual maximum (Sol's mutant) | both partial-y rows |
| exit status taken from the legacy verdict while JSON shows refusal | 99/66, cap 107, 107/107, 64/96, cap 16 (status only) |
| cap used as `cap + 1` | cap 107 only |
| purpose ignored | both method-control rows |

Every mutant is rejected.  Two observations: the exit-status mutant is
caught only because the suite asserts status, which it does; the `cap + 1`
mutant is caught by the cap-107 case alone, so that test is load-bearing.

Test-file review.  `test_frontier_external108.py` covers the required pairs
99/66, 108/72, 108/108 and 108/107, caps 107 versus 108, partial-y with
unbounded totals, method-control, legacy gcd cases, nonpositive inputs, the
implementation and source pins, and two temporary-file mutants with a fixed
three-case oracle.  Assertions are exact-value, not substring-only, except
two deliberate `assertIn` reason checks.  The hash pin means any later edit
of the gate, including the eventual flip of `TOOL_REVIEW_STATUS` after
integration, must update `EXPECTED_GATE_SHA256` in the same change; that is
expected maintenance, not a fault.

Portability limit.  `box/ideation-20260906T1210Z/` (PDF and text) and
`ops/test_frontier_external108.py` itself are untracked, and the pin test
hard-codes root-relative paths.  In a scratch copy of `ops/` lacking those
files, the pin test errors with `FileNotFoundError` while the other nine
external tests pass.  The suite is workspace-specific, as Sol states.

Tests verdict: **CONFIRMED**.

## Verdicts

| Aspect | Verdict |
|---|---|
| Theorem interface | CONFIRMED |
| Executable behaviour | CONFIRMED |
| Compatibility | CONFIRMED (scope stated above) |
| Tests | CONFIRMED (workspace-specific) |

No REFUTED finding.  No GAP that blocks integration.  No OPEN item: the only
unverifiable element is the caller's degree declaration, which the tool
already records as unverified by design.  No specific fault was found, so no
hardening is requested and no corrective action is taken; the single
integration note is the hash-pin update that must accompany any status flip.

`INCONCLUSIVE_BY_EXTERNAL_MAX_BOUND` and `NOT_CLOSED_BY_THIS_GATE` are not
openness, properness, or a check against all literature; they mean only that
the two implemented theorems do not exclude the registered scope.  This
review leaves `UNREVIEWED_PENDING_DIFFERENT_MODEL_GATE` and
`manual_external_check_required=true` unchanged in the code and its output;
whether this different-model gate discharges them is root's integration
decision.  No tool, test, canonical file or other author's artifact was
edited; the only writes are this report and the scratch directory
`box/frontier-external108-gate-r2-fable5-20260906/`.

## Handshake

```text
tag=frontier-external108-gate-r2-fable5-20260906
status=COMPLETE
reviewer_model=fable5
producer=sol56
lane_start_utc=2026-09-06T13:11Z
lane_end_utc=2026-09-06T13:19Z
frozen_inputs_verified=9/9
producer_output_pins_verified=5/5
own_suite=14/14_PASS_0.80s_20724KiB
old_pass_new_fail_control=legacy_HEAD_gate_fails_20/20_oracle_rows
scratch_mutants_rejected=10/10
extra_oracle_rows=10_all_match
malformed_cases=13_all_status2_empty_stdout
theorem_interface=CONFIRMED
executable_behaviour=CONFIRMED
compatibility=CONFIRMED
tests=CONFIRMED
refuted=0 gap=0 open=0 corrective_actions=0
review_status_flag_unchanged=UNREVIEWED_PENDING_DIFFERENT_MODEL_GATE
manual_external_check_required=true
charge_basis=NOT_APPLICABLE_NO_EXIT_PRICE_ASSERTION
tools_tests_canonical_edited=false
owned_live_writers=0
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14811`.
- Body SHA-256:
  `f802fb37d9483458d83ddcc898963c8bd33764982fa572f47e4fbbaf7e4105a6`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
