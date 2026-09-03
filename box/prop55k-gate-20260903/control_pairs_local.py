#!/usr/bin/env python3
"""Fail-closed control for PROP 5.5(k)  (high-precision radius measurement).

Genuine (existing) pairs (P,Q) in k[gamma,pi], both monic in pi with
deg = deg_pi, and J_{gamma,pi}(P,Q) = c*gamma^k exactly:

    P = phi(pi) + e*gamma^{k+1},        phi monic, deg phi = m' >= k+1
    Q = psi(P)  + a*pi,                 psi monic, deg psi = q,  n' = q*m'
    ==>  J = a * P_gamma = a*e*(k+1)*gamma^k .

(For this P the FULL solution set of J(P,Q) = c*gamma^k is Q = a*pi + psi(P):
 ker J(P,-) = k[P], and the only particular solutions are a*pi + k[P].)

For each pair: exact J check, characteristic data from the eta-expansion
(etaexp.char_data, charged driver rerun from the frozen copy), mpmath
Newton-Puiseux measurement of delta_2', delta_1' and the disc root-counts,
V_2' from Def 5.1(1), then TEST-55(k).  PROP 5.5(k) must NOT kill any of these.
"""
import sys, os
from fractions import Fraction as F
from math import gcd
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from etaexp import char_data
from prop55k import test55k, closed, phi, show

mp.mp.dps = 200

def padd(a,b):
    r=dict(a)
    for k,v in b.items():
        w=r.get(k,F(0))+v
        if w: r[k]=w
        else: r.pop(k,None)
    return r
def pmul(a,b):
    r={}
    for (i,j),u in a.items():
        for (p,q),v in b.items():
            k=(i+p,j+q); w=r.get(k,F(0))+u*v
            if w: r[k]=w
            else: r.pop(k,None)
    return r
def pscal(a,c):
    c=F(c); return {} if c==0 else {k:v*c for k,v in a.items()}
def deg(a): return max((i+j for (i,j) in a), default=-1)
def degpi(a): return max((j for (i,j) in a), default=-1)
def d_gamma(a): return {(i-1,j):v*i for (i,j),v in a.items() if i}
def d_pi(a):    return {(i,j-1):v*j for (i,j),v in a.items() if j}
def jac(a,b):   return padd(pmul(d_gamma(a),d_pi(b)), pscal(pmul(d_pi(a),d_gamma(b)),-1))
def compose(cs,P):
    out={}; cur={(0,0):F(1)}
    for c in cs:
        if c: out=padd(out,pscal(cur,c))
        cur=pmul(cur,P)
    return out
def roots_at(a, X):
    d=degpi(a); co=[mp.mpf(0)]*(d+1)
    for (i,j),v in a.items(): co[d-j]+= mp.mpf(v.numerator)/v.denominator * X**i
    return mp.polyroots(co, maxsteps=200, extraprec=400)

def cluster(rs, cut):
    n=len(rs); par=list(range(n))
    def find(a):
        while par[a]!=a: par[a]=par[par[a]]; a=par[a]
        return a
    for i in range(n):
        for j in range(i+1,n):
            if abs(rs[i]-rs[j])<=cut:
                a,b=find(i),find(j)
                if a!=b: par[a]=b
    g={}
    for i in range(n): g.setdefault(find(i),[]).append(i)
    return list(g.values())

def pairmin(idx, rs):
    return min(abs(rs[i]-rs[j]) for a,i in enumerate(idx) for j in idx[a+1:]) if len(idx)>1 else None
def pairmax(rs):
    return max(abs(rs[i]-rs[j]) for i in range(len(rs)) for j in range(i+1,len(rs)))

def measure(Q, X1=mp.mpf('30'), X2=mp.mpf('10000')):
    """two-point fit of ord_t = -log|sep|/log|X| ; returns
       (delta_top, delta_inner, cluster sizes at X2)."""
    R1, R2 = roots_at(Q,X1), roots_at(Q,X2)
    top1, top2 = pairmax(R1), pairmax(R2)
    d_top = -(mp.log(top2)-mp.log(top1))/(mp.log(X2)-mp.log(X1))
    def sub(R, X):
        mn = min(abs(R[i]-R[j]) for i in range(len(R)) for j in range(i+1,len(R)))
        cut = mp.sqrt(mn*pairmax(R))
        return cluster(R, cut)
    c1, c2 = sub(R1,X1), sub(R2,X2)
    b1, b2 = max(c1,key=len), max(c2,key=len)
    m1, m2 = pairmin(b1,R1), pairmin(b2,R2)
    d_in = None
    if m1 and m2: d_in = -(mp.log(m2)-mp.log(m1))/(mp.log(X2)-mp.log(X1))
    return d_top, d_in, sorted(len(c) for c in c2)

def run(label, phi_c, e, kk, psi_c, a):
    P = {(0,j):F(c) for j,c in enumerate(phi_c) if c}
    P = padd(P, {(kk+1,0):F(e)})
    Q = padd(compose([F(c) for c in psi_c], P), {(0,1):F(a)})
    J = jac(P,Q)
    mp_, np_ = degpi(P), degpi(Q)
    okgauge = (deg(P)==mp_ and deg(Q)==np_)
    okJ = (len(J)==1 and (kk,0) in J)
    Ms, ds, _ = char_data(P, mp_, Q, np_)
    d_top, d_in, sizes = measure(Q)
    d2 = gcd(np_, mp_)
    print("\n  %s" % label)
    print("    deg_pi(P,Q)=(%d,%d)  deg=(%d,%d)  gauge=%s   J=%s  monomial c*g^%d: %s"
          % (mp_,np_,deg(P),deg(Q),okgauge,J,kk,okJ))
    print("    char data  M=%s  d=%s  s'=%d" % (Ms, ds, len(Ms)))
    print("    measured  delta_top=%s  delta_inner=%s  Q-root clusters=%s"
          % (mp.nstr(d_top,8), mp.nstr(d_in,8) if d_in is not None else "n/a", sizes))
    if not (okgauge and okJ): print("    *** gauge/J failure ***"); return None
    if len(Ms)!=2:
        print("    -> s' != 2 : PROP 5.5(k) not applicable here"); return None
    M2 = Ms[1]; biggest = max(sizes)
    V2n = F(biggest*d2, np_)
    if V2n.denominator!=1: print("    -> non-integral V2'; skip"); return None
    V2 = int(V2n)
    cf = closed(np_, mp_, M2, V2, kk); ph = phi(np_, mp_, M2, V2, kk)
    ag = (abs(float(cf[0])-float(d_top))<2e-3 and
          (d_in is None or abs(float(cf[1])-float(d_in))<2e-3))
    print("    V2' = %d (Def 5.1(1): %d roots = (n'/d2')*V2' = %d*V2')" % (V2,biggest,np_//d2))
    print("    closed form = %s ; Phi = %s ; radii agree with measurement: %s"
          % (str(cf), str(ph), ag))
    r = test55k(np_, mp_, M2, V2, kk); show("TEST-55(k)", r)
    print("    FAIL-CLOSED:", "OK (not killed)" if r["verdict"]!="KILLED" else "*** VIOLATION ***")
    return (r["verdict"], ag)

if __name__=="__main__":
    print("== Fail-closed controls: genuine (P,Q) with J = c*gamma^k, s'=2 ==")
    res=[]
    cases=[]
    # A. phi = pi^p (m'=p=k+1), psi = u^q
    for p,q in [(2,2),(2,3),(3,2),(3,3),(4,2),(5,3),(2,5),(5,2),(4,3),(6,2)]:
        cases.append(("A: phi=pi^%d e=-1 k=%d psi=u^%d  (n',m')=(%d,%d)"%(p,p-1,q,p*q,p),
                      [0]*p+[1], -1, p-1, [0]*q+[1], 1))
    # B. m' > k+1 : phi = pi^{m'},  e*gamma^{k+1}
    for mm,kk,q in [(4,1,2),(4,1,3),(6,1,2),(6,2,2),(6,3,2),(4,2,3),(9,2,2)]:
        cases.append(("B: phi=pi^%d e=-1 k=%d psi=u^%d  (n',m')=(%d,%d)"%(mm,kk,q,q*mm,mm),
                      [0]*mm+[1], -1, kk, [0]*q+[1], 1))
    # C. phi with lower terms; psi with lower terms; a != 1
    cases.append(("C1: phi=pi^3+2pi, k=2, psi=u^2+u, a=3", [0,2,0,1], -1, 2, [0,1,1], 3))
    cases.append(("C2: phi=pi^4+pi^2, k=1, psi=u^3, a=-2", [0,0,1,0,1], -5, 1, [0,0,0,1], -2))
    cases.append(("C3: phi=pi^5+pi^3+7, k=4, psi=u^2+3u, a=1", [7,0,0,1,0,1], -1, 4, [0,3,1], 1))
    for c in cases:
        try: res.append((c[0], run(*c)))
        except Exception as ex: print("\n  %s\n    ERROR %s"%(c[0],ex)); res.append((c[0],None))
    print("\n== SUMMARY ==")
    ok = [r for r in res if r[1] is not None]
    print("  s'=2 controls run: %d" % len(ok))
    print("  killed by TEST-55(k): %d   (must be 0)" % sum(1 for _,v in ok if v[0]=="KILLED"))
    print("  closed-form radii matched the numeric measurement: %d / %d"
          % (sum(1 for _,v in ok if v[1]), len(ok)))
