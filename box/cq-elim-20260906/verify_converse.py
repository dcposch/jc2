import sympy as sp
x,y,u,v = sp.symbols('x y u v')
bb,cc,gg = sp.symbols('bb cc gg')
def J(P,Qq): return sp.expand(sp.diff(P,x)*sp.diff(Qq,y)-sp.diff(P,y)*sp.diff(Qq,x))

print("=== (C) the literal biconditional 'J(F,G)=1 <=> J(J(Q,G),G)=-2' : COUNTEREXAMPLE at J=-1 ===")
# n1=1, m1=2 shape: Phi = v - u^2 + bb*u + gg  (j<n1=1 so no uv/v terms)
F, G = -x, y+x**2                 # J(F,G) = -1
Phi = v - u**2 + bb*u + gg
Q  = sp.expand(Phi.subs({u:F,v:G},simultaneous=True))
print("  F=-x, G=y+x^2 :  J(F,G) =", J(F,G))
print("  Q = Phi(F,G)  =", Q)
print("  J(Q,G)        =", J(Q,G))
print("  J(J(Q,G),G)   =", sp.simplify(J(J(Q,G),G)), "  <-- equals -2 while J(F,G) = -1")
E1rhs = sp.expand((0*G + bb - J(Q,G))/2)
print("  (E1) rhs (b*G+c-J(Q,G))/2 =", E1rhs, " vs F =", F, "  ->  (E1) FAILS, as it must")

print()
print("=== (D) chart direction: F DEFINED by (E1) ==> J(F,G) = -(1/2)*J(J(Q,G),G) identically ===")
import random; random.seed(11)
for t in range(4):
    Qr = sum(random.randint(-3,3)*x**i*y**j for i in range(4) for j in range(4))
    Gr = sum(random.randint(-3,3)*x**i*y**j for i in range(4) for j in range(4))
    Fdef = sp.expand((bb*Gr + cc - J(Qr,Gr))/2)
    lhs = J(Fdef,Gr); rhs = sp.expand(sp.Rational(-1,2)*J(J(Qr,Gr),Gr))
    print("   trial",t," J(F_def,G) + (1/2)J(J(Q,G),G)  =", sp.simplify(sp.expand(lhs-rhs)))

print()
print("=== (E) the RELAXATION GAP: with F defined by (E1) and (E2) imposed, R := Q - Phi(F,G) obeys J(R,G)=0 ===")
a_,b_,c_,d_,e_ = sp.symbols('a_ b_ c_ d_ e_')
# take a real Keller pair with n1=3,m1=2 shape unavailable (automorphisms have min(n1,m1)=1);
# use n1=1,m1=2 and verify J(R,G)=0 symbolically for a PERTURBED Q  (Q -> Q + rho(G))
F0,G0 = x, y+x**2
Phi0 = v - u**2 + bb*u + gg
rho = sp.Symbol('rho')
Q0  = sp.expand(Phi0.subs({u:F0,v:G0},simultaneous=True))
Qp  = sp.expand(Q0 + rho*G0**2)         # add an arbitrary element of k[G]: still satisfies (E2)?
Fp  = sp.expand((0*G0 + bb - J(Qp,G0))/2)
print("  perturbed Q by rho*G^2:  J(J(Qp,G),G) =", sp.simplify(J(J(Qp,G0),G0)), " (still -2 -> (E2) holds)")
print("  F recovered            =", sp.expand(Fp), "  (differs from F=x by an element of k[G]? ->", sp.simplify(sp.expand(Fp-F0)),")")
R = sp.expand(Qp - Phi0.subs({u:Fp,v:G0},simultaneous=True))
print("  R = Qp - Phi(F_rec,G)  ->  J(R,G) =", sp.simplify(J(R,G0)), " (0 confirms R in ker J(.,G))")
