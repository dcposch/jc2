#!/usr/bin/env python3
"""Bounded probe of delta2's omitted at-level double-root location."""
import importlib.util
import json
from math import comb
from pathlib import Path
import sys
import sympy as S

here=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('face_minor_shift_engine',here/'corrected_face_engine.py')
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
h,vs=m.h3_template()
alpha,rho=S.symbols('minor_a2 rho')
raw=m.local_rows(h,'delta2',9,exact_only=False)
shifted={}
for (n,k),value in raw.items():
    for q in range(k+1):
        shifted[(n,q)]=shifted.get((n,q),0)+value*comb(k,q)*alpha**(k-q)
want={(9,2):3*rho,(9,3):1}
labels=sorted(set(shifted)|set(want))
equations=[(f'local_{n}_{k}',S.expand(shifted.get((n,k),0)-want.get((n,k),0))) for n,k in labels]
residual,mapping,pivots,zero=m.qstar_reduce(equations,set(vs))
assert not residual
assert all(m.substitute_map(row,mapping)==0 for _,row in equations)
record={
 'status':'PASS','branch':'delta2','substitution':'y=jet0+u*t+(minor_a2+zeta)*t^2',
 'target':'zeta^2*(zeta+3*rho)','raw_rows':len(equations),'pivots':len(pivots),
 'residual':[],'zeros':zero,
 'free_h_coefficients':sorted(str(v) for v in set(vs) if v not in mapping),
 'new_parameter':'minor_a2',
 'mapping':{str(v):str(S.factor(rhs)) for v,rhs in mapping.items()},
}
print(json.dumps(record,indent=2,sort_keys=True))
