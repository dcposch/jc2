#!/usr/bin/env python3
"""Derive the finite characteristic-degree55 instrument; not a branch kill."""
import json
import sympy as sp
from source_data import SOURCE as S,jsonable
n,m=S['n'],S['m'];M=S['M'];d=S['d'];F,G,H=sp.symbols('F G H')
n1=d[1]//d[2]
q={j:M[j]-(M[j-1] if j>1 else 0) for j in M}
lambda2=sum(q[j]*d[j] for j in range(1,3));mu2=sp.Rational(lambda2,d[2]);target=-int(mu2)
bound=m*n1
positions=[(j,a) for a in range(n1) for j in range(bound//n+1) if n*j+m*a<=bound]
equalities=[(j,a) for j,a in positions if n*j+m*a==bound]
assert len(equalities)==1 and equalities[0][1]==0
leading=G**n1-F**equalities[0][0]
free_positions=[p for p in positions if p not in equalities]
variables={p:sp.Symbol(f'target_{p[0]}_{p[1]}') for p in free_positions}
Q=leading+sum(variables[j,a]*F**j*G**a for j,a in free_positions)
pure=sp.Poly(sp.expand(Q.subs({F:H**S['outer_power_F'],G:H**S['outer_power_G']})),H)
# Pure H-powers have distinct highest y-degrees because H is monic degree33.
# Requiring deg_y Q<=55 successively zeroes every nonconstant H coefficient.
map0={}
pivots=[]
for (k,),coef in pure.terms():
    if k*S['k2_degree']>target:
        row=sp.expand(coef.subs(map0));xs=list(row.free_symbols)
        assert len(xs)==1
        x=xs[0];leader=sp.diff(row,x);assert leader.is_Rational and leader!=0
        map0[x]=sp.Integer(0);pivots.append({'H_power':k,'y_leading_degree':k*S['k2_degree'],'variable':str(x),'coefficient':str(leader)})
reduced=sp.expand(pure.as_expr().subs(map0));assert not reduced.has(H)
result={'characteristic_q':q,'lambda2':lambda2,'mu2':str(mu2),'target_y_degree':target,
        'Keller_e':n-1,'strict_M2_less_e':M[2]<n-1,
        'target_exponent_positions':positions,'unique_top_cancellation':equalities,
        'target_polynomial_family':str(Q),'target_coefficients_free':list(map(str,variables.values())),
        'nonzero_attainment':'[y^55]Q=lambda constant; Zlambda*lambda-1=0',
        'total_degree_bound':bound,'pure_power_restricted_control':{'F':'H^3','G':'H^2','H_y_degree':S['k2_degree'],'pivots':pivots,'remaining_polynomial':str(reduced),'y55_coefficient_after_higher_rows':'0','localized_leader_residue':'-1'},
        'scope':'Derived future characteristic instrument; pure-power control only, not a unit on the full branch chart',
        'printed_sources':['Moh p150 characteristic auxiliary numbers','Moh p151 Lemma2.1','Moh p152 Prop2.2(1),(2)','Moh p157 Prop3.1(1),(2)']}
print(json.dumps(jsonable(result),indent=2,sort_keys=True))
