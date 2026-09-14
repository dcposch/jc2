"""Independent exact certificate checker; STATIC/UNEXECUTED, no producer import."""
import argparse
import pathlib
import re
import sys
import authority

RAT = None
BINOM = None
ZERO = (0, 0, 0, 0)
MAX_TERMS = 20000
MAX_BITS = 12000
SCHEMA = 'f10-middle-real-certificate/v1'
BOUNDS = {'R_total': '40', 'R_alpha': '21', 'U_total': '32', 'U_V': '4',
          'W_total': '35', 'W_V': '6', 'rectangle_t': '40', 'rectangle_s': '21'}

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

def family(X, is_q):
    """Literal accepted E_X/Q_X, reconstructed before elimination of W."""
    V, W = variable(2), variable(3)
    shifted = lambda k: add(X, const(-k))
    if not is_q:
        return add(mul(*(shifted(k) for k in (2, 3, 4, 5))),
                   scale(mul(*(shifted(k) for k in (2, 3, 4)), V), 30),
                   scale(mul(shifted(2), shifted(3), power(V, 2)), 180),
                   scale(mul(shifted(2), power(V, 3)), 120),
                   scale(mul(shifted(2), shifted(3), W), 120),
                   scale(mul(shifted(2), V, W), 720), scale(power(W, 2), 360))
    return add(mul(*(shifted(k) for k in (3, 4, 5, 6))),
               scale(mul(*(shifted(k) for k in (3, 4, 5)), V), 42),
               scale(mul(shifted(3), shifted(4), power(V, 2)), 420),
               scale(mul(shifted(3), power(V, 3)), 840),
               scale(mul(shifted(3), shifted(4), W), 210),
               scale(mul(shifted(3), V, W), 2520),
               scale(add(mul(power(V, 2), W), power(W, 2)), 2520))

def reconstruct():
    tau, alpha = variable(0), variable(1)
    nu = add(const(2), scale(tau, -1))
    E, Q = family(nu, False), family(nu, True)
    eliminated = add(Q, scale(E, -7))
    if degree(eliminated, 3) > 1:
        raise ValueError('independent W-square cancellation')
    K = coefficient(eliminated, 3, 0)
    D = scale(coefficient(eliminated, 3, 1), RAT(1, 210))
    beta, gamma = coefficient(E, 3, 1), coefficient(E, 3, 0)
    S = add(scale(power(K, 2), 2), scale(mul(beta, K, D), RAT(-7, 6)),
            scale(mul(gamma, power(D, 2)), 245))
    Z, remainder = synthetic(add(family(alpha, True), scale(Q, -1)), 1, nu)
    if remainder or degree(Z, 3) > 1:
        raise ValueError('independent divided-difference identity')
    T = add(mul(D, coefficient(Z, 3, 0)),
            scale(mul(K, coefficient(Z, 3, 1)), RAT(-1, 210)))
    if degree(S, 2) > 7 or degree(T, 2) != 5 or coefficient(T, 2, 5) != const(10080):
        raise ValueError('independent source degree or constant leading coefficient')
    return S, T

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

def polynomial(value, name):
    if type(value) is not list or len(value) > MAX_TERMS:
        raise ValueError('polynomial term envelope')
    bounds = {'Qdiv': (3, 3, 2, False), 'Frem': (8, 8, 4, False),
              'R': (40, 21, 0, True), 'U': (32, 32, 4, True),
              'Wcof': (35, 35, 6, True)}
    total, alpha, vdegree, integral = bounds[name]
    out, previous = {}, None
    for term in value:
        if type(term) is not list or len(term) != 2 or type(term[0]) is not list or len(term[0]) != 3:
            raise ValueError('polynomial term shape')
        e = tuple(decimal(x, False) for x in term[0])
        if previous is not None and e <= previous:
            raise ValueError('duplicate or unsorted polynomial term')
        previous = e
        if sum(e) > total or e[1] > alpha or e[2] > vdegree:
            raise ValueError('polynomial degree envelope')
        c = rational(term[1])
        if not c or (integral and c.denominator != 1):
            raise ValueError('zero term or nonintegral coefficient')
        out[e+(0,)] = c
    return checked(out)

def pullback(R):
    t, s = variable(0), variable(1)
    rt = scale(add(const(6), t), RAT(1, 21))
    ra = scale(add(const(45), scale(t, -3), scale(mul(t, s), 7)), RAT(1, 21))
    out = {}
    # Nested Horner reconstruction differs from producer's cached monomial substitution.
    for i in range(degree(R, 0), -1, -1):
        row = coefficient(R, 0, i)
        acc = {}
        for j in range(degree(row, 1), -1, -1):
            acc = add(mul(acc, ra), coefficient(row, 1, j))
        out = add(mul(out, rt), acc)
    out = scale(out, 21**40)
    if any(e[0] > 40 or e[1] > 21 or e[2] or e[3] for e in out):
        raise ValueError('rectangle envelope')
    if any(c.denominator != 1 for c in out.values()):
        raise ValueError('rectangle integrality')
    return out

def verify(data):
    keys = {'schema', 'status', 'reason', 'science', 'code', 'variables', 'bounds',
            'polynomials', 'j', 'epsilon', 'bernstein'}
    if type(data) is not dict or set(data) != keys or data['schema'] != SCHEMA:
        raise ValueError('strict certificate schema')
    if data['science'] != authority.SCIENCE or data['code'] != authority.code_pins():
        raise ValueError('source or code binding')
    if data['variables'] != ['tau', 'alpha', 'V'] or data['bounds'] != BOUNDS:
        raise ValueError('variables or declared bounds')
    if data['status'] not in ('CANDIDATE', 'INCONCLUSIVE') or type(data['reason']) is not str:
        raise ValueError('producer status schema')
    polys = data['polynomials']
    if type(polys) is not dict or set(polys) != {'Qdiv', 'Frem', 'R', 'U', 'Wcof'}:
        raise ValueError('complete polynomial inventory')
    objs = {name: polynomial(value, name) for name, value in polys.items()}
    S, T = reconstruct()
    if add(mul(objs['Qdiv'], T), objs['Frem']) != S:
        raise ValueError('full quotient-remainder identity')
    identity = add(mul(objs['U'], S), mul(objs['Wcof'], T))
    # This comparison checks every coefficient, including every positive V power.
    if any(e[2] or e[3] for e in identity):
        raise ValueError('positive V cancellation')
    if identity != objs['R']:
        raise ValueError('full cofactor identity')
    hat = pullback(objs['R'])
    if not hat:
        return {'status': 'INCONCLUSIVE', 'reason': 'zero determinant polynomial'}
    reduced, count = hat, 0
    while True:
        quotient, remainder = synthetic(reduced, 0, const(1))
        if remainder:
            break
        if not quotient or count >= 40:
            raise ValueError('maximal edge factor bound')
        reduced = scale(quotient, -1)
        count += 1
    j = decimal(data['j'], False)
    if j != count or not 1 <= j <= 40:
        raise ValueError('wrong maximal excluded-edge factor')
    endpoint = hat.get(ZERO, RAT(0))
    if not endpoint:
        return {'status': 'INCONCLUSIVE', 'reason': 'zero endpoint'}
    epsilon = decimal(data['epsilon'])
    if epsilon not in (-1, 1) or epsilon*endpoint <= 0:
        raise ValueError('wrong endpoint sign')
    target = scale(reduced, epsilon)
    A = 40-j
    if degree(target, 0) > A or degree(target, 1) > 21:
        raise ValueError('reduced rectangle envelope')
    bern = data['bernstein']
    if type(bern) is not dict or set(bern) != {'degree_t', 'degree_s', 'coefficients'}:
        raise ValueError('Bernstein schema')
    if decimal(bern['degree_t'], False) != A or bern['degree_s'] != '21':
        raise ValueError('Bernstein declared degree')
    rows = bern['coefficients']
    if type(rows) is not list or len(rows) != A+1 or any(type(row) is not list or len(row) != 22 for row in rows):
        raise ValueError('complete Bernstein rectangle required')
    values = [[rational(c) for c in row] for row in rows]
    t, s = variable(0), variable(1)
    bt = [scale(mul(power(t, i), power(add(const(1), scale(t, -1)), A-i)), BINOM(A, i)) for i in range(A+1)]
    bs = [scale(mul(power(s, k), power(add(const(1), scale(s, -1)), 21-k)), BINOM(21, k)) for k in range(22)]
    expansion = {}
    for i, row in enumerate(values):
        for k, c in enumerate(row):
            expansion = add(expansion, scale(mul(bt[i], bs[k]), c))
    if expansion != target:
        raise ValueError('full Bernstein expansion')
    if any(c != abs(endpoint) for c in values[0]):
        raise ValueError('all 22 collapsed-edge coefficients')
    if any(c < 0 for row in values for c in row):
        return {'status': 'INCONCLUSIVE', 'reason': 'negative Bernstein coefficient'}
    if values[0][0] <= 0 or values[0][21] <= 0:
        return {'status': 'INCONCLUSIVE', 'reason': 'nonpositive retained-edge endpoint'}
    return {'status': 'CERTIFIED_NONRESONANCE',
            'scope': 'accepted17zzi real triangle only; no source existence or JC2 conclusion',
            'j': str(j), 'degree_t': str(A), 'degree_s': '21',
            'bernstein_entries': str((A+1)*22), 'retained_edges': ['t=0', 's=0', 's=1']}

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
    try:
        path = pathlib.Path(args.input)
        if path.stat().st_size > authority.LIMIT-authority.RECEIPT_LIMIT:
            raise ValueError('aggregate wire size limit')
        raw = path.read_bytes()
        result = verify(authority.strict_json(raw, wire=True))
        result.update({'schema': 'f10-middle-real-check/v1', 'input_sha256': authority.digest(path),
                       'code': authority.code_pins(), 'registration_sha256': permit['registration_sha256']})
        authority.postcheck(permit)
        authority.emit(args.receipt, result, min(authority.RECEIPT_LIMIT, authority.LIMIT-len(raw)))
        print(result['status'])
        return 0 if result['status'] == 'CERTIFIED_NONRESONANCE' else 2
    except (ValueError, TypeError, KeyError, RecursionError, ArithmeticError, MemoryError, OSError) as exc:
        print('INCONCLUSIVE: ' + str(exc)[:400], file=sys.stderr)
        return 2

if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, TypeError, KeyError, RuntimeError, OSError) as exc:
        print('INCONCLUSIVE: ' + str(exc)[:400], file=sys.stderr)
        raise SystemExit(2)
