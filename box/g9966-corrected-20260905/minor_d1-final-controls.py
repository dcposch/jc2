#!/usr/bin/env python3
"""Independent D1, physical-corner, row-regeneration and localization controls."""
from pathlib import Path
import hashlib,json,sys
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import minor_final_verify as M
E=M.load_code(HERE/'run-code-source-full',gauge=True)
import deep_gauge_accelerated as GAUGE
import d1_jacobian_face as FACE
S=E.S
a,b,d=sp.symbols('source_a source_b source_d')
v=M.Verifier.__new__(M.Verifier)
v.e=E;v.S=S;v.branch='delta2';v.loc=sp.Symbol('rho')
v.basefree={a,b,d,v.loc};v.cache={};v.extra_generators=set();v.graph_faces=None
v.locals={str(x):x for x in v.basefree|set(map(sp.Symbol,['Jc','ZJ']))}
v.h={(0,8):sp.Integer(1),(4,5):sp.Rational(-8,3),(8,2):a,
     (11,0):b,(10,0):sp.Integer(2),(10,1):sp.Integer(3)}
v.c2={(8,10):sp.Integer(2),(16,4):sp.Integer(3),(21,0):d,(21,1):a}
v.c3={(24,6):sp.Integer(2),(32,0):b,(32,1):sp.Integer(-1)}
v.outer={}
for index,(name,(degree,floor,threshold)) in enumerate(S['outer_specs'].items()):
    candidates=[(r,q) for r in range(degree+1) for q in range(min(32,degree-r)+1)
                if 3*r+4*q>=floor and 9*r+12*q<=threshold<=9*r+13*q]
    # Spread across the equality layer, including nonconstant Pi powers.
    slots=candidates[::max(1,len(candidates)//3)][:3]
    block={p:sp.Integer(index+j+1) for j,p in enumerate(slots)}
    block[(degree,0)]=sp.Integer(index+2)
    block[(degree-1,0)]=a+index
    block[(degree-1,1)]=b-index
    v.outer[name]=block
    assert all(r+q<=degree for r,q in block)
want,metadata=FACE.d1_face_jacobian(v.h,v.c2,v.c3,v.outer)
got=v.independent_d1_face({})
assert sp.expand(want-got)==0
origin_want,_=GAUGE.corner_from_blocks(v.h,v.c2,v.c3,v.outer)
origin_got=v.independent_origin_constant({})
assert sp.expand(origin_want-origin_got)==0
assert got!=0 and origin_got!=0

jc,zj=sp.symbols('Jc ZJ');Pi=sp.Symbol('Pi')
rows=[(f'gauge_D1_J_face_Pi{k[0]}',value) for k,value in sp.Poly(want-jc,Pi).terms()]
rows.append(('gauge_J_nonzero_wrapper',jc*zj-1))
cert={'map_before':{},'raw_new_rows_before_reduction':[(label,str(value)) for label,value in rows],
      'raw_new_rows_hash':E.rows_hash(rows)}
d1_regeneration=v.regenerate(cert)
rows=[('gauge_early_J_constant',origin_want-jc)]
cert={'map_before':{},'raw_new_rows_before_reduction':[(label,str(value)) for label,value in rows],
      'raw_new_rows_hash':E.rows_hash(rows)}
origin_regeneration=v.regenerate(cert)
mapped_rows=[('gauge_early_J_constant',origin_want-a)]
mapped_cert={'map_before':{'Jc':str(a)},
             'raw_new_rows_before_reduction':[(label,str(value)) for label,value in mapped_rows],
             'raw_new_rows_hash':E.rows_hash(mapped_rows)}
mapped_origin_regeneration=v.regenerate(mapped_cert)
v.weak_map={a:b,d:sp.Integer(0)};v.weak_residual=[]
merge_rows=[(f'weak_graph_target_{a}',a-b),(f'weak_graph_target_{d}',d)]
merge_cert={'map_before':{},'raw_new_rows_before_reduction':[(label,str(value)) for label,value in merge_rows],
            'raw_new_rows_hash':E.rows_hash(merge_rows)}
merge_regeneration=v.regenerate(merge_cert)
incomplete=dict(merge_cert);incomplete['raw_new_rows_before_reduction']=incomplete['raw_new_rows_before_reduction'][:1]
incomplete['raw_new_rows_hash']=E.rows_hash(merge_rows[:1])
try:v.regenerate(incomplete)
except AssertionError:missing_merge_relation_rejected=True
else:raise AssertionError('omitted weak graph relation was accepted')
bad_rows=[('gauge_early_J_constant',origin_want-a+1)]
bad_cert={'map_before':{'Jc':str(a)},
          'raw_new_rows_before_reduction':[(label,str(value)) for label,value in bad_rows],
          'raw_new_rows_hash':E.rows_hash(bad_rows)}
try:v.regenerate(bad_cert)
except AssertionError:changed_coefficient_rejected=True
else:raise AssertionError('changed physical Jacobian coefficient was accepted')

# Higher physical e-orders do not alter the order-zero Jacobian face.
e,p,R,T=sp.symbols('e Pi R T')
P=p**3+a*p+b;Q=p**2+d
x=e**-9;y=e**-9+e**3+p*e**4
F=e**-3*P+e**-2*R*p;G=e**-2*Q+e**-1*T*p**2
actual=sp.expand((sp.diff(F,e)*sp.diff(G,p)-sp.diff(F,p)*sp.diff(G,e))/(-9*e**-6))
assert sp.expand(actual.coeff(e,0)-(3*P*sp.diff(Q,p)-2*sp.diff(P,p)*Q)/9)==0

localizer_controls={}
for branch,loc in [('delta2',sp.Symbol('rho')),('delta52',sp.Symbol('c'))]:
    empty=M.singular_replay([('zero_face',jc),('J_inverse',jc*zj-1)],branch,3,HERE/f'minor_d1-{branch}-empty.sing')
    point=M.singular_replay([('face_value',jc-7),('J_inverse',jc*zj-1),('branch_point',loc-1)],branch,3,HERE/f'minor_d1-{branch}-point.sing')
    assert empty['unit_ideal'] and not point['unit_ideal'] and point['full_dimension']==0
    localizer_controls[branch]={'zero_J_rejected':empty,'arbitrary_nonzero_J_7_accepted':point}
q4=sp.Symbol('q4')
rational_rows=[('rational_nonlinear',q4**9/sp.Integer(32768)-sp.Rational(1,3)),
               ('linear_contradiction',q4)]
rational_empty=M.singular_replay(rational_rows,'delta52',2,HERE/'minor_d1-rational-parser-empty.sing')
rational_point=M.singular_replay([('rational_power_point',q4**9/sp.Integer(32768)-sp.Rational(1,32768)),
                                ('point',q4-1)],'delta52',2,HERE/'minor_d1-rational-parser-point.sing')
assert rational_empty['unit_ideal'] and not rational_point['unit_ideal']
assert '/' not in (HERE/'minor_d1-rational-parser-empty.sing').read_text().split('ideal Raw=',1)[1].split(';',1)[0]
out={'status':'PASS','D1_source_series_vs_helper':True,'physical_corner_vs_helper':True,
     'higher_physical_orders_leave_J_face_unchanged':True,'D1_regeneration':d1_regeneration,
     'origin_regeneration':origin_regeneration,'solved_Jc_image_regeneration':mapped_origin_regeneration,
     'changed_origin_coefficient_rejected':changed_coefficient_rejected,'localizer_controls':localizer_controls,
     'complete_weak_graph_regeneration':merge_regeneration,'omitted_weak_graph_relation_rejected':missing_merge_relation_rejected,
     'rational_nonlinear_export_controls':{'unit':rational_empty,'nonunit':rational_point},
     'D1_expression_sha256':hashlib.sha256(sp.srepr(got).encode()).hexdigest(),
     'corner_expression_sha256':hashlib.sha256(sp.srepr(origin_got).encode()).hexdigest(),
     'verifier_sha256':M.digest(HERE/'minor_final_verify.py'),
     'source_helper_sha256':M.digest(HERE/'run-code-source-full/d1_jacobian_face.py')}
(HERE/'minor_d1-final-controls.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','D1_rows':d1_regeneration['raw_rows_regenerated_before_reduction'],
                  'origin_rows':origin_regeneration['raw_rows_regenerated_before_reduction']},indent=2))
