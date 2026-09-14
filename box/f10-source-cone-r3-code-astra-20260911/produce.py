"""STATIC r3 complete reconstruction producer. Never a membership solver."""
from authority import authorize


def build():
    import arithmetic as m
    from arithmetic import (Q, qa, qs, qm, field, const, var, add, sub, neg, mul,
                            scale, power, diff, coeff, shift, series, integrate,
                            scalar, equal, wire_p, wire_f, wire_q)
    m.UNITS.clear()
    m.WIRE_TERMS = 0
    tau = Q(3, 10)
    dl = [(1 + tau) * (2 - 3 * tau), -12 * (1 - tau), Q(12)]
    kl = [2 * (2 - 3 * tau) * (1 + tau) * (2 + tau) * (3 + tau),
          42 * (1 + tau) * (2 + tau) * (4 * tau - 3),
          840 * (1 - tau * tau), Q(-840)]
    ga = [tau * (1 + tau) * (2 + tau) * (3 + tau),
          -30 * tau * (1 + tau) * (2 + tau), 180 * tau * (1 + tau), -120 * tau]
    septic = qa(qa(qs(qm(kl, kl), Q(2)),
                    qs(qm(qm([1 + tau, Q(-6)], kl), dl), -140 * tau)),
                qs(qm(ga, qm(dl, dl)), Q(245)))
    lead = -245 * 120 * 144 * tau
    equal(len(septic), 8, 'septic degree')
    equal(septic[-1], lead, 'literal septic leading coefficient')
    m.P7 = qs(septic, 1 / lead)
    dL, KL, gamma = field(dl), field(kl), field(ga)
    W = m.fm(field(Q(-1, 210)), m.fm(KL, m.fi(dL, 'dL')))
    Wi = m.fi(W, 'W')
    T, S, z = var(6), var(5), var(4)
    c = add(const(1), T, scale(power(T, 2), field([0, 1])), scale(power(T, 3), W))
    ts = series(c, Q(17, 10), 7)
    t5 = scalar(coeff(ts, 6, 5))
    t5i = m.fi(t5, 't5')
    middle, middle_i = {}, {}
    for h in (5, 6):
        middle[h] = scalar(coeff(series(c, Q(27 - h, 10), 7), 6, 7))
        middle_i[h] = m.fi(middle[h], 'middleH7:' + str(h))
    C, D = scale(c, Wi), scale(m.truncate(ts, 6, 5), t5i)
    equal(add(scale(mul(C, diff(D, 6)), 10), scale(mul(diff(C, 6), D), -17)),
          neg(power(T, 7)), 'leading ODE')
    equal(coeff(ts, 6, 6), {}, 'leading contact6')
    equal(coeff(ts, 6, 7), {}, 'leading contact7')
    a, F, H = [scalar(coeff(C, 6, j)) for j in (0, 2, 1)]
    b = scalar(coeff(D, 6, 0))

    def op(h, A, B):
        return add(scale(mul(C, diff(B, 6)), 10),
                   scale(mul(diff(C, 6), B), -(17 - h)),
                   scale(mul(A, diff(D, 6)), 10 - h),
                   scale(mul(diff(A, 6), D), -17))

    def upper(h, A, target, degree, fixed=None):
        V = {} if fixed is None else fixed
        for j in range(degree, -1, -1):
            residual = sub(op(h, A, V), target)
            pivot = 10 * j - 3 * (17 - h)
            if not pivot:
                raise ValueError('unlicensed band resonance')
            V = add(V, shift(scale(coeff(residual, 6, j + 2), Q(-1, pivot)), 6, j))
        residual = sub(op(h, A, V), target)
        if any(e[6] >= 2 for e in residual):
            raise ValueError('upper band row omitted')
        return V, [coeff(residual, 6, 1), coeff(residual, 6, 0)]

    Ab, Bb, packets, psis, witnesses = [C], [D], [], [], []
    Uglobal = {}
    for h in range(1, 11):
        forcing = {}
        for i in range(1, h):
            forcing = add(forcing,
                          scale(mul(Ab[i], diff(Bb[h - i], 6)), 10 - i),
                          scale(mul(diff(Ab[i], 6), Bb[h - i]), -(17 - h + i)))
        if h <= 6:
            part, base = upper(h, {}, neg(forcing), 4)
            basisV, columns = [], []
            for j in range(3):
                Aj = power(T, j)
                target = scale(power(T, 6), -2) if h == 4 and j == 2 else {}
                Vj, rj = upper(h, Aj, target, 4)
                rhoj = sub(scale(coeff(Vj, 6, 0), m.fm(field(10), a)),
                           scale(coeff(Aj, 6, 0), m.fm(field(17), b)))
                basisV.append(Vj)
                columns.append([scalar(rj[0]), scalar(rj[1]), scalar(rhoj)])
            matrix = [[columns[j][i] for j in range(3)] for i in range(3)]
            inverse = m.invert_matrix(matrix, 'gap' + str(h))
            rho = var(h - 1) if h <= 4 else {}
            xyz = m.apply_matrix(inverse, [neg(base[0]), neg(base[1]), rho])
            if h in (5, 6):
                ratio = Q(3 * (h - 3) - 2, 27 - h)
                equal(inverse[2][2], m.fm(field(ratio), middle[h]), 'middle H7/Phi coefficient')
                rho = scale(xyz[2], m.fm(field(-1 / ratio), middle_i[h]))
                xyz = m.apply_matrix(inverse, [neg(base[0]), neg(base[1]), rho])
            A = add(*(shift(xyz[j], 6, j) for j in range(3)))
            V = add(part, *(mul(xyz[j], basisV[j]) for j in range(3)))
            target = scale(mul(xyz[2], power(T, 6)), -2) if h == 4 else {}
            equal(add(op(h, A, V), forcing, neg(target)), {}, 'early/middle full residual')
            equal(sub(scale(coeff(sub(V, part), 6, 0), m.fm(field(10), a)),
                      scale(coeff(A, 6, 0), m.fm(field(17), b))), rho, 'homogeneous rho')
            if h in (5, 6):
                equal(xyz[2], {}, 'middle U2')
                equal(coeff(V, 6, 4), {}, 'middle V4')
            if h == 4:
                Uglobal = neg(xyz[2])
            packets.append({'kind': 'early' if h <= 4 else 'middle', 'gap': str(h),
                'forcing': wire_p(forcing), 'part': wire_p(part),
                'basisV': [wire_p(v) for v in basisV],
                'matrix': [[wire_f(v) for v in row] for row in matrix],
                'inverse': [[wire_f(v) for v in row] for row in inverse],
                'rho': wire_p(rho), 'A': wire_p(A), 'B': wire_p(V)})
        else:
            if h == 7:
                d0 = coeff(Ab[3], 6, 2)
                Apart = mul(sub(z, mul(Uglobal, d0)), T)
                target = scale(mul(z, power(T, 5)), -2)
                fixed, Avar, targetvar = {}, const(1), {}
            elif h == 8:
                Apart = {}
                target = neg(mul(power(Uglobal, 2), power(T, 5)))
                fixed = mul(power(Uglobal, 2), power(T, 3))
                Avar, targetvar = const(1), {}
            elif h == 9:
                Apart, target, fixed = {}, {}, {}
                Avar, targetvar = const(1), {}
            else:
                Apart, target, fixed = {}, {}, {}
                Avar, targetvar = {}, neg(power(T, 4))
            Vpart, base = upper(h, Apart, sub(target, forcing), 2, fixed)
            Vvar, col = upper(h, Avar, targetvar, 2)
            c1, c0 = scalar(col[0]), scalar(col[1])
            if h == 7:
                invC2 = scale(series(c, Q(-2), 6), m.fm(W, W))
                lams = []
                for R in (T, const(1)):
                    P = mul(power(C, 2), integrate(mul(R, invC2)))
                    lams.append(scalar(sub(scale(coeff(P, 6, 6), F),
                                           scale(coeff(P, 6, 5), Q(1, 2)))))
                l1, l0 = lams
            else:
                l1, l0 = m.completion(c1, c0)
            equal(m.fa(m.fm(l1, c1), m.fm(l0, c0)), field(1), 'determinant-one column')
            value = neg(add(scale(base[0], l1), scale(base[1], l0)))
            psi = sub(scale(base[1], c1), scale(base[0], c0))
            A, V = add(Apart, mul(value, Avar)), add(Vpart, mul(value, Vvar))
            residual = sub(add(op(h, A, V), forcing), add(target, mul(value, targetvar)))
            equal(residual, add(shift(scale(psi, m.fn(l0)), 6, 1), scale(psi, l1)),
                  'column full pair readback')
            psis.append(psi)
            witnesses.append((l1, l0))
            if h == 10:
                Eglobal = value
                ge = m.fm(field(Q(1, 21)), m.fa(m.fm(field(13), H),
                         m.fn(m.fm(field(Q(24, 11)), m.fm(F, F)))))
                equal(Vvar, add(power(T, 2), scale(T, m.fm(field(Q(6, 11)), F)), const(ge)),
                      'r3 ell literal column')
            packets.append({'kind': 'column', 'gap': str(h), 'forcing': wire_p(forcing),
                'part': wire_p(Vpart), 'A_part': wire_p(Apart), 'fixed': wire_p(fixed),
                'target': wire_p(target), 'A_var': wire_p(Avar), 'target_var': wire_p(targetvar),
                'B_var': wire_p(Vvar), 'column': [wire_f(c1), wire_f(c0)],
                'lambda': [wire_f(l1), wire_f(l0)], 'base': [wire_p(v) for v in base],
                'value': wire_p(value), 'Psi': wire_p(psi), 'A': wire_p(A), 'B': wire_p(V)})
        Ab.append(A)
        Bb.append(V)

    def install(bands, weight):
        out = {}
        for h, band in enumerate(bands):
            for e, cc in band.items():
                f = list(e)
                f[5] = weight - h - 3 * e[6]
                if f[5] < 0:
                    raise ValueError('negative source S exponent')
                out = add(out, {tuple(f): cc})
        return out

    Ahat = install(Ab, 10)
    Dpar = shift(add(coeff(Ahat, 6, 2), Uglobal), 5, -1)
    Vpar = shift(add(coeff(Ahat, 6, 1), neg(z), mul(Uglobal, Dpar)), 5, -1)
    Kpar = coeff(Ahat, 6, 0)
    Pihat = add(mul(z, T), neg(mul(Uglobal, power(T, 2))), mul(S, power(T, 3)))
    upperDelta = neg(add(mul(mul(Eglobal, T), Pihat), mul(T, power(Pihat, 2))))
    aa = [coeff(Ahat, 6, j) for j in range(4)]
    bb = [{} for _ in range(9)]
    bb[5] = power(S, 2)
    for j in range(4, -1, -1):
        q = add(coeff(upperDelta, 6, j + 2),
                scale(mul(diff(aa[2], 5), bb[j + 1]), -(j + 1)),
                scale(mul(aa[2], diff(bb[j + 1], 5)), 2),
                scale(mul(diff(aa[1], 5), bb[j + 2]), -(j + 2)),
                mul(aa[1], diff(bb[j + 2], 5)),
                scale(mul(diff(aa[0], 5), bb[j + 3]), -(j + 3)))
        for e, cc in q.items():
            pivot = j - 3 * e[5]
            if not pivot:
                raise ValueError('nonzero Euler resonance')
            bb[j][e] = m.fm(cc, field(Q(1, pivot)))
    Bhat = add(*(shift(bb[j], 6, j) for j in range(6)))
    for h in range(11):
        band = {}
        for e, cc in Bhat.items():
            if e[5] + 3 * e[6] == 17 - h:
                f = list(e)
                f[5] = 0
                band[tuple(f)] = cc
        equal(band, Bb[h], 'whole Euler/band equality')
    J = sub(mul(diff(Ahat, 5), diff(Bhat, 6)), mul(diff(Ahat, 6), diff(Bhat, 5)))
    adjusted = sub(J, upperDelta)

    def envelope(p, weight):
        for ex in p:
            if sum(x * y for x, y in zip(ex, (1, 2, 3, 4, 7, 1, 3))) != weight:
                raise ValueError('homogeneous envelope')

    for obj, w in ((Ahat, 10), (Bhat, 17), (Dpar, 3), (Vpar, 6),
                   (Kpar, 10), (Uglobal, 4), (Eglobal, 10), (Pihat, 10), (adjusted, 23)):
        envelope(obj, w)
    jacobian_slots = []
    for j in range(8):
        for i in range(24 - 3 * j):
            actual = coeff(coeff(adjusted, 6, j), 5, i)
            if j >= 2:
                equal(actual, {}, 'complete upper Jacobian slot')
            jacobian_slots.append(actual)
    equal(len(jacobian_slots), 108, 'Jacobian inventory')
    if any(e[6] > 7 or e[5] > 23 - 3 * e[6] for e in adjusted):
        raise ValueError('outside Jacobian support')
    P1 = [coeff(coeff(adjusted, 6, 1), 5, i) for i in range(21)]
    P0 = [coeff(coeff(adjusted, 6, 0), 5, i) for i in range(24)]
    for h in range(11):
        for j, top, rows in ((1, 20, P1), (0, 23, P0)):
            expected = {} if h < 7 else scale(psis[h - 7],
                m.fn(witnesses[h - 7][1]) if j == 1 else witnesses[h - 7][0])
            equal(rows[top - h], expected, '45-slot band readback')
    for h, p in zip(range(7, 11), psis):
        envelope(p, h)
    # Whole inverse charts, with physical theta reused as q and S as new P.
    chartS = add(shift(S, 6, 3), neg(shift(z, 6, 2)), shift(Uglobal, 6, 1))
    for obj in (Ahat, Bhat):
        inverse_poly = {}
        for ex, cc in obj.items():
            e = list(ex)
            e[5] = e[6] = 0
            term = mul({tuple(e): cc}, power(chartS, ex[5]))
            inverse_poly = add(inverse_poly, shift(term, 6, -ex[6], laurent=True))
        if any(e[6] < 0 for e in inverse_poly):
            raise ValueError('full inverse-polynomiality')
    equal(scalar(coeff(coeff(Ahat, 6, 0), 5, 10)), Wi, 'source leading a')
    equal(scalar(coeff(coeff(Bhat, 6, 0), 5, 17)), t5i, 'source leading b')
    equal(m.fm(m.fm(W, t5), m.fm(Wi, t5i)), field(1), 'original guard')
    Hq = coeff(psis[0], 4, 0)
    critical_c = scalar(coeff(psis[0], 4, 1))
    equal(psis[0], add(Hq, scale(z, critical_c)), 'whole critical graph shape')
    critical_ci = m.fi(critical_c, 'critical_c')
    zeta = scale(Hq, m.fn(critical_ci))
    graph_rows = [m.substitute_z(p, zeta) for p in psis[1:] + P1[1:10] + P0[1:13]]
    mixed = sub(mul(z, P1[0]), mul(Uglobal, P0[0]))
    graph_rows.append(m.substitute_z(mixed, zeta))
    ell = m.substitute_z(P0[0], zeta)
    g = mul(Hq, ell)
    for p, w in zip(graph_rows, [8, 9, 10] + list(range(19, 10, -1)) + list(range(22, 10, -1)) + [27]):
        envelope(p, w)
    envelope(ell, 23)
    envelope(g, 30)
    equal(m.substitute_z(psis[0], zeta), {}, 'critical row eliminated')
    names = ['K8', 'K9', 'K10'] + ['A1_' + str(i) for i in range(1, 10)] + ['A0_' + str(i) for i in range(1, 13)] + ['T']
    return {'format': 'r3-source-cone-reconstruction-v1', 'job_tag': 'f10-source-cone-r3-reconstruction-v1',
        'interface': {'raw_variables': ['X1', 'X2', 'X3', 'X4', 'z', 'S', 'theta'],
            'raw_weights': ['1', '2', '3', '4', '7', '1', '3'],
            'graph_variables': ['X1', 'X2', 'X3', 'X4'], 'graph_weights': ['1', '2', '3', '4'],
            'base': 'WHOLE Q[V]/P7; basis 1,V,...,V^6', 'scale': 'z=s^2; s invertible',
            'targets': ['P1_0-U*s^5', 'P0_0-s^7'], 'guard': 'omega=W*t5*s^8',
            'graph_guard': 'g=Hq*ell', 'graph_rows': names,
            'jacobian_order': 'j=0..7;i=0..23-3j', 'low_order': 'P1:i=0..20;P0:i=0..23'},
        'base': {'P7': [wire_q(v) for v in m.P7], 'dL': wire_f(dL), 'KL': wire_f(KL),
            'gamma': wire_f(gamma), 'W': wire_f(W), 't5': wire_f(t5),
            'middleH7': [wire_f(middle[h]) for h in (5, 6)], 'C': wire_p(C), 'D': wire_p(D),
            'units': {k: [wire_f(v[0]), wire_f(v[1])] for k, v in sorted(m.UNITS.items())}},
        'source': {k: wire_p(v) for k, v in {'Ahat': Ahat, 'Bhat': Bhat, 'U': Uglobal,
            'E': Eglobal, 'Dpar': Dpar, 'Vpar': Vpar, 'Kpar': Kpar, 'Pihat': Pihat}.items()},
        'bands': packets,
        'raw': {'Psi': [wire_p(v) for v in psis], 'P1': [wire_p(v) for v in P1],
            'P0': [wire_p(v) for v in P0], 'jacobian_slots': [wire_p(v) for v in jacobian_slots]},
        'graph': {'Hq': wire_p(Hq, True), 'c': wire_f(critical_c), 'c_inverse': wire_f(critical_ci),
            'zeta': wire_p(zeta, True), 'slots': [wire_p(v, True) for v in graph_rows],
            'ell': wire_p(ell, True), 'g': wire_p(g, True), 'U': wire_p(Uglobal, True)}}


def main():
    path = authorize('produce')
    import json
    payload = build()
    raw = (json.dumps(payload, ensure_ascii=True, sort_keys=True, separators=(',', ':')) + '\n').encode('ascii')
    if len(raw) > 134217728:
        raise SystemExit('REFUSED: output byte cap')
    with open(path, 'xb') as stream:
        stream.write(raw)
    print('FORMED_UNCHECKED_R3_25_SLOTS_NO_SOURCE_OUTCOME')


if __name__ == '__main__':
    main()
