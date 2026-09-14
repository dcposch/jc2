import sys, json; sys.path.insert(0,'box/cq-elim-20260906')
from band import *
from fractions import Fraction as Fr

def rank_of(cols,nrows):
    n=len(cols); M=[[(cols[k][i] if i<len(cols[k]) else Fr(0)) for k in range(n)] for i in range(nrows)]
    r=0
    for c in range(n):
        pr=None
        for i in range(r,nrows):
            if M[i][c]!=0: pr=i;break
        if pr is None: continue
        M[r],M[pr]=M[pr],M[r]; pv=M[r][c]; M[r]=[v/pv for v in M[r]]
        for i in range(nrows):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[M[i][j]-f*M[r][j] for j in range(n)]
        r+=1
        if r==nrows: break
    return r

# claim:  Im L_nu  ==  y^14*(y-1)^39 * { all polys of degree <= 65-nu }
D = pmul(ppow([Fr(0),Fr(1)],14), ppow([Fr(-1),Fr(1)],39))     # y^14 (y-1)^39, degree 53
print("divisor D = y^14 (y-1)^39,  deg =",len(D)-1, " = P0^4 * y^2(y-1)^7")
print()
print(" nu | rank L_nu | dim( D * deg<=%s ) | equal? | 53-row obstruction = 'D divides C_nu'"%"(65-nu)")
print("----+-----------+--------------------+--------+-------------------------------------")
ok_all=True
for nu in range(1,21):
    a=55-nu; b=66-nu; nrows=(119-nu)+1
    cols=[]
    for k in range(a+1):
        e=[Fr(0)]*(a+1); e[k]=Fr(1); cols.append(Jd(e,a,P6,66))
    for k in range(b+1):
        e=[Fr(0)]*(b+1); e[k]=Fr(1); cols.append(Jd(P5,55,e,b))
    r=rank_of(cols,nrows)
    # span of D * (deg <= 65-nu)
    cols2=[]
    for k in range(66-nu+1):
        e=[Fr(0)]*(66-nu+1); e[k]=Fr(1); cols2.append(pmul(D,e))
    r2=rank_of(cols2,nrows)
    # is Im L_nu contained in D*(...)?  test rank of the union
    ru=rank_of(cols+cols2,nrows)
    eq = (r==r2==ru)
    ok_all = ok_all and (ru==r2)
    print(" %2d | %9d | %18d | %s | %s"%(nu,r,r2, "YES" if eq else ("Im subset" if ru==r2 else "NO"),
          "%d rows"%(nrows-r)))
print()
print("containment Im L_nu subset D*(...) for all tested nu:", ok_all)
