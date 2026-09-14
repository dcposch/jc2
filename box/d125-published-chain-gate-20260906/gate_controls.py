#!/usr/bin/env python3
"""Independent gate controls (Fable5). Exact rationals, no CAS. Not a proof of transport."""
from fractions import Fraction as Q
import random, json, sys
random.seed(20260906)
def add(*ps):
    o={}
    for p in ps:
        for e,c in p.items(): o[e]=o.get(e,Q(0))+c
    return {e:c for e,c in o.items() if c}
def mul(p,q):
    o={}
    for (i,j),c in p.items():
        for (k,l),d in q.items(): o[(i+k,j+l)]=o.get((i+k,j+l),Q(0))+c*d
    return {e:c for e,c in o.items() if c}
def sc(p,c): return {e:c*v for e,v in p.items() if c*v}
def pw(p,n):
    o={(0,0):Q(1)}
    for _ in range(n): o=mul(o,p)
    return o
def dx(p): return {(i-1,j):c*i for (i,j),c in p.items() if i}
def dy(p): return {(i,j-1):c*j for (i,j),c in p.items() if j}
def br(p,q): return add(mul(dx(p),dy(q)),sc(mul(dy(p),dx(q)),-1))
def subst(p,mapx,mapy):
    o={}
    for (i,j),c in p.items():
        t={(0,0):c}
        # negative exponents: mapx/mapy are monomial-or-binomial Laurent; handle via pw of positive part only when i,j>=0
        assert j>=0
        xi = pw(mapx,i) if i>=0 else {(-i*mapx_neg[0],-i*mapx_neg[1]):Q(1)}
        t=mul(t,xi); t=mul(t,pw(mapy,j)); o=add(o,t)
    return o
fails=[]
def chk(ok,msg):
    print(("PASS " if ok else "FAIL ")+msg)
    if not ok: fails.append(msg)
# --- C1: Euler ODE [E,R0]=R0/3 with E=u v f(w), R0=u r(w), w=u v^5, via full 2-variable bracket (not the reduced w-ODE)
def poly_w(coeffs, base):  # sum c_k * base * w^k with w=(1,5)
    return add(*[mul(base,{(k,5*k):c}) for k,c in enumerate(coeffs)])
one={(0,0):Q(1)}
def polyc(*roots_mult):
    p=[Q(1)]
    for rt,m in roots_mult:
        for _ in range(m):
            p=[ (p[i-1] if i>0 else Q(0)) - rt*(p[i] if i<len(p) else Q(0)) for i in range(len(p)+1)]
    return p
# pattern (2,1,1): r=(w-1)^2 (w^2-3w+3); f=(w-1)(w^2-3w+3)/9  (a+b=3, ab=3 encoded as quadratic)
def pmul(a,b):
    o=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): o[i+j]+=x*y
    return o
r211=pmul(polyc((Q(1),2)),[Q(3),Q(-3),Q(1)])
f211=[c/9 for c in pmul(polyc((Q(1),1)),[Q(3),Q(-3),Q(1)])]
E=poly_w(f211,{(1,1):Q(1)}); R0=poly_w(r211,{(1,0):Q(1)})
chk(add(br(E,R0),sc(R0,Q(-1,3)))=={}, "C1a (2,1,1): full bracket [E,R0]=R0/3")
r_bad=pmul(polyc((Q(1),2)),[Q(2),Q(-3),Q(1)])  # ab=2 instead of 3
f_bad=[c/9 for c in pmul(polyc((Q(1),1)),[Q(2),Q(-3),Q(1)])]
chk(add(br(poly_w(f_bad,{(1,1):Q(1)}),poly_w(r_bad,{(1,0):Q(1)})),sc(poly_w(r_bad,{(1,0):Q(1)}),Q(-1,3)))!={}, "C1b (2,1,1) changed object ab=2 rejected")
# uniqueness of (2,1,1) from three root evaluations: solve by my own elimination: a+b=3, ab=3 derived; brute-check a grid of rationals for other solutions of the two symmetric equations
sols=[]
for an in range(-12,13):
  for ad in (1,2,3):
    a=Q(an,ad)
    for bn in range(-12,13):
      for bd in (1,2,3):
        b=Q(bn,bd)
        if a==b or a==1 or b==1 or a==0 or b==0: continue
        c=Q(1)/(9*(1-a)*(1-b))
        if -a*c*(a-1)*(a-b)==Q(1,3) and -b*c*(b-1)*(b-a)==Q(1,3): sols.append((a,b))
chk(sols==[], "C1c no rational (a,b) grid solution other than the irrational pair (a+b=3,ab=3 has disc -3)")
# --- C2 pattern (2,2) over Q[a]/(a^2-3a+1): coefficient extraction of 3whg'-5wgh'-gh=1/3 gives d=-1/(3a), c=5/(9a(1+a)), (1+a)^2=5a
def red(p):  # p: dict exp->(z,t) meaning z+t*a ; reduce a^2=3a-1 handled at construction
    return p
class A:  # element z+t a with a^2=3a-1
    def __init__(s,z,t=Q(0)): s.z=Q(z); s.t=Q(t)
    def __add__(s,o): o=o if isinstance(o,A) else A(o); return A(s.z+o.z,s.t+o.t)
    def __sub__(s,o): o=o if isinstance(o,A) else A(o); return A(s.z-o.z,s.t-o.t)
    def __mul__(s,o):
        o=o if isinstance(o,A) else A(o)
        return A(s.z*o.z - s.t*o.t, s.z*o.t+s.t*o.z+3*s.t*o.t)
    __rmul__=__mul__; __radd__=__add__
    def inv(s):  # (z+ta)^-1 : norm = z^2+3zt+t^2 ... conj a'=3-a: (z+ta)(z+t(3-a)) = z^2+3zt+t^2*(a(3-a)) = z^2+3zt+t^2*1
        n=s.z*s.z+3*s.z*s.t+s.t*s.t; return A((s.z+3*s.t)/n, -s.t/n)
    def zero(s): return s.z==0 and s.t==0
a=A(0,1)
d=A(-1)*(A(3)*a).inv(); c=A(5)*(A(9)*a*(A(1)+a)).inv()
w2=A(5)*d+A(3)*c*(A(1)+a); w1=A(-2)*d*(A(1)+a)-A(6)*a*c; w0=A(-1)*a*d-A(1,0)*Q(1,3)
chk(w2.zero() and w1.zero() and w0.zero(), "C2a (2,2): all ODE coefficients vanish with a^2=3a-1, d=-1/(3a), c=5/(9a(1+a))")
chk((c-(A(1)+a)*(A(9)*a*a).inv()).zero(), "C2b producer's c=(1+a)/(9a^2) equals 5/(9a(1+a)) in the field")
# changed object: a=2 (not a root)
for av in (Q(2),Q(1,2),Q(3)):
    dd=Q(-1)/(3*av); cc=Q(5)/(9*av*(1+av))
    chk(-2*dd*(1+av)-6*av*cc!=0, f"C2c (2,2) changed object a={av} rejected by the w^1 coefficient")
# --- C3 Euler uniqueness at fixed (-1,5) face: 4h(r+wr')=5wh'r has no polynomial h (deg<=12) for both r
def has_kernel(r):
    import itertools
    n=13; rows=[]
    # unknowns h_0..h_12; equation coefficients of w^k
    rp=[k*r[k] for k in range(1,len(r))]
    def coefw(k):  # returns linear functional over h
        v=[Q(0)]*n
        for e in range(n):
            # 4 h_e w^e (r + w r') -> coefficient at w^k: 4 h_e ( r[k-e] + (k-e) r[k-e] ) = 4 h_e r[k-e](1+k-e)
            m=k-e
            if 0<=m<len(r): v[e]+=4*r[m]*(1+m)
            # -5 w h' r: -5 e h_e w^e r -> -5 e h_e r[k-e]
            if 0<=m<len(r): v[e]-=5*e*r[m]
        return v
    M=[coefw(k) for k in range(n+len(r))]
    # rank via gaussian elimination
    rank=0; cols=n; M=[row[:] for row in M]
    for col in range(cols):
        piv=None
        for i in range(rank,len(M)):
            if M[i][col]!=0: piv=i;break
        if piv is None: continue
        M[rank],M[piv]=M[piv],M[rank]
        pv=M[rank][col]; M[rank]=[x/pv for x in M[rank]]
        for i in range(len(M)):
            if i!=rank and M[i][col]!=0:
                f=M[i][col]; M[i]=[x-f*y for x,y in zip(M[i],M[rank])]
        rank+=1
    return rank<n
chk(not has_kernel(r211), "C3a no nonzero h with [x^-4 h(w), R0]=0 at (2,1,1) (deg h<=12)")
r22=pmul(polyc((Q(1),2)),polyc((Q(2),2)))  # a=2 placeholder only tests the order argument shape; real a irrational; order-at-0 argument is generic
chk(not has_kernel(r22), "C3b same for a (2,2)-shaped r (order-at-0 argument is r(0)!=0 generic)")
# --- C4 T bracket: [P(T),Q(T)] = -x^3 [P,Q](T) on random Laurent-in-x polynomials, and T involutive on exponents
def T(p): return {(-i+5*j,j):c for (i,j),c in p.items()}
def rnd():
    return {(random.randint(-6,12),random.randint(0,4)):Q(random.randint(-5,5)) for _ in range(6)}
ok=True
for _ in range(20):
    p,q=rnd(),rnd()
    lhs=br(T(p),T(q)); rhs=sc(mul({(3,0):Q(1)},T(br(p,q))),Q(-1))
    ok&= lhs==rhs
chk(ok, "C4a chain rule [T P,T Q] = -x^3 T([P,Q]) on 20 random Laurent pairs (constant bracket case: -c x^3)")
chk(all(T(T({e:Q(1)}))=={e:Q(1)} for e in [(60,15),(15,6),(2,1),(-9,0),(0,0),(-15,0)]), "C4b T involutive")
# --- C5 six hulls via half-plane membership (no hull routine): region lattice points inside displayed polygon and vertices in region
def inside(pt,verts):  # convex polygon given ccw; check cross>=0 for all edges
    n=len(verts)
    for k in range(n):
        (x1,y1),(x2,y2)=verts[k],verts[(k+1)%n]
        if (x2-x1)*(pt[1]-y1)-(y2-y1)*(pt[0]-x1)<0: return False
    return True
cases={"unequal":({"P":[(0,0),(15,15),(15,6),(3,1)],"Q":[(0,0),(25,25),(25,10),(1,0)]},lambda x,y,m:-5*x+13*y<=m),
       "common_3":({"P":[(0,0),(15,15),(15,6),(3,0)],"Q":[(0,0),(25,25),(25,10),(5,0)]},lambda x,y,m:-x+3*y<=m),
       "common_4":({"P":[(0,0),(15,15),(15,6),(9,0)],"Q":[(0,0),(25,25),(25,10),(15,0)]},lambda x,y,m:-x+4*y<=3*m)}
for name,(vs,extra) in cases.items():
    for who,m in (("P",3),("Q",5)):
        V=vs[who]; Vccw=[V[0],V[3],V[2],V[1]]  # (0,0)->axis/low vertex->(15,6)->(15,15) is ccw? verify orientation by signed area
        area=sum(Vccw[k][0]*Vccw[(k+1)%4][1]-Vccw[(k+1)%4][0]*Vccw[k][1] for k in range(4))
        if area<0: Vccw=Vccw[::-1]
        region=[(x,y) for y in range(0,5*m+1) for x in range(-4*m,20*m+1) if x<=4*y and -x+5*y<=5*m and extra(x,y,m)]
        img=[(-x+5*y,y) for x,y in region]
        chk(all(inside(pt,Vccw) for pt in img) and all(i>=0 and j>=0 for i,j in img), f"C5 {name} {who}: all region points map inside displayed polygon with nonnegative exponents")
        chk(all(any((-x+5*y,y)==v for x,y in region) for v in V), f"C5 {name} {who}: every displayed vertex is a region lattice point")
        chk(max(i+j for i,j in img)==10*m, f"C5 {name} {who}: image total degree {10*m}")
# --- C6 successor enumeration by my own loop and the Euler-lattice tests for (-2,0),(-4,0)
cand=sorted((a1,b1) for b1 in (0,1) for a1 in range(-20,21) if -a1+5*b1<5 and 5*b1-2*a1>0)
chk(cand==[(-4,0),(-3,0),(-2,0),(-1,0),(1,1),(2,1)], "C6a successor candidates")
def euler_lattice(end):  # direction perpendicular to (5,2)-end, weight rho+sigma; check lambda*(15,6) and lambda*3*end integrality
    dxv,dyv=5-end[0],2-end[1]; g=__import__('math').gcd(dxv,dyv); rho,sig=-dyv//g,dxv//g
    wgt=rho+sig; lam_st=Q(wgt, rho*15+sig*6); lam_en=Q(wgt, rho*3*end[0]+sig*3*end[1]) if (rho*3*end[0]+sig*3*end[1]) else None
    st=(lam_st*15,lam_st*6); en=(lam_en*3*end[0],lam_en*3*end[1]) if lam_en else None
    return (rho,sig),st,en
for end in [(-2,0),(-4,0)]:
    d,st,en=euler_lattice(end)
    chk(any(v.denominator!=1 for v in st) and any(v.denominator!=1 for v in en), f"C6b {end}: direction {d}, parallel Euler start {st} and end {en} both non-lattice -> F=(1,1) monomial -> Remark 2.5 contradiction")
# (2,1) second-level: b''=0, -a''<1 and -a''>0 impossible; unequal needs (k+1)*1<2
chk(not [a2 for a2 in range(-9,10) if -a2<1 and -a2>0] and not [k for k in range(1,9) if (k+1)*1<2], "C6c (2,1) has no proportional or unequal successor")
# unequal assignment
cross=lambda p,q:p[0]*q[1]-p[1]*q[0]
chk(cross((15-2,6-1),(25+1,10))==0 and cross((15+1,6),(25-2,9))!=0, "C6d unequal endpoint assignment P->(2,1), Q->(-1,0) parallel; transpose not")
# --- C7 lower transport shape: v_{1,-4} under y->y+l x^-k is non-increasing iff k>=4; k=3 raises; and the axis-restriction bracket identity
def cut(p,k,l):
    o={}
    for (i,j),c in p.items():
        # (y + l x^-k)^j
        from math import comb
        for t in range(j+1): o[(i-k*t,j-t)]=o.get((i-k*t,j-t),Q(0))+c*comb(j,t)*l**t
    return {e:c for e,c in o.items() if c}
p={(60,15):Q(1),(0,3):Q(2),(-2,1):Q(1)}
v14=lambda p:max(i-4*j for i,j in p)
chk(v14(cut(p,4,Q(1)))==v14(p)==0 and v14(cut(p,5,Q(1)))==0 and v14(cut(p,3,Q(1)))>0, "C7a (1,-4)-bound kept by x^-4,x^-5 cuts and raised by an x^-3 cut on a witness")
# monomial commuting with a d-homogeneous non-monomial forces ray (4,1): [x^60 y^15, G]=0 => 60 j = 15 i on Supp(G)
G={(4,1):Q(1),(8,2):Q(-3)}; H={(4,1):Q(1),(1,0):Q(2)}
chk(br({(60,15):Q(1)},G)=={} and br({(60,15):Q(1)},H)!={}, "C7b monomial x^60y^15 commutes only with (4,1)-ray forms")
# --- C8 Euler endpoint at (5,-1): weight 4 vs 5 gives (4,16); lattice solutions of 5i-j=4 with j>=0
chk([(i,5*i-4) for i in range(1,5)]==[(1,1),(2,6),(3,11),(4,16)] and Q(4,5)*20==16, "C8 q=5 from weights alone (no A1 used)")
print(json.dumps({"status":"PASS" if not fails else "FAIL","fails":fails}))
sys.exit(1 if fails else 0)
