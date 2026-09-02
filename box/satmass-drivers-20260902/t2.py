import sympy as sp
from engine import Resolution, x, y

def psi(k, P, Q):      # (u,v) |-> (u + v^k, v)
    return (P + Q**k, Q)

tests = []
for k in range(2,7):
    tests.append((f"auto (x, y+x^{k})", x, y+x**k))
for k in range(2,5):
    tests.append((f"auto (x+y^{k}, y)", x+y**k, y))
# nested automorphism (Keller, N=1, genuinely long JvdK word)
tests.append(("auto (x+(y+x^2)^3, y+x^2)", x+(y+x**2)**3, y+x**2))
tests.append(("auto ((x+y^2)+ (y)^3, y)", x+y**2+y**3, y))
tests.append(("auto (y, x+y^3) [swap]", y, x+y**3))
# monomial / NEG-GEN family (x, x^c y^N)
for N in [1,2,3,4]:
    for c in [0,1,2,3]:
        if c==0 and N==1: continue
        tests.append((f"(x, x^{c} y^{N})", x, x**c*y**N))
# psi_k o (x, x y^N)
for N in [1,2,3]:
    for k in [2,3,4]:
        P,Q = psi(k, x, x*y**N)
        tests.append((f"psi_{k} o (x, x y^{N})", P, Q))
# assorted
tests += [
 ("(x^2, y^4)", x**2, y**4),
 ("(x, x y^2 + y)", x, x*y**2+y),
 ("(x+y^2, y+x^2)", x+y**2, y+x**2),
 ("(x^2 y, y)", x**2*y, y),
 ("(x, y^3)", x, y**3),
 ("(x^3, y^2)", x**3, y**2),
 ("(x+y^3, x)", x+y**3, x),
 ("(y, x+y^2)", y, x+y**2),
 ("(x*y, y)", x*y, y),
 ("(x^2+y, x)", x**2+y, x),
 ("(x, y+x^2+x^3)", x, y+x**2+x**3),
 ("(x+y^2, y^3)", x+y**2, y**3),
]
allok = True
rows = []
for nm,P,Q in tests:
    try:
        r = Resolution(P,Q,nm)
    except AssertionError as e:
        print("SKIP", nm, e); continue
    s = r.summary()
    bad = [k for k,v in r.checks.items() if not v]
    if bad:
        allok=False; print("FAIL", nm, bad)
    rows.append((nm, s))
print(f"{'map':30s} {'D':>3} {'N':>4} {'r':>3} {'kap':>4} {'Lam':>4} {'T':>4} {'Tcl':>4} {'T0':>3} {'suma':>5} {'ZK':>4} {'numx':>4} ok")
for nm,s in rows:
    print(f"{nm:30s} {s['D']:3d} {s['N']:4d} {s['r']:3d} {s['kappa']:4d} {s['Lam']:4d} {s['T']:4d} {s['Tclass']:4d} {s['Tzero']:3d} {s['suma']:5d} {s['ZK']:4d} {s['numax']:4d} {s['ok']}")
print("ALL IDENTITIES OK:", allok, " maps:", len(rows))
