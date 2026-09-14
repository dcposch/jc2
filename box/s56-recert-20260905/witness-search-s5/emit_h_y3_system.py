#!/usr/bin/env python3
"""Emit the fully supported h=y^3 S5 [2] subchart after exact P elimination."""
from pathlib import Path
import argparse,contextlib,importlib.util
import sympy as s

ap=argparse.ArgumentParser();ap.add_argument('--characteristic',type=int,default=32003);ns=ap.parse_args()
HERE=Path(__file__).resolve().parent
with open('/dev/null','w') as f,contextlib.redirect_stdout(f):
 z=importlib.util.spec_from_file_location('hy',HERE/'h_y3_distribution.py');hy=importlib.util.module_from_spec(z);z.loader.exec_module(hy)
x=s.symbols('x')
b2v=s.symbols('u0:7');b1v=s.symbols('v0:8');b0v=s.symbols('w1:10')
b2=sum(a*x**i for i,a in enumerate(b2v));b1=sum(a*x**i for i,a in enumerate(b1v));b0=sum(b0v[i-1]*x**i for i in range(1,10))
cc,T=s.symbols('c T')
sub={hy.b2:b2,hy.b1:b1,hy.b0:b0,hy.d2:s.diff(b2,x),hy.d1:s.diff(b1,x),hy.d0:s.diff(b0,x)}
forms=[s.cancel(z.subs(sub)) for z in hy.forms];forms[-1]=s.expand(forms[-1]-cc*x**8)
eq=[]
for form in forms:
 for z in s.Poly(form,x).all_coeffs():
  num=s.cancel(z).as_numer_denom()[0]
  if num!=0:eq.append(s.expand(num))
params=[hy.a7,hy.a8,hy.k5,hy.k4,hy.k3,hy.k2,hy.k1]
vars=list(b2v)+list(b1v)+list(b0v)+params+[cc,T]
ss=lambda z:str(z).replace('**','^')
tag=f'p{ns.characteristic}';ms=HERE/f'h_y3_full_{tag}.ms'
all_eq=[ss(z) for z in eq]+['T*c-1']
ms.write_text(','.join(map(str,vars))+'\n'+str(ns.characteristic)+'\n'+'\n'.join(z+(',' if i+1<len(all_eq) else '') for i,z in enumerate(all_eq))+'\n')
sing=HERE/f'h_y3_full_{tag}.sing'
sing.write_text(f'ring r={ns.characteristic},('+','.join(map(str,vars))+'),dp;\noption(redSB);\nideal I='+',\n'.join(all_eq)+';\nint tt=timer; ideal G=std(I); print("TIME="+string(timer-tt)); print("SIZE="+string(size(G))); print("DIM="+string(dim(G))); if(reduce(1,G)==0){print("UNIT=1");}else{print("UNIT=0");}; G; quit;\n')
print({'variables':len(vars),'equations':len(all_eq),'ms':str(ms),'sing':str(sing)})
