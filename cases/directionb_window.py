#!/usr/bin/env python3
"""SHEET6-DIRECTIONB §6: analysis phase of the 83-var forced-nonzero-
tail J-window build (the honest residue-A survivor locus).

State: /tmp/directionb_tails.pkl (or the banked copy
/tmp/directionb_tails_D21.pkl), produced by
    python3 directionb_strike.py tails        (~50 min, exact)
Rows byk[k][n] = VExpr: dict varkey -> ring elt; ring elt = dict
radkey -> K3, radkey = (z, a1, a2, w1, h1, w2, h2, B) exponents in the
reduced radical ring (z^Phi42, a_i^3 -> 3 +- r3, h_i^2 -> (3/2) w_i^2,
B^7 -> 3/2; w_1, w_2 free).  All tail rows have z = B = 0.

Phases (run: python3 directionb_window.py
                     [gate|bands|slot20|verdict|all]):

  gate    tails -> 0 must reproduce the promoted zero-tail system:
          rows 6..19 die; Row_20 == /tmp/directionb_dsys.pkl constants
          coefficient-for-coefficient (the 9-on-2 block: X1 = X2 = 0
          forced, eta^0 reads 0 = -42); + the E5/E6 anchor gate of
          directionb_strike (4/4).

  bands   rows 6..19 ledger, two tiers per band:
          S (pre-registered "Row_6-type"): radical-monomial split,
            K3-rank per band (solve6 semantics).
          V (value tier, the verdict tier): rank over the etale
            K3-algebra E = K3[a1,a2,mu]/(a1^3-(3+r3), a2^3-(3-r3),
            mu^2-3/2), one computation per h-sign branch (s1,s2),
            h_i valued s_i mu w_i, w_1, w_2 free NONZERO coordinates
            (columns are w-homogeneous, so w-monomials rescale away).
            Pivots are required to be UNITS of E (nonzero in every
            field factor <=> norm != 0), so a full-rank verdict holds
            on EVERY branch of the radical tower.  Bands force pins
            (tails = 0) consumed by later bands.

  slot20  Row_20 after the band pins: the inhomogeneous window.  The
          zero-tail contradiction 0 = -42 becomes a CONDITION on the
          surviving tails; derived exactly, per eta-component, over E.

Verdict semantics (pre-registered, §6): EMPTY forced-tail variety =
residue-A dies entirely; NONEMPTY = the surviving locus, characterized.
"""
import sys, os, time, pickle
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r1_experiment as R1
from r1_experiment import K3, mk, K0, K1, SQ3, row_reduce

OK = []
def chk(name, cond):
    OK.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, flush=True)

STATE = ("/tmp/directionb_tails_D21.pkl"
         if os.path.exists("/tmp/directionb_tails_D21.pkl")
         else "/tmp/directionb_tails.pkl")

def load():
    st = pickle.load(open(STATE, "rb"))
    assert st["D"] >= 21
    return st["byk"], st["vars"], st["D"]

def vname(vars_, key):
    return "*".join(vars_[i] for i in key) if key else "1"

TAILP = ("tf", "tg")
def istail(nm): return nm[:2] in TAILP

# ---------------------------------------------------------------- etale E
# E-basis key: (i1, i2, e) = a1^i1 a2^i2 mu^e, i in 0..2, e in 0..1.
A1c, A2c, MU2 = K3(3, 1), K3(3, -1), K3(Fr(3, 2))
def emul(x, y):
    out = {}
    for (i1, i2, e), cx in x.items():
        for (j1, j2, f), cy in y.items():
            c = cx * cy
            k1, r1 = divmod(i1 + j1, 3)
            k2, r2 = divmod(i2 + j2, 3)
            k3_, r3_ = divmod(e + f, 2)
            for _ in range(k1): c = c * A1c
            for _ in range(k2): c = c * A2c
            for _ in range(k3_): c = c * MU2
            k = (r1, r2, r3_)
            v = out.get(k)
            out[k] = c if v is None else v + c
            if out[k].iszero(): del out[k]
    return out
def eadd(x, y):
    out = dict(x)
    for k, c in y.items():
        v = out.get(k); out[k] = c if v is None else v + c
        if out[k].iszero(): del out[k]
    return out
def escal(x, c):
    return {} if c.iszero() else {k: v * c for k, v in x.items()}
def eneg(x): return {k: -v for k, v in x.items()}
EBASIS = [(i1, i2, e) for i1 in range(3) for i2 in range(3)
          for e in range(2)]
EONE = {(0, 0, 0): K1}

def enorm_nonzero(x):
    """x a unit of E?  E is etale (separable tower) = product of
    fields, so unit <=> norm != 0 <=> the 18x18 K3-multiplication
    matrix is nonsingular."""
    if not x: return False
    idx = {b: i for i, b in enumerate(EBASIS)}
    M = []
    for b in EBASIS:
        col = emul(x, {b: K1})
        M.append([col.get(bb, K0) for bb in EBASIS])
    # column vectors; rank via elimination over K3
    n = len(EBASIS)
    A = [[M[j][i] for j in range(n)] for i in range(n)]
    r = 0
    for c in range(n):
        p = next((i for i in range(r, n) if not A[i][c].iszero()), None)
        if p is None: return False
        A[r], A[p] = A[p], A[r]
        inv = A[r][c].inv()
        A[r] = [v * inv for v in A[r]]
        for i in range(n):
            if i != r and not A[i][c].iszero():
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
    return r == n

def rad_to_E(radkey, s1, s2):
    """radkey -> (E-elt, (P, Q) w-bidegree) on h-sign branch (s1,s2)."""
    z, e1, e2, p, h1, q, h2, B = radkey
    assert z == 0 and B == 0, "unexpected z/B in tail rows"
    assert h1 in (0, 1) and h2 in (0, 1)
    c = K1
    if h1 and s1 < 0: c = -c
    if h2 and s2 < 0: c = -c
    e, r = divmod(h1 + h2, 2)
    if e: c = c * MU2
    return {(e1, e2, r): c}, (p + h1, q + h2)

def erank_units(rows, ncols, tag=""):
    """Gaussian elimination over E with UNIT pivots only (invertible
    row transformations, so the echelon rows GENERATE the same
    E-module of equations).  rows = list of dict col -> E-elt.
    Returns (rank, pivcols, echelon, leftover); leftover = rows not
    reducible with unit pivots (=> undecided at this tier; report)."""
    rows = [dict(r) for r in rows]
    piv = []
    used = set()
    for c in range(ncols):
        pr = None
        for i, r in enumerate(rows):
            if i in used or c not in r: continue
            if enorm_nonzero(r[c]): pr = i; break
        if pr is None: continue
        used.add(pr); piv.append(c)
        inv = einv(rows[pr][c])
        rows[pr] = {k: emul(inv, v) for k, v in rows[pr].items()}
        for i, r in enumerate(rows):
            if i != pr and c in r:
                f = r[c]
                for k, v in rows[pr].items():
                    r[k] = eadd(r.get(k, {}), emul(eneg(f), v))
                    if not r[k]: del r[k]
    echelon = [rows[i] for i in sorted(used)]
    leftover = [r for i, r in enumerate(rows) if i not in used and r]
    return len(piv), piv, echelon, leftover

def einv(x):
    """invert a unit of E by solving the 18x18 K3-linear system."""
    n = len(EBASIS)
    idx = {b: i for i, b in enumerate(EBASIS)}
    A = [[K0] * n for _ in range(n)]
    for j, b in enumerate(EBASIS):
        col = emul(x, {b: K1})
        for bb, c in col.items(): A[idx[bb]][j] = c
    rhs = [K1 if b == (0, 0, 0) else K0 for b in EBASIS]
    # solve A y = rhs
    for c in range(n):
        p = next(i for i in range(c, n) if not A[i][c].iszero())
        A[c], A[p] = A[p], A[c]; rhs[c], rhs[p] = rhs[p], rhs[c]
        inv = A[c][c].inv()
        A[c] = [v * inv for v in A[c]]; rhs[c] = rhs[c] * inv
        for i in range(n):
            if i != c and not A[i][c].iszero():
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[c])]
                rhs[i] = rhs[i] - f * rhs[c]
    return {b: rhs[i] for i, b in enumerate(EBASIS)
            if not rhs[i].iszero()}

# ------------------------------------------------------------------ gate
def gate():
    print("== GATE: tails -> 0 reproduces the promoted zero-tail kill ==")
    byk, vars_, D = load()
    # (a) rows 6..19: every monomial carries a tail var
    for k in sorted(byk):
        if k == 20: continue
        bad = [vk for n, v in byk[k].items() for vk in v
               if not vk or not any(istail(vars_[i]) for i in vk)]
        chk("Row_%d dies at tails=0 (every term tail-loaded)" % k,
            not bad)
    # (b) Row_20 const part == banked zero-tail constants (dsys pkl)
    ds = pickle.load(open("/tmp/directionb_dsys.pkl", "rb"))
    r20d, r20t = ds["byk"][20], byk[20]
    chk("Row_20: zero-tail (const-part) eta-support == banked system "
        "(extra comps, e.g. eta^27, must be pure-tail)",
        sorted(r20d) == sorted(n for n, v in r20t.items()
                               if v.get(()) ))
    same = True
    for n in sorted(r20d):
        constt = r20t[n].get((), {})
        # tails->0 also kills var-terms; const parts must agree
        same &= (constt == r20d[n].get((), {}))
        badv = [vk for vk in r20t[n] if vk and
                not any(istail(vars_[i]) for i in vk)]
        same &= not badv
    chk("Row_20 const == banked zero-tail Row_20, coefficient-for-"
        "coefficient (9 eta-comps)", same)
    # (c) re-derive the kill from the tails state itself
    K1M = (0, 1, 0, 4, 0, 0, 0, 0); K2M = (0, 0, 1, 0, 0, 4, 0, 0)
    sysr = {}
    for n in sorted(r20d):
        c = r20d[n].get((), {})
        sysr[n] = (c.get(K1M, K0), c.get(K2M, K0))
    kconj = lambda c: K3(c[0], -c[1])
    chk("tau-covariance c2 = conj(c1), all 9 rows",
        all(c2 == kconj(c1) for c1, c2 in sysr.values()))
    dets = set()
    ns = [n for n in sorted(sysr) if n]
    for i in range(len(ns)):
        for j in range(i + 1, len(ns)):
            a, b = sysr[ns[i]], sysr[ns[j]]
            dets.add(not (a[0] * b[1] - b[0] * a[1]).iszero())
    chk("zero-tail 9-on-2: some homogeneous pair independent => "
        "X1 = X2 = 0 forced", True in dets)
    chk("zero-tail eta^0 then reads 0 = -42/(c_f c_g): INCONSISTENT "
        "(c1, c2 both nonzero)",
        not sysr[0][0].iszero() and not sysr[0][1].iszero())
    # (c2) RHS42 certification [REVIEW 2026-08-13, Grok F3]: the
    # constant every analysis phase consumes (RHS42, used by relax /
    # evaluate / build_affine / tail_linearize / slot20) must equal
    # MINUS the chart-Jacobian constant: x = t^-42, y = P + eta t^32
    # gives x_t y_eta - x_eta y_t = (-42) t^{-43} * t^{32} - 0
    # = -42 t^{-11}, so (J) reads LHS = -(42/(c_f c_g)) t^20 and the
    # analysis equation is LHS + 42 = 0 at the c_f c_g = 1 gauge.
    # Also: NEITHER banked pickle may carry a scalar (empty-radkey)
    # constant at Row_20 eta^0 -- the -42 lives ONLY on the RHS, so
    # it enters exactly once (no double count, no smuggled constant).
    EXX, EYE = -42, 32                  # x = t^EXX, y ~ eta t^EYE
    JCH = EXX                           # coefficient of t^(EXX-1+EYE)
    Z8 = (0,) * 8
    noscal = all(Z8 not in comp[0].get((), {})
                 for comp in (r20d, r20t))
    chk("RHS42 == -(chart-Jacobian constant) == 42 (x_t y_eta = "
        "-42 t^-11, slot %d) and NO scalar const in banked Row_20 "
        "eta^0 (both pickles): the -42 enters exactly once"
        % (EXX - 1 + EYE),
        RHS42 == K3(-JCH) and (EXX - 1 + EYE) == -11 and noscal)
    # (d) E5/E6 anchors (strike gate, rebuilds depth-1 jets)
    import directionb_strike as DS
    DS.OK.clear(); DS.gate()
    for name, c in DS.OK: chk("[strike] " + name, c)

# ------------------------------------------------------------- bands
def eshow(x, maxt=6):
    """print an E-elt: sum of (a+b r3) a1^i a2^j mu^e."""
    def bs(b):
        i1, i2, e = b
        s = ("a1^%d" % i1 if i1 > 1 else "a1" if i1 else "") \
            + ("a2^%d" % i2 if i2 > 1 else "a2" if i2 else "") \
            + ("mu" if e else "")
        return s or "1"
    its = sorted(x.items())
    s = " + ".join("%r%s" % (c, "" if bs(b) == "1" else "*" + bs(b))
                   for b, c in its[:maxt])
    return s + (" +..(%d)" % len(its) if len(its) > maxt else "")

def band_erows(byk, vars_, k, s1, s2):
    """Band k as E-rows over columns (varmono-name, P, Q) on h-sign
    branch (s1, s2); w-monomial w1^P w2^Q kept explicit per column.
    Also returns the eta-index of each row and the column order."""
    cols, rows, etas = {}, [], []
    for n, v in sorted(byk.get(k, {}).items()):
        row = {}
        for vk, r in v.items():
            nm = vname(vars_, vk)
            for rk, c in r.items():
                ee, pq = rad_to_E(rk, s1, s2)
                ck = (nm, pq)
                col = cols.setdefault(ck, len(cols))
                row[col] = eadd(row.get(col, {}), escal(ee, c))
                if not row[col]: del row[col]
        if row: rows.append(row); etas.append(n)
    return cols, rows, etas

def band_tierS(byk, vars_, k):
    """pre-registered split tier: radical monomials = free module
    basis; K3-rank over ALL var-monomial columns."""
    cols, srows = {}, []
    for n, v in sorted(byk.get(k, {}).items()):
        radkeys = set()
        for vk, r in v.items(): radkeys |= set(r)
        for rk in sorted(radkeys):
            row = {}
            for vk, r in v.items():
                c = r.get(rk)
                if c and not c.iszero():
                    col = cols.setdefault(vname(vars_, vk), len(cols))
                    row[col] = c
            if row: srows.append(row)
    rank, piv, red, bad = row_reduce(
        [dict(r) for r in srows], len(cols) + 1, "S%d" % k, quiet=True)
    return len(srows), len(cols), rank, piv, cols

def bands():
    """Rows 6..19 band ledger.  No zero-pins exist (Row_6 already has
    E-rank 1 < 6): each band is banked as its exact E-echelon
    condition set instead."""
    print("== BANDS: rows 6..19 -> exact E-module conditions ==")
    byk, vars_, D = load()
    bank = {}
    for k in range(6, 20):
        if k not in byk:
            print("-- Row_%d: identically 0" % k); continue
        nsr, nsc, srank, spiv, scols = band_tierS(byk, vars_, k)
        print("-- Row_%d: %d eta-comps" % (k, len(byk[k])))
        print("   tier S (split, pre-reg): %d K3-rows x %d monomial "
              "cols, rank %d" % (nsr, nsc, srank))
        for s1, s2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            cols, rows, etas = band_erows(byk, vars_, k, s1, s2)
            rank, piv, ech, left = erank_units(rows, len(cols))
            inv = {i: ck for ck, i in cols.items()}
            bank[(k, s1, s2)] = {"cols": inv, "echelon": ech,
                                 "rank": rank, "piv": piv,
                                 "leftover": left, "etas": etas}
            print("   tier V (%+d,%+d): %d E-rows x %d (varmono, "
                  "w-mono) cols -> rank %d%s" %
                  (s1, s2, len(rows), len(cols), rank,
                   "; %d UNREDUCED leftover" % len(left) if left
                   else ""))
        # print branch (+1,+1) conditions, linear part in full
        st = bank[(k, 1, 1)]
        for i, er in enumerate(st["echelon"]):
            terms = sorted(er.items(), key=lambda kv: (
                len(st["cols"][kv[0]][0].split("*")), st["cols"][kv[0]]))
            linp = [(st["cols"][c], x) for c, x in terms
                    if "*" not in st["cols"][c][0]]
            nlp = [(st["cols"][c], x) for c, x in terms
                   if "*" in st["cols"][c][0]]
            def tshow(ck, x):
                nm, (P, Q) = ck
                wm = ("w1^%d" % P if P else "") + ("w2^%d" % Q if Q else "")
                return "[%s]%s%s" % (eshow(x, 3), wm and "*" + wm, "*" + nm)
            print("   C%d.%d: %s%s = 0"
                  % (k, i + 1,
                     " + ".join(tshow(ck, x) for ck, x in linp),
                     "  +  (%d nonlinear terms)" % len(nlp)
                     if nlp else ""))
    with open("/tmp/directionb_window_conditions.pkl", "wb") as fh:
        pickle.dump(bank, fh)
    print("   banked: /tmp/directionb_window_conditions.pkl")
    return bank


# ------------------------------------------------------------- slot 20
K1M = (0, 1, 0, 4, 0, 0, 0, 0)          # alpha1 w1^4
K2M = (0, 0, 1, 0, 0, 4, 0, 0)          # alpha2 w2^4
RHS42 = K3(42)     # J: Row_20[eta^0] = -(42/(c_f c_g)); gauge c_f c_g = 1

def ring_to_E(r, s1, s2, w1, w2):
    """ring elt -> E, at h-signs (s1,s2) and pole scales w_i = given
    NONZERO rationals.  X_i = alpha_i w_i^4 is NOT free here: it is
    whatever the scales make it (this is what the zero-tail w4 solve
    could not have, and is why the -42 must be cancelled by tails)."""
    out = {}
    for rk, c in r.items():
        ee, (P, Q) = rad_to_E(rk, s1, s2)
        for _ in range(P): c = c * w1
        for _ in range(Q): c = c * w2
        out = eadd(out, escal(ee, c))
    return out

def esolve(rows, rhs, ncols):
    """inhomogeneous E-linear solve, UNIT pivots only.
    rows[i]: dict col -> E; rhs[i]: E.  Returns
    (rank, piv, sol, freecols, incons, undec):
      sol = particular solution (free cols = 0),
      incons = True if some reduced row is 0 = unit  (NO solution on
               ANY factor of E),
      undec  = rows left with zero-divisor-only coefficients."""
    rows = [dict(r) for r in rows]; rhs = list(rhs)
    piv, used = [], {}
    for c in range(ncols):
        pr = None
        for i, r in enumerate(rows):
            if i in used.values() or c not in r: continue
            if enorm_nonzero(r[c]): pr = i; break
        if pr is None: continue
        used[c] = pr; piv.append(c)
        iv = einv(rows[pr][c])
        rows[pr] = {k: emul(iv, v) for k, v in rows[pr].items()}
        rhs[pr] = emul(iv, rhs[pr])
        for i, r in enumerate(rows):
            if i != pr and c in r:
                f = eneg(r[c])
                for k, v in rows[pr].items():
                    r[k] = eadd(r.get(k, {}), emul(f, v))
                    if not r[k]: del r[k]
                rhs[i] = eadd(rhs[i], emul(f, rhs[pr]))
    sol = {c: rhs[used[c]] for c in piv}       # free cols = 0
    incons, undec = False, 0
    for i, r in enumerate(rows):
        if i in used.values(): continue
        if not r:
            if rhs[i]:
                if enorm_nonzero(rhs[i]): incons = True
                else: undec += 1
        else: undec += 1
    free = [c for c in range(ncols) if c not in piv]
    return len(piv), piv, sol, free, incons, undec

def restrict(byk, vars_, k, keep):
    """rows of band k with every var outside `keep` set to 0.
    Returns comps[n] = dict varkey -> ring (surviving terms only)."""
    out = {}
    for n, v in sorted(byk.get(k, {}).items()):
        w = {vk: r for vk, r in v.items()
             if all(vars_[i] in keep for i in vk) and r}
        if w: out[n] = w
    return out

def evaluate(byk, vars_, val, s1, s2, w1, w2):
    """EXACT certificate evaluator: substitute tail values `val`
    (name -> E elt; absent = 0) into EVERY banked row and return
    {k: {n: E-value}} of the J-identity defect
    (Row_k[eta^n], plus +42 at (20, 0))."""
    res = {}
    for k in sorted(byk):
        for n, v in byk[k].items():
            acc = {}
            for vk, r in v.items():
                m = EONE
                for i in vk:
                    m = emul(m, val.get(vars_[i], {}))
                    if not m: break
                if not m: continue
                acc = eadd(acc, emul(m, ring_to_E(r, s1, s2, w1, w2)))
            if k == 20 and n == 0:
                acc = eadd(acc, {(0, 0, 0): RHS42})
            if acc: res.setdefault(k, {})[n] = acc
    return res

WSAMPLES = ((K1, K1), (K3(2), K3(3)), (K3(Fr(1, 5)), K3(7)))

# ------------------------------------------------------- the cascade
# Bands introduce new tail levels LINEARLY, in this order; every band
# is affine in its own new levels once all lower levels are assigned
# (asserted at run time).  The 7 dead-stretch coefficients are FREE
# (no band constrains them) and enter Row_20 only via cross-terms --
# which is exactly the freedom the zero-tail theorem could not see.
SEVEN = ("uf18", "uf24", "uf30", "vf1_34", "vf1_36", "vf2_34", "vf2_36")
STAGES = [(6, ["38"]), (8, ["40"]), (10, ["42"]), (12, ["39", "44"]),
          (14, ["41", "46"]), (16, ["43", "48"])]
JOINT = ([18, 20], ["45", "50", "47", "52"])

def lvl(nm): return nm.rsplit("_", 1)[-1]

def build_affine(byk, vars_, ks, unk, val, s1, s2, w1, w2):
    """rows of bands `ks`, affine in the unknown tails `unk` (list of
    names) once every other var is given a value in `val` (name -> E;
    absent = 0).  Returns (cols, rows, rhs, labels)."""
    cols = {nm: i for i, nm in enumerate(unk)}
    U = set(unk)
    rows, rhs, lab = [], [], []
    for k in ks:
        for n, v in sorted(byk.get(k, {}).items()):
            row, const = {}, {}
            for vk, r in v.items():
                nms = [vars_[i] for i in vk]
                u = [x for x in nms if x in U]
                assert len(u) <= 1, "band %d not affine in %s" % (k, u)
                co = EONE
                for x in nms:
                    if x in U: continue
                    co = emul(co, val.get(x, {}))
                    if not co: break
                if not co: continue
                ee = emul(co, ring_to_E(r, s1, s2, w1, w2))
                if not ee: continue
                if u:
                    j = cols[u[0]]
                    row[j] = eadd(row.get(j, {}), ee)
                    if not row[j]: del row[j]
                else: const = eadd(const, ee)
            if k == 20 and n == 0:
                const = eadd(const, {(0, 0, 0): RHS42})
            if row or const:
                rows.append(row); rhs.append(eneg(const)); lab.append((k, n))
    return cols, rows, rhs, lab

def asolve(rows, rhs, ncols, presets):
    """esolve with some columns preset to given values (folded into
    the RHS).  Returns (rank, sol, free, incons, undec) with sol over
    ALL ncols columns."""
    rows2, rhs2 = [], list(rhs)
    for i, r in enumerate(rows):
        rr = {}
        for c, x in r.items():
            if c in presets:
                rhs2[i] = eadd(rhs2[i], emul(eneg(x), presets[c]))
            else: rr[c] = x
        rows2.append(rr)
    rk, piv, sol, free, incons, undec = esolve(rows2, rhs2, ncols)
    out = dict(presets); out.update(sol)
    free = [c for c in free if c not in presets]
    return rk, out, free, incons, undec

def genval(i):
    """generic nonzero rational sample values for free directions."""
    return {(0, 0, 0): K3(Fr(1 + (i % 5), 2 + (i % 3)))}

def cascade(s1=1, s2=1, w1=K1, w2=K1, dsv=None, verbose=True):
    """Solve the whole window level-by-level, generic nonzero data,
    then the joint Row_18 + Row_20 endgame.  Returns (val, defect)."""
    byk, vars_, D = load()
    val = {}
    for j, nm in enumerate(SEVEN):
        val[nm] = genval(j + 1) if dsv is None else dsv
    for (k, levs) in STAGES:
        unk = [v for v in vars_ if v[:2] in ("tf", "tg") and lvl(v) in levs]
        cols, rows, rhs, lab = build_affine(byk, vars_, [k], unk, val,
                                            s1, s2, w1, w2)
        rk, piv, sol, free, incons, undec = esolve(rows, rhs, len(cols))
        pres = {c: genval(7 + c + k) for c in free}
        rk, sol, free, incons, undec = asolve(rows, rhs, len(cols), pres)
        if verbose:
            print("   band %-2d: %2d eqs, %2d new unknowns (levels %s) "
                  "-> rank %d, %d free%s"
                  % (k, len(rows), len(cols), "/".join(levs), rk,
                     len(free), ", INCONSISTENT" if incons else ""))
        if incons or undec: return None, "band %d inconsistent" % k
        inv = {i: nm for nm, i in cols.items()}
        for c, x in sol.items():
            if x: val[inv[c]] = x
    ks, levs = JOINT
    unk = [v for v in vars_ if v[:2] in ("tf", "tg") and lvl(v) in levs]
    cols, rows, rhs, lab = build_affine(byk, vars_, ks, unk, val,
                                        s1, s2, w1, w2)
    rk, piv, sol, free, incons, undec = esolve(rows, rhs, len(cols))
    if verbose:
        print("   ENDGAME (Row_18 + Row_20): %d eqs, %d unknowns "
              "(levels %s) -> rank %d, %d free%s"
              % (len(rows), len(cols), "/".join(levs), rk, len(free),
                 ", INCONSISTENT" if incons else ""))
    if incons or undec: return None, "endgame inconsistent"
    inv = {i: nm for nm, i in cols.items()}
    for c, x in sol.items():
        if x: val[inv[c]] = x
    return val, None


def slot20(verbose=True):
    """THE verdict phase.  Stratum S = the 16 tails entering Row_20
    LINEARLY (levels 42/47/52).  On S every band 6..19 except Row_10
    vanishes identically (checked); Row_10 is linear in the six
    level-42 tails; Row_20 = const w4-block + linear(S) + quadratic in
    the level-42 tails.  Solved exactly over E per h-sign branch and
    per pole-scale sample: MEASURED INCONSISTENT (rank 4/10, residual
    defect exactly Row_20 eta^{12,15,18,21,24,27}, uniform over all
    12 (w, branch) combos), certified by exact substitution of the
    particular solve into every banked row [REVIEW 2026-08-13]."""
    byk, vars_, D = load()
    S = sorted({vars_[vk[0]] for n, v in byk[20].items()
                for vk in v if len(vk) == 1})
    L42 = [nm for nm in S if nm.endswith("_42")]
    REST = [nm for nm in S if not nm.endswith("_42")]
    print("== SLOT-20: the inhomogeneous window (THE verdict) ==")
    print("   stratum S (%d linear slot-20 tails): %s" % (len(S), " ".join(S)))
    # structural facts, checked exactly
    dead = [k for k in sorted(byk) if k != 20 and not restrict(byk, vars_, k, set(S))]
    chk("bands 6..19 except Row_10 vanish identically on S (%s dead)"
        % ",".join(map(str, dead)),
        dead == [k for k in sorted(byk) if k not in (10, 20)])
    r10 = restrict(byk, vars_, 10, set(S))
    chk("Row_10|S is LINEAR in the six level-42 tails",
        all(len(vk) == 1 and vars_[vk[0]] in L42
            for v in r10.values() for vk in v))
    r20 = restrict(byk, vars_, 20, set(S))
    q20 = {vk for v in r20.values() for vk in v if len(vk) > 1}
    chk("Row_20|S = const + linear(S) + quadratic(level-42 only) "
        "(%d quadratic monomials)" % len(q20),
        all(all(vars_[i] in L42 for i in vk) for vk in q20))

    for (w1, w2) in WSAMPLES:
        for (s1, s2) in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            tag = "w=(%r,%r) h=(%+d,%+d)" % (w1, w2, s1, s2)
            # STAGE A: Row_10|S homogeneous, six level-42 unknowns
            colsA = {nm: i for i, nm in enumerate(L42)}
            rowsA = []
            for n, v in sorted(r10.items()):
                row = {}
                for vk, r in v.items():
                    c = colsA[vars_[vk[0]]]
                    row[c] = eadd(row.get(c, {}),
                                  ring_to_E(r, s1, s2, w1, w2))
                    if not row[c]: del row[c]
                if row: rowsA.append(row)
            rkA, pivA, echA, leftA = erank_units(rowsA, len(colsA))
            pinned = (rkA == len(colsA) and not leftA)
            if verbose:
                print("   [%s] Row_10|S: %d E-rows, rank %d/6%s"
                      % (tag, len(rowsA), rkA,
                         " => ALL level-42 tails = 0" if pinned
                         else " (%d free)" % (len(colsA) - rkA)))
            # STAGE B: level-42 = 0 (stage A) -> Row_20|S linear in REST
            keep = set(REST)
            colsB = {nm: i for i, nm in enumerate(REST)}
            rowsB, rhsB, etaB = [], [], []
            for n, v in sorted(r20.items()):
                row, const = {}, {}
                for vk, r in v.items():
                    if vk and not all(vars_[i] in keep for i in vk):
                        continue                       # level-42 -> 0
                    ee = ring_to_E(r, s1, s2, w1, w2)
                    if not vk: const = eadd(const, ee)
                    else:
                        c = colsB[vars_[vk[0]]]
                        row[c] = eadd(row.get(c, {}), ee)
                        if not row[c]: del row[c]
                if n == 0: const = eadd(const, {(0, 0, 0): RHS42})
                if row or const:
                    rowsB.append(row); rhsB.append(eneg(const)); etaB.append(n)
            rk, piv, sol, free, incons, undec = esolve(
                rowsB, rhsB, len(colsB))
            # [REVIEW 2026-08-13] the checks below assert the
            # MEASURED result (rank 4/10, INCONSISTENT, defect
            # exactly Row_20 eta^{12,15,18,21,24,27}); the earlier
            # text asserted the pre-result expectation (SOLVABLE +
            # vanishing certificate + an "explicit point" that did
            # not exist) and mis-reported 24 stale FAILs.
            chk("slot-20 %s: INCONSISTENT as measured (rank %d/%d on "
                "%d eta-rows; %d free; undecided rows=%d) -- the -42 "
                "is NOT cancellable by the slot-20-linear tails"
                % (tag, rk, len(colsB), len(rowsB), len(free), undec),
                incons and undec == 0 and rk == 4)
            # residual certificate: the particular solve (free = 0)
            # substituted into EVERY banked row leaves a defect
            # EXACTLY in the 6 obstruction components of Row_20
            inv = {i: nm for nm, i in colsB.items()}
            val = {inv[c]: x for c, x in sol.items()}
            defect = evaluate(byk, vars_, val, s1, s2, w1, w2)
            chk("slot-20 %s: EXACT residual certificate -- defect "
                "exactly Row_20 eta^{12,15,18,21,24,27}" % tag,
                set(defect) == {20} and
                sorted(defect[20]) == [12, 15, 18, 21, 24, 27])
    return None

def relax(byk, vars_, ks, s1, s2, w1, w2):
    """LINEARIZATION RELAXATION: every var-monomial an INDEPENDENT
    unknown.  This is an over-approximation of the true solution set,
    so INCONSISTENT here => the forced-tail variety is EMPTY."""
    cols, rows, rhs = {}, [], []
    for k in ks:
        for n, v in sorted(byk.get(k, {}).items()):
            row, const = {}, {}
            for vk, r in v.items():
                ee = ring_to_E(r, s1, s2, w1, w2)
                if not ee: continue
                if not vk: const = eadd(const, ee)
                else:
                    c = cols.setdefault(vk, len(cols))
                    row[c] = eadd(row.get(c, {}), ee)
                    if not row[c]: del row[c]
            if k == 20 and n == 0:
                const = eadd(const, {(0, 0, 0): RHS42})
            if row or const: rows.append(row); rhs.append(eneg(const))
    rk, piv, sol, free, incons, undec = esolve(rows, rhs, len(cols))
    return len(rows), len(cols), rk, incons, undec

def tail_linearize(byk, vars_, ds, s1, s2, w1, w2):
    """THE DIFFERENTIAL of the window map at the zero-tail point:
    keep only tail-degree <= 1 terms.  Consistent <=> the -42 can be
    cancelled to FIRST ORDER in the tails."""
    TAILS = [v for v in vars_ if v[:2] in ("tf", "tg")]
    T = set(TAILS); cols = {nm: i for i, nm in enumerate(TAILS)}
    rows, rhs = [], []
    for k in sorted(byk):
        for n, v in sorted(byk[k].items()):
            row, const = {}, {}
            for vk, r in v.items():
                nms = [vars_[i] for i in vk]
                t = [x for x in nms if x in T]
                if len(t) > 1: continue          # drop degree >= 2
                co = EONE
                for x in nms:
                    if x in T: continue
                    co = emul(co, ds.get(x, {}))
                    if not co: break
                if not co: continue
                ee = emul(co, ring_to_E(r, s1, s2, w1, w2))
                if not ee: continue
                if t:
                    j = cols[t[0]]
                    row[j] = eadd(row.get(j, {}), ee)
                    if not row[j]: del row[j]
                else: const = eadd(const, ee)
            if k == 20 and n == 0:
                const = eadd(const, {(0, 0, 0): RHS42})
            if row or const: rows.append(row); rhs.append(eneg(const))
    rk, piv, sol, free, incons, undec = esolve(rows, rhs, len(cols))
    return len(rows), len(cols), rk, incons, undec

def stratum(byk, vars_, unk, val, ks, s1, s2, w1, w2):
    cols, rows, rhs, lab = build_affine(byk, vars_, ks, unk, val,
                                        s1, s2, w1, w2)
    rk, piv, sol, free, incons, undec = esolve(rows, rhs, len(cols))
    return len(rows), len(cols), rk, incons, undec

VFIBERS = ((1, 1, "1", "1"), (1, -1, "1", "1"), (-1, 1, "1", "1"),
           (-1, -1, "1", "1"), (1, 1, "2", "3"))

def verdict():
    """THE VERDICT phase: the decisive tests, in increasing strength.
    [REVIEW 2026-08-13] tests (1)(2) now LOOP over all 4 h-sign
    branches at w = (1,1) plus branch (+,+) at w = (2,3), and the
    harness asserts identical dims/ranks/verdicts on every fiber
    (previously a single fiber ran and the 4-branch identity was a
    doc-only claim, verified in review); strata (3) run on the
    default fiber ((3a) is additionally 12-combo-certified by the
    slot20 phase)."""
    byk, vars_, D = load()
    print("== VERDICT: is the forced-tail variety EMPTY? ==")
    sig = []
    for (s1, s2, ws1, ws2) in VFIBERS:
        w1, w2 = K3(Fr(ws1)), K3(Fr(ws2))
        ftag = "h=(%+d,%+d) w=(%s,%s)" % (s1, s2, ws1, ws2)
        rec = []
        # (1) relaxations -- the only tier at which an EMPTY verdict
        #     could be certified by linear algebra alone
        nr, nc, rk, ic, ud = relax(byk, vars_, [20], s1, s2, w1, w2)
        chk("[%s] Row_20 relaxation CONSISTENT (%d rows, %d monomial "
            "cols, rank %d) => no single-row invariant kills the "
            "window" % (ftag, nr, nc, rk), not ic and not ud)
        rec.append((nr, nc, rk, ic, ud))
        nr, nc, rk, ic, ud = relax(byk, vars_, sorted(byk), s1, s2, w1, w2)
        chk("[%s] FULL-WINDOW relaxation CONSISTENT (%d rows, %d "
            "monomial cols, rank %d): the -42 target IS in the column "
            "span => NO E-linear functional of these 77 depth-21 rows "
            "kills the window on this fiber" % (ftag, nr, nc, rk),
            not ic and not ud)
        rec.append((nr, nc, rk, ic, ud))
        # (2) the differential at the zero-tail point (sampled in the
        #     7: the all-zero point + one generic rational sample --
        #     rank-stability, not a closed identity in the 7)
        for tag, ds in (("dead-stretch = 0", {}),
                        ("dead-stretch generic",
                         {n: genval(i + 1) for i, n in enumerate(SEVEN)})):
            nr, nc, rk, ic, ud = tail_linearize(byk, vars_, ds,
                                                s1, s2, w1, w2)
            chk("[%s] tail-linearization at the zero-tail point (%s) "
                "INCONSISTENT (%d rows, %d tail cols, rank %d): the "
                "-42 is NOT cancellable to first order"
                % (ftag, tag, nr, nc, rk), ic)
            rec.append((nr, nc, rk, ic, ud))
        sig.append(tuple(rec))
    chk("tests (1)(2): dims/ranks/verdicts IDENTICAL on all %d "
        "certified (h-branch, w) fibers: %s"
        % (len(VFIBERS), list(sig[0])), len(set(sig)) == 1)
    s1 = s2 = 1
    w1 = w2 = K1
    # (3) exact affine strata
    T = lambda pred: [v for v in vars_ if v[:2] in ("tf", "tg") and pred(v)]
    dsg = {n: genval(i + 1) for i, n in enumerate(SEVEN)}
    for tag, unk, val in (
        ("levels 47/52 only", T(lambda v: lvl(v) in ("47", "52")), dsg),
        ("levels 45/47/50/52", T(lambda v: lvl(v) in ("45", "47", "50", "52")), dsg),
        ("levels >= 43 (low tails = 0)", T(lambda v: int(lvl(v)) >= 43), dsg)):
        nr, nc, rk, ic, ud = stratum(byk, vars_, unk, val, sorted(byk),
                                     s1, s2, w1, w2)
        chk("stratum [%s] INCONSISTENT (%d eqs, %d unknowns, rank %d)"
            % (tag, nr, nc, rk), ic)
    print("   => every closed-form affine stratum dies; the survivor "
          "locus is genuinely NONLINEAR (needs simultaneously nonzero\n"
          "      low-level tails whose degree-2/3 cross-terms feed the "
          "eta^12..27 obstruction components).")

if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "all"
    t0 = time.time()
    if ph in ("gate", "all"): gate()
    if ph in ("bands", "all"): bands()
    if ph in ("slot20", "all"): slot20()
    if ph in ("verdict", "all"): verdict()
    bad = [n for n, c in OK if not c]
    print("\nTOTAL: %d checks, %d FAIL %s  (%.1fs)"
          % (len(OK), len(bad), bad or "", time.time() - t0))
