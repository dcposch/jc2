"""Line probe: decide solvability-locus dimension via univariate elimination.

Restrict P-coefficients to a random line a(t) = a0 + t*a1 in F_p^{#a}.
The Q-side system M(a(t)) b = r(a(t)) has entries linear in t.  Fraction-free
row reduction over F_p[t] yields the consistency conditions h_j(t); their gcd
g(t) vanishes exactly at the t where the system is consistent.

  - nonconstant g on random lines  => solvability locus nonempty, codim 1
    (roots give explicit candidate points -> test corner-realizability)
  - constant nonzero g on many lines => locus empty or codim >= 2

Validated against cases already decided by msolve ([1] => zero realizable hits).
"""
import random
from linprobe import classify

# ---------- univariate polynomial arithmetic mod p (dense lists, low->high)

def ptrim(f):
    while f and f[-1] == 0:
        f.pop()
    return f

def padd_(f, g, p):
    n = max(len(f), len(g))
    return ptrim([((f[i] if i < len(f) else 0) + (g[i] if i < len(g) else 0)) % p
                  for i in range(n)])

def psub_(f, g, p):
    n = max(len(f), len(g))
    return ptrim([((f[i] if i < len(f) else 0) - (g[i] if i < len(g) else 0)) % p
                  for i in range(n)])

def pmul_(f, g, p):
    if not f or not g:
        return []
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        if a:
            for j, b in enumerate(g):
                out[i + j] = (out[i + j] + a * b) % p
    return ptrim(out)

def pdivexact(f, g, p):
    """exact division f/g (asserts remainder 0)"""
    f = f[:]
    if not g:
        raise ZeroDivisionError
    q = [0] * (len(f) - len(g) + 1) if len(f) >= len(g) else []
    ginv = pow(g[-1], p - 2, p)
    while len(f) >= len(g) and ptrim(f):
        d = len(f) - len(g)
        c = (f[-1] * ginv) % p
        q[d] = c
        for i in range(len(g)):
            f[d + i] = (f[d + i] - c * g[i]) % p
        ptrim(f)
    assert not ptrim(f), "inexact division"
    return ptrim(q)

def pmod_(f, g, p):
    f = f[:]
    ginv = pow(g[-1], p - 2, p)
    while len(f) >= len(g):
        d = len(f) - len(g)
        c = (f[-1] * ginv) % p
        for i in range(len(g)):
            f[d + i] = (f[d + i] - c * g[i]) % p
        ptrim(f)
    return ptrim(f)

def pgcd_(f, g, p):
    f, g = f[:], g[:]
    while g:
        f, g = g, pmod_(f, g, p)
    if f:
        inv = pow(f[-1], p - 2, p)
        f = [(x * inv) % p for x in f]
    return f

def peval(f, t, p):
    r = 0
    for c in reversed(f):
        r = (r * t + c) % p
    return r

def ppowmod(base, e, g, p):
    """base(t)^e mod g(t) mod p, by square and multiply"""
    r = [1]
    b = pmod_(base, g, p)
    while e:
        if e & 1:
            r = pmod_(pmul_(r, b, p), g, p)
        b = pmod_(pmul_(b, b, p), g, p)
        e >>= 1
    return r

def fp_roots(g, p):
    """all roots of g in F_p via gcd with t^p - t, then descent"""
    tp = ppowmod([0, 1], p, g, p)               # t^p mod g
    h = pgcd_(psub_(tp, [0, 1], p), g, p)       # product of (t - root)
    if not h or len(h) == 1:
        return []
    if p < 2**21:                                # small prime: direct scan is fine
        return [t for t in range(p) if peval(h, t, p) == 0]
    # equal-degree splitting for the linear-factor product h
    import random as _r
    def split(f):
        if len(f) == 2:
            return [(-f[0] * pow(f[1], p - 2, p)) % p]
        while True:
            a = [_r.randrange(p), 1]
            w = ppowmod(a, (p - 1) // 2, f, p)
            d = pgcd_(psub_(w, [1], p), f, p)
            if d and 1 < len(d) < len(f):
                return split(d) + split(pdivexact(f, d, p))
    return split(h)

# ---------- compile system along a line

def compile_line(S, p, rng):
    avars, bvars = classify(S)
    aset, bset = set(avars), set(bvars)
    bpos = {v: i for i, v in enumerate(bvars)}
    cornersA = [v for v in S.corner_vars if v in aset]
    cornersB = [v for v in S.corner_vars if v in bset]
    a0 = {v: rng.randrange(p) for v in avars}
    a1 = {v: rng.randrange(p) for v in avars}
    for v in cornersA:                       # keep corner-a(t) a nonzero poly
        a0[v] = rng.randrange(1, p)
    rows, rhs = [], []
    for c in S.equations[:-1]:
        row = [[] for _ in bvars]
        s = []
        for m, k in c.items():
            ia = [v for v in m if v in aset]
            ib = [v for v in m if v in bset]
            if len(m) == 2 and len(ia) == 1 and len(ib) == 1:
                lin = [(k * a0[ia[0]]) % p, (k * a1[ia[0]]) % p]
                row[bpos[ib[0]]] = padd_(row[bpos[ib[0]]], ptrim(lin), p)
            elif len(m) == 1 and ib:
                row[bpos[ib[0]]] = padd_(row[bpos[ib[0]]], [k % p], p)
            elif len(m) == 1 and ia:
                s = padd_(s, ptrim([(k * a0[ia[0]]) % p, (k * a1[ia[0]]) % p]), p)
            elif len(m) == 0:
                s = padd_(s, [k % p], p)
            else:
                raise AssertionError(f"unexpected monomial {m}")
        rows.append(row)
        rhs.append([(p - x) % p for x in s] if s else [])
    return rows, rhs, (a0, a1, cornersA, cornersB, avars, bvars, bpos)

def consistency_gcd(rows, rhs, p):
    """fraction-free elimination of the b-columns over F_p[t];
    returns gcd of the residual rhs entries (the obstruction polynomial)."""
    m = len(rows)
    n = len(rows[0]) if m else 0
    A = [rows[i] + [rhs[i]] for i in range(m)]
    piv_rows = []
    used = [False] * m
    for col in range(n):
        cand = [(len(A[i][col]), i) for i in range(m) if not used[i] and A[i][col]]
        if not cand:
            continue
        _, pi = min(cand)
        used[pi] = True
        piv_rows.append((pi, col))
        pv = A[pi][col]
        for i in range(m):
            if i != pi and not used[i] and A[i][col]:
                f = A[i][col]
                newrow = []
                for j in range(n + 1):
                    t1 = pmul_(pv, A[i][j], p)
                    t2 = pmul_(f, A[pi][j], p)
                    newrow.append(psub_(t1, t2, p))
                # content removal to control degree growth
                g = []
                for e in newrow:
                    if e:
                        g = pgcd_(g, e, p) if g else e[:]
                    if len(g) == 1:
                        break
                if g and len(g) > 1:
                    newrow = [pdivexact(e, g, p) if e else [] for e in newrow]
                A[i] = newrow
    obstruction = []
    for i in range(m):
        if used[i]:
            continue
        if any(A[i][j] for j in range(n)):
            continue                      # not fully reduced; skip (rare)
        e = A[i][n]
        if e:
            obstruction = pgcd_(obstruction, e, p) if obstruction else e[:]
            if len(obstruction) == 1:
                break
    return obstruction        # []: identically consistent; [c]: never; else g(t)

def probe_line(S, p, nlines=12, seed=3):
    rng = random.Random(seed)
    from linprobe import probe as _unused  # noqa
    results = []
    witness = None
    for ln in range(nlines):
        rows, rhs, meta = compile_line(S, p, rng)
        g = consistency_gcd(rows, rhs, p)
        a0, a1, cornersA, cornersB, avars, bvars, bpos = meta
        info = {"line": ln, "deg_g": (len(g) - 1) if g else None, "roots": 0, "hits": 0}
        if g and len(g) > 1:
            roots = fp_roots(g, p)
            info["roots"] = len(roots)
            for t0 in roots:
                a = {v: (a0[v] + t0 * a1[v]) % p for v in avars}
                if any(a[v] == 0 for v in cornersA):
                    continue
                from linprobe import probe as lp  # reuse solver via tiny shim below
                hit, wit = _check_point(S, p, a, bvars, bpos, cornersB, rng)
                if hit:
                    info["hits"] += 1
                    witness = wit
        results.append(info)
        if witness:
            break
    return results, witness

def _check_point(S, p, a, bvars, bpos, cornersB, rng):
    from linprobe import classify
    avars, _ = classify(S)
    aset, bset = set(avars), set(bvars)
    M, rhs = [], []
    for c in S.equations[:-1]:
        row = [0] * len(bvars)
        s = 0
        for m, k in c.items():
            ia = [v for v in m if v in aset]
            ib = [v for v in m if v in bset]
            if len(m) == 2 and len(ia) == 1 and len(ib) == 1:
                row[bpos[ib[0]]] = (row[bpos[ib[0]]] + k * a[ia[0]]) % p
            elif len(m) == 1 and ib:
                row[bpos[ib[0]]] = (row[bpos[ib[0]]] + k) % p
            elif len(m) == 1 and ia:
                s += k * a[ia[0]]
            elif len(m) == 0:
                s += k
        M.append(row)
        rhs.append((-s) % p)
    from linprobe import probe
    # reuse linprobe's internal gaussian solver by inlining a minimal copy
    import linprobe as L
    solve = None
    # minimal gaussian solve (duplicated to avoid refactor)
    n = len(M); nv = len(M[0])
    A = [M[i][:] + [rhs[i]] for i in range(n)]
    piv = []; r = 0
    for col in range(nv):
        sel = next((i for i in range(r, n) if A[i][col] % p), None)
        if sel is None: continue
        A[r], A[sel] = A[sel], A[r]
        inv = pow(A[r][col], p - 2, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(n):
            if i != r and A[i][col]:
                f = A[i][col]
                A[i] = [(x - f * y) % p for x, y in zip(A[i], A[r])]
        piv.append(col); r += 1
        if r == n: break
    for i in range(r, n):
        if A[i][nv] % p:
            return False, None
    x0 = [0] * nv
    for i, col in enumerate(piv):
        x0[col] = A[i][nv]
    free = [c for c in range(nv) if c not in piv]
    null = []
    for fc in free:
        vec = [0] * nv; vec[fc] = 1
        for i, col in enumerate(piv):
            vec[col] = (-A[i][fc]) % p
        null.append(vec)
    for _ in range(50):
        b = x0[:]
        for vec in null:
            lam = rng.randrange(p)
            b = [(x + lam * y) % p for x, y in zip(b, vec)]
        if all(b[bpos[cb]] % p for cb in cornersB):
            return True, (a, {v: b[bpos[v]] for v in bvars})
    return False, None
