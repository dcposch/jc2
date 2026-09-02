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
    r = analyse_cluster(D, pts)
    A = r['suma']
    print("%-16s D=%-3d N=%-3d  sum a=%-4d 3D=%-4d  Z.K_X = %-4d  kappa=%-2d Lam=%-3d T=%-3d"
          % (name, D, r['N'], A, 3*D, A-3*D, r['kappa'], r['Lam'], r['sat']))
print("-- Keller examples (automorphisms): Noether-Keller with S=0 predicts sum a = 3D-2N-kappa --")
for k in (2,3,4,5):
    row("(x, y+x^%d)"%k, x, y+x**k)
row("(x+y^2, y)", x+y**2, y)
row("(x+y^3, y)", x+y**3, y)
print("-- heavy affine ramification: does sum a - 3D go positive? --")
for (aa,bb) in [(2,4),(3,6),(4,8),(5,10)]:
    row("(x^%d, y^%d)"%(aa,bb), x**aa, y**bb)
