"""STATIC candidate producer: one exact B[u] Bezout identity, no source outcome."""
from entry import enter, arithmetic, receipt, need, BASE_SHA


def candidate(ctx):
    m = arithmetic(ctx)
    Q = m.Q

    def rat(s):
        need(type(s) is str and s.count('/') == 1, 'rational syntax')
        ns, ds = s.split('/')
        for text, signed in ((ns, True), (ds, False)):
            need(1 <= len(text) <= 4096, 'rational digit cap')
            d = text[1:] if signed and text.startswith('-') else text
            need(bool(d) and all(c in '0123456789' for c in d)
                 and not (len(d) > 1 and d[0] == '0') and text != '-0', 'canonical integer')
        n, d = int(ns), int(ds)
        need(d > 0, 'positive denominator')
        v = Q(n, d)
        need(v.numerator == n and v.denominator == d, 'reduced fraction')
        return v

    tau = Q(2, 7)
    dl = [(1+tau)*(2-3*tau), -12*(1-tau), Q(12)]
    kl = [2*(2-3*tau)*(1+tau)*(2+tau)*(3+tau),
          42*(1+tau)*(2+tau)*(4*tau-3), 840*(1-tau*tau), Q(-840)]
    gamma = [tau*(1+tau)*(2+tau)*(3+tau), -30*tau*(1+tau)*(2+tau),
             180*tau*(1+tau), -120*tau]
    p7 = m.qa(m.qs(m.qm(kl, kl), Q(2)), m.qa(
        m.qs(m.qm(m.qm([1+tau, Q(-6)], kl), dl), -140*tau),
        m.qs(m.qm(gamma, m.qm(dl, dl)), Q(245))))
    need(len(p7) == 8 and p7[-1] == -245*120*144*tau, 'literal septic leading')
    m.P7 = m.qs(p7, 1/p7[-1])
    doc = ctx['load'](ctx['raw'])
    need(ctx['encode'](doc) == ctx['raw'], 'canonical baseline JSON')
    need(doc['format'] == 'r2-reconstruction-19-v1'
         and doc['job_tag'] == 'f10-r2-reconstruction-v1', 'baseline format')
    interface = doc['interface']
    need(interface['variables'] == ['X1','X2','X3','z','S','vartheta']
         and interface['weights'] == ['1','2','3','5','1','2']
         and interface['basis'] == [str(i) for i in range(7)]
         and interface['base'] == 'Q[Z]/P7', 'full basis/interface')
    need(type(doc['field']['P7']) is list and len(doc['field']['P7']) == 8
         and [rat(s) for s in doc['field']['P7']] == m.P7, 'literal modulus mismatch')
    zero, one = m.field(0), m.field(1)

    def bounded(poly):
        poly = list(poly)
        while poly and poly[-1] == zero:
            poly.pop()
        need(len(poly) <= 17, 'intermediate u-degree cap')
        for c in poly:
            need(len(c) == 7 and all(v.numerator.bit_length() <= 32768
                 and v.denominator.bit_length() <= 32768 for v in c), 'intermediate bit cap')
        return poly

    def add(a, b):
        return bounded([m.fa(a[i] if i < len(a) else zero,
                             b[i] if i < len(b) else zero) for i in range(max(len(a), len(b)))])

    def neg(a):
        return [m.fn(c) for c in a]

    def mul(a, b):
        r = [zero] * max(0, len(a)+len(b)-1)
        for i, c in enumerate(a):
            for j, d in enumerate(b):
                r[i+j] = m.fa(r[i+j], m.fm(c, d))
        return bounded(r)

    rows = doc['rows']['Psi']
    need(type(rows) is list and len(rows) == 3, 'three complete Psi rows required')
    tables = []
    for h, row in zip((5,6,7), rows):
        need(type(row) is list and len(row) <= 4096, 'row term cap')
        table, prev = {}, None
        for term in row:
            need(type(term) is list and len(term) == 2, 'sparse pair')
            ex, co = term
            need(type(ex) is list and len(ex) == 6 and type(co) is list and len(co) == 7, 'full sparse coordinates')
            need(all(type(s) is str and s in tuple(str(i) for i in range(17)) for s in ex), 'exponent bounds')
            e = tuple(int(s) for s in ex)
            c = m.field([rat(s) for s in co])
            need(c != zero and (prev is None or prev < e), 'zero/unsorted/duplicate term')
            prev = e
            need(e[4] == e[5] == 0 and e[0]+2*e[1]+3*e[2]+5*e[3] == h,
                 'actual full weighted support')
            if e[3] == 0:
                key = (e[1], e[2])
                table[key] = m.fa(table.get(key, zero), c)
        tables.append(table)

    def part(table, vdegree, udegree):
        return bounded([table.get((i,vdegree), zero) for i in range(udegree+1)])

    for table, limits in zip(tables, ((2,1),(3,1,0),(3,2,0))):
        need(all(j < len(limits) and i <= limits[j] for i,j in table), 'chart shape')
    P, Qp = part(tables[0],0,2), part(tables[0],1,1)
    B3, B1, B0 = [part(tables[1],j,d) for j,d in enumerate((3,1,0))]
    C3, C2, C1 = [part(tables[2],j,d) for j,d in enumerate((3,2,0))]
    F = add(add(mul(mul(Qp,Qp),B3), neg(mul(mul(P,Qp),B1))), mul(B0,mul(P,P)))
    G = add(add(mul(mul(Qp,Qp),C3), neg(mul(mul(P,Qp),C2))), mul(C1,mul(P,P)))
    need(len(F) <= 6 and len(G) <= 6, 'derived degree-five bound')
    inverse_count = [0]

    def divide(a, b):
        need(bool(b), 'zero Euclid divisor')
        inverse_count[0] += 1
        inv = m.fi(b[-1], 'highest-leading-' + str(inverse_count[0]))
        r, q = list(a), [zero]*max(0,len(a)-len(b)+1)
        while r and len(r) >= len(b):
            shift = len(r)-len(b)
            c = m.fm(r[-1], inv)
            q[shift] = m.fa(q[shift], c)
            r = add(r, neg([zero]*shift + [m.fm(c,v) for v in b]))
        return bounded(q), r

    r0, r1, a0, a1, b0, b1 = F, G, [one], [], [], [one]
    steps = 0
    while r1:
        steps += 1
        need(steps <= 8, 'Euclid step cap')
        q, rem = divide(r0,r1)
        r0,r1,a0,a1,b0,b1 = r1,rem,a1,add(a0,neg(mul(q,a1))),b1,add(b0,neg(mul(q,b1)))
    need(len(r0) == 1, 'INCONCLUSIVE: nonconstant or zero gcd')
    inv = m.fi(r0[0], 'highest-final-constant')
    c, d = bounded([m.fm(inv,v) for v in a0]), bounded([m.fm(inv,v) for v in b0])
    need(len(c) <= 6 and len(d) <= 6, 'cofactor degree-five cap')
    need(add(mul(c,F),mul(d,G)) == [one], 'producer identity readback')
    return {'schema':'f10-r2-highest-bezout/v1', 'baseline_sha256':BASE_SHA,
            'chart':'z=0;X1=1;u=X2;v=X3', 'modulus':[m.wire_q(v) for v in m.P7],
            'c':[m.wire_f(v) for v in c], 'd':[m.wire_f(v) for v in d]}


def main():
    ctx = enter('produce')
    try:
        cert = candidate(ctx)
    except ValueError:
        receipt(ctx, 'INCONCLUSIVE_NO_CERTIFICATE')
        raise SystemExit(2)
    ctx['recheck']()
    raw = ctx['encode'](cert)
    ctx['write'](ctx['--certificate'], raw, 2097152)
    receipt(ctx, 'CANDIDATE_UNCHECKED', ctx['sha'](raw))


if __name__ == '__main__':
    main()
