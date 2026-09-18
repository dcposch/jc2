# Invariant polynomial graphs in one fixed weighted lift

Producer: swarmHQ (ROOT, gpt-6-astra), with manual same-model checking
by invariant_graph_1031; that check is NOT independent-model review.
Date: September 18, 2026 UTC.
Basis: 9efa89f98e67333842e015da2795e8e5b72c64f3.
Evidence: MANUAL, with the named injectivity-on-one-line theorem imported.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED.

## Exact statement

Work over C. In C[x,y,z] put

    u=1+xy, gamma=1-(7/6)xy+x^2*z, w=u*gamma,
    A=(u+u^2*(3w^2-4w^3))/x^2,
    B=(1+u*(4w^2-5w^3))/x, C=x*gamma.

The quotients define whole polynomials, including x=0, as verified below.
For an arbitrary polynomial h in C[y,z], define

    T_h(y,z)=(B(h(y,z),y,z), A(h(y,z),y,z)).

Assume BOTH

    h(T_h(y,z))=h(y,z)*gamma(h(y,z),y,z),
    J_yz(T_h) is a nonzero constant.

Then T_h is a polynomial automorphism of A2. There is no degree or
support bound on h. The first identity means that the same graph x=h(y,z)
is invariant under the reordered ambient map (C,B,A); no implicit
parametrization or rational-domain restriction is used.

The stronger intermediate conclusion is that graph invariance alone,
for nonzero h, forces y to divide h or z-(9/7)y^2 to divide h.
It does NOT say that every such divisible h defines an invariant graph.

## Dependencies and previous scope

The sole non-elementary import is Gwozdziewicz,
[Injectivity on one line, Theorem 1.1](https://arxiv.org/abs/alg-geom/9305008):
a complex polynomial plane map with nonzero constant Jacobian which is
injective on one affine source line is an automorphism. This is the
campaign-accepted theorem, consumed at exactly that scope, not reproved.

The [weighted-lift coordinate-fiber report](weighted-lift-coordinate-fibers-swarmHQ-root-20260916T133700Z.md)
excludes literal coordinate fibers in its stated class. The
[tangent graph report](tangent-graph-linear-projections-swarmHQ-root-20260916T182800Z.md)
handles z=Z(x,y) and constant linear outputs. The
[earlier fixed-seed graph report](alpoge-polynomial-graph-obstruction-astra-20260906.md)
likewise uses that other graph orientation. Here the changed mechanism
is exact graph invariance and its source-divisor consequence, not merely
an orientation or coefficient census. Both frozen public history and the
coordinator journal were checked before admission; no exhaustive novelty
or literature claim is made. Those earlier exclusions are not proof premises.

## Whole polynomial formulas and the zero graph

All expansions here are formal modulo powers of x in C[y,z][x]. Write

    w-1=-(1/6)xy+x^2*(z-(7/6)y^2)+O(x^3),
    4w^2-5w^3=-1-7(w-1)-11(w-1)^2+O((w-1)^3),
    3w^2-4w^3=-1-6(w-1)-9(w-1)^2+O((w-1)^3).

Substituting gives

    1+u*(4w^2-5w^3)=(1/6)xy+O(x^2),
    u+u^2*(3w^2-4w^3)=x^2*((31/4)y^2-6z)+O(x^3).

Thus the advertised divisions are exact polynomial divisions and

    g0(y,z):=T_0(y,z)=(y/6,(31/4)y^2-6z).

The h=0 case is an invariant graph, with T_0 triangular and J(T_0)=-1.
This supplies a nonvacuous control and checks the omitted x=0 chart.

## Invariance forces a semi-invariant divisor

Suppose h is nonzero. Polynomiality implies T_h congruent to g0
modulo the ideal (h) in C[y,z]. Applying the same polynomial h to both
ordered pairs and using graph invariance gives

    h composed g0 = 0 modulo (h).

This is divisibility with FULL multiplicities, not just preservation of
a reduced zero set. Use the polynomial shear

    S(y,v)=(y,v+(9/7)y^2), H=h composed S.

A direct calculation gives S^-1 composed g0 composed S=(y/6,-6v).
Consequently H divides H(y/6,-6v). The invertible diagonal substitution
preserves total degree, so

    H(y/6,-6v)=lambda*H(y,v), lambda in C*.

If neither y nor v divides H, some monomial v^j and some monomial y^i
have nonzero coefficients. Comparing their eigenvalues gives

    (-6)^j=6^(-i), i,j nonnegative integers.

Absolute values force i=j=0 and lambda=1. In particular the only
possible monomial in H(0,v) is its nonzero constant term. Hence
h(0,z)=c for some c in C*.

## The constant restriction is impossible

Restrict to the SOURCE line y=0. Since h(0,z)=c, the graph there has x=c;
thus u=1 and w=gamma=1+c^2*z, and

    B_h=(1+4w^2-5w^3)/c,
    A_h=(1+3w^2-4w^3)/c^2,
    C_h=cw.

At z=-c^-2, differentiation AFTER this restriction yields

    dB_h/dz=c*(8w-15w^2)=0,
    dA_h/dz=6w-12w^2=0,
    dC_h/dz=c^3 != 0.

This contradicts the chain rule for h(B_h,A_h)=C_h. In particular
every nonzero constant h is excluded. This argument uses invariance,
not the assumed Keller condition.

It follows that y divides H or v divides H; equivalently y divides h
or z-(9/7)y^2 divides h, respectively.

## The retained coordinate curve forces automorphy

If y divides h, then T_h(0,z)=(0,-6z), injective on a source line.
If z-(9/7)y^2 divides h, then

    (T_h composed S)(y,0)=(y/6,y^2/28),

again injective on a source line. Since J(S)=1, T_h composed S retains
the nonzero constant Jacobian. Apply the imported theorem to T_h in
the first case, or T_h composed S in the second. In either case T_h
is an automorphism, proving the statement.

## Limits and checks

This excludes this FIXED seed and this EXACT invariant polynomial
x-graph construction, uniformly for all h. It does not exclude arbitrary
embedded planes, other seeds or orientations, graphs mapped to different
graphs, arbitrary nonlinear outputs, or any arbitrary Keller map.
No ambient Jacobian or generic-degree assertion is needed as a premise.
There is no characteristic-zero JC2 counterexample or proof here.
The plane Keller condition is separately assumed, not inferred from
graph invariance or an ambient Jacobian. No new exit-price assertion.

Manual reconstruction only; no CAS, numerical test, or scientific code.
Checks include exact x-adic divisibility, full divisor multiplicities,
diagonal degree preservation, the zero and nonzero constant cases,
and source rather than target line injectivity. No successor family.

## OPEN(S) RAISED

None. Arbitrary Keller-source gaps remain outside this bounded test.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6159`.
- Body SHA-256:
  `5fd605fcc53fbab9d4450facc3732290b5ea468b8d6ee851c9c949d45d53968a`.
- Frozen basis: `9efa89f98e67333842e015da2795e8e5b72c64f3`.
