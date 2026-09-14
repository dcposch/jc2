import sys, json; sys.path.insert(0,'box/cq-elim-20260906')
from band import pmul,padd,pscal,pder,trim,ppow,Jd
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

def run(tag, n,m,D2, k1,k2, eF,eG,eQ):
    """P0 = y^k1 (y-x)^k2 ; F_top=P0^eF, G_top=P0^eG, Q_top=lam*P0^eQ"""
    p = pmul(ppow([Fr(0),Fr(1)],k1), ppow([Fr(-1),Fr(1)],k2))
    d=len(p)-1
    PF,PG,PQ = ppow(p,eF), ppow(p,eG), ppow(p,eQ)
    assert len(PF)-1==n and len(PG)-1==m and len(PQ)-1==D2, (len(PF)-1,len(PG)-1,len(PQ)-1)
    drop = D2+m-2-n
    print("== %s ==  n=%d m=%d D2=%d ; P0=y^%d(y-x)^%d deg %d ; tops P0^%d,P0^%d,lam*P0^%d"
          %(tag,n,m,D2,k1,k2,d,eF,eG,eQ))
    print("   deg Q + deg G - 2 = %d ; deg F = %d ; DEGREE DROP = %d bands"%(D2+m-2,n,drop))
    print("   top consistency  G_top^3 - F_top^2 =", "0" if not padd(ppow(PG,3),pscal(-1,ppow(PF,2))) else "NONZERO")
    print("   band nu=0  J(Q_top,G_top) =", "0" if not Jd(PQ,D2,PG,m) else "NONZERO")
    # obstruction divisor prediction: Q_top / (y*(y-x))
    Dv = pmul(ppow([Fr(0),Fr(1)],k1*eQ-1), ppow([Fr(-1),Fr(1)],k2*eQ-1))
    print("   predicted obstruction divisor  y^%d(y-x)^%d  deg %d"%(k1*eQ-1,k2*eQ-1,len(Dv)-1))
    rows=[]
    for nu in range(1,drop+1):
        a=D2-nu; b=m-nu; nrows=(D2+m-2-nu)+1
        cols=[]
        for kk in range(a+1):
            e=[Fr(0)]*(a+1); e[kk]=Fr(1); cols.append(Jd(e,a,PG,m))
        for kk in range(b+1):
            e=[Fr(0)]*(b+1); e[kk]=Fr(1); cols.append(Jd(PQ,D2,e,b))
        r=rank_of(cols,nrows)
        qdeg=nrows-1-(len(Dv)-1)
        cols2=[]
        for kk in range(qdeg+1):
            e=[Fr(0)]*(qdeg+1); e[kk]=Fr(1); cols2.append(pmul(Dv,e))
        r2=rank_of(cols2,nrows); ru=rank_of(cols+cols2,nrows)
        rows.append(dict(nu=nu,rows=nrows,rank=r,ker=(a+1)+(b+1)-r,obstr=nrows-r,pred=r2,exact=(r==r2)))
    exact=sum(1 for x in rows if x['exact']); print("   bands: %d ; obstruction divisor exact on %d/%d bands ; obstr rows/band = %s"
        %(len(rows),exact,len(rows),sorted(set(x['obstr'] for x in rows))))
    print("   kernel dims: %s ... %s ; total ker(1..%d)=%d, total obstr(2..%d)=%d"
        %([x['ker'] for x in rows[:3]],[x['ker'] for x in rows[-2:]],drop-1,
          sum(x['ker'] for x in rows[:drop-1]),drop-1,sum(x['obstr'] for x in rows[1:drop-1])))
    return rows

r99  = run("(99,66)  delta=2/5-2",  99,66,55, 3,8, 9,6,5)
print()
r108 = run("D=108    delta=3",     108,72,63, 2,7, 12,8,7)
json.dump({"g9966":r99,"d108":r108}, open('box/cq-elim-20260906/bandprofile.json','w'))
