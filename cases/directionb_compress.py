#!/usr/bin/env python3
"""SHEET6-DIRECTIONB §7.S1: EXACT SYMBOLIC BAND ELIMINATION of the
42 high tails from the nolog residual-32 decider (Sol instrument
verdict, xmodel/sol-instrument.md §C; owner: this module).

Math: in the nolog window (D21, §7 pins SUBSTITUTED, 76 rows after
C10.6 dies) the 42 occurring high tails (levels >= 43) enter
AFFINE-LINEARLY (no high*high monomial exists below slot 21:
43 + 43 = 86 > 84 -- asserted).  Each band introduces its new highs
with CONSTANT ring coefficients (their own-band pure-linear terms),
and those constants are units ON THE VARIETY (single w-monomial
weight x unit of the etale algebra E on every h-sign branch --
verified per pivot).  Fraction-free Bareiss steps
    R_t' = c_p * R_t - A_t(lows) * R_p
(c_p the constant pivot coefficient, A_t the affine coefficient of
the pivot var in R_t) eliminate the highs EXACTLY over the ring --
no denominators beyond the radical tower, branch-free.  If the
generic high-rank 16 is exact, every non-pivot row ends HIGH-FREE
(asserted): the result is the 32-row COMPATIBILITY system on the
low parameters + dead-stretch + w1, w2, joined by the untouched
low bands 6/8/10 (28 rows).

Phases: elim | emit | guards | all
State in:  /tmp/directionb_tails_D21.pkl (+ banked legend names)
State out: /tmp/directionb_compressed.pkl (rows + pivots + labels)
Files out: cases/directionb_compressed[.ms|_p105337.ms|_p200257.ms|
           _ctl0*.ms|_a3_p105337.ms] + directionb_compressed.rows.txt
"""
import os, sys, time, pickle, random
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r1_experiment as R1
import r1_fullcore as FC
import directionb_window as W
import directionb_residual32_emit as E32

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "directionb_compressed"
PRIMES = (105337, 200257)
PIN42 = ("tf1_42", "tf2_42", "tg1_42", "tg2_42", "tg01_42", "tg02_42")
REG32 = [(12, 8), (12, 11), (12, 14), (12, 17), (12, 20), (12, 23),
         (12, 26), (14, 6), (14, 9), (14, 12), (14, 15), (14, 18),
         (14, 21), (14, 24), (14, 27), (16, 13), (16, 16), (16, 19),
         (16, 22), (16, 25), (16, 28), (18, 14), (18, 17), (18, 20),
         (18, 23), (18, 26), (20, 12), (20, 15), (20, 18), (20, 21),
         (20, 24), (20, 27)]                     # claim-4 registered

OK = []
def chk(name, cond):
    OK.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, flush=True)

def lvl(nm):
    try: return int(nm.rsplit("_", 1)[-1])
    except ValueError: return -1

def load_nolog_rows():
    byk, vars_, D = W.load()
    Zs = set(PIN42)
    rows = []
    for k in sorted(byk):
        for n in sorted(byk[k]):
            v = dict(byk[k][n])
            if k == 20 and n == 0:
                v[()] = R1.radd(v.get((), R1.RZERO), R1.rC(R1.K3(42)))
            keep = {vk: r for vk, r in v.items()
                    if not (vk and any(vars_[i] in Zs for i in vk))}
            if keep: rows.append(((k, n), keep))
    return rows, vars_

def unit_on_variety(c):
    """ring elt c: single w-bidegree AND E-unit on all 4 branches."""
    pqs, ok = set(), True
    for s1, s2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        acc = {}
        for rk, x in c.items():
            ee, pq = W.rad_to_E(rk, s1, s2)
            pqs.add(pq)
            acc = W.eadd(acc, W.escal(ee, x))
        ok &= W.enorm_nonzero(acc)
    return ok and len(pqs) == 1

def affine_split(v, hid):
    """v affine in var hid: returns (A, B) with v = A*hid + B; asserts
    hid appears at most once per monomial."""
    A, B = {}, {}
    for vk, r in v.items():
        c = vk.count(hid)
        assert c <= 1, "not affine in %d" % hid
        if c:
            lst = list(vk); lst.remove(hid); k2 = tuple(lst)
            A[k2] = R1.radd(A.get(k2, R1.RZERO), r)
            if not A[k2]: del A[k2]
        else:
            B[vk] = r
    return A, B

def vsub_row(vt, At, Rp, cp):
    """R_t' = cp * R_t - A_t * R_p   (VExpr arithmetic, exact)."""
    out = {k: R1.rmul(r, cp) for k, r in vt.items()}
    out = {k: r for k, r in out.items() if r}
    for ka, ra in At.items():
        for kp, rp in Rp.items():
            k = tuple(sorted(ka + kp))
            prod = R1.rmul(ra, rp)
            if not prod: continue
            cur = out.get(k)
            nr = R1.radd(cur, R1.rscal(prod, R1.K3(-1))) if cur \
                else R1.rscal(prod, R1.K3(-1))
            if nr: out[k] = nr
            elif cur is not None: del out[k]
    return out

def phase_elim():
    t0 = time.time()
    rows, vars_ = load_nolog_rows()
    HIGH = {i for i, nm in enumerate(vars_)
            if nm[:2] in ("tf", "tg") and lvl(nm) >= 43}
    chk("nolog window: %d rows (77 - C10.6); every row affine in the "
        "highs (no high*high monomial)" % len(rows),
        len(rows) == 76 and all(
            sum(1 for i in vk if i in HIGH) <= 1
            for _, v in rows for vk in v))
    live = [[lab, dict(v)] for lab, v in rows]
    pivots = []          # (high vid, row label, cp)
    used = set()
    for bi, (lab, v) in enumerate(live):
        k, n = lab
        if k < 12: continue
        # candidate pivot: a high var with PURE-CONSTANT coefficient
        hs = sorted({i for vk in v for i in vk if i in HIGH})
        for h in hs:
            if h in [p[0] for p in pivots]: continue
            A, B = affine_split(v, h)
            if set(A) == {()} and unit_on_variety(A[()]):
                cp = A[()]
                pivots.append((h, lab, cp)); used.add(bi)
                nup = 0
                for bj, (lab2, v2) in enumerate(live):
                    if bj == bi or bj in used: continue
                    A2, B2 = affine_split(v2, h)
                    if A2:
                        live[bj][1] = vsub_row(v2, A2, v, cp)
                        nup += 1
                print("   pivot %2d: %s <- Row_%d[eta^%d], %d rows "
                      "updated (%.0fs)" % (len(pivots), vars_[h],
                                           lab[0], lab[1], nup,
                                           time.time() - t0),
                      flush=True)
                break
    resid = [(lab, v) for bi, (lab, v) in enumerate(live)
             if bi not in used and v]
    highfree = all(not any(i in HIGH for vk in v for i in vk)
                   for _, v in resid)
    chk("elimination CLEAN: %d unit pivots (variety-units on all 4 "
        "branches, single w-weight); every residual row HIGH-FREE"
        % len(pivots), highfree)
    labs = [lab for lab, _ in resid]
    ob = [l for l in labs if l[0] >= 12]
    chk("residual = the 28 low-band rows + EXACTLY the 32 registered "
        "claim-4 labels (%d + %d)" % (len(labs) - len(ob), len(ob)),
        sorted(ob) == sorted(REG32) and len(labs) == 60)
    st = {"resid": resid, "pivots": [(h, lab) for h, lab, _ in pivots],
          "pivc": [(h, lab, cp) for h, lab, cp in pivots],
          "vars": vars_}
    with open("/tmp/directionb_compressed.pkl", "wb") as fh:
        pickle.dump(st, fh)
    nt = sum(len(R1.poly_terms(v, DummyNames(vars_))) for _, v in resid)
    degs = {}
    for lab, v in resid:
        d = max((len(vk) for vk in v), default=0)
        degs[d] = degs.get(d, 0) + 1
    print("   residual: 60 rows, %d expanded terms, var-degree "
          "profile %s (%.0fs); banked /tmp/directionb_compressed.pkl"
          % (nt, dict(sorted(degs.items())), time.time() - t0),
          flush=True)
    chk("STOP-CRITERIA (Sol §C): term mass %d < 1e6 AND < raw pinned "
        "mass 67698" % nt, nt < 10**6 and nt < 67698)
    return resid, pivots

class DummyNames(dict):
    def __init__(self, vars_): self.vars_ = vars_
    def __getitem__(self, i): return "v%d" % i

# --------------------------------------------------------------- emit
def phase_emit():
    st = pickle.load(open("/tmp/directionb_compressed.pkl", "rb"))
    resid, vars_ = st["resid"], st["vars"]
    _, names, ordered, blocks, _ = E32.load_rows()
    occ = sorted({i for _, v in resid for vk in v for i in vk})
    hdrx = [names[i] for i in occ]
    hdr = hdrx + ["uW1", "uW2", "uA", "W1", "HW1", "W2", "HW2",
                  "A1", "A2", "r3"]
    body0, bodyp = [], {p: [] for p in PRIMES}
    body0c, bodypc = [], {p: [] for p in PRIMES}
    nterm, maxdeg = 0, 0
    for lab, v in resid:
        terms = R1.poly_terms(v, names)
        nterm += len(terms)
        maxdeg = max(maxdeg, max((len(vk) for vk in v), default=0))
        sc = E32.row_scale_terms(terms)
        body0.append(R1.emit_expanded(v, names))
        for p in PRIMES:
            bodyp[p].append(E32.emit_modp(terms, sc, p))
        vc = {vk: r for vk, r in v.items() if vk}
        if vc:
            tc = R1.poly_terms(vc, names)
            sc2 = E32.row_scale_terms(tc)
            body0c.append(R1.emit_expanded(vc, names))
            for p in PRIMES:
                bodypc[p].append(E32.emit_modp(tc, sc2, p))
    sat0 = ["uW1*W1-1", "uW2*W2-1", "uA*A1-uA*A2-1"]
    rad0 = ["r3^2-3", "A1^3-3-r3", "A2^3-3+r3", "2*HW1^2-3*W1^2",
            "2*HW2^2-3*W2^2"]
    def wr(path, char, eqs):
        with open(path, "w") as f:
            f.write(", ".join(hdr) + "\n%d\n" % char)
            f.write(",\n".join(eqs) + "\n")
        return os.path.getsize(path)
    sz = wr(os.path.join(HERE, BASE + ".ms"), 0, body0 + rad0 + sat0)
    wr(os.path.join(HERE, BASE + "_ctl0.ms"), 0, body0c + rad0 + sat0)
    for p in PRIMES:
        tp = ["r3^2+%d" % (p - 3), "A1^3+%d+%d*r3" % (p - 3, p - 1),
              "A2^3+%d+1*r3" % (p - 3), "2*HW1^2+%d*W1^2" % (p - 3),
              "2*HW2^2+%d*W2^2" % (p - 3), "uW1*W1+%d" % (p - 1),
              "uW2*W2+%d" % (p - 1), "uA*A1+%d*uA*A2+%d"
              % (p - 1, p - 1)]
        wr(os.path.join(HERE, "%s_p%d.ms" % (BASE, p)), p,
           bodyp[p] + tp)
        wr(os.path.join(HERE, "%s_ctl0_p%d.ms" % (BASE, p)), p,
           bodypc[p] + tp)
    # a3-chamber restriction at p105337 (Sol §C: a3 [1] reproduction
    # lane): 38s, tf40, tg40 = 0 hard-substituted; fence tg01_40.
    A3Z = {"tf1_38", "tf2_38", "tg1_38", "tg2_38", "tg01_38",
           "tg02_38", "tf1_40", "tf2_40", "tg1_40", "tg2_40"}
    p = PRIMES[0]
    b3, dead = [], 0
    for lab, v in resid:
        keep = {vk: r for vk, r in v.items()
                if not (vk and any(vars_[i] in A3Z for i in vk))}
        if not keep: dead += 1; continue
        tc = R1.poly_terms(keep, names)
        b3.append(E32.emit_modp(tc, E32.row_scale_terms(tc), p))
    xg = names[next(i for i, nm in enumerate(vars_)
                    if nm == "tg01_40")]
    hdr3 = [h for h in hdr if h not in
            {names[i] for i in occ if vars_[i] in A3Z}] + ["uF0"]
    tp = ["r3^2+%d" % (p - 3), "A1^3+%d+%d*r3" % (p - 3, p - 1),
          "A2^3+%d+1*r3" % (p - 3), "2*HW1^2+%d*W1^2" % (p - 3),
          "2*HW2^2+%d*W2^2" % (p - 3), "uW1*W1+%d" % (p - 1),
          "uW2*W2+%d" % (p - 1), "uA*A1+%d*uA*A2+%d" % (p - 1, p - 1)]
    path3 = os.path.join(HERE, "%s_a3_p%d.ms" % (BASE, p))
    with open(path3, "w") as f:
        f.write(", ".join(hdr3) + "\n%d\n" % p)
        f.write(",\n".join(b3 + tp + ["uF0*%s+%d" % (xg, p - 1)])
                + "\n")
    with open(os.path.join(HERE, BASE + ".rows.txt"), "w") as f:
        f.write("# %s: exact symbolic band elimination (§7.S1)\n"
                % BASE)
        f.write("# pivots (%d): high var <- row\n" % len(st["pivots"]))
        for h, lab in st["pivots"]:
            f.write("#   %s <- Row_%d[eta^%d]\n"
                    % (vars_[h], lab[0], lab[1]))
        for i, (lab, _) in enumerate(resid):
            f.write("eq%d = Row_%d[eta^%d]%s\n"
                    % (i, lab[0], lab[1],
                       "+42" if lab == (20, 0) else ""))
        f.write("# vars (%d): %s\n" % (len(hdrx), " ".join(
            "%s=%s" % (names[i], vars_[i]) for i in occ)))
    print("   emitted: %s.ms %.2f MB char-0; p-lanes x2 + ctl0 x3 + "
          "a3 lane (%d rows survive a3-substitution, %d die); "
          "60 rows, %d terms, max var-degree %d, %d+10 vars"
          % (BASE, sz / 1e6, len(b3), dead, nterm, maxdeg, len(hdrx)),
          flush=True)

# ------------------------------------------------------------- guards
def eval_vex_modp(v, xv, pt, p):
    tot = 0
    for vk, r in v.items():
        m = 1
        for i in vk: m = m * xv[i] % p
        tot = (tot + m * FC.ring_modp(r, pt, p)) % p
    return tot

def replay(rows, pivc, vars_, HIGH, xv, hv, pt, p):
    """independent scalar replay of the SAME pivot sequence: rows as
    (Ah: high->coef, B) pairs mod p; full-row Bareiss updates."""
    num = []
    for lab, v in rows:
        Ah, B = {}, 0
        for vk, r in v.items():
            c = FC.ring_modp(r, pt, p)
            hs = [i for i in vk if i in HIGH]
            m = 1
            for i in vk:
                if i not in HIGH: m = m * xv[i] % p
            if hs: Ah[hs[0]] = (Ah.get(hs[0], 0) + m * c) % p
            else: B = (B + m * c) % p
        num.append([lab, Ah, B])
    used = set()
    for h, plab, cp in pivc:
        pr = next(r for r in num if r[0] == plab)
        used.add(plab)
        cpv = FC.ring_modp(cp, pt, p)
        for r in num:
            if r[0] in used or h not in r[1]: continue
            a = r[1].pop(h)
            nA = {}
            for h2, v2 in r[1].items():
                nA[h2] = v2 * cpv % p
            for h2, v2 in pr[1].items():
                if h2 == h: continue
                nA[h2] = (nA.get(h2, 0) - a * v2) % p
            r[1] = {k2: x for k2, x in nA.items() if x}
            r[2] = (r[2] * cpv - a * pr[2]) % p
    return {r[0]: (r[1], r[2]) for r in num if r[0] not in used}

def phase_guards():
    st = pickle.load(open("/tmp/directionb_compressed.pkl", "rb"))
    resid, vars_, pivc = st["resid"], st["vars"], st["pivc"]
    rows, _ = load_nolog_rows()
    _, names, ordered, blocks, _ = E32.load_rows()
    HIGH = {i for i, nm in enumerate(vars_)
            if nm[:2] in ("tf", "tg") and lvl(nm) >= 43}
    files = [BASE + s for s in
             (".ms", "_ctl0.ms", "_p105337.ms", "_p200257.ms",
              "_ctl0_p105337.ms", "_ctl0_p200257.ms", "_a3_p105337.ms")]
    for fn in files:
        txt = open(os.path.join(HERE, fn)).read()
        assert "(" not in txt and ")" not in txt, fn
    chk("guard A: paren sweep, %d compressed files" % len(files), True)
    LOWIDS = [i for i in names if i not in HIGH]
    okB, okS, okR = True, True, True
    for p in PRIMES:
        pt = FC.radical_point(p)
        hdr, char, eqs = E32.FCparse("%s_p%d.ms" % (BASE, p))
        scales = [E32.row_scale_terms(R1.poly_terms(v, names))
                  for _, v in resid]
        for t in range(3):                 # 2 random + 1 zero-low pt
            rng = random.Random(8100 + p + 7 * t)
            xv = {i: (0 if vars_[i] in PIN42 or t == 2
                      else rng.randrange(1, p)) for i in LOWIDS}
            if t == 2:
                for i in LOWIDS:
                    if vars_[i][:2] not in ("tf", "tg"):
                        xv[i] = rng.randrange(1, p)
            hv = {i: rng.randrange(1, p) for i in HIGH if True}
            rep = replay(rows, pivc, vars_, HIGH, xv, pt, p, )
            # cleanliness: replay residual rows high-free numerically
            okB &= all(not Ah for lab, (Ah, B) in rep.items())
            val = dict(pt, uW1=pow(pt["W1"], p - 2, p),
                       uW2=pow(pt["W2"], p - 2, p),
                       uA=pow((pt["A1"] - pt["A2"]) % p, p - 2, p))
            for i in LOWIDS: val[names[i]] = xv[i]
            for i, (lab, v) in enumerate(resid):
                sym = eval_vex_modp(v, xv, pt, p)
                okB &= (rep[lab][1] == sym)
                got = E32._tiny_parse_eval(eqs[i], val, p)
                okS &= (got == sym * FC.frmod(scales[i], p) % p)
            for e in eqs[len(resid):]:
                okS &= (E32._tiny_parse_eval(e, val, p) == 0)
            # rank samples: A = high-coef matrix of ALL rows; expect
            # rank == #pivots; [A|b] rank +1 iff some compat != 0
            import itertools
            mat = []
            for lab, v in rows:
                Ah, B = {}, 0
                for vk, r in v.items():
                    c = FC.ring_modp(r, pt, p)
                    hs = [i for i in vk if i in HIGH]
                    m = 1
                    for i in vk:
                        if i not in HIGH: m = m * xv[i] % p
                    if hs: Ah[hs[0]] = (Ah.get(hs[0], 0) + m * c) % p
                    else: B = (B + m * c) % p
                mat.append((Ah, B))
            hlist = sorted(HIGH)
            def rank_of(rows2):
                M = [dict(r) for r in rows2]
                rk = 0
                for c in range(len(hlist) + 1):
                    pr2 = next((i for i in range(rk, len(M))
                                if M[i].get(c)), None)
                    if pr2 is None: continue
                    M[rk], M[pr2] = M[pr2], M[rk]
                    inv = pow(M[rk][c], p - 2, p)
                    M[rk] = {k2: x * inv % p for k2, x in M[rk].items()}
                    for i2 in range(len(M)):
                        if i2 != rk and M[i2].get(c):
                            f = M[i2][c]
                            for k2, x in M[rk].items():
                                M[i2][k2] = (M[i2].get(k2, 0)
                                             - f * x) % p
                            M[i2] = {k2: x for k2, x in M[i2].items()
                                     if x}
                    rk += 1
                return rk
            hidx = {h: j for j, h in enumerate(hlist)}
            A_ = [{hidx[h]: x for h, x in Ah.items()}
                  for Ah, B in mat]
            Ab = [dict(r, **{len(hlist): mat[i][1]})
                  if mat[i][1] else dict(r)
                  for i, r in enumerate(A_)]
            rA, rAb = rank_of(A_), rank_of(Ab)
            compat_nz = any(rep[lab][1] for lab in rep
                            if lab[0] >= 12)
            okR &= (rA == len(pivc)) and                 ((rAb == rA + 1) == compat_nz or rAb == rA)
            okR &= (rAb > rA) == compat_nz
    chk("guard B: independent scalar REPLAY of the pivot sequence == "
        "symbolic residual, 2 primes x 3 points (incl. all-lows-0); "
        "replay residuals numerically HIGH-FREE", okB)
    chk("guard B2: emitted strings round-trip (independent parser) == "
        "symbolic values; rad/sat rows vanish at radical points", okS)
    chk("guard E (Sol SC): rank(A) == %d == #pivots at every sample; "
        "rank([A|b]) jumps by 1 EXACTLY when some compatibility "
        "value != 0" % len(pivc), okR)
    # guard D: back-substitution at a random point, both primes:
    # solve the 16 pivot rows for the pivot highs (free highs random),
    # then EVERY original row: pivot rows AND the +42 row (a pivot)
    # vanish; residual originals match compressed up to the tracked
    # per-row scale (cross-point consistency).
    okD = True
    for p in PRIMES:
        pt = FC.radical_point(p)
        ratios = {}
        for t in range(2):
            rng = random.Random(9100 + p + t)
            xv = {i: (0 if vars_[i] in PIN42 else rng.randrange(1, p))
                  for i in LOWIDS}
            free = [h for h in HIGH
                    if h not in {h2 for h2, _, _ in pivc}]
            hv = {h: rng.randrange(1, p) for h in free}
            # linear solve for pivot highs from the pivot rows
            pvars = [h for h, _, _ in pivc]
            pidx = {h: j for j, h in enumerate(pvars)}
            M = []; rhs = []
            origmap = dict(rows)
            for h, plab, cp in pivc:
                v = origmap[plab]
                row = [0] * len(pvars); b = 0
                for vk, r in v.items():
                    c = FC.ring_modp(r, pt, p)
                    hs = [i for i in vk if i in HIGH]
                    m = 1
                    for i in vk:
                        if i not in HIGH: m = m * xv[i] % p
                    if hs:
                        h2 = hs[0]
                        if h2 in pidx: row[pidx[h2]] =                             (row[pidx[h2]] + m * c) % p
                        else: b = (b + m * c * hv[h2]) % p
                    else: b = (b + m * c) % p
                M.append(row); rhs.append((-b) % p)
            n2 = len(pvars)
            for c2 in range(n2):
                pr2 = next(i for i in range(c2, n2) if M[i][c2])
                M[c2], M[pr2] = M[pr2], M[c2]
                rhs[c2], rhs[pr2] = rhs[pr2], rhs[c2]
                inv = pow(M[c2][c2], p - 2, p)
                M[c2] = [x * inv % p for x in M[c2]]
                rhs[c2] = rhs[c2] * inv % p
                for i in range(n2):
                    if i != c2 and M[i][c2]:
                        f = M[i][c2]
                        M[i] = [(a - f * b2) % p
                                for a, b2 in zip(M[i], M[c2])]
                        rhs[i] = (rhs[i] - f * rhs[c2]) % p
            hval = dict(hv)
            for h in pvars: hval[h] = rhs[pidx[h]]
            xall = dict(xv); xall.update(hval)
            for lab, v in rows:
                got = eval_vex_modp(v, xall, pt, p)
                if lab in {pl for _, pl, _ in pivc}:
                    okD &= (got == 0)
                else:
                    sym = eval_vex_modp(dict(resid)[lab], xv, pt, p)
                    key = (p, lab)
                    if got == 0: okD &= (sym == 0)
                    else:
                        rat = sym * pow(got, p - 2, p) % p
                        if key in ratios: okD &= (ratios[key] == rat)
                        else: ratios[key] = rat
    chk("guard D (Sol SC): back-substitution -- pivot-solved highs "
        "kill every pivot row INCLUDING the +42 row exactly; residual "
        "originals match compressed rows up to a constant per-row "
        "scale (cross-point consistent), both primes", okD)
    # guard C (Sol SC): claim-4 seed protocol (pins-adapted, seeds 1
    # and 5): symbolic residual at the seed points == scalar replay.
    okC = True
    p = PRIMES[0]; pt = FC.radical_point(p)
    for seed in (1, 5):
        rng = random.Random(4000 + seed)
        xv = {}
        for i in LOWIDS:
            nm = vars_[i]
            xv[i] = 0 if nm in PIN42 else                 (FC.frmod(Fr(1 + (seed % 5), 2 + (seed % 3)), p)
                 if nm[:2] not in ("tf", "tg") else rng.randrange(1, p))
        rep = replay(rows, pivc, vars_, HIGH, xv, pt, p)
        for lab, v in resid:
            okC &= (rep[lab][1] == eval_vex_modp(v, xv, pt, p))
    chk("guard C (Sol SC): claim-4 seed protocol reproduced (pins-"
        "adapted, seeds 1/5): replay == symbolic on all 60 residual "
        "rows incl. the 32 registered labels", okC)
    # guard F: anchor at lows = 0 -- band rows die, the Row_20-
    # descended obstruction rows stay NONZERO (the -42/w4 content
    # survives compression); ctl0 origin check.
    xv0 = {i: 0 for i in LOWIDS}
    for i in LOWIDS:
        if vars_[i][:2] not in ("tf", "tg"):
            xv0[i] = 7 + i % 5
    p = PRIMES[0]; pt = FC.radical_point(p)
    nz20 = [lab for lab, v in resid
            if lab[0] == 20 and eval_vex_modp(v, xv0, pt, p)]
    band0 = all(eval_vex_modp(v, xv0, pt, p) == 0
                for lab, v in resid if lab[0] in (6, 8, 10))
    chk("guard F: pattern-positive anchor at lows=0 -- all band rows "
        "die, %d/6 Row_20-descended rows NONZERO (the -42/w4 "
        "inhomogeneity survives compression)" % len(nz20),
        band0 and len(nz20) >= 4)
    hdr, _, eqsc = E32.FCparse("%s_ctl0_p%d.ms" % (BASE, PRIMES[0]))
    val0 = dict(pt, uW1=1, uW2=1, uA=1)
    for h in hdr:
        if h.startswith("x"): val0[h] = 0
    val0["uW1"] = pow(pt["W1"], p - 2, p)
    val0["uW2"] = pow(pt["W2"], p - 2, p)
    val0["uA"] = pow((pt["A1"] - pt["A2"]) % p, p - 2, p)
    nc = len([1 for lab, v in resid if any(vk for vk in v)])
    bad = [j for j in range(nc)
           if E32._tiny_parse_eval(eqsc[j], val0, p)]
    chk("guard G: ctl0 satisfiable at the origin (var-part rows all "
        "vanish)", not bad)
    # guard H: a3-chamber samples -- compat values not all zero
    A3Z = {"tf1_38", "tf2_38", "tg1_38", "tg2_38", "tg01_38",
           "tg02_38", "tf1_40", "tf2_40", "tg1_40", "tg2_40"}
    allnz = True
    for t in range(3):
        rng = random.Random(6600 + t)
        xv = {i: (0 if vars_[i] in PIN42 or vars_[i] in A3Z
                  else rng.randrange(1, p)) for i in LOWIDS}
        allnz &= any(eval_vex_modp(v, xv, pt, p)
                     for lab, v in resid)
    chk("guard H: a3-chamber samples (3 pts): the compressed system "
        "does NOT vanish (consistent with the banked a3 GB=[1]; the "
        "emitted _a3 lane is the msolve reproduction)", allnz)


if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "all"
    t0 = time.time()
    if ph in ("elim", "all"): phase_elim()
    if ph in ("emit", "all"): phase_emit()
    if ph in ("guards", "all"): phase_guards()
    bad = [n for n, c in OK if not c]
    print("\nTOTAL: %d checks, %d FAIL %s  (%.1fs)"
          % (len(OK), len(bad), bad or "", time.time() - t0))
