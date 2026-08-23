"""r1_minimal_ext.py -- minimal-branch EXTENDED decision system
(SHEET6-R1.md sec 14; ADDITIVE, mirrors the (2,5) rung-extension sec 12).

System = UU-chart core + deferred F_s-band rows, lowest rungs:
  core part  : r1_full_core.ms VERBATIM (105 eqs; regression gate byte-
               identity).  The UNREDUCED core is used because the F_s
               rows re-engage bf_18/bf_24/bf_30 (= core x37/x43/x49),
               which the sec-10 pre-reduction eliminated; the reduced/
               leaf compressions are not sound on the extended var set.
  chart rows : uW1*W1-1, uW2*W2-1 (Rabinowitsch inverses -- sec 13:
               ZU/UZ EMPTY at 8 primes, ZZ relaxation artifact; the UU
               chart carries the diagnostic verdict).
  ext rows   : W_F band rows WF[(n,s)] = 0, 1 <= s <= 24 (rungs
               r = s/6 = 1..4 on the 1/7-lattice; W_F = gF^2 - fF^3 in
               the F_s window, exact full var-degree, slot-truncated
               at SCAP = 25; truncation-first is exact for kept slots).

Phases: fsjets | wf | emit | guards | run   (state /tmp/r1mext)
AUDIT: expanded integer monomials, no parens; p-variants fully
coefficient-reduced into [0,p) incl. radical rows (reduce_eq_str).
"""
import os, re, sys, time, pickle, random
from fractions import Fraction as Fr
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import r1_experiment as R1
import r1_fullcore as FC

SCAP = 25                     # slots 0..24 kept: rungs r = 1..4 (s = 6r)
RUNGS = (6, 12, 18, 24)
TMP = "/tmp/r1mext"
os.makedirs(TMP, exist_ok=True)
SYS = FC.OUT_DIR
RUNS = os.path.join(os.path.dirname(HERE), "runs")
BASE = "r1_minimal_ext"


def log(msg):
    print("[%s] %s" % (time.strftime("%H:%M:%S"), msg), flush=True)


def save(name, obj):
    with open(os.path.join(TMP, name), "wb") as f:
        pickle.dump(obj, f)


def load(name):
    with open(os.path.join(TMP, name), "rb") as f:
        return pickle.load(f)


# ---------------------------------------------- rnorm memo (8.11 lesson)
# rnorm(key, c) is EXACTLY linear in c (all ops: c * key-determined
# constants); memoize the key-part.  A/B-tested at patch time below.
_RNORM_MEMO = {}
_rnorm_orig = R1.rnorm


def _rnorm_memo(key, c):
    hit = _RNORM_MEMO.get(key)
    if hit is None:
        hit = _RNORM_MEMO[key] = tuple(_rnorm_orig(key, R1.K1))
    return [(k2, c * f) for k2, f in hit]


def _patch_rnorm():
    rng = random.Random(31)
    for _ in range(300):
        key = tuple(rng.randrange(-6, 12) if i in (1, 2) else
                    rng.randrange(0, 60) if i in (0, 7) else
                    rng.randrange(0, 6) for i in range(8))
        c = R1.K3(Fr(rng.randrange(-9, 9), rng.randrange(1, 7)),
                  Fr(rng.randrange(-9, 9), rng.randrange(1, 7)))
        if c.iszero():
            continue
        a = sorted((k, tuple(v)) for k, v in _rnorm_orig(key, c))
        b = sorted((k, tuple(v)) for k, v in _rnorm_memo(key, c))
        assert a == b, ("rnorm memo A/B mismatch", key)
    R1.rnorm = _rnorm_memo


_patch_rnorm()


# ------------------------------------------------------------ F_s jets
def fs_orbit_fold(orb, scap):
    """exact F_s-window product for one orbit over all 7 directions x
    suborbit factors, SEQUENTIAL linear-factor fold (dense x sparse --
    the sec-8.12 shape lesson).  Factor (k, j): (n,s) entries
    (1,0) -> zeta^{12k}, (0,s) -> -zeta^{(k+7j)s} * Ytilde_s.
    Identical math to fs_jet (rep-then-image); slot truncation at scap
    is exact for kept slots (slots additive nonnegative)."""
    yt = {lv - 12: v for lv, v in orb["series"].items() if lv - 12 < scap}
    jp = R1.JONE
    n7 = R1.C7SUB[orb["size"]]
    t0, nf = time.time(), 0
    for k in range(7):
        for j in range(n7):
            fac = {(1, 0): {(): R1.rmono(za=(12 * k) % 42)}}
            for s, v in yt.items():
                tw = R1.vscal(v, R1.rmono(za=((k + 7 * j) * s) % 42,
                                          c=R1.K3(-1)))
                if tw:
                    fac[(0, s)] = tw
            jp = R1.jmul(jp, fac, scap)
            nf += 1
            if nf % 7 == 0 and scap > 7:
                log("    %s factor %d/%d: %d keys %d terms (%.1fs)"
                    % (orb["name"], nf, 7 * n7, len(jp),
                       sum(len(v) for v in jp.values()), time.time() - t0))
    return jp


def assert_no_hivar(jet, tag):
    for v in jet.values():
        for vk in v:
            assert not (vk and vk[-1] == R1.HIVAR), "HIVAR in %s" % tag


def grading_census(jet, tag):
    # measured on the banked orbit folds: 12n + s == 0 (mod 42)
    # (sec-3 prose "s = 12n" has the sign flipped; 6-grid unaffected)
    bad = [(n, s) for (n, s) in jet if (12 * n + s) % 42]
    log("%s grading 12n + s == 0 (mod 42): %d keys, %d violations"
        % (tag, len(jet), len(bad)))
    return bad


def phase_fsjets():
    orbs = FC.build_orbs()
    t0 = time.time()
    jets = {}
    for tag, names in (("f", R1.FORB), ("g", R1.GORB)):
        jp = R1.JONE
        for on in names:
            ck = "orb_%s.pkl" % on
            if os.path.exists(os.path.join(TMP, ck)):
                ob = load(ck)
                log("fsjets %s: orbit %s loaded from checkpoint" % (tag, on))
            else:
                ob = R1.fs_block(orbs[on], SCAP)
                save(ck, ob)
            jp = R1.jmul(jp, ob, SCAP)
            log("fsjets %s: orbit %s folded (%d keys, %d terms, %.1fs)"
                % (tag, on, len(jp), sum(len(v) for v in jp.values()),
                   time.time() - t0))
        assert_no_hivar(jp, tag)
        jets[tag] = jp
    # anchors: slot-0 patterns (stage-0 identities) + grading census
    p21, pm = R1.k3poly_pow_pattern()
    p6 = [R1.K1]
    for _ in range(6):
        p6 = pm(p6, p21)
    p9 = [R1.K1]
    for _ in range(9):
        p9 = pm(p9, p21)
    assert R1.jet_matches_Tpoly(jets["f"], p6), "f slot-0 != p21^6"
    assert R1.jet_matches_Tpoly(jets["g"], p9), "g slot-0 != p21^9"
    log("anchors: f-jet slot-0 == p21^6, g-jet slot-0 == p21^9 (S_F = "
        "G_F = 1) PASS")
    badf = grading_census(jets["f"], "f")
    badg = grading_census(jets["g"], "g")
    assert not badf and not badg, "F_s grading violated"
    # independent-path cross-check at cap 7: fs_block (Newton) vs
    # fs_jet (rep-then-image) vs the sequential linear-factor fold,
    # exact dict equality per orbit
    for on in R1.FORB + R1.GORB:
        ref = R1.fs_jet((on,), orbs, 7)
        assert R1.fs_block(orbs[on], 7) == ref, "block!=jet %s" % on
        assert fs_orbit_fold(orbs[on], 7) == ref, "fold!=jet %s" % on
    log("cross-check: fs_block == fs_jet == sequential fold at slot "
        "cap 7, all 9 orbits, exact dict equality PASS")
    save("fsjets.pkl", dict(jf=jets["f"], jg=jets["g"],
                            nvars=len(R1.VARS)))
    log("fsjets banked (%.1fs)" % (time.time() - t0))


# ------------------------------------------------------------- W_F rows
def phase_wf():
    st = load("fsjets.pkl")
    jf, jg = st["jf"], st["jg"]
    t0 = time.time()
    f2 = R1.jmul(jf, jf, SCAP)
    log("f^2: %d keys %d terms (%.1fs)"
        % (len(f2), sum(len(v) for v in f2.values()), time.time() - t0))
    f3 = R1.jmul(f2, jf, SCAP)
    log("f^3: %d keys %d terms (%.1fs)"
        % (len(f3), sum(len(v) for v in f3.values()), time.time() - t0))
    g2 = R1.jmul(jg, jg, SCAP)
    log("g^2: %d keys %d terms (%.1fs)"
        % (len(g2), sum(len(v) for v in g2.values()), time.time() - t0))
    WF = R1.jadd(g2, R1.jscal(f3, R1.K3(-1)))
    assert_no_hivar(WF, "WF")
    slot0 = [(n, s) for (n, s) in WF if s == 0]
    assert not slot0, "E1 anchor broken: WF slot-0 nonzero %s" % slot0[:3]
    log("E1 anchor: WF slot-0 identically zero (g^2 top == f^3 top) PASS")
    bad = grading_census(WF, "WF")
    assert not bad
    offgrid = sorted({s for (n, s) in WF if s % 6})
    assert not offgrid, "off-6-grid W_F content at slots %s" % offgrid
    rows = []
    for (n, s), v in sorted(WF.items()):
        if 1 <= s <= SCAP - 1 and v:
            rows.append((("Fs-band", n, s), v))
    per = {}
    for (lab, n, s), v in rows:
        per.setdefault(s, []).append((n, len(v)))
    for s in sorted(per):
        log("rung r=%d (slot %d): %d rows, %d terms, n in [%d..%d]"
            % (s // 6, s, len(per[s]), sum(t for _, t in per[s]),
               min(n for n, _ in per[s]), max(n for n, _ in per[s])))
    save("wf.pkl", dict(rows=rows))
    log("wf banked: %d F_s-band rows total (%.1fs)"
        % (len(rows), time.time() - t0))


# -------------------------------------------------------------- emission
def core_name_map():
    """emitted-x -> registry-vid map: banked r1_full_core.rows.txt
    (ground truth) + blocks.pkl vmeta (name -> vid)."""
    vm = FC.load("blocks.pkl")["vmeta"]
    byname = {m["name"]: i for i, m in enumerate(vm)}
    names = {}
    for line in open(os.path.join(SYS, "r1_full_core.rows.txt")):
        m = re.match(r"(x\d+) = (\S+) \(level", line)
        if m:
            names[byname[m.group(2)]] = m.group(1)
    assert len(names) == 119, len(names)
    return names, vm


def ext_names(rows):
    """extend the banked map with newly-occurring registry vars
    (sorted vid order), continuing the compact enumeration at x119."""
    names, vm = core_name_map()
    occ = sorted({vid for _, v in rows for vk in v for vid in vk})
    new = [vid for vid in occ if vid not in names]
    for i, vid in enumerate(new):
        names[vid] = "x%d" % (119 + i)
    return names, new, vm


def row_scale(v, names):
    """the exact denominator-clearing/content scale emit_expanded uses."""
    terms = R1.poly_terms(v, names)
    L = 1
    for q, _ in terms:
        L = L * q.denominator // gcd(L, q.denominator)
    G = 0
    for q, _ in terms:
        G = gcd(G, abs((q * L).numerator))
    return Fr(L, G) if G > 1 else Fr(L)


def spec_fs_row(v, pt, p, names, scale):
    """wfree emission of one F_s row: etale gens specialized at pt,
    coefficients scaled like the char-0 emission, reduced into [0,p)."""
    acc = {}
    sc = FC.frmod(scale, p)
    for vk, r in v.items():
        for key in r:
            assert key[3] == key[4] == key[5] == key[6] == 0, \
                "W-loaded F_s row?!"
        c = FC.ring_modp(r, pt, p) * sc % p
        if c:
            acc[vk] = c
    parts = []
    for vk in sorted(acc):
        mono = []
        for vid in sorted(set(vk)):
            e = vk.count(vid)
            mono.append(names[vid] + ("^%d" % e if e > 1 else ""))
        parts.append("%d%s" % (acc[vk], "".join("*" + m for m in mono)))
    return "+".join(parts) if parts else "0"


def parse_ms(path):
    lines = open(path).read().split("\n", 2)
    hdr = [h.strip() for h in lines[0].split(",")]
    char = int(lines[1].strip())
    eqs = [e.strip() for e in lines[2].strip().rstrip(",").split(",\n")]
    return hdr, char, eqs


def phase_emit():
    rows = load("wf.pkl")["rows"]
    names, new, vm = ext_names(rows)
    hdr0, char0, eqs0 = parse_ms(os.path.join(SYS, "r1_full_core.ms"))
    assert char0 == 0 and len(eqs0) == 105, (char0, len(eqs0))
    chart = ["uW1*W1-1", "uW2*W2-1"]
    t0 = time.time()
    fs_eqs = []
    for i, (meta, v) in enumerate(rows):
        fs_eqs.append(R1.emit_expanded(v, names))
        if (i + 1) % 50 == 0:
            log("emitted %d/%d F_s rows (%.1fs)"
                % (i + 1, len(rows), time.time() - t0))
    eqs = eqs0 + chart + fs_eqs
    hdr = hdr0 + ["uW1", "uW2"] + [names[v] for v in new]
    path = os.path.join(SYS, BASE + ".ms")
    with open(path, "w") as f:
        f.write(", ".join(hdr) + "\n0\n")
        f.write(",\n".join(eqs) + "\n")
    # regression gate: core block byte-identical to the banked emission
    _, _, back = parse_ms(path)
    assert back[:105] == eqs0, "REGRESSION GATE: core block changed"
    log("emitted %s (%d eqs, %d vars, %.1f MB); regression gate: first "
        "105 eqs BYTE-IDENTICAL to r1_full_core.ms PASS"
        % (path, len(eqs), len(hdr), os.path.getsize(path) / 1e6))
    corelabs = []
    for line in open(os.path.join(SYS, "r1_full_core.rows.txt")):
        m = re.match(r"eq\d+ = (.*)", line)
        if m:
            corelabs.append(m.group(1).strip())
    assert len(corelabs) == 105
    with open(os.path.join(SYS, BASE + ".rows.txt"), "w") as f:
        f.write("# minimal-branch EXTENDED system (sec 14): full core "
                "(verbatim) + UU chart + F_s-band rungs r=1..4\n")
        for i, lab in enumerate(corelabs):
            f.write("eq%d = %s\n" % (i, lab))
        f.write("eq105 = chart row uW1*W1-1\neq106 = chart row uW2*W2-1\n")
        for j, (meta, v) in enumerate(rows):
            f.write("eq%d = %s\n" % (107 + j, meta))
        for vid, nm in sorted(names.items(), key=lambda t: int(t[1][1:])):
            f.write("%s = %s (level %d)\n"
                    % (nm, vm[vid]["name"], vm[vid]["level"]))
    for p in FC.good_primes(2):
        pp = os.path.join(SYS, BASE + "_p%d.ms" % p)
        with open(pp, "w") as f:
            f.write(", ".join(hdr) + "\n%d\n" % p)
            f.write(",\n".join(FC.reduce_eq_str(eq, p) for eq in eqs)
                    + "\n")
        log("emitted %s (%.1f MB, coeffs in [0,p) incl. radical rows)"
            % (pp, os.path.getsize(pp) / 1e6))
    for p in FC.good_primes(2):
        hdrw, charw, eqsw = parse_ms(
            os.path.join(SYS, "r1_full_core_wfree_p%d.ms" % p))
        assert charw == p and len(eqsw) == 100, (charw, len(eqsw))
        pt = FC.radical_point(p)
        weqs = eqsw + ["uW1*W1+%d" % (p - 1), "uW2*W2+%d" % (p - 1)]
        for meta, v in rows:
            weqs.append(spec_fs_row(v, pt, p, names, row_scale(v, names)))
        whdr = hdrw + ["uW1", "uW2"] + [names[v] for v in new]
        wp = os.path.join(SYS, BASE + "_wfree_p%d.ms" % p)
        with open(wp, "w") as f:
            f.write(", ".join(whdr) + "\n%d\n" % p)
            f.write(",\n".join(weqs) + "\n")
        log("emitted %s (%d eqs, %d vars, %.1f MB)"
            % (wp, len(weqs), len(whdr), os.path.getsize(wp) / 1e6))


# --------------------------------------------------------------- guards
def witness_point(p):
    """port of sec-13.4: explicit intended-chart (UU) point of the FULL
    core at prime p, via both banked back-maps; new ext vars -> 0."""
    import r1_decompose as RD
    state = RD.load_state()
    uu = state["UU"]
    with open("/tmp/r1red/reduced.pkl", "rb") as f:
        red = pickle.load(f)
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
                got = (A1, A2, w1)
                break
        if got:
            break
    assert got, "no 4th root at p=%d" % p
    A1, A2, W1 = got
    shw = pt["HW1"] * inv(pt["W1"]) % p
    val = dict(pt, A1=A1, A2=A2, W1=W1, W2=1,
               HW1=shw * W1 % p, HW2=shw)
    val["uW1"], val["uW2"] = inv(W1), 1
    xv = {v: 0 for v in range(119)}
    for v, u, s2, A in reversed(uu["subs"]):
        xv[v] = RD.eval_poly_modp(s2, val, p, xv)
    for v, u, s2, A in reversed(red["subs"]):
        xv[v] = RD.eval_poly_modp(s2, val, p, xv)
    val.update({"x%d" % v: xv[v] for v in xv})
    return val


def phase_guards():
    rows = load("wf.pkl")["rows"]
    names, new, vm = ext_names(rows)
    nfs = len(rows)
    files = [BASE + ".ms"] + \
        [BASE + "_p%d.ms" % p for p in FC.good_primes(2)] + \
        [BASE + "_wfree_p%d.ms" % p for p in FC.good_primes(2)]
    for fn in files:                                          # guard A
        txt = open(os.path.join(SYS, fn)).read()
        assert "(" not in txt and ")" not in txt, ("PAREN", fn)
    log("guard A (paren sweep, %d files): PASS" % len(files))
    hdr, _, eqs = parse_ms(os.path.join(SYS, BASE + ".ms"))
    scales = {i: row_scale(v, names) for i, (m, v) in enumerate(rows)}
    for p in FC.good_primes(2):                               # guard B
        pt = FC.radical_point(p)
        _, _, peqs = parse_ms(os.path.join(SYS, BASE + "_p%d.ms" % p))
        _, _, weqs = parse_ms(os.path.join(SYS,
                                           BASE + "_wfree_p%d.ms" % p))
        evals = []
        for t in range(2):
            rng = random.Random(6100 + p + 31 * t)
            val = dict(pt)
            val["uW1"] = pow(pt["W1"], p - 2, p)
            val["uW2"] = pow(pt["W2"], p - 2, p)
            for h in hdr:
                if h.startswith("x"):
                    val[h] = rng.randrange(1, p)
            g0 = FC.parse_eval(eqs, val, p)
            gp = FC.parse_eval(peqs, val, p)
            gw = FC.parse_eval(weqs, val, p)
            assert g0 == gp, "char0 vs p-variant mismatch"
            xval = {vid: val[nm] for vid, nm in names.items()}
            nz = 0
            for i, (meta, v) in enumerate(rows):
                want = FC.eval_vex_modp(v, pt, p, xval) \
                    * FC.frmod(scales[i], p) % p
                assert g0[107 + i] == want, ("FS-RT0", meta)
                assert gw[102 + i] == want, ("FS-RTW", meta)
                nz += want != 0
            assert g0[105] == gw[100] and g0[106] == gw[101]
            evals.append((g0, gw))
        # banked wfree core rows are UNSCALED specializations while the
        # char-0 emission is content-normalized: compare up to a per-row
        # scalar via the two-point cross-ratio (sec-12 guard E(i) style)
        (a0, aw), (b0, bw) = evals
        for i in range(98):
            assert aw[2 + i] and bw[2 + i], ("wfree row vanished", i)
            assert a0[7 + i] * bw[2 + i] % p == b0[7 + i] * aw[2 + i] \
                % p, ("wfree core cross-ratio", i)
        log("guard B (round-trip char0+p-variant exact; wfree core "
            "cross-ratio 2 pts; F_s rows exact vs internal VExpr eval, "
            "p=%d): PASS; %d/%d F_s rows nonzero at random point"
            % (p, nz, nfs))
    p = FC.good_primes(1)[0]                                  # guard C
    pt = FC.radical_point(p)
    val = dict(pt, uW1=pow(pt["W1"], p - 2, p),
               uW2=pow(pt["W2"], p - 2, p))
    for h in hdr:
        if h.startswith("x"):
            val[h] = 0
    g0 = FC.parse_eval(eqs, val, p)
    nzc = [i for i, g in enumerate(g0) if g]
    fs0 = [i for i in nzc if i >= 107]
    assert nzc, "origin satisfies the system?!"
    log("guard C (x=0 at generic UU chart point): %d/%d rows nonzero "
        "(all in the slot-20 quotient family: %s) -> origin excluded; "
        "F_s rows with constant term: %d (band rows are prefix-exact)"
        % (len(nzc), len(eqs), nzc if len(nzc) < 15 else "...", len(fs0)))
    dead = set(range(len(eqs)))                               # guard D
    for p in FC.good_primes(2):
        for t in range(3):
            rng = random.Random(7300 + p * 10 + t)
            val = {h: rng.randrange(1, p) for h in hdr}
            g0 = FC.parse_eval(eqs, val, p)
            dead -= {i for i, g in enumerate(g0) if g}
    assert not dead, ("identically-zero rows", sorted(dead))
    log("guard D (residual, 6 random point/prime combos, ALL vars "
        "random): PASS -- 0 identically-zero rows of %d" % len(eqs))
    for p in FC.good_primes(2):                               # guard E
        val = witness_point(p)
        for h in hdr:
            if h not in val:
                val[h] = 0
        g0 = FC.parse_eval(eqs, val, p)
        core_bad = [i for i in range(107) if g0[i]]
        assert not core_bad, ("witness fails core rows", core_bad)
        fs_nz = [i - 107 for i in range(107, len(eqs)) if g0[i]]
        log("guard E (sec-13.4 witness, p=%d): ALL 105 core + 2 chart "
            "rows vanish (emission validated); F_s rows nonzero at "
            "witness: %d/%d -> %s"
            % (p, len(fs_nz), nfs,
               "NON-VACUOUS extension" if fs_nz else
               "VACUOUS -- escalate one rung (pre-registered fallback)"))


# ------------------------------------------------------------------ run
def phase_run(timeout=900):
    import r1_decompose as RD
    logf = os.path.join(RUNS, BASE + "_runs.log")
    walls = []
    for p in FC.good_primes(2):
        fn = BASE + "_wfree_p%d.ms" % p
        out = os.path.join(RUNS, fn + ".out")
        verdict, wall, rss = RD.run_msolve_rss(
            os.path.join(SYS, fn), out, timeout, threads=4)
        walls.append(wall)
        line = "%s: %s wall %.1fs rss %.1f MB" % (fn, verdict, wall,
                                                  rss / 1024.0)
        log(line)
        with open(logf, "a") as f:
            f.write(line + "\n")
    if max(walls) < 300:
        fn = BASE + ".ms"
        out = os.path.join(RUNS, fn + ".out")
        verdict, wall, rss = RD.run_msolve_rss(
            os.path.join(SYS, fn), out, timeout, threads=4)
        line = "%s (char 0): %s wall %.1fs rss %.1f MB" \
            % (fn, verdict, wall, rss / 1024.0)
        log(line)
        with open(logf, "a") as f:
            f.write(line + "\n")
    else:
        log("p-screens exceeded 300 s -- char-0 deferred (box01 note)")


def phase_orb(on):
    """parallel worker: fold ONE orbit at SCAP, bank checkpoint."""
    orbs = FC.build_orbs()
    ck = "orb_%s.pkl" % on
    if os.path.exists(os.path.join(TMP, ck)):
        log("orb %s: checkpoint exists, skipping" % on)
        return
    t0 = time.time()
    ob = R1.fs_block(orbs[on], SCAP)   # Newton path (6x the linear fold)
    save(ck, ob)
    log("orb %s banked: %d keys %d terms (%.1fs)"
        % (on, len(ob), sum(len(v) for v in ob.values()),
           time.time() - t0))


if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "fsjets"
    if ph == "orb":
        phase_orb(sys.argv[2])
    elif ph == "fsjets":
        phase_fsjets()
    elif ph == "wf":
        phase_wf()
    elif ph == "emit":
        phase_emit()
    elif ph == "guards":
        phase_guards()
    elif ph == "run":
        phase_run()
