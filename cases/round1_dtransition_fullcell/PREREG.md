# Preregistered D1 full-cell gate

Frozen before the full-cell computation on 2026-08-24 UTC.

## Premise and object

The only new premise is the different-model-reviewed one-band result
`FREE-TAIL-SIGNAL` in `xmodel/review-dtransition-grok.md`.  Work is restricted
to the `p = 105337`, `a00pp` promoted D25 `A^14` cell containing the banked
witness (the zero value of the fourteen registered free coordinates).  The
map is the source-defined `X27 -> X25` transition through band 26.

The ten new-coordinate coefficient matrix has source-filtration rank four,
so its canonical left kernel defines six band-26 compatibility functions on
this cell.  The functions must be pulled back through the existing exact D25
triangular reconstruction and band-24 zero-completion; no D43 artifact or
claim may enter.

## Falsifiable verdicts and first decisive stop

1. `SMOOTH-CODIM6-STRATUM`: the six functions vanish at a certified point and
   their `6 x 14` Jacobian has rank six there.  This proves only a nonempty,
   nonsingular codimension-six band-26 compatibility stratum on this modular
   cell.  Stop immediately; do not advance to band 28.
2. `NONEMPTY-SINGULAR-OR-LOWER-RANK`: a certified common zero exists, but the
   Jacobian rank at every registered zero tested is below six.  Bank the exact
   ranks and stop; do not infer the generic rank without a nonzero minor.
3. `EMPTY-ON-CELL`: an exact elimination certificate proves the six-function
   ideal is the unit ideal.  A point sample is never enough for this verdict.
4. `TYPING-OR-CERTIFICATE-FAILURE`: the source block is not constant/rank four
   on the cell, the triangular pullback fails, the six functions fail to
   characterize affine solvability, or a provenance/replay gate fails.
5. `INCONCLUSIVE`: resource or representation growth prevents a decisive
   exact gate.

Because the registered cell origin is already the reviewed compatible D25
witness, verdict 3 is expected to be falsified immediately.  The decisive
remaining discriminator is therefore a nonzero exact `6 x 6` Jacobian minor
at that origin.  A rank-six minor is both sufficient for generic rank six and
the mandatory stopping event.

## Perimeter

No claim is permitted about band 28, D43, D75, B=168, persistence, an inverse
limit, a formal germ, characteristic zero, algebraization, a polynomial map,
or a Jacobian-conjecture counterexample.
