#!/usr/bin/env python3
"""Dual (L-eliminated) chart of (UF) at index t, b=1, modular or exact, emitted as Singular.

Rows x^k of (theta-3)P^2 + G P - R for k>=4 are linear in P_k (pivot -(k-3)/2 at b=1) AND, for k>=5, linear in
l_{k-2} with the k-INDEPENDENT pivot -(1/4)(4 eta + 3 l_2)  (l_{k-1}, l_k cancel).  Chart: unknowns
B, eta, l2, P3, P5, .., P_{N+2}, and u with u*(4 eta + 3 l2) = 1;  l_N = 1/y imposed from the start;
row 4 -> P4;  rows 5..N+1 -> l3..l_{N-1};  rows N+3..2N -> P_{N+3}..P_{2N};  conditions: row N+2, rows 2N+1..4N.
Expected at t with (V0): UNIT.  Negative controls: drop the u-equation (pivot locus not excluded) and/or drop rows.
Usage: dual_chart.py t [--prime p --droot r]
"""
import argparse
from pathlib import Path
a=argparse.ArgumentParser(); a.add_argument('t',type=int); a.add_argument('--prime',type=int,default=0); a.add_argument('--droot',type=int,default=0)
a=a.parse_args(); t=a.t; N=t+1
HERE=Path(__file__).resolve().parent
if a.prime: co=str(a.prime); rel=f'number d={a.droot};'; assert (3*a.droot**2-N)%a.prime==0
else: co='(0,d)'; rel=f'minpoly=3*d^2-{N};'
lvars=[f'l{j}' for j in range(2,N)]          # l2..l_{N-1}
pvars=[f'P{k}' for k in range(3,2*N+1)]      # P3..P_{2N}
s=[f'ring r={co},(x,B,eta,{",".join(lvars)},{",".join(pvars)},u),dp;', rel, 'option(redSB);',
'proc must(int ok,string msg){ if(!ok){print("FAIL "+msg);quit;} }',
'proc xc(poly f,int k){matrix m=coef(f,x);int i;for(i=1;i<=ncols(m);i++){if(deg(m[1,i])==k){return(m[2,i]);}}return(poly(0));}',
f'number y=(d+{N})/{2*(2*N-1)}; number om=1/(4*y^2*(2*d+1));',
f'poly L=-1+x^{N}/y'+''.join(f'+l{j}*x^{j}' for j in range(2,N))+';   // b=1, l_N=1/y',
f'poly P=-1/4-B*x+eta*x^2'+''.join(f'+P{k}*x^{k}' for k in range(3,2*N+1))+';',
'poly G=(3/2)*L*(L+1)-B*x;',
'poly R=(3/16)*(L^2)*(L*(L+2)-4*B*x)-eta*x^2*(L/2+B*x);',
'poly UF=x*diff(P^2,x)-3*P^2+G*P-R;',
'must(xc(UF,0)==0 && xc(UF,1)==0 && xc(UF,2)==0 && xc(UF,3)==0,"low_four");',
'poly Lpiv=4*eta+3*l2; poly band,piv,val;',
'// row 4 -> P4',
'band=xc(UF,4); piv=diff(band,P4); must(deg(piv)==0 && piv!=0,"pivP4"); val=-subst(band,P4,0)/piv; UF=subst(UF,P4,val); print("P4 solved");']
for k in range(5, N+2):   # rows 5..N+1 -> l3..l_{N-1}
    j=k-2
    s += [f'band=xc(UF,{k}); piv=diff(band,l{j}); must(piv+Lpiv/4==0,"Lpivot_row{k}"); val=-subst(band,l{j},0)*4*u; UF=subst(UF,l{j},val); print("l{j} solved via u");']
for k in range(N+3, 2*N+1):  # rows N+3..2N -> P_k
    s += [f'band=xc(UF,{k}); piv=diff(band,P{k}); must(deg(piv)==0 && piv!=0,"pivP{k}"); val=-subst(band,P{k},0)/piv; UF=subst(UF,P{k},val); print("P{k} solved");']
s += [f'ideal Jd=xc(UF,{N+2}); int k; for(k={2*N+1};k<={4*N};k++){{Jd=Jd,xc(UF,k);}}',
      'ideal Jfull=Jd,u*Lpiv-1;',
      f'ring rs={co},(B,eta,{",".join(lvars)},{",".join(pvars)},u),dp;', rel,
      'ideal Jfull=imap(r,Jfull); ideal Jd=imap(r,Jd);',
      'int tt=timer; ideal g=std(Jfull); print("DUAL_FULL dim="+string(dim(g))+" unit="+string(size(g)==1 && deg(g[1])==0)+" time="+string(timer-tt));',
      'tt=timer; ideal g0=std(Jd); print("DUAL_NO_U (pivot locus not excluded) dim="+string(dim(g0))+" unit="+string(size(g0)==1 && deg(g0[1])==0)+" time="+string(timer-tt));',
      f'ideal Jneg=Jfull[1..{t+1}],u*imap(r,Lpiv)-1; tt=timer; ideal gn=std(Jneg); print("DUAL_NEGCTRL_first_{t+1}_conditions dim="+string(dim(gn))+" unit="+string(size(gn)==1 && deg(gn[1])==0)+" time="+string(timer-tt));',
      'print("DUAL_DONE"); quit;']
lab=f't{t}'+(f'_p{a.prime}_d{a.droot}' if a.prime else '')
(HERE/f'dual_chart_{lab}.sing').write_text('\n'.join(s)+'\n'); print(HERE/f'dual_chart_{lab}.sing')
