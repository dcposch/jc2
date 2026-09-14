"""Exact-rational cross-check (fastchar, Fractions over Q, three independent base
points) of representative scan2 instances -- independent of the modular engine."""
import sys, json, collections
sys.path.insert(0,'/home/ubuntu/jc2/box/child-top-us2-20260905')
from fastchar import chardata_poly
from fractions import Fraction as F
rows=json.load(open('/home/ubuntu/jc2/box/child-top-us2-20260905/scan2.json'))
good=[r for r in rows if r['low_ok'] and r['u_s']>=2 and r['dxs_eq_us']]
print('modular case split over',len(good),'instances:',collections.Counter(r['case'] for r in good))
good.sort(key=lambda r:(r['s'],r['u_s'],-r['n']),reverse=True)
picked,seen=[],set()
for r in good:
    k=(r['case'],r['s'],r['u_s'])
    if k in seen: continue
    seen.add(k); picked.append(r)
def build(d): return {tuple(map(int,k.split(','))):F(c) for k,c in d.items()}
out=[]
for r in picked[:8]:
    f,g=build(r['f']),build(r['g'])
    ys=[chardata_poly(f,g,True,x0) for x0 in (F(7),F(103,5),F(-31,3))]
    xs=[chardata_poly(f,g,False,x0) for x0 in (F(7),F(103,5),F(-31,3))]
    ok = len({tuple(o['M']) for o in ys})==1 and len({tuple(o['M']) for o in xs})==1
    agree = list(ys[0]['M'])==list(r['M']) and list(xs[0]['M'])==list(r['Mx'])
    rec=dict(case=r['case'],s=r['s'],u_s=r['u_s'],f=r['f'],g=r['g'],
             y_side=dict(n=ys[0]['n'],m=ys[0]['m'],M=ys[0]['M'],d=ys[0]['d']),
             x_side=dict(n=xs[0]['n'],m=xs[0]['m'],M=xs[0]['M'],d=xs[0]['d']),
             nprime_minus_1=xs[0]['n']-1, stable_over_Q=ok, agrees_with_modular=agree)
    out.append(rec)
    print(f"\ncase={r['case']} s={r['s']} u_s={r['u_s']}  f={r['f']}  g={r['g']}")
    print(f"  y-side  n={ys[0]['n']} m={ys[0]['m']} M={ys[0]['M']} d={ys[0]['d']}  (M_s vs n-2: {ys[0]['M']}, n-2={ys[0]['n']-2})")
    print(f"  x-side  n'={xs[0]['n']} m'={xs[0]['m']} M'={xs[0]['M']} d'={xs[0]['d']}  n'-1={xs[0]['n']-1}")
    print(f"  stable over Q at 3 base points: {ok}   agrees with modular run: {agree}")
json.dump(out,open('/home/ubuntu/jc2/box/child-top-us2-20260905/exact.json','w'),indent=1,default=str)
