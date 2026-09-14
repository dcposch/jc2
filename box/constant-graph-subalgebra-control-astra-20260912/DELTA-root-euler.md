# ROOT candidate identity, supplied after independent task launch

September12,2026. Additional permitted scientific input to TASK; original
reserve01:48/HARD01:51 and every other boundary unchanged. The original
task and its frozen bytes remain unmodified. Check independently; no
external-model promotion implied by agreeing with this guidance.

ROOT derives the POSITIVE identity on H=1:

    1 = (r/4) J(p,q) + (q/4) J(p,r) - (p/2) J(q,r).

Thus 1 DOES belong to M, with literal polynomial target coefficients.
It gives no actual f,g pair by itself. At source origin, p=1,q=r=0,
J(q,r)=-2, so the signs at least pass that control.

Candidate derivation: the explicit ambient P,Q,R are homogeneous of
weights2,1,-1 for E=-x*d_x+y*d_y+2z*d_z. Their determinant should be
-2. Contract dP wedge dQ wedge dR=-2 dx wedge dy wedge dz with E,
then restrict to z=1:

    2p J(q,r)-q J(p,r)-r J(p,q) = -4.

One manual way to check the ambient determinant without bulk expansion:
on x!=0 let t=1/x, s=y+t, rho=R. Then

    P=s^2+s*t-rho*s^3,
    Q=4s+2t-3rho*s^2,
    R=rho.

det d(P,Q,R)/d(s,t,rho)=2t, and
det d(s,t,rho)/d(x,y,z)=-1/t. Product -2; polynomial identity
extends over x=0. Check the chart formulas, not just the determinants.

More generally on z=H(x,y), the same contraction would give

    2p J(q,r)-q J(p,r)-r J(p,q)
      =-2*(2H+x H_x-y H_y).

In particular H=c+y^2h(xy), c!=0, has the constant right side -4c,
so the full module contains1 there too. This is a useful exact boundary
to the homogeneous obstruction, not a polynomial Keller pair or JC2
counterexample. Prioritize H=1 original question; state any extension
separately and only if all signs/maps have been checked by the same clock.
