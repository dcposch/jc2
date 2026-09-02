# Check lane: SUBRECT-ORBIT-BRIDGE — verify the closure against the primary sources

The charged desk report (GPT-5.5) closes OPEN[SUBRECT-ORBIT-BRIDGE] YES:
every counterexample that is degree-minimal for D = max(deg P, deg Q)
in its full Aut(C^2) × Aut(C^2) orbit admits GGV's standard
subrectangular gauge preserving both coordinate degrees, because the
subrectangularising source automorphism supplied by van den Essen's
book (Cor. 10.2.21, after Makar-Limanov) must be affine linear — a
non-linear one would have an inverse lowering the degree, contradicting
minimality — and GGV's global-B minimality is replaced by orbit
degree-minimality; hence nu(F_min) = 2 (the top form of the max-degree
coordinate has exactly two distinct roots), E_0 is a free vertex of the
polar tree, and integration #14's vacuity of CH2 is unconditional at
every N. The report also separates this from the invalid short argument
"linear change + leading-form theorem" (which cannot turn >= 3 roots
into x^u y^v).
Your task (different-model check, primary sources): (1) state van den
Essen Cor. 10.2.21 (Polynomial Automorphisms and the Jacobian
Conjecture, 2000) exactly — hypotheses, the automorphism it supplies,
what it says about degrees and the shape (a <= b, the "subrectangular"
support) — from refs/ if present (hash) or with exact citation; (2)
verify the affine-linearity argument: does degree-minimality in the
Aut × Aut orbit really force the supplied automorphism to be affine
linear, or could a non-linear automorphism preserve max(deg P, deg Q)
while changing the shape (state the exact degree bookkeeping under
composition with a triangular automorphism, both sides)? (3) confirm
that GGV's Prop 4.7 / Definition 4.3 use only the subrectangular input
and not global-B minimality for the conclusion nu = 2 (the top form is
a monomial x^u y^v, u, v >= 1) — read GGV's text in refs/
(guccione_valqui2017_ja471_shape_counterexamples.pdf; hash it); (4) test on
controls: an automorphism composed to have a two-root top form; a
one-root top form (x, y + x^k) and why it is not degree-minimal; the
(LF) normal forms; (5) deliver CONFIRMED / GAP / REFUTED with a
promotion recommendation and the exact scope sentence for AUDIT. Desk
only; state the bounded quantity of any OPEN you raise; do not edit
canonical ledgers; do not inspect jc2-lean.
Report: xmodel/subrect-orbit-bridge-check-grok46-20260902.md
Seal-at-completion; bounded writes; target 8-15KB; 60 minutes.
charged_input=xmodel/subrect-orbit-bridge-gpt55-20260902.md
charged_input=xmodel/minimal-keller-shape-review-gpt55-20260902.md
charged_input=xmodel/integration14-coordinator-fable51-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
75ee84f89fdb5abcc6e8f51654c618de469ae06b32d7d7a1911c5f9d6e9602c7  {{LANE_INPUTS}}/subrect-orbit-bridge-gpt55-20260902.md
b1e09351164c134ec8aa74a7b905678e70021155b23add5bec9994e9f1268ac1  {{LANE_INPUTS}}/minimal-keller-shape-review-gpt55-20260902.md
bf1d428c7ddc03ab002410174b995cdd01e8a3c76c52475b03faf959b33da2ca  {{LANE_INPUTS}}/integration14-coordinator-fable51-20260902.md
```
