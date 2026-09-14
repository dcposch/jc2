#!/usr/bin/env python3
"""Own changed-object controls for the (25,15) positive-face slope screen.
Exact Fraction arithmetic on sparse bivariate/univariate polynomials. No CAS."""
from fractions import Fraction as F
import itertools, json, resource, signal, time
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU,(25,25)); signal.alarm(30)
t0=time.monotonic(); passed=[]
def ok(cond,name):
    if not cond: raise RuntimeError('FAIL '+name)
    passed.append(name)
# ---- generic sparse polys over Q in N variables (exponent tuples) ----
def P(d): return {k:F(v) for k,v in d.items() if v}
def add(p,q):
    r=dict(p)
    for k,v in q.items(): r[k]=r.get(k,0)+v
    return {k:v for k,v in r.items() if v}
def neg(p): return {k:-v for k,v in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    r={}
    for k1,v1 in p.items():
        for k2,v2 in q.items():
            k=tuple(a+b for a,b in zip(k1,k2)); r[k]=r.get(k,0)+v1*v2
    return {k:v for k,v in r.items() if v}
def sc(p,c): return {k:v*F(c) for k,v in p.items() if v*F(c)}
def pw(p,n):
    r=P({(0,)*len(next(iter(p))):1})
    for _ in range(n): r=mul(r,p)
    return r
def dif(p,i):
    r={}
    for k,v in p.items():
        if k[i]:
            kk=list(k); kk[i]-=1; r[tuple(kk)]=r.get(tuple(kk),0)+v*k[i]
    return {k:v for k,v in r.items() if v}
# ---- bivariate (gamma,pi): index 0 = gamma, 1 = pi; bracket [A,B]=A_g B_p - A_p B_g ----
G=P({(1,0):1}); PI=P({(0,1):1}); ONE=P({(0,0):1})
def br(A,B): return sub(mul(dif(A,0),dif(B,1)),mul(dif(A,1),dif(B,0)))
def lin(s): return sub(PI,sc(G,s))           # pi - s*gamma
def H_of(S): return mul(pw(PI,2),S)
def ez(coeffs):                                 # E = gamma^4 e(z), e given as coefficient list in z = pi/gamma
    E={}
    for j,c in enumerate(coeffs):
        E=add(E,P({(4-j,j):c}))
    return E
# 1. Direct derivation control of (E): [gamma^4 e(z), gamma^5 h(z)] = gamma^7 (4 e h' - 5 e' h), for random e,h
import random; random.seed(2515)
for trial in range(6):
    ec=[F(random.randint(-5,5)) for _ in range(5)]; hc=[F(random.randint(-5,5)) for _ in range(6)]
    E=ez(ec); Hh={}
    for j,c in enumerate(hc): Hh=add(Hh,P({(5-j,j):c}))
    # univariate e,h in z as 1-var polys (index tuple (j,))
    e1={(j,):c for j,c in enumerate(ec) if c}; h1={(j,):c for j,c in enumerate(hc) if c}
    rhs1=sub(sc(mul(e1,dif(h1,0)),4),sc(mul(dif(e1,0),h1),5))
    # homogenise rhs1 to (gamma,pi) with total degree 7
    rhs={(7-j,j):c for (j,),c in rhs1.items()}
    ok(br(E,Hh)==rhs,'derivation of (E) bivariate=univariate trial %d'%trial)
# 2. [3] partition: exact bivariate identity [E,H^5] = gamma^2 H^5 with the charged E
S3=pw(lin(1),3); H3=H_of(S3)
e3=[0,F(7,105),F(-42,105),F(60,105),F(-25,105)]   # z(z-1)(-25z^2+35z-7)/105 expanded
E3=ez(e3)
ok(sc(br(E3,H3),5)==mul(pw(G,2),H3),'[3]: 5[E,H]=gamma^2 H bivariate')
ok(br(E3,pw(H3,5))==mul(pw(G,2),pw(H3,5)),'[3]: [E,H^5]=gamma^2 H^5 bivariate (P component)')
ok(br(sc(E3,F(5,3)),pw(H3,3))==mul(pw(G,2),pw(H3,3)),'[3]: [(5/3)E,H^3]=gamma^2 H^3 (Q component)')
ok(br(E3,pw(H3,3))!=mul(pw(G,2),pw(H3,3)),'[3]: unscaled E fails for Q component (scaling load-bearing)')
# 3. pi | E and root divisibility: solve the LINEAR system for e (deg<=4) from 5(4eh'-5e'h)=h at a=2 ([2,1]) and generic [1,1,1]
def solve_linear(rows,ncols):
    """rows: list of (coeff list length ncols, rhs); exact Gaussian elimination; returns (rank, consistent, particular solution or None)"""
    M=[[F(x) for x in r]+[F(b)] for r,b in rows]; piv=[]; r=0
    for c in range(ncols):
        p=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]; pv=M[r][c]; M[r]=[x/pv for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[x-f*y for x,y in zip(M[i],M[r])]
        piv.append(c); r+=1
    consistent=all(any(row[c]!=0 for c in range(ncols)) or row[ncols]==0 for row in M)
    return r,consistent
def euler_system(hc):
    """h univariate coeff list; unknown e coeffs e0..e4; equation 5(4 e h' - 5 e' h) - h = 0 coefficientwise."""
    h={(j,):c for j,c in enumerate(hc) if c}; hp=dif(h,0)
    rows=[]
    degmax=len(hc)+4
    for d in range(degmax+1):
        coeffs=[]
        for j in range(5):
            ej={(j,):F(1)}
            expr=sub(sc(mul(ej,hp),20),sc(mul(dif(ej,0),h),25))
            coeffs.append(expr.get((d,),F(0)))
        rows.append((coeffs,h.get((d,),F(0))))
    return rows
def hcoeffs(roots_mult):
    h={(0,):F(1)}
    for root,m in roots_mult:
        for _ in range(m): h=mul(h,{(1,):F(1),(0,):F(-root)})
    return [h.get((j,),F(0)) for j in range(max(k[0] for k in h)+1)]
# [2,1] with a=2 (unforced) : inconsistent; a=golden root cannot be exact-rational, so test the polynomial residual instead
rk,cons=solve_linear(euler_system(hcoeffs([(0,2),(1,2),(2,1)])),5); ok(not cons,'[2,1] a=2: Euler system inconsistent (rank %d)'%rk)
rk,cons=solve_linear(euler_system(hcoeffs([(0,2),(1,2),(3,1)])),5); ok(not cons,'[2,1] a=3: Euler system inconsistent (denominator branch has no hidden solution)')
rk,cons=solve_linear(euler_system(hcoeffs([(0,2),(1,3)])),5); ok(cons,'[3]: Euler system consistent')
# [2,1] symbolic in a: work in Q[a] via 3-var polys (z,a,dummy)? Instead: undivided identity check with generic N and residual 30 z (a^2-a-1) h, in vars (z,a)
def P2(d): return {k:F(v) for k,v in d.items() if v}
Z=P2({(1,0):1}); A=P2({(0,1):1}); I2=P2({(0,0):1})
h21=mul(mul(pw(Z,2),pw(sub(Z,I2),2)),sub(Z,A))
Npoly=mul(mul(mul(Z,sub(Z,I2)),sub(Z,A)),sub(sub(sc(I2,3),A),sc(Z,5)))
lhs=sub(sc(sub(sc(mul(Npoly,dif(h21,0)),4),sc(mul(dif(Npoly,0),h21),5)),5),mul(sc(mul(A,sub(sc(I2,3),A)),15),h21))
gold=sub(sub(pw(A,2),A),I2)
ok(lhs==sc(mul(mul(Z,gold),h21),30),'[2,1]: undivided identity 5(4Nh\'-5N\'h)-15a(3-a)h = 30 z (a^2-a-1) h')
# necessity: with e=z(z-1)(z-a)(Az+B) generic, extract the three coefficient equations in (A,B,a); vars (z,a,Aq,Bq)
def P4(d): return {k:F(v) for k,v in d.items() if v}
Z4=P4({(1,0,0,0):1}); A4=P4({(0,1,0,0):1}); AA=P4({(0,0,1,0):1}); BB=P4({(0,0,0,1):1}); I4=P4({(0,0,0,0):1})
h4=mul(mul(pw(Z4,2),pw(sub(Z4,I4),2)),sub(Z4,A4))
e4=mul(mul(mul(Z4,sub(Z4,I4)),sub(Z4,A4)),add(mul(AA,Z4),BB))
res=sub(sc(sub(sc(mul(e4,dif(h4,0)),4),sc(mul(dif(e4,0),h4),5)),5),h4)
# collect by z-degree
byz={}
for k,v in res.items(): byz.setdefault(k[0],{})[k[1:]]=v
# Expect: res = z^2 (z-1)(z-a) * [cubic in z], so only 3 independent equations remain after dividing; report their count and check the report's three rows
# Divide res by z^2 (z-1)(z-a) exactly: do it by checking res == z^2 (z-1)(z-a) * R with R the three-term claimed
# claimed rows: 5B+(3-a)A=0, -(2+6a)B-2aA=0, 3aB=1/5  -> check they generate: substitute B=1/(15a) impossible rationally; instead verify residual coefficients are in the ideal by evaluating at a=2,A,B numeric grid
eqs_hold=True
for a_val in (F(2),F(5),F(-1),F(7,3)):
    for Av in (F(1),F(-2),F(3,7)):
        for Bv in (F(1),F(2),F(-5,11)):
            r_num={}
            for k,v in res.items():
                val=v*a_val**k[1]*Av**k[2]*Bv**k[3]; r_num[k[0]]=r_num.get(k[0],0)+val
            r_num={k:v for k,v in r_num.items() if v}
            e1=5*Bv+(3-a_val)*Av; e2=-(2+6*a_val)*Bv-2*a_val*Av; e3=3*a_val*Bv-F(1,5)
            zero_res=(not r_num); zero_eqs=(e1==0 and e2==0 and e3==0)
            # residual must vanish iff the three rows vanish at the same point (checked as implication both ways on this grid)
            if zero_res!=zero_eqs: eqs_hold=False
ok(eqs_hold,'[2,1]: residual-vanishing agrees with the three displayed rows on a rational grid')
# independent elimination of the three rows: from row3 B=1/(15a); row1 A=-5B/(3-a); row2 -> (a^2-a-1)=0 . Verify as a polynomial identity: multiply row2 by 15a(3-a) after substitution
# row2*15a(3-a) with B=1/(15a), A=-1/(3a(3-a)):  -(2+6a)(3-a) + 10 = -(6+16a-6a^2)+10 = 6a^2-16a+4 = 2(3a^2-8a+2)?? compute exactly below and compare with 30(a^2-a-1)/??? -> just compute
def eval_row2(a): 
    B=1/(15*a); Aq=-5*B/(3-a); return -(2+6*a)*B-2*a*Aq
import math
vals=[eval_row2(F(x)) for x in (2,5,-1,F(7,3))]
# a^2-a-1 at these: 1,19,1,(49/9-7/3-1)=49/9-30/9=19/9
targets=[F(x)**2-F(x)-1 for x in (2,5,-1,F(7,3))]
ratios=[v/tg for v,tg in zip(vals,targets)]
# ratio must be a fixed rational function; report it
# verify with a symbolic check: row2 * 15 a (3-a) * (-1) ?= 2(a^2-a-1)*k ... compute both for many a and check proportionality with rational function -2/(a(3-a))?
prop_ok=all(v==F(2)*(a**2-a-1)/(5*a*(3-a)) for v,a in zip(vals,[F(2),F(5),F(-1),F(7,3)]))
ok(prop_ok,'[2,1]: elimination of the three rows gives row2 = 2(a^2-a-1)/(5a(3-a)); a^2-a-1=0 necessary and sufficient off a in {0,3}')
# 4. [1,1,1]: e = lambda z s forced; (E) reduces to 5 lambda (A z^2 + 2 B z + 3 C) = 1  => A=B=0, 15 lambda C = 1
Zs=P4({(1,0,0,0):1}); As=P4({(0,1,0,0):1}); Bs=P4({(0,0,1,0):1}); Cs=P4({(0,0,0,1):1})
s=add(add(add(pw(Zs,3),mul(As,pw(Zs,2))),mul(Bs,Zs)),Cs)
h111=mul(pw(Zs,2),s); e111=mul(Zs,s)   # lambda factored out
lhs111=sub(sc(mul(e111,dif(h111,0)),4),sc(mul(dif(e111,0),h111),5))
ok(lhs111==mul(h111,add(add(mul(As,pw(Zs,2)),sc(mul(Bs,Zs),2)),sc(Cs,3))),'[1,1,1]: 4eh\'-5e\'h = h (A z^2+2B z+3C) exact with e=z s')
# cube-root face bivariate
Scube=sub(pw(PI,3),pw(G,3)); Hc=H_of(Scube); Ec=ez([0,F(1,15),0,0,F(-1,15)])
ok(br(Ec,pw(Hc,5))==mul(pw(G,2),pw(Hc,5)),'[1,1,1] S=pi^3-gamma^3: [E,H^5]=gamma^2 H^5 bivariate')
ok(br(sc(Ec,F(5,3)),pw(Hc,3))==mul(pw(G,2),pw(Hc,3)),'[1,1,1] cube face: Q component with (5/3)E')
# 5. pi | E : if E has a pi^0 term c*gamma^4 then [E,H^5] has a nonzero pi^9 term (H^5 has pi-order 10)
E_bad=add(E3,P({(4,0):1}))
lhs_bad=br(E_bad,pw(H3,5)); rhs=mul(pw(G,2),pw(H3,5))
minpi=min(k[1] for k in sub(lhs_bad,rhs)); ok(minpi==9,'pi^0 term of E creates a pi^9 defect (order 10 right side)')
# 6. Monomial endpoint Euler elements in bivariate form
for (Aexp,Bexp) in ((15,10),(0,25),(9,6),(0,15)):
    R=mul(pw(G,Aexp),pw(PI,Bexp)); Em=sc(mul(pw(G,3),PI),F(1,3*Bexp-Aexp))
    ok(br(Em,R)==mul(pw(G,2),R),'monomial endpoint (%d,%d) Euler element'%(Aexp,Bexp))
# 7. Face-exhaustion arithmetic: for support {(i,j): j<=N, i<=... } bounded by total degree N (P) and gamma-degree 15, nonzero-slope endpoint (15,10):
# any primitive positive (r,s) != (1,1) picks a monomial face given the three constraints (proved by finite enumeration over the full lattice box)
def faces(N,gmax,endpoint):
    # candidate support: all (i,j) with i+j<=N, i<=gmax, plus forced presence of (0,N) and endpoint; check which (r,s) faces contain >=2 lattice points of the BOX
    pts=[(i,j) for i in range(gmax+1) for j in range(N+1) if i+j<=N]
    multi=[]
    for r in range(1,13):
        for s in range(1,13):
            if math.gcd(r,s)!=1: continue
            w=max(r*i+s*j for i,j in pts); top=[(i,j) for i,j in pts if r*i+s*j==w]
            if len(top)>1: multi.append((r,s,top))
    return multi
m25=faces(25,15,(15,10)); m15=faces(15,9,(9,6))
ok([(r,s) for r,s,_ in m25]==[(1,1)] and [(r,s) for r,s,_ in m15]==[(1,1)],'face exhaustion: only (1,1) is a nonmonomial positive direction on both boxes (directions up to 12)')
ok(m25[0][2]==[(i,25-i) for i in range(0,16)] and m15[0][2]==[(i,15-i) for i in range(0,10)],'the (1,1) face box spans pi^25..gamma^15 pi^10 and pi^15..gamma^9 pi^6')
# 8. outer-disc mean centering arithmetic: ultrametric mean argument replay on a toy Laurent root packet (orders): if all pairwise contacts >= -1, ord(rho_i - mean) >= -1
# toy: roots rho_i = s_i*gamma + c_i + d_i*gamma^-1 ; mean subtract; check min order of differences is >= -1 in t=1/gamma
import fractions
roots=[(F(1),F(2),F(3)),(F(1),F(-1),F(0)),(F(0),F(4),F(1)),(F(2),F(0),F(0)),(F(0),F(0),F(5))]
mean=tuple(sum(r[i] for r in roots)/len(roots) for i in range(3))
def ordt(v):  # coefficients for gamma^1,gamma^0,gamma^-1 -> t-orders -1,0,1
    for o,c in zip((-1,0,1),v):
        if c: return o
    return 99
ok(all(ordt(tuple(r[i]-mean[i] for i in range(3)))>=-1 for r in roots),'toy ultrametric: mean of a radius -1 packet stays in the packet')
# zero-slope subpacket mean: roots with s_i=0 have order>=0 relative -> the constant b0 = mean of their gamma^0 coefficient
zero=[r for r in roots if r[0]==0]; b0=sum(r[1] for r in zero)/len(zero)
ok(all(ordt((F(0),r[1]-b0,r[2]-mean[2]))>=0 for r in zero),'toy: zero-slope packet mean is order >= 0 after subtracting b0 (only necessary, contact 7/5 needs Prop 5.3)')
out={'status':'PASS','count':len(passed),'checks':passed,'optimized':not __debug__,'elapsed':round(time.monotonic()-t0,4),'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
print(json.dumps(out,indent=0))
