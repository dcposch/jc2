#!/usr/bin/env python3
"""Small exact slot/character checks only; never assemble a full client row."""
import ast
from fractions import Fraction
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'box/d125-minimal-receiver-client-preflight-20260906/client.py'
PIN = 'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53'

def require(condition, message):
    if not condition:
        raise ValueError(message)

def determinant(matrix):
    a = [[Fraction(v) for v in row] for row in matrix]
    result = Fraction(1)
    for i in range(len(a)):
        k = next((k for k in range(i, len(a)) if a[k][i]), None)
        if k is None:
            return Fraction(0)
        if k != i:
            a[i], a[k] = a[k], a[i]
            result = -result
        pivot = a[i][i]
        result *= pivot
        for k in range(i+1, len(a)):
            factor = a[k][i] / pivot
            for j in range(i+1, len(a)):
                a[k][j] -= factor*a[i][j]
    return result

def main():
    require(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))), 'Assert node')
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == PIN, 'source pin')
    spec = importlib.util.spec_from_file_location('symmetry_frozen_client', SOURCE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    contract = module.make_contract('unequal', 'rational')
    witness = {'source_sha256': PIN, 'lambda_weights': [-3, -2], 'members': {}}
    for index, (name, degree) in enumerate((('A', 15), ('B', 25))):
        entries = contract['coefficient_maps'][index]
        points = {tuple(e['point']) for e in entries}
        expected = {(i, j) for i in range(degree+1) for j in range(degree+1-i)
                    if 5*i-7*j <= (3 if name == 'A' else 5)
                    and (name == 'B' or i <= 2*j)}
        require(points == expected, 'independent half-plane support census')
        free = {tuple(e['point']) for e in entries if 'variable' in e}
        expected_free = {p for p in expected if p != (0, 0) and sum(p) != degree
                         and 5*p[0]-7*p[1] != (3 if name == 'A' else 5)}
        require(free == expected_free, 'complete fixed faces and origin')
        nonzero_fixed = [e for e in entries if 'fixed' in e and module.decode(e['fixed']) != module.ZERO]
        require(all((sum(e['point'])-degree) % 12 == 0 for e in nonzero_fixed), 'mu12 fixed-face character')
        levels = {}
        for s in range(1, degree):
            r = (s+4)//5
            pivot = [(i, s-i) for i in range(r)]
            require(set(pivot) <= free, 'Hermite pivot is not a free actual slot')
            matrix = [[(-1)**(s-i-t)*comb(s-i, t) for i in range(r)] for t in range(r)]
            det = determinant(matrix)
            require(abs(det) == 1, 'Hermite determinant not a unit')
            levels[str(s)] = {'pivots': pivot, 'determinant': str(det)}
        data = {'degree': degree, 'raw_count': len(points), 'free_count': len(free),
                'fixed_nonzero': nonzero_fixed, 'hermite_levels': levels, 'fixed_loci': {}}
        for n in (2, 3, 4, 6, 12):
            selected = sorted(p for p in free if (sum(p)-degree) % n == 0)
            pivots = [p for s, level in levels.items() if (int(s)-degree) % n == 0 for p in level['pivots']]
            rows = [(t, e) for t in range((degree-1)//5+1) for e in range(5*t-degree, 0)]
            possible_rows = [(t, e) for t, e in rows if (5*t-e-degree) % n == 0]
            data['fixed_loci'][str(n)] = {'free_slots': selected, 'free_count': len(selected),
                'hermite_pivots': pivots, 'pivot_count': len(pivots),
                'remaining_count': len(selected)-len(pivots), 'potential_negative_rows': possible_rows}
        witness['members'][name] = data
    mutation = sys.argv[1] if len(sys.argv) > 1 else ''
    if mutation == '--mutate-parity':
        witness['members']['A']['fixed_loci']['2']['free_slots'].append((0, 2))
    elif mutation == '--mutate-lambda-weight':
        witness['lambda_weights'][0] = -2
    elif mutation:
        raise ValueError('unknown mutation')

    # Verify actual exported candidate data, not a separate toy assertion.
    for name, data in witness['members'].items():
        degree = data['degree']
        for nstr, locus in data['fixed_loci'].items():
            n = int(nstr)
            require(all((sum(p)-degree) % n == 0 for p in locus['free_slots']), 'forbidden parity/character slot')
        # Exact coefficient-term weight identity, including BOTH parameter weights.
        for i, j in [tuple(e['point']) for e in contract['coefficient_maps'][0 if name == 'A' else 1]]:
            for t in range(j+1):
                for b in range(j-t+1):
                    for d in range(j-t-b+1):
                        exponent = 5*t+3*b+2*d-i-j
                        measured = i+j-degree+b*witness['lambda_weights'][0]+d*witness['lambda_weights'][1]
                        require(measured == 5*t-exponent-degree, 'lift row covariance')
                        if b == 0:
                            require((i+j-(5*t-exponent)) % 2 == 0, 'Hermite parity dependency')
        # For mu3, lambda3=0; no source linear term from any actual surviving slot.
        active = [tuple(e['point']) for e in contract['coefficient_maps'][0 if name == 'A' else 1]
                  if (sum(e['point'])-degree) % 3 == 0]
        for t, exponent in ((1, 0), (0, 1)):
            contributions = [(i, j, b) for i, j in active if j >= t for b in range(j-t+1)
                             if 5*t+3*b-i-j == exponent]
            require(not contributions, 'mu3 physical linear coefficient survives')
    counts = {}
    for n in (2, 3, 4, 6, 12):
        lambdas = sum(w % n == 0 for w in (-3, -2))
        counts[str(n)] = {'raw_variables': lambdas+sum(d['fixed_loci'][str(n)]['free_count'] for d in witness['members'].values()),
                         'hermite_variables': lambdas+sum(d['fixed_loci'][str(n)]['remaining_count'] for d in witness['members'].values()),
                         'lambda_variables': lambdas}
    require([witness['members'][n]['free_count'] for n in ('A', 'B')] == [71, 196], 'baseline free counts')
    require(counts['2'] == {'raw_variables': 128, 'hermite_variables': 81, 'lambda_variables': 1}, 'mu2 counts')
    require(counts['3'] == {'raw_variables': 81, 'hermite_variables': 51, 'lambda_variables': 1}, 'mu3 counts')
    require([witness['members'][n]['fixed_loci']['2']['pivot_count'] for n in ('A','B')] == [13,34], 'mu2 Hermite counts')
    require([len(witness['members'][n]['fixed_loci']['2']['potential_negative_rows']) for n in ('A','B')] == [16,39], 'mu2 lift-row counts')
    envelope = [(i, j) for i in range(24) for j in range(39-i)]
    even = [p for p in envelope if sum(p) % 2 == 0]
    require(len(envelope) == 660 and len(even) == 336, 'Jacobian parity envelope')
    # Literal conjugacy invariant: exchange is determinant -1, central inversion +1.
    det_exchange = determinant([[0, 1], [1, 0]])
    det_central = determinant([[-1, 0], [0, -1]])
    require(det_exchange == -1 and det_central == 1 and det_exchange != det_central, 'involution control')
    # Exact odd global toy: P=u, Q=u*v^4-v. Its Jacobian is 4*u*v^3-1,
    # so parity alone does not kill the origin Jacobian; it is NOT Keller.
    toy_q = {(1, 4): 1, (0, 1): -1}
    toy_j = {(i, j-1): j*c for (i, j), c in toy_q.items() if j}
    require(toy_j == {(1, 3): 4, (0, 0): -1}, 'odd global origin toy')
    witness.update(status='PASS', counts=counts, jacobian_envelope=660,
                   mu2_possible_jacobian_rows=336, assert_nodes=0,
                   involution_determinants=[str(det_central), str(det_exchange)],
                   scope='exact metadata/characters only; no full row expansion, point or runtime claim')
    print(json.dumps(witness, sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
