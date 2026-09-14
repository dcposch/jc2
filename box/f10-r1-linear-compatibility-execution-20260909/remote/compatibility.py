"""DISABLED/UNEXECUTED generic verifier and tiny installed-API harness.
AUTHORITY GENERIC_PLAN OUTPUT. No actual source artifact or acceptance.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from execution_gate import authorize

def main():
    if len(sys.argv) != 4:
        raise SystemExit('AUTHORITY GENERIC_PLAN OUTPUT')
    custody = authorize(sys.argv[1], __file__, 'check')
    from evidence import load, sha, require, write_exclusive, producer_environment
    spec = load(Path(sys.argv[1]).read_bytes())
    require(spec.get('generic_only') is True and 'univariate_acceptance' not in spec
            and 'normalized_acceptance' not in spec, 'generic-only authorization; no source acceptance')
    planpath = Path(sys.argv[2]).resolve(strict=True)
    require(spec['file_sha256'].get(str(planpath)) == spec.get('generic_plan_sha256') == sha(planpath),
            'exact generic plan pin')
    plan = load(planpath.read_bytes())
    require(plan.get('schema') == 'F10-GENERIC-COMPATIBILITY-PLAN/v1'
            and plan.get('generic_only') is True and plan.get('actual_source_inputs') == []
            and plan.get('verifier_calls') == 12 and plan.get('flint_rref_calls') == 2,
            'finite generic compatibility plan')
    expected = {
        'checker.py': '122842e5cf38a0eab2585c7e894c1ca9d9758dd643830d5447800642554fdf69',
        'evidence.py': 'cbe5a9e05c1718cd7911e68302611e0131774e10c501ca0fa890510d0ccb7767',
        'algebra.py': '7d565299faba1a8921fdb36f345af2cae49254fa59730e0e3c7a1f98e587d9dc',
        'execution_gate.py': 'cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6'}
    for name, digest in expected.items():
        path = Path(__file__).with_name(name).resolve(strict=True)
        require(sha(path) == digest == spec['file_sha256'].get(str(path)), 'frozen generic code pin')
    environment = producer_environment(spec)  # Metadata only; NOT verified().
    import flint
    require(str(getattr(flint, '__version__', '')) == environment['version']
            and str(Path(flint.__file__).resolve()) == environment['module_file']
            and sha(flint.__file__) == environment['module_sha256'], 'installed FLINT binding differs')
    # All arithmetic imports/allocations follow authority and package pins.
    import checker
    import copy
    import json
    from fractions import Fraction
    from algebra import modulus
    K = 9007199254740993
    require(K > 2**53 and int(float(K)) == K - 1, 'genuine greater-than-2^53 rounding precondition')
    api = []
    # Exactly three standalone rational constructions/format checks.
    scalar_cases = [(0, 1, '0'), (K, 1, str(K)), (K, 2, str(K) + '/2')]
    for n, d, spelling in scalar_cases:
        value = flint.fmpq(n, d)
        require(str(value) == spelling, 'installed canonical rational string API')
        api.append({'numerator': str(n), 'denominator': str(d), 'observed': str(value)})
    # Two fixed 2x5 matrices [M|b|I2], not the actual 217x1856 matrix.
    matrices = [
        ('consistent', [[1, 2, 3, 1, 0], [2, 4, 6, 0, 1]],
         [['1', '2', '3', '0', '1/2'], ['0', '0', '0', '1', '-1/2']], [0, 3]),
        ('separating', [[1, 2, 3, 1, 0], [2, 4, 7, 0, 1]],
         [['1', '2', '0', '7', '-3'], ['0', '0', '1', '-2', '1']], [0, 2])]
    for name, entries, expected_rows, expected_pivots in matrices:
        matrix = flint.fmpq_mat(2, 5)
        for i in range(2):
            for j in range(5):
                matrix[i, j] = flint.fmpq(entries[i][j], 1)
        reduced, rank = matrix.rref()
        require(rank == 2, 'tiny augmented RREF rank')
        rows = [[str(reduced[i, j]) for j in range(5)] for i in range(2)]
        require(rows == expected_rows, 'tiny documented RREF exact entries')
        pivots = [next(j for j in range(5) if reduced[i, j] != 0) for i in range(2)]
        require(pivots == expected_pivots, 'tiny RREF pivot extraction')
        api.append({'matrix': name, 'shape': [2, 5], 'rank': rank, 'rows': rows, 'pivots': pivots})

    ids = ['E1/S1', 'E1/S2', 'E1/S3', 'E0/S1', 'E0/S2', 'E0/S3', 'E0/S4', 'P4', 'P11']
    bounds = [3, 3, 2, 4, 3, 3, 2, 2, 5]
    def pair(n, d=1):
        c = Fraction(n, d)
        return [str(c.numerator), str(c.denominator)]
    def constant(n, d=1):
        return [[[0, 0, 0, 0, 0, 0, 0], *pair(n, d)]] if n else []
    def monomial(degree, coefficient, exponent=0):
        out = [[] for _ in range(degree + 1)]
        out[exponent] = constant(coefficient)
        return out
    def fixture(kind):
        data = {'schema': 'F10-R1-NINE-UNIVARIATE/v1', 'variable': 'T',
                'coefficient_ring': 'Q[v]/p(v), entire algebra',
                'modulus': [[str(c.numerator), str(c.denominator)] for c in modulus()],
                'rows': [{'id': name, 'degree_bound': bound, 'coefficients': [[] for _ in range(bound + 1)]}
                         for name, bound in zip(ids, bounds)],
                'r': monomial(1, 1), 'h0': monomial(4, 1),
                'guard': {'variable': 'xi', 'equation': 'xi*q(T)-1',
                          'q': monomial(5, 1), 'factors': ['r', 'h0']}}
        branch = 'SEPARATOR' if kind in ('separator-zero', 'separator-T') else 'UNIT'
        witness = [pair(0) for _ in range(217 if branch == 'SEPARATOR' else 1638)]
        if kind == 'unit':
            data['rows'][0]['coefficients'] = monomial(3, 1)
            witness[0] = pair(1)
        elif kind == 'separator-zero':
            witness[0] = pair(1)
        elif kind == 'separator-T':
            data['rows'][0]['coefficients'] = monomial(3, 1, 1)
            witness[0] = pair(1)
        elif kind == 'precision':
            data['rows'][8]['coefficients'] = monomial(5, K, 5)
            data['r'], data['h0'] = monomial(1, 1, 1), monomial(4, 1, 4)
            data['guard']['q'] = monomial(5, 1, 5)
            witness[(8 * 26 + 20) * 7] = pair(1, K)
        elif kind == 'zero-guard':
            data['r'], data['guard']['q'] = monomial(1, 0), monomial(5, 0)
        else:
            raise ValueError('unregistered generic fixture')
        cert = {'schema': 'F10-LINEAR-CERTIFICATE/v1', 'rows': 217, 'columns': 1638,
                'branch': branch, 'witness': witness,
                'row_order': 'T-degree k=0..30 then v-degree a=0..6',
                'column_order': 'input i=0..8 then multiplier j=0..25 then v-degree ell=0..6'}
        # Deliberately no implementation_sha256, source input_evidence,
        # acceptance or production execution fields: these are NOT sources.
        return {'schema': 'GENERIC-VERIFIER-TEST/v1', 'generic_only': True,
                'kind': kind, 'input': data, 'certificate': cert}
    outcomes = []
    directory = Path(sys.argv[3]).parent
    def exercise(name, original, mutation=None, reason=None, extra_check=None):
        obj = copy.deepcopy(original)
        if mutation is not None:
            mutation(obj)
            require(obj != original, 'negative generic fixture must change')
        path = directory / ('generic-fixture-' + name + '.json')
        write_exclusive(path, obj)
        digest = sha(path)
        reread = json.loads(path.read_text())
        require(reread == obj, 'generic fixture serialized exact retention')
        if extra_check is not None:
            extra_check(reread)
        try:
            result = checker.verify(reread['input'], reread['certificate'])
        except Exception as exc:
            require(reason is not None and type(exc) is ValueError and str(exc) == reason,
                    name + ': unexpected rejection ' + type(exc).__name__ + ': ' + str(exc))
            result = {'status': 'EXPECTED-REJECTION', 'reason': str(exc)}
        else:
            require(reason is None, name + ': corrupted generic fixture accepted')
            expected_status = ('VERIFIED-GENERIC-ZERO-QUOTIENT' if obj['certificate']['branch'] == 'UNIT'
                               else 'VERIFIED-GENERIC-NONZERO-QUOTIENT')
            require(result['status'] == expected_status, 'generic positive branch status')
        require(sha(path) == digest, 'generic fixture changed during verify')
        outcomes.append({'name': name, 'fixture_sha256': digest, 'fixture_bytes': path.stat().st_size,
                         'result': result, 'entrypoint': 'checker.verify IN-PROCESS; generic-only, not checker.main'})
    unit = fixture('unit')
    exercise('unit-positive', unit)
    exercise('unit-negative', unit, lambda f: f['certificate']['witness'].__setitem__(0, pair(2)),
             'full 217-coordinate sum h_i f_i equals q^5')
    zero_sep = fixture('separator-zero')
    exercise('separator-zero-positive', zero_sep)
    exercise('separator-normalization-negative', zero_sep, lambda f: f['certificate']['witness'].__setitem__(0, pair(2)),
             'dual target normalization equals one')
    nonzero_sep = fixture('separator-T')
    exercise('separator-T-positive', nonzero_sep)
    exercise('separator-column-negative', nonzero_sep, lambda f: f['certificate']['witness'].__setitem__(7, pair(1)),
             'dual column annihilation i=0 j=0 ell=0')
    precision = fixture('precision'); position = (8 * 26 + 20) * 7
    def retained_large(f):
        require(f['input']['rows'][8]['coefficients'][5][0][1:] == [str(K), '1']
                and f['certificate']['witness'][position] == ['1', str(K)],
                'successful nested parser fixture retains exact large strings')
    exercise('precision-positive', precision, extra_check=retained_large)
    exercise('high-T30-negative', precision,
             lambda f: f['certificate']['witness'].__setitem__((8 * 26 + 25) * 7, pair(1)),
             'full 217-coordinate sum h_i f_i equals q^5')
    exercise('rounded-canonical-string-negative', precision,
             lambda f: f['certificate']['witness'].__setitem__(position, ['1', str(int(float(K)))]),
             'full 217-coordinate sum h_i f_i equals q^5')
    exercise('float-type-negative', precision,
             lambda f: f['certificate']['witness'].__setitem__(position, ['1', float(K)]),
             'canonical rational strings only')
    zero_guard = fixture('zero-guard')
    exercise('zero-guard-positive', zero_guard)
    def false_separator(f):
        f['certificate']['branch'] = 'SEPARATOR'
        f['certificate']['witness'] = [pair(1)] + [pair(0) for _ in range(216)]
    exercise('zero-guard-false-separator', zero_guard, false_separator,
             'dual target normalization equals one')
    require(len(outcomes) == 12 and sum(o['result']['status'] == 'EXPECTED-REJECTION' for o in outcomes) == 7,
            'exact five-positive seven-negative generic inventory')
    require(sha(planpath) == spec['generic_plan_sha256'], 'generic plan drift')
    write_exclusive(sys.argv[3], {'status': 'GENERIC-COMPATIBILITY-PASS-NOT-ACTUAL-SOURCE',
        'execution': custody, 'generic_only': True, 'generic_plan_sha256': sha(planpath),
        'harness_sha256': sha(__file__), 'checker_sha256': expected['checker.py'],
        'python_flint': environment, 'api': api, 'outcomes': outcomes,
        'counts': {'verifier_calls': 12, 'positives': 5, 'negatives': 7,
                   'flint_matrix_constructors': 2, 'flint_rref_calls': 2, 'flint_fmpq_constructors': 23},
        'scope': 'generic toy proof/parser tests and tiny installed API only; no source acceptance, actual matrix solve or actual ideal verdict'})
    print('GENERIC COMPATIBILITY ONLY; NO ACTUAL-SOURCE DECISION')

if __name__ == '__main__':
    main()
