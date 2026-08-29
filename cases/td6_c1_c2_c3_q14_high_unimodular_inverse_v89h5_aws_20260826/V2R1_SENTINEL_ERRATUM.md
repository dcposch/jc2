# TD6 V89H5V2R1 parser-sentinel erratum

Date: 2026-08-26

V2R1 used source archive
`fd5c4d7525b2411e62084b92c36f6ac4c48ded7e95cfd61dc238a5e953b9ad6b`
and again terminated identically with rc 1 before completing the first
frozen coefficient.  The V2 erratum correctly identified the polynomial
context but used it as a callable.  In python-flint 0.9.0 the required
constructor is `m.tri.CTX.constant(value)`.

No mathematical membership test, division by `F`, denominator audit, or
verdict ran.  The R1 failed client, manifest, archive, and dual AWS run
directories are frozen under names containing `r1_sentinel`.

V2R2 changes the constructor to `.constant(value)` and makes scalar division
explicit through `right.leading_coefficient()`.  It requires a new source
manifest/archive and fresh dual AWS roots.
