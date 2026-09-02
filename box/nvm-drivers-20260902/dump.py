import sympy as sp
from sympy import symbols
import sys; sys.path.insert(0,'/tmp/nvm')
from blowup import resolve
from synth import analyse_cluster
x, y = symbols('x y')
def dump(name, P, Q):
    D, cl = resolve(P, Q, x, y)
    lab = [c['label'] for c in cl]
    idx = {l:i for i,l in enumerate(lab)}
    pts = [(c['a'], ['L' if u=='L' else idx[u] for u in c['through']]) for c in cl]
    r = analyse_cluster(D, pts)
    print("%-16s D=%-2d N=%-2d kappa=%-2d Lam=%-2d sat=%-2d suma=%-3d" %
          (name, D, r['N'], r['kappa'], r['Lam'], r['sat'], r['suma']))
    print("      cluster:", pts)
    print("      m:", [int(v) for v in r['m']], " c:", [int(v) for v in r['c']])
for c in (1,2,3,4):
    dump("(x, x^%d y)"%c, x, x**c*y)
for k in (2,3,4):
    dump("psi_%d o (x,xy)"%k, x + (x*y)**k, x*y)
