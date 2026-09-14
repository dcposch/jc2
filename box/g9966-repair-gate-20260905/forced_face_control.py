#!/usr/bin/env python3
"""Exact coefficient obstruction; independent of the branch engine."""
import json
import sympy as s
p,a,b,beta=s.symbols('pi a b beta')
H=p**8+a*p**5+b*p**2
K=(p**3-beta)**8
U=sum(s.Symbol('U'+str(q))*p**q for q in (1,4,7,10))
V=sum(s.Symbol('V'+str(q))*p**q for q in (0,3,6,9))
res=s.Poly(s.expand(K-H**3-U*H-V),p)
row21=res.coeff_monomial(p**21)
assert s.expand(row21+8*beta+3*a)==0
assert row21.subs(a,-s.Rational(8,3)*beta)==0
assert row21.subs({a:0,beta:1})==-8
assert row21.subs({a:-s.Rational(8,3),beta:1})==0
row18=s.expand(res.coeff_monomial(p**18).subs(a,-s.Rational(8,3)*beta))
assert row18==s.Rational(20,3)*beta**2-3*b-s.Symbol('U10')
# Algebraic chart control: ordinary Euclidean division is possible, but its
# C2 t^4 component violates the sourced weight>=64 bound.
z=s.Symbol('z')
Q,R=s.div(-8*z**21,z**8*(1+z)**3,z)
assert s.expand(Q*z**8*(1+z)**3+R+8*z**21)==0
print(json.dumps({
    'status':'PASS','field':'Q[beta,a,b,U1,U4,U7,U10,V0,V3,V6,V9]',
    'h3_face':str(H),'h2_face':str(K),
    'C2_normalized_floor':64,'C2_face_q':[1,4,7,10],
    'C3_normalized_floor':96,'C3_face_q':[0,3,6,9],
    'pi21_row':str(row21),'forced_a':'-8*beta/3',
    'old_face_negative_control':-8,'correct_a_positive_control':0,
    'pi18_row_after_forced_a':str(row18),
    'b_status':'free at this coefficient comparison',
    'old_chart_t4_C2_quotient':str(Q),
    'old_chart_t4_C3_remainder':str(R),
    'quotient_weight_range':[12,52],
    'interpretation':'Euclidean engine output chart is internally algebraic, but old h3 face requires a C2 t^4 term below its necessary weight64 floor.'
},indent=2))
