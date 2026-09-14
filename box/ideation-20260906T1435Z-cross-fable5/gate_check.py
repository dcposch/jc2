"""Fable cross gate: independent replay + mutations of Astra Card 1 (D125 terminal-face constant pivots).
stdlib only; exact Fraction; no classifier import; no solver."""
from fractions import Fraction as Fr
from collections import defaultdict
import resource, sys, json
resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
OUT = {}
def check(cond, msg):
    if not cond: raise RuntimeError('FAIL: '+msg)
def ceil_div(a,b): return -((-a)//b)

# ---- 1. independent derivation of terminal faces from the ORIGINAL source supports ----
def source(D,U):
    return [(i,j) for i in range(D+1) for j in range(D+1-i) if 5*i-j<=U]
def norm_source(D,U,imax,jmax):
    S=[(i,j) for (i,j) in source(D,U) if j<=jmax]
    # pure vertical top: [u^i v^jmax]=0 for i<imax
    return [(i,j) for (i,j) in S if not (j==jmax and i<imax)]
def xy_monomials(S):
    # Phi(u^i v^j)=X^{5i}(Y+X^-1)^j -> (a,b)=(5i-j+b, b), 0<=b<=j
    M=set()
    for i,j in S:
        for b in range(j+1): M.add((5*i-j+b,b))
    return M
def face(S,h):
    return sorted(m for m in xy_monomials(S) if 5*m[0]-17*m[1]==h)
SP=source(75,15); SQ=source(125,25)
check(len(SP)==706 and len(SQ)==1901,'source counts')
# NOTE: the terminal halfspaces are IMPOSED by the jets (make_band: e>=ceil((17ell-h)/12)), not implied by the supports;
# raw XY monomials of the supports reach weight %d/%d above the faces.
OUT['raw_max_weights']=(max(5*a-17*b for a,b in xy_monomials(SP)),max(5*a-17*b for a,b in xy_monomials(SQ)))
check(face(SP,3)==[(4,1),(21,6)],'P* support from source')
check(face(SQ,5)==[(1,0),(18,5),(35,10)],'Q* support from source')
OUT['faces']={'P*':face(SP,3),'Q*':face(SQ,5)}
# pins -> t^e z^L = X^e Y^{e-L}
pins={('P',3,4):Fr(1),('P',15,21):Fr(1),('Q',1,1):Fr(-1),('Q',13,18):Fr(-3),('Q',25,35):Fr(-9,5)}
Pst={};Qst={}
for (side,L,e),val in pins.items():
    (Pst if side=='P' else Qst)[(e,e-L)]=val
check(sorted(Pst)==[(4,1),(21,6)] and sorted(Qst)==[(1,0),(18,5),(35,10)],'pins sit exactly on the faces')
def bracket(p,q):
    out=defaultdict(Fr)
    for (a,b),c in p.items():
        for (i,j),d in q.items():
            out[(a+i-1,b+j-1)]+=c*d*(a*j-b*i)
    return {k:v for k,v in out.items() if v}
check(bracket(Pst,Qst)=={(4,0):Fr(1)},'[P*,Q*]=X^4')
# ---- 2. graded columns: leading monomials of adapted Q basis (my own derivation, band by band) ----
def bands(S):
    B=defaultdict(list)
    for i,j in S: B[5*i-j].append(j)
    return B
def rank_mat(M,width):
    a=[r[:] for r in M]; r=0
    for c in range(width):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]; pv=a[r][c]; a[r]=[x/pv for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                f=a[i][c]; a[i]=[x-f*y for x,y in zip(a[i],a[r])]
        r+=1
    return r
from math import comb
def leading_orders(js, r):
    """orders of an adapted basis of span{(1+t)^j : j in js} with first r Taylor coeffs zero.
    Computed honestly by echelon form of the Taylor matrix (orders 0..max j)."""
    n=len(js); 
    if n==0: return []
    maxo=max(js)
    T=[[Fr(comb(j,o)) for o in range(maxo+1)] for j in js]   # rows = basis elements, cols = orders
    # jets: subspace with orders<r zero: compute nullspace-restricted basis via elimination on first r columns
    # do row reduction to find combos killing first r orders
    A=[row[:] for row in T]
    # reduce on columns 0..r-1
    piv=0; pivcols=[]
    for c in range(r):
        p=next((i for i in range(piv,n) if A[i][c]),None)
        if p is None: continue
        A[piv],A[p]=A[p],A[piv]; pv=A[piv][c]; A[piv]=[x/pv for x in A[piv]]
        for i in range(n):
            if i!=piv and A[i][c]: f=A[i][c]; A[i]=[x-f*y for x,y in zip(A[i],A[piv])]
        piv+=1; pivcols.append(c)
    sub=A[piv:]   # rows with orders<r all zero
    # leading orders of the subspace: echelon on remaining columns
    lead=[]
    B=[row[:] for row in sub]; rr=0
    for c in range(r,maxo+1):
        p=next((i for i in range(rr,len(B)) if B[i][c]),None)
        if p is None: continue
        B[rr],B[p]=B[p],B[rr]; pv=B[rr][c]; B[rr]=[x/pv for x in B[rr]]
        for i in range(len(B)):
            if i!=rr and B[i][c]: f=B[i][c]; B[i]=[x-f*y for x,y in zip(B[i],B[rr])]
        rr+=1; lead.append(c)
    return lead
def columns(S, h, removed_first, D):
    """graded columns (a,b) for Q-space S; removed_first: bands whose first column is removed (pins/gauges)"""
    cols=[]; jetcount=0
    for ell,js in sorted(bands(S).items()):
        r=max(0,ceil_div(5*ell-h,12))
        lead=leading_orders(sorted(js), r)
        jetcount+=min(r,len(js))
        if ell in removed_first:
            check(lead and lead[0]==r,'gauge/pin column must be the first post-jet order on band %d'%ell)
            lead=lead[1:]
        for b in lead: cols.append((ell+b,b))
    return cols, jetcount
def graded_rank(cols):
    groups=defaultdict(list)
    for a,b in cols: groups[5*a-17*b].append((a,b))
    tot=0; defects=[]; maxr=maxc=0
    for w,cs in groups.items():
        rows=set(); ents=[]
        for a,b in cs:
            d={}
            for pos,c in [((a+3,b),4*b-a),((a+20,b+5),21*b-6*a)]:
                if c: d[pos]=Fr(c); rows.add(pos)
            ents.append(d)
        rows=sorted(rows)
        M=[[e.get(rw,Fr(0)) for e in ents] for rw in rows]
        rk=rank_mat(M,len(cs)); tot+=rk
        maxr=max(maxr,len(rows)); maxc=max(maxc,len(cs))
        if rk!=len(cs): defects.append((w,len(cs)-rk))
    return len(cols),tot,maxr,maxc,sorted(defects),len(groups)
# independent check that the graded column image equals the literal bracket with P*
for a,b in [(1,0),(18,5),(35,10),(0,0),(21,6),(-30,7),(7,20)]:
    exp={}
    for pos,c in [((a+3,b),4*b-a),((a+20,b+5),21*b-6*a)]:
        if c: exp[pos]=Fr(c)
    check(bracket(Pst,{(a,b):Fr(1)})==exp,'graded column formula vs literal bracket')
# full original chart
colsQ,jQ=columns(SQ,5,{1,13,25,15,0},125)
check(jQ==136,'Q jet count 136')
full=graded_rank(colsQ)
OUT['full_chart']=full
check(full[0]==1760 and full[1]==1760 and not full[4],'full chart: 1760 columns, graded rank 1760')
check(full[2]<=6 and full[3]<=5,'block size')
# restoring gauges -> kernel at weights 0 and 3 exactly
c1,_=columns(SQ,5,{1,13,25,15},125); r1=graded_rank(c1); check(r1[4]==[(0,1)],'restore constant -> weight 0 kernel')
c2,_=columns(SQ,5,{1,13,25,0},125);  r2=graded_rank(c2); check(r2[4]==[(3,1)],'restore P -> weight 3 kernel')
c3,_=columns(SQ,5,{1,13,25},125);    r3=graded_rank(c3); check(r3[4]==[(0,1),(3,1)],'no gauges -> both')
# ---- 3. MUTATIONS (changed objects) ----
# (m1) wrong terminal face: drop the second P* monomial -> centraliser of a monomial is huge; graded rank must collapse
def graded_rank_face(cols,Pface):
    groups=defaultdict(list)
    for a,b in cols: groups[5*a-17*b].append((a,b))
    tot=0
    for w,cs in groups.items():
        rows=set(); ents=[]
        for a,b in cs:
            d=bracket(Pface,{(a,b):Fr(1)}); ents.append(d); rows|=set(d)
        rows=sorted(rows); M=[[e.get(rw,Fr(0)) for e in ents] for rw in rows]
        tot+=rank_mat(M,len(cs))
    return tot
m1=graded_rank_face(colsQ,{(4,1):Fr(1)})
OUT['mut_monomial_face_rank']=m1
check(m1<1760,'mutation: monomial face loses rank')
# (m2) wrong pin ratio on P*: (4,1)->1,(21,6)->2 : kernel argument needs (1+T)g'=bg; with 1+2T the kernel is (1+2T)^b => still injective off gauges? test
m2=graded_rank_face(colsQ,{(4,1):Fr(1),(21,6):Fr(2)})
OUT['mut_pin_ratio_rank']=m2
# (m3) illegal extra column (8,2) on band 6 (a jet slot) restored -> must create a kernel at weight 6
m3a=graded_rank(colsQ+[(8,2)])
OUT['mut_restore_(8,2)_alone_defects']=m3a[4]      # expected: none (P*^2 needs (25,7),(42,12) too)
m3=graded_rank(colsQ+[(8,2),(25,7),(42,12)])
OUT['mut_restore_P*^2_support_defects']=m3[4]
check(m3[4]==[(6,1)],'mutation: restoring the full P*^2 support (8,2),(25,7),(42,12) creates exactly one kernel at weight 6')
# (m4) sign mutation of a Q* pin must break [P*,Q*]=X^4 (top bracket)
Qm=dict(Qst); Qm[(18,5)]=Fr(3); check(bracket(Pst,Qm)!={(4,0):Fr(1)},'sign mutation rejected')
# ---- 4. NORMALIZED SUBCHART (rectangles 15x60 / 25x100, pure vertical tops) ----
SPn=norm_source(75,15,15,60); SQn=norm_source(125,25,25,100)
OUT['norm_counts']=(len(SPn),len(SQn))
check(len(SPn)==571 and len(SQn)==1551,'normalized raw counts 571/1551')
check(face(SPn,3)==[(4,1),(21,6)] and face(SQn,5)==[(1,0),(18,5),(35,10)],'faces unchanged in subchart')
# gauge transformation Q -> Q - aP - c stays in the subchart: supp P subset supp Q, no v^100 / u^25 v^100 hit
check(set(SPn)<=set(SQn) and all(j<100 for i,j in SPn) and (0,0) in SQn,'gauge shift preserves normalized Q chart')
colsQn,jQn=columns(SQn,5,{1,13,25,15,0},125)
check(set(colsQn)<=set(colsQ),'normalized columns are a subset of full columns (prefix property)')
normr=graded_rank(colsQn)
OUT['normalized_chart']=normr; OUT['norm_Q_jets']=jQn
check(normr[0]==normr[1] and not normr[4],'normalized subchart: graded map injective with the SAME two gauges')
cn1,_=columns(SQn,5,{1,13,25},125); check(graded_rank(cn1)[4]==[(0,1),(3,1)],'normalized: without gauges exactly the two kernels')
# P base dimension in both charts
def pdim(S):
    d=0
    for ell,js in bands(S).items():
        r=max(0,ceil_div(5*ell-3,12)); d+=max(0,len(js)-r)
    return d
OUT['P_base_dims']={'full':pdim(SP)-2,'normalized':pdim(SPn)-2}
print(json.dumps(OUT,default=str)); print('FABLE_CROSS_GATE_PASS')
