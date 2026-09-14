"""Independent direct-residue arithmetic; STATIC, UNEXECUTED.

No producer imports. Typed sparse polynomials and direct monic reduction;
coefficient recurrence for fractional powers, Horner for the graph chart.
"""
from fractions import Fraction as Rational

PRIME = None
MODULUS = None
DEGREE = None
ORIGIN = (0, 0, 0, 0, 0, 0, 0)
KINDS = {'band', 'raw', 'laurent_S', 'inverse', 'scale', 'graph'}


class Stop(ValueError):
    pass


class Mismatch(ValueError):
    pass


def need(ok, label):
    if not ok:
        raise Stop(label)


def equal(a, b, label):
    if a != b:
        raise Mismatch(label)


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def qadd(a, b):
    out = [Rational(0)] * max(len(a), len(b))
    for i, v in enumerate(a): out[i] += v
    for i, v in enumerate(b): out[i] += v
    return trim(out)


def qmul(a, b):
    out = []
    for j, v in enumerate(b):
        out = qadd(out, [Rational(0)] * j + [v * u for u in a])
    return out


def ground(q):
    q = Rational(q)
    need(q.denominator % PRIME != 0, 'rational denominator')
    return q.numerator * pow(q.denominator % PRIME, -1, PRIME) % PRIME


def padd(a, b):
    out = [0] * max(len(a), len(b))
    for i, v in enumerate(a): out[i] += v
    for i, v in enumerate(b): out[i] += v
    return trim([v % PRIME for v in out])


def pmul(a, b):
    out = [0] * max(0, len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b): out[i+j] = (out[i+j] + u*v) % PRIME
    return trim(out)


def divide(a, b):
    a, b = trim([x % PRIME for x in a]), trim([x % PRIME for x in b])
    need(bool(b), 'zero ground polynomial divisor')
    q = [0] * max(0, len(a)-len(b)+1)
    bi = pow(b[-1], -1, PRIME)
    while len(a) >= len(b):
        j = len(a)-len(b); v = a[-1]*bi % PRIME; q[j] = v
        for i, u in enumerate(b): a[i+j] = (a[i+j]-v*u) % PRIME
        a = trim(a)
    return trim(q), a


def gcd(a, b):
    while b: a, b = b, divide(a, b)[1]
    return [(v*pow(a[-1], -1, PRIME)) % PRIME for v in a] if a else []


def modular_power(a, exponent, modulus):
    out = [1]; a = divide(a, modulus)[1]
    while exponent:
        if exponent & 1: out = divide(pmul(out, a), modulus)[1]
        a = divide(pmul(a, a), modulus)[1]; exponent >>= 1
    return out


def initialize(p, phi, septic):
    global PRIME, MODULUS, DEGREE
    need(type(p) is int and 2 <= p < 2147483648, 'prime range')
    need(p == 2 or p % 2 != 0, 'composite place')
    d = 3
    while d*d <= p:
        need(p % d != 0, 'composite place'); d += 2
    PRIME = p
    septic = [ground(v) for v in septic]
    need(2 <= len(phi) <= 8 and phi[-1] == 1 and all(type(v) is int and 0 <= v < p for v in phi), 'monic phi')
    f = len(phi)-1
    need(len(septic) == 8 and septic[-1] == 1 and divide(septic, phi)[1] == [], 'literal P7/phi relation')
    x = divide([0, 1], phi)[1]
    need(modular_power([0, 1], p**f, phi) == x, 'Frobenius degree condition')
    divisors = [ell for ell in (2, 3, 5, 7) if f % ell == 0]
    for ell in divisors:
        diff = padd(modular_power([0, 1], p**(f//ell), phi), [-v for v in x])
        need(gcd(phi, diff) == [1], 'irreducibility condition')
    MODULUS, DEGREE = tuple(phi), f


def F(v):
    if isinstance(v, (int, Rational)): v = [ground(v)]
    else: v = [ground(x) for x in v]
    for i in range(len(v)-1, DEGREE-1, -1):
        c = v[i]
        for j in range(DEGREE+1): v[i-DEGREE+j] = (v[i-DEGREE+j]-c*MODULUS[j]) % PRIME
    return tuple((v+[0]*DEGREE)[:DEGREE])


def fadd(a, b): return tuple((x+y) % PRIME for x,y in zip(a,b))
def fneg(a): return tuple((-x) % PRIME for x in a)
def fmul(a, b): return F(pmul(a,b))


def inverse(a):
    need(any(a), 'zero scalar inverse input')
    old, cur, u, v = list(MODULUS), trim(a), [], [1]
    while cur:
        q, rem = divide(old,cur)
        old, cur, u, v = cur, rem, v, padd(u, [-x for x in pmul(q,v)])
    need(len(old) == 1, 'nonunit scalar')
    ans = F([x*pow(old[0],-1,PRIME) % PRIME for x in u])
    need(fmul(a,ans) == fmul(ans,a) == F(1), 'two-sided scalar inverse product')
    return ans


class Poly(dict):
    def __init__(self, kind, terms=None):
        need(kind in KINDS, 'polynomial kind')
        self.kind = kind
        super().__init__({} if terms is None else terms)
        bounded(self)

    def __eq__(self, other):
        return isinstance(other, Poly) and self.kind == other.kind and dict.__eq__(self, other)

    def __ne__(self, other): return not self == other


def bounded(p):
    need(len(p) <= 100000, 'internal term cap')
    signed = {'laurent_S': {5}, 'inverse': {6}, 'scale': {4,5}}.get(p.kind, set())
    for ex,v in p.items():
        need(len(ex) == 7 and all(type(k) is int and abs(k) <= 256 for k in ex), 'internal exponent cap')
        need(all(k >= 0 or j in signed for j,k in enumerate(ex)), 'typed signed exponent')
        need(len(v) == DEGREE and any(v) and all(type(x) is int and 0 <= x < PRIME for x in v),
             'internal dense nonzero scalar')
        if p.kind == 'band': need(ex[5] == 0, 'band is S-free')
        if p.kind == 'laurent_S': need(ex[6] == 0, 'auxiliary theta-free')
        if p.kind == 'graph': need(ex[4:] == (0,0,0), 'graph only X variables')
    return p


def zero(kind='band'): return Poly(kind)
def constant(v, kind='band'):
    v = F(v) if isinstance(v,(int,Rational)) else tuple(v)
    return Poly(kind, {ORIGIN:v} if any(v) else {})


def symbol(j, kind='band'):
    return Poly(kind, {tuple(int(k == j) for k in range(7)): F(1)})


def cast(p, kind):
    # Only explicit source-stage reindex may change the coordinate type.
    return Poly(kind, dict(p))


def add(*ps):
    need(bool(ps) and len({p.kind for p in ps}) == 1, 'sum type')
    out = Poly(ps[0].kind)
    for p in ps:
        for ex,v in p.items():
            val = fadd(out.get(ex,F(0)),v)
            if any(val): out[ex] = val
            else: out.pop(ex,None)
            need(len(out) <= 100000, 'internal sum term cap')
        bounded(out)
    return out


def neg(p): return Poly(p.kind,{ex:fneg(v) for ex,v in p.items()})
def sub(a,b): return add(a,neg(b))


def mul(a,b):
    need(a.kind == b.kind, 'product type')
    out = Poly(a.kind)
    for ea,va in a.items():
        for eb,vb in b.items():
            ex = tuple(x+y for x,y in zip(ea,eb)); v = fadd(out.get(ex,F(0)),fmul(va,vb))
            if any(v): out[ex] = v
            else: out.pop(ex,None)
            need(len(out) <= 100000, 'internal product term cap')
        bounded(out)
    return out


def scale(p,v): return mul(p,constant(v,p.kind))


def power(p,n):
    need(type(n) is int and 0 <= n <= 256, 'nonnegative power')
    out = constant(1,p.kind)
    for _ in range(n): out = mul(out,p)
    return out


def derivative(p,j):
    out = {}
    for ex,v in p.items():
        if ex[j]:
            key = list(ex); key[j] -= 1; w = fmul(v,F(ex[j]))
            if any(w): out[tuple(key)] = w
    return Poly(p.kind,out)


def extract(p,j,n):
    out = {}
    for ex,v in p.items():
        if ex[j] == n:
            key = list(ex); key[j] = 0; out[tuple(key)] = v
    return Poly(p.kind,out)


def move(p,j,n):
    out = {}
    for ex,v in p.items():
        key = list(ex); key[j] += n; out[tuple(key)] = v
    return Poly(p.kind,out)


def scalar(p):
    need(all(ex == ORIGIN for ex in p), 'statically leading scalar node')
    return p.get(ORIGIN,F(0))


def series(c,alpha,n):
    need(c.kind == 'band' and 0 <= n <= 7, 'finite scalar series type/range')
    cs = [scalar(extract(c,6,i)) for i in range(4)]
    equal(cs[0],F(1),'series constant1')
    fs = [F(1)]
    for k in range(1,n+1):
        val = F(0)
        for i in range(1,min(3,k)+1):
            fac = F((alpha*i-(k-i))/k)
            val = fadd(val,fmul(fac,fmul(cs[i],fs[k-i])))
        fs.append(val)
    return add(*(move(constant(v),6,j) for j,v in enumerate(fs)))


def primitive(p):
    need(p.kind == 'band', 'critical integration type')
    out = {}
    for ex,v in p.items():
        key = list(ex); key[6] += 1
        need(1 <= key[6] <= 8, 'critical integration bound')
        out[tuple(key)] = fmul(v,F(Rational(1,key[6])))
    return Poly('band',out)


def graph_substitute(p,zeta):
    need(p.kind == 'band' and zeta.kind == 'graph' and all(e[5:] == (0,0) for e in p), 'graph input type')
    out = zero('graph')
    for k in range(max((e[4] for e in p),default=0),-1,-1):
        out = add(mul(out,zeta),cast(extract(p,4,k),'graph'))
    return out
