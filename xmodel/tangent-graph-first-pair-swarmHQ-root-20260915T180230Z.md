# First-pair obstruction on arbitrary polynomial tangent graphs

Producer: swarmHQ ROOT (gpt-6-astra).
Date: 2026-09-15 18:03 UTC.
Basis: 20b38d93cb54bb2e9eeca18a2a39cb58b92a0772.
Evidence: MANUAL, self-contained polynomial argument.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED pending different-model review.
Claim ID: TANGENT-GRAPH-FIRST-PAIR-1. No external novelty claim.

## Statement and scope

Work over C with independent x,y. Let gamma be ANY nonzero polynomial
in C[x,y], p in C[w] have degree d>=2, and suppose

    u=1+xy, w=gamma*u, C=x*gamma,
    D=(p(w)+2*gamma)/(x*gamma)

is polynomial on the WHOLE source A2. Write n=deg_y(gamma) and let
h(x)!=0 be its y^n coefficient. Then the polynomial plane Jacobian has

    deg_y J(C,D)=d*(n+1)-1>=1,
    lc_y J(C,D)=d*p_d*(x*h)^(d-1)*(h+x*h'),

where p_d is the leading coefficient of p and h' is d/dx. In particular
C,D are not a Keller pair. Nor can ANY two polynomials in the subalgebra
C[C,D] form a Keller pair.

For the literal whole-polynomial tangent triple

    gamma=gamma0+a*xy+b*x^2*z, w=gamma*(1+xy), C=x*gamma,
    F=(C,D,E),
    D=(p(w)+2*gamma)/C, E=(q(w)+gamma*w)/C^2,
    b!=0, gamma0!=0, q'=w*p'/2,

this excludes every source graph z=Z(x,y), Z an arbitrary polynomial,
followed by any polynomial target pair depending only on C,D. There is
no bound on Z, p, or the two target polynomials. The entire triple's
polynomiality guarantees D is polynomial on each graph. Its necessary
admissibility identities force deg(p)>=2, as recalled below.

This is a first-two-output projection obstruction. It does NOT exclude
pairs involving E, arbitrary rational target changes, another orientation
of the source plane, or arbitrary embedded/nonpolynomial source planes.
No reduction of arbitrary JC2 maps to this presentation is known here.

## Proof

Compute in C(x,y) before using polynomiality. From C*D=p(w)+2*gamma,

    dC wedge dD = (p'(w)*dC wedge dw+2*dC wedge dgamma)/C.

The exact identities dC=gamma*dx+x*dgamma,
dw=u*dgamma+gamma*(y*dx+x*dy), and u-xy=1 give

    dC wedge dw
      =gamma*(gamma_y+x*gamma+x^2*gamma_x)*dx wedge dy,
    dC wedge dgamma=gamma*gamma_y*dx wedge dy.

Consequently

    J(C,D)=p'(w)*(gamma+x*gamma_x+gamma_y/x)+2*gamma_y/x.  (1)

Terms involving 1/x are interpreted in C(x)[y]; the complete expression
is polynomial by the stated hypothesis, so no localization of the
conclusion is being asserted.

Now deg_y(w)=n+1 with leading coefficient x*h. The y^n coefficient of
gamma+x*gamma_x is h+x*h'. It is nonzero: if h=sum h_i*x^i then
h+x*h'=sum (i+1)*h_i*x^i, and all i+1 are nonzero in characteristic zero.
The term gamma_y/x has degree at most n-1 in y; it vanishes for n=0.
Thus the parenthesis in (1) has degree exactly n and leading coefficient
h+x*h'. The first term in (1) has degree
(d-1)*(n+1)+n=d*(n+1)-1 and the claimed nonzero leading coefficient.
The second has degree at most n-1 and cannot cancel it. This proves the
two identities, including n=0.

For H,K in C[s,t], the chain rule gives

    J(H(C,D),K(C,D))=J_st(H,K)(C,D)*J(C,D).

Both factors are polynomials. A product equal to a nonzero constant in
C[x,y] forces both factors to be units. The second is nonconstant, a
contradiction. No converse to the chain-rule condition is used.

For completeness, the literal whole triple has p(0)=q(0)=0, obtained
along gamma=0 on x!=0. Set p=w*A, q=w^2*B using q'=w*p'/2.
Polynomiality on x=0, where gamma=gamma0 and u=1, gives
A(gamma0)=-2 and B(gamma0)=-1. If A were constant, it would be -2,
and the derivative identity plus q(0)=0 would give B=-1/2, a
contradiction. Therefore d>=2. These are the same necessary identities
in the earlier component-fiber report, not a new ambient Jacobian audit.

## Prior interfaces and controls

The [component-fiber report](tangent-component-fibres-root-20260913.md)
rules out the three literal outputs as source coordinates, but explicitly
leaves arbitrary embedded planes out of scope. Its source identities
were read through EOF. The
[embedded-plane transfer review](embedded-plane-transfer-gate-sol-20260913.md)
requires FULL ambient-output
factorization, not just projection to two outputs, and was read wholly.

The
[one-sided graph/all-output theorem](equivariant-graph-nonlinear-obstruction-root-20260912.md)
covers a fixed
degree-three ambient core, with graph monomials constrained by j-i>=2,
and arbitrary target outputs. Its stated September6 predecessor covers
all graphs but linear projections of that same fixed core. Those are
different scopes: the present argument permits every graph and all p,
but only polynomial outputs inside the first-pair subalgebra. The precise
new test is the y-leading identity (1), not another fixed-core replay.
The Laurent donor theorem concerns a rational TWO-variable donor field;
here restricting z to Z leaves gamma genuinely dependent on x,y, and
fixes no third target coordinate. Targeted history searches found no exact
prior formula, not an exhaustive novelty census.

Desk-only controls in the larger algebraic statement (not claims that
these are whole admissible triples):

- n=0: gamma=1, p=-2w^2 gives C=x, D=-4y-2xy^2,
  J=-4-4xy, with degree1 and leading coefficient -4x.
- n=1: gamma=1+xy, p=-2w^2 gives C=x+x^2*y,
  D=-6y-6xy^2-2x^2*y^3 and
  J=-6-24xy-24x^2*y^2-8x^3*y^3. Degree3 and leading -8x^3 agree.
- Removing d>=2: gamma=1, p=-2w gives (C,D)=(x,-2y),
  a Keller pair. Thus the degree hypothesis cannot simply be dropped.

All displayed identities and controls were checked manually. No CAS,
scientific program, parameter census or low-degree foundation review.

## Limitations and next test

The immediate construction decision is to discard this first-pair graph
projection without searching degrees of Z. No automatic graph, other-pair,
nonlinear three-output, or rational-target successor is selected. One
different-model hostile review checks (1), its leading term, the n=0
case, and the whole-triple attachment before promotion. JC2 is unresolved.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6126`.
- Body SHA-256:
  `b527025feabdd078999f99dd46c9b851b886f7c07c353dea7c42a8bfce9539bf`.
- Frozen basis: `20b38d93cb54bb2e9eeca18a2a39cb58b92a0772`.
