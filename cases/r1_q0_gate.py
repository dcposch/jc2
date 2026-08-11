"""r1_q0_gate.py -- Q0 gate: depth-84 slot-60 witness-specialized
quotient sub-block of the minimal-branch F_s ladder (SHEET6-R1.md sec
16; plan/pre-registration sec 16.0, semantics sec 15.6).  ADDITIVE.

Per banked prime p:
  - depth-84 registry (build_generators(84)); witness values carried by
    registry NAME (banked 135 emitted vars = sec-13.4 point + sec-14
    zero ext); every UNBANKED registry var at level <= 72 SYMBOLIC.
  - orbit series specialized mod p, folded at slot cap 61 by TWO paths
    (sequential linear-factor fold / suborbit-Newton), equality asserted.
  - W_F = g^2 - f^3; Q0 rows = WF(n,60) - s1F*c_n, c_n the eta^2-shifted
    p21^8 pattern (sec 3 C2 quotient == c*p21^8; H_F^3 = s1F S_F^4).
  - anchors A1-A5 (sec 16.0) must ALL pass before rows are trusted.

Phases: gate [p] | emit | run | all      (state /tmp/r1q0)
AUDIT: expanded integer monomials, no parens, coeffs in [0,p).
"""
import os, re, sys, time, pickle
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import r1_experiment as R1
import r1_fullcore as FC
import r1_minimal_ext as ME          # witness_point, core_name_map, memo

SCAP = 61                            # slots 0..60 kept (levels 12..72)
LVMAX = 72                           # slot 60
TMP = "/tmp/r1q0"
os.makedirs(TMP, exist_ok=True)
SYS = FC.OUT_DIR
RUNS = os.path.join(os.path.dirname(HERE), "runs")
BASE = "r1_q0"


def log(msg):
    print("[q0 %s] %s" % (time.strftime("%H:%M:%S"), msg), flush=True)


def save(name, obj):
    with open(os.path.join(TMP, name), "wb") as f:
        pickle.dump(obj, f)


def load(name):
    with open(os.path.join(TMP, name), "rb") as f:
        return pickle.load(f)


# ------------------------------------------------- witness by NAME
def banked_values(p):
    """dict registry-NAME -> witness value mod p (the 135 banked emitted
    vars: 119 core via rows.txt map + 16 sec-14 ext vars, all = 0 at the
    witness by sec-14 guard E), plus the radical point."""
    val = ME.witness_point(p)                  # sec-13.4 point, xN keys
    names54, vm54 = ME.core_name_map()         # vid54 -> xN (119 entries)
    wval = {vm54[vid]["name"]: val[xn] for vid, xn in names54.items()}
    ext = [ln.split(" = ") for ln in
           open(os.path.join(SYS, "r1_minimal_ext.rows.txt"))
           if re.match(r"x\d+ = ", ln)]
    assert len(ext) == 135, len(ext)
    for xn, rest in ext:
        nm = rest.split(" (")[0]
        if nm not in wval:
            wval[nm] = 0                       # sec-14 ext vars: 0 at witness
    assert len(wval) == 135, len(wval)
    assert sorted(nm for nm, v in wval.items() if v) == \
        ["tf1_47", "tf1_52", "tf2_47", "tf2_52"], "witness support drift"
    return wval, val


def spec_series(orbs84, wval, wpt, p, cap=SCAP):
    """witness-specialize each depth-84 orbit series: banked vars ->
    numeric mod p, pins -> ring_modp at the witness radical point,
    unbanked vars at level <= LVMAX -> SYMBOLIC {(vid,): 1}; deeper
    levels dropped (slot > 60 cannot reach a kept key).  Returns
    orb -> {level: {varkey: int}} and the symbolic vid census."""
    out, sym = {}, {}
    for on, orb in orbs84.items():
        s = {}
        for lv, vex in orb["series"].items():
            if lv - 12 >= cap:
                continue
            (vk, r), = vex.items()             # vC or vvar: single entry
            if vk == ():                       # pin / lead: ring constant
                c = FC.ring_modp(r, wpt, p)
                if c:
                    s[lv] = {(): c}
            else:
                (vid,) = vk
                nm = R1.VARS[vid]["name"]
                assert r == R1.RONE
                if nm in wval:
                    if wval[nm]:
                        s[lv] = {(): wval[nm]}
                else:
                    s[lv] = {(vid,): 1}
                    sym[vid] = nm
        out[on] = dict(series=s, size=orb["size"], name=on)
    return out, sym


# ---------------------------------------- mod-p folds (two paths)
def pvadd(x, y, p):
    out = dict(x)
    for k, c in y.items():
        c2 = (out.get(k, 0) + c) % p
        if c2:
            out[k] = c2
        elif k in out:
            del out[k]
    return out


def zpow(z, e, p):
    return pow(z, e % 42, p)


def pfold_linear(orb, p, z, cap=SCAP):
    """sequential linear-factor fold, mod-p port of ME.fs_orbit_fold:
    factor (k,j): (1,0) -> z^{12k}, (0,s) -> -z^{(k+7j)s} * Ytilde_s."""
    yt = {lv - 12: v for lv, v in orb["series"].items()}
    jp = {(0, 0): {(): 1}}
    n7 = R1.C7SUB[orb["size"]]
    for k in range(7):
        for j in range(n7):
            fac = {(1, 0): {(): zpow(z, 12 * k, p)}}
            for s, v in yt.items():
                c = (p - zpow(z, (k + 7 * j) * s, p)) % p
                fac[(0, s)] = {vk: cv * c % p for vk, cv in v.items()}
            jp = FC.pjmul(jp, fac, cap, p)
    return {k: v for k, v in jp.items() if v}


def pfold_newton(orb, p, z, cap=SCAP):
    """suborbit-Newton fold, mod-p port of R1.fs_block: e_syms of the
    C_7-suborbit via selector-aggregated power sums, then 7 images."""
    n7 = R1.C7SUB[orb["size"]]
    yt = {lv - 12: v for lv, v in orb["series"].items()}

    def smulp(a, b):
        out = {}
        for sa, va in a.items():
            for sb, vb in b.items():
                s = sa + sb
                if s >= cap:
                    continue
                cur = out.setdefault(s, {})
                for kx, cx in va.items():
                    for ky, cy in vb.items():
                        kk = tuple(sorted(kx + ky))
                        cur[kk] = (cur.get(kk, 0) + cx * cy) % p
        return {s: {k: c for k, c in v.items() if c}
                for s, v in out.items()}

    yp = {0: {0: {(): 1}}, 1: yt}
    for r in range(2, n7 + 1):
        yp[r] = smulp(yp[r - 1], yt)
    q = {}
    for r in range(1, n7 + 1):
        q[r] = {s: {k: c * n7 % p for k, c in v.items()}
                for s, v in yp[r].items()
                if (12 * r + s) % 6 == 0 and
                ((s % 2 == 0) or orb["size"] == 42)}
    e = [{0: {(): 1}}]
    for j in range(1, n7 + 1):
        acc = {}
        for r in range(1, j + 1):
            t = smulp(e[j - r], q[r])
            sgn = 1 if (r - 1) % 2 == 0 else p - 1
            for s, v in t.items():
                acc.setdefault(s, {})
                for k, c in v.items():
                    acc[s][k] = (acc[s].get(k, 0) + sgn * c) % p
        ji = pow(j, p - 2, p)
        e.append({s: {k: c * ji % p for k, c in v.items() if c * ji % p}
                  for s, v in acc.items()})
    rep = {}
    for j in range(n7 + 1):
        sgn = 1 if j % 2 == 0 else p - 1
        for s, v in e[j].items():
            vv = {k: c * sgn % p for k, c in v.items()}
            if vv:
                rep[(n7 - j, s)] = vv
    blk = {(0, 0): {(): 1}}
    for k in range(7):
        img = {(n, s): {kk: c * zpow(z, k * (12 * n + s), p) % p
                        for kk, c in v.items()}
               for (n, s), v in rep.items()}
        blk = FC.pjmul(blk, img, cap, p)
    return {k: v for k, v in blk.items() if v}


def pjadd(a, b, p, sub=False):
    out = {k: dict(v) for k, v in a.items()}
    m = (p - 1) if sub else 1
    for k, v in b.items():
        cur = out.setdefault(k, {})
        for kk, c in v.items():
            c2 = (cur.get(kk, 0) + m * c) % p
            if c2:
                cur[kk] = c2
            elif kk in cur:
                del cur[kk]
    return {k: v for k, v in out.items() if v}


# ------------------------------------------------------- pattern c_n
def pattern_cn(p, r3):
    """c_n = coeff of T^((n-2)/7) in ((T-1)^2 (T-B))^8, B = 3/2 (the
    eta^2-shifted p21^8: unique shift with 12n + 60 == 0 (mod 42));
    returns {n: c mod p} for n = 2, 9, .., 170."""
    p21, pm = R1.k3poly_pow_pattern()
    p8 = [R1.K1]
    for _ in range(8):
        p8 = pm(p8, p21)
    assert len(p8) == 25                     # T-degree 24
    out = {}
    for m, c in enumerate(p8):
        cm = (FC.frmod(c[0], p) + FC.frmod(c[1], p) * r3) % p
        if cm:
            out[7 * m + 2] = cm
    return out


# ------------------------------------------------------------ the gate
def build_gate(p):
    t0 = time.time()
    wval, val = banked_values(p)
    log("p=%d witness loaded (135 banked vars; nonzero: tf1/2_47, "
        "tf1/2_52)" % p)
    R1.reset_vars()
    orbs84 = R1.build_generators(84)
    vm84 = [dict(m) for m in R1.VARS]
    spec, sym = spec_series(orbs84, wval, val, p)
    lvs = sorted({R1.VARS[v]["level"] for v in sym})
    log("registry depth-84: %d vars; symbolic unbanked (level<=%d): %d "
        "(levels %d..%d)" % (len(vm84), LVMAX, len(sym), lvs[0], lvs[-1]))
    for on in R1.FORB + R1.GORB:             # measured witness support
        num = sorted(lv - 12 for lv, v in spec[on]["series"].items()
                     if () in v)
        log("  %s numeric slots %s + %d symbolic" %
            (on, num, sum(1 for v in spec[on]["series"].values()
                          if () not in v)))
    z = val["z"]
    folds = {}
    for on in R1.FORB + R1.GORB:             # two-path fold + assert
        t1 = time.time()
        fl = pfold_linear(spec[on], p, z)
        fn = pfold_newton(spec[on], p, z)
        assert fl == fn, "fold path mismatch %s" % on
        folds[on] = fl
        log("  fold %s: %d keys %d terms, linear==newton (%.1fs)"
            % (on, len(fl), sum(len(v) for v in fl.values()),
               time.time() - t1))
    jf = {(0, 0): {(): 1}}
    for on in R1.FORB:
        jf = FC.pjmul(jf, folds[on], SCAP, p)
    jg = {(0, 0): {(): 1}}
    for on in R1.GORB:
        jg = FC.pjmul(jg, folds[on], SCAP, p)
    log("jets: f %d keys, g %d keys (%.1fs)"
        % (len(jf), len(jg), time.time() - t0))

    # ---- anchor A1: cap-25 regression vs banked sec-14 jets at witness
    st = ME.load("fsjets.pkl")
    xv54 = {}
    names54, vm54 = ME.core_name_map()
    for vid, m in enumerate(vm54):
        xv54[vid] = wval.get(m["name"], 0)
    for tag, mine, bank in (("f", jf, st["jf"]), ("g", jg, st["jg"])):
        ref = {}
        for k, v in bank.items():
            c = FC.eval_vex_modp(v, val, p, xv54)
            if c:
                ref[k] = c
        got = {}
        for (n, s), v in mine.items():
            if s < 25 and v:
                assert list(v) == [()], "symbolic content below slot 25"
                got[(n, s)] = v[()]
        assert got == ref, "A1 jet regression FAILED (%s)" % tag
    log("anchor A1 PASS: specialized fold == banked sec-14 %s at the "
        "witness on all slots <= 24 (f: %d keys, g: %d keys)"
        % ("fsjets", sum(1 for k in jf if k[1] < 25),
           sum(1 for k in jg if k[1] < 25)))

    # ---- anchor A1b: exact-ring fs_block reference through slot 40
    # (pins at 25, tf values at 35/40 are NOT covered by A1: the banked
    # jets stop at slot 24).  Pole orbits only (B-side numeric content
    # beyond slot 24 is empty; its tail cofactors are covered by the
    # two-path fold equality); FULL cofactor comparison incl. symbolic
    # tails, exact dict equality mod p.
    for on in ("P1", "P2", "Gp1", "Gp2", "G0p1", "G0p2"):
        t1 = time.time()
        ex = R1.fs_block(orbs84[on], 41)
        ref = {}
        for k, vex in ex.items():
            acc = {}
            for vk, r in vex.items():
                c = FC.ring_modp(r, val, p)
                kk = []
                for vid in vk:
                    nm = vm84[vid]["name"]
                    if nm in wval:
                        c = c * wval[nm] % p
                    else:
                        kk.append(vid)
                kk = tuple(sorted(kk))
                c2 = (acc.get(kk, 0) + c) % p
                if c2:
                    acc[kk] = c2
                elif kk in acc:
                    del acc[kk]
            if acc:
                ref[k] = acc
        mine = {k: v for k, v in folds[on].items() if k[1] < 41 and v}
        assert mine == ref, "A1b exact-ring regression FAILED (%s)" % on
        log("  anchor A1b %s: specialized fold == exact-ring fs_block "
            "at cap 41 evaluated at the witness (%d keys incl. tail "
            "cofactors, %.1fs)" % (on, len(ref), time.time() - t1))
    log("anchor A1b PASS: slot-25/35/40 pin+tf specialization validated "
        "against the banked exact engine on all 6 pole orbits")

    f2 = FC.pjmul(jf, jf, SCAP, p)
    f3 = FC.pjmul(f2, jf, SCAP, p)
    g2 = FC.pjmul(jg, jg, SCAP, p)
    WF = pjadd(g2, f3, p, sub=True)
    log("W_F: %d keys %d terms (%.1fs)"
        % (len(WF), sum(len(v) for v in WF.values()), time.time() - t0))

    # ---- anchor A2: E1 slot-0
    assert not [k for k, v in WF.items() if k[1] == 0 and v], "A2 E1"
    log("anchor A2 PASS: WF slot-0 identically zero (E1 at witness)")

    # ---- anchor A3: grading + slot-60 census
    bad = [(n, s) for (n, s) in WF if (12 * n + s) % 42 or s % 6]
    assert not bad, ("A3 grading", bad[:5])
    q60 = sorted(n for (n, s) in WF if s == 60)
    assert len(q60) == 54 and all(n % 7 == 2 for n in q60) \
        and q60[0] == 2 and q60[-1] == 373, ("A3 census", len(q60))
    log("anchor A3 PASS: grading 12n+s==0 (42) on %d keys; slot-60 "
        "support = 54 keys, n==2 (7), n=2..373 (15.4 count)" % len(WF))

    # ---- anchor A4: free closure (15.5) measured on band constants
    bandc = {s: [n for (n, ss), v in WF.items()
                 if ss == s and () in v] for s in range(6, 60, 6)}
    assert not any(bandc[s] for s in (30, 36, 42, 48, 54)), bandc
    assert not any(bandc[s] for s in (6, 12, 18, 24)), bandc  # 14.3
    log("anchor A4 PASS: band rows s=6..54 carry ZERO constant part at "
        "the witness -- zero-extended witness satisfies the whole band "
        "(15.5 free closure reproduced mechanically)")

    # ---- rows + anchor A5 (participation census, degree, linearity)
    rows = {n: dict(WF[(n, 60)]) for n in q60}
    occ = sorted({vid for v in rows.values() for vk in v for vid in vk})
    onames = sorted(sym[vid] for vid in occ)
    exp39 = expected_39()
    extra = [x for x in onames if x not in exp39]
    assert not extra, ("A5: tails beyond the 15.5(ii) budget", extra)
    missing = [x for x in exp39 if x not in onames]
    for on in folds:                         # per-orbit selector grading
        bad = [(n, s) for (n, s) in folds[on] if (12 * n + s) % 42]
        assert not bad, ("orbit fold grading", on, bad[:3])
    for nm in missing:                       # measured-absence validation
        (vid,) = [v for v, n in sym.items() if n == nm]
        on = next(o for o in spec if any(
            v == {(vid,): 1} for v in spec[o]["series"].values()))
        lv = next(l for l, v in spec[on]["series"].items()
                  if v == {(vid,): 1})
        # mechanical reason: per-orbit selector grading forces slots == 0
        # (mod 6) per key; a lone slot-(lv-12) tail is off-grid, and its
        # cheapest SAME-orbit companion (slot >= 25) overshoots cap 60 --
        # the 15.5(ii) pairing partner (a-pin) lives in ANOTHER orbit.
        assert (lv - 12) % 6 and (lv - 12) + 25 > 60, (nm, lv)
        assert not any(vid in vk for v in folds[on].values() for vk in v)
        import copy
        spec2 = copy.deepcopy(spec)
        rnd = 1 + (vid * 7919 + p // 3) % (p - 1)
        spec2[on]["series"][lv] = {(): rnd}
        f2p = dict(folds, **{on: pfold_linear(spec2[on], p, z)})
        jfp = {(0, 0): {(): 1}}
        for o in R1.FORB:
            jfp = FC.pjmul(jfp, f2p[o], SCAP, p)
        jgp = {(0, 0): {(): 1}}
        for o in R1.GORB:
            jgp = FC.pjmul(jgp, f2p[o], SCAP, p)
        WFp = pjadd(FC.pjmul(jgp, jgp, SCAP, p),
                    FC.pjmul(FC.pjmul(jfp, jfp, SCAP, p), jfp, SCAP, p),
                    p, sub=True)
        assert WFp == WF, "A5: %s does NOT cancel -- formulation error" \
            % nm
        log("  A5 deviation VERIFIED: %s (level %d, slot %d) is BARRED "
            "by the per-orbit selector grading (off-6-grid alone, "
            "same-orbit companion overshoots cap 60); perturbation "
            "value %d leaves every W_F key unchanged.  REFINES 15.5(ii):"
            " the a-pin partner sits in another orbit." % (nm, lv,
                                                           lv - 12, rnd))
    assert len(onames) + len(missing) == 39
    log("anchor A5 RESULT: measured participation = %d tails (15.5(ii) "
        "39 minus %d grading-barred slot-40 B-side tails: %s); system = "
        "%d unknowns incl. s1F" % (len(onames), len(missing), missing,
                                   len(onames) + 1))
    dmax = max(len(vk) for v in rows.values() for vk in v)
    assert dmax <= 2, dmax
    for v in rows.values():                  # slot>=42 tails only LINEAR
        for vk in v:
            for vid in vk:
                if R1.VARS[vid]["level"] >= 54 and len(vk) > 1:
                    raise AssertionError("slot>=42 tail nonlinear")
    log("anchor A5 PASS: participation contained in the 15.5(ii) 39 "
        "(every deviation grading-barred + perturbation-verified), "
        "degree <= 2, slot>=42 tails linear")

    # ---- anchor A6: cap-67 rerun -- r=11 (slot 66) band constants must
    # vanish at the zero-extended witness (15.5(a): 66 == 1 mod 5 has no
    # pin/tf representation), and the slot-60 rows must be UNCHANGED
    # (slot-truncation exactness of the cap-61 build).
    spec7, _ = spec_series(orbs84, wval, val, p, cap=67)
    WF7 = None
    jf7 = {(0, 0): {(): 1}}
    jg7 = {(0, 0): {(): 1}}
    f7 = {on: pfold_linear(spec7[on], p, z, cap=67)
          for on in R1.FORB + R1.GORB}
    for on in R1.FORB:
        jf7 = FC.pjmul(jf7, f7[on], 67, p)
    for on in R1.GORB:
        jg7 = FC.pjmul(jg7, f7[on], 67, p)
    WF7 = pjadd(FC.pjmul(jg7, jg7, 67, p),
                FC.pjmul(FC.pjmul(jf7, jf7, 67, p), jf7, 67, p),
                p, sub=True)
    r66 = sorted(n for (n, s) in WF7 if s == 66)
    assert r66 and all(n % 7 == 5 for n in r66), r66
    assert not [n for (n, s), v in WF7.items() if s == 66 and () in v], \
        "A6: slot-66 constant at witness"
    got60 = {n: v for (n, s), v in WF7.items() if s == 60}
    assert got60 == rows, "A6: cap-67 slot-60 rows drifted"
    log("anchor A6 PASS: cap-67 rerun -- %d slot-66 (r=11) rows carry "
        "ZERO constant part at the witness (15.5(a) measured); slot-60 "
        "rows identical to the cap-61 build (truncation exactness)"
        % len(r66))

    cn = pattern_cn(p, val["r3"])
    return dict(rows=rows, cn=cn, occ=occ, sym=sym, vm84=vm84, p=p,
                wval=wval, val=val,
                bandsym={k: v for k, v in WF.items()
                         if 30 <= k[1] <= 54 and v})


def expected_39():
    """the 15.5(ii) enumeration, spelled out (anchor reference)."""
    out = ["%s_72" % t for t in
           ("tf1", "tf2", "bf", "tg1", "tg2", "tg01", "tg02",
            "bg42", "bg21")]
    out += ["bf_52", "bg42_52", "bg21_52", "bf_47", "bg42_47",
            "bf_37", "bg42_37"]
    out += ["bf_%d" % l for l in range(38, 47)]
    out += ["bg42_%d" % l for l in range(38, 47)]
    out += ["bg21_%d" % l for l in range(38, 47, 2)]
    return sorted(out)


# ---------------------------------------------------- emission + run
def phase_emit():
    for p in FC.good_primes(2):
        g = load("gate_p%d.pkl" % p)
        rows, cn, occ, sym = g["rows"], g["cn"], g["occ"], g["sym"]
        vnames = {vid: "q%d" % i for i, vid in enumerate(occ)}
        hdr = [vnames[v] for v in occ] + ["s1F"]
        eqs, zext = [], []
        for n in sorted(rows):
            v = dict(rows[n])
            zext.append(v.get((), 0))
            if n in cn:                       # - s1F * c_n
                v[("s1F",)] = (p - cn[n]) % p
            parts = []
            for vk in sorted(v, key=lambda k: (len(k), tuple(map(str, k)))):
                mono = []
                for vid in sorted(set(vk), key=str):
                    e = vk.count(vid)
                    nm = vnames[vid] if vid != "s1F" else "s1F"
                    mono.append(nm + ("^%d" % e if e > 1 else ""))
                parts.append("%d%s" % (v[vk], "".join("*" + m
                                                      for m in mono)))
            eqs.append("+".join(parts) if parts else "0")
        path = os.path.join(SYS, "%s_p%d.ms" % (BASE, p))
        with open(path, "w") as f:
            f.write(", ".join(hdr) + "\n%d\n" % p)
            f.write(",\n".join(eqs) + "\n")
        with open(os.path.join(SYS, "%s_p%d.rows.txt" % (BASE, p)),
                  "w") as f:
            f.write("# Q0 gate (sec 16): 54 witness-specialized slot-60 "
                    "quotient rows WF(n,60) - s1F*c_n at p=%d\n" % p)
            for i, n in enumerate(sorted(rows)):
                f.write("eq%d = (Q0-quot, n=%d, s=60) c_n=%d\n"
                        % (i, n, cn.get(n, 0)))
            for vid in occ:
                f.write("%s = %s (level %d)\n"
                        % (vnames[vid], sym[vid],
                           g["vm84"][vid]["level"]))
            f.write("s1F = fresh tie scale (H_F^3 = s1F S_F^4)\n")
        nz = sum(1 for c in zext if c)
        log("emitted %s (54 eqs, %d vars, %.1f kB); zero-extension "
            "constants: %d/54 NONZERO" % (path, len(hdr),
                                          os.path.getsize(path) / 1e3, nz))
        txt = open(path).read()
        assert "(" not in txt and ")" not in txt
        save("zext_p%d.pkl" % p, zext)


def phase_run(timeout=600):
    import r1_decompose as RD
    logf = os.path.join(RUNS, BASE + "_runs.log")
    for p in FC.good_primes(2):
        fn = "%s_p%d.ms" % (BASE, p)
        out = os.path.join(RUNS, fn + ".out")
        verdict, wall, rss = RD.run_msolve_rss(
            os.path.join(SYS, fn), out, timeout, threads=4)
        line = "%s: %s wall %.1fs rss %.1f MB" % (fn, verdict, wall,
                                                  rss / 1024.0)
        log(line)
        with open(logf, "a") as f:
            f.write(line + "\n")


if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "all"
    if ph == "gate":
        ps = [int(sys.argv[2])] if len(sys.argv) > 2 else FC.good_primes(2)
        for p in ps:
            g = build_gate(p)
            save("gate_p%d.pkl" % p, g)
            log("gate state banked: gate_p%d.pkl" % p)
    elif ph == "emit":
        phase_emit()
    elif ph == "run":
        phase_run()
    elif ph == "all":
        for p in FC.good_primes(2):
            g = build_gate(p)
            save("gate_p%d.pkl" % p, g)
        phase_emit()
        phase_run()
