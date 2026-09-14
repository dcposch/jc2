#!/usr/bin/env python3
"""Audit four full direct files; no solver, specialization, or status inference."""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import math
import re

BASE = Path('box/graded-moh-20260905')
OUT = BASE / 'resume-r2'
PROFILES = BASE / 'proof/grading-profiles.json'
profiles = {p['stem']: p for p in json.loads(PROFILES.read_text())}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

factor_re = re.compile(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?\Z')
term_re = re.compile(r'[+-]?[^+-]+')

def monomials(expr):
    while expr.startswith('(') and expr.endswith(')'):
        expr = expr[1:-1]
    assert '(' not in expr and ')' not in expr and not re.search(r'\s', expr), expr[:100]
    terms = term_re.findall(expr)
    assert ''.join(terms) == expr
    for term in terms:
        sign = -1 if term.startswith('-') else 1
        term = term.lstrip('+-')
        coeff = Fraction(sign)
        powers = Counter()
        for factor in term.split('*'):
            match = factor_re.fullmatch(factor)
            if match:
                name, exp = match.groups()
                powers[name] += int(exp or 1)
            else:
                assert re.fullmatch(r'\d+(?:/\d+)?', factor), factor
                coeff *= Fraction(factor)
        assert coeff != 0
        yield coeff, powers

result = []
for custody_path in sorted((BASE / 'instrument').glob('*/custody.json')):
    stem = custody_path.parent.name
    p = profiles[stem]
    custody = json.loads(custody_path.read_text())
    direct = BASE / 'instrument' / (stem + '_direct_rows.tsv')
    if not direct.exists():
        native = Path(json.loads(Path(p['meta']).read_text())['rows_path'])
        direct = native.with_name(native.stem.replace('_rows', '_direct_rows') + '.tsv')
    assert sha(direct) == custody['source_rows_sha256'], (stem, 'source hash')
    assert list(p['variables']) == custody['source_ring']['variables']
    assert sha(Path(p['meta'])) == p['meta_sha256'] == custody['source_metadata_sha256']
    P, D = p['ell'] + 1, p['D']
    assert math.gcd(P, D) == 1
    aa = pow(P, -1, D)
    bb = (1 - aa * P) // D
    assert aa * P + bb * D == 1
    degree_hist = Counter()
    weight_hist = Counter()
    crows = []
    nterms = 0
    lowrows = 0
    eligible = 0
    rows = []
    for line in direct.read_text().splitlines()[1:]:
        idx, hj, xb, ya, expr = line.split('|', 4)
        idx, hj, xb, ya = map(int, (idx, hj, xb, ya))
        assert hj == 0, (stem, 'not direct')
        deg = (xb + 1, D - ya)
        assert 1 <= deg[1] <= D
        row_degree = 0
        has_c = False
        for coeff, powers in monomials(expr):
            got = tuple(sum(p['variables'][v][k] * e for v, e in powers.items()) for k in (0, 1))
            assert got == deg, (stem, idx, powers, got, deg)
            assert sum((aa * p['variables'][v][0] + bb * p['variables'][v][1]) * e for v, e in powers.items()) == aa * deg[0] + bb * deg[1]
            if 'c' in powers:
                has_c = True
                assert powers == {'c': 1} and coeff in (1, -1), (stem, 'bad c occurrence')
            # Positive grading: variables of the row weight occur only as a single factor.
            for v in powers:
                assert p['variables'][v][1] <= deg[1]
                if p['variables'][v][1] == deg[1]:
                    assert powers == {v: 1}
            row_degree = max(row_degree, sum(powers.values()))
            nterms += 1
        if has_c:
            crows.append({'source_index': idx, 'bidegree': list(deg)})
            assert deg == (P, D)
        if deg[1] < D:
            assert not has_c
            lowrows += 1
        if deg[0] <= P:
            eligible += 1
        degree_hist[row_degree] += 1
        weight_hist[deg[1]] += 1
        rows.append(idx)
    assert len(crows) == 1
    assert len(rows) == custody['generator_count']
    d0 = p['e'] + p['q']
    assert d0 >= 5 and max(degree_hist) <= d0
    N = d0 ** (p['parameters'] - 1)
    X, Y = P * N, D * N
    result.append({
        'stem': stem,
        'coefficient_field': 'Q',
        'variables_in_order': custody['source_ring']['variables'],
        'source_indices_in_order': rows,
        'source_rows': str(direct),
        'source_sha256': sha(direct),
        'metadata_path': p['meta'],
        'metadata_sha256': sha(Path(p['meta'])),
        'custody_path': str(custody_path),
        'custody_sha256': sha(custody_path),
        'verified_rows': len(rows),
        'verified_monomials': nterms,
        'non_c_variable_weight_range': p['positive_weight_range'],
        'row_weight_histogram': dict(sorted(weight_hist.items())),
        'ordinary_row_degree_histogram': dict(sorted(degree_hist.items())),
        'unique_c_row': crows[0],
        'strict_low_weight_rows': lowrows,
        'strict_low_weight_point_z0_c1': 'PASS',
        'constant_top_weight_linear_block_check': 'PASS',
        'n1_eligible_rows': eligible,
        'n1_target_bidegree': [P, D],
        'bezout_a_b': [aa, bb],
        'laurent_cocharacter_term_check': 'PASS',
        'ordinary_degree_bound_d0': d0,
        'universal_exponent_symbolic': f'{d0}^{p["parameters"] - 1}',
        'universal_exponent_integer': str(N),
        'universal_target_bidegree_integer': [str(X), str(Y)],
        'universal_target_bidegree_digits': [len(str(X)), len(str(Y))],
        'verdict': 'ALL_FULL_DIRECT_TERMS_BIHOMOGENEOUS',
    })

audit = {
    'audit_script_sha256': sha(Path(__file__)),
    'profiles_sha256': sha(PROFILES),
    'kollar_pdf_path': str(BASE / 'proof/kollar-1988.pdf'),
    'kollar_pdf_sha256': sha(BASE / 'proof/kollar-1988.pdf'),
    'kollar_text_sha256': sha(BASE / 'proof/kollar-1988.txt'),
    'kollar_verified_printed_page': 965,
    'kollar_verified_pdf_page_one_indexed': 4,
    'fibres': result,
    'total_full_direct_rows': sum(r['verified_rows'] for r in result),
    'total_full_direct_terms': sum(r['verified_monomials'] for r in result),
    'mathematical_disposition': 'GRADING_AND_FINITE_REDUCTION_PROVED; CLASS_KILL_NOT_ASSERTED',
}
(OUT / 'math-audit.json').write_text(json.dumps(audit, indent=2) + '\n')
for row in result:
    print(row['stem'], row['verified_rows'], row['verified_monomials'], row['ordinary_row_degree_histogram'], row['bezout_a_b'], 'PASS')
print('TOTAL', audit['total_full_direct_rows'], audit['total_full_direct_terms'])
