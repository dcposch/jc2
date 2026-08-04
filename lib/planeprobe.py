"""Plane probe: codimension-2 analog of lineprobe via bivariate elimination.

Restrict P-coefficients to a random plane a(s,t) = a0 + s*a1 + t*a2 over F_p
(corner a-vars get nonzero a0 entries).  The Q-side system M(a(s,t)) b = r(a(s,t))
has entries of degree <= 1 in (s,t).  Fraction-free elimination of the b-columns
leaves residual conditions h_j(s,t) (rows with zero M-part, nonzero rhs); their
common zeros are the (s,t) where the plane meets the solvability locus.

Implementation note (fraction-free elimination).  By the Sylvester identity the
residual rhs entries of one-step fraction-free (Bareiss) elimination are exactly
the bordered minors  h_j = det [ A[P u {j}, C u {rhs}] ]  where (P, C) is the
pivot row/column set.  We compute these h_j directly: fix (P, C) from a numeric
elimination at a random point, evaluate each bordered determinant on an integer
grid (Schur-complement form, one O(r^3) elimination per grid point serving all
residual rows), and recover the h_j by exact Newton interpolation (total degree
<= rank+1).  This is algebraically identical to symbolic fraction-free
elimination but avoids its intermediate expression swell; the 5000-term swell
guard is kept on the h_j (and on resultant degree bounds / wall clock).

Locus analysis.  The bordered minors share a large common content (an artifact
of the fixed pivot block, exactly as un-reduced fraction-free residuals share
pivot factors), so raw pairwise resultants vanish identically.  We therefore
first extract the content along univariate slices (gcd_j h_j(sigma, t) for
random sigma, and transposed slices for pure-s factors) and REALITY-TEST any
common-vanishing curve: sample its F_p-points and check numeric consistency of
M(a) b = r there.  A consistent curve point => the solvability locus really
meets the plane in a curve -> "CURVE", stop.  A never-consistent common factor
is a pivot artifact and is divided out slice-wise.  Then, on the reduced first
five residuals: any pair with identically-zero resultant Res_t (probabilistic
check) is reality-tested the same way (real -> "CURVE"); otherwise R(s) = gcd
of the interpolated pair resultants (times a harmless content-leading-coeff
power), its F_p-roots s0 (primes < 2^21 only), then per s0 the F_p-roots t0 of
gcd_j h_j(s0, t).  Each (s0, t0) is a candidate: rebuild numeric a, require
corner-a nonzero, corner-b realizability via lineprobe._check_point, verify
hits with linprobe.verify_witness.  Spurious candidates from dropped/extra
factors are harmless: every candidate is checked numerically.
"""
import os, sys, time, random
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from linprobe import classify, verify_witness
from lineprobe import _check_point, fp_roots, pgcd_, pdivexact, peval, ptrim

MAX_TERMS = 5000        # swell guard on any residual polynomial
RES_MAX = 6000          # cap on resultant interpolation degree
ROOTS_MAX = 800         # cap on deg R(s) for root finding
CURVE_SAMPLES = 12      # random evaluations to declare Res_t identically zero
S0_CAP = 500            # safety cap on number of s0 roots processed

# ---------- bivariate polynomial arithmetic mod p: dict {(i, j): c} = c s^i t^j

def btrim(f):
    return {k: c for k, c in f.items() if c}

def badd(f, g, p):
    out = dict(f)
    for k, c in g.items():
        v = (out.get(k, 0) + c) % p
        if v:
            out[k] = v
        else:
            out.pop(k, None)
    return out

def bsub(f, g, p):
    out = dict(f)
    for k, c in g.items():
        v = (out.get(k, 0) - c) % p
        if v:
            out[k] = v
        else:
            out.pop(k, None)
    return out

def bmul(f, g, p):
    out = {}
    for (i1, j1), c1 in f.items():
        for (i2, j2), c2 in g.items():
            k = (i1 + i2, j1 + j2)
            out[k] = (out.get(k, 0) + c1 * c2) % p
    return btrim(out)

def beval(f, s, t, p):
    r = 0
    for (i, j), c in f.items():
        r = (r + c * pow(s, i, p) * pow(t, j, p)) % p
    return r

def bdeg_s(f):
    return max(i for i, _ in f) if f else -1

def bdeg_t(f):
    return max(j for _, j in f) if f else -1

def btotdeg(f):
    return max(i + j for i, j in f) if f else -1

def to_ts(f):
    """t-major form: list over t-degree j of s-coefficient lists (low->high)."""
    dt = bdeg_t(f)
    out = [[] for _ in range(dt + 1)]
    for (i, j), c in f.items():
        col = out[j]
        if len(col) <= i:
            col.extend([0] * (i + 1 - len(col)))
        col[i] = c
    return [ptrim(col) for col in out]

def eval_s(fts, s0, p):
    """substitute s = s0 in the t-major form -> univariate coeff list in t."""
    return ptrim([peval(col, s0, p) for col in fts])

# ---------- compile system along a plane

def compile_plane(S, p, rng):
    """rows[i] = sorted list of (col, (c0, c1, c2)) meaning c0 + c1*s + c2*t;
    col == n is the rhs column (already negated a-side)."""
    avars, bvars = classify(S)
    aset, bset = set(avars), set(bvars)
    bpos = {v: i for i, v in enumerate(bvars)}
    cornersA = [v for v in S.corner_vars if v in aset]
    cornersB = [v for v in S.corner_vars if v in bset]
    a0 = {v: rng.randrange(p) for v in avars}
    a1 = {v: rng.randrange(p) for v in avars}
    a2 = {v: rng.randrange(p) for v in avars}
    for v in cornersA:                      # keep corner-a(s,t) nonzero at origin
        a0[v] = rng.randrange(1, p)
    n = len(bvars)
    rows = []
    for c in S.equations[:-1]:
        acc = {}
        def add(col, c0, c1, c2):
            e = acc.setdefault(col, [0, 0, 0])
            e[0] = (e[0] + c0) % p
            e[1] = (e[1] + c1) % p
            e[2] = (e[2] + c2) % p
        for m, k in c.items():
            ia = [v for v in m if v in aset]
            ib = [v for v in m if v in bset]
            if len(m) == 2 and len(ia) == 1 and len(ib) == 1:
                v = ia[0]
                add(bpos[ib[0]], k * a0[v], k * a1[v], k * a2[v])
            elif len(m) == 1 and ib:
                add(bpos[ib[0]], k, 0, 0)
            elif len(m) == 1 and ia:
                v = ia[0]
                add(n, -k * a0[v], -k * a1[v], -k * a2[v])
            elif len(m) == 0:
                add(n, -k, 0, 0)
            else:
                raise AssertionError(f"unexpected monomial {m}")
        rows.append(sorted((col, tuple(e)) for col, e in acc.items() if any(e)))
    return rows, (a0, a1, a2, cornersA, cornersB, avars, bvars, bpos)

def _num_aug(rows, n, s, t, p):
    """dense numeric augmented matrix m x (n+1) at (s, t)."""
    M = []
    for row in rows:
        d = [0] * (n + 1)
        for col, (c0, c1, c2) in row:
            d[col] = (c0 + c1 * s + c2 * t) % p
        M.append(d)
    return M

# ---------- fraction-free elimination of b-columns (Sylvester-identity form)

def _pivot_structure(rows, m, n, p, rng):
    """pivot rows/cols of a generic-rank elimination (best of 3 random points)."""
    best = None
    for _ in range(3):
        M = _num_aug(rows, n, rng.randrange(p), rng.randrange(p), p)
        rused = [False] * m
        piv_rows, piv_cols = [], []
        for col in range(n):
            sel = next((i for i in range(m) if not rused[i] and M[i][col]), None)
            if sel is None:
                continue
            rused[sel] = True
            piv_rows.append(sel)
            piv_cols.append(col)
            inv = pow(M[sel][col], p - 2, p)
            Ms = [x * inv % p for x in M[sel]]
            M[sel] = Ms
            for i in range(m):
                if not rused[i] and M[i][col]:
                    f = M[i][col]
                    M[i] = [(x - f * y) % p for x, y in zip(M[i], Ms)]
        if best is None or len(piv_rows) > len(best[0]):
            best = (piv_rows, piv_cols)
    return best

def _detmod(A, p):
    """determinant of a small square matrix mod p (in place)."""
    r = len(A)
    det = 1
    for k in range(r):
        sel = next((i for i in range(k, r) if A[i][k]), None)
        if sel is None:
            return 0
        if sel != k:
            A[k], A[sel] = A[sel], A[k]
            det = (p - det) % p
        pv = A[k][k]
        det = det * pv % p
        inv = pow(pv, p - 2, p)
        Ak = A[k]
        for i in range(k + 1, r):
            if A[i][k]:
                f = A[i][k] * inv % p
                A[i] = [(x - f * y) % p for x, y in zip(A[i], Ak)]
    return det

def _schur_dets(M, piv_rows, piv_cols, resid_rows, p):
    """values of all bordered minors det A[P+{j}, C+{rhs}] at one numeric point:
    LU of the pivot block once, then h_j = det(B) * (w_j - v_j B^{-1} u)."""
    r = len(piv_rows)
    if r == 0:
        return [M[j][-1] % p for j in resid_rows]
    A = [[M[i][c] for c in piv_cols] + [M[i][-1]] for i in piv_rows]
    det = 1
    sing = False
    for k in range(r):
        sel = next((i for i in range(k, r) if A[i][k]), None)
        if sel is None:
            sing = True
            break
        if sel != k:
            A[k], A[sel] = A[sel], A[k]
            det = (p - det) % p
        pv = A[k][k]
        det = det * pv % p
        inv = pow(pv, p - 2, p)
        Ak = A[k]
        for i in range(k + 1, r):
            if A[i][k]:
                f = A[i][k] * inv % p
                Ai = A[i]
                for jj in range(k, r + 1):
                    Ai[jj] = (Ai[jj] - f * Ak[jj]) % p
    if sing:      # rare: pivot block singular at this grid point -> full dets
        out = []
        for j in resid_rows:
            B = [[M[i][c] for c in piv_cols] + [M[i][-1]] for i in piv_rows]
            B.append([M[j][c] for c in piv_cols] + [M[j][-1]])
            out.append(_detmod(B, p))
        return out
    y = [0] * r
    for i in range(r - 1, -1, -1):
        s = A[i][r]
        Ai = A[i]
        for jj in range(i + 1, r):
            s -= Ai[jj] * y[jj]
        y[i] = s % p * pow(Ai[i], p - 2, p) % p
    out = []
    for j in resid_rows:
        row = M[j]
        s = row[-1]
        for c, yy in zip(piv_cols, y):
            if row[c]:
                s -= row[c] * yy
        out.append(det * (s % p) % p)
    return out

def _inv_table(nmax, p):
    inv = [0] * (nmax + 1)
    if nmax >= 1:
        inv[1] = 1
    for i in range(2, nmax + 1):
        inv[i] = (p - (p // i) * inv[p % i]) % p
    return inv

def _newton_consec(vals, p, inv):
    """interpolate at nodes 0..len(vals)-1 -> coeff list (low->high)."""
    n = len(vals)
    c = list(vals)
    for j in range(1, n):
        ij = inv[j]
        for i in range(n - 1, j - 1, -1):
            c[i] = (c[i] - c[i - 1]) * ij % p
    poly = [c[n - 1]]
    for i in range(n - 2, -1, -1):
        xi = i % p
        new = [0] * (len(poly) + 1)
        for k, ck in enumerate(poly):
            new[k + 1] = (new[k + 1] + ck) % p
            new[k] = (new[k] - xi * ck) % p
        new[0] = (new[0] + c[i]) % p
        poly = new
    return ptrim(poly)

def _newton_nodes(xs, vals, p, inv):
    """interpolate at increasing integer nodes xs -> coeff list (low->high)."""
    n = len(vals)
    c = list(vals)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            c[i] = (c[i] - c[i - 1]) * inv[xs[i] - xs[i - j]] % p
    poly = [c[n - 1]]
    for i in range(n - 2, -1, -1):
        xi = xs[i] % p
        new = [0] * (len(poly) + 1)
        for k, ck in enumerate(poly):
            new[k + 1] = (new[k + 1] + ck) % p
            new[k] = (new[k] - xi * ck) % p
        new[0] = (new[0] + c[i]) % p
        poly = new
    return ptrim(poly)

def residual_polys(rows, n, p, rng, deadline=None):
    """fraction-free elimination of the b-columns, Sylvester-identity form.
    Returns (status, hs, rank): status "ok"|"swell"; hs = nonzero residual
    polynomials h_j(s,t) as dicts {(i,j): c}."""
    m = len(rows)
    piv_rows, piv_cols = _pivot_structure(rows, m, n, p, rng)
    r = len(piv_rows)
    resid_rows = [i for i in range(m) if i not in set(piv_rows)]
    if not resid_rows:
        return "ok", [], r
    d1 = r + 2                      # nodes 0..r+1 per axis (total degree <= r+1)
    nres = len(resid_rows)
    vals = [[[0] * d1 for _ in range(d1)] for _ in range(nres)]
    for a in range(d1):
        if deadline is not None and time.monotonic() > deadline:
            return "swell", [], r
        for b in range(d1):
            M = _num_aug(rows, n, a, b, p)
            hv = _schur_dets(M, piv_rows, piv_cols, resid_rows, p)
            for q in range(nres):
                vals[q][a][b] = hv[q]
    inv = _inv_table(d1, p)
    hs = []
    for q in range(nres):
        rowpolys = [_newton_consec(vals[q][a], p, inv) for a in range(d1)]
        h = {}
        for jt in range(d1):
            col = [rp[jt] if jt < len(rp) else 0 for rp in rowpolys]
            sp = _newton_consec(col, p, inv)
            for isx, cc in enumerate(sp):
                if cc:
                    h[(isx, jt)] = cc
        if not h:
            continue
        if len(h) > MAX_TERMS:
            return "swell", [], r
        assert btotdeg(h) <= r + 1, "interpolated residual exceeds minor degree"
        hs.append(h)
    _verify_residuals(rows, n, p, piv_rows, piv_cols, resid_rows, hs, vals)
    return "ok", hs, r

def _verify_residuals(rows, n, p, piv_rows, piv_cols, resid_rows, hs, vals):
    """check interpolation: h values at 2 fresh random points match bordered dets."""
    kept = [q for q in range(len(resid_rows))
            if any(any(row) for row in vals[q])]
    assert len(kept) == len(hs)
    for _ in range(2):
        sa, tb = random.randrange(p), random.randrange(p)
        M = _num_aug(rows, n, sa, tb, p)
        hv = _schur_dets(M, piv_rows, piv_cols, resid_rows, p)
        for h, q in zip(hs, kept):
            assert beval(h, sa, tb, p) == hv[q] % p, "interpolation mismatch"

# ---------- univariate resultant via PRS (values used for interpolation)

def _pmod(f, g, p):
    f = f[:]
    ginv = pow(g[-1], p - 2, p)
    while len(f) >= len(g):
        d = len(f) - len(g)
        c = f[-1] * ginv % p
        for i in range(len(g)):
            f[d + i] = (f[d + i] - c * g[i]) % p
        ptrim(f)
    return ptrim(f)

def ures(f, g, p):
    """resultant of univariate f, g over F_p (coeff lists, low->high)."""
    f, g = ptrim(f[:]), ptrim(g[:])
    if not f or not g:
        return 0
    res = 1
    while len(g) > 1:
        r = _pmod(f, g, p)
        if not r:
            return 0
        df, dg, dr = len(f) - 1, len(g) - 1, len(r) - 1
        res = res * pow(g[-1], df - dr, p) % p
        if (df & 1) and (dg & 1):
            res = (p - res) % p
        f, g = g, r
    return res * pow(g[0], len(f) - 1, p) % p

# ---------- locus analysis

def _normalize_dedupe(hs, p):
    seen = set()
    out = []
    for h in hs:
        mk = max(h)
        inv = pow(h[mk], p - 2, p)
        hn = {k: c * inv % p for k, c in h.items()}
        key = tuple(sorted(hn.items()))
        if key not in seen:
            seen.add(key)
            out.append(hn)
    return out

def _transpose(h):
    return {(j, i): c for (i, j), c in h.items()}

def _slice_g(structs, sg, p):
    """gcd over all residuals of h_j(sg, t); [] iff every slice is zero."""
    g = None
    for st in structs:
        ct = eval_s(st, sg, p)
        if not ct:
            continue                     # gcd(f, 0) = f
        g = ct if g is None else pgcd_(g, ct, p)
        if len(g) == 1:
            return g
    return g if g is not None else []

def _consistent_at(rows, n, s, t, p):
    """numeric consistency of M(a(s,t)) b = r(a(s,t)) at one point."""
    M = _num_aug(rows, n, s, t, p)
    m = len(M)
    r = 0
    for col in range(n):
        sel = next((i for i in range(r, m) if M[i][col]), None)
        if sel is None:
            continue
        M[r], M[sel] = M[sel], M[r]
        inv = pow(M[r][col], p - 2, p)
        M[r] = [x * inv % p for x in M[r]]
        for i in range(m):
            if i != r and M[i][col]:
                f = M[i][col]
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        r += 1
    return all(M[i][n] == 0 for i in range(r, m))

def _any_consistent(rows, n, p, pts):
    return any(_consistent_at(rows, n, s, t, p) for s, t in pts)

def analyze_locus(hs, rows, n, p, rng, deadline=None):
    """returns (status, deg_R, s0_list); status "ok"|"CURVE"|"swell".
    deg_R = -1 when R was not computed (CURVE / early swell)."""
    structs = [to_ts(h) for h in hs]
    # ---- global content along t-slices: gcd_j h_j(sigma, .) for random sigma
    prof = []
    for _ in range(6):
        sg = rng.randrange(p)
        g = _slice_g(structs, sg, p)
        if g:
            prof.append((sg, g))
    if not prof:
        return "swell", -1, []           # degenerate: all slices vanished
    gdeg = min(len(g) - 1 for _, g in prof)
    if gdeg > 0:                         # common-vanishing curve: real or artifact?
        pts = []
        for sg, g in prof:
            if len(g) - 1 == gdeg:
                for t0 in fp_roots(g, p)[:4]:
                    pts.append((sg, t0))
        if _any_consistent(rows, n, p, pts):
            return "CURVE", -1, []
    # ---- pure-s content via transposed slices (vertical lines s = const)
    tstructs = [to_ts(_transpose(h)) for h in hs]
    tprof = []
    for _ in range(4):
        tg = rng.randrange(p)
        g = _slice_g(tstructs, tg, p)
        if g:
            tprof.append((tg, g))
    sdeg = min((len(g) - 1 for _, g in tprof), default=0)
    if sdeg > 0:
        pts = []
        for tg, g in tprof:
            if len(g) - 1 == sdeg:
                for s0 in fp_roots(g, p)[:4]:
                    pts.append((s0, tg))
        if _any_consistent(rows, n, p, pts):
            return "CURVE", -1, []
    # ---- first five residuals, content-reduced along slices
    H5 = hs[:5]
    st5 = structs[:5]
    lct5 = [st[-1] for st in st5]        # leading t-coefficient (s-poly)
    dth5 = [bdeg_t(h) for h in H5]

    def red_slices(sg, g):
        out = []
        for st in st5:
            f = eval_s(st, sg, p)
            out.append(pdivexact(f, g, p) if gdeg > 0 else f)
        return out

    et = None
    for _ in range(300):                 # bootstrap generic reduced t-degrees
        sg = rng.randrange(p)
        if all(peval(lc, sg, p) for lc in lct5):
            g = _slice_g(structs, sg, p)
            if g and len(g) - 1 == gdeg:
                et = [len(f) - 1 for f in red_slices(sg, g)]
                break
    if et is None:
        return "swell", -1, []
    active = [i for i in range(len(H5)) if dth5[i] > 0 and et[i] > 0]

    cache = {}
    def node_data(sg):
        """content-reduced first-five slices at s=sg, or None if degenerate."""
        if sg in cache:
            return cache[sg]
        data = None
        if all(peval(lc, sg, p) for lc in lct5):
            g = _slice_g(structs, sg, p)
            if g and len(g) - 1 == gdeg:
                rs = red_slices(sg, g)
                if all(len(rs[i]) - 1 == et[i] for i in active):
                    data = rs
        cache[sg] = data
        return data

    R = None
    for i in range(len(H5)):
        if dth5[i] == 0:                 # t-free residual: direct s-condition
            f = [0] * (bdeg_s(H5[i]) + 1)
            for (ii, _), c in H5[i].items():
                f[ii] = c
            f = ptrim(f)
            R = f if R is None else pgcd_(R, f, p)
    if len(active) < 2 and R is None:
        if len(active) == 1:             # one condition beyond content: a curve
            i = active[0]
            pts, tries = [], 0
            while len(pts) < 12 and tries < 300:
                tries += 1
                sg = rng.randrange(p)
                rs = node_data(sg)
                if rs is not None and len(rs[i]) > 1:
                    pts.extend((sg, t0) for t0 in fp_roots(rs[i], p)[:3])
            if _any_consistent(rows, n, p, pts):
                return "CURVE", -1, []
        return "ok", 0, []

    def pair_slices(rs, i, j, cdeg):
        """coprime parts of the pair at one node, or None if gcd deg jumps."""
        fi, fj = rs[i], rs[j]
        if cdeg > 0:
            cg = pgcd_(fi, fj, p)
            if len(cg) - 1 != cdeg:
                return None
            fi = pdivexact(fi, cg, p)
            fj = pdivexact(fj, cg, p)
        return fi, fj

    def interp_pair(i, j, cdeg):
        """interpolate s -> Res_t of the pair's coprime parts (adaptive)."""
        nodes, vals = [], []
        sg = 0
        N = 64
        while True:
            while len(nodes) < N + 1:
                if sg >= min(p, RES_MAX + 800):
                    return None
                rs = node_data(sg)
                if rs is not None:
                    fij = pair_slices(rs, i, j, cdeg)
                    if fij is not None:
                        nodes.append(sg)
                        vals.append(ures(fij[0], fij[1], p))
                sg += 1
            inv = _inv_table(nodes[-1] + 2, p)
            Rij = _newton_nodes(nodes, vals, p, inv)
            okv, tries, good = 0, 0, True
            while okv < 8 and tries < 400:
                tries += 1
                rsg = rng.randrange(p)
                rs = node_data(rsg)
                if rs is None:
                    continue
                fij = pair_slices(rs, i, j, cdeg)
                if fij is None:
                    continue
                if peval(Rij, rsg, p) != ures(fij[0], fij[1], p):
                    good = False
                    break
                okv += 1
            if good and okv >= 8:
                return Rij
            if N > RES_MAX:
                return None
            N *= 2

    for i, j in combinations(active, 2):
        if deadline is not None and time.monotonic() > deadline:
            return "swell", -1, []
        if R is not None and len(R) == 1:
            break
        # generic degree of the pair's shared factor (identically-zero Res_t
        # detection) plus reality test of that shared curve
        cdegs, common_pts, tries = [], [], 0
        while len(cdegs) < CURVE_SAMPLES and tries < 300:
            tries += 1
            sg = rng.randrange(p)
            rs = node_data(sg)
            if rs is None:
                continue
            cg = pgcd_(rs[i], rs[j], p)
            cdegs.append(len(cg) - 1)
            if len(cg) > 1 and len(common_pts) < 8 and len(cdegs) <= 3:
                common_pts.extend((sg, t0) for t0 in fp_roots(cg, p)[:3])
        if not cdegs:
            continue
        cdeg = min(cdegs)
        if cdeg > 0:                     # pairwise resultant vanishes identically
            if _any_consistent(rows, n, p, common_pts):
                return "CURVE", -1, []
            if cdeg >= et[i] or cdeg >= et[j]:
                continue                 # a member is pure shared factor
        Rij = interp_pair(i, j, cdeg)
        if not Rij:
            continue
        R = Rij if R is None else pgcd_(R, Rij, p)
    if R is None:
        return "swell", -1, []           # no pair analyzable
    if len(R) <= 1:
        return "ok", 0, []
    if len(R) - 1 > ROOTS_MAX:
        return "swell", len(R) - 1, []
    return "ok", len(R) - 1, fp_roots(R, p)

# ---------- per-plane driver

def plane_candidates(rows, n, p, rng, deadline=None):
    """residual extraction + locus analysis + (s0, t0) candidate roots for one
    compiled plane.  Returns an info dict with status/rank/n_resid/deg_R/n_s0
    and the candidate list."""
    info = dict(status="ok", rank=-1, n_resid=-1, deg_R=-1, n_s0=-1, cands=[])
    status, hs_raw, rank = residual_polys(rows, n, p, rng, deadline)
    info["rank"] = rank
    if status != "ok":
        info["status"] = "swell"
        return info
    hs = _normalize_dedupe(hs_raw, p)
    hs.sort(key=lambda h: (btotdeg(h), len(h)))
    info["n_resid"] = len(hs)
    if not hs:
        info["deg_R"] = 0
        info["n_s0"] = 0
        return info
    status, degR, s0s = analyze_locus(hs, rows, n, p, rng, deadline)
    info["deg_R"] = degR
    if status != "ok":
        info["status"] = status
        return info
    info["n_s0"] = len(s0s)
    structs_all = [to_ts(h) for h in hs]
    for s0 in s0s[:S0_CAP]:
        if deadline is not None and time.monotonic() > deadline:
            info["status"] = "swell"
            break
        g = _slice_g(structs_all, s0, p)
        if g and len(g) == 1:
            continue
        if not g:                        # whole line s=s0 satisfies all h_j
            t0s = [rng.randrange(p) for _ in range(5)]
        else:
            t0s = fp_roots(g, p)
        info["cands"].extend((s0, tt) for tt in t0s)
    return info

def probe_plane(S, p, rng, timeout_s=900):
    t0 = time.monotonic()
    deadline = t0 + timeout_s
    rows, meta = compile_plane(S, p, rng)
    a0, a1, a2, cornersA, cornersB, avars, bvars, bpos = meta
    n = len(bvars)
    ci = plane_candidates(rows, n, p, rng, deadline)
    info = dict(status=ci["status"], n_resid=ci["n_resid"], deg_R=ci["deg_R"],
                n_s0=ci["n_s0"], n_cand=len(ci["cands"]), n_hits=0,
                rank=ci["rank"], secs=0.0)
    for s0, tt in ci["cands"]:
        a = {v: (a0[v] + s0 * a1[v] + tt * a2[v]) % p for v in avars}
        if any(a[v] == 0 for v in cornersA):
            continue
        hit, wit = _check_point(S, p, a, bvars, bpos, cornersB, rng)
        if hit and verify_witness(S, p, wit):
            info["n_hits"] += 1
    info["secs"] = time.monotonic() - t0
    return info

def run_planes(S, p, nplanes, seed=1, out_path=None, label="", timeout_s=900):
    rng = random.Random(seed)
    results = []
    fh = open(out_path, "a") if out_path else None
    if fh:
        fh.write(f"# case={label} p={p} nplanes={nplanes} seed={seed} "
                 f"ts={int(time.time())}\n")
        fh.flush()
    for ln in range(nplanes):
        info = probe_plane(S, p, rng, timeout_s=timeout_s)
        info["plane"] = ln
        results.append(info)
        if fh:
            fh.write(f"{ln} {info['status']} {info['n_resid']} {info['deg_R']} "
                     f"{info['n_s0']} {info['n_cand']} {info['n_hits']} "
                     f"{info['secs']:.1f}\n")
            fh.flush()
    if fh:
        fh.close()
    return results

def build_system(name):
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "cases"))
    from emit import CASES, FIX
    from jc import SystemA
    c = CASES[name]
    return SystemA(name, c["cornersP"], c["cornersQ"], c["rhs"],
                   nonvanish="nonorigin", fix_ones=FIX[name])

def main(argv):
    name = argv[0]
    p = int(argv[1])
    nplanes = int(argv[2])
    seed = int(argv[3]) if len(argv) > 3 else 1
    timeout_s = float(argv[4]) if len(argv) > 4 else 900.0
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "..", "runs", "planeprobe_results.txt")
    S = build_system(name)
    t0 = time.monotonic()
    res = run_planes(S, p, nplanes, seed=seed, out_path=out, label=name,
                     timeout_s=timeout_s)
    agg = dict(ok=0, swell=0, CURVE=0)
    cand = hits = 0
    for r in res:
        agg[r["status"]] += 1
        cand += r["n_cand"]
        hits += r["n_hits"]
    print(f"{name} p={p} planes={nplanes} ok={agg['ok']} swell={agg['swell']} "
          f"curve={agg['CURVE']} cand={cand} hits={hits} "
          f"secs={time.monotonic() - t0:.0f}")

if __name__ == "__main__":
    main(sys.argv[1:])
