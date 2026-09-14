#!/usr/bin/env python3
"""Closed form of the b-axis (monomial) stratum of (UF), symbolic in N.

On c=0 the weights force  L = u/y - b,  P = omega*u^2 + p1*b*u - b^2/4,  B = eta = 0,  u = x^N,
and theta = x d/dx acts on u^j by j*N.  (UF) <=> (theta-3)(P^2) + G*P = Rfree with G = (3/2)L(L+b).
Row u^3 fixes p1 (pivot lam(N) = 2 omega (3N+6d)); row u^2 is the axis residual e(N,d)*b^2 (= E_{2t}|axis);
rows u^1,u^0 must vanish identically.  We reduce with 3d^2=N, y=(d+N)/(2(2N-1)), omega=1/(4y^2(2d+1)).
"""
import sympy as sp, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
u, b, d, N, p1 = sp.symbols('u b d N p1')
y = (d+N)/(2*(2*N-1)); om = 1/(4*y**2*(2*d+1))
L = u/y - b
P = om*u**2 + p1*b*u - b**2/4
def theta(f):  # x d/dx on polynomials in u=x^N
    f = sp.expand(f); return sum(sp.Poly(f,u).coeff_monomial(u**j)*j*N*u**j for j in range(0,9))
G = sp.Rational(3,2)*L*(L+b)
Rf = sp.Rational(3,16)*L**2*(L*(L+2*b))          # B=eta=0
res = sp.expand(theta(P**2) - 3*P**2 + G*P - Rf)
rows = {j: sp.factor(sp.Poly(res,u).coeff_monomial(u**j)) for j in range(0,5)}
def redN(e):
    e = sp.together(sp.expand(e)); n, dd = sp.fraction(e)
    n = sp.expand(n.subs(N, 3*d**2)); dd = sp.expand(dd.subs(N, 3*d**2))
    return sp.factor(sp.cancel(n/dd))
out = {}
out['row_u4_top'] = str(redN(rows[4]))
sol = sp.solve(rows[3], p1)
assert len(sol)==1
p1s = sol[0]
out['p1_from_row_u3'] = str(redN(p1s))
e2 = redN(rows[2].subs(p1,p1s)/b**2)
out['axis_residual_e(N,d)=E_2t|axis/b^2'] = str(e2)
out['row_u1_after_p1'] = str(redN(rows[1].subs(p1,p1s)))
out['row_u0_after_p1'] = str(redN(rows[0].subs(p1,p1s)))
# zeros of e in d (with N=3d^2)
num = sp.numer(sp.together(e2))
out['numerator_factored_in_d'] = str(sp.factor(num))
out['numerator_roots_d'] = [str(r) for r in sp.solve(num, d)]
# t=2 controls: d=-1 (y=1/5) exceptional; d=+1 (y=2/5) residual -2 b^2 x^4 (Astra Sec.5)
for dv in (-1, 1):
    out[f'e_at_t2_d={dv}'] = str(sp.nsimplify(e2.subs(d, dv)))
# t=3..12 numeric on both embeddings
tab = {}
for t in range(2, 13):
    Nv = t+1; dv = sp.sqrt(sp.Rational(Nv,3))
    tab[t] = {'d=+': str(sp.nsimplify(sp.simplify(e2.subs(d, dv)))), 'd=-': str(sp.nsimplify(sp.simplify(e2.subs(d, -dv))))}
out['table_e_by_t'] = tab
(HERE/'monomial_family.json').write_text(json.dumps(out, indent=1)+'\n')
print(json.dumps(out, indent=1))
print('MONOMIAL_FAMILY_DONE')
