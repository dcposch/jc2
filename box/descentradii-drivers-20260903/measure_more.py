#!/usr/bin/env python3
"""Extra shapes: (15,10) V2=2, (21,14) V2=2 and V2=5; two-point fit of delta;
exact Newton support of (15,10) f; residual (4)/(6) check of the 12 witnesses.
"""
import random, os, sys
from math import log, gcd
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

x, y = sp.symbols('x y')

def ratapprox(val, bound=80):
    if val != val or abs(val) > 1e8:
        return None
    sign = 1 if val >= 0 else -1
    return sign * Fr(abs(val)).limit_denominator(bound)

def rQ(rng):
    return sp.Rational(rng.choice([-4,-3,-2,-1,1,2,3,4]), rng.choice([1,1,1,2]))

def roots_scaled(P, Xval):
    Pex = sp.Poly(sp.expand(P), y)
    d = Pex.degree()
    coeffs = []
    for k in range(d, -1, -1):
        ak = sp.expand(Pex.coeff_monomial(y**k))
        val = complex(ak.subs(x, Xval))
        coeffs.append(val * (Xval ** (k - d)))
    zs = np.roots(np.array(coeffs, dtype=np.complex128))
    return Xval * zs

def fit_delta(ys_by_X, i_pair_selector=None):
    """For each X, take min pairwise delta inside a selected cluster; fit
    delta_est = delta_true - log|C|/log|X| using two largest X."""
    pass

def cluster_near(ys, center, rad):
    return [z for z in ys if abs(z-center) < rad]

def report_cluster(ys, Xval, center, lab):
    pts = cluster_near(ys, center, 0.4*abs(Xval) if center != 0 else 0.5*abs(Xval))
    if center == 0:
        pts = [z for z in ys if abs(z) < 0.4*abs(Xval)]
    logX = log(abs(Xval))
    if len(pts) < 2:
        print("    %s: %d roots (need >=2)" % (lab, len(pts)))
        return None
    ds = []
    for i in range(len(pts)):
        for j in range(i+1, len(pts)):
            d = abs(pts[i]-pts[j])
            if d > 0:
                ds.append(-log(d)/logX)
    mean = float(np.mean([abs(z-center) for z in pts]))
    expo = log(mean)/log(abs(Xval)) if mean > 0 else 0
    print("    %s n=%d  min_delta=%.6f ~ %s  max=%.6f  mean|y-c|=%.6g (~|X|^%.5f ~ %s)" %
          (lab, len(pts), min(ds), ratapprox(min(ds)), max(ds),
           mean, expo, ratapprox(expo)))
    return dict(n=len(pts), min_d=min(ds), max_d=max(ds), expo=expo, mean=mean)

def two_point(d1, X1, d2, X2):
    """delta_est(X) = D - c/log|X|.  Solve D from two X."""
    L1, L2 = log(abs(X1)), log(abs(X2))
    # d1 = D - c/L1, d2 = D - c/L2
    # d1 - d2 = -c (1/L1 - 1/L2)
    c = (d2 - d1) / (1/L1 - 1/L2)
    D = d1 + c/L1
    return D, c, ratapprox(D)

def support_print(P, name):
    Po = sp.Poly(sp.expand(P), x, y)
    pts = sorted(zip(Po.monoms(), Po.coeffs()), key=lambda t: (-(t[0][0]+t[0][1]), -t[0][1]))
    print("  support %s (first 12 by total deg):" % name)
    n = 0
    for (i,j), c in pts:
        if c:
            print("    x^%d y^%d  %s" % (i, j, c))
            n += 1
            if n >= 12:
                break
    print("    total monomials", sum(1 for _,c in pts if c), " max total deg",
          max(i+j for (i,j),c in pts if c))

# ---- shapes ----
def shape_y_a_ymx_b(a, b, seed, extra_lin_x=True):
    """h = y^a (y-x)^b + lower of total degree a+b, deg_x <= b.
    beta a generic poly deg_y < a+b, with an x-linear term (Moh-style).
    f = h^2 + 2 beta  if we want d'=2; for (16,12) we'd use h^3.
    Here used for (15,10)-like (d'=2) and (21,14)-like (d'=2).
    """
    rng = random.Random(seed)
    n_h = a + b
    h = sp.expand(y**a * (y - x)**b)
    # add all monomials x^i y^j with i+j < n_h, i <= b, j < n_h (drop the top)
    for i in range(0, b+1):
        for j in range(0, n_h):
            if i + j >= n_h:
                continue
            if i == 0 and j == n_h:
                continue
            h += rQ(rng) * x**i * y**j
    h = sp.expand(h)
    # beta: deg_y <= n_h-1, deg <= 2 n_h, include a*x term
    beta = 0
    for j in range(0, n_h):
        for i in range(0, n_h+1):
            beta += rQ(rng) * x**i * y**j
    if extra_lin_x:
        beta += rQ(rng) * x
    beta = sp.expand(beta)
    f = sp.expand(h**2 + 2*beta)
    # g = h^3 + G1 h + G0, generic for disc structure of f (enough)
    G1 = sum(rQ(rng)*x**i*y**j for i in range(0, n_h) for j in range(0, n_h))
    G0 = sum(rQ(rng)*x**i*y**j for i in range(0, n_h) for j in range(0, n_h))
    g = sp.expand(h**3 + G1*h + G0)
    return f, g, h

def moh_1510(seed):
    rng = random.Random(seed)
    avals = [rQ(rng) for _ in range(12)]
    a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12 = avals
    B = (y**2 - x**2 + a1*y + a2*x + a3)*y + (a4*x + a5)
    A = sp.expand(B*y + (a6*x + a7))
    h = sp.expand(A*y + a8)
    beta = sp.expand(a9*A + a10*y + a11*x + a12)
    f = sp.expand(h**2 + 2*beta)
    return f, h, avals

print("=" * 70)
print("EXACT support of a (15,10) Moh shape f")
f, h, av = moh_1510(20260903)
support_print(h, "h")
support_print(f, "f")
print("  h leading form (homog deg 5):", sp.expand(sum(
    c*x**i*y**j for (i,j),c in zip(sp.Poly(h,x,y).monoms(), sp.Poly(h,x,y).coeffs())
    if i+j==5)))
print("  f leading form (homog deg 10):", sp.expand(sum(
    c*x**i*y**j for (i,j),c in zip(sp.Poly(f,x,y).monoms(), sp.Poly(f,x,y).coeffs())
    if i+j==10)))

def sweep(label, f, centers, Xs=(1e4, 1e5, 1e6)):
    print("\n---- %s ----" % label)
    print("  deg_y f=%s total=%s" % (sp.degree(f,y), sp.total_degree(f)))
    store = {lab: [] for lab,_ in centers}
    for Xval in Xs:
        ys = roots_scaled(f, Xval)
        print("  X=%g  n=%d  |y| range %.3g .. %.3g" %
              (Xval, len(ys), min(abs(z) for z in ys), max(abs(z) for z in ys)))
        # top contact
        logX = log(abs(Xval))
        alld = [-log(abs(ys[i]-ys[j]))/logX
                for i in range(len(ys)) for j in range(i+1,len(ys)) if abs(ys[i]-ys[j])>0]
        print("    TOP min_delta=%.6f ~ %s" % (min(alld), ratapprox(min(alld))))
        for lab, cen_fn in centers:
            cen = cen_fn(Xval)
            rec = report_cluster(ys, Xval, cen, lab)
            if rec:
                store[lab].append((Xval, rec))
    # two-point fit on last two X
    for lab, recs in store.items():
        if len(recs) >= 2:
            (X1, r1), (X2, r2) = recs[-2], recs[-1]
            Dmin, c, fr = two_point(r1['min_d'], X1, r2['min_d'], X2)
            De, c2, fr2 = two_point(r1['expo'], X1, r2['expo'], X2)
            print("  FIT %s  min_delta -> %.6f ~ %s   (using |X|=%g,%g)" %
                  (lab, Dmin, fr, X1, X2))
            print("  FIT %s  cluster-scale expo -> %.6f ~ %s" % (lab, De, fr2))

# (15,10) Moh shape, larger X, two-point
f, h, av = moh_1510(20260903)
sweep("(15,10) Moh (5)-(6) seed=20260903  [expect 2,2,6 and delta1=1/2]",
      f, [('0', lambda X: 0), ('+X', lambda X: X), ('-X', lambda X: -X)],
      Xs=(1e4, 3e4, 1e5, 3e5))

f, h, av = moh_1510(17)
sweep("(15,10) Moh seed=17",
      f, [('0', lambda X: 0), ('+X', lambda X: X), ('-X', lambda X: -X)],
      Xs=(1e4, 1e5, 3e5))

# (15,10) V2=2 shape: y^2 (y-x)^3
f,g,h = shape_y_a_ymx_b(2, 3, seed=5)
sweep("(15,10)-like V2=2  h=y^2(y-x)^3+lower  [printed delta1=4/3]",
      f, [('0', lambda X: 0), ('X', lambda X: X)],
      Xs=(1e4, 1e5, 3e5))

# (21,14) V2=5: y^5 (y-x)^2
f,g,h = shape_y_a_ymx_b(5, 2, seed=5)
sweep("(21,14)-like V2=5  h=y^5(y-x)^2+lower  [printed delta2=-1, delta1=1/3]",
      f, [('0', lambda X: 0), ('X', lambda X: X)],
      Xs=(1e3, 1e4, 1e5))

# (21,14) V2=2: y^2 (y-x)^5
f,g,h = shape_y_a_ymx_b(2, 5, seed=5)
sweep("(21,14)-like V2=2  h=y^2(y-x)^5+lower  [printed delta2=-1/2, delta1=7/6]",
      f, [('0', lambda X: 0), ('X', lambda X: X)],
      Xs=(1e3, 1e4, 1e5))

# (16,12)-like: f = h^3 + beta2 h + beta3, h=y^3(y-x)+lower
def make_1612_f(seed):
    rng = random.Random(seed)
    b1,b2,b3,b4 = [rQ(rng) for _ in range(4)]
    h = sp.expand(y**3*(y-x) + b1*y**3 + b2*y**2 + b3*y + b4)
    A = sp.expand(sp.together((h-b4)/y))
    B = sp.expand(sp.together((h-b3*y-b4)/y**2))
    cs = [rQ(rng) for _ in range(13)]
    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13 = cs
    beta2 = sp.expand(c3*A + c4)
    beta3 = sp.expand(c8*A + c9*B + c10)
    f = sp.expand(h**3 + beta2*h + beta3)
    return f, h

f,h = make_1612_f(20260903)
sweep("(16,12) Moh p.208 f  [expect 3+9, delta1=1/4]",
      f, [('0', lambda X: 0), ('X', lambda X: X)],
      Xs=(1e4, 1e5, 3e5, 1e6))
