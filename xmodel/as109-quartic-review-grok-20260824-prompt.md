# Hostile different-model review — AS109 QUARTIC-Y NO-GO

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer/review artifacts on top.

Read in full:

- `xmodel/as109-quartic-discriminator-gate-20260824.md`
- every file under `cases/as109_quartic_discriminator_20260824/`
- the reviewed cubic producer/review and the banked AS109 Hensel/carry
  materials cited by the report
- local primary/secondary material cited for priority hygiene only; do not
  infer attribution or novelty from a search snippet

Frozen hashes:

- report: `8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276`
- replay: `84fc5c3197490a405955220f95ca6f1777b0b47cc124b3763dbe158375e2e35e`
- freeze: `7f9b4c6795c74531b0fea9204133565d925427c5ce82347624ec3ee89d1b914a`

Independently rerun the replay and attack exactly:

1. Exhaust all actual top-degree patterns for `deg_y f,deg_y g<=4`, including
   equal degrees, zero/affine cases, target row reductions, and the `(1,4)`
   and `(2,4)` shears. Check that the cubic base is either correctly reproved
   or consumed only through its confirmed scope.
2. In the genuine `(3,4)` case, recompute the two highest Jacobian
   coefficients, the UFD valuation step `a3=alpha*h^3,b4=beta*h^4`, all
   constant target scalings/additions, and alignment of the two rational
   depression shifts. Look for a lost zero-leading-coefficient or descent
   case.
3. Starting from
   `f=z^3+u*z+v`, `g=z^4+a*z^2+b*z+c`, independently recompute the full
   Jacobian. In particular verify the corrected five coefficient rows

   ```text
   4u'-3a'
   4v'-3b'
   2a u'-3c'-u a'
   b u'+2a v'-u b'
   b v'-u c'
   ```

   including the formerly vulnerable `z^1` row, every sign, and the factor
   from `z=h*y+r`.
4. Derive independently the normalization
   `a=4u/3+alpha`, `b=4v/3`,
   `c=2u^2/9+2alpha*u/3+gamma`, the conserved product
   `(4u/3+2alpha)*v=delta`, and the constant Jacobian row. Audit every branch,
   especially `q=0`, `v=0`, `delta=0`, and constant/nonconstant `h`.
5. Attack the polynomiality argument from the polynomial constant terms.
   Re-derive `S,E,L,M`, the linear relation `L*u=M`, and the eliminant
   `M^2+3alpha*M*L-(9/2)E*L^2=0`. Check its degree, nonzero leading
   coefficient, treatment of `L=0`, and that after scaling it is monic over
   `Kbar[x]`, so integrality and integral closure really force the rational
   depression and coefficients into `Kbar[x]`. Seek hidden denominators or
   circular use of the conclusion.
6. Verify the final unit-product contradiction in every conserved-product
   branch and descent of automorphy from `Kbar` to an arbitrary
   characteristic-zero field. Confirm no rational source-coordinate change
   is being treated as a polynomial automorphism.
7. Recheck the AS109 consequence: both correction `y`-degrees at most four
   imply coordinate `y`-degrees at most four over `Q_109`; field automorphy
   contradicts the already reviewed residue-ball Hensel noninjectivity.
   Carries, marked sections, and finite-support restrictions must be absent.
8. Priority: report only what accessible primary material actually supports.
   Mathematical confirmation must not depend on a novelty claim.

Try hard to construct an exact counterexample or isolate the smallest missing
hypothesis. Do not edit producer or canonical files, continue to quintic
supports, or launch AWS.

Write exactly one file:

`xmodel/as109-quartic-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
full hashes, independent algebra/replay, descent and priority caveats, exact
scope exclusions, and promotion advice.
