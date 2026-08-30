# Hostile review: `RULE-ON-Y` for a proper intermediate block

You are Fable 5, the genuinely different-model hostile reviewer for the plane
Jacobian-conjecture campaign.  Work in `/Users/dc/code/math/jc2` on the exact
charged files below.  The producer is provisional: reconstruct every theorem
from its actual hypotheses and search for counterexamples before agreeing.
Do not infer correctness from seals, manifests, canonical ledgers, or prior
model agreement.

Charge these exact bytes:

```text
acfcd839a4f7af77c54a75bc30c2909f26c6afb8ec35b1862dc685e27b270819
  xmodel/block-descent-a1-ruling-transfer-audit-sol56-20260830.md
b52d063d2801885c30fe92212b86d9cda1de7c97a6438a3cc1d243de1c6b30bc
  xmodel/block-descent-a1-ruling-transfer-audit-sol56-20260830.md.artifact.json
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
f092a7152dea8bdee387825fa8181dffeb8145fc99cf65973d74f528491f57a0
  xmodel/bd-a2-a1-ruling-euler-boundary-cap-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
```

The charged block theorem conditionally supplies a hypothetical proper
intermediate factorization

```text
A2 --g1, etale quasi-finite dominant--> Y
   --g2, finite flat surjective--> A2,
```

where `Y` is an integral normal affine complex surface,
`R=NonEt_Y(g2)` is the full **source** non-etale support, `R` is nonempty and
pure of codimension one, and

```text
g1(A2) subset Y_sm minus R,       Sing(Y) subset R.
```

Audit the proposed conclusion for `U=Y minus R` item by item.

1. Verify affineness without using the false rule "open in affine is
   affine."  Check the report's Nagata theorem in the exact Weil-divisor,
   excellent-normal-surface generality.  Also test the stronger direct route:
   Stacks Project Theorem 58.29.3, Tag `0ECD`, asserts affineness of the
   maximal etale locus for a finite-type map from a normal scheme to an
   excellent regular scheme over a field.  Decide whether it applies
   literally to `g2:Y->A2` and whether it removes the dimension/purity and
   nonempty-divisor dependencies.
2. Test all edge cases: Weil versus Cartier, support versus multiplicity,
   non-Q-factorial `Y`, empty non-etale locus, a codimension-two residue, and
   deletion of only selected ramification components.  Check the relevant
   purity statement rather than assuming it.
3. Verify that `g2|U` is etale and hence `U` is smooth, and that the actual
   `g1` factors dominantly through `U`.  Keep source ramification, target
   discriminant, its inverse image, and the first-leg image distinct.
4. Reconstruct the dominant-generically-finite/log-ramification argument
   giving rationality or unirationality, `O(U)^*=C^*`, and
   `bar-kappa(U)=-infinity`.  Check the direction of every inequality and
   whether quasi-finiteness/etaleness of `g1` strengthens or changes it.
5. State the exact Miyanishi--Sugie theorem consumed.  Verify that its output
   is an actual surjective `A1`-fibration `rho:U->C` over a smooth curve over
   `C`, not merely a cylinder on an open subset or a fibration after field
   extension.  Identify any separate extension theorem needed.
6. Verify the deduction `C=A1 or P1` from rationality and units, including the
   possibility of a projective base for an affine total surface.  Audit the
   Gurjar--Miyanishi assertion that every **reduced** fibre is a disjoint union
   of affine lines and state exactly what remains uncontrolled about
   multiplicities.
7. Attempt explicit controls and counterexamples: punctured normal surfaces,
   non-Cartier divisor complements, target-discriminant deletion that loses an
   unramified sheet, and any smooth affine `bar-kappa=-infinity` surface for
   which the asserted global fibration/base statement would fail.
8. Decide precisely what transfers outside the quadratic presentation and
   what does not.  No qualitative ruling may import the quadratic Euler
   number, Picard cap, boundary rank, `D9` marking, finite-presentation
   occurrence, or a conclusion about the primitive/no-proper-block sector.

Use primary or authoritative sources for each named theorem.  The following
source leads are permitted but are not conclusions: Stacks Tags `0ECD`,
`0EB7`, `0EA4`, and `0AH7`; Nagata's 1956 Hilbert-14 paper; Miyanishi--Sugie,
Kyoto J. Math. 20 (1980), DOI `10.1215/kjm/1250522319`; and
Gurjar--Miyanishi, Michigan Math. J. 53 (2005), DOI
`10.1307/mmj/1114021083`.  Cite exact theorem statements and distinguish your
own deductions.

Return itemized `CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or `REFUTED`,
then a maximum-safe theorem, exact dependencies, and the cheapest decisive
successor.  This review makes no exit-price assertion: emit no
`charge_basis={...}` line; receipt status `ABSENT` is expected.  Do not run
heavy local CAS.  Do not inspect, list, search, stat, build, modify, or control
`jc2-lean`.  Do not read any q6/D3 report or any sibling external-model
prompt, log, report, or receipt.  Do not edit inputs, Git state, or canonical
artifacts.

Write exactly one report:

```text
xmodel/block-descent-a1-ruling-transfer-hostile-review-fable5-20260830.md
```

End with one standalone `<!-- BODY-END -->` line and no seal block.
