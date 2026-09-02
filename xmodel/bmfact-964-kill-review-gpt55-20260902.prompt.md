# Review lane: BMFACT-964-KILL-REVIEW — gate the (9,6,4) representation kill

Result to gate: the (9,6,4) braid decision returned
**NATIVE_ZERO_CURVE_ONLY** — native full ZvK generating count 0
in BOTH orientations; product-only control matches the expected
72 expansion; census_ok (11 braids: 8 tangencies + one
four-node fibre + two one-node fibres, ledger 20, matching the
desk prediction confirmed by 964-nodality-review); api_ok.
Claim: the realized six-nodal (9,6,4) curve admits no
transitive S_4 representation compatible with its braid
factorisation — curve-level kill, explicitly NOT a row kill.

Charged artifacts: box/bmfact964_result.json (01bac03c),
box/bmfact964_enum_run.log (709c08c8), the codegen report
(9266de15) whose derivation section and self-controls
(72/0/pruner-cert) you must audit, plus REP-96 (the three
CABLE-3 classes / 72 tuples used as control).

Tasks:
(1) SCRIPT AUDIT on box/bmfact_964.sage + box/bmfact964_enum.py
    (read in place; hashes in the codegen report): the ZvK
    action convention, the generating test (im=S_4 AND
    transitive), and CRITICALLY the pruning path — the decision
    ran with per-relation pruning + subsample certification;
    verify the certification actually bounds the pruner (a
    pruner bug is the one way a survivor gets dropped silently).
(2) Verify the 72-control derivation independently from
    REP-96's three classes (24-orbit expansion each).
(3) Confirm BOTH orientations genuinely ran on the FULL variant
    (unlike the 962 first pass) — cite the log lines.
(4) Basepoint: does the absent Sage base point affect the
    zero/nonzero decision for THIS run?
(5) Verdict: KILL-BINDING (scope: this realized curve) /
    KILL-BLOCKED / REPAIRS. Also state the composed consequence
    precisely: with both realized substrates rep-dead at curve
    level, what remains of the (9,6) row at N=4 (numerical-type
    orbit coverage — cite REP-96's REPRESENTATIVE discipline)
    and what transfers to N>=6 (pipeline validation only).
Report: xmodel/bmfact-964-kill-review-gpt55-20260902.md
Seal-at-completion; target 12-20KB.
charged_input=box/bmfact964_result.json
charged_input=box/bmfact964_enum_run.log
charged_input=xmodel/bmfact-964-codegen-grok46-20260902.md
charged_input=xmodel/rep-96-inner-opus5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
01bac03c71000b9bc3557e1d4387864d9d5d23842434920bf70a2c6eb24949cc  {{LANE_INPUTS}}/bmfact964_result.json
709c08c83f99b444a89e2a4b38959a014a0d19ec990f7f2e1f8351aeaf6a755c  {{LANE_INPUTS}}/bmfact964_enum_run.log
9266de1542e68b64a346103eace77afd91f24b8d5195379c2f68abd19a469b79  {{LANE_INPUTS}}/bmfact-964-codegen-grok46-20260902.md
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  {{LANE_INPUTS}}/rep-96-inner-opus5-20260901.md
```
