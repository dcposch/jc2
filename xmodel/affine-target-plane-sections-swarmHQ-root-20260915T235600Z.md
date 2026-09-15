# Affine target-plane sections of the literal running triple

Producer: swarmHQ ROOT and native co-researcher, both gpt-6-astra.
Date: September15--16,2026 UTC.
Basis: 4cfc0ea43ae01816286f5b408fffea9b8430e727.
Evidence: MANUAL / PRODUCER-CHECKED / UNPROMOTED.
Desk-only. No numerical or symbolic computation, no literature-priority claim.

## Exact statement

Over C, fix u=1+xy and the literal polynomial triple

    P=u^3*z+y^2*u*(1+3u),
    Q=y+3x*u^2*z+3x*y^2*(1+3u),
    R=2x-3x^2*y-x^3*z.

For every (alpha,beta,gamma)!=0 and every delta in C, consider the ENTIRE
affine hypersurface

    X={alpha*P+beta*Q+gamma*R=delta} inside A3_(x,y,z).

The only irreducible component of any such X that is isomorphic to A2
is the component x=0 of R=0. On it,

    (P,Q)=(z+4y^2,y),

which is an isomorphism to the target plane R=0, with inverse
y=Q, z=P-4Q^2. Thus no nontrivial plane map arises by taking an A2
component over an affine target plane of this fixed triple.

This includes arbitrary algebraic A2 components, not merely polynomial
graphs in one fixed source projection. It does NOT concern nonlinear
target surfaces, other triples in the tangent-sweep family, or arbitrary
Keller maps. It does not assert that every embedded source plane maps
into an affine target plane. No JC2 solution follows.

## Dependencies and comparison

The earlier [component-fibre argument](tangent-component-fibres-root-20260913.md)
handles the three individual outputs throughout a larger admissible
tangent-sweep family; its final scope explicitly leaves arbitrary affine
combinations open. Here the triple is fixed, but ALL affine combinations,
all levels, and all irreducible components are covered.
The [graph-wedge review](graph-wedge-gate-fable5-20260912.md) and the
[first-pair graph theorem](tangent-graph-first-pair-swarmHQ-root-20260915T180230Z.md)
have different source/projection scopes. The
[additive-action test](additive-quotient-descent-swarmHQ-root-20260915T232000Z.md)
checks equivariance, not fibers of target linear forms.

The elementary tools are polynomial factorization, the Nullstellensatz
unit criterion for an affine variety, and additivity of compactly
supported Euler characteristic. In particular chi_c(A1)=chi_c(A2)=1
and chi_c(C*)=0. No unreviewed geometric theorem from a prior report is
needed: the formulas and complete fiber decompositions are proved below.

Targeted source discovery also found the unrefereed candidate
[Degree-difference principle and affine slices](https://github.com/ipitchford/degree-difference-affine-slices),
manuscript dated July27,2026. Its introduction classifies normalized
linear--quadratic binary-form slices producing three-dimensional sources,
and uses an Euler divisibility obstruction for higher-degree sources.
Those are different slices from the additional target planes studied
here. Only the selected introduction and early sections were read; its
general claims and bundled programs are not imported or independently
verified here. No external code was run, and no priority is claimed.

## 1. Smoothness and the coefficient divisor

Write

    alpha*P+beta*Q+gamma*R-delta=C(x,y)*z+B(x,y)-delta,
    C=alpha*u^3+3beta*x*u^2-gamma*x^3,
    B=alpha*y^2*u*(1+3u)
      +beta*(y+3x*y^2*(1+3u))+gamma*x*(5-3u).

Every X is smooth, so it is reduced and distinct irreducible components
are disjoint. Here is the needed direct differential check. On x!=0 set
v=u/x, t=1/x and use (v,t,R) as coordinates. Substitution gives

    P=v^2+v*t-v^3*R,
    Q=4v+2t-3v^2*R.

The determinant of (P,Q,R) with respect to (v,t,R) is 2t; that of
(v,t,R) with respect to (x,y,z) is -x. Consequently the polynomial
determinant is -2 on x!=0 and hence everywhere. A nonzero constant
linear combination of its independent differential rows is nonzero.
This proves the smoothness assertion used here, without importing any
ambient-map classification or generic-degree theorem.

If C and B-delta have no common irreducible factor, the equation is
primitive and linear in z over C[x,y], hence irreducible by Gauss's lemma.
Projection pi:X->A2_(x,y) is an isomorphism over C!=0. Over C=0 its
fiber is A1 exactly at the zeros of B-delta, and is empty otherwise.
This describes the entire hypersurface, not just its generic chart.

If an irreducible factor l of C also divides B-delta, then
V(l) times A1_z is a vertical irreducible component. Removing the full
greatest common divisor leaves exactly one primitive linear-in-z
component dominating A2. Smoothness makes this component disjoint from
every vertical component. Thus l has no zero on the dominating component
and is a unit there. It is nonconstant there, because the projection is
an isomorphism over the nonempty dense open C!=0. No multiplicity in C
invalidates this argument: the full equation is reduced by smoothness.

## 2. The case alpha!=0

Let r range over the DISTINCT roots of

    alpha*r^3+3beta*r^2-gamma=0.

With root multiplicities retained in the product,

    C=alpha*product_r (u-r*x)^(multiplicity of r).

The reduced divisor C=0 is a disjoint union of curves

    D_r={u-r*x=0}={1+x*(y-r)=0}.

Each is C*, parameterized by x!=0 with y=r-1/x. Two different such
curves cannot meet: subtracting their equations would give x=0 and then
1=0. On D_r, direct expansion yields

    B=a_r+b_r/x,
    a_r=alpha*r^2+4beta*r,
    b_r=alpha*r+2beta.                       (1)

For a check, set k=alpha*r+3beta, so gamma=k*r^2. The three terms of B
combine using

    x*(r-1/x)^2*(1+3r*x)
      =3r^3*x^2-5r^2*x+r+1/x.

Its quadratic and linear terms cancel those from gamma*x*(5-3r*x),
leaving k*r+beta*r+(k-beta)/x, which is (1).

If B-delta vanishes identically on any D_r, there is a vertical
component D_r times A1=C* times A1, not A2 because x is a nonconstant
unit. On the unique dominating component, u-r*x is a nonconstant unit
by Section1. Any other vertical components have the same exclusion.
Thus no component is A2 in this case.

Otherwise C and B-delta are coprime. Formula (1) shows that their common
zero set consists of finitely many distinct points, say N. Each D_r
contributes at most one point; multiplicities of roots of C do not count
as extra topological points. The full decomposition in Section1 gives

    chi_c(X)=chi_c(A2 minus union D_r)+N*chi_c(A1)=1+N.

If N>0 this differs from chi_c(A2). If N=0 then X avoids every D_r,
so any u-r*x is a nonconstant unit on the irreducible X. There is at
least one root r since the polynomial is cubic. This excludes A2 also
when Euler characteristic equals1.

## 3. The case alpha=0, beta!=0

Here C=x*(3beta*u^2-gamma*x^2). The line x=0 is disjoint from every
curve u=r*x. On that line B=beta*y, so there is exactly one center point
y=delta/beta, with its complete A1_z fiber retained in X.

If gamma!=0, let r_+,r_- be the distinct nonzero square roots of
gamma/(3beta). The other two reduced components of C=0 are the disjoint
C* curves D_(r_+) and D_(r_-). Formula (1), with alpha=0, reads

    B|D_r=4beta*r+2beta/x.

Each contributes one center unless delta=4beta*r, when it contributes
none. These two exceptional delta values are different. There are
therefore N=2 or3 total centers, including the center on x=0.
No component of C=0 is a common factor with B-delta, so X is irreducible.
As chi_c(C=0)=1+0+0=1,

    chi_c(X)=1-1+N=N>=2,

and X is not A2.

If gamma=0, the reduced divisor C=0 consists of the line x=0 and the
single curve u=0, although the latter has multiplicity2 in C. On u=0
one has B=2beta/x. For delta!=0 there is one center on each component,
so X is irreducible with chi_c(X)=2. For delta=0 there is just the center
on x=0, and chi_c(X)=1; nevertheless u=0 is completely absent from X,
so u is a nonconstant unit on X. Again X is not A2. This explicitly
handles the repeated-root and Euler-characteristic-one exception.

## 4. The case alpha=beta=0, gamma!=0

Write c=delta/gamma. The equation is

    R=x*(2-3xy-x^2*z)=c.

For c!=0, x is a nonconstant unit, and in fact the fiber is C* times A1,
with x!=0 and y arbitrary, z=(2-3xy-c/x)/x^2.
For c=0 there are precisely two disjoint components:

    x=0,                         isomorphic to A2_(y,z),
    2-3xy-x^2*z=0,               isomorphic to C*_(x) times A1_(y).

The second cannot meet x=0 because its equation would read2=0.
Only the first is A2, and the displayed (P,Q) restriction at the start
is a polynomial isomorphism. This proves the classification.

## Controls, custody and limits

The R=0 plane is an essential positive control: a blanket claim that no
affine section has an A2 component would be false. The Q=0 section is an
essential negative control for using Euler characteristic alone: its
Euler characteristic is1 but it has a nonconstant unit u. Repeated roots
and common factors were handled explicitly, not discarded as nongeneric.
For an explicit common-factor control, P=0 factors as
u*(u^2*z+y^2*(1+3u))=0. The two components cannot intersect: u=0
would force y=0 in the second equation, inconsistent with 1+xy=0.
The first component is C* times A1, and u is a nonconstant unit on the
second. Thus the smoothness/disjointness argument has a literal example.

The native co-researcher's complete terminal response was collected and
authoritative COMPLETED status observed before closing this report.
It independently reconstructed the chart determinant, restriction (1),
UFD argument, every center count and the exceptional plane inverse.
This is same-model co-research, not different-model hostile review.

Root whole-read evidence pins before authoring:

- tangent-component-fibres-root-20260913.md:
  c5524dd9e10e61ea0f12e3f76ef18ef0782aa52c18845c035ae8013e12c61fd6.
- graph-wedge-gate-fable5-20260912.md:
  009c611bd8c3acf41aa9545a6fdfbe27a5b1cf88bcf1ef6e603067d1299a4dfd.
- additive-quotient-descent-swarmHQ-root-20260915T232000Z.md:
  a6919a3e38f1e0c9d78b88262435164e7905284d465e4fb94bc37a690642e96e.
- FALLACY-v2.md:
  e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.

This is one bounded construction filter. No nonlinear target-surface,
arbitrary embedded-plane or higher-parameter search follows from it.
The classification supplies neither a general reduction to this triple
nor a global proof or counterexample for JC2.

## OPENS RAISED

None. The selected affine-family question is closed at the producer's
stated evidence tier; independent different-model review is required
before promotion or dependent use.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Canonical scan completed exit0. All four listed input pins were rechecked
unchanged after drafting and before closure. This lexical scan is not a
novelty certificate or proof verification.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10736`.
- Body SHA-256:
  `9df6c54fc8244c95049895ee951608e8244e73dcc28f23dd07f308f60f410b21`.
- Frozen basis: `4cfc0ea43ae01816286f5b408fffea9b8430e727`.
