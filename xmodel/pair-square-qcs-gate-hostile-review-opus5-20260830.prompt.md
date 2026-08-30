# Hostile review: `PAIR-SQUARE-QCS/v1` curve/augmentation gate

You are Opus 5 acting as a different-model hostile reviewer for the plane
Jacobian-conjecture campaign.  Work autonomously in
`/Users/dc/code/math/jc2` on frozen basis
`0d7544ebd5cb12def6bac892646010301098be3c`.

Review in full:

```text
c02c11732defca176da0ce63f71017eb497d1cf56f213a6fa2d6b6d9571f6bfa
  xmodel/pair-square-qcs-gate-sol56-20260830.md
  body 14967 bytes / 06669e22077e4b784b0490d4150ff9aa1a54900087d37d8135bf44d0635bc52a
```

Charge its exact dependencies and controls as named in section 1.  The report
claims exact curve-level pair-square lemmas and returns QCS OPEN; it does not
claim QCS, a selector, a map, or JC2.

Independently reconstruct and attack:

1. custody, hashes, seal, and the exact residual-Cartier-divisor formulation
   for `Cbar x_(P1) Cbar`; distinguish the residual before normalization from
   its normalized pullback/pushforward zero-cycle;
2. the local contact length `e-1`, global Riemann--Hurwitz length, and whether
   tame coordinates or singular residual components hide multiplicity;
3. the Keller specialization `dg(-f_y,f_x)=1`, absence of affine
   ramification, pole length `d-s`, and the identification of generic
   finite-end local degrees with `b_i`;
4. every displayed identity separating pole contact `d-s`, finite contact
   `sum d_i(b_i-1)`, quotient collision `sum b_i(d_i-1)`, and one baseline
   per quotient line `sum b_i`;
5. the augmentation representation, fixed/moving dimensions, direct sum,
   and the equivalence between existence of a merely abstract transverse
   `B` and QCS itself;
6. whether the report is too pessimistic: try to construct a canonical
   sheet-labelled `B` from normalized off-diagonal branches, local inertia,
   braid descent, or the actual polynomial source.  Conversely test root
   choices, support overlaps, the missing constant-on-support direction,
   and failure to land in `im(sigma_infinity-1)`;
7. the degree-six passport and block-overlap controls, respecting the prior
   warning that the local germ/passport are not one glued polynomial-family
   packet;
8. the exact sharp successor.  Decide whether
   `OPEN(BASELINE-TO-POLE MAP BEFORE INJECTIVITY)` is correct, should be
   stopped, or can be advanced to an explicit construction.

Return itemized `CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or `REFUTED`
verdicts and maximum safe scope.  No local heavy CAS or Singular.  Do not
inspect, list, search, stat, build, modify, or control `jc2-lean`.  Do not
edit canonical files, scripts, or reviewed inputs.  Write exactly one report:

```text
xmodel/pair-square-qcs-gate-hostile-review-opus5-20260830.md
```

End with one standalone `<!-- BODY-END -->` line and no seal block.  Keep
actual maps, curve covers, formal quotient packets, flags, places, sheets,
and series distinctly typed.
