# Research lane: B0-REDUCIBLE — the reducible-A_F gap at N>=5

You are a flagship research lane on the all-degree front
OPEN[B0-REDUCIBLE-N>=5/COMPONENT-INCIDENCE+RAMIFIED-COVERS]
(integrations §3/§4): for N>=5 with A_F REDUCIBLE, exclude (or pin)
trivial dicriticals. The N=4 reducible case was pinned into one
one-parameter family by the machinery now promoted; build the N=5
analogue.

charged_input=xmodel/b0-all-n-eta-criticality-sol56-20260831.md
charged_input=xmodel/b0-all-n-hostile-review-grok46-20260831.md
charged_input=xmodel/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
621f1356b3b5290e32c2f2bf689b4d9a49412cb852066886a34b580366cb1652  {{LANE_INPUTS}}/b0-all-n-eta-criticality-sol56-20260831.md
f865204a3fd2ee3a6944b6739ae581cf29c41a7f2259bbc54cd1587ddf397a46  {{LANE_INPUTS}}/b0-all-n-hostile-review-grok46-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  {{LANE_INPUTS}}/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Method: (1) run the promoted budget at N=5 with A_F = D_1 ∪ ... ∪ D_m
reducible (m>=2): Sum(mu_l + corr_l) = 4, distinct owners per
component (promoted), a_{D_i} >= 1 each — enumerate ALL profiles
carrying a trivial dicritical, splitting by which component owns it;
(2) apply the promoted machinery per profile: eta-criticality per
component (each component has its own normalization; the promoted
correction-support = ramification-support transfer), Zariski-Nagata
branch locus, the aggregate Euler identity, and the promoted per-
component (M-INF)-style gates where components are polynomial curves
(derive when they are: does Orevkov 2.1 force A^1 normalization per
component at N=5 as it did at N=4?); (3) for surviving profiles,
pin the complete structure as the N=4 residual was pinned (degrees,
delta budgets, monodromy classes, the S_5 representation constraints
— the cover is 5-sheeted; meridian cycle types per component from
the profile); (4) deliver: profiles KILLED (with gates), the exact
surviving configurations fully typed (the N=5 analogue of the
residual cage), and the decision questions in PI1-S4 style. All
consumption from promoted integrations; provisional items typed.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 6 hours hard budget.

Write one report and no other file:

```text
xmodel/b0-reducible-n5-opus5-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
6,000 words. Do not include a `charge_basis` declaration.
