import sympy as sp
Z = sp.symbols('Z')
def build_cell(e,U,wall=True,params=False,drop=None,normS=False):
    g,m,n = 2*e,U,U-e
    assert (U+e)%2==0; sig=(U+e)//2
    assert (3*n)%2==0
    if params: a,b = sp.symbols('a b')
    else:      a,b = sp.Integer(1), sp.Integer(1)
    d = sp.Rational(3,2)*a/b
    def mk(pref,deg):
        cs=[sp.Symbol('%s%d'%(pref,i)) for i in range(deg+1)]
        return sum(c*Z**i for i,c in enumerate(cs)), cs
    eta,Ac = mk('A',e); s,Sc = mk('S',sig); q,Qc = mk('Q',m); r,Rc = mk('R',n)
    eta = eta - Ac[e]*Z**e + Z**e          # mu-scaling: A_e = 1
    if normS: s = s - Sc[sig]*Z**sig + Z**sig   # Z-scaling: S_sigma = 1 (needs U>3e)
    G,Gc = mk('G',g); Phi,Fc = mk('F',sig+e); pp,Pc = mk('P',3*n//2-1)
    kp = sp.Symbol('kappa'); tt = sp.Symbol('tt')
    VARS = Ac+Sc+Qc+Rc+Gc+Fc+Pc+[kp,tt]+([a,b] if params else [])
    VARS = [v for v in VARS if v is not Ac[e]]
    if normS: VARS = [v for v in VARS if v is not Sc[sig]]
    if wall:
        G = G - Gc[g]*Z**g - b*(1+2*e)*Z**g
        VARS = [v for v in VARS if v is not Gc[g]]
    dz=lambda f: sp.diff(f,Z)
    etap,etapp=dz(eta),dz(dz(eta)); sp_,qp,rp,Gp=dz(s),dz(q),dz(r),dz(G)
    psi=eta+Z*etap; chi=eta+2*Z*etap; phi=eta+3*Z*etap
    E1=b*eta*chi+G; D1=a*eta**2*phi+d*eta*G; C1=d*(psi*s+Phi/(2*b))
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
    EQ2=E2G0+Del2
    EQ4=2*(s*C1-q*E1)*rp+kp*E1+q*s*sp_-qp*s**2
    named={'EQ1':EQ1,'EQ2':EQ2,'EQ3':EQ3,'EQ4':EQ4,
           'T1':eta*Phi-s*G,'E0':2*(q*rp-pp*s)-kp}
    eqs=[]
    for k,P in named.items():
        if drop and k in drop: continue
        eqs += [c for c in sp.Poly(sp.expand(P),Z).all_coeffs() if c!=0]
    sat = (1 if normS else Sc[sig])*Qc[m]*Rc[n]*kp*(a*b if params else 1)*tt-1
    eqs.append(sp.expand(sat))
    return eqs, VARS, dict(e=e,U=U,g=g,m=m,n=n,sig=sig)
