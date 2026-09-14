"""STATIC independent full-source/readback checker. No producer import."""
from authority import authorize


def check_file(path):
    import json
    import check_arithmetic as n
    from check_arithmetic import (Rational as Q, F, constant as C0, symbol as sym,
        sum_poly as add, minus as sub, negative as neg, product as mul,
        multiply_scalar as sc, exponent as pw, derivative as der, extract as co,
        move, value, fractional_series as series, primitive as integ, require as eq)

    def object_pairs(pairs):
        result = {}
        for key, val in pairs:
            if key in result:
                raise ValueError('duplicate JSON key')
            result[key] = val
        return result

    def forbidden_number(_):
        raise ValueError('all wire numbers must be decimal strings')

    with open(path, 'rb') as f:
        raw = f.read(15728641)
    if len(raw) > 15728640:
        raise ValueError('coefficient byte cap')
    doc = json.loads(raw, object_pairs_hook=object_pairs, parse_int=forbidden_number,
                     parse_float=forbidden_number, parse_constant=forbidden_number)

    def keys(obj, expected):
        if not isinstance(obj, dict) or set(obj) != set(expected.split()):
            raise ValueError('strict object keys: ' + expected)

    def array(a, size):
        if not isinstance(a, list) or len(a) != size:
            raise ValueError('fixed array length')
        return a

    def integer(s, bound=None, signed=False):
        if not isinstance(s, str) or not 1 <= len(s) <= 4096:
            raise ValueError('decimal length/type')
        digits = s[1:] if signed and s.startswith('-') else s
        if not digits or any(c not in '0123456789' for c in digits):
            raise ValueError('decimal syntax')
        if len(digits) > 1 and digits[0] == '0' or s == '-0':
            raise ValueError('noncanonical integer')
        k = int(s)
        if bound is not None and not 0 <= k <= bound:
            raise ValueError('integer bound')
        return k

    def rational(s):
        if not isinstance(s, str) or s.count('/') != 1:
            raise ValueError('rational syntax')
        a, b = s.split('/')
        p, q = integer(a, signed=True), integer(b)
        if q <= 0:
            raise ValueError('rational denominator')
        r = Q(p, q)
        if r.numerator != p or r.denominator != q:
            raise ValueError('rational not reduced')
        return r

    def elt(a):
        return tuple(rational(v) for v in array(a, 7))

    count = [0]

    def poly(a):
        if not isinstance(a, list) or len(a) > 4096:
            raise ValueError('polynomial term bound')
        count[0] += len(a)
        if count[0] > 50000:
            raise ValueError('aggregate term bound')
        out, previous = {}, None
        for term in a:
            e, v = array(term, 2)
            ex = tuple(integer(s, 16) for s in array(e, 6))
            val = elt(v)
            if ex in out or previous is not None and ex <= previous or not any(val):
                raise ValueError('duplicate/unsorted/zero sparse term')
            previous = ex
            out[ex] = val
        return out

    keys(doc, 'format job_tag interface field source bands rows')
    eq(doc['format'], 'r2-reconstruction-19-v1', 'format')
    eq(doc['job_tag'], 'f10-r2-reconstruction-v1', 'job')
    expected_interface = {'variables': ['X1', 'X2', 'X3', 'z', 'S', 'vartheta'],
        'weights': ['1', '2', '3', '5', '1', '2'], 'base': 'Q[Z]/P7',
        'basis': ['0', '1', '2', '3', '4', '5', '6'], 'scale': 'z=s^2; s invertible',
        'targets': ['K1_0-U*s^5', 'K0_0-s^7'], 'guard': 'omega=W*t5*s^8',
        'rows': ['Psi5', 'Psi6', 'Psi7'] + ['K1_' + str(i) for i in range(1, 7)] +
                ['K0_' + str(i) for i in range(1, 9)] + ['K1_0-U*s^5', 'K0_0-s^7']}
    eq(doc['interface'], expected_interface, 'complete 19-row scale interface')
    keys(doc['field'], 'P7 dL KL gamma W t5 H7 C D units')
    # Literal primary formulas, formed with separate rational polynomial code.
    tau = Q(2, 7)
    d = [(1 + tau) * (2 - 3 * tau), -12 * (1 - tau), Q(12)]
    k = [2 * (2 - 3 * tau) * (1 + tau) * (2 + tau) * (3 + tau),
         42 * (1 + tau) * (2 + tau) * (4 * tau - 3), 840 * (1 - tau * tau), Q(-840)]
    g = [tau * (1 + tau) * (2 + tau) * (3 + tau), -30 * tau * (1 + tau) * (2 + tau),
         180 * tau * (1 + tau), -120 * tau]
    septic = n.plus([2 * q for q in n.times(k, k)],
                    n.plus([-140 * tau * q for q in n.times(n.times([1 + tau, -6], k), d)],
                           [245 * q for q in n.times(g, n.times(d, d))]))
    eq(len(septic), 8, 'septic degree')
    eq(septic[-1], -245 * 120 * 144 * tau, 'septic leading coefficient')
    n.MODULUS = [q / septic[-1] for q in septic]
    eq([rational(v) for v in array(doc['field']['P7'], 8)], n.MODULUS, 'P7 literal')
    fielddata = {key: elt(doc['field'][key]) for key in ('dL', 'KL', 'gamma', 'W', 't5', 'H7')}
    for key, val in (('dL', F(d)), ('KL', F(k)), ('gamma', F(g))):
        eq(fielddata[key], val, key)
    W = n.fproduct(F(Q(-1, 210)), n.fproduct(F(k), n.inverse(F(d))))
    eq(fielddata['W'], W, 'W independently reconstructed')
    Wi = n.inverse(W)
    T, S, z = sym(5), sym(4), sym(3)
    c = add(C0(1), T, sc(pw(T, 2), F([0, 1])), sc(pw(T, 3), W))
    ts = series(c, Q(12, 7), 7)
    t5 = value(co(ts, 5, 5))
    H7 = value(co(series(c, Q(15, 7), 7), 5, 7))
    eq(fielddata['t5'], t5, 't5')
    eq(fielddata['H7'], H7, 'H7')
    C, D = sc(c, Wi), sc({e: v for e, v in ts.items() if e[5] <= 5}, n.inverse(t5))
    eq(poly(doc['field']['C']), C, 'C')
    eq(poly(doc['field']['D']), D, 'D')
    eq(add(sc(mul(C, der(D, 5)), 7), sc(mul(der(C, 5), D), -12)), neg(pw(T, 7)), 'leading ODE')
    units = doc['field']['units']
    expected_unit_names = {'dL', 'W', 't5', 'H7'} | {
        'gap' + str(h) + ':' + str(j) for h in range(1, 5) for j in range(3)}
    if not isinstance(units, dict) or set(units) != expected_unit_names:
        raise ValueError('exact unit inventory')
    parsed_units = {}
    for label, pair in units.items():
        u, v = [elt(x) for x in array(pair, 2)]
        eq(n.fproduct(u, v), F(1), 'unit full-basis product ' + label)
        eq(v, n.inverse(u), 'independent Euclid inverse ' + label)
        parsed_units[label] = (u, v)
    for label in ('dL', 'W', 't5', 'H7'):
        eq(parsed_units[label][0], fielddata[label], 'named inverse input')
    a, b = value(co(C, 5, 0)), value(co(D, 5, 0))

    keys(doc['source'], 'Ahat Bhat U E Dpar Vpar Kpar Pihat')
    src = {key: poly(val) for key, val in doc['source'].items()}
    A, B, U, E, dp, vp, kp, pi = [src[key] for key in ('Ahat', 'Bhat', 'U', 'E', 'Dpar', 'Vpar', 'Kpar', 'Pihat')]

    def envelope(p, weight, physical=True):
        for ex in p:
            w = ex[0] + 2 * ex[1] + 3 * ex[2] + 5 * ex[3]
            if physical:
                w += ex[4] + 2 * ex[5]
            elif ex[4]:
                raise ValueError('band S coordinate')
            eq(w, weight, 'homogeneous envelope')

    for p, w in ((A, 7), (B, 12), (U, 3), (E, 7), (dp, 2), (vp, 4), (kp, 7), (pi, 7)):
        envelope(p, w)
    for p in (U, E):
        if any(ex[4] or ex[5] for ex in p):
            raise ValueError('scalar source parameter')
    for p, deg in ((dp, 2), (vp, 4), (kp, 7)):
        if any(ex[5] or ex[4] > deg for ex in p):
            raise ValueError('source coefficient-polynomial degree')
    expectedA = add(mul(S, pw(T, 3)), mul(sub(mul(S, dp), U), pw(T, 2)),
                    mul(add(z, neg(mul(U, dp)), mul(S, vp)), T), kp)
    eq(A, expectedA, 'literal A including all affine shifts')
    eq(pi, add(mul(z, T), neg(mul(U, pw(T, 2))), mul(S, pw(T, 3))), 'literal Pihat')
    eq(co(kp, 4, 0), {}, 'A constant gauge')
    upper = neg(add(mul(mul(E, T), pi), mul(T, pw(pi, 2))))
    # Independent coefficient-of-Jacobian assembly, not copied producer Q_j.
    Ac = [co(A, 5, j) for j in range(4)]
    Bc = [{} for _ in range(6)]
    Bc[5] = pw(S, 2)
    for j in range(4, -1, -1):
        other = {}
        for ak in range(3):
            ell = j + 3 - ak
            if ell <= 5:
                other = add(other, sc(mul(der(Ac[ak], 4), Bc[ell]), ell),
                            sc(mul(Ac[ak], der(Bc[ell], 4)), -ak))
        rhs = sub(co(upper, 5, j + 2), other)
        for ex, cc in rhs.items():
            pivot = j - 3 * ex[4]
            if pivot == 0:
                raise ValueError('nonzero resonant Euler slot')
            Bc[j][ex] = tuple(v / pivot for v in cc)
    rebuiltB = add(*(move(p, 5, j) for j, p in enumerate(Bc)))
    eq(B, rebuiltB, 'independent COMPLETE Euler B')
    eq(co(co(B, 5, 3), 4, 1), {}, 'mate shear gauge')
    eq(co(co(B, 5, 0), 4, 0), {}, 'mate constant gauge')
    for p, degree, total in ((A, 3, 7), (B, 5, 12)):
        for ex in p:
            if ex[5] > degree or ex[4] > total - 2 * ex[5]:
                raise ValueError('complete A/B support')

    def band(p, total, h):
        out = {}
        for ex, v in p.items():
            if ex[4] + 2 * ex[5] == total - h:
                key = list(ex)
                key[4] = 0
                out[tuple(key)] = v
        return out

    Ab, Bb = [band(A, 7, h) for h in range(8)], [band(B, 12, h) for h in range(8)]
    eq(Ab[0], C, 'source leading C')
    eq(Bb[0], D, 'source leading D')

    def oper(h, ap, bp):
        return add(sc(mul(C, der(bp, 5)), 7), sc(mul(der(C, 5), bp), h - 12),
                   sc(mul(ap, der(D, 5)), 7 - h), sc(mul(der(ap, 5), D), -12))

    def residual_pair(p):
        if any(ex[5] > 1 for ex in p):
            raise ValueError('upper band residual')
        return [co(p, 5, 1), co(p, 5, 0)]

    lambdas, psis = [], []
    for h, packet in enumerate(array(doc['bands'], 7), 1):
        forcing = {}
        for i in range(1, h):
            forcing = add(forcing, sc(mul(Ab[i], der(Bb[h - i], 5)), 7 - i),
                          sc(mul(der(Ab[i], 5), Bb[h - i]), -(12 - h + i)))
        if h < 5:
            keys(packet, 'kind gap forcing part basisV matrix inverse rho A B')
            eq(packet['kind'], 'early' if h < 4 else 'middle', 'band kind')
        else:
            keys(packet, 'kind gap forcing part A_part fixed target A_var target_var B_var column lambda base value Psi A B')
            eq(packet['kind'], 'column', 'column kind')
        eq(packet['gap'], str(h), 'ordered band gap')
        eq(poly(packet['forcing']), forcing, 'full mixed forcing')
        eq(poly(packet['A']), Ab[h], 'band A actual source extraction')
        eq(poly(packet['B']), Bb[h], 'band B actual full Euler extraction')
        envelope(forcing, h, False)
        envelope(Ab[h], h, False)
        envelope(Bb[h], h, False)
        part = poly(packet['part'])
        envelope(part, h, False)
        for j in range(5 if h < 5 else 3):
            if 7 * j - 3 * (12 - h) == 0:
                raise ValueError('upper band uniqueness/resonance')
        if h < 5:
            if any(ex[5] > 4 for ex in part):
                raise ValueError('particular V support')
            base = residual_pair(add(oper(h, {}, part), forcing))
            basisV = [poly(p) for p in array(packet['basisV'], 3)]
            matrix = [[elt(v) for v in array(row, 3)] for row in array(packet['matrix'], 3)]
            inv = [[elt(v) for v in array(row, 3)] for row in array(packet['inverse'], 3)]
            actual_columns = []
            for j, Vj in enumerate(basisV):
                envelope(Vj, 0, False)
                if any(ex[5] > 4 for ex in Vj):
                    raise ValueError('linear V support')
                Aj = pw(T, j)
                targetj = sc(pw(T, 6), -2) if h == 3 and j == 2 else {}
                rj = residual_pair(sub(oper(h, Aj, Vj), targetj))
                rhoj = sub(sc(co(Vj, 5, 0), n.fproduct(F(7), a)),
                           sc(co(Aj, 5, 0), n.fproduct(F(12), b)))
                actual_columns.append([value(rj[0]), value(rj[1]), value(rhoj)])
            eq(matrix, [[actual_columns[j][i] for j in range(3)] for i in range(3)], 'exact operator/rho matrix')
            for left, right in ((matrix, inv), (inv, matrix)):
                for i in range(3):
                    for j in range(3):
                        got = F(0)
                        for k0 in range(3):
                            got = n.fsum(got, n.fproduct(left[i][k0], right[k0][j]))
                        eq(got, F(int(i == j)), 'two-sided inverse matrix')
            # Reconstruct ordered pivot values independently, tying every
            # emitted matrix-unit array to its actual use, not just a product.
            reduced = [list(row) for row in matrix]
            for j in range(3):
                pivotrow = next((i for i in range(j, 3) if any(reduced[i][j])), None)
                if pivotrow is None:
                    raise ValueError('matrix rank')
                reduced[j], reduced[pivotrow] = reduced[pivotrow], reduced[j]
                u, ui = parsed_units['gap' + str(h) + ':' + str(j)]
                eq(reduced[j][j], u, 'actual matrix pivot witness')
                reduced[j] = [n.fproduct(v, ui) for v in reduced[j]]
                for i in range(3):
                    if i != j:
                        fac = reduced[i][j]
                        reduced[i] = [n.fsum(v, n.fnegative(n.fproduct(fac, w)))
                                      for v, w in zip(reduced[i], reduced[j])]
            rho = poly(packet['rho'])
            envelope(rho, h)
            xyz = [co(Ab[h], 5, j) for j in range(3)]
            if any(ex[5] > 2 for ex in Ab[h]):
                raise ValueError('early A support')
            eq(Bb[h], add(part, *(mul(xyz[j], basisV[j]) for j in range(3))), 'full particular plus linear mate')
            for row, wanted in zip(matrix, [neg(base[0]), neg(base[1]), rho]):
                eq(add(*(sc(x, c0) for c0, x in zip(row, xyz))), wanted, 'forward/reverse affine row map')
            eq(sub(sc(co(sub(Bb[h], part), 5, 0), n.fproduct(F(7), a)),
                   sc(co(Ab[h], 5, 0), n.fproduct(F(12), b))), rho, 'rho subtraction')
            if h < 4:
                eq(rho, sym(h - 1), 'EXACT normalized free Xi coordinate')
            else:
                eq(inv[2][2], n.fproduct(F(Q(4, 15)), H7), 'middle Phi/H7 relation')
                eq(xyz[2], {}, 'middle U2 zero')
                eq(co(Bb[h], 5, 4), {}, 'middle V4 zero')
                eq(co(Ab[h], 5, 1), sub(co(vp, 4, 0), mul(U, co(dp, 4, 1))), 'middle v0-U*d1 shift')
            if h == 3:
                eq(xyz[2], neg(U), 'modified q=-U')
                eq(xyz[1], sub(co(vp, 4, 1), mul(U, co(dp, 4, 2))), 'modified affine l')
        else:
            apart, fixed, target, avar, tvar, vvar = [poly(packet[key]) for key in
                ('A_part', 'fixed', 'target', 'A_var', 'target_var', 'B_var')]
            for p in (apart, fixed, target):
                envelope(p, h, False)
            for p in (avar, tvar, vvar):
                envelope(p, 0, False)
            if h == 5:
                y = sub(z, mul(U, co(dp, 4, 0)))
                wanted = (mul(y, T), {}, sc(mul(z, pw(T, 5)), -2), C0(1), {})
                # Literal unshifted critical D_i forcing, independently checked.
                N = sub(sub(sc(mul(z, pw(T, 5)), -2), forcing),
                        mul(y, sub(sc(mul(T, der(D, 5)), 2), sc(D, 12))))
                for i in range(5):
                    eq(co(N, 5, i), add(neg(co(forcing, 5, i)),
                        sc(mul(y, co(D, 5, i)), 12 - 2 * i)), 'critical UNshifted D_i')
            elif h == 6:
                wanted = ({}, mul(pw(U, 2), pw(T, 3)), neg(mul(pw(U, 2), pw(T, 5))), C0(1), {})
            else:
                wanted = ({}, {}, {}, {}, neg(pw(T, 4)))
            eq((apart, fixed, target, avar, tvar), wanted, 'literal critical/late/ell forcing')
            if any(ex[5] > 2 for ex in sub(part, fixed)) or any(ex[5] > 2 for ex in vvar):
                raise ValueError('column support/fixed U squared')
            base = residual_pair(add(sub(oper(h, apart, part), target), forcing))
            col = residual_pair(sub(oper(h, avar, vvar), tvar))
            c1, c0 = [value(p) for p in col]
            eq([elt(v) for v in array(packet['column'], 2)], [c1, c0], 'full operator column; late coefficient -6')
            eq([poly(v) for v in array(packet['base'], 2)], base, 'actual affine base')
            l1, l0 = [elt(v) for v in array(packet['lambda'], 2)]
            eq(n.fsum(n.fproduct(l1, c1), n.fproduct(l0, c0)), F(1), 'determinant one')
            if h == 5:
                invC2 = sc(series(c, Q(-2), 6), n.fproduct(W, W))
                expected = []
                for rpoly in (T, C0(1)):
                    p = mul(pw(C, 2), integ(mul(rpoly, invC2)))
                    expected.append(value(sub(sc(co(p, 5, 6), value(co(C, 5, 2))), sc(co(p, 5, 5), Q(1, 2)))))
                eq([l1, l0], expected, 'explicit critical Lambda')
            val = poly(packet['value'])
            psi = poly(packet['Psi'])
            envelope(val, h)
            for p in base:
                envelope(p, h)
            eq(val, neg(add(sc(base[0], l1), sc(base[1], l0))), 'variable reverse readback')
            eq(psi, sub(sc(base[1], c1), sc(base[0], c0)), 'compatibility retained')
            eq(Ab[h], add(apart, mul(val, avar)), 'column A substitution')
            eq(Bb[h], add(part, mul(val, vvar)), 'column B affine substitution')
            eq(residual_pair(sub(add(oper(h, Ab[h], Bb[h]), forcing), add(target, mul(val, tvar)))),
               [sc(psi, n.fnegative(l0)), sc(psi, l1)], 'whole determinant-one residual pair')
            if h == 7:
                eq(val, E, 'ell elimination not gauge')
                fcoef, hcoef = value(co(C, 5, 2)), value(co(C, 5, 1))
                ge = n.fproduct(F(Q(1, 10)), n.fsum(n.fproduct(F(6), hcoef), n.fnegative(n.fproduct(fcoef, fcoef))))
                eq(vvar, add(pw(T, 2), sc(T, n.fproduct(F(Q(1, 2)), fcoef)), C0(ge)), 'literal ell mate column')
            envelope(psi, h)
            psis.append(psi)
            lambdas.append((l1, l0))

    J = sub(mul(der(A, 4), der(B, 5)), mul(der(A, 5), der(B, 4)))
    adjusted = sub(J, upper)
    # Enumerate all 80 potential Jacobian positions, never just nonzero rows.
    checked_slots = 0
    for j in range(8):
        for i in range(17 - 2 * j):
            actual = co(co(adjusted, 5, j), 4, i)
            if j >= 2:
                eq(actual, {}, 'full upper Jacobian slot')
            checked_slots += 1
    eq(checked_slots, 80, '80-slot inventory')
    if any(e[5] > 7 or e[4] > 16 - 2 * e[5] for e in J):
        raise ValueError('Jacobian outside 80-slot envelope')
    keys(doc['rows'], 'Psi K1 K0')
    eq([poly(v) for v in array(doc['rows']['Psi'], 3)], psis, 'all three Psi slots')
    K1 = [poly(v) for v in array(doc['rows']['K1'], 7)]
    K0 = [poly(v) for v in array(doc['rows']['K0'], 9)]
    for j, top, low in ((1, 14, K1), (0, 16, K0)):
        for i in range(top + 1):
            actual = co(co(adjusted, 5, j), 4, i)
            if i < len(low):
                eq(actual, low[i], 'literal retained K coefficient')
                envelope(low[i], top - i)
            else:
                h = top - i
                wanted = {} if h < 5 else sc(psis[h - 5],
                    n.fnegative(lambdas[h - 5][1]) if j == 1 else lambdas[h - 5][0])
                eq(actual, wanted, 'all 32 original residual slots')
    # Full inverse-chart polynomiality: q is the NEW inverse-chart variable,
    # not coefficient z. S=P*q^3-z*q^2+U*q, vartheta=q^-1.
    chartS = add(move(sym(4), 5, 3), neg(move(z, 5, 2)), move(U, 5, 1))
    for source in (A, B):
        inverse_poly = {}
        for ex, val in source.items():
            coeffex = list(ex)
            coeffex[4] = coeffex[5] = 0
            term = mul({tuple(coeffex): val}, pw(chartS, ex[4]))
            inverse_poly = add(inverse_poly, move(term, 5, -ex[5], laurent=True))
        if any(ex[5] < 0 for ex in inverse_poly):
            raise ValueError('WHOLE inverse-polynomiality')
    # a_original=Wi*s^-3, b_original=t5^-1*s^-5. Exact s exponents
    # -3-5+8 cancel; no s=1 substitution or added scale-cover premise.
    eq(value(co(co(A, 5, 0), 4, 7)), Wi, 'source a')
    eq(value(co(co(B, 5, 0), 4, 12)), n.inverse(t5), 'source b')
    eq(n.fproduct(n.fproduct(W, t5), n.fproduct(Wi, n.inverse(t5))), F(1), 'omega*a*b=1')
    return 'CHECKED_STATIC_CONTRACT_19_ROWS_32_RESIDUALS_80_SLOTS_NO_SOURCE_OUTCOME'


def main():
    path = authorize('check')
    print(check_file(path))


if __name__ == '__main__':
    main()
