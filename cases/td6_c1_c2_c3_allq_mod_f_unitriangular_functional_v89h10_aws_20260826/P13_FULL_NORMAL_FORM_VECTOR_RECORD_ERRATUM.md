# P13 full-normal-form record-count erratum

Date: 2026-08-26

The frozen `P13_FULL_NORMAL_FORM_RESULT.md` calls the `238` data rows of
`ALLQ_P13_FULL_NORMAL_FORM.tsv` “nonzero scalar-coordinate terms.”  That
description conflates vector records with their scalar entries.

The exact corrected census is:

- `238` nonzero `(parameter monomial, q monomial)` records;
- each record stores one 18-coordinate `E3` vector;
- `535` scalar coordinates across those records are nonzero;
- coordinate 12 is nonzero in exactly one record, namely
  `(parameter,q)=((),())`, with value `(3500000000/9)*(U/V)`.

This is a terminology/count correction, not a change to the frozen TSV, its
SHA-256, the H15 normal form, or the H18 coordinate-12 conclusion.  Any later
client must call `238` the vector-record count and `535` the nonzero scalar-
entry count.
