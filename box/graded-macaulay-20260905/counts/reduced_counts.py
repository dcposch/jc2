#!/usr/bin/env python3
"""Independent ambient counts after the frozen rational unit pivots.

This audits the declared remaining variable inventory and counts its monomials;
the frozen rational replay, not this counting script, establishes the ring map.
For 111/129 the 42/37 known pivots come from N=1 selected source generators.
They remain valid global eliminations but need not be a maximal full-ideal set.
"""
from pathlib import Path
import json
from exact_counts import dp_individual, dp_grouped, sha

OUT = Path('box/graded-macaulay-20260905/counts')
PROFILES = Path('box/graded-moh-20260905/proof/grading-profiles.json')
profiles = json.loads(PROFILES.read_text())
results = []
sources = {str(PROFILES):sha(PROFILES)}
for n in (77,111,129,136):
    f = next(p for p in profiles if p['parameters']==n)
    if n in (77,136):
        path = Path(f'box/graded-moh-20260905/resume-r2/triangular/{n}/triangular-dag-custody.json')
        j = json.loads(path.read_text())
        remaining = j['remaining_free_coordinates']
        eliminated = [x['pivot'] for x in j['pivot_dag']]
    else:
        path = Path('box/graded-moh-20260905/truncation')/(f['stem']+'_N1')/'fast-eliminated-variables.txt'
        eliminated = [s.strip() for s in path.read_text().strip().split(',')]
        remaining = [v for v in f['variables'] if v not in eliminated]
    sources[str(path)] = sha(path)
    assert len(eliminated) == len(set(eliminated))
    assert set(remaining).isdisjoint(eliminated)
    assert set(remaining)|set(eliminated) == set(f['variables'])
    c_eliminated = 'c' in eliminated
    weights = {v:tuple(f['variables'][v]) for v in remaining}
    p,D = f['ell']+1,f['D']
    assert all(f['variables'][v][0]>0 for v in eliminated)
    a = dp_individual(weights.values(),3*p,3*D)
    b = dp_grouped(list(weights.values()),3*p,3*D)
    assert a == b
    no_c = dp_individual([w for v,w in weights.items() if v!='c'],3*p,3*D)
    with_c = dp_individual([w for v,w in weights.items() if v!='c']+[(p,D)],3*p,3*D)
    powers = []
    for N in (1,2,3):
        assert with_c[N*p][N*D] == sum(no_c[k*p][k*D] for k in range(N+1))
        assert a[N*p][N*D] == (no_c if c_eliminated else with_c)[N*p][N*D]
        powers.append(dict(N=N,delta=[N*p,N*D],columns=a[N*p][N*D],
            eligible_variables=sum(w[0]<=N*p for w in weights.values()),
            columns_if_c_pivot_held_out=with_c[N*p][N*D],
            c_section_filtered_columns_before_c_pivot=with_c[N*p][N*D],
            columns_after_eliminating_c_through_F_minus_c=no_c[N*p][N*D]))
    if n in (77,136):
        assert powers[0]['columns'] == j['N1']['ambient_target_component_after_pivot_elimination']
    result = dict(fibre=n,source=str(path),source_sha256=sha(path),eliminated=eliminated,
        remaining=remaining,weights=weights,pivots=len(eliminated),reduced_full_variables=len(remaining),
        c_eliminated=c_eliminated,target='phi(c)^N' if c_eliminated else 'c^N',
        no_charge_zero_pivots=True,independent_DP_crosscheck='PASS',powers=powers)
    results.append(result)
    print(n,len(eliminated),len(remaining),powers)
output = OUT/'reduced-ambient-counts.json'
output.write_text(json.dumps(results,indent=2)+'\n')
sources[str(output)] = sha(output)
sources[str(Path(__file__))] = sha(__file__)
sources[str(OUT/'exact_counts.py')] = sha(OUT/'exact_counts.py')
(OUT/'reduced-ambient-counts.sha256').write_text(''.join(f'{s}  {p}\n' for p,s in sorted(sources.items())))
