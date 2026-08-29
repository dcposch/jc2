# Hostile review V2: repaired delayed-load affine-Faber `K` composition

Work in `/Users/dc/code/math/jc2`.  Review the immutable producer together
with its controlling nonmutating repair:

```text
6178089bb11efebb304b2eb24dca6eb654bde060396fbf4f4456f515cae28989
  xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-exclusion-20260826.md
7c731df0fdf699119973c2d9c80a7096adab40bec7fb95d70f10cf9b1009ff64
  xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-source-coordinate-addendum-v2-20260826.md
```

The intermediate addendum SHA `8b17b8c1...` has a wrong homogenization
sentence and is superseded; do not use it as controlling mathematics.

Write exactly one report to

```text
xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composite-v2-hostile-review-grok-20260826.md
```

Edit no other file and do not touch `jc2-lean`.  Rehash every charged file
used.  Do not trust producer, audit, PASS, or verdict tokens.  Use exact-Q
identities as mathematical evidence and finite fields only as software
controls.

The original hostile review was instructed to look for an omitted early
kernel/source-zero face.  This V2 assignment asks whether the controlling
repair actually closes it.  Independently verify:

1. Before strict transform, `Lambda=rho^2*L` gives the common factor
   `L^2*(6*u3-L*m^3)`; saturation for the closure of `D(Lambda)` removes
   `L^2` and leaves `6*u3-L*m^3`.
2. On `L=0`, at the repeated point `b=0`, `e=p`, `m=p*x0` with `e*m` a
   unit, the homogeneous kernel rows really give
   `u3=-2*y*h`, `u4=h^2-e*y^2`, hence every kernel coordinate vanishes;
   then check that the complementary pivots remove all remaining projective
   coordinates.  Test unequal valuations and root splitting explicitly.
3. On `L!=0`, normalization to `L=1` is licensed after ramification, the
   delayed source has `kappa=0` at this predecessor, and the reviewed
   e-open K2 unit plus the exact V3 source/analytic row bridge applies before
   any `b` localization.
4. The cases `L=0` and `L!=0`, together with an earlier complement pivot,
   exhaust all fractional relative valuations.  Look for a third face or a
   load-timing mismatch.
5. The squarefree UFD branch, repeated-point coordinate map, and narrow scope
   are unchanged.  The moving sigma-through-15 computation is corroboration
   only and must not substitute for the blowup proof.

If a gap remains, give the smallest explicit valuation/counterface and the
strongest valid narrower theorem.  Keep the firewall: no `A`, `D=0`, other
source slope, order-two, maximum-twelve, or JC2 claim.

End with exactly one standalone token: `CONFIRMED`, `REPAIR`, or `REFUTED`.
