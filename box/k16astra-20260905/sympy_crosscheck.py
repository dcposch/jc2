#!/usr/bin/env python3
"""Direct exact row image check with frozen independent SymPy implementation."""
import sys, importlib.util, re
from pathlib import Path
import sympy as sp
p=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('frozen_tail','/tmp/jc2-lane.vB6DJB/inputs/tail_structure.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
t=int(sys.argv[1]);D=m.build(t)
y=D['y']; d=sp.Symbol('d')
text=(p/f't{t}_rows.sing').read_text()
for k in range(2*t):
    ss=re.search(r'^poly T'+str(k)+r'=(.*);$',text,re.M).group(1)
    expr=sp.sympify(ss.replace('^','**'))
    diff=D['red'](expr.subs(d,2*(2*t+1)*y-(t+1))-D['T'][k])
    assert diff==0,(t,k,diff)
    print(f'SYMPY_IMAGE t={t} k={k} PASS',flush=True)
print('SYMPY_CROSSCHECK_COMPLETE',flush=True)
