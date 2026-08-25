# Q8 degree-190 eliminant interpolation over `F_127`

This AWS-only diagnostic reconstructs each fixed-`w` eliminant from its
pure-Singular factorization.  Of the 126 nonzero values of `w`, 123 have
degree 190; the three exceptional values `w=39,56,125` have eliminant degree
189.  At `w=39` the quotient still has vector-space dimension 190, while at
`w=56,125` it has dimension 189.  Thus `w=39` is a failure of `v` to retain
degree 190, whereas the latter two fibres exhibit a length drop.  For each of
the 191 `v`-coefficients, the script interpolates the unique
polynomial of degree less than 123 through the 123 full-degree fibres.

That polynomial is only a candidate representative on the full-degree
sample.  In particular, it is not a representative modulo `w^126-1`, a
bound on the actual generic `w`-degree, an identification of possible
denominators, or a proof of specialization/flatness.  Its purpose is to
expose possible sparse structure and produce a candidate for subsequent
exact generic reduction.

All 126 nonzero fibres must be present, rc zero, and squarefree.  The checker
requires vector-space dimension 190 except at `w=56,125`, where it requires
189; it requires eliminant degree 190 except at `w=39,56,125`, where it
requires 189.  Every reconstructed factor product is checked against its
reported degree before interpolation.
