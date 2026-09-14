# F10 mixed resultant sizing — independent Sol FIRST

MANUAL / STATIC. I import only the already-reviewed whole septic interface and cube asymptotic from the charged inputs. No CAS, search, source execution, or new theorem lane was used.

## Itemized verdicts

**1. Simultaneous monomial bounds — CONFIRMED.** For a monomial in `[u^n]phi^(at+b)`, if `ell` nonconstant factors include `j` copies of `Xu^2` and `k` copies of `Yu^3`, then `n=ell+j+2k`; its `t`-degree is at most `ell`. Hence `i+j+2k<=n` and `2j+3k<=n`. A monomial in `[u^m](phi'/phi)=(m+1)[u^(m+1)]log(phi)` instead has `j+2k<=m` and `2j+3k<=m+1`. Adding the three coefficient degrees with `m+n1+n2=14` proves

`i+j+2k<=14`, `2j+3k<=15`.

Truncation and cancellation only delete terms. Thus `k<=5`; also `j+k<=7` (for `k=0`, `j<=7`; for `k>=1`, `2(j+k)<=15-k<=14`).

**2. Degree bounds after fifth-power clearance — CONFIRMED.** In

`G=U^5 B(t,X,V/U)`,

each term becomes `t^i X^j V^k U^(5-k)`. Using total degrees `deg U<=2`, `deg V<=4`, its total degree is at most

`i+j+4k+2(5-k)=10+i+j+2k<=24`.

Using X-degrees 2 and 3 gives

`j+3k+2(5-k)=10+j+k<=17`.

The prior bound `k<=5` is exactly what makes this a polynomial. Hence `degree_Y B<=5`, total degree at most 24, and X-degree at most 17.

**3. Sylvester degree at most 185 — CONFIRMED.** Let the actual generic X-degree of `G` be `m<=17`. A nonzero Sylvester determinant monomial uses `m` coefficients of `P0` and seven of `G`; X-scaling shows their X-index sum is `7m`. Since the coefficient of `X^j` has t-degree at most `8-j` for `P0`, and `24-j` for `G`,

`deg_t Res_X(P0,G) <= 8m+7*24-7m = 168+m <=185`.

The same inequality holds if the generic degree is below 17.

**4. Exact cube resultant order 34 — CONFIRMED.** With `delta=h^7`, each of the seven accepted branches has `ord_h(U)=4` and `ord_h(B)=14`, with nonzero leading coefficients. Therefore `ord_h(G)=5*4+14=34` on every branch. The root-product formula multiplies seven such values, giving h-order 238, hence delta-order 34. The factor `lc_X(P0)^m=[9(t-2)]^m` is nonzero at `t=5/3`, so it changes no order. Thus `(3t-5)^34` divides `R` exactly and the quotient is nonzero at the cube.

**5. Quotient degree and actual-r equivalence — CONFIRMED.** Dividing exact degree 34 from `deg R<=185` gives nonzero `Q=R/(3t-5)^34` with `deg Q<=151` and `Q(5/3)!=0`. At every actual `t`, `P0` keeps degree seven and `U` is a unit, so `B` is nonunit iff `G` is nonunit iff `Res(P0,G)=0`, equivalently `Q(t)=0`. A specialized loss of G's leading X coefficient creates no spurious zero: the fixed-generic-degree root-product identity `lc(P0)^m product G(alpha)` remains valid. The map `r -> (5r+2)/(3r+1)` is injective and never equals `5/3`. Hence at most 151 distinct integer `r>=2` can be exceptional. This is a cardinality bound, emphatically not `r<=151` or a maximum-r bound.

**6. Explicit denominator norm — CONFIRMED.** At the two roots of U, `V=A(X-x0)` and `lc_X(U)=3`, so

`Res(U,V)=3^3 A^2 product(alpha-x0)=9 A^2 U0`.

Because `P0 congruent 3V^2 mod U`, direct resultant scaling yields

`Res(P0,U)=27 Res(U,V)^2=2187 A^4 U0^2`.

Since `P0=(t-2)P` and `lc_X(P)=9`, division by `(t-2)^2*9^2` gives

`Norm_U = 27 A^4 U0^2/(t-2)^2`,

where

`A=(3t-5)(3t-4)(2t-3)/15`, `U0=(t-3)(6t-11)/196`.

Only A vanishes at the cube, to order one, so the norm has exact cube order four. This independently matches the change from resultant order 42 for `U^7B` to 34 for `U^5B`.

## Disposition

All requested quantitative assertions are confirmed within their charged premises. They give a finite exception-cardinality bound and a smaller prospective exact resultant; they do not identify exceptions, establish an effective cutoff, prove all-r unitness, alter the accepted producer, or imply REG/source exclusion/JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3821`.
- Body SHA-256:
  `37abed9b3caf2af6ba929967f8036fa8ca92742bf0ada0f6a61d0881874677b2`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
