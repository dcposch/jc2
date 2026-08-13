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

Phases (run: python3 directionb_window.py [gate|bands|slot20|all]):

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

def slot20():
    """Row_20 with tails: the inhomogeneous window.  The J-identity
    demands Row_20 = -(42/(c_f c_g)) eta^0 (gauge: -42).  Zero-tail
    made this 0 = -42 (INCONSISTENT).  With tails: derive the exact
    condition on the window tails that cancels the -42.

    Minimal stratum solve: all tails 0 EXCEPT the vars entering
    Row_20 LINEARLY (the slot-20 window coordinates).  Rows 6..18
    are then satisfied identically (gate: every term tail-loaded;
    all their vars sit at levels < the linear slot-20 set -- checked).
    Row_20 becomes an E-linear inhomogeneous system on those vars +
    the w^4-block; solved exactly over E per h-sign branch with
    w1 = w2 = 1 (so X_i = a_i^{1/3}, both nonzero: w_i != 0 kept)."""
    byk, vars_, D = load()
    r20 = byk[20]
    # linear slot-20 vars and their radical structure
    linvars = sorted({vname(vars_, vk) for n, v in r20.items()
                      for vk in v if len(vk) == 1})
    print("== SLOT-20: inhomogeneous window ==")
    print("   Row_20 linear vars (%d): %s"
          % (len(linvars), " ".join(linvars)))
    # minimal stratum: keep only linear slot-20 vars that appear in
    # NO row 6..19 and only LINEARLY in Row_20; all other tails -> 0.
    # Then rows 6..19 vanish identically on the stratum and Row_20
    # restricted is exactly E-linear.
    lower = set()
    for k in range(6, 20):
        for n, v in byk.get(k, {}).items():
            for vk in v:
                lower |= {vars_[i] for i in vk}
    nl20 = {vars_[i] for n, v in r20.items()
            for vk in v if len(vk) > 1 for i in vk}
    keepset = set(linvars) - lower - nl20
    excl = sorted(set(linvars) - keepset)
    print("   minimal stratum keeps (%d): %s"
          % (len(keepset), " ".join(sorted(keepset))))
    if excl:
        print("   excluded (appear below slot 20 or nonlinearly): %s"
              % " ".join(excl))
    linvars = sorted(keepset)
    for s1, s2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        # build augmented system over E: cols = linvars + X1 + X2,
        # last col = RHS; w1 = w2 = 1 (all w-monomials -> 1).
        cols = {nm: i for i, nm in enumerate(linvars)}
        iX1, iX2 = len(cols), len(cols) + 1
        iR = len(cols) + 2
        rows = []
        for n, v in sorted(r20.items()):
            row = {}
            def acc(col, ee):
                row[col] = eadd(row.get(col, {}), ee)
                if not row[col]: del row[col]
            for vk, r in v.items():
                if vk and not all(vars_[i] in keepset for i in vk):
                    continue                     # tails -> 0
                for rk, c in r.items():
                    if not vk and rk == K1M:
                        acc(iX1, {(0, 0, 0): c}); continue
                    if not vk and rk == K2M:
                        acc(iX2, {(0, 0, 0): c}); continue
                    ee, pq = rad_to_E(rk, s1, s2)   # w = 1: drop pq
                    acc(cols[vname(vars_, vk)] if vk else iR,
                        escal(ee, c))
            # move any non-(X,w4) const to RHS side as-is (iR col);
            # RHS of the J-identity: -42 at eta^0
            if n == 0:
                acc(iR, {(0, 0, 0): K3(42)})   # LHS - RHS: +42 on iR
            if row: rows.append((n, row))
        rank, piv, ech, left = erank_units([r for _, r in rows], iR)
        # leftover {iR: c} with c a unit = 0 = c: INCONSISTENT;
        # other leftovers (zerodivisor coefficients) = undecided.
        incons = any(set(r) == {iR} and enorm_nonzero(r[iR])
                     for r in left)
        chk("slot-20 (%+d,%+d): system SOLVABLE over E "
            "(rank %d, %d leftover rows%s)"
            % (s1, s2, rank, len(left),
               ", INCONSISTENT" if incons else ""),
            not left)
        if (s1, s2) != (1, 1): continue
        # display the solved system on branch (+1,+1)
        inv = {i: nm for nm, i in cols.items()}
        inv[iX1], inv[iX2], inv[iR] = "X1", "X2", "RHS"
        print("   -- branch (+1,+1): echelon solution "
              "(pivot = -sum of frees; w1 = w2 = 1):")
        for er in ech:
            pivc = min(er, key=lambda c: (c not in piv, c))
            terms = ["[%s]*%s" % (eshow(x, 2), inv[c])
                     for c, x in sorted(er.items()) if c != pivc]
            print("      %s = -( %s )" % (inv[pivc],
                                          " + ".join(terms) or "0"))
    return linvars


if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "all"
    t0 = time.time()
    if ph in ("gate", "all"): gate()
    if ph in ("bands", "all"): bands()
    if ph in ("slot20", "all"): slot20()
    bad = [n for n, c in OK if not c]
    print("\nTOTAL: %d checks, %d FAIL %s  (%.1fs)"
          % (len(OK), len(bad), bad or "", time.time() - t0))
