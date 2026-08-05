"""FLINT-backed fast coefficient arithmetic for the jc72108 pipeline.

Drop-in layer over python-flint's fmpq_mpoly for the coefficient dicts of
lib/jc.py (Coef = { Mon: int|Fraction }, Mon = sorted tuple of var indices
with multiplicity).  The pure-Python implementations in jc.py stay untouched
and remain the oracle; this module is only consulted when

    JC_BACKEND=flint

is set in the environment (default: python).  See lib/FASTCOEF.md.

Exposed:
  backend()                      -> "python" | "flint" (env-resolved, safe)
  cadd/cmul/cscale/cneg          -> flint-backed drop-ins (same contract)
  bracket_fast(P, Q)             -> fast [P,Q] for jc.SystemA generation
  subst_linear_many(eqs,v,g,inv) -> the Cascade3 hot kernel (v := g, v-linear)

Design notes (measured on python-flint 0.9.0):
  * fmpq_mpoly_ctx.from_dict is quadratic in the term count (repeated sorted
    insertion), so large polynomials are built via ctx.term + balanced tree
    sums (_build).
  * Contexts are created per variable-universe size and cached; every call
    maps the global var indices of its inputs onto a dense local 0..n-1
    range (monomial-tuple <-> exponent-vector adapters at the boundary), so
    exponent vectors stay short even for farm-scale systems (1300+ vars).
  * bracket_fast is accumulation-bound, not multiply-bound (coefficients are
    single variables); the win there is in-place accumulation, not FLINT.
    All conversions/adapters were benchmarked slower for that shape.
"""
import os
import sys
from fractions import Fraction

HAVE_FLINT = False
FLINT_VERSION = None
try:
    import flint as _flint
    from flint import fmpq, fmpq_mpoly_ctx, Ordering
    HAVE_FLINT = True
    FLINT_VERSION = getattr(_flint, "__version__", "unknown")
except ImportError:
    pass

_warned = [False]

def backend():
    """Resolve the arithmetic backend from JC_BACKEND (read per call so tests
    can flip it in-process).  Falls back to python with a one-time warning if
    flint is requested but python-flint is not importable."""
    b = os.environ.get("JC_BACKEND", "python").strip().lower()
    if b not in ("python", "flint"):
        raise ValueError(f"JC_BACKEND must be 'python' or 'flint', got {b!r}")
    if b == "flint" and not HAVE_FLINT:
        if not _warned[0]:
            print("fastcoef: JC_BACKEND=flint but python-flint is not "
                  "installed; falling back to python", file=sys.stderr)
            _warned[0] = True
        return "python"
    return b

# ------------------------------------------------------------ ctx + adapters

_CTXCACHE = {}

def _ctx(n):
    c = _CTXCACHE.get(n)
    if c is None:
        c = fmpq_mpoly_ctx.get(("v", n), Ordering.degrevlex)
        _CTXCACHE[n] = c
    return c

def _to_fmpq(k):
    if isinstance(k, Fraction):
        return fmpq(k.numerator, k.denominator)
    return fmpq(k)

def _from_fmpq(q):
    """fmpq -> int when integral else Fraction (both compare/format like the
    pure path: Fraction(n) == n)."""
    num, den = int(q.p), int(q.q)
    return num if den == 1 else Fraction(num, den)

def _mon_to_exp(m, vmap, n):
    e = [0] * n
    for i in m:
        e[vmap[i]] += 1
    return tuple(e)

def _exp_to_mon(e, vlist):
    mon = []
    for pos, cnt in enumerate(e):
        if cnt:
            mon.extend((vlist[pos],) * cnt)
    return tuple(mon)          # vlist ascending -> tuple sorted, as jc expects

_CHUNK = 200

def _build(ctx, items):
    """Balanced construction: ctx.from_dict is O(T^2), so build term chunks
    and tree-sum them (adds are C-level merges)."""
    if not items:
        return ctx.from_dict({})
    if len(items) <= _CHUNK:
        return ctx.from_dict(dict(items))
    polys = [ctx.from_dict(dict(items[i:i + _CHUNK]))
             for i in range(0, len(items), _CHUNK)]
    while len(polys) > 1:
        nxt = [polys[i] + polys[i + 1] for i in range(0, len(polys) - 1, 2)]
        if len(polys) % 2:
            nxt.append(polys[-1])
        polys = nxt
    return polys[0]

def _poly_of(cdict, ctx, vmap):
    n = ctx.nvars()
    return _build(ctx, [(_mon_to_exp(m, vmap, n), _to_fmpq(k))
                        for m, k in cdict.items()])

def _dict_of(p, vlist):
    return {_exp_to_mon(e, vlist): _from_fmpq(q)
            for e, q in p.to_dict().items()}

def _locals_of(*cdicts):
    vlist = sorted({i for c in cdicts for m in c for i in m})
    vmap = {v: pos for pos, v in enumerate(vlist)}
    return vlist, vmap, _ctx(max(1, len(vlist)))

# ------------------------------------------------- drop-in coef arithmetic

def cadd(c1, c2):
    """flint-backed jc.cadd (dict-in/dict-out, zero terms dropped)."""
    vlist, vmap, ctx = _locals_of(c1, c2)
    return _dict_of(_poly_of(c1, ctx, vmap) + _poly_of(c2, ctx, vmap), vlist)

def cneg(c):
    vlist, vmap, ctx = _locals_of(c)
    return _dict_of(-_poly_of(c, ctx, vmap), vlist)

def cscale(c, k):
    if k == 0:
        return {}
    vlist, vmap, ctx = _locals_of(c)
    return _dict_of(_poly_of(c, ctx, vmap) * ctx.from_dict({(0,) * ctx.nvars(): _to_fmpq(k)}), vlist)

def cmul(c1, c2):
    vlist, vmap, ctx = _locals_of(c1, c2)
    return _dict_of(_poly_of(c1, ctx, vmap) * _poly_of(c2, ctx, vmap), vlist)

# ------------------------------------------------------- generation kernel

def bracket_fast(p, q):
    """[P,Q] = P_x Q_y - P_y Q_x with in-place accumulation.  Content-equal
    to jc.padd(jc.pmul(dx p, dy q), jc.pneg(jc.pmul(dy p, dx q)))."""
    from jc import dx, dy
    r = {}
    _acc_pmul(r, dx(p), dy(q), 1)
    _acc_pmul(r, dy(p), dx(q), -1)
    return {cell: c for cell, c in r.items() if c}

def _acc_pmul(r, p1, p2, sign):
    for (i1, j1), c1 in p1.items():
        for (i2, j2), c2 in p2.items():
            cell = r.setdefault((i1 + i2, j1 + j2), {})
            for m1, v1 in c1.items():
                sv1 = sign * v1
                for m2, v2 in c2.items():
                    m = tuple(sorted(m1 + m2))
                    w = cell.get(m, 0) + sv1 * v2
                    if w:
                        cell[m] = w
                    else:
                        del cell[m]

# --------------------------------------------------------- cascade kernel

def invred_mon(m, invof):
    """Cancel (c, invof[c]) pairs inside one monomial — exact replica of the
    inner loop of reduce3.Cascade3._inv_reduce."""
    for i in m:                       # fast path: nothing to cancel
        j = invof.get(i)
        if j is not None and j in m:
            break
    else:
        return m
    cnt = {}
    for i in m:
        cnt[i] = cnt.get(i, 0) + 1
    for i in list(cnt):
        j = invof.get(i)
        if j is not None and j in cnt and j > i:
            d = cnt[i] if cnt[i] < cnt[j] else cnt[j]
            cnt[i] -= d
            cnt[j] -= d
    return tuple(sorted(i for i, e in cnt.items() for _ in range(e)))

def subst_linear_many(eqs, v, g, invof):
    """Substitute v := g (v occurring with exponent <= 1) into every equation
    of `eqs` that mentions v; inverse-pair-reduce the results.  Equations not
    mentioning v are passed through unchanged (same object).  Content-parity
    with the pure path:
        [C._subst_linear(c, v, g) if any(v in m for m in c) else c for c in eqs]

    Split c = A*v + B; result = B + A*g, computed as one FLINT multiply per
    equation (A small, g converted once), then merged term-by-term with
    inverse-pair reduction.
    """
    split = []                       # (index, A, B) with c = A*v + B
    for ei, c in enumerate(eqs):
        if not any(v in m for m in c):
            continue
        A, B = {}, {}
        for m, k in c.items():
            if v in m:
                m2 = tuple(i for i in m if i != v)
                w = A.get(m2, 0) + k       # (sum_k)*g == sum_k (k*g): parity
                if w:
                    A[m2] = w
                else:
                    del A[m2]
            else:
                B[m] = k
        split.append((ei, A, B))
    if not split:
        return list(eqs)
    vset = {i for m in g for i in m}
    for _, A, _B in split:
        for m in A:
            vset.update(m)
    vlist = sorted(vset)
    vmap = {w: pos for pos, w in enumerate(vlist)}
    ctx = _ctx(max(1, len(vlist)))
    gpoly = _poly_of(g, ctx, vmap)
    out = list(eqs)
    for ei, A, B in split:
        prod = _poly_of(A, ctx, vmap) * gpoly
        acc = {}
        for m, k in B.items():
            mr = invred_mon(m, invof)
            w = acc.get(mr, 0) + k
            if w:
                acc[mr] = w
            else:
                del acc[mr]
        for e, q in prod.to_dict().items():
            mr = invred_mon(_exp_to_mon(e, vlist), invof)
            w = acc.get(mr, 0) + _from_fmpq(q)
            if w:
                acc[mr] = w
            else:
                del acc[mr]
        out[ei] = acc
    return out
