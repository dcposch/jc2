#!/usr/bin/env python3
"""Count saved witness-algebra Hilbert pieces; never identify them with R/I."""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import re

ROOT = Path('/home/ubuntu/jc2')
OLD = ROOT / 'box/graded-moh-20260905'
OUT = ROOT / 'box/graded-macaulay-20260905/audit'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

profiles_path = OLD / 'proof/grading-profiles.json'
prior_path = OLD / 'resume-r2/nonmembership-second-audit.json'
profiles = {p['parameters']: p for p in json.loads(profiles_path.read_text())}
prior = json.loads(prior_path.read_text())['fibres']

def parse(expr, positions):
    ans = {}
    for term in re.findall(r'[+-]?[^+-]+', ''.join(expr.split())):
        coeff = Fraction(-1 if term.startswith('-') else 1)
        powers = [0] * len(positions)
        for factor in term.lstrip('+-').split('*'):
            m = re.fullmatch(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?', factor)
            if m:
                powers[positions[m[1]]] += int(m[2] or 1)
            else:
                coeff *= Fraction(factor)
        mon = tuple(powers)
        ans[mon] = ans.get(mon, Fraction(0)) + coeff
    return {m: c for m, c in ans.items() if c}

results = []
for receiver in prior:
    n = receiver['fibre']
    profile = profiles[n]
    original_degrees = profile['variables']
    cdeg = original_degrees['c']
    vs = receiver['receiver_variable_order']
    degrees = [original_degrees.get(v, [0, 1]) for v in vs]
    weights = receiver['receiver_weights']
    cap = sum(a*b for a, b in zip([int(v == 'c') for v in vs], weights))
    positions = {v: i for i, v in enumerate(vs)}
    for name, expected in receiver['hashes'].items():
        assert sha(ROOT / name) == expected, name
    basis_path = next(ROOT / p for p in receiver['hashes'] if 'basis' in Path(p).name)
    G = [parse(s, positions) for s in basis_path.read_text().strip().split(',')]
    assert len(G) == receiver['basis_size'] and all(G)
    def key(m):
        return sum(e*w for e, w in zip(m, weights)), tuple(-e for e in m[::-1])
    leaders = [max(g, key=key) for g in G]
    assert all(len({tuple(sum(e*d[k] for e, d in zip(m, degrees)) for k in (0, 1)) for m in g}) == 1 for g in G)
    # Remove divisible leaders, including duplicates. This is only monomial arithmetic.
    minimal = []
    for lm in sorted(set(leaders), key=lambda m: (sum(m), m)):
        if not any(all(a <= b for a, b in zip(other, lm)) for other in minimal):
            minimal.append(lm)
    sparse_leaders = [[(i, e) for i, e in enumerate(m) if e] for m in minimal]
    positive = [i for i, d in enumerate(degrees) if d[0] > 0]
    zero = [i for i, d in enumerate(degrees) if d[0] == 0]
    assert len(zero) <= 1
    if zero:
        assert degrees[zero[0]] == [0, 1]
    for v in vs:
        assert any(image in (v, f'{v}^1') for image in receiver['total_full_ring_map'].values()), ('map must be onto receiver', v)
    target_b, target_w = cdeg
    exps = [0] * len(vs)
    ambient = standard = 0
    standard_monomials = []
    def visit(start, b, w):
        global ambient, standard
        if b == target_b:
            if w > target_w or (not zero and w != target_w):
                return
            if zero:
                exps[zero[0]] = target_w - w
            ambient += 1
            if not any(all(exps[i] >= e for i, e in lm) for lm in sparse_leaders):
                standard += 1
                standard_monomials.append('*'.join(v + (f'^{e}' if e != 1 else '') for v, e in zip(vs, exps) if e) or '1')
            if zero:
                exps[zero[0]] = 0
            return
        for j in range(start, len(positive)):
            i = positive[j]
            db, dw = degrees[i]
            if b + db <= target_b and w + dw <= target_w:
                exps[i] += 1
                visit(j, b + db, w + dw)
                exps[i] -= 1
    visit(0, 0, 0)
    # Independent ambient count by the product generating function.
    dp = [[0] * (target_w + 1) for _ in range(target_b + 1)]
    dp[0][0] = 1
    for b, w in degrees:
        for x in range(b, target_b + 1):
            for y in range(w, target_w + 1):
                dp[x][y] += dp[x-b][y-w]
    assert dp[target_b][target_w] == ambient
    assert standard > 0
    zero_weights = [w for b, w in original_degrees.values() if b == 0]
    hp = [0] * (3 * target_w + 1)
    hp[0] = 1
    for w in zero_weights:
        for y in range(w, len(hp)):
            hp[y] += hp[y-w]
    pivots = None
    if n in (77, 136):
        dag_path = OLD / f'resume-r2/triangular/{n}/triangular-dag-custody.json'
        dag = json.loads(dag_path.read_text())
        hist = Counter(p['bidegree'][0] for p in dag['pivot_dag'])
        assert 0 not in hist
        pivots = {'count': len(dag['pivot_dag']), 'charge_histogram': dict(sorted(hist.items())), 'free_count': len(dag['remaining_free_coordinates']), 'dag_sha256': sha(dag_path)}
    assert all(target_b*w-target_w*b != 0 for v, (b, w) in original_degrees.items() if v != 'c')
    results.append({
        'fibre': n, 'target_delta_1': cdeg,
        'saved_witness_ring_variables': len(vs), 'saved_basis_size': len(G),
        'minimal_leading_monomials': len(minimal), 'witness_cutoff': cap,
        'witness_ambient_delta_1': ambient, 'witness_H_delta_1': standard,
        'witness_standard_monomials_delta_1': standard_monomials,
        'witness_H_delta_2': 0, 'witness_H_delta_3': 0,
        'zero_at_higher_targets_reason': 'Overflow in the explicitly saved receiver algebra; no positive inference in original ring.',
        'full_R_mod_I_H_delta_1_lower_bound': standard,
        'full_R_mod_I_H_delta_2': 'OPEN', 'full_R_mod_I_H_delta_3': 'OPEN',
        'charge_zero_variable_count': len(zero_weights),
        'full_R_mod_I_charge_zero_H': [{'degree': [0, k*target_w], 'dimension': hp[k*target_w]} for k in (1, 2, 3)],
        'full_R_mod_I_charge_zero_H_all_weights_through_3D': hp,
        'exact_full_charge_zero_formula': 'I_(0,Y)=0, so H_(R/I)(0,Y)=[v^Y] product_(B(z)=0)(1-v^w(z))^-1.',
        'source_basis_sha256': sha(basis_path), 'pivot_audit': pivots,
    })

report = {'script_sha256': sha(Path(__file__)), 'profiles_sha256': sha(profiles_path), 'prior_audit_sha256': sha(prior_path), 'fibres': results}
(OUT / 'hilbert-audit.json').write_text(json.dumps(report, indent=2) + '\n')
for row in results:
    print(row['fibre'], 'witness ambient/H(delta1)', row['witness_ambient_delta_1'], row['witness_H_delta_1'], 'H_full(0,ND)', row['full_R_mod_I_charge_zero_H'])
