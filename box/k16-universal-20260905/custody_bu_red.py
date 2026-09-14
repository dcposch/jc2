#!/usr/bin/env python3
"""EXACT custody of the universal x=0 recursion at index t, with every numerator reduced modulo std(J) as it is built.

Same top-down replay and frozen-row comparison as custody_bu.py.  Then, in S = k[c,b] (exact field (0,d), minpoly),
J = (E_2..E_2t), gg = std(J), and the numerator recursion
    N_k = (2/(k-3)) [ (k-3) sum N_i N_{k-i} b^{..} + sum G_i N_{k-i} b^{..} - R_k b^{..} ]
is run with N_k := reduce(N_k, gg) at every step.  Because J is an ideal, (N_k mod J) computed from the (N_i mod J)
equals N_k mod J; so the memberships  b^{2(k-3)} P^TD_k - N_k in J (k<=2N)  and  N_k in J (2N<k<=4N)  are decided
exactly, and the minimal b-power is searched as before.  Usage: custody_bu_red.py t
"""
import argparse
from pathlib import Path
a = argparse.ArgumentParser(); a.add_argument('t', type=int); a = a.parse_args(); t=a.t; N=t+1; q=2*t+1
HERE = Path(__file__).resolve().parent
cs=[f'c{i}' for i in range(1,t)]; ws=[f'w{i}' for i in range(1,q)]
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
'UF=subst(UF,eta,w1); W=subst(W,eta,w1);',
f'must(xc(UF,{4*N})==0,"top");',
'poly band,piv,val; poly solB;']
for v,k in zip(list(reversed(ws))+['B'], range(4*N-1, 2*N, -1)):
    s += [f'band=xc(UF,{k}); piv=diff(band,{v});',
          f'must(deg(piv)==0 && piv!=0,"pivot_{v}");',
          f'val=-subst(band,{v},0)/piv; UF=subst(UF,{v},val); W=subst(W,{v},val);']
    if v=='B': s+=['solB=val;']
s += ['must(xc(UF,0)==0 && xc(UF,1)==0 && xc(UF,2)==0 && xc(UF,3)==0,"low_four");',
      f'for(int k={2*N+1};k<={4*N};k++){{must(xc(UF,k)==0,"high");}}',
      'poly etasol=xc(W,1); poly w2sol=xc(W,2); poly target=solB*etasol; ideal rows;',
      f'for(k=2;k<={2*t};k++){{rows[k-1]=xc(UF,k+2);}}',
      f'list PTD; for(k=0;k<={2*N};k++){{PTD[k+1]=xc(x*W-(b^2)/4,k);}}',
      'poly G=(3/2)*L*(L+b)-B*x; G=subst(G,B,solB);',
      'poly R=(3/16)*(L^2)*(L*(L+2*b)-4*B*x); R=subst(R,B,solB); R=R-etasol*x^2*(b*L/2+solB*x);',
      f'list Gl; list Rl; for(k=0;k<={4*N};k++){{Gl[k+1]=xc(G,k); Rl[k+1]=xc(R,k);}}',
      f'ring rsmall={co},({",".join(cs)},b),wp({",".join(map(str,list(range(1,t))+[t+1]))});', rel, 'option(redSB);',
      'ideal rows=imap(r,rows); poly target=imap(r,target); poly Bsol=imap(r,solB); poly eta=imap(r,etasol); poly w2=imap(r,w2sol);',
      'list PTD=imap(r,PTD); list Gl=imap(r,Gl); list Rl=imap(r,Rl);',
      f'number y=(d+{N})/{2*q}; poly Lpivot=4*eta+3*b*c{t-1}/y;',
      'print("ROWS_BUILT nrows="+string(size(rows)));']
frz = frozen.read_text()
frz = frz.replace('ring rsmall=','ring rfro=').replace('ideal rows=','ideal rows_fro=').replace('poly Bsol=','poly B_fro=').replace('poly eta=','poly eta_fro=').replace('poly target=','poly T_fro=')
s += ['// ---- custody: frozen rows (identifiers renamed only) ----'] + frz.splitlines()
s += ['setring rsmall;',
      'ideal rows_f=imap(rfro,rows_fro); poly B_f=imap(rfro,B_fro); poly eta_f=imap(rfro,eta_fro); poly T_f=imap(rfro,T_fro);',
      'int i; int same=1; for(i=1;i<=size(rows);i++){ if(rows[i]-rows_f[i]!=0){same=0; print("ROW_MISMATCH "+string(i));} }',
      'print("CUSTODY rows_equal="+string(same)+" B_equal="+string(Bsol-B_f==0)+" eta_equal="+string(eta-eta_f==0)+" target_equal="+string(target-T_f==0));',
      'int tt=timer; ideal gg=std(rows); print("STD_DONE dim="+string(dim(gg))+" vdim="+string(vdim(gg))+" time="+string(timer-tt));',
      'print("T_in_J="+string(reduce(target,gg)==0)+" T2_in_J="+string(reduce(target^2,gg)==0));',
      f'list NB; intvec ee; for(k=0;k<={4*N};k++){{NB[k+1]=poly(0); ee[k+1]=0;}}',
      'NB[1]=-(b^2)/4; NB[2]=-Bsol; NB[3]=eta; NB[4]=w2;',
      f'for(k=4;k<={4*N};k++){{ee[k+1]=2*(k-3);}}',
      'poly acc; poly dif; int m;',
      f'for(k=4;k<={4*N};k++){{',
      '  acc=0;',
      '  for(i=1;i<=k-1;i++){ acc=acc+(k-3)*NB[i+1]*NB[k-i+1]*b^(2*(k-4)-ee[i+1]-ee[k-i+1]); }',
      '  for(i=1;i<=k;i++){ acc=acc+Gl[i+1]*NB[k-i+1]*b^(2*(k-4)-ee[k-i+1]); }',
      '  acc=acc-Rl[k+1]*b^(2*(k-4));',
      '  NB[k+1]=reduce(acc*2/(k-3),gg);',
      f'  if(k<={2*N}){{ dif=reduce(b^(2*(k-3))*PTD[k+1]-NB[k+1],gg); }} else {{ dif=NB[k+1]; }}',
      '  m=0; while(reduce(b^m*dif,gg)!=0 && m<=60){m++;}',
      '  print("BU_MEMBERSHIP_EXACT k="+string(k)+" nf_terms="+string(size(NB[k+1]))+" min_bpower="+string(m)+" (m>60 means not found)");',
      '}',
      'print("LPIVOT_in_J="+string(reduce(Lpivot,gg)==0)+" LPIVOT_terms="+string(size(Lpivot))+" LPIVOT_wt="+string(deg(Lpivot)));',
      'm=1; while(reduce(Lpivot^m,gg)!=0 && m<=40){m++;} print("LPIVOT_power_in_J="+string(m));',
      'm=1; while(reduce(Bsol^m,gg)!=0 && m<=40){m++;} print("B_power_in_J="+string(m));',
      'm=1; while(reduce(eta^m,gg)!=0 && m<=40){m++;} print("eta_power_in_J="+string(m));',
      'm=1; while(reduce(b^m,gg)!=0 && m<=60){m++;} print("b_power_in_J="+string(m));',
      'print("CUSTODY_BU_RED_DONE"); quit;']
(HERE/f'custody_bu_red_t{t}.sing').write_text('\n'.join(s)+'\n'); print(HERE/f'custody_bu_red_t{t}.sing')
