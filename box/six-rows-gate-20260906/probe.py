#!/usr/bin/env python3
"""Per-branch tables + sensitivity probes on the R063 forcing."""
import sys, json
from fractions import Fraction as F
sys.path.insert(0,'box/six-rows-gate-20260906')
import gate as G

def table(rid, level):
    C = G.child(rid); s=C["s"]
    Vt={s+1:C["d"][s+1]}
    if level==s: Vin=C["d"][s+1]; Vsel=Vt
    else:
        Vsel=dict(Vt); Vsel[s]=C["Vroster"][s]; Vin=C["Vroster"][s]
    di=G.delta_of(C,level,Vsel)
    P,Q=G.P_of(C,level,Vin),G.Q_of(C,level,Vin)
    A=(1*di).denominator
    print(f"\n{rid}  D'_{level}: (P,Q,A)=({P},{Q},{A})  delta_{level}={di}"
          f"  forbid-mult={int(P//Q) if P%Q==0 else '-'}  major iff k>{F(C['d'][level],C['n']-C['M'][level])}")
    print("  r  class   (rhoP,rhoQ)   delta_f      A'  residues   term        verdict")
    for k in range(1,int(P)+1):
        rP,rQ=G.rho(C,level,k)
        if not G.major(C,level,k):
            df=G.minor_delta(C,level,k,di)
            print(f"  {k}  minor   ({rP},{rQ})".ljust(28)+f" {str(df):10s}  {(1*df).denominator:2d}  -          0           final (delta>{C['H']})")
        else:
            V2=dict(Vsel); V2[level]=k
            dn=G.delta_of(C,level-1,V2)
            for L,tag in [(1,'L=1(zero)'),(A,f'L={A}(nonzero)')] if A>1 else [(1,'L=1')]:
                A1=(L*dn).denominator
                ok = int(rP)%A1 in (0,1) and int(rQ)%A1 in (0,1)
                print(f"  {k}  major   ({rP},{rQ})".ljust(28)+
                      f" {str(dn):10s}  {A1:2d}  ({int(rP)%A1},{int(rQ)%A1})".ljust(14)+
                      f" {str(G.term(C,rP,dn)):11s} {'pass' if ok else 'FAIL'} {tag}")

for rid,lv in [("R025",3),("R025",2),("R057",2),("R063",3),("R063",2)]:
    table(rid,lv)

print("\n=== R063 sensitivity probes (what the kill rests on) ===")
C=G.child("R063"); s=C["s"]
Vsel={s+1:C["d"][s+1], s:7}
P,Q=G.P_of(C,2,7),G.Q_of(C,2,7); di=G.delta_of(C,2,Vsel)
def sums_for(pats,label):
    out=set()
    for z,orbs,A in pats:
        facs=([z] if z>0 else [])+[k for k in orbs for _ in range(A)]
        tot=F(0); okall=True
        for k in facs:
            if not G.major(C,2,k):
                continue
            V2=dict(Vsel); V2[2]=k; dn=G.delta_of(C,1,V2)
            rP,rQ=G.rho(C,2,k); tot+=G.term(C,rP,dn)
        out.add(tot)
    print(f"  {label:52s} patterns={len(pats):3d} sums={sorted(str(x) for x in out)}")
def pats(A,forbid,need):
    r=[]
    for z,orbs in G.patterns(P,Q,A,forbid):
        ks=([z] if z>0 else [])+[k for k in orbs for _ in range(A)]
        if need is not None and need not in ks: continue
        r.append((z,orbs,A))
    return r
sums_for(pats(3,2,3),      "as printed (A=3, mult!=2, contains V'_2=3)")
sums_for(pats(1,2,3),      "COARSE stabilizer A=1 instead of 3")
sums_for(pats(3,None,3),   "drop the p.171 mult != P/Q rule")
sums_for(pats(3,2,None),   "drop 'contains V'_2=3'")
sums_for(pats(1,None,None),"drop all three")
