"""r1_12_decompose.py -- 4-leaf chart decomposition of the (1,2)
sibling core (SHEET6-R1.md sec 15; ADDITIVE, per the sec-15.0
pre-registration banked BEFORE this file was run).

Input: systems/r1/r1_12branch_core.ms (8.19 guard-certified artifact,
ground truth; 105 eqs = 7 radical + 98 rows; 9 radicals + x0..x118 +
s1).  The tie variable s1 is carried internally as x-index 119
(r1_reduce.parse_poly asserts x-names) and re-named s1 at emission.

Delta vs cases/r1_decompose.py (whose functions are REUSED, not
copied): input is the RAW core -- no sec-10 pre-reduction exists for
the sibling; leaf_eliminate subsumes it (etale W-free pivots are
chart-independent members of its pivot class); guard E certifies
soundness directly against the 98 original rows.  Emitted leaves:
systems/r1/leaves/leaf12_{ZZ,ZU,UZ,UU}[.ms|_wfree_p*.ms|.rows.txt].
Minimal-core leaf_* files are untouched (sha256 regression gate).

Phases: stats | build | emit | guards | cover | calibrate | psweep
"""
import os, re, sys, time, random, pickle
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SYS = os.path.join(ROOT, "systems", "r1")
LEAFDIR = os.path.join(SYS, "leaves")
RUNS = os.path.join(ROOT, "runs")
TMP = "/tmp/r1dec12"
os.makedirs(TMP, exist_ok=True)
sys.path.insert(0, HERE)

from r1_reduce import (IR3, IZ, IA1, IA2, IW1, IHW1, IW2, IHW2, IEB,
                       parse_ms, parse_poly, eval_poly_modp, FCMOD, log)
import r1_decompose as RD
from r1_decompose import (LEAVES, chart_kill, leaf_eliminate,
                          emit_leaf_poly, leaf_prefix_rows,
                          emit_wfree_rows, chart_point, run_msolve_rss,
                          import_fullcore)

CORE = os.path.join(SYS, "r1_12branch_core.ms")
S1X = 119                     # internal x-index for the s1 tie variable
NROW = 98

S1TOK = re.compile(r"(?<![\w])s1(?![\w])")
X119 = re.compile(r"x119(?!\d)")


def load_core():
    """parse the (1,2) core; s1 -> x119. Cached (22 MB parse)."""
    ck = os.path.join(TMP, "core.pkl")
    if os.path.exists(ck):
        with open(ck, "rb") as f:
            return pickle.load(f)
    hdr, char, eqs = parse_ms(CORE)
    assert char == 0 and hdr[-1] == "s1" and len(eqs) == 7 + NROW
    polys = [parse_poly(S1TOK.sub("x119", eq)) for eq in eqs[7:]]
    out = (hdr, eqs[:7], polys)
    with open(ck, "wb") as f:
        pickle.dump(out, f)
    return out


def rowlabels():
    labels = {}
    for line in open(os.path.join(SYS, "r1_12branch_core.rows.txt")):
        m = re.match(r"eq(\d+) = (.*)", line)
        if m and int(m.group(1)) >= 7:
            labels[int(m.group(1)) - 7] = m.group(2).strip()
    return labels


def s1name(s):
    return X119.sub("s1", s)


# ------------------------------------------------------------------ stats
def phase_stats():
    hdr, rads, polys = load_core()
    log("core: %d rows, header %d vars" % (len(polys), len(hdr)))
    w1t = w2t = botht = puret = 0
    w1r, w2r, cbear = set(), set(), []
    for i, p in enumerate(polys):
        cw = cf = False
        for (rk, xk), c in p.items():
            l1, l2 = rk[IW1] or rk[IHW1], rk[IW2] or rk[IHW2]
            if l1:
                w1r.add(i)
            if l2:
                w2r.add(i)
            botht, w1t, w2t, puret = (botht + (1 if l1 and l2 else 0),
                                      w1t + (1 if l1 and not l2 else 0),
                                      w2t + (1 if l2 and not l1 else 0),
                                      puret + (0 if l1 or l2 else 1))
            if not xk:                       # x-free (constant-bearing)
                if l1 or l2:
                    cw = True
                else:
                    cf = True
        if cw or cf:
            cbear.append((i, "W-loaded" if cw else "", "W-free" if cf
                          else ""))
    log("terms %d: W1-only %d, W2-only %d, both %d, W-free %d"
        % (sum(len(p) for p in polys), w1t, w2t, botht, puret))
    log("rows touching W1: %d, W2: %d" % (len(w1r), len(w2r)))
    log("constant-bearing rows (x-free terms): %s" % cbear)
    s1rows = sorted({i for i, p in enumerate(polys)
                     for (rk, xk) in p for v, e in xk if v == S1X})
    s1deg = max(e for p in polys for (rk, xk) in p for v, e in xk
                if v == S1X)
    log("s1 (=x119): %d rows, max degree %d" % (len(s1rows), s1deg))


# ------------------------------------------------------------------ build
def phase_build(only=None):
    hdr, rads, polys = load_core()
    pk = os.path.join(TMP, "leaves.pkl")
    state = {}
    if os.path.exists(pk):
        with open(pk, "rb") as f:
            state = pickle.load(f)
    for tag in (LEAVES if only is None else [only]):
        if tag in state:
            log("%s: already built, skip" % tag)
            continue
        u1, u2 = (tag[0] == "U"), (tag[1] == "U")
        rows, deadZ = chart_kill(polys, u1, u2)
        log("%s: chart kill -> %d rows (%d died), %d terms"
            % (tag, len(rows), len(deadZ),
               sum(len(p) for p in rows.values())))
        rows, subs, dropped = leaf_eliminate(rows, u1, u2, "12" + tag)
        remv = sorted({v for p in rows.values() for (rk, xk) in p
                       for v, e in xk})
        log("%s DONE: %d rows, %d x-vars, %d terms; %d elim'd, %d "
            "dropped, %d chart-killed" % (tag, len(rows), len(remv),
            sum(len(p) for p in rows.values()), len(subs), len(dropped),
            len(deadZ)))
        state[tag] = dict(rows=rows, subs=subs, dropped=dropped,
                          deadZ=deadZ, u1=u1, u2=u2)
        with open(pk, "wb") as f:
            pickle.dump(state, f)
    log("build state -> %s" % pk)


def load_state():
    with open(os.path.join(TMP, "leaves.pkl"), "rb") as f:
        return pickle.load(f)


# ------------------------------------------------------------- emission
def leaf_header(tag, remv):
    hdr = ["r3", "z", "A1", "A2"]
    if tag[0] == "U":
        hdr += ["W1", "HW1", "uW1"]
    if tag[1] == "U":
        hdr += ["W2", "HW2", "uW2"]
    hdr += ["EB"] + [("s1" if v == S1X else "x%d" % v) for v in remv]
    return hdr


def phase_emit():
    FC = import_fullcore()
    os.makedirs(LEAFDIR, exist_ok=True)
    state = load_state()
    hdr0, rads, polys = load_core()
    labels = rowlabels()
    allx = sorted({v for pl in polys for (rk, xk) in pl for v, e in xk})
    for tag in LEAVES:
        st = state[tag]
        rows, subs = st["rows"], st["subs"]
        remv = sorted({v for pl in rows.values() for (rk, xk) in pl
                       for v, e in xk})
        elimv = [v for v, u, s2, A in subs]
        freev = sorted(set(allx) - set(remv) - set(elimv))
        hdr = leaf_header(tag, remv)
        eqs = leaf_prefix_rows(tag, 0)
        npre = len(eqs)
        scales = {}
        for i in sorted(rows):
            s, sc = emit_leaf_poly(rows[i])
            eqs.append(s1name(s))
            scales[i] = sc
        path = os.path.join(LEAFDIR, "leaf12_%s.ms" % tag)
        with open(path, "w") as f:
            f.write(", ".join(hdr) + "\n0\n")
            f.write(",\n".join(eqs) + "\n")
        log("emitted %s (%d eqs, %d vars, %.2f MB)"
            % (path, len(eqs), len(hdr), os.path.getsize(path) / 1e6))
        with open(os.path.join(LEAFDIR, "leaf12_%s.rows.txt" % tag),
                  "w") as f:
            f.write("# leaf %s of r1_12branch_core.ms (cases/"
                    "r1_12_decompose.py): chart W1 %s, W2 %s; s1 "
                    "carried as x119 internally\n"
                    % (tag, "unit" if tag[0] == "U" else "= 0",
                       "unit" if tag[1] == "U" else "= 0"))
            f.write("# %d elim'd, %d survivors, %d dropped-as-zero, "
                    "free x's %s\n" % (len(subs), len(rows),
                                       len(st["dropped"]), freev))
            for j, (v, u, s2, A) in enumerate(subs):
                f.write("elim%d: %s via row %d (%s) |s|=%d\n"
                        % (j, "s1" if v == S1X else "x%d" % v, A,
                           labels.get(A, "?"), len(s2)))
            for j in range(npre):
                f.write("eq%d = chart/radical row\n" % j)
            for j, i in enumerate(sorted(rows)):
                f.write("eq%d = row %d (%s)\n"
                        % (npre + j, i, labels.get(i, "?")))
        for p in FC.good_primes(2):
            pt = FC.radical_point(p)
            weqs = leaf_prefix_rows(tag, p, p) \
                + [s1name(s) for s in emit_wfree_rows(rows, scales, p, pt)]
            whdr = [h for h in hdr
                    if h in ("W1", "HW1", "uW1", "W2", "HW2", "uW2")
                    or h[0] == "x" or h == "s1"]
            wp = os.path.join(LEAFDIR, "leaf12_%s_wfree_p%d.ms"
                              % (tag, p))
            with open(wp, "w") as f:
                f.write(", ".join(whdr) + "\n%d\n" % p)
                f.write(",\n".join(weqs) + "\n")
            log("emitted %s (%d eqs, %d vars, %.2f MB)"
                % (wp, len(weqs), len(whdr),
                   os.path.getsize(wp) / 1e6))


# --------------------------------------------------------------- guards
def _xval_named(remv, xv):
    return {("s1" if v == S1X else "x%d" % v): xv[v] for v in remv}


def phase_guards():
    FC = import_fullcore()
    state = load_state()
    hdr0, rads, polys = load_core()
    allx = sorted({v for pl in polys for (rk, xk) in pl for v, e in xk})
    for tag in LEAVES:
        st = state[tag]
        rows, subs = st["rows"], st["subs"]
        idx = sorted(rows)
        remv = sorted({v for pl in rows.values() for (rk, xk) in pl
                       for v, e in xk})
        scales = {i: emit_leaf_poly(rows[i])[1] for i in idx}
        files = ["leaf12_%s.ms" % tag] + \
                ["leaf12_%s_wfree_p%d.ms" % (tag, p)
                 for p in FC.good_primes(2)]
        for fn in files:  # guard A
            txt = open(os.path.join(LEAFDIR, fn)).read()
            assert "(" not in txt and ")" not in txt, ("PAREN", fn)
        log("%s guard A (paren sweep, 3 files): PASS" % tag)
        npre = len(leaf_prefix_rows(tag, 0))
        for p in FC.good_primes(2):  # guard B
            pt = chart_point(FC, p, tag)
            rng = random.Random(4412 + p)
            xv = {v: rng.randrange(1, p) for v in remv}
            val = dict(pt)
            val.update(_xval_named(remv, xv))
            eqs0 = open(os.path.join(LEAFDIR, "leaf12_%s.ms" % tag)) \
                .read().split("\n", 2)[2].strip().rstrip(",") \
                .split(",\n")[npre:]
            nprew = len(leaf_prefix_rows(tag, p, p))
            eqsw = open(os.path.join(
                LEAFDIR, "leaf12_%s_wfree_p%d.ms" % (tag, p))) \
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
            log("%s guard B (round-trip char0+wfree, p=%d): PASS %d/%d "
                "rows, %d nonzero" % (tag, p, len(idx), len(idx), nz))
        p = FC.good_primes(1)[0]  # guard C
        pt = chart_point(FC, p, tag)
        x0 = {v: 0 for v in remv}
        n0 = sum(1 for i in idx
                 if eval_poly_modp(rows[i], pt, p, x0) == 0)
        log("%s guard C (x=0,s1=0 at generic chart point): %d/%d rows "
            "vanish -> %s" % (tag, n0, len(idx),
                              "ORIGIN-SATISFIABLE" if n0 == len(idx)
                              else "origin excluded"))
        dead = set(idx)  # guard D
        for p in FC.good_primes(2):
            for t in range(3):
                pt = chart_point(FC, p, tag, seed=1 + t)
                rng = random.Random(9512 + p * 10 + t)
                xv = {v: rng.randrange(1, p) for v in remv}
                for i in sorted(dead):
                    if eval_poly_modp(rows[i], pt, p, xv):
                        dead.discard(i)
        assert not dead, (tag, dead)
        log("%s guard D (residual): PASS, 0 identically-zero rows" % tag)
        elimset = {v for v, u, s2, A in subs}
        for p in FC.good_primes(2):  # guard E
            for t in range(2):
                pt = chart_point(FC, p, tag, seed=1 + t)
                rng = random.Random(5612 + p * 10 + t)
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
                    assert eval_poly_modp(polys[i], pt, p, xv) \
                        == eval_poly_modp(rows[i], pt, p, xv), \
                        ("SURV", tag, i)
            log("%s guard E (soundness/back-map, p=%d): PASS -- %d "
                "pivot + %d dropped rows vanish; %d survivors == "
                "original rows" % (tag, p, len(subs),
                                   len(st["dropped"]), len(idx)))


def phase_cover():
    FC = import_fullcore()
    hdr0, rads, polys = load_core()
    rng = random.Random(7712)
    p = FC.good_primes(1)[0]
    for _ in range(500):  # (i) tautology
        w1, w2 = rng.randrange(p), rng.randrange(p)
        pats = [(w1 == 0) == (a == "Z") and (w2 == 0) == (b == "Z")
                for a, b in LEAVES]
        assert sum(pats) == 1
    log("cover (i): 500 random (W1,W2) samples each match EXACTLY ONE "
        "of the 4 patterns PASS")
    log("cover (ii): quadric at W_i=0 reads 2*HW_i^2 = 0 -> HW_i = 0 "
        "on the variety (char != 2) -- Z-charts substitute both")
    # (iii) REPLACED (sec 15.0): origin census on the RAW core, all 4
    # W-patterns, x = s1 = 0; the (1,2) core has 10 constant-bearing
    # rows -- measure whether their constants survive each W-pattern.
    for pp in FC.good_primes(2):
        pt = dict(FC.radical_point(pp))
        x0 = {v: 0 for v in range(120)}
        for tag in LEAVES:
            q = dict(pt)
            if tag[0] == "Z":
                q["W1"] = q["HW1"] = 0
            if tag[1] == "Z":
                q["W2"] = q["HW2"] = 0
            bad = [i for i, pl in enumerate(polys)
                   if eval_poly_modp(pl, q, pp, x0)]
            log("cover (iii') p=%d pattern %s: origin x=s1=0 leaves %d/"
                "%d rows NONZERO %s" % (pp, tag, len(bad), len(polys),
                                        ("(rows %s)" % bad[:12])
                                        if bad else
                                        "-> ORIGIN POINT EXISTS"))


# ------------------------------------------------------------ calibrate
def phase_calibrate(timeout=900):
    FC = import_fullcore()
    logf = os.path.join(RUNS, "r1_12leaves_calibrate.log")
    jobs = []
    for tag in LEAVES:
        for p in FC.good_primes(2):
            jobs.append(("leaf12_%s_wfree_p%d.ms" % (tag, p), tag, p))
    for tag in LEAVES:
        jobs.append(("leaf12_%s.ms" % tag, tag, 0))  # char-0 runs
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
    """multi-prime confirmation at n fresh primes (good_primes walk;
    NOT r1_reduce.sweepw_primes -- 13.6 bug note)."""
    FC = import_fullcore()
    state = load_state()
    banked = FC.good_primes(2)
    primes = [p for p in FC.good_primes(n + 2) if p not in banked][:n]
    logf = os.path.join(RUNS, "r1_12leaves_calibrate.log")
    for p in primes:
        pt = FC.radical_point(p)
        for tag in LEAVES:
            rows = state[tag]["rows"]
            scales = {i: emit_leaf_poly(rows[i])[1] for i in sorted(rows)}
            remv = sorted({v for pl in rows.values() for (rk, xk) in pl
                           for v, e in xk})
            weqs = leaf_prefix_rows(tag, p, p) \
                + [s1name(s) for s in emit_wfree_rows(rows, scales, p, pt)]
            whdr = [h for h in leaf_header(tag, remv)
                    if h in ("W1", "HW1", "uW1", "W2", "HW2", "uW2")
                    or h[0] == "x" or h == "s1"]
            wp = os.path.join(TMP, "leaf12_%s_wfree_p%d.ms" % (tag, p))
            with open(wp, "w") as f:
                f.write(", ".join(whdr) + "\n%d\n" % p)
                f.write(",\n".join(weqs) + "\n")
            out = os.path.join(RUNS, "leaf12_%s_wfree_p%d.sweep.out"
                               % (tag, p))
            verdict, wall, rss = run_msolve_rss(wp, out, 900)
            line = "sweep %s p=%d: %s wall %.1fs" % (tag, p, verdict,
                                                     wall)
            log(line)
            with open(logf, "a") as f:
                f.write(line + "\n")


# ------------------------------------------------------- explicit witness
def phase_witness():
    """explicit UU-chart witness of the (1,2) core at both banked
    primes: the UU residual is c*E with E EXACTLY the sec-13.1
    relation (15.1), so the 13.4 construction ports: solve E for W1
    (W2 = 1), HW_i = sqrt(3/2) W_i, free x's = s1 = 0, back-map the
    35 UU subs, verify ALL 105 emitted eqs with the independent
    parser (single back-map layer -- no sec-10 stage exists here)."""
    FC = import_fullcore()
    uu = load_state()["UU"]
    hdrC, charC, eqsC = parse_ms(CORE)
    for p in FC.good_primes(2):
        pt = dict(FC.radical_point(p))
        inv = lambda a: pow(a, p - 2, p)
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
                s2r = RD.tonelli(c, p)
                w1 = RD.tonelli(s2r, p) if s2r is not None else None
                if w1 is not None:
                    got = (A1, A2, w1, i, j)
                    break
            if got:
                break
        assert got, "no rational 4th root at p=%d" % p
        A1, A2, W1, i, j = got
        shw = pt["HW1"] * inv(pt["W1"]) % p            # sqrt(3/2)
        val = dict(pt, A1=A1, A2=A2, W1=W1, W2=1,
                   HW1=shw * W1 % p, HW2=shw)
        xv = {v: 0 for v in range(120)}                # free x's + s1 = 0
        for v, u, s2, A in reversed(uu["subs"]):
            xv[v] = eval_poly_modp(s2, val, p, xv)
        val.update({"x%d" % v: xv[v] for v in xv})
        val["s1"] = xv[S1X]
        bad = [k for k, g in enumerate(FC.parse_eval(eqsC, val, p)) if g]
        assert not bad, (p, bad)
        log("WITNESS p=%d: W1=%d, W2=1 (both nonzero), A-embedding "
            "(om^%d, om^%d), s1=%d: ALL %d emitted (1,2)-core eqs "
            "vanish (independent parser) -- explicit intended-chart "
            "point" % (p, W1, i, j, val["s1"], len(eqsC)))


if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "stats"
    if ph == "stats":
        phase_stats()
    elif ph == "build":
        phase_build(sys.argv[2] if len(sys.argv) > 2 else None)
    elif ph == "emit":
        phase_emit()
    elif ph == "guards":
        phase_guards()
    elif ph == "cover":
        phase_cover()
    elif ph == "calibrate":
        phase_calibrate(int(sys.argv[2]) if len(sys.argv) > 2 else 900)
    elif ph == "psweep":
        phase_psweep(int(sys.argv[2]) if len(sys.argv) > 2 else 6)
    elif ph == "witness":
        phase_witness()
