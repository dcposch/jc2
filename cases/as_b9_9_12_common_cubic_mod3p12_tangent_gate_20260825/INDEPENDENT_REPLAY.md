# Independent singleton-row replay

Rebuild only the determinant coefficient `[x^2 y^2]` directly from the
literal witness, without consuming the emitted Jacobian matrix or the primary
Gaussian solver.  Check all 146 coefficient unit digits at order `3^11` and
the three core digits, and verify that none changes this row modulo `3^12`.
Also check that every fresh-fresh determinant term vanishes because
`(3^11)^2` is zero modulo `3^12`.

The base row must be nonzero after division by `3^11` modulo 3.  Together
these checks are a source-independent pointwise obstruction certificate.
