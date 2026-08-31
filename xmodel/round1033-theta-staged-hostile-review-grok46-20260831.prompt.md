# Hostile review: THETA-STAGED report (Sol) — is the OPEN verdict right?

Different-model review of a fail-closed report. The charged report
stopped at Stage 0 with `OPEN[THETA-STAGE0-MARKED-SNC]`, holding that
the charged pullback `(f,g)` is nowhere explicit in the promoted
packets, no admissible marked SNC representative exists in the frozen
data, and no unique horizontal vertex is typed. A wrong OPEN wastes
the campaign's top-ranked composite; a wrong reopen list burns the
successor lane. Check both directions.

charged_input=xmodel/round1033-theta-staged-sol56-20260831.md
charged_input=xmodel/block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
charged_input=xmodel/block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md
charged_input=xmodel/ideation-20260831T1033Z-synthesis.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
1cf8f9d75e17efd2fc5d43861d721a1eb3b3c0d468e93c75d571f875576012fb  {{LANE_INPUTS}}/round1033-theta-staged-sol56-20260831.md
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5  {{LANE_INPUTS}}/block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
7a60ff245fc351a99a23815908909327dc6a9644f849a4d3b289079c98488474  {{LANE_INPUTS}}/block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md
2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef  {{LANE_INPUTS}}/ideation-20260831T1033Z-synthesis.md
```

Tasks: (1) Hunt the two charged packets line-by-line for anything the
report missed that DOES pin the pullback or a model — explicit
`P_f,Q_f,P_g,Q_g`, an equation for `B`, a divisorial pole ledger, or
data from which one is derivable by finitely many typed steps; if you
find such, the OPEN is refuted — demonstrate the derivation. (2)
Verify the transformation law (0.4) as proved (birational boundary
modifications fixing `S` preserve `d_h`, `r_h`) — including whether
`d_h` as defined in (0.3) really is model-free. (3) Verify the
report's reading of (1.12)-(1.14) as generic-point-only, against the
structure packet's own statements. (4) Audit the reopen list: is each
item necessary, and is the list sufficient (would supplying exactly
those items let Stage 2 run)? (5) Check the report's claim that the
retained chart iota (0.2) is source-side and cannot be reused as the
charged pullback. Verdict: OPEN CONFIRMED (with the reopen list
ratified or amended) or OPEN REFUTED (with the derivation).

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/round1033-theta-staged-hostile-review-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 4,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration.
