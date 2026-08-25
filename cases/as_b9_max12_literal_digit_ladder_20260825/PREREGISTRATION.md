# Preregistration — witness-first B9 literal digit ladder

Date: 2026-08-25

Given one source-hashed literal fixed-D12 integer pair whose determinant is
one modulo `M=3^n`, introduce every total-degree-at-most-12 coefficient in a
fresh correction `M(R,S)`, impose every determinant row through total degree
22 modulo `3M`, solve the exact affine `F_3` system, and literally replay any
witness.

Every invocation is pointwise.  A PASS advances only the displayed literal
branch by one digit; a failure kills only that point, never its preceding
affine fibre.  The input SHA, modulus, all 182 columns, all 276 rows, rank,
kernel, and negative control must be recorded.  No invocation implies an
inverse limit, characteristic-zero map, counterexample, or JC2.

The first registered invocation used input SHA
`d267a2b5f4d7f6fd8d0535857923cd8f842322aa59d1a4b5bbd520f3a13a52dc`
at modulus 729.  Box02 and r6d agree that this particular is inconsistent at
modulus 2187.  This is retained as the negative control for the separately
computed full-fibre survivor.
