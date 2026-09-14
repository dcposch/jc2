#!/usr/bin/env python3
"""Independent tiny parity-construction controls; never runs production paths."""
import argparse
import ast
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import comb, factorial
from pathlib import Path
import sys
import time
from types import SimpleNamespace as NS

LANE = Path('/tmp/jc2-lane.8nFKkf/inputs')
EXPECTED = {
    'FALLACY-v2.md': 'e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5',
    'baseline.py': 'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53',
    'construct.py': '22173cc6a9217a90a8537081a1229b01e58017990b728291285e8cfc01a332a2',
    'd125-b-a-hermite-composition-gate-fable5-20260907.md': '601cbe68958556ca736ade77b5b849d1326835f2328a2b951d2413609ebdbe59',
    'd125-parity-compression-code-prep-astra-20260907.md': '80240044afd0e5c0eef979fe3a80c12a34d1efc5140aa6597059265aafd7090c',
    'd125-symmetry-delta-gate-fable5-20260907.md': '3940ba00aca8033bd8206250dc007881b9b50113061dc85588e06d1ccbe7c47d',
    'exporter.py': '9fd003e420f3ee069f1ed1c06a365e5b4500d361bc3951f2f8f17ef733ab3703',
    'qpoly.py': '7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9',
    'replay.py': '2dbb7464fd7b59e361f34b5a705cc7359b98001bf570a80fc77f441e029c2a17',
    'run_once.py': 'd164af0b576fd7d8f7e3c3a294da8211df996595677aeac75267d2bf9546d40f',
    'run_tests.py': '0051183b0e97f6e9aaf205118cacc0dfe7eef42fab150ba6862f0929241cc610',
    'test_construct.py': '2f5f129eaa3492fcfc59dc07ff5cbf11963ad772d4816e525f16de3e47b792ee',
    'test_once.py': '35f3cc5b400139ba150c2365a57ba3e3513cb5ece51017c46c541bc26c00419f',
}


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name):
    path = LANE/(name+'.py')
    spec = importlib.util.spec_from_file_location(name, path)
    need(spec is not None and spec.loader is not None, 'explicit frozen import failed')
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    need(Path(module.__file__).resolve() == path.resolve(), 'relocated import drift')
    return module


def rank(matrix):
    a = [[F(x) for x in row] for row in matrix]
    if not a:
        return 0
    row = 0
    for column in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        q = a[row][column]
        a[row] = [x/q for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][column]:
                q = a[i][column]
                a[i] = [x-q*y for x, y in zip(a[i], a[row])]
        row += 1
    return row


def direct_b_matrix(d, columns):
    h3 = {0: 1, 3: 3, 6: 3, 9: 1}
    rows = []
    for output_g in range(d+14):
        row = []
        for b_g in columns:
            value = 0
            for a_g, coefficient in h3.items():
                if a_g+b_g-1 == output_g:
                    value += coefficient*(a_g*(d-b_g)-(15-a_g)*b_g)
            row.append(value)
        rows.append(row)
    return rows


def direct_lift_entry(point, t, exponent):
    i, j = point
    total = F(0)
    for u_count in range(j+1):
        for lambda_count in range(j-u_count+1):
            inverse_count = j-u_count-lambda_count
            v_exp = -i+4*u_count+lambda_count-inverse_count
            if u_count == t and v_exp == exponent and lambda_count == 0:
                ways = factorial(j)//(factorial(u_count)*factorial(lambda_count)*factorial(inverse_count))
                total += F(ways*(-1)**(lambda_count+inverse_count))
    return total


def main(output):
    started = time.monotonic()
    before = {name: sha(LANE/name) for name in EXPECTED}
    need(before == EXPECTED, 'frozen input pin mismatch')
    baseline = load('baseline')
    load('qpoly')
    construct = load('construct')
    load('replay')
    run_once = load('run_once')
    need(Path(construct.B.__file__).resolve() == (LANE/'baseline.py').resolve(), 'construct baseline import drift')
    need(Path(construct.Q.__file__).resolve() == (LANE/'qpoly.py').resolve(), 'construct qpoly import drift')

    contract = baseline.make_contract('unequal', 'rational')
    maps = contract['coefficient_maps']
    free = [[e for e in entries if 'variable' in e and sum(e['point']) % 2] for entries in maps]
    pivots = {(i, s-i) for s in range(1, 15, 2) for i in range((s+4)//5)}
    retained = [e for e in free[0] if tuple(e['point']) not in pivots]
    need([len(x) for x in maps] == [83, 215], 'literal slot census')
    need([sum('fixed' in e for e in x) for x in maps] == [12, 19], 'fixed face census')
    need([len(x) for x in free] == [33, 94] and len(pivots) == 13 and len(retained) == 20,
         'parity coordinate census')
    names = [e['name'] for e in retained]+['beta5_slice', 'lambda3']
    need(len(contract['variables'])+2 == 269 and len(names) == 22, 'map/coordinate order census')

    hermite_entries = 0
    for s in range(1, 15, 2):
        r = (s+4)//5
        got = construct.hermite_matrix(s)
        expected = [[direct_lift_entry((i, s-i), t, 5*t-s) for i in range(r)] for t in range(r)]
        need(got == expected and rank(got) == r, 'A Hermite sign/orientation')
        bad = [row[:] for row in got]
        bad[0][0] *= -1
        need(bad != expected, 'A sign mutation survived')
        hermite_entries += r*r

    op = construct.Arithmetic(dict(construct.CEILINGS), time.monotonic()+10)
    a = {(0, 1): {}, (1, 0): {(0,): F(1)}, (0, 3): construct.const(1)}
    forcing = construct.liftrow(a, 0, -1, 1, op)
    value, unused_inverse = construct.solve_constants(construct.hermite_matrix(1), [forcing], op)
    a[0, 1] = value[0]
    need(construct.liftrow(a, 0, -1, 1, op) == {}, 'descending A solve missed forcing')
    mutated = dict(a)
    mutated[0, 3] = {}
    need(construct.liftrow(mutated, 0, -1, 1, op) != {}, 'higher-term omission mutation survived')

    b_pivots = 0
    selected_labels = []
    for d in range(1, 24, 2):
        points = sorted((tuple(e['point']) for e in free[1] if sum(e['point']) == d), reverse=True)
        columns = [i for i, unused_j in points]
        matrix = construct.b_matrix(d, columns)
        need(matrix == direct_b_matrix(d, columns), 'B bracket matrix orientation')
        expected_rank = len(columns)-(1 if d in (5, 15) else 0)
        need(rank(matrix) == expected_rank, 'B rank/kernel census')
        if d in (5, 15):
            need(points[-1] == (0, d), 'kernel coordinate is not g0')
            points.remove((0, d))
            columns = [i for i, unused_j in points]
            matrix = construct.b_matrix(d, columns)
        chosen = construct.independent_rows(matrix)
        need(rank([matrix[r] for r in chosen]) == len(columns), 'selected original B rows singular')
        selected_labels += [f'J/{r}/{d+13-r}' for r in chosen]
        b_pivots += len(columns)
    need(b_pivots == 92 and len(set(selected_labels)) == 92, 'B pivot/row count')
    altered = construct.b_matrix(5, [0, 1, 2, 3])
    altered[2][0] += 1
    need(altered != direct_b_matrix(5, [0, 1, 2, 3]), 'B matrix mutation survived')

    a_points = {tuple(e['point']): e for e in maps[0]}
    for entry in maps[1]:
        if 'fixed' not in entry:
            continue
        ae = a_points.get(tuple(entry['point']))
        need(ae is None or ('fixed' in ae and baseline.decode(ae['fixed']) == baseline.ZERO),
             'whole shear would change a B fixed face')
    toy_a = {(0, 3): construct.const(1), (0, 1): construct.const(2)}
    toy_b = {(0, 5): {(0,): F(1)}, (0, 3): {}, (0, 1): construct.const(7)}
    sheared = construct.shear(toy_a, toy_b, {(1,): F(1)}, op)
    need(sheared[0, 3] == {(1,): F(1)} and sheared[0, 1] == {(): F(7), (1,): F(2)},
         'whole lower-coefficient shear')
    broken = dict(sheared)
    broken[0, 1] = toy_b[0, 1]
    need(construct.shear(toy_a, broken, {(1,): F(-1)}, op) != toy_b,
         'partial-shear mutation survived')

    fixed_labels = ['FIX/'+e['name'] for entries in maps for e in entries if 'fixed' in e]
    jac_labels = [f'J/{i}/{j}' for i in range(24) for j in range(39-i)]
    lift_a = [f'LIFT/A/{t}/{e}' for t in range(3) for e in range(5*t-15, 0)]
    lift_b = [f'LIFT/B/{t}/{e}' for t in range(5) for e in range(5*t-25, 0)]
    guards = [g['label'] for g in contract['vertex_guards']]+['GUARD/c']
    labels = fixed_labels+jac_labels+lift_a+lift_b+guards
    need([len(fixed_labels), len(jac_labels), len(lift_a), len(lift_b), len(guards)] == [31, 660, 30, 75, 7],
         'original row-class census')
    need(len(labels) == len(set(labels)) == 803, 'original label/index/order census')
    need(construct.jrow({}, {}, 2, 0, op) == construct.const(F(5, 9)), 'target sign')
    need(construct.jrow({}, {}, 1, 0, op) == {}, 'target-position mutation')

    caller_controls = 0
    def caller_fixture(fail=False, rows=803, status='ALL_ORIGINAL_ROWS_TRANSPORTED', expires=None):
        events = []
        def build():
            events.append('construct')
            if fail:
                raise RuntimeError('injected construction failure')
        def replay(*unused):
            events.append('replay')
            return {'status': status, 'rows': rows}
        arithmetic = lambda *unused: NS(stats={})
        authority = {'mode': 'slice', 'expires_unix': expires or time.time()+5, 'caps': {}}
        return NS(main=build, Arithmetic=arithmetic), NS(replay_frozen=replay), authority, events
    fake_c, fake_r, authority, events = caller_fixture()
    result = run_once.pipeline(fake_c, fake_r, authority, Path('unused'))
    need(events == ['construct', 'replay'] and result['rows'] == 803, 'caller success order')
    caller_controls += 1
    for kind in ('failure', 'expired', 'rows', 'status', 'mode'):
        fake_c, fake_r, authority, events = caller_fixture(
            fail=kind == 'failure', rows=802 if kind == 'rows' else 803,
            status='MUTATED' if kind == 'status' else 'ALL_ORIGINAL_ROWS_TRANSPORTED',
            expires=time.time()-1 if kind == 'expired' else None)
        if kind == 'mode':
            authority['mode'] = 'full'
        rejected = False
        try:
            run_once.pipeline(fake_c, fake_r, authority, Path('unused'))
        except (RuntimeError, ValueError):
            rejected = True
        need(rejected, 'caller mutation survived: '+kind)
        need(events.count('construct') <= 1 and events.count('replay') <= 1, 'caller retried')
        if kind in ('failure', 'expired'):
            need('replay' not in events, 'replay followed failed/expired construction')
        if kind == 'mode':
            need(not events, 'wrong mode performed work')
        caller_controls += 1

    source = (LANE/'construct.py').read_bytes()
    caller = (LANE/'run_once.py').read_bytes()
    need(b"points.remove((0, d))" in source and b"if mode == 'full':\n        b = shear(a, b" in source,
         'literal kernel/shear implementation drift')
    caller_tree = ast.parse(caller)
    forbidden_caller_names = {'subprocess', 'fork', 'setsid'}
    need(b"C.authorize(authority_path)" in caller and b"digest(WORK/'REGISTRATION.md')" in caller and
         b"digest(SOURCE)==C.SOURCE" in caller and
         not any(isinstance(n, ast.Name) and n.id in forbidden_caller_names for n in ast.walk(caller_tree)),
         'caller binding/sequencing drift')
    nodes = 0
    for name in ('construct.py', 'replay.py', 'run_once.py', 'test_construct.py', 'test_once.py'):
        nodes += sum(isinstance(n, ast.Assert) for n in ast.walk(ast.parse((LANE/name).read_bytes())))
    need(nodes == 0, 'Assert gate found')
    after = {name: sha(LANE/name) for name in EXPECTED}
    need(after == before, 'frozen input changed during control')
    receipt = {
        'status': 'PASS_TINY_INDEPENDENT_NO_PRODUCTION',
        'mode': 'optimized' if not __debug__ else 'normal',
        'pins': after,
        'counts': {'original_maps': 269, 'original_rows': 803, 'fixed': 31,
                   'jacobian': 660, 'lift_a': 30, 'lift_b': 75, 'guards': 7,
                   'a_pivots': 13, 'b_pivots': b_pivots, 'coordinates_slice': 22,
                   'hermite_entries_checked': hermite_entries, 'caller_controls': caller_controls,
                   'assert_nodes': nodes},
        'mutations_rejected': ['A_sign', 'A_higher_term_omission', 'B_matrix',
                               'partial_shear', 'target_position', 'caller_failure',
                               'caller_expiry', 'caller_incomplete', 'caller_status',
                               'caller_mode'],
        'exact_rational_examples': {'target': '5/9', 'slice_scalar': '-5/9'},
        'elapsed_seconds': format(time.monotonic()-started, '.6f'),
        'scope': 'metadata census and tiny exact controls only; no production constructor/replay/source stream',
    }
    with Path(output).open('x', encoding='utf-8') as stream:
        json.dump(receipt, stream, sort_keys=True, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps(receipt, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('output')
    args = parser.parse_args()
    main(args.output)
