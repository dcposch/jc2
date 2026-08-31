# Hostile review: CORR-BUDGET-N5 report (Sol) — does the profile really self-destruct?

Different-model gate. The charged report claims the sole N=5
trivial-dicritical profile under H2, `(2,1)+(1,0)` with
`(s_2,s_1,a)=(1,1,2)`, is IMPOSSIBLE: the unique correction point
forces `d eta(z)=0` on the shared normalization while the mu=1
birational copy forces eta immersive at the same z. If this holds, B0
extends to N=5 under H2 and the mechanism plausibly generalizes.
Default to refutation.

charged_input=xmodel/corr-budget-n5-sol56-20260831.md
charged_input=xmodel/block-descent-a1-b0-coordinator-integration-fable5-20260831.md
charged_input=xmodel/b0-trivial-dicritical-proof-opus5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
67a9482eecd3fcb5f06bcf2967d4b73f5761429b5be597f2809b8e0767b1b02c  {{LANE_INPUTS}}/corr-budget-n5-sol56-20260831.md
bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963  {{LANE_INPUTS}}/block-descent-a1-b0-coordinator-integration-fable5-20260831.md
b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55  {{LANE_INPUTS}}/b0-trivial-dicritical-proof-opus5-20260831.md
```

Checks: (1) §1-§2: the promoted premises are consumed at promoted
scope (both integrations); the local model at the correction point
(mu_x=3 from corr=1 on the mu=2 dicritical) and what it does NOT
determine (OPEN[LOCAL-PUISEUX-N5] typing). (2) §3-§4: re-derive the
Euler/aggregate accounting and the componentwise budgets; check every
fibre equation. (3) §5 — the heart: the two maps h_1, h_2 called
isomorphisms — verify from the promoted covering/normalization data
that BOTH dicritical parametrizations factor through the SAME
normalization eta with degree-one factors (this is where H2 s_1=s_2=1
enters; is the factorization licensed at the correction point itself,
where the covering lemma's smooth-stratum scope may not reach? — the
report claims the comparison happens at the normalization place z, not
at the singular image; audit that carefully against the flag/place
discipline). (4) Verify (5.1)-(5.2) and that no promoted statement
contradicts the conclusion. (5) §6: the counterfactual typing and the
claim that no PI1 question remains at N=5 under H2. (6) Assess
explicitly: does the argument generalize to all N under H2 (trivial
dicritical with s=1 + any correction anywhere on any dicritical with
s=1)? What breaks at s>=2? Type the exact statement of the
generalization for a successor lane.

Verdict: CONFIRMED (promote the N=5 kill) / REFUTED (exact step) /
GAP.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/corr-budget-n5-hostile-review-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 4,500 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration.
