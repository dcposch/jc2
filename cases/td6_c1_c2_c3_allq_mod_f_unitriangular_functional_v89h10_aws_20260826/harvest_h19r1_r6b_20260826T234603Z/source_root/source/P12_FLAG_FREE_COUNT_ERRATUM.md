# TD6 V89H11 free-count wording erratum

Date: 2026-08-26

The frozen V89H11 result's closing phrase "full 17-parameter normal form"
uses the wrong quotient-dimension count.  Literal transport has 132
parameter variables and the frozen FIRST block has 38 pivots, leaving 94
nonpivot variables.  The number 17 came from the nonzero records in the
earlier pure-q14 class.

No V89H11 algebra or theorem changes: V89H11 computes only the coefficient
obtained after setting **all** nonpivot variables to zero, and its client did
exactly that by rejecting every variable outside the 38-pivot set.  This
erratum withdraws only the numerical wording "17-parameter"; it does not
promote V89H11 beyond its frozen empty-parameter functional scope.
