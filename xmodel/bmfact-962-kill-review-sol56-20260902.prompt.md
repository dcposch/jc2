# Review lane: BMFACT-962-KILL-REVIEW — gate the (9,6,2) representation kill

Result to gate: the full SAGE-NATIVE ZvK intersection for the
realized (9,6,2) curve returned ZERO generating survivors
(n_fixed=6 non-generating tuples, im != S_4; product-only
positive control = 144 exact both orientations; BLOCK variants
also 0/0). Claim: **the realized (9,6,2) curve carries no
transitive S_4 representation of pi_1(C^2 \ D) compatible with
its braid factorisation — a representation-level kill of THIS
curve, convention-independent.**

Charged artifacts: box/bmfact962_result.json (the banked JSON,
7ad79c5c...), box/bmfact962_native_enum.log (full runner output,
537e0fa0...), the two scripts (hashes below), and the Sol
ideation submission whose §6 argues zero/nonzero invariance
under geometric-basis conjugacy, strand relabeling, and
inversion.

Tasks:
(1) SCRIPT AUDIT: bmfact_962.sage (the census/ZvK emitter — the
    coordinator patched line 366 radical() and ran via preparse;
    confirm nothing else consumes squarefree semantics) and
    bmfact_enum.py (the fixed-set intersection: verify the ZvK
    action implementation — Fox/Artin convention — against a
    hand-computed example; verify the "generating" test is
    im = S_4 AND transitivity; verify the pruning in the full
    variant cannot drop a survivor).
(2) THE SIX FIXED NON-GENERATING TUPLES: extract them from the
    JSON/log; verify each has im != S_4 (state the images); the
    kill claim needs transitive+S_4 — check REP-96's constraint
    set licenses exactly that requirement.
(3) INVERSION/BASEPOINT: the full variant ran as-written
    orientation only. Replay the §6 invariance argument
    (conjugacy/relabel/inversion) as a PROOF or refute it; if it
    holds, the missing inverse-full run is covered; if not,
    demand the inverse run (state so loudly). Same for
    OPEN[BMFACT-BASEPOINT]: does the absent base point affect
    the zero/nonzero DECISION (not the labels)?
(4) POSITIVE CONTROL CROSS-CHECK: 144 = REP-96's expansion —
    re-derive that count independently from the six classes.
(5) Verdict: KILL-BINDING (curve-level scope: THIS realized
    curve, not the numerical row) / KILL-BLOCKED (name defect) /
    REPAIRS. Type the surviving scope precisely.
Report: xmodel/bmfact-962-kill-review-sol56-20260902.md
Seal-at-completion; target 15-25KB.
charged_input=box/bmfact962_result.json
charged_input=box/bmfact962_native_enum.log
charged_input=xmodel/ideation-20260902T0022Z-sol56.md
charged_input=xmodel/rep-96-inner-opus5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
7ad79c5c1edcb9ecad97d068fd7aa684f03b0e0a7f3427d08d15c5560cfeed70  {{LANE_INPUTS}}/bmfact962_result.json
537e0fa036a9915ba123cee164ab66ec047730aee1e7b68cad71e6260ff6b424  {{LANE_INPUTS}}/bmfact962_native_enum.log
4b0e4dde91a8bbe06dfde68e0c8c4559d92bcb8355a0b57acf32ba8b36a7d3b4  {{LANE_INPUTS}}/ideation-20260902T0022Z-sol56.md
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  {{LANE_INPUTS}}/rep-96-inner-opus5-20260901.md
```
Repo scripts (verify hashes, read in place):
box/bmfact_962.sage
2d18c1183d8ba5d7db8db767b38929064303422deadab41857e4c1a49d82d916,
box/bmfact_enum.py
b51813adcf7a407f97c486995f7f99ba73f616d0f04594506a069757bdbf832b.
