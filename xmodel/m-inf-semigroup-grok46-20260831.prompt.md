# Research lane: M-INF — the last-exponent bound by semigroup gap counts

You are a bounded desk lane on OPEN[M-INF] (integration §3.2), two
named pieces from the charged residual report §4/§6.3:

1. Prove the embedded-resolution identity used as (4.2): for the
   place at infinity of a polynomial curve (`mult = a = d-n`,
   `I(L_infty) = b = d`, any number of characteristic pairs),
   `M_emb(C) = mult(C) + beta_h - 1` where `M_emb` is the sum of
   multiplicities over the minimal embedded resolution making the
   strict transform smooth and transverse to the total transform of
   `L_infty` at a smooth point, and `beta_h` is the last
   characteristic exponent (type the exact normalization of beta_h
   you use — Puiseux vs Newton pairs — and keep it consistent).
   Verify on: one pair (a,b)=(2,5),(3,4),(4,5); two pairs — build
   the multiplicity sequences by the Euclidean/cluster algorithm for
   e.g. the (4;6,7)-type and (4;6,9)-type germs and check the
   identity on each.
2. Prove or refute `beta_h <= 2d + n - 2` for places at infinity of
   polynomial curves, via the mechanism the charged report names:
   `delta_aff = #(N \ S)` where S is the semigroup of the branch at
   infinity, `S ⊇ <d, n>`, and genus-0 forces
   `delta_aff + delta_infty = (d-1)(d-2)/2` — the gap count bounds
   the semigroup data. Work Abhyankar-Moh style: the semigroup of a
   one-place-at-infinity polynomial curve is constrained (the
   AM theorem on the characteristic sequence — acquire and hash the
   exact statement: Abhyankar-Moh 1975 "Embeddings of the line...",
   or the survey treatments); derive the bound or exhibit a
   countermodel family. Every step sourced or proved; no analogy.

charged_input=xmodel/pi1s4-close-residual-r2-opus5-20260831.md
charged_input=xmodel/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696  {{LANE_INPUTS}}/pi1s4-close-residual-r2-opus5-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  {{LANE_INPUTS}}/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
```

Deliver: both pieces proved (then (M-INF) holds and the nodal
noncoprime closure fires via the reviewed machinery), or the exact
break. Type every semigroup convention explicitly.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 4 hours hard budget.

Write one report and no other file:

```text
xmodel/m-inf-semigroup-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,000 words. Do not include a `charge_basis` declaration.
