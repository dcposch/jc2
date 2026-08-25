# Postscript to the `20260825T1700Z` synthesis — corrected common-cubic SAT

Status: **significant-news micro-round; producer-exact finite statement,
promotion review live**  
Parent synthesis: `xmodel/ideation-20260825T1700Z-synthesis.md`, SHA-256
`a1cd2be8eb99e4ef19338c60d3d3d7721905afcb5268c8f68919ca2df20d74e2`  
V2 retraction: `xmodel/ideation-20260825T1700Z-synthesis-erratum.md`, SHA-256
`5dfca997914867c122de218c56660dcb9d2b3b01b4ae03030216d9da5ac14b17`

## Corrected event

The intended normalized B9 common-cubic gate is nonempty modulo `3^11` over
the one displayed mod-243 parent.  A source-independent AWS compiler that
does not read either SMT formula directly constructs the 299-row system:
276 determinant rows plus all 23 coefficients of

```text
P9=P_(0,9) H^3,       Q12=Q_(0,12) H^4,
H=y^3+h1*x*y^2+h2*x^2*y+h3*x^3.
```

Its complete staged finite-family dimensions are

```text
3^6:55,  3^7:81,  3^8:99,  3^9:116,  3^10:133.
```

At the first quadratic transition to `3^11`, the 133 predecessor coordinates
split into 17 active and 116 spectator directions.  The 149 fresh
map-plus-cubic coordinates have rank/kernel/cokernel `94/55/205`; the
spectator image has rank 38; and every active quadratic coefficient lies in
that image.  Hence the reduced system has zero equations, the finite
predecessor exponent is `17+(116-38)=95`, and adjoining the fresh kernel
gives a displayed complete exponent `150`.

A second implementation replays one literal witness with

```text
H = y^3 + 119880*x*y^2 + 40581*x^2*y  (mod 177147)
```

against all 276 determinant and 23 top-core rows, the pinned mod-243 parent,
the leading units, support caps, and actual degree pair `(9,12)`.  Producer:
`xmodel/as-b9-9-12-common-cubic-3p11-producer-20260825.md`, SHA-256
`b3a86bbd55ed99ca60dfc3eeb89560dbc483265db603de0bec4a26e63d673a2b`.
Independent hostile reconstruction:
`xmodel/as-b9-9-12-common-cubic-3p11-hostile-audit-codex-20260825.md`,
SHA-256
`c739e502687d34924cb8d0e22feb17019572ab87407f3ed306127468cfe15aa1`.
Different-model promotion review remains live.

## Strategy and theorem-interface composition

The global ranking does not change.  The 17:00Z blind round already selected
this exact SAT branch and prescribed core-inclusive Smith/dilatation/Hensel
analysis.  Under the coordination coalescing rule, correction of the
unpromoted V2 formula plus the anticipated finite SAT outcome is handled as
a micro-round and does not reset the 12-hour full-round clock.

The bounded interface pass gives:

1. **Direct bridge:** feed the common-core witness and complete family to the
   exact Jacobian/SNF, Fitting/dilatation, and quantitative multivariate
   Hensel compiler with all 299 rows.  Stable digit-growth alone is not formal
   smoothness; high Smith valuations can create a long transient.
2. **Conditional disproof client:** only a certified compatible `Z_3` point
   can feed the reviewed residue-ball collision theorem and characteristic-
   zero field transfer.
3. **Proof-side client:** use the order-one binary-cubic original-row gate to
   attack the three root-multiplicity strata `L^3,L^2M,LMN`.  A finite mod-3
   survivor is specialization data, not characteristic-zero landing.
4. **Scope conflict:** the reviewed selected order-three `p=1` corrected-Q8
   source cannot receive the fixed-D12 order-one seed.  It remains part of
   the general unbounded-total maximum-12 theorem only.

The core-inclusive exact Jacobian/SNF/Hensel job and the order-one
binary-cubic proof gate were launched immediately on AWS.  No local heavy
computation is permitted.

## Refusal scope

The `3^150` number is a finite staged digit-parameterization exponent, not a
Krull/relative dimension or smoothness theorem.  This result covers one
parent and one modulus.  It proves no survival to `3^12`, inverse limit,
`Z_3` point, characteristic-zero Keller map or collision, complete earlier
parent fibre, maximum-12 theorem, counterexample, or JC2.
