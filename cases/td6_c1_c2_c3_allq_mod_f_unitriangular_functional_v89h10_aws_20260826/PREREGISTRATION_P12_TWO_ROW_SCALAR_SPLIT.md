# TD6 V89H14 exact two-row/scalar P12 quotient split

Date: 2026-08-26

Status: producer gate; no exclusion claim.

Consume the frozen V89H12 complete P12 normal-form TSV literally.  Verify
coefficient support before any specialization:

- every coefficient of a surviving quotient variable is supported only in
  E3 coordinates 0 and 1;
- the empty-parameter coefficient is supported only in coordinates 0 through
  7;
- coordinates 8 through 17 vanish identically;
- the q2 coefficient block in columns `y24,y27`, rows 0 and 1, is exactly
  `[[6,8],[0,4]]`, giving q2-squared minor coefficient 24.

Emit the six exact quotient-variable-independent scalar equations in E3
coordinates 2 through 7.  As a generic-rank witness only, evaluate their
6-by-12 q3-through-q14 coefficient matrix at the good rational point
`(U,V)=(1,3)` and exhibit one exact nonzero 6-by-6 minor.  This proves generic
rank six over `Q(U,V)` but does not license inversion of that minor on all of
`D(U*H*B3)`.

A pass establishes the exact structural decomposition of P12/FIRST and the
correct low-rank Fitting level.  It does not solve the six scalar equations,
cover the rank-drop divisor, exclude a q chart or source point, provide a
total-Rees map, close TD6, or resolve JC2.  Substantive algebra runs on two
AWS lanes; no Singular qring is used.
