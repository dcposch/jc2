#!/usr/bin/env python3
"""Independent exact cotangent-rank and triangular derivative audit."""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import re

ROOT = Path('/home/ubuntu/jc2')
OUT = ROOT / 'box/graded-macaulay-20260905/audit'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(expr):
    s = ''.join(expr.split())
    ts = re.findall(r'[+-]?[^+-]+', s)
    assert ''.join(ts) == s
    ans = {}
    for t in ts:
        coeff = Fraction(-1 if t.startswith('-') else 1)
        exps = Counter()
        for f in t.lstrip('+-').split('*'):
            m = re.fullmatch(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?', f)
            if m:
                exps[m[1]] += int(m[2] or 1)
            else:
                assert re.fullmatch(r'\d+(?:/\d+)?', f), f
                coeff *= Fraction(f)
        mon = tuple(sorted(exps.items()))
        ans[mon] = ans.get(mon, Fraction(0)) + coeff
    return {m:c for m,c in ans.items() if c}

def add_scaled(row, other, scalar):
    for v, q in other.items():
        row[v] = row.get(v, Fraction(0)) + scalar*q
        if not row[v]:
            del row[v]

def exact_rank(rows, positions):
    basis = {}
    source = {}
    for row_index, rr in rows:
        r = dict(rr)
        while r:
            lead = min(r, key=positions.__getitem__)
            if lead not in basis:
                q = r[lead]
                basis[lead] = {v:c/q for v,c in r.items()}
                source[lead] = row_index
                break
            add_scaled(r, basis[lead], -r[lead])
    return len(basis), basis, source

def serialized(vector):
    return {v: str(q) for v,q in vector.items()}

all_results = []
for n in (77, 111, 129, 136):
    reduced_path = ROOT / f'box/graded-macaulay-20260905/reduced/{n}/reduced-counts.json'
    red = json.loads(reduced_path.read_text())
    source_path = Path(red['source'])
    if not source_path.is_absolute():
        source_path = ROOT / source_path
    assert sha(source_path) == red['source_sha256']
    vs = red['source_variables']
    positions = {v:i for i,v in enumerate(vs)}
    W = red['weights']
    rows = {}
    linear_rows = {}
    generator_degrees = {}
    all_constant_terms_zero = True
    for position, line in enumerate(source_path.read_text().splitlines()[1:]):
        index, hj, xb, ya, expr = line.split('|', 4)
        index, hj, xb, ya = map(int, (index, hj, xb, ya))
        assert index == position and hj == 0
        rows[index] = parse(expr)
        assert () not in rows[index]
        assert all(v in positions for m in rows[index] for v,e in m)
        degree = (xb+1, W['c'][1]-ya)
        assert all(tuple(sum(W[v][k]*e for v,e in m) for k in (0,1)) == degree for m in rows[index])
        generator_degrees[index] = degree
        linear_rows[index] = {m[0][0]:q for m,q in rows[index].items() if len(m)==1 and m[0][1]==1}
    rank, basis, rank_sources = exact_rank(linear_rows.items(), positions)
    pivots = red['pivots']
    pivot_variables = [p['variable'] for p in pivots]
    assert len(set(pivot_variables)) == len(pivot_variables)
    assert set(pivot_variables) == {v for v in vs if v.startswith('A') and W[v][0]>0}
    remaining = [v for v in vs if v not in pivot_variables]
    assert remaining == red['remaining_variables']
    final_vs = [v for v in remaining if v != 'c']
    # The triangular map fixes the origin, so its derivative is obtained from
    # the original linear terms alone, without expanding nonlinear expressions.
    derivatives = {v:{v:Fraction(1)} for v in remaining}
    pivot_checks = []
    for p in pivots:
        v = p['variable']
        index = p['index']
        q = Fraction(p['coefficient'])
        poly = rows[index]
        assert [(m,c) for m,c in poly.items() if any(z==v for z,e in m)] == [(((v,1),),q)]
        other_variables = {z for m in poly for z,e in m if z!=v}
        assert other_variables <= derivatives.keys()
        derivative = {}
        for z, c in linear_rows[index].items():
            if z != v:
                add_scaled(derivative, derivatives[z], -c/q)
        derivatives[v] = derivative
        check = {}
        for z,c in linear_rows[index].items():
            add_scaled(check, derivatives[z], c)
        assert not check
        pivot_checks.append({'source_index':index, 'variable':v, 'linear_image':serialized(derivative), 'origin_fixed':True})
    # There is exactly one c-containing monomial in all source rows.
    c_terms = [(i,m,q) for i,g in rows.items() for m,q in g.items() if any(v=='c' for v,e in m)]
    assert len(c_terms) == 1
    target_index, cmon, cq = c_terms[0]
    assert cmon == (('c',1),)
    assert target_index == red['target_source_index']
    cderivative = {}
    for v,q in linear_rows[target_index].items():
        if v != 'c':
            add_scaled(cderivative, derivatives[v], -q/cq)
    assert 'c' not in cderivative
    derivatives['c'] = cderivative
    # Replace any residual c-linear term in prior images by its final image.
    for v,d in derivatives.items():
        if v != 'c' and 'c' in d:
            coeff = d.pop('c')
            add_scaled(d, cderivative, coeff)
    assert not cderivative
    residual_nonzero = {}
    for i, rr in linear_rows.items():
        image = {}
        for v,q in rr.items():
            add_scaled(image, derivatives[v], q)
        if image:
            residual_nonzero[i] = serialized(image)
    assert not residual_nonzero
    assert all(set(d)<=set(final_vs) for d in derivatives.values())
    assert all(derivatives[v]=={v:Fraction(1)} for v in final_vs)
    assert rank == len(pivots)+1
    assert n-rank == len(final_vs)
    # N-independent minimality: tangent dimension at the origin is a lower
    # bound for the number of generators in every Q-polynomial presentation.
    result = {
        'fibre':n, 'source_rows':len(rows), 'source_variables':vs,
        'source_sha256':sha(source_path), 'reduced_counts_sha256':sha(reduced_path),
        'all_source_constants_zero':True,
        'exact_constant_linear_rank':rank,
        'exact_echelon_pivot_columns':list(basis),
        'exact_echelon_pivot_source_rows':rank_sources,
        'exact_echelon_basis':{v:serialized(row) for v,row in basis.items()},
        'A_positive_pivots':len(pivots), 'c_pivot_source_index':target_index,
        'c_pivot_coefficient':str(cq), 'target_has_no_other_linear_terms':linear_rows[target_index]=={'c':cq},
        'triangular_constant_unit_dependencies_verified':True,
        'origin_preserved':True, 'pivot_derivative_checks':pivot_checks,
        'source_linear_derivative_images':{v:serialized(derivatives[v]) for v in vs},
        'every_original_row_linear_image_zero_after_A_and_c_elimination':True,
        'remaining_variable_order':final_vs,
        'cotangent_dimension_at_origin':n-rank,
        'achieved_polynomial_presentation_variables':len(final_vs),
        'minimality':'Every Q-algebra polynomial presentation needs at least dim_Q(m/m^2) variables. The full rational-unit triangular quotient followed by c elimination achieves that number.',
        'scope':'Minimum number of polynomial generators for the full affine Q-algebra. Does not assert minimum variables after localization or on c=1 section; does not compute Krull dimension or target Hilbert function.',
    }
    all_results.append(result)
    print(n,'exact linear rank',rank,'minimal polynomial presentation variables',n-rank)

out = {'verifier_sha256':sha(Path(__file__)), 'fibres':all_results}
(OUT / 'minimality.json').write_text(json.dumps(out,indent=2)+'\n')
