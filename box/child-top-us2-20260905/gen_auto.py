import sys, json, itertools, random; sys.path.insert(0,'/home/ubuntu/jc2/box/child-top-us2-20260905')
import sympy as sp
from harness import analyse
x,y = sp.symbols('x y')

def steps(pairs, P):
    F,G = pairs
    return (G, sp.expand(F + P))

random.seed(7)
results = []
# tame automorphisms:  (F,G) -> (G, F + P(G)); then a linear tweak so that deg G = deg_y G.
base = [(x,y),(y,x)]
polys = lambda t: [t**2, t**3, t**2+t, t**3+t, t**4, t**5, t**2+1]
cands = []
for F0,G0 in base:
    for P1 in polys(G0):
        F1,G1 = steps((F0,G0), P1)
        cands.append((F1,G1))
        for P2 in polys(G1):
            F2,G2 = steps((F1,G1), P2)
            cands.append((F2,G2))
seen=set()
for F,G in cands:
    for lam in [0,1,2]:
        FF = sp.expand(F.subs({x:x+lam*y}, simultaneous=True))
        GG = sp.expand(G.subs({x:x+lam*y}, simultaneous=True))
        try:
            gp = sp.Poly(GG,y)
            if gp.degree() < 2: continue
            if sp.Poly(GG,x,y).total_degree() != gp.degree(): continue
            if sp.Poly(GG,x).degree() < 1: continue
            if sp.Poly(FF,x).degree() < 1: continue
            J = sp.expand(sp.diff(FF,x)*sp.diff(GG,y)-sp.diff(FF,y)*sp.diff(GG,x))
            key = (sp.srepr(sp.expand(FF)), sp.srepr(sp.expand(GG)))
            if key in seen: continue
            seen.add(key)
            r = analyse(FF, GG, x, y, label=f'auto lam={lam}')
            if r is None: continue
            r['J'] = str(J)
            results.append(r)
        except Exception as e:
            pass
json.dump(results, open('/home/ubuntu/jc2/box/child-top-us2-20260905/auto-scan.json','w'), indent=1)
print(len(results),'pairs')
for r in results:
    print(f"n={r['n']:3d} m={r['m']:3d} M={r['M']} d={r['d']} s={r['s']} d_s={r['d_s']} "
          f"| nt={r['nt']} u_s={r['u_s']} low_match={r.get('low_match')} "
          f"Mx={r['Mx']} extra={r.get('M_extra')} nt-1={r['nt_minus_1']} CTOP={r.get('CTOP_hypothesis')} J={r['J']}")
