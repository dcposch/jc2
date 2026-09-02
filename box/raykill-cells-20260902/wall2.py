import sympy as sp

Z = sp.symbols('Z')
a, b, kap = sp.symbols('a b kappa')
A,A1,A2, S,S1,S2, Q,Q1,Q2, R,R1,R2, C,C1g,C2g = sp.symbols(
    'A A1 A2 S S1 S2 Q Q1 Q2 R R1 R2 C C1g C2g')
d = sp.Rational(3,2)*a/b

def dz(f): return sp.expand(sp.diff(f, Z))

def trunc(expr, hi, keep):
    """drop all Z-powers strictly below hi-keep+1 ; expr must be a Laurent poly in Z"""
    out = 0
    for t in sp.Add.make_args(sp.expand(expr)):
        cf, ex = t.as_coeff_exponent(Z)
        if ex >= hi-keep+1:
            out += cf*Z**ex
    return out

def zdict(expr):
    D = {}
    for t in sp.Add.make_args(sp.expand(expr)):
        cf, ex = t.as_coeff_exponent(Z)
        D[int(ex)] = D.get(int(ex), 0) + cf
    return D

def zc(expr, k):
    return sp.expand(zdict(expr).get(k, 0))

def model(e, U, K=3):
    g, m, n = 2*e, U, U-e
    assert (U+e) % 2 == 0
    sig = (U+e)//2
    def poly(lead, cs, deg):
        f = lead*Z**deg
        for i,ci in enumerate(cs, start=1):
            if deg-i >= 0: f += ci*Z**(deg-i)
        return f
    eta = poly(A,[A1,A2][:K-1], e)
    s   = poly(S,[S1,S2][:K-1], sig)
    q   = poly(Q,[Q1,Q2][:K-1], m)
    r   = poly(R,[R1,R2][:K-1], n)
    G   = poly(C,[C1g,C2g][:K-1], g)
    return dict(e=e,U=U,g=g,m=m,n=n,sig=sig,eta=eta,s=s,q=q,r=r,G=G,K=K)

def equations(M):
    K = M['K']
    eta,s,q,r,G = M['eta'],M['s'],M['q'],M['r'],M['G']
    e,g,m,n,sig = M['e'],M['g'],M['m'],M['n'],M['sig']
    etap, etapp = dz(eta), dz(dz(eta))
    sp_, qp, rp, Gp = dz(s), dz(q), dz(r), dz(G)
    psi = eta + Z*etap; chi = eta + 2*Z*etap; phi = eta + 3*Z*etap
    E1  = sp.expand(b*eta*chi + G)
    D1  = sp.expand(a*eta**2*phi + d*eta*G)
    # Phi = s G / eta  as a truncated Laurent series (K terms), inverse built from the actual eta
    h = sp.expand(sp.cancel(eta/(A*Z**e)) - 1)
    inv = 1
    hp = 1
    for i in range(1, K):
        hp = trunc(sp.expand(hp*h), 0, K)
        inv += (-1)**i*hp
    invEta = sp.expand(inv/(A*Z**e))
    Phi = trunc(sp.expand(s*G*invEta), sig+g-e, K)
    C1  = sp.expand(d*(psi*s + Phi/(2*b)))
    Xi = sp.expand(12*a*b*eta**3*etap*(etap + 2*Z*etapp)
        + 4*d*s*(eta*sp_ - etap*s) + 8*b*eta*(q*etap - qp*eta) + 12*a*eta**3*rp
        + 12*a*eta*((eta*etapp - etap**2)*G + eta*etap*Gp))
    EQ3 = sp.expand(eta*Z**2*Xi - (sp.Integer(3)*a/b)*dz(Z*eta**2*G**2))
    EQ1 = sp.expand(6*D1*rp - 4*qp*E1 + 2*q*dz(E1) + 4*C1*sp_ - 2*dz(C1)*s + 2*kap*Z)
    E2G0 = sp.expand(6*a*Z*eta**2*(3*eta + 4*Z*etap)*rp
        + 2*b*( eta**2*q + 10*Z*eta*etap*q + 4*Z**2*(etap**2 + eta*etapp)*q
                - 6*Z*eta**2*qp - 4*Z**2*eta*etap*qp )
        + 12*a*b*Z*eta**2*etap*( eta*etap - Z*etap**2 + Z*eta*etapp )
        + 2*d*Z*( 3*eta*s*sp_ - 2*(2*etap + Z*etapp)*s**2 ))
    Del2 = sp.expand(6*a*Z*eta**2*etap*Gp
        + 6*a*eta*( eta*etap - 3*Z*etap**2 + Z*eta*etapp )*G
        + d*( eta*dz(G**2) - 4*etap*G**2 ) + 8*d*Z*eta*G*rp + 4*Z*(q*Gp - qp*G)
        + (d/b)*( Phi*s + 2*Z*(Phi*sp_ - dz(Phi)*s) ))
    EQ2 = sp.expand(E2G0 + Del2)
    EQ4 = sp.expand(2*(s*C1 - q*E1)*rp + kap*E1 + q*s*sp_ - qp*s**2)
    return dict(EQ1=EQ1,EQ2=EQ2,EQ3=EQ3,EQ4=EQ4,E1=E1,D1=D1,C1=C1,Phi=Phi,Xi=Xi)

def tops(M):
    e,U = M['e'],M['U']
    return dict(EQ1=U+2*e-1, EQ2=U+2*e, EQ3=3*e+1+U, EQ4=2*U+e-1)
