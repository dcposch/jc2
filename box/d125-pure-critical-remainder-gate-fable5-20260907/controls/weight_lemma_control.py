#!/usr/bin/env python3
"""Arrow 2 (Fable control): the filtered weight lemma at the stated bounds, by finite linear algebra.
W = span{g^i p^j : i+j<=13, 5i-7j<=WMAX}.  Kernel of reduction mod V (g^3 -> 3p-p^3) is computed
by Gaussian elimination over Q; every kernel element must be divisible by p^2 V with quotient Q of
degree<=8 and weight<=2.  No Assert nodes; failure raises ValueError (exit 1).
Mutations: --drop-weight (no weight bound), --weight-8 (bound 8): the kernel then contains
elements not divisible by p^2 (gpV, pV), so the lemma's conclusion is refuted at those bounds."""
import sys, json
from fractions import Fraction as Q
mode=sys.argv[1] if len(sys.argv)>1 else ''
DEG=13; WMAX=3
if mode=='--drop-weight': WMAX=10**6
if mode=='--weight-8': WMAX=8
def need(ok,msg):
    if not ok: raise ValueError(msg)
def w(i,j): return 5*i-7*j
mons=[(i,j) for i in range(DEG+1) for j in range(DEG+1) if i+j<=DEG and w(i,j)<=WMAX]
def reduce_mod_V(poly):
    poly=dict(poly)
    while any(a>=3 for a,b in poly):
        out={}
        for (a,b),c in poly.items():
            if a>=3:
                for e,cc in (((a-3,b+1),Q(3)),((a-3,b+3),Q(-1))):
                    out[e]=out.get(e,Q(0))+c*cc
            else: out[(a,b)]=out.get((a,b),Q(0))+c
        poly={e:c for e,c in out.items() if c}
    return poly
reduced=[reduce_mod_V({m:Q(1)}) for m in mons]
cols=sorted({e for r in reduced for e in r})
idx={e:k for k,e in enumerate(cols)}
# matrix M (len(cols) x len(mons)); nullspace of M
M=[[Q(0)]*len(mons) for _ in cols]
for k,r in enumerate(reduced):
    for e,c in r.items(): M[idx[e]][k]=c
# RREF
piv=[]; row=0
for col in range(len(mons)):
    pr=next((r for r in range(row,len(M)) if M[r][col]!=0),None)
    if pr is None: continue
    M[row],M[pr]=M[pr],M[row]
    pv=M[row][col]; M[row]=[x/pv for x in M[row]]
    for r in range(len(M)):
        if r!=row and M[r][col]!=0:
            f=M[r][col]; M[r]=[x-f*y for x,y in zip(M[r],M[row])]
    piv.append(col); row+=1
free=[c for c in range(len(mons)) if c not in piv]
kernel=[]
for fc in free:
    vec=[Q(0)]*len(mons); vec[fc]=Q(1)
    for r,pc in enumerate(piv): vec[pc]=-M[r][fc]
    kernel.append({mons[k]:c for k,c in enumerate(vec) if c})
# divide each kernel element by V (monic cubic in g over Q[p]) : long division in g
def div_by_V(P):
    P=dict(P); U={}
    while P:
        a,b=max(P)  # highest g-degree, then p
        need(a>=3,'not divisible by V: remainder has g-degree<3')
        c=P[(a,b)]; U[(a-3,b)]=U.get((a-3,b),Q(0))+c
        for e,cc in (((a,b),Q(1)),((a-3,b+3),Q(1)),((a-3,b+1),Q(-3))):
            P[e]=P.get(e,Q(0))-c*cc
        P={e:v for e,v in P.items() if v}
    return U
bad=[]; quot_stats=[]
for K in kernel:
    U=div_by_V(K)            # P = V*U, deg U <= 13-3 = 10, w(U) <= WMAX-15
    pmin=min(j for i,j in U); wU=max(w(i,j) for i,j in U); dU=max(i+j for i,j in U)
    if pmin<2: bad.append({'kernel_element_terms':len(K),'U_min_p_exp':pmin,'U_weight':wU,'U_example':sorted(U)[:3]}); continue
    Qq={(i,j-2):c for (i,j),c in U.items()}   # Q = U/p^2 : the actual quotient P/(p^2 V)
    quot_stats.append([pmin,max(w(i,j) for i,j in Qq),max(i+j for i,j in Qq)])
predicted_U=[(i,j) for i in range(11) for j in range(11) if i+j<=10 and w(i,j)<=WMAX-15]
out={'mode':mode or 'positive','WMAX':WMAX,'dim_W':len(mons),'kernel_dim':len(kernel),'predicted_U_monomials':len(predicted_U),
     'all_kernel_divisible_by_p2V':not bad,'quotient_max_weight':max(s[1] for s in quot_stats) if quot_stats else None,
     'quotient_max_degree':max(s[2] for s in quot_stats) if quot_stats else None,'failures':bad[:3]}
print(json.dumps(out,sort_keys=True,default=str))
need(len(kernel)==len(predicted_U),'kernel dimension differs from V*(deg<=10, w<=WMAX-15) count')
need(not bad,'weight lemma refuted at this bound: a kernel element is not divisible by p^2 V')
need(out['quotient_max_weight']<=WMAX-1 and out['quotient_max_degree']<=8,'quotient bounds w(Q)<=WMAX-1, deg(Q)<=8 fail')
