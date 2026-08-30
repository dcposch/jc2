# Bounded hostile review: reduced bidegree-(2,3) rational-forest classification

You are Fable 5, an independent hostile mathematical reviewer for the plane
Jacobian-conjecture campaign. Work in `/Users/dc/code/math/jc2` on frozen git
basis `201b848b4422225f9514145c9c9655b635564404`.

Review the following provisional sealed classification in full at its stated
scope, using the promoted first-leg theorem only as an input:

```text
d783cecfcc818f1ec5c056fa04126c21dab0f17c073d11d8e230703b9755feaa
  xmodel/bd-a2-firstleg-bidegree23-rational-forest-classification-sol56-20260830.md
  body 13761 / b76971e671237b906d4c772ec4008e7153ca6f47705cc994839fef33c12a604e
6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08
  xmodel/bd-a2-rational-forest-coordinator-integration-sol56-20260830.md
  body 6810 / 9c6501222049980161f209d57e1a575ebe80c4de1b8018aedf303f692e1dae46
```

Independently reconstruct and adversarially check:

1. For a reduced divisor `C` of class `(2,3)` on `P1 x P1`, prove the
   connectedness input and derive exactly
   `2=G(C)+B(C)+sum_p(delta_p-r_p+1)`. Audit whether the embedded-resolution
   dual multigraph is a forest exactly when the right singularity contribution
   equals two, including reducible, disconnected-normalization, multi-branch,
   and nonordinary singularities.
2. Re-enumerate all unordered partitions of component bidegrees with
   nonnegative entries summing to `(2,3)`, subject to reducedness and
   irreducibility of each component. Confirm that the report's nine types are
   exhaustive and nonduplicative; identify any missing vertical/horizontal,
   repeated-class, or disconnected possibility.
3. For each types F1--F7, verify both necessity and realizability of the exact
   cusp, tangency, and intersection-coalescence conditions. Recompute every
   genus and intersection budget. Check that the proposed explicit examples
   have the claimed bidegrees, are reduced/irreducible where asserted, and
   exhibit exactly the stated local singularities, including both
   irreducible F1 parametrizations (two `A2` cusps and one `A4` cusp).
4. For F8 and F9, prove impossibility from the exact budget rather than a
   generic-position heuristic. Check all ways several pairwise intersections
   can coalesce at one point and all allowed singularities on individual
   components.
5. Audit the report's Miranda translation. Keep distinct: a common zero of
   coefficient sections on the affine base, a fixed fibre root, a
   nonreduced/repeated component at infinity, singular infinity support,
   projective coefficient basepoints, literal fibre-degree drop, and target
   coefficient-degree drop. Determine exactly which reduced fixed-basis
   quadratic strata this classification covers.
6. State the maximum campaign consequence. The rational-forest theorem gives
   only a necessary first-leg condition; this classification must not be
   upgraded to a ramification-support exclusion, general quadratic-block
   closure, primitivity, map existence/nonexistence, a counterexample, or
   JC2. List the cheapest finite successor invariant that could eliminate or
   realize the seven surviving types.

Return an itemized verdict (`CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or
`REFUTED`), the maximum exact theorem safe to promote, any corrected type
table, and precise counterexamples to any false row. Do not merely agree with
the producer.

Hard output cap: at most 8,000 tokens and at most 28,000 UTF-8 bytes. Do not
restate long inputs. Do not inspect, list, search, stat, build, modify, or
control `jc2-lean`; the process sandbox also enforces this. Do not run local
heavy CAS or Singular. Do not edit any input, canonical file, script, or
dependency. Write exactly one report:

```text
xmodel/bd-a2-bidegree23-rational-forest-classification-hostile-review-fable5-20260830.md
```

End with one standalone `<!-- BODY-END -->` line and no seal block.
