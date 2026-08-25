# Q8 fixed-fibre graph interpolation successor

This producer consumes the 126 clean pure-Singular fixed-fibre shape bases
over `F_127` and the pinned bidegree `(21,190)` candidate `H(w,v)`.  It first
audits every fixed-fibre output, then attempts exact coordinate graph
reconstruction.  A reconstruction is accepted only after direct substitution
of all eight divided/localized source rows modulo `H`, plus denominator-unit
and corrected-Q8 contact checks.  Fixed-fibre interpolation or a recurrence by
itself is evidence only, never generic quotient membership.

All substantive parsing, interpolation, rational reconstruction, and symbolic
substitution runs on AWS.  The local tree contains immutable source and
harvested custody bytes only.
