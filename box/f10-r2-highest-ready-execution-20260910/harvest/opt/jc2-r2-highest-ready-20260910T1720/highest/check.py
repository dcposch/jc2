"""Independent full-row, fixed-place, special-boundary and identity check."""
from entry import enter, arithmetic, receipt, need, sufficient, Inconclusive, BASE_SHA


def verify(ctx, certificate_raw):
    n = arithmetic(ctx)  # Immutable check_arithmetic only, never producer code.
    R = n.Rational
    p, beta = 89, 0
    sufficient(p > 1 and all(p % d for d in range(2,10)), 'checker fixed-prime proof')

    def inv(value):
        value %= p
        sufficient(value != 0, 'checker dense denominator is not a p-unit')
        old_r,r,old_s,s = p,value,0,1
        steps = 0
        while r:
            steps += 1
            need(steps <= 16, 'checker inverse bound')
            q = old_r // r
            old_r,r,old_s,s = r,old_r-q*r,s,old_s-q*s
        result = old_s % p
        sufficient(old_r == 1 and value*result % p == 1, 'checker inverse readback')
        return result

    def rational(text):
        need(type(text) is str and text.count('/') == 1, 'checker rational syntax')
        a,b = text.split('/')
        for s,signed in ((a,True),(b,False)):
            digits = s[1:] if signed and s[:1] == '-' else s
            need(1 <= len(s) <= 4096 and bool(digits) and set(digits) <= set('0123456789')
                 and s != '-0' and (len(digits) == 1 or digits[0] != '0'), 'checker canonical integer')
        num,den = int(a),int(b)
        need(den > 0, 'checker positive denominator')
        result = R(num,den)
        need((result.numerator,result.denominator) == (num,den), 'checker reduced fraction')
        return result

    def residue(q):
        return (q.numerator % p)*inv(q.denominator) % p

    def list_of(obj,length):
        need(type(obj) is list and len(obj) == length, 'checker list shape')
        return obj

    t = R(2,7)
    dl = [(1+t)*(2-3*t),-12*(1-t),R(12)]
    kl = [2*(2-3*t)*(1+t)*(2+t)*(3+t),42*(1+t)*(2+t)*(4*t-3),840*(1-t*t),R(-840)]
    ga = [t*(1+t)*(2+t)*(3+t),-30*t*(1+t)*(2+t),180*t*(1+t),-120*t]
    literal = n.plus([2*x for x in n.times(kl,kl)],n.plus(
        [-140*t*x for x in n.times(n.times([1+t,-6],kl),dl)],
        [245*x for x in n.times(ga,n.times(dl,dl))]))
    need(len(literal) == 8 and literal[-1] == -245*120*144*t, 'checker literal septic')
    modulus = [x/literal[-1] for x in literal]
    base = ctx['load'](ctx['raw'])
    need(ctx['encode'](base) == ctx['raw'], 'checker canonical baseline')
    need(base['format'] == 'r2-reconstruction-19-v1'
         and base['job_tag'] == 'f10-r2-reconstruction-v1', 'checker baseline format')
    face = base['interface']
    need(face['variables'] == ['X1','X2','X3','z','S','vartheta']
         and face['weights'] == ['1','2','3','5','1','2']
         and face['basis'] == ['0','1','2','3','4','5','6']
         and face['base'] == 'Q[Z]/P7', 'checker entire basis/interface')
    actual_modulus = [rational(s) for s in list_of(base['field']['P7'],8)]
    need(actual_modulus == modulus, 'checker literal monic modulus mismatch')
    reduced_modulus = [residue(q) for q in actual_modulus]
    # At this ONE fixed beta=0, value and derivative are coefficients 0 and 1.
    sufficient(beta == 0 and reduced_modulus[0] == 0 and reduced_modulus[1] != 0,
               'checker fixed simple-root condition')

    forms = []
    for h,sparse in zip((5,6,7),list_of(base['rows']['Psi'],3)):
        need(type(sparse) is list and len(sparse) <= 4096, 'checker row cap')
        box = [[0 for _ in range(4)] for _ in range(3)]
        previous = None
        for item in sparse:
            ex,wire = list_of(item,2)
            exponent = []
            for text in list_of(ex,6):
                need(type(text) is str and text in [str(i) for i in range(17)], 'checker exponent')
                exponent.append(int(text))
            coordinates = [rational(s) for s in list_of(wire,7)]
            key = tuple(exponent)
            need(any(coordinates) and (previous is None or previous < key), 'checker sparse order/nonzero')
            previous = key
            need(exponent[4] == exponent[5] == 0
                 and sum(a*b for a,b in zip(exponent,(1,2,3,5,1,2))) == h,
                 'checker full support and weight')
            # Check every dense denominator BEFORE discarding any positive-z term.
            reduced = [residue(q) for q in coordinates]
            value = sum(q*pow(beta,i,p) for i,q in enumerate(reduced)) % p
            if exponent[3] != 0:
                continue
            limits = (2,1) if h == 5 else ((3,1,0) if h == 6 else (3,2,0))
            i,j = exponent[1],exponent[2]
            need(j < len(limits) and i <= limits[j], 'checker chart shape')
            box[j][i] = (box[j][i]+value) % p
        forms.append(box)
    sufficient(forms[0][1][1] != 0 and forms[1][0][3] != 0 and forms[1][2][0] != 0,
               'checker same-special boundary condition')

    def clean(poly):
        answer = [v % p for v in poly]
        while answer and answer[-1] == 0:
            answer.pop()
        need(len(answer) <= 11, 'checker polynomial degree cap')
        return answer

    def plus(a,b):
        answer = [0]*max(len(a),len(b))
        for i in range(len(answer)):
            answer[i] = ((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)) % p
        return clean(answer)

    def times(a,b):
        answer = [0]*max(0,len(a)+len(b)-1)
        for i in range(len(a)):
            for j in range(len(b)):
                answer[i+j] = (answer[i+j]+a[i]*b[j]) % p
        return clean(answer)

    P,Q = clean(forms[0][0]),clean(forms[0][1])
    q_squared,pq,p_squared = times(Q,Q),times(P,Q),times(P,P)
    eliminants = []
    for row in forms[1:]:
        first = times(q_squared,clean(row[0]))
        second = times(pq,clean(row[1]))
        third = times(p_squared,clean(row[2]))
        eliminants.append(plus(plus(first,[(-v)%p for v in second]),third))
    need(all(len(f)<=6 for f in eliminants), 'checker eliminant degree-five bound')
    cert = ctx['load'](certificate_raw)
    need(type(cert) is dict and set(cert) ==
         {'schema','baseline_sha256','prime','root','chart','modulus','c','d'}, 'checker certificate keys')
    need(ctx['encode'](cert) == certificate_raw, 'checker canonical certificate')
    need(cert['schema'] == 'f10-r2-highest-modular89/v1' and cert['baseline_sha256'] == BASE_SHA
         and cert['prime'] == '89' and cert['root'] == '0'
         and cert['chart'] == 'z=0;X1=1;u=X2;v=X3', 'checker exact fixed binding')
    need([rational(s) for s in list_of(cert['modulus'],8)] == modulus, 'checker certificate modulus')
    cofactors = []
    for name in ('c','d'):
        wire = cert[name]
        need(type(wire) is list and len(wire) <= 6, 'checker cofactor degree')
        need(all(type(s) is str and s in [str(j) for j in range(89)] for s in wire),
             'checker canonical finite-field strings')
        values = [int(s) for s in wire]
        need(not values or values[-1] != 0, 'checker trailing zero cofactor')
        cofactors.append(values)
    identity = plus(times(cofactors[0],eliminants[0]),times(cofactors[1],eliminants[1]))
    for i in range(11):
        got = identity[i] if i < len(identity) else 0
        if got != (1 if i == 0 else 0):
            raise ValueError('CHECK FAILED: fixed-place full modular Bezout identity')


def main():
    ctx = enter('check')
    raw = ctx['read'](ctx['--certificate'],2097152)
    try:
        verify(ctx,raw)
    except Inconclusive:
        need(ctx['read'](ctx['--certificate'],2097152) == raw, 'checker inconclusive certificate drift')
        receipt(ctx,'INCONCLUSIVE_FIXED_PLACE',ctx['sha'](raw))
        raise SystemExit(2)
    need(ctx['read'](ctx['--certificate'],2097152) == raw, 'checker certificate postcheck drift')
    receipt(ctx,'HIGHEST_SPECIAL_PROJECTIVE_CHECKED_NO_SOURCE_OUTCOME',ctx['sha'](raw))


if __name__ == '__main__':
    main()
