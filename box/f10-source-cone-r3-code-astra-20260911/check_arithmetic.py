"""Independent checker mathematics. No producer or producer arithmetic import."""
from fractions import Fraction as Rational

MODULUS = None
ORIGIN = (0, 0, 0, 0, 0, 0, 0)


def clean(v):
    v = list(v)
    while v and v[-1] == 0:
        del v[-1]
    return v


def plus(a, b):
    r = [Rational(0) for _ in range(max(len(a), len(b)))]
    for i in range(len(a)):
        r[i] += a[i]
    for i in range(len(b)):
        r[i] += b[i]
    return clean(r)


def times(a, b):
    result = []
    for j, q in enumerate(b):
        result = plus(result, [Rational(0)] * j + [q * p for p in a])
    return result


def quotient(a, b):
    r, divisor = clean([Rational(v) for v in a]), clean([Rational(v) for v in b])
    if not divisor:
        raise ValueError('zero rational divisor')
    q = [Rational(0)] * max(0, len(r) - len(divisor) + 1)
    for k in range(len(q) - 1, -1, -1):
        if len(r) == len(divisor) + k:
            c = r[-1] / divisor[-1]
            q[k] = c
            for j in range(len(divisor)):
                r[j + k] -= c * divisor[j]
            r = clean(r)
    return clean(q), r


def bezout(a, b):
    oldr, r = clean(a), clean(b)
    olds, s, oldt, t = [Rational(1)], [], [], [Rational(1)]
    while r:
        q, rem = quotient(oldr, r)
        oldr, r = r, rem
        olds, s = s, plus(olds, [-v for v in times(q, s)])
        oldt, t = t, plus(oldt, [-v for v in times(q, t)])
    if not oldr:
        return [], [], []
    k = oldr[-1]
    return [v / k for v in oldr], [v / k for v in olds], [v / k for v in oldt]


def F(v):
    if isinstance(v, (int, Rational)):
        v = [Rational(v)]
    r = [Rational(q) for q in v]
    for i in range(len(r) - 1, 6, -1):
        q = r[i]
        for j in range(8):
            r[i - 7 + j] -= q * MODULUS[j]
    return tuple((r + [Rational(0)] * 7)[:7])


def fsum(a, b):
    return tuple(a[j] + b[j] for j in range(7))


def fnegative(a):
    return tuple(-q for q in a)


def fproduct(a, b):
    return F(times(a, b))


def inverse(v):
    g, _, cofactor = bezout(MODULUS, v)
    if g != [Rational(1)]:
        raise ValueError('independent whole-algebra nonunit')
    inv = F(cofactor)
    if fproduct(v, inv) != F(1):
        raise ValueError('independent inverse product')
    return inv


def constant(v):
    if isinstance(v, (int, Rational)):
        v = F(v)
    return {ORIGIN: v} if any(v) else {}


def symbol(j):
    return {tuple(1 if k == j else 0 for k in range(7)): F(1)}


def bounded(p):
    if len(p) > 100000:
        raise ValueError('independent internal term cap')
    return p


def sum_poly(*ps):
    out = {}
    for p in ps:
        for ex, v in p.items():
            val = fsum(out.get(ex, F(0)), v)
            if any(val):
                out[ex] = val
            elif ex in out:
                del out[ex]
        bounded(out)
    return out


def negative(p):
    return {ex: fnegative(v) for ex, v in p.items()}


def minus(a, b):
    return sum_poly(a, negative(b))


def product(a, b):
    buckets = {}
    for ex, x in a.items():
        for ey, y in b.items():
            key = tuple(ex[j] + ey[j] for j in range(7))
            val = fsum(buckets.get(key, F(0)), fproduct(x, y))
            if any(val):
                buckets[key] = val
            else:
                buckets.pop(key, None)
        bounded(buckets)
    return buckets


def multiply_scalar(a, v):
    return product(a, constant(v))


def exponent(a, n):
    if n < 0:
        raise ValueError('negative exponent')
    p = constant(1)
    for _ in range(n):
        p = product(p, a)
    return p


def derivative(p, j):
    out = {}
    for ex, val in p.items():
        if ex[j]:
            key = list(ex)
            key[j] -= 1
            out[tuple(key)] = tuple(c * ex[j] for c in val)
    return out


def extract(p, j, n):
    out = {}
    for ex, val in p.items():
        if ex[j] == n:
            key = list(ex)
            key[j] = 0
            out[tuple(key)] = val
    return out


def move(p, j, n, laurent=False):
    out = {}
    for ex, val in p.items():
        key = list(ex)
        key[j] += n
        if key[j] < 0 and not laurent:
            raise ValueError('nonpolynomial quotient')
        out[tuple(key)] = val
    return out


def value(p):
    if any(ex != ORIGIN for ex in p):
        raise ValueError('expected complete-B constant')
    return p.get(ORIGIN, F(0))


def fractional_series(c, alpha, n):
    # c*f'=alpha*c'*f, distinct from producer binomial expansion.
    cs = [value(extract(c, 6, i)) for i in range(4)]
    if cs[0] != F(1):
        raise ValueError('series normalization')
    fs = [F(1)]
    for k in range(1, n + 1):
        val = F(0)
        for i in range(1, min(3, k) + 1):
            fac = (alpha * i - (k - i)) / k
            val = fsum(val, fproduct(F(fac), fproduct(cs[i], fs[k - i])))
        fs.append(val)
    return sum_poly(*(move(constant(v), 6, i) for i, v in enumerate(fs)))


def primitive(p):
    out = {}
    for ex, v in p.items():
        key = list(ex)
        key[6] += 1
        out[tuple(key)] = tuple(q / key[6] for q in v)
    return out


def substitute_graph(p, zeta):
    out = {}
    for i in range(max((e[4] for e in p), default=0), -1, -1):
        out = sum_poly(product(out, zeta), extract(p, 4, i))
    return out


def require(a, b, label):
    if a != b:
        raise ValueError('CHECK FAILED: ' + label)
