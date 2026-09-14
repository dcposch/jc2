#!/usr/bin/env python3
"""Custody of the universal x=0 recursion against the frozen (UF) top-down data at index t.

Ring (exact): (0,d), minpoly 3d^2-N, variables (x, c1..c_{t-1}, b, B, eta, w1..w_{q-1}); the top-down
(Theorem H) elimination is replayed exactly as in box/abel-polysol-20260905/uf_emit.py (rows x^{4N-1}..x^{2N+1}
solved for w_{q-1}..w_1 and B), giving P^TD, B^TD, eta^TD, and the rows E_k = [x^{k+2}](P Hdiff - Rfree), k=2..2t.
Frozen rows of box/k16xempty-20260905/controls_t{t}_raw.sing are imported and compared (identity map on c_i,b).
Then the universal bottom-up recursion is run in NUMERATOR form,
    P^BU_k = N_k / b^{2(k-3)}  (k>=4),  N_k = (2/(k-3)) [ (k-3) sum_{i=1}^{k-1} N_i N_{k-i} b^{2(k-4)-e_i-e_{k-i}}
                                       + sum_{i=1}^{k} G_i N_{k-i} b^{2(k-4)-e_{k-i}} - R_k b^{2(k-4)} ],
from the jets (b, B^TD, eta^TD, w2^TD) and L = x^2 C/y - b, and we test in S = k[c,b] with J = (E_2..E_2t):
   (ii)  for k = 4..2N:  b^{2(k-3)} P^TD_k - N_k  in J[1/b]  (minimal b-power m_k with b^{m_k}(...) in J),
         for k = 2N+1..4N:  N_k in J[1/b]  (minimal m_k);  (these are the truncation conditions Phi_k = 0 mod J)
   (iii) the L-pivot  4 eta + 3 b l_2 = 4 eta^TD + 3 b c_{t-1}/y :  in J?  in radical(J)?  (rad(J)=m when dim 0)
Usage: custody_bu.py t [--prime p --droot r] [--nostd]
"""
import argparse
from pathlib import Path
a = argparse.ArgumentParser(); a.add_argument('t', type=int); a.add_argument('--prime', type=int, default=0)
a.add_argument('--droot', type=int, default=0); a.add_argument('--nostd', action='store_true')
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
      '// top-down P coefficients P^TD_k = [x^k]P, k=0..2N (as polynomials in c,b over the field)',
      f'list PTD; for(k=0;k<={2*N};k++){{PTD[k+1]=xc(x*W-(b^2)/4,k);}}',
      '// ---- universal bottom-up recursion, numerator form, from the TD jets ----',
      'poly G=(3/2)*L*(L+b)-B*x; G=subst(G,B,solB);',
      'poly R=(3/16)*(L^2)*(L*(L+2*b)-4*B*x)-eta*x^2*(b*L/2+B*x); R=subst(R,B,solB); R=subst(R,eta,etasol);',
      f'list NB; intvec ee; for(k=0;k<={4*N};k++){{NB[k+1]=poly(0); ee[k+1]=0;}}',
      'NB[1]=-(b^2)/4; NB[2]=-solB; NB[3]=etasol; NB[4]=w2sol;',
      f'for(k=4;k<={4*N};k++){{ee[k+1]=2*(k-3);}}',
      'poly acc; int i;',
      f'for(k=4;k<={4*N};k++){{',
      '  acc=0;',
      '  for(i=1;i<=k-1;i++){ acc=acc+(k-3)*NB[i+1]*NB[k-i+1]*b^(2*(k-4)-ee[i+1]-ee[k-i+1]); }',
      '  for(i=1;i<=k;i++){ acc=acc+xc(G,i)*NB[k-i+1]*b^(2*(k-4)-ee[k-i+1]); }',
      '  acc=acc-xc(R,k)*b^(2*(k-4));',
      '  NB[k+1]=acc*2/(k-3);',
      '  print("NUM k="+string(k)+" terms="+string(size(NB[k+1])));',
      '}',
      f'ring rsmall={co},({",".join(cs)},b),wp({",".join(map(str,list(range(1,t))+[t+1]))});', rel,
      'ideal rows=imap(r,rows); poly target=imap(r,target); poly Bsol=imap(r,solB); poly eta=imap(r,etasol); poly w2=imap(r,w2sol);',
      'list PTD=imap(r,PTD); list NB=imap(r,NB);',
      f'number y=(d+{N})/{2*q};',
      f'poly Lpivot=4*eta+3*b*c{t-1}/y;',
      'print("ROWS_BUILT nrows="+string(size(rows)));']
if not a.prime:
    frz = frozen.read_text()
    frz = frz.replace('ring rsmall=','ring rfro=').replace('ideal rows=','ideal rows_fro=').replace('poly Bsol=','poly B_fro=').replace('poly eta=','poly eta_fro=').replace('poly target=','poly T_fro=')
    s += ['// ---- custody: frozen rows (identifiers renamed only) ----'] + frz.splitlines()
    s += ['setring rsmall;',
          'ideal rows_f=imap(rfro,rows_fro); poly B_f=imap(rfro,B_fro); poly eta_f=imap(rfro,eta_fro); poly T_f=imap(rfro,T_fro);',
          'int same=1; for(i=1;i<=size(rows);i++){ if(rows[i]-rows_f[i]!=0){same=0; print("ROW_MISMATCH "+string(i));} }',
          'print("CUSTODY rows_equal="+string(same)+" B_equal="+string(Bsol-B_f==0)+" eta_equal="+string(eta-eta_f==0)+" target_equal="+string(target-T_f==0));']
s += ['// weights of the numerators (homogeneity check): wt(P_k)=2N-k, wt(N_k)=2N-k+N*e_k',
      f'for(k=4;k<={4*N};k++){{ if(NB[k+1]!=0){{ if(deg(NB[k+1])!={2*N}-k+{N}*(2*(k-3)) or homog(NB[k+1])==0){{print("WEIGHT_FAIL k="+string(k)+" deg="+string(deg(NB[k+1])));}} }} }}',
      'print("WEIGHTS_CHECKED");']
if not a.nostd:
    s += ['int tt=timer; ideal gg=std(rows); print("STD_DONE dim="+string(dim(gg))+" vdim="+string(vdim(gg))+" time="+string(timer-tt));',
          'print("T_in_J="+string(reduce(target,gg)==0)+" T2_in_J="+string(reduce(target^2,gg)==0));',
          'poly dif; int m; int mx;',
          f'for(k=4;k<={4*N};k++){{',
          f'  if(k<={2*N}){{ dif=b^(2*(k-3))*PTD[k+1]-NB[k+1]; }} else {{ dif=NB[k+1]; }}',
          '  m=0; while(reduce(b^m*dif,gg)!=0 && m<=60){m++;}',
          '  print("BU_MEMBERSHIP k="+string(k)+" zero="+string(dif==0)+" min_bpower="+string(m)+" (m>60 means not found)");',
          '}',
          'print("LPIVOT_in_J="+string(reduce(Lpivot,gg)==0)+" LPIVOT_terms="+string(size(Lpivot))+" LPIVOT_wt="+string(deg(Lpivot)));',
          'm=1; while(reduce(Lpivot^m,gg)!=0 && m<=40){m++;} print("LPIVOT_power_in_J="+string(m));',
          'm=1; while(reduce(Bsol^m,gg)!=0 && m<=40){m++;} print("B_power_in_J="+string(m));',
          'm=1; while(reduce(eta^m,gg)!=0 && m<=40){m++;} print("eta_power_in_J="+string(m));',
          'm=1; while(reduce(b^m,gg)!=0 && m<=60){m++;} print("b_power_in_J="+string(m));']
s += ['print("CUSTODY_BU_DONE"); quit;']
lab=f't{t}'+(f'_p{a.prime}_d{a.droot}' if a.prime else '')
(HERE/f'custody_bu_{lab}.sing').write_text('\n'.join(s)+'\n')
print(HERE/f'custody_bu_{lab}.sing')
