import sympy as sp
from sympy import symbols
import sys; sys.path.insert(0,'/tmp/nvm')
from blowup import resolve
from synth import analyse_cluster
x, y = symbols('x y')
def row(name, P, Q):
    D, cl = resolve(P, Q, x, y)
    lab=[c['label'] for c in cl]; idx={l:i for i,l in enumerate(lab)}
    pts=[(c['a'], ['L' if u=='L' else idx[u] for u in c['through']]) for c in cl]
    r = analyse_cluster(D, pts); A=r['suma']
    print("%-22s D=%-3d N=%-3d Z.K_X=%-4d  Z.(K+Lred)=%-4d  kap=%-2d Lam=%-3d T=%-3d"
          % (name, D, r['N'], A-3*D, -2*D + A - r['sat'], r['kappa'], r['Lam'], r['sat']))
for k in (2,3,4,5):
    row("psi_%d o (x,xy)"%k, x + (x*y)**k, x*y)
for k in (2,3):
    row("psi_%d o (x,xy^2)"%k, x + (x*y**2)**k, x*y**2)
    row("psi_%d o (x,x^2y)"%k, x + (x**2*y)**k, x**2*y)
row("(x, x y^2 + y)", x, x*y**2+y)
row("(x y, x y^2)", x*y, x*y**2)
row("(x, y^3 + x y)", x, y**3+x*y)
