# ROOT candidate — a double-curve residue discriminator

September12,2026,10:58UTC. MANUAL CANDIDATE / UNREVIEWED. Every formula
below must be independently derived before it is used. No residue value,
primitive nonexistence, pair or JC2 result is asserted. No computation.

Use the supplied constant graph z=1 and its chart

    x=1/t, y=s-t,
    U=s^2+st-Ws^3, V=4s+2t-3Ws^2,
    1=5t^2-3st-Wt^3.

For two distinct chart points with the same U,V,W, put
sigma=s+s', delta=s-s', and define new parameters

    a=3W*sigma/4-1, b=W*delta/4.

Subtracting the two cubic equations
W*s^3-2*s^2+V*s-2U=0 suggests

    t=delta*(a+b), t'=-delta*(a-b),
    C=(a+1)/(3b), sigma=C*delta,
    s=delta*(C+1)/2, s'=delta*(C-1)/2.

The difference and sum of the two z values give the candidate equations

    E(a,b)=-a^2-a+20*a*b^2-3*b^2-8*a^3*b^2-24*a*b^4=0,
    K(a,b)=(10-24*b^2)*a^2-4*a-1+10*b^2-8*b^4,
    delta^2=2/K(a,b), W=4b/delta.

On a nonempty open where these expressions and t,t' are defined, they
should give two actual source points with equal target triple, not merely
an abstract curve with a matching numerical profile. Check the common U,V
using V=2*sigma-W*(sigma^2-s*s') and the chart formula for U.

Take the source primitive alpha0=x dy=(ds-dt)/t. Its difference between
the two chart maps is the following candidate rational one-form on E=0:

    eta = a/(a^2-b^2) dC
          -(a*C-b)/(2*(a^2-b^2)) dlog K
          -dlog((a+b)/(a-b)),                 C=(a+1)/(3b).

This follows from delta^2=2/K, so dlog delta=-dlog K/2. It is a formula
on the normalization of the curve, not a two-variable total differential
independent of E. The double cover adjoining delta may be needed for the
actual source maps; any nonzero base residue multiplies by its positive
ramification index on that cover and remains nonzero.

Why the test could decide the original question: if a target-polynomial
one-form alpha satisfies d(phi*alpha)=dx wedge dy, polynomial Poincare on
the source plane gives phi*alpha-alpha0=dH for a polynomial H(x,y). Pull
back along both equal-target maps. The alpha terms cancel, so eta must
be the differential of the difference of the two pulled-back H values.
That is a rational function on the collision curve cover. Its differential
has zero residue at EVERY normalized projective place, including points
where one source chart goes to infinity. Thus a single actual nonzero
residue would obstruct ALL target-polynomial primitives and hence every
Keller pair in the fixed target subalgebra. Zero residues at selected
places do NOT prove exactness or supply a pair.

ONE SPECIFIED TEST (not a pole/degree farm): consider the two points

    a=b=b0,       8*b0^2+8*b0+1=0.

On a=b one has
E(b,b)=-b*(2b-1)^2*(8b^2+8b+1), and K(b,b)=0 at those points.
ROOT's proposed local parameter is u=a-b. With b=b(u), its first derivative
would be

    b'(0)=14*b0^2/(52*b0+9),
    E_a(b0,b0)=-14*b0^2,
    E_a(b0,b0)+E_b(b0,b0)=52*b0+9.

Check that the chosen point is smooth, u is a parameter and K has the
claimed simple zero before using expansions. Compute Res eta there
EXACTLY in Q[b0]/(8*b0^2+8*b0+1), or expose an invalid formula/point.
Do not guess the answer from floating point or from the explicit dlog
term alone: the other terms may have cancelling simple-pole coefficients.
ROOT has not completed that cancellation calculation.

Optional useful simplification, itself to check: alpha0 differs from
(x dy-y dx)/2 by d(xy)/2, hence either gives the same residue. At a=b,
set v=a+b, H=(C+1)/2-v, H'=(C-1)/2+u. Then the difference of the symmetric
primitives is

    H/v*dlog delta + dH/(2*v) + H*dv/(2*v^2)
      + H'/u*dlog delta + dH'/(2*u) + H'*du/(2*u^2).

The leading apparent double pole cancels, but its simple coefficient can
still depend on the second coefficient of K(u). No zero/nonzero conclusion
is supplied here. At b=0,a=0 or -1 the even/odd local structure appears
to force the candidate eta's residue zero; this is NOT a substitute for
the specified a=b test and need not be pursued.

Scope/control: exactness on a collision curve is necessary only. A
nonclosed ambient recipe is not an obstruction, and local primitives do
not descend automatically. A failed candidate formula changes the test,
not the original polynomial pair problem. These raw source calculations
are independent of the unreviewed logarithmic-divergence reformulation.
