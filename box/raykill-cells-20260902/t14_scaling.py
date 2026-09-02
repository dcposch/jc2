import sympy as sp
Z=sp.symbols('Z'); a,b,kp=sp.symbols('a b kappa'); al,bt=sp.symbols('alpha_ beta_')
eta,s,q,r,G,pp = [sp.Function(k)(Z) for k in ('eta','s','q','r','G','pp')]
d=sp.Rational(3,2)*a/b
def dz(f): return sp.diff(f,Z)
def build(eta,s,q,r,G,pp,a,b,kp):
    d=sp.Rational(3,2)*a/b
    etap,etapp=dz(eta),dz(dz(eta)); sp_,qp,rp,Gp=dz(s),dz(q),dz(r),dz(G)
    psi=eta+Z*etap; chi=eta+2*Z*etap; phi=eta+3*Z*etap
    E1=b*eta*chi+G; D1=a*eta**2*phi+d*eta*G; Phi=s*G/eta; C1=d*(psi*s+Phi/(2*b))
    Xi=(12*a*b*eta**3*etap*(etap+2*Z*etapp)+4*d*s*(eta*sp_-etap*s)
        +8*b*eta*(q*etap-qp*eta)+12*a*eta**3*rp
        +12*a*eta*((eta*etapp-etap**2)*G+eta*etap*Gp))
    EQ3=eta*Z**2*Xi-3*a/b*dz(Z*eta**2*G**2)
    EQ1=6*D1*rp-4*qp*E1+2*q*dz(E1)+4*C1*sp_-2*dz(C1)*s+2*kp*Z
    E2G0=(6*a*Z*eta**2*(3*eta+4*Z*etap)*rp
        +2*b*(eta**2*q+10*Z*eta*etap*q+4*Z**2*(etap**2+eta*etapp)*q
              -6*Z*eta**2*qp-4*Z**2*eta*etap*qp)
        +12*a*b*Z*eta**2*etap*(eta*etap-Z*etap**2+Z*eta*etapp)
        +2*d*Z*(3*eta*s*sp_-2*(2*etap+Z*etapp)*s**2))
    Del2=(6*a*Z*eta**2*etap*Gp+6*a*eta*(eta*etap-3*Z*etap**2+Z*eta*etapp)*G
        +d*(eta*dz(G**2)-4*etap*G**2)+8*d*Z*eta*G*rp+4*Z*(q*Gp-qp*G)
        +(d/b)*(Phi*s+2*Z*(Phi*sp_-dz(Phi)*s)))
    return dict(EQ1=EQ1,EQ2=E2G0+Del2,EQ3=EQ3,
                EQ4=2*(s*C1-q*E1)*rp+kp*E1+q*s*sp_-qp*s**2,
                E0=2*(q*rp-pp*s)-kp)
base=build(eta,s,q,r,G,pp,a,b,kp)
# scaling:  a->al*a, b->bt*b, s->bt*s, q->al*q, r->bt*r, G->bt*G, p'->al*p', kappa->al*bt*kappa
scal=build(eta, bt*s, al*q, bt*r, bt*G, al*pp, al*a, bt*b, al*bt*kp)
pred={'EQ1':al*bt,'EQ2':al*bt,'EQ3':al*bt,'EQ4':al*bt**2,'E0':al*bt}
for k in base:
    print("  %s : scal - pred*base = %s"%(k, sp.simplify(sp.expand(scal[k]-pred[k]*base[k]))))
# Z-scaling  Z -> lam Z with kappa -> lam kappa : each EQ_j(lam Z) picks weight lam^{w_j}
lam=sp.symbols('lambda_')
W=sp.symbols('W')
sub={Z:lam*W}
etaL=sp.Function('eta')(lam*W); sL=sp.Function('s')(lam*W); qL=sp.Function('q')(lam*W)
rL=sp.Function('r')(lam*W); GL=sp.Function('G')(lam*W); ppL=sp.Function('pp')(lam*W)

print("mu-scaling: eta->mu*eta, s->mu^2 s, q->mu^3 q, r->mu^2 r, G->mu^2 G, p'->mu^4 p', kappa->mu^5 kappa")
mu=sp.symbols('mu_')
for pw in [4,3,5]:
    sc=build(mu*eta, mu**2*s, mu**3*q, mu**2*r, mu**2*G, mu**pw*pp, a, b, mu**5*kp)
    predm={'EQ1':mu**5,'EQ2':mu**5,'EQ3':mu**6,'EQ4':mu**7,'E0':mu**5}
    res={k: sp.simplify(sp.expand(sc[k]-predm[k]*base[k])) for k in base}
    print("  p'-weight mu^%d :"%pw, res)
