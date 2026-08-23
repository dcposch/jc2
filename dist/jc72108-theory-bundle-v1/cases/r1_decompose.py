"""r1_decompose.py -- chart decomposition of the R1 reduced core.

ADDITIVE (2026-08-11): parses systems/r1/r1_reduced_core.ms (the
guard-certified emitted artifact; ground truth, not pickles) and splits
V(reduced core) by the vanishing pattern of (W1, W2):

  V(core) = U_{pat in {Z,U}^2} pi( V(leaf_pat) )        (disjoint cover)

  Z-branch (W_i = 0): the quadric 2HW_i^2 = 3W_i^2 forces HW_i = 0 on the
    VARIETY (HW_i^2 in ideal + (W_i), char != 2), so both are substituted 0;
    W-loaded terms die, rows shrink/drop.
  U-branch (W_i != 0): Rabinowitsch var uWi with uWi*W_i = 1 adjoined; the
    chart makes every W-monomial coefficient invertible (HW_i^-1 =
    (2/3) HW_i uWi^2 via the quadric), unlocking the quasi-linear pivots
    that r1_reduce.py had to bar (its unit class was W-free).

Per-leaf: extended quasi-linear elimination (pivot coefficient = single
W-monomial x etale unit, unit certified by min-poly as in r1_reduce),
then emission (expanded monomial sums; p-variants coefficient-reduced
into [0,p)) + the four standard guards + a soundness/back-map identity.

Phases: stats | build | guards | cover | emit | calibrate
"""
import os, re, sys, time, random, pickle
from fractions import Fraction as Fr
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SYS = os.path.join(ROOT, "systems", "r1")
LEAFDIR = os.path.join(SYS, "leaves")
RUNS = os.path.join(ROOT, "runs")
TMP = "/tmp/r1dec"
os.makedirs(TMP, exist_ok=True)
sys.path.insert(0, HERE)

import r1_reduce as RR
from r1_reduce import (RADS, IR3, IZ, IA1, IA2, IW1, IHW1, IW2, IHW2, IEB,
                       parse_ms, parse_poly, rad_reduce, rmul, padd, pmul,
                       rad_inv, coeff_split, emit_poly, eval_poly_modp,
                       FCMOD, log, run_msolve)

CORE = os.path.join(SYS, "r1_reduced_core.ms")


def load_core():
    """parse the emitted reduced core -> (hdr, radical eq strings, polys)."""
    hdr, char, eqs = parse_ms(CORE)
    assert char == 0
    nrad = 7
    polys = [parse_poly(eq) for eq in eqs[nrad:]]
    return hdr, eqs[:nrad], polys


def wkey(rk):
    return (rk[IW1], rk[IHW1], rk[IW2], rk[IHW2])


# ------------------------------------------------------------------ stats
def phase_stats():
    hdr, rads, polys = load_core()
    log("core: %d rows, header %d vars" % (len(polys), len(hdr)))
    nterm = sum(len(p) for p in polys)
    # W-load census
    w1t = w2t = botht = puret = 0
    w1rows, w2rows = set(), set()
    for i, p in enumerate(polys):
        for (rk, xk), c in p.items():
            l1 = rk[IW1] or rk[IHW1]
            l2 = rk[IW2] or rk[IHW2]
            if l1:
                w1rows.add(i)
            if l2:
                w2rows.add(i)
            if l1 and l2:
                botht += 1
            elif l1:
                w1t += 1
            elif l2:
                w2t += 1
            else:
                puret += 1
    log("terms %d: W1-only %d, W2-only %d, both %d, W-free %d"
        % (nterm, w1t, w2t, botht, puret))
    log("rows touching W1: %d, W2: %d" % (len(w1rows), len(w2rows)))
    # per-x-var incidence + pivot classification
    occ = {}
    for i, p in enumerate(polys):
        for (rk, xk), c in p.items():
            for v, e in xk:
                st = occ.setdefault(v, dict(rows=set(), maxd=0, nterms=0))
                st["rows"].add(i)
                st["maxd"] = max(st["maxd"], e)
                st["nterms"] += 1
    # pivot candidacy per (v, row): every term containing v is deg-1 in v,
    # single-x, coefficient x-free; classify coefficient:
    #   ETALE (W-free unit candidate)  -- should be none (frontier complete)
    #   WMONO (all terms same W-monomial, etale part unit)  -- unlocked on
    #          the corresponding unit chart(s)
    #   MIXED (several W-monomials / not uniform)
    piv = {}
    for i, p in enumerate(polys):
        loc = {}
        for (rk, xk), c in p.items():
            for v, e in xk:
                loc.setdefault(v, []).append((rk, xk, e))
        for v, terms in loc.items():
            if any(e != 1 or len(xk) != 1 for rk, xk, e in terms):
                continue
            wks = {wkey(rk) for rk, xk, e in terms}
            if len(wks) != 1:
                piv.setdefault(v, []).append((i, "MIXED", None))
                continue
            wk = wks.pop()
            need = []
            if wk[0] or wk[1]:
                need.append("W1")
            if wk[2] or wk[3]:
                need.append("W2")
            # etale part: strip W exponents, must be a unit
            u = {}
            for rk, xk, e in terms:
                rk2 = list(rk)
                rk2[IW1] = rk2[IHW1] = rk2[IW2] = rk2[IHW2] = 0
                u[tuple(rk2)] = u.get(tuple(rk2), Fr(0)) + p[(rk, ((v, 1),))]
            res = rad_inv({k: c for k, c in u.items() if c})
            tag = ("ETALE" if not need else "WMONO:" + "+".join(need)) \
                if res is not None else "ZDIV"
            piv.setdefault(v, []).append((i, tag, wk))
    log("-- per-x-var: rows / maxdeg / linear-pivot classes --")
    unlock = {"W1": set(), "W2": set(), "W1+W2": set()}
    for v in sorted(occ):
        st = occ[v]
        tags = [t for _, t, _ in piv.get(v, [])]
        cnt = {}
        for t in tags:
            cnt[t] = cnt.get(t, 0) + 1
        if st["maxd"] == 1 and tags:
            for t in cnt:
                if t.startswith("WMONO:"):
                    unlock[t[6:]].add(v)
        log("  x%-3d rows %2d maxdeg %d terms %4d pivots %s"
            % (v, len(st["rows"]), st["maxd"], st["nterms"], cnt or "-"))
    log("UNLOCKABLE quasi-linear vars by chart: W1-unit %s, W2-unit %s, "
        "both %s" % (sorted(unlock["W1"]), sorted(unlock["W2"]),
                     sorted(unlock["W1+W2"])))
    return occ, piv


# ------------------------------------------------------------------ build
LEAVES = ["ZZ", "ZU", "UZ", "UU"]  # (W1,W2) pattern; Z = 0, U = unit
COST_CAP = 3 * 10 ** 6
ZEROKEY = tuple([0] * 9)


def chart_kill(polys, u1, u2):
    """substitute W_i = HW_i = 0 on Z sides (drop loaded terms)."""
    rows, deadrows = {}, []
    for i, p in enumerate(polys):
        q = {}
        for (rk, xk), c in p.items():
            if not u1 and (rk[IW1] or rk[IHW1]):
                continue
            if not u2 and (rk[IW2] or rk[IHW2]):
                continue
            q[(rk, xk)] = c
        if q:
            rows[i] = q
        else:
            deadrows.append(i)
    return rows, deadrows


def winv_poly(invd, wk):
    """inverse of (etale u) * W-monomial wk on the unit chart:
    u^{-1} * W1^{-(a+2b)} HW1^b W2^{-(c+2d)} HW2^d * (2/3)^{b+d}."""
    a, b, c, d = wk
    assert b in (0, 1) and d in (0, 1), wk
    out = {}
    for rk, cf in invd.items():
        nk = list(rk)
        assert nk[IHW1] == 0 and nk[IHW2] == 0 and nk[IW1] == 0 \
            and nk[IW2] == 0
        nk[IW1] -= a + 2 * b
        nk[IHW1] += b
        nk[IW2] -= c + 2 * d
        nk[IHW2] += d
        out[tuple(nk)] = cf * Fr(2, 3) ** (b + d)
    return out


def leaf_eliminate(rows, u1, u2, tag):
    """greedy quasi-linear elimination; pivot coeff = single W-monomial
    (invertible on this chart) x certified etale unit. Mirrors
    r1_reduce.phase_eliminate; banked subs for the back-map."""
    subs, dropped, black = [], [], set()
    t0, it = time.time(), 0
    while True:
        it += 1
        occ = {}
        for i, p in rows.items():
            loc = {}
            for (rk, xk), cf in p.items():
                for v, e in xk:
                    st = loc.setdefault(v, [0, 0, True, set()])
                    st[0] = max(st[0], e)
                    st[1] += 1
                    if e != 1 or len(xk) != 1:
                        st[2] = False
                    else:
                        st[3].add(wkey(rk))
            for v, st in loc.items():
                occ.setdefault(v, {})[i] = st
        best = None
        for v, byrow in occ.items():
            md = max(st[0] for st in byrow.values())
            if md > 3:
                continue
            for A, stA in byrow.items():
                if stA[0] != 1 or not stA[2] or len(stA[3]) != 1:
                    continue
                wk = next(iter(stA[3]))
                if (wk[0] or wk[1]) and not u1:
                    continue
                if (wk[2] or wk[3]) and not u2:
                    continue
                if (v, A) in black:
                    continue
                slen = max(1, len(rows[A]) - stA[1])
                cost = sum(stB[1] * slen ** stB[0]
                           for B, stB in byrow.items() if B != A)
                if cost > COST_CAP:
                    continue
                if best is None or cost < best[0]:
                    best = (cost, v, A, wk)
        if best is None:
            log("%s iter %d: frontier complete" % (tag, it))
            break
        cost, v, A, wk = best
        sp = coeff_split(rows[A], v)
        coeff = sp[1]
        etale = {}
        for (rk, xk), cf in coeff.items():
            assert not xk
            rk2 = list(rk)
            rk2[IW1] = rk2[IHW1] = rk2[IW2] = rk2[IHW2] = 0
            etale[tuple(rk2)] = etale.get(tuple(rk2), Fr(0)) + cf
        etale = {k: cf for k, cf in etale.items() if cf}
        res = rad_inv(etale)
        if res is None:
            black.add((v, A))
            continue
        invd, minpoly = res
        ip = winv_poly(invd, wk)
        # mechanical unit check: coeff * inv == 1
        chk = pmul({k: cf for k, cf in coeff.items()},
                   {(rk, ()): cf for rk, cf in ip.items()})
        assert chk == {(ZEROKEY, ()): Fr(1)}, (tag, v, A, chk)
        s = pmul({k: -cf for k, cf in sp.get(0, {}).items()},
                 {(rk, ()): cf for rk, cf in ip.items()})
        for B in list(rows):
            if B == A:
                continue
            spB = coeff_split(rows[B], v)
            if len(spB) == 1 and 0 in spB:
                continue
            newB = dict(spB.get(0, {}))
            sk, deg = dict(s), 1
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
        subs.append((v, coeff, s, A))
        del rows[A]
        log("%s iter %d: elim x%d via row %d (wk=%s |s|=%d minpoly %d "
            "cost %d) -> %d rows %d terms %.0fs"
            % (tag, it, v, A, wk, len(s), len(minpoly) - 1, cost,
               len(rows), sum(len(p) for p in rows.values()),
               time.time() - t0))
    return rows, subs, dropped


def phase_build():
    hdr, rads, polys = load_core()
    state = {}
    for tag in LEAVES:
        u1, u2 = (tag[0] == "U"), (tag[1] == "U")
        rows, deadZ = chart_kill(polys, u1, u2)
        log("%s: chart kill -> %d rows (%d died), %d terms"
            % (tag, len(rows), len(deadZ),
               sum(len(p) for p in rows.values())))
        rows, subs, dropped = leaf_eliminate(rows, u1, u2, tag)
        remv = sorted({v for p in rows.values() for (rk, xk) in p
                       for v, e in xk})
        log("%s DONE: %d rows, %d x-vars, %d terms; %d eliminated, "
            "%d rows dropped in elim, %d killed by chart"
            % (tag, len(rows), len(remv),
               sum(len(p) for p in rows.values()), len(subs),
               len(dropped), len(deadZ)))
        state[tag] = dict(rows=rows, subs=subs, dropped=dropped,
                          deadZ=deadZ, u1=u1, u2=u2)
        with open(os.path.join(TMP, "leaves.pkl"), "wb") as f:
            pickle.dump(state, f)
    log("build complete -> %s/leaves.pkl" % TMP)


# ------------------------------------------------------------- emission
def import_fullcore():
    import r1_fullcore as FC
    return FC


def load_state():
    with open(os.path.join(TMP, "leaves.pkl"), "rb") as f:
        return pickle.load(f)


def emit_leaf_poly(poly):
    """poly -> (expanded integer monomial string, scale). Negative W1/W2
    exponents become uW1/uW2 powers (unit charts only)."""
    L = 1
    for k, c in poly.items():
        L = L * c.denominator // gcd(L, c.denominator)
    G = 0
    for k, c in poly.items():
        G = gcd(G, abs((c * L).numerator))
    scale = Fr(L, G) if G > 1 else Fr(L)
    parts = []
    for (rk, xk) in sorted(poly, key=lambda t: (t[1], t[0])):
        n = (poly[(rk, xk)] * scale).numerator
        mono = []
        for i, e in enumerate(rk):
            if e > 0:
                mono.append(RADS[i] + ("^%d" % e if e > 1 else ""))
            elif e < 0:
                assert i in (IW1, IW2), (i, e)
                nm = "uW1" if i == IW1 else "uW2"
                mono.append(nm + ("^%d" % -e if e < -1 else ""))
        for v, e in xk:
            mono.append("x%d" % v + ("^%d" % e if e > 1 else ""))
        body = (str(abs(n)) + "*" if abs(n) != 1 or not mono else "") \
            + "*".join(mono) if mono else str(abs(n))
        parts.append(("-" if n < 0 else "+") + body)
    s = "".join(parts)
    return (s[1:] if s.startswith("+") else s), scale


def leaf_header(tag, remv):
    u1, u2 = tag[0] == "U", tag[1] == "U"
    hdr = ["r3", "z", "A1", "A2"]
    if u1:
        hdr += ["W1", "HW1", "uW1"]
    if u2:
        hdr += ["W2", "HW2", "uW2"]
    hdr += ["EB"] + ["x%d" % v for v in remv]
    return hdr


def leaf_prefix_rows(tag, char, p=None):
    """radical + chart rows (char 0 strings, or mod-p reduced [0,p))."""
    u1, u2 = tag[0] == "U", tag[1] == "U"
    if char == 0:
        out = ["r3^2-3", "A1^3-3-r3", "A2^3-3+r3"]
        if u1:
            out += ["2*HW1^2-3*W1^2", "uW1*W1-1"]
        if u2:
            out += ["2*HW2^2-3*W2^2", "uW2*W2-1"]
        out += ["2*EB^7-3",
                "1+z-z^3-z^4+z^6-z^8-z^9+z^11+z^12"]
        return out
    out = []
    if u1:
        out += ["2*HW1^2+%d*W1^2" % (p - 3), "uW1*W1+%d" % (p - 1)]
    if u2:
        out += ["2*HW2^2+%d*W2^2" % (p - 3), "uW2*W2+%d" % (p - 1)]
    return out


def emit_wfree_rows(rows, scales, p, pt):
    """specialize etale gens at pt; coefficients reduced into [0,p)."""
    out = []
    for i in sorted(rows):
        spec = {}
        for (rk, xk), c in rows[i].items():
            t = FCMOD(c * scales[i], p)
            for idx, nm in ((IR3, "r3"), (IZ, "z"), (IA1, "A1"),
                            (IA2, "A2"), (IEB, "EB")):
                if rk[idx]:
                    t = t * pow(pt[nm], rk[idx], p) % p
            key = ((rk[IW1], rk[IHW1], rk[IW2], rk[IHW2]), xk)
            spec[key] = (spec.get(key, 0) + t) % p
        parts = []
        for (wk, xk) in sorted(spec):
            n = spec[(wk, xk)]
            if not n:
                continue
            mono = []
            for e, nm, un in zip(wk, ("W1", "HW1", "W2", "HW2"),
                                 ("uW1", None, "uW2", None)):
                if e > 0:
                    mono.append(nm + ("^%d" % e if e > 1 else ""))
                elif e < 0:
                    mono.append(un + ("^%d" % -e if e < -1 else ""))
            for v, e in xk:
                mono.append("x%d" % v + ("^%d" % e if e > 1 else ""))
            parts.append("+" + (str(n) + "*" + "*".join(mono) if mono
                                else str(n)))
        s = "".join(parts)
        out.append(s[1:] if s else "0")
    return out


def phase_emit():
    FC = import_fullcore()
    os.makedirs(LEAFDIR, exist_ok=True)
    state = load_state()
    hdr0, rads, polys = load_core()
    labels = {}
    for line in open(os.path.join(SYS, "r1_reduced_core.rows.txt")):
        m = re.match(r"eq(\d+) = (.*)", line)
        if m and int(m.group(1)) >= 7:
            labels[int(m.group(1)) - 7] = m.group(2).strip()
    for tag in LEAVES:
        st = state[tag]
        rows, subs = st["rows"], st["subs"]
        remv = sorted({v for pl in rows.values() for (rk, xk) in pl
                       for v, e in xk})
        elimv = [v for v, u, s2, A in subs]
        allx = sorted({v for pl in polys for (rk, xk) in pl
                       for v, e in xk})
        freev = sorted(set(allx) - set(remv) - set(elimv))
        hdr = leaf_header(tag, remv)
        eqs = leaf_prefix_rows(tag, 0)
        npre = len(eqs)
        scales = {}
        for i in sorted(rows):
            s, sc = emit_leaf_poly(rows[i])
            eqs.append(s)
            scales[i] = sc
        path = os.path.join(LEAFDIR, "leaf_%s.ms" % tag)
        with open(path, "w") as f:
            f.write(", ".join(hdr) + "\n0\n")
            f.write(",\n".join(eqs) + "\n")
        log("emitted %s (%d eqs, %d vars, %.2f MB)"
            % (path, len(eqs), len(hdr), os.path.getsize(path) / 1e6))
        with open(os.path.join(LEAFDIR, "leaf_%s.rows.txt" % tag), "w") as f:
            f.write("# leaf %s of r1_reduced_core.ms (cases/r1_decompose."
                    "py): chart W1 %s, W2 %s\n"
                    % (tag, "unit" if tag[0] == "U" else "= 0",
                       "unit" if tag[1] == "U" else "= 0"))
            f.write("# %d elim'd, %d survivors, %d dropped-as-zero in "
                    "elim, free x's %s\n" % (len(subs), len(rows),
                                             len(st["dropped"]), freev))
            for j, (v, u, s2, A) in enumerate(subs):
                f.write("elim%d: x%d via row %d (%s) |s|=%d\n"
                        % (j, v, A, labels.get(A, "?"), len(s2)))
            for j in range(npre):
                f.write("eq%d = chart/radical row\n" % j)
            for j, i in enumerate(sorted(rows)):
                f.write("eq%d = row %d (%s)\n"
                        % (npre + j, i, labels.get(i, "?")))
        for p in FC.good_primes(2):
            pt = FC.radical_point(p)
            weqs = leaf_prefix_rows(tag, p, p) \
                + emit_wfree_rows(rows, scales, p, pt)
            whdr = [h for h in hdr
                    if h[0] in "WHux" and h not in ("z",)]
            wp = os.path.join(LEAFDIR, "leaf_%s_wfree_p%d.ms" % (tag, p))
            with open(wp, "w") as f:
                f.write(", ".join(whdr) + "\n%d\n" % p)
                f.write(",\n".join(weqs) + "\n")
            log("emitted %s (%d eqs, %d vars, %.2f MB)"
                % (wp, len(weqs), len(whdr), os.path.getsize(wp) / 1e6))


# --------------------------------------------------------------- guards
def chart_point(FC, p, tag, seed=1):
    pt = dict(FC.radical_point(p, seed))
    if tag[0] == "Z":
        pt["W1"] = pt["HW1"] = 0
    else:
        pt["uW1"] = pow(pt["W1"], p - 2, p)
    if tag[1] == "Z":
        pt["W2"] = pt["HW2"] = 0
    else:
        pt["uW2"] = pow(pt["W2"], p - 2, p)
    return pt


def phase_guards():
    FC = import_fullcore()
    state = load_state()
    hdr0, rads, polys = load_core()
    for tag in LEAVES:
        st = state[tag]
        rows, subs = st["rows"], st["subs"]
        idx = sorted(rows)
        remv = sorted({v for pl in rows.values() for (rk, xk) in pl
                       for v, e in xk})
        scales = {i: emit_leaf_poly(rows[i])[1] for i in idx}
        files = ["leaf_%s.ms" % tag] + \
                ["leaf_%s_wfree_p%d.ms" % (tag, p)
                 for p in FC.good_primes(2)]
        for fn in files:  # guard A
            txt = open(os.path.join(LEAFDIR, fn)).read()
            assert "(" not in txt and ")" not in txt, ("PAREN", fn)
        log("%s guard A (paren sweep, 3 files): PASS" % tag)
        npre = len(leaf_prefix_rows(tag, 0))
        for p in FC.good_primes(2):  # guard B
            pt = chart_point(FC, p, tag)
            rng = random.Random(4400 + p)
            xv = {v: rng.randrange(1, p) for v in remv}
            val = dict(pt)
            val.update({"x%d" % v: xv[v] for v in remv})
            eqs0 = open(os.path.join(LEAFDIR, "leaf_%s.ms" % tag)) \
                .read().split("\n", 2)[2].strip().rstrip(",") \
                .split(",\n")[npre:]
            nprew = len(leaf_prefix_rows(tag, p, p))
            eqsw = open(os.path.join(
                LEAFDIR, "leaf_%s_wfree_p%d.ms" % (tag, p))) \
                .read().split("\n", 2)[2].strip().rstrip(",") \
                .split(",\n")[nprew:]
            got0 = FC.parse_eval(eqs0, val, p)
            gotw = FC.parse_eval(eqsw, val, p)
            nz = 0
            for j, i in enumerate(idx):
                want = eval_poly_modp(rows[i], pt, p, xv) \
                    * FCMOD(scales[i], p) % p
                assert got0[j] == want, ("RT0", tag, p, i)
                assert gotw[j] == want, ("RTW", tag, p, i)
                nz += want != 0
            log("%s guard B (round-trip char0+wfree, p=%d): PASS "
                "%d/%d rows, %d nonzero" % (tag, p, len(idx), len(idx), nz))
        p = FC.good_primes(1)[0]  # guard C
        pt = chart_point(FC, p, tag)
        x0 = {v: 0 for v in remv}
        n0 = sum(1 for i in idx
                 if eval_poly_modp(rows[i], pt, p, x0) == 0)
        log("%s guard C (x=0 at generic chart point): %d/%d rows vanish "
            "-> %s" % (tag, n0, len(idx),
                       "ORIGIN-SATISFIABLE" if n0 == len(idx)
                       else "origin excluded"))
        dead = set(idx)  # guard D
        for p in FC.good_primes(2):
            for t in range(3):
                pt = chart_point(FC, p, tag, seed=1 + t)
                rng = random.Random(9500 + p * 10 + t)
                xv = {v: rng.randrange(1, p) for v in remv}
                for i in sorted(dead):
                    if eval_poly_modp(rows[i], pt, p, xv):
                        dead.discard(i)
        assert not dead, (tag, dead)
        log("%s guard D (residual): PASS, 0 identically-zero rows" % tag)
        allx = sorted({v for pl in polys for (rk, xk) in pl
                       for v, e in xk})
        elimset = {v for v, u, s2, A in subs}
        for p in FC.good_primes(2):  # guard E
            for t in range(2):
                pt = chart_point(FC, p, tag, seed=1 + t)
                rng = random.Random(5600 + p * 10 + t)
                xv = {v: rng.randrange(1, p) for v in allx
                      if v not in elimset}
                for v, u, s2, A in reversed(subs):
                    xv[v] = eval_poly_modp(s2, pt, p, xv)
                for v, u, s2, A in subs:
                    assert eval_poly_modp(polys[A], pt, p, xv) == 0, \
                        ("PIVOT", tag, A)
                for B in st["dropped"]:
                    assert eval_poly_modp(polys[B], pt, p, xv) == 0, \
                        ("DROPPED", tag, B)
                for i in idx:
                    a = eval_poly_modp(polys[i], pt, p, xv)
                    b = eval_poly_modp(rows[i], pt, p, xv)
                    assert a == b, ("SURV", tag, i)
            log("%s guard E (soundness/back-map, p=%d): PASS -- %d pivot "
                "+ %d dropped rows vanish; %d survivors == original rows"
                % (tag, p, len(subs), len(st["dropped"]), len(idx)))


def phase_cover():
    FC = import_fullcore()
    hdr0, rads, polys = load_core()
    # (i) boolean tautology: every point falls in exactly one pattern
    rng = random.Random(77)
    p = FC.good_primes(1)[0]
    for _ in range(500):
        w1, w2 = rng.randrange(p), rng.randrange(p)
        pats = [(w1 == 0) == (a == "Z") and (w2 == 0) == (b == "Z")
                for a, b in LEAVES]
        assert sum(pats) == 1
    log("cover (i): 500 random (W1,W2) samples each match EXACTLY ONE "
        "of the 4 patterns (tautology check) PASS")
    # (ii) Z-side HW forcing: HW_i^2 = (3/2) W_i^2 mod quadric => on the
    # variety W_i = 0 forces HW_i = 0 (char != 2): stated; mechanical:
    # quadric at (W_i, HW_i) = (0, h) is 2h^2 = 0.
    log("cover (ii): quadric at W_i=0 reads 2*HW_i^2 = 0 -> HW_i = 0 on "
        "the variety (char != 2) -- Z-charts may substitute both")
    # (iii) ZZ witness: (x = 0, W = HW = 0, any etale point) satisfies
    # ALL 49 original rows at both primes
    for p in FC.good_primes(2):
        pt = dict(FC.radical_point(p))
        pt.update(W1=0, HW1=0, W2=0, HW2=0)
        x0 = {v: 0 for v in range(119)}
        bad = [i for i, pl in enumerate(polys)
               if eval_poly_modp(pl, pt, p, x0)]
        assert not bad, bad
        log("cover (iii): ZZ witness (x=0, W=0) satisfies 49/49 original "
            "rows at p=%d PASS" % p)


def phase_e5check():
    state = load_state()
    uu = state["UU"]["rows"]
    base = uu[40]
    E = {}  # E = (9+5r3) A1 W1^4 + (9-5r3) A2 W2^4 ; row40 == -81 E
    for (cr3, ca1, ca2, cw1, cw2, cf) in (
            (0, 1, 0, 4, 0, -81 * 9), (1, 1, 0, 4, 0, -81 * 5),
            (0, 0, 1, 0, 4, -81 * 9), (1, 0, 1, 0, 4, 81 * 5)):
        rk = [0] * 9
        rk[IR3], rk[IA1], rk[IA2], rk[IW1], rk[IW2] = \
            cr3, ca1, ca2, cw1, cw2
        E[(tuple(rk), ())] = Fr(cf)
    assert base == E, "row40 != -81*E"
    fac = {}
    for i, pl in sorted(uu.items()):
        ks = {c / base[k] for k, c in pl.items()}
        assert len(ks) == 1 and len(pl) == len(base), i
        fac[i] = ks.pop()
    log("UU residual rank 1: rows 40-44 = %s x row40; row40 == -81*E "
        "with E = (9+5r3)A1W1^4 + (9-5r3)A2W2^4" %
        ([str(fac[i]) for i in sorted(fac)]))
    # intended locus: w_i^4 = k_i alpha_i^2 => E -> C*[(9+5s)(a1-4)/a1^2
    # + (9-5s)(a2-4)/a2^2], s = sqrt3, a_i = 3+-s (H_M, S_M cancel)
    def mul(x, y):
        return (x[0] * y[0] + 3 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def inv(x):
        n = x[0] * x[0] - 3 * x[1] * x[1]
        return (x[0] / n, -x[1] / n)
    a1, a2 = (Fr(3), Fr(1)), (Fr(3), Fr(-1))
    T1 = mul(mul((Fr(9), Fr(5)), (a1[0] - 4, a1[1])), inv(mul(a1, a1)))
    T2 = mul(mul((Fr(9), Fr(-5)), (a2[0] - 4, a2[1])), inv(mul(a2, a2)))
    assert T1 == (Fr(0), Fr(1, 3)) and T2 == (Fr(0), Fr(-1, 3))
    log("E5 consistency: T1 = +sqrt3/3, T2 = -sqrt3/3, T1+T2 = 0 "
        "IDENTICALLY (H_M, S_M cancel) -- intended data satisfies E")


# ------------------------------------------------------------ calibrate
def run_msolve_rss(path, out, timeout=900, threads=4):
    """msolve -g 2 -t threads with RSS sampling (1 Hz via ps)."""
    import subprocess
    t0 = time.time()
    proc = subprocess.Popen(
        ["msolve", "-g", "2", "-t", str(threads), "-f", path, "-o", out],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    rssmax = 0
    while proc.poll() is None:
        try:
            r = subprocess.run(["ps", "-o", "rss=", "-p", str(proc.pid)],
                               capture_output=True, text=True)
            rssmax = max(rssmax, int(r.stdout.strip() or 0))
        except Exception:
            pass
        if time.time() - t0 > timeout:
            proc.kill()
            proc.wait()
            return "TIMEOUT", timeout, rssmax
        time.sleep(1)
    wall = time.time() - t0
    txt = open(out).read() if os.path.exists(out) else ""
    body = [l for l in txt.splitlines() if l and not l.startswith("#")]
    verdict = "GB=[1] EMPTY" if any(l.strip().rstrip(":") == "[1]"
                                    for l in body) else "GB!=[1] NONEMPTY"
    return verdict, wall, rssmax


def phase_calibrate(timeout=900):
    FC = import_fullcore()
    logf = os.path.join(RUNS, "r1_leaves_calibrate.log")
    jobs = []
    for tag in LEAVES:
        for p in FC.good_primes(2):
            jobs.append(("leaf_%s_wfree_p%d.ms" % (tag, p), tag, p))
    jobs.append(("leaf_UU.ms", "UU", 0))  # char-0 certificate run
    for fn, tag, p in jobs:
        path = os.path.join(LEAFDIR, fn)
        out = os.path.join(RUNS, fn + ".out")
        verdict, wall, rss = run_msolve_rss(path, out, timeout)
        line = "%s: %s wall %.1fs rss %.1f MB" \
            % (fn, verdict, wall, rss / 1024.0)
        log("calibrate " + line)
        with open(logf, "a") as f:
            f.write(line + "\n")


def phase_psweep(n=6):
    """multi-prime confirmation: emit + run all 4 leaves' wfree
    variants at n fresh primes (p == 1 mod 84, radical point exists)."""
    FC = import_fullcore()
    state = load_state()
    # NOTE: RR.sweepw_primes is unusable (candidate pool ~1170 values,
    # ~1-2 admit radical points; loops forever). good_primes walk instead.
    banked = FC.good_primes(2)
    primes = [p for p in FC.good_primes(n + 2) if p not in banked][:n]
    logf = os.path.join(RUNS, "r1_leaves_calibrate.log")
    for p in primes:
        pt = FC.radical_point(p)
        for tag in LEAVES:
            rows = state[tag]["rows"]
            scales = {i: emit_leaf_poly(rows[i])[1] for i in sorted(rows)}
            remv = sorted({v for pl in rows.values() for (rk, xk) in pl
                           for v, e in xk})
            weqs = leaf_prefix_rows(tag, p, p) \
                + emit_wfree_rows(rows, scales, p, pt)
            whdr = [h for h in leaf_header(tag, remv) if h[0] in "WHux"]
            wp = os.path.join(TMP, "leaf_%s_wfree_p%d.ms" % (tag, p))
            with open(wp, "w") as f:
                f.write(", ".join(whdr) + "\n%d\n" % p)
                f.write(",\n".join(weqs) + "\n")
            out = os.path.join(RUNS, "leaf_%s_wfree_p%d.sweep.out"
                               % (tag, p))
            verdict, wall, rss = run_msolve_rss(wp, out, 900)
            line = "sweep %s p=%d: %s wall %.1fs" % (tag, p, verdict, wall)
            log(line)
            with open(logf, "a") as f:
                f.write(line + "\n")


# ------------------------------------------------------- explicit witness
def tonelli(n, p):
    """sqrt mod p (None if non-residue)."""
    if n == 0:
        return 0
    if pow(n, (p - 1) // 2, p) != 1:
        return None
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(n, q, p), pow(n, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c = i, b * b % p
        t, r = t * c % p, r * b % p
    return r


def phase_witness():
    """explicit UU-chart witness mod both banked primes, verified on the
    EMITTED reduced core (56 eqs) and full core (105 eqs) by the
    independent parser, through BOTH banked back-maps."""
    FC = import_fullcore()
    state = load_state()
    uu = state["UU"]
    hdrR, charR, eqsR = parse_ms(CORE)
    hdrF, charF, eqsF = parse_ms(os.path.join(SYS, "r1_full_core.ms"))
    with open("/tmp/r1red/reduced.pkl", "rb") as f:
        red = pickle.load(f)
    for p in FC.good_primes(2):
        pt = dict(FC.radical_point(p))
        inv = lambda a: pow(a, p - 2, p)
        # cube-root-of-unity embeddings of A1, A2; solve E for W1 (W2=1)
        om = 2
        while pow(om, (p - 1) // 3, p) == 1:
            om += 1
        om = pow(om, (p - 1) // 3, p)
        got = None
        for i in range(3):
            for j in range(3):
                A1 = pt["A1"] * pow(om, i, p) % p
                A2 = pt["A2"] * pow(om, j, p) % p
                c = (-(9 - 5 * pt["r3"]) * A2
                     * inv((9 + 5 * pt["r3"]) * A1 % p)) % p
                s2r = tonelli(c, p)
                w1 = tonelli(s2r, p) if s2r is not None else None
                if w1 is not None:
                    got = (A1, A2, w1)
                    break
            if got:
                break
        assert got, "no rational 4th root at p=%d in 9 embeddings" % p
        A1, A2, W1 = got
        shw = pt["HW1"] * inv(pt["W1"]) % p          # sqrt(3/2)
        val = dict(pt, A1=A1, A2=A2, W1=W1, W2=1,
                   HW1=shw * W1 % p, HW2=shw)
        val["uW1"], val["uW2"] = inv(W1), 1
        # x's: free = 0; back-map the 16 leaf subs, then the 19 sec-10 subs
        xv = {v: 0 for v in range(119)}
        for v, u, s2, A in reversed(uu["subs"]):
            xv[v] = eval_poly_modp(s2, val, p, xv)
        for v, u, s2, A in reversed(red["subs"]):
            xv[v] = eval_poly_modp(s2, val, p, xv)
        val.update({"x%d" % v: xv[v] for v in xv})
        gotR = FC.parse_eval(eqsR, val, p)
        gotF = FC.parse_eval(eqsF, val, p)
        assert not any(gotR), [k for k, g in enumerate(gotR) if g]
        assert not any(gotF), [k for k, g in enumerate(gotF) if g]
        log("WITNESS p=%d: W1=%d, W2=1 (both nonzero), A-embedding "
            "(om^%d, om^%d): ALL %d reduced-core eqs AND ALL %d "
            "full-core eqs vanish (independent parser) -- explicit "
            "intended-chart point" % (p, W1, i, j, len(eqsR), len(eqsF)))


if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "stats"
    if ph == "stats":
        phase_stats()
    elif ph == "build":
        phase_build()
    elif ph == "emit":
        phase_emit()
    elif ph == "guards":
        phase_guards()
    elif ph == "cover":
        phase_cover()
    elif ph == "e5check":
        phase_e5check()
    elif ph == "calibrate":
        phase_calibrate(int(sys.argv[2]) if len(sys.argv) > 2 else 900)
    elif ph == "psweep":
        phase_psweep(int(sys.argv[2]) if len(sys.argv) > 2 else 6)
    elif ph == "witness":
        phase_witness()
