# Hostile review: D3 triple-line first-jet invariant gate

You are Fable 5, the genuinely different-model hostile reviewer for the plane
Jacobian-conjecture campaign. Work in `/Users/dc/code/math/jc2` on the exact
charged files below. The producer is provisional: reconstruct the mathematics
from the stated hypotheses and actively seek counterexamples before agreeing.
Do not infer correctness from seals, manifests, prior agreement, or campaign
status.

Charge these exact bytes:

```text
7e73b7a6ebd1c4f6529c8c4502e150de1a8b4e4664d03323bfc8631b03ab08c5
  xmodel/bd-a2-d3-triple-line-first-jet-invariant-gate-sol56-20260830.md
a389b0a700a96f1ac68f3123f19fc7fa502e31b305e0973f164e50c5d6c585bd
  xmodel/bd-a2-d3-triple-line-first-jet-invariant-gate-sol56-20260830.md.artifact.json
08c523e2b2dade813d5c12652bfc501ec02de80470f44e3763571387940e852c
  ops/d3_triple_line_first_jet_invariant_replay.py
087953ec71175d8e470cd2aa89dd7928ef0ab88223009c619e2d95dc39287637
  xmodel/bd-a2-d3-hodge-level-divisor-sol56-20260830.md
e571684152a54d9921cc38bdcb9f8833a6f875bda659cf6ebeb8877871246a87
  xmodel/bd-a2-d3-hodge-level-divisor-sol56-20260830.md.artifact.json
```

Audit the proposed first-jet gate item by item.

1. Verify the formal normal form
   `F=x^3+t(xQ(y,z)+G(y,z))+O(t^2)`. Check the unit scaling and
   parameter-dependent determinant-one coordinate change, including all
   higher terms they induce and whether the gauge can be continued
   order-by-order without changing the claimed invariant valuations.
2. Check the normality claim precisely. Under a smooth generic fibre, decide
   whether `G!=0` is necessary and sufficient for the local hypersurface
   surface to be normal; distinguish a finite singular set on the central
   line from a hidden codimension-one singular locus.
3. Reconstruct Fisher's Hessian normalization and pencil identities rather
   than trusting copied constants. Verify the `xyz` control and derive the
   exact coefficients `[t^3]c4` and `[t^4]c6`, including the sign and factor
   of the binary-cubic discriminant.
4. Audit higher-jet independence. The replay computes the seven-dimensional
   normal slice, not an arbitrary ten-dimensional direction. Decide whether
   the order-by-order gauge plus polarization really prevents `F2,F3,...`
   from changing these two leading terms.
5. Verify the invariant-to-Hodge inference with the charged D3 theorem. Keep
   the direction one-way: level two forces the `8/12` bounds, but the bounds
   are not asserted to imply level two when minimal invariants vanish. Check
   that the discriminant bound is redundant as a necessary generator.
6. Verify the `PGL2` orbit classification of nonzero singular binary cubics:
   double-plus-simple and triple root. Recompute the specializations
   `G=y^2z => q2=0` and `G=y^3 => no first-jet condition on Q`. Look for a
   missed stabilizer, zero orbit, or squarefree survivor.
7. Read and rerun the exact replay in ordinary, `-O`, and `-OO` modes. Check
   the AST-assert guard, mutation, output hash, SymPy-version dependency, and
   whether the program establishes every software-dependent claim without
   circular hard-coding.
8. Price the theorem correctly: it is a necessary local finite-jet gate, not
   arc existence, minimisation, a global class-`(3,3)` surface, a map, a
   counterexample, or JC2. Propose the cheapest decisive next stratum or
   invariant calculation on the two surviving normal forms.

Use primary or authoritative sources for any theorem you do not derive.
Return itemized `CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or `REFUTED`,
then a maximum-safe theorem, exact dependencies, and the cheapest decisive
successor. This review makes no exit-price assertion: emit no
`charge_basis={...}` line; receipt status `ABSENT` is expected. Do not run
heavy local CAS. Do not inspect, list, search, stat, build, modify, or control
`jc2-lean`. Do not read any q6 report or any sibling external-model prompt,
log, report, or receipt. Do not edit inputs, Git state, or canonical
artifacts.

Write exactly one report:

```text
xmodel/bd-a2-d3-triple-line-first-jet-invariant-hostile-review-fable5-20260830.md
```

End with one standalone `<!-- BODY-END -->` line and no seal block.
