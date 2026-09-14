"""UNEXECUTED independent inverse-witness checker; no finder imports."""
from authority import authorize, TAG


class InvalidPlace(ValueError):
    pass


class NonIntegral(ValueError):
    pass


class IdentityFailure(ValueError):
    pass


def verify(ctx):
    import wire
    from fractions import Fraction

    # Independent construction from the literal rational definition, not a
    # finder-supplied modulus or any imported producer arithmetic.
    t = Fraction(3, 10)
    d = [(1+t)*(2-3*t), -12*(1-t), Fraction(12)]
    k = [2*(2-3*t)*(1+t)*(2+t)*(3+t), 42*(1+t)*(2+t)*(4*t-3),
         840*(1-t*t), Fraction(-840)]
    g = [t*(1+t)*(2+t)*(3+t), -30*t*(1+t)*(2+t), 180*t*(1+t), -120*t]
    coefficients = [Fraction(0) for _ in range(8)]
    for i in range(4):
        for j in range(4):
            coefficients[i+j] += 2*k[i]*k[j]
        for j in range(3):
            coefficients[i+j] -= 140*t*(1+t)*k[i]*d[j]
            coefficients[i+j+1] += 840*t*k[i]*d[j]
    for i in range(4):
        for j in range(3):
            for h in range(3):
                coefficients[i+j+h] += 245*g[i]*d[j]*d[h]
    wire.require(coefficients[7] == -245*120*144*t, 'literal septic leading term')
    expected = [v/coefficients[7] for v in coefficients]
    meta = ctx['meta']
    doc = wire.load(meta['baseline']['path'], 134217728, meta['baseline']['sha256'])
    modulus, slots, extras, constants = wire.baseline(doc)
    wire.require([Fraction(a,b) for a,b in modulus] == expected, 'literal monic P7')
    del doc
    place = meta['place']
    try:
        p = wire.integer(place['p'], 2147483647)
        phi_raw = place['phi']
        wire.require(isinstance(phi_raw, list) and 2 <= len(phi_raw) <= 8, 'factor degree')
        phi = [wire.integer(s, p-1) for s in phi_raw]
    except wire.WireError as exc:
        raise InvalidPlace('factor encoding') from exc
    if p < 2:
        raise InvalidPlace('prime lower bound')
    trial = 2
    while trial*trial <= p:
        if p % trial == 0:
            raise InvalidPlace('composite modulus')
        trial += 1
    f = len(phi)-1
    if phi[-1] != 1:
        raise InvalidPlace('factor monicity')

    def trim(a):
        a = [v % p for v in a]
        while a and not a[-1]:
            a.pop()
        return a

    def residue(a, b):
        a, b = trim(a), trim(b)
        if not b:
            raise InvalidPlace('zero divisor polynomial')
        while len(a) >= len(b):
            shift = len(a)-len(b)
            scale = a[-1]*pow(b[-1], -1, p) % p
            for i, v in enumerate(b):
                a[i+shift] -= scale*v
            a = trim(a)
        return a

    def scalar(pair):
        a, b = pair
        if b % p == 0:
            raise NonIntegral('dense denominator')
        return (a % p)*pow(b % p, -1, p) % p

    if residue([scalar(v) for v in modulus], phi):
        raise InvalidPlace('P7 factor divisibility')
    zero = tuple(0 for _ in range(f))
    one = (1,) + (0,)*(f-1)

    def add(a, b):
        return tuple((a[i]+b[i]) % p for i in range(f))

    def multiply(a, b):
        buf = [0]*(2*f-1)
        for i in range(f):
            for j in range(f):
                buf[i+j] += a[i]*b[j]
        for high in range(2*f-2, f-1, -1):
            c = buf[high] % p
            for i in range(f):
                buf[high-f+i] -= c*phi[i]
        return tuple(buf[i] % p for i in range(f))

    def power(a, exponent):
        value = one
        for bit in bin(exponent)[2:]:
            value = multiply(value, value)
            if bit == '1':
                value = multiply(value, a)
        return value

    def gcd_degree(a, b):
        a, b = trim(a), trim(b)
        while b:
            a, b = b, residue(a,b)
        return len(a)-1

    xsmall = residue([0,1], phi)
    x = tuple(xsmall + [0]*(f-len(xsmall)))
    frobenius = x
    for degree in range(1, f+1):
        frobenius = power(frobenius, p)
        difference = [(frobenius[i]-x[i]) % p for i in range(f)]
        if degree <= f//2 and gcd_degree(difference, phi) != 0:
            raise InvalidPlace('reducible residue factor')
    if frobenius != x:
        raise InvalidPlace('final Frobenius identity')

    def reduce_vector(v):
        raw = residue([scalar(pair) for pair in v], phi)
        return tuple(raw + [0]*(f-len(raw)))

    weights = [8,9,10] + [20-i for i in range(1,10)] + [23-i for i in range(1,13)] + [27]
    def extract(poly, weight):
        result = {}
        for ex, coeff in poly:
            wire.require(sum((i+1)*ex[i] for i in range(4)) == weight, 'whole homogeneous graph support')
            result[ex] = reduce_vector(coeff)
        return result
    projected = [extract(slots[i], weights[i]) for i in range(25)]
    for name, weight in [('Hq',7),('zeta',7),('ell',23),('g',30),('U',4)]:
        extract(extras[name], weight)
    for value in constants.values():
        reduce_vector(value)

    def monomials(weight, variable=0, prefix=()):
        if variable == 3:
            return [prefix+(weight//4,)] if weight % 4 == 0 else []
        out = []
        for exponent in range(weight//(variable+1)+1):
            out.extend(monomials(weight-(variable+1)*exponent,
                                 variable+1, prefix+(exponent,)))
        return out

    rows = monomials(30)
    columns = []
    for slot in range(25):
        columns.extend((slot, mon) for mon in monomials(30-weights[slot]))
    wire.require(len(rows) == 297 and len(columns) == 1453, 'complete ordered dimensions')
    cert = wire.load(meta['artifact']['path'], 16777216, meta['artifact']['sha256'])
    wire.keys(cert, 'format job_tag baseline_sha256 qualification_sha256 place dimensions finder_sha256 columns inverse')
    wire.require(cert['format'] == 'r3-rank-inverse-v1' and cert['job_tag'] == TAG,
                 'certificate type/job')
    wire.require(cert['baseline_sha256'] == meta['baseline']['sha256']
                 and cert['qualification_sha256'] == meta['baseline']['qualification_sha256']
                 and cert['place'] == place and cert['dimensions'] == ['297','1453']
                 and cert['finder_sha256'] == meta['files']['finder.py']['sha256'],
                 'certificate frozen bindings')
    selected = [wire.integer(v,1452) for v in wire.array(cert['columns'],297)]
    wire.require(len(set(selected)) == 297 and selected == sorted(selected), 'distinct ordered columns')
    inverse = []
    for row in wire.array(cert['inverse'],297):
        inverse.append([tuple(wire.integer(v,p-1) for v in wire.array(element,f))
                        for element in wire.array(row,297)])
    # Independent row-minus-multiplier reconstruction. No finder matrix,
    # elimination trace, reduced system, coefficient cache or gcd is trusted.
    matrix = []
    for row_exponent in rows:
        row = []
        for column_id in selected:
            slot, multiplier = columns[column_id]
            difference = tuple(row_exponent[i]-multiplier[i] for i in range(4))
            row.append(projected[slot].get(difference,zero)
                       if all(e >= 0 for e in difference) else zero)
        matrix.append(row)
    for i in range(297):
        for j in range(297):
            result = zero
            for k in range(297):
                result = add(result,multiply(matrix[i][k],inverse[k][j]))
            if result != (one if i == j else zero):
                raise IdentityFailure('full inverse identity')
    return {'rows':'297','columns':'1453','identity_positions':'88209',
            'residue_degree':str(f)}


def main():
    ctx = authorize('check')
    import wire
    import sys
    try:
        details = verify(ctx)
        status = 'R3_FULL_ROW_RANK_CHECKED_NO_AUTOMATIC_SOURCE_PROMOTION'
        ctx['finish'](status,ctx['meta']['artifact']['sha256'],details)
        print(status)
    except IdentityFailure:
        ctx['postcheck']()
        print('CHECK FAILED: full inverse identity',file=sys.stderr)
        raise SystemExit(2)
    except InvalidPlace:
        print('NONDECISION: INVALID_PLACE',file=sys.stderr)
        raise SystemExit(2)
    except NonIntegral:
        print('NONDECISION: NONINTEGRAL_BASELINE',file=sys.stderr)
        raise SystemExit(2)
    except wire.WireError:
        print('NONDECISION: MALFORMED_INPUT',file=sys.stderr)
        raise SystemExit(2)
    except (MemoryError,OverflowError):
        print('NONDECISION: INTERNAL_CAP',file=sys.stderr)
        raise SystemExit(2)


if __name__ == '__main__':
    main()
