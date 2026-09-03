#!/usr/bin/env python3
"""Fast numpy measurement of disc trees for (15,10) and (16,12) shapes."""
import random
from math import log
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

x, y = sp.symbols('x y')

def ratapprox(val, bound=64):
    if val != val or abs(val) > 1e8:
        return None
    sign = 1 if val >= 0 else -1
    return sign * Fr(abs(val)).limit_denominator(bound)

def ycoeffs(P, Xval):
    """numpy poly coeffs high-to-low of P(Xval, y)."""
    Pex = sp.Poly(sp.expand(P), y)
    d = Pex.degree()
    out = []
    for k in range(d, -1, -1):
        ck = sp.expand(Pex.coeff_monomial(y**k))
        out.append(complex(ck.subs(x, Xval)))
    return np.array(out, dtype=np.complex128)

def roots_scaled(P, Xval):
    """Roots of P(X,y)=0, using z=y/X scaling for stability."""
    # P(X, X z) = X^D * Q(z); roots y = X * z_roots of Q
    Pex = sp.Poly(sp.expand(P), y)
    d = Pex.degree()
    # Q(z) = sum_k a_k(X) (X z)^k / X^D = sum_k a_k(X) X^{k-D} z^k
    # high-to-low in z: k=d..0, coeff a_k * X^{k-d}
    coeffs = []
    for k in range(d, -1, -1):
        ak = sp.expand(Pex.coeff_monomial(y**k))
        val = complex(ak.subs(x, Xval))
        coeffs.append(val * (Xval ** (k - d)))
    zs = np.roots(np.array(coeffs, dtype=np.complex128))
    return Xval * zs

def tree_report(ys, Xval, name):
    n = len(ys)
    logX = log(abs(Xval))
    deltas = []
    for i in range(n):
        for j in range(i+1, n):
            d = abs(ys[i]-ys[j])
            deltas.append((-log(d)/logX) if d > 0 else 99.0)
    # cluster sizes at rounded delta levels
    print("  %s  |X|=%.3g  n=%d  |y| in [%.3g, %.3g]" %
          (name, abs(Xval), n, min(abs(z) for z in ys), max(abs(z) for z in ys)))
    # hierarchical by rounded delta
    items = []
    for i in range(n):
        for j in range(i+1, n):
            d = abs(ys[i]-ys[j])
            delta = -log(d)/logX if d>0 else 99.0
            items.append((delta, i, j))
    items.sort()  # coarsest (smallest delta) first
    parent = list(range(n))
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]; a=parent[a]
        return a
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: parent[rb]=ra
    last_sizes = [1]*n
    printed = 0
    # group nearly-equal deltas
    k = 0
    while k < len(items) and printed < 10:
        T0 = items[k][0]
        batch = []
        while k < len(items) and abs(items[k][0] - T0) < 0.04:
            batch.append(items[k]); k += 1
        for _, i, j in batch:
            union(i, j)
        comps = {}
        for i in range(n):
            comps.setdefault(find(i), []).append(i)
        sizes = sorted((len(v) for v in comps.values()), reverse=True)
        if sizes != last_sizes:
            fr = ratapprox(T0)
            print("    delta~% .5f  ~ %-8s  cluster sizes %s" % (T0, str(fr), sizes))
            last_sizes = sizes
            printed += 1
    return ys

def make_1510(seed):
    rng = random.Random(seed)
    avals = [sp.Rational(rng.choice([-3,-2,-1,1,2,3]), rng.choice([1,1,2])) for _ in range(12)]
    a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12 = avals
    B = (y**2 - x**2 + a1*y + a2*x + a3)*y + (a4*x + a5)
    A = sp.expand(B*y + (a6*x + a7))
    h = sp.expand(A*y + a8)
    beta = sp.expand(a9*A + a10*y + a11*x + a12)
    q, r = sp.div(sp.Poly(sp.expand(beta**2), y), sp.Poly(h, y), y)
    alpha = sp.expand(q.as_expr())
    f = sp.expand(h**2 + 2*beta)
    g = sp.expand(h**3 + 3*beta*h + sp.Rational(3, 2)*alpha)
    return f, g, h, avals

def make_1612(seed):
    rng = random.Random(seed)
    def rQ():
        return sp.Rational(rng.choice([-3,-2,-1,1,2,3]), rng.choice([1,1,2]))
    b1,b2,b3,b4 = [rQ() for _ in range(4)]
    h = sp.expand(y**3*(y-x) + b1*y**3 + b2*y**2 + b3*y + b4)
    A = sp.expand(sp.together((h-b4)/y))
    B = sp.expand(sp.together((h - b3*y - b4)/y**2))
    cs = [rQ() for _ in range(14)]
    alpha1 = cs[0]
    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13 = cs[1:]
    alpha2 = sp.expand(c1*A + c2)
    beta2  = sp.expand(c3*A + c4)
    alpha3 = sp.expand(c5*A + c6*B + c7)
    beta3  = sp.expand(c8*A + c9*B + c10)
    alpha4 = sp.expand(c11*A + c12*B + c13*(y-x))
    g = sp.expand(h**4 + alpha1*h**3 + alpha2*h**2 + alpha3*h + alpha4)
    f = sp.expand(h**3 + beta2*h + beta3)
    return f, g, h, (b1,b2,b3,b4)

def buckets_1510(ys, Xval):
    bp, bm, b0, bo = [], [], [], []
    for z in ys:
        if abs(z-Xval) < 0.3*abs(Xval): bp.append(z)
        elif abs(z+Xval) < 0.3*abs(Xval): bm.append(z)
        elif abs(z) < 0.5*abs(Xval): b0.append(z)
        else: bo.append(z)
    print("    split vs ±X,0: +X:%d -X:%d 0:%d other:%d" % (len(bp), len(bm), len(b0), len(bo)))
    logX = log(abs(Xval))
    for lab, pts in [('+X', bp), ('-X', bm), ('0', b0)]:
        if len(pts)<2: continue
        ds = [-log(abs(pts[i]-pts[j]))/logX for i in range(len(pts)) for j in range(i+1,len(pts)) if abs(pts[i]-pts[j])>0]
        print("      %s (%d): min delta~%.5f ~ %s  max~%.5f  mean|y-c|~%.4g (~|X|^%.4f)" %
              (lab, len(pts), min(ds), ratapprox(min(ds)), max(ds),
               np.mean([abs(z - (Xval if lab=='+X' else (-Xval if lab=='-X' else 0))) for z in pts]),
               log(np.mean([abs(z - (Xval if lab=='+X' else (-Xval if lab=='-X' else 0))) for z in pts]))/log(abs(Xval))))

def newton_inf(P):
    pts = []
    Po = sp.Poly(sp.expand(P), x, y)
    for (i,j), c in zip(Po.monoms(), Po.coeffs()):
        if c: pts.append((i,j,c))
    imax = max(i for i,j,c in pts)
    raw = {}
    for i,j,c in pts:
        a = imax-i
        raw[(a,j)] = raw.get((a,j), 0)+c
    by_b = {}
    for (a,b),c in raw.items():
        if c==0: continue
        by_b[b] = min(a, by_b.get(b,a))
    hull=[]
    for b in sorted(by_b):
        a=by_b[b]
        while len(hull)>=2:
            a0,b0=hull[-2]; a1,b1=hull[-1]
            cr=(a1-a0)*(b-b0)-(b1-b0)*(a-a0)
            if cr<=0: hull.pop()
            else: break
        hull.append((a,b))
    edges=[]
    for k in range(len(hull)-1):
        a1,b1=hull[k]; a2,b2=hull[k+1]
        if a2==a1: continue
        mu = Fr(a1-a2, b2-b1)
        edges.append((mu, b1, b2, -mu))  # mu=ord_t(y), y~x^{-mu}
    return hull, edges

print("CONVENTION: t=x^{-1};  delta = ord_t(yi-yj) ~ -log|yi-yj|/log|X|")
print("p.207 printed: (16,12) (-1, 1/4);  (15,10) V2=3: (-1, 1/2)")

Xs = [1e3, 1e4, 1e5]

for seed in (20260903, 17, 99):
    f,g,h,av = make_1510(seed)
    print("\n======== (15,10) seed=%s a=%s ========" % (seed, av))
    print("  deg_y f,g,h =", sp.degree(f,y), sp.degree(g,y), sp.degree(h,y),
          " total", sp.total_degree(f), sp.total_degree(g), sp.total_degree(h))
    print("  Newton-inf f:", newton_inf(f)[1])
    print("  Newton-inf g:", newton_inf(g)[1])
    print("  Newton-inf g-1:", newton_inf(g-1)[1])
    print("  Newton-inf h:", newton_inf(h)[1])
    for Xval in Xs:
        print("  -- X=%g --" % Xval)
        ys = roots_scaled(f, Xval)
        tree_report(ys, Xval, "f")
        buckets_1510(ys, Xval)
        if Xval == Xs[-1] or seed==20260903:
            ys2 = roots_scaled(g-1, Xval)
            tree_report(ys2, Xval, "g-1")
            buckets_1510(ys2, Xval)

for seed in (20260903, 7):
    f,g,h,bv = make_1612(seed)
    print("\n======== (16,12) seed=%s b=%s ========" % (seed, bv))
    print("  deg_y f,g,h =", sp.degree(f,y), sp.degree(g,y), sp.degree(h,y),
          " total", sp.total_degree(f), sp.total_degree(g), sp.total_degree(h))
    print("  Newton-inf f:", newton_inf(f)[1])
    print("  Newton-inf g:", newton_inf(g)[1])
    print("  Newton-inf g-1:", newton_inf(g-1)[1])
    print("  Newton-inf h:", newton_inf(h)[1])
    for Xval in Xs:
        print("  -- X=%g --" % Xval)
        ys = roots_scaled(f, Xval)
        tree_report(ys, Xval, "f")
        # split vs X and 0
        bX, b0, bo = [], [], []
        for z in ys:
            if abs(z-Xval)<0.3*abs(Xval): bX.append(z)
            elif abs(z)<0.5*abs(Xval): b0.append(z)
            else: bo.append(z)
        print("    split vs X,0: X:%d 0:%d other:%d" % (len(bX), len(b0), len(bo)))
        logX=log(abs(Xval))
        for lab,pts in [('X',bX),('0',b0)]:
            if len(pts)<2: continue
            ds=[-log(abs(pts[i]-pts[j]))/logX for i in range(len(pts)) for j in range(i+1,len(pts)) if abs(pts[i]-pts[j])>0]
            cen = Xval if lab=='X' else 0
            mean = np.mean([abs(z-cen) for z in pts])
            print("      %s (%d): min delta~%.5f ~ %s  mean|y-c|~%.4g (~|X|^%.4f)" %
                  (lab, len(pts), min(ds), ratapprox(min(ds)), mean, log(mean)/log(abs(Xval))))
        if seed==20260903 and Xval==Xs[-1]:
            ys2=roots_scaled(g-1, Xval)
            tree_report(ys2, Xval, "g-1")
