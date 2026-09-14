#!/usr/bin/env python3
"""Independent controls for the small-receiver polynomial-lift contract (Fable gate).
Different algorithm from the producer: direct Laurent substitution by cached repeated
multiplication (no closed multinomial), Taylor shift by Horner composition, Q(rho) as
pairs a+b*rho with rho^2=3rho-1 (no monomial reduction). Standard library only."""
import sys, random
from fractions import Fraction as Fr
from math import comb, factorial
MUT=set(a for a in sys.argv[1:] if a.startswith('--mutate'))
def m(n): return n in MUT
random.seed(20260906)
# ---------- Q(rho) ----------
def K(a,b=0): return (Fr(a),Fr(b))
Z=K(0); ONE=K(1); RHO=K(0,1)
def kadd(x,y): return (x[0]+y[0],x[1]+y[1])
def kmul(x,y):
    a,b=x; c,d=y; return (a*c-b*d, a*d+b*c+3*b*d)
def ksc(x,q): return (x[0]*q,x[1]*q)
def kinv(x):
    a,b=x; n=a*a+3*a*b+b*b
    if n==0: raise ZeroDivisionError("not a unit")
    return (Fr(a+3*b)/n, Fr(-b)/n)
def kpow(x,n):
    r=ONE
    for _ in range(n): r=kmul(r,x)
    return r
def kz(x): return x[0]==0 and x[1]==0
# ---------- Laurent polynomials: dict exponent-tuple -> K ----------
NV=4  # slots: receiver (gamma,pi,l2,l3) or source (u,v,l2,l3)
def clean(p): return {e:c for e,c in p.items() if not kz(c)}
def padd(*ps):
    out={}
    for p in ps:
        for e,c in p.items(): out[e]=kadd(out.get(e,Z),c)
    return clean(out)
def psc(p,c): return clean({e:kmul(cc,c) for e,cc in p.items()})
def pmul(p,q):
    out={}
    for e,c in p.items():
        for f,d in q.items():
            g=tuple(a+b for a,b in zip(e,f)); out[g]=kadd(out.get(g,Z),kmul(c,d))
    return clean(out)
def mono(e,c=ONE): return {tuple(e):c}
def var(k,n=1,c=ONE):
    e=[0]*NV; e[k]=n; return mono(e,c)
CONST=mono([0]*NV)
def ppow(p,n):
    r=CONST
    for _ in range(n): r=pmul(r,p)
    return r
def pder(p,k):
    out={}
    for e,c in p.items():
        if e[k]:
            f=list(e); f[k]-=1; out[tuple(f)]=ksc(c,e[k])
    return clean(out)
def jac(p,q): return padd(pmul(pder(p,0),pder(q,1)), psc(pmul(pder(p,1),pder(q,0)),K(-1)))
class Subst:
    """images[k]: Laurent poly; negative powers only for monomial images."""
    def __init__(s,images): s.im=images; s.cache={}
    def power(s,k,n):
        key=(k,n)
        if key not in s.cache:
            if n==0: s.cache[key]=CONST
            elif n>0: s.cache[key]=pmul(s.power(k,n-1),s.im[k])
            else:
                (me,mc),=s.im[k].items()
                s.cache[key]=ppow(mono([-x for x in me],kinv(mc)),-n)
        return s.cache[key]
    def __call__(s,p):
        out={}
        for e,c in p.items():
            term=mono([0]*NV,c)
            for k,n in enumerate(e):
                if n: term=pmul(term,s.power(k,n))
            for f,d in term.items(): out[f]=kadd(out.get(f,Z),d)
        return clean(out)
def req(ok,msg):
    if not ok: raise AssertionError("FAIL "+msg)
    print("PASS",msg)
def rnd(): return K(random.randint(-9,9) or 1)
def rpoly(deg,neg0=0,negmin=None):
    p={}
    for _ in range(deg*3):
        i=random.randint(-neg0,deg); j=random.randint(0,deg-max(i,0)); p=padd(p,var(0,i) if False else mono([i,j,0,0],rnd()))
    return p
# ===== C1 inverse/forward maps, determinants, compositions =====
G_img=var(1,-1)                                          # gamma = v^-1
PI_img=padd(pmul(var(1,4),var(0)), var(1,2,K(-1)) if False else psc(pmul(var(2),var(1,2)),K(-1)), psc(pmul(var(3),var(1)),K(-1)), var(1,-1,K(-1)))
inv=Subst([G_img,PI_img,var(2),var(3)])                  # receiver -> source
U_img=padd(pmul(var(0,4),var(1)), pmul(var(2),var(0,2)), pmul(var(3),var(0,3)), var(0,5))
V_img=var(0,-1)
fwd=Subst([U_img,V_img,var(2),var(3)])                   # source -> receiver
det_inv=jac(G_img,PI_img)
req(det_inv==(var(1,2) if not m('--mutate-det') else var(1,2,K(-1))),"C1a inverse determinant d(gamma,pi)/d(u,v) = +v^2")
req(jac(U_img,V_img)==var(0,2),"C1b forward determinant = +gamma^2")
for k in range(4): req(inv(fwd(var(k)))==var(k) and fwd(inv(var(k)))==var(k),"C1c composition identity on variable %d"%k)
A=rpoly(4,neg0=2); B=rpoly(4,neg0=2)
req(pmul(inv(jac(A,B)),var(1,2))==jac(inv(A),inv(B)),"C1d chain rule [A∘phi,B∘phi] = v^2 ([A,B]∘phi) on random Laurent pair")
# ===== C2 J rows definition and 780 slots =====
rows={}
for e,c in A.items():
    for f,d in B.items():
        r,s=e[0]+f[0]-1,e[1]+f[1]-1; rows[(r,s)]=kadd(rows.get((r,s),Z),ksc(kmul(c,d),e[0]*f[1]-e[1]*f[0]))
req(clean({(r,s,0,0):c for (r,s),c in rows.items()})==jac(A,B),"C2a J_(r,s)=sum(il-jk)a_ij b_kl matches bracket")
req(sum(1 for r in range(39) for s in range(39-r))==780,"C2b 780 J slots for r+s<=38")
# ===== C3 negative rows by direct expansion; compare closed form =====
def closed(i,j,t,b,d):
    z=j-t-b-d
    return K(Fr(factorial(j),factorial(t)*factorial(b)*factorial(d)*factorial(z))*(-1)**(j-t if not m('--mutate-sign') else j))
slotsets={}; maxl={}
for D in (15,25):
    S=set(); ml=0; ok=True
    for j in range(D+1):
        pj=inv.power(1,j)
        for (t,e0,b,d),c in pj.items():
            req_c=closed(0,j,t,b,d)
            if c!=req_c: ok=False
            for i in range(D-j+1):
                e=e0-i
                if e<0: S.add((t,e)); ml=max(ml,b+d)
                req(t+e<=5*D and e<=4*D and 5*t-e<=D,"") if False else None
                if not (t+e<=5*D and e<=4*D and 5*t-e<=D): ok=False
    req(ok,"C3a D=%d every expanded coefficient equals multinomial*(-1)^(j-t); degree/weight bounds"%D)
    exp={(t,e) for t in range((D-1)//5+1) for e in range(5*t-D,0)}
    req(S==exp,"C3b D=%d negative slot set is exactly {t<=floor((D-1)/5), 5t-D<=e<=-1}"%D)
    slotsets[D]=S; maxl[D]=ml
req([len(slotsets[15]),len(slotsets[25])]==[30,75] and maxl=={15:7,25:12},"C3c 30+75=105 slots, max lambda degree 7/12")
# polygons: own half-plane test from consecutive vertices
def inside(poly,i,j):
    n=len(poly); sg=set()
    for k in range(n):
        (a,b),(c,d)=poly[k],poly[(k+1)%n]; cr=(c-a)*(j-b)-(d-b)*(i-a)
        if cr: sg.add(cr>0)
    return len(sg)<=1
polys={"unequal":([(0,0),(0,15),(9,6),(2,1)],[(0,0),(0,25),(15,10),(1,0)]),
       "common3":([(0,0),(0,15),(9,6),(3,0)],[(0,0),(0,25),(15,10),(5,0)]),
       "common4":([(0,0),(0,15),(9,6),(9,0)],[(0,0),(0,25),(15,10),(15,0)])}
for name,(pa,pb) in polys.items():
    for poly,D in ((pa,15),(pb,25)):
        S=set()
        for j in range(D+1):
            te={(t,e0) for (t,e0,b,d) in inv.power(1,j)}
            for i in range(D-j+1):
                if inside(poly,i,j):
                    for (t,e0) in te:
                        if e0-i<0: S.add((t,e0-i))
        req(S==slotsets[D],"C3d %s D=%d polygon negative slots = full list"%(name,D))
# ===== C4 leaders / degrees on random monic fixtures =====
for D in (15,25):
    Apoly={(0,D,0,0):ONE}
    for _ in range(40):
        i=random.randint(0,D); j=random.randint(0,D-i)
        if (i,j)!=(0,D): Apoly[(i,j,0,0)]=rnd()
    lam=Subst([var(0),var(1),mono([0]*NV,K(3)),mono([0]*NV,K(-2))])  # numeric lambdas
    P=lam(inv(Apoly))
    top=[e for e in P if e[0]+e[1]==5*D]
    req(top==[(D,4*D,0,0)] and P[(D,4*D,0,0)]==ONE and max(e[0]+e[1] for e in P)==5*D,"C4a D=%d unique total leader u^%d v^%d, coefficient 1, degree %d"%(D,D,4*D,5*D))
    req(max(e[0] for e in P)<=D and max(e[1] for e in P)<=4*D and max(5*e[0]-e[1] for e in P)<=D,"C4b D=%d box (%d,%d) and weight<=%d"%(D,D,4*D,D))
# ===== C5 real omission control with own verifier =====
def negrows(P): return {(e[0],e[1]) for e in P if e[1]<0}
def polynomial_after(P,omit=frozenset()): return not (negrows(P)-omit)
A0=var(0); B0=padd(pmul(var(0,2),var(1)),var(0,3))
lam0=Subst([var(0),var(1),mono([0]*NV,Z),mono([0]*NV,Z)])
P0=lam0(inv(A0)); Q0=lam0(inv(B0))
req(jac(A0,B0)==var(0,2) and P0==var(1,-1) and Q0==pmul(var(1,2),var(0)) and jac(P0,Q0)==CONST,"C5a toy pair gamma, gamma^2 pi+gamma^3: P=v^-1, Q=v^2 u, [P,Q]=1")
req(negrows(P0)=={(0,-1)} and not polynomial_after(P0),"C5b own verifier rejects the single negative row")
req(polynomial_after(P0,{(0,-1)})==(not m('--mutate-omit')),"C5c omitting exactly that row makes the verifier accept a nonpolynomial P (real omission)")
for f in (ppow(var(0),3), pmul(var(0,2),var(1,3)), padd(var(0),pmul(var(0),var(1)))):
    req(polynomial_after(inv(fwd(f))) and inv(fwd(f))==f,"C5d positive fixture recovers %s"%sorted(f))
# ===== C6 Taylor/graph rows on a rich fixture, both faces, alternative algorithm =====
def poly1(coeffs): return {(0,k,0,0):c for k,c in enumerate(coeffs) if not kz(c)}
def shift_minus1(a):  # a(z) as list of K, return coefficients of a(-1+w) in w via Horner composition
    res=[Z]
    for c in reversed(a):
        # res = res*(w-1) + c
        new=[Z]*(len(res)+1)
        for k,x in enumerate(res):
            new[k+1]=kadd(new[k+1],x); new[k]=kadd(new[k],kmul(x,K(-1)))
        new[0]=kadd(new[0],c); res=new
    return res
for face,h,D0exp in (("squarefree",[Z,Z,ONE,Z,Z,ONE],K(162)),("golden",None,ksc(kpow(RHO,6),6))):
    if h is None:
        # h = z^2 (z+1) (z+1-rho)^2, computed by polynomial multiplication in one variable
        def mul1(a,b):
            out=[Z]*(len(a)+len(b)-1)
            for i,x in enumerate(a):
                for j,y in enumerate(b): out[i+j]=kadd(out[i+j],kmul(x,y))
            return out
        h=mul1(mul1([Z,Z,ONE],[ONE,ONE]),mul1([kadd(ONE,ksc(RHO,-1)),ONE],[kadd(ONE,ksc(RHO,-1)),ONE]))
    Hz=poly1(h); H3z=ppow(Hz,3)
    # A = gamma^15 * H(pi/gamma)^3 + random lower part (all i+j<=14 monomials, coefficients in Q(rho))
    Apoly={}
    for (_,k,_,_),c in H3z.items(): Apoly[(15-k,k,0,0)]=c
    for i in range(15):
        for j in range(15-i):
            Apoly[(i,j,0,0)]=(K(random.randint(-5,5),random.randint(-5,5)) if face=="golden" else rnd())
    P=inv(Apoly)
    # alternative algorithm: P = sum_k v^(k-15) a_k(-1+w), w = v^5 u - l3 v^2 - l2 v^3
    w=padd(pmul(var(1,5),var(0)), psc(pmul(var(3),var(1,2)),K(-1)), psc(pmul(var(2),var(1,3)),K(-1)))
    ak=[[Apoly.get((15-k-j,j,0,0),Z) for j in range(16-k)] for k in range(16)]
    P2={}; wp=[CONST]
    for r in range(1,16): wp.append(pmul(wp[-1],w))
    for k in range(16):
        tay=shift_minus1(ak[k])
        for r,c in enumerate(tay):
            if not kz(c):
                for f,d in psc(pmul(var(1,k-15),wp[r]),c).items(): P2[f]=kadd(P2.get(f,Z),d)
    P2=clean(P2)
    req(P==P2,"C6a %s: direct substitution equals Taylor-graph expansion sum_k v^(k-15) a_k(-1+w)"%face)
    def der_at(k,r):  # a_k^(r)(-1) = r! * Taylor coefficient
        t=shift_minus1(ak[k]); return ksc(t[r],factorial(r)) if r<len(t) else Z
    D0=der_at(0,3)
    req(D0==(D0exp if not m('--mutate-D0') else ksc(kpow(RHO,5),6)),"C6b %s: D0=a_0'''(-1) constant unit %s"%(face,D0))
    if face=="golden": req(kinv(D0)==ksc(kpow(kadd(K(3),ksc(RHO,-1)),6),Fr(1,6)),"C6c golden D0 inverse = (3-rho)^6/6; rho(3-rho)=1")
    def row(P,t,e): return {(0,0,b,d):c for (tt,ee,b,d),c in P.items() if tt==t and ee==e}
    req(row(P,2,-5)=={} and der_at(0,2)==Z,"C6d %s: [u^2 v^-5]P = a_0''(-1)/2 = 0 automatically"%face)
    req(row(P,2,-4)=={(0,0,0,0):ksc(der_at(1,2),Fr(1,2))} if not kz(der_at(1,2)) else row(P,2,-4)=={},"C6e %s: [u^2 v^-4]P = a_1''(-1)/2"%face)
    r3=padd({(0,0,0,0):der_at(2,2)}, psc(var(3),kmul(D0,K(-1)))); r3=psc(r3,K(Fr(1,2)))
    req(row(P,2,-3)==r3,"C6f %s: [u^2 v^-3]P = (a_2''(-1) - lambda3 D0)/2"%face)
    r2=padd({(0,0,0,0):der_at(3,2)}, psc(var(3),kmul(der_at(1,3),K(-1))), psc(var(2),kmul(D0,K(-1)))); r2=psc(r2,K(Fr(1,2)))
    req(row(P,2,-2)==r2,"C6g %s: [u^2 v^-2]P = (a_3''(-1) - lambda3 a_1'''(-1) - lambda2 D0)/2"%face)
    l3v=kmul(der_at(2,2),kinv(D0)); l2v=kmul(kadd(der_at(3,2),kmul(kmul(l3v,der_at(1,3)),K(-1))),kinv(D0))
    ev=Subst([var(0),var(1),mono([0]*NV,l2v),mono([0]*NV,l3v)])
    req(ev(r3)=={} and ev(r2)=={},"C6h %s: graph values lambda3=a_2''/D0, lambda2=(a_3''-lambda3 a_1''')/D0 kill both rows"%face)
    req(len(negrows(ev(P)))>0,"C6i %s: fixture is not itself polynomial (other negative rows remain) - no existence claim"%face)
# ===== C7 scaling covariance with both lambdas; c_tau = c tau^-36 =====
tau=Fr(3); D=15
Apoly={(0,15,0,0):ONE}
for _ in range(30):
    i=random.randint(0,15); j=random.randint(0,15-i); Apoly[(i,j,0,0)]=rnd()
lamv=(K(5),K(-7))
lam=Subst([var(0),var(1),mono([0]*NV,lamv[0]),mono([0]*NV,lamv[1])])
P=lam(inv(Apoly))
Atau={e:ksc(c,tau**(e[0]+e[1]-D)) for e,c in Apoly.items()}
s2,s3=(3,2) if not m('--mutate-scale') else (2,3)
lamt=Subst([var(0),var(1),mono([0]*NV,ksc(lamv[0],tau**-s2)),mono([0]*NV,ksc(lamv[1],tau**-s3))])
Ptau=lamt(inv(Atau))
want={e:ksc(c,tau**(5*e[0]-e[1]-D)) for e,c in P.items()}
req(Ptau==want,"C7a A_tau=tau^-15 A(tau.) with lambda2 tau^-3, lambda3 tau^-2 gives tau^-15 P(tau^5 u, tau^-1 v)")
req(Atau[(0,15,0,0)]==ONE,"C7b monicity of pi^15 persists under dilation")
A0t={e:ksc(c,tau**(e[0]+e[1]-15)) for e,c in A0.items()}; B0t={e:ksc(c,tau**(e[0]+e[1]-25)) for e,c in B0.items()}
req(jac(A0t,B0t)==var(0,2,K(tau**-36)),"C7c [A_tau,B_tau] = c tau^-36 gamma^2")
# constants translation harmless
Ac=padd(Apoly,mono([0]*NV,K(11)))
req(padd(lam(inv(Ac)),mono([0]*NV,K(-11)))==P,"C7d subtracting the receiver constant subtracts the same constant from P; negative rows unchanged")
# ===== C8 field and degree criterion arithmetic =====
req(kmul(RHO,kadd(K(3),ksc(RHO,-1)))==ONE,"C8a rho*(3-rho)=1 in Q[rho]/(rho^2-3rho+1)")
req(all(q*q!=5 for q in range(-3,4)) and 125%75!=0 and 75%125!=0,"C8b disc 5 nonsquare; neither of 75,125 divides the other")
kap=RHO; c_uneq=ksc(kinv(kap),Fr(-5,9)); req(not kz(c_uneq) and not kz(ksc(K(1),Fr(-5,9))),"C8c c=-5/(9 kappa) is a nonzero constant for kappa in {1,rho}: %s"%(c_uneq,))
print("ALL PASS")
