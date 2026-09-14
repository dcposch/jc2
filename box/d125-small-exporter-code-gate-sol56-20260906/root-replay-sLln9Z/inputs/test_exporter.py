#!/usr/bin/env python3
"""Bounded tiny controls ONLY. No degree15/25 J or lift polynomial generated."""
import argparse
import copy
from datetime import datetime, timezone, timedelta
import hashlib
import io
import json
from pathlib import Path
import resource
import signal
import tempfile
import time
import exporter as E
B = E.B

resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
signal.alarm(30)
started = time.monotonic()
checks = []


def require(ok, label):
    if not ok:
        raise ValueError(label)
    checks.append(label)


def rejects(fn, label):
    try:
        fn()
    except (ValueError, RuntimeError, OSError, ZeroDivisionError):
        checks.append(label)
        return
    raise ValueError('mutation accepted: '+label)


def cmul(a, b):
    out = {}
    for am, av in a.items():
        for bm, bv in b.items():
            E.add_term(out, tuple(sorted(am+bm)), av*bv)
    return out


def lmul(a, b):
    out = {}
    for (u, v), av in a.items():
        for (w, z), bv in b.items():
            row = out.setdefault((u+w, v+z), {})
            for m, c in cmul(av, bv).items():
                E.add_term(row, m, c)
    return {p: c for p, c in out.items() if c}


def compose(source, lambda2, lambda3):
    """Independent repeated multiplication of the actual Laurent inverse."""
    pi = {(1, 4): {(): B.ONE}, (0, 2): {(lambda2,): -B.ONE},
          (0, 1): {(lambda3,): -B.ONE}, (0, -1): {(): -B.ONE}}
    out = {}
    for (i, j), coefficient in source.items():
        power = {(0, -i): coefficient}
        for _ in range(j):
            power = lmul(power, pi)
        for point, row in power.items():
            target = out.setdefault(point, {})
            for m, c in row.items():
                E.add_term(target, m, c)
    return {p: c for p, c in out.items() if c}


def pair_jac(left, right):
    out = {}
    for (i, j), a in left.items():
        for (k, l), b in right.items():
            det = i*l-j*k
            if not det:
                continue
            target = out.setdefault((i+k-1, j+l-1), {})
            for m, c in cmul(a, b).items():
                E.add_term(target, m, det*c)
    return {p: row for p, row in out.items() if row}


def toy():
    def entry(who, point, fixed=None, variable=None):
        result = {'point': list(point), 'name': f'{who}_g{point[0]}_p{point[1]}'}
        if fixed is not None:
            result.update(fixed=fixed.wire(), reasons=['TOY_FIXED'])
        else:
            result['variable'] = variable
        return result
    maps = [[entry('A', (0, 0), B.ZERO), entry('A', (0, 2), B.RHO),
             entry('A', (0, 6), variable=0), entry('A', (1, 0), B.ONE)],
            [entry('B', (0, 0), B.ZERO), entry('B', (0, 1), variable=1),
             entry('B', (2, 1), B.ONE), entry('B', (3, 0), B.ONE)]]
    return {'header': {'schema': E.SCHEMA, 'mode': 'toy', 'case': 'DECLARED_TOY_NOT_D125',
                       'branch': 'golden', 'field': 'Q[rho]/(rho^2-3*rho+1)',
                       'expected_rows': 71, 'expected_jacobian_rows': 49,
                       'expected_lift_rows': 14, 'expected_variables': 6,
                       'target': 'J-c*gamma^2', 'status': 'TOY_ONLY'},
            'variables': ['a', 'b', 'c', 'z', 'lambda2', 'lambda3'], 'maps': maps,
            'sources': [E.source_map(m) for m in maps], 'degrees': (6, 6),
            'jac_indices': [(i, j) for i in range(7) for j in range(7)],
            'lambda_ids': (4, 5), 'scalar': {(2,): B.ONE},
            'scalar_guard': {(2, 3): B.ONE, (): -B.ONE},
            'guards': [{'label': 'GUARD/A/0/2', 'value': B.RHO.wire(),
                        'inverse': B.RHO.inverse().wire()}]}


def resync(records):
    """Adversarially repair footer checksum/counts after data corruption."""
    rows = [r for r in records[:-1] if r['type'] == 'row']
    counts = {}
    for row in rows:
        counts['rows'] = counts.get('rows', 0)+1
        counts[row['kind']] = counts.get(row['kind'], 0)+1
        counts['terms'] = counts.get('terms', 0)+len(row['terms'])
        counts['zero_rows'] = counts.get('zero_rows', 0)+(not row['terms'])
    prefix = b''.join(B.canonical(r) for r in records[:-1])
    records[-1] = {**records[-1], 'prefix_sha256': hashlib.sha256(prefix).hexdigest(),
                   'prefix_records': len(records)-1, 'counts': counts}
    return b''.join(B.canonical(r) for r in records)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--mutation', choices=('missing_low', 'field_split', 'target',
                                              'fixed_zero', 'guard', 'resynced'))
    args = parser.parse_args()
    spec = toy()
    rows = list(E.records(spec))
    data = b''.join(map(B.canonical, rows))
    require(rows[-1]['counts']['rows'] == 71 and rows[-1]['counts']['polynomiality'] == 14,
            'complete tiny row and footer counts')
    require(len(E.negative_indices(15)) == 30 and len(E.negative_indices(25)) == 75,
            '105 a priori index slots only, no actual receiver lift')
    for who, source in zip(('A', 'B'), spec['sources']):
        actual = compose(source, *spec['lambda_ids'])
        for t, e in E.negative_indices(6):
            require(E.lift_row(source, t, e, *spec['lambda_ids']) == actual.get((t, e), {}),
                    f'independent inverse-power coefficient {who}/{t}/{e}')
        require(all((t, e) in E.negative_indices(6) for t, e in actual if e < 0),
                who+' complete tiny negative envelope')
    naive = pair_jac(*spec['sources'])
    require(all(E.jac_row(*spec['sources'], *p) == naive.get(p, {}) for p in spec['jac_indices']),
            'forced Jacobian index versus independent tiny pair expansion')
    # Exact positive polynomiality control, with both symbolic lambdas present.
    forward_u = {(4, 1): {(): B.ONE}, (2, 0): {(4,): B.ONE},
                 (3, 0): {(5,): B.ONE}, (5, 0): {(): B.ONE}}
    require(compose(forward_u, 4, 5) == {(1, 0): {(): B.ONE}},
            'positive actual inverse composition reconstructs u')
    require(all(not E.lift_row(forward_u, t, e, 4, 5) for t, e in E.negative_indices(5)),
            'positive fixture negative rows vanish with free lambdas')
    # Real omission example from the actual inverse map, at zero lambdas.
    badA = {(1, 0): {(): B.ONE}}
    badB = {(2, 1): {(): B.ONE}, (3, 0): {(): B.ONE}}
    negative = []
    for who, source in [('A', badA), ('B', badB)]:
        for (u, v), row in compose(source, 4, 5).items():
            if v < 0 and row.get((), B.ZERO) != B.ZERO:
                negative.append((who, u, v, row[()]))
    require(negative == [('A', 0, -1, B.ONE)], 'actual zero-lambda omission is exactly A/u0/v-1')
    require(pair_jac(badA, badB) == {(2, 0): {(): B.ONE}}, 'omission fixture has genuine monomial J')
    # Metadata-only complete-client counts, without invoking production_spec/rows.
    counts = {}
    for case in B.VERTICES:
        for branch in ('rational', 'golden'):
            c = B.make_contract(case, branch)
            counts[case+'/'+branch] = [len(c['variables'])+2, c['counts']['planned_all_rows']+105]
    require(set(map(tuple, counts.values())) == {(269, 803), (295, 816), (371, 816)},
            'six complete-client presentation counts only')
    require(B.RHO*(3-B.RHO) == B.ONE, 'golden inverse without choosing embedding')
    text = E.singular_polynomial([[B.F(1, 2).wire(), [0, 0, 1]]], ['a', 'b'], True)
    require(text == '((1+(2)*rho))*a^2*b', 'single quadratic-field coefficient in Singular term')
    rejects(lambda: E.singular_polynomial([[B.RHO.wire(), []]], [], False),
            'golden coefficient cannot silently enter rational ring')
    # Pure authority checker: no actual or fake host launch.
    now = datetime.now(timezone.utc)
    observed = {'system': 'Linux', 'vendor': 'Amazon EC2', 'instance': 'i-0123456789abcdef0',
                'cwd': '/home/ubuntu/DECLARED_TEST_ONLY', 'now': now.timestamp()}
    auth = {'schema': 'jc2.d125-small-source-authority/v1', 'root_green': True,
            'construction_only': True, 'job_id': 'DECLARED_FAKE_TEST_NOT_AUTHORITY',
            'registration_sha256': '1'*64, 'case': 'unequal', 'branch': 'golden',
            'instance_id': observed['instance'], 'working_directory': observed['cwd'],
            'deadline_utc': (now+timedelta(seconds=20)).isoformat(),
            'caps': {'wall_seconds': 30, 'cpu_seconds': 25, 'as_bytes': 512*1024**2,
                     'aggregate_output_bytes': 1024**2},
            'pins': {'exporter_sha256': '2'*64, 'baseline_sha256': E.BASELINE_SHA,
                     'normalization_gate_sha256': E.NORMALIZATION_SHA, 'lift_contract_sha256': E.LIFT_SHA,
                     'lift_gate_sha256': E.LIFT_GATE_SHA}}
    E.authority_check(auth, 'unequal', 'golden', observed, '2'*64)
    require(True, 'pure authority schema positive fixture only')
    for key, value in [('root_green', False), ('construction_only', False), ('job_id', ''),
                       ('registration_sha256', ''), ('instance_id', 'i-fffffffffffffffff'),
                       ('working_directory', '/home/ubuntu'), ('caps', {})]:
        changed = copy.deepcopy(auth)
        changed[key] = value
        rejects(lambda: E.authority_check(changed, 'unequal', 'golden', observed, '2'*64),
                'fail-closed authority '+key)
    for key, value in [('system', 'Darwin'), ('vendor', 'not Amazon'), ('instance', 'host')]:
        changed = dict(observed, **{key: value})
        rejects(lambda: E.authority_check(auth, 'unequal', 'golden', changed, '2'*64),
                'fail-closed observed '+key)
    rejects(lambda: E.production_spec(None), 'production specification blocked without context')
    rejects(lambda: E.jac_row({(i, 0): {} for i in range(5)},
                             {(i, 0): {} for i in range(5)}, 0, 0), 'full J blocked without context')
    rejects(lambda: E.lift_row({(0, 15): {(): B.ONE}}, 0, -1, 0, 1),
            'actual-degree lift blocked without context')
    buffer = io.BytesIO()
    budget = E.OutputBudget(3)
    budget.write(buffer, b'ab')
    rejects(lambda: budget.write(buffer, b'cd'), 'aggregate output cap before write')
    require(buffer.getvalue() == b'ab', 'output cap leaves prior bytes unchanged')
    # Store only tiny test streams in a new temporary subdirectory of this box.
    work = Path(tempfile.mkdtemp(prefix='toy-', dir=Path(__file__).resolve().parent))
    original = work/'original.jsonl'
    original.write_bytes(data)
    E.verify_stream(original, spec)
    require(True, 'strict complete toy replay')
    mutations = {}
    for name in ('missing_low', 'field_split', 'target', 'fixed_zero', 'guard', 'resynced'):
        changed = copy.deepcopy(rows)
        if name == 'missing_low':
            changed = [r for r in changed if r.get('label') != 'LIFT/A/0/-1']
        elif name == 'field_split':
            idx = next(i for i, r in enumerate(changed) if r['type'] == 'row' and
                       any(B.decode(c).b != 0 for c, _ in r['terms']))
            old = changed[idx]
            parts = []
            for component in ('a', 'b'):
                terms = [[B.F(getattr(B.decode(c), component)).wire(), m]
                         for c, m in old['terms'] if getattr(B.decode(c), component)]
                parts.append({**old, 'label': old['label']+'/'+component, 'terms': terms})
            changed[idx:idx+1] = parts
        elif name == 'target':
            r = next(r for r in changed if r.get('label') == 'J/2/0')
            next(term for term in r['terms'] if term[1] == [2])[0] = B.ONE.wire()
        elif name == 'fixed_zero':
            r = next(r for r in changed if r['type'] == 'coefficient' and
                     r.get('fixed') == B.ZERO.wire())
            r['fixed'] = B.ONE.wire()
        elif name == 'guard':
            r = next(r for r in changed if r.get('label') == 'GUARD/c')
            r['terms'] = [term for term in r['terms'] if term[1]]
        else:
            r = next(r for r in changed if r['type'] == 'row' and r['terms'])
            r['terms'][0][0] = (B.decode(r['terms'][0][0])+B.ONE).wire()
        path = work/(name+'.jsonl')
        path.write_bytes(resync(changed))
        mutations[name] = path
        rejects(lambda: E.verify_stream(path, spec), 'actual footer-resynced mutation '+name)
    missing_footer = work/'missing-footer.jsonl'
    missing_footer.write_bytes(b''.join(B.canonical(r) for r in rows[:-1]))
    rejects(lambda: E.verify_stream(missing_footer, spec), 'missing terminal footer')
    # Exclusive output behavior is exercised with an actual existing file.
    def overwrite_attempt():
        with original.open('xb'):
            pass
    rejects(overwrite_attempt, 'exclusive output collision retains existing stream')
    require(original.read_bytes() == data, 'existing stream unchanged after collision')
    if args.mutation:
        E.verify_stream(mutations[args.mutation], spec)
    result = {'status': 'PASS', 'check_count': len(checks), 'checks': checks,
              'counts_metadata_only': counts, 'toy_directory': str(work),
              'toy_sha256': E.sha(original), 'elapsed_seconds': time.monotonic()-started,
              'maxrss_KiB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              'production_rows_generated': 0, 'aws_or_cas': False,
              'limits': {'wall_seconds': 30, 'cpu_seconds': 25, 'AS_bytes': 512*1024**2}}
    with Path(args.output).open('x') as out:
        json.dump(result, out, sort_keys=True, indent=2)
        out.write('\n')
    print(json.dumps({'status': 'PASS', 'checks': len(checks), 'seconds': result['elapsed_seconds'],
                      'maxrss_KiB': result['maxrss_KiB'], 'toy_directory': str(work)}))


if __name__ == '__main__':
    main()
