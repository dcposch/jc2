#!/usr/bin/env python3
"""Weighted Macaulay window control (Criterion W): for weighted-homogeneous f_1..f_n in n variables of weights w,
degrees d, V(f)={0} iff (f)_D = S_D for every D in [D_w, D_w+max(w)-1], D_w = sum d - sum w + 1.
Checks full column rank of the weighted Macaulay matrices modulo p (rank mod p full => rank in char 0 full).
Input: a restop file (Singular ideal RStop=...;), t, p, root of H_t mod p."""
import sys, re, itertools
from fractions import Fraction
import numpy as np
def parse_ideal(path):
    s=open(path).read(); s=s[s.index("=")+1:].strip().rstrip(";")
    polys=[]; depth=0; cur=""
    for ch in s:
        if ch=="(": depth+=1
        if ch==")": depth-=1
        if ch=="," and depth==0: polys.append(cur); cur=""
        else: cur+=ch
    polys.append(cur); return polys
def terms(poly):
    out=[]; depth=0; cur=""
    for ch in poly:
        if ch=="(": depth+=1
        if ch==")": depth-=1
        if ch in "+-" and depth==0 and cur.strip(): out.append(cur); cur=ch
        else: cur+=ch
    out.append(cur); return [x.strip() for x in out if x.strip()]
def modnum(s, p, root):
    # s like (A/B*yy+C/D) or A/B or integer, possibly with leading sign
    s=s.strip(); sign=1
    if s.startswith("-"): sign=-1; s=s[1:]
    elif s.startswith("+"): s=s[1:]
    s=s.strip("()")
    val=0
    for term in re.findall(r"[+-]?[^+-]+", s.replace(" ","")):
        if not term: continue
        if "yy" in term:
            co=term.replace("*yy","").replace("yy","")
            if co in ("","+"): co="1"
            if co=="-": co="-1"
            fr=Fraction(co); val+=fr.numerator*pow(fr.denominator,-1,p)*root
        else:
            fr=Fraction(term); val+=fr.numerator*pow(fr.denominator,-1,p)
    return sign*val%p
def parse_poly(poly, vars_, p, root):
    res={}
    for tm in terms(poly):
        m=re.match(r"([+-]?)\s*(\([^)]*\)|[0-9/]+)?\*?(.*)", tm)
        sign, co, mon = m.group(1), m.group(2), m.group(3)
        c = modnum((sign or "")+(co if co else "1"), p, root)
        e=[0]*len(vars_)
        if mon:
            for f in mon.split("*"):
                if "^" in f: v,k=f.split("^"); k=int(k)
                else: v,k=f,1
                e[vars_.index(v)]+=k
        e=tuple(e); res[e]=(res.get(e,0)+c)%p
    return res
def monos(D, ws):
    n=len(ws); out=[]
    def rec(i, d, cur):
        if i==n:
            if d==0: out.append(tuple(cur))
            return
        for k in range(d//ws[i]+1): rec(i+1, d-k*ws[i], cur+[k])
    rec(0,D,[]); return out
def rank_mod_p(M, p):
    M=M.copy()%p; rows,cols=M.shape; r=0
    for c in range(cols):
        piv=None
        for i in range(r,rows):
            if M[i,c]%p: piv=i; break
        if piv is None: continue
        M[[r,piv]]=M[[piv,r]]
        inv=pow(int(M[r,c]),-1,p); M[r]=(M[r]*inv)%p
        nz=np.nonzero(M[:,c])[0]
        for i in nz:
            if i!=r: M[i]=(M[i]-M[i,c]*M[r])%p
        r+=1
        if r==rows: break
    return r
if __name__=="__main__":
    path=sys.argv[1]; t=int(sys.argv[2]); p=int(sys.argv[3]); root=int(sys.argv[4])
    n=t-1; ws=list(range(1,n+1)); vars_=["b4"]+[f"q{j}_0" for j in range(2,t)]
    polys=parse_ideal(path)  # RStop[m] = R_{t-m}
    F=[]; ds=[]
    for m,pl in enumerate(polys, start=1):
        r=t-m; d=4*t+4+2*r; P=parse_poly(pl, vars_, p, root)
        assert all(sum(e[i]*ws[i] for i in range(n))==d for e in P), "weight mismatch"
        F.append(P); ds.append(d)
    Dw=sum(ds)-sum(ws)+1
    print(f"t={t} p={p} root={root} degrees={ds} D_w={Dw} window=[{Dw},{Dw+n-1}]")
    allok=True
    for D in range(Dw, Dw+n):
        cols=monos(D,ws); idx={e:i for i,e in enumerate(cols)}
        rowsl=[]
        for P,d in zip(F,ds):
            for mlt in monos(D-d,ws):
                row=np.zeros(len(cols),dtype=np.int64)
                for e,c in P.items():
                    ee=tuple(a+b for a,b in zip(e,mlt)); row[idx[ee]]=(row[idx[ee]]+c)%p
                rowsl.append(row)
        M=np.array(rowsl,dtype=np.int64)
        rk=rank_mod_p(M,p)
        ok = rk==len(cols)
        allok &= ok
        print(f"  D={D}: matrix {M.shape[0]}x{M.shape[1]} rank={rk} full={ok}")
    print("WINDOW_CRITERION", "PASS" if allok else "FAIL")
