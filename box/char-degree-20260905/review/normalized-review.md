# Independent audit of the normalized total-face backend

The normalized backend is mathematically equivalent to the newly sourced total-degree and leading-form instrument. Its normalizers, t shifts, leader target, and low-digit cutoff all pass independent exact-Q tests. The repaired Singular serializer also passes. This establishes arithmetic and row-emission correctness, not a completed full-branch computation.

Two substantive new results change the scope cautions in the earlier review files. Moh Proposition 4.5 and its printed proof license total-degree/top-form rows in these clients; they are not inferred from Proposition 2.2 alone. Separately, the source agent's full-face theorem excludes every identically-zero Jacobian point, rather than just Delta. Thus a verified proper augmented ideal now proves existence of a nondegenerate point over the algebraic closure, even if no coordinate assignment has been extracted. It must still be reported as abstract existence, not an exhibited rational point.

## Source necessity and absence of an extra gauge

Both clients have `M3=n-2`. Printed p169 Proposition 4.5 assumes `deg g=deg_y g=n>1` and that equality. It makes the top forms of g and `T_i`, for `i<3`, powers of one common form. Because g's y-degree equals its total degree and its y-leader is a scalar, the common form has that same property; each power does too. Therefore T2's total degree is its previously established exact y-degree 55 or 63.

The printed p172 proof removes an ambiguity about the specialized polynomial notation. Its minimum is taken over the roots of the product involving the `T_i^psi`; the contradiction for root order below -1 uses Proposition 4.2 to include the next characteristic polynomial. The existing g already has a root direction y=x, so the minimum is at most -1. The contradiction forces equality in these same coordinates. The coefficient bounds from root orders then independently show total degree equals y-degree. This uses no generic shear and spends no source gauge. Replacing the paper's Jacobian scalar 1 by a general nonzero constant changes no valuation or nonvanishing argument used here.

The fixed source F top forms determine the actual characteristic top targets, up to the free scalar lambda:

* `(99,66)`: `lambda*y^15*(y-x)^40`, degree 55;
* D108: `lambda*y^14*(y-x)^49`, degree 63.

This scalar must be retained and localized; it is not normalized to 1. The entire target polynomial is subtracted, including all binomial coefficients after writing y=(1+z)/t. The five-target representative differs from the canonical one by at most a constant once its degree is below m: the other four possible differences have distinct leading y-degrees above the target. Thus this target remains a necessary choice in the existential family.

## Exact normalizers

For a physical polynomial P of total-degree bound B, write `N_B(P)=t^B P(t^-1,(1+z)/t)`. A monic y-degree-k H of total degree k becomes a monic z-degree-k polynomial under N_k. Normalized monic z-division is exactly the transport of physical monic y-division. The quotient normalizer is the dividend normalizer minus k, while the remainder keeps the dividend normalizer.

The depressed polynomials have bounds `H:k`, `v:2k-1`, `V:3k-1`. The four physical identities are

`v^2=UH+R`, `vU=PH+R1`, `vR=QH+R2`, `U^2=WH+R3`.

Their normalizers are:

| quantity | formula | k=33 | k=36 |
| --- | ---: | ---: | ---: |
| U | 3k-2 | 97 | 106 |
| R | 4k-2 | 130 | 142 |
| P | 4k-3 | 129 | 141 |
| R1,Q | 5k-3 | 162 | 177 |
| R2 | 6k-3 | 195 | 213 |
| W | 5k-4 | 161 | 176 |
| R3 | 6k-4 | 194 | 212 |

Using these names for the normalized versions, the full coefficient rows are

`derivedV=V-(3/8)*t*U=0`,

`upper=(3/4)*R+p*t^(4k-2)-(1/8)*t*P=0`.

The remaining normalized digits are

`digit=Q-(1/8)*R1-(9/64)*t*W`, with normalizer 5k-3,

`low=R2-(9/64)*t*R3+p*t^(4k-2)*v+q*t^(6k-3)`, with normalizer 6k-3.

The normalized V itself is

`C-(b/4)*t^k*D+(ab/12+b^3/54-c/2)*t^(3k-1)`.

The extra t factors in all these expressions are necessary. They come from differences of normalizers; omitting one would change the source polynomial rather than just its representation. Every stated factor agrees with `normalized_backend.py`.

## The exact face and low rows

After the high digits vanish, the physical characteristic polynomial is `Qchar=E*H+L`, with `deg_y E,deg_y L<k`. Monic y-division respects total degree because H has total degree equal to its monic y-degree. The top target is divisible by H's top:

* k=33: `H_top=P0^3`, `Qchar_top=lambda*P0^5`, where `P0=y^3(y-x)^8`;
* k=36: `H_top=P0^4`, `Qchar_top=lambda*P0^7`, where `P0=y^2(y-x)^7`.

Homogeneous monic division therefore gives E's top as `lambda*P0^2` or `lambda*P0^3` and L's top at the characteristic degree as zero. The necessary and sufficient strengthened conditions are

`deg E<=d-k`, `E_(d-k)=the stated quotient target`, `deg L<=d-1`.

They become precisely:

| client | digit zero bands | digit equality target | low zero bands |
| --- | --- | --- | --- |
| 99 | t<140 | t140: `lambda*z^16*(1+z)^6` | t<141 |
| 108 | t<150 | t150: `lambda*z^21*(1+z)^6` | t<151 |

All coefficient rows of derivedV and upper are imposed, without truncating those identities. At the equality band the whole digit face is subtracted. The low condition includes the characteristic-degree band itself: replacing t<141 by t<140, or t<151 by t<150, would drop required rows. Conversely, zeroing the next low band would impose an unjustified extra condition.

The backend's division order `(lp(1),dp(...))` makes z the first variable. Since H's z leader is 1, division introduces no parameter denominators or hidden leader branches. Coefficient extraction in t*z then removes both physical variables before the source ideal is tested. Keeping unused t,z as extra polynomial-ring variables changes dimension by two but does not change whether the ideal is proper.

The source `(99,66)` normalized-input emitter retains the complete h3/C2/C3 tower and all surviving B2/A3 coefficients. Its finite cap applies only to the historical finite rows. Its checked source maps and declared free-coordinate inclusion guard against dropping a source coefficient while transporting the chart. D108's build through normalized h2 t36 captures the whole polynomial of degree36.

## Independent controls

`normalized_backend_control.py/.json` verifies the transport of all four divisions on dense physical polynomials of k=3 with nonconstant x coefficients. The normalized z-divisions agree identically with the normalizations of the physical y-divisions, including every quotient and remainder. It also derives every normalizer and both quotient-face formulas above.

Four controls use the actual repaired normalized Singular backend:

1. A degree-attained toy pair with the correct face returns NONUNIT.
2. Replacing its face by the wrong polynomial returns UNIT.
3. Adding a low-digit term exactly at the characteristic-degree boundary returns UNIT.
4. Adding a term one degree below that boundary remains NONUNIT.

Both leader-localization controls also pass in every script. These are backend controls, not points on either source chart. Their scripts, hashes, and actual Singular outputs are retained in this directory. The repaired recursive serializer writes rational factors separately from powers and avoids the confirmed old `b^2/4` parse failure.

## Nondegeneracy theorem audit

The new source theorem uses a valid additional characteristic-zero common-composition result: if J(F,G)=0, then F=f(H), G=g(H) for one polynomial H. Since F's total degree equals its y-degree, H has total degree equal to its positive y-degree k. Attained degree55 or63 makes k divide gcd(n,m,d), equal to11 or9.

The fixed F top then forces k=11, deg f=9 in the first client, or k=9, deg f=12 in the second. The actual negative-order D2 F faces, derived after the offset-zero outer D1 rows annihilate every outer equality face, are `(pi^3-1)^24` and `(pi^4-1)^21`. At a negative valuation the highest power f(H) uniquely leads, so those faces would have to be ninth or twelfth powers up to scalar. Their root multiplicities 24 and21 give contradictions. No Jacobian coefficient row is used in this argument.

Thus every point of the fully augmented source chart has J not identically zero. An independently verified proper ideal over Q, with all localizers and source maps, yields a point over the algebraic closure by the weak Nullstellensatz and hence a nondegenerate necessary-chart survivor. This proves abstract existence; it does not exhibit coordinates, imply constant Jacobian, or realize a Keller datum. A timeout or an unchecked dimension is still no result.

The chain rule adds the correct consistency check: total deg Qchar<=d gives `(3G^2+2aG+bF+d_target)J(F,G)=J(F,Qchar)`. The first factor has degree 4k, so the nonzero Jacobian has degree at most d-k-2, equal to20 or25. The shallow Jacobian bands in stages0–8 are consequently forced by the stronger characteristic rows. This is consistent with nondegeneracy; it does not imply a unit.
