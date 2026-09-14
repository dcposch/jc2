#!/usr/bin/env python3
"""Derive exact D1 face supports from the full generic source rows."""
import hashlib,importlib.util,json,sys,time
from pathlib import Path
import sympy as sp
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import engine as E
import d1_jacobian_face as D
from source_data import SOURCE as S,jsonable
spec=importlib.util.spec_from_file_location('generic_incidence',HERE/'print-audit-generic-incidence.py')
G=importlib.util.module_from_spec(spec);spec.loader.exec_module(G)
start=time.monotonic()
h,hvars,C2,C3,c2v,c3v,rows,mapping,pivots,gmeta=G.derive_generic()
cut=S['k2_D1_floor']//3
low=E.tz_add(E.mul_weight(E.mul_weight(h,h,cut),h,cut),E.mul_weight(C2,h,cut),{p:v for p,v in C3.items() if E.weight(p)<=cut})
H=E.substitute_map(D.extract_face(low,S['k2_D1_floor']),mapping)
assert sp.degree(H,D.PI)==8 and sp.Poly(H,D.PI).LC()==3**8
assert all(k[0]%3==2 for k,v in sp.Poly(H,D.PI).terms() if v!=0)
outer,free,metadata=E.outer_state(7)
faces={'H':H};d2={}
for name,poly in outer.items():
    floor,threshold=S['outer_specs'][name][1:]
    d2[name]=sp.expand(sum(v*D.PI**q for (r,q),v in poly.items() if E.weight((r,q))==floor))
    assert d2[name]==0
    faces[name]=D.extract_face(poly,threshold)
expected={'H':[2,5,8],'A2':[1,4,7,10],'A3':[0,3,6,9],'B1':[2,5],'B2':[1,4,7,10]}
for name,face in faces.items():assert sorted(k[0] for k,v in sp.Poly(face,D.PI).terms() if v!=0)==expected[name]
P=H**3+faces['A2']*H+faces['A3'];Q=H**2+faces['B1']*H+faces['B2']
# Degrees of the three summands prove each leading coefficient without
# expanding mapped products. No normalization is imposed here.
assert sp.degree(faces['A2'],D.PI)+sp.degree(H,D.PI)<24
assert sp.degree(faces['A3'],D.PI)<24
assert sp.degree(faces['B1'],D.PI)+sp.degree(H,D.PI)<16
assert sp.degree(faces['B2'],D.PI)<16
result={'status':'PASS','source_generic_rows':len(rows),'source_generic_Qstar_pivots':len(pivots),
'faces':{name:str(face) for name,face in faces.items()},'supports':expected,
'outer_D2_faces_zero_by_emitted_D1_equations':{name:value==0 for name,value in d2.items()},
'H_leader':3**8,'P_leader':3**24,'Q_leader':3**16,
'leaders_are_consequences_of_K2_D2_identity_and_D1_rows_not_new_gauges':True,
'pure_power_differential':0,
'custody':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in
('engine.py','source_data.py','d1_jacobian_face.py','print-audit-generic-incidence.py','print-audit-d1-source-faces.py')},
'elapsed_seconds':time.monotonic()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(jsonable(result),indent=2,sort_keys=True)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('faces','custody')},indent=2))
