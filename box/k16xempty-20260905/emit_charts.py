#!/usr/bin/env python3
"""Construct the two literal X charts from fresh, direct F3 reconstruction.

The source raw file is emitted by the hash-checked controls_emit_direct.py.
All coefficient extraction and polynomial identities run over characteristic 0.
"""
import argparse
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('t',type=int)
p.add_argument('--d',type=int)
a=p.parse_args()
t=a.t
root=Path(__file__).resolve().parent
label=f't{t}'+('' if a.d is None else f'_d{a.d}')
co='(0,d)' if a.d is None else '0'
rel=f'minpoly=3*d^2-{t+1};' if a.d is None else f'number d={a.d};'
cs=','.join(f'c{i}' for i in range(1,t))
raw=root/f'controls_{label}_raw.sing'
checks='''
proc must(int ok,string msg){if(!ok){print("FAIL "+msg);quit;}}
proc bd(poly f){if(f==0){return(0);}matrix cf=coef(f,b);int j;int dd=0;intvec ex;for(j=1;j<=ncols(cf);j++){ex=leadexp(cf[1,j]);if(ex[nvars(basering)]>dd){dd=ex[nvars(basering)];}}return(dd);}
proc clearb(poly f,poly aa,poly dd,int m){if(f==0){return(poly(0));}matrix cf=coef(f,b);int j,e;intvec ex;poly out=0;for(j=1;j<=ncols(cf);j++){ex=leadexp(cf[1,j]);e=ex[nvars(basering)];out=out+cf[2,j]*aa^e*dd^(m-e);}return(out);}
poly MM=subst(Bsol,b,0); poly NN=diff(Bsol,b);
poly rho=subst(eta,b,0); poly sigma=diff(eta,b);
must(diff(NN,b)==0 && diff(sigma,b)==0,"affine_b");
must(Bsol==MM+b*NN && eta==rho+b*sigma,"affine_maps");
poly Delta=NN-sigma; poly AA=rho-MM; poly HH=NN*rho-MM*sigma;
must(Delta*Bsol-HH==NN*(b*Delta-AA),"B_slice_identity");
must(Delta*eta-HH==sigma*(b*Delta-AA),"eta_slice_identity");
must(HH==NN*AA+MM*Delta,"H_identity");
ideal cleared; intvec bdegrees; int k,dd;
for(k=1;k<=size(rows);k++){
 dd=bd(rows[k]); bdegrees[k]=dd;
 must(dd<=3,"cubic_b_bound");
 cleared[k]=clearb(rows[k],AA,Delta,dd);
 must(diff(cleared[k],b)==0,"cleared_independent_b");
}
print("MAP_IDENTITIES_PASS"); print("B_DEGREES="+string(bdegrees));
print("B_TERMS="+string(size(Bsol))); print("ETA_TERMS="+string(size(eta)));
print("DELTA_TERMS="+string(size(Delta))); print("A_TERMS="+string(size(AA)));
print("H_TERMS="+string(size(HH)));
for(k=1;k<=size(cleared);k++){print("CLEARED_ROW "+string(k+1)+" weightmax="+string(deg(cleared[k]))+" terms="+string(size(cleared[k])));}
'''
s=raw.read_text()+checks
for v in ['MM','NN','rho','sigma','Delta','AA','HH']:
    s+=f'write("{root}/{label}_chart_data.txt","poly {v}="+string({v})+";");\n'
s+=f'write("{root}/{label}_chart_data.txt","intvec bdegrees="+string(bdegrees)+";");\n'
s+=f'write("{root}/{label}_main_prelude.sing","ring rmain={co},({cs},u),dp;");\n'
s+=f'write("{root}/{label}_main_prelude.sing","{rel}");\n'
s+=f'write("{root}/{label}_main_prelude.sing","ideal cleared="+string(cleared)+";");\n'
s+=f'write("{root}/{label}_main_prelude.sing","poly Delta="+string(Delta)+"; poly HH="+string(HH)+";");\n'
s+=f'write("{root}/{label}_boundary_prelude.sing","ring rboundary={co},({cs},b,s),dp;");\n'
s+=f'write("{root}/{label}_boundary_prelude.sing","{rel}");\n'
s+=f'write("{root}/{label}_boundary_prelude.sing","ideal rows="+string(rows)+";");\n'
s+=f'write("{root}/{label}_boundary_prelude.sing","poly Bsol="+string(Bsol)+";");\n'
s+=f'write("{root}/{label}_boundary_prelude.sing","poly Delta="+string(Delta)+"; poly AA="+string(AA)+";");\n'
s+='print("CHARTS_EMITTED"); quit;\n'
for suffix in ['_chart_data.txt','_main_prelude.sing','_boundary_prelude.sing']:
    (root/(label+suffix)).unlink(missing_ok=True)
(root/(label+'_emit_charts.sing')).write_text(s)
print(root/(label+'_emit_charts.sing'))
