# Process-local decimal-integer wire repair

Status: NEW UNREVIEWED STATIC code repair. No code parsing, compilation,
import, arithmetic, fixture/test, candidate, checker result, runtime
registration, worker action or source decision was produced here.

First action: 2026-09-10T04:16:52.462553255Z; own report and box absent.
Controlling stop: 04:34:00 UTC (earlier than first+18 minutes), with final
two-minute reserve from04:32. Basis0d39df3c9fd69c939a8420c54d03228b9077777d
is provenance only. No clock reset or follow-on authority.

## 1. Exact result

Repair the decimal conversion policy in three authorized-child locations:

- solver.generic_candidate entry: sys.set_int_max_str_digits(0), before
  its mathematical import, native conversions, extraction and export;
- solver.main: the same setting AFTER its existing authority, input and
  installed-engine checks, immediately before candidate(data, flint),
  so the actual source-wire parser also runs under the intended policy;
- checker.verify entry: the same setting before its Fraction import and
  every independent rational-string conversion. The fresh checker does
  not inherit or assume the solver child's interpreter setting.

The policy intentionally persists for the rest of that interpreter's
life. This is needed for later exports and semantic mutations. No setter
runs merely from importing either module. The internal APIs retain their
existing contract: call them only inside a separately authorized child;
they do not themselves issue or independently recreate runtime authority.

Only necessary metadata follows: repaired checker SHA in the generic
harness's FROZEN mapping; repaired solver/checker/harness SHA literals in
the SEPARATE generic caller; repaired solver/checker SHA literals in the
SEPARATE actual caller. Root explicitly approved the two otherwise-missing
harness-pin propagation steps during this task. Caller logic is unchanged.

Semantic controls, evidence, algebra, old plan and all12 generic cases are
unchanged. No new fixture case or supervisor/schema/backend is introduced.
All canonical rational checks, full217/1638 verification, raw-generator
read-back, acceptance bindings and CPU/RSS/wall/aggregate/file caps remain.

## 2. Failure evidence and what it does not prove

All13 named local inputs were current-pinned before their WHOLE bodies.
The failure stderr SHA0d1d561744fa0a0bdfd1ac6ecd09889a3d0c05b838c841c0da21e44af118c530
shows the chain main -> candidate -> generic_candidate -> rational,
at old solver line243 and then line218:

    num = int(pieces[0])

It raises ValueError for a7422-digit decimal spelling against the4300
conversion guard. The referenced source was read WHOLE. This call site
is the UNIT-solution extraction loop after RREF and pivot-form checks;
the SEPARATOR branch has a different call site. Therefore it reached
that candidate-construction branch, but did not complete a raw identity,
certificate, independent checker, semantic controls or source decision.
It is not a solved-source theorem, even though the progress is useful.

Telemetry SHA2ff614da43971af59b73a4c2e4f32251bf548822206292ac30154de7457dbc6d
records NORMAL_EXIT with child and runner return1, resource null,
wall25.908244593 seconds, sampled group RSS271491072 bytes. Caps recorded
there are CPU550, wall600, RSS2147483648 bytes. It was not that run's
CPU/RSS/wall cap event. This repairs a specific observed conversion error,
not an inferred timing or coefficient-height bottleneck. No later stage
or completion-time prediction follows.

The ROOT-CARD's collection-only reboot, byte-identical recovered artifacts
and stopped-worker status are root-attested context. No AWS, process,
worker or independent operational check occurred in this task. Only the
charged secured stderr/telemetry were read as runtime payload evidence.
The two charged earlier gates license the prior minimum-pivot semantics
and qualified synthetic runtime scope, not this new code or actual result.

## 3. Primary API verification and security tradeoff

Official Python3.12 documentation describes an interpreter-wide limit
on decimal int/string conversions, including int(text) and str(integer).
The sys setter changes that interpreter's limit; zero disables it.
Subinterpreters have separate settings. These are API facts, not a claim
about the exact installed patch release. Sources: [sys setter](https://docs.python.org/3.12/library/sys.html#sys.set_int_max_str_digits)
and [integer conversion limits](https://docs.python.org/3.12/library/stdtypes.html#integer-string-conversion-length-limitation).
Selected rendered ranges and the exact retrieved response are retained
in python-api-response.json (SHA72c2e4a99c3ebbcd6a446e2cd608c8f4626cf9d0e5ee2d50dd060635505f8deb).
This snapshot is rendered tool output, not original HTML or a whole-page
read claim; READ-SCOPE.md specifies the ranges and retrieval interval.

This is a real security-policy relaxation: the decimal denial-of-service
size guard is removed within the authorized child, not merely increased
to7422. Decimal conversions can consume substantial CPU and memory.
The unchanged immutable-input admission, finite output-file bound and
existing CPU/RSS/wall/aggregate limits remain the resource containment;
they do not prove conversions cheap or guarantee timely completion.
Sampled RSS enforcement still has its inherited overshoot limitation.
An externally malicious/unbounded-input service must not casually reuse
these internal APIs. [Python's rationale and configuration](https://docs.python.org/3.12/library/stdtypes.html#integer-string-conversion-length-limitation).

No environment variable, -X option, global installation setting, backend
replacement or arbitrary new finite digit cutoff is used. The existing
-I -B argv remains. A fresh exec must set its own policy; it cannot rely
on the producer's interpreter state. Unsupported setter availability
fails rather than silently falling back; the registered interpreter is
expected to supply the documented API. No installation occurs.

## 4. Complete call-order audit

### Actual solver

main validates argc, calls unchanged authorize(operation=build), then
evidence.verified checks the pinned artifact, prior full receipt, external
ROOT acceptance and decision-source hashes. producer_environment checks
the registered engine metadata; the existing import/flint version, path
and hash checks follow. Only then does the new main setter precede
candidate. candidate's dense source parsing and its Ring.read calls thus
do not precede the policy. No algebra.py edit is necessary.

candidate calls generic_candidate, whose setter is idempotent on this
path and also covers the separate direct generic API. rational(value)
keeps its literal native spelling split, int conversions, positive
denominator and round-trip canonical spelling checks. The same policy
covers both UNIT and SEPARATOR extraction, CRT/raw reconstruction and
wire(c)'s decimal numerator/denominator export. The coefficient rings,
monic split logic, minimum pivot, sole RREF and all return dimensions
are byte-identical outside the two small setter/comment hunks.

### Fresh full checker

checker.main independently authorizes operation=check. evidence.verified
and bound load pinned JSON with rational numerator/denominator fields as
STRINGS, not converted integers. They check the candidate's input binding
and solver SHA before verify. The new setter at verify entry therefore
precedes its independent int(a), int(b), str(n), str(d) and gcd checks.
The checker does not import solver or FLINT or trust their rank/trace.

The altered setting neither accepts floats nor relaxes exact pair shapes,
canonical decimal spelling, reduced fractions, positive denominators,
row ordering, guard multiplication, all217 primal equations or all1638
dual pairings and normalization. Canonical strings may now be long;
malformed or mathematically wrong strings must still fail. The comment
calling verify a pure function was corrected to just function, because
this deliberate interpreter-policy side effect makes purity inaccurate.

### Actual semantic controls, unchanged

Its own main first authorizes and checks pinned input/acceptance/result,
including the genuine checker SHA against the sibling checker.py. It
imports checker and defines reject. The first actual reject invocation is
omitted-high-coordinate; it copies and writes existing string fields,
then enters checker.verify before any branch-specific large-int mutation.
The setter runs even though this verify subsequently rejects a dimension.
There is no finally restoring the old policy.

Next are missing-witness-slot, floating-witness, noncanonical-witness,
wrong-modulus, wrong-indexed-row and missing-guard-factor. Each calls
verify again. The wrong-modulus int/string operation itself is AFTER
four such calls. Only after all seven common controls does the branch
either scale every SEPARATOR rational, or add1 to a UNIT cofactor; both
int/str/Fraction mutation paths therefore run in that same configured
interpreter. The all-input-rows-zero UNIT case remains explicitly
inapplicable, with no invented nonzero row. All exact failure reasons,
eight-case accounting and post-hashes remain unchanged.

The preliminary evidence/json reads do not numerically parse witness
strings. This argument is for the exact charged ordering, not arbitrary
new standalone mutation calls. A future reordered control must retain
the policy-before-conversion requirement. No semantic source edit or
extra repeated positive verification is needed for this fixed program.

### Generic positive and negative paths

The generic main verifies execution_gate, authorizes operation=build,
checks evidence and the complete flat package pins, rejects source
acceptance, validates outputs/native engine, then imports generic_candidate.
Before the first call it creates/parses the unchanged allzero-q0 fixture,
whose numeric values are small. That first generic_candidate enters the
new setter even though the zero case does not need large arithmetic.

All subsequent input round-trips, eight complete DenseFixture checks,
large native candidate conversions/exports, the scaled-separator and
raw-unit-plus-one mutations, short-witness rejection and nonreduced
coefficient-modulus refusal therefore occur AFTER a setter in the same
authorized interpreter. No new cases are added and none are dropped.
The DenseFixture verifier remains independent Fraction arithmetic using
its supplied fixture modulus, not the actual-source checker or solver.

This coverage is for the exact existing run_controls order. It does not
claim an arbitrary fresh call to parse_input/read_fraction/DenseFixture
outside that sequence configures itself. The separate prospective large
regression explicitly requires its own authorized entry and fresh-checker
boundary; it is not executed or added to the frozen plan here.

## 5. Necessary literal dependency propagation

The original generic harness hard-pins checker122842e5 in FROZEN and
enforces it before importing the solver. Without updating that literal,
the repaired checker would be rejected. Root explicitly approved this
one harness substitution and its resulting generic-caller harness pin;
neither changes control logic. The exact resulting source hashes are:

- solver.py: 4e9bb9d28c60360b39629d059b42778744c7d43c5677b52fb8351e3405e4d3f4
- checker.py: bb4263e1149eb1ba03d2dc47f5db339df6b05829280730ccf6c8420e0bc07045
- generic_controls.py: 259990f7f226e0509a18f8a230f9bbc66b1241c2ab09f511fa4134110f6a1717
- generic_dispatch_batch.py: 8bfe8f620492ba2c6f5eaf5770590f8ea3627dda1bccc9a643d31945672f4c47
- actual_dispatch_batch.py: 8141a2fbfc58e3666d174c709aa3d0e6d74ba5863522c4cb40e20da123acef0f

The generic caller has THREE literal changes (solver, checker, harness).
The actual caller has TWO (solver, checker); no generic code was
transplanted. Every authority barrier, argv, operation order, receipt,
acceptance distinction, output path, cap, STOP/no-retry condition and
external registration requirement remains its respective original bytes.
Semantic controls' checker binding is dynamic and already correct once
the genuine result and registered sibling have the new checker SHA.
Evidence's decision-source pins are likewise dynamic, with frozen
algebra/source-acceptance constants unchanged.

generic.plan.json remains byte-identical atce193898. Its source_sha256
dictionary still documents the OLD harness c369dc11 and OLD solver58cdc472;
these are deliberately stale historical fields, not runtime admission
pins. The charged caller consumes only the ordered positive/negative case
inventories, while its known mapping and the harness's spec/file hashes
bind current runtime code. This repeats the prior accepted stale-plan
scope, now for both documentary entries. No plan-body mutation is hidden.

## 6. Controls and remaining evidence

PROSPECTIVE-CONTROL.md supplies one hand-derived large-rational RREF/raw
identity and a giant canonical-coefficient mutation that leaves residual
T^2. It specifies the old4300/newzero distinction, independent all217
checking, fresh checker entry, and exact semantic failure instead of a
digit-limit failure. The stated native-constructor/RREF coverage must be
observed, not assumed. It creates no number, fixture, script, certificate
or authority, adds no thirteenth case, and claims no PASS.

The original checks themselves remain the negative controls for canonical
forms: long strings do not authorize leading-zero spellings, float wires,
negative denominators, unreduced pairs, wrong guard/rows or missing slots.
The meaningful future giant mutation must fail the full identity, not
merely fail parsing. This distinguishes interoperability from validation.

No actual-source coefficient or candidate body was an input. No new code
was imported, parsed by AST, compiled, syntax-checked or executed, locally
or remotely. Only documentary reads, hashes, literal text diffs and the
existing artifact transaction tool ran. The exact old/new/diff objects
permit an independent first static gate; that gate and every subsequent
runtime control still remain unperformed here. No completion time, output
size, coefficient-height upper bound or success of the next run is claimed.

## 7. Publication and stop

input-pins.json contains all13 original paths/full current hashes/bytes;
READ-SCOPE.md records whole reads and the permitted selected API source.
Five old code snapshots match original bytes. All five exact text diffs
are regenerated and compared with their frozen copies; no scientific
execution is hidden in that comparison. The own report/specification and
all changed hunks were read before the unique completion marker; own-only
raised-OPEN/collision checks and expected-manifest verification complete
the normal transaction. Custody excludes itself and covers all other
owned outputs plus the current13 original pins.

New canonical OPEN IDs: zero. Remaining quantity is simply whether this
exact process-local policy and its pin chain pass first static review and
the separately registered large-decimal/fresh-checker controls. Cheapest
next evidence is that targeted code/interface review; no review or test is
launched here. All writers stop before terminal custody handoff; no
promotion, retry, cap change, execution or dependent task is authorized.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15368`.
- Body SHA-256:
  `1c452feb11d33dc0f498e05c975a51287092115c2dbac6df034fae47f1fdeb22`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
