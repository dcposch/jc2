import sympy as sp
x,y = sp.symbols('x y')
a,b,c,d,e0 = sp.symbols('a b c d e0')

def J(P,Qq):
    return sp.expand(sp.diff(P,x)*sp.diff(Qq,y) - sp.diff(P,y)*sp.diff(Qq,x))

print("=== (A) chain rule J(Phi(F,G),G) = Phi_u(F,G)*J(F,G), generic F,G, symbolic Phi ===")
u,v = sp.symbols('u v')
# (99,66) shape: n1=3, m1=2
Phi = v**3 - u**2 + a*v**2 + b*u*v + c*u + d*v + e0
Phi_u = sp.diff(Phi,u)
import random
random.seed(7)
for trial in range(3):
    F = sum(random.randint(-4,4)*x**i*y**j for i in range(4) for j in range(4))
    G = sum(random.randint(-4,4)*x**i*y**j for i in range(4) for j in range(4))
    Q = sp.expand(Phi.subs({u:F, v:G}, simultaneous=True))
    lhs = J(Q,G)
    rhs = sp.expand(Phi_u.subs({u:F,v:G}, simultaneous=True)*J(F,G))
    print("  trial",trial,"chain-rule residual =", sp.simplify(sp.expand(lhs-rhs)))

print()
print("=== (B) general m1: J^{(k)}(Q,G) = d^k Phi/du^k (F,G) when J(F,G)=1 ===")
# Keller pair with J=1: F=x, G=y+x^2   (n=1,m=2 -> n1=1,m1=2)
def iterJ(P,G,k):
    for _ in range(k): P = J(P,G)
    return P
tests = []
# m1=2 instance
F2, G2 = x, y+x**2
tests.append(("m1=2  (F,G)=(x, y+x^2)", F2, G2, 1, 2))
# m1=3 instance: n1=1,m1=3 ; F=x, G=y+x^3
tests.append(("m1=3  (F,G)=(x, y+x^3)", x, y+x**3, 1, 3))
# m1=4
tests.append(("m1=4  (F,G)=(x, y+x^4)", x, y+x**4, 1, 4))
# a genuinely composed tame pair, m1=2 : F=x+y^3 (n=3), G=y (m=1)? -> m1=1. use swap
# F = x, G = y + x^2 composed with shear: F'=x+ (y+x^2)*0 ... keep simple; add nontrivial one:
tests.append(("m1=2  (F,G)=(x+7*y, y+ (x+7*y)^2)", x+7*y, y+(x+7*y)**2, 1, 2))
for name,F,G,n1,m1 in tests:
    assert sp.expand(J(F,G))==1, (name, J(F,G))
    n = sp.Poly(F,x,y).total_degree(); m = sp.Poly(G,x,y).total_degree()
    # build generic Phi of the licensed shape: v^n1 - u^m1 + sum{u^i v^j : n*i+m*j < n1*m, j<n1}
    coeffs={}
    Phi = v**n1 - u**m1
    for i in range(0,m1):
        for j in range(0,n1):
            if n*i+m*j < n1*m:
                s = sp.Symbol('k_%d_%d'%(i,j)); coeffs[(i,j)]=s
                Phi = Phi + s*u**i*v**j
    Q = sp.expand(Phi.subs({u:F,v:G},simultaneous=True))
    ok=True
    for k in range(1,m1+1):
        lhs = iterJ(Q,G,k)
        rhs = sp.expand(sp.diff(Phi,u,k).subs({u:F,v:G},simultaneous=True))
        r = sp.simplify(sp.expand(lhs-rhs))
        if r!=0: ok=False; print("   MISMATCH k=",k,r)
    top = sp.simplify(iterJ(Q,G,m1))
    # (E1)-general: F from the (m1-1)-fold iterate
    Cg = sum(coeffs.get((m1-1,j),0)*G**j for j in range(n1))
    Frec = sp.expand((sp.factorial(m1-1)*Cg - iterJ(Q,G,m1-1))/sp.factorial(m1))
    print("  %-40s n=%d m=%d  iterJ^k=d_u^k Phi: %s   J^{(m1)}(Q,G)=%s (want %s)   F-recovery residual=%s"
          %(name,n,m,ok,top,-sp.factorial(m1), sp.simplify(sp.expand(Frec-F))))
