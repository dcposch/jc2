# Research lane: BMFACT-964-CODEGEN — braid decision pipeline for the realized (9,6,4) curve

(9,6,4) is REALIZED six-nodal (charged review, four-for-four
CONFIRMED): the HF-twin parametrization has the four banked
nodes plus two at v=-11/8, u^2=-35/8. Clone the PROVEN (9,6,2)
pipeline to decide its S_4 representation existence.
Deliverables:
(1) box/bmfact_964.sage — CLONE box/bmfact_962.sage (hash below;
    it already fixes footguns #10 radical-not-squarefree_part and
    #11 no-__main__-under-sage; keep both fixes; the coordinator
    runs via preparse + python, monodromy mode env-gated).
    Changes: the (9,6,4) parametrization from the charged review;
    census assertions per its item (4): degree-8 squarefree
    tangency resultant, one four-node fibre, TWO one-node fibres
    (at the new node x-values), exponent ledger 8 + 2(4+1+1) = 20;
    ABORT loudly on census mismatch.
(2) box/bmfact964_enum.py — adapt box/bmfact_enum.py: hard-code
    the REP-96 §5 (9,6,4) class list (THREE classes / 72 tuples,
    incl. the const-4c class with Pi a 4-cycle) as CONTROL ONLY —
    the decision is the full native transposition universe with
    pruning after each relation, certified against the unpruned
    count on a subsample; both orientations; positive control =
    product-only count must match 72 expansion; negative control
    = projective-relation count 0. NO manual strand map in the
    decision path. Output SURVIVOR (full meridian tuple verbatim)
    / NATIVE_ZERO_CURVE_ONLY / OPEN(census|API mismatch) — never
    a row-level kill.
(3) Derivation section: the implicit F(x,y) for this curve
    (resultant; bidegree; verify against the exact
    p^2 - q0^3 - (9/4)q0^2 - (27/16)q0 - 27/64 identity from the
    audit trail), the discriminant census, self-checks in sympy
    run in-lane verbatim.
PACE the report per-section as you go (the 962 sibling died at
the output cap leaving its report unwritten — do not repeat).
Report: xmodel/bmfact-964-codegen-grok46-20260902.md
Seal-at-completion; target 15-25KB.
charged_input=xmodel/964-nodality-review-grok46-20260902.md
charged_input=xmodel/rep-96-inner-opus5-20260901.md
charged_input=xmodel/hf-twin-964-grok46-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
402ec9e18dcec798b46210cc4acb6b3282acbfcde14d48252c6cb89c078f24e5  {{LANE_INPUTS}}/964-nodality-review-grok46-20260902.md
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  {{LANE_INPUTS}}/rep-96-inner-opus5-20260901.md
7cef355be1af63e71bc24361955ad19755598c3925fa1cb2612e62e186f4a35b  {{LANE_INPUTS}}/hf-twin-964-grok46-20260831.md
```
Repo files to clone (verify hashes, read from repo, do not
modify): box/bmfact_962.sage
2d18c1183d8ba5d7db8db767b38929064303422deadab41857e4c1a49d82d916,
box/bmfact_enum.py
b51813adcf7a407f97c486995f7f99ba73f616d0f04594506a069757bdbf832b.
