# V27 preregistration: exact degree-15 dual on the ordered-a1 rho=0 face

Date: 2026-08-27

V26 returned the unchanged normal form `a1^3` after a degree-bounded
standard-basis calculation, but Singular warned that the resulting basis was
not complete.  Adjudicate the same question without Groebner-basis
completeness assumptions.

After setting `rho=0`, all surviving V23R1 rows are positively
sigma-homogeneous.  Enumerate every product

`m * Tg(g,r)` with `weight(m) = 15-g`,

over the surviving ordered-a1 coordinate ring, and perform exact-Q linear
algebra in the finite vector space of weight-15 monomials.

- If `a1^3` is outside the span, emit a sparse rational linear functional
  that annihilates every enumerated ideal product and takes value one on
  `a1^3`.
- If it is inside, emit exact cofactors and replay the identity.

An independent validator must reconstruct every generator multiple directly
from the hash-pinned V23 rows and verify the emitted certificate.  Run on AWS
only, with a 30-minute wall cap and a 400 GiB virtual-memory cap.

