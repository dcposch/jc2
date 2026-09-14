#!/usr/bin/env python3
"""Second audit: total maps from full charts to finite witness algebras over Q."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib, json, re, sys

BASE = Path('box/graded-moh-20260905')
OUT = BASE / 'resume-r2'
prior = json.loads((OUT / 'math-audit.json').read_text())
profiles = {p['parameters']: p for p in json.loads((BASE / 'proof/grading-profiles.json').read_text()) if p['parameters'] in (77, 111, 129, 136)}
audit_rows = {len(p['variables_in_order']): p for p in prior['fibres']}
term_pattern = re.compile(r'[+-]?[^+-]+')
factor_pattern = re.compile(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?\Z')

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def parse_raw(s):
    s = ''.join(s.split())
    while s.startswith('(') and s.endswith(')'):
        s = s[1:-1]
    assert '(' not in s and ')' not in s
    terms = term_pattern.findall(s)
    assert ''.join(terms) == s
    for t in terms:
        coefficient = Fraction(-1 if t.startswith('-') else 1)
        exponents = Counter()
        for f in t.lstrip('+-').split('*'):
            m = factor_pattern.fullmatch(f)
            if m:
                v, e = m.groups(); exponents[v] += int(e or 1)
            else:
                assert re.fullmatch(r'\d+(?:/\d+)?', f), f
                coefficient *= Fraction(f)
        if coefficient:
            yield coefficient, exponents

results = []
for fibre in map(int, sys.argv[1:] or (111, 136)):
    curve = None; L = 0
    if fibre == 111:
        d = OUT / 'truncation/C_n18m12_M2_9_ell2_s3_V3_8_N1/x-specialization'
        custody_path = d / 'custody.json'
        custody = json.loads(custody_path.read_text())
        vs = custody['variables']; expected_weights = custody['weights']
        basis_path = d / 'basis-0.txt'
        nf_path = d / 'normalform-0.txt'
        declared = json.loads((BASE / 'truncation/C_n18m12_M2_9_ell2_s3_V3_8_N1/manifest.json').read_text())
        expected_low_indices = [row['source'] for row in declared['selected_rows']]
        prior_verifier_path = d / 'independent-verification.json'
    elif fibre == 136:
        d = OUT / 'triangular/136'
        custody_path = d / 'projection-custody.json'
        custody = json.loads(custody_path.read_text())
        vs = custody['receiver_variable_order']
        expected_weights = [custody['receiver_weights'][v] for v in vs]
        basis_path = d / 'projection-basis.txt'; nf_path = d / 'projection-nf.txt'
        expected_low_indices = custody['source_generator_indices']
        prior_verifier_path = d / 'projection-independent-replay.json'
    elif fibre == 129:
        d = OUT / 'truncation/C_n24m18_Mm15_14_ell1_s3_V1_9_N1/curve-fast'
        custody_path = d / 'custody.json'; custody = json.loads(custody_path.read_text())
        vs = custody['variables']; expected_weights = custody['weights']
        basis_path = d / 'basis-0.txt'; nf_path = d / 'normalform-0.txt'
        declared = json.loads((BASE/'truncation/C_n24m18_Mm15_14_ell1_s3_V1_9_N1/manifest.json').read_text())
        expected_low_indices = [row['source'] for row in declared['selected_rows']]
        prior_verifier_path = d / 'independent-verification.json'
        curve = 'curve_t'; L = custody['L']
        assert set(custody['assignments'][0].values()) == {1}
    elif fibre == 77:
        d = OUT / 'triangular/77/curve'
        custody_path = d / 'custody.json'; custody = json.loads(custody_path.read_text())
        vs = custody['receiver_variable_order']
        expected_weights = [custody['receiver_weights'][v] for v in vs]
        basis_path = d / 'basis.txt'; nf_path = d / 'nf.txt'
        expected_low_indices = custody['source_indices']
        prior_verifier_path = d / 'independent-replay.json'
        curve = 't'; L = custody['combined_weight_multiplier']
    else:
        raise ValueError(fibre)
    p = profiles[fibre]
    original = audit_rows[fibre]
    full_vs = original['variables_in_order']
    source = Path(original['source_rows'])
    assert sha(source) == original['source_sha256']
    assert set(vs)-({curve} if curve else set()) <= set(full_vs) and len(vs) == len(set(vs))
    bidegrees = [([0,1] if v==curve else p['variables'][v]) for v in vs]
    weights = [(w+L*b if curve else b) for b,w in bidegrees]
    assert weights == expected_weights and min(weights) > 0
    C = p['variables']['c']; cap = C[1]+L*C[0] if curve else C[0]
    positions = {v: i for i, v in enumerate(vs)}
    nv = len(vs)
    mapping = {v: (v if v in positions else f'{curve}^{p["variables"][v][1]}' if curve and p['variables'][v][0]==0 else '0') for v in full_vs}
    # This is a TOTAL map on the full original ring. Setting unused or >3
    # coordinates to zero extends the already declared low-charge receiver map.
    def mapped(s, apply_map=False):
        poly = {}
        for coefficient, powers in parse_raw(s):
            if apply_map:
                assert set(powers) <= set(full_vs)
                translated = Counter()
                for v,e in powers.items():
                    if v in positions: translated[v] += e
                    elif curve and p['variables'][v][0]==0: translated[curve] += p['variables'][v][1]*e
                    else: coefficient = 0; break
                if not coefficient: continue
                powers = translated
            else:
                assert set(powers) <= set(vs)
            mono = tuple(powers.get(v, 0) for v in vs)
            poly[mono] = poly.get(mono, Fraction(0)) + coefficient
        return {m: c for m, c in poly.items() if c}
    def degree(m):
        return sum(e*w for e,w in zip(m,weights))
    def key(m):
        return degree(m), tuple(-e for e in m[::-1])
    def leading(poly):
        return max(poly, key=key)
    def subtract_multiple(poly, divisor, powers, scalar):
        for m,c in divisor.items():
            u = tuple(a+b for a,b in zip(m,powers))
            poly[u] = poly.get(u,Fraction(0)) - scalar*c
            if not poly[u]: del poly[u]
    G = [mapped(s) for s in basis_path.read_text().strip().split(',')]
    assert all(G)
    assert all(len({degree(m) for m in g}) == 1 for g in G)
    assert all(len({tuple(sum(e*d[k] for e,d in zip(m,bidegrees)) for k in (0,1)) for m in g}) == 1 for g in G)
    leaders = [(g, leading(g), g[leading(g)]) for g in G]
    def normal_form(poly):
        working = dict(poly); remainder = {}
        while working:
            top = leading(working); coefficient = working[top]
            for g, lm, lc in leaders:
                if all(a>=b for a,b in zip(top,lm)):
                    subtract_multiple(working,g,tuple(a-b for a,b in zip(top,lm)),coefficient/lc)
                    break
            else:
                remainder[top] = coefficient; del working[top]
        return remainder
    low_indices = []; low_nonzero = 0; high_indices = []; high_degrees = []; term_count = 0
    for line in source.read_text().splitlines()[1:]:
        idx,hj,xb,ya,expr = line.split('|',4)
        idx,hj,xb,ya = map(int,(idx,hj,xb,ya)); assert hj == 0
        expected = (xb+1,p['D']-ya)
        for coefficient,powers in parse_raw(expr):
            got = tuple(sum(p['variables'][v][k]*e for v,e in powers.items()) for k in (0,1))
            assert got == expected
            term_count += 1
        image = mapped(expr,True)
        combined = expected[1]+L*expected[0] if curve else expected[0]
        assert all(degree(m)==combined for m in image)
        if expected[0] <= C[0]:
            low_indices.append(idx)
            if image: low_nonzero += 1
            assert not normal_form(image), (fibre,idx)
        else:
            high_indices.append(idx)
            high_degrees.append((combined,idx,expected[0],expected[1]))
            assert combined>cap
            assert all(degree(m)>cap for m in image)
    assert low_indices == expected_low_indices
    pairs = 0
    for (g,lm,lc),(h,ln,ld) in combinations(leaders,2):
        common = tuple(max(a,b) for a,b in zip(lm,ln))
        if degree(common)>cap: continue
        sp = {}
        subtract_multiple(sp,g,tuple(a-b for a,b in zip(common,lm)),-1/lc)
        subtract_multiple(sp,h,tuple(a-b for a,b in zip(common,ln)),1/ld)
        assert not normal_form(sp)
        pairs += 1
    c = mapped('c')
    nf = normal_form(c)
    assert nf and nf == mapped(nf_path.read_text())
    assert normal_form(mapped('1')) == mapped('1')
    test = dict(G[0])
    for m,a in c.items(): test[m] = test.get(m,Fraction(0))+a
    assert normal_form(test) == nf
    # c^2 vanishes in the explicit witness algebra by the overflow quotient.
    assert all(degree(m)>cap for m in mapped('c^2'))
    results.append(dict(
        fibre=fibre, field='Q', full_source_rows=len(low_indices)+len(high_indices),
        full_source_terms=term_count, low_source_rows=len(low_indices),
        low_nonzero_images=low_nonzero, high_source_rows=len(high_indices),
        basis_size=len(G), required_spairs_verified=pairs,
        source_variable_order=full_vs, receiver_variable_order=vs,
        total_full_ring_map=mapping, receiver_weights=weights,
        receiver_bidegrees=bidegrees, both_basis_gradings_verified=True,
        combined_L=L, target_cutoff=cap, target_bidegree=C,
        omitted_minimum_combined_degree=min(v[0] for v in high_degrees),
        omitted_minimum_row=list(min(high_degrees)),
        normalform_terms=len(nf),
        witness_algebra=f'Q[receiver]/(G + all monomials of declared positive degree>{cap})',
        all_full_source_rows_zero_in_witness=True,
        c_nonzero_in_witness=True, c_squared_zero_in_witness=True,
        negative_control_row_plus_c=True, positive_control_one_nonzero=True,
        conclusion='EXACT_Q_c_NOT_IN_FULL_I; NO_RADICAL_OR_CLASS_KILL_CLAIM',
        hashes={str(q):sha(q) for q in (source,basis_path,nf_path,custody_path,prior_verifier_path)},
    ))
previous=OUT/'nonmembership-second-audit.json'
if previous.exists():
    checked={r['fibre'] for r in results}
    results += [r for r in json.loads(previous.read_text())['fibres'] if r['fibre'] not in checked]
results.sort(key=lambda r:r['fibre'])
audit=dict(verifier_sha256=sha(Path(__file__)),fibres=results)
(OUT/'nonmembership-second-audit.json').write_text(json.dumps(audit,indent=2)+'\n')
for r in results:
    print(r['fibre'],r['full_source_rows'],r['low_source_rows'],r['low_nonzero_images'],r['basis_size'],r['required_spairs_verified'],r['conclusion'])
