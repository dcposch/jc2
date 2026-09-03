#!/usr/bin/env python3
"""M2-DESCENT (3-control): positive/negative controls on the saturation of §4.2."""
import sympy as sp
x, y = sp.symbols('x y'); T = sp.Symbol('T')
a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12 = A_ = sp.symbols('a1:13')
B = (y**2 - x**2 + a1*y + a2*x + a3)*y + (a4*x + a5)
A = sp.expand(B*y + (a6*x + a7)); h = sp.expand(A*y + a8)
beta = sp.expand(a9*A + a10*y + a11*x + a12)
q, r = sp.div(sp.Poly(sp.expand(beta**2), y), sp.Poly(h, y), y)
gamma = sp.expand(r.as_expr())
s2 = {a8: 0, a6: -2*a11/a9, a7: -2*a12/a9}
ga2 = sp.expand(sp.together(gamma.subs(s2)).simplify())
b3 = sp.expand(sp.expand(beta.subs(s2))**3); h2 = sp.expand(sp.expand(h.subs(s2))**2)
q2, _ = sp.div(sp.Poly(b3, y), sp.Poly(h2, y), y)
res = sp.expand(sp.expand(q2.as_expr()) - 3*ga2)
Pr = sp.Poly(res, x, y)
E = [(mo, sp.expand(sp.numer(sp.together(co)))) for mo, co in zip(Pr.monoms(), Pr.coeffs()) if mo != (0,0)]
print("equations:", [(mo, sp.factor(co)) for mo, co in E])
def sat(sys):
    G = sp.groebner(list(sys) + [T*a9 - 1], *(list(A_)+[T]), order='lex')
    return list(G)
full = sat([e for _, e in E])
print("\n  MAIN     : saturate all 5 at a9!=0 ->", "EMPTY  [1]" if full == [1] else "non-trivial (%d gens)" % len(full))
for drop in range(len(E)):
    sub = [e for i, (_, e) in enumerate(E) if i != drop]
    G = sat(sub)
    print("  POSITIVE : drop %-10s -> %s" % (str(E[drop][0]), "EMPTY [1]" if G == [1] else "NON-TRIVIAL (%d gens)" % len(G)))
# negative control: a random consistent system in the same ring must be non-trivial
G = sat([a9 - 1, a10 - 2, a11 - 3])
print("  NEGATIVE : consistent toy system a9=1,a10=2,a11=3 ->",
      "EMPTY [1] (BAD)" if G == [1] else "NON-TRIVIAL (%d gens)  [expected]" % len(G))
