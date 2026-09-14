#!/usr/bin/env python3
from pathlib import Path
import copy,json,sys
import sympy as sp
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import minor_final_verify as m
# The fixture is an immutable saved nonunit source-ideal reduction phase.
cert=json.loads((HERE/'minor_final_controls_input.json').read_text())
e=m.load_code(HERE);v=m.Verifier(e,'delta52')
positive=v.replay_phase(cert)
rejection={}
def rejects(name,obj):
    try:v.replay_phase(obj)
    except AssertionError as err:rejection[name]=str(err) or 'assertion rejected';return
    raise AssertionError('bad certificate accepted: '+name)
bad=copy.deepcopy(cert);bad['field']='F_101';rejects('wrong_coefficient_field',bad)
bad=copy.deepcopy(cert);bad['pivot_steps'][0]['rational_leader']=str(sp.Rational(bad['pivot_steps'][0]['rational_leader'])+1);rejects('wrong_QQstar_leader',bad)
bad=copy.deepcopy(cert);name=next(iter(bad['map_after']));bad['map_after'][name]='('+bad['map_after'][name]+')+1';rejects('changed_ring_map_image',bad)
bad=copy.deepcopy(cert);bad['map_after']['undeclared_coefficient']='0';rejects('undeclared_generator',bad)
aa,bb=sorted(v.basefree,key=str)[:2]
factor=aa-bb; source=sp.expand(3*factor**2)
rad={'phase':'synthetic_sound_power_control','branch':'delta52','field':'Q','localizer':'c',
     'map_before':{},'map_after':{str(aa):str(bb)},
     'free_before':sorted(map(str,v.basefree)),'free_after':sorted(map(str,v.basefree-{aa})),
     'residual_before':[],'residual_after':[],'residual_after_hash':e.rows_hash([]),
     'raw_new_rows_before_reduction':[['power',str(source)]],
     'raw_new_rows_hash':e.rows_hash([('power',source)]),
     'pivot_steps':[{'label':'radical_of_power','variable':str(aa),'rational_leader':'1',
                     'rhs_at_pivot':str(bb),'selected_equation_at_pivot':str(factor)}],
     'radical_steps':[{'source_row':'power','new_row':'radical_of_power','source_polynomial':str(source),
                       'factor':str(factor),'power':2,'rational_unit':'3','identity_verified':True}]}
radical_positive=v.replay_phase(rad)
bad=copy.deepcopy(rad);bad['radical_steps'][0]['factor']=str(aa+bb);rejects('wrong_radical_power_identity',bad)
unit=m.singular_replay([('forbidden_open_stratum',sp.Symbol('c'))],'delta52',1,HERE/'minor_final_unit-control.sing')
nonunit=m.singular_replay([('rational_point',sp.Symbol('c')-1)],'delta52',1,HERE/'minor_final_nonunit-control.sing')
assert unit['unit_ideal'] and unit['full_dimension']==-1
assert not nonunit['unit_ideal'] and nonunit['full_dimension']==0
out={'status':'PASS','positive_phase':positive,'positive_radical_certificate':radical_positive,'negative_certificate_controls':rejection,
     'independent_Q_wrapper_unit':unit,'independent_Q_wrapper_nonunit':nonunit,
     'fixture_sha256':m.digest(HERE/'minor_final_controls_input.json'),
     'verifier_sha256':m.digest(HERE/'minor_final_verify.py')}
(HERE/'minor_final-controls.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','negative_controls':list(rejection)},indent=2))
