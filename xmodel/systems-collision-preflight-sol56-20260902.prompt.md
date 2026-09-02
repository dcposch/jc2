# Systems lane: OPEN-COLLISION hook + PREFLIGHT hard gate (bounded implementation)

Round 20260902T0741Z adopted one new systems upgrade and re-specified the
standing one (charged synthesis, sections 6 and 9; the Opus and Sol
submissions carry the designs):
(A) OPEN/BANKED COLLISION CHECK (Opus §8.3). Before a report is sealed,
    extract every OPEN[...] it RAISES and grep the banked corpus
    (xmodel/*.md, AUDIT.md, notes.md, APPROACHES.md) for the OPEN's key
    nouns plus the quantity it asks to bound; emit a COLLISIONS section
    listing candidate matches with file:line. Fail-CLOSED: an empty
    COLLISIONS section must be explicit, never absent. The coordinator
    ran the smallest useful test by hand and it PASSED (grep for
    OPEN[DEG-AF-VS-N]'s bounded quantity surfaces
    companion-curve-alln-opus5-20260902.md lines 685/785/836). Deliver
    ops/open_collision.py (pure python, no third-party deps), a
    focused test file ops/test_open_collision.py whose fixtures include
    that exact retroactive case and one negative case (an OPEN with no
    collision must yield an explicit empty COLLISIONS block), and a
    one-paragraph integration note on how lane.sh or seal.py would call
    it at seal time (describe; do NOT modify lane.sh or seal.py — live
    lanes are running under them).
(B) PREFLIGHT AS A HARD LAUNCH GATE (Sol §10). Specify and implement the
    encoding-faithfulness preflight as a gate for every N >= 6
    realisation job: before solver launch the generator must (i) emit the
    reduced approximate root beside the ideal in the declared coefficient
    ring and order; (ii) exact-diff each encoded coefficient condition;
    (iii) fail the old (8,6,19) false-positive canary on the corrected
    86A cell; (iv) pass the explicit four-node (9,6,2) curve on corrected
    96B; (v) fail closed on any ring / map / open-factor / generator-order
    mismatch; plus the two-field output typing
    artifact = NUMERICAL_PROFILE | FORMAL_EO_SERIES | SUBSYSTEM_POINT |
    FULL_EO_POINT | CURVE | REPRESENTATION | FULL_COVER | POLYNOMIAL_PAIR
    and attainment = NECESSARY | REALIZED | ADMISSIBLE_PULLBACK |
    ACTUAL_MAP | COUNTEREXAMPLE_CERTIFIED, with a checked transition table
    that rejects "A2 cell -> B3 kill", "local torsion -> global torsion",
    and FULL_EO_POINT -> ACTUAL_MAP without every declared arrow; and a
    source-fidelity canary: a generator whose EQ2_even omits -2qE1 must
    FAIL the preflight (the campaign's CELL-32 spec had exactly that
    defect; see the synthesis). Reuse the corrected ideals and semantic
    controls of xmodel/encoding-faithfulness-audit-r2-sol56-20260901.md
    if present; deliver box/preflight.py + ops/test_preflight.py with
    those five checks and the canary as tests, fail-closed by default.
    Default stack: qqideal 0.2.0 + msolveio 0.2.1 (msolve 0.10.1); tests
    must not need msolve to run (mock or skip cleanly when the binary is
    absent).
Discipline: implementation lane, no mathematics claimed; no canonical
ledger edits; do not modify lane.sh, seal.py, artifact_finalize.py, or
any running lane's files; do not inspect jc2-lean; keep every test under
10 seconds. Report: a short typed block per deliverable (file, tests
run, pass/fail counts, integration note) in
xmodel/systems-collision-preflight-sol56-20260902.md
Seal-at-completion; bounded writes; target 8-15KB; 60 minutes.
charged_input=xmodel/ideation-20260902T0741Z-opus5.md
charged_input=xmodel/ideation-20260902T0741Z-sol56.md
charged_input=xmodel/ideation-20260902T0741Z-synthesis.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
e67b2cd027e0cdbfc249d057d929e72a3e553ca61256f48b9978bedda358e9ce  {{LANE_INPUTS}}/ideation-20260902T0741Z-opus5.md
717134c733adc17b3b70409b018858fb1311c37608a24f0eebe65ae79aec8b11  {{LANE_INPUTS}}/ideation-20260902T0741Z-sol56.md
4408cfff1eb99c4f12a81c8d1b46906df260dc790ca357240dfd4567f08d140d  {{LANE_INPUTS}}/ideation-20260902T0741Z-synthesis.md
```
