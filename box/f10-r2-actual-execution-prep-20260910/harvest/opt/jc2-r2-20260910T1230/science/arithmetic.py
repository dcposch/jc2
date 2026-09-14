"""Producer-only exact arithmetic. STATIC / UNEXECUTED. No solver."""
from fractions import Fraction as Q


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def qa(a, b):
    return trim([(a[i] if i < len(a) else Q(0)) +
                 (b[i] if i < len(b) else Q(0))
                 for i in range(max(len(a), len(b)))])


def qs(a, c):
    return trim([x * c for x in a])


def qm(a, b):
    c = [Q(0)] * max(0, len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def qdiv(a, b):
    a, b = trim([Q(x) for x in a]), trim([Q(x) for x in b])
    if not b:
        raise ValueError('zero rational-polynomial divisor')
    q = [Q(0)] * max(0, len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        k, c = len(a) - len(b), a[-1] / b[-1]
        q[k] += c
        a = qa(a, [Q(0)] * k + qs(b, -c))
    return trim(q), a


def xgcd(a, b):
    r, t, u, v = [Q(1)], [], [], [Q(1)]
    while b:
        q, rem = qdiv(a, b)
        a, b = b, rem
        r, u = u, qa(r, qs(qm(q, u), -1))
        t, v = v, qa(t, qs(qm(q, v), -1))
    if not a:
        return [], [], []
    c = Q(1) / a[-1]
    return qs(a, c), qs(r, c), qs(t, c)


P7 = None
UNITS = {}


def field(a):
    if isinstance(a, (int, Q)):
        a = [Q(a)]
    r = qdiv([Q(x) for x in a], P7)[1]
    return tuple(r + [Q(0)] * (7 - len(r)))


def fa(a, b):
    return tuple(x + y for x, y in zip(a, b))


def fm(a, b):
    return field(qm(a, b))


def fn(a):
    return tuple(-x for x in a)


def fi(a, label):
    g, _, v = xgcd(P7, trim(a))
    if g != [Q(1)]:
        raise ValueError('nonunit: ' + label)
    b = field(v)
    if fm(a, b) != field(1):
        raise ValueError('Euclid product')
    if label in UNITS and UNITS[label] != (a, b):
        raise ValueError('witness label reused')
    UNITS[label] = (a, b)
    return b


ZERO = (0, 0, 0, 0, 0, 0)


def const(a):
    if isinstance(a, (int, Q)):
        a = field(a)
    return {} if not any(a) else {ZERO: a}


def var(i):
    e = list(ZERO)
    e[i] = 1
    return {tuple(e): field(1)}


def add(*aa):
    r = {}
    for a in aa:
        for e, c in a.items():
            d = fa(r.get(e, field(0)), c)
            if any(d):
                r[e] = d
            else:
                r.pop(e, None)
    return r


def neg(a):
    return {e: fn(c) for e, c in a.items()}


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    r = {}
    for e, c in a.items():
        for f, d in b.items():
            k = tuple(x + y for x, y in zip(e, f))
            val = fa(r.get(k, field(0)), fm(c, d))
            if any(val):
                r[k] = val
            else:
                r.pop(k, None)
    return r


def scale(a, c):
    return mul(a, const(c))


def power(a, n):
    r = const(1)
    while n:
        if n % 2:
            r = mul(r, a)
        a, n = mul(a, a), n // 2
    return r


def diff(a, i):
    r = {}
    for e, c in a.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            r[tuple(f)] = fm(c, field(e[i]))
    return r


def coeff(a, i, n):
    r = {}
    for e, c in a.items():
        if e[i] == n:
            f = list(e)
            f[i] = 0
            r[tuple(f)] = c
    return r


def shift(a, i, n):
    r = {}
    for e, c in a.items():
        f = list(e)
        f[i] += n
        if f[i] < 0:
            raise ValueError('nonpolynomial division')
        r[tuple(f)] = c
    return r


def truncate(a, i, n):
    return {e: c for e, c in a.items() if e[i] <= n}


def series(a, exponent, n):
    if coeff(a, 5, 0) != const(1):
        raise ValueError('series constant is not one')
    v, term, r, binom = sub(a, const(1)), const(1), const(1), Q(1)
    for j in range(1, n + 1):
        term = truncate(mul(term, v), 5, n)
        binom = binom * (exponent - j + 1) / j
        r = add(r, scale(term, binom))
    return r


def integrate(a):
    return {tuple(list(e[:5]) + [e[5] + 1]):
            fm(c, field(Q(1, e[5] + 1))) for e, c in a.items()}


def scalar(a):
    if any(e != ZERO for e in a):
        raise ValueError('parameter-dependent scalar inversion forbidden')
    return a.get(ZERO, field(0))


def invert_matrix(matrix, label):
    n = len(matrix)
    a = [list(row) + [field(int(i == j)) for j in range(n)]
         for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if any(a[i][j])), None)
        if pivot is None:
            raise ValueError('singular band matrix')
        a[j], a[pivot] = a[pivot], a[j]
        inv = fi(a[j][j], label + ':' + str(j))
        a[j] = [fm(x, inv) for x in a[j]]
        for i in range(n):
            if i != j:
                c = a[i][j]
                a[i] = [fa(x, fn(fm(c, y))) for x, y in zip(a[i], a[j])]
    result = [row[n:] for row in a]
    for left, right in ((matrix, result), (result, matrix)):
        for i in range(n):
            for j in range(n):
                s = field(0)
                for k in range(n):
                    s = fa(s, fm(left[i][k], right[k][j]))
                if s != field(int(i == j)):
                    raise ValueError('matrix inverse readback')
    return result


def apply_matrix(m, v):
    return [add(*(scale(x, c) for c, x in zip(row, v))) for row in m]


def completion(c1, c0):
    g, _, v = xgcd(P7, trim(c1))
    h, u, w = xgcd(g, trim(c0))
    if h != [Q(1)]:
        raise ValueError('column not unimodular')
    l1, l0 = field(qm(u, v)), field(w)
    if fa(fm(l1, c1), fm(l0, c0)) != field(1):
        raise ValueError('column completion')
    return l1, l0


def equal(a, b, label):
    if a != b:
        raise ValueError('identity: ' + label)


def wire_q(a):
    numerator, denominator = str(a.numerator), str(a.denominator)
    if len(numerator) > 4096 or len(denominator) > 4096:
        raise ValueError('coefficient decimal bound')
    return numerator + '/' + denominator


def wire_f(a):
    return [wire_q(x) for x in a]


WIRE_TERMS = 0


def wire_p(a):
    global WIRE_TERMS
    WIRE_TERMS += len(a)
    if len(a) > 4096 or WIRE_TERMS > 50000:
        raise ValueError('wire term bound')
    if any(len(e) != 6 or any(x < 0 or x > 16 for x in e) for e in a):
        raise ValueError('wire exponent bound')
    return [[[str(x) for x in e], wire_f(c)] for e, c in sorted(a.items())]
