# ROOT extension draft, September12 01:24UTC

UNREVIEWED ROOT scratch derivation, not a sealed report or a task invitation.
Originally drafted as an optional Astra delta, but NEVER SENT: Astra had
already completed its original task at01:23:45. Its immutable TASK and
homogeneous-only report remain unchanged. This proposed wider scope has
NOT been checked by Astra. No new agent, review or AWS lane is launched.

Conjectured same full-module obstruction for every H=y^2 K(xy,y),
K in C[w,y], i.e. every monomial x^i y^j of H has j-i>=2.
This includes arbitrary higher-weight perturbations of the original graph.

Set t=1/x,w=xy, so x=t^-1,y=tw. Write
T(t,w)=t^-2 H(t^-1,tw)=w^2 K(w,tw), a polynomial.
k(t,w)=2-3w-T(t,w). Its specialization k0(w) has k0(0)=2,
k0'(0)=-3. The restricted outputs are

 p=t^2 a, q=t b, r=t^-1 k,
 a=(1+w)^3 T+w^2(1+w)(4+3w),
 b=w+3(1+w)^2 T+3w^2(4+3w)
  =4w+6-3(1+w)^2 k.

For each root alpha of nonconstant k0, a Puiseux branch w(t)->alpha
with k(t,w(t))=0 exists (Weierstrass/Newton--Puiseux, or continuity
of complex polynomial roots after a local factor). Along it target(p,q,r)
tends to (0,0,0). All a,b,k and their partial derivatives stay bounded.
Since dx wedge dy=-t^-1 dt wedge dw, direct derivatives give

 J(p,q)=O(t^3),
 J(p,r)=-t[(2a+t*a_t)*k_w+a_w*k-t*a_w*k_t] ->0,
 J(q,r)=-[(b+t*b_t)*k_w+b_w*k-t*b_w*k_t]
        ->-(4alpha+6)*k0'(alpha).

At the actual source origin, H has zero first jet, target=(0,0,0)
and minor tuple=(0,0,-2). Hence any constant nonzero full-module
identity C0=A(p,q,r)Jpq+B(p,q,r)Jpr+C(p,q,r)Jqr forces C(0)=-C0/2.
Taking the limit along EVERY branch above forces
(4alpha+6)k0'(alpha)=2 at every root alpha of k0.
Repeated roots are impossible; the same squarefree-divisibility ODE
and -20=8deg(k0) contradiction from TASK now applies.

Check signs, branch existence including multiple roots and varying degree,
and bounded derivatives. A convergent sequence of roots tending to each
alpha suffices; no analytic derivative of w(t) is used. Thus Rouche's
theorem on a small circle may replace Puiseux entirely. No general H,
arbitrary source embedding, rational target coefficients, or JC2 claim.
