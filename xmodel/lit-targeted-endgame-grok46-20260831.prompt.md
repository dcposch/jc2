# Scout lane: LIT-TARGETED — three searches that could short-circuit the endgame

You are a targeted literature registry lane (same discipline as the
trivial-dicritical registry: REGISTRY, not proofs). Three narrow
questions, each of which could collapse a running route if the
literature already answers it:

charged_input=xmodel/pi1s4-64-triple-cover-close-sol56-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
140215427ecc2fe5ba9a176aa53ede5a6d07c0e697e6d99be3541f30044bb002  {{LANE_INPUTS}}/pi1s4-64-triple-cover-close-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

1. **Unit representation of binary cubics over polynomial rings.**
   The nonmonogenic gap: a binary cubic I(S,T) over C[x,y] with
   squarefree discriminant — when does I represent a unit (I(s,t)=1
   solvable with s,t in C[x,y])? Sweep: Miranda triple-cover
   literature and its citations; Bhargava-style composition /
   cubic-ring parametrization (Gan-Gross-Savin, Delone-Faddeev over
   arbitrary base rings — Deligne's letter, Poonen's 'Rings of low
   rank'); monogenicity of cubic algebras over affine base schemes.
   Anything giving a criterion or countermodel.
2. **pi_1 of complements of (2,q)-type polynomial curves /
   fold-unions.** Complements of unions of two rational curves
   exchanged by an involution; Zariski pairs among reducible sextics
   with two quartic... precisely: two 3-nodal quartics with
   high-contact intersection — Artal Bartolo / Cogolludo / Tokunaga
   dihedral-cover literature: existence criteria for S_3/S_4 covers
   branched at such unions (Tokunaga's work on dihedral covers and
   triple covers branched at sextics is DIRECTLY adjacent — sweep it
   thoroughly; a Tokunaga-type existence/nonexistence criterion for
   the (6,4) row's sextic could decide the row outright).
3. **Certified braid monodromy in practice.** SIROCCO/Sagemath
   braid_monodromy: version status, known limitations (degree,
   reducibility, vertical tangents), published computations at
   comparable scale; alternatives (Bettini-Marco? libbraiding).
   Practical notes for the queued AWS job.

For every statement: exact source, hash of the fetched PDF, verbatim
scope, and what it yields (CLOSES / PARTIAL / STRUCTURE / NOTHING)
for the named question. End with verdicts per question and an
acquisition list.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 4 hours hard budget.

Write one report and no other file:

```text
xmodel/lit-targeted-endgame-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,500 words. Do not include a `charge_basis` declaration.
