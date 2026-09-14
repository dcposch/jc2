#!/usr/bin/env python3
"""Emit direct F1--F3 exact coefficient elimination; no spine formulas imported."""
import argparse
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('t', type=int)
p.add_argument('--d', type=int)
p.add_argument('--prime', type=int)
p.add_argument('--droot', type=int)
p.add_argument('--raw-only', action='store_true')
p.add_argument('--root', default='box/k16f3abel-20260905')
a = p.parse_args()
t=a.t; q=2*t+1
label=f't{t}'+(f'_p{a.prime}_d{a.droot}' if a.prime else (f'_d{a.d}' if a.d is not None else ''))
root=Path(a.root).resolve()
cs=[f'c{i}' for i in range(1,t)]
ws=[f'w{i}' for i in range(1,q)]
co='0' if a.d is not None else '(0,d)'
rel=f'number d={a.d};' if a.d is not None else f'minpoly=3*d^2-{t+1};'
if a.prime:
    assert a.droot is not None and (3*a.droot*a.droot-t-1)%a.prime==0
    co=str(a.prime); rel=f'number d={a.droot};'
for suffix in ('_raw.sing','_W.txt','_gb.txt'):
    (root/f'controls_{label}{suffix}').unlink(missing_ok=True)
s=[f'ring r={co},(x,{",".join(cs)},b,B,{",".join(ws)}),dp;',rel,
'option(redSB);',
'proc must(int ok,string msg){ if(!ok){print("FAIL "+msg);quit;} }',
'proc xc(poly f,int k){matrix m=coef(f,x);int i;for(i=1;i<=ncols(m);i++){if(deg(m[1,i])==k){return(m[2,i]);}}return(poly(0));}',
f'number y=(d+{t+1})/{2*q}; number om=3*(2*d-1)/(4*y^2*{4*t+1});',
f'poly C=x^{t-1}'+''.join(f'+c{i}*x^{t-1-i}' for i in range(1,t))+';',
f'poly W=om*x^{q}-B'+''.join(f'+w{i}*x^{i}' for i in range(1,q))+';',
'poly A=3*x^3*C^2/(4*y^2); poly D=3*b*x*C/(2*y); poly K=x^2*C-y*b; poly eta=w1;',
'poly rhs=W^2+(B-2*A+D)*W+A*(A-D)/3-B*(A-D)-b*eta*K/(2*y)-B*eta*x+(b^2*A/2-b^2*(B+W))/x;',
'poly ff=2*(x*W-(b^2)/4)*diff(W,x)-rhs;',
f'must(xc(ff,{2*q})==0,"leading");',
'poly band,piv,val; poly solB;']
for v,k in zip(list(reversed(ws))+['B'],range(2*q-1,q-1,-1)):
    s += [f'band=xc(ff,{k}); piv=diff(band,{v});',
          f'must(deg(piv)==0 && piv!=0,"pivot_{v}");',
          f'val=-subst(band,{v},0)/piv; ff=subst(ff,{v},val); W=subst(W,{v},val);',
          f'print("PIVOT {v} "+string(piv));']
    if v=='B':s+=['solB=val;']
s += ['must(xc(ff,0)==0 && xc(ff,1)==0,"low_two");',
      f'for(int k={q};k<={2*q};k++){{must(xc(ff,k)==0,"high");}}',
      'eta=xc(W,1); poly target=solB*eta; ideal rows;',
      f'write("{root}/controls_{label}_W.txt",string(W));',
      f'for(k=2;k<{q};k++){{rows[k-1]=xc(ff,k);}}',
      f'write("{root}/controls_{label}_raw.sing","// Direct F1--F3; coefficient map is identity on c_i,b.");',
      f'write("{root}/controls_{label}_raw.sing","ring rsmall={co},({",".join(cs)},b),wp({",".join(map(str,list(range(1,t))+[t+1]))});");',
      f'write("{root}/controls_{label}_raw.sing","{rel}");',
      f'write("{root}/controls_{label}_raw.sing","ideal rows="+string(rows)+";");',
      f'write("{root}/controls_{label}_raw.sing","poly Bsol="+string(solB)+";");',
      f'write("{root}/controls_{label}_raw.sing","poly eta="+string(eta)+";");',
      f'write("{root}/controls_{label}_raw.sing","poly target="+string(target)+";");',
      f'ring rsmall={co},({",".join(cs)},b),wp({",".join(map(str,list(range(1,t))+[t+1]))});',rel,
      'ideal rows=imap(r,rows); poly target=imap(r,target); poly Bsol=imap(r,solB); poly eta=imap(r,eta);',
      'print("ROWS_BUILT"); print("Bsol_terms="+string(size(Bsol))); print("eta_terms="+string(size(eta)));',
      'ideal gg=std(rows); print("GB_DONE dim="+string(dim(gg))+" vdim="+string(vdim(gg)));',
      'print("target_zero="+string(reduce(target,gg)==0)); print("target2_zero="+string(reduce(target^2,gg)==0));',
      f'write("{root}/controls_{label}_gb.txt",string(gg));',
      'if(nvars(basering)==2){print("GB="+string(gg));}',
      'print("DIRECT_CONTROL_DONE"); quit;']
if a.raw_only:
    cut=next(i for i,line in enumerate(s) if line.startswith('ideal gg=std(rows);'))
    s=s[:cut]+['print("DIRECT_RAW_DONE"); quit;']
(root/f'controls_{label}.sing').write_text('\n'.join(s)+'\n')
print(root/f'controls_{label}.sing')
