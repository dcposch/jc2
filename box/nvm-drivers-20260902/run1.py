import sympy as sp
from sympy import symbols
import sys
sys.path.insert(0,'/tmp/nvm')
from blowup import resolve
x, y = symbols('x y')
for name, P, Q, Nknown in [
    ("(x, x*y)",        x,        x*y,        1),
    ("(x, y^2)",        x,        y**2,       2),
    ("(x, x*y^2)",      x,        x*y**2,     2),
    ("(x, y+x^2)",      x,        y+x**2,     1),
    ("(x, y+x^3)",      x,        y+x**3,     1),
    ("(x, x^2*y)",      x,        x**2*y,     1),
    ("(x, x*y^3)",      x,        x*y**3,     3),
]:
    print("==", name)
    D, cl = resolve(P, Q, x, y, verbose=True)
    sa = sum(c['a'] for c in cl); sq = sum(c['a']**2 for c in cl)
    print("   D=%d  r=%d  sum a=%d  sum a^2=%d   D^2-sum a^2 = %d  (N known %s)"
          % (D, len(cl), sa, sq, D*D-sq, Nknown))
