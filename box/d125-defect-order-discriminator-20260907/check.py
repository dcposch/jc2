#!/usr/bin/env python3
"""Tiny fixed-face/order discriminator; NEVER forms a full J or lift row."""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT/'box/d125-small-source-exporter-prep-20260906/baseline.py'
BASE_SHA = 'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53'


def need(condition, reason):
    if not condition:
        raise ValueError(reason)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'))+'\n').encode()


def key(monomial, weights, n):
    count = Counter(monomial)
    return tuple(sum(row[i] for i in monomial) for row in weights)+(len(monomial),)+tuple(
        -count[i] for i in range(n-1, -1, -1))


def pivots(matrix, column_order):
    """RREF only of constant matrices, at most 38 by 15."""
    need(len(matrix) <= 38 and len(column_order) <= 15, 'tiny constant matrix cap')
    a = [list(map(F, row)) for row in matrix]
    row = 0
    result = []
    for col in column_order:
        found = next((j for j in range(row, len(a)) if a[j][col]), None)
        if found is None:
            continue
        a[row], a[found] = a[found], a[row]
        scalar = a[row][col]
        a[row] = [x/scalar for x in a[row]]
        for j in range(len(a)):
            if j != row and a[j][col]:
                factor = a[j][col]
                a[j] = [x-factor*y for x, y in zip(a[j], a[row])]
        result.append(col)
        row += 1
    return result, a[:row]


def main():
    args = argparse.ArgumentParser()
    args.add_argument('--mutate', choices=['w2', 'w3', 'nonprimitive'])
    mutation = args.parse_args().mutate
    need(hashlib.sha256(BASE.read_bytes()).hexdigest() == BASE_SHA, 'baseline pin')
    spec = importlib.util.spec_from_file_location('baseline', BASE)
    base = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    contract = base.make_contract('unequal', 'rational')
    names = contract['variables']+['lambda2', 'lambda3']
    need(len(names) == 269 and contract['counts']['planned_all_rows']+105 == 803,
         'actual client metadata')
    w1, w2, w3 = [], [], []
    blocks = {}
    for member, total, entries in zip(('A', 'B'), (15, 25), contract['coefficient_maps']):
        for entry in entries:
            i, j = entry['point']
            if 'variable' not in entry:
                if i+j < total and base.decode(entry['fixed']) != base.ZERO:
                    expected = {(2, 1)} if member == 'A' else {(1, 0), (8, 5)}
                    need((i, j) in expected, 'unexpected lower fixed nonzero face')
                continue
            need(entry['variable'] == len(w1) and names[len(w1)] == entry['name'], 'index map')
            need(i+j < total, 'free outer coefficient would have zero defect')
            w1.append(total-i-j)
            w2.append(total-i-j if member == 'B' else 0)
            w3.append(i if member == 'B' else 0)
            if member == 'B':
                blocks.setdefault(i+j, []).append(i)
    w1 += [3, 2]; w2 += [0, 0]; w3 += [0, 0]
    if mutation == 'w2':
        w2 = [0]*269
    if mutation == 'w3':
        w3 = [-v for v in w3]
    weights = [w1, w2, w3]
    need(len(w1) == 269 and min(w1) > 0, 'global positive first weight')
    ids = {name: i for i, name in enumerate(names)}
    # A real, nonzero-bracket forcing term at J degree 36 (d=23).
    forcing = (ids['A_g0_p14'], ids['B_g1_p23'])
    target = (ids['B_g0_p23'],)
    need(key(target, weights, 269) > key(forcing, weights, 269), 'W2 forcing separation')
    # H has the nonzero gamma^3*pi^2 coefficient 1. A kernel relation must
    # lead at B_(3,2), not the marked free scalar B_(0,5).
    need(key((ids['B_g3_p2'],), weights, 269) >
         key((ids['B_g0_p5'],), weights, 269), 'W3 kernel marking')
    # No source pair census: only physical homogeneous degrees and whether
    # a factor is free or is a fixed coefficient-field scalar.
    degree_cases = 0
    for d in range(1, 25):
        for k in range(1, 15):
            e = d+15-k
            if not d < e <= 25:
                continue
            for afree in (False, True):
                for bfree in (False, True):
                    if bfree and e == 25:
                        continue
                    forcing_weight = ((15-k)*afree+(25-e)*bfree, (25-e)*bfree)
                    need(forcing_weight < (25-d, 25-d), 'homogeneous forcing inequality')
                    degree_cases += 1
    h = {0: F(1), 3: F(3), 6: F(3), 9: F(1)}
    if mutation == 'nonprimitive':
        h = {0: F(1)}
    witnesses = []
    for d in range(1, 25):
        q = (7*d+4)//12
        need(blocks[d] == list(range(q+1)), 'literal free block mismatch')
        matrix = [[(p*d-15*i)*h.get(p, 0) for i in range(q+1)
                   for p in [r+1-i]] for r in range(d+14)]
        need(all(r <= 23 for r, row in enumerate(matrix) if any(row)), 'J envelope missing pivot row')
        leading, reduced = pivots(matrix, list(range(q, -1, -1)))
        expected = list(range(q, 0, -1)) if d % 5 == 0 else list(range(q, -1, -1))
        need(leading == expected, 'restricted exact pivot/kernel mismatch')
        for lead, row in zip(leading, reduced):
            need(row[lead] == 1 and all(not row[j] for j in range(lead+1, q+1)),
                 'RREF leading-column direction')
        if d % 5 == 0:
            r = d//5
            kernel = [F(0)]*(q+1)
            from math import comb
            for j in range(r+1):
                kernel[3*j] = F(comb(r, j))
            need(kernel[0] == 1 and all(sum(x*y for x, y in zip(row, kernel)) == 0
                                      for row in matrix), 'actual monic H power kernel')
        witnesses.append({'d': d, 'columns': q+1, 'rank': len(leading),
                          'leading_gamma_indices': leading,
                          'kernel_scalar': f'B_g0_p{d}' if d % 5 == 0 else None})
    need(sum(row['columns'] for row in witnesses) == 196 and
         sum(row['rank'] for row in witnesses) == 192, 'all-block sums')
    descriptor = {'schema': 'jc2.d125-defect-order/v1', 'field': 'Q',
                  'variables': names, 'weight_rows': weights, 'tie_break': 'dp',
                  'comparison': 'lexicographically larger (W1,W2,W3,total,-last,...,-first)'}
    order_sha = hashlib.sha256(canonical(descriptor)).hexdigest()
    ring = 'ring R=0,('+','.join(names)+'),('+','.join(
        'a('+','.join(map(str, row))+')' for row in weights)+',dp);\n'
    print(canonical({'status': 'PASS_METADATA_AND_CONSTANT_BLOCKS_ONLY',
                     'order': descriptor, 'order_sha256': order_sha,
                     'ring_declaration': ring, 'ring_declaration_sha256': hashlib.sha256(ring.encode()).hexdigest(),
                     'degree_status_inequalities': degree_cases,
                     'blocks': witnesses, 'variables': 269, 'literal_rows_unchanged': 803,
                     'free_A': 71, 'free_B': 196, 'B_linear_leaders': 192,
                     'kernel_scalars': [f'B_g0_p{d}' for d in (5, 10, 15, 20)]}).decode(), end='')


if __name__ == '__main__':
    main()
