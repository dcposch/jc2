#!/usr/bin/env python3
"""S12: the symbolic-in-t closed forms of S1 against the fixed-t engine of S3.

Parses the "k=... / coeff = ..." blocks out of s1_r<r>.log, evaluates each at
the integer t of fixed_r<r>.json, and compares in A_t = Q[d]/(3d^2-t-1).
Closes the loop symbolic -> fixed-t -> exact record (the latter is S5).
"""
import json, re, sys, pathlib, sympy as sp
HERE = pathlib.Path("/home/ubuntu/jc2/box/k16subchart-20260903")
RV = int(sys.argv[1])
t, d = sp.symbols("t d")
log = (HERE/("s1_r%d.log" % RV)).read_text()
sec = log[log.index("# terminal bands"):]
lines = sec.split("\n")
sym = {}
for i, ln in enumerate(lines):
    m = re.match(r"\s*k=(.+?)\s+wt=(.+?)\s+x\^(\d+) b3\^(\d+)\s*$", ln)
    if not m:
        continue
    m2 = re.match(r"\s*coeff = (.+)$", lines[i+1])
    assert m2, lines[i+1][:60]
    sym[(sp.sympify(m.group(1)), int(m.group(3)), int(m.group(4)))] = sp.sympify(m2.group(1))
print("parsed %d symbolic coefficients from s1_r%d.log" % (len(sym), RV))
FIX = json.loads((HERE/("fixed_r%d.json" % RV)).read_text())
MIN = lambda tv: 3*d**2 - (tv+1)
def red(e, tv):
    e = sp.together(sp.expand(e)); n, den = sp.fraction(e)
    n = sp.rem(sp.Poly(sp.expand(n), d), sp.Poly(MIN(tv), d)).as_expr()
    den = sp.expand(den)
    if den.has(d):
        P = sp.Poly(sp.rem(sp.Poly(den, d), sp.Poly(MIN(tv), d)).as_expr(), d)
        A, B = P.nth(1), P.nth(0)
        n = sp.rem(sp.Poly(sp.expand(n*(B-A*d)), d), sp.Poly(MIN(tv), d)).as_expr()
        den = sp.expand(B**2 - A**2*sp.Rational(tv+1, 3))
    return sp.expand(sp.cancel(n/den))
ok = True
for tv in sorted(FIX, key=int):
    tv = int(tv)
    n = 0
    for kexpr, a, b in sym:
        kv = int(kexpr.subs(t, tv))
        got = FIX[str(tv)]["rows"].get(str(kv), {}).get("x^%d*b3^%d" % (a, b))
        if got is None:
            print("   t=%d k=%d x^%d b3^%d : ABSENT in fixed-t record" % (tv, kv, a, b))
            ok = False; continue
        diff = red(sym[(kexpr, a, b)].subs(t, tv) - sp.sympify(got[0]), tv)
        if diff != 0:
            print("   t=%d k=%d x^%d b3^%d : MISMATCH %s" % (tv, kv, a, b, diff))
            ok = False
        n += 1
    print("   t=%-3d %d coefficients compared" % (tv, n))
print("SYMBOLIC_VS_FIXED_T_r%d = %s" % (RV, "PASS" if ok else "FAIL"))
