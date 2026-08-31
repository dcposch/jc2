# Research lane: NODAL-REALIZATION — kill or attain the six (8,6)/(9,6) types

You are a bounded primary research lane on
OPEN[ROW-(8,6)/(9,6)-NODAL-REALIZATION] (integration §2): six
AM-numerical types — (8,6) with
`(β₁; δ_∞, δ_aff; M_∞) = (21;10,11;22),(23;11,10;24),(25;12,9;26),
(29;14,7;30)` and (9,6) with `(23;22,6;25),(25;24,4;27)` — whose
in-class attainment (a genus-0 polynomial curve of that type whose
affine singularities are EXACTLY δ_aff ordinary nodes / double
points of smooth branches) is unresolved. Each type killed by
non-realization shrinks the residual; each attained type becomes a
FIXED-TUPLE target.

charged_input=xmodel/row-sweep-sol56-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb  {{LANE_INPUTS}}/row-sweep-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

For each of the six types, in the order listed: (1) re-derive the
admissibility data (delta-sequence, semigroup, gap count δ_aff);
(2) attempt a divided-difference / parametrization construction:
`p(t)` of degree d, `q(t)` of degree n with the prescribed
characteristic sequence at infinity — the double-point scheme has
length δ_aff; determine whether it can consist of δ_aff REDUCED
pairs (nodes) — the obstruction mechanisms: coincident pairs forced
by symmetry of the construction, or the double-point scheme forced
non-reduced by the infinity type (derive the discriminant structure
of H(p,q) where feasible at desk scale — no CAS: bound the analysis
to leading-coefficient/valuation arguments and exact small cases);
(3) alternatively kill by a sourced obstruction: AM semigroup
constraints, Orevkov-style negativity, or genus/Plücker-type counts
for the projective closure (the closure has degree d, one singular
point at infinity with known δ_∞ plus δ_aff nodes — check
Plücker/class formulas for consistency; fetch and hash any source
you consume); (4) verdict per type: NON-REALIZABLE (kill, with the
obstruction), REALIZED (exhibit the construction data as far as
desk-checkable), or OPEN (name the exact missing computation and
whether it is CAS-scale — if CAS-scale, spec the exact finite
computation for a possible AWS job: ring, ideal, expected size).

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 5 hours hard budget.

Write one report and no other file:

```text
xmodel/nodal-realization-86-96-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,500 words. Do not include a `charge_basis` declaration.
