# Research lane: SHAPE-3-FINISH — the non-constant (4,3)-scaled stratum

You are the flagship lane on OPEN[SHAPE-3-ALL-g]: family 3
((d,n) = (4g,3g), outer coprime (4,3)), non-constant stratum, where
the reviewed SK-5 pins Π to a 3-CYCLE — so the S_3-resolvent does
NOT descend (psi(gamma_inf) is a 3-cycle, nontrivial) and the
ROW-KILL projective mechanism fails structurally. Find the kill or
pin the residual:

charged_input=xmodel/shape-kill-uniform-opus5-20260901.md
charged_input=xmodel/shape-kill-hostile-review-grok46-20260901.md
charged_input=xmodel/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
189bc45d83c97df3614c65450a8c6e926938e50f7ccc0b2bacd78a7fd8d11c4d  {{LANE_INPUTS}}/shape-kill-uniform-opus5-20260901.md
0213fcae67bbde4d426a50f2d5d17c71db907d78718860459f14ff50e2ce4a01  {{LANE_INPUTS}}/shape-kill-hostile-review-grok46-20260901.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  {{LANE_INPUTS}}/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Routes: (1) Π a 3-cycle means the degree-4 cover's boundary
monodromy is a 3-cycle: the cover extends over the infinity place
with ONE branch point of local degree 3 + one unramified sheet —
run the promoted chi_c/covering machinery on the EXTENDED projective
cover (Y-bar -> P^2 branched at Dbar + possibly L_inf: with
psi(gamma_inf) a 3-cycle the S_3 triple cover IS branched at
infinity — classify normal triple covers of P^2 branched at
Dbar ∪ L_inf: branch degree 4g+1 — odd! — versus the Cardano parity
constraints: derive whether a normal S_3 cover with branch
degree 4g+1 and the L_inf component simple can exist — Tokunaga T91
/ Shirane-style: the branch divisor of a triple cover has a Z/3
structure constraint on components with inertia 3 versus 2 —
L_inf's meridian maps to a 3-CYCLE (inertia Z/3, total branch)
while D's meridians map to transpositions (inertia Z/2, simple
branch) — a MIXED triple cover: fetch the mixed-branching triple
cover classification (Tokunaga's Cardano paper handles this via
the different exponents in the building data) and derive the
constraint; (2) alternatively the A-side: Theorem A at outer
coprime (4,3) gives the order fork — combine ord(Π)=3 with the
promoted divisibility (3|n', d' parity) and the inner-cable
fixedness at general g; (3) verdict: KILLED uniformly / a finite
list of surviving (g, configuration) pairs / OPEN at a named
classification input.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 5 hours hard budget.

Write one report and no other file:

```text
xmodel/shape-3-finish-opus5-20260901.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,500 words. Do not include a `charge_basis` declaration.
