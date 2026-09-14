"""STATIC / UNEXECUTED synthetic full-certificate controls.

CLI: AUTHORITY OUTPUT. This is not an actual-source acceptance entrypoint.
Only main under a fresh, separately registered AWS build authority may call
the arithmetic functions. No test, syntax/import check or fixture was run
during preparation. The sibling solver is supplied later; no fallback exists.
"""
import hashlib
import os
from pathlib import Path
import sys

sys.dont_write_bytecode = True

FROZEN = {
    'execution_gate.py': 'cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6',
    'evidence.py': 'cbe5a9e05c1718cd7911e68302611e0131774e10c501ca0fa890510d0ccb7767',
    'algebra.py': '7d565299faba1a8921fdb36f345af2cae49254fa59730e0e3c7a1f98e587d9dc',
    'checker.py': 'bb4263e1149eb1ba03d2dc47f5db339df6b05829280730ccf6c8420e0bc07045',
}
CASES = (
    'allzero-q0', 'allzero-q1', 'constant-degree25', 'raw-two-T',
    'nonreduced-remainder', 'lost-component', 'varying-pivot',
    'all-generators',
)
NEGATIVES = ('scaled-separator', 'raw-unit-plus-one', 'short-witness',
             'nonreduced-coefficient-modulus')
ROW_ORDER = 'T-degree k=0..30 then v-degree a=0..6'
COLUMN_ORDER = 'input i=0..8 then multiplier j=0..25 then v-degree ell=0..6'


def need(condition, reason):
    if not condition:
        raise ValueError(reason)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_fraction(wire, Q):
    need(type(wire) is list and len(wire) == 2, 'rational pair shape')
    n, d = wire
    need(type(n) is str and type(d) is str, 'canonical rational strings only')
    numerator, denominator = int(n), int(d)
    need(str(numerator) == n and str(denominator) == d and denominator > 0,
         'canonical reduced rational')
    value = Q(numerator, denominator)
    need(value.numerator == numerator and value.denominator == denominator,
         'canonical reduced rational')
    return value


def fraction_wire(value):
    return [str(value.numerator), str(value.denominator)]


def input_wire(p, fs, q):
    return {'p': [fraction_wire(x) for x in p],
            'fs': [[[fraction_wire(x) for x in c] for c in f] for f in fs],
            'q': [[fraction_wire(x) for x in c] for c in q]}


def parse_input(wire):
    from fractions import Fraction as Q
    need(type(wire) is dict and set(wire) == {'p', 'fs', 'q'},
         'synthetic input fields')
    need(type(wire['p']) is list and len(wire['p']) == 8,
         'synthetic modulus degree seven')
    p = [read_fraction(x, Q) for x in wire['p']]

    def polynomial(value):
        need(type(value) is list and 1 <= len(value) <= 6,
             'generic T envelope')
        out = []
        for coefficient in value:
            need(type(coefficient) is list and len(coefficient) == 7,
                 'complete seven-coordinate coefficient')
            out.append([read_fraction(x, Q) for x in coefficient])
        return out

    need(type(wire['fs']) is list and len(wire['fs']) == 9,
         'all nine synthetic generators')
    return p, [polynomial(f) for f in wire['fs']], polynomial(wire['q'])


class DenseFixture:
    """Independent dense Fraction arithmetic using the supplied fixture p.

    No solver/algebra/FLINT helper or matrix is an input to this verifier.
    This is deliberately not the unchanged actual-source checker.
    """

    def __init__(self, p):
        from fractions import Fraction
        self.Q = Fraction
        need(type(p) is list and len(p) == 8
             and all(type(c) is Fraction for c in p) and p[-1] == 1,
             'generic monic degree-seven modulus')
        self.p = p[:]
        derivative = [Fraction(i) * p[i] for i in range(1, 8)]
        left, right = self.trim(p), self.trim(derivative)
        while right:
            left, right = right, self.remainder(left, right)
        need(len(left) == 1, 'generic modulus must be squarefree')

    @staticmethod
    def trim(values):
        out = list(values)
        while out and out[-1] == 0:
            out.pop()
        return out

    def remainder(self, dividend, divisor):
        out = self.trim(dividend)
        divisor = self.trim(divisor)
        need(bool(divisor), 'zero rational-polynomial divisor')
        while len(out) >= len(divisor):
            shift = len(out) - len(divisor)
            scale = out[-1] / divisor[-1]
            for i, c in enumerate(divisor):
                out[shift + i] -= scale * c
            out = self.trim(out)
        return out

    def zero(self):
        return [self.Q(0) for _ in range(7)]

    def one(self):
        out = self.zero()
        out[0] = self.Q(1)
        return out

    def bmul(self, left, right):
        out = [self.Q(0) for _ in range(13)]
        for i in range(7):
            for j in range(7):
                out[i + j] += left[i] * right[j]
        for high in range(12, 6, -1):
            coefficient = out[high]
            for j in range(7):
                out[high - 7 + j] -= coefficient * self.p[j]
            out[high] = self.Q(0)
        return out[:7]

    def tmul(self, left, right):
        out = [self.zero() for _ in range(len(left) + len(right) - 1)]
        for i, a in enumerate(left):
            for j, b in enumerate(right):
                reduced = self.bmul(a, b)
                for ell in range(7):
                    out[i + j][ell] += reduced[ell]
        return out

    def verify(self, fs, q, certificate):
        need(type(certificate) is dict, 'certificate object')
        need(not any(key in certificate for key in
                     ('binding', 'execution', 'solver_sha256', 'engine', 'input_evidence')),
             'generic certificate must not carry source/runtime acceptance')
        need(certificate.get('schema') == 'F10-LINEAR-CERTIFICATE/v1'
             and certificate.get('status') == 'CANDIDATE-ONLY'
             and type(certificate.get('rows')) is int and certificate['rows'] == 217
             and type(certificate.get('columns')) is int and certificate['columns'] == 1638,
             'certificate dimension/schema')
        need(certificate.get('row_order') == ROW_ORDER
             and certificate.get('column_order') == COLUMN_ORDER,
             'literal certificate basis ordering')
        branch = certificate.get('branch')
        need(branch in ('UNIT', 'SEPARATOR'), 'certificate branch')
        count = 1638 if branch == 'UNIT' else 217
        wire = certificate.get('witness')
        need(type(wire) is list and len(wire) == count,
             'complete rational witness dimension')
        witness = [read_fraction(x, self.Q) for x in wire]
        target = [self.one()]
        for _ in range(5):
            target = self.tmul(target, q)
        need(len(target) <= 26, 'generic target bound')
        target.extend(self.zero() for _ in range(31 - len(target)))
        if branch == 'UNIT':
            total = [self.zero() for _ in range(31)]
            for i in range(9):
                multiplier = [witness[(i * 26 + j) * 7:(i * 26 + j + 1) * 7]
                              for j in range(26)]
                product = self.tmul(multiplier, fs[i])
                need(len(product) <= 31, 'full product bound')
                for degree, coefficient in enumerate(product):
                    for ell in range(7):
                        total[degree][ell] += coefficient[ell]
            mismatches = []
            checked = 0
            for degree in range(31):
                for ell in range(7):
                    checked += 1
                    if total[degree][ell] != target[degree][ell]:
                        mismatches.append((degree, ell))
            need(checked == 217, 'all unit coordinates checked')
            need(not mismatches, 'full 217-coordinate sum h_i f_i equals q^5')
            return {'branch': branch, 'checked_coordinates': checked,
                    'multipliers': 9, 'multiplier_degree_bound': 25}
        bad_columns = []
        checked = 0
        for i in range(9):
            for j in range(26):
                for ell in range(7):
                    basis = self.zero()
                    basis[ell] = self.Q(1)
                    pairing = self.Q(0)
                    for degree, coefficient in enumerate(fs[i]):
                        reduced = self.bmul(basis, coefficient)
                        for a in range(7):
                            pairing += witness[(j + degree) * 7 + a] * reduced[a]
                    if pairing != 0:
                        bad_columns.append((i, j, ell))
                    checked += 1
        target_pairing = self.Q(0)
        target_coordinates = 0
        for degree in range(31):
            for ell in range(7):
                target_pairing += witness[degree * 7 + ell] * target[degree][ell]
                target_coordinates += 1
        need(checked == 1638 and target_coordinates == 217,
             'all separator pairings checked')
        need(not bad_columns, 'full 1638-column annihilation')
        need(target_pairing == 1, 'dual target normalization equals one')
        return {'branch': branch, 'checked_columns': checked,
                'target_coordinates': target_coordinates}


def fixture_table():
    # Called only after the metadata gate AND installed native pins, at runtime.
    from fractions import Fraction as Q

    def product_linear(indices):
        out = [Q(1)]
        for root in indices:
            following = [Q(0) for _ in range(len(out) + 1)]
            for i, c in enumerate(out):
                following[i] -= Q(root) * c
                following[i + 1] += c
            out = following
        return out

    p = product_linear(range(7))
    e0 = [c / Q(720) for c in product_linear(range(1, 7))]

    def scalar(c):
        return [Q(c)] + [Q(0) for _ in range(6)]

    zero, one = scalar(0), scalar(1)
    complement = [one[i] - e0[i] for i in range(7)]

    def case(index, generators, guard, branch):
        fs = [[scalar(0)] for _ in range(9)]
        for i, polynomial in generators.items():
            fs[i] = polynomial
        return {'id': CASES[index], 'input': input_wire(p, fs, guard),
                'expected_branch': branch}

    return [
        case(0, {}, [zero], 'UNIT'),
        case(1, {}, [one], 'SEPARATOR'),
        case(2, {0: [one]}, [scalar(0) for _ in range(5)] + [one], 'UNIT'),
        case(3, {0: [zero, scalar(2)]}, [zero, one], 'UNIT'),
        case(4, {0: [zero, zero, one], 1: [one, one]}, [one], 'UNIT'),
        case(5, {0: [e0, complement]}, [complement], 'SEPARATOR'),
        case(6, {0: [zero, e0], 1: [zero, zero, complement]}, [zero, one], 'UNIT'),
        case(7, {0: [zero, one], 1: [scalar(-1), one]}, [one], 'UNIT'),
    ]


def run_controls(generic_candidate, flint, output, custody, spec, environment):
    from copy import deepcopy
    from fractions import Fraction as Q
    from evidence import load, write_exclusive

    def freeze(path, obj):
        write_exclusive(path, obj)
        Path(path).chmod(0o444)
        before = digest(path)
        recovered = load(Path(path).read_bytes())
        need(recovered == obj and digest(path) == before, 'fixture read-back changed')
        return recovered, {'path': str(path), 'sha256': before}

    def stable(record):
        need(digest(record['path']) == record['sha256'], 'frozen generic artifact changed')

    positives, negatives, retained = [], [], []
    for fixture in fixture_table():
        name = fixture['id']
        original, input_pin = freeze(str(output) + '.' + name + '.input.json', fixture)
        p, fs, q = parse_input(original['input'])
        candidate = generic_candidate(p, fs, q, flint)
        need(input_wire(p, fs, q) == original['input'], 'candidate mutated fixture input')
        certificate, cert_pin = freeze(str(output) + '.' + name + '.candidate.json', candidate)
        # Fresh input read-back; no candidate arithmetic, helper or trace is trusted.
        reread = load(Path(input_pin['path']).read_bytes())
        need(reread == original, 'positive input read-back')
        p, fs, q = parse_input(reread['input'])
        result = DenseFixture(p).verify(fs, q, certificate)
        need(result['branch'] == original['expected_branch'], 'wrong hand-derived branch')
        stable(input_pin)
        stable(cert_pin)
        positives.append({'id': name, 'status': 'VERIFIED-SYNTHETIC-ONLY',
                          'input': input_pin, 'certificate': cert_pin, 'check': result})
        retained.append((original, certificate))
        print('GENERIC POSITIVE ' + name + ' VERIFIED', flush=True)

    def reject(name, obj, original, expected_reason, invoke):
        need(obj != original, 'negative object did not change')
        recovered, pin = freeze(str(output) + '.' + name + '.negative.json', obj)
        try:
            invoke(recovered)
        except ValueError as error:
            need(type(error) is ValueError and str(error) == expected_reason,
                 'unexpected negative refusal: ' + repr(error))
            result = {'id': name, 'status': 'EXPECTED-REFUSAL', 'fixture': pin,
                      'exception_class': 'ValueError', 'reason': str(error)}
        else:
            raise ValueError('changed generic object was accepted: ' + name)
        stable(pin)
        negatives.append(result)
        print('GENERIC NEGATIVE ' + name + ' EXPECTED REFUSAL', flush=True)

    def verify_object(obj):
        p, fs, q = parse_input(obj['input'])
        return DenseFixture(p).verify(fs, q, obj['certificate'])

    original = {'input': retained[1][0]['input'], 'certificate': retained[1][1]}
    changed = deepcopy(original)
    changed['certificate']['witness'] = [fraction_wire(2 * read_fraction(c, Q))
                                         for c in changed['certificate']['witness']]
    reject(NEGATIVES[0], changed, original, 'dual target normalization equals one', verify_object)

    original = {'input': retained[3][0]['input'], 'certificate': retained[3][1]}
    changed = deepcopy(original)
    changed['certificate']['witness'][0] = fraction_wire(
        read_fraction(changed['certificate']['witness'][0], Q) + 1)
    reject(NEGATIVES[1], changed, original,
           'full 217-coordinate sum h_i f_i equals q^5', verify_object)

    original = {'input': retained[1][0]['input'], 'certificate': retained[1][1]}
    changed = deepcopy(original)
    changed['certificate']['witness'].pop()
    reject(NEGATIVES[2], changed, original, 'complete rational witness dimension', verify_object)

    original = deepcopy(retained[3][0]['input'])
    changed = deepcopy(original)
    changed['p'] = [fraction_wire(Q(0)) for _ in range(7)] + [fraction_wire(Q(1))]

    def candidate_refusal(obj):
        p, fs, q = parse_input(obj)
        return generic_candidate(p, fs, q, flint)

    reject(NEGATIVES[3], changed, original, 'generic modulus must be squarefree', candidate_refusal)
    need(len(positives) == 8 and len(negatives) == 4, 'exact finite control inventory')
    for result in positives:
        stable(result['input'])
        stable(result['certificate'])
    for result in negatives:
        stable(result['fixture'])
    # Post-pins include the declared native files; there is no source artifact.
    for path, expected in spec['file_sha256'].items():
        need(digest(path) == expected, 'registered file changed after controls')
    need(digest(sys.argv[1]) == custody['authority_sha256'], 'authority changed after controls')
    summary = {'schema': 'F10-GENERIC-CONTROLS/v1',
               'status': 'ALL-12-GENERIC-CONTROLS-VERIFIED-NO-SOURCE-ACCEPTANCE',
               'scope': 'synthetic rank-seven fixtures only; no actual-source decision or acceptance',
               'execution': custody, 'engine': environment,
               'harness_sha256': digest(__file__),
               'solver_sha256': digest(Path(__file__).with_name('solver.py')),
               'positives': positives, 'negatives': negatives}
    write_exclusive(output, summary)
    print(summary['status'], flush=True)


def main():
    if len(sys.argv) != 3:
        raise SystemExit('AUTHORITY OUTPUT')
    root = Path(__file__).resolve().parent
    gate = root / 'execution_gate.py'
    need(digest(gate) == FROZEN['execution_gate.py'], 'unchanged execution gate required')
    sys.path.insert(0, str(root))
    from execution_gate import authorize
    custody = authorize(sys.argv[1], __file__, 'build')
    need(digest(root / 'evidence.py') == FROZEN['evidence.py'], 'unchanged evidence required')
    from evidence import load, producer_environment
    authority_raw = Path(sys.argv[1]).read_bytes()
    need(hashlib.sha256(authority_raw).hexdigest() == custody['authority_sha256'],
         'authority changed before metadata binding')
    spec = load(authority_raw)
    need(spec.get('univariate_acceptance') is None,
         'generic controls must not use source acceptance')
    need(Path.cwd().resolve() == root, 'flat registered package cwd required')
    need(Path(sys.executable).resolve() == Path('/usr/bin/python3').resolve(),
         'registered native interpreter required')
    for name in ('generic_controls.py', 'solver.py', 'checker.py', 'evidence.py',
                 'algebra.py', 'execution_gate.py'):
        path = root / name
        need(spec['file_sha256'].get(str(path)) == digest(path), 'all flat package pins required')
        if name in FROZEN:
            need(digest(path) == FROZEN[name], 'unchanged retained module required: ' + name)
    output = Path(sys.argv[2])
    need(output.is_absolute() and output.parent.resolve() == root,
         'registered output must be absolute in the flat package')
    paths = [str(output)]
    for name in CASES:
        paths.extend((str(output) + '.' + name + '.input.json',
                      str(output) + '.' + name + '.candidate.json'))
    paths.extend(str(output) + '.' + name + '.negative.json' for name in NEGATIVES)
    need(not any(os.path.lexists(path) for path in paths), 'all generic outputs must be absent')
    environment = producer_environment(spec)
    # authorize already checked every declared native-file hash. ROOT owns
    # completeness of that installed dependency closure; no discovery occurs.
    import flint
    need(str(getattr(flint, '__version__', '')) == environment['version']
         and str(Path(flint.__file__).resolve()) == environment['module_file']
         and digest(flint.__file__) == environment['module_sha256'],
         'installed FLINT binding differs')
    from solver import generic_candidate
    run_controls(generic_candidate, flint, output, custody, spec, environment)


if __name__ == '__main__':
    main()
