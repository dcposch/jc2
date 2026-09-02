import sympy as sp
from sympy import symbols
import sys; sys.path.insert(0,'/tmp/nvm')
from ident import analyse
x, y = symbols('x y')
tests = [
    ("(x, xy)",           x,               x*y),
    ("(x, y^2)",          x,               y**2),
    ("(x, xy^2)",         x,               x*y**2),
    ("(x, xy^3)",         x,               x*y**3),
    ("(x, y+x^2)",        x,               y+x**2),
    ("(x, y+x^3)",        x,               y+x**3),
    ("(x, y+x^4)",        x,               y+x**4),
    ("(x, x^2 y)",        x,               x**2*y),
    ("(x, x^3 y)",        x,               x**3*y),
    ("(x, x^2 y^2)",      x,               x**2*y**2),
    ("(x, x^2 y^3)",      x,               x**2*y**3),
    ("(x+y^2, y)",        x+y**2,          y),
    ("(x, xy+y^2)",       x,               x*y+y**2),
    ("(x^2, y)",          x**2,            y),
    ("(x^2 y, y)",        x**2*y,          y),
    # target-Aut translates of (x,xy):  A_F becomes a degree-n rational curve
    ("psi2 o (x,xy)",     x + x**2*y**2,   x*y),
    ("psi3 o (x,xy)",     x + x**3*y**3,   x*y),
    ("psi2 o (x,xy^2)",   x + x**2*y**4,   x*y**2),
    ("psi_cusp o (x,xy)", x + (x*y)**2,    x*y + (x*y)**3),
]
for n, P, Q in tests:
    try:
        analyse(n, P, Q, verbose=False)
    except Exception as e:
        print("%-18s EXC %s" % (n, e))
