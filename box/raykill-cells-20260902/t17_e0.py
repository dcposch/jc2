import sympy as sp
Z=sp.symbols('Z'); a,b,kp,eta0=sp.symbols('a b kappa eta0')
s,q,r,G=[sp.Function(k)(Z) for k in ('s','q','r','G')]
d=sp.Rational(3,2)*a/b
dz=lambda f: sp.diff(f,Z)
eta=eta0; etap=sp.Integer(0); etapp=sp.Integer(0)
sp_,qp,rp,Gp=dz(s),dz(q),dz(r),dz(G)
psi=eta; chi=eta; phi=eta
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
EQ2=E2G0+Del2
# C32 sec 5.1 displays
B=b*eta0**2; A0=a*eta0**3; t=d*eta0; mu=t/(2*B)
I  = 3*A0*rp - 2*B*qp + t*s*sp_
E3d= 2*Z**2*I - t*dz(Z*G**2)
E1d= I + 3*t*G*rp - 2*qp*G + q*Gp + mu*s*(sp_*G - s*Gp) + kp*Z
LG = 2*Z*Gp - G
E2d= 6*Z*I + 2*B*q + 8*t*Z*G*rp - 4*Z*qp*G + 4*Z*q*Gp + 2*t*G*Gp - 2*mu*s**2*LG
print("C32 sec5.1 controls at e=0 (flagship's four identities, independently rebuilt):")
print("  Xi - 4I                        =", sp.simplify(sp.expand(Xi-4*I)))
print("  EQ1 - 2*E1d                    =", sp.simplify(sp.expand(EQ1-2*E1d)))
print("  EQ2 -   E2d                    =", sp.simplify(sp.expand(EQ2-E2d)))
print("  EQ3 - 2*eta0*(2Z^2 I - t(ZG^2)')=", sp.simplify(sp.expand(EQ3-2*eta0*E3d)))
