#!/usr/bin/env python3
"""Diagnostic of existing accepted selected routes, not a new source screen.

Track the denominator of RECORDED selected nonzero radius coefficients. Group
the existing nonzero orbit multiplicities into larger possible orbits under
that support denominator. We do not rerun Tree with changed A and do not claim
this records off-radius support or proves existence/impossibility of a source.
"""
import sys
sys.dont_write_bytecode=True
import importlib.util
import json
from collections import Counter
from fractions import Fraction as F
from math import lcm
from pathlib import Path

ROOT=Path('/home/ubuntu/jc2')
OUT=ROOT/'box/ctop-gate-20260905'
for name,path in [
    ('moh_skeleton_full_frozen',Path('/tmp/jc2-lane.yqyWvI/inputs/moh_skeleton_full.py')),
    ('r2_stabilizer_tree',ROOT/'box/centre-gate-20260903/opus5_probe.py')]:
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
B=sys.modules['moh_skeleton_full_frozen']
T=sys.modules['r2_stabilizer_tree']
assert T.B is B
rows=json.loads((OUT/'r2-enum-audit.json').read_text())['operative_rows']

def diagnose(r):
    vs={int(k):v for k,v in r['V'].items()}
    sk=B.Skel(r['n'],r['m'],r['Ms'],vs)
    tree=T.Tree(r['n'],r['m'],r['Ms'],gate=False,ode=True,capacity=False,
                passport=False,recenter=True)
    route=tree.embeds(vs)
    assert route is not None
    witness=route
    support=1
    nodes=[]
    while 'j' in route:
        j=route['j']
        exponent=F(route['delta'])
        oldA=route['A']
        supportA=(support*exponent).denominator
        assert supportA % oldA == 0
        ratio=supportA//oldA
        mults=Counter(route['orbits'])
        grouped=all(count % ratio == 0 for count in mults.values())
        degree_congruent=(route['P']-route['b']) % supportA == 0
        assert sum(k*v for k,v in mults.items())*oldA+route['b']==route['P']
        nodes.append(dict(j=j,delta=str(exponent),L_recorded_support=support,
            A_tree=oldA,A_recorded_support=supportA,required_grouping=ratio,
            P=route['P'],Q=route['Q'],b=route['b'],mode=route['mode'],
            orbit_multiplicity_histogram=dict(sorted(mults.items())),
            grouping_possible=grouped,degree_congruent=degree_congruent))
        if route['mode']=='nonzero':
            support=lcm(support,exponent.denominator)
        route=route['child']
    actualA1=(support*sk.delta[1]).denominator
    ns,ms=r['n']//sk.d[2],r['m']//sk.d[2]
    v2=vs[2]
    c12=ns*v2 % actualA1 == 0 and (ms*v2-1) % actualA1 == 0
    c13=ms*v2 % actualA1 == 0 and (ns*v2-1) % actualA1 == 0
    chain=tuple(vs[i] for i in range(2,sk.s+1))
    # free_exponents expects V_2,...,V_s and computes its existing envelope.
    free=[str(z) for z in tree.free_exponents(chain)]
    return dict(row=r,nodes=nodes,bottom=dict(L_recorded_support=support,
        delta1=str(sk.delta[1]),A1_tree=route['A1'],A1_recorded_support=actualA1,
        cond12=c12,cond13=c13),
        existing_free_exponent_envelope=free,
        selected_route_grouping_possible=all(n['grouping_possible'] for n in nodes),
        selected_route_with_bottom_possible=all(n['grouping_possible'] for n in nodes) and (c12 or c13),
        witness=witness)

diags=[diagnose(r) for r in rows if r['effective_ctop_fail']]
sortkey=lambda d:(d['row']['effective_sp'],d['row']['n1'],d['row']['effective_d'][-2],
                  d['row']['n'],d['row']['m'],d['row']['Ms'],list(d['row']['V'].values()))
passing=sorted([d for d in diags if d['selected_route_with_bottom_possible']],key=sortkey)
summary=dict(diagnosed_existing_routes=len(diags),
    grouping_possible=sum(d['selected_route_grouping_possible'] for d in diags),
    grouping_and_bottom_possible=len(passing),
    possible_by_us=dict(sorted(Counter(d['row']['u_s'] for d in passing).items())),
    possible_us1=sum(d['row']['u_s']==1 for d in passing))
out=dict(schema='jc2.ctop-gate.r2-stabilizer-diagnostic/v1',summary=summary,
    limitation='Recorded radius-coefficient support only; unrecorded off-radius support may change denominator. Existing witness orbit multiplicities are grouped, not recomputed. Failure is not a kill, and passing does not establish source existence.',
    possible_examples=passing[:12],possible_us1_examples=[d for d in passing if d['row']['u_s']==1][:12],
    named96=[d for d in diags if (d['row']['n'],d['row']['m'],d['row']['Ms'])==(96,72,[36,78,94])],
    diagnostics=diags)
(OUT/'r2-enum-stabilizer.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(summary,indent=2))
for d in passing[:12]:
    r=d['row']
    print('PASSING RECORDED ROUTE',r['n'],r['m'],r['parent_M'],r['V'],
          'child',r['n1'],r['effective_M'],r['effective_V'],r['effective_d'],
          'us',r['u_s'],'ell',r['ell'],'drops',r['drops'])
    print(json.dumps(d['nodes']))
    print('bottom',d['bottom'],'free_envelope',d['existing_free_exponent_envelope'])
