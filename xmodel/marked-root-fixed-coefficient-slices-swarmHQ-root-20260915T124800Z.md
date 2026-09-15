# Fixed-high-coefficient slices of marked-root donors

Producer: swarmHQ ROOT (gpt-6-astra), September 15, 2026.
Basis: `18be9c16c95318c2eea9a2cef76e9ea476985482`.
MANUAL, PRODUCER-CHECKED, UNPROMOTED. Novelty UNKNOWN.
Native Astra independently reconstructed the same elementary algebra;
this is same-model co-research, not different-model FIRST.

## Definition and exact scope

Take the displayed master polynomial from the
[posted marked-root manuscript](https://gitlab.com/-/snippets/6012790/raw/main/exact_fiber_geometry.md),
retrieved September 15, 2026. For an integer n>=4, its source has n
coordinates x,y,z3,...,zn. Put p=1+xy and define

    Phi(T)=(1-y*T)^(n-1)*(p*T-x)
      +(p*T-x)^2*[n*y*(y*T+1/2)+z3*(p*T+x/2)
                    +sum_{j=4}^n z_j*T^(j-2)]
      =sum_{k=3}^n C_k*T^k+A2*T^2+T-A0.

This exact formula is our definition; no floating upstream assertion,
computer verification, generic-degree claim, or external fiber theorem
is required for the argument below. The manuscript's map is
K_n=(C3,...,Cn,A2,A0). We examine ONLY fixing ALL high coefficients:

    S_c=Spec C[x,y,z3,...,zn]/(C3-c3,...,Cn-cn),
    U=Spec C[x,y,1/(1+xy)],      c=(c3,...,cn) in C^(n-2).

For every such n and c, as affine schemes,

    S_c = U                                  if cn!=0 or c_(n-1)=0;
    S_c = U disjoint-union (n-2) copies of A2 if cn=0 and c_(n-1)!=0.

The extra planes are indexed by the distinct nonzero numbers rho with
rho^(n-2)=-1/c_(n-1). Each is given by x=rho, y=-1/rho, with z3,z4 free
and z5,...,zn determined constants. On each plane, (A2,A0) is an affine
automorphism. U is not A2, and admits no dominant morphism from A2.

Thus parametrizing an actual plane component by an isomorphism gives
an automorphism, not a plane counterexample. The separate assertion
about arbitrary polynomial substitutions is stated precisely below;
they must not be silently assumed to be isomorphisms.

## Uniform scheme proof

Let m=n-1 and b=p*z_n+(-1)^m*y^m. Comparing the highest coefficient gives
C_n=p*b. In the ORIGINAL source polynomial ring,

    x^m*b=p*x^m*z_n+(1-p)^m,
    1=p*[sum_{j=0}^{m-1}(1-p)^j-x^m*z_n]+x^m*b.             (1)

Consequently the ideals (p) and (b) are comaximal, before or after imposing
any other high-coefficient relations. This is stronger than a pointwise
assertion that two components do not meet.

On the localization p!=0, all high coefficients recover z_n,...,z4,z3
by a triangular linear system. Indeed, a z_j term for j>=4 contributes

    z_j*(p^2*T^j-2*p*x*T^(j-1)+x^2*T^(j-2)),

while the z3 term has high-degree part p^3*z3*T^3. The descending diagonal
is p^2,...,p^2,p^3, whose product is p^(2n-3). For any constants c, all
z_j therefore solve uniquely as elements of C[x,y,1/p]. The projection
to (x,y) and these solved functions give mutually inverse ring maps:

    (coordinate ring of S_c)[1/p] = C[x,y,1/p].             (2)

No x!=0 assumption is used here; x=0,p=1 is included.

If cn!=0, the relation p*b=cn makes p a unit, so (2) describes all of S_c.
If cn=0, (1) and the Chinese remainder theorem split its WHOLE coordinate
ring into the p=0 and b=0 quotients. In the b=0 quotient, (1) again makes
p a unit, and (2) identifies that quotient with U.

In the p=0 quotient, x is invertible and y=-1/x. Substitution in the
defining polynomial, without using the manuscript's fiber theorem, yields

    Phi(T)=-x^(-(n-2))*(T+x)^(n-1)+n*T-n*x/2+x^3*z3/2
                      +x^2*sum_{j=4}^n z_j*T^(j-2).         (3)

Its coefficient C_(n-1) is -x^(-(n-2)). If c_(n-1)=0 this quotient is
the zero ring. Otherwise x^(n-2)=-1/c_(n-1) splits into n-2 distinct
nonzero roots x=rho over C. On each root factor the remaining equations
C3=c3,...,C_(n-2)=c_(n-2) solve z5,...,zn, each with coefficient rho^2.
There are no such equations when n=4. The remaining ring is exactly
C[z3,z4]. These are disjoint, reduced scheme components: there is no
unexamined embedded component or gluing at p=0.

From (3), the low-coefficient restriction is

    A2 =rho^2*z4-(n-1)*(n-2)/(2*rho),
    A0 =(n+2)*rho/2-rho^3*z3/2.                            (4)

The determinant in coordinates (z3,z4) is rho^5/2!=0. An explicit inverse is

    z4=[A2+(n-1)*(n-2)/(2*rho)]/rho^2,
    z3=[(n+2)*rho-2*A0]/rho^3.

This finishes the asserted scheme classification and plane restrictions.

## Units and the arbitrary-substitution boundary

The domain C[x,y,1/p] has the nonconstant unit p. Since the only units of
C[s,t] are nonzero constants, U cannot be isomorphic to A2. More strongly,
a dominant morphism A2->U would inject its coordinate ring into C[s,t],
but would send p to a constant lambda, killing the nonzero element
p-lambda. Thus no such dominant morphism exists.

Suppose a polynomial substitution h:A2->A^n has C_k composed h=c_k for
all k>=3, and (A2,A0) composed h is a Keller pair. That pair is dominant,
so h has two-dimensional image and dominates a component of S_c. Since
A2 is connected, h lands in a single component. The unit argument excludes
U, so it lands in one of the extra planes. By (4), its two outputs are
merely an invertible affine recombination of z3 composed h and z4 composed h.
Their Keller condition and invertibility are exactly those of this latter
polynomial pair. This is a passthrough of the original plane problem,
NOT an exclusion of hypothetical preexisting Keller maps. If h is an
isomorphism onto a plane component, the output pair is an automorphism.

## Checks, history, and exclusions

- At n=4, direct extraction gives C4=p*(p*z4-y^3) and
  C3=(4*p^2+4*p-1)*y^2+p^3*z3-2*p*x*z4. Formula (1) becomes
  1=p*(1-xy+x^2*y^2-x^3*z4)+x^3*(p*z4-y^3).
- For cn=0,c_(n-1)!=0, (4) supplies actual affine-plane components and
  positive automorphism controls. For cn!=0, every slice is U, not A2.
- The [September 14 dimension check](../notes.md#2026-09-14-1740-utc--source-dimensions-and-six-sheet-history-check)
  already recorded that K4 has FOUR source variables and a conditional
  four-then-two field tower. The present statement derives the actual
  codimension-(n-2) source slices; it does not attach that old tower to a plane.
- ROOT read the mathematical Sections1--10 of the external manuscript,
  including its definition and charts. This report's proof is the displayed
  coefficient/CRT argument, not an independent audit of all external claims,
  source-code execution, raw upstream checksum, or novelty/priority finding.
- No assertion covers different target-coordinate combinations, nonlinear
  target constraints, rational source substitutions, or arbitrary other
  donors. No generic slice farm or automatic successor is selected. The
  only covered family is the precisely defined fixed-high-coefficient one.
- No CAS, exact-Python science, numerical computation, primes, seeds, or
  degree-range search was used. No new exit-price declaration is asserted.
  This is a uniform construction filter, not JC2 resolution.

## COLLISIONS

status: EMPTY

- NONE -- no explicitly raised OPEN entry or successor is commissioned.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7043`.
- Body SHA-256:
  `6463cab63db897962141aefe97fd8dca567690049920ee7a8fb4983b14078f3a`.
- Frozen basis: `18be9c16c95318c2eea9a2cef76e9ea476985482`.
