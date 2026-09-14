import sys, json
sys.path.insert(0,'box/cq-elim-20260906')
from band import *
from fractions import Fraction as Fr

# ---------------------------------------------------------------- helpers
def bandrow(Ac, Bc, nu):
    """row_nu = sum_{a+b=nu} J(Q_{55-a}, G_{66-b}), dehomogenised.
       Ac[a] = Q_{55-a}, Bc[b] = G_{66-b} (lists of Fractions, may be [])."""
    R=[]
    for a in range(0,nu+1):
        b=nu-a
        A=Ac.get(a,[]); B=Bc.get(b,[])
        if A and B: R=padd(R, Jd(A,55-a,B,66-b))
    return trim(R)

print("="*72)
print("CONTROL 1 (cone-vertex / Delta family):  G = P^6, Q = lam*P^5, deg P = 11")
print("="*72)
import random; random.seed(3)
# P = p + lower homogeneous parts P_{11-j}; dehomogenised parts are polys of deg <= 11-j
Pparts={0:p}
for j in range(1,12):
    Pparts[j]=[Fr(random.randint(-3,3)) for _ in range(12-j)]
def compose_power(Pparts, e, topdeg):
    """homogeneous parts of P^e : returns dict k -> (P^e)_{e*11-k}"""
    out={0:ppow(Pparts[0],e)}
    # brute force: multiply e copies, tracking band index
    cur={0:[Fr(1)]}
    for _ in range(e):
        nxt={}
        for k1,v1 in cur.items():
            for k2,v2 in Pparts.items():
                k=k1+k2
                if k>topdeg: continue
                t=pmul(v1,v2)
                nxt[k]=padd(nxt.get(k,[]),t)
        cur={k:trim(v) for k,v in nxt.items()}
    return cur
DEPTH=21
G6=compose_power(Pparts,6,DEPTH); Q5=compose_power(Pparts,5,DEPTH)
lam=Fr(7)
Ac={a:pscal(lam,v) for a,v in Q5.items()}; Bc=dict(G6)
bad=[nu for nu in range(1,20) if bandrow(Ac,Bc,nu)]
r20=bandrow(Ac,Bc,20)
print(" bands nu=1..19 nonzero at:", bad if bad else "NONE  -> cone satisfies every degree-drop row")
print(" band nu=20 (attainment row, target -2*P0^9):", "0" if not r20 else "nonzero")
print(" => cone is EXCLUDED iff the nu=20 target is nonzero:  -2*P0^9 != 0 ->",
      "EXCLUDED" if not r20 else "NOT excluded")

print()
print("="*72)
print("CONTROL 2 (existence): solve bands 1..20 exactly with Q = lam*P0^5 homogeneous,")
print("  G = P0^6 + R,  R homogeneous of degree 46.  Need J(P0^5,R) = c*P0^9, 5*lam*c = -2.")
print("="*72)
# unknown R of homogeneous degree 46 -> dehomogenised poly of degree <= 46 (47 coeffs)
# row: J(P5,R) - c*P9 = 0   (homog degree 55+46-2 = 99)
import itertools
N=47
target = P9
rows=[]; 
cols=[]
for k in range(N):
    e=[Fr(0)]*N; e[k]=Fr(1)
    cols.append(Jd(P5,55,e,46))
maxlen=max([len(v) for v in cols]+[len(target)])
# solve  sum_k r_k * cols[k]  =  c * target,  set c = 1 (rescale later)
import fractions
A=[[ (cols[k][i] if i<len(cols[k]) else Fr(0)) for k in range(N)] for i in range(maxlen)]
bvec=[ (target[i] if i<len(target) else Fr(0)) for i in range(maxlen)]
# gaussian elimination, exact
m=len(A); n=N
M=[row[:]+[bvec[i]] for i,row in enumerate(A)]
piv=[]; r=0
for cidx in range(n):
    pr=None
    for i in range(r,m):
        if M[i][cidx]!=0: pr=i; break
    if pr is None: continue
    M[r],M[pr]=M[pr],M[r]
    pv=M[r][cidx]
    M[r]=[v/pv for v in M[r]]
    for i in range(m):
        if i!=r and M[i][cidx]!=0:
            f=M[i][cidx]; M[i]=[M[i][j]-f*M[r][j] for j in range(n+1)]
    piv.append(cidx); r+=1
    if r==m: break
incons=[i for i in range(r,m) if all(M[i][j]==0 for j in range(n)) and M[i][n]!=0]
print(" linear system: %d rows x %d unknowns, rank %d, inconsistent rows: %d"%(m,n,r,len(incons)))
if not incons:
    sol=[Fr(0)]*n
    for i,cidx in enumerate(piv): sol[cidx]=M[i][n]
    R=trim(sol[:])
    chk=padd(Jd(P5,55,R,46), pscal(-1,target))
    print(" solution found, deg R =",len(R)-1,"  residual J(P0^5,R) - P0^9 =", "0" if not chk else "NONZERO")
    # now the full band check with lam chosen so that band 20 = -2*P0^9
    lam=Fr(-2)    # J(Q,G) top = lam * J(P5,R) = lam*P9 ; want = -2*P9
    Ac2={0:pscal(lam,P5)}; Bc2={0:P6, 20:R}
    bad2=[nu for nu in range(1,20) if bandrow(Ac2,Bc2,nu)]
    r20b=bandrow(Ac2,Bc2,20)
    want=pscal(-2,P9)
    print(" bands 1..19 nonzero at:", bad2 if bad2 else "NONE")
    print(" band 20 == -2*P0^9 ?", "YES" if not padd(r20b,pscal(-1,want)) else "NO")
    print(" lam =",lam," (nonzero -> attainment localizer Z*lam-1 is satisfiable)")
    json.dump({"R_deg":len(R)-1,"lam":str(lam),"bands_1_19_all_zero":not bad2,
               "band20_matches_target":not padd(r20b,pscal(-1,want))},
              open('box/cq-elim-20260906/control2.json','w'))
