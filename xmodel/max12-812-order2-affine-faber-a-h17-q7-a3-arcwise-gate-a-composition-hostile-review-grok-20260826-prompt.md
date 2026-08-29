# Hostile review: H17/q7/a3 arcwise Gate-A composition

Work in `/Users/dc/code/math/jc2`.  Write the unique report

```text
xmodel/max12-812-order2-affine-faber-a-h17-q7-a3-arcwise-gate-a-composition-hostile-review-grok-20260826.md
```

Do not edit charged artifacts, shared ledgers, or `jc2-lean`.

Charged provisional theorem:

```text
266d85ca49aae4b893e0514a3ab1bf271c688ce54295ae20f414675a8c401bc3
  xmodel/max12-812-order2-affine-faber-a-h17-q7-a3-arcwise-gate-a-composition-theorem-20260826.md
```

Charged reviewed dependencies include:

```text
56123a6f2b110284871fe65d664ffed89cb5004d1498e59a81719c2278c59f23
  xmodel/max12-812-order2-square-normal-first-block-divisibility-bridge-theorem-20260826.md
85389a28a69b5e030fa689ccce9dcccee484dae9169679053d0870cfe1e9f0ff
  xmodel/max12-812-order2-square-normal-first-block-divisibility-bridge-hostile-review-grok-v2-20260826.md
1da9974dde45fd73c757eb315d50bc9e8abaa028ebb8d5894ca2ea4b2bd6d2de
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-review-grok-20260826.md
465f53cd423d94645f0b99f4e96d18853bb469b96dc2f85590dc7fe912d158ec
  xmodel/max12-812-order2-affine-faber-a-h17-q7-a3-sequential-g51-hostile-review-grok-20260826.md
```

The normalized all-orders theorem is under a separate review; treat the
Gate-A conclusion as conditional on it and do not review that theorem by
assumption.

Independently attack:

1. On the literal delayed ray `Lambda=sigma^3`, check exact powers: normal
   order 17 gives unloaded quadratic grade 34, loads/`mu2` grade 42,
   cubic grade 51, and targets 48/54/57.  Confirm no omitted correction can
   tie the first block.
2. Apply the ordinary-first-four bridge to
   `Q0=z^2(z^2+p)` and prove/refute `N0=m*z*(z^2+p)` on `D(p*m)`.
3. Verify both directions and every sign in the factored-normal affine
   coefficient map (3.1)--(3.2).  Audit the split into q=7 kernel and
   order>=14 complements; identify any hypothesis that is merely assumed
   rather than forced.
4. Check that the load graph and all target timings make the literal source
   rows coefficientwise identical to the frozen normalized graph.  Look for
   a lowercase/capital load or effective-target scaling error.
5. Audit the strict two-parameter lift.  Under `sigma=s^4`,
   `tau=varrho=s^3`, verify `Lambda=tau^3 varrho=sigma^3`, the unit
   coefficient change and determinant target, and membership in every
   required generic/saturation open.  Decide whether flat base change
   really licenses this explicit arc lift or only equality of central
   fibres.
6. State the strongest exact result and scope.  It is one named Newton cell,
   not a fan atlas, global total-Rees theorem, Taylor realization,
   order-two closure, max12, or JC2 result.

Start with a pin/verdict table.  Give the smallest failed identity or
missing hypothesis.  End with exactly one standalone verdict token
`CONFIRMED`, `REPAIR`, or `REFUTED`.
