"""AM delta-sequence admissibility for (b_0, Gamma), and n_AM(Gamma).

(AM-SG) as banked at dist/jc72108-theory-bundle-v1/AM-CHECK.md:50-63:
  b_0 = n; d_0 = b_0, d_i = gcd(d_{i-1}, b_i); n_i = d_{i-1}/d_i >= 2; d_h = 1;
  (ii)  n_i b_i > b_{i+1};      (iii) n_i b_i in <b_0,...,b_{i-1}>.
Canonical sequence: b_i = min(Gamma \ <b_0,...,b_{i-1}>).
Extra necessary condition from the genus formula: delta(Gamma) <= (n-1)(n-2)/2.
"""
from math import gcd, isqrt

def sgp_gen(gens, N):
    S=[False]*(N+1); S[0]=True
    for x in range(1,N+1):
        for g in gens:
            if g<=x and S[x-g]: S[x]=True; break
    return S

def semigroups_of_genus(g):
    """all numerical semigroups with exactly g gaps; represented as frozenset of
    elements up to F+1 where F<=2g-1, plus 'all >= c'."""
    out=[]
    C=2*g+1
    def rec(elems, gaps, nxt):
        if len(gaps)==g:
            out.append((frozenset(elems), tuple(gaps))); return
        if len(gaps)>g or nxt>2*g: return
        # decide membership of nxt
        # nxt in S iff exists decomposition; we build greedily: S determined by gaps
        # element nxt is forced in S if nxt = x+y with x,y in S, x,y>0
        forced = any((x in elems) and (nxt-x in elems) for x in range(1,nxt))
        if forced:
            rec(elems|{nxt}, gaps, nxt+1)
        else:
            rec(elems|{nxt}, gaps, nxt+1)
            rec(elems, gaps+(nxt,), nxt+1)
    rec({0},(),1)
    res=[]
    seen=set()
    for elems,gaps in out:
        key=gaps
        if key in seen: continue
        seen.add(key); res.append(gaps)
    return res

def memb(gaps, N):
    G=set(gaps); return [x for x in range(N+1) if x not in G]

def in_sgp(gens,x):
    if x==0: return True
    if x<0: return False
    S=[False]*(x+1); S[0]=True
    for i in range(1,x+1):
        for g in gens:
            if g<=i and S[i-g]: S[i]=True; break
    return S[x]

def am_admissible(gaps, b0, verbose=False):
    g=len(gaps); N=max(2*g+2, 4*b0+8)
    els=set(memb(gaps,N))
    if b0 not in els or b0<1: return None
    if g > (b0-1)*(b0-2)//2: return None          # genus / delta budget
    seq=[b0]; d=b0
    while d!=1:
        cur=[x for x in seq]
        nxt=None
        for x in sorted(els):
            if x==0: continue
            if x>N-1: break
            if not in_sgp(cur,x): nxt=x; break
        if nxt is None: return None
        nd=gcd(d,nxt); ni=d//nd
        if ni<2: return None
        if len(seq)>=2:
            # condition (ii) for the previous index: n_{i-1} b_{i-1} > b_i
            pass
        seq.append(nxt); d=nd
    # now check (ii) and (iii)
    ds=[b0]; 
    for i in range(1,len(seq)): ds.append(gcd(ds[-1],seq[i]))
    ns=[None]+[ds[i-1]//ds[i] for i in range(1,len(seq))]
    for i in range(1,len(seq)-1):
        if not (ns[i]*seq[i] > seq[i+1]): return None
    for i in range(2,len(seq)):
        if not in_sgp(seq[:i], ns[i]*seq[i]): return None
    # generation check
    if set(memb(gaps,N)) != set(x for x in range(N+1) if in_sgp(seq,x)): return None
    # delta formula check
    dd=sum((ns[i]-1)*seq[i] for i in range(1,len(seq)))-b0+1
    ok = (dd==2*g)
    return dict(seq=seq,ds=ds,ns=ns,delta_formula_ok=ok,delta=g)

def n_AM(gaps):
    g=len(gaps); N=max(2*g+2, 200)
    els=[x for x in memb(gaps,N) if x>=1]
    cands=[]
    for b0 in els:
        if b0> 6*g+6: break
        r=am_admissible(gaps,b0)
        if r: cands.append((b0,r))
    return cands

if __name__=="__main__":
    import sys
    # controls: explicit curves
    tests={"<2,3> cuspidal/nodal cubic":(1,),
           "<3,4>":(1,2,5),
           "<2,9> (9,6)Chau & (t^2,t^9)":(1,3,5,7),
           "<4,6,11> (t^4,t^6+t^5)":(1,2,3,5,7,9,13),
           "<3,5>":(1,2,4,7),
           "<5,7>":(1,2,3,4,6,8,9,11,13,16,18,23),
           "<4,5>":(1,2,3,6,7,11),
           "<6,9,13>":None}
    for k,gp in tests.items():
        if gp is None: continue
        c=n_AM(gp)
        print(f"{k:32s} delta={len(gp):3d}  admissible b_0 (<=6d+6): {[b for b,_ in c][:12]}  n_AM={c[0][0] if c else None}"
              f"  formula_ok={all(r['delta_formula_ok'] for _,r in c)}")
