#!/usr/bin/env python3
"""R1 FULL-DEGREE terminal core builder (SHEET6-R1.md sec 8; per
SHEET6-R1-REVIEW.md mandates 1-4). Reuses the r1_experiment engine's
verified staging machinery (orbit model, arc, suborbit Newton) but:
  - VDEG_CAP off (999): G_m-window rows are EXACT at full degree
    (slot budget 20 bounds var-degree; no sentinel can trigger).
  - f^3 / g^2 built as products of per-(orbit,k) BLOCK cubes/squares
    (slot truncation is order-independent: slots >= 0, additive).
  - emission = expanded integer monomial sums only (engine emit_expanded).
  - guard suite: paren sweep, independent-parser mod-p round trip,
    constant census + origin check, random-point residual, direct-product
    validation of the block fast path at full degree.

Phases (each checkpointed, each < ~10 min unless noted):
  --blocks   build exact per-(orbit,k) blocks           -> /tmp/r1full/blocks.pkl
  --check    mod-p full-degree validation vs direct 126/189-factor product
  --foldp    mod-p folds + rows + census + char-p screen emission + sizing
  --foldx    exact folds (tree, checkpointed; the big step)
  --emit     exact rows + char-0 core emission + guards
  --msolve   run msolve (radicals sanity, mod-p screen, char-0; timeouts)
"""
import os, pickle, random, re, subprocess, sys, time
from fractions import Fraction as Fr
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r1_experiment as R1

DEPTH = 54
DG = min(DEPTH - 32, 21)                    # 21: band 1..19 + quotient at 20
STATE_DIR = "/tmp/r1full"
OUT_DIR = "/Users/dc/code/math/jc72108/systems/r1"
_PRIMES = []
def good_primes(n=2, start=60000):
    """first n primes p == 1 mod 84 with a full radical point in GF(p)."""
    p = start - (start - 1) % 84                # p == 1 mod 84
    while p <= start: p += 84
    while len(_PRIMES) < n:
        if (p not in _PRIMES and
                all(p % q for q in range(2, int(p ** .5) + 1)) and
                radical_point(p)):
            _PRIMES.append(p)
        p += 84
    return _PRIMES[:n]
R1.VDEG_CAP = 999                           # full degree; sentinels can't fire
R1.PINS = {}

def log(msg):
    print("[fullcore %s] %s" % (time.strftime("%H:%M:%S"), msg), flush=True)

def save(name, obj):
    os.makedirs(STATE_DIR, exist_ok=True)
    with open(os.path.join(STATE_DIR, name), "wb") as f:
        pickle.dump(obj, f, protocol=4)
def load(name):
    with open(os.path.join(STATE_DIR, name), "rb") as f:
        return pickle.load(f)
def have(name): return os.path.exists(os.path.join(STATE_DIR, name))

# ---------------------------------------------------------------- blocks
def build_orbs():
    R1.reset_vars()
    return R1.build_generators(DEPTH)

def gm_blocks(orbnames, orbs):
    """exact per-(orbit,k) G_m blocks, mirroring gm_jet2 (through-d0 kept
    as one exact block per A-orbit; Delta suborbit-Newton blocks else)."""
    P = {12: R1.vC(R1.RONE)}
    for v in range(len(R1.VARS)):
        if R1.VARS[v]["kind"] == "stretch":
            if R1.VSTAT[v] is None: P[R1.VARS[v]["level"]] = R1.vvar(v)
            elif R1.VSTAT[v]: P[R1.VARS[v]["level"]] = R1.vC(R1.VSTAT[v])
    blocks = []
    for on in orbnames:
        orb = orbs[on]; Y = orb["series"]; n7 = R1.C7SUB[orb["size"]]
        lead = Y.get(12, {}).get((), R1.RZERO)
        Aside = R1.rk3(lead) and R1.rk3(lead)[0] == R1.KONE
        for k in range(7):
            if Aside and k == 0:            # exact through-d0 factors
                blk = R1.JONE
                for j in range(n7):
                    c = 7 * j
                    fac = {(1, 0): R1.vC(R1.RONE)}
                    for lv, vv in Y.items():
                        if lv >= 32 and lv - 32 < DG:
                            tw = R1.vscal(vv, R1.rmono(za=(c * lv) % 42))
                            if tw: fac[(0, lv - 32)] = R1.vscal(tw, R1.K3(-1))
                    blk = R1.jmul(blk, fac, DG)
                blocks.append(((on, "d0"), blk))
                continue
            D = {}
            for s in range(DG):
                lv = 12 + s
                dv = P.get(lv, R1.VZERO)
                yv = Y.get(lv)
                if yv:
                    dv = R1.vadd(dv, R1.vscal(
                        R1.vscal(yv, R1.rmono(za=(k * lv) % 42)), R1.K3(-1)))
                if dv: D[s] = dv
            Dp = {0: {0: R1.vC(R1.RONE)}, 1: D}
            for r in range(2, n7 + 1): Dp[r] = R1.smul(Dp[r - 1], D, DG)
            q = {r: {s: R1.vscal(v, n7) for s, v in Dp[r].items() if s % 6 == 0}
                 for r in range(1, n7 + 1)}
            e = [{0: R1.vC(R1.RONE)}]
            for jj in range(1, n7 + 1):
                acc = {}
                for r in range(1, jj + 1):
                    acc = R1.sadd(acc, R1.sscal(
                        R1.smul(e[jj - r], q[r], DG), R1.K3((-1) ** (r - 1))))
                e.append(R1.sscal(acc, R1.K3(Fr(1, jj))))
            blk = {}
            for i in range(n7 + 1):
                if 20 * i >= DG and i > 0: break
                for s, v in e[n7 - i].items():
                    if s + 20 * i < DG: blk[(i, s + 20 * i)] = v
            blocks.append(((on, k), blk))
    return blocks

def phase_blocks():
    orbs = build_orbs()
    t0 = time.time()
    fb = gm_blocks(R1.FORB, orbs)
    log("f-side blocks: %d (%.1fs)" % (len(fb), time.time() - t0))
    gb = gm_blocks(R1.GORB, orbs)
    log("g-side blocks: %d (%.1fs)" % (len(gb), time.time() - t0))
    for lab, blk in fb + gb:
        for k, v in blk.items():
            assert not any(kk and kk[-1] == R1.HIVAR for kk in v), \
                "sentinel fired at full degree?! %s %s" % (lab, k)
    save("blocks.pkl", dict(f=fb, g=gb, nvars=len(R1.VARS),
                            vmeta=[dict(m) for m in R1.VARS]))
    log("blocks saved (%d vars registered)" % len(R1.VARS))

# ------------------------------------------------- mod-p specialization
_RPT = {}
def radical_point(p, seed=1):
    """consistent radical assignment in GF(p): z (Phi42 root), r3^2=3,
    A1^3=3+r3, A2^3=3-r3, 2EB^7=3, HW_i = sqrt(3/2) W_i, W_i random.
    Cheap power pretests first; brute scans only when they must succeed."""
    if (p, seed) in _RPT: return _RPT[(p, seed)]
    rng = random.Random(seed)
    if (p - 1) % 84 or pow(3, (p - 1) // 2, p) != 1: return None
    inv2 = pow(2, p - 2, p)
    def scan(f):
        return next(x for x in range(1, p) if f(x) % p == 0)
    r3 = scan(lambda x: x * x - 3)
    got = None
    for r3c in (r3, p - r3):
        if pow((3 + r3c) % p, (p - 1) // 3, p) != 1: continue
        if pow((3 - r3c) % p, (p - 1) // 3, p) != 1: continue
        if pow(3 * inv2 % p, (p - 1) // 7, p) != 1: continue
        if pow(3 * inv2 % p, (p - 1) // 2, p) != 1: continue
        got = r3c; break
    if got is None: return None
    r3 = got
    z = next(x for x in range(2, p)
             if pow(x, 42, p) == 1 and all(pow(x, d, p) != 1
                                           for d in (6, 14, 21)))
    A1 = scan(lambda x: pow(x, 3, p) - (3 + r3))
    A2 = scan(lambda x: pow(x, 3, p) - (3 - r3))
    EB = scan(lambda x: 2 * pow(x, 7, p) - 3)
    h32 = scan(lambda x: 2 * x * x - 3)
    W1, W2 = rng.randrange(1, p), rng.randrange(1, p)
    pt = dict(z=z, r3=r3, A1=A1, A2=A2, EB=EB, W1=W1,
              HW1=h32 * W1 % p, W2=W2, HW2=h32 * W2 % p)
    _RPT[(p, seed)] = pt
    return pt

def frmod(q, p):
    q = Fr(q)
    return q.numerator % p * pow(q.denominator % p, p - 2, p) % p

def ring_modp(r, pt, p):
    tot = 0
    for (za, e1, e2, w1, h1, w2, h2, eB), c in r.items():
        m = (pow(pt["z"], za, p) * pow(pt["A1"], e1, p) * pow(pt["A2"], e2, p)
             * pow(pt["W1"], w1, p) * pow(pt["HW1"], h1, p)
             * pow(pt["W2"], w2, p) * pow(pt["HW2"], h2, p)
             * pow(pt["EB"], eB, p)) % p
        tot = (tot + m * (frmod(c[0], p) + frmod(c[1], p) * pt["r3"])) % p
    return tot

def spec_blocks(blocks, pt, p):
    out = []
    for lab, blk in blocks:
        nb = {}
        for key, vex in blk.items():
            nv = {}
            for vk, r in vex.items():
                c = ring_modp(r, pt, p)
                if c: nv[vk] = c
            if nv: nb[key] = nv
        out.append((lab, nb))
    return out

# ------------------------------------------------------- fold machinery
def pvmul(x, y, p):
    out = {}
    for kx, cx in x.items():
        for ky, cy in y.items():
            k = tuple(sorted(kx + ky))
            c = out.get(k, 0) + cx * cy
            out[k] = c % p
    return {k: c for k, c in out.items() if c}
def pjmul(a, b, dg, p):
    out = {}
    for (na, sa), va in a.items():
        for (nb, sb), vb in b.items():
            s = sa + sb
            if s >= dg: continue
            k = (na + nb, s)
            cur = out.get(k)
            if cur is None: cur = out[k] = {}
            for kx, cx in va.items():
                for ky, cy in vb.items():
                    kk = tuple(sorted(kx + ky))
                    c = cur.get(kk, 0) + cx * cy
                    cur[kk] = c % p
    return {k: {kk: c for kk, c in v.items() if c}
            for k, v in out.items()}
def jsize(j): return sum(len(v) for v in j.values())

def tree_fold(blocks, mul, tag, ckname=None):
    """balanced product; checkpoint pairs level by level."""
    layer = list(blocks); lvl = 0
    if ckname and have(ckname):
        lvl, layer = load(ckname); log("resume %s at level %d" % (tag, lvl))
    t0 = time.time()
    while len(layer) > 1:
        layer.sort(key=jsize)                # pair small with small
        nxt = []
        for i in range(0, len(layer) - 1, 2):
            nxt.append(mul(layer[i], layer[i + 1]))
        if len(layer) % 2: nxt.append(layer[-1])
        lvl += 1; layer = nxt
        log("%s: level %d -> %d nodes, sizes %s (%.1fs)"
            % (tag, lvl, len(layer), [jsize(x) for x in layer][:8],
               time.time() - t0))
        if ckname: save(ckname, (lvl, layer))
    return layer[0]

def jpow(blk, e, mul):
    out = blk
    for _ in range(e - 1): out = mul(out, blk)
    return out

# ------------------------------------------------------------- rows
def qpat_coeffs():
    pat = R1.eta_poly_ref([(R1.A1c, 2), (R1.A2c, 2)], R1.K1)
    _, pm = R1.k3poly_pow_pattern()
    return pm(pm([R1.K0, R1.K1], pat), [-R1.Bc, R1.K0, R1.K0, R1.K1])

def gm_rows(jf, jg, WG, scal, add):
    """[(label, row)] for the full G_m family. scal(v, K3), add(v, v)."""
    qp = qpat_coeffs()
    rows = []
    for tag, jet in (("C1-Gm-f", jf), ("C1-Gm-g", jg)):
        for (n, s), v in sorted(jet.items()):
            if s % 2 == 1 and v: rows.append(((tag, n, s), v))
    for (n, s), v in sorted(WG.items()):
        if 1 <= s <= 19 and v: rows.append((("WG-band", n, s), v))
        if s == 0 and v: rows.append((("WG-slot0(must-be-0)", n, 0), v))
    lead = WG.get((16, 20), {})
    for n in range(0, 17):
        v = WG.get((n, 20), {})
        r = add(scal(v, qp[16]),
                scal(lead, -qp[n]) if not R1.mk(qp[n]).iszero() else {})
        if r: rows.append((("WG-quot", n, 20), r))
    for (n, s), v in sorted(WG.items()):
        if s == 20 and n > 16 and v: rows.append((("WG-quot-deg", n, 20), v))
    return rows

def pscal(v, c, p):
    out = {}
    for k, x in v.items():
        y = x * c % p
        if y: out[k] = y
    return out
def padd(x, y, p):
    out = dict(x)
    for k, c in y.items():
        c2 = (out.get(k, 0) + c) % p
        if c2: out[k] = c2
        elif k in out: del out[k]
    return out

# --------------------------------------------------------- direct check
def eval_vex_modp(vex, pt, p, xval):
    tot = 0
    for vk, r in vex.items():
        m = ring_modp(r, pt, p)
        for vid in vk: m = m * xval[vid] % p
        tot = (tot + m) % p
    return tot

def direct_jet_modp(orbnames, orbs, pt, p, xval):
    """the SLOW-path gm_jet product (per-factor, no suborbit Newton),
    evaluated numerically mod p — independent of the block machinery."""
    P = {12: 1}
    for v in range(len(R1.VARS)):
        if R1.VARS[v]["kind"] == "stretch": P[R1.VARS[v]["level"]] = xval[v]
    Z = pt["z"]
    jp = {(0, 0): 1}
    def num(vex): return eval_vex_modp(vex, pt, p, xval)
    for on in orbnames:
        orb = orbs[on]; Y = orb["series"]; n7 = R1.C7SUB[orb["size"]]
        lead = Y.get(12, {}).get((), R1.RZERO)
        Aside = R1.rk3(lead) and R1.rk3(lead)[0] == R1.KONE
        for k in range(7):
            for j in range(n7):
                c = (k + 7 * j) % 42
                fac = {}
                if Aside and k == 0:
                    fac[(1, 0)] = 1
                    for lv, vv in Y.items():
                        if lv >= 32 and lv - 32 < DG:
                            fac[(0, lv - 32)] = (fac.get((0, lv - 32), 0)
                                - pow(Z, c * lv % 42, p) * num(vv)) % p
                else:
                    if 20 < DG: fac[(1, 20)] = 1
                    for s in range(DG):
                        lv = 12 + s
                        t = P.get(lv, 0)
                        yv = Y.get(lv)
                        if yv: t = (t - pow(Z, c * lv % 42, p) * num(yv)) % p
                        if t: fac[(0, s)] = t % p
                out = {}
                for (na, sa), ca in jp.items():
                    for (nb, sb), cb in fac.items():
                        if sa + sb >= DG: continue
                        kk = (na + nb, sa + sb)
                        out[kk] = (out.get(kk, 0) + ca * cb) % p
                jp = {kk: c for kk, c in out.items() if c}
    return jp

def phase_check():
    st = load("blocks.pkl")
    orbs = build_orbs()
    assert len(R1.VARS) == st["nvars"], "var registry drift"
    for p in good_primes(2):
        pt = radical_point(p)
        rng = random.Random(p)
        xval = {v: rng.randrange(1, p) for v in range(len(R1.VARS))}
        for side, names in (("f", R1.FORB), ("g", R1.GORB)):
            sb = spec_blocks(st[side], pt, p)
            jet = tree_fold([b for _, b in sb],
                            lambda a, b: pjmul(a, b, DG, p), "chk-" + side)
            direct = direct_jet_modp(names, orbs, pt, p, xval)
            keys = set(jet) | set(direct)
            bad = []
            for kk in keys:
                a = eval_vex_modp_int(jet.get(kk, {}), xval, p)
                b = direct.get(kk, 0)
                if a != b: bad.append((kk, a, b))
            log("check p=%d side=%s: %d keys, %d mismatches"
                % (p, side, len(keys), len(bad)))
            assert not bad, ("FAST PATH MISMATCH", p, side, bad[:5])
    log("CHECK PASS: block fold == direct 126/189-factor product "
        "(full degree, both primes)")

def eval_vex_modp_int(nv, xval, p):
    tot = 0
    for vk, c in nv.items():
        m = c
        for vid in vk: m = m * xval[vid] % p
        tot = (tot + m) % p
    return tot

# ------------------------------------------------------------ mod-p fold
def phase_foldp():
    st = load("blocks.pkl")
    p = good_primes(1)[0]
    pt = radical_point(p)
    log("mod-p fold, p=%d, radical point ok" % p)
    mul = lambda a, b: pjmul(a, b, DG, p)
    fb = spec_blocks(st["f"], pt, p); gb = spec_blocks(st["g"], pt, p)
    jf = tree_fold([b for _, b in fb], mul, "jf")
    save("pjf.pkl", jf); log("jf entries: %d" % jsize(jf))
    jg = tree_fold([b for _, b in gb], mul, "jg")
    save("pjg.pkl", jg); log("jg entries: %d" % jsize(jg))
    f3 = tree_fold([jpow(b, 3, mul) for _, b in fb], mul, "f3", "pf3.ck")
    save("pf3.pkl", f3); log("f3 entries: %d" % jsize(f3))
    g2 = tree_fold([jpow(b, 2, mul) for _, b in gb], mul, "g2", "pg2.ck")
    save("pg2.pkl", g2); log("g2 entries: %d" % jsize(g2))
    WG = {}
    for k in set(f3) | set(g2):
        v = padd(g2.get(k, {}), pscal(f3.get(k, {}), p - 1, p), p)
        if v: WG[k] = v
    save("pWG.pkl", WG); log("WG entries: %d over %d keys" % (jsize(WG), len(WG)))
    qp = qpat_coeffs()
    rows = gm_rows(jf, jg, WG,
                   lambda v, c: pscal(v, ring_modp(R1.rC(c), pt, p) if not
                                      isinstance(c, int) else c, p),
                   lambda a, b: padd(a, b, p))
    save("prows.pkl", (p, pt, rows))
    census(rows, "mod-p")
    emit_modp(rows, p, pt, st)

def census(rows, tag):
    fams = {}
    const_rows = 0
    for (fam, n, s), v in rows:
        fams[fam] = fams.get(fam, 0) + 1
        if () in v: const_rows += 1
    log("%s census: %d rows: %s; rows with constant term: %d"
        % (tag, len(rows), sorted(fams.items()), const_rows))
    return const_rows

def emit_modp(rows, p, pt, st):
    allv = sorted({vid for _, v in rows for vk in v for vid in vk})
    names = {vid: "x%d" % i for i, vid in enumerate(allv)}
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "r1_full_core_modp.ms")
    with open(path, "w") as f:
        f.write(", ".join(names[v] for v in allv) + "\n%d\n" % p)
        eqs = []
        for (fam, n, s), v in rows:
            terms = []
            for vk in sorted(v):
                xs = []
                for vid in sorted(set(vk)):
                    e = vk.count(vid)
                    xs.append(names[vid] if e == 1 else
                              "%s^%d" % (names[vid], e))
                mono = "*".join(xs)
                c = v[vk]
                terms.append("%d*%s" % (c, mono) if mono else "%d" % c)
            eqs.append("+".join(terms))
        f.write(",\n".join(eqs) + "\n")
    meta = os.path.join(OUT_DIR, "r1_full_core_modp.rows.txt")
    with open(meta, "w") as f:
        f.write("# mod-p screen core: p=%d, radical point %s\n" % (p, pt))
        for i, ((fam, n, s), v) in enumerate(rows):
            f.write("eq%d = %s n=%d s=%d (%d terms)\n"
                    % (i, fam, n, s, len(v)))
        for vid in allv:
            f.write("%s = %s (level %d)\n" % (names[vid],
                    st["vmeta"][vid]["name"], st["vmeta"][vid]["level"]))
    log("emitted %s (%d eqs, %d vars, %.1f MB)"
        % (path, len(rows), len(allv), os.path.getsize(path) / 1e6))

def jconv(a, b, p):
    out = {}
    for (na, sa), ca in a.items():
        for (nb, sb), cb in b.items():
            if sa + sb >= DG: continue
            k = (na + nb, sa + sb)
            out[k] = (out.get(k, 0) + ca * cb) % p
    return {k: c for k, c in out.items() if c}

def phase_xcheck():
    """folded powers == plain-jet powers, numerically mod p."""
    st = load("blocks.pkl")
    p = good_primes(1)[0]
    rng = random.Random(31)
    xval = {v: rng.randrange(1, p) for v in range(st["nvars"])}
    def num(name):
        j = load(name)
        d = {k: eval_vex_modp_int(v, xval, p) for k, v in j.items()}
        return {k: c for k, c in d.items() if c}
    njf, njg = num("pjf.pkl"), num("pjg.pkl")
    nf3, ng2 = num("pf3.pkl"), num("pg2.pkl")
    assert jconv(jconv(njf, njf, p), njf, p) == nf3, "f3 fold != (jet f)^3"
    assert jconv(njg, njg, p) == ng2, "g2 fold != (jet g)^2"
    log("XCHECK PASS: folded f^3 == jf^3, g^2 == jg^2 (numeric, p=%d)" % p)

def phase_qcheck():
    """prefix-only (x=0) slot-20 diagnosis via the INDEPENDENT direct
    product: is WG(n,20)|prefix proportional to qpat? Which n fail?"""
    st = load("blocks.pkl")
    orbs = build_orbs()
    qp = qpat_coeffs()
    for p in good_primes(2):
        pt = radical_point(p)
        x0 = {v: 0 for v in range(st["nvars"])}
        djf = direct_jet_modp(R1.FORB, orbs, pt, p, x0)
        djg = direct_jet_modp(R1.GORB, orbs, pt, p, x0)
        f3 = jconv(jconv(djf, djf, p), djf, p)
        g2 = jconv(djg, djg, p)
        WG = {k: (g2.get(k, 0) - f3.get(k, 0)) % p for k in set(g2) | set(f3)}
        WG = {k: c for k, c in WG.items() if c}
        band = sorted(k for k in WG if 1 <= k[1] <= 19)
        log("qcheck p=%d: prefix band slots 1..19 nonzero keys: %s"
            % (p, band[:10] or "NONE (vanishing confirmed)"))
        s20 = {n: WG.get((n, 20), 0) for n in range(0, 40)}
        qpv = [ring_modp(R1.rC(c), pt, p) for c in qp]
        H = s20[16] * pow(qpv[16], p - 2, p) % p if s20[16] else None
        bad = []
        for n in range(0, 40):
            want = H * qpv[n] % p if (H is not None and n < len(qpv)) else 0
            if (s20[n] - want) % p: bad.append(n)
        log("qcheck p=%d: slot-20 prefix vs H*qpat (H=%s): mismatch n = %s"
            % (p, H, bad or "NONE (proportional)"))
        # compare vs folded WG constants
        if have("pWG.pkl") and p == good_primes(1)[0]:
            fWG = load("pWG.pkl")
            mm = [k for k in set(WG) | set(fWG)
                  if WG.get(k, 0) != fWG.get(k, {}).get((), 0)]
            log("qcheck p=%d: direct-prefix vs folded-WG ()-parts: "
                "%d mismatches %s" % (p, len(mm), mm[:6]))

# ----------------------------- ring-mod-p fold + CRT rational recovery
# Coefficients: ring elems {ringkey: (u,v) mod p} (K3 pair mod p); ring
# monomial keys stay SYMBOLIC, so CRT over several primes recovers the
# exact char-0 ring coefficients (verified vs a fresh prime + the
# scalar-specialized folds). rnorm semantics reimplemented mod p.
def k3p_mul(a, b, p):
    return ((a[0] * b[0] + 3 * a[1] * b[1]) % p,
            (a[0] * b[1] + a[1] * b[0]) % p)
def make_ringp(p):
    inv2 = pow(2, p - 2, p)
    TH = (3 * inv2 % p, 0)                   # 3/2
    A1P, A2P = (3, 1), (3, p - 1)            # 3 +- sqrt3
    ZREDP = [{j: (frmod(c, p), 0) for j, c in d.items()} for d in R1.ZRED]
    memo = {}
    def rnorm_key(key):
        """c-independent reduction of a raw monomial key: cached
        tuple of (canonical key, K3p factor)."""
        r = memo.get(key)
        if r is None:
            za, e1, e2, w1, h1, w2, h2, eB = key
            c = (1, 0)
            q, h1 = divmod(h1, 2)
            for _ in range(q): c = k3p_mul(c, TH, p); w1 += 2
            q, h2 = divmod(h2, 2)
            for _ in range(q): c = k3p_mul(c, TH, p); w2 += 2
            q, e1 = divmod(e1, 3)
            for _ in range(q): c = k3p_mul(c, A1P, p)
            q, e2 = divmod(e2, 3)
            for _ in range(q): c = k3p_mul(c, A2P, p)
            q, eB = divmod(eB, 7)
            for _ in range(q): c = k3p_mul(c, TH, p)
            r = tuple(((j, e1, e2, w1, h1, w2, h2, eB), k3p_mul(c, zc, p))
                      for j, zc in ZREDP[za % 42].items())
            memo[key] = r
        return r
    def rmul_p(x, y):
        out = {}
        for kx, cx in x.items():
            for ky, cy in y.items():
                c = k3p_mul(cx, cy, p)
                for k2, zc in rnorm_key(tuple(a + b
                                              for a, b in zip(kx, ky))):
                    c2 = k3p_mul(c, zc, p)
                    cur = out.get(k2)
                    if cur is None: out[k2] = c2
                    else:
                        s = ((cur[0] + c2[0]) % p, (cur[1] + c2[1]) % p)
                        if s == (0, 0): del out[k2]
                        else: out[k2] = s
        return out
    return rmul_p
def ring_to_p(r, p):
    return {k: (frmod(c[0], p), frmod(c[1], p)) for k, c in r.items()}
def blocks_to_p(blocks, p):
    return [(lab, {key: {vk: ring_to_p(r, p) for vk, r in vex.items()}
                   for key, vex in blk.items()}) for lab, blk in blocks]
def rjmul_p(a, b, p, rmul_p):
    out = {}
    for (na, sa), va in a.items():
        for (nb, sb), vb in b.items():
            s = sa + sb
            if s >= DG: continue
            k = (na + nb, s)
            cur = out.get(k)
            if cur is None: cur = out[k] = {}
            for kx, rx in va.items():
                for ky, ry in vb.items():
                    kk = tuple(sorted(kx + ky))
                    pr = rmul_p(rx, ry)
                    c0 = cur.get(kk)
                    if c0 is None: cur[kk] = pr
                    else:
                        for rk, rc in pr.items():
                            v0 = c0.get(rk)
                            if v0 is None: c0[rk] = rc
                            else:
                                sm = ((v0[0] + rc[0]) % p, (v0[1] + rc[1]) % p)
                                if sm == (0, 0): del c0[rk]
                                else: c0[rk] = sm
    return {k: {kk: r for kk, r in v.items() if r}
            for k, v in out.items()}

# --- pointwise-z variant: ring elems {tail7: 24-int list} where the z
# dimension is EVALUATED at the 12 Phi42 roots mod p (pointwise mult, no
# convolution/reduction); (u,v) K3 pairs interleaved [u0,v0,u1,v1,...].
# Converted back to the za-polynomial basis at fold end (inverse
# Vandermonde), so downstream pickles/CRT are unchanged.
def phi42_roots(p):
    assert (p - 1) % 42 == 0, "need p == 1 mod 42"
    rng = random.Random(p)
    while True:
        y = pow(rng.randrange(2, p), (p - 1) // 42, p)
        if y != 1 and all(pow(y, d, p) != 1 for d in (6, 14, 21)):
            break
    ks = (1, 5, 11, 13, 17, 19, 23, 25, 29, 31, 37, 41)
    rs = [pow(y, k, p) for k in ks]
    assert len(set(rs)) == 12
    return rs
CRTV_PRIMES = []
def crt_primes_v(n):
    p = (1 << 29) + 1
    p += (42 - (p - 1) % 42) % 42            # p == 1 mod 42
    if CRTV_PRIMES: p = CRTV_PRIMES[-1] + 42
    while len(CRTV_PRIMES) < n:
        if (p not in CRTV_PRIMES and p % 5 and
                all(p % q for q in range(2, int(p ** .5) + 1))):
            CRTV_PRIMES.append(p)
        p += 42
    return CRTV_PRIMES[:n]
def make_ringpv(p):
    roots = phi42_roots(p)
    inv2 = pow(2, p - 2, p)
    TH = (3 * inv2 % p, 0)
    A1P, A2P = (3, 1), (3, p - 1)
    tmemo = {}
    def tail_reduce(t):
        r = tmemo.get(t)
        if r is None:
            e1, e2, w1, h1, w2, h2, eB = t
            c = (1, 0)
            q, h1 = divmod(h1, 2)
            for _ in range(q): c = k3p_mul(c, TH, p); w1 += 2
            q, h2 = divmod(h2, 2)
            for _ in range(q): c = k3p_mul(c, TH, p); w2 += 2
            q, e1 = divmod(e1, 3)
            for _ in range(q): c = k3p_mul(c, A1P, p)
            q, e2 = divmod(e2, 3)
            for _ in range(q): c = k3p_mul(c, A2P, p)
            q, eB = divmod(eB, 7)
            for _ in range(q): c = k3p_mul(c, TH, p)
            r = ((e1, e2, w1, h1, w2, h2, eB), c)
            tmemo[t] = r
        return r
    def rmul_v(x, y):
        out = {}
        for tx, vx in x.items():
            for ty, vy in y.items():
                t2, (cu, cv) = tail_reduce(tuple(a + b
                                                 for a, b in zip(tx, ty)))
                cur = out.get(t2)
                if cur is None: cur = out[t2] = [0] * 24
                for j in range(0, 24, 2):
                    xu = vx[j]; xv = vx[j + 1]
                    yu = vy[j]; yv = vy[j + 1]
                    pu = (xu * yu + 3 * xv * yv) % p
                    pv = (xu * yv + xv * yu) % p
                    if cu != 1 or cv != 0:
                        pu, pv = ((pu * cu + 3 * pv * cv) % p,
                                  (pu * cv + pv * cu) % p)
                    cur[j] = (cur[j] + pu) % p
                    cur[j + 1] = (cur[j + 1] + pv) % p
        return {t: v for t, v in out.items() if any(v)}
    return roots, rmul_v
def ring_to_pv(r, p, roots):
    out = {}
    for (za, e1, e2, w1, h1, w2, h2, eB), c in r.items():
        t = (e1, e2, w1, h1, w2, h2, eB)
        cur = out.get(t)
        if cur is None: cur = out[t] = [0] * 24
        u, v = frmod(c[0], p), frmod(c[1], p)
        for j, rt in enumerate(roots):
            s = pow(rt, za, p)
            cur[2 * j] = (cur[2 * j] + u * s) % p
            cur[2 * j + 1] = (cur[2 * j + 1] + v * s) % p
    return {t: v for t, v in out.items() if any(v)}
def pv_to_zbasis(vec, p, vinv):
    """24-int pointwise vector -> {za: (u,v)} via inverse Vandermonde."""
    out = {}
    for za in range(12):
        row = vinv[za]
        u = v = 0
        for j in range(12):
            u += row[j] * vec[2 * j]
            v += row[j] * vec[2 * j + 1]
        u %= p; v %= p
        if u or v: out[za] = (u, v)
    return out
def matinv_p(M, p):
    n = len(M)
    A = [row[:] + [1 if k == i else 0 for k in range(n)]
         for i, row in enumerate(M)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] % p)
        A[col], A[piv] = A[piv], A[col]
        inv = pow(A[col][col], p - 2, p)
        A[col] = [x * inv % p for x in A[col]]
        for r in range(n):
            if r != col and A[r][col]:
                f = A[r][col]
                A[r] = [(x - f * y) % p for x, y in zip(A[r], A[col])]
    return [row[n:] for row in A]
def vandermonde_inv(p, roots):
    """inverse of V with V[j][i] = roots[j]^i (values v = V c)."""
    n = len(roots)
    V = [[pow(roots[j], i, p) for i in range(n)] for j in range(n)]
    return matinv_p(V, p)
def phase_fixz(only=None):
    """repair pickles written with the transposed Vandermonde: stored =
    (V^-1)^T V c  =>  c = V^-1 V^T stored. Self-tested per prime."""
    for i, p in enumerate(crt_primes_v(12)):
        if only is not None and i != only: continue
        if not have("cWG.%d.pkl" % p) or have("fixz.%d.done" % p): continue
        roots = phi42_roots(p)
        n = 12
        V = [[pow(roots[j], k, p) for k in range(n)] for j in range(n)]
        Vinv = matinv_p(V, p)
        VT = [[V[j][k] for j in range(n)] for k in range(n)]
        def mm(A, B):
            return [[sum(A[r][k] * B[k][c] for k in range(n)) % p
                     for c in range(n)] for r in range(n)]
        T = mm(Vinv, VT)
        # self-test: simulate the bug on a random vector, T must undo it
        rng = random.Random(p)
        c0 = [rng.randrange(p) for _ in range(n)]
        v = [sum(V[j][k] * c0[k] for k in range(n)) % p for j in range(n)]
        VinvT = [[Vinv[k][r] for k in range(n)] for r in range(n)]
        stored = [sum(VinvT[r][j] * v[j] for j in range(n)) % p
                  for r in range(n)]
        fixed = [sum(T[r][k] * stored[k] for k in range(n)) % p
                 for r in range(n)]
        assert fixed == c0, "fixz self-test failed for p=%d" % p
        W = load("cWG.%d.pkl" % p)
        W2 = {}
        for key, vex in W.items():
            nv = {}
            for vk, r in vex.items():
                tails = {}
                for (za, e1, e2, w1, h1, w2, h2, eB), (u, v_) in r.items():
                    t = (e1, e2, w1, h1, w2, h2, eB)
                    cur = tails.setdefault(t, [[0] * n, [0] * n])
                    cur[0][za] = u; cur[1][za] = v_
                rr = {}
                for t, (uv0, uv1) in tails.items():
                    fu = [sum(T[r_][k] * uv0[k] for k in range(n)) % p
                          for r_ in range(n)]
                    fv = [sum(T[r_][k] * uv1[k] for k in range(n)) % p
                          for r_ in range(n)]
                    for za in range(n):
                        if fu[za] or fv[za]:
                            rr[(za,) + t] = (fu[za], fv[za])
                if rr: nv[vk] = rr
            if nv: W2[key] = nv
        save("cWG.%d.pkl" % p, W2)
        open(os.path.join(STATE_DIR, "fixz.%d.done" % p), "w").write("1")
        log("fixz done p=%d (%d entries)" % (p, jsize(W2)))

def rjmul_v(a, b, p, rmul_v):
    """jet product for the pointwise-z representation (values 24-lists)."""
    out = {}
    for (na, sa), va in a.items():
        for (nb, sb), vb in b.items():
            s = sa + sb
            if s >= DG: continue
            k = (na + nb, s)
            cur = out.get(k)
            if cur is None: cur = out[k] = {}
            for kx, rx in va.items():
                for ky, ry in vb.items():
                    kk = tuple(sorted(kx + ky))
                    pr = rmul_v(rx, ry)
                    c0 = cur.get(kk)
                    if c0 is None: cur[kk] = pr
                    else:
                        for t, vec in pr.items():
                            v0 = c0.get(t)
                            if v0 is None: c0[t] = vec
                            else:
                                for j in range(24):
                                    v0[j] = (v0[j] + vec[j]) % p
    o2 = {}
    for k, v in out.items():
        nv = {}
        for kk, r in v.items():
            rr = {t: vec for t, vec in r.items() if any(vec)}
            if rr: nv[kk] = rr
        if nv: o2[k] = nv
    return o2

def phase_foldv(nprimes=12, only=None):
    """pointwise-z per-prime fold; output converted to za-basis so the
    cWG.<p>.pkl format matches phase_foldc exactly."""
    st = load("blocks.pkl")
    if only is not None: nprimes = max(nprimes, only + 1)
    for i, p in enumerate(crt_primes_v(nprimes)):
        if only is not None and i != only: continue
        if have("cWG.%d.pkl" % p): continue
        t0 = time.time()
        roots, rmul_v = make_ringpv(p)
        mul = lambda a, b: rjmul_v(a, b, p, rmul_v)
        def conv_blocks(blocks):
            return [(lab, {key: {vk: ring_to_pv(r, p, roots)
                                 for vk, r in vex.items()}
                           for key, vex in blk.items()})
                    for lab, blk in blocks]
        fb = conv_blocks(st["f"]); gb = conv_blocks(st["g"])
        # per-stage checkpoints (kill-resume; numeric path unchanged)
        if have("vf3.%d.pkl" % p): f3 = load("vf3.%d.pkl" % p)
        else:
            f3 = fold_seq([jpow(b, 3, mul) for _, b in fb], mul, "vf3.%d" % i)
            save("vf3.%d.pkl" % p, f3)
        if have("vg2.%d.pkl" % p): g2 = load("vg2.%d.pkl" % p)
        else:
            g2 = fold_seq([jpow(b, 2, mul) for _, b in gb], mul, "vg2.%d" % i)
            save("vg2.%d.pkl" % p, g2)
        WG = {}
        for k in set(f3) | set(g2):
            v = {}
            for vk in set(f3.get(k, {})) | set(g2.get(k, {})):
                r = {t: vec[:] for t, vec in g2.get(k, {}).get(vk, {}).items()}
                for t, vec in f3.get(k, {}).get(vk, {}).items():
                    cur = r.get(t)
                    if cur is None: cur = r[t] = [0] * 24
                    for j in range(24): cur[j] = (cur[j] - vec[j]) % p
                r = {t: vec for t, vec in r.items() if any(vec)}
                if r: v[vk] = r
            if v: WG[k] = v
        vinv = vandermonde_inv(p, roots)
        WGz = {}
        for k, vex in WG.items():
            nv = {}
            for vk, r in vex.items():
                rr = {}
                for (e1, e2, w1, h1, w2, h2, eB), vec in r.items():
                    for za, uv in pv_to_zbasis(vec, p, vinv).items():
                        rr[(za, e1, e2, w1, h1, w2, h2, eB)] = uv
                if rr: nv[vk] = rr
            if nv: WGz[k] = nv
        save("cWG.%d.pkl" % p, WGz)
        log("pointwise-z WG done p=%d (%d/%d, %.1fs, %d entries)"
            % (p, i + 1, nprimes, time.time() - t0, jsize(WGz)))

def phase_foldv2(nprimes=8, only=None):
    """pointwise-z per-prime F2 = fold of f-block squares (za-basis out,
    cF2.<p>.pkl, same prime family as phase_foldv)."""
    st = load("blocks.pkl")
    if only is not None: nprimes = max(nprimes, only + 1)
    for i, p in enumerate(crt_primes_v(nprimes)):
        if only is not None and i != only: continue
        if have("cF2.%d.pkl" % p): continue
        t0 = time.time()
        roots, rmul_v = make_ringpv(p)
        mul = lambda a, b: rjmul_v(a, b, p, rmul_v)
        fb = [(lab, {key: {vk: ring_to_pv(r, p, roots)
                           for vk, r in vex.items()}
                     for key, vex in blk.items()}) for lab, blk in st["f"]]
        F2 = fold_seq([jpow(b, 2, mul) for _, b in fb], mul, "vF2.%d" % i)
        vinv = vandermonde_inv(p, roots)
        F2z = {}
        for k, vex in F2.items():
            nv = {}
            for vk, r in vex.items():
                rr = {}
                for (e1, e2, w1, h1, w2, h2, eB), vec in r.items():
                    for za, uv in pv_to_zbasis(vec, p, vinv).items():
                        rr[(za, e1, e2, w1, h1, w2, h2, eB)] = uv
                if rr: nv[vk] = rr
            if nv: F2z[k] = nv
        save("cF2.%d.pkl" % p, F2z)
        log("pointwise-z F2 done p=%d (%d/%d, %.1fs, %d entries)"
            % (p, i + 1, nprimes, time.time() - t0, jsize(F2z)))

CRT_PRIMES = []
def crt_primes(n):
    p = (1 << 29) + 1
    while len(CRT_PRIMES) < n:
        p += 2
        while not all(p % q for q in range(3, int(p ** .5) + 1, 2)): p += 2
        if p % 2 and p % 3 and p % 5 and p % 7: CRT_PRIMES.append(p)
    return CRT_PRIMES[:n]

def fold_seq(blocks, mul, tag):
    """sequential dense-x-sparse chain (the cheap shape: the growing
    partial multiplies one SPARSE low-density block at a time)."""
    acc = blocks[0]
    t0 = time.time()
    for i, b in enumerate(blocks[1:], 1):
        acc = mul(acc, b)
        if i % 5 == 0 or i == len(blocks) - 1:
            log("%s: %d/%d blocks, %d entries (%.1fs)"
                % (tag, i + 1, len(blocks), jsize(acc), time.time() - t0))
    return acc

def phase_foldc(nprimes=12, only=None):
    st = load("blocks.pkl")
    for i, p in enumerate(crt_primes(nprimes)):
        if only is not None and i != only: continue
        if have("cWG.%d.pkl" % p): continue
        t0 = time.time()
        rmul_p = make_ringp(p)
        mul = lambda a, b: rjmul_p(a, b, p, rmul_p)
        fb = blocks_to_p(st["f"], p); gb = blocks_to_p(st["g"], p)
        f3 = fold_seq([jpow(b, 3, mul) for _, b in fb], mul, "cf3.%d" % i)
        g2 = fold_seq([jpow(b, 2, mul) for _, b in gb], mul, "cg2.%d" % i)
        WG = {}
        for k in set(f3) | set(g2):
            v = {}
            for vk in set(f3.get(k, {})) | set(g2.get(k, {})):
                r = dict(g2.get(k, {}).get(vk, {}))
                for rk, rc in f3.get(k, {}).get(vk, {}).items():
                    v0 = r.get(rk, (0, 0))
                    sm = ((v0[0] - rc[0]) % p, (v0[1] - rc[1]) % p)
                    if sm == (0, 0): r.pop(rk, None)
                    else: r[rk] = sm
                if r: v[vk] = r
            if v: WG[k] = v
        save("cWG.%d.pkl" % p, WG)
        log("ring-mod-p WG done p=%d (%d/%d, %.1fs, %d entries)"
            % (p, i + 1, nprimes, time.time() - t0, jsize(WG)))

def phase_foldc2(only=None):
    st = load("blocks.pkl")
    for i, p in enumerate(crt_primes(8)):
        if only is not None and i != only: continue
        if have("cF2.%d.pkl" % p): continue
        t0 = time.time()
        rmul_p = make_ringp(p)
        mul = lambda a, b: rjmul_p(a, b, p, rmul_p)
        fb = blocks_to_p(st["f"], p)
        F2 = fold_seq([jpow(b, 2, mul) for _, b in fb], mul, "cF2.%d" % i)
        save("cF2.%d.pkl" % p, F2)
        log("ring-mod-p F2 done p=%d (%.1fs, %d entries)"
            % (p, time.time() - t0, jsize(F2)))

def ratrec(a, M):
    """rational reconstruction of a mod M (|num|,|den| <= sqrt(M/2))."""
    a %= M
    r0, r1 = M, a
    s0, s1 = 0, 1
    bound = int((M // 2) ** .5)
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if r1 > bound or abs(s1) > bound or s1 == 0: return None
    if gcd(r1, abs(s1)) != 1 and gcd(gcd(r1, abs(s1)), M) != 1: return None
    return Fr(r1, s1) if s1 > 0 else Fr(-r1, -s1)

def phase_crt(prefix="cWG", outname="xWG.pkl", scalar_check="pWG.pkl"):
    """CRT + rational reconstruction of an exact object from
    <prefix>.<p>.pkl files, verified against (a) one held-out prime,
    (b) optionally the scalar mod-p fold."""
    import glob
    files = sorted(glob.glob(os.path.join(STATE_DIR, prefix + ".*.pkl")))
    ps = sorted(int(f.split(".")[-2]) for f in files)
    assert len(ps) >= 3, "need >= 3 CRT primes"
    hold = ps[-1]; use = ps[:-1]
    log("CRT %s over %d primes, holdout %d" % (prefix, len(use), hold))
    Ws = {p: load("%s.%d.pkl" % (prefix, p)) for p in ps}
    M = 1
    for p in use: M *= p
    minv = {p: (M // p, pow(M // p % p, p - 2, p)) for p in use}
    keys = set()
    for p in use: keys |= set(Ws[p])
    WG = {}
    fails = 0
    for k in keys:
        vex = {}
        vks = set()
        for p in use: vks |= set(Ws[p].get(k, {}))
        for vk in vks:
            rr = {}
            rks = set()
            for p in use: rks |= set(Ws[p].get(k, {}).get(vk, {}))
            for rk in rks:
                uv = []
                for comp in (0, 1):
                    x = 0
                    for p in use:
                        c = Ws[p].get(k, {}).get(vk, {}).get(rk, (0, 0))[comp]
                        Mi, Ii = minv[p]
                        x = (x + c * Ii % p * Mi) % M
                    q = ratrec(x, M)
                    if q is None: fails += 1; q = Fr(0)
                    uv.append(q)
                if uv[0] or uv[1]: rr[rk] = R1.K3(uv[0], uv[1])
            if rr: vex[vk] = rr
        if vex: WG[k] = vex
    assert fails == 0, "rational reconstruction failed on %d coeffs" % fails
    # verify vs holdout prime (full structural comparison)
    Wh = Ws[hold]
    mm = 0
    for k in set(WG) | set(Wh):
        for vk in set(WG.get(k, {})) | set(Wh.get(k, {})):
            for rk in set(WG.get(k, {}).get(vk, {})) | \
                      set(Wh.get(k, {}).get(vk, {})):
                c = WG.get(k, {}).get(vk, {}).get(rk, R1.K0 if False else None)
                want = Wh.get(k, {}).get(vk, {}).get(rk, (0, 0))
                gotu = frmod(c[0], hold) if c is not None else 0
                gotv = frmod(c[1], hold) if c is not None else 0
                if (gotu, gotv) != want: mm += 1
    assert mm == 0, "holdout-prime verification failed on %d coeffs" % mm
    log("CRT %s verified against holdout prime %d (0 mismatches)"
        % (prefix, hold))
    if scalar_check and have(scalar_check):
        # verify vs scalar-specialized fold (radical point evaluation)
        p0 = good_primes(1)[0]; pt = radical_point(p0)
        pWG = load(scalar_check)
        mm = 0
        for k in set(WG) | set(pWG):
            av = {vk: ring_modp(r, pt, p0) for vk, r in WG.get(k, {}).items()}
            av = {vk: c for vk, c in av.items() if c}
            if av != pWG.get(k, {}): mm += 1
        assert mm == 0, "scalar-fold consistency failed on %d keys" % mm
        log("CRT %s consistent with the verified scalar mod-p fold (p=%d)"
            % (prefix, p0))
    save(outname, WG)
    log("exact %s banked via CRT: %d entries over %d keys"
        % (outname, jsize(WG), len(WG)))

# ------------------------------------------------------------ exact fold
def phase_foldx():
    st = load("blocks.pkl")
    mul = lambda a, b: R1.jmul(a, b, DG)
    t0 = time.time()
    if not have("xjf.pkl"):
        jf = tree_fold([b for _, b in st["f"]], mul, "xjf", "xjf.ck")
        save("xjf.pkl", jf); log("exact jf: %d entries" % jsize(jf))
    if not have("xjg.pkl"):
        jg = tree_fold([b for _, b in st["g"]], mul, "xjg", "xjg.ck")
        save("xjg.pkl", jg); log("exact jg: %d entries" % jsize(jg))
    if not have("xf3.pkl"):
        f3 = tree_fold([jpow(b, 3, mul) for _, b in st["f"]],
                       mul, "xf3", "xf3.ck")
        save("xf3.pkl", f3); log("exact f3: %d entries" % jsize(f3))
    if not have("xg2.pkl"):
        g2 = tree_fold([jpow(b, 2, mul) for _, b in st["g"]],
                       mul, "xg2", "xg2.ck")
        save("xg2.pkl", g2); log("exact g2: %d entries" % jsize(g2))
    f3 = load("xf3.pkl"); g2 = load("xg2.pkl")
    WG = R1.jadd(g2, R1.jscal(f3, R1.K3(-1)))
    save("xWG.pkl", WG)
    log("exact WG: %d entries over %d keys (%.1fs total)"
        % (jsize(WG), len(WG), time.time() - t0))

def phase_emit():
    st = load("blocks.pkl")
    WG = load("xWG.pkl")
    jf = load("xjf.pkl") if have("xjf.pkl") else {}
    jg = load("xjg.pkl") if have("xjg.pkl") else {}
    rows = gm_rows(jf, jg, WG, R1.vscal, R1.vadd)
    nconst = census(rows, "exact")
    # anchors: WG slot 0 must be identically zero; band rows no ()-key
    slot0 = [(k, v) for (f_, n, s), v in rows if f_ == "WG-slot0(must-be-0)"]
    assert not slot0, "E1 anchor broken: WG slot-0 nonzero: %s" % slot0[:2]
    rows = [(m, v) for m, v in rows if m[0] != "WG-slot0(must-be-0)"]
    allv = sorted({vid for _, v in rows for vk in v for vid in vk})
    names = {vid: "x%d" % i for i, vid in enumerate(allv)}
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "r1_full_core.ms")
    hdr = ["r3", "z", "A1", "A2", "W1", "HW1", "W2", "HW2", "EB"] + \
          [names[v] for v in allv]
    eqs = list(R1.RAD_EQS)
    labels = [("radical", i, 0) for i in range(len(R1.RAD_EQS))]
    t0 = time.time()
    for i, (meta, v) in enumerate(rows):
        eqs.append(R1.emit_expanded(v, names))
        labels.append(meta)
        if (i + 1) % 50 == 0:
            log("emitted %d/%d rows (%.1fs)" % (i + 1, len(rows),
                                                time.time() - t0))
    with open(path, "w") as f:
        f.write(", ".join(hdr) + "\n0\n")
        f.write(",\n".join(eqs) + "\n")
    with open(os.path.join(OUT_DIR, "r1_full_core.rows.txt"), "w") as f:
        f.write("# char-0 full-degree G_m core; %d radical eqs + %d rows\n"
                % (len(R1.RAD_EQS), len(rows)))
        for i, lab in enumerate(labels):
            f.write("eq%d = %s\n" % (i, lab))
        for vid in allv:
            f.write("%s = %s (level %d)\n" % (names[vid],
                    st["vmeta"][vid]["name"], st["vmeta"][vid]["level"]))
    log("emitted %s (%d eqs, %d+9 vars, %.1f MB)"
        % (path, len(eqs), len(allv), os.path.getsize(path) / 1e6))
    # full-system mod-p variants (radicals as VARIABLES, coeffs mod p):
    # the no-specialization screen; verdict still gated on char 0.
    for p in good_primes(2):
        pp = os.path.join(OUT_DIR, "r1_full_core_p%d.ms" % p)
        with open(pp, "w") as f:
            f.write(", ".join(hdr) + "\n%d\n" % p)
            peqs = []
            for eq in eqs:
                def red(m):
                    return str(int(m.group(0)) % p)
                peqs.append(re.sub(r"(?<![\w^])\d+", red, eq))
            f.write(",\n".join(peqs) + "\n")
        log("emitted %s (%.1f MB)" % (pp, os.path.getsize(pp) / 1e6))
    guards(path, rows, names, allv)

# ---------------------------------------------------------------- guards
TOKEN = re.compile(r"([+-]?)(\d+)?((?:\*?[A-Za-z]\w*(?:\^\d+)?)*)$")
def parse_eval(eqs, val, p):
    """independent evaluator of emitted polynomial strings mod p."""
    out = []
    for eq in eqs:
        tot = 0
        for sgn, term in re.findall(r"([+-]?)([^+-]+)", eq.replace(" ", "")):
            c = 1
            for a in term.split("*"):
                if not a: continue
                if a.isdigit(): c = c * int(a) % p
                else:
                    nm, _, ex = a.partition("^")
                    c = c * pow(val[nm], int(ex) if ex else 1, p) % p
            tot = (tot + (-c if sgn == "-" else c)) % p
        out.append(tot)
    return out

def guards(path, rows, names, allv):
    txt = open(path).read()
    assert "(" not in txt and ")" not in txt, "PAREN SWEEP FAIL"
    log("guard A (paren sweep): PASS — no parentheses in %s" % path)
    eqs = txt.split("\n", 2)[2].strip().rstrip(",").split(",\n")
    eqs = eqs[len(R1.RAD_EQS):]
    assert len(eqs) == len(rows), "row count drift %d vs %d" % (len(eqs), len(rows))
    for p in good_primes(2):
        pt = radical_point(p)
        rng = random.Random(1000 + p)
        xval = {vid: rng.randrange(1, p) for vid in allv}
        val = dict(pt); val.update({names[v]: xval[v] for v in allv})
        got = parse_eval(eqs, val, p)
        nz = idz = 0; mismatch = []
        for i, (meta, v) in enumerate(rows):
            L = 1
            for vk, r in v.items():
                for c in r.values():
                    for q in (Fr(c[0]), Fr(c[1])):
                        L = L * q.denominator // gcd(L, q.denominator)
            G = 0
            for vk, r in v.items():
                for c in r.values():
                    for q in (Fr(c[0]), Fr(c[1])):
                        G = gcd(G, abs((q * L).numerator))
            scale = Fr(L, G) if G > 1 else Fr(L)
            want = eval_vex_modp(v, pt, p, xval) * frmod(scale, p) % p
            if got[i] != want: mismatch.append((i, rows[i][0]))
            if got[i]: nz += 1
        assert not mismatch, ("ROUND-TRIP FAIL", p, mismatch[:5])
        log("guard B (round-trip, p=%d): PASS — %d/%d rows match "
            "independent parser; %d nonzero at random point" %
            (p, len(rows), len(rows), nz))
    # origin + constant census
    p = good_primes(1)[0]; pt = radical_point(p)
    x0 = {vid: 0 for vid in allv}
    at0 = [eval_vex_modp(v, pt, p, x0) for _, v in rows]
    n0 = sum(1 for t in at0 if t == 0)
    log("guard C (origin): %d/%d rows vanish at x=0 + radical point"
        % (n0, len(rows)))
    if n0 == len(rows):
        log("guard C: system CONTAINS the origin — msolve [1] would be a "
            "pipeline error, not a verdict (pre-registered note 8.0)")
    # identically-zero scan (3 random points, both primes)
    dead = set(range(len(rows)))
    for p in good_primes(2):
        pt = radical_point(p)
        for t in range(3):
            rng = random.Random(7000 + 100 * p + t)
            xv = {vid: rng.randrange(1, p) for vid in allv}
            for i in sorted(dead):
                if eval_vex_modp(rows[i][1], pt, p, xv): dead.discard(i)
    log("guard D (residual): %d rows identically zero at 6 random "
        "point/prime combos: %s" % (len(dead),
        [rows[i][0] for i in sorted(dead)][:10]))
    return dead

def phase_emitwfree():
    """char-p screen with W1/HW1/W2/HW2 kept as VARIABLES (only z, r3,
    A1, A2, EB specialized) — the E5-honest local screen: msolve may
    choose the w's. Emitted for two primes."""
    st = load("blocks.pkl")
    WG = load("xWG.pkl")
    rows = gm_rows({}, {}, WG, R1.vscal, R1.vadd)
    rows = [(m, v) for m, v in rows if m[0] != "WG-slot0(must-be-0)"]
    for p in good_primes(2):
        pt = radical_point(p)
        allv = sorted({vid for _, v in rows for vk in v for vid in vk})
        names = {vid: "x%d" % i for i, vid in enumerate(allv)}
        path = os.path.join(OUT_DIR, "r1_full_core_wfree_p%d.ms" % p)
        eqs = ["2*HW1^2+%d*W1^2" % (p - 3), "2*HW2^2+%d*W2^2" % (p - 3)]
        labels = [("radical-HW1", 0, 0), ("radical-HW2", 0, 0)]
        for meta, v in rows:
            acc = {}                          # {(w1,h1,w2,h2,vkey): int}
            for vk, r in v.items():
                for (za, e1, e2, w1, h1, w2, h2, eB), c in r.items():
                    s = (pow(pt["z"], za, p) * pow(pt["A1"], e1, p)
                         * pow(pt["A2"], e2, p) * pow(pt["EB"], eB, p)) % p
                    s = s * (frmod(c[0], p) + frmod(c[1], p) * pt["r3"]) % p
                    if not s: continue
                    kk = (w1, h1, w2, h2, vk)
                    acc[kk] = (acc.get(kk, 0) + s) % p
            terms = []
            for (w1, h1, w2, h2, vk), c in sorted(acc.items()):
                if not c: continue
                parts = []
                for e, nm in ((w1, "W1"), (h1, "HW1"), (w2, "W2"),
                              (h2, "HW2")):
                    if e: parts.append(nm if e == 1 else "%s^%d" % (nm, e))
                for vid in sorted(set(vk)):
                    e = vk.count(vid)
                    parts.append(names[vid] if e == 1 else
                                 "%s^%d" % (names[vid], e))
                m = "*".join(parts)
                terms.append("%d*%s" % (c, m) if m else "%d" % c)
            if terms:
                eqs.append("+".join(terms))
                labels.append(meta)
        with open(path, "w") as f:
            f.write(", ".join(["W1", "HW1", "W2", "HW2"] +
                              [names[v] for v in allv]) + "\n%d\n" % p)
            f.write(",\n".join(eqs) + "\n")
        assert "(" not in open(path).read(), "paren sweep fail wfree"
        with open(path.replace(".ms", ".rows.txt"), "w") as f:
            f.write("# w-free screen p=%d point %s\n" % (p, pt))
            for i, lab in enumerate(labels): f.write("eq%d = %s\n" % (i, lab))
        log("emitted %s (%d eqs, %d+4 vars, %.1f MB); paren sweep PASS"
            % (path, len(eqs), len(allv), os.path.getsize(path) / 1e6))

# ------------------------------------------------- (1,2) sibling branch
def phase_branch12():
    """(1,2)-branch core per SHEET6-R6.md 4.3 delta-spec: h1-stage
    18/21 -> 12/21 (W_G band slots 1..11 vanish; slot-12 pattern tie),
    then h2 = h1 - s1 f^2 stage 12/21 -> 8/21: tie rows
    WG(n,12+r) = s1*F2(n,r) for r = 0..7 (r=0 is the printed legality
    h1+ = s1 (f+)^2; s1 a fresh variable absorbs normalization), and
    slot-20 quotient prop. to qpat = P*q after the s1-subtraction."""
    st = load("blocks.pkl")
    mul = lambda a, b: R1.jmul(a, b, DG)
    WG = load("xWG.pkl")
    if have("xF2.pkl"): F2 = load("xF2.pkl")
    else:
        F2 = tree_fold([jpow(b, 2, mul) for _, b in st["f"]], mul, "xF2")
        save("xF2.pkl", F2)
    s1id = st["nvars"] + 10                  # fresh var id, sorts last
    def times_s1(v):
        return {tuple(sorted(vk + (s1id,))): r for vk, r in v.items()}
    qp = qpat_coeffs()
    rows = []
    for (n, s), v in sorted(WG.items()):
        if 1 <= s <= 11 and v: rows.append((("B12-WG-band", n, s), v))
    def tie(n, r):
        a = WG.get((n, 12 + r), {})
        b = F2.get((n, r), {})
        return R1.vadd(a, R1.vscal(times_s1(b), R1.K3(-1)))
    nset = sorted({n for (n, s) in list(WG) + list(F2)})
    for r in range(0, 8):
        for n in nset:
            v = tie(n, r)
            if v: rows.append((("B12-h2-tie", n, 12 + r), v))
    lead = tie(16, 8)
    for n in nset:
        if n == 16: continue
        v = tie(n, 8)
        r = R1.vadd(R1.vscal(v, qp[16]),
                    R1.vscal(lead, -qp[n])
                    if n < len(qp) and not R1.mk(qp[n]).iszero() else {})
        if r: rows.append((("B12-h2-quot", n, 20), r))
    nconst = census(rows, "(1,2)-branch")
    allv = sorted({vid for _, v in rows for vk in v for vid in vk})
    names = {vid: "x%d" % i for i, vid in enumerate(allv)}
    names[s1id] = "s1"
    path = os.path.join(OUT_DIR, "r1_12branch_core.ms")
    hdr = ["r3", "z", "A1", "A2", "W1", "HW1", "W2", "HW2", "EB"] + \
          [names[v] for v in allv]
    eqs = list(R1.RAD_EQS)
    labels = [("radical", i, 0) for i in range(len(R1.RAD_EQS))]
    for meta, v in rows:
        eqs.append(R1.emit_expanded(v, names))
        labels.append(meta)
    with open(path, "w") as f:
        f.write(", ".join(hdr) + "\n0\n")
        f.write(",\n".join(eqs) + "\n")
    with open(os.path.join(OUT_DIR, "r1_12branch_core.rows.txt"), "w") as f:
        f.write("# (1,2)-branch core (SHEET6-R6 4.3 delta-spec); "
                "s1 = tie scale variable\n")
        for i, lab in enumerate(labels): f.write("eq%d = %s\n" % (i, lab))
        for vid in allv:
            if vid == s1id: f.write("s1 = h2-tie scale (fresh)\n")
            else: f.write("%s = %s (level %d)\n" % (names[vid],
                          st["vmeta"][vid]["name"], st["vmeta"][vid]["level"]))
    assert "(" not in open(path).read(), "paren sweep fail (1,2)"
    log("emitted %s (%d eqs, %d+9+1 vars, %.1f MB); paren sweep PASS"
        % (path, len(eqs), len(allv) - (1 if s1id in allv else 0),
           os.path.getsize(path) / 1e6))

# ------------------------------------------- chain branches (SHEET6-R6 4.2,
# SHEET6-R1 sec 9 delta-specs; ADDITIVE — nothing above this line changed)
S1ID_OFF, CLID_OFF, T1ID_OFF, QLID_OFF, T2ID_OFF = 10, 11, 12, 13, 14

def chain_patterns():
    """K3 eta-coefficient lists (index = eta degree) for the chain
    patterns: p3/p5/p6/p10 = (t-a1)^k(t-a2)^k (t = eta^3, k=3,5,6,10),
    pq34/pq46 = eta*(t-a1)^m(t-a2)^m*(t-b) (m=5,7) — the level-2
    quotient patterns P^{i(mu2-1)}*q with q = H eta P (eta^3-b), H
    absorbed into the quotient lead variable."""
    _, pm = R1.k3poly_pow_pattern()
    P = {k: R1.eta_poly_ref([(R1.A1c, k), (R1.A2c, k)], R1.K1)
         for k in (3, 5, 6, 7, 10)}
    tb = [-R1.Bc, R1.K0, R1.K0, R1.K1]          # eta^3 - b
    pq34 = pm(pm([R1.K0, R1.K1], P[5]), tb)
    pq46 = pm(pm([R1.K0, R1.K1], P[7]), tb)
    pats = dict(p3=P[3], p5=P[5], p6=P[6], p10=P[10], pq34=pq34, pq46=pq46)
    # self-checks: convolution identities (validate the legality-row
    # reduction (p_k*cL) conv (p_k*cL) = p_{2k}*cL^2) + degrees + monic
    for a, b, c in (("p3", "p3", "p6"), ("p5", "p5", "p10")):
        got = pm(pats[a], pats[b])
        assert len(got) == len(pats[c]) and all(
            (x - y).iszero() for x, y in zip(got, pats[c])), (a, b, c)
    for nm, dg in (("p3", 18), ("p5", 30), ("p6", 36), ("p10", 60),
                   ("pq34", 34), ("pq46", 46)):
        assert len(pats[nm]) == dg + 1 and (pats[nm][dg] - R1.K1).iszero()
    # independent mod-p check at both round-trip primes
    for p in good_primes(2):
        pt = radical_point(p)
        a1, a2, b = (3 + pt["r3"]) % p, (3 - pt["r3"]) % p, 4
        x = random.Random(31 * p).randrange(2, p)
        t = pow(x, 3, p)
        for nm, (m, eta, mb) in (("p3", (3, 0, 0)), ("p5", (5, 0, 0)),
                                 ("p6", (6, 0, 0)), ("p10", (10, 0, 0)),
                                 ("pq34", (5, 1, 1)), ("pq46", (7, 1, 1))):
            want = (pow(x, eta, p) * pow(t - a1, m, p) * pow(t - a2, m, p)
                    * pow(t - b, mb, p)) % p
            got = sum((frmod(c[0], p) + frmod(c[1], p) * pt["r3"])
                      * pow(x, i, p) for i, c in enumerate(pats[nm])) % p
            assert got == want, ("pattern check fail", nm, p)
    log("chain patterns built + verified (conv identities, 2 primes)")
    return pats

def phase_chainF():
    """exact truncated folds F_l = f^l, slots 0..2 only (dg=3) — all the
    in-window chain rows need. Truncation-first is exact (slots >= 0,
    additive). Asserts: slot-0 = const * P^{2l} (the tie constant S_M^l,
    taken FROM the fold, not hardcoded), slot-1 empty (grading)."""
    st = load("blocks.pkl")
    pats = chain_patterns()
    mul = lambda a, b: R1.jmul(a, b, 3)
    out = {}
    for l, p2l in ((3, pats["p6"]), (5, pats["p10"])):
        blks = [jpow({k: v for k, v in b.items() if k[1] < 3}, l, mul)
                for _, b in st["f"]]
        Fl = tree_fold(blks, mul, "F%d" % l)
        assert not any(s == 1 for (n, s) in Fl), "F%d slot-1 nonempty" % l
        lead = Fl.get((12 * l, 0), {}).get((), R1.RZERO)
        pk = R1.rk3(lead)
        assert pk is not None and pk[0] == R1.KONE, \
            "F%d slot-0 lead not a pure K3 constant" % l
        sml = pk[1]
        for (n, s), v in Fl.items():
            if s != 0: continue
            kv = v.get((), R1.RZERO)
            assert not (set(v) - {()}), "F%d slot-0 has var content" % l
            want = sml * (p2l[n] if n < len(p2l) else R1.K0)
            pure = R1.rk3(kv)
            assert (pure is not None and pure[0] == R1.KONE and
                    (pure[1] - want).iszero()), \
                "F%d slot-0 != S_M^%d * P^%d at n=%d" % (l, l, 2 * l, n)
        out[l] = (Fl, sml)
        log("F%d fold: %d entries, slot-0 = (%s) * P^%d verified"
            % (l, jsize(Fl), sml, 2 * l))
    save("chainF.pkl", out)

def times_var(v, vid, mult=1):
    return {tuple(sorted(vk + (vid,) * mult)): r for vk, r in v.items()}

def conv_pat(pat, WG, slot, n):
    """sum_a pat[a] * WG(n-a, slot) (VExpr)."""
    acc = {}
    for a, c in enumerate(pat):
        if R1.mk(c).iszero(): continue
        v = WG.get((n - a, slot))
        if v: acc = R1.vadd(acc, R1.vscal(v, c))
    return acc

def chain_rows(chain, WG, Fl, sml, pats):
    """row list for one chain core. chain in ('23', '25').
    (2,3): band 1..17, quot slot 18 == cL*P^3, s1-legality (r=0 tie
    reduced on the level-1 variety), h2-QUOTIENT at WG^2-slot 38
    (= f^3 slot 2, d_h2 = 34/42) vs pattern pq34 with lead qL.
    (2,5): band 1..5, quot slot 6 == cL*P^5, s1-legality, h2-TIE r=2
    at WG^2-slot 14 (= f^5 slot 2) — deeper level-2 slots need interior
    W_G^2 pairs (farm; sec 9.0)."""
    st = load("blocks.pkl")
    nv = st["nvars"]
    s1, cL, t1, qL, t2 = (nv + S1ID_OFF, nv + CLID_OFF,
                          nv + T1ID_OFF, nv + QLID_OFF, nv + T2ID_OFF)
    assert not any(s == 0 for (n, s) in WG), "E1 anchor broken (slot 0)"
    assert not any(s % 2 for (n, s) in WG), "odd WG slot present?!"
    if chain == "23":
        s1st, p1, wslot, pq, l1 = 18, pats["p3"], 20, pats["pq34"], 3
        tag = "C23"
    else:
        s1st, p1, wslot, pq, l1 = 6, pats["p5"], 8, None, 5
        tag = "C25"
    rows = []
    for (n, s), v in sorted(WG.items()):
        if 1 <= s < s1st and v: rows.append(((tag + "-WG-band", n, s), v))
    d1 = len(p1) - 1                            # = deg p_h1 = 36 - s1st
    assert d1 == 36 - s1st
    ns = sorted({n for (n, s) in WG if s == s1st} |
                {n for n in range(d1 + 1) if not R1.mk(p1[n]).iszero()})
    for n in ns:
        v = WG.get((n, s1st), {})
        if n > d1:
            if v: rows.append(((tag + "-WG-quot-deg", n, s1st), v))
            continue
        r = R1.vadd(v, R1.vscal({(cL,): R1.RONE}, -R1.mk(p1[n])))
        if r: rows.append(((tag + "-WG-quot", n, s1st), r))
    # legality (level-2 tie r=0 on the level-1 variety) + s1 != 0
    rows.append(((tag + "-s1-tie", 0, 2 * s1st),
                 R1.vadd({tuple(sorted((cL, cL))): R1.RONE},
                         R1.vscal({(s1,): R1.RONE}, -R1.mk(sml)))))
    rows.append(((tag + "-s1-inv", 0, 0),
                 R1.vadd({tuple(sorted((s1, t1))): R1.RONE},
                         R1.vC(R1.rC(R1.K3(-1))))))
    # level-2 slot r=2 (WG^2 slot 2*s1st + 2): pair (s1st, s1st+2) only
    S2 = 2 * s1st + 2
    ns2 = sorted({n for n in range(len(p1) + 40)
                  if conv_pat(p1, WG, wslot, n) or (n, 2) in Fl} |
                 ({n for n in range(len(pq))
                   if not R1.mk(pq[n]).iszero()} if pq else set()))
    for n in ns2:
        r = times_var(R1.vscal(conv_pat(p1, WG, wslot, n), R1.K3(2)), cL)
        f = Fl.get((n, 2))
        if f: r = R1.vadd(r, R1.vscal(times_var(f, s1), R1.K3(-1)))
        if pq is None:                          # (2,5): tie — must vanish
            if r: rows.append(((tag + "-h2-tie", n, S2), r))
            continue
        d2 = len(pq) - 1
        if n > d2:
            if r: rows.append(((tag + "-h2-quot-deg", n, S2), r))
            continue
        r = R1.vadd(r, R1.vscal({(qL,): R1.RONE}, -R1.mk(pq[n])))
        if r: rows.append(((tag + "-h2-quot", n, S2), r))
    fresh = {s1: "s1", cL: "cL", t1: "t1"}
    if pq is not None:
        # deg p_h2@Gm EXACT (R6 4.2 B' coherence; q exact deg 10 feeds
        # the level-3 rung) => quotient lead qL != 0 (Rabinowitsch)
        rows.append(((tag + "-qL-inv", 0, 0),
                     R1.vadd({tuple(sorted((qL, t2))): R1.RONE},
                             R1.vC(R1.rC(R1.K3(-1))))))
        fresh[qL] = "qL"; fresh[t2] = "t2"
    return rows, fresh

def emit_chain_core(base, rows, fresh, st):
    """char-0 emission + rows.txt + guards A-D (mirrors phase_emit)."""
    census(rows, base)
    allv = sorted({vid for _, v in rows for vk in v for vid in vk})
    names = {vid: "x%d" % i for i, vid in enumerate(allv)}
    names.update(fresh)
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, base + ".ms")
    hdr = ["r3", "z", "A1", "A2", "W1", "HW1", "W2", "HW2", "EB"] + \
          [names[v] for v in allv]
    eqs = list(R1.RAD_EQS)
    labels = [("radical", i, 0) for i in range(len(R1.RAD_EQS))]
    t0 = time.time()
    for i, (meta, v) in enumerate(rows):
        eqs.append(R1.emit_expanded(v, names))
        labels.append(meta)
        if (i + 1) % 25 == 0:
            log("emitted %d/%d rows (%.1fs)" % (i + 1, len(rows),
                                                time.time() - t0))
    with open(path, "w") as f:
        f.write(", ".join(hdr) + "\n0\n")
        f.write(",\n".join(eqs) + "\n")
    with open(os.path.join(OUT_DIR, base + ".rows.txt"), "w") as f:
        f.write("# %s chain core (SHEET6-R6 4.2 delta-spec, SHEET6-R1 "
                "sec 9); s1 = level-2 tie scale, t1 = 1/s1 (legality "
                "s1 != 0), cL = level-1 pattern lead, qL = level-2 "
                "quotient lead\n" % base)
        for i, lab in enumerate(labels): f.write("eq%d = %s\n" % (i, lab))
        for vid in allv:
            if vid in fresh: f.write("%s = fresh chain var\n" % fresh[vid])
            else: f.write("%s = %s (level %d)\n" % (names[vid],
                          st["vmeta"][vid]["name"], st["vmeta"][vid]["level"]))
    log("emitted %s (%d eqs, %d+9 vars incl %d fresh, %.1f MB)"
        % (path, len(eqs), len(allv), len(fresh),
           os.path.getsize(path) / 1e6))
    guards(path, rows, names, allv)
    return names, allv

def emit_chain_wfree(base, rows, names, allv):
    """w-free char-p screens (z, r3, A1, A2, EB specialized; W's + all
    x/fresh vars FREE) — mirrors phase_emitwfree, same naming scheme."""
    for p in good_primes(2):
        pt = radical_point(p)
        path = os.path.join(OUT_DIR, "%s_wfree_p%d.ms" % (base, p))
        eqs = ["2*HW1^2+%d*W1^2" % (p - 3), "2*HW2^2+%d*W2^2" % (p - 3)]
        labels = [("radical-HW1", 0, 0), ("radical-HW2", 0, 0)]
        for meta, v in rows:
            acc = {}
            for vk, r in v.items():
                for (za, e1, e2, w1, h1, w2, h2, eB), c in r.items():
                    s = (pow(pt["z"], za, p) * pow(pt["A1"], e1, p)
                         * pow(pt["A2"], e2, p) * pow(pt["EB"], eB, p)) % p
                    s = s * (frmod(c[0], p) + frmod(c[1], p) * pt["r3"]) % p
                    if not s: continue
                    kk = (w1, h1, w2, h2, vk)
                    acc[kk] = (acc.get(kk, 0) + s) % p
            terms = []
            for (w1, h1, w2, h2, vk), c in sorted(acc.items()):
                if not c: continue
                parts = []
                for e, nm in ((w1, "W1"), (h1, "HW1"), (w2, "W2"),
                              (h2, "HW2")):
                    if e: parts.append(nm if e == 1 else "%s^%d" % (nm, e))
                for vid in sorted(set(vk)):
                    e = vk.count(vid)
                    parts.append(names[vid] if e == 1 else
                                 "%s^%d" % (names[vid], e))
                m = "*".join(parts)
                terms.append("%d*%s" % (c, m) if m else "%d" % c)
            if terms:
                eqs.append("+".join(terms))
                labels.append(meta)
        with open(path, "w") as f:
            f.write(", ".join(["W1", "HW1", "W2", "HW2"] +
                              [names[v] for v in allv]) + "\n%d\n" % p)
            f.write(",\n".join(eqs) + "\n")
        assert "(" not in open(path).read(), "paren sweep fail " + path
        with open(path.replace(".ms", ".rows.txt"), "w") as f:
            f.write("# w-free screen p=%d point %s\n" % (p, pt))
            for i, lab in enumerate(labels): f.write("eq%d = %s\n" % (i, lab))
        log("emitted %s (%d eqs, %d+4 vars, %.1f MB); paren sweep PASS"
            % (path, len(eqs), len(allv), os.path.getsize(path) / 1e6))

def phase_chain(chain):
    st = load("blocks.pkl")
    WG = load("xWG.pkl")
    cf = load("chainF.pkl")
    pats = chain_patterns()
    l = 3 if chain == "23" else 5
    Fl, sml = cf[l]
    rows, fresh = chain_rows(chain, WG, Fl, sml, pats)
    base = "r1_%schain_core" % chain
    names, allv = emit_chain_core(base, rows, fresh, st)
    emit_chain_wfree(base, rows, names, allv)

# ---------------------------------------------------------------- msolve
def run_msolve(path, tag, timeout, extra=("-g", "2")):
    out = os.path.join("/Users/dc/code/math/jc72108/runs",
                       os.path.basename(path) + "." + tag + ".out")
    cmd = ["msolve"] + list(extra) + ["-f", path]
    log("msolve start: %s (timeout %ds)" % (" ".join(cmd), timeout))
    t0 = time.time()
    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                           timeout=timeout)
        open(out, "w").write(r.stdout + "\n--stderr--\n" + r.stderr)
        head = (r.stdout or r.stderr).strip()[:300]
        log("msolve done rc=%d %.1fs -> %s\n  head: %s"
            % (r.returncode, time.time() - t0, out, head))
        return r.stdout
    except subprocess.TimeoutExpired:
        log("msolve TIMEOUT after %ds (%s)" % (timeout, tag))
        open(out, "w").write("TIMEOUT %ds\n" % timeout)
        return None

if __name__ == "__main__":
    args = set(sys.argv[1:])
    if "--blocks" in args: phase_blocks()
    if "--check" in args: phase_check()
    if "--foldp" in args: phase_foldp()
    if "--xcheck" in args: phase_xcheck()
    if "--qcheck" in args: phase_qcheck()
    if "--branch12" in args: phase_branch12()
    if "--foldc" in args: phase_foldc()
    for a in args:
        if a.startswith("--foldc-one="): phase_foldc(only=int(a.split("=")[1]))
        if a.startswith("--foldc2-one="):
            phase_foldc2(only=int(a.split("=")[1]))
        if a.startswith("--foldv-one="):
            phase_foldv(only=int(a.split("=")[1]))
        if a.startswith("--fixz-one="):
            phase_fixz(only=int(a.split("=")[1]))
        if a.startswith("--foldv2-one="):
            phase_foldv2(only=int(a.split("=")[1]))
    if "--crt" in args: phase_crt()
    if "--crt2" in args: phase_crt("cF2", "xF2.pkl", scalar_check="pF2.pkl")
    if "--emitwfree" in args: phase_emitwfree()
    if "--chainF" in args: phase_chainF()
    if "--chain23" in args: phase_chain("23")
    if "--chain25" in args: phase_chain("25")
    if "--foldx" in args: phase_foldx()
    if "--emit" in args: phase_emit()
    if "--msolve-screen" in args:
        run_msolve(os.path.join(OUT_DIR, "r1_full_core_modp.ms"),
                   "screen", 1200)
    if "--msolve" in args:
        run_msolve(os.path.join(OUT_DIR, "r1_full_core.ms"), "char0", 1200)
    if "--msolve-all" in args:
        import glob
        for f in sorted(glob.glob(os.path.join(OUT_DIR,
                                               "r1_full_core_wfree_p*.ms"))):
            run_msolve(f, "wfree", 1200)
        for f in sorted(glob.glob(os.path.join(OUT_DIR,
                                               "r1_full_core_p*.ms"))):
            if "wfree" not in f: run_msolve(f, "fullp", 1200)
        run_msolve(os.path.join(OUT_DIR, "r1_full_core.ms"), "char0", 1200)
