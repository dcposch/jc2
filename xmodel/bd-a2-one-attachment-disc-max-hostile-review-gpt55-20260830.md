# Hostile review: one attachment and maximal discriminant degree

Verdict: `CONFIRM_WITH_CORRECTIONS`.

I reviewed the sealed producer
`xmodel/bd-a2-one-attachment-disc-max-producer-sol56-20260830.md` in full at
repository HEAD `145f96d65021ef364a5189c4ca385fe09d7b4f46`.  The full-file
SHA and body SHA match the prompt.  I also read every charged promoted input
named by the producer:

* `xmodel/bd-a2-rational-forest-coordinator-integration-sol56-20260830.md`;
* `xmodel/bd-a2-ramification-lattice-closure-coordinator-integration-sol56-20260830.md`;
* `xmodel/bd-fix3-quadratic-discriminant-conductor-coordinator-integration-sol56-20260830.md`.

There is no mathematical gap in the new argument under the written hypotheses.
The needed corrections are scope and presentation repairs: the internal frozen
basis metadata in the producer is not the commit named in the prompt; the
resolved graph argument should be stated as a connected-subtree lemma in a
forest; and `d_min=d` must remain explicitly fixed-algebra, trace-zero-basis
minimality, not arbitrary presentation minimality.

## 1. Relative canonical and connected ramification

Status: `CONFIRMED`.

The intersection computations are correct.  On `X~dA+3B` in `P2 x P1`,
adjunction gives

```text
A^2=3,   A.B=d,   B^2=0,   K_X=(d-3)A+B,
```

and therefore

```text
R_pi=K_X-pi^*K_P2=dA+B.
```

Since the morphism is generically finite in characteristic zero, the Jacobian
determinant is a nonzero section of `O_X(dA+B)`.  The restriction of
`O(d,1)` is ample, so the zero divisor is nonempty effective ample Cartier.

The Hodge-index connectedness proof is valid even if the Cartier divisor is
reducible or nonreduced.  If the reduced support were disconnected, one can
partition the actual Cartier multiplicities as `R_pi=D_1+D_2` with disjoint
nonzero supports.  Then `D_1.D_2=0` and ampleness gives
`D_i^2=R_pi.D_i>0`, which is impossible by Hodge index.

The proof that reduced infinity shares no component with ramification is also
valid, after a minor wording repair.  In a local chart with `H:h(v,z)=0`, a
reduced irreducible factor `c` of the squarefree `h` contained in `Supp(R_pi)`
would divide `h_z`; from `h=cq` and `(c,q)=1` it follows that `c|c_z`.
Because `deg_z(c_z)<deg_z(c)` unless `c_z=0`, characteristic zero forces
`c in C[v]`; over `C` this is a vertical fibre component, contradicting
finiteness near `H`.  This is chartwise, including the chart at `z=infinity`.

Equation (1.3) is an exact set-theoretic source-support bridge:

```text
H cap Supp(R_pi)
= Sing(H) union {smooth projection-critical points of H -> L_infinity}.
```

It is not a divisor equality and does not compare the source different with a
target discriminant.  The producer keeps this distinction.

Repair: replace "pulled back from a point" by the explicit intermediate
statement `c_z=0`, hence `c in C[v]`, hence vertical over `L_infinity`.

## 2. Connected infinity and one physical attachment

Status: `CONFIRM_WITH_CORRECTIONS`.

The connectedness of reduced `(d,3)` infinity is correct.  On
`P1 x P1`, the exact sequence for `H in |O(d,3)|` and Kunneth give
`H^1(O(-d,-3))=0` for all `d>=1`, hence `H^0(O_H)=C`; reducedness converts
scheme-connectedness into connected support.

The one-physical-attachment conclusion is correct, but the clean graph proof
should be stated slightly differently.  After resolving the reduced union
`H union Supp(R_pi)`, the reduced total transforms of `H` and of `Supp(R_pi)`
are connected subgraphs of the assumed forest, hence subtrees.  In a forest,
the intersection of two connected subtrees is connected.  Two distinct
physical source intersection points would produce two disjoint nonempty
exceptional/strict-transform clusters in that intersection, one over each
physical point, contradicting the lemma.  This handles singularities,
tangencies, multiple branches, and shared exceptional chains without confusing
physical points with normalization points.

The positive intersection number `H.R_pi=4d` gives at least one physical
source point because the two effective divisors have no common component.
Thus `Supp(H) cap Supp(R_pi)={p}` as physical source points only.  It still
allows multiple analytic branches and multiple normalization points above
`p`.

Repair: replace the "two parallel edges after contraction" prose by the
connected-subtree-intersection lemma, or add it before the contraction
argument.

## 3. Componentwise Riemann-Hurwitz

Status: `CONFIRMED`.

For each irreducible component `H_i`, finiteness near `H` gives a finite
normalization map `q_i:tilde H_i -> L_infinity` of degree `b_i>=1`.  By the
source-support bridge and the one-physical-point result, every ramification
point of `q_i` lies over the single target value `t_0=pi(p)`.  A single fibre
of a degree-`b_i` map contributes at most `b_i-1` to ramification, so
Riemann-Hurwitz gives

```text
2g(tilde H_i)-2 = -2b_i + Ram(q_i) <= -2b_i+(b_i-1),
```

hence `2g(tilde H_i)+b_i<=1`.  Therefore `g=0` and `b_i=1`.

The degree-one finite map `H_i -> P1` is an isomorphism: it is finite
birational onto the normal target, so the integral extension of local rings
inside the same function field is equality.  Thus each component is a smooth
section.  The total degree over `L_infinity` is three, so there are exactly
three components.

For sections of bidegree `(a_i,1)`, the intersection formula
`H_i.H_j=a_i+a_j` is correct.  All component intersections are singular
points of the reduced union and therefore lie at the one physical point `p`.
No disjoint pair can occur: a disjoint pair would force two distinct constant
sections, and connectedness would require the third section to meet both at
the same physical point, impossible.

The ultrametric step is sound.  In completed local coordinates at `p`, the
three sections are distinct graphs `z=phi_i(t)`, and
`ord_t(phi_i-phi_j)` satisfies the usual nonarchimedean triangle rule.  The
minimum among the three contact orders is attained at least twice.  Since the
orders are `a_1+a_2`, `a_1+a_3`, and `a_2+a_3`, ordering forces
`a_2=a_3`.  Thus the only possible pattern is `(b,a,a)` with `d=2a+b` and
`0<=b<=a`.

No normalization-point uniqueness is used here.

## 4. Boundary cubic discriminant

Status: `CONFIRMED`.

The boundary map `q:H -> L_infinity` is finite flat of rank three.  Properness
plus absence of vertical components gives finiteness; since `H` is a Cartier
curve on a smooth ruled surface, it is Cohen-Macaulay, and its local modules
over the DVRs of `L_infinity` are torsion-free, hence flat.  Rank three is the
literal degree in the `P1` factor.

The discriminant divisor computation is exact.  The binary cubic defining
`H` has coefficients in `H^0(P1,O(d))`; its classical discriminant is a
nonzero section of `O(4d)`.  Its zero set is the target non-etale locus of the
finite flat boundary algebra.  By the source-support bridge and one physical
attachment, this target support is only `t_0`, and it is nonempty because the
three sections meet over `t_0`.  Therefore

```text
div Disc(H/L_infinity)=4d[t_0],
Disc(H/L_infinity)=c ell^(4d),  c in C^*.
```

The pairwise-contact check agrees: after normalization the three branches are
graphs over the base, and the root discriminant is the square of the product
of pairwise differences.  The contact sum is
`sum_{i<j}(a_i+a_j)=2d`, so the discriminant order is `4d`.

The producer correctly keeps apart source ramification, source different,
target discriminant, physical source point, analytic branches, and
normalization points.

Repair: add the finite-flat justification above if this statement is promoted
as a standalone theorem.

## 5. Full affine discriminant and `d_min`

Status: `CONFIRM_WITH_CORRECTIONS`.

The no-top-degree-cancellation argument is correct for a global trace-zero
Miranda presentation of the same finite locally free generically separable
rank-three `C[u,v]`-algebra.  If the coefficients
`alpha,beta,gamma,delta` have total degree at most `d`, then the degree-`4d`
homogeneous part of the affine discriminant is exactly the discriminant of
their degree-`d` homogeneous parts.  The boundary result proves that this
homogeneous part is `c ell^(4d)`, nonzero.  Hence `deg Delta=4d`.

The minimality conclusion is valid only in the fixed-algebra, trace-zero-basis
class.  For another trace-zero basis of the same algebra, the basis of
`ker Tr` changes by a matrix in `GL_2(C[u,v])`, and every unit of
`C[u,v]` is a nonzero constant.  The discriminant is therefore changed only
by a scalar.  If the new coefficient maximum is `e`, the promoted
finite-flat discriminant theorem gives `deg Delta<=4e`; since `deg Delta=4d`,
one gets `e>=d`, while the displayed basis has `e=d`.

This does not compare different finite algebras, non-trace-zero coordinate
systems, target automorphisms that change total degree, singular
presentations, or presentations with projective basepoints/fibre-degree drop.
It also does not use a forbidden reverse of the `DISC8-INDEX` lower bound.

Repair: every promoted statement of `d_min=d` should read
"minimum among global trace-zero bases of this fixed finite locally free
rank-three `C[u,v]`-algebra."

## 6. Boundary normalization-index length

Status: `CONFIRMED`.

This is a one-dimensional boundary-order calculation only.  Since the three
normalizations are isomorphic to `P1`,

```text
tilde C = q_*O_tildeH = O_P1^3.
```

The quotient `tilde C/C` is supported at `t_0`, because away from `p` the
three sections are disjoint smooth branches.  For a bidegree `(d,3)` divisor
on `P1 x P1`,

```text
p_a(H)=(d-1)(3-1)=2d-2.
```

The normalization exact sequence gives

```text
length(tilde C/C)
= chi(O_tildeH)-chi(O_H)
= 3 - (1-p_a(H))
= 2d.
```

After localizing at `t_0`, both `C` and `tilde C` are free rank-three modules
over the DVR, so the determinant/Fitting index has order `2d`.  The split
normalization has unit discriminant, giving the independent check
`ord Disc(C)=2*2d=4d`.

No surface normalization-index divisor, conductor length, slice statement,
Tor/base-change assertion, or affine normalization statement is being used.

## 7. Scope, usefulness, and promotion

Status: `CONFIRM_WITH_CORRECTIONS`.

The maximum safe theorem is:

Under the hypotheses that `X subset P2 x P1` is a smooth irreducible
hypersurface of class `dA+3B` with literal fibre degree three, `pi:X->P2` is
generically finite and finite near the reduced infinity divisor `H`, and the
resolved boundary containing `H` and reduced source-critical support is a
rational forest, then `H cap Supp(R_pi)` is exactly one physical source point;
`H` is the union of three smooth sections of degrees `(b,a,a)` with
`d=2a+b`; the boundary target discriminant is `c ell^(4d)`; any associated
fixed-algebra global trace-zero Miranda presentation has full affine
discriminant degree `4d` and fixed-algebra trace-zero `d_min=d`; and the
boundary curve order has normalization-index length `2d`.

This theorem is useful as a conditional boundary-shape and discriminant
maximality certificate.  It is not a new existence theorem and not a stronger
closure theorem: `d>=3` is already excluded in the smooth first-leg setting by
the promoted geometric-genus obstruction, `d=2` is handled only inside the
declared quadratic lattice scope, and `d=1` has no `(b,a,a)` solution.

The theorem must not be promoted into any of the following without separate
work: nonreduced infinity, singular or nonnormal incidence surfaces,
projective coefficient basepoints, fibre-degree drop, arbitrary presentations
or different algebras, polynomial Keller maps, counterexamples, primitive
monodromy, one-place curve conclusions, or JC2.

## Repairs and successors

Required repairs before promotion:

1. Fix or explain the provenance mismatch: the reviewed checkout is
   `145f96d65021ef364a5189c4ca385fe09d7b4f46`, while the producer's internal
   frozen-basis field says `5bc4eea1c749045d54b4ee8053be8d85c4f3bc9f`.
2. Replace the attachment graph prose with the connected-subtree-intersection
   lemma for forests.
3. Add the finite-flat justification for `H -> L_infinity`.
4. Qualify `d_min=d` as fixed finite locally free algebra, global trace-zero
   bases only.

Real gaps found: none.

Cheapest decisive successor for the correction-grade risks is a short
standalone lemma packet, no CAS: prove the forest connected-subtree lemma in
the resolved dual graph language, and record the fixed-algebra `GL_2(C[u,v])`
basis-minimality quantifier next to the discriminant integration.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12518`.
- Body SHA-256:
  `0ea337dc8a618d09fc596dce77b00f175e38a367d36be97c6589e863d4373abd`.
- Frozen basis: `145f96d65021ef364a5189c4ca385fe09d7b4f46`.
