#!/usr/bin/env python3
"""Emit exact Singular reconstruction from frozen tail_structure.py formulas.

Independent translation uses polynomials in L, then translates to h and solves
the weight-ordered scalar pivots. No previous lane's generated rows are read.
"""
import argparse
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('t', type=int)
ap.add_argument('--d', choices=['-1', '1'])
ap.add_argument('--prime', type=int)
ap.add_argument('--droot', type=int)
ap.add_argument('--out', required=True)
args = ap.parse_args()
t = args.t
q = 2*t+1
e = 3*t+1
assert t >= 2
assert (t == 2) == (args.d is not None) or args.prime
us = [f'u{i}' for i in range(2,2*t+1)]
cs = [f'c{i}' for i in range(1,t)]
resid = ['b4']+[f'u{i}' for i in range(2,t)]+['b3']
high = cs+[f'u{i}' for i in range(t,2*t+1)]+['b2']
out = Path(args.out).resolve()
coeff = '0' if args.d else '(0,d)'
rel = f'number d={args.d};' if args.d else f'minpoly=3*d^2-{t+1};'
if args.prime:
    assert args.droot is not None
    assert (3*args.droot**2-t-1)%args.prime==0
    coeff=str(args.prime)
    rel=f'number d={args.droot};'
def say(s): print(s)
say(f'ring rgen={coeff},(h,b4,b3,b2,{",".join(us+cs)}),dp;')
say(rel)
say('option(redSB);')
say('proc must(int ok,string label) { if (!ok) { print("FAIL "+label); quit; } }')
# coef groups by powers of h in one pass; avoid quadratic indexing of terms.
say('proc hco(poly f,int k) { matrix mm=coef(f,h); int ii; for(ii=1;ii<=ncols(mm);ii++) { if(deg(mm[1,ii])==k) { return(mm[2,ii]); } } return(poly(0)); }')
say(f'number y=(d+{t+1})/{2*q}; number g={e*t}*(3*d+{2*(t+1)})/{6*q**3};')
say(f'poly U=(h+b4)^{q}'+''.join(f'+u{i}*(h+b4)^{q-i}' for i in range(2,2*t+1))+';')
say(f'poly C=(h+b4)^{t-1}'+''.join(f'+c{i}*(h+b4)^{t-1-i}' for i in range(1,t))+';')
say('poly BB=0; poly SS=0; poly vv; int m; int aa; int bb; poly acc;')
say(f'for(m=0;m<{t};m++) {{ BB=BB+g*(3*m+5)*hco(C,m)*h^(m+1)/(2*y*(m+1)); }}')
say(f'for(m=0;m<={2*t};m++) {{ acc=3*g*(m+1)*hco(U,m+1)+g*b3*(5*m+7)*hco(C,m)/2; for(aa=0;aa<m;aa++) {{ bb=m-1-aa; acc=acc+(3+2*aa-bb)*hco(C,aa)*hco(BB,bb); }} SS=SS+acc*h^m/(y*(2*m+1)); }}')
say('poly VV=h^2*C-y*b3; poly YY=h*SS-b3*BB-g*b2; poly zpiece=h*BB-g*b3;')
say('poly NN=-VV*diff(YY,h)+diff(VV,h)*YY+2*diff(U,h)*zpiece;')
say('poly Nconst=subst(NN,h,0);')
say('poly PP=(NN-subst(NN,h,0))/(2*y*h);')
say('must(2*y*h*PP==NN-subst(NN,h,0),"DIVISION");')
say('poly RR=VV*PP-diff(U,h)*YY-y*g; RR=subst(RR,h,h-b4);')
say('poly band; number pv; poly val;')
for j, v in enumerate(high,1):
    say(f'band=hco(RR,{4*t+1-j}); must(diff(diff(band,{v}),{v})==0,"AFFINE{j}");')
    say(f'must(size(diff(band,{v}))==1 && deg(diff(band,{v}))==0,"SCALAR{j}"); pv=leadcoef(diff(band,{v})); must(pv!=0,"PIVOT{j}");')
    say(f'val=-subst(band,{v},0)/pv; RR=subst(RR,{v},val); print("PIVOT {j} PASS");')
    say(f'U=subst(U,{v},val); C=subst(C,{v},val); BB=subst(BB,{v},val); SS=subst(SS,{v},val); Nconst=subst(Nconst,{v},val);')
say(f'for(m={2*t};m<={4*t+1};m++) {{ must(hco(RR,m)==0,"HIGH_BAND"); }}')
for v in high: say(f'must(diff(RR,{v})==0,"ELIM_{v}");')
say('ideal rows;')
for k in range(2*t): say(f'rows[{k+1}]=-hco(RR,{k});')
say('poly spineB2=val; poly rootR=subst(diff(U,h),h,0)+b3*subst(C,h,0); poly spineB1=-Nconst/(y*g);')
say('must(y*spineB1+b3*rootR==0,"LOCAL_B1");')
say('must(-subst(RR,h,b4)-y*g+g*spineB2*rootR==0,"LOCAL_TAU");')
say('poly abelW=h*SS/g-spineB2-h^2*C*BB/(g*y)-b3*h*C/(2*y)+3*h^3*C^2/(4*y^2);')
say('poly eta=hco(abelW,1); poly bigA=3*h^3*C^2/(4*y^2); poly bigD=3*b3*h*C/(2*y);')
say('must(subst(abelW,h,0)==-spineB2,"ABEL_CONSTANT"); must(eta==3*rootR/y,"ABEL_ETA");')
say('poly abelRhs=abelW^2+(spineB2-2*bigA+bigD)*abelW+bigA*(bigA-bigD)/3-spineB2*(bigA-bigD)-b3*eta*(h^2*C-y*b3)/(2*y)-spineB2*h*eta+(b3^2*bigA/2-b3^2*(spineB2+abelW))/h;')
say('poly abelResidual=2*(h*abelW-(b3^2)/4)*diff(abelW,h)-abelRhs;')
say('must(g*y*abelResidual+3*h*(subst(RR,h,h+b4)-subst(RR,h,b4))==0,"ABEL_ROW_IDENTITY");')
say('print("ABEL_ROW_IDENTITY_PASS");')
say(f'ring rres={coeff},({",".join(resid)}),wp({",".join(map(str,list(range(1,t))+[t+1]))});')
say(rel)
say('ideal rows=imap(rgen,rows);')
say('poly spineB1=imap(rgen,spineB1); poly spineB2=imap(rgen,spineB2); poly rootR=imap(rgen,rootR);')
say(f'number y=(d+{t+1})/{2*q}; number g={e*t}*(3*d+{2*(t+1)})/{6*q**3};')
say('poly tau=rows[1]-y*g;')
say(f'poly ax=rows[{2*t}];')
for v in resid[:-1]: say(f'ax=subst(ax,{v},0);')
say(f'number aexpect=-{t*(3*t+1)}*(({27*t**3-30*t**2+t-2})*d+{6*t**3+13*t**2-3*t+2})/{12*q*q*(3*t-1)**2*(3*t+2)};')
say('must(ax==aexpect*b3^2,"AXIS_ALPHA");')
say('poly zero=tau;')
for v in resid: say(f'zero=subst(zero,{v},0);')
say('must(zero==0,"TAU_CONSTANT");')
say(f'write("{out}","// Generated from frozen coefficient-array formulas; t={t}");')
say(f'write("{out}","ring rres={coeff},({",".join(resid)}),wp({",".join(map(str,list(range(1,t))+[t+1]))});");')
say(f'write("{out}","{rel}");')
for k in range(2*t):
    say(f'write("{out}","poly T{k}="+string(rows[{k+1}])+";");')
say(f'write("{out}","poly tau="+string(tau)+";");')
for name in ['spineB1','spineB2','rootR']:
    say(f'write("{out}","poly {name}="+string({name})+";");')
say('print("LOCAL_IDENTITIES_PASS");')
say('print("ROWS_COMPLETE"); quit;')
