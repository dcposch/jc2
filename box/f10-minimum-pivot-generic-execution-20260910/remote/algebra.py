"""UNEXECUTED exact B[x,y,z][s,s^-1,S,t] backend; no entrypoint.
Only Q division and explicitly certified B-unit inverses are implemented.
"""
from fractions import Fraction as Q
from math import gcd

AXES = ['x', 'y', 'z', 's', 'S', 't', 'v']
ZERO = (0,) * 7

def require(ok, why):
    if not ok:
        raise ValueError(why)

def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a

def da(a,b):
    return trim([(a[i] if i<len(a) else Q(0))+(b[i] if i<len(b) else Q(0)) for i in range(max(len(a),len(b)))])

def ds(a,c):
    return trim([x*c for x in a])

def dm(a,b):
    out=[Q(0)]*max(0,len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):
            out[i+j]+=c*d
    return trim(out)

def dd(a,b):
    require(bool(b),'zero rational-polynomial divisor')
    a=trim(a); q=[Q(0)]*max(0,len(a)-len(b)+1)
    while a and len(a)>=len(b):
        k=len(a)-len(b); c=a[-1]/b[-1]; q[k]+=c
        a=da(a,[Q(0)]*k+ds(b,-c))
    return trim(q),a

def dxg(a,b):
    r0,r1=trim(a),trim(b); x0,x1=[Q(1)],[]; y0,y1=[],[Q(1)]
    while r1:
        q,r2=dd(r0,r1)
        r0,r1=r1,r2
        x0,x1=x1,da(x0,ds(dm(q,x1),-1))
        y0,y1=y1,da(y0,ds(dm(q,y1),-1))
    require(bool(r0),'zero gcd inputs')
    c=1/r0[-1]
    return ds(r0,c),ds(x0,c),ds(y0,c)

def modulus():
    E=list(map(Q,[39,-360,960,-512])); L=list(map(Q,[25,-144,192])); R=list(map(Q,[-195,2016,-6720,7168]))
    return da(da(ds(dm(R,R),24),dm([Q(280),Q(-1344)],dm(L,R))),ds(dm(E,dm(L,L)),49))

class Ring:
    def __init__(self):
        self.p=modulus(); require(len(self.p)==8,'degree-seven modulus')
        self.monic=ds(self.p,1/self.p[-1])
    def red(self,a):
        return dd(a,self.monic)[1]
    def c(self,c):
        return {ZERO:Q(c)} if c else {}
    def atom(self,i,n=1):
        e=list(ZERO); e[i]=n
        return {tuple(e):Q(1)}
    def embed(self,a):
        return {ZERO[:-1]+(i,):c for i,c in enumerate(self.red(a)) if c}
    def dense(self,a):
        require(all(not any(e[:-1]) for e in a),'not a B coefficient')
        return trim([a.get(ZERO[:-1]+(i,),Q(0)) for i in range(7)])
    def add(self,*args):
        out={}
        for a in args:
            for e,c in a.items(): out[e]=out.get(e,Q(0))+c
        return {e:c for e,c in out.items() if c}
    def scale(self,a,c):
        return {e:x*c for e,x in a.items() if x*c}
    def sub(self,a,b):
        return self.add(a,self.scale(b,-1))
    def mul(self,a,b):
        groups={}
        for e,c in a.items():
            for f,d in b.items():
                k=tuple(x+y for x,y in zip(e,f)); g=groups.setdefault(k[:-1],{})
                g[k[-1]]=g.get(k[-1],Q(0))+c*d
        out={}
        for e,g in groups.items():
            for i,c in enumerate(self.red([g.get(i,Q(0)) for i in range(max(g)+1)])):
                if c: out[e+(i,)]=c
        return out
    def pow(self,a,n):
        require(type(n) is int and n>=0,'nonnegative polynomial power required')
        out=self.c(1)
        while n:
            if n&1: out=self.mul(out,a)
            n//=2
            if n: a=self.mul(a,a)
        return out
    def inv(self,a,label):
        # Caller supplies ONLY a theorem-proved unit; identity still checked.
        g,x,_=dxg(self.dense(a),self.monic)
        require(g==[Q(1)],'proved unit failed: '+label)
        out=self.embed(x); self.eq(self.mul(a,out),self.c(1),'unit identity '+label)
        return out
    def pair(self,a,b):
        # Bezout of the ideal (a,b,p), NOT either coefficient inversion.
        g,x,y=dxg(self.dense(a),self.dense(b)); h,u,_=dxg(g,self.monic)
        require(h==[Q(1)],'column not unimodular')
        l,r=self.embed(dm(u,x)),self.embed(dm(u,y))
        self.eq(self.add(self.mul(a,l),self.mul(b,r)),self.c(1),'literal column identity')
        return l,r
    def eq(self,a,b,why):
        require(a==b,why)
    def diff(self,a,i):
        out={}
        for e,c in a.items():
            if e[i]:
                f=list(e); f[i]-=1; out[tuple(f)]=c*e[i]
        return out
    def coeff(self,a,i,n):
        out={}
        for e,c in a.items():
            if e[i]==n:
                f=list(e); f[i]=0; out[tuple(f)]=c
        return out
    def wire(self,a):
        return [[list(e),str(c.numerator),str(c.denominator)] for e,c in sorted(a.items())]
    def read(self,w,width=7):
        out={}; prev=None
        require(type(w) is list,'wire list')
        for e,n,d in w:
            require(type(e) is list and len(e)==width and all(type(i) is int for i in e),'exponent type/width')
            require(type(n) is str and type(d) is str,'rational strings only')
            nn,dden=int(n),int(d)
            require(str(nn)==n and str(dden)==d and nn and dden>0 and gcd(abs(nn),dden)==1,'canonical rational')
            k=tuple(e); require(prev is None or prev<k,'sorted unique wire'); prev=k
            require(all(i>=0 for a,i in enumerate(e) if a!=3) and (width!=7 or e[6]<7),'wire exponent domain')
            out[k]=Q(nn,dden)
        return out
    def compose(self,a,maps):
        out={}
        for e,c in a.items():
            term=self.c(c)
            for i,n in enumerate(e):
                if n: term=self.mul(term,self.pow(maps[i],n))
            out=self.add(out,term)
        return out
    def at_z_s2(self,a):
        out={}
        for e,c in a.items():
            f=list(e); f[3]+=2*f[2]; f[2]=0
            k=tuple(f); out[k]=out.get(k,Q(0))+c
        return {e:c for e,c in out.items() if c}
    def bracket(self,a,b):
        return self.sub(self.mul(self.diff(a,4),self.diff(b,5)),self.mul(self.diff(a,5),self.diff(b,4)))

def determinant(r,M):
    if not M: return r.c(1)
    return r.add(*(r.scale(r.mul(M[0][i],determinant(r,[[x for j,x in enumerate(row) if j!=i] for row in M[1:]])),(-1)**i) for i in range(len(M))))

def matrix_inverse(r,M,label):
    n=len(M); det=determinant(r,M); invdet=r.inv(det,label)
    out=[[r.mul(invdet,r.scale(determinant(r,[[M[a][b] for b in range(n) if b!=i] for a in range(n) if a!=j]),(-1)**(i+j))) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n): r.eq(r.add(*(r.mul(M[i][k],out[k][j]) for k in range(n))),r.c(i==j),'matrix inverse '+label)
    return out,det,invdet

def matvec(r,M,v):
    return [r.add(*(r.mul(a,b) for a,b in zip(row,v))) for row in M]
