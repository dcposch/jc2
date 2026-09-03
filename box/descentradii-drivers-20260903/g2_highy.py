#!/usr/bin/env python3
"""G2 cheapest slice: high-y coefficients of J(f,g) under the Moh expansion
with h = y(y-x)^4 + poly_y.  Force them to vanish; see what remains.
"""
import sympy as sp

x, y = sp.symbols('x y')
b0,b1,b2,b3,b4 = sp.symbols('b0:5')
p,q,r,s = sp.symbols('p q r s')
c = sp.symbols('c')

h = sp.expand(y*(y-x)**4 + b4*y**4 + b3*y**3 + b2*y**2 + b1*y + b0)
A = sp.expand((h - b0)/y)
beta = sp.expand(p*A + q*y + r*x + s)
qdiv, rdiv = sp.div(sp.Poly(sp.expand(beta**2), y), sp.Poly(h, y), y)
alpha = sp.expand(qdiv.as_expr())
f = sp.expand(h**2 + 2*beta)
g = sp.expand(h**3 + 3*beta*h + sp.Rational(3, 2)*alpha)

J = sp.expand(sp.diff(f, x)*sp.diff(g, y) - sp.diff(f, y)*sp.diff(g, x))
PJ = sp.Poly(J, y)
print("deg_y J", PJ.degree())
eqs = []
for d in range(PJ.degree(), -1, -1):
    co = sp.expand(PJ.coeff_monomial(y**d))
    if co == 0:
        print("  y^%d : 0" % d)
        continue
    # as polynomial in x
    cx = sp.Poly(co, x)
    print("  y^%d : deg_x=%s nterms=%d  %s" %
          (d, cx.degree(), len(cx.terms()), str(sp.factor(co))[:160]))
    for t in cx.coeffs():
        e = sp.expand(t)
        if e != 0:
            eqs.append(e)

print("\n#eqs from all y-coeffs as identities in x:", len(eqs))
# unique
ue = []
seen=set()
for e in eqs:
    k=str(e)
    if k not in seen:
        seen.add(k); ue.append(e)
print("unique", len(ue))

# Solve the highest few first
print("\n-- successive elimination from the top --")
vars_ = [b0,b1,b2,b3,b4,p,q,r,s,c]
acc = []
for d in range(PJ.degree(), PJ.degree()-8, -1):
    co = sp.expand(PJ.coeff_monomial(y**d))
    if co == 0:
        continue
    cx = sp.Poly(sp.expand(co.subs({v: val for v,val in acc})), x) if acc else sp.Poly(co, x)
    neweq = [sp.expand(t) for t in cx.coeffs() if sp.expand(t) != 0]
    print("  after subst, y^%d -> %d eqs" % (d, len(neweq)))
    if not neweq:
        continue
    # try solve
    try:
        sol = sp.solve(neweq, vars_, dict=True)
        print("    solve -> %d solutions" % len(sol), sol[:4] if sol else None)
        if len(sol)==1:
            acc = list(sol[0].items())
            print("    accumulated", acc)
    except Exception as e:
        print("    solve failed:", e)
        # groebner of accumulated + neweq
        G = sp.groebner(neweq, *vars_, order='lex')
        print("    lex groebner size", len(list(G)), " first", list(G)[:6])
        break
