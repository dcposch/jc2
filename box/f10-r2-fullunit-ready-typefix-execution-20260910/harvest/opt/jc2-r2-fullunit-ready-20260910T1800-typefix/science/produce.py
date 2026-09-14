"""STATIC r2 19-row coefficient producer. No solver and no source verdict."""
from authority import authorize


def build():
    import arithmetic as m
    from arithmetic import (Q, qa, qs, qm, field, const, var, add, sub, neg, mul,
                            scale, power, diff, coeff, shift, series, integrate,
                            scalar, equal, wire_p, wire_f, wire_q)
    m.UNITS.clear()
    m.WIRE_TERMS = 0

    def qp(a, n):
        r = [Q(1)]
        for _ in range(n):
            r = qm(r, a)
        return r

    tau = Q(2, 7)
    dl = [(1 + tau) * (2 - 3 * tau), -12 * (1 - tau), Q(12)]
    kl = [2 * (2 - 3 * tau) * (1 + tau) * (2 + tau) * (3 + tau),
          42 * (1 + tau) * (2 + tau) * (4 * tau - 3),
          840 * (1 - tau * tau), Q(-840)]
    ga = [tau * (1 + tau) * (2 + tau) * (3 + tau),
          -30 * tau * (1 + tau) * (2 + tau), 180 * tau * (1 + tau), -120 * tau]
    septic = qa(qa(qs(qp(kl, 2), Q(2)),
                    qs(qm(qm([1 + tau, Q(-6)], kl), dl), -140 * tau)),
                qs(qm(ga, qp(dl, 2)), Q(245)))
    lead = -245 * 120 * 144 * tau
    if len(septic) != 8 or septic[-1] != lead:
        raise ValueError('literal septic leading coefficient')
    m.P7 = qs(septic, 1 / lead)
    dL, KL, gamma = field(dl), field(kl), field(ga)
    dLi = m.fi(dL, 'dL')
    W = m.fm(field(Q(-1, 210)), m.fm(KL, dLi))
    Wi = m.fi(W, 'W')
    T, S, z = var(5), var(4), var(3)
    c = add(const(1), T, scale(power(T, 2), field([0, 1])), scale(power(T, 3), W))
    nu_series = series(c, Q(12, 7), 7)
    t5 = scalar(coeff(nu_series, 5, 5))
    t5i = m.fi(t5, 't5')
    H7 = scalar(coeff(series(c, Q(15, 7), 7), 5, 7))
    H7i = m.fi(H7, 'H7')
    C = scale(c, Wi)
    D = scale(m.truncate(nu_series, 5, 5), t5i)
    equal(add(scale(mul(C, diff(D, 5)), 7), scale(mul(diff(C, 5), D), -12)),
          neg(power(T, 7)), 'leading ODE')
    a, F, H = scalar(coeff(C, 5, 0)), scalar(coeff(C, 5, 2)), scalar(coeff(C, 5, 1))
    b = scalar(coeff(D, 5, 0))

    def op(h, A, B):
        return add(scale(mul(C, diff(B, 5)), 7),
                   scale(mul(diff(C, 5), B), -(12 - h)),
                   scale(mul(A, diff(D, 5)), 7 - h),
                   scale(mul(diff(A, 5), D), -12))

    def upper(h, A, target, degree, fixed=None):
        V = {} if fixed is None else fixed
        for j in range(degree, -1, -1):
            residual = sub(op(h, A, V), target)
            pivot = 7 * j - 3 * (12 - h)
            if not pivot:
                raise ValueError('unlicensed band resonance')
            q = scale(coeff(residual, 5, j + 2), Q(-1, pivot))
            V = add(V, shift(q, 5, j))
        residual = sub(op(h, A, V), target)
        if any(e[5] >= 2 for e in residual):
            raise ValueError('upper band row omitted')
        return V, [coeff(residual, 5, 1), coeff(residual, 5, 0)]

    Ab, Bb, packets, psis, witnesses = [C], [D], [], [], []
    Uglobal = {}
    for h in range(1, 8):
        forcing = {}
        for i in range(1, h):
            forcing = add(forcing,
                          scale(mul(Ab[i], diff(Bb[h - i], 5)), 7 - i),
                          scale(mul(diff(Ab[i], 5), Bb[h - i]), -(12 - h + i)))
        if h <= 4:
            part, base = upper(h, {}, neg(forcing), 4)
            basisV, columns = [], []
            for j in range(3):
                Aj = power(T, j)
                target = scale(power(T, 6), -2) if h == 3 and j == 2 else {}
                Vj, rj = upper(h, Aj, target, 4)
                rhoj = sub(scale(coeff(Vj, 5, 0), m.fm(field(7), a)),
                           scale(coeff(Aj, 5, 0), m.fm(field(12), b)))
                basisV.append(Vj)
                columns.append([scalar(rj[0]), scalar(rj[1]), scalar(rhoj)])
            matrix = [[columns[j][i] for j in range(3)] for i in range(3)]
            inverse = m.invert_matrix(matrix, 'gap' + str(h))
            rho = var(h - 1) if h < 4 else {}
            xyz = m.apply_matrix(inverse, [neg(base[0]), neg(base[1]), rho])
            if h == 4:
                # Phi_4 gives U_2=(4/15)(H7*rho+J4).
                if inverse[2][2] != m.fm(field(Q(4, 15)), H7):
                    raise ValueError('middle H7/Phi coefficient')
                rho = scale(xyz[2], m.fm(field(Q(-15, 4)), H7i))
                xyz = m.apply_matrix(inverse, [neg(base[0]), neg(base[1]), rho])
            A = add(*(shift(xyz[j], 5, j) for j in range(3)))
            V = add(part, *(mul(xyz[j], basisV[j]) for j in range(3)))
            target = scale(mul(xyz[2], power(T, 6)), -2) if h == 3 else {}
            residual = add(op(h, A, V), forcing, neg(target))
            equal(residual, {}, 'early/middle full residual')
            equal(sub(scale(coeff(sub(V, part), 5, 0), m.fm(field(7), a)),
                      scale(coeff(A, 5, 0), m.fm(field(12), b))), rho,
                  'homogeneous rho including particular subtraction')
            if h == 4:
                equal(xyz[2], {}, 'middle U2')
                equal(coeff(V, 5, 4), {}, 'middle V4')
            if h == 3:
                Uglobal = neg(xyz[2])
            packets.append({'kind': 'early' if h < 4 else 'middle', 'gap': str(h),
                            'forcing': wire_p(forcing), 'part': wire_p(part),
                            'basisV': [wire_p(v) for v in basisV],
                            'matrix': [[wire_f(v) for v in row] for row in matrix],
                            'inverse': [[wire_f(v) for v in row] for row in inverse],
                            'rho': wire_p(rho), 'A': wire_p(A), 'B': wire_p(V)})
        else:
            if h == 5:
                d0 = coeff(Ab[2], 5, 2)
                y = sub(z, mul(Uglobal, d0))
                Apart = mul(y, T)
                target = scale(mul(z, power(T, 5)), -2)
                fixed = {}
                Avar, targetvar = const(1), {}
            elif h == 6:
                Apart = {}
                target = neg(mul(power(Uglobal, 2), power(T, 5)))
                fixed = mul(power(Uglobal, 2), power(T, 3))
                Avar, targetvar = const(1), {}
            else:
                Apart, target, fixed = {}, {}, {}
                Avar, targetvar = {}, neg(power(T, 4))
            Vpart, base = upper(h, Apart, sub(target, forcing), 2, fixed)
            Vvar, col = upper(h, Avar, targetvar, 2)
            c1, c0 = scalar(col[0]), scalar(col[1])
            if h == 5:
                invC2 = scale(series(c, Q(-2), 6), m.fm(W, W))
                lams = []
                for R in (T, const(1)):
                    P = mul(power(C, 2), integrate(mul(R, invC2)))
                    lams.append(scalar(sub(scale(coeff(P, 5, 6), F),
                                           scale(coeff(P, 5, 5), Q(1, 2)))))
                l1, l0 = lams
            else:
                l1, l0 = m.completion(c1, c0)
            if m.fa(m.fm(l1, c1), m.fm(l0, c0)) != field(1):
                raise ValueError('determinant-one column')
            value = neg(add(scale(base[0], l1), scale(base[1], l0)))
            psi = sub(scale(base[1], c1), scale(base[0], c0))
            A, V = add(Apart, mul(value, Avar)), add(Vpart, mul(value, Vvar))
            residual = sub(add(op(h, A, V), forcing), add(target, mul(value, targetvar)))
            equal(residual, add(shift(scale(psi, m.fn(l0)), 5, 1), scale(psi, l1)),
                  'column full pair readback')
            psis.append(psi)
            witnesses.append((l1, l0))
            if h == 7:
                Eglobal = value
                ge = m.fm(field(Q(1, 10)), m.fa(m.fm(field(6), H), m.fn(m.fm(F, F))))
                equal(Vvar, add(power(T, 2), scale(T, m.fm(field(Q(1, 2)), F)), const(ge)),
                      'ell literal affine column')
            packets.append({'kind': 'column', 'gap': str(h), 'forcing': wire_p(forcing),
                            'part': wire_p(Vpart), 'A_part': wire_p(Apart),
                            'fixed': wire_p(fixed), 'target': wire_p(target),
                            'A_var': wire_p(Avar), 'target_var': wire_p(targetvar),
                            'B_var': wire_p(Vvar), 'column': [wire_f(c1), wire_f(c0)],
                            'lambda': [wire_f(l1), wire_f(l0)],
                            'base': [wire_p(v) for v in base], 'value': wire_p(value),
                            'Psi': wire_p(psi), 'A': wire_p(A), 'B': wire_p(V)})
        Ab.append(A)
        Bb.append(V)

    def install(bands, weight):
        out = {}
        for h, band in enumerate(bands):
            for e, cc in band.items():
                f = list(e)
                f[4] = weight - h - 2 * e[5]
                if f[4] < 0:
                    raise ValueError('negative source S exponent')
                out = add(out, {tuple(f): cc})
        return out

    Ahat = install(Ab, 7)
    Dpar = shift(add(coeff(Ahat, 5, 2), Uglobal), 4, -1)
    Vpar = shift(add(coeff(Ahat, 5, 1), neg(z), mul(Uglobal, Dpar)), 4, -1)
    Kpar = coeff(Ahat, 5, 0)
    Pihat = add(mul(z, T), neg(mul(Uglobal, power(T, 2))), mul(S, power(T, 3)))
    upperDelta = neg(add(mul(mul(Eglobal, T), Pihat), mul(T, power(Pihat, 2))))
    aa = [coeff(Ahat, 5, j) for j in range(4)]
    bb = [{} for _ in range(9)]
    bb[5] = power(S, 2)
    for j in range(4, -1, -1):
        q = add(coeff(upperDelta, 5, j + 2),
                scale(mul(diff(aa[2], 4), bb[j + 1]), -(j + 1)),
                scale(mul(aa[2], diff(bb[j + 1], 4)), 2),
                scale(mul(diff(aa[1], 4), bb[j + 2]), -(j + 2)),
                mul(aa[1], diff(bb[j + 2], 4)),
                scale(mul(diff(aa[0], 4), bb[j + 3]), -(j + 3)))
        for e, cc in q.items():
            pivot = j - 3 * e[4]
            if not pivot:
                raise ValueError('nonzero Euler resonance')
            bb[j][e] = m.fm(cc, field(Q(1, pivot)))
    Bhat = add(*(shift(bb[j], 5, j) for j in range(6)))
    for h in range(8):
        band = {}
        for e, cc in Bhat.items():
            if e[4] + 2 * e[5] == 12 - h:
                f = list(e)
                f[4] = 0
                band[tuple(f)] = cc
        equal(band, Bb[h], 'whole Euler/band equality')
    J = sub(mul(diff(Ahat, 4), diff(Bhat, 5)), mul(diff(Ahat, 5), diff(Bhat, 4)))
    K = sub(J, upperDelta)
    for e in K:
        if e[5] >= 2:
            raise ValueError('full upper Jacobian')
    for h in range(8):
        for j, top in ((1, 14), (0, 16)):
            r = coeff(coeff(K, 5, j), 4, top - h)
            expected = {} if h < 5 else scale(psis[h - 5],
                       m.fn(witnesses[h - 5][1]) if j == 1 else witnesses[h - 5][0])
            equal(r, expected, '32-slot eliminated/readback pair')

    def envelope(p, weight, physical=True):
        for ex in p:
            got = ex[0] + 2 * ex[1] + 3 * ex[2] + 5 * ex[3]
            if physical:
                got += ex[4] + 2 * ex[5]
            elif ex[4]:
                raise ValueError('band S support')
            if got != weight or any(i > 16 for i in ex):
                raise ValueError('weighted/support envelope')

    for obj, w in ((Ahat, 7), (Bhat, 12), (Dpar, 2), (Vpar, 4), (Kpar, 7),
                   (Uglobal, 3), (Eglobal, 7), (Pihat, 7)):
        envelope(obj, w)
    for h, p in zip((5, 6, 7), psis):
        envelope(p, h)
    K1 = [coeff(coeff(K, 5, 1), 4, i) for i in range(7)]
    K0 = [coeff(coeff(K, 5, 0), 4, i) for i in range(9)]
    for i, p in enumerate(K1):
        envelope(p, 14 - i)
    for i, p in enumerate(K0):
        envelope(p, 16 - i)
    return {'format': 'r2-reconstruction-19-v1', 'job_tag': 'f10-r2-reconstruction-v1',
            'interface': {'variables': ['X1', 'X2', 'X3', 'z', 'S', 'vartheta'],
                          'weights': ['1', '2', '3', '5', '1', '2'],
                          'base': 'Q[Z]/P7', 'basis': ['0', '1', '2', '3', '4', '5', '6'],
                          'scale': 'z=s^2; s invertible',
                          'targets': ['K1_0-U*s^5', 'K0_0-s^7'],
                          'guard': 'omega=W*t5*s^8',
                          'rows': ['Psi5', 'Psi6', 'Psi7'] +
                                  ['K1_' + str(i) for i in range(1, 7)] +
                                  ['K0_' + str(i) for i in range(1, 9)] +
                                  ['K1_0-U*s^5', 'K0_0-s^7']},
            'field': {'P7': [wire_q(v) for v in m.P7], 'dL': wire_f(dL), 'KL': wire_f(KL),
                      'gamma': wire_f(gamma), 'W': wire_f(W), 't5': wire_f(t5),
                      'H7': wire_f(H7), 'C': wire_p(C), 'D': wire_p(D),
                      'units': {k: [wire_f(v[0]), wire_f(v[1])] for k, v in sorted(m.UNITS.items())}},
            'source': {k: wire_p(v) for k, v in {'Ahat': Ahat, 'Bhat': Bhat, 'U': Uglobal,
                      'E': Eglobal, 'Dpar': Dpar, 'Vpar': Vpar, 'Kpar': Kpar,
                      'Pihat': Pihat}.items()},
            'bands': packets,
            'rows': {'Psi': [wire_p(v) for v in psis], 'K1': [wire_p(v) for v in K1],
                     'K0': [wire_p(v) for v in K0]}}


def main():
    path = authorize('produce')
    import json
    payload = build()
    raw = (json.dumps(payload, ensure_ascii=True, sort_keys=True, separators=(',', ':')) + '\n').encode('ascii')
    if len(raw) > 15728640:
        raise SystemExit('REFUSED: artifact byte cap')
    # Exclusive publication: no existing coefficient artifact is overwritten.
    with open(path, 'xb') as f:
        f.write(raw)
    print('FORMED_UNCHECKED_19_ROWS_NO_SOURCE_OUTCOME')


if __name__ == '__main__':
    main()
