# Cofinite-center Euler tests do not supply source structure

Date: 2026-09-15 02:10 UTC. Producer: swarmHQ (ROOT/native Astra).
Evidence: MANUAL. Lifecycle: PRODUCER-CHECKED, UNPROMOTED.

This is a verbatim mathematical excerpt from the
[original research journal](https://github.com/dcposch/jc2/blob/ec69252af5ca03245becb80436f5ddb0917ccef2/notes.md#2026-09-15-0210-utc--cofinite-center-euler-tests-do-not-supply-source-structure).
It retains the argument and controls; operational chronology remains in the source.
This editorial extraction adds no review, promotion, or novelty claim. The control
is not a Keller counterexample. [Current research frontier](../../APPROACHES.md).

---

One changed global-source discriminator was tested manually. The old
Kummer control fails Euler torsion-freeness after centering on an accessible
shifted line. Could requiring joint Euler and tested Bass injectivity in
EVERY polynomial frame centered in a COFINITE target set remove that
abstract obstruction? NO. This is a newly tested sufficient-package
proposal, not a refutation of any promoted source theorem.

Put h=q^2-p^3, alpha=1/5, W=A2 minus{(0,0)}, and

  M=C[p,q,h^(-1)]e,  d(e)=alpha*(dh/h)e,  e^5=h.

This is a nonzero full Weyl module, an algebraic rank-one connection of
finite monodromy on h!=0. It is not a polynomial source quotient. With
E=2p*partial_p+3q*partial_q, grade p,q,dp,dq by2,3,2,3 and e by6/5.
Every twisted de Rham form is a FINITE sum of terms with weights in
6/5+Z, hence no zero weight. Cartan gives L_E=d_nabla*i_E+i_E*d_nabla;
i_E*L_E^(-1) is an algebraic contracting homotopy. Thus ALL de Rham
cohomology of M vanishes, without analytic convergence or a rank formula.

Take ANY polynomial coordinates u,v whose common zero c lies in W.
Write H for h in those coordinates, Eu=u*partial_u, Ev=v*partial_v.
For every nonzero m in M, its generic H-divisor exponent is
lambda=1/5+k, k an integer. If a nonzero Euler polynomial P(Eu,Ev)
of degree n>0 killed m, its most singular coefficient would be a unit times

  lambda*(lambda-1)*...*(lambda-n+1)*P_n(u*H_u,v*H_v) modulo H,

where P_n is the top homogeneous part. All lower-order operator terms,
including derivatives of intermediate coefficients, have lower pole order.
The falling factorial never vanishes. Factoring P_n over C and using
irreducibility of H forces a nonzero diagonal field
a*u*partial_u+b*v*partial_v tangent to the transformed cusp. Degree
comparison makes its action on H a CONSTANT multiple of H. Its flow
therefore preserves the unique singular point. If a,b are nonzero, that
point must be the coordinate origin, contradicting c!=(0,0) in the
original plane. If one coefficient is zero, semi-invariance forces
H=u^r A(v), or the symmetric expression; irreducibility over C forces a
smooth coordinate line, not a cusp. A constant nonzero P is harmless.
Consequently M is JOINTLY C[Eu,Ev]-torsion-free in EVERY permitted frame.

The SAME symbol argument also proves injectivity of every tested operator

  L=Eu-r+u*partial_v*G(Eu,Ev), r>=0, G in C[X,Y].

For deg G=k>=1 its order-k+1 conormal coefficient is
u*H_v*G_k(u*H_u,v*H_v), with the same nonzero fractional falling factorial.
Neither u nor H_v vanishes identically on an irreducible cusp, so a kernel
again forces the forbidden diagonal tangency. For G=gamma constant,
L=u*(partial_u+gamma*partial_v)-r. A kernel would give
H dividing H_u+gamma*H_v; smaller degree forces that derivative to vanish.
Then H belongs to C[v-gamma*u] and irreducibility makes it a line.
This includes gamma=0; r contributes only a lower-order term.

Negative controls/boundary: at the EXCLUDED cusp center in the original
coordinates, (2ep+3eq-6/5)e=0. Thus extending the center quantifier to
every target point is a genuinely stronger condition, not silently proved.
Replacing alpha by0 retains the constant section, killed by Euler
operators, and also destroys acyclicity. The noninteger exponent matters.
No Mellin-rank, no-delta-line, arbitrary U-annihilator, permutation-module,
actual-Keller realization or surjectivity statement has been established.
In particular W is stipulated, NOT proved to occur as a Keller image.
The actual-source formal-lift/field/algebra conditions remain essential;
neither the old nor the new abstract control supplies them.
