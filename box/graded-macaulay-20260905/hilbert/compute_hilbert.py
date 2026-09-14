#!/usr/bin/env python3
"""Original-ring bihomogeneous Macaulay pieces; no specialization and no GB.

The cutoff omits no row capable of contributing to an output component: all
variable bidegrees are in N x N_{>0}, so a generator with too high B or Y has
no complementary monomial. Full ring variables and full generator order are
retained in custody even when irrelevant by degree to a particular component.
"""
import argparse
from collections import Counter
from fractions import Fraction
from functools import reduce
import hashlib
import heapq
import json
from math import gcd, lcm
from pathlib import Path
import re
import time

from sparse_linear import IntegerRowSpace, ModularRowSpace, controls

OUT = Path(__file__).resolve().parent
PROFILES = Path('box/graded-moh-20260905/proof/grading-profiles.json')
INSTRUMENT = Path('box/graded-moh-20260905/instrument')
TERM = re.compile(r'[+-]?[^+-]+')
FACTOR = re.compile(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?\Z')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def parse_rows(profile, audit):
    names = list(profile['variables'])
    assert names == audit['variables']
    metadata = json.loads(Path(profile['meta']).read_text())
    assert names == [v for v in metadata['variables'] if v not in ('T', 'x', 'y')]
    assert profile['K'] == int(metadata['meta']['closed_form']['K'])
    assert profile['ell'] == int(metadata['meta']['closed_form']['ell'])
    assert profile['D'] == int(metadata['meta']['row']['n']) + int(metadata['meta']['row']['m']) - 1
    lookup = {v: i for i, v in enumerate(names)}
    degrees = [tuple(profile['variables'][v]) for v in names]
    for name, degree in zip(names, degrees):
        if name == 'c':
            expected = (profile['ell'] + 1, profile['D'])
        else:
            family, b, a = name.split('_')
            level = 1 if family == 'h' else int(family[1:])
            expected = (int(b), level * profile['K'] - int(a))
        assert degree == expected, (name, degree, expected)
    assert all(b >= 0 and y > 0 for b, y in degrees)
    path = Path(audit['rows_path'])
    assert sha(path) == audit['rows_sha256']
    rows = []
    terms_total = 0
    for line in path.read_text().splitlines()[1:]:
        index, h, x, y, expression = line.split('|')
        index, h, x, y = map(int, (index, h, x, y))
        expected = (x + 1, profile['D'] - y - h * profile['K'])
        assert expected[0] >= 0 and expected[1] > 0
        expression = expression.strip()
        while expression.startswith('(') and expression.endswith(')'):
            expression = expression[1:-1]
        assert '(' not in expression and ')' not in expression
        row = {}
        for term in TERM.findall(expression):
            sign = -1 if term.startswith('-') else 1
            coefficient, monomial = Fraction(sign), []
            for factor in term.lstrip('+-').split('*'):
                match = FACTOR.fullmatch(factor)
                if match:
                    name, exponent = match.groups()
                    monomial.extend([lookup[name]] * int(exponent or 1))
                else:
                    coefficient *= Fraction(factor)
            monomial = tuple(sorted(monomial))
            actual = tuple(sum(degrees[i][j] for i in monomial) for j in (0, 1))
            assert actual == expected, (index, monomial, actual, expected)
            assert monomial not in row, (index, 'duplicate term')
            assert coefficient
            row[monomial] = coefficient
            terms_total += 1
        denominator = reduce(lcm, (a.denominator for a in row.values()), 1)
        integer_row = {m: int(a * denominator) for m, a in row.items()}
        rows.append(dict(source_index=index, h_power=h, x_power=x, y_power=y,
                         degree=expected, denominator_clear=denominator,
                         terms=integer_row))
    assert len(rows) == audit['row_count']
    assert terms_total == audit['term_count']
    return names, degrees, rows, terms_total


def monomial_pieces(degrees, max_b, max_y):
    pieces = [[[] for _ in range(max_y + 1)] for _ in range(max_b + 1)]
    counts = [[0] * (max_y + 1) for _ in range(max_b + 1)]
    pieces[0][0] = [()]
    counts[0][0] = 1
    for i, (b, y) in enumerate(degrees):
        for B in range(b, max_b + 1):
            for Y in range(y, max_y + 1):
                pieces[B][Y].extend(m + (i,) for m in pieces[B - b][Y - y])
                counts[B][Y] += counts[B - b][Y - y]
    for B in range(max_b + 1):
        for Y in range(max_y + 1):
            assert len(pieces[B][Y]) == counts[B][Y]
            assert len(set(pieces[B][Y])) == counts[B][Y]
    return pieces, counts


def run(parameter_count, max_y, max_b=None, prime=1073741827, max_columns=100000):
    start = time.monotonic()
    profiles = json.loads(PROFILES.read_text())
    profile, = [p for p in profiles if p['parameters'] == parameter_count]
    audit_path = INSTRUMENT / (profile['stem'] + '_audit.json')
    audit = json.loads(audit_path.read_text())
    names, degrees, generators, terms_total = parse_rows(profile, audit)
    if max_b is None:
        max_b = 2 * profile['variables']['c'][0]
    pieces, counts = monomial_pieces(degrees, max_b, max_y)
    results = []
    for Y in range(max_y + 1):
        for B in range(max_b + 1):
            t = time.monotonic()
            column_monomials = pieces[B][Y]
            columns = len(column_monomials)
            row_count = sum(counts[B - g['degree'][0]][Y - g['degree'][1]]
                            for g in generators if g['degree'][0] <= B and g['degree'][1] <= Y)
            if columns > max_columns:
                results.append(dict(B=B, Y=Y, columns=columns, rows=row_count,
                                    status='NOT_COMPUTED_COLUMN_CAP'))
                continue
            column_lookup = {m: i for i, m in enumerate(sorted(column_monomials))}
            qspace, pspace = IntegerRowSpace(), ModularRowSpace(prime)
            source_rows, nonzeros = 0, 0
            matrix_hash = hashlib.sha256()
            for generator in generators:
                b, y = generator['degree']
                if b > B or y > Y:
                    continue
                for multiplier in pieces[B - b][Y - y]:
                    row = {column_lookup[tuple(heapq.merge(multiplier, m))]: coefficient
                           for m, coefficient in generator['terms'].items()}
                    assert len(row) == len(generator['terms'])
                    source_rows += 1
                    nonzeros += len(row)
                    matrix_hash.update(repr((generator['source_index'], multiplier,
                                             sorted(row.items()))).encode() + b'\n')
                    qspace.add(row)
                    pspace.add(row)
            assert source_rows == row_count
            assert pspace.rank <= qspace.rank <= min(columns, row_count)
            pivot_digest = hashlib.sha256(repr(sorted((k, sorted(v.items()))
                                            for k, v in qspace.pivots.items())).encode()).hexdigest()
            result = dict(B=B, Y=Y, columns=columns, rows=row_count, nonzeros=nonzeros,
                          rank_Q=qspace.rank, rank_Fp=pspace.rank, prime=prime,
                          hilbert_Q=columns-qspace.rank, I_piece_zero=(qspace.rank == 0),
                          rational_elimination_steps=qspace.elimination_steps,
                          matrix_sha256=matrix_hash.hexdigest(),
                          exact_echelon_sha256=pivot_digest,
                          elapsed_seconds=round(time.monotonic()-t, 6),
                          status='EXACT_Q')
            results.append(result)
            print(json.dumps(dict(parameters=parameter_count, **result)), flush=True)
        (OUT / f'hilbert_{parameter_count}_checkpoint.json').write_text(json.dumps(results, indent=2)+'\n')
    output = dict(stem=profile['stem'], parameters=parameter_count,
                  ring='Q['+','.join(names)+']', variable_order=names,
                  variable_bidegrees={name:list(degree) for name,degree in zip(names,degrees)},
                  original_direct_rows_path=audit['rows_path'],
                  original_direct_rows_sha256=sha(audit['rows_path']),
                  audit_path=str(audit_path), audit_sha256=sha(audit_path),
                  metadata_path=profile['meta'], metadata_sha256=sha(profile['meta']),
                  grading_profiles_sha256=sha(PROFILES),
                  total_original_generators=len(generators),
                  total_original_monomial_terms_verified=terms_total,
                  all_original_row_bidegrees_reverified=True,
                  generator_order=[dict(source_index=g['source_index'],degree=list(g['degree']),
                                        denominator_clear=g['denominator_clear']) for g in generators],
                  max_b=max_b, max_y=max_y, max_columns=max_columns,
                  controls=controls(prime), components=results,
                  total_elapsed_seconds=round(time.monotonic()-start, 3),
                  algorithm='Exact primitive integer Gaussian row elimination over Q; modular crosscheck',
                  no_specialization=True, no_groebner_completion=True)
    target = OUT / f'hilbert_{parameter_count}_B{max_b}_Y{max_y}.json'
    target.write_text(json.dumps(output, indent=2)+'\n')
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--parameters', type=int, required=True)
    parser.add_argument('--max-y', type=int, default=12)
    parser.add_argument('--max-b', type=int)
    parser.add_argument('--max-columns', type=int, default=100000)
    args = parser.parse_args()
    run(args.parameters, args.max_y, args.max_b, max_columns=args.max_columns)
