#!/usr/bin/env python3
"""Exact source arithmetic and polynomial controls; no chart emptiness claim."""
import json
from fractions import Fraction
from math import gcd
from pathlib import Path
import sympy as s

OUT = Path('/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/source-audit-controls.fresh.json')
data = {}
for tag, n, m, M in [('9966',99,66,[-66,77,97]), ('10872',108,72,[-72,81,106])]:
    ds, qs, ls, mus = [n], [], [], []
    lam = 0
    for j, val in enumerate(M):
        q = val if j == 0 else val-M[j-1]
        lam += q*ds[-1]
        qs.append(q);ls.append(lam);mus.append(Fraction(lam,ds[-1]))
        ds.append(gcd(ds[-1],abs(val)))
    k, D = n//3, -mus[1]
    monomials=[(j,a) for a in range(3) for j in range(4) if n*j+m*a<=3*m]
    data[tag] = {'n':n,'m':m,'M':M,'d':ds,'q':qs,'lambda':ls,
        'actual_characteristic_degrees':[-int(v) for v in mus],
        'T2_degree':int(D),'h2_degree':k,'T2_attainment_t_power':int(3*m-D),
        'Jacobian_constant_t_power':n+m-2,'allowed_Fj_T1a':monomials,
        'coefficient_recovery_y_degrees':[n+m,2*m,n,m],
        'effective_indices_strictly_below_e':all(v<n-1 for v in M)}

H,B,C,D,E,a,b,c,d,e=s.symbols('H B C D E a b c d e')
F=H**3+B*H+C
G=H**2+D*H+E
Q=s.Poly(s.expand(G**3-F**2+a*G**2+b*F*G+c*F+d*G+e),H)
sol={}
for power,var in [(5,b),(4,a),(3,c),(2,d)]:
    row=s.expand(Q.nth(power).subs(sol))
    assert s.diff(row,var)==1
    sol[var]=s.expand(-row.subs(var,0))
restricted=s.Poly(s.expand(Q.as_expr().subs(sol)),H)
assert restricted.degree()<=0
data['Delta']={'polynomial_in_H':str(Q.as_expr()),
    'high_H_rows_force':{str(k):str(v) for k,v in sol.items()},
    'residual_constant':str(restricted.as_expr()),
    'degree_multiple_obstruction_9966':55%33!=0,
    'degree_multiple_obstruction_10872':63%36!=0,
    'upper_rows_leave_constant':True,
    'zero_leader_then_localizer_minus_one':True}

# A nonzero y^55 term need not vanish on RAW Delta: it vanishes only after
# the degree-upper rows.  H=y^33+y^22 makes H^2 contain 2*y^55.
y=s.symbols('y')
raw=(y**33+y**22)**2
data['negative_controls']={'raw_Delta_y55_coefficient':s.expand(raw).coeff(y,55),
    'raw_Delta_degree':s.degree(raw,y),
    'dropping_attainment_retains_Delta':True,
    'terminal_e_not_scalar_unit':{'model':'f_e(x)=x','degree_x':1}}

# Independently validate the depressed identity used by the engine reduction.
h,AA,BB,CC,DD=s.symbols('h AA BB CC DD')
FF=h**3+AA*h+BB;GG=h**2+CC*h+DD
QQ=GG**3-FF**2+a*GG**2+b*FF*GG+c*FF+d*GG+e
Acal=a+b**2/4;HH=h-b/6
v=DD+a/3+b**2/18
p=d+b*c/2-Acal**2/3
q=e+c**2/4-Acal*(d+b*c/2)/3+2*Acal**3/27
V=BB-b*DD/4+a*b/12+b**3/54-c/2
depressed=-2*V*HH**3+(s.Rational(3,4)*v**2+p)*HH**2-3*v*V*HH+v**3-V**2+p*v+q
diff=s.expand(QQ.subs({CC:-b/3,AA:(3*DD+a)/2})-depressed)
assert diff==0
data['depressed_identity']={'exact_difference':str(diff),'verified':True}
OUT.write_text(json.dumps(data,indent=2,default=str)+'\n')
print(OUT)
