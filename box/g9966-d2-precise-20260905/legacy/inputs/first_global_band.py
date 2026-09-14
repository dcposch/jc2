#!/usr/bin/env python3
"""Exact-Q first global-band probe for the (99,66) triangular chart.

Scope: six pole-end coefficient rows (three for F, three for G) and the first
ten contiguous degree-162 Jacobian coefficients, through the first G65 term.
This is deliberately not a full-tower or full-Jacobian computation.
"""
import json
import sympy as s

x, y, t, ss = s.symbols("x y t ss")
u, z, v, pi = s.symbols("u z v pi")

# Named chart coordinates needed in the first three x-axis coefficients.
h10, c2210, c3320, c3310 = s.symbols("H_10_0 C2_21_0 C3_32_0 C3_31_0")
a2980, a3970, a3960 = s.symbols("A3_98_0 A3_97_0 A3_96_0")
a2650, a2640 = s.symbols("A2_65_0 A2_64_0")
b2650, b2640, b2630 = s.symbols("B2_65_0 B2_64_0 B2_63_0")
b1320, b1310 = s.symbols("B1_32_0 B1_31_0")
a3971, b2641 = s.symbols("A3_97_1 B2_64_1")
d32 = c3320
d31 = c3310 + c2210*h10

# Direct minor pole-end rows, mechanically rechecked in a sparse tail ring.
Faxis = [a2980,
         a3970 + a2650*d32,
         a3960 + a2640*d32 + a2650*d31 + d32**3]
Gaxis = [b2650,
         b2640 + b1320*d32 + d32**2,
         b2630 + b1310*d32 + b1320*d31 + 2*d32*d31]
# The fixed tops P^9 and P^6 have y-orders 27 and 18, hence the possible
# F_(98,1),G_(65,1) terms vanish.  At the third row the surviving off-axis
# incidences pull back as F_(97,1)=A3_(97,1), G_(64,1)=B2_(64,1).
Frows = [Faxis[0], Faxis[1], Faxis[2] + u*a3971]
Grows = [Gaxis[0], Gaxis[1], Gaxis[2] + u*b2641]
ht = d32*x**32 + d31*x**31
A2t = a2650*x**65 + a2640*x**64
A3t = a2980*x**98 + a3970*x**97 + a3960*x**96
B1t = b1320*x**32 + b1310*x**31
B2t = b2650*x**65 + b2640*x**64 + b2630*x**63
Ft = s.Poly(ht**3 + A2t*ht + A3t, x)
Gt = s.Poly(ht**2 + B1t*ht + B2t, x)
assert all(s.expand(a-b)==0 for a,b in zip(Faxis,[Ft.coeff_monomial(x**k) for k in (98,97,96)]))
assert all(s.expand(a-b)==0 for a,b in zip(Gaxis,[Gt.coeff_monomial(x**k) for k in (65,64,63)]))

# Independent Poly.coeff_monomial check of the local substitution incidence.
f980,f970,f960,f981,f971 = s.symbols("f_98_0 f_97_0 f_96_0 f_98_1 f_97_1")
g650,g640,g630,g651,g641 = s.symbols("g_65_0 g_64_0 g_63_0 g_65_1 g_64_1")
Ffrag=f980*x**98+f970*x**97+f960*x**96+f981*x**98*y+f971*x**97*y
Gfrag=g650*x**65+g640*x**64+g630*x**63+g651*x**65*y+g641*x**64*y
Ad2=s.Poly(s.expand(t**98*Ffrag.subs({x:t**-1,y:u*t+z*t**2})),t)
Bd2=s.Poly(s.expand(t**65*Gfrag.subs({x:t**-1,y:u*t+z*t**2})),t)
assert [Ad2.coeff_monomial(t**k) for k in range(3)] == [f980,f970+u*f981,f960+u*f971+z*f981]
assert [Bd2.coeff_monomial(t**k) for k in range(3)] == [g650,g640+u*g651,g630+u*g641+z*g651]
Ad52=s.Poly(s.expand(ss**196*Ffrag.subs({x:ss**-2,y:u*ss**2+v*ss**4+pi*ss**5})),ss)
Bd52=s.Poly(s.expand(ss**130*Gfrag.subs({x:ss**-2,y:u*ss**2+v*ss**4+pi*ss**5})),ss)
assert [Ad52.coeff_monomial(ss**k) for k in (0,2,4)] == [f980,f970+u*f981,f960+u*f971+v*f981]
assert [Bd52.coeff_monomial(ss**k) for k in (0,2,4)] == [g650,g640+u*g651,g630+u*g641+v*g651]

# Exact first top/lower Jacobian layer: J(F_98,P^6)+J(P^9,G_65).
P = y**3*(y-x)**8
fv = s.symbols("f0:10")
g0 = s.symbols("g0")
F98 = sum(fv[j]*x**(98-j)*y**j for j in range(10))
G65 = g0*x**65
F99, G66 = s.expand(P**9), s.expand(P**6)
assert s.Poly(F99,x,y).coeff_monomial(x**98*y)==0
assert s.Poly(G66,x,y).coeff_monomial(x**65*y)==0
J162 = s.Poly(s.diff(F98,x)*s.diff(G66,y)-s.diff(F98,y)*s.diff(G66,x)
              +s.diff(F99,x)*s.diff(G65,y)-s.diff(F99,y)*s.diff(G65,x), x,y)
jraw = [s.expand(J162.coeff_monomial(x**(162-k)*y**k)) for k in range(17,27)]
j_first, j_gfirst = jraw[0], jraw[-1]
assert j_first == 1764*fv[0]

# Ring map from homogeneous coefficients to triangular-chart coordinates.
# For y-degrees 0..8 only A3 contributes. At y-degree 9, A2_65*P^3
# contributes because [x^24 y^9]P^3=1.
a3face = (a3971,) + s.symbols("A3_96_2 A3_95_3 A3_94_4 A3_93_5 A3_92_6 A3_91_7 A3_90_8 A3_89_9")
ringmap = {fv[0]:a2980, g0:b2650}
for j in range(1,9): ringmap[fv[j]] = a3face[j-1]
ringmap[fv[9]] = a3face[8] + a2650
j1_chart = s.expand(j_first.subs(ringmap))
j2_chart = s.expand(j_gfirst.subs(ringmap))
jchart = [s.expand(q.subs(ringmap)) for q in jraw]

# Sequential exact-Q Gaussian elimination with explicit requested pivot order.
rows = Frows + Grows + jchart
pivot_order = [a2980,a3970,a3960,b2650,b2640,b2630] + list(a3face[:8]) + [a2650,a3face[8]]
solutions, statuses = {}, []
for idx,row in enumerate(rows):
    r = s.cancel(s.expand(row.subs(solutions)))
    chosen = None
    for pivot_var in pivot_order:
        if pivot_var in solutions or not r.has(pivot_var): continue
        p = s.Poly(r,pivot_var)
        if p.degree()==1 and not p.coeff_monomial(pivot_var).has(*pivot_order):
            q = s.expand(p.coeff_monomial(pivot_var))
            rem = s.expand(p.coeff_monomial(1))
            solutions[pivot_var] = s.cancel(-rem/q)
            chosen=(str(pivot_var),str(q)); break
    if chosen: statuses.append({"row":idx+1,"status":"pivot","pivot":chosen[0],"coefficient":chosen[1]})
    elif r==0: statuses.append({"row":idx+1,"status":"dependent_zero"})
    else: statuses.append({"row":idx+1,"status":"residual","expression":str(r)})

assert len(solutions)==15
assert statuses[6]["status"]=="dependent_zero"
assert statuses[7]["status"]=="pivot" and statuses[7]["pivot"]==str(a3971)
assert statuses[15]["status"]=="pivot" and statuses[15]["pivot"]==str(a2650)
def fully_reduce(expr):
    old = s.expand(expr)
    for _ in range(12):
        new = s.cancel(s.expand(old.subs(solutions)))
        if new == old: return new
        old = new
    return old
assert all(fully_reduce(r)==0 for r in rows)

# Controls: adding 1 to a fully reduced duplicate is inconsistent; deleting
# the final Jacobian row removes its one new pivot.  The all-zero assignment is
# an exact point of this prefix (the localized centre parameters do not occur).
negative_control = fully_reduce(j1_chart+1)
assert negative_control == 1
drop_last_j_rank = len(solutions)-1
assert drop_last_j_rank == 14 and statuses[-1]["status"] == "pivot"
prefix_symbols = set().union(*(row.free_symbols for row in rows))
zero_point = {symbol:s.Integer(0) for symbol in prefix_symbols}
assert all(s.expand(row.subs(zero_point)) == 0 for row in rows)

def ss(z): return str(s.expand(z))
out = {
 "scope":"global triangular-chart first band only; not full tower/global Keller pair",
 "field":"Q", "chart_d32":ss(d32), "chart_d31":ss(d31),
 "direct_rows":{"F":[ss(z) for z in Frows],"G":[ss(z) for z in Grows]},
 "generic_original_incidence":{"delta2_F":[str(f980),str(f970+u*f981),str(f960+u*f971+z*f981)],
   "delta2_G":[str(g650),str(g640+u*g651),str(g630+u*g641+z*g651)],
   "delta52_F":[str(f980),str(f970+u*f981),str(f960+u*f971+v*f981)],
   "delta52_G":[str(g650),str(g640+u*g651),str(g630+u*g641+v*g651)],
   "fixed_top_map":{str(f981):"0",str(g651):"0"}},
 "branch_exponents":{"delta2":{"F":[-80,-79,-78],"G":[-53,-52,-51]},
                     "delta52":{"F":[-187,-185,-183],"G":[-124,-122,-120]}},
 "jacobian_degree162":{"contiguous_monomials":["x^%d*y^%d"%(162-k,k) for k in range(17,27)],
   "rows":[ss(q) for q in jchart],"first_row_monomial":"x^145*y^17","first_row":ss(j1_chart),
   "first_G65_row_monomial":"x^136*y^26","first_G65_row":ss(j2_chart)},
 "elimination":statuses,"rank_type":"exact Q*-triangular pivot count",
 "rank":{"direct":6,"plus_first_1_J":6,"plus_first_2_J":7,
         "plus_first_3_J":8,"plus_first_10_J_through_G65":15},
 "compatible":True,"residual_count":0,
 "controls":{"all_rows_reduce_zero":True,"all_zero_prefix_point":True,
             "drop_last_J_rank":drop_last_j_rank,
             "perturbed_duplicate_residual":ss(negative_control)},
 "next_system":"Add the degree-162 Jacobian coordinate x^135*y^27 and pole rows F_95/G_62, then intersect with unresolved outer-F/G D1 rows in this same chart."
}
print(json.dumps(out,indent=2,sort_keys=True))
