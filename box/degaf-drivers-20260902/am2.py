from math import gcd
def semigroups(g):
    """all numerical semigroups of genus g, as sorted gap tuples (F<=2g-1)."""
    res=[]
    def rec(inS, gaps, x):
        if len(gaps)>g: return
        if x>2*g-1 if g>0 else True:
            if len(gaps)==g: res.append(tuple(gaps))
            return
        forced=any((a in inS) and ((x-a) in inS) for a in range(1,x))
        rec(inS|{x}, gaps, x+1)
        if not forced: rec(inS, gaps+[x], x+1)
    if g==0: return [()]
    rec({0},[],1)
    return sorted(set(res))
def memb_array(gaps,N):
    G=set(gaps); return [x not in G for x in range(N+1)]
def sgp_from(gens,N):
    S=[False]*(N+1); S[0]=True
    for i in range(1,N+1):
        for gg in gens:
            if gg<=i and S[i-gg]: S[i]=True; break
    return S
def am_data(gaps,b0,N):
    g=len(gaps)
    M=memb_array(gaps,N)
    if b0>N or not M[b0] or b0<1: return None
    if g>(b0-1)*(b0-2)//2: return None
    seq=[b0]; d=b0
    while d!=1:
        S=sgp_from(seq,N); nxt=None
        for x in range(1,N+1):
            if M[x] and not S[x]: nxt=x; break
        if nxt is None: return None
        nd=gcd(d,nxt)
        if d//nd<2: return None
        seq.append(nxt); d=nd
    ds=[b0]
    for i in range(1,len(seq)): ds.append(gcd(ds[-1],seq[i]))
    ns=[0]+[ds[i-1]//ds[i] for i in range(1,len(seq))]
    for i in range(1,len(seq)-1):
        if not ns[i]*seq[i]>seq[i+1]: return None
    for i in range(2,len(seq)):
        Si=sgp_from(seq[:i],N)
        v=ns[i]*seq[i]
        if v>N or not Si[v]: return None
    Sall=sgp_from(seq,N)
    if any(Sall[x]!=M[x] for x in range(N+1)): return None
    dd=sum((ns[i]-1)*seq[i] for i in range(1,len(seq)))-b0+1
    return dict(seq=seq,ns=ns,ok=(dd==2*g))
def study(gmax=12, b0cap=None):
    print(" delta  #semigroups   max n_AM   argmax Gamma            (2*delta+1)")
    worst={}
    viol=[]
    for g in range(0,gmax+1):
        SG=semigroups(g); best=(-1,None)
        N=max(4*(2*g+2)+20, 80)
        cap = b0cap or (6*g+8)
        for gaps in SG:
            adm=[]
            for b0 in range(1,cap+1):
                r=am_data(gaps,b0,N)
                if r:
                    adm.append((b0,r))
                    if not r['ok']: viol.append(('deltaformula',gaps,b0))
                    b1=r['seq'][1] if len(r['seq'])>1 else None
                    if b1 and b0%b1!=0 and b0>2*g+b1-1:
                        viol.append(('ceiling',gaps,b0,b1,g))
            if adm:
                nam=adm[0][0]
                if nam>best[0]: best=(nam,gaps)
        worst[g]=best
        print(f"  {g:3d}   {len(SG):8d}   {best[0]:6d}    {('<'+','.join(map(str,minimal_gens(best[1],N)))+'>') if best[1] is not None else '-':22s}  {2*g+1}")
    print("violations:",viol[:10],"count",len(viol))
def minimal_gens(gaps,N):
    if gaps is None: return []
    M=memb_array(gaps,N); out=[]
    for x in range(1,N+1):
        if M[x] and not sgp_from(out,N)[x] if out else M[x]:
            out.append(x)
        if out and sgp_from(out,N)[:min(N,4*len(gaps)+8)+1]==M[:min(N,4*len(gaps)+8)+1]: break
    return out
study(10)
