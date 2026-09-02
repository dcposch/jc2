import sympy as sp, time
t0=time.time()
Z=sp.symbols('Z')
a0,s2,s1,s0,q3,q2,q1,q0,r2,r1,g1,g0,f3,f2,f1,f0,kp,tt = sp.symbols(
 'a0 s2 s1 s0 q3 q2 q1 q0 r2 r1 g1 g0 f3 f2 f1 f0 kappa tt')
VARS=[a0,s2,s1,s0,q3,q2,q1,q0,r2,r1,g1,g0,f3,f2,f1,f0,kp,tt]
a=b=sp.Integer(1); d=sp.Rational(3,2)
eta = Z + a0
s   = s2*Z**2+s1*Z+s0
q   = q3*Z**3+q2*Z**2+q1*Z+q0
rp  = 2*r2*Z+r1                     # r' ; r itself only enters through r'
G   = -3*Z**2+g1*Z+g0               # wall: G_2 = -b(1+2e)A^2 = -3
Phi = f3*Z**3+f2*Z**2+f1*Z+f0
def dz(f): return sp.diff(f,Z)
etap,etapp = dz(eta),dz(dz(eta)); sp_,qp,Gp = dz(s),dz(q),dz(G)
psi=eta+Z*etap; chi=eta+2*Z*etap; phi=eta+3*Z*etap
E1 = b*eta*chi+G ; D1 = a*eta**2*phi + d*eta*G
C1 = d*(psi*s + Phi/(2*b))
Xi = (12*a*b*eta**3*etap*(etap+2*Z*etapp) + 4*d*s*(eta*sp_-etap*s)
      + 8*b*eta*(q*etap-qp*eta) + 12*a*eta**3*rp
      + 12*a*eta*((eta*etapp-etap**2)*G + eta*etap*Gp))
EQ3 = sp.expand(eta*Z**2*Xi - 3*a/b*dz(Z*eta**2*G**2))
EQ1 = sp.expand(6*D1*rp - 4*qp*E1 + 2*q*dz(E1) + 4*C1*sp_ - 2*dz(C1)*s + 2*kp*Z)
E2G0 = sp.expand(6*a*Z*eta**2*(3*eta+4*Z*etap)*rp
      + 2*b*(eta**2*q+10*Z*eta*etap*q+4*Z**2*(etap**2+eta*etapp)*q
             -6*Z*eta**2*qp-4*Z**2*eta*etap*qp)
      + 12*a*b*Z*eta**2*etap*(eta*etap-Z*etap**2+Z*eta*etapp)
      + 2*d*Z*(3*eta*s*sp_-2*(2*etap+Z*etapp)*s**2))
Del2 = sp.expand(6*a*Z*eta**2*etap*Gp + 6*a*eta*(eta*etap-3*Z*etap**2+Z*eta*etapp)*G
      + d*(eta*dz(G**2)-4*etap*G**2) + 8*d*Z*eta*G*rp + 4*Z*(q*Gp-qp*G)
      + (d/b)*(Phi*s+2*Z*(Phi*sp_-dz(Phi)*s)))
EQ2 = sp.expand(E2G0+Del2)
EQ4 = sp.expand(2*(s*C1-q*E1)*rp + kp*E1 + q*s*sp_ - qp*s**2)
DIV = sp.expand(eta*Phi - s*G)                      # T1 : eta | sG, with quotient Phi
P2,P1,P0 = sp.symbols("P2 P1 P0")
VARS = VARS[:-1]+[P2,P1,P0,tt]
REM = sp.expand(2*(q*rp - (P2*Z**2+P1*Z+P0)*s) - kp)   # E0
eqs=[]
for P in (EQ1,EQ2,EQ3,EQ4,DIV,REM):
    pol=sp.Poly(sp.expand(P),Z)
    eqs += [sp.expand(c) for c in pol.all_coeffs()]
eqs=[e for e in eqs if e!=0]
eqs.append(sp.expand(s2*q3*r2*kp*tt-1))             # saturation: leaders and kappa nonzero
print("cell (1,3): %d equations, %d unknowns"%(len(eqs),len(VARS)))
gb=sp.groebner(eqs, *VARS, order='grevlex')
print("Groebner basis:", list(gb.exprs)[:6], "..." if len(gb.exprs)>6 else "")
print("IS UNIT IDEAL (cell EMPTY):", list(gb.exprs)==[sp.Integer(1)])
print("time",time.time()-t0)
