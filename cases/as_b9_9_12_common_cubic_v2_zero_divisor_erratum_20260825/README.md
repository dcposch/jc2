# Quarantined normalized common-cubic V2 formula

This package preserves a source/encoding failure as a negative control.

The V2 emitter used a residue constructor for the positive modulus.  Thus
`bv(MODULUS)` was encoded as zero, all 407 `bvurem` divisors were zero, and
the three bounds `h_i < MODULUS` became `h_i < 0`.  The invalid SMT file at
SHA-256
`182bc9f7302ba852b32d04899e6b7a86b38d0eaf0cb2faaa280717d4b9c70604`
therefore simplifies to the one-empty-clause DIMACS file at SHA-256
`69ee12c3118a428a28f674ec24e362b721e0611c800f65afbcb8a48e778c1394`.

Every `UNSAT` or proof artifact in this package certifies only that invalid
formula.  It is not evidence about the common-cubic locus.  The unaffected
normalized nonlinear parent result has SHA-256
`984dbcf57ce181c5f07308f80950b38a9c78174cd9c802c868b46ce337e90539`.

The source-honest repair is V3 in the sibling case
`cases/as_b9_9_12_common_cubic_3p11_20260825/`; it uses an explicit raw
positive-modulus constructor and a complete constructor-call audit.
