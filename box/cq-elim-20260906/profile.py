import sys, json; sys.path.insert(0,'box/cq-elim-20260906')
from band import *
from fractions import Fraction as Fr

def basis(nc): 
    for k in range(nc):
        e=[Fr(0)]*nc; e[k]=Fr(1); yield e

def rank_and_kernel(cols, nrows):
    """cols: list of y-polys (each a column vector of length nrows). exact rank + kernel basis."""
    n=len(cols)
    M=[[ (cols[k][i] if i<len(cols[k]) else Fr(0)) for k in range(n)] for i in range(nrows)]
    piv=[]; r=0; m=nrows
    for c in range(n):
        pr=None
        for i in range(r,m):
            if M[i][c]!=0: pr=i; break
        if pr is None: continue
        M[r],M[pr]=M[pr],M[r]
        pv=M[r][c]; M[r]=[v/pv for v in M[r]]
        for i in range(m):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[M[i][j]-f*M[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    ker=[]
    for fc in free:
        v=[Fr(0)]*n; v[fc]=Fr(1)
        for i,c in enumerate(piv): v[c]=-M[i][fc]
        ker.append(v)
    return r, ker, piv

print(" nu | dim(A,B) | rows | rank L_nu | ker L_nu | obstruction rows | im in p^4*(.)")
print("----+----------+------+-----------+----------+------------------+--------------")
prof=[]
for nu in range(1,21):
    a=55-nu; b=66-nu
    nrows=(119-nu)+1
    cols=[]
    for e in basis(a+1): cols.append(Jd(e,a,P6,66))          # J(Q_{55-nu}, G_66)
    for e in basis(b+1): cols.append(Jd(P5,55,e,b))          # J(Q_55,   G_{66-nu})   (Q monic-top)
    r,ker,piv = rank_and_kernel(cols,nrows)
    ndom=(a+1)+(b+1)
    obstr=nrows-r
    prof.append(dict(nu=nu,dom=ndom,rows=nrows,rank=r,ker=len(ker),obstr=obstr))
    print(" %2d | %8d | %4d | %9d | %8d | %16d | %d"%(nu,ndom,nrows,r,len(ker),obstr,76-nu))
json.dump(prof,open('box/cq-elim-20260906/profile.json','w'))
tot_ker=sum(x['ker'] for x in prof[:19]); tot_obs=sum(x['obstr'] for x in prof[1:19])
print()
print("bands 1..19 : cumulative kernel params = %d ; cumulative obstruction rows (nu=2..19) = %d"%(tot_ker,tot_obs))
