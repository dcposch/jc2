# Hostile review: generic-square vertical `c=3` divisibility lemma

You are the hostile mathematical reviewer for one sharply scoped conditional
lemma in the plane Jacobian-conjecture campaign.  Work read-only except for
writing the single requested report.  Do **not** run Singular, Sage, Lean, a
solver, or a substantive symbolic Python computation on this Mac.  Small
textual inspection, checksum verification, and hand algebra are allowed.  Do
not inspect `jc2-lean`, broad repository state, unrelated campaign files, or
any live `.run` transcript.

Write exactly one report:

`xmodel/max12-812-order2-square-c3-divisibility-review-grok-20260826.md`

The producer target is

`xmodel/max12-812-order2-square-c3-vertical-residue-lemma-20260826.md`

with SHA-256

`dd4005a92440e8241807bbe3bea4f9305de06c2d08fd0e095dc5dddba4bc7707`.

## Files licensed for inspection

Inspect the producer target and only these source/provenance files as needed:

- `cases/max12_812_order2_square_owner_cge3_universal_20260826/REGISTRATION.md`;
- `cases/max12_812_order2_square_owner_cge3_universal_20260826/compile_cge3_universal.py`;
- `cases/max12_812_order2_square_a_prolongation_owner_v2_20260826/RESULT.md`;
- `cases/max12_812_order2_square_a_prolongation_owner_v5_ptangent_validator_20260826/RESULT.md`;
- `xmodel/max12-812-order2-square-horizontal-contact-raising-design-20260826.md`;
- `xmodel/max12-812-order2-square-fan-lower-hull-reduction-20260826.md`.

The universal AWS jobs are still live, so this review is of the conditional
algebraic implication only.  Do not infer or claim that the complete
source/Faber bridge has passed merely from compiler source or prior adjacent
results.

## Load-bearing questions

Give a verdict `CONFIRMED`, `REPAIR`, or `REJECTED`.  Identify the smallest
failing identity or missing hypothesis.

1. Verify the producer SHA.  Re-expand the frozen rational receiver after
   `A=A0+sigma*A1+sigma^2*A2`,
   `C=sigma^3*E3+sigma^4*E4+sigma^5*E5`,
   `R=sigma^2*B2+sigma^3*B3`,
   `L=L0+sigma*ell1+sigma^2*ell2`, and
   `k=k0+sigma*k1`.  Check every coefficient and sign in `H13,H14,H15`.
2. Check that `kR3,kRC,kR2A` and all other registered terms really occur
   after grade 15 for `c=3,r>=2`; distinguish `r=2`, `r=3`, and `r>3`.
3. Conditional on the complete lower-unitriangular source/Laurent bridge and
   zero source rows, verify that polynomiality of each `H13,H14,H15` is the
   licensed conclusion.  Attack any hidden mixing of earlier polynomial
   parts or moving-`L` corrections.
4. On `D(p)`, verify squarefreeness of `L=z^2+p/2` in characteristic zero.
   From `L|A0*E3` with nonzero linear `A0,E3`, justify the etale root
   allocation, including possible scalar factors and deck swap.
5. Form `N14=L^2 H14`.  Verify exactly that
   `N14=-(3/8)B2*A0^2 (mod L)` after the grade-13 relation, and that
   polynomiality forces the complementary root factor to divide `B2`.
   Check both `r=2` and the specialization `B2=0` for `r>=3`.
6. Form `N15=L^3 H15`.  Reduce at the complementary root.  Verify that every
   term other than `-(1/16)A0^3` vanishes using only `L|A0*E3` and the
   grade-14 divisibility of `B2`, and that the cubic is nonzero there.
7. Audit descent/base change: ensure passing to a splitting field or etale
   algebra cannot create a false contradiction, and that no reducedness,
   radical, or global ideal-membership assertion is being smuggled in.
8. Enforce scope.  Even if confirmed, this is only the conditional
   `a=0,c=3,r>=2` vertical gate on `D(p*k0)` after its stated predecessors.
   It does not certify the still-live source replay, any horizontal fan,
   `p=0`, the square branch, order two, maximum twelve, or JC2.

State whether the clean divisibility proof is sound as a conditional theorem
and what exact computational evidence is still required before promotion.
End with exactly one of:

`ORDER2_SQUARE_C3_DIVISIBILITY_CONFIRMED`

`ORDER2_SQUARE_C3_DIVISIBILITY_REPAIR`

`ORDER2_SQUARE_C3_DIVISIBILITY_REJECTED`
