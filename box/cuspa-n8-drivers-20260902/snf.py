"""Integer SNF with transforms:  U*M*V = D."""
def snf(Min):
    m=[row[:] for row in Min]; R=len(m); C=len(m[0]) if R else 0
    U=[[1 if i==j else 0 for j in range(R)] for i in range(R)]
    V=[[1 if i==j else 0 for j in range(C)] for i in range(C)]
    def rswap(a,b):
        m[a],m[b]=m[b],m[a]; U[a],U[b]=U[b],U[a]
    def cswap(a,b):
        for row in m: row[a],row[b]=row[b],row[a]
        for row in V: row[a],row[b]=row[b],row[a]
    def raddm(src,dst,q):   # row dst -= q*row src
        for k in range(C): m[dst][k]-=q*m[src][k]
        for k in range(R): U[dst][k]-=q*U[src][k]
    def caddm(src,dst,q):   # col dst -= q*col src
        for row in m: row[dst]-=q*row[src]
        for row in V: row[dst]-=q*row[src]
    r=0; c=0
    while r<R and c<C:
        piv=None; best=None
        for i in range(r,R):
            for j in range(c,C):
                v=abs(m[i][j])
                if v and (best is None or v<best): best,piv=v,(i,j)
        if piv is None: break
        while True:
            i,j=piv; rswap(r,i); cswap(c,j)
            p=m[r][c]; changed=False
            for i2 in range(r+1,R):
                if m[i2][c]:
                    q=m[i2][c]//p
                    if q: raddm(r,i2,q)
                    if m[i2][c]: changed=True
            for j2 in range(c+1,C):
                if m[r][j2]:
                    q=m[r][j2]//p
                    if q: caddm(c,j2,q)
                    if m[r][j2]: changed=True
            if not changed: break
            best=None; piv=None
            for i2 in range(r,R):
                for j2 in range(c,C):
                    v=abs(m[i2][j2])
                    if v and (best is None or v<best): best,piv=v,(i2,j2)
        p=m[r][c]
        for i2 in range(r+1,R):
            if m[i2][c]: raddm(r,i2,m[i2][c]//p)
        for j2 in range(c+1,C):
            if m[r][j2]: caddm(c,j2,m[r][j2]//p)
        r+=1; c+=1
    return m,U,V,r

def inv_unimodular(V):
    n=len(V)
    A=[row[:]+[1 if i==j else 0 for j in range(n)] for i,row in enumerate(V)]
    from fractions import Fraction
    A=[[Fraction(x) for x in row] for row in A]
    for col in range(n):
        piv=None
        for i in range(col,n):
            if A[i][col]!=0: piv=i;break
        A[col],A[piv]=A[piv],A[col]
        pv=A[col][col]
        A[col]=[x/pv for x in A[col]]
        for i in range(n):
            if i!=col and A[i][col]!=0:
                f=A[i][col]
                A[i]=[a-f*b for a,b in zip(A[i],A[col])]
    out=[[int(A[i][n+j]) for j in range(n)] for i in range(n)]
    return out
