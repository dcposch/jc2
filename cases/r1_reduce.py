"""r1_reduce.py -- exact linear pre-reduction of the R1 full core.

ADDITIVE accelerator (2026-08-10): parses systems/r1/r1_full_core.ms
(the guard-certified emitted artifact -- ground truth, not the pickles),
separates rows LINEAR in the x-variables, Gaussian-eliminates them
EXACTLY over the radical coefficient ring
  R = Q[r3,z,A1,A2,EB]/(r3^2-3, Phi42(z), A1^3-3-r3, A2^3-3+r3, 2EB^7-3)
      [W1,HW1,W2,HW2]/(2HW1^2-3W1^2, 2HW2^2-3W2^2)
(pivots restricted to UNITS of the etale subalgebra, W-free), substitutes
into the nonlinear residue, and emits systems/r1/r1_reduced_core.ms plus
mod-p variants.  Existing emissions untouched.

Phases: analyze | reduce | emit | sweep
"""
import os, re, sys, time, random, pickle
from fractions import Fraction as Fr
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SYS = os.path.join(ROOT, "systems", "r1")
RUNS = os.path.join(ROOT, "runs")
TMP = "/tmp/r1red"
os.makedirs(TMP, exist_ok=True)

RADS = ["r3", "z", "A1", "A2", "W1", "HW1", "W2", "HW2", "EB"]
# normal-form exponent caps (reduction relations)
CAP = {"r3": 2, "z": 12, "A1": 3, "A2": 3, "EB": 7, "HW1": 2, "HW2": 2}

def log(msg):
    print("[%s] %s" % (time.strftime("%H:%M:%S"), msg), flush=True)

TERM_RE = re.compile(r"([+-]?)([^+-]+)")

def parse_ms(path):
    txt = open(path).read()
    lines = txt.split("\n", 2)
    hdr = [v.strip() for v in lines[0].split(",")]
    char = int(lines[1])
    eqs = lines[2].strip().rstrip(",").split(",\n")
    return hdr, char, eqs

def parse_poly(eq):
    """expanded monomial string -> dict {(radkey, xkey): Fraction}.
    radkey = tuple of 9 exponents (RADS order); xkey = tuple of
    (xindex, exp) pairs sorted."""
    poly = {}
    for sgn, term in TERM_RE.findall(eq.replace(" ", "").replace("\n", "")):
        c = Fr(1)
        rk = [0] * len(RADS)
        xk = {}
        for a in term.split("*"):
            if not a:
                continue
            if a.isdigit():
                c *= int(a)
            else:
                nm, _, ex = a.partition("^")
                e = int(ex) if ex else 1
                if nm in RADS:
                    rk[RADS.index(nm)] += e
                else:
                    assert nm.startswith("x"), nm
                    xk[int(nm[1:])] = xk.get(int(nm[1:]), 0) + e
        if sgn == "-":
            c = -c
        key = (tuple(rk), tuple(sorted(xk.items())))
        poly[key] = poly.get(key, Fr(0)) + c
        if poly[key] == 0:
            del poly[key]
    return poly

def xdeg(xkey):
    return sum(e for _, e in xkey)

def phase_analyze(path=None):
    path = path or os.path.join(SYS, "r1_full_core.ms")
    hdr, char, eqs = parse_ms(path)
    nrad = 7  # radical eqs first
    log("parsed %s: %d vars, char %d, %d eqs (%d radical + %d rows)"
        % (os.path.basename(path), len(hdr), char, len(eqs), nrad,
           len(eqs) - nrad))
    lin, nonlin, stats = [], [], {}
    for i, eq in enumerate(eqs[nrad:]):
        poly = parse_poly(eq)
        degs = sorted({xdeg(xk) for _, xk in poly})
        xvars = sorted({v for _, xk in poly for v, _ in xk})
        wload = any(rk[4] or rk[5] or rk[6] or rk[7]
                    for rk, _ in poly)  # W1/HW1/W2/HW2 present
        rec = dict(row=i, nterms=len(poly), xdegs=degs, nx=len(xvars),
                   wload=wload, const=0 in degs)
        (lin if max(degs) <= 1 else nonlin).append(rec)
        stats[i] = rec
    log("LINEAR rows (x-deg<=1): %d   NONLINEAR: %d" % (len(lin), len(nonlin)))
    for r in lin[:200]:
        log("  lin row %3d: %4d terms, %2d xvars, degs %s, w=%s const=%s"
            % (r["row"], r["nterms"], r["nx"], r["xdegs"], r["wload"],
               r["const"]))
    for r in nonlin:
        log("  NL  row %3d: %6d terms, %3d xvars, degs %s, w=%s const=%s"
            % (r["row"], r["nterms"], r["nx"], r["xdegs"], r["wload"],
               r["const"]))
    return stats

def load_rows(path=None):
    path = path or os.path.join(SYS, "r1_full_core.ms")
    hdr, char, eqs = parse_ms(path)
    nrad = 7
    polys = [parse_poly(eq) for eq in eqs[nrad:]]
    return hdr, char, eqs[:nrad], polys

def var_levels():
    lv = {}
    for line in open(os.path.join(SYS, "r1_full_core.rows.txt")):
        m = re.match(r"(x\d+) = (\S+) \(level (\d+)\)", line)
        if m:
            lv[int(m.group(1)[1:])] = (int(m.group(3)), m.group(2))
    return lv

def phase_incidence():
    """per-variable: max x-degree across all rows; rows containing it;
    rows where it appears linearly with an x-free W-free coefficient."""
    hdr, char, rads, polys = load_rows()
    lv = var_levels()
    maxdeg, rowsof, pivrows = {}, {}, {}
    for i, poly in enumerate(polys):
        seen = {}
        for (rk, xk), c in poly.items():
            for v, e in xk:
                seen[v] = max(seen.get(v, 0), e if len(xk) == 1 else 99
                              if False else e)
        # linear-with-constant-coeff detection: terms c*rad*x_v alone
        constlin = set()
        for (rk, xk), c in poly.items():
            if len(xk) == 1 and xk[0][1] == 1 and not (rk[4] or rk[5]
                                                       or rk[6] or rk[7]):
                constlin.add(xk[0][0])
        # a var is a clean pivot in row i if EVERY term containing it is
        # a pure c*rad*x_v term (x-free W-free coefficient, degree 1)
        allterms = {}
        for (rk, xk), c in poly.items():
            for v, e in xk:
                allterms.setdefault(v, []).append((rk, xk, e))
        for v, terms in allterms.items():
            maxdeg[v] = max(maxdeg.get(v, 0), max(t[2] for t in terms))
            rowsof.setdefault(v, set()).add(i)
            clean = all(len(xk) == 1 and e == 1 and not (rk[4] or rk[5]
                        or rk[6] or rk[7]) for rk, xk, e in terms)
            if clean:
                pivrows.setdefault(v, set()).add(i)
    linvars = sorted(v for v, d in maxdeg.items() if d == 1)
    log("x-vars total %d; QUASI-LINEAR (deg<=1 in every row): %d"
        % (len(maxdeg), len(linvars)))
    npiv = 0
    for v in sorted(maxdeg):
        d = maxdeg[v]
        piv = sorted(pivrows.get(v, []))
        tag = ""
        if d == 1 and piv:
            npiv += 1
            tag = " PIVOTABLE rows=%s" % piv[:6]
        log("  x%-3d lvl %2d deg %2d in %2d rows%s"
            % (v, lv.get(v, (0, "?"))[0], d, len(rowsof[v]), tag))
    log("PIVOTABLE quasi-linear vars (some row has x-free W-free unit-"
        "candidate coeff): %d" % npiv)
    return maxdeg, rowsof, pivrows

# ------------------------------------------------- radical ring arithmetic
# radkey = 9-tuple exponents in RADS order (r3,z,A1,A2,W1,HW1,W2,HW2,EB)
# normal form: r3<2, z<12, A1<3, A2<3, HW1<2, HW2<2, EB<7 (W1,W2 free).
IR3, IZ, IA1, IA2, IW1, IHW1, IW2, IHW2, IEB = range(9)
ZR = [Fr(-1), Fr(-1), 0, Fr(1), Fr(1), 0, Fr(-1), 0, Fr(1), Fr(1), 0, Fr(-1)]
# z^12 = -1 - z + z^3 + z^4 - z^6 + z^8 + z^9 - z^11
RULES = {IR3: (2, [((), Fr(3))]),
         IZ: (12, [((IZ, k), c) for k, c in enumerate(ZR) if c]),
         IA1: (3, [((), Fr(3)), ((IR3, 1), Fr(1))]),
         IA2: (3, [((), Fr(3)), ((IR3, 1), Fr(-1))]),
         IHW1: (2, [((IW1, 2), Fr(3, 2))]),
         IHW2: (2, [((IW2, 2), Fr(3, 2))]),
         IEB: (7, [((), Fr(3, 2))])}
_REDCACHE = {}

def rad_reduce(rk):
    """radkey -> list of (normal radkey, Fraction) summing to rk."""
    hit = _REDCACHE.get(rk)
    if hit is not None:
        return hit
    for idx, (cap, rhs) in RULES.items():
        if rk[idx] >= cap:
            base = list(rk)
            base[idx] -= cap
            out = {}
            for mono, c in rhs:
                nk = list(base)
                for j in range(0, len(mono), 2):
                    nk[mono[j]] += mono[j + 1]
                for nk2, c2 in rad_reduce(tuple(nk)):
                    out[nk2] = out.get(nk2, Fr(0)) + c * c2
            res = [(k, c) for k, c in out.items() if c]
            _REDCACHE[rk] = res
            return res
    _REDCACHE[rk] = [(rk, Fr(1))]
    return _REDCACHE[rk]

def rmul(rk1, rk2):
    return rad_reduce(tuple(a + b for a, b in zip(rk1, rk2)))

def padd(dst, src, scale=Fr(1)):
    for k, c in src.items():
        nc = dst.get(k, Fr(0)) + c * scale
        if nc:
            dst[k] = nc
        else:
            dst.pop(k, None)

def pmul(p1, p2):
    """product of two polys (dict {(radkey,xkey): coeff})."""
    out = {}
    for (rk1, xk1), c1 in p1.items():
        d1 = dict(xk1)
        for (rk2, xk2), c2 in p2.items():
            xm = dict(d1)
            for v, e in xk2:
                xm[v] = xm.get(v, 0) + e
            xkey = tuple(sorted(xm.items()))
            cc = c1 * c2
            for nrk, rc in rmul(rk1, rk2):
                key = (nrk, xkey)
                nc = out.get(key, Fr(0)) + cc * rc
                if nc:
                    out[key] = nc
                else:
                    out.pop(key, None)
    return out

def rad_inv(u):
    """u = dict {radkey: Fr} x-free. min-poly certificate: returns
    (inv dict, minpoly coeffs) or None if zero-divisor/failure."""
    basis, vecs, pows = {}, [], [{(): Fr(1)} if False else {tuple([0]*9): Fr(1)}]
    cur = pows[0]
    for step in range(1, 60):
        nxt = {}
        for rk1, c1 in cur.items():
            for rk2, c2 in u.items():
                for nrk, rc in rmul(rk1, rk2):
                    nc = nxt.get(nrk, Fr(0)) + c1 * c2 * rc
                    if nc:
                        nxt[nrk] = nc
                    else:
                        nxt.pop(nrk, None)
        pows.append(nxt)
        cur = nxt
        # try to find rational dependence among pows[0..step]
        for rk in nxt:
            if rk not in basis:
                basis[rk] = len(basis)
        for p in pows:
            for rk in p:
                if rk not in basis:
                    basis[rk] = len(basis)
        M = [[p.get(rk, Fr(0)) for p in pows] for rk in basis]
        # solve M * a = 0 with a_step = 1 (Gaussian elimination)
        ncols = len(pows)
        rowsM = [r[:] for r in M]
        piv = {}
        r = 0
        for col in range(ncols):
            sel = None
            for i in range(r, len(rowsM)):
                if rowsM[i][col]:
                    sel = i
                    break
            if sel is None:
                # col is dependent on previous: dependence found
                a = [Fr(0)] * ncols
                a[col] = Fr(1)
                for cc in range(col - 1, -1, -1):
                    if cc in piv:
                        i = piv[cc]
                        s = sum(rowsM[i][j] * a[j] for j in range(cc + 1, col + 1))
                        a[cc] = -s / rowsM[i][cc]
                if a[0] == 0:
                    return None  # zero divisor
                # u * (-1/a0)*(a1 + a2 u + ... ) = 1
                inv = {}
                acc = {tuple([0]*9): Fr(1)}
                for k in range(1, col + 1):
                    if a[k]:
                        for rk, c in pows[k - 1].items():
                            nc = inv.get(rk, Fr(0)) - c * a[k] / a[0]
                            if nc:
                                inv[rk] = nc
                            else:
                                inv.pop(rk, None)
                return inv, a[:col + 1]
            rowsM[r], rowsM[sel] = rowsM[sel], rowsM[r]
            piv[col] = r
            pv = rowsM[r][col]
            for i in range(len(rowsM)):
                if i != r and rowsM[i][col]:
                    f = rowsM[i][col] / pv
                    for j in range(col, ncols):
                        rowsM[i][j] -= f * rowsM[r][j]
            r += 1
    return None

def coeff_split(poly, v):
    """split poly by degree in x-var v: {k: poly_without_v}."""
    out = {}
    for (rk, xk), c in poly.items():
        d = dict(xk)
        k = d.pop(v, 0)
        key = (rk, tuple(sorted(d.items())))
        out.setdefault(k, {})
        nc = out[k].get(key, Fr(0)) + c
        if nc:
            out[k][key] = nc
        else:
            out[k].pop(key, None)
    return {k: p for k, p in out.items() if p}

def is_unit_candidate(cp):
    """cp = poly dict; True if x-free and W/HW-free."""
    for (rk, xk) in cp:
        if xk or rk[IW1] or rk[IHW1] or rk[IW2] or rk[IHW2]:
            return False
    return True

COST_CAP = 3 * 10 ** 6

def phase_eliminate(save="reduced.pkl"):
    hdr, char, rads, polys = load_rows()
    lv = var_levels()
    rows = {i: p for i, p in enumerate(polys)}
    subs = []          # banked (var, u dict, s poly, pivot row idx) in order
    dropped = []       # rows that became identically zero (rank deficiency)
    t0 = time.time()
    it = 0
    while True:
        it += 1
        # one-pass incidence: per row, per var -> (maxdeg, nterms>=1,
        # clean flag = every term with v is deg-1 single-x W-free)
        occ = {}   # v -> {row: [maxdeg, n_terms_with_v, clean]}
        for i, p in rows.items():
            local = {}
            for (rk, xk), c in p.items():
                wl = rk[IW1] or rk[IHW1] or rk[IW2] or rk[IHW2]
                for v, e in xk:
                    st = local.setdefault(v, [0, 0, True])
                    st[0] = max(st[0], e)
                    st[1] += 1
                    if e != 1 or len(xk) != 1 or wl:
                        st[2] = False
            for v, st in local.items():
                occ.setdefault(v, {})[i] = st
        best = None
        for v, byrow in occ.items():
            md = max(st[0] for st in byrow.values())
            if md > 3:
                continue  # power blowup guard
            pivs = [(A, st) for A, st in byrow.items()
                    if st[0] == 1 and st[2] and (v, A) not in COSTBLACK]
            if not pivs:
                continue
            for A, stA in pivs:
                slen = max(1, len(rows[A]) - stA[1])
                cost = 0
                for B, stB in byrow.items():
                    if B != A:
                        cost += stB[1] * slen ** stB[0]
                if cost > COST_CAP:
                    continue
                if best is None or cost < best[0]:
                    best = (cost, v, A)
        if best is None:
            log("iter %d: no admissible pivot left" % it)
            break
        cost, v, A = best
        sp = coeff_split(rows[A], v)
        inv = rad_inv({rk: c for (rk, xk), c in sp[1].items()})
        if inv is None:
            log("iter %d: x%d row %d coeff is ZERO-DIVISOR, skip" % (it, v, A))
            # mark as non-candidate by temporary removal hack: continue would
            # loop forever; instead blacklist via cost cap trick
            COSTBLACK.add((v, A))
            continue
        invd, minpoly = inv
        # s = -u^{-1} * rest_A   (rest_A = sp[0], the v-free part)
        invpoly = {(rk, ()): c for rk, c in invd.items()}
        s = pmul({k: -c for k, c in sp.get(0, {}).items()}, invpoly)
        # substitute into all other rows
        touched = 0
        for B in list(rows):
            if B == A:
                continue
            spB = coeff_split(rows[B], v)
            if len(spB) == 1 and 0 in spB:
                continue
            newB = spB.get(0, {})
            newB = dict(newB)
            sk = dict(s)
            deg = 1
            for k in sorted(k for k in spB if k >= 1):
                while deg < k:
                    sk = pmul(sk, s)
                    deg += 1
                padd(newB, pmul(spB[k], sk))
            if newB:
                rows[B] = newB
            else:
                dropped.append(B)
                del rows[B]
            touched += 1
        subs.append((v, {rk: c for (rk, xk), c in sp[1].items()}, s, A))
        del rows[A]
        tot = sum(len(p) for p in rows.values())
        log("iter %d: eliminated x%d (lvl %d) via row %d "
            "(|s|=%d, minpoly deg %d, cost %d, touched %d) -> %d rows, "
            "%d terms, %.0fs" % (it, v, lv.get(v, (0,))[0], A, len(s),
            len(minpoly) - 1, cost, touched, len(rows), tot,
            time.time() - t0))
        if it % 5 == 0:
            with open(os.path.join(TMP, save), "wb") as f:
                pickle.dump(dict(rows=rows, subs=subs, dropped=dropped), f)
    with open(os.path.join(TMP, save), "wb") as f:
        pickle.dump(dict(rows=rows, subs=subs, dropped=dropped), f)
    remv = sorted({v for p in rows.values() for (rk, xk) in p for v, e in xk})
    log("DONE: %d rows, %d x-vars remain (%d eliminated, %d rows dropped "
        "as identically zero)" % (len(rows), len(remv), len(subs),
                                  len(dropped)))
    log("remaining vars: %s" % remv)
    return rows, subs

COSTBLACK = set()

# ------------------------------------------------------------- emission
def import_fullcore():
    sys.path.insert(0, HERE)
    import r1_fullcore as FC
    return FC

def emit_poly(poly, order=None):
    """poly dict -> (expanded integer monomial string, scale Fraction).
    scale = L/G with L = lcm of denominators, G = content."""
    L = 1
    for k, c in poly.items():
        L = L * c.denominator // gcd(L, c.denominator)
    G = 0
    for k, c in poly.items():
        G = gcd(G, abs((c * L).numerator))
    scale = Fr(L, G) if G > 1 else Fr(L)
    parts = []
    for (rk, xk) in sorted(poly, key=lambda t: (t[1], t[0])):
        c = poly[(rk, xk)] * scale
        assert c.denominator == 1
        n = c.numerator
        mono = []
        for i, e in enumerate(rk):
            if e:
                mono.append(RADS[i] + ("^%d" % e if e > 1 else ""))
        for v, e in xk:
            mono.append("x%d" % v + ("^%d" % e if e > 1 else ""))
        if mono:
            body = (str(abs(n)) + "*" if abs(n) != 1 else "") + "*".join(mono)
        else:
            body = str(abs(n))
        parts.append(("-" if n < 0 else "+") + body)
    s = "".join(parts)
    return (s[1:] if s.startswith("+") else s), scale

def eval_poly_modp(poly, pt, p, xval):
    """internal evaluator: poly dict at radical point pt + x values."""
    names = ["r3", "z", "A1", "A2", "W1", "HW1", "W2", "HW2", "EB"]
    tot = 0
    for (rk, xk), c in poly.items():
        t = FCMOD(c, p)
        for i, e in enumerate(rk):
            if e:
                t = t * pow(pt[names[i]], e, p) % p
        for v, e in xk:
            t = t * pow(xval[v], e, p) % p
        tot = (tot + t) % p
    return tot

def FCMOD(q, p):
    return q.numerator % p * pow(q.denominator % p, p - 2, p) % p

def phase_emitred():
    FC = import_fullcore()
    with open(os.path.join(TMP, "reduced.pkl"), "rb") as f:
        st = pickle.load(f)
    rows, subs, dropped = st["rows"], st["subs"], st["dropped"]
    hdr0, char0, rads, orig = load_rows()
    # original row labels (eq7.. in rows.txt = row 0..)
    labels = {}
    for line in open(os.path.join(SYS, "r1_full_core.rows.txt")):
        m = re.match(r"eq(\d+) = (.*)", line)
        if m and int(m.group(1)) >= 7:
            labels[int(m.group(1)) - 7] = m.group(2).strip()
    remv = sorted({v for pl in rows.values() for (rk, xk) in pl
                   for v, e in xk})
    elimv = [v for v, u, s2, A in subs]
    freev = sorted(set(range(119)) - set(remv) - set(elimv))
    log("emit: %d rows, %d x-vars remain; %d eliminated; free (dropped "
        "from header): %s" % (len(rows), len(remv), len(elimv), freev))
    hdr = RADS + ["x%d" % v for v in remv]
    eqs = list(rads)
    scales = {}
    metas = [("radical", i) for i in range(len(rads))]
    for i in sorted(rows):
        s, sc = emit_poly(rows[i])
        eqs.append(s)
        scales[i] = sc
        metas.append(("row", i))
    path = os.path.join(SYS, "r1_reduced_core.ms")
    with open(path, "w") as f:
        f.write(", ".join(hdr) + "\n0\n")
        f.write(",\n".join(eqs) + "\n")
    log("emitted %s (%d eqs, %d vars, %.1f MB)"
        % (path, len(eqs), len(hdr), os.path.getsize(path) / 1e6))
    with open(os.path.join(SYS, "r1_reduced_core.rows.txt"), "w") as f:
        f.write("# reduced core from r1_full_core.ms by exact quasi-linear "
                "elimination (cases/r1_reduce.py)\n"
                "# %d eliminated vars (in order), %d surviving rows, "
                "%d rows dropped as identically zero, free vars %s\n"
                % (len(subs), len(rows), len(dropped), freev))
        for j, (v, u, s2, A) in enumerate(subs):
            f.write("elim%d: x%d via origrow %d (%s) |s|=%d\n"
                    % (j, v, A, labels.get(A, "?"), len(s2)))
        for j, m in enumerate(metas):
            lab = labels.get(m[1], "radical%d" % m[1]) if m[0] == "row" \
                else "radical eq %d" % m[1]
            f.write("eq%d = %s %s\n" % (j, m[0], lab))
    # mod-p variants (radicals as variables)
    for p in FC.good_primes(2):
        pp = os.path.join(SYS, "r1_reduced_core_p%d.ms" % p)
        with open(pp, "w") as f:
            f.write(", ".join(hdr) + "\n%d\n" % p)
            peqs = [re.sub(r"(?<![\w^])\d+", lambda m: str(int(m.group(0))
                                                           % p), eq)
                    for eq in eqs]
            f.write(",\n".join(peqs) + "\n")
        log("emitted %s (%.1f MB)" % (pp, os.path.getsize(pp) / 1e6))
    # w-free variants (z,r3,A1,A2,EB specialized; W/HW free)
    for p in FC.good_primes(2):
        pt = FC.radical_point(p)
        wq = ["%d*HW1^2-%d*W1^2" % (2 % p, 3 % p),
              "%d*HW2^2-%d*W2^2" % (2 % p, 3 % p)]
        weqs = []
        for i in sorted(rows):
            spec = {}
            for (rk, xk), c in rows[i].items():
                t = FCMOD(c * scales[i], p)
                for idx, nm in ((IR3, "r3"), (IZ, "z"), (IA1, "A1"),
                                (IA2, "A2"), (IEB, "EB")):
                    if rk[idx]:
                        t = t * pow(pt[nm], rk[idx], p) % p
                wk = (rk[IW1], rk[IHW1], rk[IW2], rk[IHW2])
                key = (wk, xk)
                spec[key] = (spec.get(key, 0) + t) % p
            parts = []
            for (wk, xk) in sorted(spec):
                n = spec[(wk, xk)]
                if not n:
                    continue
                mono = []
                for e, nm in zip(wk, ("W1", "HW1", "W2", "HW2")):
                    if e:
                        mono.append(nm + ("^%d" % e if e > 1 else ""))
                for v, e in xk:
                    mono.append("x%d" % v + ("^%d" % e if e > 1 else ""))
                body = (str(n) + "*" if mono else str(n)) + "*".join(mono)
                if body.endswith("*"):
                    body = body[:-1]
                parts.append("+" + body)
            s = "".join(parts)
            weqs.append(s[1:] if s else "0")
        pp = os.path.join(SYS, "r1_reduced_core_wfree_p%d.ms" % p)
        whdr = ["W1", "HW1", "W2", "HW2"] + ["x%d" % v for v in remv]
        with open(pp, "w") as f:
            f.write(", ".join(whdr) + "\n%d\n" % p)
            f.write(",\n".join(wq + weqs) + "\n")
        log("emitted %s (%.1f MB)" % (pp, os.path.getsize(pp) / 1e6))
    return path

def phase_guards():
    FC = import_fullcore()
    with open(os.path.join(TMP, "reduced.pkl"), "rb") as f:
        st = pickle.load(f)
    rows, subs = st["rows"], st["subs"]
    hdr0, char0, rads, orig = load_rows()
    path = os.path.join(SYS, "r1_reduced_core.ms")
    txt = open(path).read()
    assert "(" not in txt and ")" not in txt, "PAREN SWEEP FAIL"
    log("guard A (paren sweep): PASS")
    lines = txt.split("\n", 2)
    hdr = [v.strip() for v in lines[0].split(",")]
    eqs = lines[2].strip().rstrip(",").split(",\n")[7:]
    idx = sorted(rows)
    assert len(eqs) == len(idx)
    remv = sorted({v for pl in rows.values() for (rk, xk) in pl
                   for v, e in xk})
    # guard B: independent-parser round trip at 2 fresh primes
    for p in FC.good_primes(2):
        pt = FC.radical_point(p)
        rng = random.Random(4200 + p)
        xval = {v: rng.randrange(1, p) for v in remv}
        val = dict(pt)
        val.update({"x%d" % v: xval[v] for v in remv})
        got = FC.parse_eval(eqs, val, p)
        nz = 0
        for j, i in enumerate(idx):
            s, sc = emit_poly(rows[i])
            want = eval_poly_modp(rows[i], pt, p, xval) * FCMOD(sc, p) % p
            assert got[j] == want, ("ROUND-TRIP FAIL", p, i)
            if got[j]:
                nz += 1
        log("guard B (round-trip, p=%d): PASS %d/%d rows; %d nonzero at "
            "random point" % (p, len(idx), len(idx), nz))
    # guard C: origin
    p = FC.good_primes(1)[0]
    pt = FC.radical_point(p)
    x0 = {v: 0 for v in remv}
    at0 = [eval_poly_modp(rows[i], pt, p, x0) for i in idx]
    n0 = sum(1 for t in at0 if t == 0)
    log("guard C (origin): %d/%d rows vanish at x=0 (+radical point); "
        "NOT-origin-satisfiable %s" % (n0, len(idx),
        "PASS (some rows nonzero)" if n0 < len(idx) else
        "FAIL (origin satisfies all rows)"))
    # guard D: residual (identically-zero scan)
    dead = set(idx)
    for p in FC.good_primes(2):
        pt = FC.radical_point(p)
        for t in range(3):
            rng = random.Random(9100 + p * 10 + t)
            xv = {v: rng.randrange(1, p) for v in remv}
            for i in sorted(dead):
                if eval_poly_modp(rows[i], pt, p, xv):
                    dead.discard(i)
    log("guard D (residual): %d identically-zero rows among survivors"
        % len(dead))
    assert not dead
    # guard E: SOUNDNESS IDENTITY -- back-map random points; consumed
    # pivot rows must vanish; surviving original rows must equal reduced
    for p in FC.good_primes(2):
        pt = FC.radical_point(p)
        for t in range(2):
            rng = random.Random(5300 + p * 10 + t)
            xv = {v: rng.randrange(1, p) for v in remv}
            # free vars (in no surviving row, never eliminated): random
            elimset = {v for v, u, s2, A in subs}
            for v in range(119):
                if v not in xv and v not in elimset:
                    xv[v] = rng.randrange(1, p)
            # back-substitute in reverse elimination order
            for v, u, s2, A in reversed(subs):
                xv[v] = eval_poly_modp(s2, pt, p, xv)
            for j, (v, u, s2, A) in enumerate(subs):
                gotA = eval_poly_modp(orig[A], pt, p, xv)
                assert gotA == 0, ("PIVOT ROW NONZERO UNDER BACK-MAP",
                                   A, v, p, t)
            for i in idx:
                a = eval_poly_modp(orig[i], pt, p, xv)
                b = eval_poly_modp(rows[i], pt, p, xv)
                assert a == b, ("SURVIVOR MISMATCH", i, p, t)
            for B in st["dropped"]:
                gotB = eval_poly_modp(orig[B], pt, p, xv)
                assert gotB == 0, ("DROPPED ROW NONZERO UNDER BACK-MAP",
                                   B, p, t)
            log("guard E (soundness identity, p=%d, pt %d): PASS -- %d "
                "pivot rows + %d dropped rows vanish under back-map; %d "
                "survivors match original rows"
                % (p, t, len(subs), len(st["dropped"]), len(idx)))

def phase_selftest():
    one = tuple([0] * 9)
    # (a) r3^2 -> 3
    rk = list(one); rk[IR3] = 2
    assert rad_reduce(tuple(rk)) == [(one, Fr(3))]
    # (b) EB^7 -> 3/2 ; EB^8 -> 3/2 EB
    rk = list(one); rk[IEB] = 8
    ek = list(one); ek[IEB] = 1
    assert rad_reduce(tuple(rk)) == [(tuple(ek), Fr(3, 2))]
    # (c) inverse of 3(r3-3)*A1^2: u = (3r3-9) A1^2
    rk1 = list(one); rk1[IR3] = 1; rk1[IA1] = 2
    rk2 = list(one); rk2[IA1] = 2
    u = {tuple(rk1): Fr(3), tuple(rk2): Fr(-9)}
    res = rad_inv(u)
    assert res is not None, "unit not inverted"
    invd, mp = res
    chk = {}
    for rk, c in u.items():
        for rk2_, c2 in invd.items():
            for nrk, rc in rmul(rk, rk2_):
                chk[nrk] = chk.get(nrk, Fr(0)) + c * c2 * rc
    chk = {k: c for k, c in chk.items() if c}
    assert chk == {one: Fr(1)}, chk
    # (d) zero divisor: W1 (x-free but W-loaded is pre-filtered; test
    # a genuine zero divisor in the etale algebra: none easy -> test
    # that a unit z inverts: z * z^-1 = 1
    zk = list(one); zk[IZ] = 1
    res = rad_inv({tuple(zk): Fr(1)})
    assert res is not None
    invd, mp = res
    chk = {}
    for rk2_, c2 in invd.items():
        for nrk, rc in rmul(tuple(zk), rk2_):
            chk[nrk] = chk.get(nrk, Fr(0)) + c2 * rc
    chk = {k: c for k, c in chk.items() if c}
    assert chk == {one: Fr(1)}, chk
    # (e) pmul sanity: (x0 + r3)^2 = x0^2 + 2 r3 x0 + 3
    p = {(one, ((0, 1),)): Fr(1), (tuple([1] + [0] * 8), ()): Fr(1)}
    sq = pmul(p, p)
    want = {(one, ((0, 2),)): Fr(1),
            (tuple([1] + [0] * 8), ((0, 1),)): Fr(2),
            (one, ()): Fr(3)}
    assert sq == want, sq
    log("selftest PASS (rad_reduce, rad_inv unit+minpoly, pmul)")

# --------------------------------------------------------------- sweep
def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

def sweep_primes(n=10, seed=61):
    rng = random.Random(seed)
    out = []
    while len(out) < n:
        c = rng.randrange(2 ** 15, 2 ** 17) | 1
        if is_prime(c) and c not in out:
            out.append(c)
    return out

def run_msolve(path, out, timeout=1200):
    import subprocess
    t0 = time.time()
    try:
        proc = subprocess.run(["msolve", "-g", "2", "-f", path, "-o", out],
                              timeout=timeout, capture_output=True)
        wall = time.time() - t0
    except subprocess.TimeoutExpired:
        with open(out, "w") as f:
            f.write("TIMEOUT %ds\n" % timeout)
        return "TIMEOUT", timeout
    txt = open(out).read() if os.path.exists(out) else ""
    body = [l for l in txt.splitlines() if l and not l.startswith("#")]
    with open(path) as f:
        f.readline()
        char = int(f.readline().strip())
    is_unit = any(l.strip().rstrip(":") == "[1]" for l in body)
    complete_basis = (proc.returncode == 0 and
                      any(l.strip().endswith("]:") for l in body))
    if not complete_basis:
        return "NO-VERDICT (solver failure or no complete basis body)", wall
    if char == 0:
        verdict = ("FIRST-PRIME-EMPTY TRACE (NOT Q-EMPTY)" if is_unit else
                   "GB!=[1] NONEMPTY over Qbar (reconstructed Q basis; engine-trusted)")
    else:
        verdict = ("GB=[1] EMPTY over F_%d" % char if is_unit else
                   "GB!=[1] NONEMPTY over algebraic closure of F_%d" % char)
    return verdict, wall

def phase_sweep(n=10, skip=0):
    src = os.path.join(SYS, "r1_reduced_core.ms")
    txt = open(src).read()
    lines = txt.split("\n", 2)
    swdir = os.path.join(TMP, "sweep")
    os.makedirs(swdir, exist_ok=True)
    results = []
    logf = os.path.join(RUNS, "r1_reduced_sweep.log")
    for p in sweep_primes(n)[skip:]:
        pp = os.path.join(swdir, "r1_reduced_core_p%d.ms" % p)
        with open(pp, "w") as f:
            f.write(lines[0] + "\n%d\n" % p)
            f.write(re.sub(r"(?<![\w^])\d+",
                           lambda m: str(int(m.group(0)) % p), lines[2]))
        out = os.path.join(RUNS, "r1_reduced_sweep_p%d.out" % p)
        verdict, wall = run_msolve(pp, out)
        results.append((p, verdict, wall))
        line = "p=%d %s %.1fs" % (p, verdict, wall)
        log("sweep " + line)
        with open(logf, "a") as f:
            f.write(line + "\n")
    return results

def emit_wfree_at(p, pt, rows, scales, remv, path):
    wq = ["2*HW1^2-%d*W1^2" % (3 % p), "2*HW2^2-%d*W2^2" % (3 % p)]
    weqs = []
    for i in sorted(rows):
        spec = {}
        for (rk, xk), c in rows[i].items():
            t = FCMOD(c * scales[i], p)
            for idx, nm in ((IR3, "r3"), (IZ, "z"), (IA1, "A1"),
                            (IA2, "A2"), (IEB, "EB")):
                if rk[idx]:
                    t = t * pow(pt[nm], rk[idx], p) % p
            wk = (rk[IW1], rk[IHW1], rk[IW2], rk[IHW2])
            key = (wk, xk)
            spec[key] = (spec.get(key, 0) + t) % p
        parts = []
        for (wk, xk) in sorted(spec):
            n = spec[(wk, xk)]
            if not n:
                continue
            mono = []
            for e, nm in zip(wk, ("W1", "HW1", "W2", "HW2")):
                if e:
                    mono.append(nm + ("^%d" % e if e > 1 else ""))
            for v, e in xk:
                mono.append("x%d" % v + ("^%d" % e if e > 1 else ""))
            body = (str(n) + "*" if mono else str(n)) + "*".join(mono)
            if body.endswith("*"):
                body = body[:-1]
            parts.append("+" + body)
        s = "".join(parts)
        weqs.append(s[1:] if s else "0")
    whdr = ["W1", "HW1", "W2", "HW2"] + ["x%d" % v for v in remv]
    with open(path, "w") as f:
        f.write(", ".join(whdr) + "\n%d\n" % p)
        f.write(",\n".join(wq + weqs) + "\n")

def sweepw_primes(n=8, seed=17):
    """random primes ~2^15..2^17 with p == 1 mod 84 and a full radical
    point (for the w-free branch specialization)."""
    FC = import_fullcore()
    rng = random.Random(seed)
    out = []
    while len(out) < n:
        c = rng.randrange(2 ** 15 // 84, 2 ** 17 // 84) * 84 + 1
        if c in out or not is_prime(c):
            continue
        if FC.radical_point(c):
            out.append(c)
    return out

def phase_sweepw1(p):
    FC = import_fullcore()
    with open(os.path.join(TMP, "reduced.pkl"), "rb") as f:
        st = pickle.load(f)
    rows = st["rows"]
    scales = {}
    for i in sorted(rows):
        s, sc = emit_poly(rows[i])
        scales[i] = sc
    remv = sorted({v for pl in rows.values() for (rk, xk) in pl
                   for v, e in xk})
    pt = FC.radical_point(p)
    assert pt, "no radical point for %d" % p
    swdir = os.path.join(TMP, "sweep")
    os.makedirs(swdir, exist_ok=True)
    pp = os.path.join(swdir, "r1_reduced_core_wfree_p%d.ms" % p)
    emit_wfree_at(p, pt, rows, scales, remv, pp)
    out = os.path.join(RUNS, "r1_reduced_sweepw_p%d.out" % p)
    verdict, wall = run_msolve(pp, out)
    line = "wfree p=%d %s %.1fs" % (p, verdict, wall)
    log("sweepw " + line)
    with open(os.path.join(RUNS, "r1_reduced_sweep.log"), "a") as f:
        f.write(line + "\n")

def phase_msolve():
    for name, out in [("r1_reduced_core.ms", "char0"),
                      ("r1_reduced_core_p105337.ms", "fullp"),
                      ("r1_reduced_core_p105673.ms", "fullp"),
                      ("r1_reduced_core_wfree_p105337.ms", "wfree"),
                      ("r1_reduced_core_wfree_p105673.ms", "wfree")]:
        path = os.path.join(SYS, name)
        outp = os.path.join(RUNS, name + "." + out + ".out")
        verdict, wall = run_msolve(path, outp)
        log("msolve %s: %s %.1fs" % (name, verdict, wall))

if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "analyze"
    if ph == "analyze":
        phase_analyze(sys.argv[2] if len(sys.argv) > 2 else None)
    elif ph == "incidence":
        phase_incidence()
    elif ph == "eliminate":
        phase_eliminate()
    elif ph == "selftest":
        phase_selftest()
    elif ph == "emitred":
        phase_emitred()
    elif ph == "guards":
        phase_guards()
    elif ph == "sweep":
        phase_sweep(int(sys.argv[2]) if len(sys.argv) > 2 else 10,
                    int(sys.argv[3]) if len(sys.argv) > 3 else 0)
    elif ph == "sweep1":
        # single prime by value (parallel driver)
        src = os.path.join(SYS, "r1_reduced_core.ms")
        txt = open(src).read()
        lines = txt.split("\n", 2)
        swdir = os.path.join(TMP, "sweep")
        os.makedirs(swdir, exist_ok=True)
        p = int(sys.argv[2])
        pp = os.path.join(swdir, "r1_reduced_core_p%d.ms" % p)
        with open(pp, "w") as f:
            f.write(lines[0] + "\n%d\n" % p)
            f.write(re.sub(r"(?<![\w^])\d+",
                           lambda m: str(int(m.group(0)) % p), lines[2]))
        out = os.path.join(RUNS, "r1_reduced_sweep_p%d.out" % p)
        verdict, wall = run_msolve(pp, out)
        line = "p=%d %s %.1fs" % (p, verdict, wall)
        log("sweep " + line)
        with open(os.path.join(RUNS, "r1_reduced_sweep.log"), "a") as f:
            f.write(line + "\n")
    elif ph == "msolve":
        phase_msolve()
    elif ph == "sweepw1":
        phase_sweepw1(int(sys.argv[2]))
    elif ph == "sweepwprimes":
        print(sweepw_primes(int(sys.argv[2]) if len(sys.argv) > 2 else 8))
