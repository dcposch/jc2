# Hostile review: THETA-reopen report (Sol) — obstructions and the degree-8 reframe

Different-model review of a construction lane that returned typed
OPEN with two proved obstructions and a strategic reframe. Stakes:
if the obstructions are wrong the horn programme mis-prioritizes; if
the degree-8 composition claim is wrong the reframe is unsound.

charged_input=xmodel/theta-reopen-explicit-pullback-sol56-20260831.md
charged_input=xmodel/block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
charged_input=xmodel/block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md
charged_input=xmodel/block-descent-a1-mprime-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
4009c3abdc16e972aec121206664a21adc81ff8467dfe8d5a0f561e90f3a86d5  {{LANE_INPUTS}}/theta-reopen-explicit-pullback-sol56-20260831.md
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5  {{LANE_INPUTS}}/block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
7a60ff245fc351a99a23815908909327dc6a9644f849a4d3b289079c98488474  {{LANE_INPUTS}}/block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md
69970f4d2c4a2c5760e116400b1b27426edc41fdf6a8d15936df14cc567855c9  {{LANE_INPUTS}}/block-descent-a1-mprime-coordinator-integration-fable5-20260831.md
```

Directed checks, all by hand:

1. The constraint system (1.1)-(1.4): re-derive it from the promoted
   packet interfaces — is the bracket condition {f,g}=kappa the
   correct charged normalization, and are (1.3E)/(1.3O) the right
   even/odd components in the displayed normal form on
   R=C[A,U,Z]/(U^2-A-A^2Z)?
2. OBSTRUCTION[A-DEGREE-ZERO] (3.1)-(3.2): re-derive the A^0 and A^1
   coefficients and confirm the contradiction.
3. OBSTRUCTION[A-LINEAR-MINIMAL-JET] (3.3)-(3.11): re-derive
   (3.4)-(3.8) from scratch, then check the degree bookkeeping in
   (3.9)-(3.10) and the D=0 branch exhaustively — every claimed
   leading-term non-cancellation, every case. This is elementary
   polynomial algebra; verify it IS exhaustive for A-degree <=1 with
   T_0=0, and confirm the report's own scope disclaimers (does not
   cover other family points, nonzero T_0, A-degree >=2).
4. The degree-8 composition claim (3.12)-(3.14): verify the three
   displayed Jacobians term by term, the multiplicativity step, and
   [C(x,y):K]=2 as cited; confirm the conclusion 'a landed admissible
   pair composes to a noninvertible Keller map of geometric degree 8'
   and its typing as strength-evidence, not obstruction.
5. The terminology fork in §6 (locally finite vs locally quasi-finite)
   against the structure packet's lines as cited.
6. Strategic soundness: the report says a finite exhaustion cannot be
   promoted because no ruling-degree cap exists. Assess whether the
   uncancellable-leading-term mechanism of (3.10) plausibly extends
   to an all-degrees induction (do NOT attempt the proof; type what
   the inductive statement would have to be and what breaks at
   A-degree 2), so the coordinator can scope the successor lane.

Verdict: CONFIRMED / REFUTED-IN-PART per item, then: are the two
obstructions promotable as bounded exclusions, and is the degree-8
reframe safe to adopt as routing input?

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/theta-reopen-hostile-review-gpt55-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 4,500 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration.
