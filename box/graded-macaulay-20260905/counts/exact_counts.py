#!/usr/bin/env python3
"""Exact Macaulay sizes, no polynomial reduction and no Groebner computation.

All counts use Python integers. The primary unbounded-knapsack recurrence is
checked against independent grouped binomial convolution over the entire box.
Each input polynomial term is parsed, checked nonzero, and checked bihomogeneous.
The input source lists remain read-only. Run from the repository root.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import hashlib, json, math, re, time

OUT = Path('box/graded-macaulay-20260905/counts')
OLD = Path('box/graded-moh-20260905')
AUDIT = OLD/'resume-r2/math-audit.json'
NATIVE_AUDIT = OLD/'proof/row-grading-audit.json'
PROFILE = OLD/'proof/grading-profiles.json'
TOKEN = re.compile(r'(?P<coef>[+-]?(?:\d+(?:/\d+)?)?)(?P<factors>.*)')
FACTOR = re.compile(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?$')
TERM = re.compile(r'[+-]?[^+-]+')

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def dp_individual(weights, X, Y):
    d = [[0]*(Y+1) for _ in range(X+1)]
    d[0][0] = 1
    for b,w in weights:
        assert b >= 0 and w > 0
        for x in range(b,X+1):
            for y in range(w,Y+1):
                d[x][y] += d[x-b][y-w]
    return d

def dp_grouped(weights, X, Y):
    """Convolve (1-u^b v^w)^(-multiplicity), replacing table each time."""
    d = [[0]*(Y+1) for _ in range(X+1)]
    d[0][0] = 1
    for (b,w), mult in sorted(Counter(weights).items()):
        nxt = [[0]*(Y+1) for _ in range(X+1)]
        for x in range(X+1):
            for y in range(Y+1):
                a = d[x][y]
                if not a: continue
                E = (Y-y)//w
                if b: E = min(E, (X-x)//b)
                for k in range(E+1):
                    nxt[x+k*b][y+k*w] += a*math.comb(mult+k-1,k)
        d = nxt
    return d

def polynomial_degrees(expr, weights, expected):
    expr = expr.strip()
    while expr.startswith('(') and expr.endswith(')'): expr = expr[1:-1]
    assert '(' not in expr and ')' not in expr
    support = set()
    for t in TERM.findall(expr):
        coefficient, factors = TOKEN.fullmatch(t).groups()
        if coefficient in ('','+'): coefficient = '1'
        if coefficient == '-': coefficient = '-1'
        assert Fraction(coefficient) != 0
        factors = factors.lstrip('*')
        degree = [0,0]
        powers = {}
        if factors:
            for f in factors.split('*'):
                v,e = FACTOR.fullmatch(f).groups()
                e = int(e or 1)
                assert e > 0 and v not in powers
                powers[v] = e
                for j in (0,1): degree[j] += e*weights[v][j]
        assert tuple(degree) == expected, (t,degree,expected)
        key = tuple(sorted(powers.items()))
        assert key not in support, ('uncollected repeated term',key)
        support.add(key)
    assert support, 'zero polynomial in nonzero source list'
    return len(support)

def scan_rows(path, weights, K, D, expected_sha):
    assert sha(path) == expected_sha, ('source content mismatch',path)
    rows = []
    with Path(path).open() as f:
        assert next(f).strip() == 'source_index|h_power|x_power|y_power|expr'
        for line in f:
            idx,j,b,a,expr = line.rstrip('\n').split('|')
            idx,j,b,a = map(int,(idx,j,b,a))
            assert idx == len(rows), ('source row order',idx,len(rows))
            degree = (b+1,D-a-j*K)
            assert degree[0] > 0 and degree[1] > 0
            terms = polynomial_degrees(expr, weights, degree)
            rows.append(dict(source_index=idx,h_power=j,x_power=b,y_power=a,
                             degree=list(degree),terms=terms))
    return rows

def control_tests():
    # Hand enumeration of (0,1),(1,1),(2,3) at degree (2,3): a*b^2 or c.
    assert dp_individual([(0,1),(1,1),(2,3)],2,3)[2][3] == 2
    # Two distinct zero-charge weight-one variables give y+1 monomials.
    assert dp_individual([(0,1),(0,1)],0,17)[0][17] == 18
    assert dp_grouped([(0,1),(0,1)],0,17)[0][17] == 18
    # A negative complementary component contributes zero, never Python [-1].
    def at(d,x,y): return 0 if x < 0 or y < 0 else d[x][y]
    assert at([[1]],-1,0) == 0
    try: polynomial_degrees('a+1',{'a':(1,1)},(1,1))
    except AssertionError: pass
    else: raise AssertionError('inhomogeneous mutation accepted')
    return 'PASS'

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    start = time.monotonic()
    control_tests()
    audit = json.loads(AUDIT.read_text())
    native_audit = json.loads(NATIVE_AUDIT.read_text())
    profiles = {p['stem']:p for p in json.loads(PROFILE.read_text())}
    results = []
    sources = {str(p):sha(p) for p in (AUDIT,NATIVE_AUDIT,PROFILE)}
    for fibre in sorted(audit['fibres'], key=lambda p:len(p['variables_in_order'])):
        stem = fibre['stem']
        meta_path = Path(fibre['metadata_path'])
        assert sha(meta_path) == fibre['metadata_sha256']
        sources[str(meta_path)] = sha(meta_path)
        meta = json.loads(meta_path.read_text())
        assert meta['variables'] == fibre['variables_in_order']
        closed = meta['meta']['closed_form']
        K = int(closed['K']); p = int(closed['ell'])+1
        D = meta['meta']['row']['n']+meta['meta']['row']['m']-1
        weights = {}
        for v in meta['variables']:
            if v == 'c': weights[v] = (p,D)
            else:
                prefix,b,a = v.split('_')
                i = 1 if prefix == 'h' else int(prefix[1:])
                weights[v] = (int(b),i*K-int(a))
        dims = dp_individual(weights.values(),3*p,3*D)
        independent = dp_grouped(list(weights.values()),3*p,3*D)
        assert dims == independent, ('DP crosscheck',stem)
        assert dims[p][D] == profiles[stem]['N1_component_monomials']
        # c=1 does not inherit N^2 grading. Preserve the exact finite filtered
        # section induced by (NC): projection bijects the column monomials.
        no_c = dp_individual([v for k,v in weights.items() if k!='c'],3*p,3*D)
        for N in (1,2,3):
            assert dims[N*p][N*D] == sum(no_c[k*p][k*D] for k in range(N+1))
        presentations = [("direct",fibre['source_rows'],fibre['source_sha256'])]
        for old in native_audit:
            if old['stem'] == stem and '_direct_rows' not in old['rows']:
                label = 'licensed_s4_native_control' if len(weights)==77 else 'native_hadic'
                presentations.append((label,old['rows'],old['sha256']))
        all_presentations = []
        for label,path,expected_sha in presentations:
            rows = scan_rows(path,weights,K,D,expected_sha)
            sources[path] = expected_sha
            hist = Counter(tuple(r['degree']) for r in rows)
            powers = []
            for N in (1,2,3):
                X,Y = N*p,N*D
                detail = []
                for r in rows:
                    b,w = r['degree']; a=X-b; t=Y-w
                    mult = dims[a][t] if a>=0 and t>=0 else 0
                    detail.append(dict(source_index=r['source_index'],
                        degree=r['degree'],complement=[a,t],multipliers=mult,
                        original_terms=r['terms'],matrix_nonzeros=mult*r['terms']))
                R = sum(x['multipliers'] for x in detail)
                Z = sum(x['matrix_nonzeros'] for x in detail)
                powers.append(dict(N=N,delta=[X,Y],columns=dims[X][Y],rows=R,
                    nonzero_entries=Z,eligible_nonzero_generators=sum(x['multipliers']>0 for x in detail),
                    four_byte_values_plus_eight_byte_columns_CSR_lower_bytes=12*Z+8*(R+1),
                    c_section_filtered_columns=sum(no_c[k*p][k*D] for k in range(N+1)),
                    multiplier_counts_by_source_generator=detail))
                print(len(weights),label,N,(X,Y),'columns',dims[X][Y],'rows',R,'nnz',Z,flush=True)
            all_presentations.append(dict(name=label,source=path,source_sha256=expected_sha,
                generators=len(rows),source_terms=sum(r['terms'] for r in rows),
                source_indices=list(range(len(rows))),row_coordinate_inventory=rows,
                generator_bidegree_histogram=[dict(degree=list(k),multiplicity=v) for k,v in sorted(hist.items())],
                powers=powers))
        results.append(dict(stem=stem,field='Q',parameters=len(weights),K=K,p=p,D=D,
            metadata=str(meta_path),metadata_sha256=sha(meta_path),variables=list(weights),
            variable_degrees={v:list(w) for v,w in weights.items()},
            charge_zero_variables=sum(w[0]==0 for w in weights.values()),
            independent_full_rectangle_DP_crosscheck='PASS',N1_frozen_count_crosscheck='PASS',
            eligible_variables_by_N={str(N):sum(b<=N*p and w<=N*D for b,w in weights.values()) for N in (1,2,3)},
            no_c_residual_zero_shell_counts={str(N):no_c[N*p][N*D] for N in (0,1,2,3)},
            presentations=all_presentations))
    output = dict(description='Exact ambient bigraded counts, generated rows (not rank), and sparse input nnz',
        method='unbounded variable-by-variable DP crosschecked against grouped binomial convolution',
        controls='PASS',elapsed_seconds=time.monotonic()-start,sources=sources,fibres=results)
    (OUT/'ambient-counts.json').write_text(json.dumps(output,indent=2)+'\n')
    sources[str(Path(__file__))] = sha(__file__)
    sources[str(OUT/'ambient-counts.json')] = sha(OUT/'ambient-counts.json')
    (OUT/'ambient-counts.sha256').write_text(''.join(f'{s}  {p}\n' for p,s in sorted(sources.items())))
    lines = ['| Fibre | Presentation | N | Bidegree | Columns | Rows | Nonzeros |',
             '|---|---|---:|---|---:|---:|---:|']
    for f in results:
        for presentation in f['presentations']:
            for power in presentation['powers']:
                lines.append(f"| {f['parameters']} | {presentation['name']} | {power['N']} | {tuple(power['delta'])} | {power['columns']:,} | {power['rows']:,} | {power['nonzero_entries']:,} |")
    (OUT/'ambient-counts-table.md').write_text('\n'.join(lines)+'\n')

if __name__ == '__main__': main()
