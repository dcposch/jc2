import json,re,random,ast
from fractions import Fraction as Q
from math import comb
random.seed(20260906)
src=json.load(open('/tmp/jc2-lane.rM5Jkj/inputs/delta2_stage8.strongest.json'))
maps=src['maps']; norm=src['normalization']
PR=(1<<61)-1
# ---- linear-form parsing of entries (own parser, ast based) ----
def linform(e):
    t=ast.parse(str(e).replace('^','**'),mode='eval').body
    def ev(n):
        if isinstance(n,ast.Constant): return {None:Q(n.value)}
        if isinstance(n,ast.Name): return {n.id:Q(1)}
        if isinstance(n,ast.UnaryOp): return {k:-v for k,v in ev(n.operand).items()}
        if isinstance(n,ast.BinOp):
            a,b=ev(n.left),ev(n.right)
            if isinstance(n.op,ast.Add): 
                o=dict(a); [o.__setitem__(k,o.get(k,0)+v) for k,v in b.items()]; return o
            if isinstance(n.op,ast.Sub):
                o=dict(a); [o.__setitem__(k,o.get(k,0)-v) for k,v in b.items()]; return o
            if isinstance(n.op,ast.Mult):
                if list(a)==[None]: return {k:a[None]*v for k,v in b.items()}
                if list(b)==[None]: return {k:b[None]*v for k,v in a.items()}
            if isinstance(n.op,ast.Div) and list(b)==[None]: return {k:v/b[None] for k,v in a.items()}
        raise ValueError(ast.dump(n))
    return ev(t)
# ---- polynomial dict arithmetic over Q ----
def add(a,b,s=Q(1)):
    o=dict(a)
    for p,v in b.items(): o[p]=o.get(p,Q(0))+s*v
    return {p:v for p,v in o.items() if v}
def mul(a,b):
    o={}
    for (i,j),u in a.items():
        for (k,l),v in b.items(): o[(i+k,j+l)]=o.get((i+k,j+l),Q(0))+u*v
    return {p:v for p,v in o.items() if v}
def dX(a): return {(i-1,j):v*i for (i,j),v in a.items() if i}
def dW(a): return {(i,j-1):v*j for (i,j),v in a.items() if j}
def jac(a,b): return add(mul(dX(a),dW(b)),mul(dW(a),dX(b)),Q(-1))
def deg(a): return max(i+j for i,j in a) if a else -1
def evnum(e,val):
    def ev(n):
        if isinstance(n,ast.Constant): return Q(n.value)
        if isinstance(n,ast.Name): return val[n.id]
        if isinstance(n,ast.UnaryOp): return -ev(n.operand)
        if isinstance(n,ast.BinOp):
            a,b=ev(n.left),ev(n.right)
            if isinstance(n.op,ast.Add): return a+b
            if isinstance(n.op,ast.Sub): return a-b
            if isinstance(n.op,ast.Mult): return a*b
            if isinstance(n.op,ast.Div): return a/b
            if isinstance(n.op,ast.Pow): return a**int(b)
        raise ValueError(ast.dump(n))
    return ev(ast.parse(str(e).replace('^','**'),mode='eval').body)
def phys_at(key,val):
    N=norm[key]; d={}
    for r,z,e in maps[key]:
        c=evnum(e,val)
        if c: p=(N-int(r)-int(z),int(z)); d[p]=d.get(p,Q(0))+c
    return {p:v for p,v in d.items() if v}
# ---- V_C basis: 192 polynomials ----
A3=maps['A3']; lfs=[(98-int(r)-int(z),int(z),linform(e)) for r,z,e in A3]
cnames=sorted({k for _,_,lf in lfs for k in lf if k is not None}); assert len(cnames)==192
basis={}
for n in cnames:
    P={}
    for i,z,lf in lfs:
        if n in lf: P[(i,z)]=P.get((i,z),Q(0))+lf[n]
    basis[n]={p:v for p,v in P.items() if v}
assert all(k is not None for _,_,lf in lfs for k in lf), "constant entry in A3"
print("V_C: 192 basis polys; max deg",max(deg(P) for P in basis.values()),"max W-exp",max(j for P in basis.values() for i,j in P),"any W^33:",any((0,33) in P for P in basis.values()))
# ---- rank mod p of a list of polynomials (as vectors) ----
def rank_modp(polys):
    mons=sorted({m for P in polys for m in P}); idx={m:k for k,m in enumerate(mons)}
    rows=[]
    for P in polys:
        v={}
        for m,c in P.items():
            v[idx[m]]=(c.numerator*pow(c.denominator,-1,PR))%PR
        rows.append(v)
    rank=0; pivots={}
    for v in rows:
        v=dict(v)
        while v:
            c=min(v)
            if c in pivots:
                pv=pivots[c]; f=v[c]
                for k,x in pv.items(): v[k]=(v.get(k,0)-f*x)%PR
                v={k:x for k,x in v.items() if x}
            else:
                inv=pow(v[c],-1,PR); v={k:x*inv%PR for k,x in v.items()}; pivots[c]=v; rank+=1; break
    return rank
def in_span(polys,target):
    return rank_modp(polys+[target])==rank_modp(polys)
H={(3-i,8+i):Q(comb(3,i)) for i in range(4)}
def pw(a,n):
    o={(0,0):Q(1)}
    for _ in range(n): o=mul(o,a)
    return o
H3,H6=pw(H,3),pw(H,6)
Bl=list(basis.values())
# ---- own hypothesis-mutation controls ----
print("CTRL A (drop transverse line): G=H^6, P=H: J==0:",jac(H,H6)=={}, "H in V_C:",in_span(Bl,H),"G(X,0)==0:",not any(j==0 for i,j in H6))
R=add(H3,{(1,0):Q(1)}); G2=mul(R,R)
print("CTRL B (drop W^33 exclusion): P=H^3+X,G=P^2: J==0:",jac(R,G2)=={},"G(X,0):",{p:v for p,v in G2.items() if p[1]==0},"P has W^33:",R.get((0,33)),"P in V_C:",in_span(Bl,R))
R2={(1,32):Q(1),(1,0):Q(1)}; G3=mul(R2,R2)
print("CTRL C (mutate G_top: no W^66): P=XW^32+X, G=P^2: J==0:",jac(R2,G3)=={},"deg G",deg(G3),"G(X,0):",{p:v for p,v in G3.items() if p[1]==0},"G_top W^66 coeff:",G3.get((0,66)),"P deg",deg(R2),"P max W",max(j for i,j in R2),"P in V_C:",in_span(Bl,R2))
R3=add(H3,{(2,0):Q(1)}); G4=mul(R3,R3)
print("CTRL D (mutate restriction degree: G(X,0)=X^4): P=H^3+X^2, G=P^2: J==0:",jac(R3,G4)=={},"G(X,0):",{p:v for p,v in G4.items() if p[1]==0},"P in V_C:",in_span(Bl,R3))
Rc=basis['A3c_97_0']; Gc=mul(Rc,Rc)
print("CTRL C' (G_top mutated, P inside actual V_C): P=basis(A3c_97_0)=",sorted(Rc.items()),"G=P^2: J==0:",jac(Rc,Gc)=={},"deg G",deg(Gc),"G(X,0):",sorted({p:v for p,v in Gc.items() if p[1]==0}.items()),"G_top W^66:",Gc.get((0,66)),"P in V_C: True by construction; P deg",deg(Rc))
print("X alone in V_C:",in_span(Bl,{(1,0):Q(1)})," XW^32 alone in V_C:",in_span(Bl,{(1,32):Q(1)}))
print("CTRL E positive-only: J(X, X^2+W)=",jac({(1,0):Q(1)},{(2,0):Q(1),(0,1):Q(1)}))
# ---- sample base points ----
bnames=sorted({k for key in ['h3','C2','C3','B2'] for r,z,e in maps[key] for k in re.findall(r'[A-Za-z_][A-Za-z0-9_]*',str(e))}); assert len(bnames)==245
def build(val,b):
    h3,C2,C3,D=phys_at('h3',val),phys_at('C2',val),phys_at('C3',val),phys_at('B2',val)
    h=add(add(mul(mul(h3,h3),h3),mul(C2,h3)),C3)
    G=add(add(mul(h,h),h,Q(-b,3)),D)
    return h,D,G
def report(tag,val,b):
    h,D,G=build(val,b)
    top={p:v for p,v in G.items() if p[0]+p[1]==66}
    line={p:v for p,v in G.items() if p[1]==0}
    Js=[jac(P,G) for P in Bl]
    rk=rank_modp(Js)
    Jsp=[{p:v for p,v in J.items() if p!=(0,0)} for J in Js]
    rkp=rank_modp(Jsp)
    Ja=jac({p:v/2 for p,v in h.items()},G)
    rka=rank_modp(Js+[Ja]); rkap=rank_modp(Jsp+[{p:v for p,v in Ja.items() if p!=(0,0)}])
    print(f"{tag}: deg h={deg(h)} deg D={deg(D)} deg G={deg(G)} G_top==H^6:{top==H6} G(X,0)={sorted(line.items())} | rank full C map={rk} positive-only C={rkp} | (C,a) full={rka} (C,a) positive-only={rkap}")
    return h,G
val={n:Q(random.randint(-3,3)) for n in bnames}; b=Q(random.randint(-3,3))
h,G=report("RANDOM base point",val,b)
val0={n:(Q(0) if n.startswith('B2c_') else Q(random.randint(-3,3))) for n in bnames}
h0,G0=report("D=0,b=0 base point",val0,Q(0))
val1={n:(Q(0) if n.startswith('B2c_') and n!='B2c_65_0' else Q(random.randint(-3,3))) for n in bnames}; val1['B2c_65_0']=Q(5)
report("D=const,b!=0 base point",val1,Q(3))
# ---- W-adapted lemma instantiation ----
V0=[basis[n] for n in cnames if n not in ('A3c_97_0','A3c_98_0')]; assert len(V0)==190
def key(m): return (m[1],-m[0])   # W-exp ascending, X-exp descending
# echelon over Q with leading monomial = min under key
ech=[]
for P in V0:
    P=dict(P)
    while P:
        lm=min(P,key=key)
        hit=[E for E in ech if E[0]==lm]
        if hit:
            E=hit[0]; f=P[lm]; P=add(P,E[1],-f)
        else:
            c=P[lm]; P={p:v/c for p,v in P.items()}; ech.append((lm,P)); break
ech.sort(key=lambda E:key(E[0]))
print("W-adapted basis size:",len(ech),"distinct leading (i,r):",len({E[0] for E in ech}),"min r:",min(E[0][1] for E in ech),"max r:",max(E[0][1] for E in ech))
def selected_matrix(G):
    rows=[(i+1,r-1) for (i,r),_ in ech]
    Js=[jac(P,G) for _,P in ech]
    M=[[Js[l].get(rows[k],Q(0)) for l in range(len(ech))] for k in range(len(ech))]
    return rows,M
def check(tag,G):
    rows,M=selected_matrix(G); n=len(M)
    upper_zero=all(M[k][l]==0 for k in range(n) for l in range(k+1,n))
    diag=[M[k][k] for k in range(n)]
    expect=[Q(-2)*r for (i,r),_ in ech]
    print(f"{tag}: rows distinct={len(set(rows))==n} all rows positive degree={all(a+b>=1 for a,b in rows)} upper-zero={upper_zero} diag==-2r:{diag==expect} zero-diag count={sum(1 for d in diag if d==0)} G_X(X,0)={sorted(dX({p:v for p,v in G.items() if p[1]==0}).items())}")
check("W-lemma at RANDOM actual G",G)
check("W-lemma at D=0,b=0 actual G",G0)
check("W-lemma NEG G=H^6 (G(X,0)=0)",H6)
check("W-lemma NEG G=H^6+X (G(X,0) linear)",add(H6,{(1,0):Q(1)}))
check("W-lemma non-monic G=H^6+3X^2",add(H6,{(2,0):Q(3)}))
