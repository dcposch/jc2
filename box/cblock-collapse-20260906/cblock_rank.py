import json,random,hashlib,sys
import numpy as np
import sympy as S
P=(1<<31)-1
SRC='/home/ubuntu/jc2/box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json'
raw=open(SRC,'rb').read()
assert hashlib.sha256(raw).hexdigest()=='778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea'
d=json.loads(raw); assert d['residual_rows']==[]
NORM={'h3':11,'C2':22,'C3':33,'B2':65,'A3':98}
maps={k:[(r,z,S.sympify(e)) for r,z,e in v] for k,v in d['maps'].items()}
syms={k:set().union(*(e.free_symbols for _,_,e in v)) for k,v in maps.items()}
cvars=sorted(syms['A3'],key=str); assert len(cvars)==192
other=set().union(*(syms[n] for n in ('h3','C2','C3','B2')))
assert not (set(cvars)&other)
# extra scalars a,b
extra=set()
for row in d.get('degree_premap',[]) if isinstance(d.get('degree_premap'),list) else []: pass
allsyms=sorted(other|set(cvars),key=str)
rng=random.Random(20260906)
val={s:rng.randrange(1,P) for s in other}
N=110
def zeros(): return np.zeros((N,N),dtype=np.int64)
def addterm(A,i,j,c): A[i,j]=(A[i,j]+c)%P
def mul(A,B):
    R=zeros(); nz=np.argwhere(A%P!=0)
    for i,j in nz:
        c=int(A[i,j])%P
        if c==0: continue
        h_,w_=int(i),int(j)
        R[h_:N,w_:N]=(R[h_:N,w_:N]+c*B[0:N-h_,0:N-w_])%P
    return R
def dX(A):
    R=zeros(); R[0:N-1,:]=(A[1:N,:]*np.arange(1,N)[:,None])%P; return R
def dW(A):
    R=zeros(); R[:,0:N-1]=(A[:,1:N]*np.arange(1,N)[None,:])%P; return R
def jac(A,B): return (mul(dX(A),dW(B))-mul(dW(A),dX(B)))%P
def build(name,subs):
    Nn=NORM[name]; A=zeros()
    for r,z,e in maps[name]:
        c=int(e.subs(subs))%P if not e.is_Symbol else int(subs.get(e,0))%P
        i=Nn-r-z; assert i>=0
        addterm(A,i,z,c)
    return A
inv=lambda t:pow(int(t)%P,P-2,P)
h3=build('h3',val); C2=build('C2',val); C3=build('C3',val); B2=build('B2',val)
h=(mul(mul(h3,h3),h3)+mul(C2,h3)+C3)%P
D=B2
a=rng.randrange(1,P); b=rng.randrange(1,P)
def deg(A):
    nz=np.argwhere(A%P!=0)
    return -1 if len(nz)==0 else int(max(i+j for i,j in nz))
print('deg h3,C2,C3,h,D =',deg(h3),deg(C2),deg(C3),deg(h),deg(D))
G=(mul(h,h)-b*inv(3)%P*h+D)%P
print('deg G =',deg(G))
half=inv(2); 
T1=mul((3*D+ (a*np.eye(N,dtype=np.int64)*0)) %P, zeros())  # placeholder
coef=(3*D)%P; coef[0,0]=(coef[0,0]+a)%P; coef=(coef+b*h)%P; coef=(coef*half)%P
Phi0=mul(coef,jac(h,D))%P
print('deg Phi0 (no C) =',deg(Phi0))
# C columns: C is affine-linear in cvars
def Cpoly(cval):
    A=zeros()
    for r,z,e in maps['A3']:
        c=int(e.subs(cval))%P
        addterm(A,98-r-z,z,c)
    return A
zero_c={s:0 for s in cvars}
C0=Cpoly(zero_c)
idx={s:k for k,s in enumerate(cvars)}
lin=[[] for _ in cvars]
for r,z,e in maps['A3']:
    pe=S.expand(e)
    for s in pe.free_symbols:
        c=pe.coeff(s,1)
        assert c.is_number
        lin[idx[s]].append((98-r-z,z,int(c)%P))
cols=[]
for k in range(len(cvars)):
    Ck=zeros()
    for i,j,c in lin[k]: addterm(Ck,i,j,c)
    cols.append(jac(Ck,G)%P)
Phi=(Phi0+jac(C0,G))%P
print('deg C0 =',deg(C0),' deg J(C,G) col0 =',deg(cols[0]))
# assemble matrix over all monomial positions that are nonzero in some column or Phi
pos=set()
for M in cols+[Phi]:
    for i,j in np.argwhere(M%P!=0): pos.add((int(i),int(j)))
pos=sorted(pos)
posp=[p for p in pos if p!=(0,0)]
print('nonzero positions total, positive-degree =',len(pos),len(posp))
def mat(rows):
    A=np.zeros((len(rows),len(cols)),dtype=np.int64)
    for c,M in enumerate(cols):
        for r,(i,j) in enumerate(rows): A[r,c]=M[i,j]%P
    return A
def rank(A):
    A=A.copy()%P; m,n=A.shape; r=0
    for c in range(n):
        piv=None
        for i in range(r,m):
            if A[i,c]%P: piv=i;break
        if piv is None: continue
        A[[r,piv]]=A[[piv,r]]
        iv=inv(A[r,c]); A[r]=(A[r]*iv)%P
        col=A[r+1:,c].copy()
        nzr=np.nonzero(col)[0]
        if len(nzr): A[r+1+nzr]=(A[r+1+nzr]-col[nzr][:,None]*A[r][None,:])%P
        r+=1
        if r==m: break
    return r
A=mat(posp)
rk=rank(A)
Ph=np.array([[Phi[i,j]%P] for (i,j) in posp],dtype=np.int64)
rk2=rank(np.hstack([A,Ph]))
print('rows=%d cols=%d  rank(A)=%d  rank([A|Phi])=%d'%(A.shape[0],A.shape[1],rk,rk2))
print('corank of C-block =',192-rk)
