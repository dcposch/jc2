"""r1_q2_screen.py -- Q2: depth-84 slot-60 quotient screen over the UU
chart with W NOT specialized and free-x directions OPEN (SHEET6-R1.md
sec 19; staging 15.6/16.5, saturation standing rule sec 17/18).
ADDITIVE new file; no prior emission touched.

Design (15.6 "leaf-compressed", with the sizing gate honored):
  - back-map: the 35 banked UU+sec-10 substitutions composed SYMBOLICALLY
    mod p over the 84 free core directions; W1/HW1/W2/HW2 carried as a
    canonical Laurent W-part per monomial (quotient by the quadrics
    2HW_i^2 = 3W_i^2, uW_i emitted for negative powers); etale radicals
    at the banked point (wfree methodology).  The three DEEP back-map
    values bf_18/bf_24/bf_30 (24/348/3552 terms) are NOT folded: kept as
    variables with their defining rows adjoined (exact compression).
  - stratum parameter LCUT: free core vars at slot < LCUT are set to 0
    (slot = level-12).  LCUT=1 is the FULL locus.  Sizing is MEASURED
    per LCUT (phase sz); the 15.6 gate (<= 10^7 terms local/box01)
    decides what runs where.  KILL SEMANTICS: EMPTY at LCUT=L proves
    every depth-84 survivor on the UU chart has a nonzero free
    dead-stretch coefficient at slot < L (EMPTY at L=1 = full kill).
  - rows: quadrics + uW + relation E + 3 defining rows + quotient rows
    WF(n,60) - s1F*c_n for n <= NCAP=44 (n=2,9,..,44) + E5 quartic (HM
    restored) + E6 cube tie + s1F*tSAT-1.  Row-subset soundness: a
    subset ideal can only ENLARGE the variety, so EMPTY(subset) =>
    EMPTY(full tier); the n<=44 subset is MEASURED sufficient for the
    banked family kill (fam_sub probe, SHEET6-R1-Q2E5.md).
  - anchors: A-Q2-1 witness regression (rows specialize to the banked
    gate rows EXACTLY); A-Q2-2 family regression (rows at free-x=0,
    W SYMBOLIC == the banked exact fam rows mod p); A7 pattern-positive
    (independent binomial c_n + perturbation suite, r1_q0_gate); E1
    slot-0; grading; two-path fold equality.  Phase pert: deliberate
    formulation perturbations must be CAUGHT before runs are trusted.

Phases: sz | build [lcut] | emit | run | ctl | pert | all
State: /tmp/r1q2.  AUDIT: expanded integer monomials, no parens.
"""
import os
import sys
import time
import pickle

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import r1_experiment as R1
import r1_fullcore as FC
import r1_minimal_ext as ME
import r1_q0_gate as Q0

SYS = FC.OUT_DIR
RUNS = os.path.join(os.path.dirname(HERE), "runs")
TMP = "/tmp/r1q2"
os.makedirs(TMP, exist_ok=True)
BASE = "r1_q2"
SCAP = 61
NCAP = 44                       # eta-degree cap; rows n = 2,9,..,44
KEEPX = (37, 43, 49)            # bf_18 / bf_24 / bf_30 kept as variables
TERMCAP = 2 * 10 ** 7           # 15.6 sizing gate (local/box01 bound)
W0 = (0, 0, 0, 0)


class SizingAbort(Exception):
    pass


def log(msg):
    print("[q2 %s] %s" % (time.strftime("%H:%M:%S"), msg), flush=True)


def save(name, obj):
    with open(os.path.join(TMP, name), "wb") as f:
        pickle.dump(obj, f)


def load(name):
    with open(os.path.join(TMP, name), "rb") as f:
        return pickle.load(f)


# ---------------------------------------------- W-part canonical algebra
def wnorm(w, c, p):
    """(w1,h1,w2,h2) Laurent monomial mod the quadrics: h -> h%2,
    c *= (3/2)^(h//2), W += 2(h//2).  Exact on the emitted quotient
    presentation (quadric rows are always adjoined)."""
    w1, h1, w2, h2 = w
    th = 3 * pow(2, p - 2, p) % p
    q, h1 = divmod(h1, 2)
    if q:
        c = c * pow(th if q > 0 else pow(th, p - 2, p), abs(q), p) % p
        w1 += 2 * q
    q, h2 = divmod(h2, 2)
    if q:
        c = c * pow(th if q > 0 else pow(th, p - 2, p), abs(q), p) % p
        w2 += 2 * q
    return (w1, h1, w2, h2), c


def vmulp(x, y, p):
    out = {}
    for (wx, kx), cx in x.items():
        for (wy, ky), cy in y.items():
            w, c = wnorm(tuple(a + b for a, b in zip(wx, wy)),
                         cx * cy % p, p)
            k = (w, tuple(sorted(kx + ky)))
            c2 = (out.get(k, 0) + c) % p
            if c2:
                out[k] = c2
            elif k in out:
                del out[k]
    return out


def vaddp(x, y, p):
    out = dict(x)
    for k, c in y.items():
        c2 = (out.get(k, 0) + c) % p
        if c2:
            out[k] = c2
        elif k in out:
            del out[k]
    return out


def jmulp(a, b, p, scap=SCAP, ncap=NCAP):
    out = {}
    for (na, sa), va in a.items():
        for (nb, sb), vb in b.items():
            n, s = na + nb, sa + sb
            if s >= scap or n > ncap:
                continue
            k = (n, s)
            cur = out.setdefault(k, {})
            for (wx, kx), cx in va.items():
                for (wy, ky), cy in vb.items():
                    w, c = wnorm(tuple(x + y for x, y in zip(wx, wy)),
                                 cx * cy % p, p)
                    kk = (w, tuple(sorted(kx + ky)))
                    c2 = (cur.get(kk, 0) + c) % p
                    if c2:
                        cur[kk] = c2
                    elif kk in cur:
                        del cur[kk]
    return {k: v for k, v in out.items() if v}


def jsize(j):
    return sum(len(v) for v in j.values())


def ring2vex(r, pt, p):
    """exact ring element -> {(wvec, ()): int} mod p (etale specialized,
    W-part symbolic; ring normal form already has h in {0,1})."""
    out = {}
    for (za, e1, e2, w1, h1, w2, h2, eB), c in r.items():
        cc = (FC.frmod(c[0], p) + FC.frmod(c[1], p) * pt["r3"]) % p
        m = (pow(pt["z"], za % 42, p) * pow(pt["A1"], e1 % (p - 1), p)
             * pow(pt["A2"], e2 % (p - 1), p)
             * pow(pt["EB"], eB % (p - 1), p)) % p
        k = ((w1, h1, w2, h2), ())
        c2 = (out.get(k, 0) + cc * m) % p
        if c2:
            out[k] = c2
        elif k in out:
            del out[k]
    return out


# ----------------------------------------------------------- back-map
def q2_backmap(p, lcut, vmap):
    """compose the banked UU + sec-10 subs symbolically mod p.
    vmap: core xN -> depth-84 registry vid (by NAME).  Free core vars at
    slot >= lcut -> their own symbol; below -> 0; KEEPX -> own symbol,
    with the composed defining polys returned separately.
    Returns (xv: xN -> VExpr, defs: xN -> VExpr)."""
    from r1_reduce import IR3
    pt = FC.radical_point(p)
    with open("/tmp/r1dec/leaves.pkl", "rb") as f:
        uu = pickle.load(f)["UU"]["subs"]
    with open("/tmp/r1red/reduced.pkl", "rb") as f:
        red = pickle.load(f)["subs"]
    assigned = {v for v, u, s2, A in uu} | {v for v, u, s2, A in red}
    names54, vm54 = ME.core_name_map()
    lv54 = {int(xn[1:]): vm54[vid]["level"] for vid, xn in names54.items()}
    xv = {}
    for v in range(119):
        if v in assigned:
            continue
        if lv54[v] - 12 >= lcut:
            xv[v] = {(W0, (vmap[v],)): 1}
        else:
            xv[v] = {}

    def rk2wc(rk, cf):
        e3 = rk[IR3]
        c = FC.frmod(cf, p) * pow(3, e3 // 2 if e3 >= 0 else 0, p) % p
        if e3 < 0:
            c = c * pow(pow(3, (-e3) // 2, p), p - 2, p) % p
        if e3 % 2:
            c = c * pt["r3"] % p
        for nm, e in (("z", rk[1]), ("A1", rk[2]), ("A2", rk[3]),
                      ("EB", rk[8])):
            if e:
                b = pt[nm] if e > 0 else pow(pt[nm], p - 2, p)
                c = c * pow(b, abs(e), p) % p
        w, c = wnorm((rk[4], rk[5], rk[6], rk[7]), c, p)
        return w, c

    def peval(s2):
        acc = {}
        for (rk, xk), cf in s2.items():
            w, c = rk2wc(rk, cf)
            term = {(w, ()): c}
            for v, e in xk:
                for _ in range(e):
                    term = vmulp(term, xv[v], p)
                    if not term:
                        break
                if not term:
                    break
            acc = vaddp(acc, term, p)
        return acc

    defs = {}
    for v, u, s2, A in list(reversed(uu)) + list(reversed(red)):
        val = peval(s2)
        if v in KEEPX:
            defs[v] = val
            xv[v] = {(W0, (vmap[v],)): 1}
        else:
            xv[v] = val
    # regression: at frees -> 0 and W -> witness, xv == banked witness
    wval, val = Q0.banked_values(p)
    wit = {"W1": val["W1"], "HW1": val["HW1"], "W2": val["W2"],
           "HW2": val["HW2"]}
    x2n = {int(xn[1:]): vm54[vid]["name"] for vid, xn in names54.items()}
    for v in range(119):
        obj = defs[v] if v in KEEPX else xv[v]
        tot = 0
        for (w, vk), c in obj.items():
            if vk:
                continue                      # free-x content -> 0
            m = c
            for nm, e in zip(("W1", "HW1", "W2", "HW2"), w):
                b = wit[nm] if e > 0 else pow(wit[nm], p - 2, p)
                m = m * pow(b, abs(e), p) % p
            tot = (tot + m) % p
        want = wval.get(x2n[v], 0) % p
        if v in assigned or lv54[v] - 12 >= lcut:
            assert tot == want, ("backmap witness drift", v, x2n[v])
    log("back-map composed (lcut=%d): witness regression EXACT on all "
        "119 core vars; def sizes %s" %
        (lcut, {v: len(defs[v]) for v in defs}))
    return xv, defs


# ------------------------------------------------------------- build
def q2_spec(p, lcut):
    """depth-84 series spec with VExpr entries; returns (spec, meta)."""
    R1.reset_vars()
    orbs84 = R1.build_generators(84)
    vm84 = [dict(m) for m in R1.VARS]
    name2vid = {m["name"]: i for i, m in enumerate(vm84)}
    names54, vm54 = ME.core_name_map()
    corexn = {int(xn[1:]): vm54[vid]["name"]
              for vid, xn in names54.items()}
    vmap = {v: name2vid[nm] for v, nm in corexn.items()}
    extnames = set()
    import re
    for ln in open(os.path.join(SYS, "r1_minimal_ext.rows.txt")):
        m = re.match(r"x\d+ = (\S+) \(", ln)
        if m and m.group(1) not in set(corexn.values()):
            extnames.add(m.group(1))
    xv, defs = q2_backmap(p, lcut, vmap)
    xbyname = {corexn[v]: xv[v] for v in range(119)}
    pt = FC.radical_point(p)
    spec, sym, census = {}, {}, {}
    for on, orb in orbs84.items():
        s = {}
        for lv, vex in orb["series"].items():
            if lv - 12 >= SCAP:
                continue
            (vk, r), = vex.items()
            if vk == ():                       # pin: ring const (W symbolic)
                v = ring2vex(r, pt, p)
                if v:
                    s[lv] = v
            else:
                (vid,) = vk
                nm = R1.VARS[vid]["name"]
                if nm in xbyname:
                    if xbyname[nm]:
                        s[lv] = xbyname[nm]
                else:                          # ext-16 + fresh: symbolic
                    s[lv] = {(W0, (vid,)): 1}
                    sym[vid] = nm
        spec[on] = dict(series=s, size=orb["size"], name=on)
        census[on] = (len(s), sum(len(v) for v in s.values()))
    log("spec (lcut=%d): per-orbit (levels, terms) %s; fresh+ext "
        "symbolic %d" % (lcut, census, len(sym)))
    return spec, dict(vm84=vm84, sym=sym, defs=defs, vmap=vmap,
                      corexn=corexn, extnames=extnames, lcut=lcut, p=p)


def q2_fold_linear(orb, p, z, budget=TERMCAP):
    yt = {lv - 12: v for lv, v in orb["series"].items()}
    jp = {(0, 0): {(W0, ()): 1}}
    n7 = R1.C7SUB[orb["size"]]
    for k in range(7):
        for j in range(n7):
            fac = {(1, 0): {(W0, ()): Q0.zpow(z, 12 * k, p)}}
            for s, v in yt.items():
                c = (p - Q0.zpow(z, (k + 7 * j) * s, p)) % p
                fac[(0, s)] = {kk: cv * c % p for kk, cv in v.items()}
            jp = jmulp(jp, fac, p)
            if jsize(jp) > budget:
                raise SizingAbort("block %s: %d terms > budget %d"
                                  % (orb["name"], jsize(jp), budget))
    return {k: v for k, v in jp.items() if v}


def q2_fold_newton(orb, p, z):
    """suborbit-Newton path (validation twin of q2_fold_linear)."""
    n7 = R1.C7SUB[orb["size"]]
    yt = {lv - 12: v for lv, v in orb["series"].items()}

    def smulp(a, b):
        out = {}
        for sa, va in a.items():
            for sb, vb in b.items():
                s = sa + sb
                if s >= SCAP:
                    continue
                cur = out.setdefault(s, {})
                for (wx, kx), cx in va.items():
                    for (wy, ky), cy in vb.items():
                        w, c = wnorm(tuple(x + y for x, y in
                                           zip(wx, wy)), cx * cy % p, p)
                        kk = (w, tuple(sorted(kx + ky)))
                        c2 = (cur.get(kk, 0) + c) % p
                        if c2:
                            cur[kk] = c2
                        elif kk in cur:
                            del cur[kk]
        return {s: {k: c for k, c in v.items() if c}
                for s, v in out.items() if v}

    yp = {0: {0: {(W0, ()): 1}}, 1: yt}
    for r in range(2, n7 + 1):
        yp[r] = smulp(yp[r - 1], yt)
    q = {}
    for r in range(1, n7 + 1):
        q[r] = {s: {k: c * n7 % p for k, c in v.items()}
                for s, v in yp[r].items()
                if (12 * r + s) % 6 == 0 and
                ((s % 2 == 0) or orb["size"] == 42)}
    e = [{0: {(W0, ()): 1}}]
    for j in range(1, n7 + 1):
        acc = {}
        for r in range(1, j + 1):
            t = smulp(e[j - r], q[r])
            sgn = 1 if (r - 1) % 2 == 0 else p - 1
            for s, v in t.items():
                cur = acc.setdefault(s, {})
                for k, c in v.items():
                    cur[k] = (cur.get(k, 0) + sgn * c) % p
        ji = pow(j, p - 2, p)
        e.append({s: {k: c * ji % p for k, c in v.items() if c * ji % p}
                  for s, v in acc.items()})
    rep = {}
    for j in range(n7 + 1):
        sgn = 1 if j % 2 == 0 else p - 1
        for s, v in e[j].items():
            vv = {k: c * sgn % p for k, c in v.items()}
            vv = {k: c for k, c in vv.items() if c}
            if vv:
                rep[(n7 - j, s)] = vv
    blk = {(0, 0): {(W0, ()): 1}}
    for k in range(7):
        img = {(n, s): {kk: c * Q0.zpow(z, k * (12 * n + s), p) % p
                        for kk, c in v.items()}
               for (n, s), v in rep.items()}
        blk = jmulp(blk, img, p, ncap=10 ** 9)
    return {k: v for k, v in blk.items() if v}


def build_q2(p, lcut, budget=TERMCAP, twopath=True):
    t0 = time.time()
    spec, meta = q2_spec(p, lcut)
    val = ME.witness_point(p)
    z = val["z"]
    folds = {}
    for on in R1.FORB + R1.GORB:
        t1 = time.time()
        fl = q2_fold_linear(spec[on], p, z, budget)
        if twopath:
            fn = q2_fold_newton(spec[on], p, z)
            assert fl == fn, "two-path fold mismatch %s" % on
        folds[on] = fl
        log("  fold %s: %d keys %d terms%s (%.1fs)"
            % (on, len(fl), jsize(fl),
               ", linear==newton" if twopath else "", time.time() - t1))
    jf = {(0, 0): {(W0, ()): 1}}
    for on in R1.FORB:
        jf = jmulp(jf, folds[on], p)
        if jsize(jf) > budget:
            raise SizingAbort("jf: %d > %d" % (jsize(jf), budget))
    jg = {(0, 0): {(W0, ()): 1}}
    for on in R1.GORB:
        jg = jmulp(jg, folds[on], p)
        if jsize(jg) > budget:
            raise SizingAbort("jg: %d > %d" % (jsize(jg), budget))
    log("jets: f %d keys %d terms, g %d keys %d terms (%.1fs)"
        % (len(jf), jsize(jf), len(jg), jsize(jg), time.time() - t0))
    f2 = jmulp(jf, jf, p)
    if jsize(f2) > budget:
        raise SizingAbort("f2: %d" % jsize(f2))
    f3 = jmulp(f2, jf, p)
    g2 = jmulp(jg, jg, p)
    if jsize(f3) + jsize(g2) > 2 * budget:
        raise SizingAbort("f3+g2: %d" % (jsize(f3) + jsize(g2)))
    WF = {}
    for k, v in g2.items():
        WF[k] = dict(v)
    for k, v in f3.items():
        cur = WF.setdefault(k, {})
        for kk, c in v.items():
            c2 = (cur.get(kk, 0) - c) % p
            if c2:
                cur[kk] = c2
            elif kk in cur:
                del cur[kk]
    WF = {k: v for k, v in WF.items() if v}
    log("W_F: %d keys %d terms (%.1fs)"
        % (len(WF), jsize(WF), time.time() - t0))
    # anchors: E1 slot-0, grading
    assert not [k for k, v in WF.items() if k[1] == 0 and v], "E1 slot-0"
    bad = [k for k in WF if (12 * k[0] + k[1]) % 42]
    assert not bad, ("grading", bad[:5])
    rows = {n: WF.get((n, 60), {}) for n in range(2, NCAP + 1, 7)}
    log("anchors E1/grading PASS; %d quotient rows n=%s (%s empty)"
        % (len(rows), sorted(rows),
           sum(1 for v in rows.values() if not v)))
    return rows, meta, folds


# -------------------------------------------------- anchors vs banked
def specialize_row(v, p, wit=None, dropvids=(), keepvids=None):
    """specialize a Q2 VExpr row: W-part -> wit values (or keep if None);
    keys containing dropvids are dropped; returns {vk-or-(w,vk): int}."""
    out = {}
    for (w, vk), c in v.items():
        if any(x in dropvids for x in vk):
            continue
        if keepvids is not None and any(x not in keepvids for x in vk):
            continue
        if wit is None:
            k = (w, vk)
            m = c
        else:
            m = c
            for nm, e in zip(("W1", "HW1", "W2", "HW2"), w):
                b = wit[nm] if e > 0 else pow(wit[nm], p - 2, p)
                m = m * pow(b, abs(e), p) % p
            k = vk
        c2 = (out.get(k, 0) + m) % p
        if c2:
            out[k] = c2
        elif k in out:
            del out[k]
    return out


def anchor_regressions(p, rows, meta):
    """A-Q2-1 (witness == banked gate rows) and A-Q2-2 (free-x=0, W
    symbolic == banked exact fam rows mod p), n <= NCAP."""
    g = Q0.load("gate_p%d.pkl" % p)
    wval, val = Q0.banked_values(p)
    wit = {k: val[k] for k in ("W1", "HW1", "W2", "HW2")}
    # vids zero at the witness/family section: free-x + KEEPX + ext-16
    name2vid = {m["name"]: i for i, m in enumerate(meta["vm84"])}
    corevids = {meta["vmap"][v] for v in range(119)} | \
        {name2vid[nm] for nm in meta["extnames"]}
    for n in sorted(rows):
        mine = specialize_row(rows[n], p, wit=wit, dropvids=corevids)
        # remaining keys: fresh-tail vids only; gate rows use same vids
        want = {vk: c for vk, c in g["rows"][n].items()}
        assert mine == want, ("A-Q2-1 gate regression", n)
    log("anchor A-Q2-1 PASS p=%d: witness-specialized Q2 rows == banked "
        "gate rows EXACTLY (n=%s)" % (p, sorted(rows)))
    fam = Q0.load("fam.pkl")
    pt = FC.radical_point(p)
    for n in sorted(rows):
        mine = specialize_row(rows[n], p, wit=None, dropvids=corevids)
        want = {}
        for vk, r in fam["rows"][n].items():
            for (w, _), c in ring2vex(r, pt, p).items():
                k = (w, vk)
                c2 = (want.get(k, 0) + c) % p
                if c2:
                    want[k] = c2
                elif k in want:
                    del want[k]
        assert mine == want, ("A-Q2-2 fam regression", n)
    log("anchor A-Q2-2 PASS p=%d: free-x=0 Q2 rows (W SYMBOLIC) == "
        "banked exact family rows mod p (n=%s)" % (p, sorted(rows)))


# ---------------------------------------------------------- emission
def emit_name(vid, vm84):
    return vm84[vid]["name"]


def emit_vex(v, p, vm84, extra=()):
    """VExpr {(wvec, vk): int} (+ optional extra symbol terms) -> string."""
    parts = []
    for (w, vk), c in sorted(v.items(), key=lambda t: (len(t[0][1]),
                                                       str(t[0]))):
        mono = []
        for nm, e in zip(("W1", "HW1", "W2", "HW2"), w):
            if e > 0:
                mono.append(nm + ("^%d" % e if e > 1 else ""))
            elif e < 0:
                assert nm in ("W1", "W2"), (nm, e)
                un = "uW1" if nm == "W1" else "uW2"
                mono.append(un + ("^%d" % -e if e < -1 else ""))
        for vid in sorted(set(vk), key=lambda x: emit_name(x, vm84)):
            e = vk.count(vid)
            mono.append(emit_name(vid, vm84) + ("^%d" % e if e > 1 else ""))
        parts.append("%d%s" % (c, "".join("*" + m for m in mono)))
    for t in extra:
        parts.append(t)
    return "+".join(parts) if parts else "0"


def phase_emit(lcut):
    for p in FC.good_primes(2):
        st = load("build_p%d_l%d.pkl" % (p, lcut))
        rows, meta = st["rows"], st["meta"]
        vm84 = meta["vm84"]
        pt = FC.radical_point(p)
        r3 = pt["r3"]
        cn = Q0.pattern_cn(p, r3)
        occ = sorted({vid for v in rows.values() for (w, vk) in v
                      for vid in vk} |
                     {vid for d in meta["defs"].values()
                      for (w, vk) in d for vid in vk} |
                     {meta["vmap"][v] for v in KEEPX})
        hdr = (["W1", "HW1", "W2", "HW2", "uW1", "uW2"] +
               [emit_name(v, vm84) for v in occ] + ["s1F", "HM", "tSAT"])
        labels, eqs = [], []

        def add(lab, eq):
            labels.append(lab)
            eqs.append(eq)
        add("quadric 2HW1^2-3W1^2", "2*HW1^2+%d*W1^2" % (p - 3))
        add("quadric 2HW2^2-3W2^2", "2*HW2^2+%d*W2^2" % (p - 3))
        add("chart uW1*W1-1", "uW1*W1+%d" % (p - 1))
        add("chart uW2*W2-1", "uW2*W2+%d" % (p - 1))
        c1 = (9 + 5 * r3) % p * pt["A1"] % p
        c2 = (9 - 5 * r3) % p * pt["A2"] % p
        add("relation E (13.1 core residual on the UU chart)",
            "%d*W1^4+%d*W2^4" % (c1, c2))
        for v in KEEPX:
            nm = meta["corexn"][v]
            neg = {k: (p - c) % p for k, c in meta["defs"][v].items()}
            add("defining row %s (kept back-map value)" % nm,
                emit_vex({(W0, (meta["vmap"][v],)): 1}, p, vm84) +
                ("+" + emit_vex(neg, p, vm84) if neg else ""))
        for n in sorted(rows):
            extra = []
            if n in cn:
                extra.append("%d*s1F" % ((p - cn[n]) % p))
            add("Q2-quot n=%d s=60 (WF - s1F*c_n)" % n,
                emit_vex(rows[n], p, vm84, extra))
        SM = 7 ** 12 * pow(2 ** 6, p - 2, p) % p
        for i, (ai, Ai, Wn) in enumerate(
                (((3 + r3) % p, pt["A1"], "W1"),
                 ((3 - r3) % p, pt["A2"], "W2")), 1):
            cH = 4 * (ai - 4) % p
            # 243 = 3^5: TEMPLATE 2c-E5 erratum 2026-08-12 (was 729)
            cQ = 243 * pow(SM, 3, p) % p * 144 % p * (ai * ai % p) % p \
                * Ai % p
            add("E5-quartic pole %d (HM restored, W symbolic)" % i,
                "%d*%s^4+%d*HM" % (cQ, Wn, cH))
        add("E6-tie cube form 2^24 HM^3 = 7^48 s1F^3",
            "16777216*HM^3+%d*s1F^3" % (p - pow(7, 48, p)))
        add("SAT s1F (Rabinowitsch)", "s1F*tSAT+%d" % (p - 1))
        fn = "%s_l%d_p%d" % (BASE, lcut, p)
        path = os.path.join(SYS, fn + ".ms")
        with open(path, "w") as f:
            f.write(", ".join(hdr) + "\n%d\n" % p)
            f.write(",\n".join(eqs) + "\n")
        txt = open(path).read()
        assert "(" not in txt and ")" not in txt
        with open(os.path.join(SYS, fn + ".rows.txt"), "w") as f:
            f.write("# Q2 slot-graded depth-84 screen (sec 19): UU chart"
                    " with W SYMBOLIC + free core directions at slot >= "
                    "%d OPEN (below: 0);\n# quotient rows n<=%d (subset "
                    "kill-sound; measured sufficient for the family "
                    "kill), E5/E6 tie + s1F saturation (sec-17 rule).\n"
                    "# etale radicals at the banked point (wfree "
                    "methodology); uW_i = W_i^-1 on the chart.\n"
                    % (lcut, NCAP))
            for i, lab in enumerate(labels):
                f.write("eq%d = %s\n" % (i, lab))
            for vid in occ:
                f.write("%s = registry level %d\n"
                        % (emit_name(vid, vm84), vm84[vid]["level"]))
        log("emitted %s (%d eqs, %d vars, %.1f kB)"
            % (path, len(eqs), len(hdr), os.path.getsize(path) / 1e3))
        save("emit_p%d_l%d.pkl" % (p, lcut),
             dict(labels=labels, eqs=eqs, hdr=hdr))


def phase_run(lcut, timeout=1200):
    import r1_decompose as RD
    logf = os.path.join(RUNS, BASE + "_runs.log")
    for p in FC.good_primes(2):
        fn = "%s_l%d_p%d.ms" % (BASE, lcut, p)
        out = os.path.join(RUNS, fn + ".out")
        verdict, wall, rss = RD.run_msolve_rss(
            os.path.join(SYS, fn), out, timeout, threads=4)
        line = "%s: %s wall %.1fs rss %.1f MB" % (fn, verdict, wall,
                                                  rss / 1024.0)
        log(line)
        with open(logf, "a") as f:
            f.write(line + "\n")


def phase_ctl(lcut, timeout=1200):
    """ctlA = relaxed (no E5/E6/SAT rows): must stay NONEMPTY (the
    witness family's zero-extension lives on it); ctlB = saturation
    only (no E5/E6): EMPTY iff s1F == 0 is forced on the whole stratum."""
    import r1_decompose as RD
    logf = os.path.join(RUNS, BASE + "_runs.log")
    for p in FC.good_primes(2):
        st = load("emit_p%d_l%d.pkl" % (p, lcut))
        labels, eqs, hdr = st["labels"], st["eqs"], st["hdr"]
        assert labels[-1].startswith("SAT") and \
            labels[-2].startswith("E6") and labels[-3].startswith("E5")
        for tag, ee, hh in (
                ("ctlA_relaxed", eqs[:-4], hdr[:-3] + ["s1F"]),
                ("ctlB_satonly", eqs[:-4] + [eqs[-1]],
                 hdr[:-3] + ["s1F", "tSAT"])):
            fn = "%s_l%d_%s_p%d" % (BASE, lcut, tag, p)
            path = os.path.join(SYS, fn + ".ms")
            with open(path, "w") as f:
                f.write(", ".join(hh) + "\n%d\n" % p)
                f.write(",\n".join(ee) + "\n")
            out = os.path.join(RUNS, fn + ".ms.out")
            verdict, wall, rss = RD.run_msolve_rss(path, out, timeout,
                                                   threads=4)
            line = "%s.ms: %s wall %.1fs" % (fn, verdict, wall)
            log(line)
            with open(logf, "a") as f:
                f.write(line + "\n")


def phase_pert(lcut):
    """formulation-positive test: a deliberately perturbed build must be
    CAUGHT by the regression anchors (run BEFORE trusting the runs)."""
    p = FC.good_primes(1)[0]
    spec, meta = q2_spec(p, lcut)
    val = ME.witness_point(p)
    z = val["z"]
    import copy
    # perturbation 1: corrupt one substituted back-map entry (tf1_42)
    sp2 = copy.deepcopy(spec)
    tgt = sp2["P1"]["series"][42]
    tgt[(W0, ())] = (tgt.get((W0, ()), 0) + 12345) % p
    # perturbation 2: slot shift of the P2 witness-tail entry 47 -> 48
    sp3 = copy.deepcopy(spec)
    sp3["P2"]["series"][48] = sp3["P2"]["series"].pop(47)
    caught = 0
    for tag, sp in (("value-corrupt tf1_42", sp2), ("slot-shift 47->48",
                                                    sp3)):
        folds = {on: q2_fold_linear(sp[on], p, z)
                 for on in R1.FORB + R1.GORB}
        jf = {(0, 0): {(W0, ()): 1}}
        for on in R1.FORB:
            jf = jmulp(jf, folds[on], p)
        jg = {(0, 0): {(W0, ()): 1}}
        for on in R1.GORB:
            jg = jmulp(jg, folds[on], p)
        f3 = jmulp(jmulp(jf, jf, p), jf, p)
        g2 = jmulp(jg, jg, p)
        WF = {}
        for k, v in g2.items():
            WF[k] = dict(v)
        for k, v in f3.items():
            cur = WF.setdefault(k, {})
            for kk, c in v.items():
                c2 = (cur.get(kk, 0) - c) % p
                if c2:
                    cur[kk] = c2
                elif kk in cur:
                    del cur[kk]
        rows = {n: {kk: c for kk, c in v.items() if c}
                for (n, s), v in WF.items() if s == 60}
        rows = {n: v for n, v in rows.items() if v}
        try:
            anchor_regressions(p, rows, meta)
            raise SystemExit("PERTURBATION NOT CAUGHT: " + tag)
        except AssertionError as e:
            caught += 1
            log("  pert '%s': CAUGHT (%s)" % (tag, str(e)[:60]))
    log("phase pert PASS: %d/2 deliberate formulation perturbations "
        "caught by the regression anchors" % caught)


def phase_sz():
    """15.6 sizing gate: budgeted builds at descending lcut; bank the
    measured (or aborted-at) sizes."""
    p = FC.good_primes(1)[0]
    table = []
    for lcut in (26, 19, 13, 8, 4, 1):
        t0 = time.time()
        try:
            rows, meta, folds = build_q2(p, lcut, budget=TERMCAP,
                                         twopath=False)
            tot = sum(len(v) for v in rows.values())
            table.append((lcut, "OK", tot, time.time() - t0))
            log("sz lcut=%d: rows %d terms (%.0fs)"
                % (lcut, tot, time.time() - t0))
        except SizingAbort as e:
            table.append((lcut, "ABORT %s" % e, None, time.time() - t0))
            log("sz lcut=%d: SIZING ABORT %s (%.0fs)"
                % (lcut, e, time.time() - t0))
            break
    save("sizing.pkl", table)
    return table


def phase_build(lcut):
    for p in FC.good_primes(2):
        rows, meta, folds = build_q2(p, lcut)
        anchor_regressions(p, rows, meta)
        save("build_p%d_l%d.pkl" % (p, lcut),
             dict(rows=rows, meta=dict(meta, folds=None)))
        log("build banked: build_p%d_l%d.pkl (%d rows, %d terms)"
            % (p, lcut, len(rows), sum(len(v) for v in rows.values())))


# ------------------------------------------ exact char-0 leg (phase x)
S1FID, HMID, TSID = 10 ** 8, 10 ** 8 + 1, 10 ** 8 + 2


def exact_build(lcut):
    """exact-ring twin of build_q2 (radicals + W symbolic in the ring,
    free/tail directions as VExpr vids); char-0 emission material."""
    from fractions import Fraction as Fr
    from r1_reduce import IR3
    R1.reset_vars()
    orbs84 = R1.build_generators(84)
    vm84 = [dict(m) for m in R1.VARS]
    name2vid = {m["name"]: i for i, m in enumerate(vm84)}
    names54, vm54 = ME.core_name_map()
    corexn = {int(xn[1:]): vm54[vid]["name"]
              for vid, xn in names54.items()}
    lv54 = {v: vm54[vid]["level"] for vid, xn in names54.items()
            for v in [int(xn[1:])]}
    vmap = {v: name2vid[nm] for v, nm in corexn.items()}
    with open("/tmp/r1dec/leaves.pkl", "rb") as f:
        uu = pickle.load(f)["UU"]["subs"]
    with open("/tmp/r1red/reduced.pkl", "rb") as f:
        red = pickle.load(f)["subs"]
    assigned = {v for v, u, s2, A in uu} | {v for v, u, s2, A in red}
    xv = {}
    for v in range(119):
        if v not in assigned:
            xv[v] = {(vmap[v],): R1.RONE} \
                if lv54[v] - 12 >= lcut else {}

    def poly_to_vex(s2):
        acc = {}
        for (rk, xk), c in s2.items():
            e3 = rk[IR3]
            kc = R1.mk(Fr(c) * Fr(3) ** (e3 // 2)) * \
                (R1.SQ3 if e3 % 2 else R1.K1)
            r = R1.rmono(za=rk[1], a1=rk[2], a2=rk[3], w1=rk[4],
                         h1=rk[5], w2=rk[6], h2=rk[7], B=rk[8], c=kc)
            term = {(): r}
            for v, e in xk:
                for _ in range(e):
                    term = R1.vmul(term, xv[v])
                    if not term:
                        break
                if not term:
                    break
            acc = R1.vadd(acc, term)
        return acc

    defs = {}
    for v, u, s2, A in list(reversed(uu)) + list(reversed(red)):
        val = poly_to_vex(s2)
        if v in KEEPX:
            defs[v] = val
            xv[v] = {(vmap[v],): R1.RONE}
        else:
            xv[v] = val
    xbyname = {corexn[v]: xv[v] for v in range(119)}
    spec, sym = {}, {}
    for on, orb in orbs84.items():
        s = {}
        for lv, vex in orb["series"].items():
            if lv - 12 >= SCAP:
                continue
            (vk, r), = vex.items()
            if vk == ():
                s[lv] = {(): r}
            else:
                (vid,) = vk
                nm = R1.VARS[vid]["name"]
                if nm in xbyname:
                    if xbyname[nm]:
                        s[lv] = xbyname[nm]
                else:
                    s[lv] = {(vid,): R1.RONE}
                    sym[vid] = nm
        spec[on] = dict(series=s, size=orb["size"], name=on)
    folds = {}
    for on in R1.FORB + R1.GORB:
        t1 = time.time()
        folds[on] = R1.fs_block(spec[on], SCAP)
        log("  exact fold %s: %d keys %d terms (%.1fs)"
            % (on, len(folds[on]),
               sum(len(v) for v in folds[on].values()),
               time.time() - t1))
    jf, jg = R1.JONE, R1.JONE
    for on in R1.FORB:
        jf = R1.jmul(jf, folds[on], SCAP, ndeg=NCAP)
    for on in R1.GORB:
        jg = R1.jmul(jg, folds[on], SCAP, ndeg=NCAP)
    f3 = R1.jmul(R1.jmul(jf, jf, SCAP, ndeg=NCAP), jf, SCAP, ndeg=NCAP)
    g2 = R1.jmul(jg, jg, SCAP, ndeg=NCAP)
    WF = R1.jadd(g2, R1.jscal(f3, R1.mk(-1)))
    log("exact W_F: %d keys %d terms"
        % (len(WF), sum(len(v) for v in WF.values())))
    assert not any(v for (n, s), v in WF.items() if s == 0), "E1 exact"
    assert not [k for k in WF if (12 * k[0] + k[1]) % 42], "grading"
    rows = {n: WF.get((n, 60), {}) for n in range(2, NCAP + 1, 7)}
    # cross-engine regression: exact rows reduce to the mod-p rows
    for p in FC.good_primes(2):
        st = load("build_p%d_l%d.pkl" % (p, lcut))
        pt = FC.radical_point(p)
        for n in sorted(rows):
            acc = {}
            for vk, r in rows[n].items():
                for (w, _), c in ring2vex(r, pt, p).items():
                    k = (w, vk)
                    c2 = (acc.get(k, 0) + c) % p
                    if c2:
                        acc[k] = c2
                    elif k in acc:
                        del acc[k]
            assert acc == st["rows"][n], ("exact-vs-modp", p, n)
        log("exact CROSS-ENGINE regression PASS p=%d (rows n<=%d "
            "reduce to the banked mod-p build EXACTLY)" % (p, NCAP))
    return rows, defs, vm84, vmap, corexn


def phase_exact(lcut, timeout=3600):
    import r1_decompose as RD
    rows, defs, vm84, vmap, corexn = exact_build(lcut)
    names = {vid: vm84[vid]["name"] for vid in range(len(vm84))}
    names.update({S1FID: "s1F", HMID: "HM", TSID: "tSAT"})
    p21, pm = R1.k3poly_pow_pattern()
    p8 = [R1.K1]
    for _ in range(8):
        p8 = pm(p8, p21)
    from fractions import Fraction as Fr
    cn = {7 * m + 2: c for m, c in enumerate(p8) if not c.iszero()}
    SM = R1.mk(Fr(7 ** 12, 2 ** 6))
    SM3 = SM * SM * SM
    eqs = list(R1.RAD_EQS) + ["uW1*W1-1", "uW2*W2-1",
                              "9*A1*W1^4+5*r3*A1*W1^4+9*A2*W2^4"
                              "-5*r3*A2*W2^4"]
    labels = [("radical/chart", e) for e in eqs[:-1]] + \
             [("relation E", eqs[-1])]

    def clear_laurent(v):
        w1m = min((min((k[3] for k in r), default=0)
                   for r in v.values() if r), default=0)
        w2m = min((min((k[5] for k in r), default=0)
                   for r in v.values() if r), default=0)
        if w1m < 0 or w2m < 0:
            mul = R1.rmono(w1=max(0, -w1m), w2=max(0, -w2m))
            v = {vk: R1.rmul(r, mul) for vk, r in v.items()}
        return v, w1m, w2m
    for v in KEEPX:
        nm = corexn[v]
        row = {(vmap[v],): R1.RONE}
        for vk, r in defs[v].items():
            row[vk] = R1.radd(row.get(vk, R1.RZERO), R1.rscal(r, -1))
        row = {vk: r for vk, r in row.items() if r}
        row, w1m, w2m = clear_laurent(row)
        eqs.append(R1.emit_expanded(row, names))
        labels.append(("defining row %s%s" % (nm,
                       " *W-cleared" if w1m < 0 or w2m < 0 else ""),
                       eqs[-1]))
    for n in sorted(rows):
        v = {vk: dict(r) for vk, r in rows[n].items()}
        if n in cn:
            v[(S1FID,)] = R1.radd(v.get((S1FID,), R1.RZERO),
                                  R1.rC(-cn[n]))
        v, w1m, w2m = clear_laurent(v)
        eqs.append(R1.emit_expanded(v, names))
        labels.append(("Q2-quot n=%d s=60%s" % (n,
                       " *W-cleared" if w1m < 0 or w2m < 0 else ""),
                       eqs[-1]))
    for i, (ai2, arg) in enumerate(((R1.A1c * R1.A1c, dict(a1=1, w1=4)),
                                    (R1.A2c * R1.A2c,
                                     dict(a2=1, w2=4))), 1):
        ai = R1.A1c if i == 1 else R1.A2c
        # 243 = 3^5: TEMPLATE 2c-E5 erratum 2026-08-12 (was 729)
        v = {(HMID,): R1.rC(R1.mk(4) * (ai - R1.Bc)),
             (): R1.rmono(c=R1.mk(243 * 144) * SM3 * ai2, **arg)}
        eqs.append(R1.emit_expanded(v, names))
        labels.append(("E5-quartic pole %d (HM restored)" % i, eqs[-1]))
    eqs.append(R1.emit_expanded({(HMID,) * 3: R1.rC(R1.mk(2 ** 24)),
                                 (S1FID,) * 3:
                                 R1.rC(R1.mk(-(7 ** 48)))}, names))
    labels.append(("E6-tie cube form", eqs[-1]))
    eqs.append("s1F*tSAT-1")
    labels.append(("SAT s1F (Rabinowitsch)", eqs[-1]))
    occ = sorted({vid for src in
                  ([r for r in rows.values()] +
                   [defs[v] for v in KEEPX])
                  for vk in src for vid in vk} |
                 {vmap[v] for v in KEEPX})
    hdr = ["r3", "z", "A1", "A2", "W1", "HW1", "W2", "HW2", "EB",
           "uW1", "uW2"] + [names[v] for v in occ] + \
          ["s1F", "HM", "tSAT"]
    fn = "%s_l%d" % (BASE, lcut)
    path = os.path.join(SYS, fn + ".ms")
    with open(path, "w") as f:
        f.write(", ".join(hdr) + "\n0\n")
        f.write(",\n".join(eqs) + "\n")
    txt = open(path).read()
    assert "(" not in txt and ")" not in txt
    with open(os.path.join(SYS, fn + ".rows.txt"), "w") as f:
        f.write("# Q2 CHAR-0 exact object (sec 19): stratum lcut=%d, "
                "radicals as variables, W symbolic, all anchors +\n"
                "# cross-engine regression vs both mod-p builds.\n"
                % lcut)
        for i, (lab, _) in enumerate(labels):
            f.write("eq%d = %s\n" % (i, lab))
    log("emitted %s (%d eqs, %d vars, %.1f kB)"
        % (path, len(eqs), len(hdr), os.path.getsize(path) / 1e3))
    out = os.path.join(RUNS, fn + ".ms.out")
    verdict, wall, rss = RD.run_msolve_rss(path, out, timeout,
                                           threads=4)
    line = "%s.ms (char 0): %s wall %.1fs rss %.1f MB" \
        % (fn, verdict, wall, rss / 1024.0)
    log(line)
    with open(os.path.join(RUNS, BASE + "_runs.log"), "a") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "sz"
    arg = int(sys.argv[2]) if len(sys.argv) > 2 else None
    if ph == "sz":
        phase_sz()
    elif ph == "build":
        phase_build(arg if arg else 13)
    elif ph == "emit":
        phase_emit(arg if arg else 13)
    elif ph == "run":
        phase_run(arg if arg else 13)
    elif ph == "ctl":
        phase_ctl(arg if arg else 13)
    elif ph == "pert":
        phase_pert(arg if arg else 13)
    elif ph == "x":
        phase_exact(arg if arg else 13)
