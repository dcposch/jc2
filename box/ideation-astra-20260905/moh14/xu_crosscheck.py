#!/usr/bin/env python3
"""Consume the promoted Xu screen on the 14 old tree-only excess rows."""
import importlib.util
import json
import sys
import hashlib
from pathlib import Path

root=Path('/home/ubuntu/jc2')
receipt={line.split('=',1)[0]:line.split('=',1)[1] for line in (root/'xmodel/xu-screen-gate-fable5-20260903.run.v2').read_text().splitlines() if '=' in line}
for i in (2,6,7):
    q=root/receipt[f'charged_input_{i}']
    assert hashlib.sha256(q.read_bytes()).hexdigest()==receipt[f'charged_input_{i}_sha256'],q
print('GATE_IMPORT_HASHES 3/3 match historical Xu gate receipt (driver, skeleton, full tree).')
sys.path.insert(0,str(root/'box/mohprog-drivers-20260903'))
sys.path.insert(0,str(root/'box'))
path=Path('/home/ubuntu/jc2/box/xuscreen-20260903/xu_screen.py')
spec=importlib.util.spec_from_file_location('astra_old_xu',path)
mod=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=mod
spec.loader.exec_module(mod)
out=Path(__file__).resolve().parent
rows=json.loads((out/'rows.json').read_text())['rows']
alive=[]
dead=[]
for r in rows:
    n,m,Ms,V=r['ancestor']
    S=mod.M.Skel(n,m,Ms,dict(V))
    bound=mod.XuBounder(S).row_bound()
    assert bound is not None
    r['ancestor_characteristic']={'n':n,'m':m,'M':[S.M[i] for i in range(1,S.s+1)],
        'd':[S.d[i] for i in range(1,S.s+2)],'V':dict(V),'s':S.s}
    r['xu']={'IM_max':str(bound['IM_max']),'Im_min':str(bound['Im_min']),
        'principal_minor_floor':str(bound['principal_minor_floor']),
        'tree_minor_min':str(bound['tree_minor_min']),'survives':bound['xu_ok'],
        'status':'SURVIVES_BOUND' if bound['xu_ok'] else 'DEAD_BY_PROMOTED_XU'}
    verdict='SURVIVES_BOUND' if bound['xu_ok'] else 'DEAD_BY_PROMOTED_XU'
    print(verdict,'ancestor=',(n,m,Ms,V),'IM_max=',bound['IM_max'],'Im_min=',bound['Im_min'])
    (alive if bound['xu_ok'] else dead).append(r)
assert len(dead)==2 and len(alive)==12
assert all(r['ancestor'][0:3]==[90,60,[45,80,88]] for r in dead)
classes={(r['descent']['n'],r['descent']['m'],tuple(r['descent']['M']),r['descent']['ell']) for r in alive}
print('RESULT 14 old excess - 2 already promoted Xu kills = 12 strongest-screen survivors; 6 characteristic classes')
print('LIVE_CLASSES',sorted(classes))
print('TYPE max/min bounds consumed as promoted; survival does not assert realizability.')
(out/'xu_live12.json').write_text(json.dumps(alive,indent=2)+'\n')
class_rows=[]
for c in sorted(classes):
    members=[r for r in alive if (r['descent']['n'],r['descent']['m'],tuple(r['descent']['M']),r['descent']['ell'])==c]
    class_rows.append({'key':c,'multiplicity':len(members),'descent':members[0]['descent'],
        'ancestor_V_assignments':[r['descent']['ancestral_V'] for r in members],
        'xu_bounds':sorted({(r['xu']['IM_max'],r['xu']['Im_min']) for r in members})})
(out/'final_table.json').write_text(json.dumps({'type':'MEASURED exact arithmetic, promoted screen consumed',
    'old_tree_excess':14,'already_xu_dead':2,'strongest_screen_live':12,
    'characteristic_class_count':6,'coarse_degree_jacobian_class_count':4,
    'classes':class_rows,'rows':rows},indent=2)+'\n')
