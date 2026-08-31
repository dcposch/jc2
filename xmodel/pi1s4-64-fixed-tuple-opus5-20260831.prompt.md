# Research lane: FIXED-TUPLE — the (6,4) cable braid decision

You are the campaign's flagship proof lane. The N=4 residual
topological core is ONE explicit object (integration §2): the
three-node polynomial curve of type `(d,n)=(6,4)`, delta-sequence
`Δ=(6,4,3)`, `β₁=15`, `(δ_∞, δ_aff, M_∞) = (7,3,16)`; the (8,4)
survivor is target-equivalent. The single missing lemma:

> **OPEN[PI1S4-(6,4)-FIXED-TUPLE].** Let `D` be an irreducible
> polynomial curve of type `(6,4)` (one place at infinity, cable
> braid `ρ_∞` determined by the two-pair Puiseux data `g=2`,
> outer `(3,2)`, inner per `Δ=(6,4,3)`, `β₁=15`) with exactly three
> affine nodes. Does a 6-tuple of transpositions in `S_4` exist
> that (i) is fixed by the Hurwitz action of the full braid
> monodromy (in particular of `ρ_∞`), (ii) satisfies the node
> commutation relations, and (iii) generates `S_4`?
>
> NO kills rows (6,4) AND (8,4), leaving only the (8,6)/(9,6)
> nodal-realization types between the campaign and unconditional
> B0 at N=4.

charged_input=xmodel/row-sweep-sol56-20260831.md
charged_input=xmodel/pi1-s4-decision-opus5-20260831.md
charged_input=xmodel/pi1s4-close-residual-r2-opus5-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb  {{LANE_INPUTS}}/row-sweep-sol56-20260831.md
010330d208c5899ce41832f1187b73d9a63268725d809b0370f2b4d9cd66eadd  {{LANE_INPUTS}}/pi1-s4-decision-opus5-20260831.md
b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696  {{LANE_INPUTS}}/pi1s4-close-residual-r2-opus5-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Method, in order:

1. **Write the cable braid explicitly.** For the `(6,4)` place with
   `Δ=(6,4,3)`, `β₁=15`: 6 strands in 3 tubes of 2 (outer torus
   braid `δ_3^2`-type on the tubes per the leading exponent 6/4 →
   reduced (3,2); inner full twists per the second pair — derive the
   exact inner exponent from `β₁=15` and the promoted cluster data).
   Cross-check the total exponent sum against `e(ρ_∞) = (d-1) +
   2δ_aff = 5 + 6 = 11` (the promoted (V)+(G) mechanism — verify
   this number first from the sweep's invariants).
2. **Promoted block machinery.** Apply promoted Theorem A'(1)-(4):
   the three tube-products `U_1,U_2,U_3` form one `<P>`-conjugacy
   orbit under the outer (3,2) action (gcd(3,2)=1 — the outer level
   is COPRIME here, so the full Theorem A argument may rerun at the
   outer level: `P^2` central etc. — derive exactly what it forces
   on `(U_1,U_2,U_3)` and `P = U_1U_2U_3`). Each `U_i` is a product
   of 2 transpositions: enumerate the possible `U_i` values (id-like
   products: e, double-transpositions, 3-cycles... a product of two
   transpositions in S_4 is e, a 3-cycle, or a double transposition)
   and run the orbit/centrality constraints.
3. **Inner twists.** The inner full twists conjugate each tube's
   pair by powers of `U_i` — derive the fixedness conditions on the
   pair within each tube.
4. **Node relations.** Three nodes ⟹ three commutation relations
   between specific meridian pairs; the tuple must also be Hurwitz-
   fixed under the three node braids (σ² factors). Combine with the
   spanning-tree/tangency structure: `V = d-1 = 5` simple tangency
   braids identify generators pairwise; track what survives.
5. **Decide.** Either derive a contradiction (NO — state the theorem
   at the exact scope: which braid data were used, does the argument
   cover every three-node (6,4) curve with this delta-sequence or
   only the specific attained one — type carefully), or exhibit a
   consistent tuple (YES — then check it against the FULL braid
   monodromy group, not just ρ_∞ and the local braids; a surviving
   tuple is a structured step toward a counterexample and must be
   reported with its complete data).

Consume only promoted statements (integrations; the coprime Theorem
A machinery; A'(1)-(4)); the ROW-SWEEP invariants are PROVISIONAL —
cite as conditional. Fail closed; every constraint derivation
explicit.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 6 hours hard budget.

Write one report and no other file:

```text
xmodel/pi1s4-64-fixed-tuple-opus5-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
6,000 words. Do not include a `charge_basis` declaration.
