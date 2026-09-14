#!/usr/bin/env python3
"""Provisional mu2 slice: capped construction, never a solver or certificate.

No production invocation is authorized by this preparation. All coefficient
polynomials are sparse Q polynomials in sorted repeated variable indices.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import os
import platform
import resource
import signal
import sys
import time
import baseline as B
import qpoly as Q

SOURCE = 'b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac'
SYMMETRY = '9bed554644b1bd3c881ba4e289ea0950601ed6141677a45152577442fd477b12'
ROOT = '/home/ubuntu/d125-parity-compression-pilot-20260907'
INSTANCE = 'i-0da0cebfc97c9fd54'
CEILINGS = dict(wall_seconds=300, cpu_seconds=300, address_bytes=4*1024**3,
                output_bytes=128*1024**2, polynomial_terms=100000,
                multiply_pairs=1000000, coefficient_bits=4096,
                retained_terms=1000000)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def const(value):
    value = F(value)
    return {(): value} if value else {}


def rational(wire):
    value = B.decode(wire)
    need(not value.b, 'Q coefficient required; no field splitting')
    return value.a


def wire(poly):
    return [[[[str(c.numerator), str(c.denominator)], ['0', '1']], list(m)]
            for m, c in sorted(poly.items())]


class Arithmetic:
    def __init__(self, caps, deadline):
        self.caps, self.deadline = caps, deadline
        self.production = False
        self.stats = dict(operations=0, max_terms=0, max_degree=0,
                          max_coefficient_bits=0, retained_terms=0)

    def check(self, p):
        need(time.monotonic() < self.deadline, 'wall cap')
        need(len(p) <= self.caps['polynomial_terms'], 'polynomial term cap')
        bits = max((max(abs(c.numerator).bit_length(), c.denominator.bit_length())
                    for c in p.values()), default=0)
        need(bits <= self.caps['coefficient_bits'], 'coefficient bit cap')
        self.stats['operations'] += 1
        self.stats['max_terms'] = max(self.stats['max_terms'], len(p))
        self.stats['max_degree'] = max(self.stats['max_degree'],
                                       max(map(len, p), default=0))
        self.stats['max_coefficient_bits'] = max(self.stats['max_coefficient_bits'], bits)
        return p

    def add(self, a, b, scale=F(1)):
        need(len(a)+len(b) <= 2*self.caps['polynomial_terms'], 'addition cap')
        return self.check(Q.add(a, b, F(scale)))

    def mul(self, a, b):
        need(len(a)*len(b) <= self.caps['multiply_pairs'], 'multiplication pair cap')
        return self.check(Q.mul(a, b))

    def keep(self, p):
        self.check(p)
        self.stats['retained_terms'] += len(p)
        need(self.stats['retained_terms'] <= self.caps['retained_terms'], 'retained term cap')
        return p


def inverse(matrix):
    n = len(matrix)
    need(n and all(len(row) == n for row in matrix), 'square constant matrix')
    a = [[F(c) for c in row]+[F(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for j in range(n):
        k = next((k for k in range(j, n) if a[k][j]), None)
        need(k is not None, 'singular constant pivot matrix')
        a[j], a[k] = a[k], a[j]
        pivot = a[j][j]
        a[j] = [v/pivot for v in a[j]]
        for k in range(n):
            if k != j:
                factor = a[k][j]
                a[k] = [v-factor*w for v, w in zip(a[k], a[j])]
    return [row[n:] for row in a]


def independent_rows(matrix):
    basis, chosen = {}, []
    width = len(matrix[0])
    for index, row in enumerate(matrix):
        v = list(map(F, row))
        for pivot in sorted(basis):
            factor = v[pivot]
            v = [x-factor*y for x, y in zip(v, basis[pivot])]
        pivot = next((j for j, c in enumerate(v) if c), None)
        if pivot is not None:
            factor = v[pivot]
            basis[pivot] = [x/factor for x in v]
            chosen.append(index)
        if len(chosen) == width:
            return chosen
    raise ValueError('constant block lacks full column rank')


def solve_constants(matrix, forcing, ops):
    inv = inverse(matrix)
    out = []
    for row in inv:
        p = {}
        for c, rhs in zip(row, forcing):
            p = ops.add(p, rhs, -c)
        out.append(ops.keep(p))
    return out, inv


def hermite_matrix(s):
    r = (s+4)//5
    return [[(-1)**(s-i-t)*comb(s-i, t) for i in range(r)] for t in range(r)]


def b_matrix(d, columns):
    h = {0: 1, 3: 3, 6: 3, 9: 1}
    return [[((r+1-i)*d-15*i)*h.get(r+1-i, 0) for i in columns]
            for r in range(d+14)]


def jrow(a, b, I, J, ops, target=True):
    need(ops.production or len(a)*len(b) <= 64, 'production J needs authorized context')
    out = const(F(5, 9)) if target and (I, J) == (2, 0) else {}
    for (i, j), av in a.items():
        k, l = I+1-i, J+1-j
        det = i*l-j*k
        if det and av and b.get((k, l)):
            out = ops.add(out, ops.mul(av, b[k, l]), det)
    return out


def liftrow(coeffs, t, e, lambda_id, ops):
    """Exact lambda2=0 specialization, with lambda3 never normalized."""
    need(ops.production or len(coeffs) <= 16, 'production lift needs authorized context')
    out = {}
    for (i, j), value in coeffs.items():
        twice_d = e+i+j-5*t
        if not value or t > j or twice_d < 0 or twice_d % 2:
            continue
        d = twice_d//2
        z = j-t-d
        if z < 0:
            continue
        c = F((-1)**(j-t)*factorial(j), factorial(t)*factorial(d)*factorial(z))
        out = ops.add(out, ops.mul(value, {(lambda_id,)*d: F(1)}), c)
    return out


def transport(poly, maps, ops):
    out = {}
    for monomial, coefficient in poly.items():
        term = const(coefficient)
        for index in monomial:
            need(index in maps, 'missing original variable map')
            term = ops.mul(term, maps[index])
        out = ops.add(out, term)
    return out


def verify_transport(original, maps, traces, ops):
    """Exact toy/replay interface; all supplied original rows mandatory."""
    need(len(original) == len(traces), 'missing original row trace')
    residual = 0
    for index, ((label, p), trace) in enumerate(zip(original, traces)):
        expected = transport(p, maps, ops)
        need(trace['original_index'] == index and trace['label'] == label, 'row order drift')
        need(trace['terms'] == wire(expected), 'transported row mismatch')
        need(trace['residual_index'] == (residual if expected else None), 'residual omitted/reindexed')
        residual += bool(expected)
    return residual


def check_fixed(entries, coefficients):
    for entry in entries:
        if 'fixed' in entry:
            need(coefficients[tuple(entry['point'])] == const(rational(entry['fixed'])),
                 'fixed face/constant drift: '+entry['name'])


def shear(a, b, scalar, ops):
    need(set(a) <= set(b), 'A support outside B polygon')
    return {point: ops.keep(ops.add(value, ops.mul(scalar, a.get(point, {}))))
            for point, value in b.items()}


def metadata(mode, ops):
    """Production metadata only: not called by the local toy suite."""
    need(ops.production, 'production metadata requires authorized context')
    need(mode in ('slice', 'full'), 'unknown shear presentation')
    contract = B.make_contract('unequal', 'rational')
    maps = contract['coefficient_maps']
    free = [[e for e in entries if 'variable' in e and sum(e['point']) % 2]
            for entries in maps]
    pivots = {(i, s-i) for s in range(1, 15, 2) for i in range((s+4)//5)}
    retained = [e for e in free[0] if tuple(e['point']) not in pivots]
    need([len(v) for v in free] == [33, 94] and len(pivots) == 13 and len(retained) == 20,
         'parity metadata count drift')
    need(pivots <= {tuple(e['point']) for e in free[0]}, 'unlicensed A pivot')
    names = [e['name'] for e in retained]+['beta5_slice']
    if mode == 'full':
        names += ['shear_s']
    names += ['lambda3']
    original = contract['variables']+['lambda2', 'lambda3']
    need(len(original) == 269 and len(names) == (22 if mode == 'slice' else 23), 'dimension metadata')
    return contract, free, pivots, retained, names, original


def reconstruct(mode, ops):
    contract, free, pivots, retained, names, original = metadata(mode, ops)
    coefficients = []
    for entries in contract['coefficient_maps']:
        coefficients.append({tuple(e['point']): const(rational(e['fixed']))
                             if 'fixed' in e else {} for e in entries})
    a, b = coefficients
    for index, entry in enumerate(retained):
        a[tuple(entry['point'])] = {(index,): F(1)}
    lam = names.index('lambda3')
    graph = []
    selected = set()
    for s in range(13, 0, -2):
        points = [(i, s-i) for i in range((s+4)//5)]
        labels = [f'LIFT/A/{t}/{5*t-s}' for t in range(len(points))]
        forcing = [liftrow(a, t, 5*t-s, lam, ops) for t in range(len(points))]
        values, inv = solve_constants(hermite_matrix(s), forcing, ops)
        a.update(zip(points, values))
        selected.update(labels)
        graph.append(dict(member='A', degree=s, pivots=points, rows=labels, inverse=inv))
    b[0, 5] = {(names.index('beta5_slice'),): F(1)}
    need(not b[0, 15], 'slice beta15 must start at zero')
    for d in range(23, 0, -2):
        points = sorted((tuple(e['point']) for e in free[1] if sum(e['point']) == d), reverse=True)
        if d in (5, 15):
            points.remove((0, d))
        columns = [i for i, j in points]
        matrix = b_matrix(d, columns)
        chosen = independent_rows(matrix)
        labels = [f'J/{r}/{d+13-r}' for r in chosen]
        forcing = [jrow(a, b, r, d+13-r, ops) for r in chosen]
        values, inv = solve_constants([matrix[r] for r in chosen], forcing, ops)
        b.update(zip(points, values))
        selected.update(labels)
        graph.append(dict(member='B', degree=d, pivots=points, rows=labels, inverse=inv))
    need(sum(len(g['pivots']) for g in graph if g['member'] == 'B') == 92, 'B pivot count')
    if mode == 'full':
        b = shear(a, b, {(names.index('shear_s'),): F(1)}, ops)
    for entries, coeffs in zip(contract['coefficient_maps'], (a, b)):
        check_fixed(entries, coeffs)
    maps = {}
    for entries, coeffs in zip(contract['coefficient_maps'], (a, b)):
        for entry in entries:
            if 'variable' in entry:
                maps[entry['variable']] = coeffs[tuple(entry['point'])]
    maps[len(original)-2] = {}
    maps[len(original)-1] = {(lam,): F(1)}
    return contract, names, original, a, b, maps, graph, selected


def original_rows(contract, a, b, lam, ops):
    for entries, coeffs in zip(contract['coefficient_maps'], (a, b)):
        for entry in entries:
            if 'fixed' in entry:
                yield 'FIX/'+entry['name'], ops.add(coeffs[tuple(entry['point'])], const(rational(entry['fixed'])), -1)
    for I in range(24):
        for J in range(39-I):
            yield f'J/{I}/{J}', jrow(a, b, I, J, ops)
    for member, degree, coeffs in [('A', 15, a), ('B', 25, b)]:
        for t in range((degree-1)//5+1):
            for e in range(5*t-degree, 0):
                yield f'LIFT/{member}/{t}/{e}', liftrow(coeffs, t, e, lam, ops)
    for guard in contract['vertex_guards']:
        value = rational(guard['value'])*rational(guard['inverse'])-1
        need(not value, 'vertex guard drift')
        yield guard['label'], const(value)
    value = rational(contract['scalar']['fixed'])*rational(contract['scalar']['inverse'])-1
    need(not value, 'scalar guard drift')
    yield 'GUARD/c', const(value)


class Stream:
    def __init__(self, path, cap):
        self.file = open(path, 'xb')
        self.cap, self.used = cap, 0
        self.digest = hashlib.sha256()

    def emit(self, record):
        # Conservative pre-serialization bound covers decimal rational strings
        # and monomial indices. Generic metadata is uniformly small here.
        if 'terms' in record:
            estimate = 256+len(record.get('label', ''))
            for coefficient, monomial in record['terms']:
                estimate += 64+sum(len(v) for part in coefficient for v in part)+12*len(monomial)
            need(self.used+estimate <= self.cap, 'pre-serialization byte ceiling')
        data = B.canonical(record)
        need(self.used+len(data) <= self.cap, 'aggregate output byte cap')
        self.file.write(data)
        self.used += len(data)
        self.digest.update(data)

    def polynomial(self, record, poly):
        # Check before converting rational integers to decimal strings or
        # allocating wire lists. log10(2)<1/3, and IDs here are at most268.
        estimate = 512+len(record.get('label', ''))+len(record.get('name', ''))
        for monomial, c in poly.items():
            estimate += 100+(abs(c.numerator).bit_length()+c.denominator.bit_length())//3+12*len(monomial)
        need(self.used+estimate <= self.cap, 'pre-wire byte ceiling')
        self.emit(dict(record, terms=wire(poly)))

    def close(self):
        self.file.flush()
        os.fsync(self.file.fileno())
        self.file.close()


def authorize(path):
    authority = json.loads(Path(path).read_text())
    need(platform.system() == 'Linux' and os.getcwd() == ROOT, 'exact registered Linux cwd required')
    need('Amazon EC2' in Path('/sys/class/dmi/id/sys_vendor').read_text(), 'EC2 only')
    need(Path('/sys/class/dmi/id/board_asset_tag').read_text().strip() == INSTANCE, 'instance mismatch')
    need(Path('/proc/sys/kernel/random/boot_id').read_text().strip() == authority['boot_id'], 'boot mismatch')
    need(authority.get('root_green') is True and authority.get('construction_only') is True,
         'explicit root construction authority absent')
    need(authority.get('job') and authority.get('registration_sha256') and
         authority.get('symmetry_gate_accepted') is True and authority.get('symmetry_gate_sha256'),
         'registered job and future accepted symmetry gate required')
    need(authority['source_sha256'] == SOURCE and authority['symmetry_sha256'] == SYMMETRY, 'source pins')
    for name in ('construct.py', 'baseline.py', 'qpoly.py'):
        need(hashlib.sha256(Path(name).read_bytes()).hexdigest() == authority['code_sha256'][name], 'code pin '+name)
    caps = authority['caps']
    need(set(caps) == set(CEILINGS), 'exact caps schema')
    need(all(type(caps[k]) is int and 0 < caps[k] <= limit for k, limit in CEILINGS.items()), 'caps enlargement')
    need(time.time() < authority['expires_unix'] <= time.time()+caps['wall_seconds']+10, 'authority expiry')
    resource.setrlimit(resource.RLIMIT_AS, (caps['address_bytes'], caps['address_bytes']))
    resource.setrlimit(resource.RLIMIT_CPU, (caps['cpu_seconds'], caps['cpu_seconds']))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    resource.setrlimit(resource.RLIMIT_FSIZE, (caps['output_bytes'], caps['output_bytes']))
    signal.setitimer(signal.ITIMER_REAL, min(caps['wall_seconds'], authority['expires_unix']-time.time()))
    return authority


def main():
    need(len(sys.argv) == 2, 'one authority JSON path required; no toy-to-production switch')
    authority = authorize(sys.argv[1])
    caps = authority['caps']
    started = time.monotonic()
    ops = Arithmetic(caps, started+min(caps['wall_seconds'], authority['expires_unix']-time.time()))
    ops.production = True
    # Exclusive single result file: no overwrite/retry, including after a cap.
    stream = Stream('construction.jsonl', caps['output_bytes'])
    try:
        contract, names, original, a, b, maps, graph, selected = reconstruct(authority['mode'], ops)
        stream.emit(dict(type='header', schema='jc2.parity-construction-prep/v1',
                         status='PROVISIONAL_MU2_SUFFICIENT_SLICE_NO_IDEAL_DECISION',
                         source_sha256=SOURCE, symmetry_sha256=SYMMETRY,
                         authority_sha256=hashlib.sha256(Path(sys.argv[1]).read_bytes()).hexdigest(),
                         mode=authority['mode'], variables=names, original_variables=original,
                         field='Q', coefficient_order='dp', baseline_variables=128,
                         parity_baseline_variables=[e['name'] for entries in contract['coefficient_maps']
                                                    for e in entries if 'variable' in e and sum(e['point']) % 2]+['lambda3'],
                         original_rows=803, semantics='lambda2=0; odd A/B; whole B+s*A',
                         scalar='-5/9', target='J(A,B)+5*gamma^2/9'))
        for i in range(269):
            stream.polynomial(dict(type='map', original_index=i, name=original[i]), maps[i])
        for g in graph:
            g = dict(g)
            g['inverse'] = [[[str(c.numerator), str(c.denominator)] for c in row] for row in g['inverse']]
            stream.emit(dict(type='graph', **g))
        rows = residuals = terms = zeros = 0
        used = set()
        for label, p in original_rows(contract, a, b, names.index('lambda3'), ops):
            if label in selected or label.startswith('LIFT/A/'):
                need(not p, 'graph or A polynomiality identity failed: '+label)
            stream.polynomial(dict(type='row', original_index=rows, label=label,
                                   residual_index=residuals if p else None,
                                   justification='retained' if p else 'exact_coefficient_zero'), p)
            rows += 1
            residuals += bool(p)
            zeros += not p
            terms += len(p)
            used.update(v for monomial in p for v in monomial)
        need(rows == 803, 'complete original row count mismatch')
        stream.emit(dict(type='footer', complete=True, original_rows=rows, residuals=residuals,
                         zero_rows=zeros, residual_terms=terms, prefix_sha256=stream.digest.hexdigest(),
                         elapsed_seconds=time.monotonic()-started, stats=ops.stats,
                         map_terms=sum(map(len, maps.values())),
                         unused_residual_coordinates=[i for i in range(len(names)) if i not in used],
                         process_maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                         self_replay='same-formula; independent original-stream substitution pending'))
    except Exception as error:
        print(json.dumps(dict(status='INCOMPLETE', error=str(error), stats=ops.stats,
                              elapsed_seconds=time.monotonic()-started)), file=sys.stderr)
        raise
    finally:
        stream.close()


if __name__ == '__main__':
    main()
