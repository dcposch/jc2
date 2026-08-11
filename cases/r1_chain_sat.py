"""r1_chain_sat.py -- SATURATED terminal gates for the sheet-6 two-pole
chain branches (2,3)->(6,17) and (2,5)->(6,23) (SHEET6-R1.md sec 20;
standing rules AUDIT + sec 17/18 + LADDER-REVIEW mandates 1-4 baked in
FROM BIRTH).  ADDITIVE new file; no prior emission or engine touched.

Gate = base chain core (sec 9/11, guard-certified) VERBATIM
       + uW_i*W_i - 1 (W_i template-forced nonzero: pole pattern
         p_h1@P = -(3/4) s0 lam_i^3 w_i^4 (eta^2-(4/3)w_i^2) is a
         NONZERO deg-2 pattern -- R6 post-review (D) d_h1@P = 1/7;
         axis poles excluded St 7.2)  [closes the 18.3 exposure]
       + cL*tcL - 1 (level-1 G_m lead: p_h1@Gm = (-)P^l1 deg EXACT
         forced tower data; explicitness rule -- redundant given the
         s1-tie cL^2 = S_M^l1 s1 with s1 saturated from birth).
s1 (t1*s1-1) and, for (2,3), qL (t2*qL-1) are saturated IN THE BASE.

TIE-ROW DERIVATION (sec 20.0; Q2E5 lesson -- St 3.9(ii) transports
need the 3.9(i) count equality, per member per edge): at the chain
pole edges (m_P = 0) the count scan mult(p@Gm,c_i) vs deg p@P gives
f: 2==2 (COUNT-EXACT -> E6-analogue unit pin lam_i = 9 S_M c_i^4
(a1-a2)^2, m_i^2 = s0 lam_i^3 -- ring constants already inside the
W_G fold), g: 3>2, h1: l1>2, h2: 2mu2-1 > 2k1=4, h3: 12(mu2-1)+6 >
24: NO count-exact dead member => the E5-quartic analogue set is
EMPTY BY DERIVATION; the in-window E6-tie analogue is the legality
row S_M^l1 s1 = cL^2, in the base from birth.  Phase `inventory`
verifies all of this mechanically (exact K3) and gates emission.

Phases: inventory | anchor | emit | run [budget] | all
AUDIT: expanded integer monomial sums, no parens; p-rows in [0,p).
"""
import os
import re
import sys
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import r1_experiment as R1
import r1_fullcore as FC

SYS = FC.OUT_DIR
RUNS = os.path.join(os.path.dirname(HERE), "runs")

CH = {
    "23": dict(base="r1_23chain_core", sat="r1_23sat", l1=3, mu2=3,
               s1st=18, ncore=115, nwrows=None),
    "25": dict(base="r1_25chain_core", sat="r1_25sat", l1=5, mu2=4,
               s1st=6, ncore=44, nwrows=None),
}
SAT_ROWS_0 = [("SAT W1 (uW chart row)", "uW1*W1-1"),
              ("SAT W2 (uW chart row)", "uW2*W2-1"),
              ("SAT cL (level-1 lead)", "cL*tcL-1")]


def log(msg):
    print("[chainsat %s] %s" % (time.strftime("%H:%M:%S"), msg),
          flush=True)


def read_ms(path):
    hdr, char, body = open(path).read().split("\n", 2)
    return ([h.strip() for h in hdr.split(",")], int(char),
            [e.strip() for e in body.strip().rstrip(",").split(",\n")])


def read_labels(path):
    out = []
    for line in open(path):
        m = re.match(r"eq\d+ = \('([^']+)', (\d+), (\d+)\)", line.strip())
        if m: out.append((m.group(1), int(m.group(2)), int(m.group(3))))
    return out


# ---------------------------------------------------- phase inventory
def phase_inventory():
    K3, mk, s3 = R1.K3, R1.mk, R1.SQ3
    a1, a2, b = R1.A1c, R1.A2c, R1.Bc
    SM, GM = mk(Fr(7 ** 12, 2 ** 6)), mk(Fr(-(7 ** 18), 2 ** 9))
    # shared vertex data: E6 transport consistency + moduli pin
    assert (GM * GM - SM * SM * SM).iszero(), "G_M^2 != S_M^3"
    assert ((a1 - a2) * (a1 - a2) - mk(12)).iszero()
    assert not (b - a1).iszero() and not (b - a2).iszero()
    # E6-analogue f-transport: lam_i = 9 S_M c_i^4 (a1-a2)^2 with
    # c_i^3 = a_i; m_i = 648 sqrt3 G_M a_i^2 solves m_i^2 = s0 lam_i^3
    # in K3 (s0 = 1): lam_i^3 = 729 * 1728 * S_M^3 * a_i^4.
    for ai in (a1, a2):
        lam3 = mk(729) * mk(1728) * SM * SM * SM * ai * ai * ai * ai
        mi = mk(648) * s3 * GM * ai * ai
        assert (mi * mi - lam3).iszero(), "E6 f-transport pin fails"
        assert not lam3.iszero(), "lam_i == 0?!"
    log("E6-analogue f-transport verified: lam_i = 9 S_M c_i^4 "
        "(a1-a2)^2 unit, m_i^2 = s0 lam_i^3 solvable in K3; pole "
        "lead -(3/4) s0 lam_i^3 w_i^4 vanishes IFF w_i = 0 => uW rows "
        "genome-justified")
    # count scan: NO count-exact dead member at the chain pole edges
    for c, d in CH.items():
        k1, l1, mu2 = 2, d["l1"], d["mu2"]
        members = [("f", 2, 2), ("g", 3, 2), ("h1", l1, 2),
                   ("h2", 2 * mu2 - 1, 2 * k1),
                   ("h3", 12 * (mu2 - 1) + 6, 12 * k1)]
        exact = [nm for nm, mG, dP in members if mG == dP]
        leaks = [(nm, mG, dP) for nm, mG, dP in members if mG != dP]
        assert exact == ["f"], (c, exact)
        assert all(mG > dP for _, mG, dP in leaks), (c, leaks)
        log("(%s) count scan: f COUNT-EXACT (E6, ring consts); leaks "
            "%s all St 3.11(i)-legal (m_P = 0) => E5-quartic analogue "
            "set EMPTY BY DERIVATION" % (c, leaks))
        # base-core saturation-from-birth + exposure census
        labs = [l for l, _, _ in read_labels(
            os.path.join(SYS, d["base"] + ".rows.txt"))]
        assert "C%s-s1-tie" % c in labs and "C%s-s1-inv" % c in labs
        if c == "23": assert "C23-qL-inv" in labs
        assert not any("uW" in l for l in labs), "uW already present?!"
        log("(%s) base rows: s1-tie + s1-inv%s present from birth; "
            "NO uW rows (the 18.3 exposure -- closed by this gate)"
            % (c, " + qL-inv" if c == "23" else ""))
    log("inventory PASS: gate = base VERBATIM + uW1 + uW2 + tcL; "
        "s2 disposition: (2,3) via qL != 0; (2,5) deferred (farm r=14 "
        "quotient carries H); F_s leads deferred to the chain ladder")


# ------------------------------------------------------ phase anchor
def _pmul(A, B):
    out = [R1.K0] * (len(A) + len(B) - 1)
    for i, x in enumerate(A):
        if x.iszero(): continue
        for j, y in enumerate(B):
            if y.iszero(): continue
            out[i + j] = out[i + j] + x * y
    return out


def _tpow(base, k):
    out = [R1.K1]
    for _ in range(k): out = _pmul(out, base)
    return out


def _root_mult(tp, a):
    """multiplicity of root t = a via repeated synthetic division."""
    m = 0
    while len(tp) > 1:
        q, carry = [R1.K0] * (len(tp) - 1), R1.K0
        for i in range(len(tp) - 1, 0, -1):
            carry = tp[i] + carry * a
            q[i - 1] = carry
        if not (tp[0] + carry * a).iszero(): return m
        m += 1
        tp = q
    return m


def ind_patterns(bval=4):
    """INDEPENDENT pattern build (plain K3 convolution; no engine
    pattern code): t-polys, then eta-map (t = eta^3)."""
    a1, a2 = R1.A1c, R1.A2c
    b = R1.mk(bval)
    P2 = [a1 * a2, -(a1 + a2), R1.K1]
    out = {}
    for nm, l in (("p3", 3), ("p5", 5)):
        tp = _tpow(P2, l)
        pe = [R1.K0] * (3 * (len(tp) - 1) + 1)
        for i, cc in enumerate(tp): pe[3 * i] = cc
        out[nm] = (tp, pe)
    tq = _pmul(_pmul(_tpow([-a1, R1.K1], 5), _tpow([-a2, R1.K1], 5)),
               [-b, R1.K1])
    pe = [R1.K0] * (3 * (len(tq) - 1) + 2)
    for i, cc in enumerate(tq): pe[3 * i + 1] = cc
    out["pq34"] = (tq, pe)
    return out


def acheck(chain, rows, ids, pi):
    """A-C-2 row-level pattern check against the independent
    reference pi = ind_patterns()-style dict (raises on mismatch)."""
    s1id, cLid, qLid = ids
    d = CH[chain]
    pl = pi["p3" if chain == "23" else "p5"][1]
    pq = pi["pq34"][1] if chain == "23" else None
    smL = R1.mk(Fr(7 ** 12, 2 ** 6) ** d["l1"])
    seen_quot = seen_top = seen_h2 = 0
    for (lab, n, s), v in rows:
        keys_cL = [k for k in v if cLid in k]
        keys_qL = [k for k in v if qLid in k] if qLid else []
        if lab.endswith("-WG-quot"):
            assert s == d["s1st"] and n % 3 == 0 and n <= len(pl) - 1
            cc = v.get((cLid,))
            assert cc is not None and keys_cL == [(cLid,)], (lab, n)
            k3 = R1.rk3(cc)
            assert k3 is not None and k3[0] == R1.KONE
            assert (k3[1] + pl[n]).iszero(), ("cL-coeff != -P^l1", n)
            seen_quot += 1
            if n == len(pl) - 1: seen_top += 1
        elif lab.endswith("-WG-quot-deg") or lab.endswith("-WG-band"):
            assert not keys_cL and not keys_qL, (lab, n)
        elif lab.endswith("-h2-quot"):
            qq = v.get((qLid,))
            assert qq is not None and keys_qL == [(qLid,)], (lab, n)
            k3 = R1.rk3(qq)
            assert k3 is not None and k3[0] == R1.KONE
            assert (k3[1] + pq[n]).iszero(), ("qL-coeff != -pq34", n)
            seen_h2 += 1
        elif lab.endswith("-h2-quot-deg"):
            assert not keys_qL, (lab, n)
        elif lab.endswith("-s1-tie"):
            assert set(v) == {(cLid, cLid), (s1id,)}
            kc = R1.rk3(v[(cLid, cLid)])
            ks = R1.rk3(v[(s1id,)])
            assert kc[0] == R1.KONE and (kc[1] - R1.K1).iszero()
            assert ks[0] == R1.KONE and (ks[1] + smL).iszero(), \
                "s1-tie: -S_M^l1 mismatch vs independent recompute"
        # lattice/grading (every WG/h2 row; the s1/qL-inv constant
        # rows sit at slot 0 by construction)
        if "-WG-" in lab or "-h2-" in lab or lab.endswith("-s1-tie"):
            assert s % 2 == 0 and s != 0, (lab, n, s)
    assert seen_top == 1, "monic top row not seen exactly once"
    assert seen_quot >= 1 and (chain == "25" or seen_h2 >= 1)
    return seen_quot, seen_h2


def phase_anchor():
    pi = ind_patterns()
    # A-C-1: value vs engine build + alignment + positivity
    pats = FC.chain_patterns()
    for nm, dg, mults in (("p3", 18, 3), ("p5", 30, 5), ("pq34", 34, 5)):
        tp, pe = pi[nm]
        assert len(pe) == dg + 1 and (pe[dg] - R1.K1).iszero()
        assert len(pats[nm]) == len(pe) and all(
            (x - y).iszero() for x, y in zip(pats[nm], pe)), nm
        for a in (R1.A1c, R1.A2c):
            assert _root_mult(tp, a) == mults, (nm, "root mult")
        if nm == "pq34":
            assert _root_mult(tp, R1.Bc) == 1, "pq34 b-root mult"
    log("A-C-1 PASS: independent convolution == engine patterns "
        "(p3/p5/pq34, every coefficient); deg/monic/lattice OK; root "
        "mults EXACTLY (3,3), (5,5), (5,5,1@b=4) by synthetic division")
    st = FC.load("blocks.pkl")
    WG = FC.load("xWG.pkl")
    cf = FC.load("chainF.pkl")
    nv = st["nvars"]
    ids = (nv + FC.S1ID_OFF, nv + FC.CLID_OFF, nv + FC.QLID_OFF)
    allrows = {}
    for chain in ("23", "25"):
        l = CH[chain]["l1"]
        Fl, sml = cf[l]
        rows, fresh = FC.chain_rows(chain, WG, Fl, sml, pats)
        allrows[chain] = (rows, fresh)
        nq, nh2 = acheck(chain, rows,
                         ids if chain == "23" else (ids[0], ids[1], None),
                         pi)
        log("A-C-2 PASS (%s): %d quot rows pattern-true (cL part == "
            "-P^l1[n] coeff-for-coeff), %d h2-quot rows (qL part == "
            "-pq34[n]); band/deg rows lead-free; s1-tie == "
            "{cL^2, -S_M^l1 s1}" % (chain, nq, nh2))
    # perturbation suite (reference side): each must be CAUGHT
    caught = []
    for tag, mut in (
            ("wrong-b 4->-4", lambda: ind_patterns(bval=-4)),
            ("index shift n->n+3", "shift"),
            ("sign flip", "flip"),
            ("single-coeff corruption", "corrupt")):
        bad = mut() if callable(mut) else ind_patterns()
        if mut == "shift":
            for nm in ("p3", "p5", "pq34"):
                tp, pe = bad[nm]
                bad[nm] = (tp, [R1.K0] * 3 + pe[:-3])
        elif mut == "flip":
            for nm in ("p3", "p5", "pq34"):
                tp, pe = bad[nm]
                bad[nm] = (tp, [-c for c in pe])
        elif mut == "corrupt":
            tp, pe = bad["p3"]
            pe = list(pe); pe[6] = pe[6] + R1.K1
            bad["p3"] = (tp, pe)
            tp, pe = bad["p5"]
            pe = list(pe); pe[15] = pe[15] + R1.K1
            bad["p5"] = (tp, pe)
        ok = True
        for chain in ("23", "25"):
            try:
                acheck(chain, allrows[chain][0],
                       ids if chain == "23" else (ids[0], ids[1], None),
                       bad)
            except AssertionError:
                ok = False
        assert not ok, "perturbation NOT caught: " + tag
        caught.append(tag)
    # build-side perturbations: corrupt a row copy -> caught
    for chain in ("25",):
        rows = [(m, dict(v)) for m, v in allrows[chain][0]]
        qi = next(i for i, (m, _) in enumerate(rows)
                  if m[0].endswith("-WG-quot"))
        v = dict(rows[qi][1])
        v[(ids[1],)] = R1.rscal(v[(ids[1],)], R1.mk(2))
        rows[qi] = (rows[qi][0], v)
        try:
            acheck(chain, rows, (ids[0], ids[1], None), pi)
            raise RuntimeError("build perturbation (value) NOT caught")
        except AssertionError:
            caught.append("build: cL-coeff corruption")
        rows = [(m, v) for m, v in allrows[chain][0]]
        m, v = rows[qi]
        rows[qi] = ((m[0], m[1] + 3, m[2]), v)
        try:
            acheck(chain, rows, (ids[0], ids[1], None), pi)
            raise RuntimeError("build perturbation (slot) NOT caught")
        except AssertionError:
            caught.append("build: row n-shift")
    log("perturbation suite: %d/%d CAUGHT (%s)"
        % (len(caught), 6, "; ".join(caught)))
    # emission<->state closure: guards A-D on the BANKED core files
    for chain in ("23", "25"):
        rows, fresh = allrows[chain]
        allv = sorted({vid for _, v in rows for vk in v for vid in vk})
        names = {vid: "x%d" % i for i, vid in enumerate(allv)}
        names.update(fresh)
        FC.guards(os.path.join(SYS, CH[chain]["base"] + ".ms"),
                  rows, names, allv)
        log("banked %s.ms re-certified against state-rebuilt rows "
            "(guards A-D)" % CH[chain]["base"])
    log("anchor PASS (all gates green)")


# -------------------------------------------------------- phase emit
def emit_gate(chain):
    d = CH[chain]
    base, sat = d["base"], d["sat"]
    hdr, char, eqs = read_ms(os.path.join(SYS, base + ".ms"))
    assert char == 0 and len(eqs) == d["ncore"], (chain, len(eqs))
    labs = read_labels(os.path.join(SYS, base + ".rows.txt"))
    p0 = os.path.join(SYS, sat + ".ms")
    with open(p0, "w") as f:
        f.write(", ".join(hdr + ["uW1", "uW2", "tcL"]) + "\n0\n")
        f.write(",\n".join(eqs + [e for _, e in SAT_ROWS_0]) + "\n")
    # verbatim regression: base rows byte-identical inside the gate
    _, c2, e2 = read_ms(p0)
    assert c2 == 0 and e2[:len(eqs)] == eqs and \
        e2[len(eqs):] == [e for _, e in SAT_ROWS_0]
    with open(os.path.join(SYS, sat + ".rows.txt"), "w") as f:
        f.write("# %s: SATURATED chain terminal gate (sec 20) = %s "
                "rows VERBATIM + uW1/uW2 (W_i template-forced nonzero,"
                " 18.3 exposure closed) + tcL (cL = level-1 G_m lead)."
                "\n# s1 (and qL for 23) saturated IN the base from "
                "birth; E5-analogue EMPTY BY DERIVATION (20.0).\n"
                % (sat, base))
        for i, lab in enumerate(labs):
            f.write("eq%d = %s\n" % (i, ("('%s', %d, %d)" % lab)))
        for i, (lab, _) in enumerate(SAT_ROWS_0):
            f.write("eq%d = %s\n" % (len(labs) + i, lab))
    log("emitted %s (%d eqs, %d vars, %.1f MB); base VERBATIM check "
        "PASS" % (p0, len(eqs) + 3, len(hdr) + 3,
                  os.path.getsize(p0) / 1e6))
    # wfree p-variants + controls
    wlabs = None
    for p in FC.good_primes(2):
        wf = os.path.join(SYS, "%s_wfree_p%d.ms" % (base, p))
        hw, cw, ew = read_ms(wf)
        assert cw == p
        wlabs = read_labels(wf.replace(".ms", ".rows.txt"))
        assert len(wlabs) == len(ew), (len(wlabs), len(ew))
        satp = ["uW1*W1+%d" % (p - 1), "uW2*W2+%d" % (p - 1),
                "cL*tcL+%d" % (p - 1)]
        variants = {
            "_p%d" % p: (ew + satp, hw + ["uW1", "uW2", "tcL"]),
            "_ctlA_relaxed_p%d" % p:
                ([e for (l, _, _), e in zip(wlabs, ew)
                  if not l.endswith("-s1-inv") and not
                  l.endswith("-qL-inv")], hw),
            "_ctlB_satonly_p%d" % p:
                ([e for (l, _, _), e in zip(wlabs, ew)
                  if l.startswith("radical") or "-WG-" in l] + satp,
                 hw + ["uW1", "uW2", "tcL"]),
        }
        for tag, (rows_p, hdr_p) in variants.items():
            path = os.path.join(SYS, sat + tag + ".ms")
            with open(path, "w") as f:
                f.write(", ".join(hdr_p) + "\n%d\n" % p)
                f.write(",\n".join(rows_p) + "\n")
            txt = open(path).read()
            assert "(" not in txt and ")" not in txt, path
            assert not any(int(t) >= p for t in
                           re.findall(r"\d+", txt.split("\n", 2)[2])
                           if t.isdigit() and len(t) > 5), "unreduced!"
            log("emitted %s (%d eqs, %d vars)"
                % (path, len(rows_p), len(hdr_p)))
        # guard C (origin census) on the main p-gate
        val = {nm: 0 for nm in hw + ["uW1", "uW2", "tcL"]}
        got = FC.parse_eval(ew + satp, val, p)
        nz = [i for i, t in enumerate(got) if t]
        want = 5 if chain == "23" else 4
        assert len(nz) == want, ("origin census", chain, p, nz)
        log("guard C p=%d: origin fails EXACTLY the %d constant rows "
            "(s1-inv%s + uW1/uW2/tcL) -- gate excludes the zero point"
            % (p, want, "/qL-inv" if chain == "23" else ""))
        # ctlA explicit-point certificate (origin on the relaxed locus)
        arows = variants["_ctlA_relaxed_p%d" % p][0]
        got = FC.parse_eval(arows, {nm: 0 for nm in hw}, p)
        assert not any(got), "ctlA origin cert FAILED"
        log("ctlA p=%d: NONEMPTY BY EXPLICIT POINT (origin zero-"
            "extension; independent parser, %d/%d rows vanish)"
            % (p, len(arows), len(arows)))


def emit_ext_retrofit():
    """(2,5) box01 decider, saturated re-emission (18.3 mandate):
    banked ext wfree rows VERBATIM + the 3 sat rows."""
    for p in FC.good_primes(2):
        src = os.path.join(SYS, "r1_25chain_ext_wfree_p%d.ms" % p)
        dst = os.path.join(SYS, "r1_25sat_ext_p%d.ms" % p)
        hw, cw, ew = read_ms(src)
        assert cw == p
        satp = ["uW1*W1+%d" % (p - 1), "uW2*W2+%d" % (p - 1),
                "cL*tcL+%d" % (p - 1)]
        with open(dst, "w") as f:
            f.write(", ".join(hw + ["uW1", "uW2", "tcL"]) + "\n%d\n" % p)
            f.write(",\n".join(ew + satp) + "\n")
        _, c2, e2 = read_ms(dst)
        assert c2 == p and e2[:len(ew)] == ew and e2[len(ew):] == satp
        log("emitted %s (%d eqs, %d vars, %.1f MB) -- fleet object, "
            "not run locally" % (dst, len(ew) + 3, len(hw) + 3,
                                 os.path.getsize(dst) / 1e6))


def phase_emit():
    for chain in ("25", "23"):
        emit_gate(chain)
    emit_ext_retrofit()


# --------------------------------------------------------- phase run
def phase_run(timeout=1200, which="p"):
    import r1_decompose as RD
    jobs = []
    if which in ("p", "all"):
        for chain in ("25", "23"):
            sat = CH[chain]["sat"]
            for p in FC.good_primes(2):
                jobs.append((chain, "%s_p%d.ms" % (sat, p)))
            for p in FC.good_primes(2):
                jobs.append((chain, "%s_ctlB_satonly_p%d.ms" % (sat, p)))
    if which in ("0", "all"):
        for chain in ("25", "23"):
            jobs.append((chain, CH[chain]["sat"] + ".ms"))
    if which.startswith("file:"):
        jobs.append(("?", which[5:]))
    for chain, fn in jobs:
        logf = os.path.join(RUNS, CH.get(chain, CH["25"])["sat"]
                            + "_runs.log") if chain in CH else \
            os.path.join(RUNS, "r1_chain_sat_runs.log")
        out = os.path.join(RUNS, fn + ".out")
        t0 = time.time()
        verdict, wall, rss = RD.run_msolve_rss(
            os.path.join(SYS, fn), out, timeout, threads=4)
        if verdict != "TIMEOUT" and (not os.path.exists(out) or
                                     os.path.getsize(out) == 0):
            verdict = "NO-OUTPUT (NOT a verdict; 19.2 hygiene)"
        line = "%s: %s wall %.1fs rss %.1f MB" % (fn, verdict, wall,
                                                  rss / 1024.0)
        log(line)
        with open(logf, "a") as f:
            f.write(line + "\n")


if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "all"
    if ph in ("inventory", "all"): phase_inventory()
    if ph in ("anchor", "all"): phase_anchor()
    if ph in ("emit", "all"): phase_emit()
    if ph in ("run", "all"):
        arg = sys.argv[2] if len(sys.argv) > 2 else "p"
        phase_run(which=arg)
