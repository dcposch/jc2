import sympy as sp

Z, T = sp.symbols('Z T')
a, b, kap = sp.symbols('a b kappa')
A, A1, S, S1, Q, Q1, R, R1, C, C1g = sp.symbols('A A1 S S1 Q Q1 R R1 C C1g')
d = sp.Rational(3,2)*a/b

def dz(f): return sp.diff(f, Z)

def model(e, U, nterms=2):
    """Chamber II (g=2e) simultaneous-top cell.  Truncated top-`nterms` parts."""
    g   = 2*e
    m   = U
    n   = U - e
    assert (U+e) % 2 == 0, "parity: 2*sigma = U+e"
    sig = (U+e)//2
    eta = A*Z**e     + (A1*Z**(e-1)   if e>=1 else 0)
    s   = S*Z**sig   + (S1*Z**(sig-1) if sig>=1 else 0)
    q   = Q*Z**m     + (Q1*Z**(m-1)   if m>=1 else 0)
    r   = R*Z**n     + (R1*Z**(n-1)   if n>=1 else 0)
    G   = C*Z**g     + (C1g*Z**(g-1)  if g>=1 else 0)
    return dict(e=e,U=U,g=g,m=m,n=n,sig=sig,eta=eta,s=s,q=q,r=r,G=G)

def equations(M):
    eta,s,q,r,G = M['eta'],M['s'],M['q'],M['r'],M['G']
    etap, etapp = dz(eta), dz(dz(eta))
    sp_, qp, rp, Gp = dz(s), dz(q), dz(r), dz(G)

    psi = eta + Z*etap
    chi = eta + 2*Z*etap
    phi = eta + 3*Z*etap
    E1  = b*eta*chi + G                 # = (b Z eta^2)' + G
    D1  = a*eta**2*phi + d*eta*G        # = (a Z eta^3)' + d eta G
    Phi = s*G/eta
    C1  = d*(psi*s + Phi/(2*b))

    Xi = (12*a*b*eta**3*etap*(etap + 2*Z*etapp)
        + 4*d*s*(eta*sp_ - etap*s)
        + 8*b*eta*(q*etap - qp*eta)
        + 12*a*eta**3*rp
        + 12*a*eta*((eta*etapp - etap**2)*G + eta*etap*Gp))

    EQ3 = eta*Z**2*Xi - (sp.Integer(3)*a/b)*dz(Z*eta**2*G**2)
    EQ1 = 6*D1*rp - 4*qp*E1 + 2*q*dz(E1) + 4*C1*sp_ - 2*dz(C1)*s + 2*kap*Z

    E2G0 = (6*a*Z*eta**2*(3*eta + 4*Z*etap)*rp
        + 2*b*( eta**2*q + 10*Z*eta*etap*q + 4*Z**2*(etap**2 + eta*etapp)*q
                - 6*Z*eta**2*qp - 4*Z**2*eta*etap*qp )
        + 12*a*b*Z*eta**2*etap*( eta*etap - Z*etap**2 + Z*eta*etapp )
        + 2*d*Z*( 3*eta*s*sp_ - 2*(2*etap + Z*etapp)*s**2 ))
    Del2 = (6*a*Z*eta**2*etap*Gp + 6*a*eta*( eta*etap - 3*Z*etap**2 + Z*eta*etapp )*G
        + d*( eta*dz(G**2) - 4*etap*G**2 ) + 8*d*Z*eta*G*rp + 4*Z*(q*Gp - qp*G)
        + (d/b)*( Phi*s + 2*Z*(Phi*sp_ - dz(Phi)*s) ))
    EQ2 = E2G0 + Del2

    EQ4 = 2*(s*C1 - q*E1)*rp + kap*E1 + q*s*sp_ - qp*s**2
    return dict(EQ1=EQ1, EQ2=EQ2, EQ3=EQ3, EQ4=EQ4, E1=E1, D1=D1, C1=C1, Phi=Phi)

def tops(M):
    e,U = M['e'], M['U']
    return dict(EQ1=U+2*e-1, EQ2=U+2*e, EQ3=3*e+1+U, EQ4=2*U+e-1)

def laurent(expr, top, k=3):
    """coefficients of Z^top, Z^(top-1), ... , Z^(top-k+1)"""
    f = sp.cancel(sp.together(expr)).subs(Z, 1/T)
    f = sp.cancel(sp.expand(f)*T**top)
    ser = sp.series(f, T, 0, k).removeO()
    ser = sp.expand(ser)
    return [sp.simplify(ser.coeff(T, i)) for i in range(k)]
