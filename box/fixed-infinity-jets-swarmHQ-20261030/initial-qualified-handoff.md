# Qualified INITIAL0955 diagnostic handoff

INTERNAL / ROOT-MANUAL / UNREVIEWED. This new sealed handoff preserves the exact two original unsealed ROOT notes below. The seal authenticates this copy; it does not retrospectively seal the originals, supply independent review, establish novelty, or claim a Keller counterexample. Treat the formulas as an explicitly qualified diagnostic to check, not as an admitted theorem. All displayed pairs have nonconstant full Jacobian.

## Exact original: briefs/initial0955-finite-jet-obstruction.md (SHA256 99273774dabe7ff1ed30dacec5e3a6a8870f32e11a40312a7ee1ebfd4b69b388)

# Finite infinity jets do not exclude the normalized degree-two fold

INTERNAL / ROOT-MANUAL / UNREVIEWED. This falsifies a weaker proposed test, not JC2; no novelty or public promotion is claimed. Basis1721739a7b2fdc5570d1d43a69e6c4e957a311ec. No polynomial Keller pair is constructed.

Put z=xy^3-1 and, for an integer n>=1, define the actual polynomials

    P=xy,  Q_n=(1/2) sum_{k=1}^n (-1)^(k+1) z^k/k.

With {f,g}=f_x*g_y-f_y*g_x, direct differentiation gives {P,z}=2(1+z). The finite geometric-series identity therefore gives

    {P,Q_n}=(1+z) sum_{j=0}^{n-1} (-z)^j = 1-(-z)^n.

This Jacobian is nonconstant for every n. The maps are NOT Keller.

Use the rational source coordinates u=y and t=(xy^3-1)/y, so x=(1+ut)/u^3, y=u and z=ut. They generate C(x,y). The chart (u,t) with u=0 defines a divisorial valuation at infinity, since its u!=0 open set is isomorphic to the original y!=0 plane chart. Its volume form is

    dx wedge dy = -u^(-2) du wedge dt.

Thus the primitive raw discrepancy (order of this form plus one) is -1. For every n, along u=0,

    P=u^(-2)(1+ut),  Q_n=ut/2+O(u^2),  {P,Q_n}-1=(-1)^(n+1)u^n t^n.

On the target take genuine rational field generators U=Q and V=P*Q^2, with inverse P=V/U^2, Q=U. The target volume is -U^(-2)dU wedge dV, so the primitive target u=0-type valuation likewise has raw discrepancy -1. Pullback gives

    U=u(t/2+O(u)),  V=t^2/4+O(u).

Consequently the restricted valuation has normal index1 and residue extension C(t)/C(t^2/4) of degree2. The leading normal coefficient t/2 is exactly the derivative of the residue map t^2/4, as required by the leading volume identity. This statement concerns the generic point of the divisors, not an everywhere regular map of these charts.

For every fixed finite order M, choosing n>=M gives Jacobian1 modulo u^M while retaining the SAME source and target discrepancies, normal index and residue degree. Hence those data, together with any fixed truncation of the Jacobian identity along this divisor, do not imply absence of the fold, even when both components come from global polynomials. The degrees are allowed to grow with M; there is no fixed-degree assertion.

The formal limit Q_infinity=(1/2)log(1+z) satisfies the formal Jacobian identity but is not a polynomial. This is only a formal series identity at z=0, not a global map or an allowed replacement for a Keller component.

The missing implication must use exact global polynomial termination or another global compatibility condition. This does not rule out finite certificates that use all coefficients of a given pair, associated-graded methods with additional global input, or the full Keller no-fold conjecture. No control-family continuation, paid/source successor, independent review debt or new public claim follows.

## Exact original: briefs/initial0955-graded-ring.md (SHA256 45bfacca1715b671eb470ed475088ee3eec3b896a36151bef0be34e81179cd3d)

# The full associated graded rings in the finite-jet obstruction

INTERNAL / ROOT-MANUAL / UNREVIEWED supplement to initial0955-finite-jet-obstruction.md. No JC2, novelty or public-promotion claim. This is the same single construction, not a further example program.

Use z=xy^3-1 and u=y. The valuation in the companion note is v(u)=v(z)=1 with z/u transcendental in the residue field. Write U=in_v(u), Z=in_v(z), using valuation degrees deg(U)=deg(Z)=1. Every polynomial in x,y, after x=(1+z)/u^3, y=u, is a finite Laurent polynomial in u,z. Its lowest homogeneous part therefore lies in C[U,U^(-1),Z]. Conversely U=in_v(y), U^(-1)=in_v(xy^2), and Z=in_v(xy^3-1) all come from source polynomials. Thus

    gr_v C[x,y] = C[U,U^(-1),Z].

This equality includes all source initial forms, not only a chosen leading pair. The graded source is finitely generated, normal, smooth, and has nonconstant units. Direct differentiation gives {y,xy^3-1}=-y^3, hence the induced bracket is

    {U,Z}=-U^3.

It is a regular nondegenerate Poisson structure on this Laurent-polynomial ring, since U is invertible. Its degree shift is +1 in valuation degrees, corresponding to raw discrepancy -1. Equivalently the volume form is -U^(-3)dU wedge dZ; setting Z=Ut gives -U^(-2)dU wedge dt.

For the target subalgebra A_n=C[P,Q_n], the initial forms are p=U^(-2), q=Z/2. Distinct monomials P^a Q_n^b have distinct leading monomials 2^(-b)U^(-2a)Z^b, so no cancellation among equal-valuation terms introduces an additional initial generator. Therefore gr_v A_n=C[p,q], embedded by these formulas. Its induced bracket is exactly {p,q}=1, agreeing with the initial form of the nonconstant Jacobian1-(-z)^n. The target valuation is v(p)=-2,v(q)=1, with residue coordinate pq^2=(Z/U)^2/4 and primitive normal coordinate q.

Consequently finite generation, normality and regular symplectic structure of the ACTUAL full graded polynomial source, together with the exact leading Poisson identity and the normalized a_source=a_target=-1,e=1 data, do not force residual degree1. This observation does not assert that these properties hold at every Keller witness; even where they hold, further information is needed.

For these examples the missing information is visible in the lower semidegree terms of the full Jacobian. The source ring before grading has only constant units, while the graded source acquires U and U^(-1). A method retaining the full filtered algebra and exact global Jacobian may still work. This rules out neither such a method nor a finite certificate using all coefficients of a given pair. No separate paid/source/review or control-family successor is admitted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6215`.
- Body SHA-256:
  `29d1d463a1705056b672723ff56fbd5f877456fc17e34e54e65a388bafd4c902`.
- Frozen basis: `397632cbdf8eaaac8c6f22db1c69921adc85f9e4`.
