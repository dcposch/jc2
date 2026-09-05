#!/usr/bin/env python3
"""OPEN[Q-IS-T1] numerical witness: M_1' = -m' on every frozen fibre.

Moh p.185 (printed, verbatim): deg T_1^psi(f(x,y),g(x,y)) = deg_y T_1^psi = -M_1.
So M_1' = -m' says: the descendant's OWN first approximate-root replacement has
y-degree m' = deg_y Q'.  That is exactly "normalising Q' to T_1'^psi(P') is
degree-neutral on this row", i.e. the row datum (n',m',M',ell,s') is unchanged
by the normalisation.
"""
import json
from fractions import Fraction as F

ROOT = '/home/ubuntu/jc2/'
MAN = ROOT + 'box/moh14-charts-20260905/hsupport-gate-20260905/classes_manifest.json'
rows = []
for cls in json.load(open(MAN)):
    for r in cls['rows']:
        M1 = r['M_prime']['1']; m = r['m_prime']; n = r['n_prime']
        s = r['s_prime']; Ms = r['M_prime'][str(s)]
        ok = (M1 == -m)
        # cross-checks from the descent law
        us, vs, ds = r['u_s'], r['v_s'], r['d_s']
        ell_law = vs - us - 1
        rows.append(dict(stem=r['stem'], n=n, m=m, M1=M1, M=r['M_prime'], s=s, Ms=Ms,
                         ell=r['ell'], ell_law=ell_law, ell_ok=(r['ell'] == ell_law),
                         us=us, vs=vs, ds=ds, M1_eq_minus_m=ok,
                         Ms_le_n_minus_2=(Ms <= n - 2),
                         d=str(F(r['ell'] + 1, n - Ms - 1))))
print('%-32s %5s %4s %5s %6s %6s %5s %6s %s' %
      ('stem', 'n\'', 'm\'', 'M_1\'', 'M1=-m', 'ell', 'ell_law', 'Ms<=n-2', 'd'))
for r in rows:
    print('%-32s %5d %4d %5d %6s %6d %7d %8s %s' % (
        r['stem'][2:], r['n'], r['m'], r['M1'], r['M1_eq_minus_m'], r['ell'],
        r['ell_law'], r['Ms_le_n_minus_2'], r['d']))
print()
print('M_1\' = -m\'      : %d/%d' % (sum(r['M1_eq_minus_m'] for r in rows), len(rows)))
print('ell = v_s-u_s-1 : %d/%d' % (sum(r['ell_ok'] for r in rows), len(rows)))
print('M_s\' <= n\'-2    : %d/%d' % (sum(r['Ms_le_n_minus_2'] for r in rows), len(rows)))
json.dump(rows, open(ROOT + 'box/source-support-closeout-20260905/q_is_t1_witness.json', 'w'), indent=1)
