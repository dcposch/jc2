# V35 evidence-language erratum

Date: 2026-08-27

The frozen preregistration overstates two custody properties; its hashes and
harvested outputs are intentionally left immutable.

1. The F65521 lane is a separately registered modular shadow of the exact-Q
   reconstruction, not an independent finite-field implementation.  The
   compiler reconstructs with `Fraction` in both lanes and reduces the same
   coefficients and scalar values modulo 65521.
2. The 63 upstream bridges are hash-pinned algebraic polynomial equalities,
   not byte-equality of independently serialized rebuilt rows.

V35 remains valid discovery evidence for the scalar values
`Tg19_1=...=Tg19_6=0`, `Tg19_7=-7077888`, whose modular shadow is 63901.
Its validator is not promotion-grade because it does not independently
derive every nonzero-row/outcome field.  Promotion must instead cite V36,
which verifies all seven Q/F65521 row shadows and sigma weights, proves that
no weight-19 receiver occurs, and runs ordinary Singular independently in
the two fields to obtain a nonzero normal form and the unit ideal.
