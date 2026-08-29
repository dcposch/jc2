# V37 ordered-`a1` graded localizer ladder

Date: 2026-08-27

Status: **exact mathematical discovery evidence; independently replayed;
validation/custody metadata require the frozen erratum and a hardened
successor.**

For the homogeneous `rho=0` raw ordered-`a1` row ideal generated through
grade 19, V37 spans every monomial multiple at the indicated fixed sigma
weight.  Two registered EC2 runs used different modular selector primes but
solved and replayed the final certificates over exact Q.

```text
target       weight  products  target component       rank  verdict
a1*k^3          17       217   0 products / 1 monomial    0  nonmember
a1^2*k^2        18       426   0 products / 1 monomial    0  nonmember
a1^3*k          19       803   50 / 696 / 2086 nnz       50  nonmember
a1^4            20      1473   161 / 982 / 2951 nnz     156  nonmember
```

The exact duals have respectively 1, 1, 5, and 14 nonzero coordinates.  The
two canonical mathematical records are identical after selector/lane metadata
is removed, and every dual annihilates every full fixed-weight product while
taking its target to one.

Harvested validated-result hashes:

```text
065c96a9499e085db1d65a9034f2b24c75e681d27518cb372c3eb41ced753338  q65521
fe2f6ef30e7423d81ee0bde4cb6cdf9116ab0c9b5dcfb8585f5d769367cdfce5  q65519
```

Because later homogeneous rows have weight at least 20, the W17--W19
nonmembership answers are final at those weights.  W20 is only a statement
for rows through grade 19: a grade-20 row with constant cofactor could change
it.  These negative answers show that the hoped-for total-exponent-four raw
localizer certificate does not exist at the tested weights.  They do not show
that `D(a1*k)` is nonempty, and they make no saturated-Rees, chart, Gate-T, or
JC2 inference.

Independent audit approved the mathematics but found that the frozen
validator accepts mutations to several metadata/scope fields and that its
evidence manifests contain remote-absolute paths.  All 11/11 hashes per lane
verify after relocation.  The immutable details and successor requirements
are recorded in the case `ERRATUM.md`; promotion must cite a hardened replay,
not the frozen PASS token alone.
