import sys, json; sys.path.insert(0,'box/cq-elim-20260906')
from band import *
from fractions import Fraction as Fr

def kernel(cols,nrows):
    n=len(cols); M=[[(cols[k][i] if i<len(cols[k]) else Fr(0)) for k in range(n)] for i in range(nrows)]
    piv=[];r=0
    for c in range(n):
        pr=None
        for i in range(r,nrows):
            if M[i][c]!=0: pr=i;break
        if pr is None: continue
        M[r],M[pr]=M[pr],M[r]; pv=M[r][c]; M[r]=[v/pv for v in M[r]]
        for i in range(nrows):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[M[i][j]-f*M[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==nrows: break
    free=[c for c in range(n) if c not in piv]; K=[]
    for fc in free:
        v=[Fr(0)]*n; v[fc]=Fr(1)
        for i,c in enumerate(piv): v[c]=-M[i][fc]
        K.append(v)
    return K

nu=1; a=55-nu; b=66-nu; nrows=(119-nu)+1
cols=[]
for k in range(a+1):
    e=[Fr(0)]*(a+1); e[k]=Fr(1); cols.append(Jd(e,a,P6,66))
for k in range(b+1):
    e=[Fr(0)]*(b+1); e[k]=Fr(1); cols.append(Jd(P5,55,e,b))
K=kernel(cols,nrows)
NP=len(K); print("dim ker L_1 =",NP)

# Q54 = sum_s u_s * KA_s(y) ,  G65 = sum_s u_s * KB_s(y)
KA=[trim([K[s][k] for k in range(a+1)]) for s in range(NP)]
KB=[trim([K[s][a+1+k] for k in range(b+1)]) for s in range(NP)]
# sanity: each kernel vector must satisfy L_1 = 0
for s in range(NP):
    chk=padd(Jd(KA[s],a,P6,66), Jd(P5,55,KB[s],b))
    assert not chk, ("kernel check failed",s)
print("kernel vectors verified against L_1 = 0 :", NP,"/",NP)

# band-2 obstruction:  D | J(Q54,G65)  with D = y^14 (y-1)^39
D = pmul(ppow([Fr(0),Fr(1)],14), ppow([Fr(-1),Fr(1)],39))
# bilinear: J(Q54,G65) = sum_{s<=t} c_st * u_s u_t
pairs={}
for s in range(NP):
    for t in range(NP):
        Jst = Jd(KA[s],a,KB[t],b)
        if not Jst: continue
        key=(min(s,t),max(s,t))
        pairs[key]=padd(pairs.get(key,[]),Jst)
print("nonzero bilinear pair-polys:",len(pairs))
# reduce each pair-poly mod D -> remainder of degree < 53 ; those 53 coeffs are the rows
def prem(A,Dv):
    A=A[:]; dd=len(Dv)-1; lc=Dv[-1]
    for i in range(len(A)-1,dd-1,-1):
        if A[i]==0: continue
        f=A[i]/lc
        for j in range(dd+1): A[i-dd+j]-=f*Dv[j]
    return trim(A[:dd])
rem={k:prem(v,D) for k,v in pairs.items()}
NR=len(D)-1   # 53
rows=[[Fr(0)]*0 for _ in range(NR)]
eqs=[dict() for _ in range(NR)]
for (s,t),v in rem.items():
    for i,ci in enumerate(v):
        if ci: eqs[i][(s,t)]=ci
nz=[i for i in range(NR) if eqs[i]]
print("obstruction rows: %d slots, %d nonzero -> %d quadrics in %d unknowns"%(NR,len(nz),len(nz),NP))
# emit Singular
with open('box/cq-elim-20260906/band2.sing','w') as f:
    f.write('ring R=0,(u(1..%d)),dp;\n'%NP)
    f.write('ideal I=\n')
    terms=[]
    for i in nz:
        s=[]
        for (p_,q_),c in sorted(eqs[i].items()):
            num,den=c.numerator,c.denominator
            s.append(("%+d"%num if den==1 else "%+d/%d"%(num,den))+"*u(%d)*u(%d)"%(p_+1,q_+1))
        terms.append("".join(s))
    f.write(",\n".join(terms)+";\n")
    f.write('option(redSB);\n')
    f.write('def t0=timer;\n')
    f.write('ideal S=std(I);\n')
    f.write('"rows="+string(size(I));\n')
    f.write('"GBsize="+string(size(S));\n')
    f.write('"dim="+string(dim(S));\n')
    f.write('"UNIT?="+string(S[1]==1);\n')
    f.write('"secs="+string(timer-t0);\n')
    f.write('exit;\n')
json.dump({"kerL1":NP,"quadrics":len(nz)},open('box/cq-elim-20260906/band2.json','w'))
print("emitted box/cq-elim-20260906/band2.sing")
