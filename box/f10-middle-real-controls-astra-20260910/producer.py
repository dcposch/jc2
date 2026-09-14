"""Prospective exact certificate producer. STATIC/UNEXECUTED."""
import argparse
import sys
import authority

F = None
COMB = None
MAX_TERMS = 20000
MAX_BITS = 12000
C0 = 10080
SCHEMA = 'f10-middle-real-certificate/v1'
BOUNDS = {'R_total': '40', 'R_alpha': '21', 'U_total': '32', 'U_V': '4',
          'W_total': '35', 'W_V': '6', 'rectangle_t': '40', 'rectangle_s': '21'}

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
    t, a, v = (var(i) for i in range(3))
    nu = 2 - t
    D = 12*v**2 - 12*(1-t)*v + (1+t)*(2-3*t)
    K = -840*v**3 + 840*(1-t**2)*v**2 + 42*(1+t)*(2+t)*(4*t-3)*v + 2*(2-3*t)*(1+t)*(2+t)*(3+t)
    gamma = t*((1+t)*(2+t)*(3+t)-30*(1+t)*(2+t)*v+180*(1+t)*v**2-120*v**3)
    sigma, pi = a+nu, a*nu
    A = sigma-7
    B2 = sigma**2-pi-12*sigma+47
    B3 = sigma**3-2*sigma*pi-18*(sigma**2-pi)+119*sigma-342
    bigP = 840*v**3+420*A*v**2+42*B2*v+B3
    S = 2*K**2-140*t*(1+t-6*v)*K*D+245*gamma*D**2
    T = D*bigP-(12*v+A)*K
    return S, T

def cofactors(matrix):
    # For mask size k: determinant of rows 1..k, ordered mask columns.
    import itertools
    states = {0: P(1)}
    for k in range(1, 9):
        fresh = {}
        for cols in itertools.combinations(range(9), k):
            mask = sum(1 << c for c in cols)
            value = P()
            for position, col in enumerate(cols):
                term = matrix[k][col] * states[mask ^ (1 << col)]
                value = value + (term if (k-1+position) % 2 == 0 else -term)
            fresh[mask] = value
        states = fresh
    full = (1 << 9)-1
    co = [states[full ^ (1 << j)].scale(-1 if j % 2 else 1) for j in range(9)]
    determinant = sum((matrix[0][j]*co[j] for j in range(9)), P())
    return determinant, co

def rectangle(poly):
    t, s = var(0), var(1)
    tp, ap = (6+t).scale(F(1, 21)), (45-3*t+7*t*s).scale(F(1, 21))
    powers_t = [P(1)]
    powers_a = [P(1)]
    for _ in range(40):
        powers_t.append(powers_t[-1]*tp)
    for _ in range(21):
        powers_a.append(powers_a[-1]*ap)
    out = P()
    for (i, j, k), coefficient in poly.d.items():
        if k or i+j > 40 or j > 21:
            raise ValueError('R degree envelope')
        out = out + (powers_t[i]*powers_a[j]).scale(coefficient)
    return out.scale(F(21**40))

def at_one(poly):
    out = P()
    for (i, j, k), value in poly.d.items():
        out = out + P({(0, j, k): value})
    return out

def remove_edge(poly):
    exponent = 0
    if poly.zero():
        raise ValueError('zero determinant')
    while at_one(poly).zero():
        degree = max(e[0] for e in poly.d)
        if degree == 0 or exponent >= 40:
            raise ValueError('edge factor bound')
        # a_i=b_i-b_(i-1): exact division by (1-t), ascending.
        coeffs = [poly.coeff(0, i) for i in range(degree+1)]
        cumulative, quotient = P(), P()
        for i in range(degree):
            cumulative = cumulative + coeffs[i]
            quotient = quotient + cumulative*var(0)**i
        if not (coeffs[degree]+cumulative).zero():
            raise ValueError('edge division residual')
        poly = quotient
        exponent += 1
    return exponent, poly

def qwire(value):
    value = F(value)
    return [str(value.numerator), str(value.denominator)]

def wire(poly):
    return [[[str(k) for k in e], qwire(value)] for e, value in sorted(poly.d.items())]

def build():
    S, T = sources()
    if T.coeff(2, 5).d != P(C0).d:
        raise ValueError('fixed leading coefficient')
    rem, quotient = S, P()
    for power in (2, 1, 0):
        q = rem.coeff(2, power+5).scale(F(1, C0))
        term = q*var(2)**power
        quotient = quotient+term
        rem = rem-term*T
    if any(e[2] > 4 for e in rem.d):
        raise ValueError('division V remainder')
    integer_rem = rem.scale(F(C0**3))
    if any(q.denominator != 1 for q in integer_rem.d.values()):
        raise ValueError('integerized remainder')
    columns = [integer_rem*var(2)**i for i in range(5)] + [T*var(2)**j for j in range(4)]
    matrix = [[column.coeff(2, row) for column in columns] for row in range(9)]
    R, co = cofactors(matrix)
    AA = sum((co[i]*var(2)**i for i in range(5)), P())
    BB = sum((co[5+j]*var(2)**j for j in range(4)), P())
    U = AA.scale(F(C0**3))
    Wcof = BB-U*quotient
    for obj in (R, U, Wcof):
        if any(q.denominator != 1 for q in obj.d.values()):
            raise ValueError('nonintegral reconstructed cofactor')
    hat = rectangle(R)
    j, reduced = remove_edge(hat)
    if j < 1:
        raise ValueError('missing excluded-edge factor')
    endpoint = hat.d.get((0, 0, 0), F(0))
    epsilon = 1 if endpoint > 0 else -1 if endpoint < 0 else 0
    degree = 40-j
    bern = []
    if epsilon:
        G = reduced.scale(F(epsilon))
        for i in range(degree+1):
            row = []
            for jj in range(22):
                value = F(0)
                for (k, l, v), coefficient in G.d.items():
                    if v or k > degree or l > 21:
                        raise ValueError('Bernstein degree envelope')
                    if k <= i and l <= jj:
                        value += coefficient*F(COMB(i, k), COMB(degree, k))*F(COMB(jj, l), COMB(21, l))
                row.append(value)
            bern.append(row)
    reason = 'fixed certificate candidate'
    if not epsilon:
        reason = 'zero endpoint'
    elif any(x < 0 for row in bern for x in row):
        reason = 'negative Bernstein coefficient'
    elif any(x != abs(endpoint) for x in bern[0]):
        reason = 'collapsed-edge row mismatch'
    elif bern[0][0] <= 0 or bern[0][21] <= 0:
        reason = 'zero endpoint'
    return {'schema': SCHEMA, 'status': 'CANDIDATE' if reason == 'fixed certificate candidate' else 'INCONCLUSIVE',
            'reason': reason, 'science': authority.SCIENCE, 'code': authority.code_pins(),
            'variables': ['tau', 'alpha', 'V'], 'bounds': BOUNDS,
            'polynomials': {name: wire(obj) for name, obj in
                            [('Qdiv', quotient), ('Frem', rem), ('R', R), ('U', U), ('Wcof', Wcof)]},
            'j': str(j), 'epsilon': str(epsilon),
            'bernstein': {'degree_t': str(degree), 'degree_s': '21',
                          'coefficients': [[qwire(x) for x in row] for row in bern]}}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--job', required=True)
    parser.add_argument('--registration', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    permit = authority.authorize('produce', args.job, args.registration, [args.output])
    global F, COMB
    from fractions import Fraction
    from math import comb
    F, COMB = Fraction, comb
    try:
        artifact = build()
        authority.postcheck(permit)
        sha, size = authority.emit(args.output, artifact, authority.LIMIT-authority.RECEIPT_LIMIT)
        print('PRODUCER_' + artifact['status'] + ' sha256=' + sha + ' bytes=' + str(size))
        return 0 if artifact['status'] == 'CANDIDATE' else 2
    except (ValueError, ArithmeticError, MemoryError, OSError) as exc:
        print('INCONCLUSIVE: ' + str(exc)[:400], file=sys.stderr)
        return 2

if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, TypeError, KeyError, RuntimeError, OSError) as exc:
        print('INCONCLUSIVE: ' + str(exc)[:400], file=sys.stderr)
        raise SystemExit(2)
