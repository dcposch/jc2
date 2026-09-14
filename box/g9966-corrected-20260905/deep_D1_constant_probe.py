#!/usr/bin/env python3
"""Exact Pi^0 coefficient of derived D1 Jacobian: full saved minor locus."""
import sys,json,time
from pathlib import Path
import sympy as s
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'run-code-source-full'))
import engine as E
from source_data import SOURCE as S
from math import comb
outer,_,_=E.outer_state(-1)
for branch,phase in [('delta2','0117'),('delta52','0239')]:
 q=json.loads((HERE/f'results-source-full/source-full-{branch}_phase{phase}.json').read_text())
 mapping={s.Symbol(v):s.sympify(value) for v,value in q['map_after'].items()}
 cover,base,child=S['D1_substitution']
 def coeff(name,k):
  threshold=S['outer_specs'][name][2]
  raw=sum(value*comb(p,k) for (r,p),value in outer[name].items() if p>=k and cover*r+base*p+(child-base)*k==threshold)
  return E.substitute_map(raw,mapping)
 b0=coeff('A3',0);d0=coeff('B2',1)
 # Generic H begins at Pi^2, a at Pi^1,c at Pi^2 by source lattice,
 # hence P0=b0 and Qprime0=d0, and Pprime0=Q0=0.
 print(branch,'b0=',b0,'d0=',d0,flush=True)
 out={'branch':branch,'b0':str(b0),'d0':str(d0),'Jface_Pi0':str(s.factor(b0*d0/3)),
      'derivation':'P=H^3+aH+b,Q=H^2+cH+d; H divisiblePi^2,a,d divisiblePi,c divisiblePi^2,b inQ[Pi^3]; (3PQprime-2PprimeQ)/9 atPi0=b0*d0/3'}
 (HERE/f'deep_D1_constant_{branch}.json').write_text(json.dumps(out,indent=2)+'\n')
