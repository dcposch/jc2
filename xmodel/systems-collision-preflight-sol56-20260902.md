# OPEN-collision hook and realization PREFLIGHT hard gate

**Lane:** `systems-collision-preflight-sol56-20260902`  
**Status:** IMPLEMENTED / FOCUSED TESTS PASS  
**Scope:** implementation and regression controls only; no mathematical claim,
promotion, canonical-ledger edit, or solver verdict.

## 0. Frozen-input gate and write boundary

Before reading the charged designs, SHA-256 was recomputed over the three
frozen copies.  All values matched the charge exactly:

```text
e67b2cd027e0cdbfc249d057d929e72a3e553ca61256f48b9978bedda358e9ce  inputs/ideation-20260902T0741Z-opus5.md
717134c733adc17b3b70409b018858fb1311c37608a24f0eebe65ae79aec8b11  inputs/ideation-20260902T0741Z-sol56.md
4408cfff1eb99c4f12a81c8d1b46906df260dc790ca357240dfd4567f08d140d  inputs/ideation-20260902T0741Z-synthesis.md
```

Here `inputs/` abbreviates the frozen lane directory
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.Ng2gjj/inputs/`.
The implementation follows the collision card at frozen Opus lines 519--535,
the hard-gate specification at frozen Sol lines 408--439, and the corrected
incidence/control specification in
`xmodel/encoding-faithfulness-audit-r2-sol56-20260901.md:462-511`.

Writes are bounded to the four requested implementation/test files and this
report.  `ops/lane.sh`, `ops/seal.py`, `ops/artifact_finalize.py`, canonical
ledgers, and other running-lane artifacts were not modified.  The excluded
tree was not inspected.

## 1. Typed deliverable A -- OPEN/banked collision check

```text
deliverable       = OPEN_BANKED_COLLISION_CHECK
implementation    = ops/open_collision.py
focused_tests     = ops/test_open_collision.py
status             = PASS
tests_run          = python3 -m unittest -v ops/test_open_collision.py
pass_fail_skip     = 11 passed / 0 failed / 0 errors / 0 skipped
optimized_run      = 11 passed / 0 failed under python3 -O
runtime            = 0.47 s focused; every individual test < 10 s
integration_note   = Section 1.4
```

### 1.1 Input and extraction contract

`open_collision.py` is pure Python and imports only the standard library.  It
takes an unsealed report and repository root.  It recognizes explicit,
anchored raised/opened headings, list entries, bold entries, heading entries,
and the narrow inline form `THIS REPORT RAISES: OPEN[...]`.  Multiple tokens on
one declared line are all retained.  Prose that merely discusses previously
raised items does not activate extraction.  Broken bracket syntax inside an
active section is an error, not an empty result.

Each extracted token must carry an explicit bounded-quantity description.  A
word such as `BOUND` inside the token identifier is removed before quantity
parsing and cannot masquerade as that description.  This deliberate
fail-closed requirement prevents a vague identifier from expanding into a
hundreds-of-kilobytes seal artifact.  A producer with an unsearchable question
must first state the quantity or refine its schema; the hook does not invent
one.

The corpus is exactly the charged set: nonrecursive `xmodel/*.md`, plus
top-level `AUDIT.md`, `notes.md`, and `APPROACHES.md`.  The report being sealed
is excluded by resolved identity.  A missing required file, symlinked corpus
entry, unreadable/non-UTF-8 file, escaping path, invalid context window, or
candidate fan-out above the declared cap returns exit 2 with an explicit
`status: ERROR` block.

### 1.2 Candidate semantics and output

The search is lexical and candidate-only.  It requires the identifier's key
nouns in a local context window and bounded-quantity terms on the
relation-bearing line.  It recognizes ASCII, Unicode, and common LaTeX
inequalities.  A relation line is still eligible when it carries an older
`OPEN[...]` label; that label is useful provenance, not evidence against a
collision.  Results are sorted deterministically and rendered as portable
repository-relative `file:line` locations.  A candidate does not close,
answer, or promote anything.

Every successful invocation emits exactly one Markdown section headed
`## COLLISIONS`.  With candidates it reports `status: CANDIDATES`; with no
candidate or no declared raised item it reports `status: EMPTY` and an
explicit `NONE` row.  The section is therefore never silently absent.  Errors
also use the same heading with `status: ERROR`, while the nonzero exit blocks a
seal wrapper.

### 1.3 Required controls

The retroactive fixture preserves the relevant source text at the exact
1-based positions from
`xmodel/companion-curve-alln-opus5-20260902.md`.  Feeding the bounded quantity
for `OPEN[DEG-AF-VS-N]` produces, in order:

```text
xmodel/companion-curve-alln-opus5-20260902.md:685
xmodel/companion-curve-alln-opus5-20260902.md:785
xmodel/companion-curve-alln-opus5-20260902.md:836
```

The negative fixture declares a synthetic quantity with no banked match and
asserts an explicit `status: EMPTY` block and per-token `NONE`.  Additional
regressions cover same-line multiple tokens, malformed syntax, missing corpus
files, prose false activation, identifier/quantity confusion, bounded fan-out,
older labels on candidate lines, bold/heading entries, and LaTeX inequalities.

### 1.4 Seal-time integration note

Immediately before the standalone `BODY-END` marker is written, a future
`lane.sh` seal phase (or a pre-step called by `seal.py`) would run
`python3 ops/open_collision.py "$report" --root "$repo"`; any nonzero status
aborts sealing, while exit 0 supplies the report's single `## COLLISIONS`
block, which is inserted before `BODY-END` and only then hashed and stamped.
The wrapper must reject a second block rather than append twice.  This lane
describes that call boundary only and makes no change to either live tool.

## 2. Typed deliverable B -- encoding-faithfulness PREFLIGHT

```text
deliverable       = N_GE_6_REALIZATION_PREFLIGHT
implementation    = box/preflight.py
focused_tests     = ops/test_preflight.py
status             = PASS
tests_run          = python3 -m unittest -v ops/test_preflight.py
pass_fail_skip     = 16 passed / 0 failed / 0 errors / 0 skipped
optimized_run      = 16 passed / 0 failed under python3 -O
runtime            = 2.14 s focused; every individual test < 10 s
builtin_canaries   = 3 passed / 0 failed
integration_note   = Section 2.6
```

### 2.1 Strict generator/solver contract

The gate consumes a strict JSON manifest and the exact `.ms` file intended for
launch:

```text
python3 box/preflight.py job.preflight.json job.ms
```

Unknown, missing, extra, duplicate, or wrongly typed JSON fields fail.  The
manifest declares `N`, corrected cell, coefficient field, monomial order,
ordered ring generators, explicit source order and generator images, the
entire reduced approximate root, ordered ideal rows, the open factor and
inverse, source-fidelity data, two-field output type, transition evidence, the
pinned stack, and `solver_input_sha256`.  `N < 6`, any unknown cell family, a
non-`QQ` field, or a non-`GRevLex` order is denied.  The bounded native cell set
is `86A`, `86B`, `86C`, `86D`, `96A`, and `96B`; a new family requires an
explicit schema extension and otherwise fails closed.

The second CLI path is mandatory.  Its bytes must match the manifest SHA-256,
be NUL-free UTF-8 POSIX text, and end in LF.  The gate parses the actual
variable line, characteristic-zero line, comma framing, generator count, every
ordered closed row, and the final Rabinowitsch row, then compares the parsed
polynomials to the checked manifest.  Thus a correct sidecar cannot approve a
stale or different ideal, even if that stale file's digest is copied into a
new manifest.

### 2.2 Exact root, coefficient, ring-map, and open checks

The corrected expansions are recomputed exactly over `Fraction` arithmetic by
reusing `box/qq_oracle_jobs.py`: the audit's `G86` with the target-dependent
auxiliary terms and `G96` with `a15*p*q + a12*q^2 + a9*p + a6*q`.  The emitted
root must contain exactly the recomputed nonzero coefficient sequence in
descending degree.  Every encoded closed condition is parsed as a polynomial
and exact-diffed against both that emitted coefficient and the independently
recomputed coefficient; rendered-string equality is not trusted.

The declared source ring order is fixed for the chosen cell.  Map images are
parsed in the target ring and must form an explicit permutation isomorphism of
the declared generators.  The manifest and actual solver variable orders must
agree.  Exactly one open is permitted: the corrected `g_c` factor must be
nonzero, its inverse must be the mapped `u`, and the actual final solver row
must be polynomially equal to `u*g_c-1`.  No `sat()` wrapper is used.

### 2.3 Fixed semantic and source-fidelity canaries

The built-in controls are computations, not self-reported booleans:

1. The charged old-A point is first checked to satisfy the old 86A closed rows
   and old open.  Corrected top cancellation then forces the degree-19
   residual `g19=11`, so corrected 86A rejects it.
2. For `q=t^6+8*t^2`, `p=t^9+12*t^5+24*t`, and
   `(a15,a12,a9,a6)=(0,0,0,-64)`, corrected 96B recomputes every closed
   coefficient `g16,...,g3` as zero and the open coefficient `g2=64`.
3. Source fidelity uses the canonical nonvacuous tuple
   `(oldEQ2,q,E1)` and exact identity `EQ2_even=oldEQ2-2*q*E1`.
   Renamed/zero aliases and the stale expression omitting `-2*q*E1` fail.

These are encoding regression controls only.  Their execution here makes no
new statement about curves, maps, attainment, or emptiness.

### 2.4 Orthogonal output typing

The accepted artifact field is exactly:

```text
NUMERICAL_PROFILE | FORMAL_EO_SERIES | SUBSYSTEM_POINT | FULL_EO_POINT |
CURVE | REPRESENTATION | FULL_COVER | POLYNOMIAL_PAIR
```

The accepted attainment field is independently:

```text
NECESSARY | REALIZED | ADMISSIBLE_PULLBACK | ACTUAL_MAP |
COUNTEREXAMPLE_CERTIFIED
```

Impossible pairings, unknown values, and advanced outputs without a checked
provenance path are rejected.  The fields are emitted separately in the JSON
result; no lossy single verdict is synthesized.

### 2.5 Checked transition ladder

Advanced A2 outputs must follow the complete, contiguous global path below;
self-loops, late starts, unknown domains/scopes/claims, missing arrows, extra
arrows, and noncontiguous states all fail.

| From | To | Exact required arrows |
|---|---|---|
| `SUBSYSTEM_POINT/REALIZED` | `FULL_EO_POINT/REALIZED` | `FULL_EO_EQUATIONS`, `DECLARED_QUOTIENT` |
| `FULL_EO_POINT/REALIZED` | `FULL_EO_POINT/ADMISSIBLE_PULLBACK` | `EO_ALL_OPENS`, `BOUNDARY_DATA`, `GENERAL_FIBRE_DATA`, `FIELD_DEGREE_FOUR` |
| `FULL_EO_POINT/ADMISSIBLE_PULLBACK` | `POLYNOMIAL_PAIR/ACTUAL_MAP` | `SOURCE_CHART` |
| `POLYNOMIAL_PAIR/ACTUAL_MAP` | `POLYNOMIAL_PAIR/COUNTEREXAMPLE_CERTIFIED` | `NONINVERTIBILITY`, `GEOMETRIC_DEGREE` |

The table explicitly rejects an A2-to-B3 kill, local-to-global torsion, and a
full-E/O point promoted to an actual map without the complete intermediate
state and every declared arrow.

### 2.6 Launch integration note

A realization generator writes the strict manifest and `.ms` payload from the
same ordered coefficient data, records the payload SHA-256 in the manifest,
and the launch wrapper invokes `python3 box/preflight.py manifest.json job.ms`
before starting qqideal/msolve; only exit 0 permits launch, the emitted JSON is
retained as custody evidence, and the wrapper launches those same hash-pinned
bytes (or rechecks the digest immediately before exec).  This lane implements
the gate but does not alter any currently running launcher.

## 3. Verification ledger

Final local commands and results:

```text
python3 -m py_compile ops/open_collision.py ops/test_open_collision.py \
    box/preflight.py ops/test_preflight.py
PASS

python3 -m unittest -v ops/test_open_collision.py ops/test_preflight.py
Ran 27 tests in 2.589s -- OK

python3 -O -m unittest -q ops/test_open_collision.py ops/test_preflight.py
Ran 27 tests in 2.605s -- OK

python3 box/preflight.py --self-test
3/3 exact canaries PASS
```

All six reference manifests (`86A/B/C/D`, `96A/B`) also pass with their
canonical in-memory solver payloads and an injected matching stack observation.
No unit test invokes `msolve` or imports `qqideal`/`msolveio`.  The local live
stack probe found `msolve=0.10.1`, while `qqideal` and `msolveio` are absent;
therefore a real launch on this host is correctly refused until the pinned
`qqideal=0.2.0` and `msolveio=0.2.1` packages are present.

## 4. Guardrail and disposition

This is an implementation lane.  Collision hits are candidates for human
review, never closures.  Solver preflight success means only that the encoded
job, controls, stack, solver bytes, and declared type transitions satisfy this
contract; it is not a solver result or a mathematical realization.  The
variable/ring map is explicit, the open is Rabinowitsch, raw remainder slots
are exact-diffed in the declared ring/order, and attainment cannot be inferred
from a weaker carrier.  No exit-price assertion is made, so no `charge_basis`
line is emitted.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13152`.
- Body SHA-256:
  `3325b7a9c1b4d456c0722854641f4d316b385d84cb21692147e8a0dd41dd693b`.
- Frozen basis: `621c9edc6bb8932e4aed6ac9805a5684a4436789`.
