# Hostile review: D1-DEGREE report (Sol)

Different-model gate. The charged report claims: no finite raw-degree
bound on `deg D_1` exists (unbounded under target automorphisms); the
correct invariant phrasing is `min over Aut(A^2) of deg T(D_1)`;
unconditional constraints on an escaping residual —
`gcd(d,n)=g>=2`, quotient shapes `(u,1)/(odd u,2)/(4,3)`,
`d = 2g_L + c(Pi) + 2`, `g <= gcd(deg P, deg Q) - 2`; the Chau filter
list through d<=9; the coprime intermediate kill-list reduced to
`(4,3)`. Default to refutation.

charged_input=xmodel/d1-degree-bound-sol56-20260831.md
charged_input=xmodel/pi1s4-close-residual-r2-opus5-20260831.md
charged_input=xmodel/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
0549dfafe339d20c67fe0d64a0bc713c1e64850013fbaab9f07f654c7fbf8fc2  {{LANE_INPUTS}}/d1-degree-bound-sol56-20260831.md
b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696  {{LANE_INPUTS}}/pi1s4-close-residual-r2-opus5-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  {{LANE_INPUTS}}/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
```

Verify: (1) §2's unboundedness argument (target postcomposition
raising deg D_1 with N=4 fixed) — is the construction actually
Keller-compatible, i.e. does postcomposing by a target automorphism
preserve the Keller property and the residual structure? re-derive;
(2) the Jelonek/Chau typing in §3 (re-open the cited theorems —
hash what you fetch — and check each 'does not bound' claim and the
shape constraints from Chau Theorem B: re-derive the (u,1)/(odd
u,2)/(4,3) trichotomy and the g <= gcd(deg P,deg Q)-2 inequality);
(3) the identity `d = 2g_L + c(Pi) + 2` — what is g_L, is the
derivation sound; (4) §6's noncoprime list through d<=9 — recompute
it from the constraints; (5) the claim that the coprime kill-list
reduces to (4,3) — check against the promoted survivor table
((4,3),(5,4),(7,4),(8,3),(9,4),(9,8)) and the residual's shape
constraints: is the elimination of the other five sourced?; (6) the
invariant-phrasing caveat on the CLOSE-RESIDUAL payoff. Verdict per
item + promotion recommendation.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/d1-degree-hostile-review-gpt55-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
4,500 words. Do not include a `charge_basis` declaration.
