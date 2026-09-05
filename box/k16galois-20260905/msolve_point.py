#!/usr/bin/env python3
"""Extract F_p-rational points from an msolve rational parametrization (-P 1 output over a prime field).
Roots of the eliminating polynomial w are found by brute-force Horner evaluation at all of F_p (numpy),
coordinates by the parametrization; every candidate is re-verified later in Singular against the minors."""
import sys, re, numpy as np
txt = open(sys.argv[1]).read()
# msolve -P 1 format over F_p:  [char, nvars, deg, vars, linform, [1, [ [dw, [w coeffs]], [dwp, [w' coeffs]], [ [d1,[c1]], ... ] ] ] ]
nums = txt.replace('\n', ' ')
# parse with a tiny recursive descent (lists of ints/strings)
tok = re.findall(r"\[|\]|,|[-]?\d+|'[^']*'|[A-Za-z_][A-Za-z_0-9]*", nums)
pos = 0
def parse():
    global pos
    if tok[pos] == '[':
        pos += 1; out = []
        while tok[pos] != ']':
            if tok[pos] == ',': pos += 1; continue
            out.append(parse())
        pos += 1; return out
    v = tok[pos]; pos += 1
    try: return int(v)
    except ValueError: return v.strip("'")
data = parse()
if isinstance(data, list) and len(data) == 2 and data[0] == 0 and isinstance(data[1], list): data = data[1]
p = data[0]; nv = data[1]; deg = data[2]; vars_ = data[3]; linform = data[4]; body = data[5]
print("char", p, "nvars", nv, "deg", deg, "vars", vars_, "linform", linform, file=sys.stderr)
par = body[1]
w = par[0][1]; wp = par[1][1]; params = par[2]
def horner_all(coeffs, xs, p):
    acc = np.zeros_like(xs)
    for c in reversed(coeffs):
        acc = (acc * xs + c) % p
    return acc
xs = np.arange(p, dtype=np.int64)
vals = horner_all(w, xs, p)
roots = [int(r) for r in xs[vals == 0]]
print("rational roots of w:", len(roots), roots[:20], file=sys.stderr)
# squarefreeness at the roots: w'(a) != 0
def ev(coeffs, a, p):
    acc = 0
    for c in reversed(coeffs): acc = (acc * a + c) % p
    return acc
for a in roots:
    d = ev(wp, a, p)
    if d == 0:
        print("root", a, "is a multiple root of w (w'(a)=0)", file=sys.stderr); continue
    dinv = pow(d, p - 2, p)
    coords = []
    for pr in params:
        c = pr[0][1] if isinstance(pr[0], list) else pr[1]
        coords.append((-ev(c, a, p) * dinv) % p)
    # last variable = linear form value (msolve convention when the last variable separates)
    print("ROOT", a, "COORDS", coords)
