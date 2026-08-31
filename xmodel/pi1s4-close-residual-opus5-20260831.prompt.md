# Research lane: PI1S4-CLOSE-RESIDUAL — pin (C1) for D_1, or close the noncoprime stratum

You are the flagship follow-up lane. The Main Theorem of the charged
PI1-S4 report answers NO on the coprime stratum (C1). The campaign
needs the answer for the SPECIFIC curve `D_1` of the repaired N=4
reducible residual (B0 integration §1.5): the image of the
`(mu,corr)=(2,0)` dicritical of a hypothetical degree-4 Keller map
with reducible `A_F = D_1 ∪ D_0`, both polynomial curves,
`Sing D_1 ∩ D_0 = ∅`, `a_{D_1}=2`, every `D_1`-singularity a double
point of two smooth branches with `a_p=0` and disjoint-transposition
local monodromy, `pi_1(C^2-D_1) ->> S_4` meridians-to-transpositions.

charged_input=xmodel/pi1-s4-decision-opus5-20260831.md
charged_input=xmodel/b0-trivial-dicritical-proof-opus5-20260831.md
charged_input=xmodel/block-descent-a1-b0-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
010330d208c5899ce41832f1187b73d9a63268725d809b0370f2b4d9cd66eadd  {{LANE_INPUTS}}/pi1-s4-decision-opus5-20260831.md
b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55  {{LANE_INPUTS}}/b0-trivial-dicritical-proof-opus5-20260831.md
bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963  {{LANE_INPUTS}}/block-descent-a1-b0-coordinator-integration-fable5-20260831.md
```

Two routes to closure; pursue in order, fail closed:

1. **Pin (C1).** Determine whether the promoted N=4 fibre/cover data
   force the place at infinity of `D_1` to have one Puiseux pair.
   Available leverage: `D_1` is a polynomial curve of some degree
   `d_1` with `deg p > deg q =: n_1` after the report's
   normalization; the degree-4 cover `q: Y -> C^2` is etale over
   `C^2 - D_1` with meridian type `(2,1,1)`; the boundary structure
   of Y over infinity is constrained by the Keller extension (the
   dicritical `l_1` has `mu=2, corr=0, s=1`; Orevkov's chain
   structure at infinity applies to the compactified cover). Also
   try the OTHER direction: Theorem A of the charged report holds for
   ALL (d,n) coprime-or-not? — No: Theorem A used `rho_infty =
   delta^n` which needs (C1); but its §9 successor sketch
   (block-collapse for cable braids) is typed as hypothesis. Derive
   the cable form: for `g = gcd(d,n) >= 2` write the braid at
   infinity of a one-place curve as the `(g)`-cable of `delta_{g}`
   -type outer braid with inner full twists; PROVE the block-collapse
   compatibility (inner full twists conjugate each block by its own
   product, acting trivially on block products) and re-run the
   Theorem A argument at the outer level; identify exactly what
   group-theoretic condition on the block products replaces
   centrelessness, and what it yields for S_4 tuples. This is the
   charged report's stated successor hypothesis — settle it.
2. **(M-INF) in general.** Prove `M_infty <= 3d-3` for the place at
   infinity of an arbitrary polynomial curve (`mult = d-n`, `I = d`,
   any number of Puiseux pairs), or find a countermodel. Use the
   shared-cluster identity (the initial cluster segment sums to d)
   plus `mult_Q = d-n`; the charged report locates the residual
   content as bounding the non-initial multiplicities by `2d-3`.
   With (M-INF) and the (ii-a) equisingular nodalization or the
   direct representation transport, Theorem B/C extend; if you prove
   (M-INF) but not (ii), state exactly the nodal-case closure you DO
   get (Theorem B needs only (M-INF) + Nori for nodal curves — that
   already covers the residual D_1 whenever its singularities are
   transverse; the tangential case then rides (ii)).
3. Assemble: the strongest closure statement for the N=4 reducible
   residual you can prove, and the exact typed OPEN if any case
   escapes (which (d_1, n_1, tangency) configurations survive).

Consume only promoted statements and hashed sources (re-fetch Nori
from Numdam and verify `1b848c19...`; the charged report's Theorems
A/B/C are PROVISIONAL until their review lands — you may cite them
as conditional inputs, clearly typed). Six hours hard budget.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 6 hours hard budget.

Write one report and no other file:

```text
xmodel/pi1s4-close-residual-opus5-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 6,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration.
