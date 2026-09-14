"""Fixed contact Gram producer. STATIC/UNEXECUTED; authorize before arithmetic."""
import argparse
import sys
import authority

F = None
COMB = None
GCD = None
MAX_TERMS = 20000
MAX_BITS = 12000
SCHEMA = 'f10-contact-gram-certificate/v1'
BOUNDS = {'R_weight': '52', 'cofactor_weight': '64', 'U0_V': '3',
          'U1_V': '3', 'Uphi_V': '5', 'rectangle_t': '52', 'rectangle_v': '52'}

class P:
    def __init__(self, data=0):
        if F is None:
            raise RuntimeError('authorize before arithmetic')
        if isinstance(data, P):
            data = data.d
        elif not isinstance(data, dict):
            data = {(0, 0, 0): F(data)} if data else {}
        self.d = {e: F(v) for e, v in data.items() if v}
        self.bound()

    def bound(self):
        if len(self.d) > MAX_TERMS:
            raise ValueError('internal term cap')
        for e, v in self.d.items():
            if len(e) != 3 or min(e) < 0 or max(e) > 100:
                raise ValueError('internal exponent cap')
            if max(abs(v.numerator).bit_length(), v.denominator.bit_length()) > MAX_BITS:
                raise ValueError('internal coefficient bit cap')

    def __add__(self, other):
        other = P(other)
        out = dict(self.d)
        for e, v in other.d.items():
            out[e] = out.get(e, F(0)) + v
            if not out[e]:
                del out[e]
        return P(out)
    __radd__ = __add__

    def __neg__(self):
        return P({e: -v for e, v in self.d.items()})

    def __sub__(self, other):
        return self + -P(other)

    def __rsub__(self, other):
        return P(other) + -self

    def __mul__(self, other):
        other = P(other)
        out = {}
        for a, x in self.d.items():
            for b, y in other.d.items():
                e = tuple(a[i] + b[i] for i in range(3))
                out[e] = out.get(e, F(0)) + x * y
                if not out[e]:
                    del out[e]
                if len(out) > MAX_TERMS:
                    raise ValueError('internal term cap')
        return P(out)
    __rmul__ = __mul__

    def __pow__(self, n):
        if type(n) is not int or n < 0 or n > 100:
            raise ValueError('power bound')
        ans, base = P(1), self
        while n:
            if n & 1:
                ans = ans * base
            n //= 2
            if n:
                base = base * base
        return ans

    def scale(self, x):
        return P({e: v * x for e, v in self.d.items()})

    def coeff(self, axis, degree):
        out = {}
        for e, v in self.d.items():
            if e[axis] == degree:
                z = list(e)
                z[axis] = 0
                out[tuple(z)] = v
        return P(out)

    def zero(self):
        return not self.d

def var(axis):
    e = [0, 0, 0]
    e[axis] = 1
    return P({tuple(e): F(1)})


def sources():
    s, p, v = (var(i) for i in range(3))
    d = 210*(s-3)
    K = p-(s-3)*(s-4)
    D0 = (-5*s**3+62*s**2-259*s+394+(10*s-62)*p).scale(F(1, 2))
    N = 420*v**3-210*(s-1)*v**2+63*K*v+D0
    A = 120*v**3+180*(s-5)*v**2+30*(s**2-p-9*s+26)*v+s**3-2*s*p-14*(s**2-p)+71*s-154
    phi = (d*A+120*(s-5+6*v)*N).scale(F(1, 302400))
    fa0 = p**2-s**2*p-(30*v-14)*s*p-(71-270*v+180*v**2)*p+120-720*v+1080*v**2-240*v**3
    q0 = d**2*fa0+d*(-120*p+720-1440*v)*N+360*N**2
    I0 = -840*v**3+840*(p-3)*v**2+42*((4*s-33)*p+60)*v-6*p**2+(6*s**2-80*s+378)*p-480
    q1 = d*I0+630*(p-4+4*v+4*v**2)*N
    return phi, q0, q1

def divide(poly, phi):
    if phi.coeff(2, 4).d != P(1).d or any(e[2] > 4 for e in phi.d):
        raise ValueError('monic quartic required')
    quotient, remainder = P(), poly
    for k in range(max((e[2] for e in remainder.d), default=-1), 3, -1):
        term = remainder.coeff(2, k)*var(2)**(k-4)
        quotient = quotient+term
        remainder = remainder-term*phi
    if any(e[2] >= 4 for e in remainder.d):
        raise ValueError('monic division residual')
    return quotient, remainder

def primitive(column):
    # One fixed positive rational CONSTANT scaling per whole column.
    den = 1
    for entry in column:
        for x in entry.d.values():
            den = den//GCD(den, x.denominator)*x.denominator
    content = 0
    for entry in column:
        for x in entry.d.values():
            content = GCD(content, abs(x.numerator*(den//x.denominator)))
    c = F(den, content) if content else F(1)
    return c, [entry.scale(c) for entry in column]

def det(matrix):
    # Fixed size <=4 Laplace expansion, no parameter division.
    if not matrix:
        return P(1)
    out = P()
    for j, entry in enumerate(matrix[0]):
        minor = [[row[k] for k in range(len(matrix)) if k != j] for row in matrix[1:]]
        out = out+entry*det(minor).scale(-1 if j % 2 else 1)
    return out

def rectangle(poly):
    t, v = var(0), var(1)
    a = (6+t).scale(F(1, 21))
    b = (3-3*t+7*t*v).scale(F(1, 21))
    s = 4-a-b
    p = 4-2*(a+b)+a*b
    sp, pp = [P(1)], [P(1)]
    for _ in range(52):
        sp.append(sp[-1]*s)
    for _ in range(26):
        pp.append(pp[-1]*p)
    out = P()
    for (i, j, k), c in poly.d.items():
        if k or i+2*j > 52:
            raise ValueError('R weight envelope')
        out = out+(sp[i]*pp[j]).scale(c)
    out = out.scale(F(21**52))
    if any(e[0] > 52 or e[1] > 52 or e[2] for e in out.d):
        raise ValueError('rectangle bidegree envelope')
    return out

def remove_edge(poly):
    count = 0
    if poly.zero():
        raise ValueError('zero R polynomial')
    while True:
        at_one = P()
        for (i, j, k), c in poly.d.items():
            at_one = at_one+P({(0, j, k): c})
        if not at_one.zero():
            return count, poly
        degree = max(e[0] for e in poly.d)
        if degree < 1 or count >= 52:
            raise ValueError('edge factor bound')
        cumulative, quotient = P(), P()
        for i in range(degree):
            cumulative = cumulative+poly.coeff(0, i)
            quotient = quotient+cumulative*var(0)**i
        if not (poly.coeff(0, degree)+cumulative).zero():
            raise ValueError('edge division residual')
        poly = quotient
        count += 1

def bernstein(poly, n):
    # Two separable power-to-Bernstein conversions at ONE fixed degree.
    if any(e[0] > n or e[1] > 52 or e[2] for e in poly.d):
        raise ValueError('reduced rectangle envelope')
    temp = [[F(0) for _ in range(53)] for _ in range(n+1)]
    for (k, l, _), c in poly.d.items():
        for i in range(k, n+1):
            temp[i][l] += c*F(COMB(i, k), COMB(n, k))
    ans = [[F(0) for _ in range(53)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(53):
            ans[i][j] = sum((temp[i][l]*F(COMB(j, l), COMB(52, l)) for l in range(j+1)), F(0))
    return ans

def qwire(c):
    c = F(c)
    if max(abs(c.numerator).bit_length(), c.denominator.bit_length()) > MAX_BITS:
        raise ValueError('wire coefficient bit cap')
    return [str(c.numerator), str(c.denominator)]

def wire(poly):
    return [[[str(k) for k in e], qwire(c)] for e, c in sorted(poly.d.items())]

def build():
    phi, q0, q1 = sources()
    cols = []
    scales = []
    for q in (q0, q1):
        for j in range(4):
            _, remainder = divide(q*var(2)**j, phi)
            c, col = primitive([remainder.coeff(2, i) for i in range(4)])
            scales.append(c)
            cols.append(col)
    B = [[cols[j][i] for j in range(8)] for i in range(4)]
    G = [[sum((B[i][k]*B[j][k] for k in range(8)), P()) for j in range(4)] for i in range(4)]
    h = [det([[G[row][col] for col in range(4) if col != i] for row in range(1, 4)]).scale(-1 if i % 2 else 1) for i in range(4)]
    R = sum((G[0][i]*h[i] for i in range(4)), P())
    z = [sum((B[i][j]*h[i] for i in range(4)), P()).scale(scales[j]) for j in range(8)]
    u0 = sum((z[j]*var(2)**j for j in range(4)), P())
    u1 = sum((z[4+j]*var(2)**j for j in range(4)), P())
    uphi, rem = divide(R-u0*q0-u1*q1, phi)
    if not rem.zero():
        raise ValueError('full cofactor identity')
    objects = {'R': R, 'U0': u0, 'U1': u1, 'Uphi': uphi}
    for name, poly in objects.items():
        vd = {'R': 0, 'U0': 3, 'U1': 3, 'Uphi': 5}[name]
        weight = 52 if name == 'R' else 64
        if any(e[0]+2*e[1]+e[2] > weight or e[2] > vd for e in poly.d):
            raise ValueError('cofactor weight or V envelope')
    hat = rectangle(R)
    j, reduced = remove_edge(hat)
    values = bernstein(reduced, 52-j)
    endpoint = hat.d.get((0, 0, 0), F(0))
    reason = 'fixed certificate candidate'
    if any(x != endpoint for x in values[0]):
        reason = 'collapsed edge not constant'
    elif endpoint <= 0:
        reason = 'nonpositive endpoint'
    elif any(x < 0 for row in values for x in row):
        reason = 'negative Bernstein coefficient'
    return {'schema': SCHEMA, 'status': 'CANDIDATE' if reason == 'fixed certificate candidate' else 'INCONCLUSIVE',
            'reason': reason, 'science': authority.SCIENCE, 'code': authority.code_pins(),
            'variables': ['s', 'p', 'V'], 'bounds': BOUNDS,
            'polynomials': {name: wire(poly) for name, poly in objects.items()},
            'j': str(j), 'bernstein': {'degree_t': str(52-j), 'degree_v': '52',
            'coefficients': [[qwire(x) for x in row] for row in values]}}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--job', required=True)
    parser.add_argument('--registration', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    permit = authority.authorize('produce', args.job, args.registration, [args.output])
    global F, COMB, GCD
    from fractions import Fraction
    from math import comb, gcd
    F, COMB, GCD = Fraction, comb, gcd
    artifact = build()
    authority.postcheck(permit)
    sha, size = authority.emit(args.output, artifact, authority.LIMIT-authority.RECEIPT_LIMIT)
    print('PRODUCER_' + artifact['status'] + ' sha256=' + sha + ' bytes=' + str(size))
    return 0 if artifact['status'] == 'CANDIDATE' else 2

if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, TypeError, KeyError, RuntimeError, RecursionError, ArithmeticError, MemoryError, OSError) as exc:
        print('INCONCLUSIVE: ' + str(exc)[:400], file=sys.stderr)
        raise SystemExit(2)
