"""Producer-only direct residue arithmetic. STATIC / UNEXECUTED."""
from fractions import Fraction as Q

P = None
PHI = None
DEGREE = None
UNITS = {}
DENOMINATORS = {}
ZERO = (0,)*7
WIRE_TERMS = 0


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def qa(a,b):
    return trim([(a[i] if i<len(a) else Q(0))+(b[i] if i<len(b) else Q(0))
                 for i in range(max(len(a),len(b)))])


def qs(a,c):
    return trim([v*c for v in a])


def qm(a,b):
    out = [Q(0)]*max(0,len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):
            out[i+j] += v*w
    return trim(out)


def integer(s, upper):
    if (not isinstance(s,str) or not s or len(s)>10 or not s.isascii()
            or not s.isdecimal() or (len(s)>1 and s[0]=='0')):
        raise ValueError('STOP_BAD_PLACE: decimal string')
    n = int(s)
    if n>upper:
        raise ValueError('STOP_BAD_PLACE: integer bound')
    return n


def ground(x):
    x=Q(x)
    if x.denominator % P == 0:
        raise ValueError('STOP_BAD_DENOMINATOR')
    return (x.numerator % P)*pow(x.denominator % P,-1,P) % P


def rem(a,b):
    a,b=trim([v%P for v in a]),trim([v%P for v in b])
    if not b:
        raise ValueError('zero divisor polynomial')
    while len(a)>=len(b):
        k,c=len(a)-len(b),a[-1]*pow(b[-1],-1,P)%P
        for i,v in enumerate(b):
            a[k+i]=(a[k+i]-c*v)%P
        a=trim(a)
    return a


def field(a):
    if isinstance(a,(int,Q)):
        a=[a]
    r=rem([ground(v) for v in a],PHI)
    return tuple(r+[0]*(DEGREE-len(r)))


def fa(a,b):
    return tuple((x+y)%P for x,y in zip(a,b))


def fn(a):
    return tuple((-x)%P for x in a)


def fm(a,b):
    out=[0]*(2*DEGREE-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):
            out[i+j]=(out[i+j]+v*w)%P
    r=rem(out,PHI)
    return tuple(r+[0]*(DEGREE-len(r)))


def fpow(a,n):
    out=field(1)
    while n:
        if n%2:
            out=fm(out,a)
        a,n=fm(a,a),n//2
    return out


def initialize(place,monic):
    global P,PHI,DEGREE
    P=integer(place['p'],2147483647)
    DEGREE=integer(place['degree'],7)
    if P<2 or DEGREE<1:
        raise ValueError('STOP_BAD_PLACE: bounds')
    trial=2
    while trial*trial<=P:
        if P%trial==0:
            raise ValueError('STOP_BAD_PLACE: composite')
        trial+=1
    if len(place['phi'])!=DEGREE+1 or len(place['P7_mod_p'])!=8:
        raise ValueError('STOP_BAD_PLACE: lengths')
    PHI=[integer(v,P-1) for v in place['phi']]
    prescribed=[integer(v,P-1) for v in place['P7_mod_p']]
    if PHI[-1]!=1 or prescribed[-1]!=1 or prescribed!=[ground(v) for v in monic]:
        raise ValueError('STOP_BAD_PLACE: actual monic coefficients')
    if rem(prescribed,PHI):
        raise ValueError('STOP_BAD_PLACE: factor')
    x=field([0,1]); v=x
    for i in range(1,DEGREE+1):
        v=fpow(v,P)
        if i<=DEGREE//2:
            a,b=trim(list(fa(v,fn(x)))),PHI
            while b:
                a,b=b,rem(a,b)
            if len(a)!=1:
                raise ValueError('STOP_BAD_PLACE: reducible')
    if v!=x:
        raise ValueError('STOP_BAD_PLACE: Frobenius')
    UNITS.clear(); DENOMINATORS.clear()


def fi(a,label):
    if not any(a):
        raise ValueError('STOP_BAD_INVERSE: '+label)
    b=fpow(a,P**DEGREE-2)
    if fm(a,b)!=field(1) or fm(b,a)!=field(1):
        raise ValueError('inverse product: '+label)
    if label in UNITS and UNITS[label]!=(a,b):
        raise ValueError('inverse label reused')
    UNITS[label]=(a,b)
    return b


def denominator(label,value):
    v=ground(value)
    if not v:
        raise ValueError('STOP_BAD_DENOMINATOR: '+label)
    inv=pow(v,-1,P)
    if v*inv%P!=1 or label in DENOMINATORS:
        raise ValueError('denominator registry')
    DENOMINATORS[label]=(v,inv)


class Poly(dict):
    def __init__(self,kind='band',terms=None):
        self.kind=kind
        super().__init__({} if terms is None else terms)


def kindof(*args):
    kinds={getattr(a,'kind','band') for a in args if any(e!=ZERO for e in a)}
    if len(kinds)>1:
        raise ValueError('typed polynomial mismatch')
    return next(iter(kinds)) if kinds else next((a.kind for a in args if isinstance(a,Poly)),'band')


def bounded(a):
    if len(a)>100000:
        raise ValueError('STOP_INTERNAL_TERM_CAP')
    signed={'band':(), 'raw':(), 'laurent_S':(5,), 'inverse':(6,), 'scale':(4,5), 'graph':()}
    if a.kind not in signed:
        raise ValueError('polynomial kind')
    for e in a:
        if len(e)!=7 or any(abs(v)>256 or (v<0 and i not in signed[a.kind]) for i,v in enumerate(e)):
            raise ValueError('typed exponent cap')
        if ((a.kind=='band' and e[5]) or (a.kind=='laurent_S' and e[6])
                or (a.kind=='graph' and any(e[4:]))):
            raise ValueError('typed variable support')
    return a


def retype(a,kind):
    return bounded(Poly(kind,a))


def const(c,kind='band'):
    if isinstance(c,(int,Q)):
        c=field(c)
    return Poly(kind,{} if not any(c) else {ZERO:c})


def var(i,kind='band'):
    e=list(ZERO);e[i]=1
    return Poly(kind,{tuple(e):field(1)})


def add(*args):
    r=Poly(kindof(*args))
    for a in args:
        for e,c in a.items():
            v=fa(r.get(e,field(0)),c)
            if any(v): r[e]=v
            else: r.pop(e,None)
        bounded(r)
    return r


def neg(a):
    return Poly(kindof(a),{e:fn(c) for e,c in a.items()})


def sub(a,b):
    return add(a,neg(b))


def mul(a,b):
    r=Poly(kindof(a,b))
    for e,c in a.items():
        for f,d in b.items():
            k=tuple(x+y for x,y in zip(e,f))
            v=fa(r.get(k,field(0)),fm(c,d))
            if any(v):r[k]=v
            else:r.pop(k,None)
            if len(r)>100000:raise ValueError('STOP_INTERNAL_TERM_CAP')
        bounded(r)
    return r


def scale(a,c):
    return mul(a,const(c,kindof(a)))


def power(a,n):
    if n<0:raise ValueError('negative polynomial power')
    r=const(1,kindof(a))
    while n:
        if n%2:r=mul(r,a)
        n//=2
        if n:a=mul(a,a)
    return r


def coeff(a,i,n):
    r=Poly(kindof(a))
    for e,c in a.items():
        if e[i]==n:
            f=list(e);f[i]=0;r[tuple(f)]=c
    return r


def diff(a,i):
    r=Poly(kindof(a))
    for e,c in a.items():
        if e[i]:
            f=list(e);f[i]-=1;value=fm(c,field(e[i]))
            if any(value):r[tuple(f)]=value
    return bounded(r)


def shift(a,i,n):
    r=Poly(kindof(a))
    for e,c in a.items():
        f=list(e);f[i]+=n;r[tuple(f)]=c
    return bounded(r)


def truncate(a,i,n):
    return Poly(kindof(a),{e:c for e,c in a.items() if e[i]<=n})


def series(a,alpha,n):
    equal(coeff(a,6,0),const(1),'series constant')
    v,term,out,binom=sub(a,const(1)),const(1),const(1),Q(1)
    for j in range(1,n+1):
        term=truncate(mul(term,v),6,n)
        binom=binom*(alpha-j+1)/j
        out=add(out,scale(term,binom))
    return out


def integrate(a):
    out=Poly(kindof(a))
    for e,c in a.items():
        f=list(e);f[6]+=1;out[tuple(f)]=fm(c,field(Q(1,f[6])))
    return bounded(out)


def scalar(a):
    if any(e!=ZERO for e in a):raise ValueError('parameter-dependent scalar node')
    return a.get(ZERO,field(0))


def equal(a,b,label):
    if a!=b:raise ValueError('construction identity: '+label)


def det3(a):
    v=field(0)
    for perm,sign in [((0,1,2),1),((1,2,0),1),((2,0,1),1),
                      ((0,2,1),-1),((2,1,0),-1),((1,0,2),-1)]:
        v=fa(v,fm(field(sign),fm(a[0][perm[0]],fm(a[1][perm[1]],a[2][perm[2]]))))
    return v


def invert_matrix(a,label):
    inv=fi(det3(a),label)
    out=[]
    for i in range(3):
        row=[]
        for j in range(3):
            rr=[k for k in range(3) if k!=j];cc=[k for k in range(3) if k!=i]
            minor=fa(fm(a[rr[0]][cc[0]],a[rr[1]][cc[1]]),fn(fm(a[rr[0]][cc[1]],a[rr[1]][cc[0]])))
            row.append(fm(inv,fn(minor) if (i+j)%2 else minor))
        out.append(row)
    for left,right in ((a,out),(out,a)):
        for i in range(3):
            for j in range(3):
                v=field(0)
                for k in range(3):v=fa(v,fm(left[i][k],right[k][j]))
                equal(v,field(int(i==j)),'two-sided matrix inverse')
    return out


def apply_matrix(a,v):
    return [add(*(scale(x,c) for c,x in zip(row,v))) for row in a]


def substitute_z(a,zeta):
    out=Poly('graph')
    for e,c in a.items():
        if e[5] or e[6]:raise ValueError('graph source variables')
        f=list(e);f[4]=0
        out=add(out,mul(Poly('graph',{tuple(f):c}),power(zeta,e[4])))
    return out


def wire_f(a):
    if len(a)!=DEGREE or any(v<0 or v>=P for v in a):raise ValueError('field wire')
    return [str(v) for v in a]


def wire_p(a,weight):
    global WIRE_TERMS
    WIRE_TERMS+=len(a)
    if len(a)>20000 or WIRE_TERMS>400000:raise ValueError('STOP_WIRE_TERM_CAP')
    for e,c in a.items():
        if (any(e[4:]) or any(v<0 for v in e) or not any(c)
                or sum((i+1)*e[i] for i in range(4))!=weight):
            raise ValueError('graph weight/support')
    return {'kind':'graph','terms':[[[str(v) for v in e[:4]],wire_f(c)] for e,c in sorted(a.items())]}
