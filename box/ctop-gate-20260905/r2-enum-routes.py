#!/usr/bin/env python3
"""Read-only route diagnostic for ten numerical C-TOP failures.
Uses already independently verified rows; reexecutes Tree for each example.
No new screen or count-based exclusion is implemented.
"""
import sys
sys.dont_write_bytecode = True
import importlib.util
import json
from collections import Counter
from pathlib import Path

ROOT = Path('/home/ubuntu/jc2')
OUT = ROOT/'box/ctop-gate-20260905'
for name,path in [
    ('moh_skeleton_full_frozen',Path('/tmp/jc2-lane.yqyWvI/inputs/moh_skeleton_full.py')),
    ('r2_route_tree',ROOT/'box/centre-gate-20260903/opus5_probe.py')]:
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
B=sys.modules['moh_skeleton_full_frozen']
T=sys.modules['r2_route_tree']
assert T.B is B
rows=json.loads((OUT/'r2-enum-audit.json').read_text())['operative_rows']
fails=[r for r in rows if r['effective_ctop_fail']]
key=lambda r:(r['effective_sp'],r['n1'],r['effective_d'][-2],r['n'],r['m'],
              r['Ms'],list(r['V'].values()))

selected=[]
for n,m,Ms,V in [
    (96,72,[36,78,94],[1,3,5]),
    (96,72,[36,78,94],[4,3,5]),
    (90,60,[10,45,88],[1,8,4]),
    (108,72,[24,78,106],[1,4,5]),
    (108,72,[48,90,106],[1,3,5]),
    (144,96,[-32,104,142],[1,14,7]),
    (96,72,[-60,56,94],[1,9,3]),
    (144,96,[-16,72,140,142],[1,10,5,3]),
    (150,100,[-60,65,148],[1,6,3]),
    (150,100,[-60,65,148],[5,6,3]),
]:
    hits=[r for r in fails if (r['n'],r['m'],r['Ms'],list(r['V'].values())) == (n,m,Ms,V)]
    assert len(hits)==1
    r=hits[0]
    vs={int(k):v for k,v in r['V'].items()}
    sk=B.Skel(n,m,Ms,vs)
    tree=T.Tree(n,m,Ms,gate=False,ode=True,capacity=False,passport=False,recenter=True)
    witness=tree.embeds(vs)
    assert witness is not None
    nodes=[]
    route=witness
    while 'j' in route:
        j=route['j']
        dl,L,A,P,Q,lo=tree.node(j,tuple(vs[k] for k in range(j+1,sk.s+1)))
        assert (str(dl),A,P,Q)==(route['delta'],route['A'],route['P'],route['Q'])
        nodes.append(dict(j=j,delta=str(dl),L=L,A=A,P=P,Q=Q,lower_bound=str(lo),
            selected_V=vs[j],selected_mode=route['mode'],zero_multiplicity=route['b'],
            nonzero_orbit_multiplicities=route['orbits'],danger=route['danger'],
            removable=(dl.denominator==1 and dl<=0)))
        route=route['child']
    selected.append(dict(row=r,parent_delta={str(k):str(v) for k,v in sk.delta.items()},
        parent_delta_sminus1=str(sk.delta[sk.s-1]),parent_V_sminus1=vs[sk.s-1],
        nodes=nodes,bottom=route,witness=witness))

summary=dict(effective_ctop_fails_by_us=dict(sorted(Counter(r['u_s'] for r in fails).items())),
    us1_fail_count=sum(r['u_s']==1 for r in fails),
    us1_fail_ell0=sum(r['u_s']==1 and r['ell']==0 for r in fails),
    us1_all_ell0=sum(r['u_s']==1 and r['ell']==0 for r in rows),
    us1_fail_effective_sp2=sum(r['u_s']==1 and r['effective_sp']==2 for r in fails),
    any_fail_effective_sp2=sum(r['effective_sp']==2 for r in fails),
    higher_fail_ell0=sum(r['u_s']>1 and r['ell']==0 for r in fails))
result=dict(schema='jc2.ctop-gate.r2-route-diagnostic/v1',summary=summary,
    limitation='Displays existing Tree witnesses; no new source-symmetry screen or impossibility verdict.',
    examples=selected)
(OUT/'r2-enum-routes.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(summary,indent=2))
for i,e in enumerate(selected,1):
    r=e['row']
    print('EXAMPLE',i,'parent',r['n'],r['m'],r['parent_M'],r['V'])
    print('child',r['n1'],r['m1'],r['effective_M'],r['effective_V'],r['effective_d'],
          'ell',r['ell'],'us',r['u_s'],'drops',r['drops'],'delta(s-1)',e['parent_delta_sminus1'])
    print('route',json.dumps(e['nodes']))
    print('bottom',e['bottom'])
