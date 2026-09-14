#!/usr/bin/env python3
from pathlib import Path
import json,sys
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'run-code-source-full'))
import engine as E
from source_data import SOURCE as S
from d1_jacobian_face import extract_face,PI
outer,free,meta=E.outer_state(0)
data={}
for name,poly in outer.items():
    degree,floor,threshold=S['outer_specs'][name]
    first={p:sp.expand(v) for p,v in poly.items() if E.weight(p)==floor}
    assert all(value==0 for value in first.values())
    face=extract_face(poly,threshold)
    p=sp.Poly(face,PI)
    data[name]={'first_weight_layer_identically_zero':True,
                'D1_face_degree':p.degree(),'equality_threshold':threshold,
                'stage0_pivots':meta['D1_cumulative_pivots']}
e=sp.Symbol('e');pi=sp.Symbol('pi')
orbit_face=sp.expand(S['k2_face'].subs({sp.Symbol('beta'):1,pi:1+PI*e}))
gap=S['k2_D1_floor']-S['D1_substitution'][0]//S['D2_weight'][0]*S['k2_floor']
h_leader=sp.expand(orbit_face).coeff(e,gap).coeff(PI,gap)
assert h_leader==3**8 and gap==8
Fdeg=max(data['A2']['D1_face_degree']+gap,data['A3']['D1_face_degree'])
Gdeg=max(data['B1']['D1_face_degree']+gap,data['B2']['D1_face_degree'])
assert Fdeg<3*gap and Gdeg<2*gap
out={'status':'PASS','outer':data,'H_D1_degree':gap,'H_D1_leading_coefficient':str(h_leader),
     'F_D1_degree':3*gap,'F_D1_leading_coefficient':str(h_leader**3),
     'G_D1_degree':2*gap,'G_D1_leading_coefficient':str(h_leader**2),
     'largest_outer_contribution_F_degree':Fdeg,'largest_outer_contribution_G_degree':Gdeg,
     'no_further_degree_or_leading_coefficient_localizer_needed':True}
(HERE/'minor_D1-leader-control.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
