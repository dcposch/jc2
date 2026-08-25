# Hostile review — maximum-12 parity-normal `Q12` checkpoint

Act as a hostile different-model mathematical reviewer in
`/Users/dc/code/math/jc2`. Read in full:

- `xmodel/max12-912-order3-nu-parity-normal-q12-20260824.md`;
- every file in `cases/max12_912_order3_nu_parity_normal_q12_20260824/`;
- the exact compiler file and reviewed parity theorem/review pinned by that
  case; and
- only the named reviewed Faber/order-three dependencies needed to check the
  stated scope.

Charged hashes:

```text
report    9616396705d071efac3cf52332c5007a4a045989940bcc8743a545e87f763a1c
manifest  2af02f169f4c65e7bfd3627d8f05934b0bdbdc35df1c1b9a0577f765b0a6b70e
freeze    a2d342a0d70911263a72172ba3ee02f21e33951ca9d2f4753f8de39d1dca54d0
```

Independently reconstruct and attack:

1. the involution, its fixed parity locus, and the invariant/anti-invariant
   typing of all eight rows;
2. why the displayed `4 x 4` block is the complete first-order normal block,
   including whether the loaded constraint `r6=nu` or eliminated even rows
   contribute hidden normal conditions;
3. the reversible generic-chart substitutions for `x3,x1,x5`;
4. the exact determinant, including every scalar, exponent, denominator, and
   the degree-12 polynomial `Q12`;
5. squarefreeness and every claimed gcd/coprimality, and why all non-`Q12`
   determinant factors are truly excluded on the retained chart rather than
   saturated away improperly;
6. existence of loaded algebraic points above roots of `Q12`, with the
   `r6=nu != 0` equation and constant-field/Kummer typing respected; and
7. the exact geometric conclusion licensed by invertibility: first-order
   absence of a normal tangent at a parity point, not formal trapping,
   neighborhood emptiness, exclusion of a disjoint component, or a
   maximum-twelve theorem.

Run the frozen replay, but also recompute the determinant and gcd data by an
independent implementation or direct symbolic derivation. Attack chart
boundaries, hidden denominator components, dependence of the four rows,
scheme-versus-point language, and any misuse of the already excluded parity
trajectory as though it supplied an actual base solution.

Write exactly
`xmodel/max12-912-order3-nu-parity-normal-q12-review-grok-20260824.md`.
Do not edit producer, case, canonical, coordination, or other review files.
End with exactly one verdict: `CONFIRMED`, `GAP`, or `REFUTED`, and state the
smallest failing identity or missing hypothesis if applicable.
