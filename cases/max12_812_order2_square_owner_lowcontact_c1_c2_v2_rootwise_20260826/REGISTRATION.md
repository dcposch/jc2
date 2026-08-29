# Registration: low-contact `c=1,c=2` rootwise endpoint

Date: 2026-08-26

The frozen V1 source compiler reached the `c=1` radical endpoint in both
fields but its broad `c=2` `radical()` call was still running.  This V2 pins
that compiler and replaces only the post-source radical blocks with the
short rootwise divisibility proof.

For `c=1`, grade 11 gives `L|A*C1`; after moving-denominator correction,
the grade-12 common numerator modulo `L` and the lower remainder is
`(3/8)C1^2`.  Hence `C1` vanishes at both roots of squarefree `L`.

For `c=2`, grade 12 gives `L|A*C2`.  At a root where `A` is nonzero this
already kills `C2`; at a root where `A=0`, the corrected grade-14 numerator
modulo `L`, `A`, and the grade-12/13 remainders is `(3/8)C2^2`.  Thus `C2`
again vanishes at both roots.  Moving `p`, moving `k10`, `R`, and all fresh
corrections are retained.

All seven source rows are compared through the exact moving lower-
unitriangular Laurent-coordinate transformation.  Exact Q is the producer;
`F_65521` is a control.  The endpoint is only the generic-square low-contact
gate on `D(p*k0)`, not square-branch or order-two closure.
