"""STATIC: fixed-cut positive full-unit search only; no completeness claim."""
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

    names = (['Psi5','Psi6','Psi7'] + ['K1_' + str(i) for i in range(1,7)]
             + ['K0_' + str(i) for i in range(1,9)] + ['K1_0-U*K0_0'])
    weights = [5,6,7] + [14-i for i in range(1,7)] + [16-i for i in range(1,9)] + [19]
    limits = [25,24,23] + [12]*15
    expected_source_names = names[:-1] + ['K1_0-U*s^5','K0_0-s^7']
    need(face['rows'] == expected_source_names and face['scale'] == 'z=s^2; s invertible'
         and face['targets'] == ['K1_0-U*s^5','K0_0-s^7']
         and face['guard'] == 'omega=W*t5*s^8', 'source cover interface')
    rows = doc['rows']
    need(type(rows) is dict and set(rows) == {'Psi','K1','K0'}, 'full row families')
    need(all(type(rows[k]) is list and len(rows[k]) == v for k,v in
             (('Psi',3),('K1',7),('K0',9))), 'full row slot counts')
    parsed_terms = 0

    def source_poly(sparse, weight):
        nonlocal parsed_terms
        need(type(sparse) is list and len(sparse) <= 4096, 'source row cap')
        parsed_terms += len(sparse)
        need(parsed_terms <= 50000, 'source aggregate term cap')
        result, previous = {}, None
        for term in sparse:
            need(type(term) is list and len(term) == 2, 'source sparse pair')
            ex, wire = term
            need(type(ex) is list and len(ex) == 6 and type(wire) is list and len(wire) == 7,
                 'source full exponent/seven-coordinate shape')
            need(all(type(s) is str and s in [str(i) for i in range(17)] for s in ex),
                 'source canonical exponents')
            e = tuple(int(s) for s in ex)
            coordinates = [rat(s) for s in wire]
            need(any(coordinates) and (previous is None or previous < e), 'source sparse order/nonzero')
            previous = e
            need(e[4] == e[5] == 0 and e[0]+2*e[1]+3*e[2]+5*e[3] == weight,
                 'source whole support/weight')
            # All seven denominators, including every positive-z term, precede projection.
            residues = [reduce_rational(v) for v in coordinates]
            scalar = 0
            for v in reversed(residues):
                scalar = (scalar*root+v) % prime
            key = e[:3]  # Exactly z=1; never X1=1 or a quotient reduction.
            result[key] = (result.get(key,0)+scalar) % prime
        return {e:c for e,c in result.items() if c}

    psis = [source_poly(row,h) for row,h in zip(rows['Psi'],(5,6,7))]
    k1 = [source_poly(row,14-i) for i,row in enumerate(rows['K1'])]
    k0 = [source_poly(row,16-i) for i,row in enumerate(rows['K0'])]
    u = source_poly(doc['source']['U'],3)
    mixed = dict(k1[0])
    for e,c in u.items():
        for f,d in k0[0].items():
            key = tuple(e[i]+f[i] for i in range(3))
            mixed[key] = (mixed.get(key,0)-c*d) % prime
    mixed = {e:c for e,c in mixed.items() if c}
    generators = psis + k1[1:] + k0[1:] + [mixed]
    need(len(generators) == len(names) == 18, 'all eighteen generator slots')

    def weight(e):
        return e[0]+2*e[1]+3*e[2]

    for f,h in zip(generators,weights):
        need(all(weight(e) <= h and weight(e) % 5 == h % 5 for e in f),
             'projected generator bound/class')

    def monomials(cap, congruence):
        result = []
        for i in range(cap+1):
            for j in range(cap//2+1):
                for k in range(cap//3+1):
                    e = (i,j,k)
                    if weight(e) <= cap and weight(e) % 5 == congruence:
                        result.append(e)
        return sorted(result)

    positions = monomials(30,0)
    columns = [(slot,e) for slot,(h,cap) in enumerate(zip(weights,limits))
               for e in monomials(cap,(-h) % 5)]
    # Documentary expected sizes are checked at runtime; mismatch is NONDECISION.
    need(len(positions) == 247 and len(columns) == 754
         and sum(slot < 3 for slot,e in columns) == 424, 'fixed-cut matrix dimensions')
    index = {e:i for i,e in enumerate(positions)}
    matrix = [[0]*(len(columns)+1) for _ in positions]
    matrix[index[(0,0,0)]][-1] = 1
    for col,(slot,e) in enumerate(columns):
        for f,c in generators[slot].items():
            key = tuple(e[i]+f[i] for i in range(3))
            need(key in index, 'no dropped product position')
            matrix[index[key]][col] = (matrix[index[key]][col]+c) % prime
    pivot_columns = []
    rank = 0
    for col in range(len(columns)):
        pivot = next((i for i in range(rank,len(matrix)) if matrix[i][col]),None)
        if pivot is None:
            continue
        matrix[rank],matrix[pivot] = matrix[pivot],matrix[rank]
        unit = inverse(matrix[rank][col])
        matrix[rank] = [v*unit % prime for v in matrix[rank]]
        for i in range(rank+1,len(matrix)):
            factor = matrix[i][col]
            if factor:
                matrix[i] = [(x-factor*y) % prime for x,y in zip(matrix[i],matrix[rank])]
        pivot_columns.append(col)
        rank += 1
        if rank == len(matrix):
            break
    sufficient(all(any(row[:-1]) or row[-1] == 0 for row in matrix), 'fixed cut has no unit candidate')
    solution = [0]*len(columns)
    for i in range(rank-1,-1,-1):
        col = pivot_columns[i]
        solution[col] = (matrix[i][-1]-sum(matrix[i][j]*solution[j]
                                         for j in range(col+1,len(columns)))) % prime
    cofactors = [{} for _ in range(18)]
    for (slot,e),c in zip(columns,solution):
        if c:
            cofactors[slot][e] = c
    # Literal-polynomial readback, not only a rank or echelon flag.
    full = {}
    for cofactor,f in zip(cofactors,generators):
        for e,c in cofactor.items():
            for g,d in f.items():
                key = tuple(e[i]+g[i] for i in range(3))
                full[key] = (full.get(key,0)+c*d) % prime
    full = {e:c for e,c in full.items() if c}
    need(full == {(0,0,0):1}, 'producer literal full-unit identity')
    return {'schema':'f10-r2-fullunit-modular89/v1','baseline_sha256':BASE_SHA,
            'prime':'89','root':'0','specialization':'z=1',
            'variables':['Y1','Y2','Y3'],'weights':['1','2','3'],'cut':'30',
            'modulus':[m.wire_q(v) for v in modulus],
            'cofactors':[{'generator':name,'terms':[[[str(v) for v in e],str(c)]
                         for e,c in sorted(cofactor.items())]}
                         for name,cofactor in zip(names,cofactors)]}


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
