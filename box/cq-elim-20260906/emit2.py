import sys, json, math; sys.path.insert(0,'box/cq-elim-20260906')
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
def primitive(vec):
    den=1
    for c in vec: den=den*c.denominator//math.gcd(den,c.denominator)
    ints=[int(c*den) for c in vec]
    g=0
    for v in ints: g=math.gcd(g,abs(v))
    return [v//g for v in ints] if g else ints

nu=1; a=54; b=65; nrows=119
cols=[]
for k in range(a+1):
    e=[Fr(0)]*(a+1); e[k]=Fr(1); cols.append(Jd(e,a,P6,66))
for k in range(b+1):
    e=[Fr(0)]*(b+1); e[k]=Fr(1); cols.append(Jd(P5,55,e,b))
K=[primitive(v) for v in kernel(cols,nrows)]
K=[[Fr(c) for c in v] for v in K]
NP=len(K)
KA=[trim([K[s][k] for k in range(a+1)]) for s in range(NP)]
KB=[trim([K[s][a+1+k] for k in range(b+1)]) for s in range(NP)]
for s in range(NP): assert not padd(Jd(KA[s],a,P6,66), Jd(P5,55,KB[s],b))
print("ker L_1 dim",NP,"(primitive integer basis, all verified)")

D = pmul(ppow([Fr(0),Fr(1)],14), ppow([Fr(-1),Fr(1)],39))
def prem(A,Dv):
    A=A[:]; dd=len(Dv)-1
    for i in range(len(A)-1,dd-1,-1):
        if A[i]==0: continue
        f=A[i]/Dv[-1]
        for j in range(dd+1): A[i-dd+j]-=f*Dv[j]
    return trim(A[:dd])
pairs={}
for s in range(NP):
    for t in range(NP):
        Jst=Jd(KA[s],a,KB[t],b)
        if Jst:
            key=(min(s,t),max(s,t)); pairs[key]=padd(pairs.get(key,[]),Jst)
rem={k:prem(v,D) for k,v in pairs.items()}
NR=len(D)-1
eqs=[dict() for _ in range(NR)]
for (s,t),v in rem.items():
    for i,ci in enumerate(v):
        if ci: eqs[i][(s,t)]=ci
nz=[i for i in range(NR) if eqs[i]]
print("obstruction: %d quadrics in %d unknowns"%(len(nz),NP))

def polystr(d):
    keys=sorted(d); prim=primitive([d[k] for k in keys])
    out=[]; line=""; lines=[]
    for (s,t),c in zip(keys,prim):
        term="%+d*u%d*u%d"%(c,s+1,t+1)
        if len(line)+len(term)>62: lines.append(line); line=term
        else: line+=term
    if line: lines.append(line)
    return "\n".join(lines)

def emit(fn, charac, extra=""):
    with open(fn,'w') as f:
        vl=['u%d'%(i+1) for i in range(NP)]
        rl=[]; cur=''
        for v in vl:
            if len(cur)+len(v)>55: rl.append(cur); cur=v+','
            else: cur+=v+','
        rl.append(cur.rstrip(','))
        f.write('ring R=%s,(%s),dp;\n'%(charac,'\n'.join(rl)))
        f.write('ideal I=\n'+",\n".join(polystr(eqs[i]) for i in nz)+';\n')
        f.write('int t0=timer;\n')
        f.write('option(redSB);\nideal S=std(I);\n')
        f.write('"MARK rows="+string(size(I));\n"MARK GBsize="+string(size(S));\n')
        f.write('"MARK unit="+string(S[1]==1);\n"MARK dim="+string(dim(S));\n')
        f.write('"MARK degree="+string(mult(S));\n')
        f.write('"MARK secs="+string(timer-t0);\n'+extra+'exit;\n')
emit('box/cq-elim-20260906/band2_p.sing',32003)
emit('box/cq-elim-20260906/band2_q.sing',0)
print("emitted band2_p.sing (mod 32003 scout) and band2_q.sing (exact Q)")
json.dump({"kerL1":NP,"quadrics":len(nz)},open('box/cq-elim-20260906/band2.json','w'))
