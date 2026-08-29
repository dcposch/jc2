# V26R1 grade-two row provenance clarification

Date: 2026-08-27

The V26 compiler field `Q1_to_Q6` is a legacy list name, not the logical
row-number label used by V22/R6.  Its exact construction is

```text
[expanded[(row,2)] for row in (1,2,3,4,5,7)].
```

Thus it contains the six nonzero literal grade-two row polynomials.  Literal
row 6 is exactly zero and is omitted from an ideal by Singular.  In any V26R1
worker/report these generators must be named

```text
G2_row1, G2_row2, G2_row3, G2_row4, G2_row5, G2_row7,
```

not `Q1,...,Q6` without provenance.  The exact R6R1 syzygy uses literal rows
1, 3, and 4, so it proves `W=0` modulo both the six-nonzero-row base and the
full prior ideal regardless of the legacy list name.
