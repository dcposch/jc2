#!/usr/bin/env python3
"""Custody of the tacnode objects against the frozen (UF) top-down data at index t (same replay as the charged custody_bu.py:
ring (0,d) minpoly 3d^2-N, Theorem H elimination rows x^{4N-1}..x^{2N+1}, rows E_k=[x^{k+2}](P Hdiff - Rfree), frozen rows by imap).
Then, exactly in the polynomial ring:
 (D)  D = d_Y Q_P(x,L) with Q_P = R(x,Y) - G(x,Y) P - (theta-3)P^2:  [x^0]D=[x^1]D=0,  [x^2]D = (b/4)(4 eta + 3 b c_{t-1}/y),
      deg_x D = 3N, lc = (3/(4y^3))(1-4 om y^2);  [x^3]D + (3/4)(2 B l2 + b^2 l3 + 2 b w2) in (4 eta + 3 b l2)  with cofactor.
 (H)  Hensel factor of Q_P at b=1 to order M=2N+2: F0 = Y^2 + sY + p;  L|_{b=1} root of F0;  Ltilde = -s - L;
      ltilde_2 + l_2 = -8 eta/3;  s_3 = 4 w2 - 16 B eta/3;  tau*Psi + q = 0;  delta_2 = -(8/3)[x^2]D.
 (M)  membership table in J = (E_2..E_2t): [x^j]D in J?  minimal power in J (<=12);  Lpivot, second pivot piv2 = 2Bl2+b^2l3+2bw2.
Usage: custody_tacnode.py t [--prime p --droot r]
"""
import argparse
from pathlib import Path
a = argparse.ArgumentParser(); a.add_argument('t', type=int); a.add_argument('--prime', type=int, default=0); a.add_argument('--droot', type=int, default=0); a.add_argument('--hensel', action='store_true')
a = a.parse_args(); t = a.t; N = t+1; q = 2*t+1
HERE = Path(__file__).resolve().parent
cs = [f'c{i}' for i in range(1, t)]; ws = [f'w{i}' for i in range(1, q)]
if a.prime:
    co = str(a.prime); rel = f'number d={a.droot};'; assert (3*a.droot*a.droot - N) % a.prime == 0
else:
    co = '(0,d)'; rel = f'minpoly=3*d^2-{N};'
frozen = Path('/home/ubuntu/jc2/box/k16xempty-20260905')/f'controls_t{t}_raw.sing'
wts = list(range(1, t)) + [N]
s = [f'ring r={co},(x,Y,{",".join(cs)},b,B,eta,{",".join(ws)}),dp;', rel, 'option(redSB);',
'proc must(int ok,string msg){ if(!ok){print("FAIL "+msg);quit;} }',
'proc xc(poly f,int k){matrix m=coef(f,x);int i;for(i=1;i<=ncols(m);i++){if(deg(m[1,i])==k){return(m[2,i]);}}return(poly(0));}',
f'number y=(d+{N})/{2*q}; number om=1/(4*y^2*(2*d+1));',
f'poly C=x^{t-1}'+''.join(f'+c{i}*x^{t-1-i}' for i in range(1, t))+';',
f'poly W=om*x^{q}-B'+''.join(f'+w{i}*x^{i}' for i in range(1, q))+';',
'poly L=x^2*C/y-b; poly P=x*W-(b^2)/4;',
'poly Hdiff=2*x*diff(P,x)-3*P-B*x+(3/2)*L*(L+b);',
'poly Rfree=(3/16)*(L^2)*(L*(L+2*b)-4*B*x)-eta*x^2*(b*L/2+B*x);',
'poly UF=P*Hdiff-Rfree;',
'UF=subst(UF,eta,w1); W=subst(W,eta,w1);',
f'must(xc(UF,{4*N})==0,"top");',
'poly band,piv,val; poly solB;']
for v, k in zip(list(reversed(ws))+['B'], range(4*N-1, 2*N, -1)):
    s += [f'band=xc(UF,{k}); piv=diff(band,{v});', f'must(deg(piv)==0 && piv!=0,"pivot_{v}");',
          f'val=-subst(band,{v},0)/piv; UF=subst(UF,{v},val); W=subst(W,{v},val);']
    if v == 'B': s += ['solB=val;']
s += ['must(xc(UF,0)==0 && xc(UF,1)==0 && xc(UF,2)==0 && xc(UF,3)==0,"low_four");',
      f'for(int k={2*N+1};k<={4*N};k++){{must(xc(UF,k)==0,"high");}}',
      'poly etasol=xc(W,1); poly w2sol=xc(W,2); poly target=solB*etasol; ideal rows;',
      f'for(k=2;k<={2*t};k++){{rows[k-1]=xc(UF,k+2);}}',
      'poly PTD=x*W-(b^2)/4;   // top-down P with B, w_i substituted (B still a ring variable inside? no: solB substituted)',
      'PTD=subst(PTD,B,solB);',
      '// ---- (D): the quartic Q_P(x,Y) and D = d_Y Q_P(x, L)',
      'poly RY=(3/16)*Y^2*(Y*(Y+2*b)-4*solB*x)-etasol*x^2*(b*Y/2+solB*x);',
      'poly GY=(3/2)*Y*(Y+b)-solB*x;',
      'poly QP=RY-GY*PTD-(x*diff(PTD^2,x)-3*PTD^2);',
      'must(subst(QP,Y,L)+UF==0,"Q_P(x,L)=-UF (identity)");',
      'poly D=subst(diff(QP,Y),Y,L);',
      f'number yv=y; poly l2=c{t-1}/yv; poly l3=c{t-2}/yv;',
      'poly Lpivot=4*etasol+3*b*l2;',
      'print("D_x0_zero="+string(xc(D,0)==0)+" D_x1_zero="+string(xc(D,1)==0));',
      'print("D_x2_equals_(b/4)Lpivot="+string(xc(D,2)-(b/4)*Lpivot==0));',
      f'print("deg_x_D="+string(deg(D,intvec(1,0'+',0'*(len(cs)+len(ws)+3)+f')))+" expected {3*N}");',
      f'print("lc_D_ok="+string(xc(D,{3*N})-(3/(4*y^3))*(1-4*om*y^2)==0));',
      'poly piv2=2*solB*l2+b^2*l3+2*b*w2sol;',
      'poly w3sol=xc(W,3); poly T2=3*b^2*w3sol+18*solB*w2sol-10*etasol^2;',
      '// ---- move to the small ring (c,b) with the weights; D coefficients as polynomials there',
      f'list Dc; for(k=0;k<={3*N};k++){{Dc[k+1]=xc(D,k);}}',
      f'ring rsmall={co},({",".join(cs)},b),wp({",".join(map(str, wts))});', rel,
      'ideal rows=imap(r,rows); poly target=imap(r,target); poly Bsol=imap(r,solB); poly eta=imap(r,etasol); poly w2=imap(r,w2sol);',
      'poly Lpivot=imap(r,Lpivot); poly piv2=imap(r,piv2); poly T2=imap(r,T2); list Dc=imap(r,Dc);',
      'print("T2+Lpivot^2/4+6*E2==0 (exact identity; T2 = 3b^2 w3 + 18 B w2 - 10 eta^2 is P-only): "+string(T2+(Lpivot^2)/4+6*rows[1]==0));',
      'print("ROWS_BUILT nrows="+string(size(rows)));']
if not a.prime:
    frz = frozen.read_text()
    frz = frz.replace('ring rsmall=', 'ring rfro=').replace('ideal rows=', 'ideal rows_fro=').replace('poly Bsol=', 'poly B_fro=').replace('poly eta=', 'poly eta_fro=').replace('poly target=', 'poly T_fro=')
    s += ['// ---- custody: frozen rows (identifiers renamed only) ----'] + frz.splitlines()
    s += ['setring rsmall;',
          'ideal rows_f=imap(rfro,rows_fro); poly B_f=imap(rfro,B_fro); poly eta_f=imap(rfro,eta_fro); poly T_f=imap(rfro,T_fro);',
          'int same=1; int i; for(i=1;i<=size(rows);i++){ if(rows[i]-rows_f[i]!=0){same=0; print("ROW_MISMATCH "+string(i));} }',
          'print("CUSTODY rows_equal="+string(same)+" B_equal="+string(Bsol-B_f==0)+" eta_equal="+string(eta-eta_f==0)+" target_equal="+string(target-T_f==0));']
s += ['// weights of D coefficients: wt([x^j]D) = 3N - j',
      f'int j; for(j=2;j<={3*N};j++){{ if(Dc[j+1]!=0){{ if(deg(Dc[j+1])!={3*N}-j or homog(Dc[j+1])==0){{print("WEIGHT_FAIL j="+string(j)+" deg="+string(deg(Dc[j+1])));}} }} }}',
      'print("D_WEIGHTS_CHECKED");',
      '// [x^3]D + (3/4) piv2 in (Lpivot)?  (identity on the degenerate locus, exact division)',
      'poly rem3=Dc[4]-(3/4)*piv2; ideal Ipiv=std(ideal(Lpivot)); print("x3D_minus_3/4piv2_in_(Lpivot)="+string(reduce(rem3,Ipiv)==0));',
      'poly cof3=division(rem3,ideal(Lpivot))[1][1,1]; print("cofactor="+string(cof3));',
      '// ---- (M) memberships in J',
      'int tt=timer; ideal gg=std(rows); print("STD_DONE dim="+string(dim(gg))+" vdim="+string(vdim(gg))+" time="+string(timer-tt));',
      'print("T_in_J="+string(reduce(target,gg)==0)+" T2_in_J="+string(reduce(target^2,gg)==0));',
      'int m; string line;',
      f'for(j=2;j<={3*N-1};j++){{ m=1; while(reduce(Dc[j+1]^m,gg)!=0 && m<=8){{m++;}} print("DJ_MEMBERSHIP j="+string(j)+" wt="+string({3*N}-j)+" terms="+string(size(Dc[j+1]))+" inJ="+string(reduce(Dc[j+1],gg)==0)+" minpow="+string(m)); }}',
      'm=1; while(reduce(Lpivot^m,gg)!=0 && m<=12){m++;} print("LPIVOT_inJ="+string(reduce(Lpivot,gg)==0)+" minpow="+string(m));',
      'm=1; while(reduce(piv2^m,gg)!=0 && m<=12){m++;} print("PIV2_inJ="+string(reduce(piv2,gg)==0)+" minpow="+string(m)+" wt="+string(deg(piv2)));',
      'm=1; while(reduce(T2^m,gg)!=0 && m<=12){m++;} print("T2_inJ="+string(reduce(T2,gg)==0)+" minpow="+string(m)+" wt="+string(deg(T2))+" terms="+string(size(T2)));',
      '// Lpivot * piv2 ? and Lpivot*B, Lpivot*eta',
      'print("Lpivot*piv2_inJ="+string(reduce(Lpivot*piv2,gg)==0)+" Lpivot*B_inJ="+string(reduce(Lpivot*Bsol,gg)==0)+" Lpivot*eta_inJ="+string(reduce(Lpivot*eta,gg)==0)+" Lpivot^2_inJ="+string(reduce(Lpivot^2,gg)==0));',
      '// ---- degenerate stratum J+(Lpivot) and the target',
      'ideal gdeg=std(rows+Lpivot); print("Jdeg=J+(Lpivot): dim="+string(dim(gdeg))+" vdim="+string(vdim(gdeg)));',
      'int n=1; while(reduce(target^n,gdeg)!=0 && n<=6){n++;} print("(B*eta)^n_in_J+(Lpivot): n="+string(n)+"  (Beta wt "+string(deg(target))+")");',
      'print("B_in_Jdeg="+string(reduce(Bsol,gdeg)==0)+" eta_in_Jdeg="+string(reduce(eta,gdeg)==0)+" piv2_in_Jdeg="+string(reduce(piv2,gdeg)==0));',
      'ideal gT=std(rows+target); print("J+(Beta): dim="+string(dim(gT))+" vdim="+string(vdim(gT)));',
      'm=1; while(reduce(Lpivot^m,gT)!=0 && m<=6){m++;} print("Lpivot^m_in_J+(Beta): m="+string(m));',
      'ideal gB=std(rows+Bsol); m=1; while(reduce(Lpivot^m,gB)!=0 && m<=6){m++;} print("Lpivot^m_in_J+(B): m="+string(m)+"  vdim(J+(B))="+string(vdim(gB)));',
      'ideal gE=std(rows+eta); m=1; while(reduce(Lpivot^m,gE)!=0 && m<=6){m++;} print("Lpivot^m_in_J+(eta): m="+string(m)+"  vdim(J+(eta))="+string(vdim(gE)));',
      'print("MEMBERSHIP_DONE");',
]
if a.hensel:
    s += [      '// ---- (H) Hensel factor at b=1 (exact), order M=2N+2',
      f'ring rb1={co},(x,{",".join(cs)}),dp;', rel,
      'proc xc(poly f,int k){matrix m=coef(f,x);int i;for(i=1;i<=ncols(m);i++){if(deg(m[1,i])==k){return(m[2,i]);}}return(poly(0));}',
      f'number y=(d+{N})/{2*q};',
      'map tob1=r,x,0,'+','.join(cs)+',1,0,0'+',0'*len(ws)+';   // Y->0, b->1, B,eta,w_i -> 0 (already substituted where needed)',
      'poly PTD=tob1(PTD); poly L=tob1(L); poly Bsol=tob1(solB); poly eta=tob1(etasol); poly w2=tob1(w2sol);',
      f'poly QP0=tob1(QP);  // note: QP had Y; tob1 sends Y->0 so recompute the Y-coefficients from PTD instead',
      'number b=1;',
      f'int M={2*N+2}; intvec wx=1' + ',0'*(t-1) + ';   // x-weight truncation: jet(f,M,wx) keeps x-degree <= M (jet(f,M) alone truncates by TOTAL degree)',
      '// coefficients of Q_P/(3/16) in Y: c3 = 2b, c2 = -4Bx-8P, c1 = -(8/3)eta x^2 - 8P, c0 = (16/3)(BxP - eta B x^3 - (x(P^2)\'-3P^2))',
      'poly c3=2; poly c2=-4*Bsol*x-8*PTD; poly c1=-(8/3)*eta*x^2-8*PTD; poly c0=(16/3)*(Bsol*x*PTD-eta*Bsol*x^3-(x*diff(PTD^2,x)-3*PTD^2));',
      'poly s=2; poly p=1; poly s1=0; poly p1=1; poly r1,r2,r3,r4,S,Pp,S1,P1; int n;',
      'for(n=1;n<=M;n++){',
      '  r1=xc(c3,n)-xc(s+s1,n); r2=xc(c2,n)-xc(p+p1+s*s1,n); r3=xc(c1,n)-xc(s*p1+s1*p,n); r4=xc(c0,n)-xc(p*p1,n);',
      '  P1=(r3-r1)/2; Pp=r4-P1; S1=(r2-r4)/2; S=r1-S1;',
      '  s=s+S*x^n; p=p+Pp*x^n; s1=s1+S1*x^n; p1=p1+P1*x^n;',
      '}',
      'poly chk=jet((s+s1)-c3,M,wx); poly chk2=jet(p+p1+s*s1-c2,M,wx); poly chk3=jet(s*p1+s1*p-c1,M,wx); poly chk4=jet(p*p1-c0,M,wx);',
      'print("HENSEL_OK="+string(chk==0 && chk2==0 && chk3==0 && chk4==0));',
      'print("HENSEL_T="+string(timer)); poly UFb1=tob1(UF); poly F0L=jet(L^2+s*L+p,M,wx); poly F1L=jet(L^2+s1*L+p1,M,wx);',
      'print("F0(L)F1(L)+(16/3)UF=0 mod x^M (identity; so L is a root of F0 modulo J): "+string(jet(F0L*F1L+(16/3)*UFb1,M,wx)==0)); print("T_after_F0F1="+string(timer));',
      'print("s_1=0: "+string(xc(s,1)==0)+"  s_2=8eta/3 (b=1): "+string(xc(s,2)-(8/3)*eta==0)+"  s_3=4w2-16Beta/3: "+string(xc(s,3)-(4*w2-(16/3)*Bsol*eta)==0));',
      'print("p_1=0: "+string(xc(p,1)==0)+"  p_2=(8/3)eta: "+string(xc(p,2)-(8/3)*eta==0)+"  p_3=(4/3)(3w2-4Beta): "+string(xc(p,3)-(4/3)*(3*w2-4*Bsol*eta)==0));',
      'poly Disc0=jet(s^2-4*p,M,wx); print("Disc(F0): x^0..x^3 coefficients vanish: "+string(xc(Disc0,0)==0 && xc(Disc0,1)==0 && xc(Disc0,2)==0 && xc(Disc0,3)==0));',
      'poly Lpiv1=tob1(Lpivot); poly E2b1=xc(UFb1,4);',
      'poly d4=xc(Disc0,4)-(4/9)*Lpiv1^2; print("[x^4]Disc(F0) - (4/9)Lpivot^2 in (E2) (exact division): "+string(reduce(d4,std(ideal(E2b1)))==0));',
      'poly w3=xc(PTD,4); print("[x^4]Disc(F0) + (16/9) T2 == 0 (b=1; T2 = 3w3+18Bw2-10eta^2): "+string(xc(Disc0,4)+(16/9)*(3*w3+18*Bsol*w2-10*eta^2)==0));',
      'print("s_4, p_4 closed forms (b=1): "+string(xc(s,4)-(8/9)*(12*Bsol^2*eta+6*w3+eta^2)==0)+" "+string(xc(p,4)-(4/9)*(24*Bsol^2*eta+18*Bsol*w2+15*w3-4*eta^2)==0));',
      'print("HENSEL_END_T="+string(timer));',
]
s += [      'print("CUSTODY_TACNODE_DONE"); quit;']
lab = f't{t}' + (f'_p{a.prime}_d{a.droot}' if a.prime else '')
(HERE/f'custody_tacnode_{lab}.sing').write_text('\n'.join(s)+'\n')
print(HERE/f'custody_tacnode_{lab}.sing')
