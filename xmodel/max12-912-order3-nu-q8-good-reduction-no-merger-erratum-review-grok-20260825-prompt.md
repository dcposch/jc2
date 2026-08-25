# Hostile review: repaired selected-Q8 good-reduction no-merger lemma

Act as an independent hostile algebraic geometer. Work read-only except for
the one output file named below. Do not browse, use a shell, access the
network, or run computation. Read in full:

- `xmodel/max12-912-order3-nu-q8-good-reduction-no-merger-lemma-20260825.md`
- `xmodel/max12-912-order3-nu-q8-good-reduction-no-merger-erratum-20260825.md`
- `xmodel/max12-912-order3-nu-q8-generic-length-degree-one-lemma-20260825.md`

The original lemma is expressly superseded. Review the erratum only as a
conditional abstract theorem and discharge checklist; none of its Q8
computational hypotheses is assumed complete.

Try to refute every load-bearing point:

1. Verify the explicit counterexample to the original wording, including
   the special/generic irreducible components, flatness and reducedness at
   the generic point of `C`, and why two distinct horizontal axes meet the
   marked point through the higher-dimensional vertical component.
2. Audit the corrected hypothesis: `C` must be the unique irreducible
   component of the special fibre through each marked point in every
   dimension. Determine whether regular completed local ring `k[[w]]` is a
   sufficient stronger replacement.
3. Check the proof that `A=O_(X,eta_C)` is a domain from DVR-flatness and
   `A/pi A` a field. Attack the Krull-intersection step, dimension claim,
   excellence assumption, and behavior after a common finite DVR extension.
4. For a geometric generic curve component `Y_i`, audit its
   scheme-theoretic closure `Z_i`: dominance/flatness over the DVR, special
   fibre dimension, passage from `q_i` to a component dense in `C`, and the
   conclusion that all generic components give the same prime. Look for
   hidden properness, catenarity, equidimensionality, or normalization
   assumptions.
5. Decide whether the checklist correctly separates: the common integral
   source scheme; actual mod-127 component and generic multiplicity; all
   eight full contacts and local uniqueness; integral specialization of
   each characteristic-zero branch; and identity with the components used
   by the primitive-grouping/infinity theorems.
6. Enforce scope. Even if the abstract lemma is correct, it proves nothing
   until every checklist item is separately certified. It gives no landing,
   maximum-twelve, or JC2 conclusion by itself.

If false, give the smallest counterexample. If repairable, state the minimal
hypotheses and replacement proof. Keep the report concise enough to complete.

Write only
`xmodel/max12-912-order3-nu-q8-good-reduction-no-merger-erratum-review-grok-20260825.md`.
End with exactly one verdict token on its own line:

```text
CONFIRMED
CONFIRMED_WITH_REPAIRS
INCONCLUSIVE
REFUTED
```
