# F2 published-chain discriminator: a three-polygon necessary family

Status: **PROVISIONAL DESK DERIVATION — independent gate required.** One bounded discriminator, not a solve, classifier run, full source attachment, or new JC2 theorem. Frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d`. Author `nonemptiness_certificate`, 2026-09-06.

## Outcome and exact interface

Card 2's `q=5` is derivable, but not from its guessed successor. The first lower face has a degree-one root and therefore has no split-root alternative. The initial upper face has the two familiar quartic multiplicity patterns `(2,1,1)` and `(2,2)`. Applying the actual GGV endpoint statements gives a finite necessary family **without making the optional final upper shifts**. This stopping choice matters: a later `x^-3` shift can destroy the zero lower-support bound.

Here is the exact proposed implication. Work over an algebraically closed characteristic-zero field. Suppose an **actual polynomial Keller pair** of degrees `(75,125)` is already a standard `(3,5)` pair generating the published F2 row

`A0=(5,20), A0'=(1,0), A1=(7/5,2)`.

Then there exist polynomials `U,V` with `[U,V]=x^3` and one of the following Newton polygons (listed vertices, convex hull understood):

| case | N(U) | N(V) |
|---|---|---|
| unequal terminal endpoints | `(0,0),(15,15),(15,6),(3,1)` | `(0,0),(25,25),(25,10),(1,0)` |
| common successor at direction `(-1,3)` | `(0,0),(15,15),(15,6),(3,0)` | `(0,0),(25,25),(25,10),(5,0)` |
| common successor at direction `(-1,4)` | `(0,0),(15,15),(15,6),(9,0)` | `(0,0),(25,25),(25,10),(15,0)` |

All three have total degrees `(30,50)`. This is a finite polynomial **monomial-Jacobian receiver** statement, not a Keller counterexample acceptance theorem. No row ideal is emitted or claimed proper. All nonzero vertices and the Jacobian scalar are retained as necessary guards. The constant coefficients may be made nonzero by target translations.

| arrow | status and exact scope |
|---|---|
| arbitrary actual `(75,125)` pair → standard F2 pair | Conditional external/written input: pinned Strinz Theorem A plus the published census. Its full separate proof bundle is not replayed here. Not an assertion about the original coordinates or Roy coefficients. |
| literal standard F2 pair → the three receiver polygons above | New **provisional derivation in this packet** from the named primary lemmas and the already promoted affine/Euler normalization. No global minimal-gcd hypothesis is added. |
| receiver polynomial point with `[U,V]=x^3` → original polynomial Keller pair | **MISSING.** Inverse Laurent coordinate changes must cancel all negative powers and restore source degrees, starting triple, root data and any desired literal scalar pins. Bare receiver rows do not impose that. |
| receiver / F2 normalization → Roy B0 or Strinz carrier coefficients | **MISSING coefficientwise attachment.** The finite polygon result does not supply those source-image equations or prove their normalizations necessary. |

Thus an exact exclusion of all three fully guarded receiver systems would be usable in the necessary direction after a gate of this reduction. Properness of one receiver system alone would not certify a JC2 counterexample. No exclusion, properness, novelty priority, new licensed compute client, or performance win is claimed.

## 1. Entry normalization and the independently derived denominator

Write the standard variables as `(u,v)` and put `w=u v^5`. The starting face has weights `(5,-1)`, endpoints `3(1,0),3(5,20)` for P and the corresponding multiples by 5 for Q. Commutation and coprimality give

`P_face=lambdaP R0^3, Q_face=lambdaQ R0^5, R0=u r(w)`,

where `deg r=4`, `r(0)!=0`. The F2 generated corner identity is

`A1=A0'+gamma(1/5,1)`.

The published F2 row supplies `gamma=2`, not an arbitrary choice of `q`. Equivalently the chosen nonzero root of `r` has multiplicity exactly two. This is precisely the fifth-root Puiseux successor of the census; here we will later cut the reciprocal variable directly in the unramified Laurent ring.

By GGV1 Theorem 7.6(3), for this type-II starting corner the Euler element E of Theorem 2.6 has end parallel to `(5,20)`. Its weight is `5-1=4`, while `(5,20)` has weight 5. Consequently

`en_(5,-1) E=(4,16)=(4/5)(5,20)`.

The reduced denominator is **5**. This derivation precedes and is independent of `A1`. Polynomiality of E implies

`E=u v f(w), deg f=3`.

Indeed the nonnegative integer solutions of `5i-j=4` are `(1+k,1+5k)` and the endpoint has `k=3`. A start parallel to `(1,0)` would be nonintegral; the Euler start is `(1,1)`.

For the later lower analysis we first use affine source changes to make the top vertex `(15,60)` unique, put P in the rectangle `deg_u<=15, deg_v<=60`, and arrange its highest-v coefficient to be a scalar times `u^15`; the same change works for Q with rectangle `(25,100)`. These are the general polynomial/Euler arguments in the terminal promoted normalization packet, **not** a presumption that every F2 pair has Roy's five pins. Their hypotheses are just the total-degree bounds, the `(5,-1)` support bound and the nonzero corner coefficients, which this standard row supplies. The changes are `u -> u-sv`, then `u -> u-r`; both strictly lower `(5,-1)` weight and leave the starting face unchanged. The earlier proof derives `s` and `r` from coefficient ratios with nonzero leading coefficients. We use only that affine/rectangle conclusion, not its separate B0 pin-preservation assertions.

Swap variables, writing `(x,y)=(v,u)`. Denote the resulting pair again P,Q. The common upper corner is now `(20,5)` times `(3,5)`, the direction is `d0=(-1,5)`, the opposite face endpoint is `(0,1)` times `(3,5)`, and the Euler start is `(16,4)`. The bracket changes sign under the swap. Both total-degree and y-degree ratios are `3/5`; the highest-x and highest-y terms are the unique common-corner terms.

## 2. The lower side: checking the positivity range, not assuming it

Let d be the closest lower edge to `(1,0)` among the two polygons. At d the end points are still `3(20,5),5(20,5)`. It lies strictly between `(0,-1)` and `(1,0)`, since the highest-x vertex is unique and the initial face supplies points of smaller y-degree. GGV2 Proposition 2.1, whose statement is for a polynomial Jacobian pair, puts d strictly below `(1,-1)`.

The Corollary 7.4 positivity condition is not omitted. At least one of `P(x,0),Q(x,0)` is nonconstant: if both were constant, both x-derivatives would vanish on that line, contradicting the constant nonzero bracket. Because `rho>0` at d, that polynomial has positive d-value. Both d-values are computed at the common corner and have ratio `3/5`, hence both are positive. All intermediate directions up to d0 have the same common vertex or positive endpoint values, so Remark 7.5 gives the whole required positive interval.

Also both polygons have an edge at d. Otherwise their leading bracket is zero (its predicted weight exceeds zero), but a monomial leading form commuting with a nonmonomial homogeneous form of nonzero value would force the latter to be a monomial, by the common-power lemma. This is a contradiction.

Corollary 7.4 therefore supplies `P_d=R^(5m)` with `m=3`, and the analogous conclusion for Q. The common primitive root has end `(4,1)`. It is polynomial at this first edge: a Laurent polynomial whose positive power is polynomial cannot have a negative minimum x-exponent. Its y-degree is exactly one. Thus, up to nonzero scalars,

`R=x^(4-k)(x^k y-lambda)`, `lambda!=0`, `d=(1,-k)`.

Primitivity of d follows from the y-exponent difference one. Positivity says `4-k>0`; d below `(1,-1)` says `k>1`. Hence **k=2 or3**. There is one nonzero root, not the b=2 split-root situation of GGV2 Proposition 3.12 / the approximate-roots proposition. Those more complicated cited alternatives are unnecessary here.

Cut this root by `y -> y+lambda x^-k`. The positive face collapses to the common vertex and the d0 face is unchanged, since `k<5`. The total-degree and y-degree ratios are preserved. If another lower edge lies strictly between `(1,-4)` and the removed edge, positivity follows directly from its common end `(20,5)`; Corollary 7.4 applies again. Its root still has end `(4,1)` and y-degree one, even though negative x powers are now allowed. Integer k then leaves only k=3 after k=2, and nothing after k=3. Consequently at most two cuts yield

`v_(1,-4)(P)=v_(1,-4)(Q)=0`.

Constants are adjusted to be nonzero after these cuts; they do not affect positive faces. The zero bound follows because `(0,0)` and the common corner both have `(1,-4)` value zero, and no intervening positive edge remains. There is no reliance on silently treating the swapped pair as a standard/minimal `(m,n)` pair for GGV2 Proposition 2.2. The elementary line argument above replaces that scope-sensitive invocation.

For completeness, the Euler element used by Corollary 7.4 still has denominator 5 after these Laurent cuts. The d0 face remains `R0=y r(x^5 y)` of weight 5 and y-valuation one. Two weight-4 Euler solutions differ by a weight-4 element H commuting with R0. The homogeneous common-power lemma would imply `H^5=c R0^4` for nonzero H; y-valuations would give `5 ord_y H=4`, impossible. Hence the Euler solution is unique even in the Laurent x-ring, and it is the unchanged swapped original solution. This argument does not misapply Proposition 2.11's positive-rho hypothesis at d0.

## 3. Both initial upper-root cases, with exact controls

Normalize the selected double root of r to 1. This is an existential nonzero torus scaling over the algebraic closure; it is not a commitment to the remaining Roy terminal coefficients. Since r has degree four and the selected root has multiplicity two, its patterns are `(2,1,1)` or `(2,2)`.

From `[E,R0]=R0/3` one obtains exactly

`4 w f r' - 5 w f' r - f r = r/3`.

GGV1 Proposition 2.11(3), applied at the original positive-rho direction `(5,-1)` using `z=u^(1/5)v` and `w=z^5`, says that f is squarefree and contains every distinct root of r.

For `(2,1,1)`, write `r=(w-1)^2(w-a)(w-b)` and `f=c(w-1)(w-a)(w-b)`. Evaluation at a root lambda of multiplicity e gives `(4e-5)lambda f'(lambda)=1/3`. The three evaluations imply `a+b=3, ab=3, c=1/9`. Thus

`r=(w-1)^2(w^2-3w+3), f=(w-1)(w^2-3w+3)/9`.

For `(2,2)`, write `g=(w-1)(w-a), r=g^2, f=g(cw+d)`. The same ODE gives

`a^2-3a+1=0, d=-1/(3a), c=(1+a)/(9a^2)`.

All indicated roots are nonzero and distinct from 1; the extra Euler root in the second case is `3a/(1+a)` and is distinct from both double roots. The first quadratic has discriminant -3, the second discriminant 5. The owned checker verifies the complete multiplication identities over Q and over `Q[a]/(a^2-3a+1)`, not just evaluations at sample points. This is known-looking carrier structure, not a novelty claim: the pinned public record already uses the same quadratic coefficient field and squarefree/repeated-root branches.

In the swapped variables the initial root is `R0=y r(x^5 y)`. A double-root cut `y -> y+lambda x^-5` moves its opposite endpoint from `(0,1)` to `(5,2)` and leaves its main endpoint `(20,5)` fixed. For example, after lambda=1,

`R0 -> (y+x^-5)(x^5 y)^2 h(1+x^5 y)`, `h(1)!=0`, `deg h=2`.

Its least-y term is a nonzero multiple of `x^5 y^2`. Both initial quartic cases satisfy this. The cut strictly lowers `(1,-4)` weight, so the zero lower bound survives. Let the pair at this exact stage be P1,Q1. It is Laurent in x, polynomial in y, has constant nonzero bracket, and has common end `(5,2)` at d0, scaled by `(3,5)`.

## 4. Exact successor alternatives and why we stop here

Apply GGV1 Proposition 8.2(1–2), whose statement is explicitly for Laurent `L^(1)` pairs with constant bracket; no global-minimality or polynomial-axis condition is required. If the next ends are proportional, the common normalized end `(a',b')` is integral, `0<=b'<2`, and

`-a'+5b'<5`, `5b'-2a'>0`.

The finite list is

`(-4,0),(-3,0),(-2,0),(-1,0),(1,1),(2,1)`.

Theorem 2.6(4) excludes `(1,1)`. For `(-2,0)`, the direction is `(-2,7)`; the Euler weight is 5. A start parallel to `(5,2)` would be `(25/4,5/2)`, impossible in the integer lattice, so its start is `(1,1)`. Its end cannot also be `(1,1)` because E would be monomial; a parallel end would be `(-5/2,0)`, also impossible. For `(-4,0)` the same argument at `(-2,9)` gives a nonintegral parallel start and end `(-7/2,0)`.

For `(2,1)` the direction is `(-1,3)`. Apply Proposition 8.2 once more. A proportional successor has b''=0 and `0<-a''<1`, impossible for an integer. An unequal successor would require an integer `k>=1` with `k+1<2`, also impossible. This rules out `(2,1)` without assuming a terminal list.

The remaining proportional ends are precisely `(-1,0)` at `(-1,3)` and `(-3,0)` at `(-1,4)`. They already lie on y=0, so no additional upper vertices intervene before the horizontal bottom edge. Their common face roots have shapes `x^-1 r2(x^3 y)` and `x^-3 r2(x^4 y)`. In either case r2 must be a square of a nonzero-root linear factor: a simple-root shift would give respectively `(2,1)` (just excluded) or `(1,1)` (Euler forbidden). This double-root fact is not needed merely to list the polygons but verifies the root-splitting alternatives.

If the next ends are unequal, Proposition 8.2 gives `(k+1)2<5`, so k=1 and the ends are `{(-1,0),(2,1)}`. Parallelism of the two edge vectors for `(m,n)=(3,5)` forces

`en P1=(2,1), en Q1=(-1,0), direction=(-5,13)`.

Indeed `(15,6)-(2,1)=(13,5)` and `(25,10)-(-1,0)=(26,10)` are parallel; the transposed assignment has nonzero cross product. The integer lattice, y>=0 and the zero lower bound determine the last P segment to `(0,0)`; Q already ends on y=0.

The full polygon determination now uses explicit support half-planes, not just an endpoint sketch. In all cases `y>=0`, `x-4y<=0`, and `-x+5y<=5m` for each member with multiplier m. In the unequal case the additional bound is `-5x+13y<=m`; for m=3 its lattice hull replaces the fractional axis endpoint by `(0,0)`, while m=5 has axis endpoint `(-1,0)`. In the common cases add respectively `-x+3y<=m` or `-x+4y<=3m`. Together with the actual displayed vertices these bounds give exactly the polygons listed after inversion in the outcome table.

**Do not automatically continue cutting.** Removing the common `(-1,4)` face by an `x^-4` shift preserves the zero `(1,-4)` bound, but a subsequent nonzero `x^-3` shift can change it to `v_(1,-3)=5m`, with new axis vertex `(5m,0)`. The tentative two-case terminal-only polygon claim would therefore need new lower-support data. We avoid that issue by retaining the three genuine cases above. This is a deliberate mathematical stopping rule, not deletion of a branch.

## 5. Monomial-Jacobian map, sign and the missing reverse arrow

Use the Laurent automorphism

`T(x)=x^-1, T(y)=x^5 y`.

It is an involution, acts on exponents by `(i,j)->(-i+5j,j)`, and has coordinate Jacobian `-x^3`. The polygons in section 4 map into the nonnegative quadrant, hence T(P1),T(Q1) are ordinary polynomials. The table at the beginning is the literal image. If `[P1,Q1]=c`, then `[T(P1),T(Q1)]=-c x^3`; replacing the second member by `-T(Q1)/c` normalizes the bracket to x^3. The earlier source swap contributes another minus sign relative to the original bracket. No fifth-root ramification occurs in this receiver map: its exponent determinant is -1.

All source cuts are invertible in `K[x,x^-1,y]`, but not polynomial automorphisms there viewed as maps of the affine plane. To go backward one must choose their parameters and verify that all negative x powers cancel after undoing T and the cuts; one must then undo the swap/affine changes and check the original polynomial source and degrees. Those are actual equations, not guaranteed by `[U,V]=x^3`. As a simple negative control, `(U,V)=(x,x^3 y)` has bracket x^3, while T(U)=x^-1 is not polynomial. This fixture does not satisfy the large polygon guards and is not offered as a counterexample to a stronger, unproved guarded reverse theorem.

The separate missing Roy/Strinz arrow remains particularly important. Roy's certified ramified chart has bracket `X^4`, terminal direction `(5,-17)`, and terminal vertices `(4,1)/(1,0)`; the modified chart has exponent determinant -3 and bracket `-3 xi^2 y^2`. The historical Moh receiver has degrees `(25,15)` and bracket `c gamma^2`. Our necessary receiver has degrees `(30,50)`, bracket x^3 and an unramified involution. These literal presentations are not equal, but differing coordinates do not prove different moduli or mathematical novelty. No lower coefficient dictionary or reverse Moh lift has been constructed. The pinned Strinz ledger explicitly separates its Theorem A from carrier attachment. The root quadratics obtained here overlap its existing carrier structure, so they are not an independent new obstruction.

## 6. Read perimeter, history, exact controls and custody

History checked against explicit terminal reports, APPROACHES.md, AUDIT.md and `ladder/REDUCTION.md` (there is no root REDUCTION.md), including the earlier D125 source intake and receiver distinction. The terminal 1435 Fable body was read whole only after its collection manifest indicated completion. No 1435-cross submission, body, code, log or receipt, live gate, or `jc2-lean` was read. No AWS, CAS, classifier execution, ideal builder or solve was used.

Primary use and proof-read boundaries:

- GGV1 [arXiv:1401.1784v3](https://arxiv.org/pdf/1401.1784v3): the consumed statements and proofs of Theorem 2.6, Proposition 2.11, Corollary 7.4 (whose printed proof refers to the preceding corollary), Theorem 7.6, and Proposition 8.2 were read; the relevant proof of the preceding common-power corollary and support lemmas was also inspected. The entire paper was not newly replayed. The paper's existence results are named external inputs, not formal certificates in this packet.
- GGV2 [arXiv:1605.09430v2](https://arxiv.org/pdf/1605.09430v2): the whole statements/proofs of Propositions 2.1 and 2.2 and Proposition 3.12 were read, as were the standing hypotheses. Only Proposition 2.1 is actually imported into the lower proof; no swapped-standard assumption is borrowed from Proposition 2.2. Proposition 3.12's split b=2 machinery is not needed.
- Algorithms [arXiv:1708.07936v1](https://arxiv.org/pdf/1708.07936v1): exact F2 table, generated-corner relation and relevant Theorem 2.20 statements/proof passages read. No classifier/census implementation or whole census proof replay. The F2 row itself is the stated input, not inferred from two integers or from the sub-125 result.
- GGHV [arXiv:2204.14178v1](https://arxiv.org/pdf/2204.14178v1): Section 4 polygon-cut arguments read directly for method comparison. There is no imported degree-125 Proposition 4.3; the finite analogue above is this provisional derivation, not a quotation from that paper. The approximate-roots b=2 proposition is not load-bearing here.
- Pinned Strinz HEAD `16ae8b263cb8355c0d107138034aa452444390ff`: whole theorem ledger read; pertinent manuscript sections inspected. Pinned Roy HEAD `d715826f4cd996dc8cb8fcde76c51b525195fac6`: exact initial chain, normalization, source and modified-map sections read; no fresh full intermediate Fitting/forcing proof replay. Previously terminal source-intake and normalization packets supply their stated scoped results only.

`box/d125-published-chain-discriminator-20260906/check.py` uses exact rational dictionary arithmetic. Ordinary and `python3 -O` runs pass. Both modes reject an injected wrong vertex through the actual checker with nonzero exit. Other controls reject a wrong Euler term, wrong q, wrong terminal assignment, wrong inversion exponent and use of an unsafe x^-3 support shift. An initial fixture expectation had the bracket sign reversed; the actual derivative checker caught it, and the fixture was corrected to `[x^2 y,x^-1]=+1`, with transformed bracket `-x^3`. This is recorded rather than calling the initial run a pass. The checker is an arithmetic control, not an independent proof of the geometric implication or a point in any full ideal.

The same checker enumerates the tiny bounded lattice regions cut out by the exact half-planes in section 4 and takes their integer convex hulls. All six polygon hulls equal the displayed vertices after T. This is a support control, not execution of the published chain classifier.

The owned input pins, registration and terminal custody are in `box/d125-published-chain-discriminator-20260906/`. All owned arithmetic writers are finished; no background process or worker is retained. Root controls any independent gate and any later decision. The cheapest honest next discriminator is one different-model proof gate of the three-polygon implication, especially the joint lower-edge positivity and complete lattice hull, followed by a novelty/source-attachment check—not a solve launched from this provisional prose.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20995`.
- Body SHA-256:
  `e11c5d2c0e4570dbe90ee7d60e0d0799bd08da01effb3a7129512b64b5c1538e`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
