#!/usr/bin/env python3
"""Independent tiny preflight for the sealed six-client coefficient interface.

Standard library only.  This deliberately constructs no production Jacobian,
lift stream, adapter input, ideal, or solver job.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction
import hashlib
import importlib.util
import json
from math import isqrt
from pathlib import Path
import resource
import signal
import sys
import time


LIMIT_AS = 512 * 1024**2
resource.setrlimit(resource.RLIMIT_AS, (LIMIT_AS, LIMIT_AS))
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
signal.alarm(30)
STARTED = time.monotonic()
sys.dont_write_bytecode = True

INPUT = Path('/tmp/jc2-lane.MAp4nm/inputs')
PINS = {
    'd125-minimal-receiver-client-preflight-astra-20260906.md':
        'e0debc7da22b8864ba43f0d29928e2104f2d8f161421ad26f29d8017f7b95e80',
    'client.py': 'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53',
    'test_client.py': '15d49bf7b4047ae0394379335a8614d53d083a38efd6042de4110cb9854de741',
    'd125-minimal-receiver-gate-fable5-20260906.md':
        'cd69c23885de119e4bd910992dad5ef695e7b12013168ec1c401546d8aa6ed8d',
    'd125-minimal-monomial-receiver-composition-astra-20260906.md':
        '7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413',
    'd125-small-receiver-polynomial-lift-contract-astra-20260906.md':
        '433cc2fe9f11ce1b2e1f1fc57aab24def921afb1f93154a2d631ddee0b88cdad',
    'FALLACY-v2.md':
        'e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5',
}

spec = importlib.util.spec_from_file_location('sealed_client', INPUT / 'client.py')
if spec is None or spec.loader is None:
    raise RuntimeError('cannot load sealed client')
C = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = C
spec.loader.exec_module(C)

Pair = tuple[Fraction, Fraction]
ZERO: Pair = (Fraction(0), Fraction(0))
ONE: Pair = (Fraction(1), Fraction(0))
RHO: Pair = (Fraction(0), Fraction(1))


class AuditError(ValueError):
    pass


checks: list[str] = []


def require(condition: bool, name: str) -> None:
    if not condition:
        raise AuditError(name)
    checks.append(name)


def reject(call, name: str) -> None:
    try:
        call()
    except (AuditError, ValueError, RuntimeError, ZeroDivisionError, json.JSONDecodeError):
        checks.append(name)
        return
    raise AuditError('corruption accepted: ' + name)


def add(x: Pair, y: Pair) -> Pair:
    return (x[0] + y[0], x[1] + y[1])


def neg(x: Pair) -> Pair:
    return (-x[0], -x[1])


def sub(x: Pair, y: Pair) -> Pair:
    return add(x, neg(y))


def mul(x: Pair, y: Pair) -> Pair:
    a, b = x
    c, d = y
    return (a*c - b*d, a*d + b*c + 3*b*d)


def scale(n, x: Pair) -> Pair:
    n = Fraction(n)
    return (n*x[0], n*x[1])


def conjugate(x: Pair) -> Pair:
    return (x[0] + 3*x[1], -x[1])


def norm(x: Pair) -> Fraction:
    return mul(x, conjugate(x))[0]


def inverse(x: Pair) -> Pair:
    n = norm(x)
    if n == 0:
        raise ZeroDivisionError('zero pair')
    return scale(1/n, conjugate(x))


def power(x: Pair, n: int) -> Pair:
    if n < 0:
        return power(inverse(x), -n)
    out = ONE
    base = x
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n //= 2
    return out


def wire(x: Pair) -> list[list[str]]:
    return [[str(x[0].numerator), str(x[0].denominator)],
            [str(x[1].numerator), str(x[1].denominator)]]


def from_client(x) -> Pair:
    return (Fraction(x.a), Fraction(x.b))


def canonical(value) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(',', ':')) + '\n').encode()


def poly_mul(left: dict[tuple[int, int], Pair],
             right: dict[tuple[int, int], Pair]) -> dict[tuple[int, int], Pair]:
    out: dict[tuple[int, int], Pair] = {}
    for (i, j), a in left.items():
        for (k, l), b in right.items():
            p = (i+k, j+l)
            out[p] = add(out.get(p, ZERO), mul(a, b))
    return {p: x for p, x in out.items() if x != ZERO}


def poly_power(poly: dict[tuple[int, int], Pair], n: int):
    out = {(0, 0): ONE}
    for _ in range(n):
        out = poly_mul(out, poly)
    return out


VERTICES = {
    'unequal': (((0, 0), (0, 15), (9, 6), (2, 1)),
                ((0, 0), (0, 25), (15, 10), (1, 0))),
    'common_3': (((0, 0), (0, 15), (9, 6), (3, 0)),
                 ((0, 0), (0, 25), (15, 10), (5, 0))),
    'common_4': (((0, 0), (0, 15), (9, 6), (9, 0)),
                 ((0, 0), (0, 25), (15, 10), (15, 0))),
}
NORMAL = {'unequal': (5, -7), 'common_3': (1, -1), 'common_4': (1, 0)}


def cross(a, b, c) -> int:
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])


def area2(vertices) -> int:
    return abs(sum(a[0]*b[1]-a[1]*b[0]
                   for a, b in zip(vertices, vertices[1:]+vertices[:1])))


def independent_lattice(vertices) -> list[tuple[int, int]]:
    """Convex membership by area decomposition, not the client's sign test."""
    total = area2(vertices)
    points = []
    for i in range(max(x for x, _ in vertices)+1):
        for j in range(max(y for _, y in vertices)+1):
            p = (i, j)
            if sum(abs(cross(a, b, p))
                   for a, b in zip(vertices, vertices[1:]+vertices[:1])) == total:
                points.append(p)
    return points


def face_data(case: str, branch: str):
    kappa = ONE if branch == 'rational' else RHO
    cubic = ({(0, 3): ONE, (3, 0): ONE} if branch == 'rational' else
             {(0, 3): ONE, (1, 2): sub(scale(3, ONE), scale(2, RHO)),
              (2, 1): sub(scale(2, ONE), RHO), (3, 0): RHO})
    h = {(i, j+2): value for (i, j), value in cubic.items()}
    outer = (poly_power(h, 3), poly_power(h, 5))
    if case == 'unequal':
        inner = ({(2, 1): ONE, (9, 6): power(kappa, 3)},
                 {(1, 0): scale(Fraction(5, 9), inverse(kappa)),
                  (8, 5): scale(Fraction(5, 3), power(kappa, 2)),
                  (15, 10): power(kappa, 5)})
        scalar = neg(scale(Fraction(5, 9), inverse(kappa)))
    else:
        root = ({(3, 2): ONE, (2, 1): scale(-2, ONE), (1, 0): ONE}
                if case == 'common_3' else
                {(3, 2): ONE, (3, 1): scale(-2, ONE), (3, 0): ONE})
        inner = (poly_power(root, 3), poly_power(root, 5))
        inner = tuple({p: mul(power(kappa, n), value) for p, value in poly.items()}
                      for n, poly in zip((3, 5), inner))
        scalar = None
    return kappa, outer, inner, scalar


def expected_contract(case: str, branch: str):
    kappa, outer, inner, scalar = face_data(case, branch)
    variables: list[str] = []
    maps = []
    guards = []
    fixed_counts = []
    face_census = []
    for member, vertices, degree, outface, inface in zip(
            ('A', 'B'), VERTICES[case], (15, 25), outer, inner):
        support = independent_lattice(vertices)
        nx, ny = NORMAL[case]
        top = max(nx*i + ny*j for i, j in vertices)
        entries = []
        outer_points = [p for p in support if sum(p) == degree]
        inner_points = [p for p in support if nx*p[0] + ny*p[1] == top]
        face_census.append((len(outer_points), len(inner_points),
                            len(set(outer_points) & set(inner_points))))
        for i, j in support:
            specifications = []
            if i+j == degree:
                specifications.append(('outer', outface.get((i, j), ZERO)))
            if nx*i+ny*j == top:
                specifications.append(('inner', inface.get((i, j), ZERO)))
            if (i, j) == (0, 0):
                specifications.append(('target_constant', ZERO))
            label = f'{member}_g{i}_p{j}'
            if specifications:
                value = specifications[0][1]
                if any(other != value for _, other in specifications):
                    raise AuditError('independent face intersection conflict')
                entries.append({'point': [i, j], 'name': label,
                                'fixed': wire(value),
                                'reasons': [reason for reason, _ in specifications]})
            else:
                entries.append({'point': [i, j], 'name': label,
                                'variable': len(variables)})
                variables.append(label)
        bypoint = {tuple(entry['point']): entry for entry in entries}
        for point in vertices[1:]:
            value_wire = bypoint[point]['fixed']
            value = (Fraction(int(value_wire[0][0]), int(value_wire[0][1])),
                     Fraction(int(value_wire[1][0]), int(value_wire[1][1])))
            if value == ZERO:
                raise AuditError('independent zero vertex')
            guards.append({'label': f'GUARD/{member}/{point[0]}/{point[1]}',
                           'value': wire(value), 'inverse': wire(inverse(value))})
        maps.append(entries)
        fixed_counts.append(sum('fixed' in entry for entry in entries))
    free = len(variables)
    if scalar is None:
        variables += ['c', 'z']
        scalar_data = {'variable': free, 'inverse_variable': free+1,
                       'row': 'z*c-1'}
    else:
        scalar_data = {'fixed': wire(scalar), 'inverse': wire(inverse(scalar))}
    contract = {
        'schema': 'jc2.minimal-receiver-preflight/v1',
        'status': 'PROVISIONAL_PREP_ONLY_NO_PRODUCTION_AUTHORITY',
        'case': case,
        'branch': branch,
        'field': 'Q' if branch == 'rational' else 'Q[rho]/(rho^2-3*rho+1)',
        'geometric_scope': 'algebraically closed characteristic zero',
        'order': 'global degree reverse lexicographic, displayed variable order',
        'variables': variables,
        'coefficient_maps': maps,
        'vertex_guards': guards,
        'scalar': scalar_data,
        'counts': {
            'raw': [len(member) for member in maps],
            'fixed': fixed_counts,
            'free': free,
            'variables': len(variables),
            'raw_pair_upper_bound': len(maps[0])*len(maps[1]),
            'jacobian_envelope_rows': 660,
            'planned_all_rows': 660+sum(fixed_counts)+7,
        },
        'target': 'J(A,B)-c*gamma^2; J=A_gamma*B_pi-A_pi*B_gamma',
        'row_envelope': '0<=I<=23, 0<=J, I+J<=38; all 660 rows including zero',
        'degree_guards': 'A_(0,15)=B_(0,25)=1; six nonorigin vertices guarded',
        'production_export_implemented': False,
    }
    return contract, face_census


def independent_validate(contract) -> None:
    expected, _ = expected_contract(contract.get('case'), contract.get('branch'))
    if canonical(expected) != canonical(contract):
        raise AuditError('independent contract mismatch')


def reindex_after_map_change(contract) -> None:
    variables = []
    fixed_counts = []
    for entries in contract['coefficient_maps']:
        for entry in entries:
            if 'fixed' not in entry:
                entry['variable'] = len(variables)
                variables.append(entry['name'])
            else:
                entry.pop('variable', None)
        fixed_counts.append(sum('fixed' in entry for entry in entries))
    free = len(variables)
    if 'row' in contract['scalar']:
        variables += ['c', 'z']
        contract['scalar']['variable'] = free
        contract['scalar']['inverse_variable'] = free+1
    contract['variables'] = variables
    counts = contract['counts']
    counts['raw'] = [len(entries) for entries in contract['coefficient_maps']]
    counts['fixed'] = fixed_counts
    counts['free'] = free
    counts['variables'] = len(variables)
    counts['raw_pair_upper_bound'] = counts['raw'][0]*counts['raw'][1]
    counts['planned_all_rows'] = 660+sum(fixed_counts)+7


def cp_add(left, right):
    out = dict(left)
    for monomial, value in right.items():
        out[monomial] = add(out.get(monomial, ZERO), value)
    return {m: x for m, x in out.items() if x != ZERO}


def cp_scale(n, poly):
    return {m: scale(n, x) for m, x in poly.items() if scale(n, x) != ZERO}


def cp_mul(left, right):
    out = {}
    for am, av in left.items():
        for bm, bv in right.items():
            monomial = tuple(sorted(am+bm))
            out[monomial] = add(out.get(monomial, ZERO), mul(av, bv))
    return {m: x for m, x in out.items() if x != ZERO}


def derivative(poly, axis):
    out = {}
    for (i, j), coefficient in poly.items():
        exponent = i if axis == 0 else j
        if not exponent:
            continue
        point = (i-1, j) if axis == 0 else (i, j-1)
        out[point] = cp_add(out.get(point, {}), cp_scale(exponent, coefficient))
    return out


def polynomial_product(left, right):
    out = {}
    for (i, j), a in left.items():
        for (k, l), b in right.items():
            point = (i+k, j+l)
            out[point] = cp_add(out.get(point, {}), cp_mul(a, b))
    return {p: x for p, x in out.items() if x}


def independent_jacobian(left, right):
    first = polynomial_product(derivative(left, 0), derivative(right, 1))
    second = polynomial_product(derivative(left, 1), derivative(right, 0))
    points = set(first) | set(second)
    return {p: cp_add(first.get(p, {}), cp_scale(-1, second.get(p, {})))
            for p in points
            if cp_add(first.get(p, {}), cp_scale(-1, second.get(p, {})))}


def convert_coeff_poly(poly):
    return {monomial: from_client(value) for monomial, value in poly.items()}


def convert_input(poly):
    return {point: convert_coeff_poly(coefficient) for point, coefficient in poly.items()}


def decode_wire(raw) -> Pair:
    if (not isinstance(raw, list) or len(raw) != 2 or
            any(not isinstance(part, list) or len(part) != 2 for part in raw) or
            any(not isinstance(item, str) for part in raw for item in part)):
        raise AuditError('field wire shape/type')
    try:
        value = (Fraction(int(raw[0][0]), int(raw[0][1])),
                 Fraction(int(raw[1][0]), int(raw[1][1])))
    except (ValueError, ZeroDivisionError) as error:
        raise AuditError('field wire fraction') from error
    if wire(value) != raw:
        raise AuditError('noncanonical field wire')
    return value


def stream_records(data: bytes):
    return [json.loads(line) for line in data.splitlines()]


def rebuild_stream(records) -> bytes:
    body = [record for record in records if record.get('type') != 'footer']
    rows = [record for record in body if record.get('type') == 'row']
    footer = {
        'type': 'footer',
        'complete': True,
        'rows': len(rows),
        'terms': sum(len(row['terms']) for row in rows),
        'zero_rows': sum(not row['terms'] for row in rows),
        'prefix_sha256': hashlib.sha256(b''.join(map(canonical, body))).hexdigest(),
    }
    return b''.join(map(canonical, body+[footer]))


def independent_verify_toy(data, left, right, outputs, scalar, variables) -> None:
    """Tiny verifier derived from differentiation, not the forced-index kernel."""
    try:
        records = stream_records(data)
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise AuditError('invalid JSONL') from error
    if not records or any(not isinstance(record, dict) for record in records):
        raise AuditError('record shape')
    if b''.join(map(canonical, records)) != data:
        raise AuditError('noncanonical stream bytes')
    header = {'type': 'header', 'schema': 'jc2.toy-literal-field/v1',
              'field': 'Q[rho]/(rho^2-3*rho+1)', 'index_base': 0,
              'variables': variables, 'status': 'TOY_NOT_A_RECEIVER_EXPORT'}
    if records[0] != header or records[-1].get('type') != 'footer':
        raise AuditError('header/footer')
    rows = records[1:-1]
    ordered_outputs = sorted(outputs)
    if (len(set(outputs)) != len(outputs) or (2, 0) not in outputs or
            [row.get('label') for row in rows] !=
            [f'J/{i}/{j}' for i, j in ordered_outputs]):
        raise AuditError('row roster/order')
    own_rows = independent_jacobian(convert_input(left), convert_input(right))
    scalar_pair = convert_coeff_poly(scalar)
    term_count = zero_count = 0
    for point, row in zip(ordered_outputs, rows):
        if row.get('type') != 'row' or not isinstance(row.get('terms'), list):
            raise AuditError('row shape')
        expected = own_rows.get(point, {})
        if point == (2, 0):
            expected = cp_add(expected, cp_scale(-1, scalar_pair))
        actual = {}
        prior = None
        for term in row['terms']:
            if not isinstance(term, list) or len(term) != 2 or not isinstance(term[1], list):
                raise AuditError('term shape')
            monomial = tuple(term[1])
            if (any(not isinstance(index, int) or index < 0 or index >= len(variables)
                    for index in monomial) or tuple(sorted(monomial)) != monomial):
                raise AuditError('monomial ids')
            if prior is not None and monomial <= prior:
                raise AuditError('duplicate/unsorted monomial')
            prior = monomial
            coefficient = decode_wire(term[0])
            if coefficient == ZERO:
                raise AuditError('serialized zero term')
            actual[monomial] = coefficient
        if actual != expected:
            raise AuditError('row semantics')
        term_count += len(actual)
        zero_count += not actual
    prefix = b''.join(map(canonical, records[:-1]))
    expected_footer = {'type': 'footer', 'complete': True, 'rows': len(rows),
                       'terms': term_count, 'zero_rows': zero_count,
                       'prefix_sha256': hashlib.sha256(prefix).hexdigest()}
    if records[-1] != expected_footer:
        raise AuditError('footer values/checksum')


def make_mutations(base_contract, stream, left, right, outputs, scalar, variables,
                   field_row, field_left, field_right, field_outputs,
                   field_scalar, field_variables):
    wrong_target = C.toy_stream(left, right, outputs, {(3,): -C.ONE}, variables)

    rows_missing = stream_records(stream)
    remove_at = next(i for i, record in enumerate(rows_missing)
                     if record.get('type') == 'row' and record['label'] == 'J/1/1')
    rows_missing.pop(remove_at)
    missing_row = rebuild_stream(rows_missing)

    no_footer = b''.join(map(canonical, stream_records(stream)[:-1]))

    field_records = stream_records(stream)
    term = next(term for record in field_records if record.get('type') == 'row'
                for term in record['terms'])
    decoded = C.decode(term[0])
    term[0] = (decoded + C.RHO).wire()
    field_change = rebuild_stream(field_records)

    split_records = stream_records(field_row)
    original = split_records[1]
    if len(original['terms']) != 2:
        raise AuditError('field-row split fixture')
    first = copy.deepcopy(original)
    second = copy.deepcopy(original)
    first['terms'] = [original['terms'][0]]
    second['terms'] = [original['terms'][1]]
    split_row = rebuild_stream([split_records[0], first, second, split_records[-1]])

    vertex = copy.deepcopy(base_contract)
    point = tuple(VERTICES['unequal'][0][1])
    entry = next(e for e in vertex['coefficient_maps'][0] if tuple(e['point']) == point)
    entry['fixed'] = wire((Fraction(2), Fraction(0)))
    guard = next(g for g in vertex['vertex_guards'] if g['label'] == 'GUARD/A/0/15')
    guard['value'] = wire((Fraction(2), Fraction(0)))
    guard['inverse'] = wire((Fraction(1, 2), Fraction(0)))

    face = copy.deepcopy(base_contract)
    zero_face = next(e for e in face['coefficient_maps'][0]
                     if 'outer' in e.get('reasons', []) and e['fixed'] == wire(ZERO))
    zero_face.pop('fixed')
    zero_face.pop('reasons')
    zero_face['variable'] = -1
    reindex_after_map_change(face)

    return {
        'target': lambda: independent_verify_toy(
            wrong_target, left, right, outputs, scalar, variables),
        'missing_row': lambda: independent_verify_toy(
            missing_row, left, right, outputs, scalar, variables),
        'footer': lambda: independent_verify_toy(
            no_footer, left, right, outputs, scalar, variables),
        'field': lambda: independent_verify_toy(
            field_change, left, right, outputs, scalar, variables),
        'split_row': lambda: independent_verify_toy(
            split_row, field_left, field_right, field_outputs,
            field_scalar, field_variables),
        'vertex': lambda: independent_validate(vertex),
        'face': lambda: independent_validate(face),
    }, {
        'target': wrong_target,
        'missing_row': missing_row,
        'footer': no_footer,
        'field': field_change,
        'split_row': split_row,
        'vertex': vertex,
        'face': face,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output')
    parser.add_argument('--inject', choices=(
        'target', 'missing_row', 'footer', 'field', 'split_row', 'vertex', 'face'))
    args = parser.parse_args()
    if not args.output and not args.inject:
        parser.error('--output is required for a positive run')

    observed_pins = {name: hashlib.sha256((INPUT/name).read_bytes()).hexdigest()
                     for name in PINS}
    require(observed_pins == PINS, 'all seven immutable input pins')

    # Independent quadratic arithmetic, including the formal two embeddings.
    require(mul(RHO, RHO) == sub(scale(3, RHO), ONE), 'independent minimal polynomial')
    require(isqrt(5)**2 != 5, 'quadratic discriminant nonsquare over Q')
    require(mul(RHO, sub(scale(3, ONE), RHO)) == ONE, 'independent rho inverse')
    require(conjugate(RHO) == sub(scale(3, ONE), RHO)
            and conjugate(conjugate(RHO)) == RHO, 'both embeddings retained by conjugation')
    samples = [(Fraction(a, 3), Fraction(b, 2)) for a in range(-2, 3)
               for b in range(-2, 3)]
    for x in samples:
        cx = C.F(x[0], x[1])
        require(from_client(cx*cx) == mul(x, x), f'field square {x}')
        require(from_client(C.F(x[0]+3*x[1], -x[1])) == conjugate(x),
                f'field conjugate {x}')
        if x != ZERO:
            require(from_client(cx.inverse()) == inverse(x)
                    and mul(x, inverse(x)) == ONE, f'field inverse {x}')
    reject(lambda: C.decode([['2', '2'], ['0', '1']]), 'unreduced field wire')
    reject(lambda: C.decode([['1', '-1'], ['0', '1']]), 'negative denominator wire')
    reject(lambda: C.decode([[1, 1], ['0', '1']]), 'numeric field wire')
    reject(lambda: C.decode([['1', '0'], ['0', '1']]), 'zero denominator wire')
    require(C.canonical({'b': 1, 'a': 2}) == canonical({'b': 1, 'a': 2}),
            'independent canonical JSON')

    contracts = {}
    face_censuses = {}
    expected_counts = {
        'unequal': ([83, 215], [12, 19], 267, 267, 698),
        'common_3': ([94, 241], [17, 27], 291, 293, 711),
        'common_4': ([115, 296], [17, 27], 367, 369, 711),
    }
    for case in VERTICES:
        for branch in ('rational', 'golden'):
            key = case + '/' + branch
            actual = C.make_contract(case, branch)
            expected, census = expected_contract(case, branch)
            require(canonical(actual) == canonical(expected), key+' independent full contract')
            independent_validate(actual)
            counts = actual['counts']
            require((counts['raw'], counts['fixed'], counts['free'],
                     counts['variables'], counts['planned_all_rows']) == expected_counts[case],
                    key+' independent counts')
            require(census == ([(10, 2, 1), (16, 3, 1)] if case == 'unequal'
                               else [(10, 7, 1), (16, 11, 1)]),
                    key+' complete face/intersection census')
            require(all(entry.get('fixed') == wire(ZERO)
                        for member in actual['coefficient_maps']
                        for entry in member if entry['point'] == [0, 0]),
                    key+' both constants fixed zero')
            require(not any(guard['label'].endswith('/0/0')
                            for guard in actual['vertex_guards']), key+' origin not guarded')
            require(len(actual['vertex_guards']) == 6, key+' exactly six vertex guards')
            require(all(mul((Fraction(int(g['value'][0][0]), int(g['value'][0][1])),
                             Fraction(int(g['value'][1][0]), int(g['value'][1][1]))),
                            (Fraction(int(g['inverse'][0][0]), int(g['inverse'][0][1])),
                             Fraction(int(g['inverse'][1][0]), int(g['inverse'][1][1])))
                            ) == ONE for g in actual['vertex_guards']),
                    key+' all vertex units exact')
            base_names = [entry['name'] for member in actual['coefficient_maps']
                          for entry in member if 'variable' in entry]
            require(actual['variables'][:len(base_names)] == base_names,
                    key+' A-then-B lexicographic variable order')
            require(actual['variables'][len(base_names):] == ([] if case == 'unequal'
                                                               else ['c', 'z']),
                    key+' exact scalar variable tail')
            contracts[key] = actual
            face_censuses[key] = census

    envelope = [(i, j) for i in range(24) for j in range(39-i)]
    require(len(envelope) == 660 and len(set(envelope)) == 660
            and (2, 0) in envelope, 'all 660 conservative row indices')

    # The target residual adds -c, hence +5/(9*kappa) in unequal clients.
    target_signs = {}
    for branch, kappa in (('rational', C.ONE), ('golden', C.RHO)):
        c = -C.F(Fraction(5, 9))*kappa**-1
        data = C.toy_stream({}, {}, [(2, 0)], {(): c}, [])
        row = stream_records(data)[1]
        got = C.decode(row['terms'][0][0])
        require(got == C.F(Fraction(5, 9))*kappa**-1,
                branch+' unequal residual target sign')
        target_signs[branch] = got.wire()

    # Tiny derivative-product oracle versus the sealed forced-index lookup.
    left = {(0, 0): {(2,): C.ONE}, (1, 0): {(0,): C.ONE},
            (0, 2): {(): C.RHO}}
    right = {(2, 1): {(1,): C.ONE}, (1, 0): {(): C.RHO},
             (0, 1): {(): C.ONE}}
    outputs = [(i, j) for i in range(4) for j in range(3)]
    scalar = {(3,): C.ONE}
    variables = ['a', 'b', 'Aconstant_unused', 'c']
    own_rows = independent_jacobian(convert_input(left), convert_input(right))
    require(all(convert_coeff_poly(C.coefficient_row(left, right, point)) ==
                own_rows.get(point, {}) for point in outputs),
            'forced-index kernel versus own formal differentiation')
    stream = C.toy_stream(left, right, outputs, scalar, variables)
    C.verify_toy_stream(stream, left, right, outputs, scalar, variables)
    independent_verify_toy(stream, left, right, outputs, scalar, variables)
    records = stream_records(stream)
    prefix = b''.join(map(canonical, records[:-1]))
    require(records[-1]['prefix_sha256'] == hashlib.sha256(prefix).hexdigest(),
            'footer prefix checksum independently recomputed')
    require(records[-1]['rows'] == len(outputs)
            and records[-1]['terms'] == sum(len(r['terms']) for r in records[1:-1])
            and records[-1]['zero_rows'] == sum(not r['terms'] for r in records[1:-1]),
            'footer counts independently recomputed')

    # The discriminating equation z+rho=0 remains one field-valued row.
    field_left = {(1, 0): {(): C.ONE}}
    field_right = {(2, 1): {(0,): C.ONE, (): C.RHO}}
    field_outputs = [(2, 0)]
    field_scalar = {}
    field_variables = ['z']
    one_row = C.toy_stream(field_left, field_right, field_outputs,
                           field_scalar, field_variables)
    independent_verify_toy(one_row, field_left, field_right, field_outputs,
                           field_scalar, field_variables)
    one_records = stream_records(one_row)
    terms = {tuple(term[1]): decode_wire(term[0]) for term in one_records[1]['terms']}
    require(len(one_records) == 3 and len(one_records[1]['terms']) == 2
            and terms == {(): RHO, (0,): ONE}
            and add(terms[()], mul(neg(RHO), terms[(0,)])) == ZERO,
            'z+rho is one atomic row with witness z=-rho')

    mutations, mutation_objects = make_mutations(
        contracts['unequal/rational'], stream, left, right, outputs, scalar, variables,
        one_row, field_left, field_right, field_outputs, field_scalar, field_variables)
    for name, probe in mutations.items():
        reject(probe, name+' actual changed object rejected')
    # Also feed contract corruptions through the producer's self-validator.
    reject(lambda: C.validate_contract(mutation_objects['vertex']),
           'producer rejects consistent nonzero vertex corruption')
    reject(lambda: C.validate_contract(mutation_objects['face']),
           'producer rejects reindexed fixed-zero face corruption')
    reject(lambda: C.verify_toy_stream(mutation_objects['split_row'], field_left,
                                       field_right, field_outputs,
                                       field_scalar, field_variables),
           'producer replay rejects recomputed-checksum coordinate split')
    reject(lambda: C.verify_toy_stream(
        json.dumps(stream_records(stream), indent=2).encode(),
        left, right, outputs, scalar, variables), 'noncanonical serialization rejected')
    reject(C.production_export, 'production exporter absent')
    reject(lambda: C.coefficient_row({(i, 0): {} for i in range(9)},
                                     {(i, 0): {} for i in range(9)}, (0, 0)),
           'production-size row kernel refused before expansion')

    # Narrow extension interface only: exponent algebra, index roster and names.
    # No receiver coefficient or lift polynomial is expanded here.
    for i in range(3):
        for j in range(5):
            for t in range(j+1):
                for b in range(j-t+1):
                    for d in range(j-t-b+1):
                        remainder = j-t-b-d
                        direct_exponent = -i + 4*t + 2*b + d - remainder
                        formula_exponent = 5*t + 3*b + 2*d - i - j
                        direct_sign = -1 if (b+d+remainder) % 2 else 1
                        formula_sign = -1 if (j-t) % 2 else 1
                        require(direct_exponent == formula_exponent
                                and direct_sign == formula_sign,
                                f'lift exponent/sign identity {i}/{j}/{t}/{b}/{d}')
    lift_rows = []
    for source, degree in (('A', 15), ('B', 25)):
        for t in range((degree-1)//5 + 1):
            for e in range(5*t-degree, 0):
                lift_rows.append((source, t, e))
                require(0 <= 5*t-e <= degree, f'{source}/{t}/{e} pi-axis witness')
    require(len(lift_rows) == 105, 'extension has exactly 105 negative-v row indices')
    require(sorted({t for source, t, _ in lift_rows if source == 'A'}) == [0, 1, 2]
            and sorted({t for source, t, _ in lift_rows if source == 'B'}) == [0, 1, 2, 3, 4],
            'extension u exponents are A 0..2 and B 0..4')
    extension_variables = ['lambda2', 'lambda3']
    require(all(name not in contract['variables'] for contract in contracts.values()
                for name in extension_variables), 'extension variables have no receiver collision')
    require(len(extension_variables) == 2, 'exactly two collision-free extension names')
    augmented = {case: {'variables': values[3]+2, 'rows': values[4]+105}
                 for case, values in expected_counts.items()}
    require(augmented == {'unequal': {'variables': 269, 'rows': 803},
                          'common_3': {'variables': 295, 'rows': 816},
                          'common_4': {'variables': 371, 'rows': 816}},
            'projected extension count arithmetic')

    if args.inject:
        # An injected run must terminate nonzero on the actual altered object.
        mutations[args.inject]()
        raise AuditError('injected corruption unexpectedly accepted')

    result = {
        'status': 'PASS',
        'check_count': len(checks),
        'checks': checks,
        'input_sha256': observed_pins,
        'baseline_counts': {case: {
            'raw': expected_counts[case][0],
            'fixed': expected_counts[case][1],
            'free_coefficients': expected_counts[case][2],
            'ring_variables': expected_counts[case][3],
            'planned_rows': expected_counts[case][4],
        } for case in expected_counts},
        'augmented_interface_counts': augmented,
        'jacobian_index_count': len(envelope),
        'lift_index_count': len(lift_rows),
        'target_residual_constants': target_signs,
        'toy_stream_sha256': hashlib.sha256(stream).hexdigest(),
        'one_field_row_sha256': hashlib.sha256(one_row).hexdigest(),
        'elapsed_seconds': time.monotonic()-STARTED,
        'maxrss_KiB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'limits': {'wall_seconds': 30, 'cpu_seconds': 25, 'AS_bytes': LIMIT_AS},
        'production_J_expanded': False,
        'production_lift_expanded': False,
        'adapter_or_solver_used': False,
    }
    output = Path(args.output)
    with output.open('x') as handle:
        json.dump(result, handle, sort_keys=True, indent=2)
        handle.write('\n')
    print(json.dumps({'status': 'PASS', 'checks': len(checks),
                      'elapsed_seconds': result['elapsed_seconds'],
                      'maxrss_KiB': result['maxrss_KiB']}, sort_keys=True))


if __name__ == '__main__':
    main()
