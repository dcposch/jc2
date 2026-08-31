# Research lane: FOLD-REDUCTION — the braid-free kill of the (6,4) row

You are the flagship proof lane on OPEN[PI1S4-(6,4)-FOLD-REDUCTION]
(charged FIXED-TUPLE report §9, named most likely to decide the row).
The setup, from the charged report: the ROW-SWEEP witness has
`p = r²` with `r = t³+t+1`, so `D` (the three-node (6,4) curve) is
the image under the fold `ν(u,y) = (u², y)` of the COPRIME curve
`D' = {(r(t), q(t))}` of normalized type (4,3) — a 3-nodal rational
quartic with `π₁(C²−D') = Z` by the promoted coprime Main Theorem.
The charged report proves: every `φ: π₁(C²−D) ↠ S_4` (meridians to
transpositions) restricts through the double cover to a surjection
`π₁(C² − (D' ∪ D'^-)) ↠ S_4` with all meridians transpositions,
where `D'^- = D'` reflected under `u ↦ −u`.

Your task: decide whether that two-component surjection can exist,
fail closed:

1. **Structure of `D' ∪ D'^-`.** Both components are 3-nodal coprime
   quartics with abelian individual complements (promoted). Compute
   their intersection: `D' ∩ D'^-` lies over `{u=0} ∪` fixed
   points; derive the intersection number and the local types
   (transverse? tangential?) from the explicit `r, q` of the witness
   — but ALSO determine what is forced for EVERY curve in the row
   (the fold structure `p = r²`: is it forced by Δ=(6,4,3), or
   witness-specific? The charged report's §8 covers the row via
   ρ_∞ only; here type carefully what quantifies over the row vs
   the witness. If `p=r²` is witness-specific, determine the
   fold-existence condition — `p` a perfect square after target
   automorphism — and whether every row member admits SOME such
   structure, e.g. via the (8,4) target-equivalence `P = p + q²`).
2. **Two-component machinery.** Apply the promoted Theorem N-A to
   `D = D' ∪ D'^-` on the infinity-resolved surface (both components
   coprime (4,3) with δ_∞=0 — flex at infinity? compute; `E` =
   infinity divisor): the hypothesis needs `C² > 2r₁ + 4T + T_x` for
   EACH component — compute `C'²`, the nodes r₁=3 per component, and
   T_x = tangential cross-points from step 1. If N-A fires, the
   kernel is abelian and NO S_4 surjection exists — the row DIES.
   If the inequality fails, quantify the gap and try: (a) the
   reducible aggregate machinery; (b) a direct ZvK on the union
   (the components' individual braids are trivial-ish since each
   complement is abelian; the cross-relations carry everything);
   (c) the promoted conversion law applied to the S_4-cover pulled
   back through ν.
3. **Verdict.** Row KILLED (theorem, with exact quantification over
   the row), SURVIVES the fold route (with the residual typed), or
   OPEN at a named computation.

Consume only promoted statements; the FIXED-TUPLE restriction
theorem and the ROW-SWEEP witness data are PROVISIONAL — cite as
conditional (the restriction proof is in the charged report §9;
re-derive its two-line cover argument yourself as part of step 2).
charged_input=xmodel/pi1s4-64-fixed-tuple-opus5-20260831.md
charged_input=xmodel/row-sweep-sol56-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
a60887501137251f50f1ce7bf8ddc8921b1f22e20a4aebced47ce35699a0fad8  {{LANE_INPUTS}}/pi1s4-64-fixed-tuple-opus5-20260831.md
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb  {{LANE_INPUTS}}/row-sweep-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 6 hours hard budget.

Write one report and no other file:

```text
xmodel/pi1s4-64-fold-reduction-opus5-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
6,000 words. Do not include a `charge_basis` declaration.
