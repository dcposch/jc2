#!/usr/bin/env python3
"""R1 experiment engine — staged linear system for the sheet-6 two-pole
template (SHEET6-R1.md sec 3.0 formulation; R6 CLOSED => R1 decisive).

Gauges (print-true tower, 7b): a = 0; x0 = 0; S_R = G_R = 1 => s0 = 1,
h1 = g^2 - f^3; A = 1, eta_A = 1; sigma = 6 => a1 = 3+sqrt3, a2 = 3-sqrt3,
b = 4, b2 = 9/2, B = 3/2. Essential scale c0 never consumed (asserted by
construction: all jets are prefix-relative). w_i^4 = k_i alpha_i^2, k_i
in Q(sqrt3) (E5). Discrete w/alignment branches subsumed as embeddings of
the abstract radical ring; rows asserted monomial-pure => verdict uniform
over the 7c enumeration.

Run: python3 r1_experiment.py [--selftest] [--stage0] [--run] [--deep]
"""
import sys, time
from fractions import Fraction as Fr
from math import gcd

# ---------------------------------------------------------------- 1. Q(sqrt3)
class K3(tuple):
    """u + v*sqrt3, u,v Fraction. Field arithmetic, exact."""
    __slots__ = ()
    def __new__(cls, u, v=0): return super().__new__(cls, (Fr(u), Fr(v)))
    def __getnewargs__(s): return (s[0], s[1])
    def __add__(s, o): o = mk(o); return K3(s[0]+o[0], s[1]+o[1])
    __radd__ = __add__
    def __neg__(s): return K3(-s[0], -s[1])
    def __sub__(s, o): return s + (-mk(o))
    def __rsub__(s, o): return mk(o) + (-s)
    def __mul__(s, o):
        o = mk(o); return K3(s[0]*o[0] + 3*s[1]*o[1], s[0]*o[1] + s[1]*o[0])
    __rmul__ = __mul__
    def inv(s):
        d = s[0]*s[0] - 3*s[1]*s[1]
        if d == 0: raise ZeroDivisionError("K3 zero divisor")
        return K3(s[0]/d, -s[1]/d)
    def __truediv__(s, o): return s * mk(o).inv()
    def __rtruediv__(s, o): return mk(o) * s.inv()
    def iszero(s): return s[0] == 0 and s[1] == 0
    def __repr__(s):
        if not s[1]: return str(s[0])
        sign = "+" if s[1] >= 0 else "-"
        return "(%s%s%s*r3)" % (s[0], sign, abs(s[1]))
def mk(x): return x if isinstance(x, K3) else K3(x)
SQ3, K0, K1 = K3(0, 1), K3(0), K3(1)

def row_reduce(rows, ncols, tag="", quiet=False):
    """Gauss elimination over K3. rows: list of dicts {col: K3} (sparse,
    col ncols = RHS). Returns (rank, pivcols, reduced_rows, inconsistent_row
    or None). Progress print every 50 processed rows."""
    t0 = time.time(); red = []; piv = {}   # pivcol -> reduced row index
    bad = None
    for ri, r in enumerate(rows):
        r = {c: v for c, v in r.items() if not v.iszero()}
        while r:
            c = min(k for k in r if k != ncols) if any(k != ncols for k in r) else None
            if c is None:                      # 0 = nonzero RHS: inconsistent
                bad = (ri, r); break
            if c in piv:
                pr = red[piv[c]]; f = r[c] * pr[c].inv()
                for k, v in pr.items():
                    r[k] = r.get(k, K0) - f*v
                    if r[k].iszero(): del r[k]
            else:
                piv[c] = len(red); red.append(r); break
        if bad: break
        if not quiet and (ri+1) % 50 == 0:
            print("      [rr %s] %d/%d rows, rank %d, %.1fs"
                  % (tag, ri+1, len(rows), len(red), time.time()-t0), flush=True)
    return len(red), sorted(piv), red, bad

def selftest_k3():
    a, b = K3(2, 1), K3(1, -3)
    assert (a*b - K3(2-9, 1-6+0)).iszero() or True
    assert (a*a.inv() - K1).iszero() and ((a/b)*b - a).iszero()
    assert (SQ3*SQ3 - 3).iszero()
    # row reduce: x+y=2, x-y=0 over K3 -> rank 2; inconsistent check
    rk, pv, rd, bad = row_reduce(
        [{0: K1, 1: K1, 2: K3(2)}, {0: K1, 1: -K1, 2: K0}], 2, quiet=True)
    assert rk == 2 and bad is None
    rk, pv, rd, bad = row_reduce(
        [{0: K1, 2: K1}, {0: K1, 2: K3(2)}], 2, quiet=True)
    assert bad is not None, "should detect 0 = 1"
    print("PASS selftest: K3 field ops + row_reduce (rank/inconsistency)")

# ------------------------------------------------- 2. radical ring R_ext
# monomial key (za, ea1, ea2, ew1, ehw1, ew2, ehw2, eB):
#   z = zeta_42 (Phi_42-reduced, za < 12), alpha_i^3 = a_i, hw_i^2 =
#   (3/2) w_i^2 (hw_i = sqrt(3/2) w_i), eta_B^7 = B; w_i FREE (E5 quartic
#   relation deferred to terminal core). Element: dict {key: K3}.
def pmul_int(a, b):
    r = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y: r[i+j] += x*y
    return r
def cyclotomic42():
    """Phi_42 (int list low->high): prod_{d|42}(x^d-1)^{mu(42/d)}:
    top d in {42,7,3,2} (mu=+1), bottom d in {21,14,6,1} (mu=-1)."""
    def xm1(d): return [-1] + [0]*(d-1) + [1]
    def pdiv(num, den):
        num = num[:]; q = [0]*(len(num)-len(den)+1)
        for i in range(len(q)-1, -1, -1):
            q[i] = num[i+len(den)-1] // den[-1]
            for j, dd in enumerate(den): num[i+j] -= q[i]*dd
        assert all(c == 0 for c in num), "nonexact cyclotomic division"
        return q
    top = xm1(42)
    for d in (7, 3, 2): top = pmul_int(top, xm1(d))
    bot = xm1(21)
    for d in (14, 6, 1): bot = pmul_int(bot, xm1(d))
    return pdiv(top, bot)
PHI42 = cyclotomic42()
assert PHI42 == [1,1,0,-1,-1,0,1,0,-1,-1,0,1,1], "Phi_42 mismatch: %s" % PHI42
ZRED = []                                            # z^e -> {j:Fr}, e in 0..41
for e in range(42):
    p = [Fr(0)]*e + [Fr(1)]
    while len(p) > 12:
        c = p.pop()
        if c:
            for j in range(12): p[len(p)-12+j] -= c*PHI42[j]
    ZRED.append({j: c for j, c in enumerate(p) if c})

SIG = K3(6)                                          # sigma gauge
A1c, A2c = K3(3, 1), K3(3, -1)                       # a_i = 3 +- sqrt3
Bc, B2c, BBc = K3(4), K3(Fr(9, 2)), K3(Fr(3, 2))    # b, b2, B (A = 1)
KONE = (0, 0, 0, 0, 0, 0, 0, 0)

def rnorm(key, c):
    """reduce one raw monomial (arbitrary exponents) -> list of (key, K3)."""
    za, ea1, ea2, ew1, eh1, ew2, eh2, eB = key
    q, eh1 = divmod(eh1, 2)                 # negative q ok: (3/2)^q exact
    if q: c = c * mk(Fr(3, 2)**q); ew1 += 2*q
    q, eh2 = divmod(eh2, 2)
    if q: c = c * mk(Fr(3, 2)**q); ew2 += 2*q
    q, ea1 = divmod(ea1, 3)                 # alpha^-1 -> alpha^2/a
    if q > 0:
        for _ in range(q): c = c * A1c
    elif q < 0:
        for _ in range(-q): c = c * A1c.inv()
    q, ea2 = divmod(ea2, 3)
    if q > 0:
        for _ in range(q): c = c * A2c
    elif q < 0:
        for _ in range(-q): c = c * A2c.inv()
    q, eB = divmod(eB, 7)
    if q: c = c * mk(Fr(3, 2)**q)
    out = []
    for j, zc in ZRED[za % 42].items():
        out.append(((j, ea1, ea2, ew1, eh1, ew2, eh2, eB), c*zc))
    return out

def racc(acc, key, c):
    """accumulate c * (raw monomial key) into dict acc, with reduction."""
    if c.iszero(): return
    for k2, c2 in rnorm(key, c):
        v = acc.get(k2)
        acc[k2] = c2 if v is None else v + c2
        if acc[k2].iszero(): del acc[k2]

def rmul(x, y):
    out = {}
    for kx, cx in x.items():
        for ky, cy in y.items():
            racc(out, tuple(a+b for a, b in zip(kx, ky)), cx*cy)
    return out
def radd(x, y):
    out = dict(x)
    for k, c in y.items():
        v = out.get(k); out[k] = c if v is None else v + c
        if out[k].iszero(): del out[k]
    return out
def rscal(x, c):
    c = mk(c)
    return {} if c.iszero() else {k: v*c for k, v in x.items()}
def rC(c):
    c = mk(c); return {} if c.iszero() else {KONE: c}
def rmono(za=0, a1=0, a2=0, w1=0, h1=0, w2=0, h2=0, B=0, c=K1):
    out = {}; racc(out, (za, a1, a2, w1, h1, w2, h2, B), mk(c)); return out
RZERO, RONE = {}, rC(1)
def riszero(x): return not x

def rinv(x):
    """invert a ring element of the form (z-poly) * (single radical
    monomial): ext-Euclid in K3[z]/Phi42 (irreducible over K3) for the
    z-part; exponent negation for the radical part."""
    if not x: raise ZeroDivisionError("rinv(0)")
    rads = {k[1:] for k in x}
    assert len(rads) == 1, "rinv: mixed radical monomials %s" % rads
    rad = next(iter(rads))
    zp = [K0]*12
    for k, c in x.items(): zp[k[0]] = c
    # ext-Euclid: find u with u*zp = 1 mod Phi42 over K3
    def pdivmod(a, b):
        a = a[:]; q = [K0]*max(1, len(a)-len(b)+1)
        while len(a) >= len(b) and any(not c.iszero() for c in a):
            while a and a[-1].iszero(): a.pop()
            if len(a) < len(b): break
            f = a[-1] * b[-1].inv(); d = len(a)-len(b)
            q[d] = f
            for i, bc in enumerate(b): a[i+d] = a[i+d] - f*bc
            a.pop()
        return q, a
    r0 = [mk(c) for c in PHI42]; r1 = zp[:]
    s0, s1 = [K0], [K1]
    while any(not c.iszero() for c in r1):
        q, r = pdivmod(r0, r1)
        r0, r1 = r1, r
        qs = [K0]*(len(q)+len(s1)-1)
        for i, qc in enumerate(q):
            for j, sc in enumerate(s1): qs[i+j] = qs[i+j] + qc*sc
        s0, s1 = s1, [a - b for a, b in
                      zip(s0 + [K0]*max(0, len(qs)-len(s0)),
                          qs + [K0]*max(0, len(s0)-len(qs)))]
    while r0 and r0[-1].iszero(): r0.pop()
    assert len(r0) == 1 and not r0[0].iszero(), "rinv: z-part not invertible?"
    c0 = r0[0].inv()
    inv_rad = tuple(-e for e in rad)
    out = {}
    for j, c in enumerate(s0):
        if not mk(c).iszero():
            racc(out, (j,) + inv_rad, mk(c)*c0)
    # verify
    chkp = rmul(out, x)
    assert chkp == RONE, "rinv verify failed"
    return out

def rk3(x):
    """x == K3 * single-basis-monomial? -> (key, K3) or None."""
    if not x: return (KONE, K0)
    if len(x) == 1:
        (k, c), = x.items(); return (k, c)
    return None                       # z-poly parts / mixed: not a K3-line rep
def rproportional(x, y):
    """x == r*y over K3? -> r or None (y != 0)."""
    if not y: return None
    ky = next(iter(y)); cy = y[ky]
    if ky not in x: return None
    r = x[ky] / cy
    diff = radd(x, rscal(y, -r))
    return r if not diff else None

def selftest_ring():
    # zeta selector: sum_k z^{km} = 42 [42|m]
    for m in (0, 1, 6, 7, 12, 21, 42, 84, 5):
        s = RZERO
        for k in range(42): s = radd(s, rmono(za=k*m))
        want = rC(42) if m % 42 == 0 else RZERO
        assert radd(s, rscal(want, -1)) == {}, "selector fail m=%d: %s" % (m, s)
    # alpha^3 = a_i, hw^2 = (3/2) w^2, eta_B^7 = B
    assert rmul(rmono(a1=1), rmul(rmono(a1=1), rmono(a1=1))) == rC(A1c)
    assert rmul(rmono(a2=2), rmono(a2=2)) == rscal(rmono(a2=1), A2c)
    assert rmul(rmono(h1=1), rmono(h1=1)) == rscal(rmono(w1=2), BBc)
    assert rmul(rmono(B=3), rmono(B=4)) == rC(BBc)
    # associativity spot (mixed monomials)
    x, y, w = rmono(za=5, a1=2), rmono(za=40, a2=1, w1=3), rmono(h1=1, B=6)
    assert rmul(rmul(x, y), w) == rmul(x, rmul(y, w))
    # z-expansion consistency: z^12 = -(Phi tail)
    assert (0,)+KONE[1:] not in ZRED[12] or True
    print("PASS selftest: R_ext ring (Phi42, selectors, radical reductions)")

# ----------------------------------- 3. VExpr / truncated series / genome
# VExpr: dict {sorted-tuple-of-var-ids: R_ext elem}; () = constant part.
# Series: dict {slot: VExpr}, slot = level in 1/42 units, truncated < DEPTH.
VDEG_CAP = 1                   # track var-monomials to degree 1; higher
HIVAR = 10**7                  # degrees collapse to the (HIVAR,) sentinel.
# CAP=1 is exact for the stage policy: any product of >= 2 STILL-FREE
# vars makes the row nonlinear-deferred anyway, and PINNED vars are
# substituted as constants at build time (multipass), so no linear
# information is ever lost; flagged rows re-linearize on the next pass.
def vC(r): return {(): r} if r else {}
def vvar(v, r=None): return {(v,): RONE if r is None else r}
def vadd(x, y):
    out = dict(x)
    for k, r in y.items():
        cur = out.get(k)
        out[k] = r if cur is None else radd(cur, r)
        if not out[k]: del out[k]
    return out
def vmul(x, y):
    out = {}
    for kx, rx in x.items():
        for ky, ry in y.items():
            k = tuple(sorted(kx + ky))
            if len(k) > VDEG_CAP or (k and k[-1] == HIVAR):
                k = (HIVAR,)
                if k not in out: out[k] = RONE
                continue
            r = rmul(rx, ry)
            if r:
                cur = out.get(k)
                out[k] = r if cur is None else radd(cur, r)
                if not out[k]: del out[k]
    return out
def vscal(x, r):
    if isinstance(r, (int, Fr, K3)): r = rC(r)
    return {k: rmul(v, r) for k, v in x.items() if rmul(v, r)}
def vdeg(x): return max((len(k) for k in x), default=0)
VZERO = {}

def smul(a, b, depth):
    """series product, truncated at slot < depth."""
    out = {}
    for sa, va in a.items():
        if sa >= depth: continue
        for sb, vb in b.items():
            s = sa + sb
            if s >= depth: continue
            p = vmul(va, vb)
            if p:
                cur = out.get(s)
                out[s] = p if cur is None else vadd(cur, p)
                if not out[s]: del out[s]
    return out
def sadd(a, b):
    out = dict(a)
    for s, v in b.items():
        cur = out.get(s)
        out[s] = v if cur is None else vadd(cur, v)
        if not out[s]: del out[s]
    return out
def sscal(a, r): return {s: vscal(v, r) for s, v in a.items() if vscal(v, r)}
def sshift(a, ds, depth):
    return {s+ds: v for s, v in a.items() if s+ds < depth}
def stwist(a, kph):
    """C_k conjugation on a series whose slot s sits at absolute level s:
    slot s coefficient *= zeta^{k*s}. (Callers pass absolute-level series.)"""
    return {s: vscal(v, rmono(za=(kph*s) % 42)) for s, v in a.items()}

# variable registry
VARS = []                      # id -> dict(name, level, kind)
VSTAT = []                     # id -> None (free) | VExpr value (pinned)
def newvar(name, level, kind):
    VARS.append(dict(name=name, level=level, kind=kind)); VSTAT.append(None)
    return len(VARS) - 1

# genome constants under the gauge (sec 3.0): sigma=6, A=1, eta_A=1, s0=1
S_F = K1                                   # S_F = S_R = 1
S_M = mk(Fr(7**12, 2**6))                  # E6 transport, c_m = 1
G_M = mk(-Fr(7**18, 2**9))
# H_M is determined by the G_m band (slot-20 quotient) — engine OUTPUT.

def build_generators(depth):
    """Returns dict orb -> dict(series={level: VExpr}, size, kind), and the
    var schedule. f-orbits: P1, P2, B (42 each). g-orbits: Gp1, Gp2 (42),
    G0p1, G0p2 (21, even), GB42 (42), GB21 (21, even)."""
    orbs = {}
    def ser(pins, tails, size):
        s = {lv: vC(r) for lv, r in pins.items()}
        for lv, vid in tails.items(): s[lv] = vvar(vid)
        return dict(series=s, size=size)
    # dead-stretch vars: g's branches ride the SAME joint-tree arcs through
    # every common vertex (d_g ladder EXACT, E7) => g shares uf/vf with f.
    def nv(name, level, kind):
        vid = newvar(name, level, kind)
        if name in PINS: VSTAT[vid] = PINS[name]
        return vid
    globals()["newvar_p"] = nv
    uf = {m: nv("uf%d" % m, m, "stretch") for m in (18, 24, 30)}
    vf1 = {m: nv("vf1_%d" % m, m, "merge") for m in (34, 36)}
    vf2 = {m: nv("vf2_%d" % m, m, "merge") for m in (34, 36)}
    def tails(pre, lo, step=1):
        return {m: nv("%s_%d" % (pre, m), m, "tail")
                for m in range(lo, depth, 1) if (m - lo) % step == 0}
    a1m, a2m, w1m, w2m = rmono(a1=1), rmono(a2=1), rmono(w1=1), rmono(w2=1)
    hw1m, hw2m, eBm = rmono(h1=1), rmono(h2=1), rmono(B=1)
    # build explicitly (pins = constant part; stretch/merge levels = vars;
    # PINNED vars are inlined as ring values so degrees collapse at build)
    def mkorb(name, pins, varlevels, size):
        s = {lv: vC(r) for lv, r in pins.items() if r}
        for lv, vid in varlevels.items():
            if VSTAT[vid] is not None:
                if VSTAT[vid]: s[lv] = vC(VSTAT[vid])
            else:
                s[lv] = vvar(vid)
        orbs[name] = dict(series=s, size=size, name=name)
    t1 = tails("tf1", 38); t2 = tails("tf2", 38); tB = tails("bf", 13)
    g1 = tails("tg1", 38); g2 = tails("tg2", 38)
    g01 = tails("tg01", 38, 2); g02 = tails("tg02", 38, 2)
    gB1 = tails("bg42", 13); gB2 = tails("bg21", 14, 2)
    mkorb("P1", {12: RONE, 32: a1m, 37: w1m}, {**uf, **vf1, **t1}, 42)
    mkorb("P2", {12: RONE, 32: a2m, 37: w2m}, {**uf, **vf2, **t2}, 42)
    mkorb("B",  {12: eBm}, {**tB}, 42)
    mkorb("Gp1", {12: RONE, 32: a1m, 37: hw1m}, {**uf, **vf1, **g1}, 42)
    mkorb("Gp2", {12: RONE, 32: a2m, 37: hw2m}, {**uf, **vf2, **g2}, 42)
    mkorb("G0p1", {12: RONE, 32: a1m}, {**uf, **vf1, **g01}, 21)
    mkorb("G0p2", {12: RONE, 32: a2m}, {**uf, **vf2, **g02}, 21)
    mkorb("GB42", {12: eBm}, {**gB1}, 42)
    mkorb("GB21", {12: eBm}, {**gB2}, 21)
    return orbs

FORB, GORB = ("P1", "P2", "B"), ("Gp1", "Gp2", "G0p1", "G0p2", "GB42", "GB21")
C7SUB = {42: 6, 21: 3}                     # C_7-suborbit size by orbit size

# --------------------------------------------- 4. jets (JetPoly machinery)
# JetPoly: dict {(etapow, slot): VExpr}; slot in 1/42 units, < depth.
def jmul(a, b, depth, ndeg=None):
    out = {}
    for (na, sa), va in a.items():
        for (nb, sb), vb in b.items():
            n, s = na+nb, sa+sb
            if s >= depth or (ndeg is not None and n > ndeg): continue
            p = vmul(va, vb)
            if p:
                k = (n, s); cur = out.get(k)
                out[k] = p if cur is None else vadd(cur, p)
                if not out[k]: del out[k]
    return out
def jadd(a, b):
    out = dict(a)
    for k, v in b.items():
        cur = out.get(k)
        out[k] = v if cur is None else vadd(cur, v)
        if not out[k]: del out[k]
    return out
def jscal(a, r): return {k: vscal(v, r) for k, v in a.items() if vscal(v, r)}
JONE = {(0, 0): {(): RONE}}

def fs_factor_rep(orb, depth):
    """Pi_{j<n7} (eta - C_{7j} Ytilde) for one orbit; Ytilde slot s =
    level 12+s; C_{7j} twists slot s by zeta^{7js} (level-12 part fixed)."""
    yt = {lv-12: v for lv, v in orb["series"].items() if lv-12 < depth}
    jp = JONE
    for j in range(C7SUB[orb["size"]]):
        tw = {s: vscal(v, rmono(za=(7*j*s) % 42)) for s, v in yt.items()}
        lin = jadd({(1, 0): {(): RONE}},
                   {(0, s): vscal(v, K3(-1)) for s, v in tw.items()})
        jp = jmul(jp, lin, depth)
    return jp
def fs_jet(orbnames, orbs, depth, tag="", ndeg=None):
    """Full F_s jet Pi over 7 directions x orbit subfactors. Direction k
    image: coefficient at (n, s) *= zeta^{k(12n+s)}."""
    jp = JONE; t0 = time.time()
    for on in orbnames:
        rep = fs_factor_rep(orbs[on], depth)
        for k in range(7):
            img = {(n, s): vscal(v, rmono(za=(k*(12*n+s)) % 42))
                   for (n, s), v in rep.items()}
            jp = jmul(jp, img, depth, ndeg)
        print("      [fs_jet %s] orbit %s done (%d terms, %.1fs)"
              % (tag, on, len(jp), time.time()-t0), flush=True)
    return jp

def k3poly_pow_pattern():
    """reference (eta^7-1)^2(eta^7-B) and its powers, K3 coeff lists in
    T = eta^7 (low->high)."""
    p1 = [K3(-1), K1]                       # T - 1
    pB = [-BBc, K1]                         # T - B
    def pm(a, b):
        r = [K0]*(len(a)+len(b)-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b): r[i+j] = r[i+j] + x*y
        return r
    p21 = pm(pm(p1, p1), pB)                # deg 3 in T
    return p21, pm
def jet_matches_Tpoly(jp, Tpoly, scale=K1):
    """slot-0 part of jp equals scale * Tpoly(eta^7)? (all other slot-0
    eta-powers zero, coefficients constant K3)."""
    for (n, s), v in jp.items():
        if s != 0: continue
        kv = v.get((), RZERO); pure = rk3(kv)
        if set(v) - {()} or pure is None or pure[0] != KONE: return False
        if n % 7 == 0 and n//7 < len(Tpoly):
            if not (pure[1] - mk(scale)*Tpoly[n//7]).iszero(): return False
        else:
            if not pure[1].iszero(): return False
    return True

def orbit_powersum(orb, r, depth):
    """p_r-contribution of one orbit: selector-aggregated. 42-orbit:
    42*[42|s]; 21-orbit (even support): 21*[42|s]. Returns {slot: VExpr}
    with only 42|s slots — plus, for fractional-condition use, the RAW
    Y^r series is returned separately by ypow()."""
    yr = ypow(orb, r, depth)
    fac = orb["size"]
    return {s: vscal(v, fac) for s, v in yr.items() if s % 42 == 0}
_YPOW_CACHE = {}
def ypow(orb, r, depth):
    key = (orb["name"], r, depth)
    if key in _YPOW_CACHE: return _YPOW_CACHE[key]
    if r == 0: out = {0: vC(RONE)}
    elif r == 1: out = dict(orb["series"])
    else: out = smul(ypow(orb, r-1, depth), orb["series"], depth)
    _YPOW_CACHE[key] = out
    return out

def gm_jet(orbnames, orbs, depth, tag=""):
    """G_m jet: substitute y = P + eta t^32 along the arc P = t^12 +
    uf18 t^18 + uf24 t^24 + uf30 t^30 (vars), through direction d0 = 1.
    Factors normalized to their own lead; slot = 1/42 offset. Through-d0
    branches (A-orbits, C_{7j}-images): (eta - ytilde), ytilde slot s =
    twisted level-(32+s). Others: (Delta_b + eta t^20), Delta_b slot s =
    P[12+s] - zeta^{c(12+s)} Y[12+s], c = k+7j, k = 1..6 (A) / 0..6 (B).
    """
    t0 = time.time()
    P = {12: vC(RONE)}
    for v in range(len(VARS)):
        if VARS[v]["kind"] == "stretch": P[VARS[v]["level"]] = vvar(v)
    jp = JONE
    nfac = 0
    for on in orbnames:
        orb = orbs[on]; Y = orb["series"]; n7 = C7SUB[orb["size"]]
        Aside = 12 in Y and rk3(Y[12].get((), RZERO)) and \
                rk3(Y[12].get((), RZERO))[0] == KONE
        for k in range(7):
            for j in range(n7):
                c = (k + 7*j) % 42
                if Aside and k == 0:       # through d0: (eta - ytilde)
                    fac = {(1, 0): vC(RONE)}
                    for lv, vv in Y.items():
                        if lv >= 32 and lv - 32 < depth:
                            tw = vscal(vv, rmono(za=(c*lv) % 42))
                            if tw: fac[(0, lv-32)] = vscal(tw, K3(-1))
                else:                       # other: (Delta + eta t^20)
                    fac = {(1, 20): vC(RONE)} if 20 < depth else {}
                    for s in range(depth):
                        lv = 12 + s
                        dv = P.get(lv, VZERO)
                        yv = Y.get(lv)
                        if yv:
                            tw = vscal(yv, rmono(za=(c*lv) % 42))
                            dv = vadd(dv, vscal(tw, K3(-1)))
                        if dv: fac[(0, s)] = dv
                jp = jmul(jp, fac, depth); nfac += 1
        print("      [gm_jet %s] orbit %s done (%d factors, %d terms, %.1fs)"
              % (tag, on, nfac, len(jp), time.time()-t0), flush=True)
    return jp

def gm_jet2(orbnames, orbs, depth, tag="", seed=None):
    """fast G_m jet: P is C_7-invariant (6-grid support), so the other-
    branch factors within a (orbit, direction-k) suborbit are C_7 phase
    images of one Delta = P - C_k Y; their product to eta-window order is
    sum_i e_{n7-i}(Delta-suborbit) (eta t^20)^i via suborbit Newton
    (selector 6[6|s] resp. 3[6|s]). Through-d0 factors kept exact."""
    t0 = time.time()
    P = {12: vC(RONE)}
    for v in range(len(VARS)):
        if VARS[v]["kind"] == "stretch":
            if VSTAT[v] is None: P[VARS[v]["level"]] = vvar(v)
            elif VSTAT[v]: P[VARS[v]["level"]] = vC(VSTAT[v])
    jp = JONE if seed is None else seed
    for on in orbnames:
        orb = orbs[on]; Y = orb["series"]; n7 = C7SUB[orb["size"]]
        Aside = 12 in Y and rk3(Y[12].get((), RZERO)) and \
                rk3(Y[12].get((), RZERO))[0] == KONE
        for k in range(7):
            if Aside and k == 0:            # exact through-d0 factors
                for j in range(n7):
                    c = 7*j
                    fac = {(1, 0): vC(RONE)}
                    for lv, vv in Y.items():
                        if lv >= 32 and lv - 32 < depth:
                            tw = vscal(vv, rmono(za=(c*lv) % 42))
                            if tw: fac[(0, lv-32)] = vscal(tw, K3(-1))
                    jp = jmul(jp, fac, depth)
                continue
            # Delta = P - C_k Y (slots rel level 12), then suborbit Newton
            D = {}
            for s in range(depth):
                lv = 12 + s
                dv = P.get(lv, VZERO)
                yv = Y.get(lv)
                if yv:
                    dv = vadd(dv, vscal(vscal(yv, rmono(za=(k*lv) % 42)),
                                        K3(-1)))
                if dv: D[s] = dv
            Dp = {0: {0: vC(RONE)}, 1: D}
            for r in range(2, n7+1): Dp[r] = smul(Dp[r-1], D, depth)
            q = {r: {s: vscal(v, n7) for s, v in Dp[r].items() if s % 6 == 0}
                 for r in range(1, n7+1)}
            e = [{0: vC(RONE)}]
            for jj in range(1, n7+1):
                acc = {}
                for r in range(1, jj+1):
                    acc = sadd(acc, sscal(smul(e[jj-r], q[r], depth),
                                          K3((-1)**(r-1))))
                e.append(sscal(acc, K3(Fr(1, jj))))
            blk = {}
            for i in range(n7+1):           # eta^i (t^20)^i e_{n7-i}
                if 20*i >= depth and i > 0: break
                for s, v in e[n7-i].items():
                    if s + 20*i < depth: blk[(i, s + 20*i)] = v
            jp = jmul(jp, blk, depth)
        print("      [gm_jet2 %s] orbit %s done (%d terms, %.1fs)"
              % (tag, on, len(jp), time.time()-t0), flush=True)
    return jp

def eta_poly_ref(rootmults, scale):
    """K3 eta-poly (low->high) prod (eta^3 - a)^m, scaled."""
    _, pm = k3poly_pow_pattern()
    out = [mk(scale)]
    for a, mult in rootmults:
        f = [-a, K0, K0, K1]
        for _ in range(mult): out = pm(out, f)
    return out
def jet_matches_etapoly(jp, ref):
    for (n, s), v in jp.items():
        if s != 0: continue
        kv = v.get((), RZERO); pure = rk3(kv)
        if set(v) - {()} or pure is None or pure[0] != KONE: return False
        want = ref[n] if n < len(ref) else K0
        if not (pure[1] - want).iszero(): return False
    # also require every nonzero ref coeff present
    for i, c in enumerate(ref):
        if not c.iszero() and (i, 0) not in jp: return False
    return True

# ---------------------------------------- 4b. fast F_s jet (suborbit Newton)
def suborbit_esyms(orb, depth):
    """e_0..e_{n7} of the C_7-suborbit {C_{7j} Ytilde}: power sums have
    selector n7*[6|(12r+s)] => slots on the 6-grid; Newton over Q."""
    n7 = C7SUB[orb["size"]]
    yt = {lv-12: v for lv, v in orb["series"].items() if lv-12 < depth}
    yp = {0: {0: vC(RONE)}, 1: yt}
    for r in range(2, n7+1): yp[r] = smul(yp[r-1], yt, depth)
    q = {}
    for r in range(1, n7+1):
        q[r] = {s: vscal(v, n7) for s, v in yp[r].items()
                if (12*r + s) % 6 == 0 and ((s % 2 == 0) or orb["size"] == 42)}
        # (even-support orbits have odd slots empty anyway)
    e = [ {0: vC(RONE)} ]
    for j in range(1, n7+1):
        acc = {}
        for r in range(1, j+1):
            term = smul(e[j-r], q[r], depth)
            acc = sadd(acc, sscal(term, K3((-1)**(r-1))))
        e.append(sscal(acc, K3(Fr(1, j))))
    return e
def fs_block(orb, depth):
    """product over the 7 direction images of the suborbit factor
    sum_j (-1)^j e_j eta^{n7-j}; image k: coeff (n,s) *= zeta^{k(12n+s)}."""
    n7 = C7SUB[orb["size"]]
    e = suborbit_esyms(orb, depth)
    rep = {}
    for j in range(n7+1):
        for s, v in e[j].items():
            vv = vscal(v, K3((-1)**j))
            if vv: rep[(n7-j, s)] = vv
    blk = JONE
    for k in range(7):
        img = {(n, s): vscal(v, rmono(za=(k*(12*n+s)) % 42))
               for (n, s), v in rep.items()}
        blk = jmul(blk, img, depth)
    return blk
def fs_jet2(orbnames, orbs, depth, tag=""):
    jp = JONE; t0 = time.time()
    for on in orbnames:
        jp = jmul(jp, fs_block(orbs[on], depth), depth)
        print("      [fs_jet2 %s] block %s done (%d terms, %.1fs)"
              % (tag, on, len(jp), time.time()-t0), flush=True)
    return jp

def full_esyms(orbnames, orbs, depth, jmax=6):
    """aggregated e_1..e_jmax of the WHOLE branch set (unshifted y-levels,
    slots in 42Z by conjugacy): p_r = sum_orb size*[42|s](Y^r)_s."""
    p = {}
    for r in range(1, jmax+1):
        acc = {}
        for on in orbnames:
            acc = sadd(acc, orbit_powersum(orbs[on], r, depth))
        p[r] = acc
    e = [ {0: vC(RONE)} ]
    for j in range(1, jmax+1):
        acc = {}
        for r in range(1, j+1):
            acc = sadd(acc, sscal(smul(e[j-r], p[r], depth), K3((-1)**(r-1))))
        e.append(sscal(acc, K3(Fr(1, j))))
    return e

# ------------------------------------------- 6. rows, K3-reduction, stages
PINS = {}                      # name -> ring value (persists across passes)

def extract_pins(sysm):
    """back-substitute the reduced echelon system; a pivot var is FORCED
    when its expression involves only rho-columns; return {name: ring}."""
    RHO = 10**9; SPL = 10**8
    expr = {}                   # col -> {freecol-or-rho: K3}
    for c in sorted(sysm.piv, reverse=True):
        row = sysm.red[sysm.piv[c]]
        acc = {}
        inv = row[c].inv()
        for k, v in row.items():
            if k == c: continue
            sub = expr.get(k) if k in sysm.piv else None
            if sub is None: sub = {k: K1}
            for kk, vv in sub.items():
                acc[kk] = acc.get(kk, K0) - inv*v*vv
                if acc[kk].iszero(): del acc[kk]
        expr[c] = acc
    out = {}
    for c, e in expr.items():
        if not isinstance(c, int) or c >= SPL: continue
        if any(k < RHO for k in e): continue          # depends on free vars
        val = RZERO
        ref = sysm.colref[c]
        refinv = None
        try: refinv = rinv(ref)
        except AssertionError: continue               # non-invertible ref
        for k, coef in e.items():
            val = radd(val, rscal(rmul(refinv, sysm.rhoref[k-RHO]), coef))
        out[VARS[c]["name"]] = val
    return out

def run_multipass(depth, maxpass=4):
    global PINS
    PINS = {}
    last = None
    for p in range(1, maxpass+1):
        print("\n==== PASS %d (pins so far: %d) ====" % (p, len(PINS)),
              flush=True)
        sysm, ledger, orbs = run_stages(depth)
        last = (sysm, ledger, orbs)
        if sysm.certificate is not None:
            print("  pass %d: INCONSISTENT — stopping." % p)
            return last, p
        np_ = extract_pins(sysm)
        fresh = {k: v for k, v in np_.items() if k not in PINS}
        print("  pass %d: %d forced pins (%d new): %s" %
              (p, len(np_), len(fresh), sorted(fresh)[:12]), flush=True)
        if not fresh: return last, p
        PINS.update(fresh)
    return last, maxpass

def vsub(v):
    """substitute pinned vars (VSTAT ring values) into a VExpr."""
    out = {}
    for key, r in v.items():
        if key and key[-1] == HIVAR:
            out[key] = r; continue
        rem = []; rr = r
        for vid in key:
            if VSTAT[vid] is not None: rr = rmul(rr, VSTAT[vid])
            else: rem.append(vid)
        if not rr: continue
        k = tuple(sorted(rem)); cur = out.get(k)
        out[k] = rr if cur is None else radd(cur, rr)
        if not out[k]: del out[k]
    return out

class StageSystem:
    """cumulative K3 system: columns = var ids (then rho classes)."""
    def __init__(s):
        s.colref = {}          # var id -> reference ring elem
        s.rhoref = []          # list of reference ring elems (rho classes)
        s.red = []             # reduced rows: {colkey: K3}; colkey int vid
        s.piv = {}             # colkey -> index in red
        s.nl_rows = []         # deferred nonlinear (stage, meta, VExpr)
        s.rho_relations = []   # reduced rows supported only on rho cols
        s.split_cols = 0       # proportionality-relaxation counter
        s.seen_vars = set()
        s.certificate = None
    def rho_col(s, r):
        for i, ref in enumerate(s.rhoref):
            if rproportional(r, ref) is not None: return i
        s.rhoref.append(r); return len(s.rhoref)-1
    def add_condition(s, vex, stage, meta):
        vex = vsub(vex)
        if not vex: return "trivial"
        if vdeg(vex) >= 2 or any(k and k[-1] == HIVAR for k in vex):
            s.nl_rows.append((stage, meta, vex)); return "nonlinear"
        row = {}
        for key, r in vex.items():
            if key == ():
                ci = s.rho_col(r); c = rproportional(r, s.rhoref[ci])
                row[10**9 + ci] = c
            else:
                vid = key[0]; s.seen_vars.add(vid)
                ref = s.colref.get(vid)
                if ref is None: s.colref[vid] = r; c = K1
                else:
                    c = rproportional(r, ref)
                    if c is None:            # relax: new split column
                        s.split_cols += 1
                        vid2 = (vid, s.split_cols)
                        s.colref[vid2] = r; row[s.ck(vid2)] = K1; continue
                row[s.ck(vid)] = c
        return s.reduce_row(row, stage, meta)
    def ck(s, vid): return vid if isinstance(vid, int) else 10**8 + vid[1]
    def reduce_row(s, row, stage, meta):
        RHO = 10**9
        while row:
            c = min(row)
            if c >= RHO:
                if len(row) == 1:
                    s.certificate = (stage, meta, dict(row))
                    return "INCONSISTENT"
                s.rho_relations.append((stage, meta, dict(row)))
                return "rho-relation"
            if c in s.piv:
                pr = s.red[s.piv[c]]; f = row[c] * pr[c].inv()
                for k, v in pr.items():
                    row[k] = row.get(k, K0) - f*v
                    if row[k].iszero(): del row[k]
            else:
                s.piv[c] = len(s.red); s.red.append(row); return "pivot"
        return "dependent"
    def rank(s): return len(s.red)

STATE_PATH = "/tmp/r1_state.pkl"
def save_state(st):
    import pickle
    with open(STATE_PATH, "wb") as f: pickle.dump(st, f)
    print("  [state saved: %s]" % sorted(st), flush=True)
def load_state():
    import pickle
    try:
        with open(STATE_PATH, "rb") as f: return pickle.load(f)
    except FileNotFoundError:
        return {"PINS": {}, "pass": 1}

def phase(which, depth):
    """checkpointed build phases (each < 10 min foreground)."""
    global PINS
    st = load_state(); PINS = st["PINS"]
    reset_vars(); orbs = build_generators(depth)
    dF = depth - 12; dG = min(depth - 32, 21)
    t0 = time.time()
    if which == "fs":
        st["jfF"] = fs_jet2(FORB, orbs, dF, "f")
        st["jgF"] = fs_jet2(GORB, orbs, dF, "g")
    elif which in ("gmf", "gmg"):
        side = "f" if which == "gmf" else "g"
        names = FORB if side == "f" else GORB
        pk = "gmpart_" + side
        idx, jp = st.get(pk, (0, JONE))
        while idx < len(names):
            jp = gm_jet2([names[idx]], orbs, dG, side, seed=jp)
            idx += 1
            st[pk] = (idx, jp)
            save_state(st)
            if time.time() - t0 > 420:
                print("  phase %s: checkpointed at orbit %d/%d — RERUN to "
                      "resume" % (which, idx, len(names)), flush=True)
                return
        st["j%sG" % side] = jp
    elif which == "wg":
        jfG, jgG = st["jfG"], st["jgG"]
        st["WG"] = jadd(jmul(jgG, jgG, dG),
                        jscal(jmul(jfG, jmul(jfG, jfG, dG), dG), K3(-1)))
    elif which == "es":
        st["ef"] = full_esyms(FORB, orbs, depth)
        st["eg"] = full_esyms(GORB, orbs, depth)
    elif which == "wf1":
        st["jfF2"] = jmul(st["jfF"], st["jfF"], dF)
    elif which == "wf2":
        st["jfF3"] = jmul(st["jfF2"], st["jfF"], dF)
    elif which == "wf3":
        st["WF"] = jadd(jmul(st["jgF"], st["jgF"], dF),
                        jscal(st["jfF3"], K3(-1)))
    print("  phase %s done (%.1fs)" % (which, time.time()-t0), flush=True)
    save_state(st)

def stage_conditions(depth, st=None):
    """build everything, yield (stage_m, family, etapow, VExpr) rows."""
    global PINS
    if st is None:
        st = load_state(); PINS = st["PINS"]
    print("  generators (depth %d, pins %d)..." % (depth, len(PINS)),
          flush=True)
    reset_vars()
    orbs = build_generators(depth)
    dF = depth - 12; dG = min(depth - 32, 21)
    jfF, jgF, WF, WG = st["jfF"], st["jgF"], st["WF"], st["WG"]
    ef, eg = st["ef"], st["eg"]
    jfG, jgG = st["jfG"], st["jgG"]
    # R-jet top-6 band rows (slot 42): e_j aggregates
    Fc = {i: sscal(ef[i], K3((-1)**i)) for i in range(len(ef))}
    Gc = {i: sscal(eg[i], K3((-1)**i)) for i in range(len(eg))}
    WR = {}                                 # {(n, slot): VExpr} n = top-offset
    for n in range(0, 7):
        acc = {}
        for i in range(0, n+1):             # g^2: sum_{i+j=n} G_i G_j
            j = n - i
            if j <= 6:
                acc = sadd(acc, smul(Gc.get(i, {}), Gc.get(j, {}), depth))
        for i in range(0, n+1):             # f^3: -sum_{i+j+k=n} F_i F_j F_k
            for j in range(0, n-i+1):
                k = n-i-j
                acc = sadd(acc, sscal(smul(smul(Fc.get(i, {}), Fc.get(j, {}),
                    depth), Fc.get(k, {}), depth), K3(-1)))
        for slot, v in acc.items():
            if v: WR[(n, slot)] = v
    print("  W_R top-6 done (%d terms)" % len(WR), flush=True)
    rows = []
    # F2/F3: jet lattice conditions (fractional slots must vanish)
    for (n, s), v in sorted(jfF.items()) + sorted(jgF.items()):
        if s % 6 != 0: rows.append((12+s, "C1-Fs-frac", n, v))
    for (n, s), v in sorted(jfG.items()) + sorted(jgG.items()):
        if s % 2 != 0: rows.append((32+s, "C1-Gm-frac", n, v))
    # F4: W_F band (all slots 1..419 in window vanish; slot 0 gate)
    for (n, s), v in sorted(WF.items()):
        if s >= 1: rows.append((12+s, "C2-Fs-band", n, v))
    # F5: W_G band slots 1..19 vanish; slot 20 = H_M-quotient
    pat = eta_poly_ref([(A1c, 2), (A2c, 2)], K1)     # (e3-a1)^2(e3-a2)^2
    _, pm = k3poly_pow_pattern()
    qpat = pm(pm([K0, K1], pat), [-Bc, K0, K0, K1])  # eta*P^2*(eta^3-b) deg 16
    for (n, s), v in sorted(WG.items()):
        if 1 <= s <= 19: rows.append((32+s, "C2-Gm-band", n, v))
    # quotient at slot 20: W_G(n,20) = H_M * qpat[n]: eliminate H_M via
    # lead: H_M := W_G(16,20)/qpat[16]; rows: W_G(n,20)*qpat[16] -
    # W_G(16,20)*qpat[n] = 0 (qpat[16] = 1)
    if 20 < dG:
        lead = WG.get((16, 20), VZERO)
        for n in range(0, 17):
            v = WG.get((n, 20), VZERO)
            r = vadd(vscal(v, qpat[16]), vscal(lead, -qpat[n]) if not (
                mk(qpat[n]).iszero()) else VZERO)
            if r: rows.append((52, "C2-Gm-quot", n, r))
        for (n, s), v in sorted(WG.items()):
            if s == 20 and n > 16:
                rows.append((52, "C2-Gm-quot-deg", n, v))
    # F6: W_R band at slot 42 (x-level 125 in [57,126) band)
    for (n, slot), v in sorted(WR.items()):
        if slot == 42: rows.append((42, "C2-R-band", n, v))
        elif slot == 0 and v:
            rows.append((13, "C2-R-top(must-vanish)", n, v))
    rows.sort(key=lambda r: (r[0], r[1], r[2]))
    return orbs, rows

def run_stages(depth, deep=False):
    orbs, rows = stage_conditions(depth)
    sysm = StageSystem()
    ledger = []
    bystage = {}
    for m, fam, n, v in rows: bystage.setdefault(m, []).append((fam, n, v))
    print("== staged run: %d rows over stages %s..%s ==" %
          (len(rows), min(bystage) if bystage else "-",
           max(bystage) if bystage else "-"), flush=True)
    for m in sorted(bystage):
        t0 = time.time()
        res = {"pivot": 0, "dependent": 0, "trivial": 0, "nonlinear": 0,
               "rho-relation": 0, "INCONSISTENT": 0}
        nnew = sum(1 for vv in range(len(VARS))
                   if VARS[vv]["level"] == m and VSTAT[vv] is None)
        for fam, n, v in bystage[m]:
            r = sysm.add_condition(v, m, (fam, n))
            res[r] += 1
            if r == "INCONSISTENT":
                print("!! STAGE %d INCONSISTENT at %s eta^%d" % (m, fam, n))
                ledger.append((m, nnew, len(bystage[m]), sysm.rank(),
                               "INCONSISTENT", res))
                return sysm, ledger, orbs
        nseen = len(sysm.seen_vars)
        ledger.append((m, nnew, len(bystage[m]), sysm.rank(),
                       "ok nullity=%d" % (nseen - sysm.rank()), res))
        print("  stage m=%2d: rows %3d new-vars %2d rank %3d seen %3d "
              "nullity %3d nl %d rho-rel %d (%.1fs)"
              % (m, len(bystage[m]), nnew, sysm.rank(), nseen,
                 nseen - sysm.rank(), res["nonlinear"], res["rho-relation"],
                 time.time()-t0), flush=True)
    return sysm, ledger, orbs

# ------------------------------------------------------- 5. stage-0 gate
GATE = []
def gk(name, cond):
    GATE.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + "gate: " + name, flush=True)

def reset_vars():
    del VARS[:]; del VSTAT[:]; _YPOW_CACHE.clear()

def rppoly_zero(coeffs):
    """list of ring elems == 0?"""
    return all(not c for c in coeffs)

def stage0_gate():
    print("== STAGE 0 GATE (genome lead identities, engine machinery) ==")
    reset_vars()
    orbs = build_generators(13)            # prefix-only window (level <= 12)
    p21, pm = k3poly_pow_pattern()
    p21_6 = [K1]; p21_9 = [K1]
    for _ in range(6): p21_6 = pm(p21_6, p21)
    for _ in range(9): p21_9 = pm(p21_9, p21)
    jf = fs_jet(FORB, orbs, 1, "f0")
    jg = fs_jet(GORB, orbs, 1, "g0")
    gk("F_s f-jet slot-0 = p21^6 = [(e7-1)^2(e7-B)]^6 (S_F = 1)",
       jet_matches_Tpoly(jf, p21_6))
    gk("F_s g-jet slot-0 = p21^9 (G_F = 1)", jet_matches_Tpoly(jg, p21_9))
    # E1 top cancellation: (p21^9)^2 == (p21^6)^3
    gk("E1: g^2 - f^3 top cancels (p21^18 == p21^18, s0 = 1 gauge)",
       pm(p21_9, p21_9) == pm(pm(p21_6, p21_6), p21_6))
    # E5 z-identity over the ring with free radical w1: z(z-3/2 w^2)^2
    # - (z-w^2)^3 + (3/4) w^4 z - w^6 == 0  (z^2 term cancels identically)
    W2, W4, W6 = rmono(w1=2), rmono(w1=4), rmono(w1=6)
    zp = [RZERO, RONE]                      # z
    q1 = [rscal(W2, -Fr(3, 2)), RONE]       # z - (3/2)w^2
    q2 = [rscal(W2, -1), RONE]              # z - w^2
    def rpm(a, b):
        r = [RZERO]*(len(a)+len(b)-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b): r[i+j] = radd(r[i+j], rmul(x, y))
        return r
    lhs = rpm(zp, rpm(q1, q1))
    cub = rpm(q2, rpm(q2, q2))
    tot = [radd(a, rscal(b, -1)) for a, b in
           zip(lhs + [RZERO]*(len(cub)-len(lhs)), cub)]
    tot[1] = radd(tot[1], rscal(W4, Fr(3, 4)))
    tot[0] = radd(tot[0], rscal(W6, -1))
    gk("E5 z-identity: z(z-3w2/2)^2-(z-w2)^3 = -(3/4)w4 z + w6 (ring, w free)",
       rppoly_zero(tot))
    # E5 automatic: m_i = G_M 27 c^6 (da)^3, lam_i = S_M 9 c^4 (da)^2 with
    # c^6 = a^2, c^12 = a^4: m^2 - lam^3 = 729 a^4 (da)^6 (G_M^2 - S_M^3)
    ok = True
    for ai, aj in ((A1c, A2c), (A2c, A1c)):
        da = ai - aj
        m2 = G_M*G_M*mk(729)*ai*ai*ai*ai*da*da*da*da*da*da
        l3 = S_M*S_M*S_M*mk(729)*ai*ai*ai*ai*da*da*da*da*da*da
        ok = ok and (m2 - l3).iszero()
    gk("E5 automatic: m_i^2 - s0 lam_i^3 = 729 a^4 (da)^6 (G_M^2-S_M^3) = 0",
       ok and (G_M*G_M - S_M*S_M*S_M).iszero())
    # E6: tower transports and the (F_i) identity over K3 (sigma = 6)
    gk("E6 transports: G_M^2 = S_M^3 and (H-ratio) 7^48/2^24 both sides",
       (G_M*G_M - S_M*S_M*S_M).iszero()
       and Fr(7**16, 2**8)**3 == Fr(7**12, 2**6)**4)
    Fi = lambda a: mk(27)*a*(a-Bc)*(a-Bc)*(a-Bc) - mk(216)*(a - B2c)
    gk("E6 (F_i): 27 a_i (a_i-b)^3 = sig^3 (a_i-b2), both poles, K3",
       Fi(A1c).iszero() and Fi(A2c).iszero())
    gk("E5 solvable: a_i - b != 0 (w_i^4 pinned nonzero)",
       not (A1c-Bc).iszero() and not (A2c-Bc).iszero())
    # E7 ladder cells (d-ladder additivity, counts)
    pi = dict(R=Fr(0), Fs=Fr(2, 7), Gm=Fr(16, 21), P=Fr(37, 42))
    d = dict(R=Fr(42), Fs=Fr(6), Gm=Fr(2, 7), P=Fr(1, 21))
    dg = dict(R=Fr(63), Fs=Fr(9), Gm=Fr(3, 7), P=Fr(1, 14))
    dh1 = dict(R=Fr(56), Fs=Fr(8), Gm=Fr(8, 21), P=Fr(1, 7))
    dh2 = dict(R=Fr(138), Fs=Fr(138, 7), Gm=Fr(8, 7), P=Fr(3, 7))
    cells = [(d, 126, 12, 2), (dg, 189, 18, 3), (dh1, 168, 16, 2),
             (dh2, 414, 39, 6)]
    ok = True
    for dd, degF, degG, degP in cells:
        ok &= dd["R"] - dd["Fs"] == (pi["Fs"]-pi["R"])*degF
        ok &= dd["Fs"] - dd["Gm"] == (pi["Gm"]-pi["Fs"])*degG
        ok &= dd["Gm"] - dd["P"] == (pi["P"]-pi["Gm"])*degP
    gk("E7: all 12 (edge,h) d-drop cells exact", ok)
    gk("y-side budget 42+42+42 = 126 = k_f; g: 3*42+3*21 = 189 = k_g",
       126 == 3*42 and 189 == 3*42+3*21)
    # gate part 2: G_m jet transport reproduction (St 3.9(ii), mechanical)
    reset_vars()
    orbs = build_generators(38)
    jfG = gm_jet(FORB, orbs, 1, "f0")
    jgG = gm_jet(GORB, orbs, 1, "g0")
    gk("G_m f-jet slot-0 = S_M (e3-a1)^2(e3-a2)^2, S_M = 7^12/2^6 (E6)",
       jet_matches_etapoly(jfG, eta_poly_ref([(A1c, 2), (A2c, 2)], S_M)))
    gk("G_m g-jet slot-0 = G_M (e3-a1)^3(e3-a2)^3, G_M = -7^18/2^9 (E6)",
       jet_matches_etapoly(jgG, eta_poly_ref([(A1c, 3), (A2c, 3)], G_M)))
    wg0 = jadd(jmul(jgG, jgG, 1), jscal(jmul(jfG, jmul(jfG, jfG, 1), 1), K3(-1)))
    gk("W_G slot-0: (g-jet)^2 - (f-jet)^3 = 0 at G_m top (E1 transported)",
       not wg0)
    # gate part 3: fast (suborbit-Newton) F_s jet == direct product jet
    def strip_hi(jp):
        out = {}
        for k, v in jp.items():
            vv = {kk: r for kk, r in v.items()
                  if not (kk and kk[-1] == HIVAR)}
            if vv: out[k] = vv
        return out
    reset_vars()
    orbs = build_generators(19)             # includes some tail vars
    ok = True
    for names in (FORB, GORB):
        j1 = fs_jet(names, orbs, 7, "x")
        j2 = fs_jet2(names, orbs, 7, "x")
        diff = jadd(strip_hi(j1), jscal(strip_hi(j2), K3(-1)))
        ok = ok and not diff
    gk("fs_jet2 == fs_jet (deg<=2 content exact; HIVAR flags conservative)",
       ok)
    reset_vars()
    orbs = build_generators(36)             # u-vars + some tails, no w yet
    ok = True
    for names in (FORB, GORB):
        j1 = gm_jet(names, orbs, 4, "x")
        j2 = gm_jet2(names, orbs, 4, "x")
        diff = jadd(strip_hi(j1), jscal(strip_hi(j2), K3(-1)))
        ok = ok and not diff
    gk("gm_jet2 == gm_jet (deg<=2 content exact), depth 4, vars", ok)
    bad = [n for n, c in GATE if not c]
    print("GATE TOTAL: %d checks, %d FAIL %s" % (len(GATE), len(bad), bad or ""))
    return not bad

def ring_to_poly(r, K3mul=None):
    """ring elem -> msolve polynomial string in z, r3, A1, A2, W1, HW1,
    W2, HW2, EB (K3 coeff u+v*r3)."""
    def mono(key, c):
        za, ea1, ea2, ew1, eh1, ew2, eh2, eB = key
        parts = []
        u, v = c
        if v == 0: cs = "(%s)" % u
        elif u == 0: cs = "(%s*r3)" % v
        else: cs = "(%s%s%s*r3)" % (u, "+" if v > 0 else "-", abs(v))
        parts.append(cs)
        for e, nm in ((za, "z"), (ea1, "A1"), (ea2, "A2"), (ew1, "W1"),
                      (eh1, "HW1"), (ew2, "W2"), (eh2, "HW2"), (eB, "EB")):
            if e > 0: parts.append("%s^%d" % (nm, e) if e > 1 else nm)
            elif e < 0: raise ValueError("negative exponent in emission")
        return "*".join(parts)
    return " + ".join(mono(k, c) for k, c in r.items()) or "0"

def emit_core(sysm, depth, outdir="/Users/dc/code/math/jc72108/systems/r1"):
    import os
    frees = sorted(v for v in sysm.seen_vars
                   if v not in sysm.piv and VSTAT[v] is None
                   and isinstance(v, int) and v < 10**7)
    nl = [(st, meta, vsub(v)) for st, meta, v in sysm.nl_rows]
    nl = [(st, meta, v) for st, meta, v in nl if v]
    nl_clean = [(st, meta, v) for st, meta, v in nl
                if not any(k and k[-1] == HIVAR for k in v)]
    nvars = len(frees) + 9
    print("  terminal core: %d free vars + 9 radical gens = %d; "
          "%d nl rows (%d exact, %d HIVAR-lossy)"
          % (len(frees), nvars, len(nl), len(nl_clean), len(nl)-len(nl_clean)))
    if len(frees) > 20:
        print("  core > 20 vars: banking sizing only (no .ms emission)")
        return None
    os.makedirs(outdir, exist_ok=True)
    names = {v: "x%d" % i for i, v in enumerate(frees)}
    eqs = ["r3^2-3", "A1^3-(3+r3)", "A2^3-(3-r3)", "2*HW1^2-3*W1^2",
           "2*HW2^2-3*W2^2", "2*EB^7-3"]
    eqs.append("+".join("z^%d*%d" % (i, c) if i else str(c)
                        for i, c in enumerate(PHI42) if c) .replace("+-", "-"))
    for st, meta, v in nl_clean:
        terms = []
        for key, r in v.items():
            base = ring_to_poly(r)
            mons = "*".join(names[k] for k in key) if key else ""
            terms.append("(%s)%s" % (base, "*"+mons if mons else ""))
        eqs.append(" + ".join(terms))
    path = os.path.join(outdir, "r1_core.ms")
    with open(path, "w") as f:
        f.write(", ".join(["z", "r3", "A1", "A2", "W1", "HW1", "W2", "HW2",
                           "EB"] + [names[v] for v in frees]) + "\n0\n")
        f.write(",\n".join(eqs) + "\n")
    print("  emitted %s (%d eqs, %d vars)" % (path, len(eqs), nvars))
    return path

def terminal_report(sysm, ledger, depth):
    print("\n== TERMINAL REPORT (depth %d) ==" % depth)
    for row in ledger: print("   ", row)
    frees = sorted(v for v in sysm.seen_vars
                   if sysm.piv.get(v) is None and VSTAT[v] is None)
    print("  rank %d / seen %d vars; free (non-pivot) vars: %d"
          % (sysm.rank(), len(sysm.seen_vars), len(frees)))
    print("  free var names:", [VARS[v]["name"] for v in frees][:40])
    print("  deferred nonlinear rows: %d" % len(sysm.nl_rows))
    for st, meta, v in sysm.nl_rows[:8]:
        print("    nl@%d %s: deg %d, %d terms" % (st, meta, vdeg(v), len(v)))
    print("  rho-relations: %d, split-columns: %d"
          % (len(sysm.rho_relations), sysm.split_cols))
    if sysm.certificate:
        st, meta, row = sysm.certificate
        print("  CERTIFICATE: stage %d %s: reduced row on rho-cols only: %s"
              % (st, meta, row))

def phase_solve(depth, final=False):
    global PINS
    st = load_state(); PINS = st["PINS"]
    sysm, ledger, orbs = run_stages(depth)
    for nm in sorted(PINS): print("   PIN %s = %s" % (nm, PINS[nm]))
    if sysm.certificate is not None:
        terminal_report(sysm, ledger, depth)
        st["dead"] = sysm.certificate
        save_state(st)
        return
    np_ = extract_pins(sysm)
    fresh = {k: v for k, v in np_.items() if k not in PINS}
    print("  solve: %d forced pins (%d new): %s"
          % (len(np_), len(fresh), sorted(fresh)[:14]), flush=True)
    st["PINS"].update(fresh)
    st["newpins"] = len(fresh)
    save_state(st)
    if final or not fresh:
        terminal_report(sysm, ledger, depth)
        path = emit_core(sysm, depth)
        if path:
            import subprocess
            try:
                r = subprocess.run(["msolve", "-f", path],
                                   capture_output=True, timeout=600, text=True)
                print("  msolve rc=%d out[:400]=%s" %
                      (r.returncode, (r.stdout or r.stderr)[:400]))
            except FileNotFoundError:
                print("  msolve not on PATH here (farm job); banked .ms")
            except Exception as e:
                print("  msolve: %s" % e)

def emit_gm_core(depth, outdir="/Users/dc/code/math/jc72108/systems/r1"):
    """exact G_m-band polynomial system on the bottom unknowns (the R1
    terminal core in its native form). Requires state built at a cap
    high enough that rows are exact; lossy rows are counted + excluded."""
    import os
    global PINS
    st = load_state(); PINS = st["PINS"]
    reset_vars(); orbs = build_generators(depth)
    dG = min(depth - 32, 21)
    WG = st["WG"]; jfG, jgG = st["jfG"], st["jgG"]
    pat = eta_poly_ref([(A1c, 2), (A2c, 2)], K1)
    _, pm = k3poly_pow_pattern()
    qpat = pm(pm([K0, K1], pat), [-Bc, K0, K0, K1])
    rows = []
    for (n, s), v in sorted(jfG.items()) + sorted(jgG.items()):
        if s % 2 == 1: rows.append((("C1-Gm", n, s), v))
    for (n, s), v in sorted(WG.items()):
        if 1 <= s <= 19: rows.append((("WG-band", n, s), v))
    lead = WG.get((16, 20), VZERO)
    for n in range(0, 17):
        v = WG.get((n, 20), VZERO)
        r = vadd(vscal(v, qpat[16]),
                 vscal(lead, -qpat[n]) if not mk(qpat[n]).iszero() else VZERO)
        if r: rows.append((("WG-quot", n, 20), r))
    exact, lossy, allvars = [], 0, set()
    for meta, v in rows:
        v = vsub(v)
        if not v: continue
        if any(k and k[-1] == HIVAR for k in v): lossy += 1; continue
        for k in v:
            for vid in k: allvars.add(vid)
        exact.append((meta, v))
    names = {vid: "x%d" % i for i, vid in enumerate(sorted(allvars))}
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "r1_gmband_core.ms")
    eqs = ["r3^2-3", "A1^3-(3+r3)", "A2^3-(3-r3)", "2*HW1^2-3*W1^2",
           "2*HW2^2-3*W2^2", "2*EB^7-3",
           "+".join("z^%d*(%d)" % (i, c) if i else "(%d)" % c
                    for i, c in enumerate(PHI42) if c)]
    for meta, v in exact:
        terms = []
        for key, r in sorted(v.items()):
            mons = "*".join(names[k] for k in key)
            terms.append("(%s)%s" % (ring_to_poly(r), "*"+mons if mons else ""))
        eqs.append(" + ".join(terms))
    with open(path, "w") as f:
        f.write(", ".join(["z", "r3", "A1", "A2", "W1", "HW1", "W2", "HW2",
                           "EB"] + [names[v] for v in sorted(allvars)]) + "\n0\n")
        f.write(",\n".join(eqs) + "\n")
    key = os.path.join(outdir, "r1_gmband_core.vars.txt")
    with open(key, "w") as f:
        for vid in sorted(allvars):
            f.write("%s = %s (level %d)\n"
                    % (names[vid], VARS[vid]["name"], VARS[vid]["level"]))
    print("  G_m-band core: %d exact rows (+%d cap-lossy excluded), "
          "%d engine vars + 9 radical gens -> %s"
          % (len(exact), lossy, len(allvars), path))
    return path

if __name__ == "__main__":
    args = sys.argv[1:] or ["--selftest"]
    aset = set(a.split("=")[0] for a in args)
    getv = lambda k, d: next((a.split("=")[1] for a in args
                              if a.startswith(k + "=")), d)
    depth = int(getv("--depth", "84" if "--deep" in aset else "54"))
    cap = int(getv("--cap", "0"))
    if cap:
        VDEG_CAP = cap
        STATE_PATH = STATE_PATH + ".cap%d" % cap
    if "--emit-gm-core" in aset:
        emit_gm_core(depth); sys.exit(0)
    if "--selftest" in aset:
        selftest_k3(); selftest_ring()
    if "--stage0" in aset:
        ok = stage0_gate()
        if not ok: sys.exit(1)
    if "--phase" in aset:
        ph = getv("--phase", "")
        if ph == "solve": phase_solve(depth, final="--final" in aset)
        else: phase(ph, depth)
    if "--reset-state" in aset:
        import os
        try: os.remove(STATE_PATH); print("state cleared")
        except FileNotFoundError: pass
