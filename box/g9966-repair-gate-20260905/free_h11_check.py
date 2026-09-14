#!/usr/bin/env python3
"""Exact image comparison after freeing Hc_11_0; never edits source engine."""
import ast
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import sys
import sympy as sp

ROOT=Path('/home/ubuntu/jc2')
SOURCE=ROOT/'box/g9966-d2-precise-20260905/band_engine.py'
spec=importlib.util.spec_from_file_location('precise_h11_audit',SOURCE)
engine=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=engine
spec.loader.exec_module(engine)
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='76d8c7206f70ba190d1a21fff812c016cbde497cd64071c29c91cfe8089f3c06'
H=engine.symbol('Hc_11_0')
base, free0, meta0=engine.build_major_h2('delta52',8)
oldmap=engine.h3_branch_map

def released_map(branch):
    mapping,free,meta=oldmap(branch)
    if branch=='delta52':
        assert mapping[H]==0 and H not in free
        mapping=dict(mapping)
        del mapping[H]
        free=[*free,H]
        meta={**meta,'Hc_11_0':'free','b0':'mislabel removed'}
    return mapping,free,meta

# Recompile only the original build function, changing its fail-closed count.
# No polynomial operations, supports, faces, row formulas, or pivots change.
tree=ast.parse(inspect.getsource(engine.build_major_h2))
class CountChange(ast.NodeTransformer):
    count=0
    def visit_Constant(self,node):
        if node.value==103:
            self.count+=1
            return ast.copy_location(ast.Constant(value=104),node)
        return node
change=CountChange()
tree=change.visit(tree)
assert change.count==1
ast.fix_missing_locations(tree)
namespace=dict(engine.__dict__)
namespace['h3_branch_map']=released_map
exec(compile(tree,'<build_major_h2_count104>','exec'),namespace)
released,free1,meta1=namespace['build_major_h2']('delta52',8)
assert set(base)==set(released)
assert all(sp.expand(base[k]-released[k])==0 for k in base)
assert free1-free0=={H} and not free0-free1
assert not any(H in row.free_symbols for row in released.values())
# Local leader control cannot see t^11=s^22: preserve the raw leader with H free.
h3,_=engine.h3_template()
mp,_,_=released_map('delta52')
h3={k:engine.substitute_map(v,mp) for k,v in h3.items()}
assert h3[(11,0)]==H
result={
    'status':'PASS', 'engine_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'field':'Q', 'branch':'delta52', 'endpoint_stage':8,'max_t':8,
    'max_t_formula':'max(J t-power 8, ceil(pole local power 16 / 2), 4)=8',
    'only_map_release':'Hc_11_0=0 removed; Hc_11_0 adjoined freely',
    'only_build_code_change':'count assertion 103 -> 104',
    'h3_extra_term':'Hc_11_0*t^11',
    'inner_dimensions':[len(free0),len(free1)],
    'K2_terms':len(base),'K2_identical_exactly':True,
    'K2_hfree_hash':engine.rows_hash([(str(k),v) for k,v in sorted(released.items())]),
    'extra_ring_generators':sorted(map(str,free1-free0)),
    'h3_leader_control':engine.h3_minor_control('delta52',h3),
    'downstream_reason':'outer_state is independent of h3 map. build_FG and cumulative_rows receive identical K2 and outer polynomials, hence every endpoint raw row is unchanged. All Q* pivot candidates appearing in rows remain identical; H never appears. The original unit identity extends to the polynomial ring adjoining H.',
    'unit_identity':'1=(1/64)*stage8_G_local16_coord0',
    'scope':'Image equality in the declared engine only; source-support necessity audited separately.'
}
result['h3_leader_control'].pop('ODE_compatibility',None)
print(json.dumps(result,indent=2))
