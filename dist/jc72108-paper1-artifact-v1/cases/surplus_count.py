#!/usr/bin/env python3
"""Lattice-arithmetic surplus count for the vertex-gap lemma condition (iii).

Given a strip family (corners of N(P), N(Q), rhs x^k) satisfying hypothesis
(i) (vertex normalization) and the symmetrized gap condition, compute on the
near-origin block (Minkowski columns k+1, k+2, after the gap columns are
killed):

  n_keys      forced-vanishing bracket keys in the block (vertex key (k+1,1)
              and identically-zero keys excluded)
  n_unknowns  eliminable coefficients = ground truth from an in-block cascade
              (M2 single-monomial zeroings + unit-cofactor eliminations of
              gap-side coefficients, eager substitution); gap-column variables
              are excluded by construction (they die below the block)
  surplus     n_keys - n_unknowns = number of leftover equations; each
              leftover is classified PINS (reduces to unit * nonunit-monomial:
              the obstruction (unit)*M*b_q0 = 0) / TRIVIAL (reduces to 0) /
              OTHER.

Orientation is normalized so the gap side is Q ((q0)_x = max); a_{p0}, b_{q0}
are treated as units per hypothesis (i).  Exact Fraction arithmetic; block
local only (valid by the localization result, LEMMA-REVIEW front 4.3).
Self-contained: no repo lib imports.  See SURPLUS.md.
"""
from collections import defaultdict
from fractions import Fraction
from math import gcd

# ---------------- lattice geometry ----------------

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def hull(pts):
    pts = sorted(set(pts))
    if len(pts) <= 2:
        return pts
    def half(ps):
        h = []
        for p in ps:
            while len(h) >= 2 and cross(h[-2], h[-1], p) <= 0:
                h.pop()
            h.append(p)
        return h
    lo, up = half(pts), half(pts[::-1])
    return lo[:-1] + up[:-1]                      # counterclockwise

def lattice_points(corners):
    H = hull(corners)
    xs = [p[0] for p in H]; ys = [p[1] for p in H]
    pts = [(x, y)
           for x in range(min(xs), max(xs) + 1)
           for y in range(min(ys), max(ys) + 1)
           if all(cross(H[i], H[(i+1) % len(H)], (x, y)) >= 0
                  for i in range(len(H)))]
    return pts, H

def primitive(v):
    g = gcd(abs(v[0]), abs(v[1]))
    return (v[0]//g, v[1]//g)

class Strip:
    """Polygon with origin corner, top edge through origin along d, bottom
    corner p0 adjacent to origin."""
    def __init__(self, corners, tag):
        self.tag = tag
        self.pts, H = lattice_points(corners)
        assert (0, 0) in H, f"{tag}: origin not a corner"
        i0 = H.index((0, 0))
        self.p0 = H[(i0+1) % len(H)]              # CCW successor = bottom corner
        top = H[(i0-1) % len(H)]                  # CCW predecessor = top far corner
        self.d = primitive(top)
        d1, d2 = self.d
        assert d1 == 1, f"{tag}: d1 != 1 unhandled (sparse columns)"
        self.w = lambda p: d2*p[0] - d1*p[1]
        ws = [self.w(p) for p in self.pts]
        assert min(ws) == 0, f"{tag}: top edge not through origin"
        self.width = max(ws)
        assert self.w(self.p0) == self.width, f"{tag}: bottom corner not saturated"
        assert all(p == (0, 0) for p in self.pts if p[0] == 0), \
            f"{tag}: y-axis support (breaks gap-kill; c1 regime)"
        self.cols = defaultdict(list)
        for p in self.pts:
            self.cols[p[0]].append(p)

# ---------------- tiny exact polynomial engine ----------------
# variable = ('a'|'b', point); monomial = tuple(sorted((var, exp)));
# poly = {monomial: Fraction}.  Units may carry negative exponents.

def mono(d):
    return tuple(sorted((v, e) for v, e in d.items() if e))

def mmul(m1, m2):
    d = defaultdict(int)
    for v, e in m1: d[v] += e
    for v, e in m2: d[v] += e
    return mono(d)

def padd_into(p, m, c):
    c2 = p.get(m, Fraction(0)) + c
    if c2: p[m] = c2
    elif m in p: del p[m]

def pmul(p1, p2):
    r = {}
    for m1, c1 in p1.items():
        for m2, c2 in p2.items():
            padd_into(r, mmul(m1, m2), c1*c2)
    return r

def ppow(p, e):
    r = {(): Fraction(1)}
    for _ in range(e):
        r = pmul(r, p)
    return r

def psubst(p, v, expr):
    """substitute variable v := expr (a poly) in p"""
    r = {}
    for m, c in p.items():
        ex = dict(m).get(v, 0)
        if not ex:
            padd_into(r, m, c)
        else:
            base = mono({vv: ee for vv, ee in m if vv != v})
            for m2, c2 in ppow(expr, ex).items():
                padd_into(r, mmul(base, m2), c*c2)
    return r

def mstr(m):
    return "*".join(f"{v[0]}{v[1]}^{e}" if e != 1 else f"{v[0]}{v[1]}"
                    for v, e in m) or "1"

def torus_probe(polys, units, tries=80, seed=20260804):
    """Numeric probe: do the leftover polys admit a common zero with every
    non-unit variable nonzero (units set to 1)?  Returns a verdict string."""
    import random
    rng = random.Random(seed)
    eqs = [p for p in polys if p]
    if not eqs:
        return "no constraint"
    vs = sorted({v for p in eqs for m in p for v, e in m if v not in units})
    def ev(p, x):
        s = 0.0
        for m, c in p.items():
            t = float(c)
            for v, e in m:
                t *= x.get(v, 1.0) ** e
            s += t
        return s
    n, m = len(vs), len(eqs)
    for _ in range(tries):
        sol = rng.sample(vs, min(m, n))
        x = {v: rng.uniform(0.3, 2.0) * rng.choice([-1, 1]) for v in vs}
        ok = False
        for _ in range(60):
            F = [ev(p, x) for p in eqs]
            if max(abs(f) for f in F) < 1e-11:
                ok = True
                break
            J = [[(ev(p, {**x, v: x[v] + 1e-7}) - f) / 1e-7 for v in sol]
                 for p, f in zip(eqs, F)]
            # Gauss-Newton step via normal equations (tiny dense system)
            k = len(sol)
            A = [[sum(J[r][i]*J[r][j] for r in range(m)) for j in range(k)]
                 for i in range(k)]
            b = [-sum(J[r][i]*F[r] for r in range(m)) for i in range(k)]
            for i in range(k):                    # gaussian elim, partial pivot
                piv = max(range(i, k), key=lambda r: abs(A[r][i]))
                if abs(A[piv][i]) < 1e-14:
                    break
                A[i], A[piv] = A[piv], A[i]
                b[i], b[piv] = b[piv], b[i]
                for r in range(i+1, k):
                    f = A[r][i] / A[i][i]
                    for c2 in range(i, k):
                        A[r][c2] -= f * A[i][c2]
                    b[r] -= f * b[i]
            dx = [0.0]*k
            for i in range(k-1, -1, -1):
                if abs(A[i][i]) < 1e-14:
                    continue
                dx[i] = (b[i] - sum(A[i][j]*dx[j] for j in range(i+1, k))) / A[i][i]
            for v, d in zip(sol, dx):
                x[v] = x[v] + max(-1.0, min(1.0, d))
        if ok and all(1e-4 < abs(x[v]) < 1e4 for v in vs):
            return f"torus-solvable ({n} vars, {m} eqs): P-constraint, no empty-chart obstruction"
    return f"NO torus point found ({n} vars, {m} eqs): candidate obstruction"

# ---------------- the analysis ----------------

def analyze(name, cornersP, cornersQ, k, depth=2, verbose=True):
    """depth D block: P cols 1..D, Q cols k..k+D-1, Minkowski cols k+1..k+D.
    Self-contained for every D >= 2 (lower P/Q columns are gap or origin)."""
    P, Q = Strip(cornersP, "P"), Strip(cornersQ, "Q")
    assert P.d == Q.d, "no common strip direction"
    swapped = False
    if P.p0[0] > Q.p0[0]:                        # normalize: gap side = Q
        P, Q = Q, P
        swapped = True
    p0, q0 = P.p0, Q.p0
    d2 = P.d[1]
    tgt = (k+1, 1)
    assert (p0[0]+q0[0], p0[1]+q0[1]) == tgt, "p0+q0 != (k+1,1)"

    # hypothesis (i): unique det!=0 decomposition of the vertex, |det| = 1
    sq = set(Q.pts)
    decs = [(p, (tgt[0]-p[0], tgt[1]-p[1])) for p in P.pts
            if (tgt[0]-p[0], tgt[1]-p[1]) in sq]
    live_decs = [(p, q) for p, q in decs if p[0]*q[1] - p[1]*q[0] != 0]
    assert live_decs == [(p0, q0)], f"(i) fails: {live_decs}"
    vdet = p0[0]*q0[1] - p0[1]*q0[0]
    assert abs(vdet) == 1, f"(i) fails: det = {vdet}"

    # gap columns 1..(q0)_x - 1 of Q: verify triangular-kill structure (y >= 1)
    gap_cols = list(range(1, q0[0]))
    for g in gap_cols:
        assert all(q[1] >= 1 for q in Q.cols[g]), "gap point on x-axis"

    units = {('a', p0), ('b', q0)}

    # block equations: live pairs P cols 1..D x Q cols k..k+D-1
    D = depth
    mcols = set(range(k+1, k+D+1))
    livP = sum((P.cols[c] for c in range(1, D+1)), [])
    livQ = sum((Q.cols[c] for c in range(k, k+D)), [])
    eqs = defaultdict(dict)
    for p in livP:
        for q in livQ:
            X = p[0] + q[0]
            if X not in mcols:
                continue
            D = p[0]*q[1] - p[1]*q[0]
            if D == 0:
                continue
            padd_into(eqs[(X, p[1]+q[1])],
                      mono({('a', p): 1, ('b', q): 1}), Fraction(D))
    eqs = {m: e for m, e in eqs.items() if e}
    vtx = eqs.pop(tgt)
    assert list(vtx.values()) in ([Fraction(1)], [Fraction(-1)]) \
        and set(dict(next(iter(vtx))).keys()) == units, "vertex eq malformed"

    n_keys = len(eqs)
    ncol = {X: sum(1 for m in eqs if m[0] == X) for X in sorted(mcols)}
    level = lambda m: (d2*m[0] + m[1], m)

    # ---- in-block cascade ----
    active = {m: dict(e) for m, e in eqs.items()}
    zeroedP, zeroedQ, exprQ = [], [], []
    def subst_all(v, expr, skip):
        for mk in list(active):
            if mk != skip:
                active[mk] = psubst(active[mk], v, expr)
    progress = True
    while progress:
        progress = False
        # M2: single-monomial equation with exactly one distinct non-unit var
        for mk in sorted(active, key=level):
            e = active[mk]
            if len(e) == 1:
                m, c = next(iter(e.items()))
                nu = [v for v, ex in m if v not in units]
                if len(nu) == 1:
                    v = nu[0]
                    del active[mk]
                    (zeroedP if v[0] == 'a' else zeroedQ).append(v)
                    subst_all(v, {}, None)
                    progress = True
                    break
        if progress:
            continue
        # elimination: gap-side (b) var, exp 1, unit cofactors, sole occurrence
        cands = []
        for mk in sorted(active, key=level):
            e = active[mk]
            for m, c in e.items():
                lin = [(v, ex) for v, ex in m if v not in units]
                if len(lin) == 1 and lin[0][1] == 1 and lin[0][0][0] == 'b':
                    v = lin[0][0]
                    if sum(1 for mm in e if v in dict(mm)) == 1:
                        cands.append((level(mk), len(e), v, mk, m, c))
        if cands:
            _, _, v, mk, m, c = min(cands)
            inv = mono({vv: -ee for vv, ee in m if vv != v})   # unit inverse
            expr = {}
            for m2, c2 in active[mk].items():
                if m2 != m:
                    padd_into(expr, mmul(m2, inv), -c2/c)
            del active[mk]
            exprQ.append(v)
            subst_all(v, expr, None)
            progress = True

    n_unknowns = len(zeroedP) + len(zeroedQ) + len(exprQ)
    surplus = n_keys - n_unknowns
    assert surplus == len(active)

    # leftover classification
    leftovers = []
    for mk in sorted(active, key=level):
        e = active[mk]
        if not e:
            leftovers.append((mk, "TRIVIAL", ""))
        elif len(e) == 1:
            m, c = next(iter(e.items()))
            nu = mono({v: ex for v, ex in m if v not in units})
            if nu:
                leftovers.append((mk, "PINS", f"{c}*unit*{mstr(nu)}"))
            else:
                leftovers.append((mk, "UNIT-CONST", str(c)))
        else:
            leftovers.append((mk, "OTHER", f"{len(e)} monomials"))
    probe = ""
    if any(cl == "OTHER" for _, cl, _ in leftovers):
        probe = torus_probe([active[mk] for mk in active], units)

    res = dict(name=name, d=P.d, k=k, wP=P.width, wQ=Q.width, swapped=swapped,
               probe=probe,
               n_keys=n_keys, ncol=ncol, nQ=len(zeroedQ)+len(exprQ),
               nP=len(zeroedP), n_unknowns=n_unknowns, surplus=surplus,
               leftovers=leftovers, zeroedP=zeroedP,
               formula_keys=2*(P.width+Q.width) - 1)
    if verbose:
        lo = "; ".join(f"{mk}:{cl} {info}" for mk, cl, info in leftovers)
        print(f"== {name}: d={P.d} k={k} wP={P.width} wQ={Q.width} "
              f"swapped={swapped} (i) OK det={vdet}")
        print(f"   n_keys={n_keys} (cols {ncol})  "
              f"closed-form 2(wP+wQ)-1={res['formula_keys']}"
              f" {'MATCH' if res['formula_keys']==n_keys else 'MISMATCH'}")
        print(f"   n_unknowns={n_unknowns} (Q-elim {res['nQ']}, "
              f"P-zeroed {len(zeroedP)}: {[mstr(mono({v:1})) for v in zeroedP]})")
        print(f"   surplus={surplus}  leftovers: {lo}")
        if probe:
            print(f"   probe: {probe}")
    return res

# ---------------- families ----------------

FAMILIES = {
    # name: (cornersP, cornersQ, k, expected surplus)
    "open_8_28_c2": ([(0,0),(1,0),(8,14),(8,16)],
                     [(0,0),(2,1),(12,21),(12,24)], 2, 1),
    "swap_8_28_c2": ([(0,0),(2,1),(12,21),(12,24)],
                     [(0,0),(1,0),(8,14),(8,16)], 2, 1),
    "mini_gap":     ([(0,0),(1,0),(4,6),(4,8)],
                     [(0,0),(2,1),(6,9),(6,12)], 2, 1),
    "reg_9_24_c3":  ([(0,0),(1,1),(6,16),(6,18)],
                     [(0,0),(1,0),(9,24),(9,27)], 1, 0),
    "toy_k3":       ([(0,0),(1,0),(5,8),(5,10)],
                     [(0,0),(3,1),(8,11),(8,16)], 3, 1),
    "toy_w3":       ([(0,0),(1,0),(4,9),(4,12)],
                     [(0,0),(2,1),(6,13),(6,18)], 2, 1),
}

def main():
    rows = []
    for name, (cP, cQ, k, exp) in FAMILIES.items():
        r = analyze(name, cP, cQ, k)
        pins = sum(1 for _, cl, _ in r["leftovers"] if cl == "PINS")
        dep = 2
        while pins == 0 and k >= 2 and dep < 5:   # probe deeper blocks
            dep += 1
            r = analyze(name + f"@D{dep}", cP, cQ, k, depth=dep)
            pins = sum(1 for _, cl, _ in r["leftovers"] if cl == "PINS")
        rows.append((name, k, r["d"], r["wP"], r["wQ"], "yes" if k >= 2 else "no",
                     r["n_keys"], r["n_unknowns"], r["surplus"], pins, exp, dep))
    # lock against LEMMA.md ground truth for open_8_28_c2
    r0 = analyze(*(("open_8_28_c2",) + FAMILIES["open_8_28_c2"][:3]), verbose=False)
    assert r0["surplus"] == 1 and r0["leftovers"][0][1] == "PINS"
    assert "a(1, 1)^2" in r0["leftovers"][0][2] and "a(2, 4)" in r0["leftovers"][0][2]
    print("\nfamily          k  d      wP wQ gap  n_keys n_unk surplus PINS expected D")
    for nm, k, d, wP, wQ, gap, nk, nu, s, pins, exp, dep in rows:
        print(f"{nm:15s} {k}  {str(d):6s} {wP}  {wQ}  {gap:4s} {nk:5d} {nu:5d} "
              f"{s:5d}  {pins:3d}  {exp}  {dep}")

def scan():
    """Scope map for phase 2: generic strips (lengths 3 past the corners),
    p0=(1,0), q0=(k,1), top direction d=(1,d2); depth-2 block."""
    print("k d2 | wP wQ | n_keys n_unk surplus | PINS TRIV OTHER | probe")
    for d2 in (1, 2, 3, 4):
        for k in (2, 3, 4, 5):
            cP = [(0,0), (1,0), (4, 3*d2), (4, 4*d2)]
            cQ = [(0,0), (k,1), (k+3, 1+3*d2), (k+3, (k+3)*d2)]
            r = analyze(f"scan_k{k}_d{d2}", cP, cQ, k, verbose=False)
            cls = [cl for _, cl, _ in r["leftovers"]]
            pins, triv = cls.count("PINS"), cls.count("TRIVIAL")
            oth = cls.count("OTHER")
            pr = r["probe"].split("(")[0].strip() if r["probe"] else "-"
            print(f"{k} {d2}  | {r['wP']:2d} {r['wQ']:2d} | {r['n_keys']:5d} "
                  f"{r['n_unknowns']:5d} {r['surplus']:5d}   | {pins:4d} "
                  f"{triv:4d} {oth:5d} | {pr}")

if __name__ == "__main__":
    import sys as _s
    scan() if "scan" in _s.argv else main()
