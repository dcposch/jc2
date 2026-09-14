"""STATIC / UNEXECUTED separate decimal regression, never source acceptance.
AUTHORITY INPUT MODE OUTPUT; MODE is old, new, or fresh-check.
All arithmetic below requires a separately registered capped AWS child.
"""
import sys
sys.dont_write_bytecode = True
import hashlib
import os
from pathlib import Path

LIMIT = 16777216
FROZEN = {
    'oldsolver.py': '961e22e64ec768da6d78a886aa987f7ebaf0325b21b87c68e04db88e91778589',
    'solver.py': '4e9bb9d28c60360b39629d059b42778744c7d43c5677b52fb8351e3405e4d3f4',
    'checker.py': 'bb4263e1149eb1ba03d2dc47f5db339df6b05829280730ccf6c8420e0bc07045',
    'generic_controls.py': '259990f7f226e0509a18f8a230f9bbc66b1241c2ab09f511fa4134110f6a1717',
    'algebra.py': '7d565299faba1a8921fdb36f345af2cae49254fa59730e0e3c7a1f98e587d9dc',
    'evidence.py': 'cbe5a9e05c1718cd7911e68302611e0131774e10c501ca0fa890510d0ccb7767',
    'execution_gate.py': 'cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6',
}


def need(ok, why):
    if not ok:
        raise ValueError(why)


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(262144), b''):
            h.update(block)
    return h.hexdigest()


def read_bounded(path, maximum=LIMIT):
    path = Path(path)
    need(path.is_file() and not path.is_symlink(), 'regular nonsymlink input required')
    need(path.stat().st_size <= maximum, 'input exceeds finite read bound')
    with path.open('rb') as stream:
        raw = stream.read(maximum + 1)
    need(len(raw) <= maximum, 'input grew beyond finite read bound')
    return raw


def freeze(path, obj, load):
    import json
    raw = (json.dumps(obj, sort_keys=True, separators=(',', ':'), allow_nan=False) + '\n').encode()
    need(len(raw) <= LIMIT, 'output exceeds sixteen MiB')
    with Path(path).open('xb') as stream:
        stream.write(raw)
    Path(path).chmod(0o444)
    recovered = read_bounded(path)
    need(recovered == raw and load(recovered) == obj, 'exclusive artifact read-back differs')
    return {'path': str(path), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def primitive_fixture():
    # NO decimal parsing, formatting, input_wire, solver priming or setter.
    from fractions import Fraction as Q
    from algebra import modulus
    N = 10 ** 7421 + 1
    raw_p = modulus()
    need(len(raw_p) == 8 and raw_p[-1] != 0, 'literal fixed modulus degree')
    p = [c / raw_p[-1] for c in raw_p]
    def scalar(x):
        return [Q(x)] + [Q(0) for _ in range(6)]
    fs = [[scalar(0)] for _ in range(9)]
    fs[0] = [scalar(0), scalar(0), scalar(1)]
    fs[1] = [scalar(1), scalar(N), scalar(0), scalar(1)]
    return N, raw_p, p, fs, [scalar(1)]


def actual_bundle(raw_p, fs, certificate):
    # Called ONLY after repaired generic_candidate has set policy to zero.
    def wire(q):
        return [str(q.numerator), str(q.denominator)]
    def coefficient(c):
        return [[[0, 0, 0, 0, 0, 0, i], *wire(q)]
                for i, q in enumerate(c) if q]
    bounds = [3, 3, 2, 4, 3, 3, 2, 2, 5]
    ids = ['E1/S1', 'E1/S2', 'E1/S3', 'E0/S1', 'E0/S2', 'E0/S3', 'E0/S4', 'P4', 'P11']
    rows = []
    for name, degree, f in zip(ids, bounds, fs):
        need(len(f) <= degree + 1, 'synthetic row envelope')
        rows.append({'id': name, 'degree_bound': degree,
                     'coefficients': [coefficient(c) for c in f] + [[] for _ in range(degree + 1 - len(f))]})
    one = [[[0, 0, 0, 0, 0, 0, 0], '1', '1']]
    data = {'schema': 'F10-R1-NINE-UNIVARIATE/v1', 'variable': 'T',
            'coefficient_ring': 'Q[v]/p(v), entire algebra',
            'modulus': [wire(c) for c in raw_p], 'rows': rows,
            'guard': {'variable': 'xi', 'equation': 'xi*q(T)-1', 'factors': ['r', 'h0'],
                      'q': [one] + [[] for _ in range(5)]},
            'r': [one, []], 'h0': [one] + [[] for _ in range(4)]}
    return {'input': data, 'certificate': certificate}


def main():
    need(len(sys.argv) == 5, 'AUTHORITY INPUT MODE OUTPUT')
    authority, input_name, mode, output_name = sys.argv[1:]
    need(mode in ('old', 'new', 'fresh-check'), 'fixed regression mode required')
    need(sys.platform.startswith('linux'), 'Linux registered child required')
    root = Path(__file__).resolve().parent
    need(Path.cwd().resolve() == root, 'flat-package cwd required')
    gate = root / 'execution_gate.py'
    need(digest(gate) == FROZEN['execution_gate.py'], 'unchanged gate hash before import')
    sys.path.insert(0, str(root))
    from execution_gate import authorize
    custody = authorize(authority, __file__, 'check' if mode == 'fresh-check' else 'build')
    need(digest(root / 'evidence.py') == FROZEN['evidence.py'], 'unchanged evidence before import')
    from evidence import load, producer_environment
    import resource
    authority_path = Path(authority).resolve(strict=True)
    raw_auth = read_bounded(authority_path, 65536)
    need(hashlib.sha256(raw_auth).hexdigest() == custody['authority_sha256'], 'authority re-read changed')
    spec = load(raw_auth)
    need(spec.get('univariate_acceptance') is None and spec.get('synthetic_only') is True
         and spec.get('large_decimal_mode') == mode, 'explicit synthetic-only mode, no source acceptance')
    need(spec.get('file_size_limit_bytes') == LIMIT
         and resource.getrlimit(resource.RLIMIT_FSIZE) == (LIMIT, LIMIT), 'inherited exact sixteen-MiB file cap')
    need(Path(sys.executable).resolve() == Path('/usr/bin/python3').resolve(), 'registered interpreter')
    files = spec['file_sha256']
    for name, expected in FROZEN.items():
        path = root / name
        need(path.is_file() and not path.is_symlink()
             and files.get(str(path)) == expected == digest(path), 'fixed flat sibling pin: ' + name)
    need(files.get(str(Path(__file__).resolve())) == digest(__file__)
         and '/usr/bin/python3' in files, 'helper and interpreter pins required')
    inp, output = Path(input_name), Path(output_name)
    need(inp.is_absolute() and inp.parent == root and inp != output, 'flat absolute pinned INPUT')
    need(output.is_absolute() and output.parent == root, 'flat absolute OUTPUT')
    suffixes = ('', '.fixture.json', '.certificate.json', '.bundle.json', '.mutation.json', '.failure.json')
    outputs = [Path(str(output) + suffix) for suffix in suffixes]
    need(not any(os.path.lexists(p) for p in outputs), 'all exclusive regression outputs absent')
    need(not any(str(p) in files or p == inp or p == authority_path for p in outputs), 'outputs must not alias inputs')
    raw_input = read_bounded(inp)
    input_sha = hashlib.sha256(raw_input).hexdigest()
    need(files.get(str(inp)) == input_sha, 'explicit INPUT pin required in every mode')
    environment = producer_environment(spec)  # Metadata only; no FLINT import.
    for filename, expected in files.items():
        need(digest(filename) == expected, 'registered input/native file changed before science')
    need(digest(authority_path) == custody['authority_sha256'], 'authority changed before science')
    need(sys.get_int_max_str_digits() == 4300, 'fresh default4300 interpreter required; no priming')
    entered_limit = 4300
    artifacts = []
    try:
        if mode == 'fresh-check':
            # Loading quoted wires does not turn their digits into integers.
            bundle = load(raw_input)
            need(type(bundle) is dict and set(bundle) == {'input', 'certificate'}, 'synthetic actual-schema bundle')
            cert = bundle['certificate']
            need(type(cert) is dict and cert.get('status') == 'CANDIDATE-ONLY'
                 and not any(k in cert for k in ('binding', 'execution', 'engine', 'solver_sha256', 'input_evidence')),
                 'synthetic certificate only')
            witness_wire = cert.get('witness')
            need(type(witness_wire) is list and len(witness_wire) == 1638
                 and type(witness_wire[0]) is list and len(witness_wire[0]) == 2
                 and type(witness_wire[0][0]) is str and len(witness_wire[0][0]) > 4300
                 and witness_wire[0][1] == '1', 'fresh test must contain a giant quoted coefficient')
            from copy import deepcopy
            pristine = deepcopy(bundle)
            import checker
            need('solver' not in sys.modules and 'oldsolver' not in sys.modules
                 and 'flint' not in sys.modules, 'fresh checker must not import producer or FLINT')
            need(sys.get_int_max_str_digits() == 4300, 'fresh checker unprimed before verify')
            positive = checker.verify(bundle['input'], cert)
            need(sys.get_int_max_str_digits() == 0, 'checker entry did not set decimal policy')
            need(bundle == pristine, 'positive checker mutated its bundle')
            need(positive.get('branch') == 'UNIT' and positive.get('checked_coordinates') == 217
                 and positive.get('multipliers') == 9 and positive.get('multiplier_degree_bound') == 25,
                 'fresh full UNIT verification required')
            from fractions import Fraction
            changed = deepcopy(bundle)
            n, d = cert['witness'][0]
            before = Fraction(int(n), int(d))
            need(before == (10 ** 7421 + 1) ** 2, 'literal giant h1 constant required')
            after = before + 1
            changed['certificate']['witness'][0] = [str(after.numerator), str(after.denominator)]
            need(changed != pristine and len(cert['witness']) == 1638, 'actual changed full witness')
            restored = deepcopy(changed)
            restored['certificate']['witness'][0] = deepcopy(pristine['certificate']['witness'][0])
            need(restored == pristine and bundle == pristine, 'only h1 constant rational may change')
            need(after - before == 1, 'literal coefficient delta one')
            pin = freeze(str(output) + '.mutation.json', changed, load)
            artifacts.append(pin)
            reread = load(read_bounded(pin['path']))
            try:
                checker.verify(reread['input'], reread['certificate'])
            except ValueError as exc:
                need(type(exc) is ValueError and str(exc) == 'full 217-coordinate sum h_i f_i equals q^5',
                     'mutation must fail full identity, not decimal parsing')
                negative = {'exception_class': 'ValueError', 'reason': str(exc)}
            else:
                raise ValueError('giant coefficient mutation was accepted')
            result = {'status': 'FRESH-SYNTHETIC-CHECK-AND-MUTATION-VERIFIED',
                      'positive': positive, 'negative': negative, 'changed_witness_position': 0}
        else:
            descriptor = load(raw_input)
            need(descriptor == {'schema': 'F10-LARGE-DECIMAL-FIXTURE/v1', 'synthetic_only': True,
                                'fixture': 'T2__1+NT+T3', 'N_exponent': 7421}, 'fixed fixture metadata only')
            import flint
            need(str(getattr(flint, '__version__', '')) == environment['version']
                 and str(Path(flint.__file__).resolve()) == environment['module_file']
                 and digest(flint.__file__) == environment['module_sha256'], 'native FLINT binding')
            from copy import deepcopy
            N, raw_p, p, fs, q = primitive_fixture()
            pristine = deepcopy((p, fs, q))
            if mode == 'old':
                from oldsolver import generic_candidate
            else:
                from solver import generic_candidate
            need(sys.get_int_max_str_digits() == 4300, 'no conversion setter before selected API')
            if mode == 'old':
                import traceback
                try:
                    generic_candidate(p, fs, q, flint)
                except ValueError as exc:
                    message = str(exc)
                    trace = traceback.format_exc()
                    need(type(exc) is ValueError and 'Exceeds the limit (4300 digits)' in message
                         and 'integer string conversion' in message, 'old API failed for wrong reason')
                    need(sys.get_int_max_str_digits() == 4300, 'old call changed conversion policy')
                    sites = [{'file': f.filename, 'line': f.lineno, 'function': f.name}
                             for f in traceback.extract_tb(exc.__traceback__)]
                else:
                    raise ValueError('old API did not exhibit required decimal failure: STOP/GAP')
                # AFTER the observed old failure only, for fixture custody.
                sys.set_int_max_str_digits(0)
                result = {'status': 'EXPECTED-OLD-DECIMAL-FAILURE', 'exception_class': 'ValueError',
                          'reason': message, 'traceback': trace, 'sites': sites,
                          'helper_set_zero_only_after_old_failure': True}
            else:
                candidate = generic_candidate(p, fs, q, flint)
                need(sys.get_int_max_str_digits() == 0, 'new API setter missing')
                need(candidate.get('branch') == 'UNIT' and len(candidate.get('witness', [])) == 1638,
                     'new complete UNIT candidate required')
                trace = candidate.get('construction_trace', {})
                need(trace.get('splits') == 0 and trace.get('small_rows') == 14
                     and trace.get('small_columns') == 112 and trace.get('rref_calls') == 1,
                     'required positive-degree quotient/RREF path')
                leaves = trace.get('leaves')
                need(type(leaves) is list and len(leaves) == 1
                     and leaves[0].get('degree') == 2 and leaves[0].get('pivot') == 0
                     and leaves[0].get('modulus') == [[str(c.numerator), str(c.denominator)] for c in p],
                     'entire rank-seven degree-two leaf')
                from generic_controls import DenseFixture, read_fraction
                from fractions import Fraction as Q
                check = DenseFixture(p).verify(fs, q, candidate)
                need(check == {'branch': 'UNIT', 'checked_coordinates': 217,
                               'multipliers': 9, 'multiplier_degree_bound': 25}, 'complete independent fixture verification')
                witness = [read_fraction(w, Q) for w in candidate['witness']]
                expected = [Q(0) for _ in range(1638)]
                expected[0], expected[7], expected[14] = Q(N * N), Q(-1), Q(N)
                expected[182], expected[189] = Q(1), Q(-N)
                need(witness == expected, 'literal full raw-cofactor identity differs')
                artifacts.append(freeze(str(output) + '.certificate.json', candidate, load))
                artifacts.append(freeze(str(output) + '.bundle.json', actual_bundle(raw_p, fs, candidate), load))
                result = {'status': 'NEW-SYNTHETIC-GIANT-UNIT-VERIFIED', 'check': check, 'trace': trace,
                          'literal_cofactor_check': 'ALL1638', 'giant_decimal_digits': 7422}
            need((p, fs, q) == pristine, 'selected API mutated synthetic input')
            from generic_controls import input_wire, parse_input
            wire = input_wire(*pristine)  # First wire creation is AFTER selected API outcome.
            fixture_pin = freeze(str(output) + '.fixture.json', wire, load)
            artifacts.append(fixture_pin)
            reread = parse_input(load(read_bounded(fixture_pin['path'])))
            need(reread == pristine, 'arithmetic pristine fixture differs after wire read-back')
            result['fixture_sha256'] = fixture_pin['sha256']
        for artifact in artifacts:
            need(digest(artifact['path']) == artifact['sha256'], 'retained output drift')
        for filename, expected in files.items():
            need(digest(filename) == expected, 'registered input/native file changed after science')
        need(digest(authority_path) == custody['authority_sha256'] and digest(inp) == input_sha,
             'authority or INPUT changed')
        result.update({'schema': 'F10-LARGE-DECIMAL-CONTROL/v1', 'synthetic_only': True,
                       'source_acceptance': None, 'mode': mode, 'execution': custody,
                       'input_sha256': input_sha, 'entered_decimal_limit': entered_limit,
                       'final_decimal_limit': sys.get_int_max_str_digits(),
                       'helper_sha256': digest(__file__), 'artifacts': artifacts})
        freeze(output, result, load)
        print(result['status'], flush=True)
    except BaseException as exc:
        import traceback
        failure = {'schema': 'F10-LARGE-DECIMAL-CONTROL/v1', 'status': 'STOP-GAP-NO-RETRY',
                   'synthetic_only': True, 'source_acceptance': None, 'mode': mode,
                   'execution': custody, 'input_sha256': input_sha,
                   'exception_class': type(exc).__name__, 'reason': str(exc),
                   'traceback': traceback.format_exc(), 'artifacts': artifacts}
        freeze(str(output) + '.failure.json', failure, load)
        raise


if __name__ == '__main__':
    main()
