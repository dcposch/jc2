#!/usr/bin/env python3
"""Emit the exact centered even-Q/odd-P residual system for Singular."""
from pathlib import Path
import sympy as s
import importlib.util, contextlib
import argparse

ap=argparse.ArgumentParser()
ap.add_argument('--degrees',default='3,6,9')
ap.add_argument('--extra',action='append',default=[])
ap.add_argument('--characteristic',type=int,default=32003)
ns=ap.parse_args()
da,db,dc=map(int,ns.degrees.split(','))
tag=f'd{da}_{db}_{dc}' + (('_'+'_'.join(z.replace('-','m') for z in ns.extra)) if ns.extra else '')
ptag=f'p{ns.characteristic}'
HERE=Path(__file__).resolve().parent
with open('/dev/null','w') as f,contextlib.redirect_stdout(f):
    z=importlib.util.spec_from_file_location('eo',HERE/'even_odd_distribution.py')
    eo=importlib.util.module_from_spec(z);z.loader.exec_module(eo)
x=s.symbols('x')
avec=s.symbols(f'a0:{da+1}'); bvec=s.symbols(f'b0:{db+1}'); cvec=s.symbols(f'q1:{dc+1}')
A=sum(v*x**i for i,v in enumerate(avec))
B=sum(v*x**i for i,v in enumerate(bvec))
C=sum(cvec[i-1]*x**i for i in range(1,dc+1))
cc,T=s.symbols('c T')
sub={eo.A:A,eo.B:B,eo.C:C,eo.dA:s.diff(A,x),eo.dB:s.diff(B,x),eo.dC:s.diff(C,x)}
forms=[s.cancel(z.subs(sub)) for z in eo.forms]
forms[2]=s.expand(forms[2]-cc*x**8)
eq=[]
for form in forms:
    poly=s.Poly(form,x)
    for coeff in poly.all_coeffs():
        num=s.cancel(coeff).as_numer_denom()[0]
        if num!=0:eq.append(s.expand(num))
eq.extend(s.sympify(z,locals={str(v):v for v in list(avec)+list(bvec)+list(cvec)}) for z in ns.extra)
vars=list(avec)+list(bvec)+list(cvec)+[eo.k3,eo.k2,eo.k1,eo.k0,cc,T]
def ss(z): return str(z).replace('**','^')
lines=[f'ring r={ns.characteristic},('+','.join(map(str,vars))+'),dp;','option(redSB);']
lines.append('ideal I='+',\n'.join(ss(z) for z in eq)+',T*c-1;')
lines += ['int t=timer;','ideal G=std(I);','print("TIME="+string(timer-t));','print("SIZE="+string(size(G)));','print("DIM="+string(dim(G)));','if(reduce(1,G)==0){print("UNIT=1");}else{print("UNIT=0");}','G;','quit;']
out=HERE/f'even_odd_{tag}_{ptag}.sing';out.write_text('\n'.join(lines)+'\n')
ms=HERE/f'even_odd_{tag}_{ptag}.ms'
ms_lines=[','.join(map(str,vars)),str(ns.characteristic)]
ms_eq=[ss(z) for z in eq]+['T*c-1']
ms_lines += [z+(',' if i+1<len(ms_eq) else '') for i,z in enumerate(ms_eq)]
ms.write_text('\n'.join(ms_lines)+'\n')
print({'variables':len(vars),'equations':len(eq)+1,'path':str(out),'msolve':str(ms)})
