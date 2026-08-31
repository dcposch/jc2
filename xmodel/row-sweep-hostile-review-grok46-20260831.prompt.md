# Hostile review: ROW-SWEEP report (Sol)

Different-model gate for four claimed row-kills and the exact
residual ledger. Default to refutation.

charged_input=xmodel/row-sweep-sol56-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
charged_input=xmodel/pi1s4-close-residual-r2-opus5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb  {{LANE_INPUTS}}/row-sweep-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696  {{LANE_INPUTS}}/pi1s4-close-residual-r2-opus5-20260831.md
```

Verify, row by row: (1) the (6,3) tangential kills — the triangular
target reduction to coprime (5,3) resp. (4,3): re-derive the
reduction (what target automorphism, why does it preserve the
residual data and land in the promoted coprime theorem's scope?);
(2) the (8,2) and (9,3) (M-INF) kills — enumerate the admissible
infinity types yourself with the corrected cluster identity and
confirm every `M_∞` bound; (3) the (6,4) survivor: re-derive the
delta-sequence census (why is `Δ=(6,4,3)` the SOLE survivor), the
invariants `(7,3,16)`, and the three-node attainment (verify the
double-point scheme of the attaining curve — nodes, not tangencies
or worse); (4) the (8,4) survivor and the claimed target-equivalence
to (6,4); (5) the (8,6)/(9,6) numerical-type lists (re-enumerate);
(6) the ledger's consumption discipline (no A'(5), no coprime order
fork off-stratum, no AM converse, no attainment claims). Verdict per
row + promotion recommendation.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/row-sweep-hostile-review-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,000 words. Do not include a `charge_basis` declaration.
