# Hostile review: smooth quadratic degeneracy absorption

Reviewer: GPT-5.5 xhigh  
Basis checked: workspace `145f96d65021ef364a5189c4ca385fe09d7b4f46`  
Producer object checked: `73a200972954df9799da77bb25a7b76a591e5ec9:xmodel/bd-a2-smooth-quadratic-degeneracy-absorption-sol56-20260830.md`  
Verdict: `CONFIRM_WITH_CORRECTIONS`

## 0. Custody

The producer body seal verifies: 19665 bytes through `<!-- BODY-END -->`,
SHA-256 `ecff0c0f3b373e00128b10cad561a0738e8db32e60d4c04f475c5e0fa38c25bd`.

The four Section 0 charged integrations were read at the stated workspace
basis and their full-file SHA-256 values match the producer list:

```text
c9871c92ce8748fd934dc57061f667b49952a1aba39aee43eb3af7b0aadbf392
c8dee3199ecfaf73b6debedea625346a11babbe42082cff5bff049f8585763c2
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
```

Correction required: the producer body internally says its frozen basis is
`5bc4eea1...`, while this review was requested and performed on
`145f96d...`. This is custody noise, not a mathematical defect, but promotion
should state exactly which object was reviewed and should not use the
producer's internal frozen-basis line as the review basis.

## 1. DVR common-factor exclusion

Verdict: `CONFIRMED`.

At the generic DVR of an irreducible affine divisor `h`, if `h` divides all
four Miranda coefficients, the special multiplication table is

```text
kappa direct-sum V,        dim(V)=2,        V^2=0.
```

Normality of the localized rank-three integral algebra gives a semilocal
Dedekind order. The displayed special fibre is local, so there is one prime
over the DVR. Since the generic degree is three, the only decompositions are:

```text
e=1, f=3: special fibre is a cubic residue field, radical zero;
e=3, f=1: special fibre is S/(pi)=S/(tau^3), radical square nonzero.
```

No multi-prime case is compatible with a local fibre. Thus a divisorial
common coefficient factor is impossible.

The codimension-two bound is also sound. With no common affine divisor, the
common-zero ideal has height two or is the unit ideal in `C[u,v]`. For
quadratic coefficients, two general complex linear combinations have no
common curve. Since those two combinations lie inside the coefficient ideal,
the coefficient common-zero scheme is a closed subscheme of a complete
intersection of two degree-at-most-two plane curves, hence has length at most
four. This is a scheme-length bound, not just a set-theoretic count.

## 2. Smoothness forces squarefree infinity

Verdict: `CONFIRMED`, with one exposition correction.

The normal-jet proof is valid. On
`S=L_infinity times P1`, let a reduced integral component `C` of bidegree
`(alpha,beta)` occur in `H=X cap S` with multiplicity at least two. Tangent
derivatives along `S` vanish on the reduced component. The first normal jet
is a section of

```text
O_C(A+3B),        deg = beta + 3 alpha.
```

The bidegree convention is the one used in the lattice input:
`A.C=beta`, `B.C=alpha`. For every actual vertical or horizontal curve this
degree is positive: `(alpha,beta)!=(0,0)`. If the normal jet is identically
zero, the ambient gradient vanishes generically along `C`; if it is nonzero,
its pullback to the normalization of the complete curve has a zero, and at
that physical point all ambient first derivatives vanish. Singular components
do not escape the argument because the tangent derivatives vanish on the
reduced nonreduced-support component, and the normal section has a well
defined value at the image point.

The independent intersection calculation checks out:

```text
K_X=-A+B,
p_a(C_i)=(alpha_i-1)(beta_i-1),
C_i^2=2 alpha_i beta_i - 3 alpha_i - beta_i,
C_i.C_j=alpha_i beta_j + alpha_j beta_i  (i != j).
```

Intersecting `H=A=sum m_i C_i` with `C_i`, using
`sum m_i alpha_i=2` and `sum m_i beta_i=3`, gives

```text
(m_i-1)(3 alpha_i + beta_i)=0.
```

Thus each nonzero component has multiplicity one. The exposition should say
explicitly that the distinct-component intersection number is being computed
on the smooth ambient incidence surface; at intersection points of distinct
components smoothness forces the normal derivative to be a unit, so the
intersection product agrees with the product on `S`. The normal-jet proof is
the primary proof and does not depend on this explanatory shortcut.

## 3. Local coefficient basepoint

Verdict: `CONFIRMED`.

At a coefficient basepoint `q`, with parameters `(s,t)`, the first jet

```text
Phi = s p(X,Y) + t r(X,Y) + higher base order
```

has `p,r` cubic sections on `E={q} times P1`. Smoothness along `E` is exactly
the condition that `p,r` have no common zero. They are not proportional, and
the basepoint-free pencil gives

```text
rho=[p:r]:E=P1 -> P1,        deg(rho)=3.
```

The scheme-theoretic blowup factorization is correct. On `p!=0`,
`s=-t r/p + O(t^2)`, so `(s,t)O_X=(t)`; similarly on `r!=0`. Hence
`pi^*I_q=I_E=O_X(-E)`, giving `X -> Bl_q(P2)`. Therefore `A-E` is nef.
Adjunction gives

```text
A.E=0, B.E=1, K_X.E=1, E^2=-3.
```

The different calculation is also correct. In the chart `p!=0`, after
substitution into the fibre derivative,

```text
(Phi_z/t)|_E = (p r_z - r p_z)/p.
```

The Wronskian is not identically zero in characteristic zero for a degree
three morphism, so `E` appears in the ramification/different divisor with
Cartier coefficient exactly one:

```text
R_pi=E+D,        D effective,        D ~ 2A+B-E.
```

Moreover `D|E=Ram(rho)` and `D.E=4`. Riemann-Hurwitz gives total
ramification four; a degree-three characteristic-zero map has local
ramification contribution at most two at one physical point, so the support
of `D cap E` contains at least two distinct physical points.

Finally,

```text
D=(A+B)+(A-E)
```

is ample because `A+B` is the restriction of an ample ambient divisor and
`A-E` is nef. The reduced support of an effective ample divisor on a smooth
projective surface is connected by Hodge index. Thus the promised `-3` curve,
coefficient-one different, ample connected residual divisor, and two physical
attachments are all established.

## 4. Graph-cycle boundary attack

Verdict: `CONFIRM_WITH_CORRECTIONS`.

The graph argument itself is valid. If the connected total transform of
`Supp(D)` is not a rational tree, the rational-forest obstruction has already
fired. If it is a tree, the rational curve `E` attaches to it in at least two
distinct physical points. Any embedded resolution only subdivides paths or
adds exceptional vertices over those physical points; it cannot identify the
two attachments. The resolved full boundary therefore contains a graph cycle.

For an infinity basepoint, `E subset H`, hence `E` is a boundary component.
The components of `D` are either in `H` or are closures of the affine
non-etale support, so they are also in the full first-leg boundary used by
the lattice integration.

For an affine common zero, `E` is not an infinity component. It is nevertheless
boundary after the Stein bridge: it is the preimage of a contracted point of
`Y` that lies in the non-etale locus of `g2`, and the promoted first-leg
sandwich says the first-leg image misses that non-etale locus. Thus the lift
of the first leg avoids `E`.

Correction required: the producer's sentence "every other component is the
closure of affine non-etale support" is too narrow when there are several
affine basepoints. For a chosen `E_q`, the residual divisor `D=R_pi-E_q` may
contain another exceptional curve `E_q'`. Such a curve is still boundary, but
for the same contracted-non-etale-point reason, not because it is the closure
of a divisorial affine non-etale component. Replace the sentence by:

```text
Every component of D is boundary: components in H are infinity boundary;
components meeting the no-basepoint affine locus are closures of the
non-etale support there; and exceptional components over other affine
coefficient basepoints are preimages of contracted non-etale points missed by
the first leg.
```

This is a repair of wording, not of the proof.

## 5. Affine Stein bridge

Verdict: `CONFIRM_WITH_CORRECTIONS`.

The sequence

```text
0 -> O(-3) --Phi--> O -> O_Xaff -> 0
```

is legitimate: `Phi` is a nonzero section of an invertible sheaf on the
integral threefold `A2 times P1`, hence a nonzerodivisor. Relative cohomology
over `A2` gives

```text
0 -> A0 -> (pi_0)_*O_Xaff -> A0^2 -> 0,
```

and this splits as an `A0`-module because the quotient is free. Hence the
Stein algebra is locally free of rank three.

Over `A2-Z`, where the four coefficients have no common zero, the incidence
is a finite cubic divisor in the relative `P1`; Miranda's construction for
the displayed trace-zero basis identifies its direct-image algebra with the
given block algebra `B_K`. Since both algebras are locally free, the
isomorphism and inverse extend across the finite set `Z` as maps between
reflexive modules on the regular surface. The multiplication identities
extend because they hold on the dense open. Thus the bridge gives an algebra
isomorphism, not merely a module isomorphism.

No invalid base-change is used. At an affine basepoint `q`, the fibre of
`B_K tensor k(q)` is read directly from the specialized Miranda multiplication
table and is the local square-zero length-three algebra. Therefore the
corresponding point of `Y` is non-etale over `A2`. This conclusion is not
deduced from `H^0(E,O_E)`.

The Stein morphism contracts `E_q={q} times P1` to that one non-etale point
and is an isomorphism over the complement of the finite contracted set. Since
`g1(A2) subset Y_sm minus R`, the first-leg image misses the contracted
point and lifts through the isomorphism locus. Normality of `B_K` is used
only on the block side and in the promoted sandwich; no normality of the
incidence or of `(pi_0)_*O_Xaff` is being silently assumed.

Required exposition repair: state the Miranda identification on `A2-Z`
explicitly before invoking Hartogs/reflexive extension, and keep the
square-zero special fibre on the `B_K` side. With that repair, Corollary 4.1
is proved in the stated normal finite-flat proper cubic-block scope.

## 6. Degree drops and final composition

Verdict: `CONFIRM_WITH_CORRECTIONS`.

The four degree-drop routes are correctly typed.

1. If all target degree-two coefficient parts vanish, the basis is affine
   linear and the charged `AL3-CLOSED` theorem applies. Artificial degree-two
   homogenization must not be treated as a smooth quadratic incidence.
2. Literal homogeneous fibre-degree drop gives a `K`-rational fibre linear
   factor, contradicting the generic cubic field. Vanishing of one chart
   coefficient is only relevant when it gives such a homogeneous factor.
3. If `[C(x,y):K]=1`, the upper intermediate field is not proper; this is not
   a polynomial-support theorem.
4. If `[K:C(f,g)]` drops to two, the quotient is Galois in characteristic zero
   and is excluded by the charged Galois block obstruction; degree one is not
   a proper lower intermediate field.

After the repairs above, the smooth exact quadratic case composes with the
promoted lattice theorem as follows. Smoothness gives reduced squarefree
infinity. Divisorial affine common factors are impossible. Any remaining
projective or affine coefficient basepoint produces the boundary cycle above,
contradicting the promoted rational-forest first-leg package. Hence no
basepoints remain. Then every fibre over `P2` is a nonzero cubic divisor in
`P1`; proper plus quasi-finite makes `pi` finite. The hypotheses of the
charged lattice integration are met, and that integration excludes the finite
reduced-squarefree quadratic stratum.

Important scope correction: this composition consumes the same promoted
first-leg boundary package that is an explicit hypothesis inside the lattice
integration `c9871c92...`: resolved full boundary is a rational forest, the
boundary classification applies, and the unit/localization input applies.
The four block algebra integrations alone do not restate that package.
Promotion should either cite it through `c9871c92...` exactly or include it
explicitly in the theorem's dependency list.

## 7. Maximum safe theorem

Verdict on `SMOOTH-Q2-CLOSED`: it follows with corrected quantifiers and
dependency wording.

Safe promotion:

```text
Assume the promoted proper cubic block sandwich for a hypothetical
noninvertible plane Keller map, including the promoted first-leg boundary
package consumed by the quadratic lattice integration. Let B_K be the normal
finite-flat cubic block algebra over C[u,v], and choose a global trace-zero
Miranda basis with coefficients a,b,c,d.

If max deg(a,b,c,d) <= 1, the affine-linear theorem gives a contradiction.
If max deg(a,b,c,d) = 2 and the degree-two projective incidence
X={Phi^h=0} in P2 times P1 attached to this same basis is smooth, then a
contradiction follows.
```

Equivalently, in the exact quadratic branch: no proper cubic intermediate
block in the promoted Keller first-leg setting admits a chosen global
trace-zero basis whose Miranda coefficients have maximum total degree two
and whose associated exact degree-two incidence hypersurface is smooth.

Quantifier corrections:

```text
The basis quantifier is existential/fixed-presentation: "there exists this
basis" is contradicted. No assertion is made for all bases.

"Exact degree two" must mean max coefficient degree is exactly two before
projective homogenization. Degree <= 1 is a separate AL3-CLOSED route, not a
smooth exact-quadratic incidence.

Smoothness is the smoothness of the projective incidence attached to the same
basis. It is not invariant under basis change and is not a claim about a
singular quadratic presentation becoming smooth after changing basis.
```

No real mathematical gap remains after the corrections above. The cheapest
successor is therefore not another check of this smooth packet, but the
separate singular-incidence client.

## 8. Firewall

Do not promote beyond the following boundary. This packet does not prove:

```text
singular incidence closure;
nonnormal incidence closure;
existence of a quadratic Miranda basis;
minimality of coefficient degree over all bases;
higher coefficient degree;
block degree other than cubic;
primitive extension or primitive monodromy;
existence or nonexistence of a polynomial Keller map;
construction of a counterexample;
JC2.
```

Singular and nonnormal incidences must remain separate. Basis existence and
basis minimization must remain separate. The affine-linear theorem is already
promoted, but it is not a license to smooth an artificial degree-two
homogenization.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14623`.
- Body SHA-256:
  `7d1a36e66a3d71833ace8eb28f7a4e92030b03fad91d226986e6394e0ba50d24`.
- Frozen basis: `145f96d65021ef364a5189c4ca385fe09d7b4f46`.
