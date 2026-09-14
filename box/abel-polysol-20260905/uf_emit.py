#!/usr/bin/env python3
"""Emit the terminal rows E_2..E_2t DIRECTLY from (UF) = P*Hdiff - Rfree (not from eq. (1)),
by the top-down unit-pivot recurrence, as a Singular script; then compare with the frozen
controls_t{t}_raw.sing rows of box/k16xempty-20260905 under the identity map on (c_i, b),
and (optionally) run the exact std to test T, T^2 in J.  Usage: uf_emit.py t [--std]
"""
import argparse, subprocess, sys
from pathlib import Path
a = argparse.ArgumentParser(); a.add_argument('t', type=int); a.add_argument('--std', action='store_true')
a.add_argument('--prime', type=int, default=0); a.add_argument('--droot', type=int, default=0)
a = a.parse_args(); t=a.t; N=t+1; q=2*t+1
HERE = Path(__file__).resolve().parent
cs=[f'c{i}' for i in range(1,t)]; ws=[f'w{i}' for i in range(1,q)]
if a.prime:
    co=str(a.prime); rel=f'number d={a.droot};'
    assert (3*a.droot*a.droot-N) % a.prime == 0
else:
    co='(0,d)'; rel=f'minpoly=3*d^2-{N};'
frozen = Path('/home/ubuntu/jc2/box/k16xempty-20260905')/f'controls_t{t}_raw.sing'
s=[f'ring r={co},(x,{",".join(cs)},b,B,eta,{",".join(ws)}),dp;', rel, 'option(redSB);',
'proc must(int ok,string msg){ if(!ok){print("FAIL "+msg);quit;} }',
'proc xc(poly f,int k){matrix m=coef(f,x);int i;for(i=1;i<=ncols(m);i++){if(deg(m[1,i])==k){return(m[2,i]);}}return(poly(0));}',
f'number y=(d+{N})/{2*q}; number om=1/(4*y^2*(2*d+1));',
f'poly C=x^{t-1}'+''.join(f'+c{i}*x^{t-1-i}' for i in range(1,t))+';',
f'poly W=om*x^{q}-B'+''.join(f'+w{i}*x^{i}' for i in range(1,q))+';',
'poly L=x^2*C/y-b; poly P=x*W-(b^2)/4;',
'poly Hdiff=2*x*diff(P,x)-3*P-B*x+(3/2)*L*(L+b);',
'poly Rfree=(3/16)*(L^2)*(L*(L+2*b)-4*B*x)-eta*x^2*(b*L/2+B*x);',
'poly UF=P*Hdiff-Rfree;',
'// jets: eta is W\'(0)=w1',
'UF=subst(UF,eta,w1); W=subst(W,eta,w1);',
f'must(xc(UF,{4*N})==0,"top");',
'poly band,piv,val; poly solB;']
for v,k in zip(list(reversed(ws))+['B'], range(4*N-1, 2*N, -1)):
    s += [f'band=xc(UF,{k}); piv=diff(band,{v});',
          f'must(deg(piv)==0 && piv!=0,"pivot_{v}");',
          f'val=-subst(band,{v},0)/piv; UF=subst(UF,{v},val); W=subst(W,{v},val);',
          f'print("UFPIVOT {v} "+string(piv));']
    if v=='B': s+=['solB=val;']
s += ['must(xc(UF,0)==0 && xc(UF,1)==0 && xc(UF,2)==0 && xc(UF,3)==0,"low_four");',
      f'for(int k={2*N+1};k<={4*N};k++){{must(xc(UF,k)==0,"high");}}',
      'poly etasol=xc(W,1); poly target=solB*etasol; ideal rows;',
      f'for(k=2;k<={2*t};k++){{rows[k-1]=xc(UF,k+2);}}   // E_k = [x^(k+2)](P Hdiff - Rfree) = [x^k]F',
      f'ring rsmall={co},({",".join(cs)},b),wp({",".join(map(str,list(range(1,t))+[t+1]))});', rel,
      'ideal rows=imap(r,rows); poly target=imap(r,target); poly Bsol=imap(r,solB); poly eta=imap(r,etasol);',
      'print("UF_ROWS_BUILT nrows="+string(size(rows)));']
if not a.prime:
    frz = frozen.read_text()
    frz = frz.replace('ring rsmall=','ring rfro=').replace('ideal rows=','ideal rows_fro=').replace('poly Bsol=','poly B_fro=').replace('poly eta=','poly eta_fro=').replace('poly target=','poly T_fro=')
    s += ['// ---- custody: frozen rows of box/k16xempty-20260905 (identifiers renamed, bytes otherwise unchanged) ----']
    s += frz.splitlines()
    s += ['setring rsmall;',
          'ideal rows_f=imap(rfro,rows_fro); poly B_f=imap(rfro,B_fro); poly eta_f=imap(rfro,eta_fro); poly T_f=imap(rfro,T_fro);',
          'int i; int same=1; for(i=1;i<=size(rows);i++){ if(rows[i]-rows_f[i]!=0){same=0; print("ROW_MISMATCH "+string(i));} }',
          'print("CUSTODY rows_equal="+string(same)+" B_equal="+string(Bsol-B_f==0)+" eta_equal="+string(eta-eta_f==0)+" target_equal="+string(target-T_f==0)+" nrows_frozen="+string(size(rows_f)));']
if a.std:
    s += ['ideal gg=std(rows); print("STD_DONE dim="+string(dim(gg))+" vdim="+string(vdim(gg)));',
          'print("T_in_J="+string(reduce(target,gg)==0)); print("T2_in_J="+string(reduce(target^2,gg)==0));',
          'print("B_in_J="+string(reduce(Bsol,gg)==0)); print("eta_in_J="+string(reduce(eta,gg)==0));',
          'print("B2_in_J="+string(reduce(Bsol^2,gg)==0)); print("eta2_in_J="+string(reduce(eta^2,gg)==0));']
s += ['print("UF_EMIT_DONE"); quit;']
lab=f't{t}'+(f'_p{a.prime}_d{a.droot}' if a.prime else '')
(HERE/f'uf_emit_{lab}.sing').write_text('\n'.join(s)+'\n')
print(HERE/f'uf_emit_{lab}.sing')
