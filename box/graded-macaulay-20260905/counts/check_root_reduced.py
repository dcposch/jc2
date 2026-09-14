#!/usr/bin/env python3
"""Independent arithmetic audit of the newly completed reduced presentations.

Checks source coordinate custody, row partitions and all contribution counts.
The exact-flint zero identities are consumed, not re-expanded in this check.
"""
from pathlib import Path
from fractions import Fraction
import json
from exact_counts import sha, dp_individual, dp_grouped

OUT = Path('box/graded-macaulay-20260905/counts')
AMBIENT = OUT/'ambient-counts.json'
ROOT = Path('box/graded-macaulay-20260905/reduced')
ambient = json.loads(AMBIENT.read_text())
results = []
for n in (77,111,129,136):
    path = ROOT/str(n)/'reduced-counts.json'
    j = json.loads(path.read_text())
    f = next(f for f in ambient['fibres'] if f['parameters']==n)
    full = next(p for p in f['presentations'] if p['name']=='direct')
    assert sha(j['source']) == j['source_sha256'] == full['source_sha256']
    assert j['weights'] == f['variable_degrees']
    assert j['source_variables'] == f['variables']
    assert j['source_row_count'] == full['generators']
    p,D,K = f['p'],f['D'],f['K']
    source_degrees = {}
    with Path(j['source']).open() as source:
        assert next(source).strip() == 'source_index|h_power|x_power|y_power|expr'
        for line in source:
            i,h,b,a,expr = line.rstrip('\n').split('|')
            i,h,b,a = map(int,(i,h,b,a))
            degree = [b+1,D-a-h*K]
            assert full['row_coordinate_inventory'][i]['degree'] == degree
            source_degrees[i] = degree
    pivot_indices = {r['index'] for r in j['pivots']}
    pivot_variables = {r['variable'] for r in j['pivots']}
    extra_zero = set(j['additional_zero_rows_exact_flint'])
    nonzero = {int(k) for k in j['nonzero_evaluations']}
    assert len(pivot_indices) == len(pivot_variables) == j['pivot_count']
    assert j['pivot_count'] == {77:27,111:57,129:57,136:71}[n]
    assert not (pivot_indices&extra_zero or pivot_indices&nonzero or extra_zero&nonzero)
    assert pivot_indices|extra_zero|nonzero == set(source_degrees)
    assert len(nonzero) == j['nonzero_reduced_generator_count']
    for r in j['pivots']:
        assert r['degree'] == source_degrees[r['index']] == j['weights'][r['variable']]
        assert r['degree'][0] > 0
        coefficient = Fraction(r['coefficient'])
        assert coefficient.numerator % j['nonzero_evaluation_prime']
        assert coefficient.denominator % j['nonzero_evaluation_prime']
    assert all(any(v % j['nonzero_evaluation_prime'] for v in values)
               for values in j['nonzero_evaluations'].values())
    remaining = j['remaining_variables']
    assert 'c' in remaining and 'c' not in pivot_variables
    assert [v for v in f['variables'] if v not in pivot_variables] == remaining
    weights = [tuple(j['weights'][v]) for v in remaining]
    cfree_weights = [tuple(j['weights'][v]) for v in remaining if v!='c']
    d = dp_individual(weights,3*p,3*D)
    dc = dp_individual(cfree_weights,3*p,3*D)
    assert d == dp_grouped(weights,3*p,3*D)
    assert dc == dp_grouped(cfree_weights,3*p,3*D)
    for x in range(3*p+1):
        for y in range(3*D+1):
            predecessor = d[x-p][y-D] if x>=p and y>=D else 0
            assert dc[x][y] == d[x][y]-predecessor
    target = j['target_source_index']
    assert target in nonzero and source_degrees[target] == [p,D]
    def contribution(table,degree,X,Y):
        a,b = X-degree[0],Y-degree[1]
        return table[a][b] if a>=0 and b>=0 else 0
    tests = []
    contributions_checked = 0
    for test in j['tests']:
        N = test['N'];X,Y = N*p,N*D
        assert test['degree'] == [X,Y]
        assert test['columns'] == d[X][Y]
        assert test['c_eliminated_columns'] == dc[X][Y]
        totals = {}
        for key,table,indices in [('contributions',d,nonzero),
                                 ('c_eliminated_contributions',dc,nonzero-{target})]:
            claimed = {r['source_index']:r for r in test[key]}
            expected_indices = {i for i in indices if source_degrees[i][0]<=X and source_degrees[i][1]<=Y}
            assert set(claimed) == expected_indices
            assert len(claimed) == len(test[key])
            total = 0
            for i in sorted(indices):
                count = contribution(table,source_degrees[i],X,Y)
                total += count
                if i in claimed:
                    assert claimed[i]['degree'] == source_degrees[i]
                    assert claimed[i]['rows'] == count
                    contributions_checked += 1
            totals[key] = total
        assert test['rows'] == totals['contributions']
        assert test['c_eliminated_rows'] == totals['c_eliminated_contributions']
        tests.append(dict(N=N,degree=[X,Y],columns=d[X][Y],rows=totals['contributions'],
            cfree_columns=dc[X][Y],cfree_rows=totals['c_eliminated_contributions']))
    results.append(dict(fibre=n,input=str(path),input_sha256=sha(path),
        source_sha256=j['source_sha256'],positive_charge_pivots=len(pivot_indices),
        exact_extra_zero_rows=len(extra_zero),nonzero_rows=len(nonzero),
        ordered_variable_partition='PASS',source_degree_partition='PASS',
        independent_DPs_entire_rectangle='PASS',cfree_difference_entire_rectangle='PASS',
        checked_per_source_contributions=contributions_checked,tests=tests))
result = dict(verdict='PASS',scope='Independent dimension and per-source multiplier arithmetic; existing exact zero expansions consumed without re-expansion',
    driver_sha256=sha(__file__),ambient_count_input_sha256=sha(AMBIENT),fibres=results)
(OUT/'independent-reduced-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
