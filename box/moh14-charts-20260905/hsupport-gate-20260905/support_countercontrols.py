#!/usr/bin/env python3
"""Exact countercontrols; none claims a descended Jacobian-pair witness."""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp
x,y,z,pi=sp.symbols('x y z pi')
h0=sp.expand(y*(y-x**2)**3)
poly=sp.Poly(h0,x,y)
weights=[]
for delta,B in [(F(9,4),F(-15,4)),(F(1,2),F(-11,2))]:
    got=min(F(a)*delta-b for (b,a),c in poly.terms())
    assert got==B
    assert sp.total_degree(h0)==7
    assert 2+3>4 and F(3)*delta-2>=B
    weights.append(dict(delta1=str(delta),min_weight=str(got),B=str(B)))
h=sp.expand(h0+x**5)
# t=z^4 converts the Puiseux substitution to a Laurent polynomial.
f=sp.expand(h.subs({x:z**-4,y:z**4+pi*z**9}))
orders={}
for term in sp.Add.make_args(f):
    power=int(term.as_powers_dict().get(z,0))
    orders[power]=sp.expand(orders.get(power,0)+term/z**power)
leading=min(k for k,v in orders.items() if v!=0)
assert leading==-15 and orders[leading]==-pi
assert F(-5)<F(-15,4)
eta=-sp.Poly(h,y).coeff_monomial(y**3)/4
assert eta==sp.Rational(3,4)*x**2
translated=sp.Poly(sp.expand(h.subs(y,y+eta)),x,y)
assert max(b+2*a for (b,a),coef in translated.terms())==8
assert sp.Poly(translated.as_expr(),y).coeff_monomial(y**3)==0
out=dict(scope='monicity/order/centering countercontrols only; NOT a source Jacobian pair',
         old_cap_weight_controls=weights,
         nonzero_center=dict(h=str(h),substitution='x=z^-4, y=z^4+pi*z^9',
                             lowest_z_exponent=leading,leading_coefficient=str(orders[leading]),
                             omitted_raw_term='x^5',raw_weight='-5',floor='-15/4'),
         trace_translation=dict(eta=str(eta),transformed_h=str(translated.as_expr()),
                                max_outer_weight=8,outer_d=2,trace_coefficient_zero=True))
p=Path(__file__).resolve().parent/'support-countercontrols.json'
p.write_text(json.dumps(out,indent=2)+'\n');print('SUPPORT_COUNTERCONTROLS_PASS',p)
