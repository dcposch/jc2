#!/usr/bin/env python3
"""Q-linear face coefficient proof, with free ell and no parameter division."""
import json
import sympy as sp
from source_data import SOURCE, jsonable

pi,beta,ell=sp.symbols('pi beta ell')
H=SOURCE['h3_face']
Uslots=SOURCE['Uslots'];Vslots=SOURCE['Vslots']
Uvars={q:sp.Symbol(f'U{q}') for r,q in Uslots}
Vvars={q:sp.Symbol(f'V{q}') for r,q in Vslots}
U=sum(v*pi**q for q,v in Uvars.items())
V=sum(v*pi**q for q,v in Vvars.items())
E=sp.Poly(sp.expand(SOURCE['k2_face']-H**SOURCE['inner_power']-U*H-V),pi)
# Keep the lowest U coefficient as a coordinate; all other variables pivot
# with scalar +/-1.  Equality U,V are valuation faces, not typed polynomials.
order=[Uvars[q] for q in sorted(Uvars,reverse=True)[:-1]]+[Vvars[q] for q in sorted(Vvars,reverse=True)]
sub={};pivots=[]
for variable in order:
    candidates=[]
    for (power,),coefficient in E.terms():
        row=sp.expand(coefficient.subs(sub))
        coefficient_variable=sp.diff(row,variable)
        if coefficient_variable.is_Rational and coefficient_variable!=0:
            candidates.append((power,row,coefficient_variable))
    assert candidates
    power,row,pivot=candidates[0]
    sub[variable]=sp.expand(-(row-pivot*variable)/pivot)
    pivots.append({'degree':power,'variable':str(variable),'scalar':str(pivot),'rhs':str(sub[variable])})
assert sp.expand(E.as_expr().subs(sub))==0
U1=Uvars[min(Uvars)]
old_residual=sp.Poly(sp.expand(SOURCE['k2_face']-(pi**SOURCE['h3_major'])**SOURCE['inner_power']),pi)
negative_degree=SOURCE['h3_major']*SOURCE['inner_power']-SOURCE['D2_weight'][0]
assert old_residual.coeff_monomial(pi**negative_degree)!=0
# Free low-q K2 output directions are not individually C2-floor directions.
# At order t^5, the perturbation z^21 divides by the leading monic h3.
z=sp.Symbol('z')
P=z**SOURCE['h3_major']*(1+z)**SOURCE['h3_minor']
quotient,remainder=sp.div(z**(2*SOURCE['h3_degree']-1),P,z)
assert sp.expand(P*quotient+remainder-z**(2*SOURCE['h3_degree']-1))==0
weights=[SOURCE['D2_weight'][0]*5+SOURCE['D2_weight'][1]*q for (q,),v in sp.Poly(quotient,z).terms() if v!=0]
result={'full_face_residual':'0','free_face_coordinates':[str(ell),str(U1)],'pivots':pivots,
        'old_face_negative_control':{'pi_degree':negative_degree,'coefficient':str(old_residual.coeff_monomial(pi**negative_degree))},
        'arbitrary_K2_output_floor_counterexample':{'K2_perturbation':'t^5*z^21','C2_order5_quotient':str(quotient),
          'C3_order5_remainder':str(remainder),'C2_normalized_weight_min':min(weights),'required_C2_floor':SOURCE['C2_floor']}}
print(json.dumps(jsonable(result),indent=2,sort_keys=True))
