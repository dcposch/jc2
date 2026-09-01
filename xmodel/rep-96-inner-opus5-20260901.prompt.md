# Research lane: REP-96-INNER — the (9,6) representation question (family 2, g=3, inner case)

You are the new keystone flagship. Context: the encoding audit
(charged) vacated all six N=4 realization-suite verdicts and
EXHIBITED an explicit realization of type Delta=(9,6,2): the
curve q=t^6+8t^2, p=t^9+12t^5+24t satisfies p^2-q^3-64q=64t^2
exactly (coordinator desk-verified: identity exact, gcd(p',q')=1,
exactly 4 affine nodes at 4 distinct image points, and the
identity itself exhibits the pole-order-2 generator, so
Delta=(9,6,2) with one place at infinity is REALIZED). A
corrected (9,6,4) locus is NONEMPTY (its point is the HF-twin
curve); its six-node question is open. Consequence: the (9,6) row
CANNOT die at the curve level. It dies at the S_4 representation
level or not at all.

(9,6) = (3*3, 2*3): g=3, outer pair (3,2) — family 2 (odd u=3,
nbar=2) at g=3, which is exactly OPEN[SHAPE-2-INNER-g>=3] (named
in the charged prebuild, which resolved family 3 at g=2 by the
tube-braid divisibility gate; the family-2 g=2 case A'(5) was
held as a GAP there — read its sections 3 and 5 for why, and do
not repeat that error pattern).

Task:
(1) Reconstruct the family-2 block/cable structure at g=3 for
    (9,6): Pi-blocks, rho_inf word, the cable exponent e(iota)
    analogue. Derive the divisibility/obstruction gate for this
    family if one exists — the prebuild's family-3 gate came from
    3 | e(iota) on the rho_inf-fixed tuple condition; derive the
    correct family-2 analogue at g=3 honestly (do NOT transplant
    the family-3 formula; the block periodicity differs — family
    2 at g=2 has 2-periodic block products, determine the g=3
    structure from scratch).
(2) Apply it to both live (9,6) types: Delta=(9,6,2) (delta_aff=4,
    beta_1 and delta_inf: recompute from the Galindo conversion
    yourself and state them) and Delta=(9,6,4) (six-node target).
    Verdict per type: rep-level KILLED / survives gate / OPEN at
    a named finer input.
(3) CRITICAL FORK — if (9,6,2) SURVIVES the representation gate:
    the realized curve is then the campaign's strongest
    counterexample-candidate substrate ever. State precisely what
    remains between "realized numerical type + surviving S_4
    representation" and "Keller map exists": the covering-space
    realization (Riemann existence step), the b=0/budget
    constraints from the charged rowkill integration, and the
    (M') identity. Check the realized curve's data against EVERY
    binding constraint in the rowkill integration — does any
    already-promoted theorem kill (9,6,2) on other grounds
    (torus-type exclusion, INF-TRIVIAL even-word, Shirane Cor
    0.6, N-A)? Be exhaustive; a missed applicable kill here costs
    the campaign a false alarm, a falsely-applied kill costs a
    missed counterexample.
(4) Typed verdict block, OPENs named, deviations logged.

Rules: hostile-review standard; no raw-remainder-degree
substitutions; cite charged inputs by section; observed
timestamps only.
charged_input=xmodel/row-86-prebuild-opus5-20260901.md
charged_input=xmodel/encoding-faithfulness-audit-r2-sol56-20260901.md
charged_input=xmodel/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
7247cef3961576b9919a2ca6e67c484f9f84e6e0af5bca4ceaa353d900bbd4ed  {{LANE_INPUTS}}/row-86-prebuild-opus5-20260901.md
a3c7137cdb2cf46c7d9026cfbcba54b0b6e5b47a6ef36ad7ee2976a905c8b196  {{LANE_INPUTS}}/encoding-faithfulness-audit-r2-sol56-20260901.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  {{LANE_INPUTS}}/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
```

Write your report to `xmodel/rep-96-inner-opus5-20260901.md`.
Seal-at-completion contract: write the skeleton WITHOUT the
BODY-END marker, fill sections with bounded per-section writes,
seal only at completion via ops/seal.py. Pace structurally: this
must fit well inside the output budget — target 25-35KB body.
