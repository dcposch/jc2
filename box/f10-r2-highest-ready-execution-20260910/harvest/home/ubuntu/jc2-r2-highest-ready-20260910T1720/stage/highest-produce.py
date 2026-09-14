"""STATIC: fixed-place candidate only; no prime search or source verdict."""
from entry import enter, arithmetic, receipt, need, sufficient, BASE_SHA


def candidate(ctx):
    m = arithmetic(ctx)
    Q = m.Q
    prime, root = 89, 0
    divisor = 2
    sufficient(prime >= 2, 'candidate prime')
    while divisor * divisor <= prime:
        sufficient(prime % divisor != 0, 'candidate primality')
        divisor += 1

    def inverse(a):
        a %= prime
        sufficient(a != 0, 'nonunit modulo fixed prime')
        result = pow(a, prime-2, prime)
        sufficient(a * result % prime == 1, 'inverse readback')
        return result

    def rat(s):
        need(type(s) is str and s.count('/') == 1, 'rational syntax')
        ns, ds = s.split('/')
        for text, signed in ((ns, True), (ds, False)):
            need(1 <= len(text) <= 4096, 'rational digit cap')
            digits = text[1:] if signed and text.startswith('-') else text
            need(bool(digits) and all(c in '0123456789' for c in digits)
                 and not (len(digits) > 1 and digits[0] == '0') and text != '-0', 'canonical integer')
        n, d = int(ns), int(ds)
        need(d > 0, 'positive denominator')
        value = Q(n, d)
        need(value.numerator == n and value.denominator == d, 'reduced fraction')
        return value

    def reduce_rational(value):
        return value.numerator % prime * inverse(value.denominator) % prime

    tau = Q(2, 7)
    dl = [(1+tau)*(2-3*tau), -12*(1-tau), Q(12)]
    kl = [2*(2-3*tau)*(1+tau)*(2+tau)*(3+tau),
          42*(1+tau)*(2+tau)*(4*tau-3), 840*(1-tau*tau), Q(-840)]
    ga = [tau*(1+tau)*(2+tau)*(3+tau), -30*tau*(1+tau)*(2+tau),
          180*tau*(1+tau), -120*tau]
    literal = m.qa(m.qs(m.qm(kl, kl), Q(2)), m.qa(
        m.qs(m.qm(m.qm([1+tau, Q(-6)], kl), dl), -140*tau),
        m.qs(m.qm(ga, m.qm(dl, dl)), Q(245))))
    need(len(literal) == 8 and literal[-1] == -245*120*144*tau, 'literal septic')
    modulus = m.qs(literal, 1/literal[-1])
    doc = ctx['load'](ctx['raw'])
    need(ctx['encode'](doc) == ctx['raw'], 'canonical baseline JSON')
    need(doc['format'] == 'r2-reconstruction-19-v1'
         and doc['job_tag'] == 'f10-r2-reconstruction-v1', 'baseline format')
    face = doc['interface']
    need(face['variables'] == ['X1','X2','X3','z','S','vartheta']
         and face['weights'] == ['1','2','3','5','1','2']
         and face['basis'] == [str(i) for i in range(7)]
         and face['base'] == 'Q[Z]/P7', 'full source basis')
    need(type(doc['field']['P7']) is list and len(doc['field']['P7']) == 8, 'eight modulus coordinates')
    actual_modulus = [rat(s) for s in doc['field']['P7']]
    need(actual_modulus == modulus, 'literal modulus mismatch')
    reduced_modulus = [reduce_rational(q) for q in actual_modulus]
    value = 0
    for a in reversed(reduced_modulus):
        value = (value * root + a) % prime
    derivative = 0
    for i in range(7, 0, -1):
        derivative = (derivative * root + i * reduced_modulus[i]) % prime
    sufficient(value == 0 and derivative != 0, 'fixed simple-root condition')

    rows = doc['rows']['Psi']
    need(type(rows) is list and len(rows) == 3, 'three full Psi rows')
    tables = []
    for h, row in zip((5,6,7), rows):
        need(type(row) is list and len(row) <= 4096, 'row term cap')
        table, previous = {}, None
        for term in row:
            need(type(term) is list and len(term) == 2, 'sparse pair')
            ex, wire = term
            need(type(ex) is list and len(ex) == 6 and type(wire) is list and len(wire) == 7,
                 'complete seven-coordinate term')
            need(all(type(s) is str and s in tuple(str(i) for i in range(17)) for s in ex), 'exponent bound')
            e = tuple(int(s) for s in ex)
            coordinates = [rat(s) for s in wire]
            need(any(coordinates) and (previous is None or previous < e), 'canonical sparse order/nonzero')
            previous = e
            need(e[4] == e[5] == 0 and e[0]+2*e[1]+3*e[2]+5*e[3] == h,
                 'whole-row support/weight')
            # ALL seven denominators are checked, including positive-z terms.
            reduced = [reduce_rational(q) for q in coordinates]
            residue = 0
            for q in reversed(reduced):
                residue = (residue * root + q) % prime
            if e[3] == 0:
                key = (e[1], e[2])
                table[key] = (table.get(key, 0) + residue) % prime
        tables.append(table)
    for table, limits in zip(tables, ((2,1),(3,1,0),(3,2,0))):
        need(all(j < len(limits) and i <= limits[j] for i,j in table), 'actual chart shape')
    sufficient(tables[0].get((1,1),0) != 0 and tables[1].get((3,0),0) != 0
               and tables[1].get((0,2),0) != 0, 'same-special boundary condition')

    def trim(poly):
        result = [v % prime for v in poly]
        while result and result[-1] == 0:
            result.pop()
        need(len(result) <= 17, 'intermediate degree cap')
        return result

    def add(a,b):
        return trim([(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
                     for i in range(max(len(a),len(b)))])

    def neg(a):
        return [(-v) % prime for v in a]

    def mul(a,b):
        out = [0]*max(0,len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                out[i+j] = (out[i+j]+x*y) % prime
        return trim(out)

    def part(table,j,d):
        return trim([table.get((i,j),0) for i in range(d+1)])

    P, Qp = part(tables[0],0,2), part(tables[0],1,1)
    B3,B1,B0 = [part(tables[1],j,d) for j,d in enumerate((3,1,0))]
    C3,C2,C1 = [part(tables[2],j,d) for j,d in enumerate((3,2,0))]
    F = add(add(mul(mul(Qp,Qp),B3),neg(mul(mul(P,Qp),B1))),mul(B0,mul(P,P)))
    G = add(add(mul(mul(Qp,Qp),C3),neg(mul(mul(P,Qp),C2))),mul(C1,mul(P,P)))
    need(len(F) <= 6 and len(G) <= 6, 'eliminant degree cap')

    def divide(a,b):
        need(bool(b), 'zero Euclid divisor')
        inv = inverse(b[-1])
        rem, quotient = list(a), [0]*max(0,len(a)-len(b)+1)
        while rem and len(rem) >= len(b):
            shift = len(rem)-len(b)
            q = rem[-1]*inv % prime
            quotient[shift] = (quotient[shift]+q) % prime
            rem = add(rem,neg([0]*shift+[q*v % prime for v in b]))
        return trim(quotient),rem

    r0,r1,c0,c1,d0,d1 = F,G,[1],[],[],[1]
    steps = 0
    while r1:
        steps += 1
        need(steps <= 8, 'Euclid division cap')
        quotient,rem = divide(r0,r1)
        r0,r1,c0,c1,d0,d1 = r1,rem,c1,add(c0,neg(mul(quotient,c1))),d1,add(d0,neg(mul(quotient,d1)))
    sufficient(len(r0) == 1, 'no unit modular cofactor')
    inv = inverse(r0[0])
    c,d = trim([inv*x for x in c0]),trim([inv*x for x in d0])
    need(len(c) <= 6 and len(d) <= 6, 'cofactor degree cap')
    need(add(mul(c,F),mul(d,G)) == [1], 'producer modular identity readback')
    return {'schema':'f10-r2-highest-modular89/v1','baseline_sha256':BASE_SHA,
            'prime':'89','root':'0','chart':'z=0;X1=1;u=X2;v=X3',
            'modulus':[m.wire_q(q) for q in modulus],
            'c':[str(q) for q in c],'d':[str(q) for q in d]}


def main():
    ctx = enter('produce')
    try:
        certificate = candidate(ctx)
    except ValueError:
        receipt(ctx,'INCONCLUSIVE_NO_CERTIFICATE')
        raise SystemExit(2)
    ctx['recheck']()
    raw = ctx['encode'](certificate)
    ctx['write'](ctx['--certificate'],raw,2097152)
    receipt(ctx,'CANDIDATE_UNCHECKED',ctx['sha'](raw))


if __name__ == '__main__':
    main()
