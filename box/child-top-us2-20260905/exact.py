"""Exact (symbolic base variable) re-run of representative scan2 instances,
using the independent sympy engine chardata.py -- no modular arithmetic."""
import sys, json, collections
sys.path.insert(0, '/home/ubuntu/jc2/box/child-top-us2-20260905')
import sympy as sp
from chardata import chardata
from fractions import Fraction as F

x, y = sp.symbols('x y')
rows = json.load(open('/home/ubuntu/jc2/box/child-top-us2-20260905/scan2.json'))
good = [r for r in rows if r['low_ok'] and r['u_s'] >= 2 and r['dxs_eq_us']]
print('modular case split over', len(good), 'instances:',
      collections.Counter(r['case'] for r in good))

# pick the richest instances: largest s, then largest u_s, then largest n
good.sort(key=lambda r: (r['s'], r['u_s'], r['n']), reverse=True)
picked, seen = [], set()
for r in good:
    k = (r['case'], r['s'], r['u_s'])
    if k in seen:
        continue
    seen.add(k); picked.append(r)
    if len(picked) >= 6:
        break

def build(d):
    e = 0
    for k, c in d.items():
        i, j = map(int, k.split(','))
        e += c * x**i * y**j
    return sp.expand(e)

out = []
for r in picked:
    f, g = build(r['f']), build(r['g'])
    cy = chardata(f, g, y, x)
    cx = chardata(f, g, x, y)
    rec = dict(case=r['case'], s=r['s'], u_s=r['u_s'],
               mod_y=(r['M'], r['d']), exact_y=(cy['M'], cy['d']),
               mod_x=(r['Mx'], r['dx']), exact_x=(cx['M'], cx['d']),
               n=cy['n'], m=cy['m'], nprime=cx['n'], mprime=cx['m'],
               nprime_minus_1=cx['n'] - 1,
               f=sp.srepr(f) and str(f), g=str(g),
               J=str(sp.expand(sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x))))
    rec['agrees'] = (list(rec['mod_y'][0]) == list(cy['M']) and
                     list(rec['mod_x'][0]) == list(cx['M']))
    out.append(rec)
    print(f"\ncase={r['case']}  s={r['s']} u_s={r['u_s']}")
    print(f"  f = {f}")
    print(f"  g = {g}")
    print(f"  J = {rec['J']}")
    print(f"  y-side (Moh's own): n={cy['n']} m={cy['m']} M={cy['M']} d={cy['d']}")
    print(f"  x-side (the CHILD): n'={cx['n']} m'={cx['m']} M'={cx['M']} d'={cx['d']}"
          f"   n'-1={cx['n']-1}")
    print(f"  modular run agrees exactly: {rec['agrees']}")

json.dump(out, open('/home/ubuntu/jc2/box/child-top-us2-20260905/exact.json', 'w'), indent=1)
