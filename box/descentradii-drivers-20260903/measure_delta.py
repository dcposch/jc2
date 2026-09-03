#!/usr/bin/env python3
"""DESCENT-RADII (B): measure logarithmic radii of Moh's (15,10) and (16,12)
Appendix-II shapes.

Convention (SOURCE-READ, Prop 5.1 p.173 + Remark p.146 + Intro p.141):
  t = x^{-1};
  the roots tau are Puiseux series in t for y, of f=0 / g=c / g=0;
  |tau_i - tau_j| = 2^{-ord_t(tau_i-tau_j)};
  logarithmic radius of a disc D = min { ord_t(tau_i - tau_j) : tau_i, tau_j in D },
  which is also -log2 of the nonarchimedean radius.
  Top disc of a pair whose highest form has >=2 distinct linear factors has delta = -1.

Measurement: (i) exact Newton-polygon leading exponents over Q;
(ii) high-precision numerical roots at several large X, pairwise contact
delta_ij = - log|yi-yj| / log|X|, rational-reconstructed.
"""
from fractions import Fraction as Fr
from math import gcd, log
import random
import numpy as np
import sympy as sp
import mpmath as mp

x, y = sp.symbols('x y')

# ---------- continued-fraction rational reconstruction ----------
def ratapprox(val, bound=64):
    """best Fraction with den<=bound; also return residual."""
    if val != val or abs(val) > 1e6:
        return None, val
    a = abs(val); sign = 1 if val >= 0 else -1
    fr = Fr(a).limit_denominator(bound)
    return sign * fr, val - sign * float(fr)

# ---------- Newton polygon at x = infinity ----------
def support(poly, xx, yy):
    P = sp.Poly(sp.expand(poly), xx, yy)
    return [(i, j, c) for (i, j), c in zip(P.monoms(), P.coeffs()) if c != 0]

def newton_edges_infinity(poly, xx, yy):
    """Newton polygon of P(t^{-1}, y)*t^{max_i} at t=0.
    Points: (alpha, beta) = (max_i - i, j) for monomial x^i y^j.
    Lower convex hull from smallest beta to largest, left-to-right in alpha.
    Each edge of slope -mu (dy/dalpha = -mu) gives y ~ t^{mu} = x^{-mu},
    i.e. ord_t(y) = mu, so y ~ x^{-mu}.
    Returns list of (mu=Fraction, y_exponents on the edge, leading poly in z= y t^{-mu}).
    """
    pts = support(poly, xx, yy)
    if not pts:
        return []
    imax = max(i for i, j, c in pts)
    # points (a, b) = (imax-i, j)
    raw = {}
    for i, j, c in pts:
        a = imax - i
        key = (a, j)
        raw[key] = raw.get(key, 0) + c
    pts2 = [(a, b) for (a, b), c in raw.items() if c != 0]
    # lower hull: for each b, the minimal a
    by_b = {}
    for a, b in pts2:
        by_b[b] = min(a, by_b.get(b, a))
    bs = sorted(by_b)
    hull = []
    for b in bs:
        a = by_b[b]
        while len(hull) >= 2:
            a0, b0 = hull[-2]
            a1, b1 = hull[-1]
            # cross of (a1-a0,b1-b0) x (a-a1,b-b1) : keep right turns for LOWER hull
            # we want increasing b, and the lower-left envelope in (a,b) with a to the right being higher t-order
            # slope da/db should be nondecreasing (convex from below in the (b,a) plot? )
            # Standard: plot a horizontal, b vertical. Lower hull = minimal a for the envelope.
            # Actually we plot (a, b) with a = t-valuation of coeff, b = y-power.
            # Newton polygon = lower convex hull (small a).
            # Edge from (a1,b1) to (a,b): slope s = (b-b1)/(a-a1) if a>a1.
            # Cross product (a1-a0, b1-b0) x (a-a0, b-b0) = (a1-a0)*(b-b0)-(b1-b0)*(a-a0)
            # For LOWER hull in (a,b) with b up, a right: we want clockwise = negative cross if a is x and b is y.
            cr = (a1 - a0) * (b - b0) - (b1 - b0) * (a - a0)
            if cr <= 0:
                hull.pop()
            else:
                break
        hull.append((a, b))
    # filter to true lower: drop vertical-only at the start if needed
    edges = []
    for k in range(len(hull) - 1):
        a1, b1 = hull[k]
        a2, b2 = hull[k + 1]
        if a2 == a1:
            continue  # vertical
        # mu = (b2-b1)/(a2-a1)?  NO.
        # On the edge, t^a y^b ~ 1, y^b ~ t^{-a}, y ~ t^{-a/b wait}
        # monomial t^a y^b : if y ~ t^mu z, t^a t^{mu b} z^b, valuation a + mu b equal on the edge.
        # a1 + mu b1 = a2 + mu b2  => mu (b2-b1) = a1-a2 => mu = (a1-a2)/(b2-b1)
        mu = Fr(a1 - a2, b2 - b1)
        # leading polynomial: sum c z^b over points on the edge
        # val = a + mu * b constant on edge
        val0 = a1 + mu * b1
        terms = []
        for (a, b), c in raw.items():
            if a + mu * b == val0:
                terms.append((b, c))
        terms.sort()
        z = sp.symbols('z')
        lp = sum(c * z**b for b, c in terms)
        edges.append((mu, terms, sp.expand(lp)))
    return hull, edges

def format_edges(edges):
    out = []
    for mu, terms, lp in edges:
        out.append("    mu=%s  (y ~ t^{%s} = x^{%s})  lead=%s" % (mu, mu, -mu, lp))
    return "\n".join(out)

# ---------- numerical disc tree ----------
def poly_in_y_coeffs(P, xx, yy, Xval):
    """numeric coefficients [a0..an] of P(Xval, y) as a polynomial in y (low to high)."""
    Pex = sp.expand(P)
    d = sp.degree(Pex, yy)
    coeffs = []
    for k in range(d + 1):
        ck = sp.expand(Pex.coeff(yy, k))
        coeffs.append(complex(ck.subs(xx, Xval)))
    return coeffs  # a0..an

def roots_at(P, xx, yy, Xval, dps=80):
    coeffs = poly_in_y_coeffs(P, xx, yy, Xval)  # low to high
    mp.mp.dps = dps
    # mpmath wants high-to-low
    hi = [mp.mpc(c.real, c.imag) for c in coeffs[::-1]]
    # scale for numerical stability: y = s z with s = |Xval|
    # P = sum a_k y^k = sum a_k s^k z^k
    s = abs(Xval)
    scaled = []
    pows = mp.mpf(1)
    # hi[0] is a_n, hi[-1] is a_0
    n = len(hi) - 1
    # work unscaled first; if it fails, scale
    try:
        rts = mp.polyroots(hi, extra_roots=0, maxsteps=200)
        return [complex(r) for r in rts]
    except Exception:
        pass
    # scale y = s*z
    his = []
    for i, a in enumerate(hi):  # i=0 is y^n
        his.append(a * (mp.mpf(s) ** (n - i)))
    rts = mp.polyroots(his, extra_roots=0, maxsteps=200)
    return [complex(r) * s for r in rts]

def pairwise_deltas(ys, Xval):
    n = len(ys)
    D = {}
    logX = log(abs(Xval))
    for i in range(n):
        for j in range(i + 1, n):
            d = abs(ys[i] - ys[j])
            if d == 0:
                delta = float('inf')
            else:
                # |yi-yj| ~ C |X|^{-delta}  => delta = - log(d)/log|X|   (C absorbed for large X)
                delta = -log(d) / logX
            D[(i, j)] = (delta, d)
    return D

def cluster_tree(ys, Xval, gaps=None):
    """Single-linkage clustering of roots by estimated delta = -log|yi-yj|/log|X|.
    Returns a list of (delta, list of clusters as index-sets) at each split.
    """
    n = len(ys)
    D = pairwise_deltas(ys, Xval)
    # unique deltas, sorted increasing (coarsest contact first: more negative / smaller)
    vals = sorted(set(round(D[p][0], 6) for p in D if D[p][0] == D[p][0]))
    # hierarchical: at threshold T, i~j if delta_ij >= T  (they agree at least to T)
    # A disc of radius T contains roots with pairwise ord >= T.
    report = []
    # start from coarsest
    for T in vals:
        parent = list(range(n))
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra
        for (i, j), (delta, d) in D.items():
            if delta >= T - 1e-4:
                union(i, j)
        comps = {}
        for i in range(n):
            comps.setdefault(find(i), []).append(i)
        sizes = sorted((len(v) for v in comps.values()), reverse=True)
        report.append((T, sizes, comps))
    return report, D

def summarize_tree(ys, Xval, label, expected_top=-1):
    report, D = cluster_tree(ys, Xval)
    print("  [%s] |X|=%g  nroots=%d  min|y|=%.3g max|y|=%.3g" %
          (label, abs(Xval), len(ys), min(abs(z) for z in ys), max(abs(z) for z in ys)))
    # print the coarsest few distinct delta levels
    seen_sizes = None
    levels = []
    for T, sizes, comps in report:
        if sizes != seen_sizes:
            fr, res = ratapprox(T, 48)
            levels.append((T, fr, res, sizes))
            seen_sizes = sizes
    print("    contact levels (delta, reconstructed, cluster sizes):")
    for T, fr, res, sizes in levels[:12]:
        print("      delta~%.6f  ~ %s  (resid %.2e)  sizes %s" % (T, fr, res, sizes))
    return levels, D

# ---------- (15,10) shape ----------
def make_1510(rng=None, avals=None):
    if avals is None:
        rng = rng or random.Random(20260903)
        # admissible rationals, avoid 0 for a8,a9 to stay generic
        avals = []
        for i in range(12):
            num = rng.choice([-3, -2, -1, 1, 2, 3])
            den = rng.choice([1, 1, 1, 2, 3])
            avals.append(sp.Rational(num, den))
    a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12 = avals
    B = (y**2 - x**2 + a1*y + a2*x + a3)*y + (a4*x + a5)
    A = sp.expand(B*y + (a6*x + a7))
    h = sp.expand(A*y + a8)
    beta = sp.expand(a9*A + a10*y + a11*x + a12)
    q, r = sp.div(sp.Poly(sp.expand(beta**2), y), sp.Poly(h, y), y)
    alpha = sp.expand(q.as_expr())
    f = sp.expand(h**2 + 2*beta)
    g = sp.expand(h**3 + 3*beta*h + sp.Rational(3, 2)*alpha)
    return dict(h=h, beta=beta, alpha=alpha, f=f, g=g, a=avals,
                A=A, B=B)

# ---------- (16,12) shape of p.208 ----------
def make_1612(rng=None):
    rng = rng or random.Random(20260903)
    def rQ():
        return sp.Rational(rng.choice([-3,-2,-1,1,2,3]), rng.choice([1,1,2]))
    b1,b2,b3,b4 = [rQ() for _ in range(4)]
    h = sp.expand(y**3*(y - x) + b1*y**3 + b2*y**2 + b3*y + b4)
    # A, B as on p.208: h = y A + b4 = y^2 B + b3 y + b4
    A = sp.expand((h - b4)/y)          # y^3 - x y^2 + b1 y^2 + b2 y + b3
    B = sp.expand((h - b3*y - b4)/y**2)  # y^2 - x y + b1 y + b2? wait
    # α1 constant; α2 = c1 A + c2; β2 = c3 A + c4
    # α3 = c5 A + c6 B + c7; β3 = c8 A + c9 B + c10
    # α4 = c11 A + c12 B + c13 (y-x)
    cs = [rQ() for _ in range(13)]
    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13 = cs
    alpha1 = c1  # reuse c1 as the constant; keep 13 coeffs as on p.208
    # actually α1 is a constant independent; use cs[0] as α1, shift
    alpha1 = rQ()
    alpha2 = sp.expand(c1*A + c2)
    beta2  = sp.expand(c3*A + c4)
    alpha3 = sp.expand(c5*A + c6*B + c7)
    beta3  = sp.expand(c8*A + c9*B + c10)
    alpha4 = sp.expand(c11*A + c12*B + c13*(y - x))
    g = sp.expand(h**4 + alpha1*h**3 + alpha2*h**2 + alpha3*h + alpha4)
    f = sp.expand(h**3 + beta2*h + beta3)
    return dict(h=h, f=f, g=g, A=A, B=B,
                alphas=(alpha1, alpha2, alpha3, alpha4),
                betas=(beta2, beta3),
                b=(b1,b2,b3,b4), cs=cs)

def run_one(shape, tag, Xs, which=('f', 'g', 'gm1')):
    print("\n==== %s ====" % tag)
    h, f, g = shape['h'], shape['f'], shape['g']
    print("  deg_y h,f,g =", sp.degree(h, y), sp.degree(f, y), sp.degree(g, y))
    print("  total deg h,f,g =", sp.total_degree(h), sp.total_degree(f), sp.total_degree(g))
    print("  Newton polygon of f at x=∞:")
    hull, edges = newton_edges_infinity(f, x, y)
    print("    hull (t-val, y-exp) =", hull)
    print(format_edges(edges))
    print("  Newton polygon of g at x=∞:")
    hullg, edgesg = newton_edges_infinity(g, x, y)
    print("    hull =", hullg)
    print(format_edges(edgesg))
    print("  Newton polygon of g-1 at x=∞:")
    hullc, edgesc = newton_edges_infinity(g - 1, x, y)
    print("    hull =", hullc)
    print(format_edges(edgesc))

    polys = {}
    if 'f' in which: polys['f'] = f
    if 'g' in which: polys['g'] = g
    if 'gm1' in which: polys['g-1'] = g - 1
    if 'h' in which: polys['h'] = h

    results = {}
    for Xval in Xs:
        print("\n  -- numerical roots at X = %s --" % Xval)
        for name, P in polys.items():
            try:
                ys = roots_at(P, x, y, Xval, dps=60)
            except Exception as e:
                print("    ROOT FAIL %s at X=%s: %s" % (name, Xval, e))
                continue
            levels, D = summarize_tree(ys, Xval, name)
            results[(name, Xval)] = (levels, ys)
            # special: for f, check 2,2,6 split of the three clusters around ±X and 0
            if name == 'f' and tag.startswith('(15,10)'):
                classify_226(ys, Xval)
            if name == 'f' and tag.startswith('(16,12)'):
                classify_1612_f(ys, Xval)
    return results

def classify_226(ys, Xval):
    """Moh p.210: three subdiscs of D2 contain 2, 2, 6 roots of f."""
    # expected centers: y ~ X, y ~ -X, y ~ 0
    buckets = {'+X': [], '-X': [], '0': [], 'other': []}
    for i, z in enumerate(ys):
        if abs(z - Xval) < 0.25 * abs(Xval):
            buckets['+X'].append(z)
        elif abs(z + Xval) < 0.25 * abs(Xval):
            buckets['-X'].append(z)
        elif abs(z) < 0.5 * abs(Xval):
            buckets['0'].append(z)
        else:
            buckets['other'].append(z)
    print("    subdisc split vs ±X, 0: +X:%d  -X:%d  0:%d  other:%d" %
          (len(buckets['+X']), len(buckets['-X']), len(buckets['0']), len(buckets['other'])))
    logX = log(abs(Xval))
    for lab, pts in buckets.items():
        if len(pts) < 2:
            continue
        ds = []
        for i in range(len(pts)):
            for j in range(i+1, len(pts)):
                d = abs(pts[i]-pts[j])
                ds.append(-log(d)/logX if d else float('inf'))
        fr, _ = ratapprox(min(ds), 48)
        print("      inside %s (%d roots): min delta ~ %.6f ~ %s ; max delta ~ %.6f" %
              (lab, len(pts), min(ds), fr, max(ds)))
        # also the scale of the cluster: mean |y - center|
        if lab == '0':
            scale = np.mean([abs(z) for z in pts])
            print("        mean |y| of 0-cluster = %.6g  ~ |X|^{%.4f}" %
                  (scale, log(scale)/log(abs(Xval)) if scale else 0))
        elif lab == '+X':
            scale = np.mean([abs(z - Xval) for z in pts])
            print("        mean |y-X| = %.6g  ~ |X|^{%.4f}" %
                  (scale, log(scale)/log(abs(Xval)) if scale else 0))

def classify_1612_f(ys, Xval):
    buckets = {'X': [], '0': [], 'other': []}
    for z in ys:
        if abs(z - Xval) < 0.25 * abs(Xval):
            buckets['X'].append(z)
        elif abs(z) < 0.5 * abs(Xval):
            buckets['0'].append(z)
        else:
            buckets['other'].append(z)
    print("    subdisc split vs X, 0: X:%d  0:%d  other:%d" %
          (len(buckets['X']), len(buckets['0']), len(buckets['other'])))
    logX = log(abs(Xval))
    for lab, pts in buckets.items():
        if len(pts) < 2:
            continue
        ds = [(-log(abs(pts[i]-pts[j]))/logX)
              for i in range(len(pts)) for j in range(i+1, len(pts))
              if abs(pts[i]-pts[j]) > 0]
        if not ds:
            continue
        fr, _ = ratapprox(min(ds), 48)
        print("      inside %s (%d roots): min delta ~ %.6f ~ %s" % (lab, len(pts), min(ds), fr))
        if lab == '0':
            scale = np.mean([abs(z) for z in pts])
            print("        mean |y| of 0-cluster = %.6g  ~ |X|^{%.4f}" %
                  (scale, log(scale)/log(abs(Xval)) if scale else 0))

def main():
    Xs = [10**4, 10**5, 3*10**5]
    print("CONVENTION: t=x^{-1}; delta = ord_t(tau_i-tau_j) = -log|yi-yj|/log|X|  (large-X limit)")
    print("Printed p.207: (16,12) delta2=-1, delta1=1/4; (15,10) V2=3: delta2=-1, delta1=1/2")

    # several draws of (15,10)
    for draw, seed in enumerate([20260903, 17, 99]):
        rng = random.Random(seed)
        sh = make_1510(rng=rng)
        print("\n### (15,10) draw %d  a=%s" % (draw, sh['a']))
        run_one(sh, "(15,10) draw%d" % draw, Xs if draw == 0 else [10**5],
                which=('f', 'g-1') if draw == 0 else ('f',))

    sh16 = make_1612(rng=random.Random(20260903))
    print("\n### (16,12)  b=%s" % (sh16['b'],))
    run_one(sh16, "(16,12)", Xs, which=('f', 'g-1'))

    # a second (16,12) draw
    sh16b = make_1612(rng=random.Random(7))
    run_one(sh16b, "(16,12) draw1", [10**5], which=('f',))

if __name__ == '__main__':
    main()
