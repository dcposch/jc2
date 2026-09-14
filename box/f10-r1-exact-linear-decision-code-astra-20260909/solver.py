"""DISABLED/UNEXECUTED exact 17m candidate producer; ONE FLINT RREF.
AUTHORITY UNIVARIATE FULL_RECEIPT ROOT_ACCEPTANCE CERTIFICATE
No result is a decision until the independent checker accepts it.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from execution_gate import authorize

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
        out = {}
        for k, w in enumerate(wire):
            coefficient = r.read(w)
            require(all(not any(e[:6]) for e in coefficient), 'coefficient in entire B')
            out = r.add(out, r.mul(coefficient, r.atom(0, k)))
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
    def vector(poly):
        require(all(not any(e[1:6]) and 0 <= e[0] <= 30 and 0 <= e[6] <= 6
                    for e in poly), 'complete 217-coordinate window')
        return [poly.get((k, 0, 0, 0, 0, 0, a), Q(0))
                for k in range(31) for a in range(7)]
    target = vector(r.pow(q, 5))
    columns = []
    for f in fs:
        for j in range(26):
            for ell in range(7):
                columns.append(vector(r.mul(f, r.mul(r.atom(0, j), r.atom(6, ell)))))
    require(len(columns) == 1638, 'every multiplier column')
    # Identity block records every row operation; there is no second solve.
    augmented = flint.fmpq_mat(217, 1856)
    def fq(c):
        return flint.fmpq(c.numerator, c.denominator)
    for row in range(217):
        for col in range(1638):
            augmented[row, col] = fq(columns[col][row])
        augmented[row, 1638] = fq(target[row])
        augmented[row, 1639 + row] = flint.fmpq(1, 1)
    reduced, rank = augmented.rref()  # Sole exact-Q elimination call.
    require(rank == 217, 'augmented identity block rank')
    pivots = []
    for row in range(217):
        pivot = next((col for col in range(1856) if reduced[row, col] != 0), None)
        require(pivot is not None and (not pivots or pivots[-1] < pivot)
                and reduced[row, pivot] == 1, 'documented RREF pivot form')
        pivots.append(pivot)
    # Parse only FLINT's one-rational string, never an expression/eval. The
    # independent checker still proves every rational identity from scratch.
    def rational(value):
        text = str(value)
        pieces = text.split('/')
        require(len(pieces) in (1, 2), 'unsupported FLINT rational format')
        num = int(pieces[0]); den = int(pieces[1]) if len(pieces) == 2 else 1
        require(str(num) == pieces[0] and den > 0
                and (len(pieces) == 1 or str(den) == pieces[1]), 'unsupported FLINT rational spelling')
        out = Q(num, den)
        return [str(out.numerator), str(out.denominator)]
    if 1638 in pivots:
        row = pivots.index(1638)
        witness = [rational(reduced[row, 1639 + i]) for i in range(217)]
        branch = 'SEPARATOR'
    else:
        witness = [['0', '1'] for _ in range(1638)]
        for row, pivot in enumerate(pivots):
            if pivot < 1638:
                witness[pivot] = rational(reduced[row, 1638])
        branch = 'UNIT'
    return {'schema': 'F10-LINEAR-CERTIFICATE/v1', 'status': 'CANDIDATE-ONLY',
            'rows': 217, 'columns': 1638, 'branch': branch, 'witness': witness,
            'row_order': 'T-degree k=0..30 then v-degree a=0..6',
            'column_order': 'input i=0..8 then multiplier j=0..25 then v-degree ell=0..6'}

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
