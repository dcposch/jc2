#!/usr/bin/env python3
"""Moh p.150 characteristic invariants, implemented literally from the CHARGED
char-degree report Section 2 (d_1=n, d_{i+1}=gcd(n,M_1..M_i), n_i=d_i/d_{i+1},
q_1=M_1, q_i=M_i-M_{i-1}, Lambda_i=sum_{j<=i} q_j d_j, mu_i=Lambda_i/d_i,
D_i=-mu_i).  Controls: the two char-degree clients.  Then the K=16 ray."""
from math import gcd
from fractions import Fraction
import json

def chardata(n, Ms):
    d = [n]
    for i in range(len(Ms)):
        g = n
        for j in range(i+1):
            g = gcd(g, abs(Ms[j]))
        d.append(g)
    ni = [Fraction(d[i], d[i+1]) for i in range(len(d)-1)]
    q  = [Ms[0]] + [Ms[i]-Ms[i-1] for i in range(1, len(Ms))]
    Lam, mu, D, acc = [], [], [], 0
    for i in range(len(Ms)):
        acc += q[i]*d[i]
        Lam.append(acc); mu.append(Fraction(acc, d[i])); D.append(-Fraction(acc, d[i]))
    return dict(d=d, n_i=[str(v) for v in ni], q=q, Lambda=Lam,
                mu=[str(v) for v in mu], D=[str(v) for v in D])

out = {}
# --- controls from the charged report table ---
c1 = chardata(99, [-66, 77, 97]);  out['ctrl_99_66'] = c1
c2 = chardata(108, [-72, 81, 106]); out['ctrl_108_72'] = c2
ok1 = c1['d'][:4] == [99,33,11,1] and c1['Lambda'] == [-6534,-1815,-1595] and c1['D'] == ['66','55','145']
ok2 = c2['d'][:4] == [108,36,9,1] and c2['Lambda'] == [-7776,-2268,-2043] and c2['D'] == ['72','63','227']
out['CONTROL_99_66_MATCHES_CHARGED_TABLE'] = ok1
out['CONTROL_108_72_MATCHES_CHARGED_TABLE'] = ok2

# --- the K=16 ray: banked 4-tuple (n,m;M_2;V_2) = (12t+4, 8t+4; 12t+1; 3) ---
ray = {}
for t in range(2, 9):
    n, m, M2 = 12*t+4, 8*t+4, 12*t+1
    r = chardata(n, [-m, M2])
    r['closed_form_check'] = {
        'd2_is_4':  r['d'][1] == 4,
        'n1_is_3t+1': r['n_i'][0] == str(3*t+1),
        'n2_is_4':  r['n_i'][1] == str(4),
        'D1_is_m':  r['D'][0] == str(m),
        'D2_is_24t^2-1': r['D'][1] == str(24*t*t-1),
        'D2_mod_4': (24*t*t-1) % 4,
        'ambient_L_n1*m': (3*t+1)*m,
        'leader_depth_L-D2': (3*t+1)*m - (24*t*t-1),
    }
    ray[f't={t}'] = r
out['K16_ray'] = ray
# --- the 3:2 hypothesis of the lane prompt: K=16 => (48,32) ---
out['prompt_premise_3to2_K16'] = {
    'n': 48, 'm': 32, 'n1_if_3to2': 3,
    'ray_has_n1_equal_3_for_some_t': any((12*t+4)//4 == 3 for t in range(1, 10000)),
    'ray_n_equals_48_for_some_t': any(12*t+4 == 48 for t in range(1, 10000)),
    'ray_gcd_n_m': 4,
}
print(json.dumps(out, indent=1))
