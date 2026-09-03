#!/usr/bin/env python3
"""M2-DESCENT step (1c): does the Jacobian condition alone force M_2 > m?

Population: genuine Keller pairs = polynomial automorphisms of A^2_Q, put into
Moh's gauge (monic in y, deg = deg_y for both members) by a generic linear
precomposition.  For each we compute Moh's characteristic data {M_j, d_j}
(box/m2descent-drivers-20260903/etaexp.py) and test the predicate M_2 > m.
FAIL-CLOSED: the Jacobian of every pair is verified to be a nonzero constant
and deg = deg_y is verified before the pair is used.
"""
import sys, os, random
from fractions import Fraction as F
from math import gcd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from etaexp import char_data

# ---- Q[x,y] as dict {(i,j): Fraction} -------------------------------------
def add(a,b):
    r=dict(a)
    for k,v in b.items():
        w=r.get(k,F(0))+v
        if w: r[k]=w
        else: r.pop(k,None)
    return r
def scal(a,c):
    c=F(c); return {} if c==0 else {k:v*c for k,v in a.items()}
def mul(a,b):
    r={}
    for (i,j),u in a.items():
        for (k,l),v in b.items():
            t=(i+k,j+l); w=r.get(t,F(0))+u*v
            if w: r[t]=w
            else: r.pop(t,None)
    return r
def powp(a,e):
    r={(0,0):F(1)}
    for _ in range(e): r=mul(r,a)
    return r
def dx(a):
    r={}
    for (i,j),v in a.items():
        if i: 
            t=(i-1,j); w=r.get(t,F(0))+v*i
            if w: r[t]=w
            else: r.pop(t,None)
    return r
def dy(a):
    r={}
    for (i,j),v in a.items():
        if j:
            t=(i,j-1); w=r.get(t,F(0))+v*j
            if w: r[t]=w
            else: r.pop(t,None)
    return r
def jac(a,b): return add(mul(dx(a),dy(b)), scal(mul(dy(a),dx(b)),-1))
def deg(a): return max(i+j for (i,j) in a) if a else -1
def degy(a): return max(j for (i,j) in a) if a else -1
def subst(P, X, Y):
    """P(X,Y) where X,Y are polynomials."""
    out={}
    dxm=max(i for (i,j) in P); dym=max(j for (i,j) in P)
    XP=[{(0,0):F(1)}]; 
    for _ in range(dxm): XP.append(mul(XP[-1],X))
    YP=[{(0,0):F(1)}]
    for _ in range(dym): YP.append(mul(YP[-1],Y))
    for (i,j),c in P.items(): out=add(out, scal(mul(XP[i],YP[j]), c))
    return out
def normalize_monic_y(P):
    d=degy(P); lead=[(i,j) for (i,j) in P if j==d]
    if len(lead)!=1 or lead[0][0]!=0: return None
    return scal(P, F(1)/P[lead[0]])

X={(1,0):F(1)}; Y={(0,1):F(1)}

def build(seq, rnd):
    """seq = list of (degree of p);  (F,G) <- (G, F + p(G))."""
    Ff, Gg = X, Y
    for dgr in seq:
        p={}
        for e in range(dgr+1):
            c=rnd.choice([-3,-2,-1,1,2,3]) if e<dgr else 1
            if e==0: c=rnd.choice([-2,-1,0,1,2])
            if c: p=add(p,{(0,e):F(c)})   # p as a poly in the 2nd slot
        # p(G):
        pg={}
        Gp={(0,0):F(1)}
        for e in range(dgr+1):
            c=p.get((0,e),F(0))
            if c: pg=add(pg, scal(Gp,c))
            Gp=mul(Gp,Gg)
        Ff, Gg = Gg, add(Ff, pg)
    return Ff, Gg

def gauge(Ff,Gg,rnd):
    """precompose with a generic linear map, then make monic in y."""
    for _ in range(30):
        a,b,c,d = (rnd.randint(-4,4) for _ in range(4))
        if a*d-b*c==0: continue
        L1=add(scal(X,a),scal(Y,b)); L2=add(scal(X,c),scal(Y,d))
        f2=subst(Ff,L1,L2); g2=subst(Gg,L1,L2)
        if degy(f2)!=deg(f2) or degy(g2)!=deg(g2): continue
        f2=normalize_monic_y(f2); g2=normalize_monic_y(g2)
        if f2 is None or g2 is None: continue
        return f2,g2
    return None,None

rnd=random.Random(20260903)
print("  %-22s %4s %4s %4s %-22s %-16s %6s" % ("build","n","m","K","M_2..M_s","d_1..","M_2>m"))
seen=set(); rows=[]
for trial in range(400):
    L=rnd.choice([[2],[3],[2,2],[3,2],[2,3],[4],[5],[2,2,2],[3,3],[4,2],[2,4]])
    Ff,Gg=build(L,rnd)
    f2,g2=gauge(Ff,Gg,rnd)
    if f2 is None: continue
    J=jac(f2,g2)
    if len(J)!=1 or (0,0) not in J: continue          # FAIL-CLOSED: Jacobian constant
    m,n=degy(f2),degy(g2)
    if not (1<n<=26 and 0<m<n): continue
    if n % m == 0 and n//m>=2: pass
    key=(tuple(L),n,m)
    if key in seen: continue
    seen.add(key)
    Ms,ds,fj=char_data(f2,m,g2,n)
    M2 = Ms[1] if len(Ms)>1 else None
    rows.append((L,n,m,gcd(n,m),Ms,ds,M2))
    print("  %-22s %4d %4d %4d %-22s %-16s %6s" % (str(L),n,m,gcd(n,m),str(Ms[1:]),str(ds),
          ("n/a" if M2 is None else str(M2>m))))
    if len(rows)>=22: break
print("\n  pairs with a second characteristic exponent M_2 :", sum(1 for r in rows if r[6] is not None))
print("  of those, M_2 > m :", sum(1 for r in rows if r[6] is not None and r[6]>r[2]))
print("  of those, M_2 <= m:", sum(1 for r in rows if r[6] is not None and r[6]<=r[2]))
