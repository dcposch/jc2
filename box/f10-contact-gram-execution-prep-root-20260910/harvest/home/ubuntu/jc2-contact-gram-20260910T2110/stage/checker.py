"""Independent contact identity/sign checker. No producer/science-arithmetic import."""
import argparse
import hashlib
import pathlib
import re
import sys
import authority

RAT = None
BINOM = None
ZERO = (0, 0, 0, 0)
MAX_TERMS = 20000
MAX_BITS = 12000
SCHEMA = 'f10-contact-gram-certificate/v1'
BOUNDS = {'R_weight': '52', 'cofactor_weight': '64', 'U0_V': '3',
          'U1_V': '3', 'Uphi_V': '5', 'rectangle_t': '52', 'rectangle_v': '52'}

def checked(a):
    if RAT is None:
        raise RuntimeError('authorize before arithmetic')
    a = {e: RAT(c) for e, c in a.items() if c}
    if len(a) > MAX_TERMS:
        raise ValueError('checker term cap')
    for e, c in a.items():
        if len(e) != 4 or min(e) < 0 or max(e) > 100:
            raise ValueError('checker exponent cap')
        if max(abs(c.numerator).bit_length(), c.denominator.bit_length()) > MAX_BITS:
            raise ValueError('checker coefficient bit cap')
    return a

def const(c):
    if RAT is None:
        raise RuntimeError('authorize before arithmetic')
    return {ZERO: RAT(c)} if c else {}

def variable(axis):
    e = list(ZERO)
    e[axis] = 1
    return {tuple(e): RAT(1)}

def add(*polys):
    result = {}
    for poly in polys:
        for e, c in poly.items():
            result[e] = result.get(e, RAT(0)) + c
            if not result[e]:
                del result[e]
    return checked(result)

def scale(poly, c):
    return checked({e: value*c for e, value in poly.items()})

def mul(*polys):
    result = const(1)
    for poly in polys:
        out = {}
        for a, x in result.items():
            for b, y in poly.items():
                e = tuple(a[i]+b[i] for i in range(4))
                out[e] = out.get(e, RAT(0))+x*y
                if not out[e]:
                    del out[e]
                if len(out) > MAX_TERMS:
                    raise ValueError('checker term cap')
        result = checked(out)
    return result

def power(poly, n):
    if type(n) is not int or not 0 <= n <= 100:
        raise ValueError('checker power bound')
    # Deliberately ordinary multiplication, not producer exponentiation.
    result = const(1)
    for _ in range(n):
        result = mul(result, poly)
    return result

def coefficient(poly, axis, degree):
    out = {}
    for e, c in poly.items():
        if e[axis] == degree:
            key = list(e)
            key[axis] = 0
            out[tuple(key)] = c
    return checked(out)

def degree(poly, axis):
    return max((e[axis] for e in poly), default=-1)

def synthetic(poly, axis, root):
    """Divide by variable-root, with root independent of that variable."""
    if degree(root, axis) > 0:
        raise ValueError('synthetic root depends on variable')
    quotient, remainder = {}, poly
    x = variable(axis)
    for k in range(degree(poly, axis), 0, -1):
        lead = coefficient(remainder, axis, k)
        term = mul(lead, power(x, k-1))
        quotient = add(quotient, term)
        remainder = add(remainder, scale(mul(term, add(x, scale(root, -1))), -1))
    return quotient, remainder

def decimal(text, signed=True):
    pattern = r'(0|-?[1-9][0-9]*)' if signed else r'(0|[1-9][0-9]*)'
    if type(text) is not str or len(text) > authority.DECIMAL_LIMIT or not re.fullmatch(pattern, text):
        raise ValueError('canonical decimal string required')
    return int(text)

def rational(value):
    if type(value) is not list or len(value) != 2:
        raise ValueError('canonical rational pair required')
    n, d = decimal(value[0]), decimal(value[1], False)
    if d <= 0:
        raise ValueError('positive rational denominator required')
    c = RAT(n, d)
    if c.numerator != n or c.denominator != d:
        raise ValueError('noncanonical rational pair')
    if max(abs(n).bit_length(), d.bit_length()) > MAX_BITS:
        raise ValueError('wire coefficient bit cap')
    return c


def reconstruct():
    # Literal quartic coefficients FIRST, then all four X^2-sX+p remainders.
    s, p, V, W = (variable(i) for i in range(4))
    a3 = add(scale(V, 30), const(-14))
    a2 = add(const(71), scale(V, -270), scale(power(V, 2), 180), scale(W, 120))
    a1 = add(const(-154), scale(V, 780), scale(power(V, 2), -900), scale(power(V, 3), 120), scale(W, -600), scale(mul(V, W), 720))
    a0 = add(const(120), scale(V, -720), scale(power(V, 2), 1080), scale(power(V, 3), -240), scale(W, 720), scale(mul(V, W), -1440), scale(power(W, 2), 360))
    b3 = add(scale(V, 42), const(-18))
    b2 = add(const(119), scale(V, -504), scale(power(V, 2), 420), scale(W, 210))
    b1 = add(const(-342), scale(V, 1974), scale(power(V, 2), -2940), scale(power(V, 3), 840), scale(W, -1470), scale(mul(V, W), 2520))
    b0 = add(const(360), scale(V, -2520), scale(power(V, 2), 5040), scale(power(V, 3), -2520), scale(W, 2520), scale(mul(V, W), -7560), scale(mul(power(V, 2), W), 2520), scale(power(W, 2), 2520))
    X4lin = add(power(s, 3), scale(mul(s, p), -2))
    X4const = add(power(p, 2), scale(mul(power(s, 2), p), -1))
    X3lin = add(power(s, 2), scale(p, -1))
    fa1 = add(X4lin, mul(a3, X3lin), mul(a2, s), a1)
    fa0 = add(X4const, scale(mul(a3, s, p), -1), scale(mul(a2, p), -1), a0)
    fb1 = add(X4lin, mul(b3, X3lin), mul(b2, s), b1)
    fb0 = add(X4const, scale(mul(b3, s, p), -1), scale(mul(b2, p), -1), b0)
    elimination = add(fb1, scale(fa1, RAT(-7, 2)))
    d = scale(add(s, const(-3)), 210)
    if degree(elimination, 3) != 1 or coefficient(elimination, 3, 1) != scale(d, -1):
        raise ValueError('literal W elimination coefficient')
    N = coefficient(elimination, 3, 0)

    def clear(poly, exponent):
        if degree(poly, 3) > exponent:
            raise ValueError('literal W denominator envelope')
        return add(*(mul(coefficient(poly, 3, k), power(N, k), power(d, exponent-k)) for k in range(exponent+1)))

    phi = scale(clear(fa1, 1), RAT(1, 302400))
    q0 = clear(fa0, 2)
    q1 = clear(add(fb0, scale(fa0, -7)), 1)
    if degree(phi, 2) != 4 or coefficient(phi, 2, 4) != const(1):
        raise ValueError('independent monic quartic')
    if degree(q0, 2) > 6 or degree(q1, 2) > 5:
        raise ValueError('independent Q degrees')
    return phi, q0, q1

def polynomial(value, name):
    if type(value) is not list or len(value) > MAX_TERMS:
        raise ValueError('polynomial term envelope')
    weight = 52 if name == 'R' else 64
    vmax = {'R': 0, 'U0': 3, 'U1': 3, 'Uphi': 5}[name]
    out, previous = {}, None
    for term in value:
        if type(term) is not list or len(term) != 2 or type(term[0]) is not list or len(term[0]) != 3:
            raise ValueError('polynomial term shape')
        e = tuple(decimal(x, False) for x in term[0])
        if previous is not None and e <= previous:
            raise ValueError('duplicate or unsorted polynomial term')
        previous = e
        if e[0]+2*e[1]+e[2] > weight or e[2] > vmax:
            raise ValueError('polynomial weight or V envelope')
        c = rational(term[1])
        if not c:
            raise ValueError('zero polynomial term')
        out[e+(0,)] = c
    return checked(out)

def pullback(poly):
    # Independent nested Horner in s,p; p=(2-a)(2-b).
    t, v = variable(0), variable(1)
    a = scale(add(const(6), t), RAT(1, 21))
    b = scale(add(const(3), scale(t, -3), scale(mul(t, v), 7)), RAT(1, 21))
    X, Y = add(const(2), scale(a, -1)), add(const(2), scale(b, -1))
    sigma, product = add(X, Y), mul(X, Y)
    out = {}
    for i in range(degree(poly, 0), -1, -1):
        row = coefficient(poly, 0, i)
        acc = {}
        for j in range(degree(row, 1), -1, -1):
            acc = add(mul(acc, product), coefficient(row, 1, j))
        out = add(mul(out, sigma), acc)
    out = scale(out, 21**52)
    if any(e[0] > 52 or e[1] > 52 or e[2] or e[3] for e in out):
        raise ValueError('rectangle envelope')
    return out

def bernstein_expansion(values, n):
    # Expand the v basis one row at a time, then the t basis.
    # This is not the producer's power-to-Bernstein triangular conversion.
    temp = [[RAT(0) for _ in range(53)] for _ in range(n+1)]
    for i, row in enumerate(values):
        for j, c in enumerate(row):
            for k in range(53-j):
                temp[i][j+k] += c*BINOM(52, j)*BINOM(52-j, k)*(-1 if k % 2 else 1)
    out = {}
    for i, row in enumerate(temp):
        for l, c in enumerate(row):
            for k in range(n-i+1):
                key = (i+k, l, 0, 0)
                out[key] = out.get(key, RAT(0))+c*BINOM(n, i)*BINOM(n-i, k)*(-1 if k % 2 else 1)
    return checked(out)

def verify(data):
    keys = {'schema', 'status', 'reason', 'science', 'code', 'variables', 'bounds', 'polynomials', 'j', 'bernstein'}
    if type(data) is not dict or set(data) != keys or data['schema'] != SCHEMA:
        raise ValueError('strict certificate schema')
    if data['science'] != authority.SCIENCE or data['code'] != authority.code_pins():
        raise ValueError('source or code binding')
    if data['variables'] != ['s', 'p', 'V'] or data['bounds'] != BOUNDS:
        raise ValueError('variables or bounds')
    if data['status'] not in ('CANDIDATE', 'INCONCLUSIVE') or type(data['reason']) is not str or len(data['reason']) > 400:
        raise ValueError('producer status schema')
    if type(data['polynomials']) is not dict or set(data['polynomials']) != {'R', 'U0', 'U1', 'Uphi'}:
        raise ValueError('complete four-polynomial inventory')
    obj = {name: polynomial(value, name) for name, value in data['polynomials'].items()}
    phi, q0, q1 = reconstruct()
    identity = add(mul(obj['U0'], q0), mul(obj['U1'], q1), mul(obj['Uphi'], phi))
    if identity != obj['R']:
        raise ValueError('full contact cofactor identity')
    hat = pullback(obj['R'])
    if not hat:
        raise ValueError('zero R cannot carry a maximal-factor sign certificate')
    reduced, count = hat, 0
    while True:
        quotient, remainder = synthetic(reduced, 0, const(1))
        if remainder:
            break
        if not quotient or count >= 52:
            raise ValueError('maximal edge factor bound')
        reduced = scale(quotient, -1)
        count += 1
    j = decimal(data['j'], False)
    if j != count or not 0 <= j <= 52:
        raise ValueError('wrong maximal excluded-edge factor')
    n = 52-j
    if degree(reduced, 0) > n or degree(reduced, 1) > 52:
        raise ValueError('reduced rectangle envelope')
    bern = data['bernstein']
    if type(bern) is not dict or set(bern) != {'degree_t', 'degree_v', 'coefficients'}:
        raise ValueError('Bernstein schema')
    if decimal(bern['degree_t'], False) != n or bern['degree_v'] != '52':
        raise ValueError('Bernstein declared degree')
    rows = bern['coefficients']
    if type(rows) is not list or len(rows) != n+1 or any(type(row) is not list or len(row) != 53 for row in rows):
        raise ValueError('complete Bernstein rectangle')
    values = [[rational(c) for c in row] for row in rows]
    if bernstein_expansion(values, n) != reduced:
        raise ValueError('full Bernstein expansion')
    endpoint = hat.get(ZERO, RAT(0))
    if any(c != endpoint for c in values[0]):
        raise ValueError('all 53 collapsed-edge entries')
    if endpoint <= 0:
        return {'status': 'INCONCLUSIVE', 'reason': 'nonpositive endpoint; full identity and expansion checked'}
    if any(c < 0 for row in values for c in row):
        return {'status': 'INCONCLUSIVE', 'reason': 'negative Bernstein coefficient; full identity and expansion checked'}
    return {'status': 'PRESCRIBED_CONTACT_EXCLUDED_BY_CERTIFICATE',
            'scope': 'prescribed triangle t<1 only; not full-window equivalence, source or JC2',
            'identity': 'full contact cofactor identity; Gram determinant equality NOT independently checked',
            'j': str(j), 'degree_t': str(n), 'degree_v': '52',
            'bernstein_entries': str((n+1)*53), 'retained_edges': ['t=0', 'v=0', 'v=1']}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--job', required=True)
    parser.add_argument('--registration', required=True)
    parser.add_argument('--input', required=True)
    parser.add_argument('--receipt', required=True)
    args = parser.parse_args()
    permit = authority.authorize('check', args.job, args.registration, [args.receipt], args.input)
    global RAT, BINOM
    from fractions import Fraction
    from math import comb
    RAT, BINOM = Fraction, comb
    path = pathlib.Path(args.input)
    if path.stat().st_size > authority.LIMIT-authority.RECEIPT_LIMIT:
        raise ValueError('aggregate wire size limit')
    raw = path.read_bytes()
    if len(raw) > authority.LIMIT-authority.RECEIPT_LIMIT:
        raise ValueError('aggregate wire size limit')
    raw_sha = hashlib.sha256(raw).hexdigest()
    if raw_sha != permit['pins'][str(path.resolve())]:
        raise ValueError('verified raw input SHA mismatch')
    result = verify(authority.strict_json(raw, wire=True))
    result.update({'schema': 'f10-contact-gram-check/v1', 'input_sha256': raw_sha,
                   'code': authority.code_pins(), 'registration_sha256': permit['registration_sha256']})
    authority.postcheck(permit)
    authority.emit(args.receipt, result, min(authority.RECEIPT_LIMIT, authority.LIMIT-len(raw)))
    print(result['status'])
    return 0 if result['status'] == 'PRESCRIBED_CONTACT_EXCLUDED_BY_CERTIFICATE' else 2

if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, TypeError, KeyError, RuntimeError, RecursionError, ArithmeticError, MemoryError, OSError) as exc:
        print('INCONCLUSIVE: ' + str(exc)[:400], file=sys.stderr)
        raise SystemExit(2)
