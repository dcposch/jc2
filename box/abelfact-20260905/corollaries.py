import sympy as sp
x, y, b, B, eta, d = sp.symbols('x y b B eta d')

def data(t):
    w = sp.symbols('w0:%d' % (2*t+2)); c = sp.symbols('c0:%d' % (t-1))
    W = sum(w[i]*x**i for i in range(2*t+2))
    C = sum(c[i]*x**i for i in range(t-1)) + x**(t-1)
    r = b**2/4; K = x**2*C - y*b; M = K + y*b
    Phi = x*W - r
    Lam = 2*x*sp.diff(Phi,x) - 3*Phi + 3*K*M/(2*y**2) - B*x
    Gee = (3*K**3*(K+2*b*y)/(16*y**4) - 3*B*x*K**2/(4*y**2)
           - b*eta*x**2*K/(2*y) - B*eta*x**3)
    return W,C,K,M,Phi,Lam,Gee,w,c

print("=== COR 1:  Gee mod K  ==  -B*eta*x^3   (so K | Gee  <=>  B*eta = 0)")
for t in (2,3,4,5):
    _,_,K,_,_,_,Gee,_,_ = data(t)
    q,rem = sp.div(sp.Poly(sp.expand(Gee),x), sp.Poly(sp.expand(K),x))
    print("  t=%d :  Gee mod K + B*eta*x^3 = %s" % (t, sp.simplify(rem.as_expr() + B*eta*x**3)))

print()
print("=== COR 2:  Res(K,Phi)*Res(K,Lam) = -(B*eta)^(t+1) * b^3 * y^3")
print("    (consequence of Phi*Lam = Gee and COR 1; checked on random integer data)")
import random
random.seed(11)
for t in (2,3,4):
    W,C,K,M,Phi,Lam,Gee,w,c = data(t)
    for trial in range(2):
        sub = {y: random.randint(2,7), b: random.randint(2,7),
               B: random.randint(-6,6), eta: random.randint(-6,6)}
        for s in list(w)+list(c): sub[s] = random.randint(-5,5)
        Kp = sp.Poly(sp.expand(K.subs(sub)), x)
        Pp = sp.Poly(sp.expand(Phi.subs(sub)), x)
        Lp = sp.Poly(sp.expand(Lam.subs(sub)), x)
        lhs = sp.resultant(Kp,Pp)*sp.resultant(Kp,Lp)
        rhs = -(sub[B]*sub[eta])**(t+1) * sub[b]**3 * sub[y]**3
        print("  t=%d trial %d : lhs-rhs = %s" % (t, trial, sp.nsimplify(lhs-rhs)))

print()
print("=== COR 3: top coefficient of (F3') <=> 3 d^2 = t+1")
tt = sp.symbols('t', positive=True)
omega = 3*(2*d-1)/(4*y**2*(4*tt+1))
lc_lhs = (4*tt+1)*omega**2 + 3*omega/(2*y**2)     # lc(Phi*Lam)
lc_rhs = sp.Rational(3,16)/y**4                    # lc(Gee)
rel = sp.simplify(sp.factor(sp.numer(sp.together(lc_lhs - lc_rhs))))
print("  numer(lc(Phi*Lam) - lc(Gee)) =", rel)
print("  solve for t :", sp.solve(sp.Eq(lc_lhs, lc_rhs), tt))
