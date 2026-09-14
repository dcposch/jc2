#!/usr/bin/env python3
"""Bottom-up (x=0, Briot-Bouquet) instrument for (UF), emitted as Singular.

(UF) <=> (theta-3)(P^2) + G*P = R,  G=(3/2)L(L+b)-Bx,  R=Rfree(x,L).
Row x^k:  (k-3)*(P^2)_k + (G P)_k - R_k = 0.  Since G_0=0 and P_0=-(b^2)/4, for k>=4
   P_k = [ (k-3) sum_{i=1}^{k-1} P_i P_{k-i} + sum_{i=1}^{k} G_i P_{k-i} - R_k ] * 2/((k-3) b^2)
with P_1=-B, P_2=eta, P_3=w2 FREE (resonance k=3; row x^3 vanishes identically).
These P_k = Phi_k(b,B,eta,w2,l_2..l_k) are t-INDEPENDENT rational functions (denominator b^{2(k-3)}).
At index t: l_j=0 (j>N), l_N=1/y; polynomial solution <=> Phi_{2N+1}=...=Phi_{4N}=0 (then P_k=0 for all k>4N),
and the top row then forces Phi_{2N} in {omega_+, omega_-}; we add Phi_{2N}=omega (declared factor).
Dehomogenise b=1 (G_m, b has weight N).  Usage: bottom_up.py t [--prime p --droot r]
"""
import argparse
from pathlib import Path
a=argparse.ArgumentParser(); a.add_argument('t',type=int); a.add_argument('--prime',type=int,default=0); a.add_argument('--droot',type=int,default=0)
a=a.parse_args(); t=a.t; N=t+1
HERE=Path(__file__).resolve().parent
cs=[f'c{i}' for i in range(1,t)]
if a.prime: co=str(a.prime); rel=f'number d={a.droot};'; assert (3*a.droot**2-N)%a.prime==0
else: co='(0,d)'; rel=f'minpoly=3*d^2-{N};'
s=[f'ring r={co},(x,{",".join(cs)},B,eta,w2),dp;', rel, 'option(redSB);',
'proc xc(poly f,int k){matrix m=coef(f,x);int i;for(i=1;i<=ncols(m);i++){if(deg(m[1,i])==k){return(m[2,i]);}}return(poly(0));}',
f'number y=(d+{N})/{2*(2*N-1)}; number om=1/(4*y^2*(2*d+1)); number omalt=1/(4*y^2*(1-2*d));',
f'poly C=x^{t-1}'+''.join(f'+c{i}*x^{t-1-i}' for i in range(1,t))+';',
'poly L=x^2*C/y-1;   // b=1',
'poly G=(3/2)*L*(L+1)-B*x;',
'poly R=(3/16)*(L^2)*(L*(L+2)-4*B*x)-eta*x^2*(L/2+B*x);',
f'list Pc; int k; int i; for(k=1;k<={4*N}+1;k++){{Pc[k]=poly(0);}}   // Pc[k+1] = P_k',
'Pc[1]=-1/4; Pc[2]=-B; Pc[3]=eta; Pc[4]=w2;',
'poly acc;',
f'for(k=4;k<={4*N};k++){{',
'  acc=0;',
'  for(i=1;i<=k-1;i++){ acc=acc+(k-3)*Pc[i+1]*Pc[k-i+1]; }',
'  for(i=1;i<=k;i++){ acc=acc+xc(G,i)*Pc[k-i+1]; }',
'  acc=acc-xc(R,k);',
'  Pc[k+1]=acc*2/(k-3);',
'  print("PHI "+string(k)+" terms="+string(size(Pc[k+1]))+" deg="+string(deg(Pc[k+1])));',
'}',
'// residue check: row x^3 vanishes identically',
'acc=0; for(i=1;i<=2;i++){acc=acc+0*Pc[i+1]*Pc[3-i+1];} for(i=1;i<=3;i++){acc=acc+xc(G,i)*Pc[3-i+1];} acc=acc-xc(R,3);',
'print("ROW_X3_RESIDUE_ZERO="+string(acc==0));',
f'ideal J0; for(k={2*N+1};k<={4*N};k++){{J0[k-{2*N}]=Pc[k+1];}}',
f'ideal J1=J0, Pc[{2*N}+1]-om;',
f'ideal J2=J0, Pc[{2*N}+1]-omalt;',
'ring rs='+co+',('+','.join(cs)+',B,eta,w2),dp;', rel,
'ideal J0=imap(r,J0); ideal J1=imap(r,J1); ideal J2=imap(r,J2);',
'int tt=timer;',
'ideal g1=std(J1); print("BOTTOMUP_J1_std dim="+string(dim(g1))+" unit="+string(size(g1)==1 && deg(g1[1])==0)+" time="+string(timer-tt));',
'tt=timer; ideal g0=std(J0); print("BOTTOMUP_J0_std dim="+string(dim(g0))+" unit="+string(size(g0)==1 && deg(g0[1])==0)+" time="+string(timer-tt));',
'tt=timer; ideal g2=std(J2); print("BOTTOMUP_J2_std(other top root) dim="+string(dim(g2))+" unit="+string(size(g2)==1 && deg(g2[1])==0)+" time="+string(timer-tt));',
f'ideal Jneg=J0[1..{t+1}]; ideal gn=std(Jneg); print("NEGCTRL_first_{t+1}_rows dim="+string(dim(gn))+" unit="+string(size(gn)==1 && deg(gn[1])==0));',
'print("BOTTOMUP_DONE"); quit;']
lab=f't{t}'+(f'_p{a.prime}_d{a.droot}' if a.prime else '')
(HERE/f'bottom_up_{lab}.sing').write_text('\n'.join(s)+'\n'); print(HERE/f'bottom_up_{lab}.sing')
