# Research lane: CORR-BUDGET-N5 — the single correction point at N=5

You are a bounded primary research lane on the promoted N=5 residual.
Under H2 exactly one profile carries a trivial dicritical
(integration §1.7): `(μ,corr) = (2,1)+(1,0)` with covering degrees
`(s_2, s_1, a) = (1,1,2)`. The single correction point on the μ=2
dicritical is, by promoted [Z-6.5b]/[O-5.2], the UNIQUE critical
point of the immersed parametrization of its image component — the
only non-immersive point anywhere over `A_F`.

charged_input=xmodel/block-descent-a1-b0-coordinator-integration-fable5-20260831.md
charged_input=xmodel/b0-trivial-dicritical-proof-opus5-20260831.md
charged_input=xmodel/b0-proof-hostile-review-sol56-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963  {{LANE_INPUTS}}/block-descent-a1-b0-coordinator-integration-fable5-20260831.md
b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55  {{LANE_INPUTS}}/b0-trivial-dicritical-proof-opus5-20260831.md
8ffc0a06edcf2be3908b1486da57e7d4a024973e679f9d25577cc281ef005320  {{LANE_INPUTS}}/b0-proof-hostile-review-sol56-20260831.md
```

Task, fail closed: classify that germ against the fibre data and kill
the profile or pin it. Concretely: (1) write the local model at the
correction point `x` — Orevkov's `μ_x > μ_l = 2` with
`corr = μ_x - μ_l = 1`, so `μ_x = 3` — a local degree-3 point on a
generically 2-sheeted dicritical; derive what singularity the image
curve has there (locally irreducible by [Z-6.5b]; which Puiseux types
are consistent with `μ_x=3` over a smooth target disc transverse to
the image?); (2) run the promoted Euler/aggregate machinery on the
N=5 configuration (both components, their normalizations, the
correction point's contribution) exactly as the repaired N=4 residual
was pinned — derive the analogues of `s_0=1, c_0=1`, normalization
constraints, and the singularity budget of each component; (3)
determine whether the configuration self-destructs (as row (d) did at
N=4 under H2 via strictness) or survives with a completely pinned
shape — either way state exactly what a PI1-S4-style residual question
looks like at N=5. Consume only promoted items (both integrations)
plus hashed primary sources; re-derive anything else.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 6 hours hard budget.

Write one report and no other file:

```text
xmodel/corr-budget-n5-sol56-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 5,500 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Include a `charge_basis` declaration only if you assert a genuinely new
exit price with a direct mathematical-source citation; otherwise omit.
