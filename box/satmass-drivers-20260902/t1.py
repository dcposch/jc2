import sympy as sp
from engine import Resolution, x, y

tests = [
    ("(x, y+x^2)",  x, y + x**2),
    ("(x, y+x^3)",  x, y + x**3),
    ("(x, y+x^4)",  x, y + x**4),
    ("(x, xy)",     x, x*y),
    ("(x, xy^2)",   x, x*y**2),
    ("(x, x^2 y)",  x, x**2*y),
    ("(x, y^2)",    x, y**2),
]
for nm,P,Q in tests:
    r = Resolution(P,Q,nm)
    s = r.summary()
    print(nm, s)
    for row in r.table():
        print("   ", row)
    bad = [k for k,v in r.checks.items() if not v]
    if bad: print("   FAIL:", bad)
