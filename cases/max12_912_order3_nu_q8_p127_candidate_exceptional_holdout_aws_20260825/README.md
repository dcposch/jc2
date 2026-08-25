# Q8 `F_127` exceptional-fibre holdout for the candidate eliminant

The degree-190 candidate `H(w,v)` was interpolated using only the 123
full-degree nonzero fibres.  This AWS-only diagnostic evaluates that candidate
at the three excluded values `w=39,56,125` and compares it exactly with each
pure-Singular degree-189 fibre eliminant.

For every exceptional value it reports exact divisibility, quotient,
candidate/fibre gcd degree, squarefree gcd of the candidate, and whether a
linear quotient root is already a root of the fibre eliminant.  This is a
genuine holdout test of the interpolated candidate, but agreement is still not
a generic ideal-membership, flatness, or characteristic-zero certificate.

## Frozen result

The Box02 lane `q8_p127_candidate_exceptional_holdout_v1` returned rc zero.
At `w=56` and `w=125`, the fibre eliminant divides the candidate with quotient
`v`; the extra root zero is not a root of the localized fibre, and the
candidate remains squarefree.  At `w=39`, the quotient is `v+38`; its root 89
is already a fibre root, and the candidate has squarefree-gcd degree one.
These outcomes exactly distinguish the two length drops from the one
nonprimitive-coordinate fibre.

The frozen result JSON has SHA-256
`e129efe2e538014bf0f97abcd4576af395fb54575f2aa584ab2d127664e52f84`.
