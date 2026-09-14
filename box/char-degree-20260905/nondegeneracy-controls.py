#!/usr/bin/env python3
"""Exact arithmetic certificate for equality faces and composition obstruction."""
from pathlib import Path
from math import comb, gcd
import json
import sympy as s

DATA={
 '9966':{'degrees':(99,66,55),'top_F_multiplicities':(27,72),
  'weight':(3,4),'D1_multiplier':3,'qcap':32,'Fface_root_multiplicity':24,
  'Fface_root_count':3,'K2_face_weight':96,
  'specs':{'A2':(65,189,583),'A3':(98,285,879),
           'B1':(32,93,287),'B2':(65,189,583)}},
 '10872':{'degrees':(108,72,63),'top_F_multiplicities':(24,84),
  'weight':(4,5),'D1_multiplier':2,'qcap':35,'Fface_root_multiplicity':21,
  'Fface_root_count':4,'K2_face_weight':140,
  'specs':{'A2':(71,276,566),'A3':(107,416,853),
           'B1':(35,136,279),'B2':(71,276,566)}}}
OUT={}
for tag,data in DATA.items():
 wt,wz=data['weight'];qcap=data['qcap'];out={'outer_faces':{}}
 for block,(degree,floor,threshold) in data['specs'].items():
  sites=[(r,q) for r in range(degree+1)
         for q in range(min(qcap,degree-r)+1) if wt*r+wz*q==floor]
  sites.sort(key=lambda p:p[1])
  mult=threshold-data['D1_multiplier']*floor
  M=s.Matrix([[comb(q,k) if q>=k else 0 for r,q in sites] for k in range(mult)])
  assert M.rank()==len(sites)
  assert all(q%wt==0 for r,q in sites)
  out['outer_faces'][block]={'sites':sites,'pi_powers':[q for r,q in sites],
     'polynomial_degree_in_pi_to_cover':max(q//wt for r,q in sites),
     'D1_vanishing_order_at_pi1':mult,'matrix_rank':M.rank(),
     'number_columns':len(sites),'all_equality_coefficients_forced_zero':True}
 n,m,D=data['degrees'];bound=gcd(gcd(n,m),D);topgcd=gcd(*data['top_F_multiplicities'])
 candidates=[k for k in range(1,bound+1) if bound%k==0]
 feasible=[k for k in candidates if topgcd%(n//k)==0]
 assert len(feasible)==1
 k=feasible[0];power=n//k;mult=data['Fface_root_multiplicity']
 physical_order=3*data['K2_face_weight']-wt*n
 assert physical_order==-power
 assert mult%power!=0
 out['common_generator']={'degree_gcd':bound,'candidate_y_degrees':candidates,
    'F_top_gcd':topgcd,'top_compatible_degrees':feasible,
    'required_F_power':power,'physical_D2_s_order_F':physical_order,
    'forced_s_order_generator':-1,'Fface_root_multiplicity':mult,
    'multiplicity_mod_required_power':mult%power,'contradiction':True}
 OUT[tag]=out
Path(__file__).with_suffix('.json').write_text(json.dumps(OUT,indent=2)+'\n')
print(json.dumps({k:{b:v['matrix_rank'] for b,v in r['outer_faces'].items()} for k,r in OUT.items()}))
