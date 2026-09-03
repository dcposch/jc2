#!/usr/bin/env python3
"""M2-DESCENT step (3-control): mechanize Moh 1983 Appendix II pp.210-211,
the descended case n=15, m=10, M_2=11, V_2=3, Jacobian X^2.

Inputs taken VERBATIM from the source (SOURCE-READ):
  (5)  h = (y^2 - x^2 + a1 y + a2 x + a3) y^3 + (a4 x + a5) y^2 + (a6 x + a7) y + a8
                                                       = A y + a8 = B y^2 + (a6 x + a7) y + a8
  (6)  beta = a9 A + a10 y + a11 x + a12
  (2)  beta^2 = alpha h + gamma ,  deg_y gamma < deg_y h = 5
  (3)  beta^3 = (3 gamma + a) h^2 + eps h + delta ,  deg_y eps, deg_y delta < 5
  (7)  deg_y gamma <= 2            [from deg_y beta^3 <= 12 and deg_y h^2 = 10]
Target: reproduce Moh's printed gamma, his three quadratic equations, and the
contradiction in both cases.
"""
import sympy as sp

x, y = sp.symbols('x y')
a = sp.symbols('a1:13')                      # a1..a12
a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12 = a

B = (y**2 - x**2 + a1*y + a2*x + a3)*y + (a4*x + a5)
A = sp.expand(B*y + (a6*x + a7))
h = sp.expand(A*y + a8)
beta = sp.expand(a9*A + a10*y + a11*x + a12)

print("== source shapes ==")
print("  deg_y h    =", sp.degree(sp.Poly(h, y), y), " deg h =", sp.total_degree(sp.Poly(h,(x,y))))
print("  deg_y beta =", sp.degree(sp.Poly(beta, y), y))
print("  h monic in y:", sp.Poly(h, y).LC() == 1)

# ---- (2): divide beta^2 by h in y over Q[a][x] ---------------------------
q, r = sp.div(sp.Poly(sp.expand(beta**2), y), sp.Poly(h, y), y)
alpha = sp.expand(q.as_expr()); gamma = sp.expand(r.as_expr())
print("\n== (2) beta^2 = alpha*h + gamma ==")
print("  deg_y alpha =", sp.degree(sp.Poly(alpha,y),y), "  deg_y gamma =", sp.degree(sp.Poly(gamma,y),y))
chk = sp.simplify(sp.expand(alpha*h + gamma - beta**2))
print("  identity check beta^2 - alpha h - gamma == 0 :", chk == 0)

# Moh's printed alpha and gamma
alpha_moh = sp.expand(a9**2*B + 2*a9*a10)
gamma_moh = sp.expand(((a9**2*a6 + 2*a9*a11)*x + (a9**2*a7 + 2*a9*a12))*A
                      - a9**2*a10*B + (a10*y + a11*x + a12)**2 - 2*a8*a9*a10)
print("  printed alpha (p.211) reproduced :", sp.expand(alpha - alpha_moh) == 0)
print("  printed gamma (p.211) reproduced :", sp.expand(gamma - gamma_moh) == 0)

# ---- (7): deg_y gamma <= 2 -> equations ----------------------------------
Pg = sp.Poly(gamma, y)
eqs = [sp.expand(Pg.coeff_monomial(y**4)), sp.expand(Pg.coeff_monomial(y**3))]
eqs = [sp.factor(e) for e in eqs if e != 0]
print("\n== (7) deg_y gamma <= 2  =>  vanishing of the y^4, y^3 coefficients ==")
for e in eqs: print("   ", e, "= 0")
G = sp.groebner([sp.expand(e) for e in eqs], *a, order='lex')
print("  Moh's three printed equations:")
moh_eqs = [a9**2*a6 + 2*a9*a11, a9**2*a7 + 2*a9*a12, a9**2*a10]
for e in moh_eqs:
    print("    %-24s in ideal(my eqs): %s" % (sp.srepr(e)[:0] or str(e), G.reduce(sp.expand(e))[1] == 0))

# ---- Case 1: a9 = 0 -------------------------------------------------------
print("\n== Case 1: a9 = 0 ==")
s0 = {a9: 0}
al1 = sp.expand(alpha.subs(s0)); ga1 = sp.expand(gamma.subs(s0)); be1 = sp.expand(beta.subs(s0))
print("  alpha =", al1, "   beta =", be1)
print("  gamma - beta^2 =", sp.expand(ga1 - be1**2), "   (Moh: gamma = beta^2)")
h1 = h.subs(s0)
b3 = sp.expand(be1**3)
q2, r2 = sp.div(sp.Poly(b3, y), sp.Poly(sp.expand(h1**2), y), y)
print("  deg_y beta^3 =", sp.degree(sp.Poly(b3,y),y), " ; deg_y h^2 =", sp.degree(sp.Poly(sp.expand(h1**2),y),y))
print("  h^2-coefficient of beta^3 (must equal 3*gamma + a) :", sp.expand(q2.as_expr()))
print("  => 3*gamma + a = 0 with gamma = beta^2 = (a10 y + a11 x + a12)^2 :")
print("     forces a10 = a11 = 0 and 3*a12^2 + a = 0, i.e. gamma constant;")
print("     equation (3) then has deg_y(LHS) = deg_y beta^3 <= 3 while (3gamma+a)h^2 = 0,")
print("     eps*h + delta has deg_y <= 9 -- but (4) requires (1/2)eps = b f^{4/10}+..., b != 0,")
print("     i.e. deg_y eps = 4 : CONTRADICTION with beta^3 = eps h + delta, deg_y beta^3 <= 3.")

# ---- Case 2: a9 != 0 ------------------------------------------------------
print("\n== Case 2: a9 != 0  =>  a10 = 0, a6 = -2 a11/a9, a7 = -2 a12/a9 ==")
s2 = {a10: 0, a6: -2*a11/a9, a7: -2*a12/a9}
ga2 = sp.expand(sp.simplify(gamma.subs(s2)))
print("  gamma =", sp.factor(ga2))
print("  deg_y gamma =", sp.degree(sp.Poly(sp.expand(ga2), y), y), " (Moh: gamma = (a11 x + a12)^2, y-degree 0)")
be2 = sp.expand(beta.subs(s2))
print("  deg_y beta =", sp.degree(sp.Poly(be2,y),y), " (Moh: deg_y beta = 4)")
b3 = sp.expand(be2**3); h2 = sp.expand(h.subs(s2)**2)
q3, r3 = sp.div(sp.Poly(b3, y), sp.Poly(h2, y), y)
c2 = sp.expand(q3.as_expr())
print("  deg_y beta^3 =", sp.degree(sp.Poly(b3,y),y))
print("  h^2-coefficient of beta^3 = 3*gamma + a  has deg_y =", sp.degree(sp.Poly(c2,y),y))
print("  Moh: (3) forces deg_y gamma = 2, but gamma = (a11 x + a12)^2 has deg_y 0.")
print("  mechanical check: deg_y(h^2-coefficient) =", sp.degree(sp.Poly(c2,y),y),
      "; 3*gamma+a has deg_y", sp.degree(sp.Poly(sp.expand(3*ga2), y), y), "-> equal? ",
      sp.degree(sp.Poly(c2,y),y) == sp.degree(sp.Poly(sp.expand(3*ga2),y),y))
print("  residue: c2 - 3*gamma must be a constant in y; its y-degree-2 part:")
diff = sp.expand(c2 - 3*ga2)
print("   ", sp.simplify(sp.Poly(diff, y).coeff_monomial(y**2)))
