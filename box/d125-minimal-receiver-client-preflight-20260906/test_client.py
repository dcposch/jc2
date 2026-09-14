#!/usr/bin/env python3
"""Tiny exact arithmetic / changed-object controls, never a full receiver J.

Entire process capped at 30 wall seconds, 25 CPU seconds, 512 MiB address space.
Outputs are exclusively created in the requested NEW evidence filename.
"""
import argparse
import copy
import hashlib
import json
import resource
import signal
import time
from pathlib import Path
import client as C

resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
signal.alarm(30)
started = time.monotonic()
checks = []


def require(condition, name):
    if not condition:
        raise ValueError(name)
    checks.append(name)


def rejects(function, name):
    try:
        function()
    except (ValueError, RuntimeError, ZeroDivisionError):
        checks.append(name)
        return
    raise ValueError('mutation accepted: '+name)


def independent_pair_rows(left, right):
    rows = {}
    for (i, j), a in left.items():
        for (k, l), b in right.items():
            coefficient = i*l-j*k
            if not coefficient:
                continue
            point = (i+k-1, j+l-1)
            row = rows.setdefault(point, {})
            for am, av in a.items():
                for bm, bv in b.items():
                    key = tuple(sorted(am+bm))
                    row[key] = row.get(key, C.ZERO)+coefficient*av*bv
    return {point: {m: v for m, v in row.items() if v != C.ZERO}
            for point, row in rows.items()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--mutate', choices=('target', 'face'))
    args = parser.parse_args()
    rho = C.RHO
    require(rho*rho == 3*rho-C.ONE, 'golden minimal polynomial exactly')
    require(rho*(3-rho) == C.ONE, 'golden inverse and both embeddings')
    require((3-rho)**2-3*(3-rho)+C.ONE == C.ZERO, 'conjugate retained')
    require(C.F(2, 3)*C.F(2, 3).inverse() == C.ONE, 'general field inverse')
    rejects(lambda: C.ZERO.inverse(), 'zero-field inverse rejected')
    require(rho*rho != 3*rho+C.ONE, 'wrong minimal polynomial changes object')
    contracts = []
    expected = {'unequal': ([83, 215], [12, 19], 267, 267, 698),
                'common_3': ([94, 241], [17, 27], 291, 293, 711),
                'common_4': ([115, 296], [17, 27], 367, 369, 711)}
    for case in C.VERTICES:
        for branch in ('rational', 'golden'):
            contract = C.make_contract(case, branch)
            C.validate_contract(contract)
            count = contract['counts']
            got = (count['raw'], count['fixed'], count['free'],
                   count['variables'], count['planned_all_rows'])
            require(got == expected[case], f'{case}/{branch} closed lattice and full-face counts')
            require(all(C.decode(g['value'])*C.decode(g['inverse']) == C.ONE
                        for g in contract['vertex_guards']), f'{case}/{branch} all six guards')
            # Every full face lattice slot, including prescribed zero, is fixed.
            for member, degree in zip(contract['coefficient_maps'], (15, 25)):
                require(all('fixed' in e for e in member if sum(e['point']) == degree),
                        f'{case}/{branch}/{degree} entire outer face')
            contracts.append(contract)
    counts = {c['case']+'/'+c['branch']: c['counts'] for c in contracts}
    require(sum(39-i for i in range(24)) == 660, 'complete a priori ordinary J envelope')
    base = contracts[0]
    bad = copy.deepcopy(base)
    # Rational outer face contains prescribed zero; turning it free is forbidden.
    zero = next(e for e in bad['coefficient_maps'][0]
                if 'outer' in e.get('reasons', []) and e['fixed'] == C.ZERO.wire())
    zero.pop('fixed')
    zero['variable'] = 999
    rejects(lambda: C.validate_contract(bad), 'prescribed zero face coefficient cannot become free')
    bad_face = copy.deepcopy(bad)
    bad = copy.deepcopy(base)
    bad['coefficient_maps'][0].pop(next(n for n, e in enumerate(bad['coefficient_maps'][0])
                                     if 'variable' in e))
    rejects(lambda: C.validate_contract(bad), 'free lattice coefficient deletion rejected')
    bad = copy.deepcopy(base)
    bad['vertex_guards'][0]['value'] = C.ZERO.wire()
    rejects(lambda: C.validate_contract(bad), 'zero nonorigin vertex rejected')
    bad = copy.deepcopy(base)
    bad['scalar']['fixed'] = C.ONE.wire()
    rejects(lambda: C.validate_contract(bad), 'unlicensed second c=1 gauge rejected')
    # Check normalization at a genuine nonzero scale in both embeddings.
    tau = C.F(2)
    for kappa in (C.ONE, rho, 3-rho):
        a = tau**12
        d = C.F(C.Q(5, 9))*a*a*kappa**-1
        e = C.F(C.Q(5, 3))*a*kappa**2
        c = -C.F(C.Q(5, 9))*a**3*kappa**-1
        require(a*tau**-12 == C.ONE and d*tau**-24 == C.F(C.Q(5, 9))*kappa**-1
                and e*tau**-12 == C.F(C.Q(5, 3))*kappa**2
                and c*tau**-36 == -C.F(C.Q(5, 9))*kappa**-1,
                'unequal exact one-scale normalization '+str(kappa))
        # The literal three-term inner bracket must have the stated target.
        af = {(2, 1): {(): C.ONE}, (9, 6): {(): kappa**3}}
        bf = {(1, 0): {(): C.F(C.Q(5, 9))*kappa**-1},
              (8, 5): {(): C.F(C.Q(5, 3))*kappa**2}, (15, 10): {(): kappa**5}}
        r = independent_pair_rows(af, bf)
        r = {p: v for p, v in r.items() if v}
        require(r == {(2, 0): {(): -C.F(C.Q(5, 9))*kappa**-1}},
                'literal unequal inner face J and sign '+str(kappa))
    require(tau**2*tau**-2 == C.ONE and tau*tau**-1 == C.ONE,
            'common mu normalization exponents')
    # Three-by-three TOY only. A constant coefficient variable is retained.
    left = {(0, 0): {(2,): C.ONE}, (1, 0): {(0,): C.ONE}, (0, 2): {(): rho}}
    right = {(2, 1): {(1,): C.ONE}, (1, 0): {(): rho}, (0, 1): {(): C.ONE}}
    outputs = [(i, j) for i in range(4) for j in range(3)]
    scalar = {(3,): C.ONE}
    variables = ['a', 'b', 'Aconstant_unused', 'c']
    pair_rows = independent_pair_rows(left, right)
    require(all(C.coefficient_row(left, right, point) == pair_rows.get(point, {})
                for point in outputs), 'forced-index kernel versus independent tiny pair expansion')
    stream = C.toy_stream(left, right, outputs, scalar, variables)
    C.verify_toy_stream(stream, left, right, outputs, scalar, variables)
    require(True, 'strict whole toy stream replay')
    records = [json.loads(line) for line in stream.splitlines()]
    require(records[-1]['rows'] == 12 and records[-1]['zero_rows'] > 0,
            'zero rows retained in complete footer')
    require(all(2 not in term[1] for record in records[1:-1] for term in record['terms'])
            and 'Aconstant_unused' in records[0]['variables'], 'unused constant not silently deleted')
    wrong = C.toy_stream(left, right, outputs, {(3,): -C.ONE}, variables)
    rejects(lambda: C.verify_toy_stream(wrong, left, right, outputs, scalar, variables),
            'changed actual target sign rejected')
    rejects(lambda: C.verify_toy_stream(b'\n'.join(stream.splitlines()[:-1])+b'\n',
                                       left, right, outputs, scalar, variables),
            'missing footer rejected')
    rejects(lambda: C.toy_stream(left, right, [(0, 0)], scalar, variables),
            'missing target obligation rejected')
    rejects(lambda: C.coefficient_row({(i, 0): {} for i in range(9)},
                                      {(i, 0): {} for i in range(9)}, (0, 0)),
            'production-sized kernel attempt rejected')
    rejects(C.production_export, 'production export unavailable')
    # Nonzero-J monomial fixture: exact target gives all zero residual rows.
    fixture = C.toy_stream({(1, 0): {(): C.ONE}}, {(2, 1): {(): C.ONE}},
                           [(0, 0), (1, 0), (2, 0), (0, 1)], {(): C.ONE}, [])
    require(json.loads(fixture.splitlines()[-1])['zero_rows'] == 4,
            'same-ring positive target control')
    # Optional changed-object process controls must fail even under -O.
    if args.mutate == 'target':
        C.verify_toy_stream(wrong, left, right, outputs, scalar, variables)
    if args.mutate == 'face':
        C.validate_contract(bad_face)
    result = {'status': 'PASS', 'checks': checks, 'check_count': len(checks),
              'counts': counts, 'contract_sha256': [hashlib.sha256(C.canonical(c)).hexdigest()
                                                   for c in contracts],
              'toy_stream_sha256': hashlib.sha256(stream).hexdigest(),
              'elapsed_seconds': time.monotonic()-started,
              'maxrss_KiB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              'limits': {'wall_seconds': 30, 'cpu_seconds': 25, 'AS_bytes': 512*1024**2},
              'production_J_expanded': False, 'production_pair_census': False}
    with Path(args.output).open('x') as out:
        json.dump(result, out, sort_keys=True, indent=2)
        out.write('\n')
    print(json.dumps({'status': 'PASS', 'checks': len(checks), 'counts': counts,
                      'elapsed_seconds': result['elapsed_seconds'], 'maxrss_KiB': result['maxrss_KiB']}))


if __name__ == '__main__':
    main()
