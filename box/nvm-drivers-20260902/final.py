import sympy as sp
from sympy import symbols
import sys; sys.path.insert(0,'/tmp/nvm')
from blowup import resolve
from synth import analyse_cluster
x, y = symbols('x y')
tests = [("(x, xy)",x,x*y),("(x, y^2)",x,y**2),("(x, xy^2)",x,x*y**2),("(x, xy^3)",x,x*y**3),
 ("(x, y+x^2)",x,y+x**2),("(x, y+x^3)",x,y+x**3),("(x, y+x^4)",x,y+x**4),("(x, y+x^5)",x,y+x**5),
 ("(x+y^2, y)",x+y**2,y),("(x+y^3, y)",x+y**3,y),
 ("(x, x^2y)",x,x**2*y),("(x, x^3y)",x,x**3*y),("(x, x^4y)",x,x**4*y),
 ("(x, x^2y^2)",x,x**2*y**2),("(x, x^3y^2)",x,x**3*y**2),("(x, x^4y^2)",x,x**4*y**2),
 ("(x, x^2y^3)",x,x**2*y**3),("(x, x^3y^3)",x,x**3*y**3),("(x, x^4y^3)",x,x**4*y**3),
 ("(x^2, y)",x**2,y),("(x^2y, y)",x**2*y,y),("(x, xy+y^2)",x,x*y+y**2),
 ("(x^2,y^4)",x**2,y**4),("(x^3,y^6)",x**3,y**6),("(x^4,y^8)",x**4,y**8),("(x^5,y^10)",x**5,y**10),
 ("(x, xy^2+y)",x,x*y**2+y),("(xy, xy^2)",x*y,x*y**2),("(x, y^3+xy)",x,y**3+x*y)]
for k in (1,2,3,4,5): tests.append(("psi_%d o (x,xy)"%k, x+(x*y)**k, x*y))
for k in (1,2,3,4):   tests.append(("psi_%d o (x,xy^2)"%k, x+(x*y**2)**k, x*y**2))
for k in (2,3):       tests.append(("psi_%d o (x,x^2y)"%k, x+(x**2*y)**k, x**2*y))
tests.append(("psi_cusp o (x,xy)", x+(x*y)**2, x*y+(x*y)**3))
nok=0; zk=[]; names=set()
for name,P,Q in tests:
    if name in names: continue
    names.add(name)
    D, cl = resolve(P,Q,x,y)
    lab=[c['label'] for c in cl]; idx={l:i for i,l in enumerate(lab)}
    pts=[(c['a'],['L' if u=='L' else idx[u] for u in c['through']]) for c in cl]
    r=analyse_cluster(D,pts)
    ok = r['ok_I1'] and r['ok_I2'] and r['ok_BND'] and r['ok_Z2'] and r['ok_mnonneg'] and r['ok_prox']
    nok += 1 if ok else 0
    zk.append((name, r['suma']-3*D, ok))
print("distinct maps:", len(names), " all identities OK:", nok)
print("Z.K_X range:", min(v for _,v,_ in zk), "..", max(v for _,v,_ in zk))
print("Keller (Jac const) instances:", [(n,v) for n,v,_ in zk if n.startswith('(x, y+x') or n.startswith('(x+y')])
bad=[z for z in zk if not z[2]]
print("failures:", bad)
