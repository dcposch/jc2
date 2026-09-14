#!/usr/bin/env python3
import importlib.util
import json
from pathlib import Path
import sys
import sympy as S

root=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('face_minor_engine',root/'box/g9966-d2-precise-20260905/band_engine.py')
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
E45,E82=S.symbols('E45 E82')
results={}
for branch in ('delta2','delta52'):
    h,vs=m.h3_template()
    h[(4,5)]=h.get((4,5),0)-S.Rational(8,3)
    h[(8,2)]=h.get((8,2),0)+E82
    max_power=9 if branch=='delta2' else 21
    rows=m.local_rows(h,branch,max_power,exact_only=False)
    rho,c=S.symbols('rho c')
    want={(9,2):3*rho,(9,3):1} if branch=='delta2' else {(21,1):-c,(21,3):1}
    labels=sorted(set(rows)|set(want))
    equations=[(f'local_{n}_{k}',S.expand(rows.get((n,k),0)-want.get((n,k),0))) for n,k in labels]
    residual,mapping,pivots,zero=m.qstar_reduce(equations,set(vs)|{E82})
    assert all(m.substitute_map(row,mapping)==0 for _,row in equations) if not residual else True
    results[branch]={
      'raw_rows':len(equations),'pivots':len(pivots),'zeros':zero,
      'residual':[(label,str(S.factor(row))) for label,row in residual],
      'free_h_coefficients':sorted(str(v) for v in set(vs)|{E82} if v not in mapping),
      'mapping':{str(v):str(S.factor(rhs)) for v,rhs in mapping.items()},
      'conditional_E45':'-8/3',
    }
print(json.dumps(results,indent=2,sort_keys=True))
