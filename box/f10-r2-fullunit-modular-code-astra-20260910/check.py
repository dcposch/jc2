"""Independent full-source fixed-place literal unit-identity check; STATIC."""
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

    labels = ['Psi5','Psi6','Psi7']
    labels.extend('K1_' + str(j) for j in range(1,7))
    labels.extend('K0_' + str(j) for j in range(1,9))
    labels.append('K1_0-U*K0_0')
    degree = [5,6,7,13,12,11,10,9,8,15,14,13,12,11,10,9,8,19]
    caps = [25,24,23] + [12 for _ in range(15)]
    need(face['scale'] == 'z=s^2; s invertible' and face['guard'] == 'omega=W*t5*s^8'
         and face['targets'] == ['K1_0-U*s^5','K0_0-s^7']
         and face['rows'] == labels[:-1] + ['K1_0-U*s^5','K0_0-s^7'], 'checker source cover binding')
    source_rows = base['rows']
    need(type(source_rows) is dict and set(source_rows) == {'Psi','K1','K0'}, 'checker row family keys')
    psi_rows = list_of(source_rows['Psi'],3)
    first_rows = list_of(source_rows['K1'],7)
    second_rows = list_of(source_rows['K0'],9)
    total_terms = 0

    def reconstruct(wire, homogeneous_weight):
        nonlocal total_terms
        need(type(wire) is list and len(wire) <= 4096, 'checker original row size')
        total_terms += len(wire)
        need(total_terms <= 50000, 'checker original aggregate terms')
        values = {}
        previous = None
        for pair in wire:
            ex, dense = list_of(pair,2)
            e = []
            for text in list_of(ex,6):
                need(type(text) is str and text in [str(j) for j in range(17)],
                     'checker original exponent string')
                e.append(int(text))
            full_key = tuple(e)
            coords = [rational(text) for text in list_of(dense,7)]
            need(any(coords) and (previous is None or previous < full_key),
                 'checker original sparse canonicality')
            previous = full_key
            need(e[4] == 0 and e[5] == 0
                 and sum(x*w for x,w in zip(e,(1,2,3,5,1,2))) == homogeneous_weight,
                 'checker original full weight/support')
            # Conservative integrality of every dense coordinate BEFORE z=1.
            residues = [residue(x) for x in coords]
            scalar = sum(residues[j]*pow(beta,j,p) for j in range(7)) % p
            projected = (e[0],e[1],e[2])
            values[projected] = (values.get(projected,0)+scalar) % p
        return [(e,c) for e,c in sorted(values.items()) if c]

    fs = [reconstruct(psi_rows[j],j+5) for j in range(3)]
    first = [reconstruct(first_rows[j],14-j) for j in range(7)]
    second = [reconstruct(second_rows[j],16-j) for j in range(9)]
    uu = reconstruct(base['source']['U'],3)
    # Rebuild the actual mixed polynomial independently; no producer M or reductions.
    mix = {e:c for e,c in first[0]}
    for (i,j,k),c in uu:
        for (x,y,z),d in second[0]:
            key = (i+x,j+y,k+z)
            mix[key] = (mix.get(key,0)-c*d) % p
    generators = fs + first[1:] + second[1:] + [[(e,c) for e,c in sorted(mix.items()) if c]]
    need(len(generators) == 18, 'checker all eighteen slots')
    for gen,h in zip(generators,degree):
        for (i,j,k),v in gen:
            need(i+2*j+3*k <= h and (i+2*j+3*k-h) % 5 == 0,
                 'checker full specialized degree/class')

    cert = ctx['load'](certificate_raw)
    need(type(cert) is dict and set(cert) ==
         {'schema','baseline_sha256','prime','root','specialization','variables','weights','cut','modulus','cofactors'},
         'checker full-unit certificate keys')
    need(ctx['encode'](cert) == certificate_raw, 'checker canonical full-unit certificate')
    need(cert['schema'] == 'f10-r2-fullunit-modular89/v1' and cert['baseline_sha256'] == BASE_SHA
         and cert['prime'] == '89' and cert['root'] == '0' and cert['specialization'] == 'z=1'
         and cert['variables'] == ['Y1','Y2','Y3'] and cert['weights'] == ['1','2','3']
         and cert['cut'] == '30', 'checker exact full-unit binding')
    need([rational(x) for x in list_of(cert['modulus'],8)] == modulus, 'checker certificate literal P7')
    all_cofactors = list_of(cert['cofactors'],18)
    decoded = []
    cofactor_terms = 0
    for position,obj in enumerate(all_cofactors):
        need(type(obj) is dict and set(obj) == {'generator','terms'}
             and obj['generator'] == labels[position], 'checker indexed generator slot')
        wire = obj['terms']
        need(type(wire) is list and len(wire) <= 754, 'checker cofactor sparse bound')
        cofactor_terms += len(wire)
        need(cofactor_terms <= 754, 'checker total cofactor term bound')
        terms, previous = [], None
        for pair in wire:
            ex,c = list_of(pair,2)
            need(all(type(s) is str and s in [str(j) for j in range(31)]
                     for s in list_of(ex,3)), 'checker cofactor exponent wire')
            e = tuple(int(s) for s in ex)
            need(previous is None or previous < e, 'checker cofactor order/duplicate')
            previous = e
            need(type(c) is str and c in [str(j) for j in range(1,89)], 'checker canonical nonzero residue')
            weight = e[0]+2*e[1]+3*e[2]
            need(weight <= caps[position] and (weight+degree[position]) % 5 == 0,
                 'checker cofactor degree/class')
            terms.append((e,int(c)))
        decoded.append(terms)
    # Independent dense rectangular accumulator, not producer's echelon/matrix code.
    accumulated = [[[0 for _ in range(11)] for _ in range(16)] for _ in range(31)]
    for multiplier,gen in zip(decoded,generators):
        for (a,b,c),coefficient in multiplier:
            for (i,j,k),value in gen:
                x,y,z = a+i,b+j,c+k
                need(x+2*y+3*z <= 30 and (x+2*y+3*z) % 5 == 0,
                     'checker no omitted high product')
                need(x < 31 and y < 16 and z < 11, 'checker full identity box')
                accumulated[x][y][z] = (accumulated[x][y][z]+coefficient*value) % p
    # Every position, even positions outside the class/weight simplex, is checked.
    for x in range(31):
        for y in range(16):
            for z in range(11):
                if accumulated[x][y][z] != (1 if (x,y,z) == (0,0,0) else 0):
                    raise ValueError('CHECK FAILED: fixed-place literal full-source unit identity')


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
    receipt(ctx,'FULL_SPECIAL_UNIT_CHECKED_NO_SOURCE_OUTCOME',ctx['sha'](raw))


if __name__ == '__main__':
    main()
