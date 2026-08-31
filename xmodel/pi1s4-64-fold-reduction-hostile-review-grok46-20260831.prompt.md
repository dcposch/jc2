# Hostile review: FOLD-REDUCTION report (Opus)

Different-model gate. The charged report claims: Theorem FOLD (every
member of the (6,4) row Δ=(6,4,3) is, after a triangular target
automorphism, {(r(t)^2, q(t))} with deg r=3, deg q=4 — row-level);
the (8,4) coverage via shear (landing on coprime (7,4) killed, or on
(6,4)); the complete geometry of D' ∪ D'^- (3-nodal quartics,
hyperflexes at a common point, cross-locus over {u=0}, I(Q')=13,
Lemma 2.3 β₁ = I(Q')+2 giving an UNCONDITIONAL β₁=15); π₁(C²−D')=Z
from promoted machinery; the N-A union deficit exactly 3 (robust);
the restriction/cover argument; and the verdict that the fold route
fails intrinsically. Default to refutation.

charged_input=xmodel/pi1s4-64-fold-reduction-opus5-20260831.md
charged_input=xmodel/pi1s4-64-fixed-tuple-opus5-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
8529de8ec1b11450a95481ffdf19f6e5116129aeef2ea2c27579b4e4fcc93a74  {{LANE_INPUTS}}/pi1s4-64-fold-reduction-opus5-20260831.md
a60887501137251f50f1ce7bf8ddc8921b1f22e20a4aebced47ce35699a0fad8  {{LANE_INPUTS}}/pi1s4-64-fixed-tuple-opus5-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Verify: (1) Theorem FOLD's proof — why does Δ=(6,4,3) force p a
square after a triangular automorphism? re-derive; (2) the (8,4)
shear dichotomy; (3) §2's geometry: the hyperflex claims, the
cross-locus computation (one point per root of r, contact μ_τ, sum
3), Bezout I(Q')=13, and Lemma 2.3 — including the UNCONDITIONAL
β₁=15 re-derivation (this upgrades a provisional datum; gate it
hard); (4) §3's restriction argument (index-2 cover, μ null-homotopy)
— re-derive; (5) §4: C_i²=3 on every admissible surface, the
threshold 2r₁=6, the deficit-3 robustness claims, and the
exchange-rate computation (deficit 1 downstairs); (6) the §5 verdict
logic and §6's successor typings (especially
OPEN[NA-R1-SHARPNESS-IRREDUCIBLE] — is the sharpness question
correctly posed?). Verdict per item + promotion recommendation.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/pi1s4-64-fold-reduction-hostile-review-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,000 words. Do not include a `charge_basis` declaration.
