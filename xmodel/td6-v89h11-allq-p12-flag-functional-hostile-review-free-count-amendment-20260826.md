# Live hostile-review amendment: V89H11 free-variable count

Date: 2026-08-26

This is an addendum to the immutable V89H11 hostile-review prompt with SHA
`e7b13084ae539bbf13cef69424afe67ba3854b815e08f986a78199a0d5271006`.
Read and adjudicate it before issuing the final report.

The frozen producer result closes by saying that it did not compute the
"full 17-parameter normal form."  The number 17 is wrong.  The transported
kernel has 132 parameter variables and the frozen FIRST pivot list has 38
distinct variables, leaving a 94-dimensional nonpivot quotient.  The number
17 is only the number of nonzero records, including the empty record, in the
pure-q14 cokernel class.

The frozen wording erratum is

```text
cases/td6_c1_c2_c3_allq_mod_f_unitriangular_functional_v89h10_aws_20260826/P12_FLAG_FREE_COUNT_ERRATUM.md
SHA256 c6bc9942ec60b90433f6044d299cce6e2f4e49ffd237d3680d118b73c39babd2
```

The H11 computation itself sets every variable outside the 38-pivot set to
zero by testing membership in the complete pivot dictionary; it does not
enumerate or assume 17 nonpivots.  Therefore the claimed empty-nonpivot
functional may remain valid even though the closing dimension label does
not.

The final hostile report must explicitly:

1. distinguish the 94 nonpivot variables from the 17 nonzero pure-q14
   records;
2. determine whether H11's empty-parameter functional theorem remains
   mathematically valid after this correction;
3. use `CORRECTED` if the frozen result's wrong count makes `CONFIRMED`
   inappropriate, and identify the smallest corrected theorem statement;
4. preserve the original scope: one empty-nonpivot functional only, not a
   full 94-variable normal form or an exclusion theorem.

Do not promote H11 unless this amendment is expressly adjudicated in the
required final report.
