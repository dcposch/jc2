# Design erratum: Singular minor-object storage in V27 successors

Date: 2026-08-27

Scope: the prepared six-variable R4 runner and the alternate full-`P6`
rank-two-chart runner.  This erratum does not alter the immutable failed
full-`P6` R0 source freeze or endpoint.

The post-Fable repair correctly replaced every positional `size()` loop by an
`ncols()` loop, but then added an incorrect guard asserting that every
`minor(A,r)` object retained all `binomial(7,r)^2` literal slots.  Exact AWS
Singular 4.3.2 replay gives the actual storage tuple

```text
rank             6      5       4        3       2
ncols             1     90     594      813     441
size              0     90     594      813     351
combinatorial     49    441    1225     1225     441
```

Corrected successor guards must validate those actual `ncols`/`size` values.
They must iterate every stored slot with `ncols()`.  For ranks 5, 4, and 3,
the stored object already consists of the complete nonzero generator list;
for rank 2, it contains 441 stored positions with 90 interior zeros, so the
filter must scan all 441 columns and retain exactly 351 nonzero generators.
The independent complete combinatorial row/column label universe remains
provenance metadata, not a claim that its list index is a Singular object
slot.  The selected determinant continues to bind by exact polynomial
identity to Singular minor-object column 37.

The mathematical raw targets remain unchanged: R4 has
`7+90+594+813+1=1505` nonzero raw columns, and the full-`P6` chart has
`35+813+1=849`.  Singular comma concatenation and empty-ideal assignment
preserve their repeated columns on the frozen engine.  No corrected runner
may be launched from this erratum alone; it requires a fresh source freeze,
hostile static review, and explicit authorization.
