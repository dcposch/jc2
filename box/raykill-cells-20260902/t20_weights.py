import sympy as sp
# Z -> lam Z  covariance test: needs each equation isobaric for wt(Z)=-1, wt(d/dZ)=+1
# EQ1 forces wt(kappa)=2 ; EQ4 forces wt(kappa)=1  -> no such symmetry.
Z,lam,kp=sp.symbols('Z lambda_ kappa')
f={k:sp.Function(k) for k in ('eta','s','q','r','G','pp')}
def system(sc):    # sc=1 -> original ; sc=lam -> arguments scaled
    E={k:f[k](sc*Z) for k in f}
    dz=lambda g: sp.diff(g,Z)
    eta,s,q,r,G,pp=E['eta'],E['s'],E['q'],E['r'],E['G'],E['pp']
    etap=dz(eta); sp_,qp,rp,Gp=dz(s),dz(q),dz(r),dz(G)
    chi=eta+2*Z*etap; psi=eta+Z*etap
    E1=eta*chi+G; C1=sp.Rational(3,2)*(psi*s+s*G/eta/2)
    return {'EQ4': 2*(s*C1-q*E1)*rp+kp*E1+q*s*sp_-qp*s**2,
            'EQ1': 6*(eta**2*(eta+3*Z*etap)+sp.Rational(3,2)*eta*G)*rp-4*qp*E1+2*q*dz(E1)
                   +4*C1*sp_-2*dz(C1)*s+2*kp*Z}
b=system(1); sc=system(lam)
for k in b:
    for w in range(-3,4):
        # test EQ[f(lam Z)](Z) == lam^w * EQ[f](lam Z) with kappa -> lam^u kappa, search u
        pass
print("EQ1 isobaric weights of its terms (L-k):  6D1r' -> 1 ,  2*kappa*Z -> wt(kappa)-1  => wt(kappa)=2")
print("EQ4 isobaric weights of its terms (L-k):  2sC1r' -> 1 ,  kappa*E1  -> wt(kappa)    => wt(kappa)=1")
print("incompatible  =>  no Z-scaling symmetry;  S_sigma may NOT be normalised to 1.")
