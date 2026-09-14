"""Independent highest-chart extraction and full rational-basis certificate check."""
from entry import enter, arithmetic, receipt, need, BASE_SHA


def verify(ctx, certificate_raw):
    n = arithmetic(ctx)  # Pinned check_arithmetic.py, never producer arithmetic.
    R = n.Rational

    def rational(text):
        need(type(text) is str and text.count('/') == 1, 'checker rational syntax')
        numerator, denominator = text.split('/')
        for s, sign in ((numerator,True),(denominator,False)):
            digits = s[1:] if sign and s[:1] == '-' else s
            need(1 <= len(s) <= 4096 and bool(digits)
                 and set(digits) <= set('0123456789') and s != '-0'
                 and (len(digits) == 1 or digits[0] != '0'), 'checker canonical digits')
        a,b = int(numerator),int(denominator)
        need(b > 0, 'checker denominator')
        q = R(a,b)
        need((q.numerator,q.denominator) == (a,b), 'checker reduced fraction')
        return q

    def exact_list(obj, length):
        need(type(obj) is list and len(obj) == length, 'checker list shape')
        return obj

    t = R(2,7)
    dl = [(1+t)*(2-3*t),-12*(1-t),R(12)]
    kl = [2*(2-3*t)*(1+t)*(2+t)*(3+t),42*(1+t)*(2+t)*(4*t-3),840*(1-t*t),R(-840)]
    ga = [t*(1+t)*(2+t)*(3+t),-30*t*(1+t)*(2+t),180*t*(1+t),-120*t]
    literal = n.plus([2*x for x in n.times(kl,kl)], n.plus(
        [-140*t*x for x in n.times(n.times([1+t,-6],kl),dl)],
        [245*x for x in n.times(ga,n.times(dl,dl))]))
    need(len(literal) == 8 and literal[-1] == -245*120*144*t, 'checker literal septic')
    n.MODULUS = [x/literal[-1] for x in literal]
    base = ctx['load'](ctx['raw'])
    need(ctx['encode'](base) == ctx['raw'], 'checker canonical baseline')
    need(base['format'] == 'r2-reconstruction-19-v1'
         and base['job_tag'] == 'f10-r2-reconstruction-v1', 'checker baseline format')
    face = base['interface']
    need(face['variables'] == ['X1','X2','X3','z','S','vartheta']
         and face['weights'] == ['1','2','3','5','1','2']
         and face['basis'] == ['0','1','2','3','4','5','6']
         and face['base'] == 'Q[Z]/P7', 'checker full coordinate basis')
    need([rational(s) for s in exact_list(base['field']['P7'],8)] == n.MODULUS,
         'checker actual literal modulus')
    zero, one = n.F(0), n.F(1)

    def vector(obj):
        return tuple(rational(s) for s in exact_list(obj,7))

    # Independently extract whole highest forms into a dense (v-power,u-power) box.
    coefficients = []
    for h, sparse in zip((5,6,7), exact_list(base['rows']['Psi'],3)):
        need(type(sparse) is list and len(sparse) <= 4096, 'checker row term cap')
        box = [[zero for _ in range(4)] for _ in range(3)]
        previous = None
        for item in sparse:
            exponent, coefficient = exact_list(item,2)
            e = []
            for s in exact_list(exponent,6):
                need(type(s) is str and s in [str(j) for j in range(17)], 'checker exponent')
                e.append(int(s))
            val = vector(coefficient)
            key = tuple(e)
            need(any(val) and (previous is None or key > previous), 'checker sparse canonical order')
            previous = key
            need(e[4] == 0 and e[5] == 0, 'checker forbidden S/vartheta support')
            need(sum(a*b for a,b in zip(e,(1,2,3,5,1,2))) == h, 'checker exact row weight')
            if e[3] != 0:
                continue
            bounds = (2,1) if h == 5 else ((3,1,0) if h == 6 else (3,2,0))
            need(e[2] < len(bounds) and e[1] <= bounds[e[2]], 'checker actual chart shape')
            box[e[2]][e[1]] = n.fsum(box[e[2]][e[1]],val)
        coefficients.append(box)

    def clean(poly):
        poly = list(poly)
        while poly and poly[-1] == zero:
            poly.pop()
        need(len(poly) <= 11, 'checker identity degree envelope')
        for v in poly:
            need(all(q.numerator.bit_length() <= 32768 and q.denominator.bit_length() <= 32768
                 for q in v), 'checker intermediate bit cap')
        return poly

    def times(a,b):
        result = [zero]*max(0,len(a)+len(b)-1)
        for i in range(len(a)):
            for j in range(len(b)):
                result[i+j] = n.fsum(result[i+j],n.fproduct(a[i],b[j]))
        return clean(result)

    def plus(a,b):
        return clean([n.fsum(a[i] if i<len(a) else zero,b[i] if i<len(b) else zero)
                      for i in range(max(len(a),len(b)))])

    P = clean(coefficients[0][0]); Q = clean(coefficients[0][1])
    q2, pq, p2 = times(Q,Q),times(P,Q),times(P,P)
    fg = []
    for row in coefficients[1:]:
        first = times(q2,clean(row[0]))
        second = times(pq,clean(row[1]))
        third = times(p2,clean(row[2]))
        fg.append(plus(plus(first,[n.fnegative(v) for v in second]),third))
    need(all(len(f) <= 6 for f in fg), 'checker eliminant degree-five bound')
    cert = ctx['load'](certificate_raw)
    need(type(cert) is dict and set(cert) == {'schema','baseline_sha256','chart','modulus','c','d'},
         'checker certificate keys')
    need(ctx['encode'](cert) == certificate_raw, 'checker canonical certificate JSON')
    need(cert['schema'] == 'f10-r2-highest-bezout/v1'
         and cert['baseline_sha256'] == BASE_SHA
         and cert['chart'] == 'z=0;X1=1;u=X2;v=X3', 'checker certificate binding')
    need([rational(s) for s in exact_list(cert['modulus'],8)] == n.MODULUS,
         'checker certificate literal modulus')
    witness = []
    for name in ('c','d'):
        v = cert[name]
        need(type(v) is list and len(v) <= 6, 'checker cofactor degree cap')
        parsed = [vector(x) for x in v]
        need(not parsed or parsed[-1] != zero, 'checker trailing zero cofactor')
        witness.append(parsed)
    product = plus(times(witness[0],fg[0]),times(witness[1],fg[1]))
    # Exactly all 11 u-powers times all seven Q-basis coordinates, including zeros.
    for i in range(11):
        v = product[i] if i < len(product) else zero
        for j in range(7):
            if v[j] != R(1 if i == 0 and j == 0 else 0):
                raise ValueError('CHECK FAILED: full B[u] Bezout identity')


def main():
    ctx = enter('check')
    raw = ctx['read'](ctx['--certificate'],2097152)
    verify(ctx,raw)
    need(ctx['read'](ctx['--certificate'],2097152) == raw, 'certificate postcheck drift')
    receipt(ctx,'HIGHEST_CHART_IDENTITY_CHECKED_NO_SOURCE_OUTCOME',ctx['sha'](raw))


if __name__ == '__main__':
    main()
