#!/usr/bin/env python3
"""Read-only lattice audit on 20 deterministic random frozen roster rows."""
import json
import math
import random
from pathlib import Path
import sympy as sp

FROZEN = Path('/tmp/jc2-lane.QKyQBy/inputs/roster.jsonl')
OUT = Path(__file__).with_name('lemmas_audit.json')
SEED = 20260906
rows = [json.loads(line) for line in FROZEN.read_text().splitlines()]
chosen = sorted(random.Random(SEED).sample(rows, 20), key=lambda r: r['row_id'])
records = []
for row in chosen:
    source = row['source']
    n, M, d = source['n'], source['M'], source['d']
    assert len(d) == len(M) + 1
    recurrence = [math.gcd(n, *M[:i]) == d[i] for i in range(len(d))]
    pairs = []
    for ancestor in range(1, len(M)):
        for deeper in range(ancestor):
            divisor, exponent = d[ancestor], M[deeper]
            pairs.append({'ancestor_i': ancestor + 1, 'deeper_j': deeper + 1,
                          'd_i': divisor, 'M_j': exponent,
                          'W_j': n - exponent,
                          'divides': exponent % divisor == 0,
                          'W_congruence': ((n - exponent) - n) % divisor == 0})
    # Negative control: same-index characteristic exponent must leave the lattice.
    own_index_nondivisibility = [M[i] % d[i] != 0 for i in range(len(M))]
    assert all(recurrence)
    assert all(p['divides'] and p['W_congruence'] for p in pairs)
    assert all(own_index_nondivisibility)
    records.append({'row_id': row['row_id'], 'n': n, 'm': source['m'],
                    'M': M, 'd': d, 'gcd_recurrence': recurrence,
                    'ancestor_pairs': pairs,
                    'negative_control_same_index_not_divisible': own_index_nondivisibility})
pi = sp.symbols('pi')
h = pi**10 - 5*pi**5 + 5
s = pi**6 - 3*pi
p = h**2
q = h*s
ode_check = sp.expand(20*p*sp.diff(q, pi) - 16*sp.diff(p, pi)*q + 300*p)
q_squarefree_check = sp.gcd(q, sp.diff(q, pi))
assert ode_check == 0 and q_squarefree_check == 1
assert sp.gcd(h, sp.diff(h, pi)) == 1 and sp.gcd(h, s) == 1
assert sp.div(q, h)[1] == 0
result = {
    'input': str(FROZEN), 'random_method': 'random.Random(seed).sample(rows,20)',
    'seed': SEED, 'sample_size': len(records),
    'interpretation': ('Tests only the printed global characteristic-chain implication '
                       'j<i => d_i divides M_j. This does not test or prove the bridge '
                       'from a free effective sibling W to a nonzero eta-support exponent.'),
    'pair_count': sum(len(r['ancestor_pairs']) for r in records),
    'passed_rows': len(records), 'records': records,
    'lemma_A_local_ODE_counterexample': {
        'proposed_by': 'root; independently verified in this script',
        'h': str(h), 's': str(s), 'p': '(pi**10-5*pi**5+5)**2',
        'q': '(pi**10-5*pi**5+5)*(pi**6-3*pi)',
        'P': 20, 'Q': 16, 'A': 5,
        'identity': "20*p*q_prime - 16*p_prime*q = -300*p",
        'identity_residual': str(ode_check),
        'gcd_q_qprime': str(q_squarefree_check),
        'gcd_h_hprime': str(sp.gcd(h, sp.diff(h, pi))),
        'gcd_h_s': str(sp.gcd(h, s)),
        'all_p_roots_multiplicity': 2,
        'p_is_power_of_q': False,
        'status': 'Exact polynomial witness to the reduced local ODE and Prop4.6 numerical conclusions; no global pair claimed.'
    },
    'lemma_A_printed_countercontrol': {
        'source': 'Xu section 6.1(i), PDF p8, xu.txt:406-416',
        'row_id': 'R002', 'n': 75, 'm': 50, 'd_2': 25,
        'f_multiplicity_each_of_ten_roots': 4,
        'g_multiplicity_each_of_ten_roots': 6,
        'm_over_d_2': 2,
        'reduced_pattern_multiplicities': [2] * 10,
        'setwise_gcd': math.gcd(*([2] * 10)),
        'status': 'Violates Lemma A as stated; retained by Xu numerical test; not a polynomial-pair witness.'
    }
}
OUT.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ('seed','sample_size','pair_count','passed_rows')}, sort_keys=True))
print(' '.join(r['row_id'] for r in records))
