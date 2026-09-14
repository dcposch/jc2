#!/usr/bin/env python3
"""Independent exact controls for the (15,25) monomial-J receiver composition.
sympy only; no ideal build, no solve. Every check prints PASS/FAIL; exit 1 on any FAIL."""
import sys, random
from itertools import product
from math import gcd
import sympy as sp
from sympy import Rational as Q, sqrt, symbols, expand, Poly, simplify, cancel, S

random.seed(20260906)
x,y,g,p,tau = symbols('x y gamma pi tau')
fails=[]
def chk(name, ok):
    print(("PASS " if ok else "FAIL ")+name); 
    if not ok: fails.append(name)

def br(P,Qq,u,v): return expand(sp.diff(P,u)*sp.diff(Qq,v)-sp.diff(P,v)*sp.diff(Qq,u))
def Smap(U): return expand(U.subs({x:g, y:p/g}, simultaneous=True))
def T5(U): return expand(U.subs({x:1/x, y:x**5*y}, simultaneous=True))
def T4(U): return expand(U.subs({x:1/g, y:g**4*p}, simultaneous=True))

# --- C1 maps: determinants and chain rules on random Laurent pairs ---
def randpoly(vars_, expo, n=6):
    return sum(Q(random.randint(-5,5)) * vars_[0]**i * vars_[1]**j for (i,j) in random.sample(expo, n))
expo_ij=[(i,j) for i in range(0,8) for j in range(0,i+1)]      # i>=j supports
ok=True
for _ in range(5):
    U=randpoly((x,y),expo_ij); V=randpoly((x,y),expo_ij)
    ok &= expand(br(Smap(U),Smap(V),g,p) - Smap(br(U,V,x,y))/g)==0
chk("C1a [S U,S V] = gamma^-1 S([U,V]) (5 random pairs, i>=j)", ok)
expo_L=[(i,j) for i in range(-6,8) for j in range(0,6)]
ok=True
for _ in range(5):
    U=randpoly((x,y),expo_L); V=randpoly((x,y),expo_L)
    ok &= expand(br(T4(U),T4(V),g,p) + g**2*T4(br(U,V,x,y)))==0
    ok &= expand(Smap(T5(U))-T4(U))==0
chk("C1b [T4 P,T4 Q] = -gamma^2 T4([P,Q]) and T4 = S o T5 (5 random Laurent pairs)", ok)
chk("C1c Jac S = 1/gamma, Jac T4 = -gamma^2 (symbolic)",
    simplify(sp.Matrix([[g, p/g]]).jacobian([g,p]).det()-1/g)==0 and
    simplify(sp.Matrix([[1/g, g**4*p]]).jacobian([g,p]).det()+g**2)==0)
chk("C1d S inverse U(x,y)=A(x,xy) on random pair", all(expand(Smap(U).subs({g:x,p:x*y},simultaneous=True)-U)==0 for U in [randpoly((x,y),expo_ij) for _ in range(3)]))

# --- C2 full-row transport, coefficientwise in symbolic coefficient names (tiny polygon) ---
old_supp_U=[(i,j) for i in range(0,5) for j in range(0,i+1)]
old_supp_V=[(i,j) for i in range(0,4) for j in range(0,i+1)]
cu=symbols('u0:%d'%len(old_supp_U)); cv=symbols('v0:%d'%len(old_supp_V))
U=sum(c*x**i*y**j for c,(i,j) in zip(cu,old_supp_U)); V=sum(c*x**i*y**j for c,(i,j) in zip(cv,old_supp_V))
rows_old=Poly(br(U,V,x,y)-x**3, x,y).as_dict()
rows_new=Poly(br(Smap(U),Smap(V),g,p)-g**2, g,p).as_dict()
ok = all(I-J>=1 for (I,J) in rows_old) and set(rows_new)=={(I-J-1,J) for (I,J) in rows_old} \
     and all(expand(rows_new[(I-J-1,J)]-rows_old[(I,J)])==0 for (I,J) in rows_old)
chk("C2 every old row has I-J>=1; new rows = old rows renamed by (I,J)->(I-J-1,J), identical coefficient polynomials, target (3,0)->(2,0)", ok)

# --- C3 lattice counts by explicit half-planes + Pick ---
cases={"unequal":([(0,0),(0,15),(9,6),(2,1)],[(0,0),(0,25),(15,10),(1,0)]),
       "common_3":([(0,0),(0,15),(9,6),(3,0)],[(0,0),(0,25),(15,10),(5,0)]),
       "common_4":([(0,0),(0,15),(9,6),(9,0)],[(0,0),(0,25),(15,10),(15,0)])}
def inside(pt,poly):
    # convex polygon given counterclockwise or clockwise: point inside iff on same side of all edges
    n=len(poly); s=[]
    for k in range(n):
        (a,b),(c,d)=poly[k],poly[(k+1)%n]; s.append((c-a)*(pt[1]-b)-(d-b)*(pt[0]-a))
    return all(v>=0 for v in s) or all(v<=0 for v in s)
def lattice(poly):
    return [(i,j) for i in range(0,max(v[0] for v in poly)+1) for j in range(0,max(v[1] for v in poly)+1) if inside((i,j),poly)]
def pick(poly):
    n=len(poly); A2=abs(sum(poly[k][0]*poly[(k+1)%n][1]-poly[(k+1)%n][0]*poly[k][1] for k in range(n)))
    B=sum(gcd(abs(poly[k][0]-poly[(k+1)%n][0]),abs(poly[k][1]-poly[(k+1)%n][1])) for k in range(n))
    return (A2+B+2)//2
expected={"unequal":(83,215),"common_3":(94,241),"common_4":(115,296)}
L={}
for k,(PA,PB) in cases.items():
    L[k]=(lattice(PA),lattice(PB))
    chk(f"C3 {k} counts {len(L[k][0])},{len(L[k][1])} == pick {pick(PA)},{pick(PB)} == producer {expected[k]}",
        (len(L[k][0]),len(L[k][1]))==(pick(PA),pick(PB))==expected[k])
# bijection with old (30,50) polygons: old = image under (a,b)->(a+b,b)
old_cases={"unequal":([(0,0),(15,15),(15,6),(3,1)],[(0,0),(25,25),(25,10),(1,0)]),
           "common_3":([(0,0),(15,15),(15,6),(3,0)],[(0,0),(25,25),(25,10),(5,0)]),
           "common_4":([(0,0),(15,15),(15,6),(9,0)],[(0,0),(25,25),(25,10),(15,0)])}
ok=True
for k in cases:
    for new,old in zip(L[k],old_cases[k]):
        ok &= sorted((a+b,b) for (a,b) in new)==sorted(lattice(old))
chk("C3x S is a lattice bijection old (30,50) polygons -> new (15,25) polygons (all six)", ok)

# --- C4 outer face from the predecessor's face data, both quartic patterns, both conjugates ---
w=symbols('w')
def check_ode(r,f):  # predecessor: 4 w f r' - 5 w f' r - f r = r/3
    return expand(4*w*f*sp.diff(r,w)-5*w*sp.diff(f,w)*r-f*r-r/3)==0
r_sq=(w-1)**2*(w**2-3*w+3); f_sq=(w-1)*(w**2-3*w+3)/9
chk("C4a squarefree pattern (2,1,1): r=(w-1)^2(w^2-3w+3), f=(w-1)(w^2-3w+3)/9 satisfy the Euler ODE", check_ode(r_sq,f_sq))
def golden(a):
    gg=(w-1)*(w-a); r=gg**2; f=gg*((1+a)/(9*a**2)*w-1/(3*a)); return r,f
ok=True
for a in [(3+sqrt(5))/2,(3-sqrt(5))/2]:
    r,f=golden(a); ok &= simplify(expand(4*w*f*sp.diff(r,w)-5*w*sp.diff(f,w)*r-f*r-r/3))==0
chk("C4b golden pattern (2,2): both conjugates a=(3±sqrt5)/2 satisfy the Euler ODE", ok)
def H_from_r(r):
    h=sp.quo(r,(w-1)**2,w); R0cut=(y+x**-5)*(x**5*y)**2*h.subs(w,1+x**5*y)
    return expand(T4(expand(R0cut))), h
H0,h0=H_from_r(r_sq)
chk("C4c squarefree: T4 of cut face = pi^2 (pi^3+gamma^3), kappa=h(1)=1", expand(H0-p**2*(p**3+g**3))==0 and h0.subs(w,1)==1)
ok=True; kap={}
for lab,a in [("rho+",(3+sqrt(5))/2),("rho-",(3-sqrt(5))/2)]:
    r,_=golden(a); Hg,hg=H_from_r(r)
    target=p**2*(p+g)*(p+(1-a)*g)**2
    expanded=p**2*(p**3+(3-2*a)*g*p**2+(2-a)*g**2*p+a*g**3)
    ok &= simplify(expand(Hg-target))==0 and simplify(expand(Hg-expanded))==0
    ok &= simplify(hg.subs(w,1)-a)==0 and simplify((1-a)**2-a)==0
    kap[lab]=a
    # polynomiality, homogeneity of degree 5, nonnegative exponents
    ok &= all(i+j==5 and i>=0 and j>=0 for (i,j) in Poly(Hg,g,p).as_dict())
chk("C4d golden: H = pi^2 (pi+gamma)(pi+(1-rho)gamma)^2 = pi^2[pi^3+(3-2rho)gamma pi^2+(2-rho)gamma^2 pi+rho gamma^3], kappa=rho=h(1), (1-rho)^2=rho, both conjugates, homogeneous deg 5", ok)
chk("C4e golden and squarefree faces distinct; rho nonzero, !=1; cubic factors distinct", 
    all(simplify(expand((p**2*(p+g)*(p+(1-a)*g)**2)-H0))!=0 and a!=0 and simplify(a-1)!=0 and simplify((1-a)-1)!=0 for a in kap.values()))

# --- C5 inner faces: unequal bracket, target-weight, solved constants; common faces transport ---
a_,b_,d_,e_,f_,c_,mu,kappa=symbols('a b d e f c mu kappa')
Af=a_*g**2*p+b_*g**9*p**6; Bf=d_*g+e_*g**8*p**5+f_*g**15*p**10
B=br(Af,Bf,g,p)
chk("C5a unequal face bracket = -ad gamma^2 + (2ae-6bd) gamma^9 pi^5 + (5af-3be) gamma^16 pi^10",
    expand(B-(-a_*d_*g**2+(2*a_*e_-6*b_*d_)*g**9*p**5+(5*a_*f_-3*b_*e_)*g**16*p**10))==0)
def wmax(poly,wt): 
    vals={(i,j):wt[0]*i+wt[1]*j for (i,j) in lattice(poly)}; m=max(vals.values()); return m,[k for k,v in vals.items() if v==m]
mA,fA=wmax(cases["unequal"][0],(5,-7)); mB,fB=wmax(cases["unequal"][1],(5,-7))
chk("C5b (5,-7) is the top weight on both unequal polygons: A max 3 on {(2,1),(9,6)}, B max 5 on {(1,0),(8,5),(15,10)}, bracket weight 3+5+2 = 10 = weight of gamma^2",
    (mA,sorted(fA))==(3,[(2,1),(9,6)]) and (mB,sorted(fB))==(5,[(1,0),(8,5),(15,10)]) and mA+mB-(5-7)==5*2)
sol=sp.solve([2*a_*e_-6*b_*d_, 5*a_*f_-3*b_*e_],[d_,e_],dict=True)[0]
sol={k:v.subs({b_:kappa**3,f_:kappa**5}) for k,v in sol.items()}
chk("C5c monic: e=(5/3) a kappa^2, d=(5/9) a^2/kappa, c=-ad=-(5/9) a^3/kappa",
    simplify(sol[e_]-Q(5,3)*a_*kappa**2)==0 and simplify(sol[d_]-Q(5,9)*a_**2/kappa)==0)
root_vals={k:v.subs(a_,1) for k,v in sol.items()}
chk("C5d root normalization a=1: e=5kappa^2/3, d=5/(9kappa), c=-5/(9kappa)",
    simplify(root_vals[e_]-Q(5,3)*kappa**2)==0 and simplify(root_vals[d_]-Q(5,9)/kappa)==0)
ok=True
for kv in [S(1),kap["rho+"],kap["rho-"]]:
    dd=Q(5,9)/kv; cc=-Q(5,9)/kv; ee=Q(5,3)*kv**2
    Afull=g**2*p+kv**3*g**9*p**6; Bfull=dd*g+ee*g**8*p**5+kv**5*g**15*p**10
    ok &= simplify(expand(br(Afull,Bfull,g,p)-cc*g**2))==0 and simplify(cc)!=0 and simplify(dd)!=0
    if kv!=1: ok &= simplify(cc+Q(5,9)*(3-kv))==0   # 1/rho = 3-rho only for the golden conjugates (own earlier check wrongly applied it at kappa=1)
chk("C5e a=1 faces bracket to c gamma^2 with c=-5/(9kappa) != 0, d != 0 for kappa in {1, rho+, rho-}; c in Q(kappa)", ok)
chk("C5f c cannot also be 1 after a=1: c=-5/(9kappa) equals 1 for no kappa in {1,rho+,rho-}", all(simplify(-Q(5,9)/kv-1)!=0 for kv in [S(1),kap["rho+"],kap["rho-"]]))
chk("C5g common_3 transport x^-1(x^3y-mu)^2 -> gamma(gamma pi-mu)^2; common_4 x^-3(x^4y-mu)^2 -> gamma^3(pi-mu)^2",
    expand(T4(expand(x**-1*(x**3*y-mu)**2))-g*(g*p-mu)**2)==0 and expand(T4(expand(x**-3*(x**4*y-mu)**2))-g**3*(p-mu)**2)==0)
G3=g*(g*p-mu)**2; G4=g**3*(p-mu)**2
ok=True
for k,Gk,wt,facesA,facesB in [("common_3",G3,(1,-1),[(3,0),(9,6)],[(5,0),(15,10)]),("common_4",G4,(1,0),[(9,0),(9,6)],[(15,0),(15,10)])]:
    PA,PB=cases[k]
    sA=set(Poly(expand(Gk**3),g,p).as_dict()); sB=set(Poly(expand(Gk**5),g,p).as_dict())
    mA,fA=wmax(PA,wt); mB,fB=wmax(PB,wt)
    ok &= sA==set(fA) and sB==set(fB)  # face supports = full top-weight lattice segments
    ok &= Poly(expand(Gk**3),g,p).as_dict()[(9,6)]==1 and Poly(expand(Gk**5),g,p).as_dict()[(15,10)]==1  # monic at shared corner
    ok &= mA+mB-(wt[0]+wt[1]) > 2*wt[0]   # face bracket weight exceeds target weight -> must commute
    ok &= expand(br(Gk**3,Gk**5,g,p))==0
chk("C5h common faces: Gk^3/Gk^5 supports are exactly the full top-weight segments, monic at (9,6)/(15,10) so scalars are kappa^3, kappa^5; bracket weight exceeds target so they commute", ok)

# --- C6 normalizations: translation, target scaling, dilation ---
cA=symbols('A0:12'); cB=symbols('B0:16')
suppA=random.sample(L["unequal"][0],12); suppB=random.sample(L["unequal"][1],16)
A=sum(c*g**i*p**j for c,(i,j) in zip(cA,suppA)); Bp=sum(c*g**i*p**j for c,(i,j) in zip(cB,suppB))
lamP,lamQ,k0=symbols('lambdaP lambdaQ k0')
chk("C6a translation A+k0, B+k0 leaves the bracket unchanged", expand(br(A+k0,Bp+k0,g,p)-br(A,Bp,g,p))==0)
chk("C6b target scaling A/lamP, B/lamQ divides the bracket by lamP*lamQ", expand(br(A/lamP,Bp/lamQ,g,p)-br(A,Bp,g,p)/(lamP*lamQ))==0)
def dil(F,k): return expand(tau**(-k)*F.subs({g:tau*g,p:tau*p},simultaneous=True))
chk("C6c dilation: [A_tau,B_tau] = tau^-38 ([A,B])(tau gamma,tau pi); on c gamma^2 gives c tau^-36 gamma^2",
    expand(br(dil(A,15),dil(Bp,25),g,p)-tau**-38*br(A,Bp,g,p).subs({g:tau*g,p:tau*p},simultaneous=True))==0
    and expand(tau**-38*(c_*g**2).subs({g:tau*g,p:tau*p},simultaneous=True)-c_*tau**-36*g**2)==0)
Hs=p**2*(p**3+kappa*g**3); Hgen=p**2*(p**3+(3-2*kappa)*g*p**2+(2-kappa)*g**2*p+kappa*g**3)
chk("C6d dilation fixes both outer faces H^3, H^5 entirely (all slope ratios, kappa)",
    all(expand(dil(H**3,15)-H**3)==0 and expand(dil(H**5,25)-H**5)==0 for H in [Hs,Hgen]))
chk("C6e dilation: unequal a->a/tau^12, e->e/tau^12, d->d/tau^24, b,f fixed; common_3 mu->mu/tau^2; common_4 mu->mu/tau",
    expand(dil(Af,15)-(a_/tau**12*g**2*p+b_*g**9*p**6))==0 and expand(dil(Bf,25)-(d_/tau**24*g+e_/tau**12*g**8*p**5+f_*g**15*p**10))==0
    and expand(dil(G3**3,15)-(G3**3).subs(mu,mu/tau**2))==0 and expand(dil(G4**3,15)-(G4**3).subs(mu,mu/tau))==0)
chk("C6f vertex coefficients scale by nonzero tau-powers (nonzero stays nonzero); origin coefficient multiplies by tau^-15/tau^-25",
    all(expand(dil(g**i*p**j,15)/(g**i*p**j))==tau**(i+j-15) for (i,j) in [(0,0),(0,15),(9,6),(2,1),(3,0),(9,0)]))
# residual torus after a=1: tau^12=1 only (unequal); after mu=1: tau^2=1 (common_3), tau=1 (common_4)
chk("C6g residual dilation after the root normalizations: mu_12 (unequal), mu_2 (common_3), trivial (common_4); c cannot be further normalized there",
    sp.solve(tau**12-1,tau).__len__()==12 and sp.solve(tau**2-1,tau).__len__()==2 and sp.solve(tau-1,tau)==[1])
# composite normalization on an arbitrary unequal face point: a0!=1 -> a=1 with the root's constants (needs tau^12=a0 over Kbar)
a0=Q(7); kv=kap["rho+"]
d0=Q(5,9)*a0**2/kv; e0=Q(5,3)*a0*kv**2
Af0=a0*g**2*p+kv**3*g**9*p**6; Bf0=d0*g+e0*g**8*p**5+kv**5*g**15*p**10
t=sp.root(a0,12)
An=expand(dil(Af0,15).subs(tau,t)); Bn=expand(dil(Bf0,25).subs(tau,t))
chk("C6h explicit normalization of an a=7 golden face point by tau=7^(1/12): lands on a=1, d=5/(9rho), e=5rho^2/3, c=-5/(9rho) (algebraic extension needed)",
    simplify(expand(An-(g**2*p+kv**3*g**9*p**6)))==0 and simplify(expand(Bn-(Q(5,9)/kv*g+Q(5,3)*kv**2*g**8*p**5+kv**5*g**15*p**10)))==0
    and simplify(expand(br(An,Bn,g,p)+Q(5,9)/kv*g**2))==0 and not t.is_rational)

# --- C7 unknown / row counts of the proposed guarded presentation (no ideal built) ---
def seg(P0,P1):
    dx,dy=P1[0]-P0[0],P1[1]-P0[1]; s=gcd(abs(dx),abs(dy)); return [(P0[0]+dx//s*k,P0[1]+dy//s*k) for k in range(s+1)]
forced={"unequal":(seg((0,15),(9,6))+seg((2,1),(9,6)), seg((0,25),(15,10))+seg((1,0),(15,10))),
        "common_3":(seg((0,15),(9,6))+seg((3,0),(9,6)), seg((0,25),(15,10))+seg((5,0),(15,10))),
        "common_4":(seg((0,15),(9,6))+seg((9,0),(9,6)), seg((0,25),(15,10))+seg((15,0),(15,10)))}
print("case | free A | free B | extra vars | rows of [A,B]-c gamma^2 (potential)")
for k in cases:
    fa=set(forced[k][0]); fb=set(forced[k][1])
    freeA=len(set(L[k][0])-fa-{(0,0)}); freeB=len(set(L[k][1])-fb-{(0,0)})
    rows=set()
    for (i,j) in L[k][0]:
        for (kk,l) in L[k][1]:
            if i*l-j*kk!=0: rows.add((i+kk-1,j+l-1))
    extra = 0 if k=="unequal" else 2
    print(f"{k} | {freeA} | {freeB} | {extra} | {len(rows)}")
    chk(f"C7 {k}: all potential rows have nonnegative exponents; (2,0) is a potential row", all(I>=0 and J>=0 for (I,J) in rows) and (2,0) in rows)
# N(A) subset N(B) (optional B -> B + lambda A same-field reduction; not required)
chk("C7x N(A) ⊆ N(B) in all three cases (so B->B+lambda*A is an extra same-field symmetry; optional, not needed)",
    all(set(L[k][0])<=set(L[k][1]) for k in cases))

# --- C8 negative controls (must FAIL when the claim is wrong) ---
neg=[]
neg.append(("wrong kappa=2 in golden ODE", simplify(expand(4*w*golden(2)[1]*sp.diff(golden(2)[0],w)-5*w*sp.diff(golden(2)[1],w)*golden(2)[0]-golden(2)[1]*golden(2)[0]-golden(2)[0]/3))==0))
neg.append(("wrong sign +ad in unequal bracket", expand(B-(a_*d_*g**2+(2*a_*e_-6*b_*d_)*g**9*p**5+(5*a_*f_-3*b_*e_)*g**16*p**10))==0))
neg.append(("wrong scaling exponent tau^-35", expand(tau**-38*(c_*g**2).subs({g:tau*g,p:tau*p},simultaneous=True)-c_*tau**-35*g**2)==0))
neg.append(("wrong row shift (I-J,J)", set(rows_new)=={(I-J,J) for (I,J) in rows_old}))
neg.append(("wrong golden coefficient (3-rho) gamma pi^2", all(simplify(expand(H_from_r(golden(a)[0])[0]-p**2*(p**3+(3-a)*g*p**2+(2-a)*g**2*p+a*g**3)))==0 for a in kap.values())))
neg.append(("wrong T3 instead of T4 composition", expand(Smap(T5(x**2*y))-expand((x**2*y).subs({x:1/g,y:g**3*p},simultaneous=True)))==0))
for name,res in neg:
    chk("C8 negative control rejected: "+name, res is False)

print("TOTAL FAILS:",len(fails)); sys.exit(1 if fails else 0)
