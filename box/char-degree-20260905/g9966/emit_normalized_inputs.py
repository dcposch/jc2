#!/usr/bin/env python3
"""Frozen corrected99 normalized coefficient maps, stages0--8, exact Q.

This emits finite row data and the COMPLETE source tower for the global
characteristic instrument. The cap applies only to historical finite rows.
"""
import argparse, hashlib, json, sys, time
from pathlib import Path
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'source'))
import engine as E
from source_data import SOURCE as S, jsonable

def encode_table(tab):return [[r,q,str(v)] for (r,q),v in sorted(tab.items()) if v!=0]
def build(branch,stage,out):
    start=time.monotonic();h,c2,c3,inner,imeta=E.inner_state(branch)
    outer,ofree,ometa=E.outer_state(min(stage,7))
    a,b,c,d,e,lam,Z=sp.symbols('target_a target_b target_c target_d target_e leader55 Z55')
    pre={v:sp.Integer(0) for v in ofree if str(v).startswith('B1c_')}
    pre[sp.Symbol('B1c_32_0')]=-b/3
    for v in ofree:
        if str(v).startswith('A2c_'):pre[v]=sp.Rational(3,2)*sp.Symbol(str(v).replace('A2c_','B2c_'))
    pre[sp.Symbol('A2c_65_0')]+=a/2
    outer={name:{p:E.substitute_map(v,pre) for p,v in poly.items()} for name,poly in outer.items()}
    assert all(sp.expand(outer['A2'].get(p,0)-sp.Rational(3,2)*outer['B2'].get(p,0)-(a/2 if p==(65,0) else 0))==0 for p in set(outer['A2'])|set(outer['B2']))
    assert all(sp.expand(v-(-b/3 if p==(32,0) else 0))==0 for p,v in outer['B1'].items())
    cap=max(stage if stage>=2 else 1,(E.stage_spec(branch,stage)['pole_local_power']+S['minor'][branch]['cover']-1)//S['minor'][branch]['cover'],4)
    Hlow,_,_=E.build_major_h2(branch,cap);F,G=E.build_FG(Hlow,outer,cap)
    rows,counts=E.cumulative_rows(branch,stage,F,G);rows=list(imeta['additional_rows'])+rows
    free=(inner|ofree)-set(pre)|{a,b,c,d,e,lam,Z}
    sep=sp.Symbol('rho' if branch=='delta2' else 'c')
    res,mapping,pivots,zero=E.qstar_reduce(rows,free-{sep,a,b,c,d,e,lam,Z})
    mapping=E.resolve_map(mapping)
    def apply(tab):return {p:E.substitute_map(v,mapping) for p,v in tab.items()}
    maps={name:encode_table(apply(tab)) for name,tab in [('h3',h),('C2',c2),('C3',c3),('B2',outer['B2']),('A3',outer['A3'])]}
    expected=free-set(mapping)
    images=set().union(*(sp.sympify(v).free_symbols for tab in maps.values() for _,_,v in tab),*(v.free_symbols for _,v in res))
    assert images<=expected,images-expected
    data={'branch':branch,'stage':stage,'field':'Q','normalization':{'h3':11,'C2':22,'C3':33,'h2':33,'B2':65,'A3':98},
          'maps':maps,'residual_rows':[(l,str(v)) for l,v in res],
          'finite':{'cap':cap,'raw_rows':len(rows),'row_accounting':counts,'raw_hash':E.rows_hash(rows),'Qstar_pivots':len(pivots),'zero':zero,'residual':len(res)},
          'raw_finite_rows':[(l,str(v)) for l,v in rows],
          'degree_premap':{str(k):str(v) for k,v in pre.items()},'finite_map':{str(k):str(v) for k,v in mapping.items()},
          'finite_pivots':[{'row':p.label,'variable':str(p.variable),'leader':str(p.coefficient),'rhs':str(p.rhs)} for p in pivots],
          'full_free_coordinates':sorted(map(str,expected)),
          'source_inner':{k:v for k,v in imeta.items() if k!='additional_rows'},'source_outer':ometa,
          'source_gauge':'all source centres retained; two target coefficients replace source outer constants by proved equations; no new gauge',
          'complete_characteristic_input':True,'only_finite_rows_use_cap':True,
          'elapsed_seconds':round(time.monotonic()-start,3)}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jsonable(data),indent=2,sort_keys=True)+'\n')
    print(branch,stage,'READY',len(expected),len(res),data['elapsed_seconds'],flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--branch',choices=['delta2','delta52'],required=True)
    ap.add_argument('--stage',type=int);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    if args.stage is not None:build(args.branch,args.stage,args.out)
    else:
        for stage in range(9):build(args.branch,stage,args.out/f'{args.branch}_stage{stage}.json')
