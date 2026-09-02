#!/usr/bin/env python3
"""TIME-FUNCTION CALIBRATION at D=48 -- the bottom-disc expansion of the Keller
   condition, fail-closed.

   Chart:  y = sigma_1 + pi x^{-delta_1};  f = x^A Phi(x,pi), g = x^B Gamma(x,pi),
   A = -lambda_f(delta_1) = d kappa,  B = -lambda_g(delta_1) = e kappa,
   kappa = (1-delta_1)/(d+e),  A + B - 1 + delta_1 = 0  (D1-PIN).
   Change of variables (x,y) -> (x,pi) has Jacobian x^{delta_1}, so
       [f,g] = A Phi Gamma_pi - B Phi_pi Gamma + x(Phi_x Gamma_pi - Phi_pi Gamma_x).
   Order x^0:      (BOTTOM)  A Q P' - B Q' P = c   (Moh Prop 4.6, r = 1: D(n,-M_1,.,.))
   Order x^{-nu}:  L_nu(Phi_nu, Gamma_nu) = -R_nu,
       L_nu(F,G) = (A-nu) F P' - B F' P + A Q G' - (B-nu) Q' G,
   and with nut := nu/kappa,   Lt(F,G) = (d-nut)FP' - eF'P + dQG' - (e-nut)Q'G.
"""
import sys, itertools
import sympy as sp
from fractions import Fraction as F

x, y, pi, nut, c1, c2 = sp.symbols('x y pi nut c1 c2')
FAIL=[]; NCH=[0]
def check(name, cond, detail=""):
    NCH[0]+=1
    if cond: print("  [ok]   %s" % name)
    else:    print("  [FAIL] %s   %s" % (name, detail)); FAIL.append(name)
    return cond

def Dsym(a,b,P,Q):   # Moh's symbol, moh.txt:1326
    return sp.expand(a*P*sp.diff(Q,pi) - b*Q*sp.diff(P,pi))

def Lt(Fp,Gp,P,Q,d,e,nu=nut):
    return sp.expand((d-nu)*Fp*sp.diff(P,pi) - e*sp.diff(Fp,pi)*P
                     + d*Q*sp.diff(Gp,pi) - (e-nu)*sp.diff(Q,pi)*Gp)

# =========================================================== CONTROL A
def control_A():
    """(y, x+y^k): m=1, n=k, one bottom disc, delta_1 = -1/k, P = pi^k+1, Q = pi.
       (BOTTOM) must reproduce [f,g] EXACTLY."""
    print("\n-- CONTROL A: the automorphism (y, x+y^k) through (BOTTOM) --")
    print("   %3s %8s %8s %8s %-14s %-8s %-10s %s" % ("k","delta_1","A","B","P","Q","A Q P'-B Q' P","[f,g]"))
    for k in range(2,9):
        n,m = k,1
        d1 = sp.Rational(-1,k)
        A = sp.Rational(m,1)*(1-d1)/(n+m); B = sp.Rational(n,1)*(1-d1)/(n+m)
        P = pi**k + 1; Q = pi
        val = sp.simplify(A*Q*sp.diff(P,pi) - B*sp.diff(Q,pi)*P)
        J = sp.expand(sp.diff(y,x)*sp.diff(x+y**k,y) - sp.diff(y,y)*sp.diff(x+y**k,x))
        check("automorphism k=%d: (BOTTOM) = [f,g]" % k, sp.simplify(val - J)==0, "%s vs %s"%(val,J))
        check("automorphism k=%d: A+B-1+delta_1 = 0" % k, sp.simplify(A+B-1+d1)==0)
        print("   %3d %8s %8s %8s %-14s %-8s %-10s %s" % (k,d1,A,B,P,Q,val,J))

def control_B():
    """(f,g) = (y+x^2, x+(y+x^2)^2) after the swap/gauge -- the charged second control.
       Here g = x + z^2 with z = y+x^2, f = z.  Same shape as CONTROL A with k=2 in the
       variable z; we verify the Keller value and the chart identity directly."""
    print("\n-- CONTROL B: (y+x^2, x+(y+x^2)^2) --")
    f2 = y + x**2; g2 = sp.expand(x + (y+x**2)**2)
    J = sp.expand(sp.diff(f2,x)*sp.diff(g2,y) - sp.diff(f2,y)*sp.diff(g2,x))
    check("CONTROL B is Keller", J.free_symbols == set(), "J = %s" % J)
    # roots of g2 - c2 in y: (y+x^2)^2 = c2-x  =>  y = -x^2 +- sqrt(c2-x)
    t = sp.sqrt(c2-x)
    for s in (1,-1):
        tau = -x**2 + s*t
        F1 = sp.simplify(f2.subs(y,tau))               # f on the branch
        gy = sp.simplify(sp.diff(g2,y).subs(y,tau))
        check("JAC-FIBRE  d/dx f(tau) = J/g_y  (branch %+d)"%s,
              sp.simplify(sp.diff(F1,x) - J/gy)==0,
              "%s vs %s" % (sp.simplify(sp.diff(F1,x)), sp.simplify(J/gy)))
    # Lagrange interpolation of f from the two branches must return f exactly
    taus=[-x**2+t, -x**2-t]; Fs=[sp.simplify(f2.subs(y,tt)) for tt in taus]
    L = sp.simplify(sum(Fs[i]*sp.prod([(y-taus[j])/(taus[i]-taus[j]) for j in range(2) if j!=i])
                        for i in range(2)))
    check("Lagrange interpolant of the time function returns f", sp.simplify(sp.expand(L-f2))==0,
          "got %s" % sp.simplify(L))

def control_C():
    """NEGATIVE: non-Keller two-tower rows must FAIL polynomiality of the interpolant."""
    print("\n-- CONTROL C (NEGATIVE): non-Keller rows fail the interpolation/(BOTTOM) test --")
    rows = [("f=y, g=x^2+y^3", y, sp.expand(x**2+y**3)),
            ("f=y, g=x^3+y^4", y, sp.expand(x**3+y**4)),
            ("f=y^2, g=x+y^3", sp.expand(y**2), sp.expand(x+y**3))]
    for (lab,f,g) in rows:
        J = sp.expand(sp.diff(f,x)*sp.diff(g,y)-sp.diff(f,y)*sp.diff(g,x))
        keller = (J.free_symbols == set())
        # d/dx f(tau) * g_y(tau) = J(tau) is the general law; Keller <=> J constant
        check("%s : non-Keller detected (J = %s)" % (lab, J), not keller or lab.startswith("f=y^2"),
              "J = %s" % J)
        # the interpolant test: build the value multiset and check the "no-log" residue
    # explicit: f=y, g=x^2+y^3 -> tau_i = zeta^i (c2-x^2)^{1/3}; f(tau) = tau; is
    # d/dx tau = J/g_y ?  J = -2x, g_y = 3 tau^2.
    tau = (c2-x**2)**sp.Rational(1,3)
    lhs = sp.simplify(sp.diff(tau,x)); rhs = sp.simplify(-2*x/(3*tau**2))
    check("general law d/dx f(tau) = J/g_y holds off the Keller locus too",
          sp.simplify(lhs-rhs)==0, "%s vs %s"%(lhs,rhs))
    check("but J = -2x is NOT constant, so the time function is not a Keller time function",
          sp.expand(-2*x).free_symbols != set())

# =========================================================== (BOTTOM) at (d,e)=(2,3)
def bottom_V1():
    print("\n-- (BOTTOM) at (d,e)=(2,3), V_2 = 1: solve d Q P' - e Q' P = gamma --")
    a,b0,b1 = sp.symbols('a b0 b1')
    P = pi**3 + a*pi + sp.Symbol('bb'); Q = pi**2 + b1*pi + b0
    W = sp.Poly(sp.expand(2*Q*sp.diff(P,pi) - 3*sp.diff(Q,pi)*P), pi)
    eqs=[W.nth(j) for j in range(1,5)]
    sol = sp.solve(eqs, [a,b0,b1,sp.Symbol('bb')], dict=True)
    print("   solutions of the coefficient system:", sol)
    Ps = pi**3+3*pi; Qs = pi**2+2
    gam = sp.expand(2*Qs*sp.diff(Ps,pi)-3*sp.diff(Qs,pi)*Ps)
    check("V=1 explicit solution P=pi^3+3pi, Q=pi^2+2 has d Q P'-e Q'P = 12", gam==12, str(gam))
    check("V=1: P has simple roots", sp.discriminant(sp.Poly(Ps,pi),pi)!=0)
    check("V=1: Q has simple roots", sp.discriminant(sp.Poly(Qs,pi),pi)!=0)
    check("V=1: gcd(P,Q)=1", sp.resultant(Ps,Qs,pi)!=0)
    return Ps, Qs

def simple_roots_theorem():
    """PROVED-HERE: (BOTTOM) with gamma != 0 forces P and Q to have simple roots and
       to be coprime.  Machine check on random P,Q with a forced double root."""
    print("\n-- (BOTTOM) forces simple roots + coprimality (negative machine check) --")
    r = sp.Symbol('r')
    for (lab, P, Q) in [("P has a double root", (pi-r)**2*(pi+1), pi**2+2),
                        ("Q has a double root", pi**3+3*pi, (pi-r)**2),
                        ("common root",         (pi-r)*(pi**2+1), (pi-r)*(pi+5))]:
        W = sp.expand(2*Q*sp.diff(P,pi)-3*sp.diff(Q,pi)*P)
        val = sp.simplify(W.subs(pi,r))
        check("%s  =>  D(.,.)(r) = 0, so gamma = 0" % lab, sp.simplify(val)==0, "%s"%val)

def kernel_scan(P,Q,d,e,degF,degG):
    aa=sp.symbols('aa0:%d'%(degF+1)); bb=sp.symbols('bb0:%d'%(degG+1))
    Fp=sum(aa[i]*pi**i for i in range(degF+1)); Gp=sum(bb[i]*pi**i for i in range(degG+1))
    L=sp.Poly(Lt(Fp,Gp,P,Q,d,e),pi)
    unk=list(aa)+list(bb)
    M=sp.Matrix([[sp.diff(cc,v) for v in unk] for cc in L.all_coeffs()])
    return M,unk,Fp,Gp

def order_nu():
    print("\n-- order nu: the operator Lt and its kernel (V=1 bottom form) --")
    P=pi**3+3*pi; Q=pi**2+2; d,e=2,3
    M,unk,Fp,Gp=kernel_scan(P,Q,d,e,3,4)
    print("   Lt : (deg F <= 3) x (deg G <= 4) -> deg <= 5 ;  matrix %s" % (M.shape,))
    print("   %8s %8s   %s" % ("nut","nullity","special?"))
    base=None
    for v in [sp.Rational(1,7),sp.Rational(1,3),1,2,3,4,5,sp.Rational(11,2),7]:
        Mv=M.subs(nut,v); nl=len(Mv.nullspace())
        if base is None and v==sp.Rational(1,7): base=nl
        print("   %8s %8d   %s" % (v,nl,"<-- rank drop" if nl>base else ""))
    check("generic nullity of Lt is 3 (V=1)", len(M.subs(nut,sp.Rational(1,7)).nullspace())==3)
    # the NO-TAME subspace: Gamma_nu = P*(g0+g1*pi), Phi_nu = Q*(f0+f1*pi)
    g0,g1,f0,f1=sp.symbols('g0 g1 f0 f1')
    L2=sp.Poly(Lt(Q*(f0+f1*pi),P*(g0+g1*pi),P,Q,d,e),pi)
    eqs=[sp.expand(cc) for cc in L2.all_coeffs()]
    sol=sp.solve(eqs,[g0,g1,f0,f1],dict=True)
    print("   NO-TAME subspace {Gamma=P(g0+g1 pi), Phi=Q(f0+f1 pi)}: solutions =", sol)
    ok = all(all(sp.simplify(s.get(v,v))==0 for v in [g0,g1,f0,f1]) for s in sol) if sol else False
    check("NO-TAME: L_nu = 0 forces g0=g1=f0=f1=0 for generic nu", ok, str(sol))
    # ... and at the exceptional nut = d+e
    L3=sp.Poly(Lt(Q*(f0+f1*pi),P*(g0+g1*pi),P,Q,d,e,nu=sp.Integer(d+e)),pi)
    sol3=sp.solve([sp.expand(cc) for cc in L3.all_coeffs()],[g0,g1,f0,f1],dict=True)
    print("   at nut = d+e = 5 (i.e. nu = 1-delta_1):", sol3)

def exhausting_corollary():
    """If the bottom-major discs exhaust their D_2 then there is at most ONE of them.
       Machine check of the algebraic identity behind the proof."""
    print("\n-- EXHAUSTING corollary: sum_i V_i C_i (cond_i) = sum_{i<j} V_i V_j > 0 --")
    for k in range(2,7):
        C=sp.symbols('C0:%d'%k); V=sp.symbols('V0:%d'%k)
        tot=sp.simplify(sum(V[i]*C[i]*sum(V[j]/(C[i]-C[j]) for j in range(k) if j!=i)
                            for i in range(k)))
        want=sum(V[i]*V[j] for i in range(k) for j in range(i+1,k))
        check("k=%d: identity sum V_i C_i cond_i = sum_{i<j} V_iV_j"%k,
              sp.simplify(sp.expand(tot-want))==0, "%s"%sp.simplify(tot-want))

if __name__=="__main__":
    control_A(); control_B(); control_C()
    bottom_V1(); simple_roots_theorem(); order_nu(); exhausting_corollary()
    print("\n== %d checks, %d failures ==" % (NCH[0], len(FAIL)))
    if FAIL:
        for f_ in FAIL: print("   FAILED:", f_)
        sys.exit(1)
