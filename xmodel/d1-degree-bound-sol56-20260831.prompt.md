# Research lane: D1-DEGREE — bound the degree of the residual curve

You are a bounded primary research lane on the campaign's
highest-leverage open item, OPEN[PI1S4-D1-DEGREE] (integration §3.1):

> For the repaired N=4 reducible residual (both components polynomial
> curves; `D_1` = image of the `(mu,corr)=(2,0)` dicritical, `s_1=1`,
> `a_{D_1}=2`; `D_0` = image of the trivial dicritical, `s_0=1`,
> `a_{D_0}=3`; `Sing D_1 ∩ D_0 = ∅`; every `D_1` singularity a
> double point of two smooth branches with `a_p=0`, disjoint
> transpositions), derive an upper bound on `deg D_1` — or any
> constraint on its normalized degree pair `(d,n)` — from the
> promoted Keller-cover data. `deg D_1 <= 4` closes B0 at N=4
> unconditionally (PROVISIONALLY reviewed residual closure); any
> bound B yields a finite `(d,n)` checklist against the promoted
> kill-list (survivors at d<=9: (4,3),(5,4),(7,4),(8,3),(9,4),(9,8))
> and the per-curve (M-INF) test.

charged_input=xmodel/pi1s4-close-residual-r2-opus5-20260831.md
charged_input=xmodel/b0-trivial-dicritical-proof-opus5-20260831.md
charged_input=xmodel/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696  {{LANE_INPUTS}}/pi1s4-close-residual-r2-opus5-20260831.md
b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55  {{LANE_INPUTS}}/b0-trivial-dicritical-proof-opus5-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  {{LANE_INPUTS}}/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
```

Leverage to try, fail closed at each: (1) the degree-4 extension at
infinity: compactify the Keller map and run Orevkov's regularization
— the dicritical `l_1` (mu=2, s=1, corr=0) maps onto D_1; relate
`deg D_1` to the chain data / self-intersections of the Orevkov
tree at N=4 (the budget N-1=3 is spent as 2+1; what does the SHAPE of
the tree force about the polar/degree invariants of the images?);
(2) Jelonek/Chau degree bounds: primary sources bound `deg A_F` for
polynomial maps (Jelonek's bound on the non-properness set degree in
terms of deg F — acquire and hash the exact statement: Jelonek,
"The set of points at which a polynomial map is not proper", and the
sharper "Testing sets for properness..." papers; Chau 1999 §2 also
relates deg of E_f components to (deg P, deg Q) via Newton data);
at N=4 the map degree is bounded how? — careful: geometric degree 4
does NOT bound deg F; type exactly what does and does not follow;
(3) the fibre identity: `a_{D_1}=2` generic and `a_p=0` at
singular points, with the promoted (M')/aggregate machinery on the
two-component configuration — the aggregate identity plus both
components' polynomial-curve structure may bound `delta_aff(D_1)`
hence `(d-1)(n-1)`-type quantities; work the numbers; (4) the S_4
cover: Y -> C^2 etale over C^2-D_1 with cycle type (2,1,1), Y
irreducible; chi_c(Y) computations against the promoted toolkit pin
chi_c relations between s, delta data; combined with the genus
identity this may cap d. Deliver: a proved bound (any B), or a typed
OPEN naming exactly the missing invariant, with all partials proved.
Consume only promoted items; the residual-closure r2 is PROVISIONAL
— cite as conditional where needed.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 6 hours hard budget.

Write one report and no other file:

```text
xmodel/d1-degree-bound-sol56-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,500 words. Do not include a `charge_basis` declaration.
