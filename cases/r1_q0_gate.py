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


# =====================================================================
# SATURATED mode (SHEET6-R1.md sec 18; SHEET6-R1-LADDER-REVIEW R2
# mandates 1-4).  ADDITIVE: nothing above this line changed.
# =====================================================================
SATBASE = "r1_q0_sat"


def e5e6_rows(p, val):
    """The relaxation-dropped tie rows, witness-specialized mod p.
    E5 (TEMPLATE 2c-E5, H_M RESTORED as a variable; review-verified
    formula, f12_witness.py):  per pole i,
      4*(a_i-b)*HM + 729*S_M^3*(a1-a2)^4*a_i^2*alpha_i*W_i^4 = 0
    (s0 = 1, S_M = 7^12/2^6, a_i = 3+-r3, b = 4, alpha_i = A_i).
    E6 in the embedding-free CUBE form (H_M^3/S_M^4 = H_F^3/S_F^4 = s1,
    s1F = H_F the quotient lead, S_F = 1):  (H_M/H_F)^3 = (S_M/S_F)^4:
      2^24*HM^3 - 7^48*s1F^3 = 0.
    Returns ([(label, eqstr)], HM pinned by E5: asserted nonzero and
    pole-consistent -- the review's front-2 computation reproduced)."""
    inv = lambda a: pow(a % p, p - 2, p)
    r3 = val["r3"]
    SM = 7 ** 12 * inv(2 ** 6) % p
    rows, hm = [], []
    for i, (ai, Ai, Wi) in enumerate(
            (((3 + r3) % p, val["A1"], val["W1"]),
             ((3 - r3) % p, val["A2"], val["W2"])), 1):
        cH = 4 * (ai - 4) % p
        d = (729 * pow(SM, 3, p) % p * pow(2 * r3 % p, 4, p) % p
             * pow(ai, 2, p) % p * Ai % p * pow(Wi, 4, p) % p)
        rows.append(("E5-quartic pole %d (HM pinned)" % i,
                     "%d*HM+%d" % (cH, d)))
        hm.append((p - d) * inv(cH) % p)
    assert hm[0] == hm[1] != 0, ("E5-implied H_M inconsistent/zero", hm)
    rows.append(("E6-tie cube form 2^24 HM^3 = 7^48 s1F^3",
                 "16777216*HM^3+%d*s1F^3" % (p - pow(7, 48, p))))
    return rows, hm[0]


def phase_satemit():
    """r1_q0_sat_p*.ms = the banked Q0 rows VERBATIM (regression: byte
    reuse of the guard-passed emission) + deferred E5/E6 tie rows
    (mandate 2) + Rabinowitsch saturation s1F*tSAT-1 (mandate 1).
    HM != 0 follows from E5's pin; W_i are nonzero witness constants;
    the 36 tails are free template parameters (no saturation row)."""
    for p in FC.good_primes(2):
        val = ME.witness_point(p)
        path0 = os.path.join(SYS, "%s_p%d.ms" % (BASE, p))
        hdr, char, eqs = (lambda t: (t[0], t[1], t[2]))(
            open(path0).read().split("\n", 2))
        assert int(char) == p and len(hdr.split(", ")) == 37
        eqs = [e.strip() for e in eqs.strip().rstrip(",").split(",\n")]
        assert len(eqs) == 54, len(eqs)
        tie, hmv = e5e6_rows(p, val)
        sf = hmv * pow(2, 8, p) % p * pow(pow(7, 16, p), p - 2, p) % p
        labels = [(("Q0-quot verbatim eq%d" % i), e)
                  for i, e in enumerate(eqs)] + tie + \
                 [("SAT s1F (Rabinowitsch)", "s1F*tSAT+%d" % (p - 1))]
        path = os.path.join(SYS, "%s_p%d.ms" % (SATBASE, p))
        with open(path, "w") as f:
            f.write(hdr + ", HM, tSAT\n%d\n" % p)
            f.write(",\n".join(e for _, e in labels) + "\n")
        with open(os.path.join(SYS, "%s_p%d.rows.txt" % (SATBASE, p)),
                  "w") as f:
            f.write("# Q0 SATURATED (sec 18): 54 banked Q0 rows verbatim"
                    " + E5 quartic (HM restored) + E6 cube tie + "
                    "s1F*tSAT-1.\n# NAMING FIX (review nit 5): s1F is "
                    "the QUOTIENT LEAD H_F (linear); the cube-tie scale"
                    " is s1 = H_F^3/S_F^4.\n# E5-pinned HM = %d, "
                    "E6-implied s1F (om^0 embedding) = %d -- both "
                    "NONZERO; the banked Q0 GB contains s1F.\n"
                    % (hmv, sf))
            for i, (lab, _) in enumerate(labels):
                f.write("eq%d = %s\n" % (i, lab))
        txt = open(path).read()
        assert "(" not in txt and ")" not in txt
        log("emitted %s (58 eqs, 39 vars; E5-pinned HM=%d, implied "
            "s1F=%d nonzero)" % (path, hmv, sf))


def a7_check(p, cn, q60supp):
    """A7 PATTERN-POSITIVE anchor (sec 18 mandate 4; front-5 fix).
    (a) VALUE: every c_n == coeff of T^((n-2)/7) in ((T-1)^2(T-B))^8,
        B = 3/2, recomputed HERE by binomial expansion + Fraction
        convolution (independent of pattern_cn/k3poly_pow_pattern);
    (b) ALIGNMENT: support = {7m+2} = 2..170 with c_2 = B^8 and MONIC
        top c_170 = 1; min support == min of the MEASURED WF slot-60
        n-support (an index shift n->n+7 breaks this);
    (c) POSITIVITY (Prop 8.1 form): the T-poly q from the EMITTED c_n
        has a root of multiplicity EXACTLY 16 at T = A = 1 and EXACTLY
        8 at T = B (synthetic division mod p), deg q == 24; and the
        space of deg <= 24 polys with those multiplicities is
        1-DIMENSIONAL (Fraction rank of the 24x25 condition matrix ==
        24), so c_n is THE template quotient pattern up to scale and
        (b) pins the scale.  Raises AssertionError on any corruption."""
    from math import comb
    t1 = [Fr(comb(16, k)) * (-1) ** (16 - k) for k in range(17)]
    tB = [Fr(comb(8, k)) * Fr(-3, 2) ** (8 - k) for k in range(9)]
    ref = [sum(t1[i] * tB[m - i] for i in range(max(0, m - 8),
               min(16, m) + 1)) for m in range(25)]
    refp = {7 * m + 2: FC.frmod(c, p) for m, c in enumerate(ref)
            if FC.frmod(c, p)}
    assert cn == refp, "A7(a): c_n != independent binomial reference"
    assert min(cn) == 2 and max(cn) == 170 and cn[170] == 1, \
        "A7(b): support/monic broken"
    assert cn[2] == FC.frmod(Fr(3, 2) ** 8, p), "A7(b): c_2 != B^8"
    assert all((n - 2) % 7 == 0 for n in cn), "A7(b): residue"
    assert min(cn) == min(q60supp), \
        "A7(b): pattern min-index != measured WF slot-60 min-index"
    q = [0] * 25
    for n, c in cn.items():
        q[(n - 2) // 7] = c % p
    assert q[24] % p, "A7(c): deg q != 24"
    for root, mult in ((1, 16), (FC.frmod(Fr(3, 2), p), 8)):
        w = list(q)
        for _ in range(mult):          # synthetic division by (T-root)
            r, out = 0, [0] * (len(w) - 1)
            for i in range(len(w) - 1, -1, -1):
                if i:
                    out[i - 1] = (w[i] + r) % p
                r = (w[i] + r) * root % p
            assert r % p == 0, "A7(c): mult < %d at %d" % (mult, root)
            w = out
        r = 0
        for i in range(len(w) - 1, -1, -1):
            r = (w[i] + r) * root % p if i else (w[i] + r) % p
        assert r % p, "A7(c): mult > %d at %d" % (mult, root)
    rows, piv = [], 0                  # uniqueness rank over Q
    for root, mult in ((Fr(1), 16), (Fr(3, 2), 8)):
        for d in range(mult):          # d-th derivative at root = 0
            row = [Fr(0)] * 25
            for j in range(d, 25):
                f = Fr(1)
                for t in range(d):
                    f *= (j - t)
                row[j] = f * root ** (j - d)
            rows.append(row)
    for col in range(25):
        pr = next((i for i in range(piv, len(rows)) if rows[i][col]), None)
        if pr is None:
            continue
        rows[piv], rows[pr] = rows[pr], rows[piv]
        for i in range(len(rows)):
            if i != piv and rows[i][col]:
                f = rows[i][col] / rows[piv][col]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[piv])]
        piv += 1
    assert piv == 24, "A7(c): condition rank %d != 24 (corank != 1)" % piv


def phase_a7(pert=False):
    for p in FC.good_primes(2):
        g = load("gate_p%d.pkl" % p)
        supp = sorted(g["rows"])
        a7_check(p, dict(g["cn"]), supp)
        log("anchor A7 PASS p=%d: pattern value/alignment/positivity "
            "(independent binomial ref; mult EXACTLY (16,8); corank-1 "
            "uniqueness)" % p)
        if not pert:
            continue
        from math import comb
        tB = [Fr(comb(8, k)) * Fr(3, 2) ** (8 - k) for k in range(9)]
        t1 = [Fr(comb(16, k)) * (-1) ** (16 - k) for k in range(17)]
        wrongB = [sum(t1[i] * tB[m - i] for i in range(max(0, m - 8),
                      min(16, m) + 1)) for m in range(25)]
        perts = [
            ("wrong sign B=-3/2", {7 * m + 2: FC.frmod(c, p)
             for m, c in enumerate(wrongB) if FC.frmod(c, p)}),
            ("index shift n->n+7", {n + 7: c for n, c in g["cn"].items()}),
            ("global sign flip", {n: p - c for n, c in g["cn"].items()}),
            ("single-coeff corruption",
             {n: ((c + 1) % p if n == 9 else c)
              for n, c in g["cn"].items()}),
        ]
        for lab, bad in perts:
            try:
                a7_check(p, bad, supp)
                raise SystemExit("A7 BLIND to perturbation: " + lab)
            except AssertionError as e:
                log("  A7 pert '%s': CAUGHT (%s)" % (lab, e))


def phase_satrun(timeout=1200):
    import r1_decompose as RD
    logf = os.path.join(RUNS, SATBASE + "_runs.log")
    for p in FC.good_primes(2):
        fn = "%s_p%d.ms" % (SATBASE, p)
        out = os.path.join(RUNS, fn + ".out")
        verdict, wall, rss = RD.run_msolve_rss(
            os.path.join(SYS, fn), out, timeout, threads=4)
        line = "%s: %s wall %.1fs rss %.1f MB" % (fn, verdict, wall,
                                                  rss / 1024.0)
        log(line)
        with open(logf, "a") as f:
            f.write(line + "\n")


# =====================================================================
# FAMILY object (char 0 + both primes): the Q0 quotient tier over the
# WHOLE sec-13.4 witness family -- W1/W2 SYMBOLIC on relation E (every
# 4th-root branch and A-embedding at once: the Q1 sweep subsumed),
# free x = 0 section, exact-ring fold.  Sec-18 mandate 3a char-0 leg.
# =====================================================================
FAMBASE = "r1_q0_fam"
S1FID, HMID, TSID = 10 ** 8, 10 ** 8 + 1, 10 ** 8 + 2


def family_backmap():
    """symbolic sec-13.4 back-map at free-x = 0 over the exact ring
    (banked UU + sec-10 substitution chains).  Returns {registry NAME:
    ring elem}.  Asserts: support EXACTLY {tf1/2_42, tf1/2_47,
    tf1/2_52, tg1/2_42} (slots 30/35/40; the slot-30 values are
    E-multiples -- zero AT the banked witnesses, NOT identically), and
    mod-p equality with ME.witness_point at both banked primes."""
    import r1_decompose as RD
    from r1_reduce import IR3

    def poly_to_ring(poly, xv):
        acc = R1.RZERO
        for (rk, xk), c in poly.items():
            e3 = rk[IR3]
            kc = R1.mk(c) * R1.mk(3 ** (e3 // 2)) * \
                (R1.SQ3 if e3 % 2 else R1.K1)
            r = R1.rmono(za=rk[1], a1=rk[2], a2=rk[3], w1=rk[4],
                         h1=rk[5], w2=rk[6], h2=rk[7], B=rk[8], c=kc)
            for v, e in xk:
                for _ in range(e):
                    r = R1.rmul(r, xv[v])
            acc = R1.radd(acc, r)
        return acc

    uu = RD.load_state()["UU"]["subs"]
    with open("/tmp/r1red/reduced.pkl", "rb") as f:
        red = pickle.load(f)["subs"]
    xv = {v: R1.RZERO for v in range(119)}
    for v, u, s2, A in reversed(uu):
        xv[v] = poly_to_ring(s2, xv)
    for v, u, s2, A in reversed(red):
        xv[v] = poly_to_ring(s2, xv)
    names54, vm54 = ME.core_name_map()
    bmap = {vm54[vid]["name"]: xv[int(xn[1:])]
            for vid, xn in names54.items()}
    for ln in open(os.path.join(SYS, "r1_minimal_ext.rows.txt")):
        m = re.match(r"x\d+ = (\S+) \(", ln)
        if m and m.group(1) not in bmap:
            bmap[m.group(1)] = R1.RZERO      # sec-14 ext vars: 0
    nz = sorted(nm for nm, r in bmap.items() if r)
    assert nz == ["tf1_42", "tf1_47", "tf1_52", "tf2_42", "tf2_47",
                  "tf2_52", "tg1_42", "tg2_42"], nz
    for p in FC.good_primes(2):
        wval, val = banked_values(p)
        for nm, r in bmap.items():
            got = FC.ring_modp(r, val, p) if r else 0
            assert got == wval.get(nm, 0) % p, ("backmap drift", nm, p)
    log("family back-map banked: support %s; mod-p exact vs the "
        "banked witnesses at both primes" % nz)
    return bmap


def phase_fam():
    t0 = time.time()
    bmap = family_backmap()
    R1.reset_vars()
    orbs84 = R1.build_generators(84)
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
                if nm in bmap:
                    if bmap[nm]:
                        s[lv] = {(): bmap[nm]}
                else:
                    s[lv] = {(vid,): R1.RONE}
                    sym[vid] = nm
        spec[on] = dict(series=s, size=orb["size"], name=on)
    log("family spec: %d symbolic tails; ring entries at slots 30/35/40"
        % len(sym))
    folds = {}
    for on in R1.FORB + R1.GORB:
        t1 = time.time()
        folds[on] = R1.fs_block(spec[on], SCAP)
        log("  fam fold %s: %d keys %d terms (%.1fs)"
            % (on, len(folds[on]),
               sum(len(v) for v in folds[on].values()), time.time() - t1))
    jf, jg = R1.JONE, R1.JONE
    for on in R1.FORB:
        jf = R1.jmul(jf, folds[on], SCAP)
    for on in R1.GORB:
        jg = R1.jmul(jg, folds[on], SCAP)
    log("fam jets: f %d keys, g %d keys (%.1fs)"
        % (len(jf), len(jg), time.time() - t0))
    f3 = R1.jmul(R1.jmul(jf, jf, SCAP), jf, SCAP)
    g2 = R1.jmul(jg, jg, SCAP)
    WF = R1.jadd(g2, R1.jscal(f3, R1.mk(-1)))
    log("fam W_F: %d keys %d terms (%.1fs)"
        % (len(WF), sum(len(v) for v in WF.values()), time.time() - t0))
    assert not any(v for (n, s), v in WF.items() if s == 0), "fam E1"
    assert not [k for k in WF if (12 * k[0] + k[1]) % 42], "fam grading"
    rows = {n: v for (n, s), v in WF.items() if s == 60 and v}
    occ = sorted({vid for v in rows.values() for vk in v for vid in vk})
    for p in FC.good_primes(2):          # REGRESSION vs the banked gate
        g = load("gate_p%d.pkl" % p)
        wval, val = banked_values(p)
        assert occ == g["occ"], "fam occ != gate occ"
        for n in sorted(set(rows) | set(g["rows"])):
            acc = {}
            for vk, r in rows.get(n, {}).items():
                c = FC.ring_modp(r, val, p)
                if c:
                    acc[vk] = (acc.get(vk, 0) + c) % p
            acc = {k: c for k, c in acc.items() if c}
            assert acc == g["rows"][n], ("fam regression", p, n)
        log("fam REGRESSION PASS p=%d: exact-ring family rows reduce to "
            "the banked gate rows at the witness (54/54 exact)" % p)
    save("fam.pkl", dict(rows=rows, occ=occ, sym=sym))
    log("fam state banked: fam.pkl (54 rows, %d unknowns + s1F/HM)"
        % len(occ))


def phase_famemit():
    st = load("fam.pkl")
    rows, occ, sym = st["rows"], st["occ"], st["sym"]
    names = {vid: "q%d" % i for i, vid in enumerate(occ)}
    names.update({S1FID: "s1F", HMID: "HM", TSID: "tSAT"})
    p21, pm = R1.k3poly_pow_pattern()
    p8 = [R1.K1]
    for _ in range(8):
        p8 = pm(p8, p21)
    cn = {7 * m + 2: c for m, c in enumerate(p8) if not c.iszero()}
    SM3 = R1.mk(Fr(7 ** 12, 2 ** 6)) * R1.mk(Fr(7 ** 12, 2 ** 6)) \
        * R1.mk(Fr(7 ** 12, 2 ** 6))
    eqs = list(R1.RAD_EQS) + ["uW1*W1-1", "uW2*W2-1",
                              "9*A1*W1^4+5*r3*A1*W1^4+9*A2*W2^4"
                              "-5*r3*A2*W2^4"]
    labels = [("radical/chart", e) for e in eqs[:-1]] + \
             [("relation E (13.1 core residual on the family)", eqs[-1])]
    for n in sorted(rows):
        v = {vk: dict(r) for vk, r in rows[n].items()}
        if n in cn:
            v[(S1FID,)] = R1.radd(v.get((S1FID,), R1.RZERO),
                                  R1.rC(-cn[n]))
        w1m = min(min(k[3] for k in r) for r in v.values() if r)
        w2m = min(min(k[5] for k in r) for r in v.values() if r)
        if w1m < 0 or w2m < 0:              # clear W-Laurent (UU units)
            mul = R1.rmono(w1=max(0, -w1m), w2=max(0, -w2m))
            v = {vk: R1.rmul(r, mul) for vk, r in v.items()}
        eqs.append(R1.emit_expanded(v, names))
        labels.append(("Q0-fam-quot n=%d s=60%s" % (n,
                       " *W1^%d*W2^%d" % (-w1m, -w2m)
                       if w1m < 0 or w2m < 0 else ""), eqs[-1]))
    for i, (ai2, arg) in enumerate(((R1.A1c * R1.A1c, dict(a1=1, w1=4)),
                                    (R1.A2c * R1.A2c, dict(a2=1, w2=4))),
                                   1):
        ai = R1.A1c if i == 1 else R1.A2c
        v = {(HMID,): R1.rC(R1.mk(4) * (ai - R1.Bc)),
             (): R1.rmono(c=R1.mk(729 * 144) * SM3 * ai2, **arg)}
        eqs.append(R1.emit_expanded(v, names))
        labels.append(("E5-quartic pole %d (HM restored)" % i, eqs[-1]))
    eqs.append(R1.emit_expanded({(HMID,) * 3: R1.rC(R1.mk(2 ** 24)),
                                 (S1FID,) * 3: R1.rC(R1.mk(-(7 ** 48)))},
                                names))
    labels.append(("E6-tie cube form", eqs[-1]))
    eqs.append("s1F*tSAT-1")
    labels.append(("SAT s1F (Rabinowitsch)", eqs[-1]))
    hdr = ["r3", "z", "A1", "A2", "W1", "HW1", "W2", "HW2", "EB",
           "uW1", "uW2"] + [names[v] for v in occ] + \
          ["s1F", "HM", "tSAT"]
    path = os.path.join(SYS, FAMBASE + ".ms")
    with open(path, "w") as f:
        f.write(", ".join(hdr) + "\n0\n")
        f.write(",\n".join(eqs) + "\n")
    txt = open(path).read()
    assert "(" not in txt and ")" not in txt
    with open(os.path.join(SYS, FAMBASE + ".rows.txt"), "w") as f:
        f.write("# Q0 FAMILY saturated verdict object (sec 18): the "
                "depth-84 slot-60 quotient tier over the WHOLE sec-13.4"
                " witness family (free x = 0, W1/W2 symbolic on E -- "
                "all 4th-root branches + A-embeddings at once), exact "
                "ring, char 0 + reduced p-variants.\n# s1F = quotient "
                "LEAD H_F (naming fix); HM = G_m h1-lead restored; "
                "E5/E6 = the relaxation-dropped tie rows.\n")
        for i, (lab, _) in enumerate(labels):
            f.write("eq%d = %s\n" % (i, lab))
        for vid in occ:
            f.write("%s = %s (level %d)\n"
                    % (names[vid], sym[vid], R1.VARS[vid]["level"]
                       if vid < len(R1.VARS) else -1))
    log("emitted %s (%d eqs, %d vars, %.1f kB)"
        % (path, len(eqs), len(hdr), os.path.getsize(path) / 1e3))
    for p in FC.good_primes(2):
        pp = os.path.join(SYS, "%s_p%d.ms" % (FAMBASE, p))
        with open(pp, "w") as f:
            f.write(", ".join(hdr) + "\n%d\n" % p)
            f.write(",\n".join(FC.reduce_eq_str(e, p) for e in eqs) + "\n")
        log("emitted %s (reduced [0,p))" % pp)


def phase_famctl(timeout=1200):
    """controls on the char-0 family object (INPUTS banked to
    systems/r1 per the Q2E5 review -- the sec-18 minor flag):
    ctlA = RELAXED family (no E5/E6/sat rows, no HM/tSAT) -- must stay
           NONEMPTY (the zero-extension: the review-confirmed relaxed
           survival, family-wide);
    ctlB = saturation WITHOUT the tie rows (s1F*tSAT-1 only) -- [1]
           here proves s1F == 0 on the ENTIRE family variety in char 0
           (the 16.3 structural finding upgraded from 2 primes)."""
    import r1_decompose as RD
    hdr, char, body = open(os.path.join(SYS, FAMBASE + ".ms")).read() \
        .split("\n", 2)
    eqs = [e.strip() for e in body.strip().rstrip(",").split(",\n")]
    assert eqs[-1] == "s1F*tSAT-1" and len(eqs) == 68
    h = [x.strip() for x in hdr.split(",")]
    ctls = [("ctlA_relaxed", h[:-2], eqs[:-4]),
            ("ctlB_satonly", h, eqs[:-4] + [eqs[-1]])]
    logf = os.path.join(RUNS, FAMBASE + "_runs.log")
    for tag, hh, ee in ctls:
        path = os.path.join(SYS, "%s_%s.ms" % (FAMBASE, tag))
        with open(path, "w") as f:
            f.write(", ".join(hh) + "\n0\n" + ",\n".join(ee) + "\n")
        out = os.path.join(RUNS, "%s_%s.ms.out" % (FAMBASE, tag))
        verdict, wall, rss = RD.run_msolve_rss(path, out, timeout,
                                               threads=4)
        line = "%s_%s.ms (char 0): %s wall %.1fs rss %.1f MB" \
            % (FAMBASE, tag, verdict, wall, rss / 1024.0)
        log(line)
        with open(logf, "a") as f:
            f.write(line + "\n")


def phase_famrun(timeout=1200):
    import r1_decompose as RD
    logf = os.path.join(RUNS, FAMBASE + "_runs.log")
    files = ["%s_p%d.ms" % (FAMBASE, p) for p in FC.good_primes(2)] + \
            [FAMBASE + ".ms"]
    for fn in files:
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
    elif ph == "satemit":
        phase_satemit()
    elif ph == "satrun":
        phase_satrun()
    elif ph == "saturated":
        phase_satemit()
        phase_satrun()
    elif ph == "a7":
        phase_a7()
    elif ph == "a7pert":
        phase_a7(pert=True)
    elif ph == "fam":
        phase_fam()
    elif ph == "famemit":
        phase_famemit()
    elif ph == "famrun":
        phase_famrun()
    elif ph == "famctl":
        phase_famctl()
    elif ph == "famall":
        phase_fam()
        phase_famemit()
        phase_famrun()
    elif ph == "all":
        for p in FC.good_primes(2):
            g = build_gate(p)
            save("gate_p%d.pkl" % p, g)
        phase_emit()
        phase_run()
