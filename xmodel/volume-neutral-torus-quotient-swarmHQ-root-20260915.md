# Volume-neutral torus quotient obstruction

Producer: ROOT/Astra, swarmHQ, September15,2026.
Evidence: MANUAL proof with the explicitly accepted external injective-line
criterion below. Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending FIRST.
Native Astra co-research found no gap; same-model checking is not FIRST.

## Exact statement

VOLUME-NEUTRAL-TORUS-QUOTIENT-1. Work over C. Let n>=3 and let an
algebraic torus T of dimension n-2 act effectively and linearly on C^n.
Assume its determinant character is trivial, and its invariant ring is
abstractly a polynomial ring in two variables. Let F:C^n->C^n be a
polynomial map with nonzero constant Jacobian determinant, equivariant
for this source representation and a linear target representation of
the SAME T. Then F is a polynomial automorphism.

An isomorphism identifying source and target tori may be absorbed in the
target representation. No arbitrary isogeny, nonlinear-action,
singular-quotient or nontrivial-determinant-character extension is asserted.
There is no degree bound. Identity stabilization or polynomial frame
changes are covered only if the resulting map has ALL stated hypotheses.
The claim neither excludes arbitrary plane Keller maps nor resolves JC2.

The only non-elementary closing import is the already accepted theorem:
a complex polynomial plane Keller map injective on one affine line is an
automorphism, Gwozdziewicz, *Injectivity on one line*, Theorem1.1,
https://arxiv.org/abs/alg-geom/9305008 . This import is recorded in AUDIT's
August24 prime-degree source audit and September11 PP-HOM-1 qualification.
It is consumed, not reproved or newly audited here. No degree-125 or other
closed-degree premise is used.

## 1. Normalize the representations

Put b=F(0) and M=DF(0). Equivariance makes b fixed by the target T,
and differentiating at0 makes M an invertible intertwiner of the source
and target representations. Thus

    G=M^(-1)(F-b)

commutes with a single source representation, G(0)=0, DG(0)=I and
det DG=1. Subtracting b is compatible with the action because b is fixed.
It suffices to prove G invertible. Diagonalize the linear torus action.

Let W:Z^n->X^*(T) be its weight map, K=ker W and S=K intersect N^n.
The effective action has weight rank n-2, so K has rank2. The trivial
determinant character says the vector 1=(1,...,1) belongs to S. For any
h in K, h+k*1 is nonnegative for sufficiently large integer k. Hence

    S-S=K.

The invariant ring is the monomial algebra C[S].

## 2. The quotient forces two disjoint product coordinates

Let m be the monomial maximal ideal of C[S], consisting of all
nonconstant monomials. Its quotient is C. The monomials indexed by
indecomposable nonzero elements of S form a C-basis of m/m^2: decomposable
monomials span m^2, and distinct monomials are linearly independent.
Since C[S] is abstractly C[u,v], this maximal ideal is a smooth point of
dimension2. There are exactly two indecomposables, alpha and beta.
Induction on total exponent shows that they generate S. Since S-S=K has
rank2, they are independent and K=Z*alpha+Z*beta.

Write 1=a*alpha+b*beta with a,b nonnegative integers. Both are positive.
For example, if a=0, choose k so that k*1-alpha is nonnegative. It lies
in S but has alpha-coordinate -1 in the independent basis alpha,beta,
contradicting generation by NONNEGATIVE coefficients. Similarly b!=0.
Any nonzero coordinate of alpha now gives 1>=a, and any nonzero coordinate
of beta gives 1>=b. Thus a=b=1 and

    alpha+beta=1.

Both exponent vectors are squarefree and have disjoint nonempty supports
I,J which partition all coordinates. The invariant monomial generators
can therefore be chosen literally as

    u=product_(i in I) x_i,   v=product_(j in J) x_j.

The torus image is exactly the product of the determinant-one diagonal
tori on the two blocks: both block products are invariant, the image is
contained in that connected torus, and both have dimension n-2.
This also follows from the just established kernel lattice.

For i in a nonsingleton block, a monomial of the same weight as x_i has
exponent e_i+a*alpha+b*beta, with a,b integers. At a DIFFERENT index of
its own block, nonnegativity forces that block coefficient >=0; at an
index of the other block it forces the other coefficient >=0. Therefore

    G_i=x_i*P_i(u,v),  P_i in C[u,v].

A singleton block is a zero-weight coordinate, whose component can be
an arbitrary invariant polynomial. Since n>=3, at least one block is
nonsingleton and at most one is singleton. No unmentioned freeness of a
graded piece or assumed coordinate presentation has been used.

## 3. Constant Jacobian descends without a boundary factor

The invariant polynomials u(G),v(G) give a polynomial quotient map
H:C^2_(u,v)->C^2_(u,v). Fix an anchor in each block and take the n-2
fundamental vector fields

    D_i=x_i*d/dx_i-x_anchor*d/dx_anchor

at all other indices of that block. A singleton contributes no field.
For Omega=dx_1 wedge ... wedge dx_n, their successive contraction gives

    i_(D_(n-2)) ... i_(D_1) Omega = +/- du wedge dv.

This equality is polynomial on the WHOLE affine space. On each block the
coefficient of the anchor differential is the product of all other block
variables, and every other coefficient is the corresponding product with
that variable omitted, exactly the differential of the block product.
The two blocks introduce only a wedge-order sign, no additional monomial
or integer factor.

Equivariance makes every D_i G-related to itself. Pullback consequently
commutes with these contractions; G^*Omega=Omega gives

    d(u(G)) wedge d(v(G))=du wedge dv.

Because u,v are algebraically independent, this is det DH=1 in C[u,v].
The relation does not divide by a boundary equation or assert that the
quotient morphism is a principal torus bundle on its boundary.

## 4. A line closes the quotient; coordinate primality closes the lift

Relabel the blocks so I is nonsingleton. Then

    H_1=u*A(u,v),   A=product_(i in I) P_i.

On u=0 the determinant identity becomes

    A(0,v) * (d/dv) H_2(0,v)=1.

Both factors are nonzero constants in C[v]. Thus H restricted to u=0
is (0,a*v+b), a!=0, and is injective on that affine line. The named,
already accepted injective-line theorem makes H an automorphism.

An automorphism coordinate H_1 is an irreducible polynomial. Since
H_1=u*A and u is a nonunit, A is a nonzero constant. Every factor P_i is
therefore constant. If J is also nonsingleton, H_2=v*product_(j in J)P_j
is likewise a coordinate, so all its factors are constant too. Then G
is diagonal, and DG(0)=I makes it the identity.

If J is a singleton with coordinate z, all nonsingleton components have
already become constant diagonal multiples of their input variables.
Write the remaining invariant component as B(u,z). The full Jacobian
identity forces partial_z B to be a nonzero constant, hence

    G_z=a*z+C(u),  a!=0.

This is triangular and has a polynomial inverse. In the normalized G,
the diagonal constants and a are1, and C(0)=0. Undoing the affine target
normalization proves the exact statement for F.

## 5. Controls and limits

- Positive control: weights(1,-1,0), u=xy,v=z, and
  G=(x,y,z+P(xy)) for any P in C[t]. Its quotient is
  (u,v+P(u)), and both determinants are1. Constant terms are allowed
  before normalization.
- Dropping the Keller hypothesis: for the SAME action,
  G=(x,y*(1+xy),z) has determinant1+2xy. Its quotient is
  (u+u^2,v), determinant1+2u. Volume preservation of the ACTION and
  smoothness of the quotient alone do not make the map invertible.
- The known three-dimensional running example has source weights
  (1,-1,-2), whose sum is -2. It is outside the determinant-character
  hypothesis. No ambient-map or monodromy reaudit is claimed.
- If n=2, T is trivial and both blocks can be singletons. The line
  argument has no product coordinate to use; the conclusion would be
  JC2 itself. This edge is EXCLUDED, not solved.
- No conclusion for singular quotient surfaces, nonlinear torus actions,
  smaller-rank actions, non-volume-neutral actions or arbitrary source
  planes/projections. No assertion that a hypothetical plane Keller map
  can be put in the stated higher-dimensional equivariant class.

## 6. Priority, source scope, allocation and replay

This is a candidate exclusion of one complete construction mechanism,
not a new plane degree bound, global proof or evidence against JC2.
The September13 14:42 cyclic-cone rational-reparameterization stop and
the accepted low-fiber full-factorization towers were checked before
commissioning. Neither supplies this literal arbitrary-n torus statement.
Several broad searches clipped and were narrowed; no exhaustive novelty
or whole-map-refresh claim. The new test stops the volume-neutral smooth
plane-quotient shortcut; it licenses no singular-quotient or weight-family
successor and changes no global ranking.

ROOT's selected primary read of Shaska2607.20210v2,
https://arxiv.org/html/2607.20210v2 , covered the opening and Section2
representation facts, Sections9.1--9.2's quotient determinant formula,
and Section10.3's parabolic/m=1 statements, with nearby context. These
are priority/context only, not additional proof dependencies or a whole
paper audit. The argument above derives its own semigroup, contraction
and transfer identities. No novelty or contradiction with that paper is
claimed. Its m=1 quotient equality does not automatically identify its
restricted quotient pairs with arbitrary plane Keller pairs.

ROOT independently derived the proof and native Astra checked it in a
bounded message-only task, terminal before publication. Same model,
not different-model review. No scientific code, AWS job, parameter
enumeration, degree search or computational certificate. Replay is the
displayed symbolic proof, including the two explicit determinant controls.
No optimized-interpreter or formal-verification claim. No raised OPEN;
out-of-scope hypotheses are not disguised as solved problems.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10106`.
- Body SHA-256:
  `e52f7d16b002b958854a0d5a2ca8a5b432c4eb4292cc7ef13ad501de97f85aea`.
- Frozen basis: `fca8a3c553955a488764ce49fe00b10c8748f5bb`.
