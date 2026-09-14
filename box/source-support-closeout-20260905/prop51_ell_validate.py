#!/usr/bin/env python3
"""OPEN[PROP51-ELL-EXTENSION] numerical validation of  delta_s = -(ell+1)/(n-M_s-1).

A. Moh Appendix II, printed p.207 (4 rows with u_3 = d_3 - v_3 = 1).
B. All 12 frozen campaign fibres: recorded delta_prime[s'] vs the formula.
"""
from fractions import Fraction as F
import json
ROOT = '/home/ubuntu/jc2/'
appII = [("16,12 main", 16, 12, 13, 1, F(-1)),
         ("21,14 main", 21, 14, 16, 1, F(-1, 2)),
         ("21,14 [br]", 21, 14, 18, 1, F(-1)),
         ("15,10 main", 15, 10, 11, 2, F(-1))]
print('A. Moh Appendix II p.207')
okA = 0
for name, n, m, Ms, ell, pr in appII:
    f_ell = F(-(ell + 1), n - Ms - 1); f_0 = F(-1, n - Ms - 1)
    okA += (f_ell == pr)
    print('  %-11s n=%2d M_s=%2d ell=%d  printed=%-5s  -(ell+1)/(n-M-1)=%-5s %-3s   ell=0 form=%-5s %s' % (name, n, Ms, ell, pr, f_ell, 'OK' if f_ell == pr else 'NO', f_0, 'OK' if f_0 == pr else 'NO'))  #
print('  ell-form %d/4 ; ell=0 form %d/4'
      % (okA, sum(F(-1, n - Ms - 1) == pr for _, n, _, Ms, _, pr in appII)))
print()
print('B. 12 frozen fibres')
okB = 0; rows = 0
for cls in json.load(open(ROOT + 'box/moh14-charts-20260905/hsupport-gate-20260905/classes_manifest.json')):
    for r in cls['rows']:
        rows += 1
        n, s, ell = r['n_prime'], r['s_prime'], r['ell']
        Ms = r['M_prime'][str(s)]
        rec = F(r['delta_prime'][str(s)]); f_ell = F(-(ell + 1), n - Ms - 1)
        okB += (rec == f_ell)
        print('  %-32s n=%2d M_s=%2d ell=%d  recorded=%-6s formula=%-6s %s'
              % (r['stem'][2:], n, Ms, ell, rec, f_ell, 'OK' if rec == f_ell else 'NO'))
print('  %d/%d' % (okB, rows))
