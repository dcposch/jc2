"""DISABLED/UNEXECUTED quotient-remainder candidate producer (17zg).
AUTHORITY UNIVARIATE FULL_RECEIPT ROOT_ACCEPTANCE CERTIFICATE
One small rational RREF, no full 217-by-1638 search matrix. Every output
remains a candidate until the unchanged independent checker accepts it.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from execution_gate import authorize

def generic_candidate(p, fs, q, flint):
    # Internal mathematical API: call only inside a separately authorized
    # child. main() authorizes before reaching any mathematical import.
    from algebra import Q, trim, da, ds, dm, dd, dxg, require
    require(type(p) is list and len(p) == 8
            and all(type(c) is Q for c in p) and p[-1] == Q(1),
            'generic monic rank-seven Fraction modulus')
    derivative = [Q(i) * p[i] for i in range(1, 8)]
    require(dxg(p, derivative)[0] == [Q(1)], 'generic modulus must be squarefree')
    require(type(fs) is list and len(fs) == 9, 'generic nine polynomials')
    def input_poly(f):
        require(type(f) is list and 1 <= len(f) <= 6,
                'generic T-degree at most five with zero slot retained')
        require(all(type(c) is list and len(c) == 7
                    and all(type(x) is Q for x in c) for c in f),
                'generic dense seven-Fraction coefficients')
    for f in fs:
        input_poly(f)
    input_poly(q)

    class Coefficients:
        # This is Q[v]/pa, NOT a field. The only inverses below are certified
        # with rational polynomial xgcd. Its T quotient need not be reduced.
        def __init__(self, pa):
            self.pa = pa
            self.e = len(pa) - 1
        def red(self, c):
            return dd(c, self.pa)[1]
        def mul(self, c, d):
            return self.red(dm(c, d))
        def tt(self, f):
            f = list(f)
            while f and not f[-1]:
                f.pop()
            return f
        def project(self, f):
            return self.tt([self.red(c) for c in f])
        def add(self, f, g):
            return self.tt([da(f[i] if i < len(f) else [],
                               g[i] if i < len(g) else [])
                            for i in range(max(len(f), len(g)))])
        def scale(self, f, c):
            return self.tt([self.mul(a, c) for a in f])
        def product(self, f, g):
            if not f or not g:
                return []
            out = [[] for _ in range(len(f) + len(g) - 1)]
            for i, c in enumerate(f):
                for j, a in enumerate(g):
                    out[i + j] = da(out[i + j], self.mul(c, a))
            return self.tt(out)
        def fifth(self, f):
            out = [[Q(1)]]
            for _ in range(5):
                out = self.product(out, f)
            return out
        def divide(self, f, monic):
            require(bool(monic) and monic[-1] == [Q(1)],
                    'only monic T division is permitted')
            out = [[] for _ in range(max(0, len(f) - len(monic) + 1))]
            rem = self.tt(f)
            while rem and len(rem) >= len(monic):
                k = len(rem) - len(monic)
                c = rem[-1]
                out[k] = da(out[k], c)
                subtract = [[] for _ in range(k)] + self.scale(monic, ds(c, Q(-1)))
                rem = self.add(rem, subtract)
            return self.tt(out), rem
        def vector(self, f, d):
            require(len(f) <= d, 'complete remainder basis envelope')
            return [(f[j][l] if j < len(f) and l < len(f[j]) else Q(0))
                    for j in range(d) for l in range(self.e)]

    # Partition only by rational gcds of ACTUAL projected leading
    # coefficients. Both children rescan all nine projected polynomials.
    leaves = []
    pending = [list(p)]
    splits = 0
    visits = 0
    while pending:
        pa = pending.pop()
        visits += 1
        require(visits <= 13, 'rank-seven split termination bound')
        a = Coefficients(pa)
        local = [a.project(f) for f in fs]
        degree = max(len(f) - 1 for f in local)
        if degree < 0:
            leaves.append({'a': a, 'fs': local, 'd': -1, 'pivot': None})
            continue
        pivot = next(i for i, f in enumerate(local) if len(f) - 1 == degree)
        c = local[pivot][-1]
        g, inverse, _ = dxg(c, pa)
        if g == [Q(1)]:
            inverse = a.red(inverse)
            require(a.mul(c, inverse) == [Q(1)], 'literal leading-coefficient unit identity')
            leaves.append({'a': a, 'fs': local, 'd': degree,
                           'pivot': pivot, 'inverse': inverse,
                           'monic': a.scale(local[pivot], inverse)})
        else:
            require(0 < len(g) - 1 < a.e, 'proper nonunit leading-coefficient split')
            h, remainder = dd(pa, g)
            require(not remainder and dxg(g, h)[0] == [Q(1)],
                    'exact coprime squarefree split')
            splits += 1
            require(splits <= 6, 'at most six proper splits')
            pending.extend([h, g])
    require(sum(leaf['a'].e for leaf in leaves) == 7, 'all coefficient components retained')
    product = [Q(1)]
    for leaf in leaves:
        product = dm(product, leaf['a'].pa)
    require(product == p, 'leaf product is entire original modulus')

    def wire(c):
        return [str(c.numerator), str(c.denominator)]
    trace = {'schema': 'F10-QUOTIENT-REMAINDER-TRACE/v1', 'splits': splits,
             'leaves': [{'modulus': [wire(c) for c in leaf['a'].pa],
                         'degree': leaf['d'], 'pivot': leaf['pivot']} for leaf in leaves],
             'small_rows': 0, 'small_columns': 0, 'rref_calls': 0}
    def certificate(branch, witness):
        require(len(witness) == (1638 if branch == 'UNIT' else 217),
                'full original certificate dimension')
        return {'schema': 'F10-LINEAR-CERTIFICATE/v1', 'status': 'CANDIDATE-ONLY',
                'rows': 217, 'columns': 1638, 'branch': branch,
                'witness': [wire(c) for c in witness],
                'row_order': 'T-degree k=0..30 then v-degree a=0..6',
                'column_order': 'input i=0..8 then multiplier j=0..25 then v-degree ell=0..6',
                'construction_trace': trace}

    active = []
    for leaf in leaves:
        a = leaf['a']
        b = a.fifth(a.project(q))
        leaf['target'] = b
        leaf['hs'] = [[] for _ in range(9)]
        if leaf['d'] < 0:
            if b:
                # Coordinate functional on the entire all-zero component.
                # Reducedness ensures q != 0 implies q^5 != 0; actually
                # inspect b, and normalize by a NONZERO RATIONAL coordinate.
                k = next(i for i, c in enumerate(b) if c)
                l = next(i for i, c in enumerate(b[k]) if c)
                beta = b[k][l]
                values = []
                for old_k in range(31):
                    for old_l in range(7):
                        image = a.red([Q(0)] * old_l + [Q(1)])
                        values.append((image[l] if l < len(image) else Q(0)) / beta
                                      if old_k == k else Q(0))
                return certificate('SEPARATOR', values)
        elif leaf['d'] == 0:
            leaf['hs'][leaf['pivot']] = a.scale(b, leaf['inverse'])
        else:
            active.append(leaf)

    # Direct sum of all positive-degree remainder modules. The coefficient
    # matrix is at most 35 by 280; b and I are appended for exact extraction.
    rows = sum(leaf['a'].e * leaf['d'] for leaf in active)
    columns = 8 * rows
    trace.update({'small_rows': rows, 'small_columns': columns})
    require(rows <= 35 and columns <= 280, 'small direct-sum dimension bound')
    solution = []
    if rows:
        augmented = flint.fmpq_mat(rows, columns + 1 + rows)
        def fq(c):
            return flint.fmpq(c.numerator, c.denominator)
        row_base = 0
        column_base = 0
        for leaf in active:
            a, d, monic = leaf['a'], leaf['d'], leaf['monic']
            leaf['row_base'], leaf['column_base'] = row_base, column_base
            local_rows = a.e * d
            target = a.vector(a.divide(leaf['target'], monic)[1], d)
            for k, c in enumerate(target):
                augmented[row_base + k, columns] = fq(c)
            col = column_base
            for i, f in enumerate(leaf['fs']):
                if i == leaf['pivot']:
                    continue
                for j in range(d):
                    for l in range(a.e):
                        shifted = [[] for _ in range(j)] + a.scale(f, [Q(0)] * l + [Q(1)])
                        vector = a.vector(a.divide(shifted, monic)[1], d)
                        for k, c in enumerate(vector):
                            augmented[row_base + k, col] = fq(c)
                        col += 1
            require(col == column_base + 8 * local_rows, 'all small multiplier columns')
            row_base += local_rows
            column_base = col
        require(row_base == rows and column_base == columns, 'complete small direct sum')
        for k in range(rows):
            augmented[k, columns + 1 + k] = flint.fmpq(1, 1)
        reduced, rank = augmented.rref()  # Sole elimination; no second solve.
        trace['rref_calls'] = 1
        require(rank == rows, 'augmented identity block rank')
        pivots = []
        for k in range(rows):
            pivot = next((j for j in range(columns + 1 + rows) if reduced[k, j] != 0), None)
            require(pivot is not None and (not pivots or pivots[-1] < pivot)
                    and reduced[k, pivot] == 1, 'documented RREF pivot form')
            pivots.append(pivot)
        def rational(value):
            text = str(value)
            pieces = text.split('/')
            require(len(pieces) in (1, 2), 'unsupported FLINT rational format')
            num = int(pieces[0]); den = int(pieces[1]) if len(pieces) == 2 else 1
            require(str(num) == pieces[0] and den > 0
                    and (len(pieces) == 1 or str(den) == pieces[1]),
                    'unsupported FLINT rational spelling')
            return Q(num, den)
        if columns in pivots:
            k = pivots.index(columns)
            mu = [rational(reduced[k, columns + 1 + j]) for j in range(rows)]
            values = [Q(0) for _ in range(217)]
            for leaf in active:
                a, d, monic = leaf['a'], leaf['d'], leaf['monic']
                start = leaf['row_base']
                functional = mu[start:start + a.e * d]
                power = [[Q(1)]]
                for old_k in range(31):
                    for old_l in range(7):
                        image = a.vector(a.scale(power, a.red([Q(0)] * old_l + [Q(1)])), d)
                        values[old_k * 7 + old_l] += sum((x * y for x, y in zip(functional, image)), Q(0))
                    power = a.divide([[]] + power, monic)[1]
            # mu is defined on the COMPLETE direct-sum C basis, including
            # coordinates outside the image of the small multiplier map.
            return certificate('SEPARATOR', values)
        solution = [Q(0) for _ in range(columns)]
        for k, pivot in enumerate(pivots):
            if pivot < columns:
                solution[pivot] = rational(reduced[k, columns])

    for leaf in active:
        a, d = leaf['a'], leaf['d']
        col = leaf['column_base']
        numerator = leaf['target']
        for i, f in enumerate(leaf['fs']):
            if i == leaf['pivot']:
                continue
            h = []
            for _ in range(d):
                h.append(trim(solution[col:col + a.e]))
                col += a.e
            h = a.tt(h)
            leaf['hs'][i] = h
            numerator = a.add(numerator, a.scale(a.product(h, f), [Q(-1)]))
        quotient, remainder = a.divide(numerator, leaf['monic'])
        require(not remainder, 'small UNIT solution has exact monic divisibility')
        raw_multiplier = a.scale(quotient, leaf['inverse'])
        require(len(raw_multiplier) <= 26 - d, 'raw pivot multiplier degree bound')
        leaf['hs'][leaf['pivot']] = raw_multiplier

    # CRT only in v; it never raises T degree. fhat was monic, but witnesses
    # are for the RAW generator: h_pivot=(N/fhat)/lc(raw), not N/fhat.
    whole = Coefficients(p)
    hs = [[] for _ in range(9)]
    for leaf in leaves:
        cofactor, remainder = dd(p, leaf['a'].pa)
        require(not remainder, 'CRT exact cofactor')
        g, inverse, _ = dxg(cofactor, leaf['a'].pa)
        require(g == [Q(1)], 'CRT cofactor is a certified unit')
        idempotent = whole.red(dm(cofactor, inverse))
        for other in leaves:
            require(other['a'].red(idempotent) == ([Q(1)] if other is leaf else []),
                    'complete CRT projection identity')
        for i in range(9):
            hs[i] = whole.add(hs[i], whole.scale(leaf['hs'][i], idempotent))
    require(all(len(h) <= 26 for h in hs), 'all nine padded degree-25 multipliers')
    witness = [(h[j][l] if j < len(h) and l < len(h[j]) else Q(0))
               for h in hs for j in range(26) for l in range(7)]
    return certificate('UNIT', witness)

def candidate(data, flint):
    from algebra import Ring, Q, ZERO, require
    r = Ring()
    ids = ['E1/S1', 'E1/S2', 'E1/S3', 'E0/S1', 'E0/S2', 'E0/S3', 'E0/S4', 'P4', 'P11']
    bounds = [3, 3, 2, 4, 3, 3, 2, 2, 5]
    require(data['schema'] == 'F10-R1-NINE-UNIVARIATE/v1'
            and data['variable'] == 'T'
            and data['coefficient_ring'] == 'Q[v]/p(v), entire algebra', 'literal input schema')
    require(data['modulus'] == [[str(c.numerator), str(c.denominator)] for c in r.p],
            'literal full degree-seven modulus')
    require(type(data['rows']) is list and len(data['rows']) == 9, 'all nine rows')
    def dense(wire, degree):
        require(type(wire) is list and len(wire) == degree + 1, 'all dense coefficient slots')
        out = []
        for w in wire:
            coefficient = r.read(w)
            require(all(not any(e[:6]) for e in coefficient), 'coefficient in entire B')
            out.append([coefficient.get(ZERO[:-1] + (l,), Q(0)) for l in range(7)])
        return out
    fs = []
    for obj, name, degree in zip(data['rows'], ids, bounds):
        require(obj['id'] == name and type(obj['degree_bound']) is int
                and obj['degree_bound'] == degree, 'indexed row/envelope')
        fs.append(dense(obj['coefficients'], degree))
    guard = data['guard']
    require(set(guard) == {'variable', 'equation', 'q', 'factors'}
            and guard['variable'] == 'xi' and guard['equation'] == 'xi*q(T)-1'
            and guard['factors'] == ['r', 'h0'], 'full guard')
    q = dense(guard['q'], 5)
    return generic_candidate([c / r.p[-1] for c in r.p], fs, q, flint)

def main():
    if len(sys.argv) != 6:
        raise SystemExit('AUTHORITY UNIVARIATE FULL_RECEIPT ROOT_ACCEPTANCE CERTIFICATE')
    custody = authorize(sys.argv[1], __file__, 'build')
    from evidence import verified, producer_environment, write_exclusive, sha, require
    data, binding, spec = verified(*sys.argv[1:5])
    environment = producer_environment(spec)
    import flint  # Missing/incompatible package: fail closed, never install/fallback.
    require(str(getattr(flint, '__version__', '')) == environment['version']
            and str(Path(flint.__file__).resolve()) == environment['module_file']
            and sha(flint.__file__) == environment['module_sha256'], 'installed FLINT binding differs')
    certificate = candidate(data, flint)
    certificate.update({'binding': binding, 'execution': custody,
                        'solver_sha256': sha(__file__), 'engine': environment})
    write_exclusive(sys.argv[5], certificate)
    print('EXACT-Q CANDIDATE ONLY; INDEPENDENT CHECK REQUIRED')

if __name__ == '__main__':
    main()
