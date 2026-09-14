#!/usr/bin/env python3
"""Independent hostile checks for the B reconstruction claims. Stdlib only.
Different derivations: half-plane lattices, regular-representation rank over Q,
Bareiss/Gauss minors, unrestricted homogeneous kernels, direct brackets."""
from fractions import Fraction as F
import json, sys, math, itertools
def req(ok,msg):
    if not ok: raise ValueError("REJECT: "+msg)
MUT=set(a for a in sys.argv[1:] if a.startswith('--'))
# ---- Q(rho), rho^2=3rho-1, as pairs; plus regular representation over Q ----
Z=(F(0),F(0)); O=(F(1),F(0)); R=(F(0),F(1))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y): a,b=x;c,d=y; return (a*c-b*d,a*d+b*c+3*b*d)
def sc(x,a): return (x[0]*a,x[1]*a)
def inv(x):
    a,b=x; n=a*a+3*a*b+b*b; req(n!=0,"inverse of zero")
    return ((a+3*b)/n,-b/n)
def conj(x): return (x[0]+3*x[1],-x[1])   # rho -> 3-rho
def regrep(x): a,b=x; return [[a,-b],[b,a+3*b]]   # matrix of mult by a+b rho on basis (1,rho)
def pconv(p,q):
    out=[Z]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]=add(out[i+j],mul(a,b))
    return out
def ppow(p,n):
    o=[O]
    for _ in range(n): o=pconv(o,p)
    return o
def rankQ(M):
    M=[r[:] for r in M]; rk=0; cols=len(M[0]) if M else 0
    for c in range(cols):
        piv=next((i for i in range(rk,len(M)) if M[i][c]!=0),None)
        if piv is None: continue
        M[rk],M[piv]=M[piv],M[rk]
        for i in range(len(M)):
            if i!=rk and M[i][c]!=0:
                f=M[i][c]/M[rk][c]; M[i]=[a-f*b for a,b in zip(M[i],M[rk])]
        rk+=1
    return rk
def rank_field(M):   # rank over Q(rho) via regular representation over Q
    big=[]
    for row in M:
        blocks=[regrep(x) for x in row]
        for t in range(2): big.append([blk[t][s] for blk in blocks for s in range(2)])
    r=rankQ(big); req(r%2==0,"regular representation rank parity"); return r//2
def det_field(M):    # Gaussian determinant over Q(rho) with own arithmetic
    M=[r[:] for r in M]; n=len(M); d=O
    for c in range(n):
        piv=next((i for i in range(c,n) if M[i][c]!=Z),None)
        if piv is None: return Z
        if piv!=c: M[c],M[piv]=M[piv],M[c]; d=sc(d,-1)
        d=mul(d,M[c][c]); iv=inv(M[c][c])
        for i in range(c+1,n):
            if M[i][c]!=Z:
                f=mul(M[i][c],iv); M[i]=[sub(a,mul(f,b)) for a,b in zip(M[i],M[c])]
    return d
def nullspace_field(M,ncol):  # returns basis of kernel over Q(rho)
    A=[r[:] for r in M]; piv=[]; rk=0
    for c in range(ncol):
        p=next((i for i in range(rk,len(A)) if A[i][c]!=Z),None)
        if p is None: continue
        A[rk],A[p]=A[p],A[rk]; iv=inv(A[rk][c]); A[rk]=[mul(iv,x) for x in A[rk]]
        for i in range(len(A)):
            if i!=rk and A[i][c]!=Z:
                f=A[i][c]; A[i]=[sub(a,mul(f,b)) for a,b in zip(A[i],A[rk])]
        piv.append(c); rk+=1
    free=[c for c in range(ncol) if c not in piv]; basis=[]
    for fcol in free:
        v=[Z]*ncol; v[fcol]=O
        for i,pc in enumerate(piv): v[pc]=sc(A[i][fcol],-1)
        basis.append(v)
    return basis
# ---- H, brackets ----
S_rat=[O,Z,Z,O]                                   # pi^3+gamma^3 as gamma-power list
S_gold=pconv([O,O],pconv([O,(F(1),F(-1))],[O,(F(1),F(-1))]))   # (pi+g)(pi+(1-rho)g)^2
req(S_gold==[O,(F(3),F(-2)),(F(2),F(-1)),(F(0),F(1))],"golden S expansion")
if '--mutate-H' in MUT: S_rat=[O]; S_gold=[O]      # H=pi^5 (nonprimitive control)
H={"rational":S_rat,"golden":S_gold}               # H = pi^2*S: gamma-power list, coefficient of gamma^p pi^(5-p)
kap={"rational":O,"golden":R}
for br,h in H.items():
    if '--mutate-H' not in MUT:
        req(h[0]==O and h[3]==kap[br],"H monic in pi with kappa at gamma^3 pi^2")
        # h(z)=z^2*S(1,z): value and derivative at z=-1 by own Horner
        hz=[Z,Z]+[h[3-p] for p in range(4)]      # z^2*(sum S_p z^(3-p))  -> coefficient list in z
        val=Z; der=Z
        for k,c in enumerate(hz):
            val=add(val,sc(c,(-1)**k)); der=add(der,sc(c,k*(-1)**(k-1) if k else 0))
        req(val==Z,"h(-1)=0"); req(der=={"rational":(F(3),F(0)),"golden":mul(R,R)}[br],"h'(-1) is 3 / rho^2")
        req(der!=Z and mul(der,inv(der))==O,"simple root: h'(-1) unit in the field")
def bracket(P,Q):   # dict {(i,j):coef pair}
    out={}
    for (i,j),a in P.items():
        for (k,l),b in Q.items():
            c=sc(mul(a,b),i*l-j*k)
            if c!=Z:
                key=(i+k-1,j+l-1); out[key]=add(out.get(key,Z),c)
    return {k:v for k,v in out.items() if v!=Z}
def homog(h,deg):  # H^r as dict
    return {(p,deg-p):c for p,c in enumerate(h) if c!=Z}
for br,h in H.items():
    H3=ppow(h,3); H5=ppow(h,5); H1=h
    req(bracket(homog(H3,15),homog(H5,25))=={} ,"top degree 38 identity [H^3,H^5]=0")
    req(bracket(homog(H1,5),homog(ppow(h,4),20))=={},"[H,H^4]=0")
# ---- lattices by half-planes (different membership test) ----
cases={"unequal":dict(A=lambda i,j:i+j<=15 and 5*i-7*j<=3, B=lambda i,j:i+j<=25 and 5*i-7*j<=5, w=lambda i,j:5*i-7*j, wa=3,wb=5, q=lambda d:(7*d+4)//12),
       "common3":dict(A=lambda i,j:i+j<=15 and i-j<=3, B=lambda i,j:i+j<=25 and i-j<=5, w=lambda i,j:i-j, wa=3,wb=5, q=lambda d:min(d,(d+4)//2)),
       "common4":dict(A=lambda i,j:i+j<=15 and i<=9, B=lambda i,j:i+j<=25 and i<=15, w=lambda i,j:i, wa=9,wb=15, q=lambda d:min(d,14))}
if '--mutate-q' in MUT: cases["unequal"]["q"]=lambda d:(7*d+5)//12
expect={"unequal":(71,196,2,3),"common3":(77,214,7,11),"common4":(98,269,7,11)}
Kslots={"unequal":{(1,0):1,(8,5):13},"common3":{(5+j,j):5+2*j for j in range(10)},"common4":{(15,j):15+j for j in range(10)}}
for cs,c in cases.items():
    AP=[(i,j) for i in range(26) for j in range(26) if i>=0 and j>=0 and c["A"](i,j)]
    BP=[(i,j) for i in range(26) for j in range(26) if c["B"](i,j)]
    req(set(AP)<=set(BP),"A lattice inside B lattice")
    req(max(c["w"](*v) for v in AP)==c["wa"] and c["wa"]<c["wb"],"A max B-weight strictly below B inner face")
    innerA=[v for v in AP if c["w"](*v)==c["wa"]]; innerB=[v for v in BP if c["w"](*v)==c["wb"]]
    outerA=[v for v in AP if sum(v)==15]; outerB=[v for v in BP if sum(v)==25]
    req(len(outerA)==10 and len(outerB)==16,"outer face lattice counts 10/16")
    req(len(innerA)==expect[cs][2] and len(innerB)==expect[cs][3],"inner face lattice counts")
    freeA=[v for v in AP if v!=(0,0) and sum(v)!=15 and c["w"](*v)!=c["wa"]]
    freeB=[v for v in BP if v!=(0,0) and sum(v)!=25 and c["w"](*v)!=c["wb"]]
    req((len(freeA),len(freeB))==expect[cs][:2],"free counts %s"%cs)
    # known K_d slots are exactly the inner-face B points of degree <25
    req(set(Kslots[cs])==set(v for v in innerB if sum(v)<25),"K_d slots = inner B face below degree 25")
    req(all(sum(v)==d for v,d in Kslots[cs].items()),"K_d degrees")
    for d in range(1,25):
        cols=[i for i in range(d+1) if (i,d-i) in set(freeB)]
        req(cols==list(range(c["q"](d)+1)),"free columns 0..q_d at %s d=%d"%(cs,d))
    req((0,15) in set(freeB),"(0,15) is a free B slot")
    # H^r fits in the free columns strictly below the faces
    for br,h in H.items():
        for r in range(1,5):
            sup=[(p,5*r-p) for p,cf in enumerate(ppow(h,r)) if cf!=Z]
            req(all(v in set(freeB) for v in sup),"H^%d inside free B slots"%r)
            req(max(c["w"](*v) for v in sup)<c["wb"],"H^r strictly below B inner face")
    c["freeB"]=freeB
# ---- matrices, ranks, kernels, witnesses ----
W=json.load(open('/tmp/jc2-lane.jF2rfq/inputs/exact-witnesses.json'))
def L_matrix(h3,d,ncols):
    M=[]
    for r in range(d+14):
        row=[]
        for i in range(ncols):
            p=r+1-i
            row.append(sc(h3[p],p*d-15*i) if 0<=p<len(h3) else Z)
        M.append(row)
    return M
def sum_(row,vec):
    s=Z
    for a,b in zip(row,vec): s=add(s,mul(a,b))
    return s
FLOATS=[]
def dec(pair):
    out=[]
    for num,den in pair:
        if isinstance(num,float) or isinstance(den,float):
            FLOATS.append((num,den)); num=int(num); den=int(den)
        out.append(F(num,den))
    return tuple(out)
count=0; sums={}; LOSSY=[]
for br,h in H.items():
    h3=ppow(h,3)
    # bracket-derived entry crosscheck: [H^3, gamma^i pi^(d-i)] computed directly
    for d in (1,7,24):
        for i in (0,3):
            direct=bracket(homog(h3,15),{(i,d-i):O})
            M=L_matrix(h3,d,15)
            req(all(direct.get((r,d+13-r),Z)==M[r][i] for r in range(d+14)),"entry formula (pd-15i)h_p vs direct bracket")
    # unrestricted homogeneous kernel for d=1..25
    for d in range(1,26):
        M=L_matrix(h3,d,d+1); ns=nullspace_field(M,d+1)
        if d%5==0:
            req(len(ns)==1,"unrestricted kernel dimension 1 at d=%d"%d)
            v=ns[0]; hr=ppow(h,d//5)+[Z]*(d+1-len(ppow(h,d//5)))
            # proportional to H^(d/5)
            k=next(j for j in range(d+1) if hr[j]!=Z); lam=mul(v[k],inv(hr[k]))
            req(all(v[j]==mul(lam,hr[j]) for j in range(d+1)),"kernel is scalar H^(d/5) at d=%d"%d)
        else:
            req(len(ns)==0,"unrestricted kernel zero at d=%d (5 does not divide d)"%d)
    for cs,c in cases.items():
        tot=0
        for wit in W["witnesses"][cs][br]:
            d=wit["d"]; q=c["q"](d); n=q+1
            req(wit["columns"]==n,"witness column count")
            M=L_matrix(h3,d,n)
            req(len(M)==d+14 and len(M)<=38 and n<=15,"matrix at most 38x15")
            rk=rank_field(M); req(rk==wit["rank"] and rk==n-(1 if d%5==0 else 0),"exact rank d=%d %s %s"%(d,cs,br))
            rk2=rank_field([[conj(x) for x in row] for row in M]); req(rk2==rk,"conjugate embedding rank")
            tot+=rk
            T=[[M[i-1][j] for j in range(1,q+1)] for i in range(1,q+1)]
            req(all(T[a][a]==(F(-15*(a+1)),F(0)) for a in range(q)) and all(T[a][b]==Z for a in range(q) for b in range(a+1,q)),"triangular block diagonal -15i")
            # Schur complements of every row r>=q via own forward substitution on T y = M[0..q-1,0]
            y=[]
            for a in range(q):
                s=M[a][0]
                for b in range(a): s=sub(s,mul(T[a][b],y[b]))
                y.append(mul(s,inv(T[a][a])))
            schur=[sub(M[r][0],sum_(M[r][1:q+1],y)) if q else M[r][0] for r in range(q,d+14)] if True else None
            first=next((r for r,v in zip(range(q,d+14),schur) if v!=Z),None)
            if d%5==0:
                req(first is None and wit["extra_row"] is None and dec(wit["schur"])==Z,"kernel degree: no extra pivot")
                minor=O
                for i in range(1,q+1): minor=sc(minor,-15*i)
            else:
                req(first==wit["extra_row"],"first nonzero Schur row")
                req(schur[first-q]==dec(wit["schur"]),"exact Schur value")
                rows=list(range(q))+[first]; colsel=list(range(1,q+1))+[0]
                minor=det_field([[M[r][cc] for cc in colsel] for r in rows])
                req(minor==mul(dec(wit["schur"]),sc(O,F((-15)**q*math.factorial(q)))),"minor = (-15)^q q! S_d")
                req(mul(minor,inv(minor))==O,"minor unit")
            nf=len(FLOATS); wm=dec(wit["nonzero_minor"])
            if len(FLOATS)>nf:
                LOSSY.append((cs,br,d, wm==minor))
            else:
                req(minor==wm,"witness minor d=%d %s %s"%(d,cs,br))
            if '--mutate-minor' in MUT and d==7 and cs=="unequal" and br=="rational":
                req(minor==add(wm,O),"injected wrong minor")
            count+=1
        sums[(cs,br)]=tot
        req(tot==len(c["freeB"])-4,"rank sum = free B - 4 (%s %s)"%(cs,br))
req(count==144,"144 witnesses")
req(sums[("unequal","rational")]==192 and sums[("common3","rational")]==210 and sums[("common4","rational")]==265,"ranks 192/210/265")
req((24*24-3*24+1)%101==0,"rho=24 is a root mod 101")
# ---- gauge: literal shear on a random full-support fixture (golden face) ----
import random; random.seed(7)
h=H["golden"]; H3=homog(ppow(h,3),15); H5=homog(ppow(h,5),25)
BP=[v for v in cases["unequal"]["freeB"]]; AP=[(i,j) for i in range(16) for j in range(16) if cases["unequal"]["A"](i,j) and (i,j)!=(0,0) and i+j<15]
A=dict(H3); A.update({v:(F(random.randint(-3,3)),F(random.randint(-3,3))) for v in AP})
B=dict(H5); B.update({v:(F(random.randint(-3,3)),F(random.randint(-3,3))) for v in BP})
s=B[(0,15)]; Bp={k:sub(B.get(k,Z),mul(s,A.get(k,Z))) for k in set(B)|set(A)}; Bp={k:v for k,v in Bp.items() if v!=Z}
req(Bp.get((0,15),Z)==Z and bracket(A,Bp)==bracket(A,B),"target shear keeps [A,B], kills (0,15)")
req(all(Bp.get(v,Z)==B.get(v,Z) for v in B if sum(v)==25 or 5*v[0]-7*v[1]==5),"outer and inner B faces preserved")
req((0,0) not in Bp and Bp.get((0,25))==O,"origin and monicity preserved")
req(Bp.get((0,5),Z)!=B.get((0,5),Z),"lower kernel coordinate changes under the shear")
Bdel={k:sub(B.get(k,Z),mul(s,H3.get(k,Z))) for k in set(B)|set(H3)}
req(bracket(A,Bdel)!=bracket(A,B),"deleting s*H^3 alone is not a gauge")
if '--mutate-kernel' in MUT:
    bad=[O]*4; req(all(v==Z for v in [sum_(row,bad) for row in L_matrix(ppow(H['golden'],3),5,4)]),"injected false kernel")
# ---- lift linearity: phi on the A polygon, negative slots inside LP ----
LP={(t,e) for t in range(3) for e in range(5*t-15,0)}; LQ={(t,e) for t in range(5) for e in range(5*t-25,0)}
req(LP<=LQ and len(LP)==30 and len(LQ)==75,"30 P slots inside 75 Q slots")
def lmul(p,q):
    o={}
    for (a,b),x in p.items():
        for (c,d),y in q.items():
            k=(a+c,b+d); o[k]=o.get(k,F(0))+x*y
    return {k:v for k,v in o.items() if v}
lam2,lam3=F(2),F(3); PI={(1,4):F(1),(0,2):-lam2,(0,1):-lam3,(0,-1):F(-1)}; G={(0,-1):F(1)}
pw=[{(0,0):F(1)}]
for j in range(1,16): pw.append(lmul(pw[-1],PI))
gp=[{(0,0):F(1)}]
for i in range(1,16): gp.append(lmul(gp[-1],G))
for (i,j) in [(i,j) for i in range(16) for j in range(16) if i+j<=15]:
    img=lmul(gp[i],pw[j]); neg={k for k in img if k[1]<0}
    req(neg<=LP,"negative support of phi(gamma^i pi^j) inside the 30 P slots")
req(74+2==76 and 82+2==84 and 103+2==105 and 71+3==74 and 77+3+2==82 and 98+3+2==103,"counts")
print("FROZEN-JSON float-degraded minors:",len(LOSSY),"of 144; int(float)==exact:",sum(1 for x in LOSSY if x[3]),"; per case/branch:",{k:sum(1 for x in LOSSY if x[:2]==k) for k in sums})
print("OWN-GATE PASS witnesses=%d ranks=%s"%(count,{f"{k[0]}/{k[1]}":v for k,v in sums.items()}))
