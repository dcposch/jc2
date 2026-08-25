# Hostile scope review: classical closure of strict fixed-total-D12 lanes

Write the verdict to
`xmodel/fixed-total-d12-classical-closure-review-claude-20260825.md`.
Do not mutate producer files and do not run substantive computation locally.

Audit this proposed campaign-routing correction from primary sources and the
frozen local evidence.

1. Guccione--Guccione--Valqui, arXiv:1401.1784v3, states that over a
   characteristic-zero field every counterexample `(P,Q)` has
   `gcd(deg_total P,deg_total Q)>=16`.  Check the paper's definition of
   counterexample, whether the result applies to every counterexample or
   only a specially minimal representative, and descent/base-extension to
   `Q_3` or a finite extension.

2. Check the exact scopes in:
   - `xmodel/as-b9-max12-leading-shear-q8-interface-audit-v2-20260825.md`
   - its Grok review;
   - `cases/max12_912_order1_binary_cubic_bands_aws_20260825/PREREGISTRATION.md`;
   - `xmodel/ideation-20260825T1700Z-synthesis.md`;
   - the normalized B9 common-cubic producer/reviews.

   Decide whether the strict boxes really have actual total degree pairs
   `(9,12)` and `(8,12)`, rather than merely partial-y degrees or weighted
   degrees.  Check that their gcds are 3 and 4.

3. If so, decide whether these strict boxes are already closed as possible
   JC2 counterexamples, regardless of whether automorphic Keller pairs may
   exist in the boxes.  Separately decide what may be concluded about exact
   all-depth B8/B9 lifts when the reviewed residue-ball theorem would make
   such a lift noninjective.  Do not silently use special-fibre
   noninjectivity as characteristic-zero noninjectivity.

4. Check the compactness statement carefully: a fixed finite support and a
   genuinely prefix-compatible, finitely branching nonempty tower at every
   3-adic depth yields a `Z_3` coefficient limit satisfying the exact
   determinant identity.  Distinguish this from unrelated nonempty sets at
   each depth or one incomplete parent chart.

5. State the allocation consequence.  Is continued deep Singular/Z3 work on
   the strict `(9,12)` and `(8,12)` boxes only a method/control exercise for
   JC2, while the broad partial-y `(9,12)`/`(8,12)` cells with unbounded total
   degree remain live?  Identify any valid transfer of the new fractional-
   power recurrence to those broad or weighted cells.

Use only primary sources for external mathematical claims.  Return
`CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REJECTED`, list every scope defect,
and give the strongest safe routing theorem.  Do not claim maximum-12, a
counterexample, or JC2.
