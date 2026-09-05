#!/usr/bin/env python3
"""Emit Singular analysis scripts for the exact-square question tau_t^2 in I_{t,+}.

main <tag> <t>        : homogeneity, std(I_+), weighted Hilbert histogram / socle weight,
                        exponent N_t, exact identities (B1),(B2), natural-quantity memberships,
                        slice memberships, lift(I_+, tau^2) cofactor support.
sub  <tag> <t> <label> <k1,k2,...> : the sub-ideal <T_k1,...>: dim, vdim, socle, tau / tau^2 membership.
"""
import sys
from pathlib import Path
D = Path('/home/ubuntu/jc2/box/k16sq-20260905')
kind, tag, t = sys.argv[1], sys.argv[2], int(sys.argv[3])
q, e = 2*t+1, 3*t+1
resid = ['b4'] + [f'u{i}' for i in range(2, t)] + ['b3']
wts = list(range(1, t)) + [t+1]
o = []
say = o.append
say(f'< "{D}/{tag}_rows.sing";')
say('option(redSB);')
say(f'int t={t}; int q={q};')
say(f'intvec wv={",".join(map(str,wts))};')
say(f'number y=(d+{t+1})/{2*q}; number g={e*t}*(3*d+{2*(t+1)})/{6*q**3};')
say('proc ishomog(poly f, int w) { return(f==jet(f,w,wv)-jet(f,w-1,wv)); }')
say('proc hist(ideal KB) { int i; int w; int mx=0; for(i=1;i<=size(KB);i++){ if(deg(KB[i])>mx){mx=deg(KB[i]);} } intvec h; h[mx+1]=0; for(i=1;i<=size(KB);i++){ w=deg(KB[i]); h[w+1]=h[w+1]+1; } string s=""; for(w=0;w<=mx;w++){ s=s+string(h[w+1])+","; } print("HF_BY_WEIGHT "+s); print("SOCLE_WEIGHT "+string(mx)); }')
rows = ','.join(f'T{k}' for k in range(1, 2*t))
if kind == 'main':
    say('int k;')
    for k in range(0, 2*t):
        say(f'print("ROW {k} wdeg "+string(deg(T{k}))+" homog "+string(ishomog(T{k},{4*t+1-k}))+" nterms "+string(size(T{k})));')
    say(f'print("TAU wdeg "+string(deg(tau))+" homog "+string(ishomog(tau,{4*t+1}))+" T0-tau-const "+string(T0-tau));')
    say('poly b2=spineB2; poly R=rootR; poly b1=spineB1;')
    say('print("B1_IDENTITY "+string(y*b1+b3*R==0));')
    say('poly acc=tau+g*b2*R;')
    for k in range(1, 2*t): say(f'acc=acc+b4^{k}*T{k};')
    say('print("B2_IDENTITY "+string(acc==0));')
    say(f'ideal Iplus={rows};')
    say('int tt=timer; ideal GI=std(Iplus); print("STD_TIME_S "+string(timer-tt)+" ms"); print("STD_SIZE "+string(size(GI)));')
    say('print("IPLUS_DIM "+string(dim(GI))); print("IPLUS_VDIM "+string(vdim(GI)));')
    say('if(dim(GI)==0){ ideal KB=kbase(GI); hist(KB); }')
    say('int N; for(N=1;N<=3;N++){ print("TAU_POWER "+string(N)+" ZERO "+string(reduce(tau^N,GI)==0)); }')
    say('list nat=list("b2",b2,"R",R,"b1",b1,"b2R",b2*R,"b2R2",b2*R^2,"b22R",b2^2*R,"b22R2",b2^2*R^2,"b1b2",b1*b2,"b1R",b1*R,"b1sq",b1^2,"b1b2R",b1*b2*R,"b2sq",b2^2,"Rsq",R^2,"b3tau",b3*tau,"b4tau",b4*tau,"Rtau",R*tau,"b2tau",b2*tau,"b1tau",b1*tau,"b3b2",b3*b2,"b3R",b3*R,"b3b1",b3*b1);')
    say('int i; for(i=1;i<=size(nat);i=i+2){ print("NAT "+string(nat[i])+" wdeg "+string(deg(nat[i+1]))+" IN_IPLUS "+string(reduce(nat[i+1],GI)==0)); }')
    for v in resid:
        say(f'ideal Gs=std(Iplus+ideal({v})); print("SLICE {v} tau_in "+string(reduce(tau,Gs)==0)+" tau2_in "+string(reduce(tau^2,Gs)==0));')
    say('tt=timer; matrix M=lift(Iplus,ideal(tau^2)); print("LIFT_TIME_S "+string(timer-tt)+" ms");')
    say('poly chk=0; for(k=1;k<=ncols(Iplus);k++){ chk=chk+Iplus[k]*M[k,1]; } print("LIFT_VERIFIED "+string(chk==tau^2));')
    say('string sup=""; for(k=1;k<=ncols(Iplus);k++){ if(M[k,1]!=0){ sup=sup+string(k)+"(w"+string(deg(M[k,1]))+",h"+string(ishomog(M[k,1],4*t+1+k))+",n"+string(size(M[k,1]))+",b3deg"+string(deg(M[k,1],intvec(0:(t-1),1)))+") "; } } print("LIFT_SUPPORT "+sup);')
    say(f'write("{D}/{tag}_lift.txt",string(M));')
    say('print("MAIN_COMPLETE"); quit;')
else:
    label, ks = sys.argv[4], [int(x) for x in sys.argv[5].split(',')]
    say(f'ideal J={",".join(f"T{k}" for k in ks)};')
    say('int tt=timer; ideal GJ=std(J); print("STD_TIME_S "+string(timer-tt)+" ms");')
    say(f'print("SUB {label} rows {sys.argv[5]} DIM "+string(dim(GJ))+" VDIM "+string(vdim(GJ)));')
    say('if(dim(GJ)==0){ ideal KB=kbase(GJ); hist(KB); }')
    say(f'print("SUB {label} TAU_IN "+string(reduce(tau,GJ)==0)+" TAU2_IN "+string(reduce(tau^2,GJ)==0)+" TAU3_IN "+string(reduce(tau^3,GJ)==0));')
    say('print("SUB_COMPLETE"); quit;')
print('\n'.join(o))
