"""Independent full-r3 raw/band/Euler/inverse/graph checker. No producer import."""
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

    with open(path, 'rb') as stream:
        raw = stream.read(134217729)
    if len(raw) > 134217728:
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
        if (len(digits) > 1 and digits[0] == '0') or s == '-0':
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

    def poly(a, graph=False):
        if not isinstance(a, list) or len(a) > 20000:
            raise ValueError('polynomial term cap')
        count[0] += len(a)
        if count[0] > 400000:
            raise ValueError('aggregate term cap')
        out, previous = {}, None
        bounds = (30, 15, 10, 7) if graph else (30, 15, 10, 7, 4, 30, 16)
        for term in a:
            e, v = array(term, 2)
            ex = tuple(integer(s, b) for s, b in zip(array(e, len(bounds)), bounds))
            if graph:
                ex += (0, 0, 0)
            val = elt(v)
            if ex in out or (previous is not None and ex <= previous) or not any(val):
                raise ValueError('duplicate/unsorted/zero sparse term')
            previous, out[ex] = ex, val
        return out

    keys(doc, 'format job_tag interface base source bands raw graph')
    eq(doc['format'], 'r3-source-cone-reconstruction-v1', 'format')
    eq(doc['job_tag'], 'f10-source-cone-r3-reconstruction-v1', 'job')
    names = ['K8', 'K9', 'K10'] + ['A1_' + str(i) for i in range(1, 10)] + ['A0_' + str(i) for i in range(1, 13)] + ['T']
    expected_interface = {'raw_variables': ['X1', 'X2', 'X3', 'X4', 'z', 'S', 'theta'],
        'raw_weights': ['1', '2', '3', '4', '7', '1', '3'],
        'graph_variables': ['X1', 'X2', 'X3', 'X4'], 'graph_weights': ['1', '2', '3', '4'],
        'base': 'WHOLE Q[V]/P7; basis 1,V,...,V^6', 'scale': 'z=s^2; s invertible',
        'targets': ['P1_0-U*s^5', 'P0_0-s^7'], 'guard': 'omega=W*t5*s^8',
        'graph_guard': 'g=Hq*ell', 'graph_rows': names,
        'jacobian_order': 'j=0..7;i=0..23-3j', 'low_order': 'P1:i=0..20;P0:i=0..23'}
    eq(doc['interface'], expected_interface, 'complete raw/graph interface')
    keys(doc['base'], 'P7 dL KL gamma W t5 middleH7 C D units')
    # Rebuild literal E and Q-7E elimination with separate rational arithmetic.
    tau = Q(3, 10)
    d = [(1 + tau) * (2 - 3 * tau), -12 * (1 - tau), Q(12)]
    k = [2 * (2 - 3 * tau) * (1 + tau) * (2 + tau) * (3 + tau),
         42 * (1 + tau) * (2 + tau) * (4 * tau - 3), 840 * (1 - tau * tau), Q(-840)]
    gam = [tau * (1 + tau) * (2 + tau) * (3 + tau), -30 * tau * (1 + tau) * (2 + tau),
           180 * tau * (1 + tau), -120 * tau]
    septic = n.plus([2 * q for q in n.times(k, k)],
                   n.plus([-140 * tau * q for q in n.times(n.times([1 + tau, -6], k), d)],
                          [245 * q for q in n.times(gam, n.times(d, d))]))
    eq(len(septic), 8, 'septic degree')
    eq(septic[-1], -245 * 120 * 144 * tau, 'septic leading coefficient')
    n.MODULUS = [q / septic[-1] for q in septic]
    eq([rational(v) for v in array(doc['base']['P7'], 8)], n.MODULUS, 'P7 literal')
    base = {key: elt(doc['base'][key]) for key in ('dL', 'KL', 'gamma', 'W', 't5')}
    for key, val in (('dL', F(d)), ('KL', F(k)), ('gamma', F(gam))):
        eq(base[key], val, key)
    W = n.fproduct(F(Q(-1, 210)), n.fproduct(F(k), n.inverse(F(d))))
    eq(base['W'], W, 'independently reconstructed W')
    Wi = n.inverse(W)
    T, S, z = sym(6), sym(5), sym(4)
    c = add(C0(1), T, sc(pw(T, 2), F([0, 1])), sc(pw(T, 3), W))
    ts = series(c, Q(17, 10), 7)
    t5 = value(co(ts, 6, 5))
    eq(base['t5'], t5, 't5')
    middle = {h: value(co(series(c, Q(27 - h, 10), 7), 6, 7)) for h in (5, 6)}
    eq([elt(v) for v in array(doc['base']['middleH7'], 2)], [middle[5], middle[6]], 'two literal middle coefficients')
    C = sc(c, Wi)
    D = sc({e: v for e, v in ts.items() if e[6] <= 5}, n.inverse(t5))
    eq(poly(doc['base']['C']), C, 'C')
    eq(poly(doc['base']['D']), D, 'D')
    eq(add(sc(mul(C, der(D, 6)), 10), sc(mul(der(C, 6), D), -17)), neg(pw(T, 7)), 'leading ODE')
    eq(co(ts, 6, 6), {}, 'leading contact6')
    eq(co(ts, 6, 7), {}, 'leading contact7')
    a, b = value(co(C, 6, 0)), value(co(D, 6, 0))
    units = doc['base']['units']
    expected_unit_names = {'dL', 'W', 't5', 'middleH7:5', 'middleH7:6', 'critical_c'} | {
        'gap' + str(h) + ':det' for h in range(1, 7)}
    if not isinstance(units, dict) or set(units) != expected_unit_names:
        raise ValueError('exact unit inventory')
    parsed_units = {}
    for label, pair in units.items():
        u, v = [elt(x) for x in array(pair, 2)]
        eq(n.fproduct(u, v), F(1), 'all-seven-coordinate inverse product ' + label)
        eq(v, n.inverse(u), 'independent Euclid inverse ' + label)
        parsed_units[label] = (u, v)
    for label, u in [('dL', base['dL']), ('W', W), ('t5', t5)] + [
            ('middleH7:' + str(h), middle[h]) for h in (5, 6)]:
        eq(parsed_units[label][0], u, 'actual named inverse input')

    def envelope(p, weight, physical=True):
        for ex in p:
            w = sum(ex[j] * (1, 2, 3, 4, 7)[j] for j in range(5))
            if physical:
                w += ex[5] + 3 * ex[6]
            elif ex[5]:
                raise ValueError('band S coordinate')
            eq(w, weight, 'homogeneous envelope')

    keys(doc['source'], 'Ahat Bhat U E Dpar Vpar Kpar Pihat')
    src = {key: poly(val) for key, val in doc['source'].items()}
    A, B, U, E, dp, vp, kp, pi = [src[key] for key in ('Ahat', 'Bhat', 'U', 'E', 'Dpar', 'Vpar', 'Kpar', 'Pihat')]
    for p, w in ((A, 10), (B, 17), (U, 4), (E, 10), (dp, 3), (vp, 6), (kp, 10), (pi, 10)):
        envelope(p, w)
    for p in (U, E):
        if any(ex[5] or ex[6] for ex in p):
            raise ValueError('scalar source parameter')
    for p, deg in ((dp, 3), (vp, 6), (kp, 10)):
        if any(ex[6] or ex[5] > deg for ex in p):
            raise ValueError('source coefficient degree')
    eq(A, add(mul(S, pw(T, 3)), mul(sub(mul(S, dp), U), pw(T, 2)),
              mul(add(z, neg(mul(U, dp)), mul(S, vp)), T), kp), 'literal complete A')
    eq(pi, add(mul(z, T), neg(mul(U, pw(T, 2))), mul(S, pw(T, 3))), 'literal Pi')
    eq(co(kp, 5, 0), {}, 'A translation gauge')
    upper = neg(add(mul(mul(E, T), pi), mul(T, pw(pi, 2))))
    # Rebuild B from coefficient-of-Jacobian assembly, not producer Q_j text.
    Ac = [co(A, 6, j) for j in range(4)]
    Bc = [{} for _ in range(6)]
    Bc[5] = pw(S, 2)
    for j in range(4, -1, -1):
        other = {}
        for ak in range(3):
            ell = j + 3 - ak
            if ell <= 5:
                other = add(other, sc(mul(der(Ac[ak], 5), Bc[ell]), ell),
                            sc(mul(Ac[ak], der(Bc[ell], 5)), -ak))
        rhs = sub(co(upper, 6, j + 2), other)
        for ex, cc in rhs.items():
            pivot = j - 3 * ex[5]
            if not pivot:
                raise ValueError('nonzero Euler resonance')
            Bc[j][ex] = tuple(v / pivot for v in cc)
    rebuiltB = add(*(move(p, 6, j) for j, p in enumerate(Bc)))
    eq(B, rebuiltB, 'independently reconstructed full Euler B')
    eq(co(co(B, 6, 3), 5, 1), {}, 'mate shear gauge')
    eq(co(co(B, 6, 0), 5, 0), {}, 'mate translation gauge')
    for p, degree, total in ((A, 3, 10), (B, 5, 17)):
        if any(ex[6] > degree or ex[5] > total - 3 * ex[6] for ex in p):
            raise ValueError('complete A/B support')

    def band(p, total, h):
        out = {}
        for ex, v in p.items():
            if ex[5] + 3 * ex[6] == total - h:
                key = list(ex)
                key[5] = 0
                out[tuple(key)] = v
        return out

    Ab = [band(A, 10, h) for h in range(11)]
    Bb = [band(B, 17, h) for h in range(11)]
    eq(Ab[0], C, 'source leading C')
    eq(Bb[0], D, 'source leading D')

    def oper(h, ap, bp):
        # Literal coefficient pairs i+l=k+1, assembled without derivatives.
        out = {}
        for i in range(4):
            for ell in range(6):
                if i + ell:
                    term = sc(mul(co(C, 6, i), co(bp, 6, ell)), 10 * ell - (17 - h) * i)
                    out = add(out, move(term, 6, i + ell - 1))
        for i in range(3):
            for ell in range(6):
                if i + ell:
                    term = sc(mul(co(ap, 6, i), co(D, 6, ell)), (10 - h) * ell - 17 * i)
                    out = add(out, move(term, 6, i + ell - 1))
        return out

    def residual_pair(p):
        if any(ex[6] > 1 for ex in p):
            raise ValueError('upper band residual')
        return [co(p, 6, 1), co(p, 6, 0)]

    def solve_upper(h, ap, target, degree, fixed=None):
        bp = {} if fixed is None else fixed
        for j in range(degree, -1, -1):
            pivot = 10 * j - 3 * (17 - h)
            if pivot == 0:
                raise ValueError('band resonance')
            defect = co(sub(oper(h, ap, bp), target), 6, j + 2)
            bp = add(bp, move(sc(defect, Q(-1, pivot)), 6, j))
        residual_pair(sub(oper(h, ap, bp), target))
        return bp

    def determinant(matrix):
        ans = F(0)
        for perm, sign in (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                           ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)):
            term = F(sign)
            for i in range(3):
                term = n.fproduct(term, matrix[i][perm[i]])
            ans = n.fsum(ans, term)
        return ans

    lambdas, psis = [], []
    for h, packet in enumerate(array(doc['bands'], 10), 1):
        forcing = {}
        for i in range(1, h):
            # Independent ordered coefficient convolution of the earlier bracket.
            for ak in range(3):
                for bl in range(5):
                    if ak + bl:
                        term = sc(mul(co(Ab[i], 6, ak), co(Bb[h - i], 6, bl)),
                                  (10 - i) * bl - (17 - h + i) * ak)
                        forcing = add(forcing, move(term, 6, ak + bl - 1))
        if h <= 6:
            keys(packet, 'kind gap forcing part basisV matrix inverse rho A B')
            eq(packet['kind'], 'early' if h <= 4 else 'middle', 'band kind')
        else:
            keys(packet, 'kind gap forcing part A_part fixed target A_var target_var B_var column lambda base value Psi A B')
            eq(packet['kind'], 'column', 'column kind')
        eq(packet['gap'], str(h), 'ordered band gap')
        eq(poly(packet['forcing']), forcing, 'full mixed forcing')
        eq(poly(packet['A']), Ab[h], 'band A actual extraction')
        eq(poly(packet['B']), Bb[h], 'band B actual Euler extraction')
        for p in (forcing, Ab[h], Bb[h]):
            envelope(p, h, False)
        part = poly(packet['part'])
        envelope(part, h, False)
        if h <= 6:
            eq(part, solve_upper(h, {}, neg(forcing), 4), 'independent particular mate')
            basepair = residual_pair(add(oper(h, {}, part), forcing))
            basisV = [poly(p) for p in array(packet['basisV'], 3)]
            matrix = [[elt(v) for v in array(row, 3)] for row in array(packet['matrix'], 3)]
            inv = [[elt(v) for v in array(row, 3)] for row in array(packet['inverse'], 3)]
            actual_columns = []
            for j, Vj in enumerate(basisV):
                envelope(Vj, 0, False)
                Aj = pw(T, j)
                targetj = sc(pw(T, 6), -2) if h == 4 and j == 2 else {}
                eq(Vj, solve_upper(h, Aj, targetj, 4), 'independent homogeneous mate')
                rj = residual_pair(sub(oper(h, Aj, Vj), targetj))
                rhoj = sub(sc(co(Vj, 6, 0), n.fproduct(F(10), a)),
                           sc(co(Aj, 6, 0), n.fproduct(F(17), b)))
                actual_columns.append([value(rj[0]), value(rj[1]), value(rhoj)])
            eq(matrix, [[actual_columns[j][i] for j in range(3)] for i in range(3)], 'exact operator/rho matrix')
            det, deti = parsed_units['gap' + str(h) + ':det']
            eq(det, determinant(matrix), 'ACTUAL whole determinant inverse input')
            # Product checks both prove inverse and tie its actual use below.
            for left, right in ((matrix, inv), (inv, matrix)):
                for i in range(3):
                    for j in range(3):
                        got = F(0)
                        for k0 in range(3):
                            got = n.fsum(got, n.fproduct(left[i][k0], right[k0][j]))
                        eq(got, F(int(i == j)), 'two-sided whole matrix inverse')
            eq(n.fproduct(det, deti), F(1), 'determinant witness use')
            rho = poly(packet['rho'])
            envelope(rho, h)
            xyz = [co(Ab[h], 6, j) for j in range(3)]
            if any(ex[6] > 2 for ex in Ab[h]):
                raise ValueError('early A degree')
            rhs = [neg(basepair[0]), neg(basepair[1]), rho]
            for row, wanted in zip(matrix, rhs):
                eq(add(*(sc(x, c0) for c0, x in zip(row, xyz))), wanted, 'forward affine row map')
            for row, wanted in zip(inv, xyz):
                eq(add(*(sc(x, c0) for c0, x in zip(row, rhs))), wanted, 'inverse actually used')
            eq(Bb[h], add(part, *(mul(xyz[j], basisV[j]) for j in range(3))), 'complete affine mate')
            eq(sub(sc(co(sub(Bb[h], part), 6, 0), n.fproduct(F(10), a)),
                   sc(co(Ab[h], 6, 0), n.fproduct(F(17), b))), rho, 'rho particular subtraction')
            if h <= 4:
                eq(rho, sym(h - 1), 'literal normalized free Xi')
            else:
                ratio = Q(3 * (h - 3) - 2, 27 - h)
                eq(inv[2][2], n.fproduct(F(ratio), middle[h]), 'middle Phi/H7 relation')
                eq(xyz[2], {}, 'middle U2 zero')
                eq(co(Bb[h], 6, 4), {}, 'middle V4 zero')
                eq(xyz[1], sub(co(vp, 5, 6 - h), mul(U, co(dp, 5, 7 - h))), 'actual middle shift')
            if h <= 3:
                eq(xyz[2], co(dp, 5, 3 - h), 'early d readback')
                eq(xyz[1], co(vp, 5, 6 - h), 'early v readback')
            if h == 4:
                eq(xyz[2], neg(U), 'modified q=-U')
                eq(xyz[1], sub(co(vp, 5, 2), mul(U, co(dp, 5, 3))), 'modified affine l')
            eq(xyz[0], co(kp, 5, 10 - h), 'early/middle k readback')
            target = sc(mul(xyz[2], pw(T, 6)), -2) if h == 4 else {}
            eq(add(oper(h, Ab[h], Bb[h]), forcing, neg(target)), {}, 'complete early/middle band')
        else:
            apart, fixed, target, avar, tvar, vvar = [poly(packet[key]) for key in
                ('A_part', 'fixed', 'target', 'A_var', 'target_var', 'B_var')]
            for p in (apart, fixed, target):
                envelope(p, h, False)
            for p in (avar, tvar, vvar):
                envelope(p, 0, False)
            if h == 7:
                y = sub(z, mul(U, co(dp, 5, 0)))
                wanted = (mul(y, T), {}, sc(mul(z, pw(T, 5)), -2), C0(1), {})
                N = sub(sub(sc(mul(z, pw(T, 5)), -2), forcing),
                        mul(y, sub(sc(mul(T, der(D, 6)), 3), sc(D, 17))))
                for i in range(5):
                    eq(co(N, 6, i), add(neg(co(forcing, 6, i)),
                        sc(mul(y, co(D, 6, i)), 17 - 3 * i)), 'critical unshifted D_i')
            elif h == 8:
                wanted = ({}, mul(pw(U, 2), pw(T, 3)), neg(mul(pw(U, 2), pw(T, 5))), C0(1), {})
            elif h == 9:
                wanted = ({}, {}, {}, C0(1), {})
            else:
                wanted = ({}, {}, {}, {}, neg(pw(T, 4)))
            eq((apart, fixed, target, avar, tvar), wanted, 'literal critical/late/ell fixed forcing')
            eq(part, solve_upper(h, apart, sub(target, forcing), 2, fixed), 'independent column particular')
            eq(vvar, solve_upper(h, avar, tvar, 2), 'independent column variation')
            basepair = residual_pair(add(sub(oper(h, apart, part), target), forcing))
            col = residual_pair(sub(oper(h, avar, vvar), tvar))
            c1, c0 = [value(p) for p in col]
            eq([elt(v) for v in array(packet['column'], 2)], [c1, c0], 'literal full column')
            eq([poly(v) for v in array(packet['base'], 2)], basepair, 'actual forced base')
            l1, l0 = [elt(v) for v in array(packet['lambda'], 2)]
            eq(n.fsum(n.fproduct(l1, c1), n.fproduct(l0, c0)), F(1), 'whole column completion')
            if h == 7:
                invC2 = sc(series(c, Q(-2), 6), n.fproduct(W, W))
                expected = []
                for R in (T, C0(1)):
                    p = mul(pw(C, 2), integ(mul(R, invC2)))
                    expected.append(value(sub(sc(co(p, 6, 6), value(co(C, 6, 2))), sc(co(p, 6, 5), Q(1, 2)))))
                eq([l1, l0], expected, 'general critical Lambda specialized honestly')
            else:
                gg, _, vv = n.bezout(n.MODULUS, c1)
                hh, uu, ww = n.bezout(gg, c0)
                eq(hh, [Q(1)], 'independent column ideal unit')
                eq([l1, l0], [F(n.times(uu, vv)), F(ww)], 'independent Bezout representatives')
            val, psi = poly(packet['value']), poly(packet['Psi'])
            envelope(val, h)
            envelope(psi, h)
            eq(val, neg(add(sc(basepair[0], l1), sc(basepair[1], l0))), 'variable reconstruction')
            eq(psi, sub(sc(basepair[1], c1), sc(basepair[0], c0)), 'retained compatibility')
            eq(Ab[h], add(apart, mul(val, avar)), 'full affine A reconstruction')
            eq(Bb[h], add(part, mul(val, vvar)), 'full affine B reconstruction')
            eq(residual_pair(sub(add(oper(h, Ab[h], Bb[h]), forcing), add(target, mul(val, tvar)))),
               [sc(psi, n.fnegative(l0)), sc(psi, l1)], 'whole determinant-one residual pair')
            if h < 10:
                eq(val, co(kp, 5, 10 - h), 'critical/late source k readback')
            else:
                eq(val, E, 'ell elimination not gauge')
                fcoef, hcoef = value(co(C, 6, 2)), value(co(C, 6, 1))
                ge = n.fproduct(F(Q(1, 21)), n.fsum(n.fproduct(F(13), hcoef),
                     n.fnegative(n.fproduct(F(Q(24, 11)), n.fproduct(fcoef, fcoef)))))
                eq(vvar, add(pw(T, 2), sc(T, n.fproduct(F(Q(6, 11)), fcoef)), C0(ge)), 'r3 ell column')
            psis.append(psi)
            lambdas.append((l1, l0))

    # Independent COMPLETE Jacobian assembly from its coefficient pairs.
    J = {}
    for ak in range(4):
        for bl in range(6):
            if ak + bl:
                piece = sub(sc(mul(der(Ac[ak], 5), Bc[bl]), bl),
                            sc(mul(Ac[ak], der(Bc[bl], 5)), ak))
                J = add(J, move(piece, 6, ak + bl - 1))
    adjusted = sub(J, upper)
    envelope(adjusted, 23)
    if any(ex[6] > 7 or ex[5] > 23 - 3 * ex[6] for ex in adjusted):
        raise ValueError('Jacobian outside full support')
    keys(doc['raw'], 'Psi P1 P0 jacobian_slots')
    emitted = [poly(v) for v in array(doc['raw']['jacobian_slots'], 108)]
    slot = 0
    for j in range(8):
        for i in range(24 - 3 * j):
            actual = co(co(adjusted, 6, j), 5, i)
            eq(emitted[slot], actual, 'literal 108-slot readback')
            if j >= 2:
                eq(actual, {}, 'full upper equation')
            slot += 1
    eq(slot, 108, 'complete Jacobian slot inventory')
    eq([poly(v) for v in array(doc['raw']['Psi'], 4)], psis, 'all four raw compatibility slots')
    P1 = [poly(v) for v in array(doc['raw']['P1'], 21)]
    P0 = [poly(v) for v in array(doc['raw']['P0'], 24)]
    checked = 0
    for j, top, rows in ((1, 20, P1), (0, 23, P0)):
        for i in range(top + 1):
            actual = co(co(adjusted, 6, j), 5, i)
            eq(rows[i], actual, 'literal 45-slot low readback')
            envelope(rows[i], top - i)
            h = top - i
            if h <= 10:
                wanted = {} if h < 7 else sc(psis[h - 7],
                    n.fnegative(lambdas[h - 7][1]) if j == 1 else lambdas[h - 7][0])
                eq(actual, wanted, 'eliminated or compatibility readback')
            checked += 1
    eq(checked, 45, 'all low rows including zeros/duplicates')

    # BOTH complete inverse maps. S=P*q^3-z*q^2+U*q, theta=q^-1.
    # Here coordinate5 denotes new P and coordinate6 denotes q, not old theta.
    chartS = add(move(S, 6, 3), neg(move(z, 6, 2)), move(U, 6, 1))
    for source in (A, B):
        inverse_poly = {}
        for ex, val in source.items():
            coeffex = list(ex)
            coeffex[5] = coeffex[6] = 0
            term = mul({tuple(coeffex): val}, pw(chartS, ex[5]))
            inverse_poly = add(inverse_poly, move(term, 6, -ex[6], laurent=True))
        if any(ex[6] < 0 for ex in inverse_poly):
            raise ValueError('WHOLE inverse-polynomiality')
    eq(value(co(co(A, 6, 0), 5, 10)), Wi, 'original leading a after scale')
    eq(value(co(co(B, 6, 0), 5, 17)), n.inverse(t5), 'original leading b after scale')
    eq(n.fproduct(n.fproduct(W, t5), n.fproduct(Wi, n.inverse(t5))), F(1), 'omega*a*b=1')
    # Exact Laurent source-normalization back-map. Coordinate4 now denotes s,
    # NOT free z. The injection z -> s^2 is used, never z=1 or U^-1.
    def to_scale(p, divide_power=0, rescale_theta=False):
        out = {}
        for ex, val in p.items():
            key = list(ex)
            key[4] = 2 * ex[4] + (ex[6] if rescale_theta else 0) - divide_power
            out = add(out, {tuple(key): val})
        return out

    origA, origB = to_scale(A, 3, True), to_scale(B, 5, True)
    origd, origv, origk = to_scale(dp, 1), to_scale(vp, 2), to_scale(kp, 3)
    origu, origell = to_scale(U, 1), to_scale(E, 3)
    origPi = add(T, neg(mul(origu, pw(T, 2))), mul(S, pw(T, 3)))
    eq(origA, add(mul(S, pw(T, 3)), mul(sub(mul(S, origd), origu), pw(T, 2)),
                 mul(add(C0(1), neg(mul(origu, origd)), mul(S, origv)), T), origk),
       'literal source A inverse normalization')
    origUpper = neg(add(mul(mul(origell, T), origPi), mul(T, pw(origPi, 2))))
    eq(origUpper, to_scale(upper, 7, True), 'full source target inverse normalization')
    origJ = sub(mul(der(origA, 5), der(origB, 6)), mul(der(origA, 6), der(origB, 5)))
    eq(origJ, to_scale(J, 7, True), 'source bracket scaling')
    origResidual = sub(sub(origJ, origUpper), add(C0(1), mul(origu, T)))
    for i in range(21):
        wanted = to_scale(P1[i], 6)
        if i == 0:
            wanted = sub(wanted, origu)
        eq(co(co(origResidual, 6, 1), 5, i), wanted, 'all original t1 residuals and low target')
    for i in range(24):
        wanted = to_scale(P0[i], 7)
        if i == 0:
            wanted = sub(wanted, C0(1))
        eq(co(co(origResidual, 6, 0), 5, i), wanted, 'all original t0 residuals and low target')
    guard = move(C0(n.fproduct(W, t5)), 4, 8)
    orig_a = co(co(origA, 6, 0), 5, 10)
    orig_b = co(co(origB, 6, 0), 5, 17)
    eq(mul(guard, mul(orig_a, orig_b)), C0(1), 'literal Laurent omega*a*b guard')
    # Symbolic exponent checks in the actual unit scale, never s=1:
    eq(-3 - 5 + 8, 0, 'original top-product scale guard')
    eq(2 * 20 - (2 * 4 + 5 * 7), -3, 'first low w target exponent')
    eq(2 * 23 - 7 * 7, -3, 'second low w target exponent')
    # Both targets are three powers higher: w^40*(L1-U0*w^3),
    # w^46*(L0-w^3). Their compatibility is L1-U0*L0, not L1 alone.

    keys(doc['graph'], 'Hq c c_inverse zeta slots ell g U')
    graph = doc['graph']
    Hq = co(psis[0], 4, 0)
    critical_c = value(co(psis[0], 4, 1))
    eq(psis[0], add(Hq, sc(z, critical_c)), 'complete Psi7=Hq+c*z')
    ci = n.inverse(critical_c)
    eq(parsed_units['critical_c'], (critical_c, ci), 'critical inverse actual use')
    eq(elt(graph['c']), critical_c, 'critical c literal')
    eq(elt(graph['c_inverse']), ci, 'critical inverse literal')
    zeta = sc(Hq, n.fnegative(ci))
    eq(poly(graph['Hq'], True), Hq, 'Hq literal')
    eq(poly(graph['zeta'], True), zeta, 'graph substitution literal')
    eq(n.substitute_graph(psis[0], zeta), {}, 'critical graph equation')
    wanted = [n.substitute_graph(p, zeta) for p in psis[1:] + P1[1:10] + P0[1:13]]
    mixed = sub(mul(z, P1[0]), mul(U, P0[0]))
    wanted.append(n.substitute_graph(mixed, zeta))
    actual = [poly(v, True) for v in array(graph['slots'], 25)]
    for label, p, w, rawrow in zip(names, actual,
            [8, 9, 10] + list(range(19, 10, -1)) + list(range(22, 10, -1)) + [27], wanted):
        eq(p, rawrow, 'all25 literal graph rows ' + label)
        envelope(p, w)
    ell = n.substitute_graph(P0[0], zeta)
    g = mul(Hq, ell)
    eq(poly(graph['ell'], True), ell, 'literal ell')
    eq(poly(graph['g'], True), g, 'literal guarded target g')
    eq(poly(graph['U'], True), U, 'U_* graph readback')
    envelope(ell, 23)
    envelope(g, 30)
    # Graph guard: zeta*ell=-c^-1*g, preserving the open scheme.
    eq(mul(zeta, ell), sc(g, n.fnegative(ci)), 'critical localization guard identity')
    return 'CHECKED_R3_25_GRAPH_SLOTS_45_LOW_108_JACOBIAN_NO_SOURCE_OUTCOME'


def main():
    path = authorize('check')
    print(check_file(path))


if __name__ == '__main__':
    main()
