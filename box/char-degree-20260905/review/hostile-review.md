# Independent review of the characteristic-degree instrument

**Scope update:** the later `normalized-review.md` audits an additional printed necessity from Moh Proposition4.5 and a full-face nondegeneracy theorem. Those results strengthen the y-degree-only scope below: total-degree/top-form rows are now sourced, and a verified proper full augmented ideal proves abstract nondegenerate existence over the algebraic closure. The earlier caution against deriving these facts from Proposition2.2 alone remains valid.

The printed characteristic-degree condition is a valid new necessary refinement, and it excludes the complete four-constant cone family in the question. It is not a low-truncation condition in the existing engines. The frozen reports establish an inclusion of a degenerate locus in the support chart; they do not establish that this locus exhausts the chart. Therefore the cone exclusion by itself cannot be promoted to a branch kill.

This review reads the frozen inputs at `/tmp/jc2-lane.Q25z05/inputs/` and the existing engines without changing either. The source agent independently inspected the page images and confirmed the specialization and effective-index details below. This review also read the corresponding local PDF text. Exact controls are in this directory; no fleet computation is claimed by this independent review.

## 1. Correct logical premises

The frozen corrected `(99,66)` report, lines 184–188, constructs support-chart points with `F=h2^3`, `G=h2^2`, and `J=0`. It explicitly limits their scope. The preceding lines 168–170 record nonunit stronger Jacobian/D1 prefixes and separate actual-constant controls. There is no claim or proof that all survivors are those points.

The cone gate, lines 167–168, explicitly states `Delta_T subset V(R_T)` and rejects equality of these loci. Its lines 115–119 also explain that raw Delta must first be cut by the inner `h2` rows; raw Delta is not automatically a solution to every support row.

Consequently:

* A unit after pulling the enlarged ideal back to Delta proves that Delta is excluded.
* It proves nothing by itself about the unrestricted complement of Delta.
* A full-chart unit requires a certificate retaining all ambient source coordinates and every declared localization.
* A nonunit ideal, including one with a positive dimension, does not exhibit a point with `J != 0`. That needs an actual point, lifting through the maps, and an exact evaluation of its full Jacobian.

The user’s proposed dichotomy can therefore legitimately end at typed `OPEN` if the exact computation is incomplete or a nonunit ideal has no certified point. It cannot be completed by interpreting nonunit as nondegenerate.

## 2. The source allows exact y-degree and a scalar unit leader

Moh, printed p151 Lemma 2.1, gives the Keller criterion `e=n-1`. Printed p152 Proposition 2.2(1) supplies exact `deg_y T_i^psi(f(x,y),g(x,y))=-mu_i` for `M_i <= e`. Clause (2) supplies a unit leading coefficient for `M_i < e`. Printed p154 explicitly says that “monic” means that the highest coefficient is a unit; it does not mean the scalar is already 1. A fresh nonzero scalar and reciprocal are therefore legitimate graph/localization coordinates without spending a dilation.

The specialization must be read correctly. Printed p152 explicitly extends `psi:k[x]->k` to the formal polynomial ring with `f,g` as symbols. One first specializes the coefficients of `T_i`, obtaining a polynomial in `k[f,g]`, and then composes it with the full polynomials `f(x,y),g(x,y)`. One does not evaluate the source pair at `x=0`. Proposition 2.2 explicitly states the degree of that full composite. Thus the coefficients of `y^q` above the target vanish as polynomials in x, and the leading coefficient is a scalar.

Only y-degree is established here. The stronger assertion `total_degree T_i^psi <= -mu_i` needs an independent source argument. No such argument is used in this review. A control below accepts `y^55+17*x^197*y+5`, of exact y-degree 55 and scalar leader, despite its total degree 198. Such a polynomial is an extractor control, not a purported realized characteristic polynomial.

For every effective tower index `i <= s`, one has `M_i < n-1`, so exact y-degree and a scalar unit are available. If the notation includes the terminal characteristic index with `M_h=e=n-1`, clause (3) instead gives leader `c*f_e(x)`, which is affine nonconstant under Lemma 2.1. The scalar-unit assertion does not extend to that terminal index. The distinction must remain explicit in a uniform theorem.

## 3. Arithmetic and exhaustive target family

Use `F` for the polynomial of degree n and `G` for that of degree m, reversing Moh’s lower/upper degree names as necessary. For the two cases:

| datum | M1 | M2 | d2 | q2=M2-M1 | lambda2 | -mu2 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (99,66) | -66 | 77 | 33 | 143 | -1815 | 55 |
| (108,72) | -72 | 81 | 36 | 153 | -2268 | 63 |

Here `lambda2=n*M1+d2*q2`, `mu2=lambda2/d2`. In particular the D=108 characteristic degree is **63**, not 60. Its first three degree ratios are `108:72:63=12:8:7`; the `(99,66)` values give `9:6:5`.

In both cases `n/d2=3`, and Proposition 3.1 on p157 permits precisely the weighted monomials

`G^3, F^2, F*G, G^2, F, G, 1`.

The first two have weighted degree `B=2n=3m`, and their common monic y-leading term forces coefficient -1 on `F^2`. The resulting exhaustive family is

`Q=G^3-F^2+a*G^2+b*F*G+c*F+d*G+e`.

All five lower scalar coefficients belong in the necessary existential chart. They may subsequently be eliminated only by recorded equations with justified leaders. The constant e does not occur in any of the degree/leader rows when the target is positive; it remains a free target coordinate. The statement that all five coefficients become determined by attainment is therefore inaccurate. No equation can determine e from these rows alone.

## 4. Exact polynomial rows and weights

Let d be 55 or 63 and B be 198 or 216. In a chart retaining all source coefficient coordinates and the five target coefficients, write `Q=sum Q_pq x^p y^q`. Each `Q_pq` is polynomial in the chart coordinates. Add

* `Q_pq=0` for `q>d`, `p>=0`, `p+q<=B`;
* `Q_pd=0` for `p>0`, `p+d<=B`;
* `Q_0d-L=0` and `Z*L-1=0`.

These equations assert exact y-degree d and a scalar unit leader. Equality uses target subtraction. Zeroing `Q_0d` would produce a false unit and reject the elementary positive control `Q=y^d`, `L=Z=1`.

The engine coordinates satisfy `x=t^-1`, `y=w/t=(1+z)/t`. Therefore

`KQ=t^B Q(t^-1,w/t)`

and

`[t^r w^q]KQ=[x^(B-r-q)y^q]Q`.

Converting a z band to a w band is an invertible rational triangular coefficient operation, not a specialization. The corresponding index schedule is all `q>=d` with `0<=r<=B-q`, subtracting L at `(r,q)=(B-d,d)`, together with `Z*L-1`. The formal scalar row counts, including structural zero rows, the leading equation, and the localizer, are 10,441 and 11,936. Only the part `t<=B-d` of KQ is needed; total degrees above d with y-degree below d must be retained freely.

For `(99,66)`, the normalized expression is

`KQ=KG^3-KF^2+b*t^33*KF*KG+a*t^66*KG^2+c*t^99*KF+d*t^132*KG+e*t^198`.

The leader is at `t^143*w^55`, while the constant Jacobian coefficient is at `t^163`. For D=108 replace the shifts by `36,72,108,144,216`; the leader is at `t^153*w^63`, and the constant Jacobian is at `t^178`.

The relation `-mu2=(n/d2)*m-q2` gives `B-d=q2`. These defects 143 and 153 are the intrinsic first characteristic gaps, not small depths. They are lower than the corresponding Jacobian constant defects by 20 and 25, but stages 0–8 only reach the small pole/Jacobian windows described by their schedules. Adding these full rows at stage 0 is a legitimate independent instrument, not a shallow truncation computation.

In the D2 monomial weights, the actual leader slots have weights `3*143+4*55=649` and `4*153+5*63=927`. Thus they are not small D2 bands either. In the global defect grading one may assign the target variables weights `b=33,a=66,c=99,d=132,e=198,L=143` in the first case, with the analogous values in the second. The localizer has weight zero after assigning `Z=-143` or `-153`; that does not turn the high-weight coefficient-identification equation into a low-depth row.

One must never ask a truncated polynomial for its missing leading coefficient and treat the omitted value as zero. Doing so would manufacture a unit when adding `Z*L-1`.

## 5. Full Delta exclusion and exact unit identity

Write the four-constant cone family as

`F=H^3+u*H+v`, `G=H^2+r*H+w`.

Then Q is a scalar polynomial in H. Since H is monic of y-degree h=33 or 36, every nonzero nonconstant scalar polynomial in H has y-degree a positive multiple of h. Neither 55 nor 63 is a multiple of h. This alone proves the exclusion, including the zero-polynomial case explicitly.

The exact polynomial control records more: the high coefficients at y-degrees `5h,4h,3h,2h` successively yield rational-unit pivots

`b=-3r`,

`a=2u-3w`,

`c=-r^3-r*u+3r*w+2v`,

`d=r^2*u+3r*v+u^2-4u*w+3w^2`.

After these substitutions the H coefficient also cancels identically, leaving

`Q=e-r^3*v+r^2*u*w-r*u*v+3r*v*w+u^2*w-2u*w^2+v^2+w^3`.

Thus the target coefficient is zero, the attainment row becomes `-L`, and the literal ideal identity

`Z*(-L)+(Z*L-1)=-1`

certifies a unit on the pullback to Delta. All four cone constants and all five characteristic coefficients were retained. This is a complete Delta exclusion, not an unrestricted branch certificate.

The warning about order is material: the raw y55 coefficient need not vanish on Delta before the higher-degree equations. For example `H=y^33+y^22`, pure `F=H^3,G=H^2`, and target coefficient `d=1` gives `Q=H^2`, with y55 coefficient 2 and degree 66. The degree bound excludes this choice first. The exact control checks it as a negative example to the stronger false claim.

## 6. Uniformity and gate limits

The same construction is uniform as an existential polynomial refinement of a chart whose characteristic datum has been realized: recursively use the finite standard-monomial expression supplied by Proposition 3.1, retain its permitted coefficient variables, identify the exact y-degree by Proposition 2.2, and localize the scalar leader for every effective index. Coefficient extraction is finite because the source and recursively composed target polynomials have finite degree bounds.

The theorem does not supply a uniform small truncation depth or a uniform computational complexity. The two explicit first-characteristic defects already refute describing this instrument as reachable at stages 0–8 by the old band depth alone. For later indices one must declare the normalization and actual total-degree bound used for extraction; a y-degree bound is not a total-degree bound. Nothing in the cited statements promotes all 38 family-C leaves, or D=108, to killed branches without their own full necessary rows and exact elimination.

Attainment also is not logically equivalent to `J != 0`. It excludes the specific common-H locus when a required degree is incompatible with deg H. Other degenerate configurations require separate analysis. A loudly reported necessary-chart survivor must therefore include a concrete point satisfying every row claimed and a directly evaluated nonzero Jacobian, exactly as the requested gate requires.

## 7. Artifacts and controls

`delta_attainment_control.py/.json` uses exact SymPy rational polynomial arithmetic in the declared ring, records every leader and map, rechecks all H powers above one, and derives the literal -1 ideal identity. It also checks a nonzero raw y55 coefficient and the distinction between y-degree and total degree.

`row_index_control.py/.json` independently checks the x,y-to-t,z-to-t,w monomial map, both complete index counts, positive points with scalar unit leaders and allowed high total degree, separate wrong-high-degree and nonconstant-leader failures, and the leading-row target subtraction. Its positive points test row extraction only and are never labeled actual source pairs.

These controls pass over Q. They supply source-independent arithmetic checks for the review. They do not replace the coordinator’s full finite schedule, printed-necessity audit, gauge audit, derived-face checks, or fleet termination receipt.
