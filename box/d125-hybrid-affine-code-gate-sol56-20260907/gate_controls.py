#!/usr/bin/env python3
"""Independent tiny controls for the frozen hybrid-affine producer."""
import resource
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))

import ast
import copy
import hashlib
import json
import sys
import tempfile
import time
from fractions import Fraction as Q
from pathlib import Path

FROZEN = Path('/tmp/jc2-lane.5eg5Cq/inputs')
OWN = Path('/home/ubuntu/jc2/box/d125-hybrid-affine-code-gate-sol56-20260907')
sys.path.insert(0, str(FROZEN))
import construct as C
import replay as R


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


def reject(call, message):
    try:
        call()
    except (ValueError, KeyError, TypeError, StopIteration, FileExistsError):
        return
    raise RuntimeError('mutation accepted: ' + message)


def ops(**changes):
    caps = dict(C.CAPS)
    caps.update(changes)
    return C.Ops(caps, time.monotonic() + 20)


def wire_fraction(value):
    value = Q(value)
    return [[str(value.numerator), str(value.denominator)], ['0', '1']]


def trace(label, polynomial, index=0):
    power = {'GUARD/A/2/1': 1, 'GUARD/B/1/0': 2, 'GUARD/c': 3}.get(label, 0)
    factor = independent_factor(label)
    cofactor = {tuple(sorted((C.K,) * j + (C.Z,) * j)): Q(1) for j in range(power)}
    return {'type': 'row', 'label': label, 'original_index': index,
            'terms': C.wire(polynomial), 'old_from_new_ell_power': factor,
            'guard_power': power, 'guard_cofactor': C.wire(cofactor)}


def independent_factor(label):
    parts = label.split('/')
    if parts[0] == 'J':
        numerator = 38 - int(parts[1]) - int(parts[2])
    elif parts[0] == 'LIFT':
        numerator = (15 if parts[1] == 'A' else 25) + int(parts[3]) - 5 * int(parts[2])
    else:
        return 0
    return None if numerator % 2 else numerator // 2


def test_01_pins_and_paths():
    expected = {
        'construct.py': 'aa65e7104d3fcf5ad868eea952587a6841d784c6f9469c6c42ea2a02913ef264',
        'replay.py': '06475a2a566b4ed617068d65f3a0473ef83c16e2cb357dcb959ee46716781c23',
        'baseline.py': 'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53',
        'test_tiny.py': '54f03f6af6c8e7462f620e11f588bcf0aa209cca18c2fbb465da938c7c3ad2db',
        'REPLAY-CONTRACT.md': 'fa3d8e676b032a419f4ac34f5ebca911a5f208a167a7aa9cc4fb504fec1b09c1',
        'pins.json': '26145bb7938f3bd1016c9030592d9da7a40ffee635fe31ea50108478dbb9a94d',
        'd125-hybrid-affine-code-prep-astra-20260907.md': '18f983a99c0496f4928fc4cb04bee33c1b80d8c7cbd3eeda57bf4ac01bb4e3c0',
    }
    for name, digest in expected.items():
        need(hashlib.sha256((FROZEN / name).read_bytes()).hexdigest() == digest, 'pin ' + name)
    need(Path(C.__file__).resolve() == FROZEN / 'construct.py', 'constructor import path')
    need(Path(R.__file__).resolve() == FROZEN / 'replay.py', 'replay import path')
    need(sys.dont_write_bytecode, '-B absent')


def test_02_shifted_matrix_inverse():
    columns = [1, 2, 3]
    matrix = [[(-1) ** (15-i-t) * __import__('math').comb(15-i, t) for i in columns] for t in range(3)]
    inverse = [[Q(78), Q(12), Q(1)], [Q(168), Q(25), Q(2)], [Q(91), Q(13), Q(1)]]
    need(matrix == [[1, -1, 1], [-14, 13, -12], [91, -78, 66]], 'B15 signs')
    need(sum(matrix[0][j] * (matrix[1][(j+1)%3] * matrix[2][(j+2)%3] - matrix[1][(j+2)%3] * matrix[2][(j+1)%3]) for j in range(3)) == -1, 'determinant')
    need(C.columns('B', 15) == columns and C.inverse(C.matrix(15, columns)) == inverse, 'producer inverse')


def test_03_graph_object_mutations():
    inv = C.inverse(C.matrix(15, [1, 2, 3]))
    graph = {'type': 'graph', 'member': 'B', 'degree': 15,
             'pivots': [[1, 14], [2, 13], [3, 12]],
             'inverse': [[[str(x.numerator), str(x.denominator)] for x in row] for row in inv]}
    R.check_graph(graph, 'B', 15)
    bad = copy.deepcopy(graph); bad['pivots'][0] = [0, 15]
    reject(lambda: R.check_graph(bad, 'B', 15), 'unshifted B15 pivot')
    bad = copy.deepcopy(graph); bad['inverse'][0][0] = ['79', '1']
    reject(lambda: R.check_graph(bad, 'B', 15), 'inverse entry')


def test_04_lift_against_power_expansion():
    base = {(1, 4): Q(1), (0, 1): Q(-1), (0, -1): Q(-1)}
    powers = {(0, 0): Q(1)}
    o = ops()
    for j in range(5):
        coefficients = {(1, j): C.const(2)}
        for exponent in range(-6, 0):
            expected = C.const(2 * powers.get((0, exponent + 1), Q(0)))
            need(C.liftrow(coefficients, 0, exponent, o) == expected, 'independent lift expansion')
        nxt = {}
        for (u, v), a in powers.items():
            for (du, dv), b in base.items():
                nxt[u+du, v+dv] = nxt.get((u+du, v+dv), Q(0)) + a*b
        powers = {key: value for key, value in nxt.items() if value}


def test_05_toy_hermite_mutation():
    o = ops()
    coefficients = {(0, 3): C.const(1), (1, 2): C.const(1), (0, 1): {}, (1, 0): C.mono((0,))}
    C.solve_level(coefficients, 'A', 1, o)
    need(C.liftrow(coefficients, 0, -1, o) == {}, 'toy Hermite forcing')
    coefficients[0, 1] = o.add(coefficients[0, 1], C.const(1))
    need(C.liftrow(coefficients, 0, -1, o) != {}, 'Hermite coefficient mutation invisible')


def test_06_affine_shape_mutations():
    C.shape({(): Q(2), (C.K,): Q(3), (0,): Q(-1)}, 'A')
    C.shape({(): Q(1, 9), (C.K, C.K): Q(5, 9), (20,): Q(2, 3)}, 'B')
    reject(lambda: C.shape({(0, 1): Q(1)}, 'A'), 'nonlinear A')
    reject(lambda: C.shape({(C.K, C.K): Q(1)}, 'A'), 'A k-square')
    reject(lambda: C.shape({(): Q(1, 10)}, 'B'), 'B denominator')
    reject(lambda: C.shape({(C.Z,): Q(1)}, 'B'), 'z in coefficient')


def test_07_jacobian_shape_and_bound():
    need(20*59 + 3*20 + 2*59 + 4 == 1362, 'support census')
    small = {(0, 20): Q(1), (0, C.K, C.K): Q(1, 9), (20, C.K): Q(2, 9), (C.K,)*3: Q(5, 9)}
    C.jshape(small)
    bad = dict(small); bad[(C.K,)*4] = Q(1)
    reject(lambda: C.jshape(bad), 'degree four')
    bad = dict(small); bad[(0, 1)] = Q(1)
    reject(lambda: C.jshape(bad), 'two A variables')
    bad = dict(small); bad[(C.Z,)] = Q(1)
    reject(lambda: C.jshape(bad), 'z support')


def test_08_jrow_sign_target_and_mutation():
    o = ops()
    left = {(1, 0): C.mono((0,))}
    right = {(2, 1): C.mono((20,))}
    expected = {(0, 20): Q(1), (C.K, C.K, C.K): Q(5, 9)}
    need(C.jrow(left, right, 2, 0, o) == expected, 'J sign/target')
    changed = {(2, 1): C.mono((20,), -1)}
    need(C.jrow(left, changed, 2, 0, o) != expected, 'J object mutation invisible')


def test_09_factors_independent():
    labels = ['J/2/0', 'J/1/0', 'LIFT/A/0/-1', 'LIFT/A/0/-2', 'LIFT/B/4/-1', 'FIX/A_g0_p0']
    for label in labels:
        need(C.factor(label) == independent_factor(label), 'constructor factor ' + label)
        need(R.row_factor(label) == independent_factor(label), 'replay factor ' + label)


def test_10_guard_cofactors_and_cover():
    o = ops()
    unit = {(C.K, C.Z): Q(1), (): Q(-1)}
    for power in (1, 2, 3):
        guard = {tuple(sorted((C.K,) * power + (C.Z,) * power)): Q(1), (): Q(-1)}
        cofactor = {tuple(sorted((C.K,) * j + (C.Z,) * j)): Q(1) for j in range(power)}
        need(o.mul(unit, cofactor) == guard, 'geometric cofactor')
        need(R.cover(guard) == {}, 'guard cover')
    bad = {(C.K, C.Z): Q(1)}
    need(o.mul(unit, bad) != C.guard(3), 'dropped cofactor accepted')


def test_11_fixed_maps_independent_pullback():
    cases = [('A', 15, [2, 1], Q(1), (C.K,)),
             ('B', 25, [8, 5], Q(5, 3), (C.K,)),
             ('B', 25, [1, 0], Q(5, 9), (C.K, C.K))]
    for member, degree, point, value, monomial in cases:
        entry = {'point': point, 'name': 'literal_fixed', 'fixed': wire_fraction(value)}
        polynomial = {monomial: value}
        need(R.old_coefficient(polynomial, degree, sum(point)) == {((), 0): value}, 'fixed pullback')
        R.check_coefficient(member, degree, entry, polynomial, {})
        reject(lambda member=member, degree=degree, entry=entry, value=value:
               R.check_coefficient(member, degree, entry, C.const(value), {}), 'fixed exponent')
    zero = {'point': [2, 0], 'name': 'literal_zero', 'fixed': wire_fraction(0)}
    R.check_coefficient('A', 15, zero, {}, {})
    reject(lambda: R.check_coefficient('A', 15, zero, C.const(1), {}), 'fixed zero')


def test_12_decode_wire_mutations():
    valid = C.wire({(): Q(1, 2), (0,): Q(3)})
    need(R.decode(valid, 81) == {(): Q(1, 2), (0,): Q(3)}, 'wire decode')
    reject(lambda: R.decode(list(reversed(valid)), 81), 'term order')
    reject(lambda: R.decode([valid[0], valid[0]], 81), 'duplicate term')
    reject(lambda: R.decode([[[['1', '1'], ['1', '1']], []]], 81), 'nonrational field part')


def test_13_literal_j_transport_mutations():
    o = ops()
    normalized = {(0, 20): Q(1), (C.K,)*3: Q(5, 9)}
    literal = {'label': 'J/2/0', 'terms': C.wire({(0, 1): Q(1), (): Q(5, 9)})}
    maps = {0: {((0,), 7): Q(1)}, 1: {((20,), 11): Q(1)}}
    good = trace('J/2/0', normalized)
    R.verify_row(literal, good, maps, 0, o)
    bad = copy.deepcopy(good); bad['terms'] = C.wire({(0, 20): Q(1)})
    reject(lambda: R.verify_row(literal, bad, maps, 0, o), 'missing target')
    bad = copy.deepcopy(good); bad['old_from_new_ell_power'] = 17
    reject(lambda: R.verify_row(literal, bad, maps, 0, o), 'row factor')
    bad = copy.deepcopy(good); bad['original_index'] = 1
    reject(lambda: R.verify_row(literal, bad, maps, 0, o), 'row index')


def test_14_literal_guard_mutations():
    o = ops()
    literal = {'label': 'GUARD/c', 'terms': []}
    good = trace('GUARD/c', C.guard(3))
    R.verify_row(literal, good, {}, 0, o)
    for field, value in [('terms', []), ('guard_cofactor', []), ('guard_power', 2)]:
        bad = copy.deepcopy(good); bad[field] = value
        reject(lambda bad=bad: R.verify_row(literal, bad, {}, 0, o), 'guard ' + field)


def test_15_wrong_parity_both_sides():
    o = ops()
    literal = {'label': 'J/1/0', 'terms': []}
    R.verify_row(literal, trace('J/1/0', {}), {}, 0, o)
    bad = trace('J/1/0', C.const(1))
    reject(lambda: R.verify_row(literal, bad, {}, 0, o), 'normalized wrong parity')
    literal_bad = {'label': 'J/1/0', 'terms': C.wire({(): Q(1)})}
    reject(lambda: R.verify_row(literal_bad, trace('J/1/0', {}), {}, 0, o), 'original wrong parity')


def test_16_canonical_footer_and_trailing():
    with tempfile.TemporaryDirectory(prefix='gate-', dir=OWN) as directory:
        path = Path(directory) / 'stream.jsonl'
        stream = C.Stream(path, 65536)
        row = trace('J/2/0', C.mono((C.K,)*3, Q(5, 9)))
        stream.emit(row)
        stream.emit({'type': 'footer', 'complete': True, 'prefix_sha256': stream.h.hexdigest()})
        stream.close()
        need(len(list(R.records(path))) == 2, 'valid record stream')
        with path.open('ab') as handle:
            handle.write(C.B.canonical({'type': 'row'}))
        reject(lambda: list(R.records(path)), 'post-footer bytes')


def test_17_exclusive_outputs_and_stale_receipt():
    with tempfile.TemporaryDirectory(prefix='exclusive-', dir=OWN) as directory:
        construction = Path(directory) / 'construction.jsonl'
        stream = C.Stream(construction, 128); stream.close()
        reject(lambda: C.Stream(construction, 128), 'construction overwrite')
        receipt = Path(directory) / 'replay-result.json'
        with receipt.open('xb') as handle:
            handle.write(b'STALE')
        reject(lambda: receipt.open('xb'), 'receipt overwrite')
        need(receipt.read_bytes() == b'STALE', 'stale receipt changed')


def test_18_caps_and_stage_context():
    o = ops(polynomial_terms=1, multiply_pairs=1)
    o.stage(stage='tiny', member='B', degree=7)
    try:
        o.add(C.const(1), C.mono((20,)))
    except ValueError as error:
        data = json.loads(str(error)); need(data['pending_terms'] == 2 and data['degree'] == 7, 'cap context')
    else:
        raise RuntimeError('term cap accepted')
    reject(lambda: o.mul({(): Q(1), (20,): Q(1)}, C.const(1)), 'pair cap')


def test_19_authority_mutations():
    pins = {name: 'a'*64 for name in ('construct.py', 'replay.py', 'baseline.py')}
    authority = {'schema': 'jc2.hybrid-affine-authority/v1', 'root_green': True,
                 'construction_only': True, 'job': 'TOY', 'mode': 'normalized-hermite-only-slice',
                 'boot_id': 'boot', 'code_sha256': pins, 'registration_sha256': 'b'*64,
                 'root_green_sha256': 'c'*64, 'source_path': C.SOURCE_PATH,
                 'source_sha256': C.SOURCE, 'desk_sha256': C.DESK,
                 'normalization_gate_sha256': C.NORMALIZATION, 'hybrid_gate_sha256': 'd'*64,
                 'code_gate_sha256': 'e'*64, 'gates_accepted': True,
                 'caps': dict(C.CAPS), 'expires_unix': 110}
    observed = {'system': 'Linux', 'vendor': 'Amazon EC2', 'instance': C.INSTANCE,
                'cwd': str(C.ROOT), 'boot': 'boot', 'now': 100}
    C.authority_check(authority, observed, pins, 'b'*64, 'c'*64)
    mutations = [('root_green', False), ('registration_sha256', 'f'*64),
                 ('boot_id', 'wrong'), ('code_gate_sha256', ''),
                 ('gates_accepted', False), ('source_path', '/tmp/wrong')]
    for field, value in mutations:
        bad = copy.deepcopy(authority); bad[field] = value
        reject(lambda bad=bad: C.authority_check(bad, observed, pins, 'b'*64, 'c'*64), 'authority ' + field)
    bad_observed = dict(observed, vendor='Other')
    reject(lambda: C.authority_check(authority, bad_observed, pins, 'b'*64, 'c'*64), 'host')
    bad = copy.deepcopy(authority); bad['caps']['wall_seconds'] = 301
    reject(lambda: C.authority_check(bad, observed, pins, 'b'*64, 'c'*64), 'cap increase')


def test_20_static_and_local_fail_closed():
    o = ops()
    reject(lambda: C.layout({}, o), 'local layout')
    reject(lambda: C.build({}, o), 'local build')
    reject(lambda: R.replay_frozen('missing', 'missing', o), 'local replay')
    for name in ('construct.py', 'replay.py'):
        tree = ast.parse((FROZEN / name).read_bytes())
        need(not any(isinstance(node, ast.Assert) for node in ast.walk(tree)), 'Assert node ' + name)
        need(not any(isinstance(node, (ast.Import, ast.ImportFrom)) and
                     any(alias.name == 'subprocess' for alias in node.names)
                     for node in ast.walk(tree)), 'subprocess import ' + name)
    source = (FROZEN / 'construct.py').read_text()
    need(source.index("need(sha(SOURCE_PATH)==SOURCE") > source.index('a,ops=authorize'), 'source before authority')
    need("open('xb')" in source and "(ROOT/'replay-result.json').open('xb')" in source, 'exclusive outputs')


TESTS = [value for name, value in sorted(globals().items()) if name.startswith('test_')]
for test in TESTS:
    test()
print(json.dumps({'status': 'PASS', 'tests': len(TESTS), 'optimized': not __debug__,
                  'frozen': str(FROZEN), 'full_source_rows': 0,
                  'baseline_make_contract_calls': 0}, sort_keys=True))
