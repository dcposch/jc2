# Cubic-scroll conic nets and the double-root étale locus

First action 2026-09-12 00:13:37 UTC; reserve00:29/HARD00:32 unchanged.
Manual co-research only; no promotion or execution. Sole input TASK.md,
SHA256 b83818c6fad6a7c2179e8cb7ed269e483d31a41306fc321150449ff8d94550fd,
matched before fresh WHOLE read. No outside or live report was consumed.

## 1. Exhaustive normal forms

All assertions below are independently derived, still producer-level and
unreviewed. The proposed dichotomy is correct; moreover G is removable,
so there are exactly TWO orbits over C under source automorphisms of F1
and target projective transformations.

Restriction of the net to E has image in H⁰(E,O_E(1)). Basepoint-freeness
forces image dimension2: a one-dimensional image has a common zero on E.
Choose its basis as u,v and its one-dimensional kernel as Q3. Hence

    Q1=wu+A u²+Buv+C v²,
    Q2=wv+D u²+Euv+F v²,       Q3=q3(u,v)≠0.

Here the coefficient E in this display is unrelated to the exceptional
curve. A zero q3 would contradict independence of the three sections.
Over C a nonzero binary quadratic is squarefree or a square. Source GL2
and target rescaling give respectively q3=uv or q3=u².

Squarefree case: replace w by the coordinate w'=w+A u+Fv; then subtract
(B−F)Q3 and (E−A)Q3 from Q1,Q2. This gives

    [wu+a v² : wv+b u² : uv],       a=C, b=D.

The point (0:1:0) is an extra base point if a=0; (1:0:0) is one if b=0.
Conversely ab≠0 leaves no common zero away from P, since Q3=0 forces one
of u,v zero. On E the restrictions u,v have no common zero.
Under u=λu',v=μv',w=νw' and corresponding target diagonal scaling,
a'=aμ²/(λν), b'=bλ²/(μν). Take λ=1, μ³=b/a, ν=aμ²: both become1.
These are permitted invertible transformations over C.

Double case: take w'=w+E u+Bv, subtract (A−E)Q3 from Q1 and DQ3 from Q2.
The result is

    [wu+C v² : wv+G v² : u²],       G=F−B.

C=0 gives the extra base point (0:1:−G); C≠0 gives none. The exceptional
restrictions remain u,v. Thus G is genuinely arbitrary in this displayed
family, and the family is not excluded by basepoint-freeness or finiteness.

It has no residual G modulus. Substitute

    v=v'+h u,       w=w'−2Ch v'+(2Ch²−2Gh)u.

Subtract the resulting u² term from Q1; replace Q2 by Q2−hQ1 and subtract
its u² term. The new normal form has C'=C, G'=G−3Ch. Choose h=G/(3C).
Then w=Cw'' and target division of the first two coordinates by C give
the representative [uw+v²:vw:u²]. No division by G was used, including G=0.

Every displayed admissible net is finite: its pullback line divisor is
D0=2H−E. It has intersection1 with E and intersection2d−m>0 with every
other irreducible curve of plane degree d and multiplicity m≤d at P.
A positive-dimensional fibre would contain a contracted curve, impossible.
Properness then gives finiteness, and D0²=3 gives degree3 onto P².
The two cases are distinct intrinsically: the unique section restricting
to zero on E has divisor E+f1+f2 or E+2f0. Automorphisms of F1 preserve
its unique exceptional curve and cannot change these multiplicities.

The ROOT message's fixed-compactification extension also checks out.
For ANY finite degree3 morphism F1→P², its ample pullback is aE+bf with
a>0,b>a integers, and a(2b−a)=3. The possibility a=3,b=2 violates b>a;
therefore a=1,b=2, giving E+2f=2H−E. Its coordinate sections form exactly
such a net. This extension is only for the fixed surface F1, not arbitrary
degree3 covers or compactifications.

## 2. Full ramification and étale charts in the double case

Keep arbitrary C≠0,G, without using its further normalization. The
homogeneous Jacobian determinant of the three conics is

    −2u(uw+2Guv−2Cv²).

Thus off E the critical divisor is f0={u=0} plus the proper transform R1
of the displayed smooth conic. To check E rather than discard it, use
the blowup chart w=1, v=t, u=ta. After cancelling the base factor t the
map is [a+Ct:1+Gt:ta²]. Where 1+Gt≠0 its affine Jacobian is

    a(a+2Gta−2Ct)/(1+Gt)³.

There is NO factor t. At E={t=0} this vanishes only at a=0, where the
two reduced branches f0={a=0} and R1={a+2Gta−2Ct=0} meet transversely.
This agrees with the divisor class
(H−E)+(2H−E)=3H−2E=K_W+3(2H−E).
The other exceptional points are unramified, also seen in the full chart
below. Hence the ramification divisor is exactly f0+R1, not that sum plus E.
For smooth complex surfaces the invertible differential criterion gives
the étale locus precisely as its complement.

The ruling identifies W−f0 with A¹_v×P¹_[λ:μ], with blowdown
[u:v:w]=[λ:λv:μ]; λ=0 is E−f0. The morphism on this chart is

    [μ+Cλv² : vμ+Gλv² : λ].

Put h(v)=2Cv²−2Gv. The section R1 is μ=h(v)λ, so its complement has
the GLOBAL coordinate r=λ/(μ−hλ), including r=0 on E−f0. Its inverse
is [λ:μ]=[r:1+h(v)r]. Consequently the ENTIRE étale locus is A²_(v,r),
not just the chart where w is finite, and the map there is

    [1+r(3Cv²−2Gv) : v+r(2Cv³−Gv²) : r].

These homogeneous coordinates never vanish simultaneously: r≠0 gives
the third coordinate, while r=0 gives the first coordinate1. At r=0,
in target Y1≠0 coordinates, the Jacobian is a nonzero unit (up to orientation).
Thus the chart explicitly retains the unramified exceptional section.

## 3. Every target line, and the exact obstruction

For any nonzero triple (α,β,γ), the pullback of its line is the zero set of

    L=α+βv+r[α(3Cv²−2Gv)+β(2Cv³−Gv²)+γ].

This polynomial is nonzero: L=0 identically would force α=β=0 by its
r⁰ coefficient, and then γ=0. It is also nonconstant. If β≠0, its r⁰
coefficient is nonconstant. If β=0 and α≠0, its coefficient of rv² is
3Cα≠0. If α=β=0, it is the nonzero multiple γr. This covers ALL lines,
not only a finite list or lines in a preferred position.

For the chosen target-affine plane P²−line, the full étale donor is
therefore EXACTLY D(L)⊂A²_(v,r). Its coordinate ring is
C[v,r,L⁻¹], in which L is a nonconstant unit. A dominant morphism from
A² would give an injection of this ring into C[x,y], but send L to a
constant k∈C*, because those are all polynomial-ring units. Then nonzero
L−k maps to zero: a contradiction. No degree condition on the proposed
dominant first leg is needed.

In particular, a factorization A²→W→P² whose composite lands in ANY such
target-affine plane and is étale cannot use this double-root map: the
chain rule forces its first-leg image into D(L), and dominance contradicts
the unit argument. This is not a reduction of arbitrary Keller maps to W.
It is not an assertion about arbitrary target base changes or nonprojective
changes of compactification.

Controls preserve the scope. C=0 is not a counterexample: there is then
an additional base point. Deleting E as well would miss genuine étale
points and is not the chart proof given here. Conversely, WITHOUT deleting
a target line, the entire étale locus really IS A² and admits its identity
map; the all-line unit obstruction must not be misstated as forbidding a
dominant A²→W_ét in isolation. The nonconstant-unit conclusion uses the
target-affine condition essentially.

## Custody and limits

The ROOT in-turn hint concerning D²=3 was independently checked above;
it supplied no additional document or accepted premise. Only TASK.md was
read as input. No scientific computation, external lookup, live-peer read,
new agent, coefficient fixture or source modification occurred. The
manual test had an original ≤20-minute UNMEASURED planning bound, not a
runtime claim. No mathematical GAP or new canonical OPEN is introduced;
independent FIRST review remains necessary before promotion. No conclusion
about the squarefree net's donor is imported or asserted here.
No novelty or literature-priority claim is made.

Own whole-read, sole-input postpin and destination-collision checks must
precede the unique closing marker. This report and documentary PINS/custody
are the only authored deliverables; no follow-on or execution is authorized.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8113`.
- Body SHA-256:
  `615175abb320f2e071b9841d15a3f996adeb86d312c0cf6ea6aa1c7879fdd7de`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
