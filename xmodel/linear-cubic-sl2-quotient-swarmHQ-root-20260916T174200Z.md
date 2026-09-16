# The natural SL2 quotient of linear/cubic resultant-one multiplication

Producer: swarmHQ ROOT (gpt-6-astra), September16,2026.
Basis: d71be3003c4555a0775c21675edeb12ce0435d44.
Evidence: MANUAL, elementary characteristic-zero invariant/ring algebra.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending different-model FIRST.
Claim: LINEAR-CUBIC-SL2-QUOTIENT-1. JC2 remains unresolved.
No scientific computation or novelty claim.

## Statement and construction decision

Work over C, with independent binary variables X,Y. Let V be the affine
space of binary quartics, and let

    Z = { (L,Q): deg L=1, deg Q=3, Res(L,Q)=1 }.

Here forms are homogeneous, L=aX+bY, and our exact resultant convention is

    Res(L,Q)=Q(-b,a).

SL2 acts by the same determinant-one linear substitution on both forms.
The multiplication map m:Z->V, (L,Q)->LQ, is equivariant.

Both affine invariant-theoretic quotients are A2, and the induced map is
the polynomial automorphism

    (u,v) |-> (I,J)=(-3u,-27v).

This covers the WHOLE resultant-one source, not only an open coefficient
chart or the squarefree quartic locus. In particular this natural quotient
does not provide a plane Keller counterexample. The source Z itself is
SL2 times A2, not asserted to be affine five-space. We assert neither a
general reduction of JC2 to this construction nor an exclusion of other
quotients, target surfaces, factor degrees, or arbitrary parametrizations.

## 1. A canonical global frame on the source

For (L,Q) in Z put e=(-b,a), and define the linear form

    M(X,Y) = (Q_X(e) X + Q_Y(e) Y)/3.

Every coefficient is polynomial in the original source coefficients.
Euler's degree-three identity gives

    det(L,M) = (a Q_Y(e)-b Q_X(e))/3 = Q(e)=1.

Thus L,M are a determinant-one frame at EVERY source point. There is no
localization at a, b, a discriminant, or an unproved nonzero coefficient.
Changing variables from X,Y to L,M and back is polynomial in this frame's
coefficients, because its inverse matrix has determinant denominator1.

Expand Q in that frame as

    Q=c0 M^3+c1 L M^2+u L^2 M+v L^3.

Since L(e)=0 and M(e)=1, evaluating at e gives c0=1. By definition,
the coefficient vector of M is grad Q(e)/3; hence

    grad(Q-M^3)(e)=0.

In the displayed expansion this gradient is c1 grad L. The vector grad L
is nonzero (indeed det(L,M)=1), so c1=0. Consequently

    Q=M^3+u L^2 M+v L^3.                            (1)

The coefficients u,v are polynomial functions on Z: substitute the
polynomial inverse frame into Q and extract the two coefficients.

Conversely, from any frame (L,M) with determinant1 and any u,v in C,
formula(1) gives a cubic Q with Q(-b,a)=1. Its canonical gradient form
is precisely M. These constructions are mutually inverse polynomial
maps and prove

    Z is isomorphic to SL2 times A2_(u,v).           (2)

The canonical M can equivalently be characterized as the unique
determinant-one complement of L for which the LM^2 coefficient vanishes.
Indeed every other complement is M+sL, and substituting it shifts that
coefficient by -3s. This also proves equivariance of(2): simultaneous
SL2 substitution preserves the frame determinant and characterization,
and fixes u,v. The group acts transitively on the frame factor.
Evaluation at the identity frame therefore gives the exact invariant ring

    C[Z]^SL2=C[u,v].                                (3)

This is a global ring identity, not merely a rational quotient.

## 2. The target invariant ring, with an elementary check

Write a quartic as

    H=A X^4+B X^3 Y+C X^2 Y^2+D X Y^3+E Y^4.

Use the classical, unnormalized-coefficient formulas

    I=12AE-3BD+C^2,
    J=72ACE+9BCD-27AD^2-27B^2E-2C^3.                (4)

Their SL2 invariance can be checked without importing a classification
theorem. For substitution X->X+tY, Y->Y, the infinitesimal derivation
on the coefficient algebra is

    Delta=4A partial_B+3B partial_C+2C partial_D+D partial_E.

Direct differentiation gives Delta(I)=0 and Delta(J)=0. Since this
substitution is the exponential of the locally nilpotent Delta, both
polynomials are invariant under the whole one-parameter subgroup.
They are also invariant under (X,Y)->(Y,-X), which sends the coefficient
list to (E,-D,C,-B,A). These substitutions generate SL2, proving the
claimed invariance. Only the standard elementary-matrix generation of
SL2 over a field is used here.

For the normal frame L=X,M=Y, multiplication yields

    H=X(Y^3+u X^2 Y+v X^3)
     =v X^4+u X^3 Y+X Y^3.

Thus, globally on Z by equivariance,

    m^*I=-3u,                 m^*J=-27v.            (5)

For completeness these formulas also prove that(4) generate the entire
target invariant ring. The map m is dominant: any squarefree binary
quartic factors as L0 Q0 with R=Res(L0,Q0)!=0. Replacing L0,Q0 by
lambda L0, lambda^(-1) Q0 preserves their product and scales R by
lambda^2. Choose lambda with lambda^2 R=1. Hence the image of m contains
the squarefree open set of V. This argument is used only for dominance;
it does not restrict the source in(1)--(5).

If f is any polynomial SL2 invariant on V, then by(3) its pullback is
a polynomial h(u,v). The invariant polynomial

    h(-I/3,-J/27)

has the same pullback by(5). Dominance of m makes pullback injective,
so f=h(-I/3,-J/27). Formula(5) and algebraic independence of u,v also
prove algebraic independence of I,J. Therefore

    C[V]^SL2=C[I,J].                                (6)

Equations(3),(5),(6) identify the induced affine quotient map exactly.
Its inverse is (I,J)->(-I/3,-J/27), and its Jacobian determinant is81.
No generic-fiber degree is substituted for the degree of this quotient.

## Controls, scope and provenance

- u=v=0 gives Q=Y^3 and H=XY^3. The source and formulas are valid
  despite repeated roots: the proof does not invert the discriminant.
- L=Y is covered by the same gradient construction; no a!=0 chart
  assumption is hidden in the normalization.
- Dropping the resultant-one premise breaks the determinant-one frame:
  L=X,Q=X^3 has Q(-b,a)=0 and the proposed gradient M is zero.
  We make no assertion for variable or zero resultant.
- The original factor-forgetting morphism has a different source and
  dimension. Its behavior cannot be assigned to its two-dimensional
  invariant quotient. The explicit quotient calculation is decisive here.

The construction was screened after the accepted small-degree ambient
tower and weighted-coordinate-fiber results: neither supplies this
linear/cubic SL2 calculation. The equal-degree scaling quotient concerns
a different group and different factor degrees. No preceding campaign
theorem is needed in the proof above. Scoped searches found older quartic
covariants and an SL2/ODE card, but those have different objects; absence
of an exact hit is not priority evidence. These classical invariant
formulas and frame normalization carry no claim of literature novelty.

Exploratory primary context was the author's
[factorization/pseudo-plane index](https://github.com/nasqret/jacobian-counterexample/blob/main/knowledge/index.md),
read September16,2026, which itself distinguishes the higher-dimensional
construction from the plane problem. Its quadratic scaffold is the
already-recorded pseudo-plane, not a new source used here. No external
software or unverified theorem from that repository enters this proof.

No computational engine, random seed, prime or software replay applies:
all identities are displayed manual algebra. Shared protocol and
FALLACY were read at unchanged SHA256 values
9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e and
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.

Decision: do not commission a search for noninjective plane maps from
THIS natural quotient. Other actions, added cuts, arbitrary target
coordinates or higher-degree families get no automatic successor.
Independent different-model FIRST is required before promotion or use.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8042`.
- Body SHA-256:
  `0b52d7090017c230ee643b47147c410ba5a5ed9ed53a20e1973952da99e2e0d5`.
- Frozen basis: `d71be3003c4555a0775c21675edeb12ce0435d44`.
