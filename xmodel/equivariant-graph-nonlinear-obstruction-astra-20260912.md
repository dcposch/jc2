# Equivariant graphs: unrestricted polynomial-output obstruction

Author: Astra geometry. MANUAL / UNREVIEWED, not promotion.
First action 2026-09-12 01:18:51 UTC; original reserve01:32/HARD01:35,
never reset. Sole input TASK was current-hashed before FRESH_WHOLE:
67e29d9b67fc4038bacb5380ca424530eea9ae477aca045ed4955bc04469b46c.

## Exact grading and necessary Jacobian module

Theorem. For EVERY h in C[w], on the exact graph z=y²h(xy), let p,q,r
be the restrictions of TASK's three displayed polynomials and B=C[p,q,r].
Then the B-module

    M=B J(p,q)+B J(p,r)+B J(q,r)  inside C[x,y]

satisfies M intersect C={0}. In particular there are NO f,g in B with
nonzero constant Jacobian. No degree bound on h,f,g is imposed. This is
a claim about the entire polynomial graph, including y=0, not an open
chart exclusion or a constant-linear-projection test.

Put w=xy. The localization C[x,y,y^-1]=C[w,y,y^-1] is faithful, so it
may be used to derive identities without changing the original ring.
Literal substitution in the given P,Q,R yields

    p=y²a(w), q=y b(w), r=y^-1 c(w),
    a=(1+w)³h+(1+w)(4+3w),
    b=1+3w(1+w)²h+3w(4+3w),
    c=w k,  k=2-3w-w²h.

Give x weight -1 and y weight1. These three generators are homogeneous
of weights2,1,-1. Thus B is a Z-graded subring: projecting any expression
in p,q,r to a weight means retaining its monomials of that weight.
Algebraic relations among the generators do not invalidate this operation,
since the ambient grading is a direct sum.

A monomial p^i q^j r^k has weight2i+j-k. For weight -n, n>=0, it equals
r^n (pr²)^i (qr)^j. Conversely all these monomials occur. Therefore,
as actual subspaces in C[x,y],

    B_0=C[qr,pr²]=C[bc,ac²],
    B_-1=r B_0,             B_-3=r³ B_0.

Neither free generators nor unique polynomial representatives are assumed.
The evaluations used below work for any chosen representative in C[S,T].

For F=y^m A(w), G=y^n B(w), the chain rule, with
J_xy(w,y)=y, gives

    J_xy(F,G)=y^(m+n)(n A'B-m AB').

Consequently J(p,q)=y³(a'b-2ab'),
J(p,r)=-y(a'c+2ac'), and J(q,r)=-(bc)'. Their weights are3,1,0.
If C0 in C* belonged to M, taking weight zero in a module expression
would therefore give polynomials d1,d2,d3 in two variables such that

    C0=d1(bc,ac²)c³(a'b-2ab')
       -d2(bc,ac²)c(a'c+2ac')-d3(bc,ac²)(bc)'.            (1)

Finally, for arbitrary f=F(p,q,r), g=G(p,q,r), Cauchy--Binet expresses
J(f,g) as the sum of the three generator Jacobians with coefficients
F_i G_j-F_j G_i in B. Thus exclusion from M is sufficient to exclude
every such pair. Membership in M is only a necessary condition for
existence of a pair; no converse is claimed.

## Root obstruction for every h

We have c(0)=0, b(0)=1 and c'(0)=k(0)=2. Evaluating (1) at0 gives
d3(0,0)=-C0/2, a nonzero scalar. Let alpha be ANY root of k. Since
k(0)=2, alpha is nonzero, and c(alpha)=0. Both arguments bc,ac² again
vanish. Evaluating the SAME polynomial d3 at this same ordered pair gives

    b(alpha)c'(alpha)=2.                                 (2)

There is no cancellation by c or normalization on c!=0. In particular,
a repeated root of k would give c'(alpha)=alpha*k'(alpha)=0 and violate
(2). Every root of k must therefore be simple.

Direct substitution of w²h=2-3w-k in b gives the exact identity

    w b=4w+6-3(1+w)²k.

At a root alpha of k, c'(alpha)=alpha*k'(alpha), so (2) becomes

    (4alpha+6)k'(alpha)=2.                                (3)

This argument does not divide by b or 4alpha+6. If either vanishes,
(2) or (3) itself is already a contradiction.

For every h, k'(0)=-3. Thus D=deg k>=1: D=1 for h=0 and D=deg h+2
for h nonzero, including nonzero constants. Over C, k has D roots counted
with multiplicity; under (2) they are distinct. Equation (3) says that
each is a zero of L=(4w+6)k'-2. Hence squarefreeness implies k divides L.
The degree of L is exactly D, with leading coefficient4D times that of k,
because characteristic is zero. We obtain the literal polynomial identity

    (4w+6)k'-2=4D k.

Evaluating at0 now forces 6(-3)-2=4D*2, that is -20=8D, impossible for
a positive integer D. This disproves the assumed nonzero C0 and proves
the stronger module theorem. Repeated roots, all constant h, and h=0
were handled explicitly; there is no generic-root exception.

## Controls, scope and closure

For h=0, k=2-3w, b=1+12w+9w² and c=2w-3w². At the two roots0,2/3
of c, the generator J(q,r)=-(bc)' takes respectively -2 and26: at2/3,
b=13 and c'=-2. The forced shared coefficient d3(0,0) cannot convert
both values to the same nonzero constant. This is a concrete control of
the actual coefficient-ring constraint, not merely a root count.

Changing the plane destroys the obstruction: on x=0, with independent
coordinates (y,z), the same three ambient polynomials restrict to
(z+4y²,y,0), whose first two entries have Jacobian -1. This plane is
outside the family z=y²h(xy). Thus no conclusion about all embedded planes,
all graphs, the ambient map's global properties, or JC2 follows.

Polynomial reparametrization by a polynomial automorphism psi of A2 is
harmless. Its Jacobian is a nonzero constant, by the chain rule with its
polynomial inverse. For f,g in B,

    J(psi*f,psi*g)=(psi*J(f,g))*J(psi).

Applying the inverse automorphism proves the same nonexistence for psi*B.
Indeed the entire transformed module is J(psi)*psi*M, so its intersection
with nonzero constants remains empty. This is not an extension to
arbitrary noninvertible parametrizations.

The polynomial coefficient ring B is essential to the argument:
d3(bc,ac²) is defined at the shared pair(0,0). Arbitrary rational or other
non-polynomial target coefficients are not licensed; poles could make
those evaluations meaningless. Enlarging coefficients to arbitrary source
functions also loses the asserted B_0 description. No statement about such
enlargements is claimed.

QUANTITY: M intersect C*, proved empty, rather than a degree-limited
search for f,g. CHEAPEST TEST: the displayed grading and root-multiplicity
audit, manual planned under15 minutes; numerical/computational wall is
UNMEASURED, and no scientific execution occurred. OPEN: none in this
exact deduction, subject to independent review. No new canonical OPEN,
promotion, implementation, resource request or descendant is created.
ROOT separately checks history; there is no novelty assertion here.

Own-only collision/scope check: initial report, manifest, PINS and custody
were absent. Only the leased report and designated PINS/custody are
authored; TASK and all existing files are untouched. Final WHOLE readbacks,
input postpin, marker-last transaction and exact expected verification are
recorded in custody. All tools were administrative text/hash/date or the
existing documentary transaction; no scientific subprocess, external
source, peer, worker, protected tree or shared edit was used.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6885`.
- Body SHA-256:
  `57f7673771342d6c61a2efd8c7e735f9ee07b9b50060d97d1f6089ebc6bcb5f5`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
