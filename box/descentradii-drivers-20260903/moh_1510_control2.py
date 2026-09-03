#!/usr/bin/env python3
"""M2-DESCENT (3-control, corrected): Moh Appendix II pp.210-211, case
n=15,m=10,M_2=11,V_2=3, Jacobian X^2 -- with the printed gamma audited."""
import sympy as sp
x, y = sp.symbols('x y')
a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12 = A_ = sp.symbols('a1:13')

B = (y**2 - x**2 + a1*y + a2*x + a3)*y + (a4*x + a5)
A = sp.expand(B*y + (a6*x + a7))
h = sp.expand(A*y + a8)
beta = sp.expand(a9*A + a10*y + a11*x + a12)
q, r = sp.div(sp.Poly(sp.expand(beta**2), y), sp.Poly(h, y), y)
alpha, gamma = sp.expand(q.as_expr()), sp.expand(r.as_expr())

bracket = (a9**2*a6 + 2*a9*a11)*x + (a9**2*a7 + 2*a9*a12)
print("== AUDIT of the printed gamma (p.211) ==")
for lab, cand in [("printed  (coefficient of B = -a9^2*a10)", -a9**2*a10),
                  ("audited  (coefficient of B = -a9^2*a8 )", -a9**2*a8)]:
    g_try = sp.expand(bracket*A + cand*B + (a10*y+a11*x+a12)**2 - 2*a8*a9*a10)
    print("   %s : gamma reproduced = %s" % (lab, sp.expand(gamma - g_try) == 0))
print("   printed alpha = a9^2 B + 2 a9 a10 reproduced :",
      sp.expand(alpha - (a9**2*B + 2*a9*a10)) == 0)

# ---- (7) deg_y gamma <= 2 : split the y^4,y^3 coefficients in x -----------
Pg = sp.Poly(gamma, y)
eqs = []
for d in (4, 3):
    c = sp.Poly(sp.expand(Pg.coeff_monomial(y**d)), x)
    eqs += [sp.expand(t) for t in c.all_coeffs() if sp.expand(t) != 0]
eqs = sorted(set([sp.factor(e) for e in eqs]), key=str)
print("\n== (7) => the equations (each an identity in x) ==")
for e in eqs: print("    ", e, "= 0")

# ---- Case 1 : a9 = 0 ------------------------------------------------------
print("\n== Case 1 : a9 = 0 ==")
s = {a9: 0}
be, ga = sp.expand(beta.subs(s)), sp.expand(gamma.subs(s))
print("   alpha =", sp.expand(alpha.subs(s)), " ; beta =", be, " ; gamma - beta^2 =", sp.expand(ga-be**2))
print("   deg_y beta^3 =", sp.degree(sp.Poly(sp.expand(be**3), y), y), " < 5 = deg_y h")
print("   => in (3) beta^3 = (3gamma+a)h^2 + eps h + delta we must have 3gamma+a=0 and eps=0,")
print("      so gamma is the constant -a/3, i.e. a10=a11=0;  but (4) needs (1/2)eps = b f^{2/5}+...")
print("      with b != 0, i.e. deg_y eps = 4.   CONTRADICTION.        [Moh's Case 1, reproduced]")

# ---- Case 2 : a9 != 0 -----------------------------------------------------
print("\n== Case 2 : a9 != 0  =>  a8 = 0 , a6 = -2a11/a9 , a7 = -2a12/a9  (audited form) ==")
s2 = {a8: 0, a6: -2*a11/a9, a7: -2*a12/a9}
ga2 = sp.expand(sp.together(gamma.subs(s2)).simplify())
be2 = sp.expand(beta.subs(s2)); h2 = sp.expand(h.subs(s2))
print("   gamma =", sp.factor(ga2), "  deg_y gamma =", sp.degree(sp.Poly(ga2,y),y))
print("   (Moh printed 'a10 = 0, gamma = (a11 x + a12)^2, deg_y gamma = 0' -> the audited")
print("    equations give a8 = 0 instead of a10 = 0, and gamma = (a10 y + a11 x + a12)^2")
print("    which HAS y-degree 2 when a10 != 0: Moh's stated contradiction does not close here.)")
b3 = sp.expand(be2**3)
q2, r2 = sp.div(sp.Poly(b3, y), sp.Poly(sp.expand(h2**2), y), y)
c2 = sp.expand(q2.as_expr())
print("\n   h^2-coefficient of beta^3 :  deg_y =", sp.degree(sp.Poly(c2,y),y),
      ", deg_x =", sp.degree(sp.Poly(c2,x),x))
res = sp.expand(c2 - 3*ga2)
Pr = sp.Poly(res, x, y)
print("   (3) requires  c2 - 3*gamma = a  in k  =>  every non-constant monomial vanishes.")
mons = [(mo, sp.factor(co)) for mo, co in zip(Pr.monoms(), Pr.coeffs()) if mo != (0,0)]
print("   number of resulting equations:", len(mons))
for mo, co in mons[:14]:
    print("      x^%d y^%d :  %s = 0" % (mo[0], mo[1], co))
if len(mons) > 14: print("      ... (%d more)" % (len(mons)-14))
sysm = [sp.expand(sp.numer(sp.together(co))) for _, co in mons]
Gb = sp.groebner(sysm + [sp.Symbol('T')*a9 - 1], *(list(A_)+[sp.Symbol('T')]), order='lex')
print("\n   saturated Groebner basis at a9 != 0 :", "EMPTY (1 in ideal)" if list(Gb) == [1] else "non-trivial")
if list(Gb) != [1]:
    print("   basis size", len(list(Gb)), " first elements:", [sp.factor(t) for t in list(Gb)[:6]])
