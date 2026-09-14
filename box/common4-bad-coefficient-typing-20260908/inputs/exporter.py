#!/usr/bin/env python3
"""Complete six-client receiver+lift exporter; production is host/authority gated.

No solver execution. Lift theorem gated; implementation still requires its own gate.
JSONL is authoritative; optional Singular text is IMPORT ONLY.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from math import factorial
import os
from pathlib import Path
import platform
import re
import resource
import signal
import time
import baseline as B

BASELINE_SHA = 'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53'
NORMALIZATION_SHA = 'cd69c23885de119e4bd910992dad5ef695e7b12013168ec1c401546d8aa6ed8d'
LIFT_SHA = '433cc2fe9f11ce1b2e1f1fc57aab24def921afb1f93154a2d631ddee0b88cdad'
LIFT_GATE_SHA = '4295593a57a65e4d31630aecdef0b54e9d6078935e07cfb5e64acfd83fae4122'
SCHEMA = 'jc2.d125-small-source-literal/v1'
FAC = [factorial(n) for n in range(26)]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            digest.update(block)
    return digest.hexdigest()


def strict_json(data):
    def unique(pairs):
        out = {}
        for k, v in pairs:
            require(k not in out, 'duplicate JSON key')
            out[k] = v
        return out
    return json.loads(data, object_pairs_hook=unique)


def authority_check(authority, case, branch, observed, builder_sha):
    """Pure checker permits tiny changed-host tests without touching a worker."""
    require(authority.get('schema') == 'jc2.d125-small-source-authority/v1', 'authority schema')
    require(authority.get('root_green') is True and authority.get('construction_only') is True,
            'explicit construction-only root GREEN required')
    require(isinstance(authority.get('job_id'), str) and authority['job_id'].strip(), 'registered job absent')
    require(re.fullmatch(r'[0-9a-f]{64}', authority.get('registration_sha256', '')) is not None,
            'registration pin absent')
    require(authority.get('case') == case and authority.get('branch') == branch, 'wrong client authority')
    require(observed['system'] == 'Linux' and observed['vendor'] == 'Amazon EC2', 'not Linux EC2')
    require(re.fullmatch(r'i-(?:[0-9a-f]{8}|[0-9a-f]{17})', observed['instance']) is not None,
            'DMI instance id invalid')
    require(authority.get('instance_id') == observed['instance'], 'DMI instance mismatch')
    require(authority.get('working_directory') == observed['cwd'] and
            observed['cwd'].startswith('/home/ubuntu/') and
            observed['cwd'] != '/home/ubuntu/', 'registered exact cwd required')
    expected = {'exporter_sha256': builder_sha, 'baseline_sha256': BASELINE_SHA,
                'normalization_gate_sha256': NORMALIZATION_SHA, 'lift_contract_sha256': LIFT_SHA,
                'lift_gate_sha256': LIFT_GATE_SHA}
    require(authority.get('pins') == expected, 'authority source pins mismatch')
    caps = authority.get('caps', {})
    for key, ceiling in [('wall_seconds', 600), ('cpu_seconds', 600),
                         ('as_bytes', 8*1024**3), ('aggregate_output_bytes', 1024**3)]:
        value = caps.get(key)
        require(type(value) is int and 0 < value <= ceiling, 'missing/out-of-range cap '+key)
    deadline = datetime.fromisoformat(authority.get('deadline_utc', '').replace('Z', '+00:00'))
    require(deadline.tzinfo is not None, 'UTC deadline required')
    remaining = deadline.timestamp()-observed['now']
    require(0 < remaining <= caps['wall_seconds'], 'expired/unbounded job deadline')
    return caps, remaining


class ProductionContext:
    def __init__(self, authority_bytes, case, branch):
        self.authority = strict_json(authority_bytes)
        self.authority_sha = hashlib.sha256(authority_bytes).hexdigest()
        observed = {'system': platform.system(),
                    'vendor': Path('/sys/class/dmi/id/sys_vendor').read_text().strip(),
                    'instance': Path('/sys/class/dmi/id/board_asset_tag').read_text().strip(),
                    'cwd': str(Path.cwd().resolve()), 'now': time.time()}
        require(sha(Path(__file__).with_name('baseline.py')) == BASELINE_SHA, 'baseline drift')
        self.builder_sha = sha(__file__)
        self.caps, remaining = authority_check(self.authority, case, branch, observed, self.builder_sha)
        self.observed = observed
        self.case, self.branch = case, branch
        self.pid, self.pgid = os.getpid(), os.getpgid(0)
        self.start_ticks = Path('/proc/self/stat').read_text().split(') ', 1)[1].split()[19]
        self.boot_id = Path('/proc/sys/kernel/random/boot_id').read_text().strip()
        self.deadline = time.monotonic()+remaining
        resource.setrlimit(resource.RLIMIT_AS, (self.caps['as_bytes'], self.caps['as_bytes']))
        resource.setrlimit(resource.RLIMIT_CPU, (self.caps['cpu_seconds'], self.caps['cpu_seconds']))
        signal.setitimer(signal.ITIMER_REAL, remaining)

    def check(self):
        require(os.getpid() == self.pid and os.getpgid(0) == self.pgid, 'child identity changed')
        require(str(Path.cwd().resolve()) == self.observed['cwd'], 'cwd drift')
        require(time.monotonic() < self.deadline, 'construction/replay deadline reached')


def add_term(out, monomial, value):
    if value != B.ZERO:
        out[monomial] = out.get(monomial, B.ZERO)+value
        if out[monomial] == B.ZERO:
            del out[monomial]


def source_map(entries):
    return {tuple(e['point']): ({(): B.decode(e['fixed'])} if 'fixed' in e
                               else {(e['variable'],): B.ONE}) for e in entries}


def jac_row(left, right, I, J, context=None):
    if context is None:
        require(len(left)*len(right) <= 16, 'full J requires host-bound authority')
    else:
        require(isinstance(context, ProductionContext), 'invalid production context')
        context.check()
    out = {}
    for (i, j), a in sorted(left.items()):
        k, l = I+1-i, J+1-j
        b = right.get((k, l))
        determinant = i*l-j*k
        if b is None or k < 0 or l < 0 or not determinant:
            continue
        for am, av in a.items():
            for bm, bv in b.items():
                add_term(out, tuple(sorted(am+bm)), determinant*av*bv)
    return out


def lift_row(source, t, e, lambda2, lambda3, context=None):
    """[u^t v^e] A(v^-1,v^4u-l2*v^2-l3*v-v^-1), exact forced d."""
    require(t >= 0 and e < 0, 'negative polynomiality index required')
    if context is None:
        require(len(source) <= 4 and all(i+j <= 7 for i, j in source),
                'full lift requires host-bound authority')
    else:
        require(isinstance(context, ProductionContext), 'invalid production context')
        context.check()
    out = {}
    for (i, j), coefficient in sorted(source.items()):
        require(i >= 0 and 0 <= j <= 25, 'ordinary supported source required')
        if j < t:
            continue
        for b in range(j-t+1):
            twice_d = e+i+j-5*t-3*b
            if twice_d < 0 or twice_d % 2:
                continue
            d = twice_d//2
            z = j-t-b-d
            if z < 0:
                continue
            multiplier = FAC[j]//(FAC[t]*FAC[b]*FAC[d]*FAC[z]) * (-1)**(j-t)
            lambdas = (lambda2,)*b+(lambda3,)*d
            for monomial, value in coefficient.items():
                add_term(out, tuple(sorted(monomial+lambdas)), multiplier*value)
    return out


def negative_indices(degree):
    return [(t, e) for t in range((degree-1)//5+1) for e in range(5*t-degree, 0)]


def row_record(label, polynomial, kind):
    return {'type': 'row', 'kind': kind, 'label': label,
            'terms': [[c.wire(), list(m)] for m, c in sorted(polynomial.items()) if c != B.ZERO]}


def payload(spec, context=None):
    """Shared literal record formula; access only through guarded records()."""
    yield {'type': 'header', **spec['header']}
    for index, name in enumerate(spec['variables']):
        yield {'type': 'variable', 'id': index, 'name': name}
    for who, entries in zip(('A', 'B'), spec['maps']):
        for entry in entries:
            yield {'type': 'coefficient', 'member': who, **entry}
    for who, entries in zip(('A', 'B'), spec['maps']):
        for entry in entries:
            if 'fixed' in entry:
                yield row_record('FIX/'+entry['name'], {}, 'fixed_assignment')
    for I, J in spec['jac_indices']:
        out = jac_row(*spec['sources'], I, J, context)
        if (I, J) == (2, 0):
            for m, c in spec['scalar'].items():
                add_term(out, m, -c)
        yield row_record(f'J/{I}/{J}', out, 'jacobian')
    for who, source, degree in zip(('A', 'B'), spec['sources'], spec['degrees']):
        for t, e in negative_indices(degree):
            yield row_record(f'LIFT/{who}/{t}/{e}',
                             lift_row(source, t, e, *spec['lambda_ids'], context), 'polynomiality')
    for guard in spec['guards']:
        value, inverse = B.decode(guard['value']), B.decode(guard['inverse'])
        require(value != B.ZERO and value*inverse == B.ONE, 'bad fixed vertex guard')
        yield {**row_record(guard['label'], {}, 'fixed_unit_guard'),
               'value': guard['value'], 'inverse': guard['inverse']}
    yield row_record('GUARD/c', spec['scalar_guard'], 'scalar_guard')


def production_spec(context):
    require(isinstance(context, ProductionContext), 'host-bound construction context absent')
    context.check()
    contract = B.make_contract(context.case, context.branch)
    B.validate_contract(contract)
    variables = contract['variables']+['lambda2', 'lambda3']
    n = len(contract['variables'])
    s = contract['scalar']
    if 'fixed' in s:
        scalar = {(): B.decode(s['fixed'])}
        require(next(iter(scalar.values()))*B.decode(s['inverse']) == B.ONE, 'bad fixed scalar guard')
        scalar_guard = {}
    else:
        scalar = {(s['variable'],): B.ONE}
        scalar_guard = {tuple(sorted((s['variable'], s['inverse_variable']))): B.ONE, (): -B.ONE}
    return {'header': {'schema': SCHEMA, 'status': 'GATED_SUFFICIENT_CLIENT_NO_POINT_OR_CE_CLAIM',
                       'implementation_gate': 'PENDING_AT_SOURCE_SEAL',
                       'mode': 'production', 'case': context.case, 'branch': context.branch,
                       'field': contract['field'], 'index_base': 0, 'order': contract['order'],
                       'target': contract['target'], 'authority_sha256': context.authority_sha,
                       'jacobian_scalar': contract['scalar'],
                       'pins': context.authority['pins'],
                       'expected_rows': contract['counts']['planned_all_rows']+105,
                       'expected_jacobian_rows': 660, 'expected_lift_rows': 105,
                       'expected_variables': len(variables),
                       'lambda_guard': 'NONE: lambda2 and lambda3 are unrestricted',
                       'lift': 'g=v^-1,p=v^4*u-lambda2*v^2-lambda3*v-v^-1'},
            'variables': variables, 'maps': contract['coefficient_maps'],
            'sources': [source_map(m) for m in contract['coefficient_maps']],
            'degrees': (15, 25), 'jac_indices': [(I, J) for I in range(24) for J in range(39-I)],
            'lambda_ids': (n, n+1), 'scalar': scalar, 'scalar_guard': scalar_guard,
            'guards': contract['vertex_guards']}


def records(spec, context=None):
    if spec['header']['mode'] == 'production':
        require(isinstance(context, ProductionContext), 'production authority absent')
        context.check()
        require(spec == production_spec(context), 'production contract mutation')
    else:
        require(spec['header']['mode'] == 'toy' and max(spec['degrees']) <= 7 and
                len(spec['sources'][0])*len(spec['sources'][1]) <= 16 and
                len(spec['jac_indices']) <= 64, 'not a declared tiny toy')
    require((2, 0) in spec['jac_indices'] and len(set(spec['jac_indices'])) == len(spec['jac_indices']),
            'target obligation/row-index duplication')
    digest = hashlib.sha256()
    counts = Counter()
    used = set()
    nrecords = 0
    for record in payload(spec, context):
        if context:
            context.check()
        if record['type'] == 'row':
            counts['rows'] += 1
            counts[record['kind']] += 1
            counts['terms'] += len(record['terms'])
            counts['zero_rows'] += not record['terms']
            for coefficient, monomial in record['terms']:
                require(B.decode(coefficient) != B.ZERO, 'explicit zero term')
                require(monomial == sorted(monomial) and all(type(i) is int and
                        0 <= i < len(spec['variables']) for i in monomial), 'invalid variable id')
                used.update(monomial)
        digest.update(B.canonical(record))
        nrecords += 1
        yield record
    require(counts['rows'] == spec['header']['expected_rows'], 'complete row count mismatch')
    require(counts['jacobian'] == spec['header']['expected_jacobian_rows'] and
            counts['polynomiality'] == spec['header']['expected_lift_rows'], 'row obligation mismatch')
    yield {'type': 'footer', 'complete': True, 'prefix_sha256': digest.hexdigest(),
           'prefix_records': nrecords, 'counts': dict(counts),
           'unused_variables': [i for i in range(len(spec['variables'])) if i not in used]}


def verify_stream(path, spec, context=None):
    """Strict same-formula full replay, including resynchronized corruption."""
    with Path(path).open('rb') as stream:
        for expected in records(spec, context):
            got = stream.readline()
            require(got == B.canonical(expected), 'strict full stream replay mismatch at '+expected['type'])
        require(stream.read(1) == b'', 'trailing data after complete footer')


class OutputBudget:
    def __init__(self, limit):
        self.limit, self.used = limit, 0

    def write(self, stream, data):
        require(self.used+len(data) <= self.limit, 'aggregate output cap')
        stream.write(data)
        self.used += len(data)


def rational_text(q):
    return str(q.numerator) if q.denominator == 1 else f'({q.numerator}/{q.denominator})'


def singular_polynomial(terms, variables, golden):
    out = []
    for wire, monomial in terms:
        c = B.decode(wire)
        require(golden or c.b == 0, 'golden coefficient in rational ring')
        coeff = f'({rational_text(c.a)}+({rational_text(c.b)})*rho)' if c.b else rational_text(c.a)
        factors = [f'({coeff})']
        for i, power in sorted(Counter(monomial).items()):
            factors.append(variables[i] if power == 1 else f'{variables[i]}^{power}')
        out.append('*'.join(factors))
    return '+'.join(out) if out else '0'


def construct(context, singular=False):
    spec = production_spec(context)
    prefix = 'client-'+context.case+'-'+context.branch
    budget = OutputBudget(context.caps['aggregate_output_bytes'])
    json_path = Path(prefix+'.jsonl')
    singular_path = Path(prefix+'.sing') if singular else None
    # All outputs are exclusive; incomplete files survive any failure/cap.
    with json_path.open('xb') as out:
        sing = singular_path.open('xb') if singular_path else None
        try:
            if sing:
                coefficient_ring = '(0,rho)' if context.branch == 'golden' else '0'
                declaration = f'ring R={coefficient_ring},('+','.join(spec['variables'])+'),dp;\n'
                if context.branch == 'golden':
                    declaration += 'minpoly=rho^2-3*rho+1;\n'
                budget.write(sing, (declaration+'ideal I=\n').encode())
            first = True
            footer = None
            for record in records(spec, context):
                budget.write(out, B.canonical(record))
                if sing and record['type'] == 'row':
                    line = ('' if first else ',\n')+'// '+record['label']+'\n'+singular_polynomial(
                        record['terms'], spec['variables'], context.branch == 'golden')
                    budget.write(sing, line.encode())
                    first = False
                if record['type'] == 'footer':
                    footer = record
            if sing:
                ending = ';\nprint("D125_COMPLETE_LITERAL_IMPORT_ONLY");\nprint(size(I));\nquit;\n'
                budget.write(sing, ending.encode())
                sing.flush()
                os.fsync(sing.fileno())
            out.flush()
            os.fsync(out.fileno())
        finally:
            if sing:
                sing.close()
    verify_stream(json_path, spec, context)
    context.check()
    manifest = {'status': 'CONSTRUCTION_AND_SAME_FORMULA_REPLAY_COMPLETE',
                'authority_sha256': context.authority_sha, 'pins': context.authority['pins'],
                'identity': {'pid': context.pid, 'pgid': context.pgid, 'start_ticks': context.start_ticks,
                             'boot_id': context.boot_id, **context.observed},
                'caps': context.caps, 'footer': footer, 'variables': len(spec['variables']),
                'jsonl': {'path': str(json_path), 'bytes': json_path.stat().st_size, 'sha256': sha(json_path)},
                'singular': None if not singular_path else {'path': str(singular_path),
                             'bytes': singular_path.stat().st_size, 'sha256': sha(singular_path)},
                'independent_certification': False, 'cas_executed': False}
    with Path(prefix+'.manifest.json').open('xb') as out:
        budget.write(out, B.canonical(manifest))
        out.flush()
        os.fsync(out.fileno())
    return manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--authority', required=True)
    parser.add_argument('--case', required=True, choices=tuple(B.VERTICES))
    parser.add_argument('--branch', required=True, choices=('rational', 'golden'))
    parser.add_argument('--singular-import-only', action='store_true')
    args = parser.parse_args()
    context = ProductionContext(Path(args.authority).read_bytes(), args.case, args.branch)
    print(json.dumps(construct(context, args.singular_import_only), sort_keys=True))


if __name__ == '__main__':
    main()
