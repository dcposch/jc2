# Preparation lane: R5-CHARGE — draft the disproof-matrix charge sheet

You are a preparation lane on the disproof side. The AS109-D12
registry gated any matrix work behind an 11-step fail-closed
preflight (charged below, §6). Nobody has yet attempted a compliant
charge sheet. Draft one for the SOLE legitimate target: a declared
finite-support cell of R5 (the hypothetical exact Z_109 polynomial
lift of (x - x^109, y)).

charged_input=xmodel/as109-d12-seed-provenance-reconciliation-grok46-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
bb2a3d0753583ef08f78f989e2c9b6a1026652e423f1b2722533274d80ae9a6a  {{LANE_INPUTS}}/as109-d12-seed-provenance-reconciliation-grok46-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Work through the preflight steps 1-11 IN ORDER, drafting the charge
sheet entry for each: name R5 explicitly; declare lift ring
(Z_109[x,y] packed identity per the closed-support artifact it
cites) and matrix ring with the reduction map exhibited; declare the
Witt level n explicitly (justify the choice — the floor-twelve
theorem constrains it); freeze finite x- and y-support exponent sets
(the floor-twelve theorem gives deg_y >= 12 for corrections — choose
the minimal admissible bidegree shape and justify from the cited
producers; if no finite exhaustive gauge-normal grammar exists,
declare NO-FROZEN-GRAMMAR at that step and STOP — that is a
legitimate outcome that permanently closes the matrix route until
new theory); declare generator order, gauge slice (with the
sigma_tau restriction), and the collision as ONE typed condition;
run the image checks; spec the eventual computation's shape (ring,
variables, expected dimensions) WITHOUT running anything. Deliver:
either a complete draft charge sheet ready for coordinator review +
different-model audit, or a typed STOP at the first preflight step
that cannot be discharged, with exactly what new input would
discharge it.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 4 hours hard budget.

Write one report and no other file:

```text
xmodel/r5-charge-sheet-draft-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,500 words. Do not include a `charge_basis` declaration.
