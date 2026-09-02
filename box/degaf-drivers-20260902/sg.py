"""Semigroup at infinity Gamma = { deg_t f(a(t),b(t)) } of a polynomial curve,
computed over GF(P) by Gaussian elimination on the monomials a^i b^j.
Gamma is computed as the set of leading degrees of the span."""
P = (1<<61) - 1   # prime

def pmul(u,v):
    r=[0]*(len(u)+len(v)-1)
    for i,ui in enumerate(u):
        if ui:
            for j,vj in enumerate(v):
                r[i+j]=(r[i+j]+ui*vj)%P
    return r

def deg(u):
    d=len(u)-1
    while d>=0 and u[d]%P==0: d-=1
    return d

def gamma(a,b,Mbig):
    da,db=deg(a),deg(b)
    mons=[]
    i=0
    while i*da<=Mbig:
        j=0
        cur=[1]
        for _ in range(i): cur=pmul(cur,a)
        row=cur
        while i*da+j*db<=Mbig:
            mons.append(row[:])
            row=pmul(row,b); j+=1
        i+=1
    # gaussian elimination, pivot = top degree
    piv={}   # degree -> reduced row
    for v in mons:
        v=v+[0]*(Mbig+1-len(v)) if len(v)<Mbig+1 else v[:Mbig+1]
        while True:
            d=deg(v)
            if d<0: break
            if d in piv:
                c=v[d]*pow(piv[d][d],P-2,P)%P
                v=[(v[k]-c*piv[d][k])%P for k in range(len(v))]
            else:
                piv[d]=v; break
    return sorted(piv.keys())

def gaps(G,M):
    return [m for m in range(M+1) if m not in set(G)]

def report(name,a,b,Mbig=None):
    da,db=deg(a),deg(b)
    if Mbig is None: Mbig=4*da*db+4*max(da,db)+8
    G=gamma(a,b,Mbig)
    S=set(G)
    # conductor: smallest c with [c, Mbig-max(da,db)] all present
    lim=Mbig-max(da,db)-1
    c=0
    for m in range(lim,-1,-1):
        if m not in S: c=m+1; break
    gp=[m for m in range(c) if m not in S]
    # symmetry test: z in Gamma  <=>  c-1-z not in Gamma, for 0<=z<=c-1
    sym=all(((z in S) != ((c-1-z) in S)) for z in range(c))
    mingen=[]
    for g in sorted(S):
        if g==0: continue
        if g>lim: break
        if not any((g-h) in S and g-h>0 for h in mingen): mingen.append(g)
    print(f"{name}: deg(a),deg(b)=({da},{db})  conductor={c}  delta_aff=#gaps={len(gp)}  symmetric={sym}")
    print(f"    gaps={gp}")
    print(f"    min gens={mingen}   delta==c/2 ? {len(gp)==c/2}")
    return G,len(gp),c,mingen

if __name__=="__main__":
    report("cuspidal cubic (t^2,t^3)",[0,0,1],[0,0,0,1])
    report("nodal cubic (t^2-t, t^3-t)",[0,-1,1],[0,-1,0,1])
    report("(t^3,t^4)",[0,0,0,1],[0,0,0,0,1])
    report("(t^3,t^5)",[0,0,0,1],[0,0,0,0,0,1])
    report("(t^4, t^6+t^5)",[0,0,0,0,1],[0,0,0,0,0,1,1])
    report("(t^2,t^7)",[0,0,1],[0,0,0,0,0,0,0,1])
    report("line-in-disguise (t^2, t^4+t)",[0,0,1],[0,1,0,0,1])
    report("(t^4, t^6+t^7) [deg 7]",[0,0,0,0,1],[0,0,0,0,0,0,1,1])
    report("(9,6) Chau realised: (t^9+12t^5+24t, t^6+8t^2)",
           [0,24,0,0,0,12,0,0,0,1],[0,0,8,0,0,0,1])
